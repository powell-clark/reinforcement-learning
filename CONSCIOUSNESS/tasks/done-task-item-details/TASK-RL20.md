# TASK-RL20: 9b TRPO PPO practical

## Context
Deliverable: `notebooks/9b_*.ipynb` for STORY-RL10 (Trust Region and PPO). Lesson 9 — stable policy optimization. KL constraints, natural gradients, clipped surrogate objective.

## Acceptance Criteria
- [x] Implement production PPO with Stable-Baselines3
- [x] Use vectorized environments for faster training
- [x] Tune PPO for continuous control

## Cross-cutting Criteria
- [x] Notebook runs top-to-bottom on Google Colab (FEAT-RL1)
- [x] Uses the Gymnasium environment API where an environment is involved (FEAT-RL3)
- [x] Reproduces the algorithm with Stable-Baselines3 alongside the from-scratch version (FEAT-RL2)

## Technical Notes
MuJoCo environments (HalfCheetah, Ant, Humanoid).

## Dependencies
- Blocked by: TASK-RL19
- Blocks: TASK-RL21
- Story: STORY-RL10 (Trust Region and PPO)
- Directive: DIRECT-RL1 (Ship complete RL curriculum)
