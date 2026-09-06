# TASK-RL057: Fix remaining FEAT-RL1 Colab-runnable gaps

## Context

AC-1/AC-2 partially fixed by TASK-RL044 (7a/7b/9b/13b/X1 install cells). TASK-RL042's verification hedged 'roughly half the 34-notebook curriculum' lacks install cells for gymnasium/SB3/wandb/mujoco imports on a fresh Colab runtime. Fix: repo-wide grep + audit of all 34 notebooks for missing install-cell coverage beyond the 5 already fixed; add install cells where missing; re-execute affected notebooks top-to-bottom.

## Acceptance criteria

- [ ] Every notebook in the 34-notebook curriculum outside the 5 TASK-RL044 already fixed (7a, 7b, 9b, 13b, X1) is audited for missing install-cell coverage of every third-party import used (gymnasium, torch, stable-baselines3, wandb, mujoco, etc.) on a fresh Colab runtime
- [ ] Each notebook found missing coverage gains a pip-install cell (matching the `subprocess.check_call([sys.executable, '-m', 'pip', 'install', package, '-q'])` pattern already used by the 5 fixed notebooks) placed before first use of the import
- [ ] Every notebook edited for this task is re-executed top-to-bottom with outputs retained, confirming no ModuleNotFoundError or unhandled exception attributable to a missing install
- [ ] FEAT-RL1 AC-1 and AC-2 are updated from PARTIAL to MET (or to a narrower PARTIAL/NOT-MET with named exceptions) citing this task's evidence

## Dependencies

- Directive: DIRECT-RL1
- Features: FEAT-RL1

## Pre-mortem

### Failure modes

- A naive grep for the literal substring "pip install" produces false negatives, since the actual install pattern splits 'pip' and 'install' across separate subprocess.check_call list arguments (discovered during TASK-RL056/RL044 investigation) — the audit must inspect actual import statements per notebook, not grep for install syntax
- A notebook may import a package already preinstalled on Colab's base image (numpy, matplotlib) — flagging those as "missing install cells" would be a false positive; only third-party packages absent from Colab's base image need a cell

### Weak assumptions

- Assumes the Colab base image's preinstalled package set is stable enough that TASK-RL044's precedent (gymnasium, torch, stable-baselines3, wandb, mujoco as needing explicit install) generalizes across the rest of the curriculum without per-notebook Colab verification
