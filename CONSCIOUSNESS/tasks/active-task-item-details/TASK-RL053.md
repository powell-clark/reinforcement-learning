# TASK-RL053: Fix FEAT-RL12 PPO gaps

## Context

2 ACs NOT MET per FEAT-RL12.md verification (TASK-RL042): the clipped surrogate objective is derived and implemented, but adaptive KL penalty is never mentioned anywhere in the notebook; 9b's SB3 PPO run on HalfCheetah-v4 is real code but unexecuted, so no output confirms the reproduction. Fix: add adaptive KL penalty coverage and execute the SB3 PPO cell.

Pre-flight (this session) found the second gap already closed: TASK-RL056 (commit `82008af`) fixed a PPOAgent log-prob shape bug and re-executed 9b_ppo_practical.ipynb top-to-bottom, which also executed the previously-unexecuted SB3 PPO cell (cell-12: avg return -0.14 on HalfCheetah-v4, 0 errors). FEAT-RL12.md AC-3 updated to `[x]` citing that evidence. Only the adaptive-KL-penalty gap (AC-2) remains live — confirmed by direct inspection, no mention of an adaptive/penalty KL variant anywhere in 9a or 9b. Scope narrowed to that gap alone.

## Acceptance criteria

- [x] **AC-1** — 9a_trpo_ppo_theory.ipynb gains a markdown derivation of the adaptive KL-penalty PPO variant (PPO-Penalty): the objective $L^{KLPEN}(\theta) = \mathbb{E}[r_t(\theta)A_t] - \beta \cdot \mathrm{KL}[\pi_{old} \| \pi_\theta]$ and the adaptation rule for $\beta$ against a target KL. Evidence: new markdown cell (index 9, "Part 4b: PPO-Penalty (Adaptive KL Penalty Variant)") inserted after the `PPOObjective` cell.
- [x] **AC-2** — 9a_trpo_ppo_theory.ipynb gains a code cell implementing the adaptive-KL objective and its $\beta$-adaptation step, analogous in style to the existing `PPOObjective` class. Evidence: new code cell (index 10) defines `AdaptiveKLPPOObjective` (`kl_penalty_loss`, `update_beta`, `value_loss`, `entropy_bonus`, `total_loss`), executed with exec_count=4, 0 errors, output demonstrates β adapting 1.0→0.5→1.0→1.0→2.0 across 4 measured-KL steps.
- [x] **AC-3** — The TRPO vs PPO comparison table (or adjoining text) in 9a distinguishes the two PPO variants (clip vs adaptive-KL-penalty) so a reader can see the notebook now covers both. Evidence: "Part 5" table (index 11) now has separate PPO-Clip / PPO-Penalty columns plus a paragraph naming both variants and citing Part 3 / Part 4b.
- [x] **AC-4** — 9a_trpo_ppo_theory.ipynb executed top-to-bottom (`jupyter nbconvert --execute --inplace`) with 0 error cells. Evidence: `jupyter nbconvert --to notebook --execute --inplace notebooks/9a_trpo_ppo_theory.ipynb` completed; all 4 code cells (indices 2,6,8,10) show non-null execution_count and 0 error outputs (verified via nbformat inspection).
- [x] **AC-5** — FEAT-RL12.md AC-2 updated to `[x]` citing this task and the new cells as evidence.

## Dependencies

- Directive: DIRECT-RL1
- Story: STORY-RL10
- Features: FEAT-RL12

## Pre-mortem

### Failure modes

- _(to be filled in)_

### Weak assumptions

- _(to be filled in)_
