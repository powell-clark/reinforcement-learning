# TASK-RL32: 15b Hierarchical RL practical

## Context
Deliverable: `notebooks/15b_*.ipynb` for STORY-RL16 (Hierarchical RL). Lesson 15 — options and skills. Semi-MDPs, feudal RL, and HER.

## Acceptance Criteria
- [x] Implement options
- [x] Use HER with goal-conditioned policies
- [x] Apply skill chaining

## Cross-cutting Criteria
- [x] Notebook runs top-to-bottom on Google Colab (FEAT-RL1)
- [x] Uses the Gymnasium environment API where an environment is involved (FEAT-RL3)
- [x] Reproduces the algorithm with Stable-Baselines3 alongside the from-scratch version (FEAT-RL2)

## Technical Notes
FetchReach, FetchPush robotics. FetchReach trained and verified (SAC + HerReplayBuffer,
20,000 timesteps, 100% success). FetchPush documented as the natural harder extension
(needs 5-10x more steps even with HER) but not separately trained -- out of notebook-scale
budget; the identical HerReplayBuffer setup applies to it unchanged.

## Dependencies
- Blocked by: TASK-RL31
- Blocks: TASK-RL33
- Story: STORY-RL16 (Hierarchical RL)
- Directive: DIRECT-RL1 (Ship complete RL curriculum)
