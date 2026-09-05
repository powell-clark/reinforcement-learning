# FEAT-RL4: Markov Decision Processes (Lesson 1)

## Kano
must-have

## Context
Formal mathematical foundation of RL. The MDP tuple and Bellman equations underpin every algorithm that follows.

## Acceptance Criteria
- [x] **AC-1** — MDP tuple (S, A, P, R, gamma) formally defined (evidence: 1a_mdp_theory.ipynb, "Formal Definition" section + MDP class)
- [x] **AC-2** — Bellman expectation and optimality equations derived step by step (evidence: TASK-RL047, commit ebe2a15, 1a_mdp_theory.ipynb cell 12 — derives V^π and Q^π from G_t via linearity of expectation and the law of total expectation, then derives V*/Q* from V*(s)=max_a Q*(s,a))
- [x] **AC-3** — V(s) and Q(s,a) value functions defined and related (evidence: 1a_mdp_theory.ipynb, Bellman Equations section defining V^π and Q^π, with Q nested inside V's summation and V*/Q* related via max)
- [x] **AC-4** — A from-scratch MDP solver produces optimal policies on small MDPs (evidence: TASK-RL047, commit ebe2a15 — MDPSolver.value_iteration() executed on student_mdp, converged in 154 iterations to V(S)=42.1053/V(L)=100.0000, π=Study in both states; hand-verified exact match against the MDP's own reward structure)

## Stories
STORY-RL2

## Links
- Directive: DIRECT-RL1 (Ship complete RL curriculum)
- Cross-cutting: FEAT-RL1 (Colab), FEAT-RL2 (NumPy+SB3), FEAT-RL3 (Gymnasium)
