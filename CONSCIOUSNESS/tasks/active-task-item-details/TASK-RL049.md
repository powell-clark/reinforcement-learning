# TASK-RL049: Fix FEAT-RL7 TD-learning gaps

## Context

2 ACs NOT MET per FEAT-RL7.md verification (TASK-RL042): no code cell implements TD(0) V(s) prediction in either notebook (4b only codes Sarsa/Q-learning control), despite TD error being well explained in 4a; Expected Sarsa appears only as a formula in 4a, never implemented in code in either notebook. Fix: implement TD(0) prediction and Expected Sarsa as running code.

## Acceptance criteria

- [ ] **AC1** — Implement `td_zero_prediction(env, policy, n_episodes, alpha=0.1, gamma=0.9)` in `4b_td_practical.ipynb`, following the algorithm in `4a_td_theory.ipynb` cell 5 exactly: online per-step update `δ = R + γV(S') − V(S)`, `V(S) += α·δ`, no waiting for episode end (the property that distinguishes TD(0) from the MC prediction implemented in `3b_mc_practical.ipynb`).
- [ ] **AC2** — Run `td_zero_prediction` on CliffWalking under an epsilon-greedy behavior policy derived from the already-trained `Q_ql` (reusing cell 4's trained table so the policy is near-optimal but still stochastic enough to visit varied states across episodes, since CliffWalking's transitions are deterministic and a purely greedy fixed policy would replay one identical trajectory every episode), for `n_episodes=500` matching the existing Sarsa/Q-learning scale, printing V(s) estimates for a handful of sample states along the near-optimal path.
- [ ] **AC3** — Implement `expected_sarsa(env, episodes, alpha, gamma, epsilon)` in `4b_td_practical.ipynb` following the formula in `4a_td_theory.ipynb` cell 10 exactly: the update uses `E[Q(S',A')] = (1-ε)·max_a Q(S',a) + (ε/|A|)·Σ_a Q(S',a)` under the current epsilon-greedy policy — never Sarsa's sampled `Q(S',A')` nor Q-learning's `max_a Q(S',a)`. Run it on CliffWalking with the same `episodes/alpha/gamma/epsilon` as the existing `sarsa()`/`qlearning()` calls, printing its mean reward alongside both for direct comparison.
- [ ] **AC4** — Add markdown tying the new cells back to 4a's existing explanations: TD(0) prediction's online per-step update vs MC's episode-end update (bootstrapping, per cell 4/5 of 4a); Expected Sarsa's variance reduction vs Sarsa from replacing a sampled next-action value with its expectation (per 4a's bias-variance discussion, cell 6).
- [ ] **AC5** — Verify both new update rules independent of environment stochasticity, the same way TASK-RL048 verified MC prediction: (a) reproduce the TD(0) update's exact arithmetic against a fixed, hand-computable 3-state chain trajectory (S0→S1→S2→Terminal, rewards 1,2,0, α=0.5, γ=1) and confirm it matches the hand-derived result `V={S0:0.5, S1:1.0, S2:0.0}` after one episode; (b) reproduce Expected Sarsa's expectation term against a fixed `Q(S')=[1,3,2,0], ε=0.1` and confirm it matches the hand-derived `E[Q(S',A')] = 0.9·3 + 0.025·6 = 2.85`.
- [ ] **AC6** — Fix the pre-existing structural defect discovered incidentally while scoping this task: `4b_td_practical.ipynb`'s final cell (markdown, "Summary") is missing its `metadata` key, which fails strict nbformat validation (`nbformat.read` raises `ValidationError: ... missing an expected key: metadata`) even though the notebook otherwise executes. Add `metadata: {}` to restore validity, and confirm via a raw-JSON key scan that no other cell in either 4a or 4b shares the defect.
- [ ] **AC7** — Execute `4b_td_practical.ipynb` top-to-bottom so all cells (existing and new) carry real stored output — sequential `execution_count`, no gaps — and confirm zero error cells via an independent nbformat error-cell scan (`total error cells: N / total cells: M`), matching the pattern used for TASK-RL046/047/048.

## Dependencies

- Directive: DIRECT-RL1
- Story: STORY-RL5
- Features: FEAT-RL7

## Pre-mortem

### Failure modes

- CliffWalking's transitions are deterministic (no environment stochasticity, only reset randomness which is absent here) — a purely greedy fixed policy would generate the exact same trajectory every episode, making `n_episodes>1` pointless for demonstrating TD(0) prediction's convergence. Mitigate by using an epsilon-greedy behavior policy (fixed epsilon, derived from the already-trained `Q_ql`) so different episodes visit different states.
- Expected Sarsa's expectation term must never silently collapse to Sarsa's sampled `Q(S',A')` or Q-learning's `max_a Q(S',a)` — a copy-paste from either existing function is the likeliest way this regresses unnoticed since all three share the same TD-error skeleton. Mitigate with the isolated fixed-input arithmetic check (AC5b), which only passes if the expectation formula is used verbatim.
- The pre-existing missing-`metadata` defect might not be confined to 4b's last cell — must confirm via a raw-JSON key scan across every cell of both 4a and 4b before declaring the notebook fixed, not just patch the one cell already found.
- Inserting new cells after cell 4 shifts every subsequent cell's index; 4b has no internal anchor links (`<a name=...>`) unlike 4a, so this shift is safe, but that must be confirmed by inspection rather than assumed.

### Weak assumptions

- Using `Q_ql` (already computed in cell 4) as the base for the TD(0) prediction behavior policy assumes cell 4 always executes before the new cells — true only because the insertion point is strictly after cell 4; would break if cells were reordered later.
- 500 episodes (matching the existing Sarsa/Q-learning scale) is assumed sufficient for TD(0) prediction's V(s) estimates to stabilize along the near-optimal path — not formally proven, only sanity-checked by inspecting the printed values for plausibility (e.g., higher V(s) closer to the goal).
