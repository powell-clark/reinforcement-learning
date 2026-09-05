# FEAT-RL11: Policy Gradient Methods (Lesson 8)

## Kano
must-have

## Context
Directly optimizing policies. The policy gradient theorem, REINFORCE, and Actor-Critic algorithms enable learning on continuous action spaces.

## Acceptance Criteria
- [x] **AC-1** — Policy gradient theorem derived (evidence: TASK-RL052, 8a_policy_gradients_theory.ipynb cell-3 now carries a 4-step derivation from $J(\theta)=\mathbb{E}[R(\tau)]$ through the log-derivative trick, factoring out environment dynamics, and the causal $Q^\pi$ substitution, to the policy gradient theorem)
- [x] **AC-2** — REINFORCE and Actor-Critic implemented from scratch (evidence: 8a_policy_gradients_theory.ipynb, reinforce_with_baseline function and ActorCritic class)
- [x] **AC-3** — Baselines and the advantage function A(s,a)=Q-V explained; SB3 A2C reproduced (evidence: TASK-RL052, 8b_policy_gradients_practical.ipynb cells 8/10 fixed to `gym.make('LunarLander-v3', continuous=True)` and executed: from-scratch A2C cell exec_count=4 with real training returns, SB3 A2C comparison cell exec_count=5 returning avg -33.71, both 0 errors)

## Stories
STORY-RL9

## Links
- Directive: DIRECT-RL1 (Ship complete RL curriculum)
- Cross-cutting: FEAT-RL1 (Colab), FEAT-RL2 (NumPy+SB3), FEAT-RL3 (Gymnasium)
