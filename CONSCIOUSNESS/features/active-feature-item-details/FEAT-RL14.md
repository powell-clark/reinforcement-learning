# FEAT-RL14: Model-Based RL (Lesson 11)

## Kano
must-have

## Context
Learning and planning. Dyna, Monte Carlo tree search, and world models enable sample-efficient learning through explicit planning.

## Acceptance Criteria
- [x] **AC-1** — Dyna-Q implemented from scratch (integrated planning and learning) (evidence: 11b_model_based_practical.ipynb, DynaQAgent trained on GridWorld vs. plain Q-learning, steps-to-goal comparison plot)
- [x] **AC-2** — Model learning framed as supervised learning within RL (evidence: 11b_model_based_practical.ipynb Part 1, ForwardModel trained via MSE regression on collected transitions, with real-vs-model rollout sanity-check plot)
- [x] **AC-3** — MCTS and AlphaZero-style planning introduced (evidence: 11b_model_based_practical.ipynb Part 4-5, working MCTSNode/mcts_search run on CartPole with the true simulator, plus PUCTNode/puct_search AlphaZero-style sketch executed)

## Stories
STORY-RL12

## Links
- Directive: DIRECT-RL1 (Ship complete RL curriculum)
- Cross-cutting: FEAT-RL1 (Colab), FEAT-RL2 (NumPy+SB3), FEAT-RL3 (Gymnasium)
