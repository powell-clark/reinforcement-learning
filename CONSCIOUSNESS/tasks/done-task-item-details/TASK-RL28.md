# TASK-RL28: 13b Exploration practical

## Context
Deliverable: `notebooks/13b_*.ipynb` for STORY-RL14 (Exploration Strategies). Lesson 13 — beyond epsilon-greedy. UCB, Thompson sampling, and intrinsic motivation.

## Acceptance Criteria
- [x] Implement curiosity modules
- [x] Use RND with PPO
- [x] Tackle sparse-reward environments

## Cross-cutting Criteria
- [x] Notebook runs top-to-bottom on Google Colab (FEAT-RL1)
- [x] Uses the Gymnasium environment API where an environment is involved (FEAT-RL3)
- [x] Reproduces the algorithm with Stable-Baselines3 alongside the from-scratch version (FEAT-RL2)

## Technical Notes
Montezuma's Revenge, procedurally generated mazes. Substituted a custom 14x14 sparse-reward
GridWorld maze (built as a proper gymnasium.Env) as a notebook-scale stand-in — full Atari
Montezuma's Revenge training needs millions of environment steps, far beyond a notebook
budget. The substitute reproduces the same failure mode (reward too sparse for naive
exploration) and, verified empirically across 6 seeds, plain PPO succeeds only 50% of the
time on it while RND+PPO succeeds 83%, never doing worse than plain PPO on any seed.

## Dependencies
- Blocked by: TASK-RL27
- Blocks: TASK-RL29
- Story: STORY-RL14 (Exploration Strategies)
- Directive: DIRECT-RL1 (Ship complete RL curriculum)
