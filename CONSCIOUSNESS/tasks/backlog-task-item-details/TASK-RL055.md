# TASK-RL055: Fix FEAT-RL15 multi-agent RL gaps

## Context

1 AC NOT MET per FEAT-RL15.md verification (TASK-RL042): independent Q-learning is genuinely trained (RPS via PettingZoo), but CTDE is only an untrained toy sketch in the theory notebook, and the practical notebook implements parameter-sharing explicitly labeled 'CTDE-adjacent,' not a trained centralized-critic/decentralized-actor loop. Fix: implement a genuine trained CTDE (centralized-critic, decentralized-actor) example.

## Acceptance criteria

- [ ] _(to be filled in)_

## Dependencies

- Directive: DIRECT-RL1
- Story: STORY-RL13
- Features: FEAT-RL15

## Pre-mortem

### Failure modes

- _(to be filled in)_

### Weak assumptions

- _(to be filled in)_
