"""
Reinforcement Learning Algorithms Module

This module contains production-ready implementations of core RL algorithms:
- Tabular methods: Q-Learning, SARSA, Monte Carlo
- Deep RL: DQN, DDQN, Dueling DQN
- Policy Gradients: REINFORCE, Actor-Critic, PPO
- Continuous Control: DDPG, TD3, SAC

All implementations follow elite university standards with:
- Type hints and comprehensive docstrings
- Proper logging and reproducibility
- Efficient vectorized operations
- Clean, readable code following PEP 8

Version: 1.0.0
Author: Powell-Clark Limited
"""

__version__ = "1.0.0"
__author__ = "Powell-Clark Limited"

from .tabular import QLearning, SARSA, MonteCarlo
from .deep import DQN, DoubleDQN
from .policy_gradient import REINFORCE, ActorCritic

__all__ = [
    "QLearning",
    "SARSA",
    "MonteCarlo",
    "DQN",
    "DoubleDQN",
    "REINFORCE",
    "ActorCritic",
]
