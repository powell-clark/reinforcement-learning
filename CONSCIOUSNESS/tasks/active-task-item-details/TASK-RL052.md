# TASK-RL052: Fix FEAT-RL11 policy-gradient gaps

## Context

2 ACs NOT MET per FEAT-RL11.md verification (TASK-RL042): 8a states the policy gradient theorem's final formula with a one-line intuition but shows no derivation steps from J(theta) to the gradient expression; 8b's SB3 A2C comparison is unexecuted and calls LunarLander-v2 (discrete default) with a continuous Normal policy, a likely runtime bug. Fix: add the derivation and fix+execute the A2C comparison cell.

Unlike TASK-RL051 (which found its target gaps already fixed by a later commit), direct inspection this session confirms both gaps here are genuinely live: `git log --oneline --follow` on both `notebooks/8a_policy_gradients_theory.ipynb` and `notebooks/8b_policy_gradients_practical.ipynb` shows neither has been touched since original creation (`b44b8b7`, `8f7ab00`). nbformat inspection confirms every cell in both notebooks has `execution_count=None` — not just the two flagged cells, the entire notebooks are unexecuted.

8a cell [3] (the derivation gap) reads in full:
> "We want to maximize: $J(\theta) = \mathbb{E}_{\tau \sim \pi_\theta}[R(\tau)]$ ... The **policy gradient theorem** (Sutton, 1999) tells us: $\nabla_\theta J(\theta) \propto \mathbb{E}[...]$ ... Key insight: We take gradients of the **log policy**, weighted by the **action value**."

It jumps straight from stating the objective to citing the final theorem with no intermediate steps — confirmed exactly as the task card describes.

8b's bug is broader than the card states: `gym.make('LunarLander-v2')` (cells [8] and [10]) is not merely deprecated but a hard `ValueError` under the installed gymnasium 1.3.0 ("Environment version v2 for LunarLander is deprecated. Please use LunarLander-v3 instead"), so the notebook cannot run at all until the env id is bumped to v3. Separately, `LunarLander-v3`'s default action space is discrete, while `ActorNetwork.forward` (cell [4]) returns a continuous Gaussian `(mean, std)` — so the fix is `gym.make('LunarLander-v3', continuous=True)`, which additionally requires the `Box2D` package, absent from `requirements.txt`. Resolved and verified this session at the environment level: `pip install swig` (prebuilt wheel `swig-4.5.0`) then `pip install "gymnasium[box2d]"` (prebuilt wheel `box2d-2.3.10`), followed by a direct `.reset()`/`.step()` smoke test on `gym.make('LunarLander-v3', continuous=True)` returning a real reward with no error.

## Acceptance criteria

- [ ] **AC-1** — Add explicit derivation steps to 8a cell [3] (or a new cell immediately after it) from $J(\theta) = \mathbb{E}_{\tau\sim\pi_\theta}[R(\tau)]$ through the log-derivative trick ($\nabla_\theta \pi_\theta(\tau) = \pi_\theta(\tau)\nabla_\theta \log \pi_\theta(\tau)$) to the final policy gradient theorem expression, not just the objective and the final formula
- [ ] **AC-2** — Add `gymnasium[box2d]` to `requirements.txt` (the dependency required for LunarLander, currently absent)
- [ ] **AC-3** — Fix 8b cell [8]: `gym.make('LunarLander-v2')` → `gym.make('LunarLander-v3', continuous=True)`
- [ ] **AC-4** — Fix 8b cell [10]: same env-id/continuous fix for the SB3 A2C comparison
- [ ] **AC-5** — Execute `8a_policy_gradients_theory.ipynb` top-to-bottom with outputs retained; confirm 0 errors across all cells via nbformat inspection (execution_count set, no error outputs)
- [ ] **AC-6** — Execute `8b_policy_gradients_practical.ipynb` top-to-bottom with outputs retained; confirm 0 errors and genuine convergence output in the LunarLander training cell and the SB3 comparison cell
- [ ] **AC-7** — Update FEAT-RL11.md AC-1 and AC-3 from NOT MET to `[x]`, citing this task and specific cell-level evidence (exec counts, output content)

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
