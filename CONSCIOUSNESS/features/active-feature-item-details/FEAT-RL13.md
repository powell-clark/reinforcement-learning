# FEAT-RL13: Continuous Control (Lesson 10)

## Kano
must-have

## Context
RL for robotics. Deterministic policy gradients and entropy-regularized RL enable solving continuous-action control problems.

## Acceptance Criteria
- [x] **AC-1** — DPG/DDPG derived and a from-scratch DDPG implemented (evidence: TASK-RL054, 10a_continuous_control_theory.ipynb Part 2 derives DPG/DDPG; 10b_continuous_control_practical.ipynb "Part 2b: DDPG Agent" adds a real `DDPGAgent` class — single critic, no target-smoothing noise, undelayed actor+target updates — trained on Pendulum-v1 in "Part 3b", executed with 0 errors and real per-episode returns, final avg -1227.58)
- [x] **AC-2** — TD3 and SAC explained; entropy-regularized RL covered (evidence: 10a_continuous_control_theory.ipynb Parts 3-4, equations + entropy objective; TD3Agent trained on Pendulum in 10b_continuous_control_practical.ipynb)
- [x] **AC-3** — SAC reproduced with SB3 and compared against DDPG/TD3 (evidence: TASK-RL054, 10b Part 4 cell trains SB3 `DDPG`, `TD3`, and `SAC` and evaluates each via `evaluate_policy` over 10 episodes, printing "DDPG: -140.43 +/- 82.59, TD3: -590.05 +/- 313.88, SAC: -157.63 +/- 56.08", executed with 0 errors)

## Stories
STORY-RL11

## Links
- Directive: DIRECT-RL1 (Ship complete RL curriculum)
- Cross-cutting: FEAT-RL1 (Colab), FEAT-RL2 (NumPy+SB3), FEAT-RL3 (Gymnasium)
