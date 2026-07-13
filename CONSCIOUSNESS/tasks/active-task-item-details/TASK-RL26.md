# TASK-RL26: 12b MARL practical

## Context
Deliverable: `notebooks/12b_*.ipynb` for STORY-RL13 (Multi-Agent RL). Lesson 12 — multiple agents. CTDE, Nash equilibria, and credit assignment.

## Acceptance Criteria
- [x] Use PettingZoo environments
- [x] Implement multi-agent training loops
- [x] Run cooperative navigation and competitive games

## Cross-cutting Criteria
- [x] Notebook runs top-to-bottom on Google Colab (FEAT-RL1)
- [x] Uses the Gymnasium environment API where an environment is involved (FEAT-RL3) — PettingZoo per-agent spaces are gymnasium.spaces; the SB3 section bridges to a real Gym-API VecEnv via SuperSuit
- [x] Reproduces the algorithm with Stable-Baselines3 alongside the from-scratch version (FEAT-RL2)

## Technical Notes
PettingZoo API. MPE's `simple_spread` ("cooperative navigation") is no longer bundled with
core PettingZoo (>=1.25 dropped the `mpe` extra) — substituted `sisl.pursuit_v4` as the
cooperative task, `classic.rps_v2` as the competitive one.

## Dependencies
- Blocked by: TASK-RL25
- Blocks: TASK-RL27
- Story: STORY-RL13 (Multi-Agent RL)
- Directive: DIRECT-RL1 (Ship complete RL curriculum)
