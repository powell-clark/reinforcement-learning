# FEAT-RL15: Multi-Agent RL (Lesson 12)

## Kano
must-have

## Context
Multiple agents learning in cooperative, competitive, and mixed settings. CTDE and Nash equilibria govern multi-agent training.

## Acceptance Criteria
- [x] **AC-1** — Cooperative/competitive/mixed settings and Nash equilibria explained (evidence: 12a_marl_theory.ipynb Parts 1-2, Markov game formalism + Nash equilibrium definition with find_pure_nash run on Prisoner's Dilemma/Matching Pennies)
- [x] **AC-2** — Independent Q-learning and CTDE implemented — MET (TASK-RL055): IQL is genuinely trained (RPS via PettingZoo); 12b_marl_practical.ipynb cell-11 now adds a genuine trained CTDE loop — separately-parameterized `DecentralizedActor` per pursuer (no weight sharing) plus a `CentralizedCritic` on the joint observation, trained with real per-step TD(0) advantage actor-critic gradient updates on the same pursuit_v4 config as the DQN baseline. Evidence: "CTDE -- First 10 episodes mean team return: -10.0" -> "CTDE -- Last 10 episodes mean team return: -6.4" (500 episodes), notebook executed top-to-bottom with 0 error cells.
- [x] **AC-3** — Multi-agent training loops run on PettingZoo environments (evidence: 12b_marl_practical.ipynb, RPS AEC loop + Pursuit parallel-API DQN-lite training + SuperSuit/SB3 PPO loop, all with real printed/plotted results)

## Stories
STORY-RL13

## Links
- Directive: DIRECT-RL1 (Ship complete RL curriculum)
- Cross-cutting: FEAT-RL1 (Colab), FEAT-RL2 (NumPy+SB3), FEAT-RL3 (Gymnasium)
