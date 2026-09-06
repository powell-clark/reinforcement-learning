# FEAT-RL23: Temporal difference exercise and correctness review

## Kano
must-have

## Context
FEAT-RL7 (Temporal Difference Learning, Lesson 4) verifies TD(0), SARSA, and Q-learning are correctly implemented — pure algorithmic correctness. It carries no acceptance criterion for a learner-facing objective, a checked-answer exercise, or an independent correctness review of that exercise's answer, mirroring the gap closed for Lesson 1 by FEAT-RL20.

## Acceptance Criteria
- [ ] **AC-1** — Learning objective: `4a_td_theory.ipynb`'s introduction states an explicit, learner-facing "Learning Objective"
- [ ] **AC-2** — Exercise with checked answer: `4b_td_practical.ipynb`'s exercise section includes an automated check/assertion verifying the learner's computed answer against a known-correct value, not merely a printed observation
- [ ] **AC-3** — Correctness review: the check's own reference value is independently verified against a second, non-self-referential method or ground-truth source
- [ ] **AC-4** — Runnable code: `4a_td_theory.ipynb` and `4b_td_practical.ipynb` execute top-to-bottom with zero error-type output cells after the above changes, verified via an independent nbformat scan

## Stories
STORY-RL5

## Links
- Directive: DIRECT-RL1 (Ship complete RL curriculum)
- Related: FEAT-RL7 (Temporal Difference Learning (Lesson 4))
