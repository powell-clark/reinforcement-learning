# TASK-RL052: Fix FEAT-RL11 policy-gradient gaps

## Context

2 ACs NOT MET per FEAT-RL11.md verification (TASK-RL042): 8a states the policy gradient theorem's final formula with a one-line intuition but shows no derivation steps from J(theta) to the gradient expression; 8b's SB3 A2C comparison is unexecuted and calls LunarLander-v2 (discrete default) with a continuous Normal policy, a likely runtime bug. Fix: add the derivation and fix+execute the A2C comparison cell.

Unlike TASK-RL051 (which found its target gaps already fixed by a later commit), direct inspection this session confirms both gaps here are genuinely live: `git log --oneline --follow` on both `notebooks/8a_policy_gradients_theory.ipynb` and `notebooks/8b_policy_gradients_practical.ipynb` shows neither has been touched since original creation (`b44b8b7`, `8f7ab00`). nbformat inspection confirms every cell in both notebooks has `execution_count=None` — not just the two flagged cells, the entire notebooks are unexecuted.

8a cell [3] (the derivation gap) reads in full:
> "We want to maximize: $J(\theta) = \mathbb{E}_{\tau \sim \pi_\theta}[R(\tau)]$ ... The **policy gradient theorem** (Sutton, 1999) tells us: $\nabla_\theta J(\theta) \propto \mathbb{E}[...]$ ... Key insight: We take gradients of the **log policy**, weighted by the **action value**."

It jumps straight from stating the objective to citing the final theorem with no intermediate steps — confirmed exactly as the task card describes.

8b's bug is broader than the card states: `gym.make('LunarLander-v2')` (cells [8] and [10]) is not merely deprecated but a hard `ValueError` under the installed gymnasium 1.3.0 ("Environment version v2 for LunarLander is deprecated. Please use LunarLander-v3 instead"), so the notebook cannot run at all until the env id is bumped to v3. Separately, `LunarLander-v3`'s default action space is discrete, while `ActorNetwork.forward` (cell [4]) returns a continuous Gaussian `(mean, std)` — so the fix is `gym.make('LunarLander-v3', continuous=True)`, which additionally requires the `Box2D` package, absent from `requirements.txt`. Resolved and verified this session at the environment level: `pip install swig` (prebuilt wheel `swig-4.5.0`) then `pip install "gymnasium[box2d]"` (prebuilt wheel `box2d-2.3.10`), followed by a direct `.reset()`/`.step()` smoke test on `gym.make('LunarLander-v3', continuous=True)` returning a real reward with no error.

## Acceptance criteria

- [x] **AC-1** — Added a 4-step derivation to 8a cell-3: (1) differentiate under the integral, (2) log-derivative trick substitution yielding the expectation form, (3) factor $\pi_\theta(\tau)$ into policy vs. dynamics terms, showing dynamics terms vanish, (4) replace $R(\tau)$ with causal $Q^\pi(s_t,a_t)$ to reach the policy gradient theorem. Committed `b6830dd`.
- [x] **AC-2** — `gymnasium[box2d]>=0.29.0` and `swig>=4.0.0` added to `requirements.txt`. Committed `b6830dd`.
- [x] **AC-3** — 8b cell-8: `gym.make('LunarLander-v2')` → `gym.make('LunarLander-v3', continuous=True)`. Executed exec_count=4, 0 error outputs; produced real training returns (Episode 10: -511.15 ... Episode 50: -370.10, final avg -423.60).
- [x] **AC-4** — 8b cell-10: same fix applied inside the SB3 `A2C` block. Executed exec_count=5, 0 error outputs; SB3 A2C avg return -33.71 over 5 eval episodes.
- [x] **AC-5** — `8a_policy_gradients_theory.ipynb` executed top-to-bottom via `jupyter nbconvert --execute --inplace`. nbformat inspection confirms every code cell has execution_count set (cell-2 exec=1, cell-5 exec=2, cell-7 exec=3) and 0 cells of output_type=='error'.
- [x] **AC-6** — `8b_policy_gradients_practical.ipynb` executed top-to-bottom, same nbconvert method. nbformat inspection: cell-2 exec=1 ("Using device: cuda"), cell-4 exec=2, cell-6 exec=3, cell-8 exec=4 (LunarLander A2C training, genuine noisy non-monotonic returns matching the notebook's stated 50-episode demonstration scope), cell-10 exec=5 (SB3 comparison, avg return -33.71). 0 error outputs across both notebooks.
- [x] **AC-7** — FEAT-RL11.md AC-1 and AC-3 updated to `[x]` citing this task, below.

## Dependencies

- Directive: DIRECT-RL1
- Story: STORY-RL9
- Features: FEAT-RL11

## Pre-mortem

### Failure modes

- Adding derivation steps that are mathematically sloppy or skip the log-derivative trick itself, reproducing the same "states result without justification" defect one level down
- Training A2C on LunarLander-v3-continuous for too few episodes to show real convergence, producing technically-executed-but-unconvincing output (mitigate: match or exceed the notebook's own stated 50-episode / batch_size=64 schedule, checked against actual returned reward trend, not just absence of errors)
- Fixing only the two cells the task card names ([8], [10]) while leaving other unexecuted cells in the notebook silently broken

### Weak assumptions

- That the Box2D/swig install resolved this session persists into whatever environment actually executes the notebook (e.g. a background execution task) — mitigated by adding the dependency to `requirements.txt` itself rather than relying on the ambient pip environment
- That REINFORCE-with-baseline and Actor-Critic (8a's other code cells, [5] and [7]) will execute cleanly on first run since they were never previously run — verify their output directly rather than assuming success from lack of syntax errors
