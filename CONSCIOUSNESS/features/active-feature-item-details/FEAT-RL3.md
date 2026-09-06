# FEAT-RL3: Gymnasium environment integration across all lessons

## Kano
must-have

## Context
All practical work uses the Gymnasium (formerly OpenAI Gym) environment API plus a custom GridWorld for teaching, giving learners a single consistent interface across the curriculum.

## Acceptance Criteria
- [x] **AC-1** — Notebooks use the Gymnasium reset()/step()/render() API consistently — MET (TASK-RL046, commit 441ca98): 0a's GridWorld is now a real `gym.Env` subclass with `render_modes` metadata; its random-trajectory, Q-learning training, and policy-test cells were migrated from the old 4-tuple to the 5-tuple `state, reward, terminated, truncated, info = env.step(action)` form, matching the rest of the curriculum from 0b onward. Verified live: zero remaining 4-tuple `step()` unpacking in 0a.
- [x] **AC-2** — A custom GridWorld environment is provided for tabular lessons — MET (TASK-RL059, commit ab01c06): 1b (the MDP/tabular-DP lesson) now trains a model-free tabular Q-learning algorithm against `gym.make('GridWorld-v0')`, using the 5-tuple step API and a seeded `reset(seed=...)` for reproducibility, alongside — not replacing — its existing FrozenLake dynamic-programming work. GridWorld-v0 was not substitutable into 1b's existing DP pipeline (`extract_mdp_from_env` depends on FrozenLake's internal `P`/`R` dict, which GridWorld-v0 doesn't expose), so the new section demonstrates the model-free alternative instead. The learned policy converges to a 100% empirical success rate over 100 evaluation episodes. Verified live: 1b re-executed top-to-bottom with zero error-type output cells (independent nbformat scan, 18/18 code cells clean).
- [x] **AC-3** — Environments are registered and reproducible with seeds — MET (TASK-RL046, commit 441ca98): GridWorld-v0, TreasureHuntEnv-v0, and SparseMaze-v0 are all registered via `gym.register()`, each guarded against re-registration, with seeded `reset(seed=...)` reproducibility. Verified live: `gym.register`/`register(` calls present in notebooks/0a, 0b, 13b, 15b.
- [x] **AC-4** — Rendering works within Colab (rgb_array / inline display) — MET (TASK-RL044): 7b cell 13 executes an `rgb_array` render and displays the captured frame inline via matplotlib imshow, with retained image/png output. Evidence: commit 6fce882457be1430db49670c6a2be04494ee960e.

## Stories
STORY-RL1, STORY-RL2, STORY-RL3, STORY-RL4, STORY-RL5, STORY-RL6, STORY-RL7, STORY-RL8, STORY-RL9, STORY-RL10, STORY-RL11, STORY-RL12, STORY-RL13, STORY-RL14, STORY-RL15, STORY-RL16, STORY-RL17

## Links
- Directive: DIRECT-RL1 (Ship complete RL curriculum)
