# FEAT-RL6: Monte Carlo Methods (Lesson 3)

## Kano
must-have

## Context
Learning from complete episodes without a model. Introduces model-free prediction and control via importance sampling.

## Acceptance Criteria
- [ ] **AC-1** — First-visit and every-visit MC prediction implemented — NOT MET: only every-visit MC is coded (3b_mc_practical.ipynb mc_prediction()); first-visit is illustrated with a hand-worked numeric example in 3a, never implemented as running code.
- [x] **AC-2** — MC control with exploring starts and epsilon-greedy policies implemented (evidence: 3b_mc_practical.ipynb, mc_control_exploring_starts() and mc_control_epsilon_greedy() functions coded against the Blackjack env)
- [x] **AC-3** — On-policy vs off-policy explained with importance sampling (evidence: 3a_mc_theory.ipynb, "Off-Policy Learning" and "Importance Sampling" sections with the ratio derivation)

## Stories
STORY-RL4

## Links
- Directive: DIRECT-RL1 (Ship complete RL curriculum)
- Cross-cutting: FEAT-RL1 (Colab), FEAT-RL2 (NumPy+SB3), FEAT-RL3 (Gymnasium)
