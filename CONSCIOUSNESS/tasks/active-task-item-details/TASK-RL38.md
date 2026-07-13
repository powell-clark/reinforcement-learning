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

- [ ] Every task row carries the story_ids and feature_ids that claim it
- [ ] Every story lists exactly the tasks whose story_ids reference it
- [ ] Every feature lists exactly the tasks whose feature_ids reference it
- [ ] PGPS Rule 35b and Rule 35f back-link warnings clear

## Dependencies

- Directive: DIRECT-RL1 (Ship complete RL curriculum)
