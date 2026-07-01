# TASK-RL11: 5a N-step eligibility theory

## Context
Deliverable: `notebooks/5a_*.ipynb` for STORY-RL6 (N-Step and Eligibility Traces). Lesson 5 — beyond one-step TD. TD(lambda) and the forward/backward view equivalence.

## Acceptance Criteria
- [ ] Derive n-step TD prediction and n-step Sarsa
- [ ] Present the forward and backward views of eligibility traces
- [ ] Show the forward/backward equivalence for TD(lambda)
- [ ] Implement Sarsa(lambda) from scratch

## Cross-cutting Criteria
- [ ] Notebook runs top-to-bottom on Google Colab (FEAT-RL1)
- [ ] Uses the Gymnasium environment API where an environment is involved (FEAT-RL3)
- [ ] Includes a from-scratch implementation of the core algorithm (FEAT-RL2)

## Technical Notes
RandomWalk isolates the prediction problem cleanly.

## Dependencies
- Story: STORY-RL6 (N-Step and Eligibility Traces)
- Directive: DIRECT-RL1 (Ship complete RL curriculum)
