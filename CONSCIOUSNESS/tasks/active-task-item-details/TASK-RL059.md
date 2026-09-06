# TASK-RL059: Fix FEAT-RL3 gym API and registration gaps

## Context

TASK-RL042 verification (superseded, see below): FEAT-RL3 AC-1/AC-2/AC-3 all NOT MET.

**Narrowed scope.** Shipped-check pre-flight (this session, 2026-09-06) found TASK-RL046 (Fix FEAT-RL3 Gymnasium-integration gaps, commit 441ca98) already closed AC-1 and AC-3 before this task was even reserved: 0a's GridWorld is now a real `gym.Env` subclass using the 5-tuple `reset()`/`step()` API throughout its pedagogical cells (verified live: zero remaining 4-tuple `step()` unpacking in 0a), and GridWorld-v0/TreasureHuntEnv-v0/SparseMaze-v0 are all registered via guarded `gym.register()` calls with seeded reproducibility. FEAT-RL3.md's AC-1/AC-3 text was stale (still read NOT MET) and has been corrected in a separate commit (81a77e0) citing this evidence.

One genuine gap survives: **AC-2** — "a custom GridWorld environment is provided for tabular lessons." TASK-RL046 registered GridWorld-v0 but never wired it (or any custom env) into a tabular lesson: 1b still trains on FrozenLake and 3b still trains on Blackjack (verified live: zero GridWorld/SparseMaze/TreasureHuntEnv references in either notebook). GridWorld itself appears only as a `gym.make()` demo inside the theory notebook 0a. This task is narrowed to closing that one gap: add a from-scratch tabular Q-learning demonstration on the registered GridWorld-v0 environment to 1b (the MDP/tabular-DP lesson), alongside its existing FrozenLake work, so FEAT-RL3's AC-2 becomes genuinely MET without displacing 1b's existing pedagogical content.

## Acceptance criteria

- [ ] **AC-1** — 1b trains a tabular algorithm (e.g. Q-learning) against `gym.make('GridWorld-v0')`, using the 5-tuple step API and a seeded `reset(seed=...)` for reproducibility
- [ ] **AC-2** — 1b's GridWorld cell(s) execute cleanly top-to-bottom (zero error-type output cells, verified via an independent nbformat error-cell scan, not just the executor's exit code)
- [ ] **AC-3** — FEAT-RL3's AC-2 is updated to MET, citing this task's commit and the GridWorld-v0 cell added to 1b

## Dependencies

- Directive: DIRECT-RL1
- Features: FEAT-RL3

## Pre-mortem

### Failure modes

- Re-registering GridWorld-v0 inside 1b without a re-registration guard raises `gymnasium.error.Error: Cannot re-register id` if the cell is re-run in the same kernel — reuse 0a's guarded registration pattern (TASK-RL046) rather than a bare `gym.register()` call.
- Treating this as licence to replace 1b's existing FrozenLake work — AC-2's intent is an additional custom-env demonstration, not a rewrite of the existing lesson.

### Weak assumptions

- Assuming GridWorld-v0's action/observation space needs no adaptation to plug into 1b's existing tabular Q-learning code — verify 1b's algorithm loop against GridWorld's actual `action_space`/`observation_space` shapes before wiring it in, rather than assuming FrozenLake's shapes carry over.
