# TASK-RL047: Fix FEAT-RL4 MDP theory gaps

## Context

2 ACs NOT MET per FEAT-RL4.md verification (TASK-RL042): Bellman expectation/optimality equations are presented as given formulas, never derived step by step from the return definition G_t; MDPSolver.value_iteration() in 1a_mdp_theory.ipynb has no stored execution output, so there is no evidence it was ever run. Fix: add the step-by-step derivation and execute the solver cell with output retained.

## Acceptance criteria

- [ ] **AC1** — Insert a step-by-step derivation of the Bellman expectation equation for `V^π(s)` in `1a_mdp_theory.ipynb`'s Bellman-equations section (cell 12 or new cells at that point): define `G_t = R_{t+1} + γR_{t+2} + ...`, show the recursive form `G_t = R_{t+1} + γG_{t+1}`, define `V^π(s) = E_π[G_t | S_t=s]`, and apply linearity of expectation plus the law of total expectation (condition on action via `π(a|s)`, then on next state/reward via `P(s',r|s,a)`) to arrive at the given closed-form `V^π(s)` equation.
- [ ] **AC2** — Parallel derivation for `Q^π(s,a) = E_π[G_t | S_t=s, A_t=a]`, arriving at the given closed-form Bellman expectation equation for `Q^π`, and showing how `V^π(s)` and `Q^π(s,a)` relate (`V^π(s) = Σ_a π(a|s) Q^π(s,a)`).
- [ ] **AC3** — Derive the Bellman optimality equations from `V*(s) = max_π V^π(s)` and the identity `V*(s) = max_a Q*(s,a)`, showing how substituting into the Bellman expectation equation for `Q` yields the given `V*`/`Q*` optimality formulas.
- [ ] **AC4** — Execute `1a_mdp_theory.ipynb` top-to-bottom so cell 15 (`MDPSolver` + `student_mdp` value-iteration driver) has real stored output (non-empty `outputs`, non-`None` `execution_count`); the printed optimal value function and optimal policy must be sanity-checked against the Student MDP's reward structure (evidence in commit message / task card, not just an execution flag).
- [ ] **AC5** — Notebook executes clean top-to-bottom with zero error cells after both changes, verified by an independent nbformat error-cell scan (not just the executor's own exit message), matching the `total error cells: N / total cells: M` pattern used for TASK-RL046.

## Dependencies

- Directive: DIRECT-RL1
- Story: STORY-RL2
- Features: FEAT-RL4

## Pre-mortem

### Failure modes

- The derivation markdown could restate the given equations in different notation without actually deriving them step-by-step from `G_t` — mitigate by explicitly writing the `G_t = R_{t+1} + γG_{t+1}` recursion and the law-of-total-expectation conditioning step, not just asserting the final formula.
- Cell 15 may reveal a hidden pre-existing bug once actually executed (as 0a cell 12 did in TASK-RL046) — confirmed low-risk via static interface check (cell 9's `MDP` class exposes `get_transition_prob`, `get_reward`, `.S`, `.A`, `.gamma`, all used correctly by cell 15's `MDPSolver`), but not yet empirically confirmed by a real run.
- Executing top-to-bottom could disturb earlier cells' stored output/state (e.g. `np.random.seed` reuse in cell 7) in a way that changes their printed values — mitigate by treating any output diff in unrelated cells as a finding to investigate, not silently overwrite.

### Weak assumptions

- Assumes `student_mdp` (cell 11) is a well-posed MDP whose value iteration converges within `max_iterations=1000` at `epsilon=1e-6` — plausible given the small 2-state/2-action structure, but not yet empirically confirmed.
- Assumes the notebook's existing kernel/dependency environment (networkx, numpy, matplotlib, seaborn, pandas) is already working, since 0a/0b/13b all executed cleanly this session in the same environment.
