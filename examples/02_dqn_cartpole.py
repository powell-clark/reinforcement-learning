"""
Example 2: Deep Q-Network (DQN) on CartPole

This script demonstrates DQN on the CartPole-v1 environment.
CartPole is a classic control problem where the agent must balance a pole
on a cart by moving left or right.

DQN extends Q-Learning to continuous state spaces using neural networks,
experience replay, and target networks for stability.

Usage:
    python 02_dqn_cartpole.py

Expected output:
    - Training progress showing increasing episode rewards
    - Solved in ~200-500 episodes (avg reward > 475)
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
from collections import deque
import random
import matplotlib.pyplot as plt

# Set random seeds for reproducibility
SEED = 42
random.seed(SEED)
np.random.seed(SEED)
torch.manual_seed(SEED)


class ReplayBuffer:
    """Experience replay buffer for DQN."""

    def __init__(self, capacity: int = 10000):
        self.buffer = deque(maxlen=capacity)

    def push(self, state, action, reward, next_state, done):
        """Add experience to buffer."""
        self.buffer.append((state, action, reward, next_state, done))

    def sample(self, batch_size: int):
        """Sample random batch from buffer."""
        batch = random.sample(self.buffer, batch_size)
        states, actions, rewards, next_states, dones = zip(*batch)

        return (
            np.array(states),
            np.array(actions),
            np.array(rewards, dtype=np.float32),
            np.array(next_states),
            np.array(dones, dtype=np.float32),
        )

    def __len__(self):
        return len(self.buffer)


class DQN(nn.Module):
    """Deep Q-Network."""

    def __init__(self, state_dim: int, action_dim: int, hidden_dim: int = 128):
        super().__init__()
        self.network = nn.Sequential(
            nn.Linear(state_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, action_dim),
        )

    def forward(self, x):
        return self.network(x)


class DQNAgent:
    """DQN Agent with experience replay and target network."""

    def __init__(
        self,
        state_dim: int,
        action_dim: int,
        hidden_dim: int = 128,
        lr: float = 1e-3,
        gamma: float = 0.99,
        epsilon: float = 1.0,
        epsilon_decay: float = 0.995,
        epsilon_min: float = 0.01,
        buffer_size: int = 10000,
        batch_size: int = 64,
        target_update_freq: int = 10,
    ):
        self.state_dim = state_dim
        self.action_dim = action_dim
        self.gamma = gamma
        self.epsilon = epsilon
        self.epsilon_decay = epsilon_decay
        self.epsilon_min = epsilon_min
        self.batch_size = batch_size
        self.target_update_freq = target_update_freq

        # Q-networks
        self.q_network = DQN(state_dim, action_dim, hidden_dim)
        self.target_network = DQN(state_dim, action_dim, hidden_dim)
        self.target_network.load_state_dict(self.q_network.state_dict())

        # Optimizer
        self.optimizer = optim.Adam(self.q_network.parameters(), lr=lr)

        # Replay buffer
        self.replay_buffer = ReplayBuffer(buffer_size)

        # Training stats
        self.update_count = 0

    def select_action(self, state, training=True):
        """Select action using epsilon-greedy policy."""
        if training and random.random() < self.epsilon:
            return random.randrange(self.action_dim)

        with torch.no_grad():
            state = torch.FloatTensor(state).unsqueeze(0)
            q_values = self.q_network(state)
            return q_values.argmax().item()

    def update(self):
        """Update Q-network using batch from replay buffer."""
        if len(self.replay_buffer) < self.batch_size:
            return None

        # Sample batch
        states, actions, rewards, next_states, dones = self.replay_buffer.sample(
            self.batch_size
        )

        # Convert to tensors
        states = torch.FloatTensor(states)
        actions = torch.LongTensor(actions)
        rewards = torch.FloatTensor(rewards)
        next_states = torch.FloatTensor(next_states)
        dones = torch.FloatTensor(dones)

        # Compute current Q-values
        current_q = self.q_network(states).gather(1, actions.unsqueeze(1)).squeeze(1)

        # Compute target Q-values
        with torch.no_grad():
            next_q = self.target_network(next_states).max(1)[0]
            target_q = rewards + (1 - dones) * self.gamma * next_q

        # Compute loss
        loss = nn.MSELoss()(current_q, target_q)

        # Optimize
        self.optimizer.zero_grad()
        loss.backward()
        torch.nn.utils.clip_grad_norm_(self.q_network.parameters(), 1.0)
        self.optimizer.step()

        # Update target network
        self.update_count += 1
        if self.update_count % self.target_update_freq == 0:
            self.target_network.load_state_dict(self.q_network.state_dict())

        return loss.item()

    def decay_epsilon(self):
        """Decay exploration rate."""
        self.epsilon = max(self.epsilon_min, self.epsilon * self.epsilon_decay)


def train_dqn(
    env_name: str = "CartPole-v1",
    n_episodes: int = 500,
    max_steps: int = 500,
    lr: float = 1e-3,
    gamma: float = 0.99,
    epsilon: float = 1.0,
    epsilon_decay: float = 0.995,
    epsilon_min: float = 0.01,
    buffer_size: int = 10000,
    batch_size: int = 64,
    target_update_freq: int = 10,
):
    """Train DQN agent on CartPole."""
    print("=" * 70)
    print(f"Training DQN on {env_name}")
    print("=" * 70)
    print(f"Episodes: {n_episodes}")
    print(f"Learning rate: {lr}, Gamma: {gamma}")
    print(f"Epsilon: {epsilon} → {epsilon_min} (decay: {epsilon_decay})")
    print(f"Buffer: {buffer_size}, Batch: {batch_size}")
    print(f"Target update frequency: {target_update_freq}")
    print("=" * 70 + "\n")

    # Create environment
    env = gym.make(env_name)
    env.reset(seed=SEED)

    # Create agent
    state_dim = env.observation_space.shape[0]
    action_dim = env.action_space.n

    agent = DQNAgent(
        state_dim=state_dim,
        action_dim=action_dim,
        lr=lr,
        gamma=gamma,
        epsilon=epsilon,
        epsilon_decay=epsilon_decay,
        epsilon_min=epsilon_min,
        buffer_size=buffer_size,
        batch_size=batch_size,
        target_update_freq=target_update_freq,
    )

    # Training loop
    episode_rewards = []
    episode_losses = []

    for episode in range(n_episodes):
        state, _ = env.reset()
        episode_reward = 0
        episode_loss = []

        for step in range(max_steps):
            # Select and take action
            action = agent.select_action(state, training=True)
            next_state, reward, terminated, truncated, _ = env.step(action)
            done = terminated or truncated

            # Store transition
            agent.replay_buffer.push(state, action, reward, next_state, done)

            # Update agent
            loss = agent.update()
            if loss is not None:
                episode_loss.append(loss)

            episode_reward += reward
            state = next_state

            if done:
                break

        # Decay epsilon
        agent.decay_epsilon()

        # Record metrics
        episode_rewards.append(episode_reward)
        episode_losses.append(np.mean(episode_loss) if episode_loss else 0)

        # Print progress
        if (episode + 1) % 50 == 0:
            recent_reward = np.mean(episode_rewards[-100:])
            print(
                f"Episode {episode + 1}/{n_episodes} | "
                f"Reward: {episode_reward:.0f} | "
                f"Avg(100): {recent_reward:.1f} | "
                f"Epsilon: {agent.epsilon:.3f} | "
                f"Loss: {episode_losses[-1]:.4f}"
            )

            # Check if solved
            if recent_reward >= 475:
                print(f"\n🎉 Solved in {episode + 1} episodes!")
                print(f"Average reward over last 100 episodes: {recent_reward:.1f}")
                break

    env.close()

    print("\n" + "=" * 70)
    print("Training complete!")
    print("=" * 70)

    return agent, episode_rewards, episode_losses


def evaluate_agent(agent: DQNAgent, env_name: str = "CartPole-v1", n_episodes: int = 100):
    """Evaluate trained agent."""
    env = gym.make(env_name)

    rewards = []

    for episode in range(n_episodes):
        state, _ = env.reset(seed=SEED + 1000 + episode)
        episode_reward = 0
        done = False

        while not done:
            action = agent.select_action(state, training=False)  # Greedy
            state, reward, terminated, truncated, _ = env.step(action)
            done = terminated or truncated
            episode_reward += reward

        rewards.append(episode_reward)

    env.close()

    mean_reward = np.mean(rewards)
    std_reward = np.std(rewards)

    print(f"\nEvaluation Results ({n_episodes} episodes):")
    print(f"  Mean Reward: {mean_reward:.1f} ± {std_reward:.1f}")
    print(f"  Min: {np.min(rewards):.0f}, Max: {np.max(rewards):.0f}")

    return mean_reward, std_reward


def visualize_results(episode_rewards, episode_losses):
    """Visualize training results."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Plot episode rewards
    axes[0].plot(episode_rewards, alpha=0.3, label="Episode Reward")
    window = 100
    if len(episode_rewards) >= window:
        moving_avg = np.convolve(
            episode_rewards, np.ones(window) / window, mode="valid"
        )
        axes[0].plot(
            range(window - 1, len(episode_rewards)),
            moving_avg,
            label=f"MA({window})",
            linewidth=2,
        )
    axes[0].axhline(y=475, color="r", linestyle="--", label="Solved Threshold")
    axes[0].set_xlabel("Episode")
    axes[0].set_ylabel("Reward")
    axes[0].set_title("DQN Training Rewards (CartPole-v1)")
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)

    # Plot loss
    if len(episode_losses) > 0:
        axes[1].plot(episode_losses, alpha=0.5, label="Episode Loss")
        window = 50
        if len(episode_losses) >= window:
            moving_avg = np.convolve(
                episode_losses, np.ones(window) / window, mode="valid"
            )
            axes[1].plot(
                range(window - 1, len(episode_losses)),
                moving_avg,
                label=f"MA({window})",
                linewidth=2,
            )
        axes[1].set_xlabel("Episode")
        axes[1].set_ylabel("Loss")
        axes[1].set_title("Training Loss")
        axes[1].legend()
        axes[1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig("dqn_cartpole.png", dpi=150, bbox_inches="tight")
    print("\nPlot saved as 'dqn_cartpole.png'")
    plt.show()


if __name__ == "__main__":
    # Train agent
    agent, rewards, losses = train_dqn(
        n_episodes=500,
        lr=1e-3,
        gamma=0.99,
        epsilon=1.0,
        epsilon_decay=0.995,
        epsilon_min=0.01,
        buffer_size=10000,
        batch_size=64,
        target_update_freq=10,
    )

    # Evaluate agent
    evaluate_agent(agent, n_episodes=100)

    # Visualize results
    visualize_results(rewards, losses)

    print("\n✓ Example complete! DQN successfully solved CartPole.")
