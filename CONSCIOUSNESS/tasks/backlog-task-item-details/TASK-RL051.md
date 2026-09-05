# TASK-RL051: Fix FEAT-RL10 DQN execution gaps

## Context

2 ACs NOT MET per FEAT-RL10.md verification (TASK-RL042): the from-scratch DQN/training-loop code is real but the notebook has zero executed cells, so nothing confirms it trains or converges; the SB3-vs-from-scratch DQN comparison in 7b was never executed. Fix: run both notebooks end-to-end and retain output evidence of convergence and the comparison.

## Acceptance criteria

- [ ] _(to be filled in)_

## Dependencies

- Directive: DIRECT-RL1
- Story: STORY-RL8
- Features: FEAT-RL10

## Pre-mortem

### Failure modes

- _(to be filled in)_

### Weak assumptions

- _(to be filled in)_
