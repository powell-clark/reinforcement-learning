# FEAT-RL12: Trust Region and PPO (Lesson 9)

## Kano
must-have

## Context
Stable policy optimization. KL constraints, natural gradients, and the clipped surrogate objective make PPO the industry standard.

## Acceptance Criteria
- [x] **AC-1** — TRPO and KL-constrained/natural policy gradients explained (evidence: 9a_trpo_ppo_theory.ipynb, TRPO KL-constraint / conjugate-gradient section)
- [x] **AC-2** — PPO clipped surrogate objective and adaptive KL penalty derived (evidence: TASK-RL053, 9a_trpo_ppo_theory.ipynb "Part 4b: PPO-Penalty" markdown cell derives $L^{KLPEN}$ and the β-adaptation rule; `AdaptiveKLPPOObjective` code cell implements it, executed with 0 errors, β adapts 1.0→0.5→1.0→1.0→2.0 across 4 demo steps; Part 5 comparison table updated to cover both PPO-Clip and PPO-Penalty variants)
- [x] **AC-3** — Production PPO reproduced with SB3 on continuous control (evidence: TASK-RL056, 9b_ppo_practical.ipynb cell-12 executed, SB3 `PPO` on HalfCheetah-v4, avg return -0.14 over 3 eval episodes, 0 errors; from-scratch PPO cell-10 also executes, avg return -672.62)

## Stories
STORY-RL10

## Links
- Directive: DIRECT-RL1 (Ship complete RL curriculum)
- Cross-cutting: FEAT-RL1 (Colab), FEAT-RL2 (NumPy+SB3), FEAT-RL3 (Gymnasium)
