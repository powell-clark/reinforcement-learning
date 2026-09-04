# TASK-RL36: X4 RL research frontiers

## Context
Deliverable: `notebooks/X4_*.ipynb` for STORY-RL17 (Professional Practice Series). X-series — professional practice. Cross-cutting practitioner skills independent of any single algorithm.

## Acceptance Criteria
- [x] Survey meta-RL, transfer learning, and Sim2Real
- [x] Cover Decision Transformers and transformer-based RL
- [x] Point to resources for staying current

## Cross-cutting Criteria
- [x] Notebook runs top-to-bottom on Google Colab (FEAT-RL1)
- [x] Uses the Gymnasium environment API where an environment is involved (FEAT-RL3)

## Technical Notes
Research orientation. Notebook already existed uncommitted in the working tree with strong
content (algorithm distillation for meta-RL, transfer/Sim2Real discussion, a from-scratch
Decision Transformer on GridWorld, staying-current resources) but Part 3's GridWorld used a
hand-rolled `grid_step` function rather than the Gymnasium API. Wired it through a
`GridWorldEnv(gym.Env)` matching this curriculum's established custom-environment convention
(same shape as `TreasureHuntEnv` in 0b), preserving identical dynamics/rewards. Verified by
executing the notebook top-to-bottom locally (`jupyter nbconvert --execute`, exit 0, no
errors): Meta-RL distilled policy improves within-episode (26%→37% best-arm rate) and nearly
matches the Thompson sampling it was distilled from (11.74 vs 11.64 mean reward, random
baseline 10.28); the Decision Transformer reproduces the conditioned return (100% success at
target=1.0/-3.0, 7% at target=-15.0), matching the notebook's own narrative claims exactly.

## Dependencies
- Blocked by: TASK-RL35
- Blocks: none
- Story: STORY-RL17 (Professional Practice Series)
- Directive: DIRECT-RL1 (Ship complete RL curriculum)
