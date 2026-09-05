# TASK-RL047: Fix FEAT-RL4 MDP theory gaps

## Context

2 ACs NOT MET per FEAT-RL4.md verification (TASK-RL042): Bellman expectation/optimality equations are presented as given formulas, never derived step by step from the return definition G_t; MDPSolver.value_iteration() in 1a_mdp_theory.ipynb has no stored execution output, so there is no evidence it was ever run. Fix: add the step-by-step derivation and execute the solver cell with output retained.

## Acceptance criteria

- [ ] _(to be filled in)_

## Dependencies

- Directive: DIRECT-RL1
- Story: STORY-RL2
- Features: FEAT-RL4

## Pre-mortem

### Failure modes

- _(to be filled in)_

### Weak assumptions

- _(to be filled in)_
