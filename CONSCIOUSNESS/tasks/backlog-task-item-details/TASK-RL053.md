# TASK-RL053: Fix FEAT-RL12 PPO gaps

## Context

2 ACs NOT MET per FEAT-RL12.md verification (TASK-RL042): the clipped surrogate objective is derived and implemented, but adaptive KL penalty is never mentioned anywhere in the notebook; 9b's SB3 PPO run on HalfCheetah-v4 is real code but unexecuted, so no output confirms the reproduction. Fix: add adaptive KL penalty coverage and execute the SB3 PPO cell.

## Acceptance criteria

- [ ] _(to be filled in)_

## Dependencies

- Directive: DIRECT-RL1
- Story: STORY-RL10
- Features: FEAT-RL12

## Pre-mortem

### Failure modes

- _(to be filled in)_

### Weak assumptions

- _(to be filled in)_
