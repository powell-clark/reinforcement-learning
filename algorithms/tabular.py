"""
Tabular Reinforcement Learning Algorithms

This module implements classic tabular RL algorithms that work with discrete
state and action spaces. These algorithms store value functions in tables.

Algorithms:
- Q-Learning: Off-policy TD control
- SARSA: On-policy TD control
- Monte Carlo: Episode-based learning

All implementations use incremental updates and support:
- ε-greedy exploration
- Learning rate schedules
- Discount factor
- Reproducible random seeds
"""

import numpy as np
from typing import Tuple, Dict, Optional, Callable
from collections import defaultdict


class QLearning:
    """
    Q-Learning: Off-policy Temporal Difference Control Algorithm.

    Q-Learning learns the optimal action-value function Q*(s,a) using:
        Q(s,a) ← Q(s,a) + α[r + γ max_a' Q(s',a') - Q(s,a)]

    This is off-policy because it learns about the greedy policy while
    following an ε-greedy policy for exploration.

    Args:
        n_actions: Number of actions in the environment
        alpha: Learning rate (step size)
        gamma: Discount factor for future rewards
        epsilon: Exploration rate for ε-greedy policy
        epsilon_decay: Multiplicative decay for epsilon per episode
        epsilon_min: Minimum value for epsilon
        seed: Random seed for reproducibility

    Example:
        >>> agent = QLearning(n_actions=4, alpha=0.1, gamma=0.99, epsilon=0.1)
        >>> action = agent.select_action(state)
        >>> agent.update(state, action, reward, next_state, done)
    """

    def __init__(
        self,
        n_actions: int,
        alpha: float = 0.1,
        gamma: float = 0.99,
        epsilon: float = 0.1,
        epsilon_decay: float = 0.995,
        epsilon_min: float = 0.01,
        seed: Optional[int] = None,
    ):
        self.n_actions = n_actions
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.epsilon_decay = epsilon_decay
        self.epsilon_min = epsilon_min

        # Q-table: maps (state, action) to Q-value
        self.Q = defaultdict(lambda: np.zeros(n_actions))

        # Set random seed
        if seed is not None:
            np.random.seed(seed)

        # Statistics
        self.training_steps = 0
        self.episodes = 0

    def select_action(self, state: Tuple, training: bool = True) -> int:
        """
        Select action using ε-greedy policy.

        Args:
            state: Current state
            training: If True, use ε-greedy exploration. If False, use greedy policy.

        Returns:
            Selected action index
        """
        if training and np.random.rand() < self.epsilon:
            # Explore: random action
            return np.random.randint(self.n_actions)
        else:
            # Exploit: greedy action
            return int(np.argmax(self.Q[state]))

    def update(
        self,
        state: Tuple,
        action: int,
        reward: float,
        next_state: Tuple,
        done: bool,
    ) -> float:
        """
        Update Q-value using Q-learning update rule.

        Args:
            state: Current state
            action: Action taken
            reward: Reward received
            next_state: Next state observed
            done: Whether episode terminated

        Returns:
            TD error (for monitoring learning progress)
        """
        # Current Q-value
        current_q = self.Q[state][action]

        # Target: r + γ max_a' Q(s',a') for Q-learning
        if done:
            target = reward  # No future value at terminal state
        else:
            target = reward + self.gamma * np.max(self.Q[next_state])

        # TD error
        td_error = target - current_q

        # Q-learning update
        self.Q[state][action] = current_q + self.alpha * td_error

        # Update statistics
        self.training_steps += 1

        return td_error

    def decay_epsilon(self):
        """Decay epsilon after each episode."""
        self.epsilon = max(self.epsilon_min, self.epsilon * self.epsilon_decay)
        self.episodes += 1

    def get_value(self, state: Tuple) -> float:
        """Get state value V(s) = max_a Q(s,a)."""
        return float(np.max(self.Q[state]))

    def get_policy(self) -> Dict[Tuple, int]:
        """Get greedy policy π(s) = argmax_a Q(s,a)."""
        return {state: int(np.argmax(q_values))
                for state, q_values in self.Q.items()}


class SARSA:
    """
    SARSA: On-policy Temporal Difference Control Algorithm.

    SARSA learns the action-value function for the policy being followed:
        Q(s,a) ← Q(s,a) + α[r + γ Q(s',a') - Q(s,a)]

    This is on-policy because it learns about the same ε-greedy policy
    that it uses to select actions.

    Args:
        n_actions: Number of actions
        alpha: Learning rate
        gamma: Discount factor
        epsilon: Exploration rate
        epsilon_decay: Epsilon decay per episode
        epsilon_min: Minimum epsilon
        seed: Random seed

    Example:
        >>> agent = SARSA(n_actions=4, alpha=0.1, gamma=0.99)
        >>> action = agent.select_action(state)
        >>> next_action = agent.select_action(next_state)
        >>> agent.update(state, action, reward, next_state, next_action, done)
    """

    def __init__(
        self,
        n_actions: int,
        alpha: float = 0.1,
        gamma: float = 0.99,
        epsilon: float = 0.1,
        epsilon_decay: float = 0.995,
        epsilon_min: float = 0.01,
        seed: Optional[int] = None,
    ):
        self.n_actions = n_actions
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.epsilon_decay = epsilon_decay
        self.epsilon_min = epsilon_min

        self.Q = defaultdict(lambda: np.zeros(n_actions))

        if seed is not None:
            np.random.seed(seed)

        self.training_steps = 0
        self.episodes = 0

    def select_action(self, state: Tuple, training: bool = True) -> int:
        """Select action using ε-greedy policy."""
        if training and np.random.rand() < self.epsilon:
            return np.random.randint(self.n_actions)
        else:
            return int(np.argmax(self.Q[state]))

    def update(
        self,
        state: Tuple,
        action: int,
        reward: float,
        next_state: Tuple,
        next_action: int,
        done: bool,
    ) -> float:
        """
        Update Q-value using SARSA update rule.

        Note: Unlike Q-learning, SARSA requires next_action (actually taken).

        Args:
            state: Current state
            action: Action taken
            reward: Reward received
            next_state: Next state
            next_action: Next action actually taken (not max!)
            done: Terminal flag

        Returns:
            TD error
        """
        current_q = self.Q[state][action]

        # Target: r + γ Q(s',a') for SARSA (uses actual next action)
        if done:
            target = reward
        else:
            target = reward + self.gamma * self.Q[next_state][next_action]

        td_error = target - current_q
        self.Q[state][action] = current_q + self.alpha * td_error

        self.training_steps += 1
        return td_error

    def decay_epsilon(self):
        """Decay epsilon after each episode."""
        self.epsilon = max(self.epsilon_min, self.epsilon * self.epsilon_decay)
        self.episodes += 1

    def get_value(self, state: Tuple) -> float:
        """Get state value."""
        return float(np.max(self.Q[state]))

    def get_policy(self) -> Dict[Tuple, int]:
        """Get greedy policy."""
        return {state: int(np.argmax(q_values))
                for state, q_values in self.Q.items()}


class MonteCarlo:
    """
    Monte Carlo Control with Epsilon-Greedy Exploration.

    Monte Carlo methods learn from complete episodes. This implementation
    uses first-visit MC with incremental updates.

    MC Update (after episode):
        For each (s,a) in episode:
            Q(s,a) ← Q(s,a) + α[G - Q(s,a)]
        where G is the actual return from that visit.

    Args:
        n_actions: Number of actions
        gamma: Discount factor
        epsilon: Exploration rate
        epsilon_decay: Epsilon decay
        epsilon_min: Minimum epsilon
        seed: Random seed

    Example:
        >>> agent = MonteCarlo(n_actions=4, gamma=0.99)
        >>> # Collect episode
        >>> episode = [(s0, a0, r1), (s1, a1, r2), ...]
        >>> agent.update_from_episode(episode)
    """

    def __init__(
        self,
        n_actions: int,
        gamma: float = 0.99,
        epsilon: float = 0.1,
        epsilon_decay: float = 0.995,
        epsilon_min: float = 0.01,
        seed: Optional[int] = None,
    ):
        self.n_actions = n_actions
        self.gamma = gamma
        self.epsilon = epsilon
        self.epsilon_decay = epsilon_decay
        self.epsilon_min = epsilon_min

        # Q-values and visit counts
        self.Q = defaultdict(lambda: np.zeros(n_actions))
        self.N = defaultdict(lambda: np.zeros(n_actions))  # Visit counts

        if seed is not None:
            np.random.seed(seed)

        self.episodes = 0

    def select_action(self, state: Tuple, training: bool = True) -> int:
        """Select action using ε-greedy policy."""
        if training and np.random.rand() < self.epsilon:
            return np.random.randint(self.n_actions)
        else:
            return int(np.argmax(self.Q[state]))

    def update_from_episode(
        self,
        episode: list,
        first_visit: bool = True,
    ) -> float:
        """
        Update Q-values from complete episode.

        Args:
            episode: List of (state, action, reward) tuples
            first_visit: If True, use first-visit MC. Else every-visit.

        Returns:
            Total return for the episode
        """
        # Calculate returns for each timestep
        G = 0.0
        returns = []

        # Work backwards through episode
        for t in range(len(episode) - 1, -1, -1):
            _, _, reward = episode[t]
            G = reward + self.gamma * G
            returns.insert(0, G)

        # Update Q-values
        visited = set() if first_visit else None

        for t, (state, action, _) in enumerate(episode):
            sa_pair = (state, action)

            # Skip if already visited (for first-visit MC)
            if first_visit and sa_pair in visited:
                continue

            if first_visit:
                visited.add(sa_pair)

            # Incremental update
            self.N[state][action] += 1
            alpha = 1.0 / self.N[state][action]  # Diminishing step size
            self.Q[state][action] += alpha * (returns[t] - self.Q[state][action])

        self.episodes += 1
        return returns[0] if returns else 0.0

    def decay_epsilon(self):
        """Decay epsilon after episode."""
        self.epsilon = max(self.epsilon_min, self.epsilon * self.epsilon_decay)

    def get_value(self, state: Tuple) -> float:
        """Get state value."""
        return float(np.max(self.Q[state]))

    def get_policy(self) -> Dict[Tuple, int]:
        """Get greedy policy."""
        return {state: int(np.argmax(q_values))
                for state, q_values in self.Q.items()}
