# TASK-RL045: Fix FEAT-RL2 dual-implementation gaps

## Context

3 ACs NOT MET per FEAT-RL2.md verification (TASK-RL042): 1b imports SB3 but never trains/compares it ('this is a preview'); 3b has no SB3 or equivalent-framework usage for MC control; only 7b (and conditionally 9b) actually runs a from-scratch-vs-SB3 comparison on the same environment; no notebook in the sampled set (0a,0b,1b,3b,7a,7b,9b,13b,X1) documents API differences between the custom implementation and SB3's API. Fix: add real SB3 training+comparison to 1b and 3b, and an API-differences section to at least one representative notebook.

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
