# TASK-RL055: Fix FEAT-RL15 multi-agent RL gaps

## Context

1 AC NOT MET per FEAT-RL15.md verification (TASK-RL042): independent Q-learning is genuinely trained (RPS via PettingZoo), but CTDE is only an untrained toy sketch in the theory notebook, and the practical notebook implements parameter-sharing explicitly labeled 'CTDE-adjacent,' not a trained centralized-critic/decentralized-actor loop. Fix: implement a genuine trained CTDE (centralized-critic, decentralized-actor) example.

## Acceptance criteria

- [x] **AC-1** — 12b_marl_practical.ipynb gains a genuine trained CTDE implementation: separately-parameterized per-agent decentralized actors (no weight sharing, local observation only) plus a centralized critic that sees the joint observation during training only — a real algorithm with gradient updates, not a static toy sketch. Evidence: cell-11, `DecentralizedActor`/`CentralizedCritic` classes, per-step TD(0) bootstrapped advantage actor-critic with real `.backward()`/`.step()` gradient updates for the critic and each of the 2 actors, 500 episodes.
- [x] **AC-2** — The CTDE implementation trains on the same cooperative Pursuit task used by the existing parameter-sharing baseline (pursuit_v4, same env config), with real per-episode team-return output demonstrating learning (first-10 vs last-10 episode comparison). Evidence: `pursuit_v4.parallel_env(n_pursuers=2, n_evaders=2, x_size=10, y_size=10, max_cycles=100, n_catch=1, surround=False)` (identical to cell-8's baseline config); printed output "CTDE -- First 10 episodes mean team return: -10.0" / "CTDE -- Last 10 episodes mean team return: -6.4" — a genuine, directional improvement after 3 prior attempts (whole-episode REINFORCE untuned, whole-episode REINFORCE tuned, per-step TD actor-critic at 100 episodes) all showed flat/no learning. Root cause of the earlier failures was a sample-efficiency gap versus the notebook's own on-policy control (SB3 PPO needs ~600 episode-equivalents for partial improvement at the same entropy coefficient); scaling `ctde_n_episodes` 100->500 and `ctde_entropy_coef` 0.01->0.02 closed enough of that gap to show real learning.
- [x] **AC-3** — 12b_marl_practical.ipynb executed top-to-bottom (`jupyter nbconvert --execute --inplace`) with 0 error cells. Evidence: `verify_12b.py` output "Total code cells: 8" / "PASS: all code cells executed with execution_count set and zero error outputs" after the final run (nbconvert exit code 0).
- [x] **AC-4** — FEAT-RL15.md AC-2 updated to `[x]` citing this task and the new CTDE cells/output as evidence.

## Dependencies

- Directive: DIRECT-RL1
- Story: STORY-RL13
- Features: FEAT-RL15

## Pre-mortem

### Failure modes

- _(to be filled in)_

### Weak assumptions

- _(to be filled in)_
