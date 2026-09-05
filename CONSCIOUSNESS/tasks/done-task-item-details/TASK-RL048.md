# TASK-RL048: Fix FEAT-RL6 Monte Carlo gaps

## Context

1 AC NOT MET per FEAT-RL6.md verification (TASK-RL042): only every-visit MC prediction is coded (3b_mc_practical.ipynb mc_prediction()); first-visit MC is illustrated only via a hand-worked numeric example in 3a, never implemented as running code. Fix: add a working first-visit MC prediction implementation.

## Acceptance criteria

- [x] **AC1** — Parameterize `mc_prediction()` in `3b_mc_practical.ipynb` (cell 7) with a `first_visit: bool = False` argument: default (`False`) preserves the existing every-visit behavior exactly (a return appended for every occurrence of a state in the trajectory); `True` counts only the return from a state's first occurrence per episode, skipping later occurrences of the same state within that episode. (evidence: commit 2116b3a, cell 7 rewritten with `is_first_occurrence` per-episode tracking)
- [x] **AC2** — Add a new code cell after the existing MC-prediction print block that runs `mc_prediction(env, simple_policy, n_episodes=10000, first_visit=True)` on the same Blackjack env/policy, printing the estimated-state count and sample values for the same three states (`(20,5,False)`, `(12,5,False)`, `(15,2,True)`) already printed for every-visit. (evidence: commit 2116b3a cell 9, executed output — "Estimated 280 states", `V(20,5,False)=0.689`, `V(12,5,False)=-0.649`, `V(15,2,True)=-0.571`)
- [x] **AC3** — Print an explicit first-visit vs. every-visit comparison at those same sample states, with markdown noting Blackjack states rarely repeat within an episode. (evidence: cell 9 printed comparison — |diff| 0.058/0.075/0.127 at the three sample states, consistent with ordinary MC sampling variance between two independent 10000-episode draws, not a bug; independently confirmed the accumulation logic itself is exact by reproducing 3a_mc_theory.ipynb cell 8's hand-worked S0→S1→S2→S1→S3 example against the actual first_visit/every_visit code — got V(S0)=12, V(S1)=12, V(S2)=11, V(S3)=10 for first-visit and V(S0)=12, V(S1)=10.5, V(S2)=11, V(S3)=10 for every-visit, an exact match)
- [x] **AC4** — Execute `3b_mc_practical.ipynb` top-to-bottom so the new cell(s) have real stored output (non-empty `outputs`, non-`None` `execution_count`), and confirm no other cell's stored output changed in a way that indicates the run disturbed shared state. (evidence: all 9 code cells carry sequential execution_count 1-9 with no gaps — a single clean top-to-bottom run touched every cell including the pre-existing MC control/SB3 comparison cells)
- [x] **AC5** — Notebook executes clean top-to-bottom with zero error cells after the change, verified by an independent nbformat error-cell scan. (evidence: `total error cells: 0 / total cells: 9`)

## Dependencies

- Directive: DIRECT-RL1
- Story: STORY-RL4
- Features: FEAT-RL6

## Pre-mortem

### Failure modes

- A naive first-visit implementation could dedupe by scanning `returns[state]` after the fact (state-value keyed) rather than by trajectory index, which silently drops legitimate distinct-episode returns for a state that IS a genuine first visit in a later episode — mitigate by tracking first-occurrence per trajectory index (`seen` set reset every episode), never per global `returns` dict.
- Blackjack's env is stateful (`gym.make` instance reused across cells) — running the new first-visit cell after the every-visit cell already consumed episodes from the same `env` object is fine (each `env.reset()` starts a fresh episode) but must be verified empirically, not assumed, since a subtly stateful wrapper could leak between calls.
- The "first-visit ≈ every-visit for Blackjack" expectation is a prediction, not a guarantee — if the notebook's actual `simple_policy` or Blackjack's `sab=False` (default) reward variant does allow same-state revisits, the comparison could show real (not bug-induced) divergence; treat any divergence as a finding to explain via trajectory inspection, not to force-fix.

### Weak assumptions

- Assumes `defaultdict(list)` returns accumulation and `np.mean` averaging generalize unchanged from every-visit to first-visit once the correct return subset is selected — plausible since only the *set of returns fed in* changes, not the averaging step.
- Assumes 10000 episodes (matching the existing every-visit call) gives both estimators enough samples to converge closely enough for the AC3 sanity comparison to be meaningful — not yet empirically confirmed.
- Assumes the existing every-visit cell's stored output for `V_simple` at the three sample states remains unchanged after adding new cells later in the notebook (no shared mutable state crosses cell boundaries) — to be confirmed by diffing that cell's output before/after execution.
