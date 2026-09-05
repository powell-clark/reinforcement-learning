# TASK-RL044: Fix FEAT-RL1 Colab-runnable gaps

## Context

4 ACs NOT MET per FEAT-RL1.md verification (TASK-RL042): 7a/7b/9b/13b/X1 import gymnasium/SB3/wandb/mujoco with no install cell, hitting ModuleNotFoundError on a fresh Colab runtime; pip-install cell present in 0a/0b/1b/3b but absent in 7a/7b/9b/13b/X1 (9b's SB3 import only prints an install hint on failure); no notebook captures/displays an environment rgb_array render frame; no notebook exposes a reduced-timestep quick-run toggle for long training cells (7b, 13b, X1 all hardcode full-size runs). Fix: add install cells, an rgb_array render+display example, and a quick-run parameter to the affected notebooks.

## Acceptance criteria

- [ ] Notebooks 7a, 7b, 9b, 13b, and X1 each carry a pip-install cell (matching the pattern already used in 0a/0b/1b/3b) covering every third-party import they use (gymnasium, stable-baselines3, wandb, mujoco as applicable), placed before the first cell that imports it
- [ ] 9b's stable-baselines3 import no longer silently degrades to a print-only install hint on failure — it either installs inline or raises clearly
- [ ] At least one notebook in the curriculum executes an environment render in `rgb_array` mode and displays the captured frame inline (e.g. via matplotlib imshow) with retained cell output
- [ ] Each of 7b, 13b, and X1 exposes a reduced-timestep "quick-run" parameter (e.g. a `QUICK_RUN` flag or reduced `total_timesteps`/`n_episodes` constant near the top of the notebook) that lets the long training cell complete in under a minute for smoke-testing, without deleting the full-size run
- [ ] Every notebook edited for this task is re-executed top-to-bottom with outputs retained, confirming no ModuleNotFoundError or unhandled exception

## Dependencies

- Directive: DIRECT-RL1
- Features: FEAT-RL1

## Pre-mortem

### Failure modes

- Adding install cells without pinning versions could break on a future Colab base image with a newer conflicting package — mitigate by matching version pins already used elsewhere in the repo (e.g. requirements.txt or 0a/0b's install cell) rather than inventing new ones
- A quick-run toggle left defaulted to "on" would silently ship under-trained results as if they were the full run — default it to off/full-size and document the flag inline
- Re-executing 13b's SparseMaze or other custom envs top-to-bottom may surface the pre-existing FEAT-RL3 gaps (no rgb_array render, old gym API) as execution errors unrelated to this task's scope — if so, scope this task's fix narrowly to install/quick-run/one rgb_array example and file any newly discovered execution failures as their own task rather than silently expanding scope

### Weak assumptions

- Assumes Colab's base image does not already ship gymnasium/SB3/wandb/mujoco preinstalled for every notebook — TASK-RL042's verification found ModuleNotFoundError risk specifically because it does not
- Assumes "at least one notebook" with an rgb_array render satisfies FEAT-RL1's AC as written; if the feature card intends broader rgb_array coverage across most notebooks, that is out of scope here and should be a separate follow-up
