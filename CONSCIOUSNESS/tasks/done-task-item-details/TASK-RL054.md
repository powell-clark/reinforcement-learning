# TASK-RL054: Fix FEAT-RL13 continuous-control gaps

## Context

2 ACs NOT MET per FEAT-RL13.md verification (TASK-RL042): DDPG appears only as unrunnable pseudocode (undefined helpers like mse_loss/soft_update) — only TD3 is actually implemented and trained from scratch; 10b Part 4 trains TD3 and SAC briefly via SB3 but never DDPG, and prints no comparison metric. Fix: implement a real from-scratch DDPG and add a DDPG/TD3/SAC comparison with metrics.

## Acceptance criteria

- [x] **AC-1** — 10b_continuous_control_practical.ipynb gains a from-scratch `DDPGAgent` class (single critic, no target-policy smoothing, no delayed actor update — the actual DDPG update rule), analogous in style to the existing `TD3Agent`. Evidence: new markdown cell "Part 2b: DDPG Agent" + code cell (index 8, exec_count=4) defining `DDPGAgent` — single `critic`/`critic_target` (no twin), `update()` uses the raw `actor_target(next_states_t)` with no smoothing noise, and calls `_soft_update` on every `update()` call (no delay gate), reusing the same `_build_network`/`select_action`/`_soft_update` shape as `TD3Agent`.
- [x] **AC-2** — 10b trains `DDPGAgent` on Pendulum-v1 with a training loop analogous to the TD3 training loop, executed with real per-episode return output. Evidence: new markdown cell "Part 3b: Training DDPG on Pendulum" + code cell (index 12, exec_count=6) mirrors the TD3 training loop (cell index 10) structurally; executed output shows real per-episode returns (Episode 5: -1162.99, 10: -1207.47, 15: -1726.83, 20: -1391.72, final avg -1227.58).
- [x] **AC-3** — 10b Part 4 (SB3 validation) extended to also train SB3's `DDPG` alongside `TD3` and `SAC`, and prints a comparison metric (mean evaluation return per algorithm over several episodes, via `evaluate_policy` or equivalent) rather than just "trained and validated". Evidence: cell index 14 (exec_count=7) trains all three via SB3, evaluates each with `evaluate_policy(n_eval_episodes=10)`, and prints "Algorithm comparison (mean return over 10 eval episodes on Pendulum-v1): DDPG: -140.43 +/- 82.59, TD3: -590.05 +/- 313.88, SAC: -157.63 +/- 56.08".
- [x] **AC-4** — 10b_continuous_control_practical.ipynb executed top-to-bottom (`jupyter nbconvert --execute --inplace`) with 0 error cells. Evidence: `jupyter nbconvert --to notebook --execute --inplace` exited 0; all 7 code cells (indices 2,4,6,8,10,12,14) show non-null execution_count and 0 error outputs (verified via nbformat inspection script).
- [x] **AC-5** — FEAT-RL13.md AC-1 and AC-3 updated to `[x]` citing this task and the new cells/output as evidence.

## Dependencies

- Directive: DIRECT-RL1
- Story: STORY-RL11
- Features: FEAT-RL13

## Pre-mortem

### Failure modes

- _(to be filled in)_

### Weak assumptions

- _(to be filled in)_
