# TASK-RL055: Fix FEAT-RL15 multi-agent RL gaps

## Context

1 AC NOT MET per FEAT-RL15.md verification (TASK-RL042): independent Q-learning is genuinely trained (RPS via PettingZoo), but CTDE is only an untrained toy sketch in the theory notebook, and the practical notebook implements parameter-sharing explicitly labeled 'CTDE-adjacent,' not a trained centralized-critic/decentralized-actor loop. Fix: implement a genuine trained CTDE (centralized-critic, decentralized-actor) example.

## Acceptance criteria

- [ ] **AC-1** — 12b_marl_practical.ipynb gains a genuine trained CTDE implementation: separately-parameterized per-agent decentralized actors (no weight sharing, local observation only) plus a centralized critic that sees the joint observation during training only — a real algorithm with gradient updates, not a static toy sketch.
- [ ] **AC-2** — The CTDE implementation trains on the same cooperative Pursuit task used by the existing parameter-sharing baseline (pursuit_v4, same env config), with real per-episode team-return output demonstrating learning (first-10 vs last-10 episode comparison).
- [ ] **AC-3** — 12b_marl_practical.ipynb executed top-to-bottom (`jupyter nbconvert --execute --inplace`) with 0 error cells.
- [ ] **AC-4** — FEAT-RL15.md AC-2 updated to `[x]` citing this task and the new CTDE cells/output as evidence.

## Dependencies

- Directive: DIRECT-RL1
- Story: STORY-RL13
- Features: FEAT-RL15

## Pre-mortem

### Failure modes

- _(to be filled in)_

### Weak assumptions

- _(to be filled in)_
