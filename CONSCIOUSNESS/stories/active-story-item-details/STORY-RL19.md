# STORY-RL19: Bounded currency refresh cadence

## User Story
I want a bounded refresh cadence — library versions, datasets, and a full notebook execution sweep — so that the corpus keeps updating itself between operator visits rather than silently going stale.

## Context
The operator's charge frames the repo as "always updating itself." Today there is no scheduled or triggered refresh: notebooks were executed once at build time (DIRECT-RL1) and nothing re-checks pinned library versions, dataset availability, or execution health afterward. This story defines and runs that cadence.

## Acceptance Criteria
- [ ] A bounded cadence is defined (a stated interval or trigger condition, not "whenever"): what gets checked, how often or on what signal
- [ ] Library versions pinned in requirements.txt / notebook cells are checked against current upstream releases at least once under this story
- [ ] A full notebook execution sweep (all 36 notebooks, top-to-bottom, zero error-type output cells) runs at least once under this story
- [ ] Any drift found (breaking library release, dead dataset URL, execution failure) has a filed task

## Notebooks
Sweep target: all 36 built notebooks.

## Dependencies
- Blocked by: none
- Blocks: none

## Links
- Directive: DIRECT-RL2 (Maintain the curriculum as a living Feynman-style corpus)
- Features: none yet
