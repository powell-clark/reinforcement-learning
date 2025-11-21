"""
Tests for environment wrappers and utilities.
"""

import pytest
import gymnasium as gym
import numpy as np
from utils.wrappers import NormalizeObservation, ClipReward, EpisodeMonitor


def test_normalize_observation():
    """Test observation normalization wrapper."""
    env = gym.make("CartPole-v1")
    env = NormalizeObservation(env)

    obs, info = env.reset()
    assert obs.shape == env.observation_space.shape

    for _ in range(10):
        obs, reward, terminated, truncated, info = env.step(env.action_space.sample())
        assert not np.any(np.isnan(obs)), "Normalized observation contains NaN"
        assert not np.any(np.isinf(obs)), "Normalized observation contains Inf"

    env.close()


def test_clip_reward():
    """Test reward clipping wrapper."""
    env = gym.make("CartPole-v1")
    env = ClipReward(env, clip_value=1.0)

    obs, info = env.reset()

    for _ in range(10):
        obs, reward, terminated, truncated, info = env.step(env.action_space.sample())
        assert -1.0 <= reward <= 1.0, "Reward not properly clipped"

    env.close()


def test_episode_monitor():
    """Test episode monitoring wrapper."""
    env = gym.make("CartPole-v1")
    env = EpisodeMonitor(env)

    # Run a few episodes
    for episode in range(3):
        obs, info = env.reset()
        done = False
        while not done:
            obs, reward, terminated, truncated, info = env.step(env.action_space.sample())
            done = terminated or truncated

    returns, lengths = env.get_statistics()
    assert len(returns) == 3, "Should have recorded 3 episodes"
    assert len(lengths) == 3, "Should have recorded 3 episode lengths"
    assert all(r > 0 for r in returns), "All returns should be positive"

    env.close()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
