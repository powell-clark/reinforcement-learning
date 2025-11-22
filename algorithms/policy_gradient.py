"""
Policy Gradient Algorithms

Direct policy optimization methods that learn a parameterized policy π_θ(a|s).

Algorithms:
- REINFORCE: Monte Carlo policy gradient
- Actor-Critic: Combines policy gradient with value function learning
"""

import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
from typing import List, Tuple, Optional


class PolicyNetwork(nn.Module):
    """
    Policy network that outputs action probabilities.

    Args:
        state_dim: State space dimension
        action_dim: Action space dimension
        hidden_dim: Hidden layer size
    """

    def __init__(self, state_dim: int, action_dim: int, hidden_dim: int = 128):
        super(PolicyNetwork, self).__init__()

        self.network = nn.Sequential(
            nn.Linear(state_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, action_dim),
            nn.Softmax(dim=-1),  # Output probabilities
        )

    def forward(self, state: torch.Tensor) -> torch.Tensor:
        """Returns action probabilities."""
        return self.network(state)


class ValueNetwork(nn.Module):
    """
    Value network for critic in actor-critic.

    Args:
        state_dim: State space dimension
        hidden_dim: Hidden layer size
    """

    def __init__(self, state_dim: int, hidden_dim: int = 128):
        super(ValueNetwork, self).__init__()

        self.network = nn.Sequential(
            nn.Linear(state_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, 1),  # Output single value
        )

    def forward(self, state: torch.Tensor) -> torch.Tensor:
        """Returns state value."""
        return self.network(state)


class REINFORCE:
    """
    REINFORCE: Monte Carlo Policy Gradient Algorithm.

    The policy gradient theorem shows:
        ∇_θ J(θ) = E[∇_θ log π_θ(a|s) * G_t]

    REINFORCE uses full episode returns G_t to update the policy.

    Reference:
        "Simple Statistical Gradient-Following Algorithms for
         Connectionist Reinforcement Learning"
        Williams, Machine Learning 1992

    Args:
        state_dim: State space dimension
        action_dim: Action space dimension
        hidden_dim: Hidden layer size
        lr: Learning rate
        gamma: Discount factor
        device: 'cpu' or 'cuda'
        seed: Random seed

    Example:
        >>> agent = REINFORCE(state_dim=4, action_dim=2)
        >>> # Collect episode
        >>> for step in episode:
        >>>     action, log_prob = agent.select_action(state)
        >>>     agent.store_transition(log_prob, reward)
        >>> # Update after episode
        >>> loss = agent.update()
    """

    def __init__(
        self,
        state_dim: int,
        action_dim: int,
        hidden_dim: int = 128,
        lr: float = 0.001,
        gamma: float = 0.99,
        device: str = "cpu",
        seed: Optional[int] = None,
    ):
        self.gamma = gamma
        self.device = torch.device(device)

        # Set seeds
        if seed is not None:
            torch.manual_seed(seed)
            np.random.seed(seed)

        # Policy network
        self.policy = PolicyNetwork(state_dim, action_dim, hidden_dim).to(self.device)
        self.optimizer = optim.Adam(self.policy.parameters(), lr=lr)

        # Episode storage
        self.log_probs: List[torch.Tensor] = []
        self.rewards: List[float] = []

        # Statistics
        self.episodes = 0

    def select_action(self, state: np.ndarray) -> Tuple[int, torch.Tensor]:
        """
        Select action from policy.

        Args:
            state: Current state

        Returns:
            action: Sampled action
            log_prob: Log probability of the action
        """
        state_tensor = torch.FloatTensor(state).unsqueeze(0).to(self.device)

        # Get action probabilities
        probs = self.policy(state_tensor)

        # Sample action
        dist = torch.distributions.Categorical(probs)
        action = dist.sample()

        # Store log probability for policy gradient
        log_prob = dist.log_prob(action)

        return int(action.item()), log_prob

    def store_transition(self, log_prob: torch.Tensor, reward: float):
        """Store transition for episode."""
        self.log_probs.append(log_prob)
        self.rewards.append(reward)

    def compute_returns(self) -> List[float]:
        """
        Compute discounted returns for episode.

        Returns:
            List of returns G_t for each timestep
        """
        returns = []
        G = 0.0

        # Work backwards through episode
        for reward in reversed(self.rewards):
            G = reward + self.gamma * G
            returns.insert(0, G)

        return returns

    def update(self) -> float:
        """
        Update policy using REINFORCE algorithm.

        Returns:
            Policy loss
        """
        # Compute returns
        returns = self.compute_returns()

        # Normalize returns (reduces variance)
        returns = torch.FloatTensor(returns).to(self.device)
        returns = (returns - returns.mean()) / (returns.std() + 1e-8)

        # Compute policy loss: -E[log π(a|s) * G]
        policy_loss = []
        for log_prob, G in zip(self.log_probs, returns):
            policy_loss.append(-log_prob * G)

        policy_loss = torch.stack(policy_loss).sum()

        # Optimize
        self.optimizer.zero_grad()
        policy_loss.backward()
        self.optimizer.step()

        # Clear episode data
        self.log_probs = []
        self.rewards = []
        self.episodes += 1

        return policy_loss.item()

    def save(self, filepath: str):
        """Save model checkpoint."""
        torch.save(
            {
                "policy": self.policy.state_dict(),
                "optimizer": self.optimizer.state_dict(),
                "episodes": self.episodes,
            },
            filepath,
        )

    def load(self, filepath: str):
        """Load model checkpoint."""
        checkpoint = torch.load(filepath, map_location=self.device)
        self.policy.load_state_dict(checkpoint["policy"])
        self.optimizer.load_state_dict(checkpoint["optimizer"])
        self.episodes = checkpoint["episodes"]


class ActorCritic:
    """
    Actor-Critic Algorithm.

    Combines policy gradient (actor) with value function learning (critic).
    Uses TD error as baseline to reduce variance:

        Advantage: A(s,a) = r + γV(s') - V(s)
        Policy gradient: ∇_θ log π_θ(a|s) * A(s,a)

    Args:
        state_dim: State space dimension
        action_dim: Action space dimension
        hidden_dim: Hidden layer size
        actor_lr: Actor learning rate
        critic_lr: Critic learning rate
        gamma: Discount factor
        device: 'cpu' or 'cuda'
        seed: Random seed

    Example:
        >>> agent = ActorCritic(state_dim=4, action_dim=2)
        >>> action, log_prob, value = agent.select_action(state)
        >>> loss = agent.update(log_prob, value, reward, next_value, done)
    """

    def __init__(
        self,
        state_dim: int,
        action_dim: int,
        hidden_dim: int = 128,
        actor_lr: float = 0.001,
        critic_lr: float = 0.001,
        gamma: float = 0.99,
        device: str = "cpu",
        seed: Optional[int] = None,
    ):
        self.gamma = gamma
        self.device = torch.device(device)

        # Set seeds
        if seed is not None:
            torch.manual_seed(seed)
            np.random.seed(seed)

        # Actor (policy) and critic (value function)
        self.actor = PolicyNetwork(state_dim, action_dim, hidden_dim).to(self.device)
        self.critic = ValueNetwork(state_dim, hidden_dim).to(self.device)

        # Separate optimizers
        self.actor_optimizer = optim.Adam(self.actor.parameters(), lr=actor_lr)
        self.critic_optimizer = optim.Adam(self.critic.parameters(), lr=critic_lr)

        # Statistics
        self.training_steps = 0

    def select_action(
        self, state: np.ndarray
    ) -> Tuple[int, torch.Tensor, torch.Tensor]:
        """
        Select action and compute value.

        Returns:
            action: Sampled action
            log_prob: Log probability of action
            value: State value from critic
        """
        state_tensor = torch.FloatTensor(state).unsqueeze(0).to(self.device)

        # Actor: select action
        probs = self.actor(state_tensor)
        dist = torch.distributions.Categorical(probs)
        action = dist.sample()
        log_prob = dist.log_prob(action)

        # Critic: estimate value
        value = self.critic(state_tensor)

        return int(action.item()), log_prob, value

    def update(
        self,
        log_prob: torch.Tensor,
        value: torch.Tensor,
        reward: float,
        next_value: torch.Tensor,
        done: bool,
    ) -> Tuple[float, float]:
        """
        Update actor and critic.

        Args:
            log_prob: Log probability of action taken
            value: Value estimate for current state
            reward: Reward received
            next_value: Value estimate for next state
            done: Episode termination flag

        Returns:
            actor_loss: Policy loss
            critic_loss: Value function loss
        """
        # Compute TD target
        if done:
            td_target = reward
        else:
            td_target = reward + self.gamma * next_value.item()

        td_target = torch.FloatTensor([td_target]).to(self.device)

        # TD error = advantage
        advantage = (td_target - value).detach()  # Detach to not backprop through critic

        # Actor loss: -log π(a|s) * A(s,a)
        actor_loss = -log_prob * advantage

        # Critic loss: MSE between value and target
        critic_loss = nn.functional.mse_loss(value, td_target)

        # Update actor
        self.actor_optimizer.zero_grad()
        actor_loss.backward()
        self.actor_optimizer.step()

        # Update critic
        self.critic_optimizer.zero_grad()
        critic_loss.backward()
        self.critic_optimizer.step()

        self.training_steps += 1

        return actor_loss.item(), critic_loss.item()

    def save(self, filepath: str):
        """Save model checkpoint."""
        torch.save(
            {
                "actor": self.actor.state_dict(),
                "critic": self.critic.state_dict(),
                "actor_optimizer": self.actor_optimizer.state_dict(),
                "critic_optimizer": self.critic_optimizer.state_dict(),
                "training_steps": self.training_steps,
            },
            filepath,
        )

    def load(self, filepath: str):
        """Load model checkpoint."""
        checkpoint = torch.load(filepath, map_location=self.device)
        self.actor.load_state_dict(checkpoint["actor"])
        self.critic.load_state_dict(checkpoint["critic"])
        self.actor_optimizer.load_state_dict(checkpoint["actor_optimizer"])
        self.critic_optimizer.load_state_dict(checkpoint["critic_optimizer"])
        self.training_steps = checkpoint["training_steps"]
