# TASK-RL058: Fix FEAT-RL2 SB3 comparison gaps

## Context

TASK-RL042 verification originally found FEAT-RL2 AC-2/AC-3/AC-4 all NOT MET
across sampled notebooks 0a/0b/1b/3b/7a/7b/9b/13b/X1, and this card's original
scope (add SB3 comparison + same-env comparison cells to 1b/3b) reflected that
finding. TASK-RL045 (Fix FEAT-RL2 dual-implementation gaps) has since shipped
real SB3 training and a same-environment numeric comparison to both notebooks
(1b: commit 37c9bff, including API-differences documentation; 3b: commit
af859db, comparison only, no API-differences section). AC-2 and AC-3 are
therefore already satisfied for 1b and 3b — re-verified live via
`audit_feat_rl2.py` (scratchpad), which reads each notebook's SB3 cell and
confirms `sb3_trained=True` for 1b, 3b, 7b, 9b, 13b, X1 and `api_diff_section`
present only for 1b.

This card's remaining, narrowed scope is AC-4 only: add the "API differences:
from-scratch X vs. Stable-Baselines3" documentation block — matching 1b's
existing style (a `print()` block appended to the end of the notebook's
existing SB3-training cell, cell 21 in 1b) — to the four notebooks that have
real SB3 training but no such section: **3b_mc_practical.ipynb**,
**7b_dqn_practical.ipynb**, **9b_ppo_practical.ipynb**,
**13b_exploration_practical.ipynb**.

**X1_rl_debugging.ipynb is explicitly excluded from this task's scope.**
FEAT-RL2's own AC-1 evidence enumerates exactly six dual-implementation
algorithm-lesson notebooks: 0a, 1b, 3b, 7b, 9b, 13b. X1 is not among them —
its SB3 cell (cell 7) trains PPO purely to demonstrate a Weights&Biases/
TensorBoard logging workflow, with no from-scratch counterpart anywhere in
the notebook to compare against. Writing a fabricated "from-scratch vs SB3"
section for X1 would misrepresent content the notebook doesn't have.

**0a_bandits_gridworld.ipynb has a separate, pre-existing AC-2 gap not
absorbed into this task.** 0a has zero SB3 usage at all (`sb3_import=False`)
— bandits and a simple tabular GridWorld have no idiomatic SB3 equivalent the
way the deep-RL lessons do, and building a new SB3 training pipeline for 0a
is a materially larger scope than "add API-differences documentation to an
existing SB3 cell." This is flagged as a residual caveat on FEAT-RL2's AC-2
rather than silently claimed complete.

0b and 7a remain out of scope as theory/setup notebooks with no SB3 usage
expected.

## Acceptance criteria

- [ ] **AC-1** — 3b_mc_practical.ipynb's existing SB3-comparison cell (cell 20) ends with a genuine, code-grounded "API differences: from-scratch MC control vs. Stable-Baselines3" print block
- [ ] **AC-2** — 7b_dqn_practical.ipynb's existing SB3-comparison cell (cell 15) ends with a genuine, code-grounded "API differences: from-scratch DQN vs. Stable-Baselines3" print block
- [ ] **AC-3** — 9b_ppo_practical.ipynb's existing SB3-comparison cell (cell 12) ends with a genuine, code-grounded "API differences: from-scratch PPO vs. Stable-Baselines3" print block, grounded in the notebook's actual from-scratch PPO cell (cell 10, HalfCheetah-v4) and SB3 PPO cell (cell 12, same env)
- [ ] **AC-4** — 13b_exploration_practical.ipynb's existing SB3-comparison cell (cell 12) ends with a genuine, code-grounded API-differences print block honestly framed around the notebook's actual structure (from-scratch tabular Q-learning + count-based bonus in Part 2 vs. a hand-rolled RND novelty wrapper bolted onto SB3 PPO in Part 3) rather than a naive copy of 1b's from-scratch-vs-SB3 numeric-comparison framing
- [ ] **AC-5** — all 4 modified notebooks re-execute top-to-bottom (`jupyter nbconvert --to notebook --execute --inplace`, QUICK_RUN enabled where supported) with zero ModuleNotFoundError/error-type output cells, verified via an nbformat scan, preserving FEAT-RL1's Colab-runnable acceptance criteria
- [ ] **AC-6** — FEAT-RL2.md's AC-2/AC-3/AC-4 rewritten to accurate current-state MET text, citing TASK-RL045 (commits af859db, 37c9bff) and this task's evidence commit(s), with 0a's residual SB3 gap and X1's out-of-scope status both stated explicitly rather than silently folded into "MET"

## Dependencies

- Directive: DIRECT-RL1
- Features: FEAT-RL2

## Pre-mortem

### Failure modes

- Copying 1b's API-differences bullets verbatim into a different notebook produces documentation that doesn't match that notebook's actual code — mitigated by reading each target notebook's actual from-scratch and SB3 cells directly (via scratchpad dump scripts) before writing any bullet.
- Fabricating a "from-scratch vs SB3" section for X1, which never had a from-scratch implementation to compare against — mitigated by excluding X1 from scope with reasoning stated above.
- Re-executing 9b (MuJoCo/HalfCheetah) or 13b (multi-seed PPO+RND) without QUICK_RUN could run long or time out — mitigated by enabling QUICK_RUN where the notebook supports it during the verification re-execute pass.
- Silently overclaiming FEAT-RL2 AC-2 as fully MET across all six AC-1 algorithm-lesson notebooks when 0a still has zero SB3 usage — mitigated by stating the 0a gap explicitly as a residual caveat in FEAT-RL2.md rather than hiding it.

### Weak assumptions

- Assumed the SB3-training cell is the last code cell before a "Summary"/"Key Takeaways" markdown cell in each target notebook, so appending to it introduces no new cell and no fresh execution dependency — verified via a cell-index TOC dump: true for 3b (cell 20 of 22), 7b (cell 15 of 17), 9b (cell 12 of 14), 13b (cell 12 of 14).
- Assumed 9b's from-scratch PPO (cell 10) and SB3 PPO (cell 12) are genuinely comparable as "same environment" despite not being printed side-by-side in one cell — verified by reading both cells: both construct their own `gym.make('HalfCheetah-v4')` instance independently.
