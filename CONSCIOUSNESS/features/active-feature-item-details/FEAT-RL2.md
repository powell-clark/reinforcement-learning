# FEAT-RL2: From-scratch NumPy plus Stable-Baselines3 dual implementation per lesson

## Kano
must-have

## Context
Each algorithm lesson pairs a from-scratch implementation (NumPy, or PyTorch for deep methods) with a production-framework reference (Stable-Baselines3), so learners see both the mechanics and the professional tool.

## Acceptance Criteria
- [x] **AC-1** — Each algorithm lesson ships a from-scratch implementation of its core algorithm (evidence: consistent across 0a bandit/GridWorld Q-learning, 1b policy/value iteration, 3b MC control, 7b DQN in PyTorch, 9b PPO in PyTorch, 13b tabular Q-learning + RND)
- [x] **AC-2** — Each algorithm lesson reproduces results with Stable-Baselines3 (or an equivalent framework) — MET: 1b and 3b gained real SB3 training (previously 1b only imported SB3 as an unrun "preview" and 3b had no SB3 usage at all) via TASK-RL045 (commits 37c9bff, af859db); 7b, 9b, and 13b already trained SB3 unconditionally (9b's earlier conditional try/except path was resolved by TASK-RL045 too). 0a, 0b, and 7a are theory/setup notebooks with no SB3 (or equivalent-framework) pairing expected — 0a is multi-armed bandit + GridWorld Q-learning with no natural SB3 equivalent, 0b/7a are pure-theory notebooks with no implementation to pair. X1 (RL debugging) is a Weights & Biases/TensorBoard workflow demo, not one of AC-1's six dual-implementation lessons, so it is excluded from this criterion.
- [x] **AC-3** — From-scratch and framework results are compared on the same environment — MET: 1b and 3b now run a genuine same-environment from-scratch-vs-SB3 comparison (TASK-RL045, commits 37c9bff, af859db), joining 7b, 9b, and 13b's pre-existing same-environment comparisons. 0a/0b/7a/X1 are excluded from this criterion for the same reasons given under AC-2.
- [x] **AC-4** — API differences between the from-scratch and framework versions are documented — MET: 1b already carried an "API differences: from-scratch vs. Stable-Baselines3" print-block section (TASK-RL045, commit 37c9bff); the same style of section, grounded in each notebook's own code, was added to 3b, 7b, 9b, and 13b (TASK-RL058). 0a/0b/7a/X1 are excluded from this criterion for the same reasons given under AC-2.

## Stories
STORY-RL2, STORY-RL3, STORY-RL4, STORY-RL5, STORY-RL6, STORY-RL7, STORY-RL8, STORY-RL9, STORY-RL10, STORY-RL11, STORY-RL12, STORY-RL13, STORY-RL14, STORY-RL15, STORY-RL16

## Links
- Directive: DIRECT-RL1 (Ship complete RL curriculum)
