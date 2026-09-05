# FEAT-RL7: Temporal Difference Learning (Lesson 4)

## Kano
must-have

## Context
Combining MC and DP by bootstrapping. TD(0), Sarsa, and Q-learning form the core of online model-free control.

## Acceptance Criteria
- [x] **AC-1** — TD(0) prediction implemented with the TD error explained (evidence: TASK-RL049 — `td_zero_prediction()` implemented and run in 4b_td_practical.ipynb per 4a's TD-error explanation, sample V(s) estimates printed and plausibility-checked)
- [x] **AC-2** — Sarsa (on-policy) and Q-learning (off-policy) implemented from scratch (evidence: 4b_td_practical.ipynb, sarsa() and qlearning() functions coded against the CliffWalking env)
- [x] **AC-3** — Expected Sarsa implemented; bias-variance tradeoff discussed (evidence: TASK-RL049 — `expected_sarsa()` implemented and run in 4b_td_practical.ipynb, mean-reward comparison printed against Sarsa/Q-learning; markdown ties the implementation back to 4a's bias-variance discussion)

## Stories
STORY-RL5

## Links
- Directive: DIRECT-RL1 (Ship complete RL curriculum)
- Cross-cutting: FEAT-RL1 (Colab), FEAT-RL2 (NumPy+SB3), FEAT-RL3 (Gymnasium)
