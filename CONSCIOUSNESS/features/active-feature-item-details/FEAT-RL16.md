# FEAT-RL16: Exploration Strategies (Lesson 13)

## Kano
must-have

## Context
Principled exploration beyond epsilon-greedy. UCB, Thompson sampling, and intrinsic motivation enable solving hard, sparse-reward tasks.

## Acceptance Criteria
- [x] **AC-1** — UCB and Thompson sampling explained and implemented (evidence: 13a_exploration_theory.ipynb Parts 2-3, run_ucb1/run_thompson implemented and compared against epsilon-greedy via regret-curve plot on a 10-armed bandit)
- [x] **AC-2** — Curiosity-driven and count-based exploration covered (evidence: 13a Part 4 formulas + 13b_exploration_practical.ipynb Part 2, count-based bonus tabular Q-learning with plotted plain-vs-bonus success-rate comparison)
- [x] **AC-3** — Random Network Distillation combined with PPO on a sparse-reward task (evidence: 13b_exploration_practical.ipynb Part 3, RNDWrapper + SB3 PPO trained across 6 seeds vs. plain-PPO baseline on SparseMaze)

## Stories
STORY-RL14

## Links
- Directive: DIRECT-RL1 (Ship complete RL curriculum)
- Cross-cutting: FEAT-RL1 (Colab), FEAT-RL2 (NumPy+SB3), FEAT-RL3 (Gymnasium)
