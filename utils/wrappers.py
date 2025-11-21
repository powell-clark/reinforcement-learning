"""
Environment wrappers for preprocessing and monitoring.

Common wrappers:
- Observation normalization
- Reward scaling/clipping
- Frame stacking for Atari
- Episode recording
- Monitoring and logging
"""

import gymnasium as gym
import numpy as np
from typing import Optional, Tuple


class NormalizeObservation(gym.ObservationWrapper):
    """
    Normalize observations using running mean and std.
    """

    def __init__(self, env: gym.Env, epsilon: float = 1e-8):
        super().__init__(env)
        self.epsilon = epsilon
        self.running_mean = np.zeros(env.observation_space.shape)
        self.running_var = np.ones(env.observation_space.shape)
        self.count = 0

    def observation(self, obs: np.ndarray) -> np.ndarray:
        """Normalize observation."""
        self.count += 1
        delta = obs - self.running_mean
        self.running_mean += delta / self.count
        self.running_var += delta * (obs - self.running_mean)

        std = np.sqrt(self.running_var / self.count + self.epsilon)
        return (obs - self.running_mean) / std


class ClipReward(gym.RewardWrapper):
    """
    Clip rewards to [-clip_value, clip_value].
    """

    def __init__(self, env: gym.Env, clip_value: float = 1.0):
        super().__init__(env)
        self.clip_value = clip_value

    def reward(self, reward: float) -> float:
        """Clip reward."""
        return np.clip(reward, -self.clip_value, self.clip_value)


class EpisodeMonitor(gym.Wrapper):
    """
    Monitor episode statistics (returns, lengths).
    """

    def __init__(self, env: gym.Env):
        super().__init__(env)
        self.episode_returns = []
        self.episode_lengths = []
        self.current_return = 0.0
        self.current_length = 0

    def reset(self, **kwargs):
        """Reset and record episode statistics."""
        if self.current_length > 0:
            self.episode_returns.append(self.current_return)
            self.episode_lengths.append(self.current_length)

        self.current_return = 0.0
        self.current_length = 0
        return self.env.reset(**kwargs)

    def step(self, action):
        """Step and accumulate statistics."""
        obs, reward, terminated, truncated, info = self.env.step(action)
        self.current_return += reward
        self.current_length += 1
        return obs, reward, terminated, truncated, info

    def get_statistics(self) -> Tuple[np.ndarray, np.ndarray]:
        """Get episode statistics."""
        return np.array(self.episode_returns), np.array(self.episode_lengths)


# TODO: Add more wrappers as needed
# - FrameStack for Atari
# - TimeLimit wrapper
# - RecordVideo wrapper
# - ActionRepeat wrapper
