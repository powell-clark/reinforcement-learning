"""
Deep Reinforcement Learning Algorithms

Deep RL algorithms using neural networks as function approximators.
Requires PyTorch.

Algorithms:
- DQN: Deep Q-Network with experience replay and target networks
- DoubleDQN: Reduces overestimation bias
"""

import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
from typing import Tuple, Optional
from collections import deque
import random


class ReplayBuffer:
    """
    Experience Replay Buffer for off-policy learning.

    Stores transitions (s, a, r, s', done) and samples random minibatches
    for training. This breaks temporal correlations in the data.

    Args:
        capacity: Maximum number of transitions to store
        seed: Random seed for reproducibility
    """

    def __init__(self, capacity: int = 10000, seed: Optional[int] = None):
        self.buffer = deque(maxlen=capacity)
        if seed is not None:
            random.seed(seed)

    def push(
        self,
        state: np.ndarray,
        action: int,
        reward: float,
        next_state: np.ndarray,
        done: bool,
    ):
        """Add transition to buffer."""
        self.buffer.append((state, action, reward, next_state, done))

    def sample(self, batch_size: int) -> Tuple:
        """Sample random minibatch."""
        batch = random.sample(self.buffer, batch_size)

        states = np.array([e[0] for e in batch])
        actions = np.array([e[1] for e in batch])
        rewards = np.array([e[2] for e in batch])
        next_states = np.array([e[3] for e in batch])
        dones = np.array([e[4] for e in batch])

        return states, actions, rewards, next_states, dones

    def __len__(self) -> int:
        return len(self.buffer)


class QNetwork(nn.Module):
    """
    Neural network for Q-function approximation.

    Simple fully-connected network with 2 hidden layers.

    Args:
        state_dim: Dimension of state space
        action_dim: Dimension of action space
        hidden_dim: Size of hidden layers
    """

    def __init__(self, state_dim: int, action_dim: int, hidden_dim: int = 128):
        super(QNetwork, self).__init__()

        self.network = nn.Sequential(
            nn.Linear(state_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, action_dim),
        )

    def forward(self, state: torch.Tensor) -> torch.Tensor:
        """Forward pass returns Q-values for all actions."""
        return self.network(state)


class DQN:
    """
    Deep Q-Network (DQN) Algorithm.

    Key components:
    - Neural network for Q-function approximation
    - Experience replay buffer
    - Target network (updated periodically)
    - ε-greedy exploration

    Reference:
        "Human-level control through deep reinforcement learning"
        Mnih et al., Nature 2015

    Args:
        state_dim: State space dimension
        action_dim: Action space dimension
        hidden_dim: Hidden layer size
        lr: Learning rate
        gamma: Discount factor
        epsilon: Initial exploration rate
        epsilon_decay: Epsilon decay rate
        epsilon_min: Minimum epsilon
        buffer_size: Replay buffer capacity
        batch_size: Minibatch size
        target_update_freq: Steps between target network updates
        device: 'cpu' or 'cuda'
        seed: Random seed

    Example:
        >>> agent = DQN(state_dim=4, action_dim=2)
        >>> action = agent.select_action(state)
        >>> agent.store_transition(state, action, reward, next_state, done)
        >>> if len(agent.buffer) > batch_size:
        >>>     loss = agent.train_step()
    """

    def __init__(
        self,
        state_dim: int,
        action_dim: int,
        hidden_dim: int = 128,
        lr: float = 0.001,
        gamma: float = 0.99,
        epsilon: float = 1.0,
        epsilon_decay: float = 0.995,
        epsilon_min: float = 0.01,
        buffer_size: int = 10000,
        batch_size: int = 64,
        target_update_freq: int = 100,
        device: str = "cpu",
        seed: Optional[int] = None,
    ):
        self.state_dim = state_dim
        self.action_dim = action_dim
        self.gamma = gamma
        self.epsilon = epsilon
        self.epsilon_decay = epsilon_decay
        self.epsilon_min = epsilon_min
        self.batch_size = batch_size
        self.target_update_freq = target_update_freq
        self.device = torch.device(device)

        # Set seeds
        if seed is not None:
            torch.manual_seed(seed)
            np.random.seed(seed)

        # Q-network and target network
        self.q_network = QNetwork(state_dim, action_dim, hidden_dim).to(self.device)
        self.target_network = QNetwork(state_dim, action_dim, hidden_dim).to(
            self.device
        )
        self.target_network.load_state_dict(self.q_network.state_dict())
        self.target_network.eval()  # Target network is not trained directly

        # Optimizer
        self.optimizer = optim.Adam(self.q_network.parameters(), lr=lr)

        # Replay buffer
        self.buffer = ReplayBuffer(capacity=buffer_size, seed=seed)

        # Training stats
        self.training_steps = 0
        self.episodes = 0

    def select_action(self, state: np.ndarray, training: bool = True) -> int:
        """
        Select action using ε-greedy policy.

        Args:
            state: Current state
            training: If True, use exploration. If False, greedy.

        Returns:
            Selected action
        """
        if training and np.random.rand() < self.epsilon:
            return np.random.randint(self.action_dim)
        else:
            with torch.no_grad():
                state_tensor = torch.FloatTensor(state).unsqueeze(0).to(self.device)
                q_values = self.q_network(state_tensor)
                return int(q_values.argmax(1).item())

    def store_transition(
        self,
        state: np.ndarray,
        action: int,
        reward: float,
        next_state: np.ndarray,
        done: bool,
    ):
        """Store transition in replay buffer."""
        self.buffer.push(state, action, reward, next_state, done)

    def train_step(self) -> float:
        """
        Perform one gradient descent step.

        Returns:
            Loss value
        """
        if len(self.buffer) < self.batch_size:
            return 0.0

        # Sample minibatch
        states, actions, rewards, next_states, dones = self.buffer.sample(
            self.batch_size
        )

        # Convert to tensors
        states = torch.FloatTensor(states).to(self.device)
        actions = torch.LongTensor(actions).unsqueeze(1).to(self.device)
        rewards = torch.FloatTensor(rewards).unsqueeze(1).to(self.device)
        next_states = torch.FloatTensor(next_states).to(self.device)
        dones = torch.FloatTensor(dones).unsqueeze(1).to(self.device)

        # Current Q-values
        current_q_values = self.q_network(states).gather(1, actions)

        # Target Q-values (using target network)
        with torch.no_grad():
            max_next_q_values = self.target_network(next_states).max(1, keepdim=True)[0]
            target_q_values = rewards + (1 - dones) * self.gamma * max_next_q_values

        # Compute loss (MSE between current and target Q-values)
        loss = nn.functional.mse_loss(current_q_values, target_q_values)

        # Optimize
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()

        # Update target network periodically
        self.training_steps += 1
        if self.training_steps % self.target_update_freq == 0:
            self.target_network.load_state_dict(self.q_network.state_dict())

        return loss.item()

    def decay_epsilon(self):
        """Decay epsilon after episode."""
        self.epsilon = max(self.epsilon_min, self.epsilon * self.epsilon_decay)
        self.episodes += 1

    def save(self, filepath: str):
        """Save model checkpoint."""
        torch.save(
            {
                "q_network": self.q_network.state_dict(),
                "target_network": self.target_network.state_dict(),
                "optimizer": self.optimizer.state_dict(),
                "epsilon": self.epsilon,
                "training_steps": self.training_steps,
            },
            filepath,
        )

    def load(self, filepath: str):
        """Load model checkpoint."""
        checkpoint = torch.load(filepath, map_location=self.device)
        self.q_network.load_state_dict(checkpoint["q_network"])
        self.target_network.load_state_dict(checkpoint["target_network"])
        self.optimizer.load_state_dict(checkpoint["optimizer"])
        self.epsilon = checkpoint["epsilon"]
        self.training_steps = checkpoint["training_steps"]


class DoubleDQN(DQN):
    """
    Double DQN - Reduces overestimation bias.

    Key difference from DQN: Uses online network to select action,
    but target network to evaluate that action.

    Standard DQN:
        target = r + γ max_a' Q_target(s', a')

    Double DQN:
        a* = argmax_a' Q_online(s', a')
        target = r + γ Q_target(s', a*)

    Reference:
        "Deep Reinforcement Learning with Double Q-learning"
        van Hasselt et al., AAAI 2016
    """

    def train_step(self) -> float:
        """Train step with double Q-learning."""
        if len(self.buffer) < self.batch_size:
            return 0.0

        states, actions, rewards, next_states, dones = self.buffer.sample(
            self.batch_size
        )

        states = torch.FloatTensor(states).to(self.device)
        actions = torch.LongTensor(actions).unsqueeze(1).to(self.device)
        rewards = torch.FloatTensor(rewards).unsqueeze(1).to(self.device)
        next_states = torch.FloatTensor(next_states).to(self.device)
        dones = torch.FloatTensor(dones).unsqueeze(1).to(self.device)

        # Current Q-values
        current_q_values = self.q_network(states).gather(1, actions)

        # Double DQN: select action with online network, evaluate with target network
        with torch.no_grad():
            # Select best action using online network
            next_actions = self.q_network(next_states).argmax(1, keepdim=True)
            # Evaluate that action using target network
            next_q_values = self.target_network(next_states).gather(1, next_actions)
            target_q_values = rewards + (1 - dones) * self.gamma * next_q_values

        # Compute loss
        loss = nn.functional.mse_loss(current_q_values, target_q_values)

        # Optimize
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()

        # Update target network
        self.training_steps += 1
        if self.training_steps % self.target_update_freq == 0:
            self.target_network.load_state_dict(self.q_network.state_dict())

        return loss.item()
