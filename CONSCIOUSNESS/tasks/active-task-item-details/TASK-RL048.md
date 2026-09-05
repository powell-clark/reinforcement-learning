# TASK-RL048: Fix FEAT-RL6 Monte Carlo gaps

## Context

1 AC NOT MET per FEAT-RL6.md verification (TASK-RL042): only every-visit MC prediction is coded (3b_mc_practical.ipynb mc_prediction()); first-visit MC is illustrated only via a hand-worked numeric example in 3a, never implemented as running code. Fix: add a working first-visit MC prediction implementation.

## Acceptance criteria

- [ ] **AC1** — Parameterize `mc_prediction()` in `3b_mc_practical.ipynb` (cell 7) with a `first_visit: bool = False` argument: default (`False`) preserves the existing every-visit behavior exactly (a return appended for every occurrence of a state in the trajectory); `True` counts only the return from a state's first occurrence per episode, skipping later occurrences of the same state within that episode.
- [ ] **AC2** — Add a new code cell after the existing MC-prediction print block that runs `mc_prediction(env, simple_policy, n_episodes=10000, first_visit=True)` on the same Blackjack env/policy, printing the estimated-state count and sample values for the same three states (`(20,5,False)`, `(12,5,False)`, `(15,2,True)`) already printed for every-visit, so the notebook has a real, running first-visit MC prediction implementation (not a hand-worked example).
- [ ] **AC3** — Print an explicit first-visit vs. every-visit comparison at those same sample states, and note in markdown that Blackjack states rarely repeat within an episode (player_sum is not revisited exactly, and an ace's value-demotion changes the `has_ace` component of the state tuple), so the two estimates are expected to be nearly identical here — this doubles as a correctness sanity check: a large divergence would indicate a bug in the first-visit skip logic.
- [ ] **AC4** — Execute `3b_mc_practical.ipynb` top-to-bottom so the new cell(s) have real stored output (non-empty `outputs`, non-`None` `execution_count`), and confirm no other cell's stored output changed in a way that indicates the run disturbed shared state (env/policy reuse).
- [ ] **AC5** — Notebook executes clean top-to-bottom with zero error cells after the change, verified by an independent nbformat error-cell scan (not just the executor's own exit message), matching the `total error cells: N / total cells: M` pattern used for TASK-RL046/TASK-RL047.

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
