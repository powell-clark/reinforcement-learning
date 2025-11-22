"""
Example 1: Q-Learning on FrozenLake

This script demonstrates Q-Learning on the FrozenLake-v1 environment.
FrozenLake is a simple 4x4 grid where the agent must navigate from start
to goal while avoiding holes.

The agent learns to find the optimal path using Q-Learning, a fundamental
off-policy TD control algorithm.

Usage:
    python 01_qlearning_frozen_lake.py

Expected output:
    - Training progress showing increasing success rate
    - Final performance metrics
    - Learned policy visualization
"""

import sys
import os

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import gymnasium as gym
import numpy as np
from algorithms.tabular import QLearning
import matplotlib.pyplot as plt

# Set random seed for reproducibility
SEED = 42
np.random.seed(SEED)


def train_qlearning(
    env_name: str = "FrozenLake-v1",
    n_episodes: int = 10000,
    max_steps: int = 100,
    alpha: float = 0.1,
    gamma: float = 0.99,
    epsilon: float = 1.0,
    epsilon_decay: float = 0.9995,
    epsilon_min: float = 0.01,
):
    """
    Train Q-Learning agent on FrozenLake.

    Args:
        env_name: Environment name
        n_episodes: Number of training episodes
        max_steps: Maximum steps per episode
        alpha: Learning rate
        gamma: Discount factor
        epsilon: Initial exploration rate
        epsilon_decay: Epsilon decay per episode
        epsilon_min: Minimum epsilon

    Returns:
        agent: Trained Q-Learning agent
        rewards: List of episode rewards
        success_rate: List of rolling success rates
    """
    print("=" * 70)
    print(f"Training Q-Learning on {env_name}")
    print("=" * 70)
    print(f"Episodes: {n_episodes}")
    print(f"Alpha: {alpha}, Gamma: {gamma}")
    print(f"Epsilon: {epsilon} → {epsilon_min} (decay: {epsilon_decay})")
    print("=" * 70 + "\\n")

    # Create environment
    env = gym.make(env_name, is_slippery=False)  # Deterministic for easier learning
    env.reset(seed=SEED)

    # Create agent
    agent = QLearning(
        n_actions=env.action_space.n,
        alpha=alpha,
        gamma=gamma,
        epsilon=epsilon,
        epsilon_decay=epsilon_decay,
        epsilon_min=epsilon_min,
        seed=SEED,
    )

    # Training loop
    episode_rewards = []
    episode_successes = []

    for episode in range(n_episodes):
        state, _ = env.reset()
        episode_reward = 0
        success = False

        for step in range(max_steps):
            # Select action
            action = agent.select_action(state, training=True)

            # Take step
            next_state, reward, terminated, truncated, _ = env.step(action)
            done = terminated or truncated

            # Update Q-values
            agent.update(state, action, reward, next_state, done)

            episode_reward += reward
            state = next_state

            if done:
                if reward > 0:  # Reached goal
                    success = True
                break

        # Decay epsilon
        agent.decay_epsilon()

        # Record metrics
        episode_rewards.append(episode_reward)
        episode_successes.append(1.0 if success else 0.0)

        # Print progress
        if (episode + 1) % 1000 == 0:
            recent_success_rate = np.mean(episode_successes[-100:]) * 100
            print(
                f"Episode {episode + 1}/{n_episodes} | "
                f"Success Rate (last 100): {recent_success_rate:.1f}% | "
                f"Epsilon: {agent.epsilon:.3f}"
            )

    env.close()

    print("\\n" + "=" * 70)
    print("Training complete!")
    print("=" * 70)

    return agent, episode_rewards, episode_successes


def evaluate_agent(agent: QLearning, env_name: str = "FrozenLake-v1", n_episodes: int = 100):
    """Evaluate trained agent."""
    env = gym.make(env_name, is_slippery=False)

    successes = []
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
        successes.append(1.0 if episode_reward > 0 else 0.0)

    env.close()

    success_rate = np.mean(successes) * 100
    mean_reward = np.mean(rewards)

    print(f"\\nEvaluation Results ({n_episodes} episodes):")
    print(f"  Success Rate: {success_rate:.1f}%")
    print(f"  Mean Reward: {mean_reward:.3f}")

    return success_rate, mean_reward


def visualize_results(episode_rewards, episode_successes):
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
            range(window - 1, len(episode_rewards)), moving_avg, label=f"MA({window})"
        )
    axes[0].set_xlabel("Episode")
    axes[0].set_ylabel("Reward")
    axes[0].set_title("Training Rewards")
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)

    # Plot success rate
    success_rate = []
    window = 100
    for i in range(len(episode_successes)):
        if i >= window - 1:
            success_rate.append(np.mean(episode_successes[i - window + 1 : i + 1]))
        else:
            success_rate.append(np.mean(episode_successes[: i + 1]))

    axes[1].plot([s * 100 for s in success_rate], linewidth=2)
    axes[1].set_xlabel("Episode")
    axes[1].set_ylabel("Success Rate (%)")
    axes[1].set_title(f"Success Rate (Rolling {window}-episode average)")
    axes[1].grid(True, alpha=0.3)
    axes[1].set_ylim([0, 100])

    plt.tight_layout()
    plt.savefig("q_learning_frozen_lake.png", dpi=150, bbox_inches="tight")
    print("\\nPlot saved as 'q_learning_frozen_lake.png'")
    plt.show()


if __name__ == "__main__":
    # Train agent
    agent, rewards, successes = train_qlearning(
        n_episodes=10000,
        alpha=0.1,
        gamma=0.99,
        epsilon=1.0,
        epsilon_decay=0.9995,
        epsilon_min=0.01,
    )

    # Evaluate agent
    evaluate_agent(agent, n_episodes=100)

    # Visualize results
    visualize_results(rewards, successes)

    print("\\n✓ Example complete! Q-Learning successfully learned FrozenLake.")
