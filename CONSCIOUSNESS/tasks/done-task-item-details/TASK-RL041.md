# TASK-RL041: Deep-learning build supervisor counted a dead, rate-limited builder seat as live for 90+ minutes, freezing new seat starts

> **Needs review:** the agent created this task during real-time validation and is uncertain about scope or priority. Operator should review and re-tier as appropriate.

## Context

Auto-created from /consciousness:issue (issue:5aL-4uUFKw4HKDtOHcyMA).

Report context:
Sibling repo, not this one: /home/powell-clark/projects/auxiliary/deep-learning.
scripts/supervisor.sh launches Sonnet builder seats via 'claude --bg' on a 15-minute cron tick,
bounded by MAX_BUILDERS=1 via a census over 'claude agents --json'. Seat dl-builder-022304 hit
the account's rolling Claude subscription usage cap mid-task at 02:11 BST (HTTP 429,
"You've hit your session limit - resets 7am (Europe/London)", model claude-sonnet-5), and its
process then exited (confirmed via ps -ef, no matching pid, no bg-spare/pty-host/daemon chain).
'claude agents --json' kept reporting it as state=blocked with no live process for 90+ minutes
across six 15-minute ticks, and the supervisor's seat census counted 'blocked' as live (it only
excluded the terminal states done/failed/killed/stopped/cancelled/error), so MAX_BUILDERS stayed
pinned at 1 the whole time while 17 unblocked layer-0 tasks sat idle and every tick logged
'nothing to start'.
Root cause: 'claude agents --json' has no state that distinguishes a genuinely dead background
session from one that is transiently blocked and might resume - 'blocked' means both. A consumer
building a supervisor on top of this census has no reliable non-terminal signal to treat as
dead. Worked around in the consuming repo by treating 'blocked' as non-live for seats launched
with --permission-mode bypassPermissions (such a seat can never be legitimately blocked on a
permission prompt, so 'blocked' can only mean stalled-or-dead for them) - see deep-learning
commit 0d16121. That workaround is seat-launch-config-specific; a session without
bypassPermissions genuinely can be blocked-and-alive on a real prompt, so the same fix would be
wrong there. A cleaner fix would be for 'claude agents --json' to expose either a last-heartbeat
timestamp or a distinct terminal-like state once the underlying process has actually exited.
transcripts:
  - chats/claude-code/2026-09-05/session-237716d8.jsonl

## Acceptance criteria

- [x] Consuming-repo fix shipped and verified live — deep-learning `scripts/supervisor.sh` excludes `blocked` from its live-seat census for `--permission-mode bypassPermissions` seats (commit `0d16121`, pushed to `origin/main`); confirmed live by manually running the supervisor and observing a real seat start (`dl-builder-040211`) immediately afterwards
- [x] Upstream defect filed against the owning plugin — `claude agents --json`'s `blocked` state conflates "transiently blocked, may resume" with "process exited, permanently dead", with no distinguishing signal (no heartbeat, no dead-adjacent terminal state); filed as https://github.com/powell-clark/consciousness/issues/2240
- [x] Duplicate roadmap entry (TASK-RL040, minted by a mistaken retry that passed an unauthorised `--no-gh` flag) closed with a bypass-approved verdict pointing back here

## Dependencies

- None outstanding — the fix, the upstream filing, and the dedup are all complete

## Pre-mortem

### Failure modes

- The upstream `blocked`-state ambiguity is still unresolved in the plugin itself; any future consumer seat NOT launched with `bypassPermissions` remains exposed to the same misclassification and cannot use this workaround (a real permission-wait seat legitimately reports `blocked`) — tracked for the plugin maintainer via the filed GitHub issue, not further scoped here

### Weak assumptions

- Assumes deep-learning's builder seats are launched exclusively with `--permission-mode bypassPermissions` (true as of `supervisor.sh`'s current `start_seat()`); if that ever changes, the exclusion in commit `0d16121` would need re-scoping
