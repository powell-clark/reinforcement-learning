# FEAT-RL20: MDP lesson exercise and correctness review

## Kano
must-have

## Context
FEAT-RL4 (Markov Decision Processes) verifies the MDP tuple, Bellman equations, and a from-scratch solver — pure algorithmic correctness. It carries no acceptance criterion for a learner-facing objective, a checked-answer exercise, or an independent correctness review of that exercise's answer. `1b_mdp_practical.ipynb` already contains 3 exercises (non-slippery FrozenLake comparison, discount-factor sensitivity sweep, reward-scaling experiment) but each ends in a printed "Observation:" line rather than an automated check — a learner can run the cell, see any output, and never know whether their answer was right. This feature adds that missing pedagogical layer on top of the existing algorithmic implementation.

## Acceptance Criteria
- [x] **AC-1** — Learning objective: `1a_mdp_theory.ipynb`'s introduction states an explicit, learner-facing "Learning Objective" (not just an informal "in this lesson we'll..." list). MET: TASK-RL060, commit 2df18cd.
- [x] **AC-2** — Exercise with checked answer: `1b_mdp_practical.ipynb`'s Exercise 1 (non-slippery FrozenLake comparison) is extended with an automated check that verifies the learner's `V_noslip`/`policy_noslip` result, replacing reliance on the printed "Observation:" prose alone. MET: TASK-RL060, commit eb0bcbe, cells 32-33; executed output prints "PASS: V_noslip satisfies the Bellman optimality equation and policy_noslip is greedy w.r.t. it." with residual 0.00e+00.
- [x] **AC-3** — Correctness review: the check's own reference is independently derived from the Bellman optimality equation directly, not by re-invoking the same `value_iteration()` call that produced the value under test. MET: TASK-RL060, commit eb0bcbe; `bellman_q()` in cell 33 loops `P_noslip[s][a].items()` directly and never calls `value_iteration()`.
- [x] **AC-4** — Runnable code: `1a_mdp_theory.ipynb` and `1b_mdp_practical.ipynb` execute top-to-bottom with zero error-type output cells after the above changes, verified via an independent nbformat scan. MET: TASK-RL060, `jupyter nbconvert --execute --inplace` on both (commit eb0bcbe), followed by a standalone nbformat scan of `outputs[].output_type == 'error'` across both notebooks returning zero matches.

## Stories
STORY-RL2

## Links
- Directive: DIRECT-RL1 (Ship complete RL curriculum)
- Related: FEAT-RL4 (Markov Decision Processes (Lesson 1))
