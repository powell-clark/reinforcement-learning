# FEAT-RL10: Deep Q-Networks (Lesson 7)

## Kano
must-have

## Context
Deep learning meets RL. Experience replay and fixed targets enable stable learning in high-dimensional state spaces.

## Acceptance Criteria
- [x] **AC-1** — DQN derived with experience replay and fixed Q-targets (evidence: 7a_deep_q_networks.ipynb, Experience Replay / Fixed Q-Targets loss-function derivation cells)
- [x] **AC-2** — From-scratch DQN in PyTorch trains on CartPole (evidence: commit `6fce882` re-executed 7b_dqn_practical.ipynb end to end; training cell [9] exec_count=5, 0 errors, converges Avg Return 14.4→173.4 over episodes 50-300; TASK-RL051 verified this against the live notebook JSON, not just the commit message)
- [x] **AC-3** — Double, Dueling, and Prioritized-Replay DQN variants explained; SB3 DQN reproduced (evidence: variants explained in 7a_deep_q_networks.ipynb; SB3 comparison cell [15] in 7b, exec_count=8, 0 errors, reports "Our DQN: 155.0 ± 5.2, SB3 DQN: 284.5 ± 45.0" — reproduction confirmed via commit `6fce882`, verified by TASK-RL051)

## Stories
STORY-RL8

## Links
- Directive: DIRECT-RL1 (Ship complete RL curriculum)
- Cross-cutting: FEAT-RL1 (Colab), FEAT-RL2 (NumPy+SB3), FEAT-RL3 (Gymnasium)
