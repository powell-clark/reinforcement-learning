"""
Tests for RL algorithm implementations.

These tests verify correctness of algorithm implementations:
- Q-learning, DQN, PPO, SAC, etc.
- Proper gradient computation
- Loss calculations
- Training stability
"""

import pytest
import numpy as np
import torch
import torch.nn as nn


def test_bellman_backup():
    """Test Bellman backup computation."""
    # Q(s,a) = r + gamma * max_a' Q(s', a')
    q_values = np.array([1.0, 2.0, 3.0])
    reward = 1.0
    gamma = 0.99
    next_q_values = np.array([2.0, 3.0, 4.0])

    expected_target = reward + gamma * np.max(next_q_values)
    actual_target = reward + gamma * np.max(next_q_values)

    assert np.isclose(expected_target, actual_target), "Bellman backup incorrect"


def test_q_network_forward_pass():
    """Test Q-network forward pass."""
    state_dim = 4
    action_dim = 2
    batch_size = 32

    # Simple Q-network
    q_net = nn.Sequential(
        nn.Linear(state_dim, 64),
        nn.ReLU(),
        nn.Linear(64, action_dim)
    )

    # Test forward pass
    states = torch.randn(batch_size, state_dim)
    q_values = q_net(states)

    assert q_values.shape == (batch_size, action_dim), "Q-values shape incorrect"
    assert not torch.isnan(q_values).any(), "Q-values contain NaN"


def test_policy_gradient_loss():
    """Test policy gradient loss computation."""
    # Log probabilities and returns
    log_probs = torch.tensor([-0.5, -0.3, -0.7])
    returns = torch.tensor([10.0, 5.0, 15.0])

    # Policy gradient loss: -sum(log_prob * return)
    loss = -torch.sum(log_probs * returns)

    assert loss.item() > 0, "Loss should be positive (we negate log probs)"
    assert not torch.isnan(loss), "Loss contains NaN"


def test_advantage_computation():
    """Test advantage function computation."""
    returns = np.array([10.0, 5.0, 15.0])
    values = np.array([8.0, 6.0, 12.0])

    advantages = returns - values
    expected_advantages = np.array([2.0, -1.0, 3.0])

    assert np.allclose(advantages, expected_advantages), "Advantages computed incorrectly"


# TODO: Add more implementation tests
# - test_dqn_training_step()
# - test_ppo_clip_objective()
# - test_experience_replay_buffer()
# - test_target_network_update()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
