# FEAT-RL12: Trust Region and PPO (Lesson 9)

## Kano
must-have

## Context
Stable policy optimization. KL constraints, natural gradients, and the clipped surrogate objective make PPO the industry standard.

## Acceptance Criteria
- [x] **AC-1** — TRPO and KL-constrained/natural policy gradients explained (evidence: 9a_trpo_ppo_theory.ipynb, TRPO KL-constraint / conjugate-gradient section)
- [ ] **AC-2** — PPO clipped surrogate objective and adaptive KL penalty derived — NOT MET: the clipped surrogate is derived and implemented (ppo_clip/PPOObjective), but adaptive KL penalty is never mentioned anywhere in the notebook.
- [ ] **AC-3** — Production PPO reproduced with SB3 on continuous control — NOT MET: 9b's SB3 PPO run on HalfCheetah-v4 is real code but unexecuted; no output confirms reproduction.

## Stories
STORY-RL10

## Links
- Directive: DIRECT-RL1 (Ship complete RL curriculum)
- Cross-cutting: FEAT-RL1 (Colab), FEAT-RL2 (NumPy+SB3), FEAT-RL3 (Gymnasium)
