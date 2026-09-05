# TASK-RL056: Fix 9b PPOAgent update shape bug

## Context

notebooks/9b_ppo_practical.ipynb cell 10 (the from-scratch PPO training loop, pre-existing, not part of TASK-RL044 scope) raises RuntimeError: The size of tensor a (64) must match the size of tensor b (6) at non-singleton dimension 1, inside PPOAgent.update() at 'ratio = torch.exp(log_probs - log_probs_old_batch)'. Root cause: PPOAgent.select_action() returns the raw per-action-dimension log-prob (dist.log_prob(action), shape (6,) for HalfCheetah's 6-dim continuous action space) without summing across action dimensions, while PPOAgent.update() computes the properly summed joint log-prob (dist.log_prob(actions_batch).sum(dim=1), shape (64,) per batch) and then subtracts the un-summed stored log_probs_old_batch (shape (64,6)) from it, producing a shape mismatch. Fix: sum select_action's returned log_prob across the action dimension (dist.log_prob(action).sum(-1)) before storing it, matching update()'s convention. Discovered while re-executing 9b for TASK-RL044 AC-5 (full top-to-bottom execution with outputs retained); out of scope for that task's pre-mortem carve-out. Diagnosed via allow_errors=True re-execution isolating the failure to cell 10 only; cells 2 and 12 (the TASK-RL044 edits) execute cleanly.

## Acceptance criteria

- [ ] _(to be filled in)_

## Dependencies

- _(to be filled in)_

## Pre-mortem

### Failure modes

- _(to be filled in)_

### Weak assumptions

- _(to be filled in)_
