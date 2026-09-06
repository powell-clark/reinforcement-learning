# STORY-RL18: Style conformance audit against the operator's Feynman lessons

## User Story
I want every lesson audited against the operator's own supervised-learning lessons 1A, 1B, 2A, 2B, 2C, and 3 onward so that the whole curriculum holds one consistent teaching voice: Richard Feynman first-principles, performable by a rusty 18-year-old with good A-level maths (not further maths), and runnable end to end.

## Context
DIRECT-RL1 (Ship complete RL curriculum) verified algorithmic correctness — from-scratch NumPy implementations, Bellman-equation derivations, Gymnasium integration — but never checked voice or pedagogical register against the operator's reference lessons in the supervised-machine-learning repo. This story is the standing audit that closes that gap and keeps closing it as lessons or the reference series change.

## Acceptance Criteria
- [ ] Every one of the 20 lesson notebook pairs (Lesson 0–15, X1–X4) has a recorded conformance verdict against supervised-machine-learning lessons 1A, 1B, 2A, 2B, 2C, and 3 onward, on: Feynman voice, first-principles derivation, performability by a rusty 18-year-old with good A-level (not further) maths, and end-to-end runnability
- [ ] Each lesson that falls short on any axis has a filed refinement task (TASK-RL#, story STORY-RL18) naming the specific shortfall
- [ ] The audit method (what "Feynman voice" and "A-level, not further" mean operationally) is written down once so repeat audits are consistent, not re-litigated per lesson

## Notebooks
Audit target: all 36 built notebooks (Lessons 0–15 theory+practical, X1–X4).

## Dependencies
- Blocked by: none — DIRECT-RL1's 36/36 build is complete
- Blocks: none

## Links
- Directive: DIRECT-RL2 (Maintain the curriculum as a living Feynman-style corpus)
- Features: none yet — filed as audit findings land
