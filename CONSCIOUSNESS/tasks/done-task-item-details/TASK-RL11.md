# TASK-RL11: 5a N-step eligibility theory

## Context
Deliverable: `notebooks/5a_*.ipynb` for STORY-RL6 (N-Step and Eligibility Traces). Lesson 5 — beyond one-step TD. TD(lambda) and the forward/backward view equivalence.

## Acceptance Criteria
- [x] Derive n-step TD prediction and n-step Sarsa
- [x] Present the forward and backward views of eligibility traces
- [x] Show the forward/backward equivalence for TD(lambda)
- [x] Implement Sarsa(lambda) from scratch

## Cross-cutting Criteria
- [x] Notebook runs top-to-bottom on Google Colab (FEAT-RL1)
- [x] Uses the Gymnasium environment API where an environment is involved (FEAT-RL3)
- [x] Includes a from-scratch implementation of the core algorithm (FEAT-RL2)

## Technical Notes
RandomWalk isolates the prediction problem cleanly.

## Dependencies
- Blocked by: TASK-RL10
- Blocks: TASK-RL12
- Story: STORY-RL6 (N-Step and Eligibility Traces)
- Directive: DIRECT-RL1 (Ship complete RL curriculum)
