# TASK-RL050: Fix FEAT-RL8 eligibility-trace gaps

## Context

2 ACs NOT MET per FEAT-RL8.md verification (TASK-RL042): n-step returns/TD/Sarsa appear only as formulas in 5a_nstep_eligibility.ipynb — both notebooks jump straight to eligibility-trace (lambda) code with no literal n-step update ever implemented; the forward/backward-view equivalence is only asserted ('The Key Theorem') with no derivation or empirical comparison, and only the backward view is implemented. Fix: implement literal n-step TD/Sarsa and add a derivation or empirical equivalence check.

## Acceptance criteria

- [ ] _(to be filled in)_

## Dependencies

- Directive: DIRECT-RL1
- Story: STORY-RL6
- Features: FEAT-RL8

## Pre-mortem

### Failure modes

- _(to be filled in)_

### Weak assumptions

- _(to be filled in)_
