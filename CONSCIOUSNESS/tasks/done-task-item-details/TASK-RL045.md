# TASK-RL045: Fix FEAT-RL2 dual-implementation gaps

## Context

3 ACs NOT MET per FEAT-RL2.md verification (TASK-RL042): 1b imports SB3 but never trains/compares it ('this is a preview'); 3b has no SB3 or equivalent-framework usage for MC control; only 7b (and conditionally 9b) actually runs a from-scratch-vs-SB3 comparison on the same environment; no notebook in the sampled set (0a,0b,1b,3b,7a,7b,9b,13b,X1) documents API differences between the custom implementation and SB3's API. Fix: add real SB3 training+comparison to 1b and 3b, and an API-differences section to at least one representative notebook.

## Acceptance criteria

- [x] `notebooks/1b_mdp_practical.ipynb`: the existing SB3 cell (currently imports SB3, prints "This is a preview—Q-Learning is covered in Lesson 4!" and never trains it) is replaced with a real SB3 agent trained on the same `FrozenLake-v1` (4x4, slippery) environment used earlier in the notebook, evaluated empirically (reusing the notebook's own `evaluate_policy_empirically` helper or an equivalent), and printed side-by-side against the from-scratch DP-optimal policy's success rate/avg reward on the same environment — done in commit 37c9bff (SB3 DQN 59.0% vs DP Value Iteration 57.0% success rate, 100 episodes each)
- [x] `notebooks/3b_mc_practical.ipynb`: a new section trains a real SB3 (or equivalent-framework) agent on `Blackjack-v1`, using a `Tuple`-to-`Box` observation wrapper (e.g. `gymnasium.wrappers.FlattenObservation` or a custom flattening wrapper) since SB3's `MlpPolicy` does not accept the env's native `Tuple(Discrete(32), Discrete(11), Discrete(2))` observation space, and reports a direct numeric comparison (e.g. average return over N evaluation episodes) against the notebook's existing `policy_opt`/`policy_eps` MC-control policies on the same environment — done in commit af859db (SB3 DQN -0.156 vs MC Exploring Starts -0.234 vs MC Epsilon-Greedy -0.111, 1000 episodes each)
- [x] At least one of the two edited notebooks (1b or 3b) gains a new markdown+code section documenting concrete API differences between the from-scratch implementation and SB3's API (e.g. `predict()` vs. indexing a policy dict, `model.learn(total_timesteps=...)` vs. an explicit episode loop, built-in vecenv/logging vs. none) — done in 1b (commit 37c9bff), five concrete contrasts printed
- [x] Both edited notebooks execute top-to-bottom with `nbclient` (`allow_errors=False`) with zero error cells, outputs retained, verified by an independent post-execution scan for `output_type == 'error'` — verified via nbformat scan, `error cells: []` for both notebooks
- [x] No other notebook's existing passing cells are broken by the edit (spot-checked by the full-notebook execution result itself, since nbclient runs every cell in order) — both notebooks executed clean top-to-bottom with allow_errors=False

## Dependencies

- Directive: DIRECT-RL1
- Features: FEAT-RL2

## Pre-mortem

### Failure modes

- SB3 training on `Blackjack-v1` silently fails or trains a degenerate policy because the raw `Tuple` observation space is incompatible with `MlpPolicy` — mitigated by wrapping the env in a flattening/Box-observation wrapper before constructing the SB3 model, and sanity-checking `env.observation_space` post-wrap before training
- Long SB3 training runs (e.g. full 50000-timestep DQN on FrozenLake, or a large Blackjack run) blow the notebook execution timeout or take excessive wall-clock time in an unattended run — mitigated by keeping timesteps modest (e.g. a few thousand to ~20000) since the comparison only needs to be directionally real, not state-of-the-art, matching the scale already used elsewhere in this notebook set (7b uses 2000-50000 depending on QUICK_RUN)
- FrozenLake-v1 is stochastic (`is_slippery=True`) and single-run SB3 success rate could look arbitrarily worse than the DP-optimal policy purely from variance — mitigated by evaluating both policies over the same number of episodes (100, matching the notebook's existing `evaluate_policy_empirically` convention) rather than a handful of runs
- Editing cell 21 of 1b in place could silently orphan a downstream cell that assumed the old preview cell's absence of trained-model variables — mitigated by executing the full notebook top-to-bottom after the edit and checking for errors in every cell, not just the edited one

### Weak assumptions

- Assuming `evaluate_policy_empirically(policy, env, n_episodes=100)` from 1b cell 25 can be reused as-is for an SB3 model requires it to accept anything indexable/callable by `obs` — the current signature calls `policy[obs]`, which is dict-style DP-policy indexing and does NOT work for an SB3 model object; the fix must adapt evaluation (e.g. a small `model.predict(obs)`-based loop or a thin policy-shaped wrapper) rather than assuming direct reuse
- Assuming the 7b notebook's from-scratch-vs-SB3 comparison pattern (cells 15-16) transfers directly to 1b/3b without adjustment for each notebook's own state representation and evaluation convention — worth reviewing 7b's cell 15 pattern as a template, not copying it verbatim
- Assuming "at least one representative notebook" for the API-differences AC can be satisfied by a thin paragraph — the task's context field ties this AC to the same verification pass (TASK-RL042) that found zero of 9 sampled notebooks had it, so the section should include concrete, checkable code-level contrasts, not just prose
