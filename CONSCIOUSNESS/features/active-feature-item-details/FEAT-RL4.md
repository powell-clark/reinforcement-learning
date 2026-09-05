# FEAT-RL4: Markov Decision Processes (Lesson 1)

## Kano
must-have

## Context
Formal mathematical foundation of RL. The MDP tuple and Bellman equations underpin every algorithm that follows.

## Acceptance Criteria
- [x] **AC-1** — MDP tuple (S, A, P, R, gamma) formally defined (evidence: 1a_mdp_theory.ipynb, "Formal Definition" section + MDP class)
- [ ] **AC-2** — Bellman expectation and optimality equations derived step by step — NOT MET: equations are presented as given formulas with an interpretation, never derived step by step from the return definition G_t.
- [x] **AC-3** — V(s) and Q(s,a) value functions defined and related (evidence: 1a_mdp_theory.ipynb, Bellman Equations section defining V^π and Q^π, with Q nested inside V's summation and V*/Q* related via max)
- [ ] **AC-4** — A from-scratch MDP solver produces optimal policies on small MDPs — NOT MET: MDPSolver.value_iteration() code is real and correct, but the code cell in 1a_mdp_theory.ipynb has no stored execution output, so there is no evidence it was ever run or actually produced the claimed optimal policy.

## Stories
STORY-RL2

## Links
- Directive: DIRECT-RL1 (Ship complete RL curriculum)
- Cross-cutting: FEAT-RL1 (Colab), FEAT-RL2 (NumPy+SB3), FEAT-RL3 (Gymnasium)
