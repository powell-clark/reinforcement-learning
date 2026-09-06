# TASK-RL057: Fix remaining FEAT-RL1 Colab-runnable gaps

## Context

AC-1/AC-2 partially fixed by TASK-RL044 (7a/7b/9b/13b/X1 install cells). TASK-RL042's verification hedged 'roughly half the 34-notebook curriculum' lacks install cells for gymnasium/SB3/wandb/mujoco imports on a fresh Colab runtime. Fix: repo-wide grep + audit of all 34 notebooks for missing install-cell coverage beyond the 5 already fixed; add install cells where missing; re-execute affected notebooks top-to-bottom.

## Acceptance criteria

- [ ] _(to be filled in)_

## Dependencies

- Directive: DIRECT-RL1
- Features: FEAT-RL1

## Pre-mortem

### Failure modes

- _(to be filled in)_

### Weak assumptions

- _(to be filled in)_
