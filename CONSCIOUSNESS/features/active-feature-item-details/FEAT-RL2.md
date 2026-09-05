# FEAT-RL2: From-scratch NumPy plus Stable-Baselines3 dual implementation per lesson

## Kano
must-have

## Context
Each algorithm lesson pairs a from-scratch implementation (NumPy, or PyTorch for deep methods) with a production-framework reference (Stable-Baselines3), so learners see both the mechanics and the professional tool.

## Acceptance Criteria
- [x] **AC-1** — Each algorithm lesson ships a from-scratch implementation of its core algorithm (evidence: consistent across 0a bandit/GridWorld Q-learning, 1b policy/value iteration, 3b MC control, 7b DQN in PyTorch, 9b PPO in PyTorch, 13b tabular Q-learning + RND)
- [ ] **AC-2** — Each algorithm lesson reproduces results with Stable-Baselines3 (or an equivalent framework) — NOT MET: 1b imports SB3 but never trains/compares it ("this is a preview"); 3b has no SB3 or equivalent-framework usage at all for MC control.
- [ ] **AC-3** — From-scratch and framework results are compared on the same environment — NOT MET: an actual same-environment from-scratch-vs-SB3 comparison only occurs in 7b (and conditionally in 9b behind a try/except); 1b and 3b never run the comparison.
- [ ] **AC-4** — API differences between the from-scratch and framework versions are documented — NOT MET: no notebook in the sample (0a, 0b, 1b, 3b, 7a, 7b, 9b, 13b, X1) contains a section documenting API differences between the custom implementation and SB3's API.

## Stories
STORY-RL2, STORY-RL3, STORY-RL4, STORY-RL5, STORY-RL6, STORY-RL7, STORY-RL8, STORY-RL9, STORY-RL10, STORY-RL11, STORY-RL12, STORY-RL13, STORY-RL14, STORY-RL15, STORY-RL16

## Links
- Directive: DIRECT-RL1 (Ship complete RL curriculum)
