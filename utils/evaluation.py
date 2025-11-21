"""
Evaluation utilities for RL agents.

Functions for:
- Evaluating trained policies
- Computing metrics (success rate, average return, sample efficiency)
- Statistical testing across multiple seeds
- Benchmark comparisons
"""

import numpy as np
from typing import Callable, List, Optional, Tuple
import gymnasium as gym


def evaluate_policy(
    env: gym.Env,
    policy: Callable,
    n_episodes: int = 100,
    max_steps: int = 1000,
    render: bool = False,
    seed: Optional[int] = None,
) -> Tuple[float, float, List[float]]:
    """
    Evaluate a policy over multiple episodes.

    Args:
        env: Gymnasium environment
        policy: Policy function mapping observations to actions
        n_episodes: Number of evaluation episodes
        max_steps: Maximum steps per episode
        render: Whether to render episodes
        seed: Random seed for reproducibility

    Returns:
        mean_return: Mean episodic return
        std_return: Standard deviation of returns
        all_returns: List of all episode returns
    """
    if seed is not None:
        np.random.seed(seed)

    returns = []

    for episode in range(n_episodes):
        obs, info = env.reset(seed=seed + episode if seed else None)
        episode_return = 0.0
        done = False
        steps = 0

        while not done and steps < max_steps:
            action = policy(obs)
            obs, reward, terminated, truncated, info = env.step(action)
            episode_return += reward
            done = terminated or truncated
            steps += 1

            if render:
                env.render()

        returns.append(episode_return)

    mean_return = np.mean(returns)
    std_return = np.std(returns)

    return mean_return, std_return, returns


def compute_success_rate(
    returns: List[float],
    threshold: float,
) -> float:
    """
    Compute success rate based on return threshold.

    Args:
        returns: List of episode returns
        threshold: Success threshold

    Returns:
        success_rate: Fraction of episodes above threshold
    """
    successes = sum(1 for r in returns if r >= threshold)
    return successes / len(returns)


# TODO: Add more evaluation utilities
# - bootstrap_confidence_intervals()
# - statistical_comparison()
# - sample_efficiency_curves()
# - rliable integration for rigorous evaluation
