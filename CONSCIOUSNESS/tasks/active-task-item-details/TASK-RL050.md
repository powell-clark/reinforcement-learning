# TASK-RL050: Fix FEAT-RL8 eligibility-trace gaps

## Context

2 ACs NOT MET per FEAT-RL8.md verification (TASK-RL042): n-step returns/TD/Sarsa appear only as formulas in 5a_nstep_eligibility.ipynb — both notebooks jump straight to eligibility-trace (lambda) code with no literal n-step update ever implemented; the forward/backward-view equivalence is only asserted ('The Key Theorem') with no derivation or empirical comparison, and only the backward view is implemented. Fix: implement literal n-step TD/Sarsa and add a derivation or empirical equivalence check.

## Acceptance criteria

- [ ] **AC1** — Implement `n_step_td_prediction(env, n, alpha, gamma, num_episodes)` in 5a_nstep_eligibility.ipynb: literal per-episode n-step TD prediction matching cell 3's return formula `G_t^(n) = R_{t+1} + γR_{t+2} + ... + γ^(n-1)R_{t+n} + γ^n V(S_{t+n})` and cell 4's update `V(S_t) += α[G_t^(n) - V(S_t)]` — waits n steps before each update, never collapsing to the backward-view/eligibility-trace code already present.
- [ ] **AC2** — Run `n_step_td_prediction` on the RandomWalk environment for at least n=1 and n=4, and show the n=1 case numerically matches standard TD(0) on the same trajectory (the bias-variance special case from cell 3), demonstrating the formula is a genuine independent implementation, not eligibility-trace code relabeled.
- [ ] **AC3** — Add a forward-backward equivalence check: compute the offline λ-return (forward view, cell 6's `G_t^λ = (1-λ)Σλ^(n-1)G_t^(n)`) for a fixed trajectory with V held frozen, and compare it numerically to the backward-view eligibility-trace update's value estimate on the same frozen-V trajectory, reporting agreement within numerical tolerance — replacing "The Key Theorem"'s bare assertion with actual evidence. Must use the offline (batch, V-frozen-during-episode) formulation, since exact forward/backward equivalence does not hold for online updating.
- [ ] **AC4** — Add markdown tying the two new cells back to the existing theory cells (3, 4, 6).
- [ ] **AC5** — Verify `n_step_td_prediction` and the equivalence check independent of environment stochasticity against fixed hand-computable inputs, continuing the verify_*.py pattern from TASK-RL046/047/048/049.
- [ ] **AC6** — Fix the pre-existing cell-ordering defect in 5a_nstep_eligibility.ipynb: the Sarsa(λ) practical section's cells are ordered so later cells reference names earlier cells haven't defined yet (the plotting cell uses `returns_td`/`returns_lambda` from the training cell that follows it; the training cell uses the `SarsaLambda` class and `RandomWalk` env defined in cells after it; the introductory markdown for the section is the notebook's last cell). Reorder into dependency-correct sequence.
- [ ] **AC7** — Fix the equivalent pre-existing cell-ordering defect in 5b_nstep_eligibility_practical.ipynb: the Stable-Baselines3 DQN cell references `env_mc` and `returns_mc`, both defined two cells later by the tile-coded Sarsa(λ)-on-MountainCar cell. Reorder so definitions precede use.
- [ ] **AC8** — Execute 5a_nstep_eligibility.ipynb top-to-bottom for the first time ever (all execution_count currently `None`): 0 error cells, sequential execution_count with no gaps.
- [ ] **AC9** — Execute 5b_nstep_eligibility_practical.ipynb top-to-bottom for the first time ever (all execution_count currently `None`): 0 error cells, sequential execution_count with no gaps.

## Dependencies

- Directive: DIRECT-RL1
- Story: STORY-RL6
- Features: FEAT-RL8

## Pre-mortem

### Failure modes

- Reordering cells in 5a/5b could silently break code that implicitly relied on the old order (e.g. an RNG seed cell, an import) — re-verify every moved cell's dependencies (not just the ones motivating the move) still precede their uses after reorder.
- 5b's Stable-Baselines3 DQN cell (existing, untouched code) trains for 20,000 timesteps and has never been executed — first-ever execution may be slow or may surface a latent SB3/gymnasium incompatibility unrelated to this task's two gaps; time-box it and report as a separate finding if it blocks AC9 rather than silently expanding scope to fix it.
- Claiming exact forward-backward equivalence from an online (V-updated-during-episode) backward-view run would be false — the textbook equivalence holds only for offline/batch updating with V frozen during the trajectory. AC3 must freeze V for both sides of the comparison, not compare the online eligibility-trace code as-is against the offline λ-return.

### Weak assumptions

- RandomWalk's 10-state chain (5a cell 15) has enough length for an n=1 vs n=4 comparison to show a visible bias/variance difference — confirm by inspecting the resulting value estimates before treating the comparison as informative, not just non-crashing.
- gymnasium 1.3.0 / stable-baselines3 2.9.0 are compatible for 5b's MountainCar-v0 + SB3 DQN cell — confirmed via direct import and `gym.make('MountainCar-v0')` this session (Discrete/Box spaces resolve, sb3 imports cleanly modulo an unrelated legacy-Gym deprecation warning at import time); MountainCar-v0 itself carries no deprecation, unlike CliffWalking-v0 in TASK-RL049.
