# TASK-RL19: 9a TRPO PPO theory

## Context
Deliverable: `notebooks/9a_*.ipynb` for STORY-RL10 (Trust Region and PPO). Lesson 9 — stable policy optimization. KL constraints, natural gradients, clipped surrogate objective.

## Acceptance Criteria
- [ ] Explain why large policy updates are unstable
- [ ] Derive TRPO with KL-divergence constraints and natural gradients
- [ ] Derive PPO's clipped surrogate objective and adaptive KL penalty
- [ ] Explain why PPO became the standard

## Cross-cutting Criteria
- [ ] Notebook runs top-to-bottom on Google Colab (FEAT-RL1)
- [ ] Uses the Gymnasium environment API where an environment is involved (FEAT-RL3)
- [ ] Includes a from-scratch implementation of the core algorithm (FEAT-RL2)

## Technical Notes
MuJoCo continuous-control framing.

## Dependencies
- Story: STORY-RL10 (Trust Region and PPO)
- Directive: DIRECT-RL1 (Ship complete RL curriculum)
