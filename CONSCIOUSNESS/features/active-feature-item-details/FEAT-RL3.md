# FEAT-RL3: Gymnasium environment integration across all lessons

## Kano
must-have

## Context
All practical work uses the Gymnasium (formerly OpenAI Gym) environment API plus a custom GridWorld for teaching, giving learners a single consistent interface across the curriculum.

## Acceptance Criteria
- [x] **AC-1** — Notebooks use the Gymnasium reset()/step()/render() API consistently — MET (TASK-RL046, commit 441ca98): 0a's GridWorld is now a real `gym.Env` subclass with `render_modes` metadata; its random-trajectory, Q-learning training, and policy-test cells were migrated from the old 4-tuple to the 5-tuple `state, reward, terminated, truncated, info = env.step(action)` form, matching the rest of the curriculum from 0b onward. Verified live: zero remaining 4-tuple `step()` unpacking in 0a.
- [ ] **AC-2** — A custom GridWorld environment is provided for tabular lessons — STILL NOT MET: TASK-RL046 modernized and registered GridWorld-v0, TreasureHuntEnv-v0, and SparseMaze-v0, but wired none of them into a tabular lesson — 1b still uses FrozenLake and 3b still uses Blackjack (verified live: zero GridWorld/SparseMaze/TreasureHuntEnv references in either notebook). GridWorld itself is demonstrated only inside the theory notebook 0a (a `gym.make('GridWorld-v0')` demo cell), and SparseMaze is used only in 13b (exploration, not one of this AC's sampled tabular lessons). This is the genuine remaining gap, tracked as TASK-RL059.
- [x] **AC-3** — Environments are registered and reproducible with seeds — MET (TASK-RL046, commit 441ca98): GridWorld-v0, TreasureHuntEnv-v0, and SparseMaze-v0 are all registered via `gym.register()`, each guarded against re-registration, with seeded `reset(seed=...)` reproducibility. Verified live: `gym.register`/`register(` calls present in notebooks/0a, 0b, 13b, 15b.
- [x] **AC-4** — Rendering works within Colab (rgb_array / inline display) — MET (TASK-RL044): 7b cell 13 executes an `rgb_array` render and displays the captured frame inline via matplotlib imshow, with retained image/png output. Evidence: commit 6fce882457be1430db49670c6a2be04494ee960e.

## Stories
STORY-RL1, STORY-RL2, STORY-RL3, STORY-RL4, STORY-RL5, STORY-RL6, STORY-RL7, STORY-RL8, STORY-RL9, STORY-RL10, STORY-RL11, STORY-RL12, STORY-RL13, STORY-RL14, STORY-RL15, STORY-RL16, STORY-RL17

## Links
- Directive: DIRECT-RL1 (Ship complete RL curriculum)
