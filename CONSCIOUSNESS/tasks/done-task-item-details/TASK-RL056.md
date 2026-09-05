# TASK-RL056: Fix 9b PPOAgent update shape bug

## Context

notebooks/9b_ppo_practical.ipynb cell 10 (the from-scratch PPO training loop, pre-existing, not part of TASK-RL044 scope) raises RuntimeError: The size of tensor a (64) must match the size of tensor b (6) at non-singleton dimension 1, inside PPOAgent.update() at 'ratio = torch.exp(log_probs - log_probs_old_batch)'. Root cause: PPOAgent.select_action() returns the raw per-action-dimension log-prob (dist.log_prob(action), shape (6,) for HalfCheetah's 6-dim continuous action space) without summing across action dimensions, while PPOAgent.update() computes the properly summed joint log-prob (dist.log_prob(actions_batch).sum(dim=1), shape (64,) per batch) and then subtracts the un-summed stored log_probs_old_batch (shape (64,6)) from it, producing a shape mismatch. Fix: sum select_action's returned log_prob across the action dimension (dist.log_prob(action).sum(-1)) before storing it, matching update()'s convention. Discovered while re-executing 9b for TASK-RL044 AC-5 (full top-to-bottom execution with outputs retained); out of scope for that task's pre-mortem carve-out. Diagnosed via allow_errors=True re-execution isolating the failure to cell 10 only; cells 2 and 12 (the TASK-RL044 edits) execute cleanly.

## Acceptance criteria

- [ ] `PPOAgent.select_action` in notebooks/9b_ppo_practical.ipynb sums the per-action-dimension log-prob across the action dimension (`.sum(-1)`) before returning it, matching `update()`'s convention.
- [ ] notebooks/9b_ppo_practical.ipynb cell 10 (the from-scratch PPO training loop over HalfCheetah-v4) executes with no RuntimeError or other unhandled exception.
- [ ] The full notebook is re-executed top-to-bottom with `allow_errors=False` and outputs retained, confirming zero error cells across all cells (including cell 12's SB3 comparison, unaffected by this change).

## Dependencies

- Directive: DIRECT-RL1
- Features: FEAT-RL1

## Pre-mortem

### Failure modes

- Summing at the wrong point (e.g. inside `update()` a second time) would double-apply the sum and silently change the PPO ratio's numerical scale rather than just fixing the shape mismatch — the fix must land only in `select_action`, once.
- Squeezing/reshaping post-hoc during `update()` reading (e.g. slicing to one dim) could mask the shape bug without actually producing a valid joint log-prob, running clean while training an incorrect policy gradient.

### Weak assumptions

- Assumes HalfCheetah-v4 (via `gymnasium[mujoco]`, already installed by TASK-RL044's cell 2 pip-install cell) is available in this execution environment; verified true this session since TASK-RL044 already executed this same notebook's other cells successfully.
- Assumes no other cell reads `log_probs` expecting the un-summed per-dimension shape; verified by inspection — `update()` is the only consumer and already expects the summed shape.
