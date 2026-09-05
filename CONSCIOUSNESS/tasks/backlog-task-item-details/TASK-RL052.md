# TASK-RL052: Fix FEAT-RL11 policy-gradient gaps

## Context

2 ACs NOT MET per FEAT-RL11.md verification (TASK-RL042): 8a states the policy gradient theorem's final formula with a one-line intuition but shows no derivation steps from J(theta) to the gradient expression; 8b's SB3 A2C comparison is unexecuted and calls LunarLander-v2 (discrete default) with a continuous Normal policy, a likely runtime bug. Fix: add the derivation and fix+execute the A2C comparison cell.

## Acceptance criteria

- [ ] _(to be filled in)_

## Dependencies

- Directive: DIRECT-RL1
- Story: STORY-RL9
- Features: FEAT-RL11

## Pre-mortem

### Failure modes

- _(to be filled in)_

### Weak assumptions

- _(to be filled in)_
