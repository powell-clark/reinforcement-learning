# TASK-RL30: 14b Offline RL practical

## Context
Deliverable: `notebooks/14b_*.ipynb` for STORY-RL15 (Offline RL and Imitation). Lesson 14 — learning from data. Behavioral cloning, IRL, GAIL, and CQL.

## Acceptance Criteria
- [x] Implement behavioral cloning
- [x] Use offline RL libraries
- [x] Combine offline and online RL on the D4RL benchmark

## Cross-cutting Criteria
- [x] Notebook runs top-to-bottom on Google Colab (FEAT-RL1)
- [x] Uses the Gymnasium environment API where an environment is involved (FEAT-RL3)
- [x] Reproduces the algorithm with Stable-Baselines3 alongside the from-scratch version (FEAT-RL2)

## Technical Notes
D4RL datasets. D4RL itself is effectively unmaintained (legacy mujoco-py dependency);
substituted d3rlpy (real, actively-maintained offline RL library: DiscreteBC, DiscreteCQL)
plus a locally-generated dataset built with D4RL's own "medium" recipe (rollouts from a
partially-trained policy) rather than pulling a large remote Minari (D4RL's Farama-maintained
successor) dataset, which would be slow/unreliable inside a notebook execution budget.

## Dependencies
- Blocked by: TASK-RL29
- Blocks: TASK-RL31
- Story: STORY-RL15 (Offline RL and Imitation)
- Directive: DIRECT-RL1 (Ship complete RL curriculum)
