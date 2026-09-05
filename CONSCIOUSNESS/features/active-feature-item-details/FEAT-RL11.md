# FEAT-RL11: Policy Gradient Methods (Lesson 8)

## Kano
must-have

## Context
Directly optimizing policies. The policy gradient theorem, REINFORCE, and Actor-Critic algorithms enable learning on continuous action spaces.

## Acceptance Criteria
- [ ] **AC-1** — Policy gradient theorem derived — NOT MET: 8a states the theorem's final formula and a one-line intuition but shows no derivation steps from J(θ) to the gradient expression.
- [x] **AC-2** — REINFORCE and Actor-Critic implemented from scratch (evidence: 8a_policy_gradients_theory.ipynb, reinforce_with_baseline function and ActorCritic class)
- [ ] **AC-3** — Baselines and the advantage function A(s,a)=Q-V explained; SB3 A2C reproduced — NOT MET: baseline/advantage is explained in 8a, but 8b's SB3 A2C comparison is unexecuted (and calls LunarLander-v2 with its default discrete action space while using a continuous Normal policy, a likely runtime bug).

## Stories
STORY-RL9

## Links
- Directive: DIRECT-RL1 (Ship complete RL curriculum)
- Cross-cutting: FEAT-RL1 (Colab), FEAT-RL2 (NumPy+SB3), FEAT-RL3 (Gymnasium)
