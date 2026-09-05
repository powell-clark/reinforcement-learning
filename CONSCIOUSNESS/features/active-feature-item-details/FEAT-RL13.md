# FEAT-RL13: Continuous Control (Lesson 10)

## Kano
must-have

## Context
RL for robotics. Deterministic policy gradients and entropy-regularized RL enable solving continuous-action control problems.

## Acceptance Criteria
- [ ] **AC-1** — DPG/DDPG derived and a from-scratch DDPG implemented — NOT MET: DDPG appears only as unrunnable pseudocode (undefined helpers like mse_loss/soft_update); only TD3 is actually implemented and trained from scratch.
- [x] **AC-2** — TD3 and SAC explained; entropy-regularized RL covered (evidence: 10a_continuous_control_theory.ipynb Parts 3-4, equations + entropy objective; TD3Agent trained on Pendulum in 10b_continuous_control_practical.ipynb)
- [ ] **AC-3** — SAC reproduced with SB3 and compared against DDPG/TD3 — NOT MET: 10b Part 4 trains TD3 and SAC briefly via SB3 but never DDPG, and prints no comparison metric (no returns, no plot).

## Stories
STORY-RL11

## Links
- Directive: DIRECT-RL1 (Ship complete RL curriculum)
- Cross-cutting: FEAT-RL1 (Colab), FEAT-RL2 (NumPy+SB3), FEAT-RL3 (Gymnasium)
