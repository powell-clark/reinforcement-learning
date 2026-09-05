# TASK-RL054: Fix FEAT-RL13 continuous-control gaps

## Context

2 ACs NOT MET per FEAT-RL13.md verification (TASK-RL042): DDPG appears only as unrunnable pseudocode (undefined helpers like mse_loss/soft_update) — only TD3 is actually implemented and trained from scratch; 10b Part 4 trains TD3 and SAC briefly via SB3 but never DDPG, and prints no comparison metric. Fix: implement a real from-scratch DDPG and add a DDPG/TD3/SAC comparison with metrics.

## Acceptance criteria

- [ ] _(to be filled in)_

## Dependencies

- Directive: DIRECT-RL1
- Story: STORY-RL11
- Features: FEAT-RL13

## Pre-mortem

### Failure modes

- _(to be filled in)_

### Weak assumptions

- _(to be filled in)_
