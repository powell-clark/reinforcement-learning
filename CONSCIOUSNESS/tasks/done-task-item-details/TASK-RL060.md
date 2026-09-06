# TASK-RL060: Build FEAT-RL20 exercise and correctness review

## Context

FEAT-RL20 (MDP lesson exercise and correctness review) has 4 unmet acceptance
criteria: an explicit learning objective in `1a_mdp_theory.ipynb`, an
automated checked-answer mechanism added to `1b_mdp_practical.ipynb`'s
existing Exercise 1 (non-slippery FrozenLake comparison), an independent
correctness review of that check's own reference value, and a clean
top-to-bottom re-execution of both notebooks. Investigated this session:
Exercise 1 (cell 30 markdown, cell 31 code) already computes `V_noslip`,
`policy_noslip` via `value_iteration(P_noslip, R_noslip, gamma, 16, 4)` but
only ends in a printed "Observation:" line — no automated check exists.
Both notebooks' intro cells (1a cell 0, 1b cell 0) already carry an informal
"in this lesson we'll..." bullet list but no cell states an explicit,
labelled Learning Objective.

## Acceptance criteria

- [x] **AC-1** — Add an explicit "**Learning Objective:**" statement to `1a_mdp_theory.ipynb`'s introduction (cell 0), stating in one sentence what the learner will be able to do after the lesson (define an MDP tuple, derive the Bellman equations, implement a from-scratch solver). MET: commit 2df18cd.
- [x] **AC-2** — Add a new cell pair after `1b_mdp_practical.ipynb`'s existing Exercise 1 code cell (cell 31) that independently recomputes the Bellman-optimality residual for `V_noslip`/`policy_noslip` (NOT by re-calling `value_iteration()`) and asserts it is near zero and that `policy_noslip` is greedy with respect to it, printing PASS/FAIL. MET: commit eb0bcbe, cells 32-33; executed output prints "PASS: V_noslip satisfies the Bellman optimality equation and policy_noslip is greedy w.r.t. it." with residual 0.00e+00.
- [x] **AC-3** — The new check is a genuine correctness review, not a duplicate of the exercise's own method: it recomputes Q(s,a) directly from the Bellman optimality equation using `P_noslip`/`R_noslip`/`gamma`, independent of `value_iteration()`'s internal iteration. MET: commit eb0bcbe, `bellman_q()` in cell 33 loops `P_noslip[s][a].items()` directly and never calls `value_iteration()`.
- [x] **AC-4** — `1a_mdp_theory.ipynb` and `1b_mdp_practical.ipynb` execute top-to-bottom with zero error-type output cells after the above changes, verified via an independent nbformat scan (not just the executor's own exit code). MET: `jupyter nbconvert --execute --inplace` on both (commit eb0bcbe), followed by a standalone nbformat scan of `outputs[].output_type == 'error'` across both notebooks returning zero matches.

## Dependencies

- Directive: DIRECT-RL1
- Story: STORY-RL2
- Feature: FEAT-RL20

## Pre-mortem

### Failure modes

- The new check could silently re-call `value_iteration()` under a different name, making it a duplicate rather than an independent review — mitigate by deriving Q(s,a) with a fresh loop over `P_noslip[s][a].items()` directly in the check cell, never invoking the `value_iteration` function.
- A tie in Q-values at a state could flag a false "policy mismatch" even though the reported action is equally optimal — mitigate by only flagging a mismatch when the reported action's Q-value is measurably below the max, not on any argmax disagreement.
- Re-executing both notebooks top-to-bottom could disturb unrelated cells' stored output (e.g. reseeded RNG) — mitigate by treating any output diff outside the touched cells as a finding to investigate, not silently overwrite.

### Weak assumptions

- Assumes `P_noslip`/`R_noslip` (built by `extract_mdp_from_env` in cell 7, reused in cell 31) are still in scope when the new cell runs immediately after cell 31 — true only if execution stays strictly top-to-bottom.
- Assumes the existing FrozenLake 4x4 non-slippery MDP has a unique optimal value per state (no arbitrarily-close ties) tight enough for a 1e-3 residual tolerance to be meaningful — plausible given the deterministic non-slippery dynamics, not yet empirically confirmed.
