# TASK-RL046: Fix FEAT-RL3 Gymnasium-integration gaps

## Context

4 ACs NOT MET per FEAT-RL3.md verification (TASK-RL042): 0a's custom GridWorld uses the old 4-tuple gym API instead of the modern 5-tuple reset()/step(); tabular lessons (1b FrozenLake, 3b Blackjack) use built-in Gymnasium envs instead of the custom GridWorld, which only appears as a plain non-gym.Env class in 0a; a repo-wide grep found zero gym.register() calls for any custom env (TreasureHuntEnv, SparseMaze, GridWorld); no notebook captures/displays an rgb_array frame, and custom envs render only ASCII or nothing (13b's SparseMaze has no render() at all). Fix: modernize 0a's API, register the custom envs, and add rgb_array rendering.

## Acceptance criteria

- [ ] **AC1** — 0a's `GridWorld` class subclasses `gym.Env` and implements the modern 5-tuple API: `reset(seed=None, options=None) -> (obs, info)` and `step(action) -> (obs, reward, terminated, truncated, info)`, replacing the current bare-state `reset()` and 4-tuple `step()`.
- [ ] **AC2** — 0a's `GridWorld` is registered via `gym.register()` and instantiable via `gym.make('GridWorld-v0')`; 0b's already-`gym.Env`-compliant `TreasureHuntEnv` and 13b's already-`gym.Env`-compliant `SparseMaze` are also registered via `gym.register()` (they are already modern-API, just unregistered).
- [ ] **AC3** — 0a's `GridWorld` and 13b's `SparseMaze` support `render_mode='rgb_array'` and return a real image array from `render()`; each of 0a and 13b gains a cell that calls `render()` and displays the frame inline via `plt.imshow()`. (0b's `TreasureHuntEnv` is a 1-D line environment already visualised via its own plotting cells — no additional render mode is added there.)
- [ ] AC4 — 0a's Q-learning training/demo/test cells (currently written against the old 4-tuple API) are updated to the new 5-tuple API end-to-end; 0a, 0b, and 13b each execute clean top-to-bottom with zero error cells after the change.
- [ ] AC5 (deferred, in scope-notes below) — FEAT-RL3's own AC-2 ("a custom GridWorld environment is provided for tabular lessons") and AC-3's broader "any custom environment" wording are intentionally NOT fully closed by this task; see Scope notes.

## Scope notes

FEAT-RL3 names two other gaps this task does not close, and this is deliberate,
not an oversight:

- **FEAT-RL3 AC-2** (custom GridWorld used in place of FrozenLake/Blackjack in
  1b/3b) would mean ripping out already-shipped, already-verified tabular
  lessons built around specific built-in envs whose semantics (card-drawing
  randomness for Blackjack, slippery-ice stochasticity for FrozenLake) are
  themselves the pedagogical point of those lessons. That is a pedagogical
  content decision for FEAT-RL3 / its owning stories, not a mechanical API fix
  — out of scope for this task.
- **2b's, 11b's, and X4's `GridWorld`/`GridWorldEnv` classes** are left as-is.
  2b's and 11b's are plain (non-`gym.Env`) classes deliberately exposing a
  dict-based transition model (`.P`) for direct-DP/model-based lessons —
  converting them to registered `gym.Env`s would not serve those lessons and
  risks breaking the DP code that reads `.P` directly. X4's `GridWorldEnv` is
  already a modern `gym.Env` used only as a narrow, local offline-RL data
  source for one research-frontiers demo, not a reusable teaching env — not
  worth registering globally.

## Dependencies

- Directive: DIRECT-RL1
- Features: FEAT-RL3

## Pre-mortem

### Failure modes

- Modernizing `GridWorld`'s `step()`/`reset()` signature without updating every downstream call site in 0a (random-trajectory demo, Q-learning training loop, policy test) leaves stale 4-tuple unpacking that raises `TypeError` or silently misreads `done` — mitigate by grep-ing all `env.reset(` / `env.step(` / `.reset()` / `.step(` call sites in 0a before editing, and re-executing the whole notebook after.
- `gym.register()` with a class object (not a string) as `entry_point` may behave differently across Gymnasium versions, or `gym.make()` may wrap the env in `TimeLimit`/`OrderEnforcing`, changing `.unwrapped` access patterns for any later cell reading GridWorld's raw attributes — mitigate by verifying `gym.make()` roundtrip and any `.unwrapped` needs immediately after registering, in a scratch script first.
- Adding `render_mode='rgb_array'` support requires drawing a grid image (agent position, goal, obstacles) as a numpy array; a naive implementation could return the wrong shape/dtype for `plt.imshow()` or silently return `None` for other render modes — mitigate by asserting the returned array's shape/dtype in a scratch check before writing it into the real notebook.
- 13b's `SparseMaze` (14x14, up to 250 steps, existing exploration-algorithm cells) may already assume no `render()` exists (e.g. never calling it) — adding one is additive and low-risk, but the notebook's existing training loops must still execute unchanged; verify via a full top-to-bottom re-run with `allow_errors=False`.

### Weak assumptions

- Assuming `gym.register(entry_point=SomeClass)` (a live class object, not an import-string) is supported by the installed Gymnasium version in this environment — must verify empirically via a scratch script before depending on it in the real notebooks; if unsupported, register via a wrapper factory function instead.
- Assuming 0b's `TreasureHuntEnv` and 13b's `SparseMaze` have no existing direct-instantiation call sites (`TreasureHuntEnv(...)`, `SparseMaze(...)`) that would need switching to `gym.make(...)` for the registration to be meaningful — must grep each notebook's call sites, not just the class definitions, before claiming AC2 met.
- Assuming pre-existing cells in 0a/0b/13b already execute clean (zero error cells) before this task's edits, so any new error introduced by this task's changes is attributable to this task — verify via `git show HEAD:<path>` outputs before editing, same pre-existing-bug-detection pattern used on TASK-RL045.
