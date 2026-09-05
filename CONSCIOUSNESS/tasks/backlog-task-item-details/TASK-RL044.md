# TASK-RL044: Fix FEAT-RL1 Colab-runnable gaps

## Context

4 ACs NOT MET per FEAT-RL1.md verification (TASK-RL042): 7a/7b/9b/13b/X1 import gymnasium/SB3/wandb/mujoco with no install cell, hitting ModuleNotFoundError on a fresh Colab runtime; pip-install cell present in 0a/0b/1b/3b but absent in 7a/7b/9b/13b/X1 (9b's SB3 import only prints an install hint on failure); no notebook captures/displays an environment rgb_array render frame; no notebook exposes a reduced-timestep quick-run toggle for long training cells (7b, 13b, X1 all hardcode full-size runs). Fix: add install cells, an rgb_array render+display example, and a quick-run parameter to the affected notebooks.

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
