# FEAT-RL15: Multi-Agent RL (Lesson 12)

## Kano
must-have

## Context
Multiple agents learning in cooperative, competitive, and mixed settings. CTDE and Nash equilibria govern multi-agent training.

## Acceptance Criteria
- [x] **AC-1** — Cooperative/competitive/mixed settings and Nash equilibria explained (evidence: 12a_marl_theory.ipynb Parts 1-2, Markov game formalism + Nash equilibrium definition with find_pure_nash run on Prisoner's Dilemma/Matching Pennies)
- [ ] **AC-2** — Independent Q-learning and CTDE implemented — NOT MET: IQL is genuinely trained (RPS via PettingZoo), but CTDE is only an untrained toy sketch in the theory notebook, and the practical notebook implements parameter-sharing explicitly labeled "CTDE-adjacent," not a trained centralized-critic/decentralized-actor loop.
- [x] **AC-3** — Multi-agent training loops run on PettingZoo environments (evidence: 12b_marl_practical.ipynb, RPS AEC loop + Pursuit parallel-API DQN-lite training + SuperSuit/SB3 PPO loop, all with real printed/plotted results)

## Stories
STORY-RL13

## Links
- Directive: DIRECT-RL1 (Ship complete RL curriculum)
- Cross-cutting: FEAT-RL1 (Colab), FEAT-RL2 (NumPy+SB3), FEAT-RL3 (Gymnasium)
