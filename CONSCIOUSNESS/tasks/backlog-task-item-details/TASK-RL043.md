# TASK-RL043: Wire reinforcement-learning sibling channel to EGLPK bus

## Context

Superseded — duplicate filing. This card was minted here by mistake: CCC's
append-task-cli.js resolves its target repo from the invoking process's
current working directory rather than from the invoked script's own path, so
running it while cwd was still this RL checkout filed it into RL's own
backlog instead of CCC's. The correctly-targeted card for this same defect
is TASK-CCC31371 (Wire reinforcement-learning sibling channel to EGLPK bus)
in the consciousness repo, commit 3039456adea48db3f4c3ed7b9167a4180348085f.
The cwd-detection defect itself is filed separately. Leaving this card in
place rather than cancelling it (cancellations are operator-only) — track
and work the defect via TASK-CCC31371, not here.

reinforcement-learning (RL) has no federation.siblings entry in its CONSCIOUSNESS/config.json and no RL->EGLPK channel declared in ~/.claude/federation-router.md (only streams:rl-epc, RL->EPC, exists). An operator ruling for RL requires posting a one-line bus row to EGLPK with the commit SHA after every merge. bus-send.mjs --to EGLPK --from RL run from the RL repo fails: 'Bus send refused: EGLPK addresses no consumer of the target bus... Live addresses in the target repo: <RL session id>' -- it resolves against RL's own local bus instead of routing cross-repo, because no sibling/channel wiring exists. Reproduced twice across two sessions (2026-09-05), same failure both times, exit 1. Fix: add RL to federation.siblings in RL's config.json and declare an RL->EGLPK channel (or route via EPC) in federation-router.md, then verify bus-send.mjs --to EGLPK --from RL succeeds from the RL repo.

## Acceptance criteria

- [ ] _(to be filled in)_

## Dependencies

- _(to be filled in)_

## Pre-mortem

### Failure modes

- _(to be filled in)_

### Weak assumptions

- _(to be filled in)_
