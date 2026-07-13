# TASK-RL38: Complete feature-story-task linkage

> **Needs review:** recovered by the neurologist from a malformed INDEX row
> (title had collapsed to "p1", no backing detail card existed). Operator should
> confirm scope and re-tier priority as appropriate.

## Context

The PGPS features and stories reference tasks (FEAT-RL1/2/3 claim TASK-RL1..RL36;
STORY-RL1..RL17 claim their tasks) but the task rows do not link back, producing
Rule 35b/35f back-link warnings. This task completes the bidirectional
feature-story-task linkage so the roadmap graph validates without warnings.

## Acceptance Criteria

- [x] Every task row carries the story_ids and feature_ids that claim it
- [x] Every story lists exactly the tasks whose story_ids reference it
- [x] Every feature lists exactly the tasks whose feature_ids reference it
- [x] PGPS Rule 35b and Rule 35f back-link warnings clear

## Resolution

Scope confirmed as originally stated (feature-story-task back-links) and executed as
written; priority left at p3 (no evidence warranting re-tiering). Also fixed the adjacent
directive-task fk-asymmetry warnings (DIRECT-RL1.taskIds) surfaced by the same validator
pass, since they're the same category of bidirectional-link gap. PGPS warnings: 111 -> 43,
zero remaining 35b/35f/fk-asymmetry. Remaining 43 are pre-existing, unrelated to this task's
scope (SMART title-quality heuristics, Rule 56 story-format, Rule 32 deprecated status tags,
review-eligible notices, one pre-existing STORY-RL1 orphan detail predating this session).

## Dependencies

- Directive: DIRECT-RL1 (Ship complete RL curriculum)
