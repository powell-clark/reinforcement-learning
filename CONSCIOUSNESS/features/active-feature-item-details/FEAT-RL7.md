# FEAT-RL7: Temporal Difference Learning (Lesson 4)

## Kano
must-have

## Context
Combining MC and DP by bootstrapping. TD(0), Sarsa, and Q-learning form the core of online model-free control.

## Acceptance Criteria
- [ ] **AC-1** — TD(0) prediction implemented with the TD error explained — NOT MET: TD error is well explained (4a_td_theory.ipynb) but no code cell implements TD(0) V(s) prediction in either notebook; 4b only codes Sarsa/Q-learning control.
- [x] **AC-2** — Sarsa (on-policy) and Q-learning (off-policy) implemented from scratch (evidence: 4b_td_practical.ipynb, sarsa() and qlearning() functions coded against the CliffWalking env)
- [ ] **AC-3** — Expected Sarsa implemented; bias-variance tradeoff discussed — NOT MET: Expected Sarsa appears only as a formula in 4a_td_theory.ipynb, never implemented in code in either notebook, despite bias-variance tradeoff being well covered.

## Stories
STORY-RL5

## Links
- Directive: DIRECT-RL1 (Ship complete RL curriculum)
- Cross-cutting: FEAT-RL1 (Colab), FEAT-RL2 (NumPy+SB3), FEAT-RL3 (Gymnasium)
