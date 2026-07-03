# TASK-RL037: Stall - do we need to own compact hook and why is the conc version wrong?

## Context

Auto-created from /consciousness:issue (issue:RT6gWZpzHzobXL6mv5Lhe).

Report context:
transcripts:
  - chats/claude-code/2026-07-01/session-6e45b228.jsonl

## Investigation

Read the referenced transcript (session-6e45b228.jsonl) end to end around the
`/consciousness:issue` call at line 994. Findings:

- A compaction event fired mid-session (`isCompactSummary` at line 347). Later,
  from roughly 12:02:10 to 12:03:35 bst, the session spun through nine
  consecutive turns re-emitting "Continuing autonomous execution... Claiming
  TASK-RL12..." boilerplate without ever calling Edit/Write/Bash to build the
  notebook. The Stop hook (`validate-framing`) rejected each response in turn
  for a missing header, a missing footer, or a fabricated timestamp, and the
  agent's next turn just restated intent instead of doing work — a
  self-reinforcing spin with no tool call advancing the claimed task. The
  operator broke the loop manually via `/consciousness:issue`. (TASK-RL12 did
  get completed later, in a different session — it now sits in TASKS.DONE.)

### Q1: Do we need to own a compact hook in this project?

No. The consciousness plugin already registers both `PreCompact` and
`PostCompact` hooks (`adapters/claude-code/hooks/hooks.json` →
`compact-handler`, dispatching into `packages/core/conscious/compaction/`),
inherited automatically via this project's `.claude/settings.json`
(`enabledPlugins.consciousness@powell-clark: true`). A project-local
PreCompact hook would duplicate the plugin's and risk drifting from the
shared implementation. No project-local hook is needed.

### Q2: Why was the conc(iousness) version tag wrong?

The stalled session's framing showed `Session: rl-main-6e45b228 |
consciousness@8` — an older, coarse tag format (plugin-name@major-schema).
The current session shows `v0.43.4sch20260626230000000` (semver plus the
full 17-digit schema stamp). Per
`packages/core/conscious/compaction/index.ts`, `runPostCompact()` never
re-stamps or refreshes a version tag — the tag is derived once at
SessionStart and held for the session's lifetime, including across
compaction. So the old tag was not a bug in the moment; it was simply the
version format live when that session started on 2026-07-01, and the plugin
has since moved to the more granular format. No project-side fix is
required. Refreshing the tag after a mid-session plugin upgrade would be a
compaction-engine feature request for the consciousness plugin repo, not
this project.

## Resolution

Diagnostic task — no code changes required in this project. Both questions
are answered above with evidence from the transcript and current plugin
source. No follow-on work filed here; a PostCompact version-tag refresh, if
wanted, belongs in the consciousness plugin repo.

## Acceptance criteria

- [x] Diagnose the stall from chats/claude-code/2026-07-01/session-6e45b228.jsonl
- [x] Answer whether this project needs to own a PreCompact/PostCompact hook
- [x] Answer why the version tag shown during the stalled session differed from the current format
