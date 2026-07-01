# TASK-RL12: 5b N-step eligibility practical

## Context
Deliverable: `notebooks/5b_*.ipynb` for STORY-RL6 (N-Step and Eligibility Traces). Lesson 5 — beyond one-step TD. TD(lambda) and the forward/backward view equivalence.

## Acceptance Criteria
- [x] Implement eligibility traces efficiently
- [x] Explore choices of lambda and n and trace-decay mechanisms
- [x] Apply to MountainCar

## Cross-cutting Criteria
- [x] Notebook runs top-to-bottom on Google Colab (FEAT-RL1)
- [x] Uses the Gymnasium environment API where an environment is involved (FEAT-RL3)
- [x] Reproduces the algorithm with Stable-Baselines3 alongside the from-scratch version (FEAT-RL2)

## Technical Notes
MountainCar introduces the need for function approximation next.

## Dependencies
- Blocked by: TASK-RL11
- Blocks: TASK-RL13
- Story: STORY-RL6 (N-Step and Eligibility Traces)
- Directive: DIRECT-RL1 (Ship complete RL curriculum)
