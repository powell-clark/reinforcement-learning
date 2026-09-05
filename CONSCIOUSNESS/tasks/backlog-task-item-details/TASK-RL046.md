# TASK-RL046: Fix FEAT-RL3 Gymnasium-integration gaps

## Context

4 ACs NOT MET per FEAT-RL3.md verification (TASK-RL042): 0a's custom GridWorld uses the old 4-tuple gym API instead of the modern 5-tuple reset()/step(); tabular lessons (1b FrozenLake, 3b Blackjack) use built-in Gymnasium envs instead of the custom GridWorld, which only appears as a plain non-gym.Env class in 0a; a repo-wide grep found zero gym.register() calls for any custom env (TreasureHuntEnv, SparseMaze, GridWorld); no notebook captures/displays an rgb_array frame, and custom envs render only ASCII or nothing (13b's SparseMaze has no render() at all). Fix: modernize 0a's API, register the custom envs, and add rgb_array rendering.

## Acceptance criteria

- [ ] _(to be filled in)_

## Dependencies

- Directive: DIRECT-RL1
- Features: FEAT-RL3

## Pre-mortem

### Failure modes

- _(to be filled in)_

### Weak assumptions

- _(to be filled in)_
