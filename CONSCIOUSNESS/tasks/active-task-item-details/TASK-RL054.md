# TASK-RL054: Fix FEAT-RL13 continuous-control gaps

## Context

2 ACs NOT MET per FEAT-RL13.md verification (TASK-RL042): DDPG appears only as unrunnable pseudocode (undefined helpers like mse_loss/soft_update) — only TD3 is actually implemented and trained from scratch; 10b Part 4 trains TD3 and SAC briefly via SB3 but never DDPG, and prints no comparison metric. Fix: implement a real from-scratch DDPG and add a DDPG/TD3/SAC comparison with metrics.

## Acceptance criteria

- [ ] **AC-1** — 10b_continuous_control_practical.ipynb gains a from-scratch `DDPGAgent` class (single critic, no target-policy smoothing, no delayed actor update — the actual DDPG update rule), analogous in style to the existing `TD3Agent`.
- [ ] **AC-2** — 10b trains `DDPGAgent` on Pendulum-v1 with a training loop analogous to the TD3 training loop, executed with real per-episode return output.
- [ ] **AC-3** — 10b Part 4 (SB3 validation) extended to also train SB3's `DDPG` alongside `TD3` and `SAC`, and prints a comparison metric (mean evaluation return per algorithm over several episodes, via `evaluate_policy` or equivalent) rather than just "trained and validated".
- [ ] **AC-4** — 10b_continuous_control_practical.ipynb executed top-to-bottom (`jupyter nbconvert --execute --inplace`) with 0 error cells.
- [ ] **AC-5** — FEAT-RL13.md AC-1 and AC-3 updated to `[x]` citing this task and the new cells/output as evidence.

## Dependencies

- Directive: DIRECT-RL1
- Story: STORY-RL11
- Features: FEAT-RL13

## Pre-mortem

### Failure modes

- _(to be filled in)_

### Weak assumptions

- _(to be filled in)_
