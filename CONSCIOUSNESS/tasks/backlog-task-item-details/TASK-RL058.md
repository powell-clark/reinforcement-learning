# TASK-RL058: Fix FEAT-RL2 SB3 comparison gaps

## Context

TASK-RL042 verification: FEAT-RL2 AC-2/AC-3/AC-4 all NOT MET across sampled notebooks 0a/0b/1b/3b/7a/7b/9b/13b/X1. 1b and 3b lack a Stable-Baselines3 comparison against the from-scratch implementation, lack a same-environment side-by-side comparison, and no notebook documents the Gymnasium-vs-SB3 API differences learners need. Fix: add SB3 comparison + same-env comparison cells to 1b/3b, add API-differences documentation.

## Acceptance criteria

- [ ] _(to be filled in)_

## Dependencies

- Directive: DIRECT-RL1
- Features: FEAT-RL2

## Pre-mortem

### Failure modes

- _(to be filled in)_

### Weak assumptions

- _(to be filled in)_
