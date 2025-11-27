"""
Example 4: RLHF (Reinforcement Learning from Human Feedback) - Simple Demo

This script demonstrates the core concepts of RLHF used to align LLMs like ChatGPT.
We implement a simplified version showing:
1. Reward model training from preferences
2. Policy optimization with PPO
3. Direct Preference Optimization (DPO)

For full LLM training, see notebook 16b_rlhf_practical.ipynb

This example uses a simple text generation task to illustrate RLHF mechanics
without requiring large transformer models or GPUs.

Usage:
    python 04_rlhf_simple_demo.py

Expected output:
    - Reward model training on preferences
    - Policy improvement via learned rewards
    - Comparison of PPO-RLHF vs DPO
"""

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from collections import defaultdict
import matplotlib.pyplot as plt

# Set random seeds
SEED = 42
np.random.seed(SEED)
torch.manual_seed(SEED)


class SimpleRewardModel(nn.Module):
    """
    Reward model that learns to predict human preferences.

    In real RLHF (ChatGPT), this would be a transformer that processes
    (prompt, response) pairs and outputs a scalar reward.

    For this demo, we use a simple network that rates text quality.
    """

    def __init__(self, input_dim: int = 10, hidden_dim: int = 32):
        super().__init__()
        self.network = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, 1),  # Scalar reward
        )

    def forward(self, x):
        """Predict reward for a response."""
        return self.network(x).squeeze(-1)


class SimplePolicy(nn.Module):
    """
    Policy network that generates responses.

    In real RLHF, this would be an LLM like GPT-3.5.
    For this demo, it's a simple network.
    """

    def __init__(self, state_dim: int = 5, action_dim: int = 10, hidden_dim: int = 32):
        super().__init__()
        self.network = nn.Sequential(
            nn.Linear(state_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, action_dim),
        )

    def forward(self, x):
        """Generate action distribution given state."""
        return self.network(x)

    def get_logprobs(self, states, actions):
        """Get log probabilities of actions."""
        logits = self.forward(states)
        log_probs = F.log_softmax(logits, dim=-1)
        return log_probs.gather(1, actions.unsqueeze(1)).squeeze(1)


def generate_preference_data(n_samples: int = 1000):
    """
    Generate synthetic preference data.

    In real RLHF:
    - Humans compare two LLM responses: "Which is better?"
    - Creates dataset of (response_1, response_2, preference)

    This simulates that with synthetic data.
    """
    preferences = []

    for _ in range(n_samples):
        # Generate two random "responses" (in practice: LLM outputs)
        response_1 = torch.randn(10)
        response_2 = torch.randn(10)

        # Simulate human preference (higher sum = "better quality")
        # In reality: actual human judgment
        score_1 = response_1.sum().item()
        score_2 = response_2.sum().item()
        preference = 1 if score_2 > score_1 else 0  # 1 = prefer response_2

        preferences.append((response_1, response_2, preference))

    return preferences


def train_reward_model(preferences, n_epochs: int = 100):
    """
    Train reward model from human preferences using Bradley-Terry model.

    This is Step 2 of RLHF pipeline:
    1. SFT (supervised fine-tuning) - not shown
    2. Train reward model ← WE ARE HERE
    3. PPO with learned reward

    Bradley-Terry model: P(y1 > y2) = σ(r(y1) - r(y2))
    """
    print("=" * 70)
    print("Step 1: Training Reward Model from Human Preferences")
    print("=" * 70)
    print(f"Preferences: {len(preferences)}")
    print(f"Epochs: {n_epochs}")
    print("=" * 70 + "\n")

    reward_model = SimpleRewardModel()
    optimizer = optim.Adam(reward_model.parameters(), lr=1e-3)

    losses = []

    for epoch in range(n_epochs):
        epoch_loss = 0

        for response_1, response_2, preference in preferences:
            # Compute rewards for both responses
            r1 = reward_model(response_1.unsqueeze(0))
            r2 = reward_model(response_2.unsqueeze(0))

            # Bradley-Terry loss
            # If preference=1: prefer r2, so maximize σ(r2 - r1)
            # If preference=0: prefer r1, so maximize σ(r1 - r2)
            if preference == 1:
                loss = -F.logsigmoid(r2 - r1)
            else:
                loss = -F.logsigmoid(r1 - r2)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            epoch_loss += loss.item()

        avg_loss = epoch_loss / len(preferences)
        losses.append(avg_loss)

        if (epoch + 1) % 20 == 0:
            print(f"Epoch {epoch + 1}/{n_epochs} | Loss: {avg_loss:.4f}")

    print("\n✓ Reward model trained!\n")
    return reward_model, losses


def train_policy_with_rlhf(reward_model, n_iterations: int = 200):
    """
    Train policy using PPO with learned reward model.

    This is Step 3 of RLHF pipeline:
    Objective: max E[r_RM(x,y) - β * KL(π || π_ref)]

    Where:
    - r_RM: Learned reward model
    - KL penalty: Prevents policy from drifting too far from reference
    """
    print("=" * 70)
    print("Step 2: Training Policy with PPO-RLHF")
    print("=" * 70)
    print(f"Iterations: {n_iterations}")
    print("Using learned reward model + KL penalty")
    print("=" * 70 + "\n")

    state_dim, action_dim = 5, 10

    # Policy to optimize
    policy = SimplePolicy(state_dim, action_dim)

    # Reference policy (frozen) - prevents collapse
    ref_policy = SimplePolicy(state_dim, action_dim)
    ref_policy.load_state_dict(policy.state_dict())

    optimizer = optim.Adam(policy.parameters(), lr=3e-4)

    rewards_history = []
    kl_history = []

    beta = 0.1  # KL penalty coefficient

    for iteration in range(n_iterations):
        # Sample states
        states = torch.randn(32, state_dim)

        # Get actions from current policy
        logits = policy(states)
        actions = torch.distributions.Categorical(logits=logits).sample()

        # Compute "responses" for reward model
        responses = torch.randn(32, 10)  # Simplified

        # Get rewards from learned reward model
        with torch.no_grad():
            rm_rewards = reward_model(responses)

        # Compute KL divergence from reference policy
        with torch.no_grad():
            ref_logits = ref_policy(states)
        ref_dist = torch.distributions.Categorical(logits=ref_logits)
        curr_dist = torch.distributions.Categorical(logits=logits)
        kl_div = torch.distributions.kl_divergence(curr_dist, ref_dist)

        # RLHF objective: reward - β * KL
        rlhf_rewards = rm_rewards - beta * kl_div

        # Policy gradient (simplified PPO)
        log_probs = policy.get_logprobs(states, actions)
        loss = -(log_probs * rlhf_rewards).mean()

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        rewards_history.append(rm_rewards.mean().item())
        kl_history.append(kl_div.mean().item())

        if (iteration + 1) % 40 == 0:
            print(
                f"Iter {iteration + 1}/{n_iterations} | "
                f"Reward: {rm_rewards.mean():.3f} | "
                f"KL: {kl_div.mean():.3f}"
            )

    print("\n✓ Policy trained with RLHF!\n")
    return policy, rewards_history, kl_history


def train_policy_with_dpo(preferences, n_epochs: int = 100):
    """
    Train policy using Direct Preference Optimization (DPO).

    DPO is simpler than PPO-RLHF:
    - No separate reward model needed
    - Directly optimizes from preferences
    - More stable training

    DPO Loss: -E[log σ(β log(π/π_ref)[y_w] - β log(π/π_ref)[y_l])]

    Where:
    - y_w: preferred response
    - y_l: less preferred response
    """
    print("=" * 70)
    print("Step 3: Training Policy with DPO (Direct Preference Optimization)")
    print("=" * 70)
    print(f"Preferences: {len(preferences)}")
    print(f"Epochs: {n_epochs}")
    print("DPO = Simpler RLHF (no reward model needed)")
    print("=" * 70 + "\n")

    state_dim, action_dim = 5, 10

    policy = SimplePolicy(state_dim, action_dim)
    ref_policy = SimplePolicy(state_dim, action_dim)
    ref_policy.load_state_dict(policy.state_dict())

    optimizer = optim.Adam(policy.parameters(), lr=1e-3)

    losses = []
    beta = 0.1

    # Create simplified dataset
    states = torch.randn(len(preferences), state_dim)
    actions_w = torch.randint(0, action_dim, (len(preferences),))  # Preferred
    actions_l = torch.randint(0, action_dim, (len(preferences),))  # Less preferred

    for epoch in range(n_epochs):
        # Get log probs from current policy
        log_pi_w = policy.get_logprobs(states, actions_w)
        log_pi_l = policy.get_logprobs(states, actions_l)

        # Get log probs from reference policy
        with torch.no_grad():
            log_ref_w = ref_policy.get_logprobs(states, actions_w)
            log_ref_l = ref_policy.get_logprobs(states, actions_l)

        # DPO loss
        logits = beta * (log_pi_w - log_ref_w) - beta * (log_pi_l - log_ref_l)
        loss = -F.logsigmoid(logits).mean()

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        losses.append(loss.item())

        if (epoch + 1) % 20 == 0:
            print(f"Epoch {epoch + 1}/{n_epochs} | Loss: {loss.item():.4f}")

    print("\n✓ Policy trained with DPO!\n")
    return policy, losses


def visualize_results(rm_losses, rlhf_rewards, rlhf_kl, dpo_losses):
    """Visualize RLHF training."""
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Reward model training
    axes[0, 0].plot(rm_losses, linewidth=2)
    axes[0, 0].set_xlabel("Epoch")
    axes[0, 0].set_ylabel("Loss")
    axes[0, 0].set_title("Step 1: Reward Model Training (Bradley-Terry)")
    axes[0, 0].grid(True, alpha=0.3)

    # RLHF rewards
    axes[0, 1].plot(rlhf_rewards, linewidth=2, color="green")
    axes[0, 1].set_xlabel("Iteration")
    axes[0, 1].set_ylabel("Average Reward")
    axes[0, 1].set_title("Step 2: PPO-RLHF Rewards")
    axes[0, 1].grid(True, alpha=0.3)

    # RLHF KL divergence
    axes[1, 0].plot(rlhf_kl, linewidth=2, color="orange")
    axes[1, 0].set_xlabel("Iteration")
    axes[1, 0].set_ylabel("KL Divergence")
    axes[1, 0].set_title("Step 2: KL from Reference Policy")
    axes[1, 0].grid(True, alpha=0.3)

    # DPO training
    axes[1, 1].plot(dpo_losses, linewidth=2, color="purple")
    axes[1, 1].set_xlabel("Epoch")
    axes[1, 1].set_ylabel("Loss")
    axes[1, 1].set_title("Step 3: DPO Training (Simpler Alternative)")
    axes[1, 1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig("rlhf_demo.png", dpi=150, bbox_inches="tight")
    print("\nPlot saved as 'rlhf_demo.png'\n")
    plt.show()


if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("RLHF DEMO: How ChatGPT-Style Alignment Works")
    print("=" * 70)
    print("\nRLHF Pipeline:")
    print("  1. Supervised Fine-Tuning (SFT) - train on demonstrations")
    print("  2. Reward Model Training - learn from human preferences ← SHOWN")
    print("  3. PPO Optimization - maximize learned reward ← SHOWN")
    print("  Alternative: DPO - direct preference optimization ← SHOWN")
    print("\n" + "=" * 70 + "\n")

    # Generate preference data
    print("Generating synthetic preference data...")
    preferences = generate_preference_data(n_samples=1000)
    print(f"✓ Generated {len(preferences)} preference pairs\n")

    # Step 1: Train reward model
    reward_model, rm_losses = train_reward_model(preferences, n_epochs=100)

    # Step 2: Train policy with PPO-RLHF
    policy_rlhf, rlhf_rewards, rlhf_kl = train_policy_with_rlhf(
        reward_model, n_iterations=200
    )

    # Step 3: Train policy with DPO (alternative approach)
    policy_dpo, dpo_losses = train_policy_with_dpo(preferences, n_epochs=100)

    # Visualize
    visualize_results(rm_losses, rlhf_rewards, rlhf_kl, dpo_losses)

    print("=" * 70)
    print("RLHF Demo Complete!")
    print("=" * 70)
    print("\nKey Takeaways:")
    print("  1. Reward models learn from comparisons (Bradley-Terry)")
    print("  2. PPO-RLHF optimizes policy with learned reward + KL penalty")
    print("  3. DPO is simpler alternative (no reward model)")
    print("  4. This is how ChatGPT, Claude, and modern LLMs are aligned!")
    print("\nFor full LLM implementation, see: notebooks/16b_rlhf_practical.ipynb")
    print("=" * 70 + "\n")

    print("✓ Example complete! RLHF concepts demonstrated.")
    print("  This is the MOST IMPORTANT RL technique for 2025-2026! ⭐⭐⭐")
