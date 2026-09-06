# TASK-RL059: Fix FEAT-RL3 gym API and registration gaps

## Context

TASK-RL042 verification: FEAT-RL3 AC-1/AC-2/AC-3 all NOT MET. AC-1: 0a's custom GridWorld uses the old 4-tuple gym API (bare-state reset(), 4-tuple step()) instead of the modern 5-tuple API used from 0b onward; render() is essentially unused across the sample. AC-2: tabular lessons 1b/3b use built-in FrozenLake/Blackjack rather than the custom GridWorld, which appears only as a non-gym.Env class in 0a. AC-3: a repo-wide grep across all 34 notebooks found zero gym.register()/registry calls for TreasureHuntEnv, SparseMaze, or GridWorld. Fix: migrate 0a's GridWorld to the 5-tuple API and make it a proper gym.Env subclass, register it (and TreasureHuntEnv/SparseMaze) via gym.register(), and use the registered GridWorld in at least one tabular lesson.

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
