"""
Example 3: Proximal Policy Optimization (PPO) on LunarLander

This script demonstrates PPO on the LunarLander-v2 environment.
LunarLander is a classic control problem where the agent must land a spacecraft
safely between flags while conserving fuel.

PPO is the most popular RL algorithm in 2025, used in everything from
robotics to ChatGPT training. It's stable, general-purpose, and works
for both continuous and discrete actions.

Usage:
    python 03_ppo_lunarlander.py

Expected output:
    - Training progress showing increasing episode rewards
    - Solved at 200+ average reward
    - Training curves visualization
"""

import sys
import os

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import gymnasium as gym
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.distributions import Categorical
import matplotlib.pyplot as plt

# Set random seeds for reproducibility
SEED = 42
np.random.seed(SEED)
torch.manual_seed(SEED)


class ActorCritic(nn.Module):
    """Combined Actor-Critic network for PPO."""

    def __init__(self, state_dim: int, action_dim: int, hidden_dim: int = 64):
        super().__init__()

        # Shared feature extractor
        self.shared = nn.Sequential(
            nn.Linear(state_dim, hidden_dim),
            nn.Tanh(),
        )

        # Actor head (policy)
        self.actor = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim),
            nn.Tanh(),
            nn.Linear(hidden_dim, action_dim),
        )

        # Critic head (value function)
        self.critic = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim),
            nn.Tanh(),
            nn.Linear(hidden_dim, 1),
        )

    def forward(self, x):
        features = self.shared(x)
        return self.actor(features), self.critic(features)

    def get_action_and_value(self, x):
        """Get action distribution and value estimate."""
        logits, value = self.forward(x)
        dist = Categorical(logits=logits)
        action = dist.sample()
        log_prob = dist.log_prob(action)
        entropy = dist.entropy()
        return action, log_prob, entropy, value

    def evaluate_actions(self, x, actions):
        """Evaluate actions for PPO update."""
        logits, value = self.forward(x)
        dist = Categorical(logits=logits)
        log_prob = dist.log_prob(actions)
        entropy = dist.entropy()
        return log_prob, entropy, value


class PPOAgent:
    """PPO Agent with clipped objective."""

    def __init__(
        self,
        state_dim: int,
        action_dim: int,
        hidden_dim: int = 64,
        lr: float = 3e-4,
        gamma: float = 0.99,
        gae_lambda: float = 0.95,
        clip_epsilon: float = 0.2,
        value_coef: float = 0.5,
        entropy_coef: float = 0.01,
        ppo_epochs: int = 4,
        mini_batch_size: int = 64,
    ):
        self.gamma = gamma
        self.gae_lambda = gae_lambda
        self.clip_epsilon = clip_epsilon
        self.value_coef = value_coef
        self.entropy_coef = entropy_coef
        self.ppo_epochs = ppo_epochs
        self.mini_batch_size = mini_batch_size

        # Actor-Critic network
        self.ac = ActorCritic(state_dim, action_dim, hidden_dim)
        self.optimizer = optim.Adam(self.ac.parameters(), lr=lr)

    def select_action(self, state):
        """Select action and compute log prob, value."""
        state = torch.FloatTensor(state).unsqueeze(0)
        with torch.no_grad():
            action, log_prob, entropy, value = self.ac.get_action_and_value(state)
        return action.item(), log_prob.item(), value.item()

    def compute_gae(self, rewards, values, dones):
        """Compute Generalized Advantage Estimation."""
        advantages = []
        gae = 0

        # Add terminal value
        values = values + [0]

        for t in reversed(range(len(rewards))):
            delta = rewards[t] + self.gamma * values[t + 1] * (1 - dones[t]) - values[t]
            gae = delta + self.gamma * self.gae_lambda * (1 - dones[t]) * gae
            advantages.insert(0, gae)

        return advantages

    def update(self, states, actions, old_log_probs, returns, advantages):
        """Update policy using PPO clipped objective."""
        states = torch.FloatTensor(np.array(states))
        actions = torch.LongTensor(np.array(actions))
        old_log_probs = torch.FloatTensor(np.array(old_log_probs))
        returns = torch.FloatTensor(np.array(returns))
        advantages = torch.FloatTensor(np.array(advantages))

        # Normalize advantages
        advantages = (advantages - advantages.mean()) / (advantages.std() + 1e-8)

        # PPO update for multiple epochs
        total_loss = 0
        total_policy_loss = 0
        total_value_loss = 0
        total_entropy = 0

        for _ in range(self.ppo_epochs):
            # Mini-batch updates
            indices = np.arange(len(states))
            np.random.shuffle(indices)

            for start in range(0, len(states), self.mini_batch_size):
                end = start + self.mini_batch_size
                batch_indices = indices[start:end]

                batch_states = states[batch_indices]
                batch_actions = actions[batch_indices]
                batch_old_log_probs = old_log_probs[batch_indices]
                batch_returns = returns[batch_indices]
                batch_advantages = advantages[batch_indices]

                # Evaluate actions with current policy
                log_probs, entropy, values = self.ac.evaluate_actions(
                    batch_states, batch_actions
                )
                values = values.squeeze()

                # Compute ratio for PPO
                ratio = torch.exp(log_probs - batch_old_log_probs)

                # Clipped surrogate objective
                surr1 = ratio * batch_advantages
                surr2 = (
                    torch.clamp(ratio, 1 - self.clip_epsilon, 1 + self.clip_epsilon)
                    * batch_advantages
                )
                policy_loss = -torch.min(surr1, surr2).mean()

                # Value loss
                value_loss = nn.MSELoss()(values, batch_returns)

                # Entropy bonus
                entropy_loss = -entropy.mean()

                # Total loss
                loss = (
                    policy_loss
                    + self.value_coef * value_loss
                    + self.entropy_coef * entropy_loss
                )

                # Optimize
                self.optimizer.zero_grad()
                loss.backward()
                torch.nn.utils.clip_grad_norm_(self.ac.parameters(), 0.5)
                self.optimizer.step()

                total_loss += loss.item()
                total_policy_loss += policy_loss.item()
                total_value_loss += value_loss.item()
                total_entropy += entropy.mean().item()

        n_updates = self.ppo_epochs * (len(states) // self.mini_batch_size)
        return {
            "loss": total_loss / n_updates,
            "policy_loss": total_policy_loss / n_updates,
            "value_loss": total_value_loss / n_updates,
            "entropy": total_entropy / n_updates,
        }


def train_ppo(
    env_name: str = "LunarLander-v2",
    n_iterations: int = 500,
    steps_per_iteration: int = 2048,
    lr: float = 3e-4,
    gamma: float = 0.99,
):
    """Train PPO agent on LunarLander."""
    print("=" * 70)
    print(f"Training PPO on {env_name}")
    print("=" * 70)
    print(f"Iterations: {n_iterations}")
    print(f"Steps per iteration: {steps_per_iteration}")
    print(f"Learning rate: {lr}, Gamma: {gamma}")
    print("=" * 70 + "\n")

    # Create environment
    env = gym.make(env_name)
    env.reset(seed=SEED)

    # Create agent
    state_dim = env.observation_space.shape[0]
    action_dim = env.action_space.n

    agent = PPOAgent(state_dim=state_dim, action_dim=action_dim, lr=lr, gamma=gamma)

    # Training loop
    iteration_rewards = []
    iteration_losses = []

    state, _ = env.reset()
    episode_reward = 0
    episode_rewards = []

    for iteration in range(n_iterations):
        # Collect trajectories
        states = []
        actions = []
        log_probs = []
        rewards = []
        values = []
        dones = []

        for _ in range(steps_per_iteration):
            action, log_prob, value = agent.select_action(state)

            next_state, reward, terminated, truncated, _ = env.step(action)
            done = terminated or truncated

            states.append(state)
            actions.append(action)
            log_probs.append(log_prob)
            rewards.append(reward)
            values.append(value)
            dones.append(done)

            episode_reward += reward
            state = next_state

            if done:
                episode_rewards.append(episode_reward)
                episode_reward = 0
                state, _ = env.reset()

        # Compute advantages and returns
        advantages = agent.compute_gae(rewards, values, dones)
        returns = [adv + val for adv, val in zip(advantages, values)]

        # Update policy
        metrics = agent.update(states, actions, log_probs, returns, advantages)

        # Record metrics
        avg_reward = np.mean(episode_rewards[-10:]) if episode_rewards else 0
        iteration_rewards.append(avg_reward)
        iteration_losses.append(metrics["loss"])

        # Print progress
        if (iteration + 1) % 10 == 0:
            print(
                f"Iter {iteration + 1}/{n_iterations} | "
                f"Reward: {avg_reward:.1f} | "
                f"Loss: {metrics['loss']:.4f} | "
                f"Entropy: {metrics['entropy']:.4f}"
            )

            if avg_reward >= 200:
                print(f"\n🎉 Solved in {iteration + 1} iterations!")
                break

    env.close()

    print("\n" + "=" * 70)
    print("Training complete!")
    print("=" * 70)

    return agent, iteration_rewards, iteration_losses


def evaluate_agent(agent: PPOAgent, env_name: str = "LunarLander-v2", n_episodes: int = 100):
    """Evaluate trained agent."""
    env = gym.make(env_name)

    rewards = []

    for episode in range(n_episodes):
        state, _ = env.reset(seed=SEED + 1000 + episode)
        episode_reward = 0
        done = False

        while not done:
            action, _, _ = agent.select_action(state)
            state, reward, terminated, truncated, _ = env.step(action)
            done = terminated or truncated
            episode_reward += reward

        rewards.append(episode_reward)

    env.close()

    mean_reward = np.mean(rewards)
    std_reward = np.std(rewards)

    print(f"\nEvaluation Results ({n_episodes} episodes):")
    print(f"  Mean Reward: {mean_reward:.1f} ± {std_reward:.1f}")

    return mean_reward, std_reward


def visualize_results(iteration_rewards, iteration_losses):
    """Visualize training results."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Plot rewards
    axes[0].plot(iteration_rewards, linewidth=2)
    axes[0].axhline(y=200, color="r", linestyle="--", label="Solved Threshold")
    axes[0].set_xlabel("Iteration")
    axes[0].set_ylabel("Average Reward (last 10 episodes)")
    axes[0].set_title("PPO Training Rewards (LunarLander-v2)")
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)

    # Plot loss
    axes[1].plot(iteration_losses, linewidth=2)
    axes[1].set_xlabel("Iteration")
    axes[1].set_ylabel("Loss")
    axes[1].set_title("Training Loss")
    axes[1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig("ppo_lunarlander.png", dpi=150, bbox_inches="tight")
    print("\nPlot saved as 'ppo_lunarlander.png'")
    plt.show()


if __name__ == "__main__":
    # Train agent
    agent, rewards, losses = train_ppo(n_iterations=500, steps_per_iteration=2048)

    # Evaluate agent
    evaluate_agent(agent, n_episodes=100)

    # Visualize results
    visualize_results(rewards, losses)

    print("\n✓ Example complete! PPO successfully trained on LunarLander.")
    print("  PPO is the most popular RL algorithm - works for 80% of problems!")
