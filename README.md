# Reinforcement Learning

A university-grade curriculum for reinforcement learning, from Markov decision processes and
dynamic programming through deep Q-networks, policy gradients, PPO and continuous control. Every
method is derived from first principles, implemented from scratch in NumPy or PyTorch, then checked
against Stable-Baselines3 or another production library. All notebooks run in Google Colab with no
local setup.

## The series

Four repositories, one curriculum. The first three are *how* a model learns; the fourth is *what*
it is built from, and cuts across all three.

- [Supervised learning](https://github.com/powell-clark/supervised-learning) — learning from labelled examples
- [Unsupervised learning](https://github.com/powell-clark/unsupervised-learning) — finding structure with no labels
- **[Reinforcement learning](https://github.com/powell-clark/reinforcement-learning)** — learning from reward (you are here)
- [Deep learning & transformers](https://github.com/powell-clark/deep-learning) — the architecture the other three can each be built on

**Status:** 20 of 20 lessons complete (36 notebooks)

## Overview

- **From First Principles**: every algorithm derived from MDPs and the Bellman equations, not quoted
- **Dual Structure**: theory (a) + practical (b) notebooks for each lesson
- **Interactive Environments**: hands-on work in Gymnasium and PettingZoo
- **Complete Implementations**: from scratch first, then production libraries
- **Google Colab Compatible**: runs in the browser, no local setup

## Lesson catalog

#### Foundations

- **Lesson 0**: Introduction to Reinforcement Learning
  - [`0a_rl_introduction_theory.ipynb`](notebooks/0a_rl_introduction_theory.ipynb) — the agent-environment loop, rewards and returns, and how RL differs from supervised and unsupervised learning [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/reinforcement-learning/blob/main/notebooks/0a_rl_introduction_theory.ipynb)
  - [`0b_gymnasium_setup_practical.ipynb`](notebooks/0b_gymnasium_setup_practical.ipynb) — the Gymnasium environment API that every later lesson builds on [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/reinforcement-learning/blob/main/notebooks/0b_gymnasium_setup_practical.ipynb)
- **Lesson 1**: Markov Decision Processes
  - [`1a_mdp_theory.ipynb`](notebooks/1a_mdp_theory.ipynb) — states, actions, transitions, value functions and the Bellman equations, derived [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/reinforcement-learning/blob/main/notebooks/1a_mdp_theory.ipynb)
  - [`1b_mdp_practical.ipynb`](notebooks/1b_mdp_practical.ipynb) — policy evaluation, policy iteration and value iteration on FrozenLake, compared [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/reinforcement-learning/blob/main/notebooks/1b_mdp_practical.ipynb)
- **Lesson 2**: Dynamic Programming
  - [`2a_dp_theory.ipynb`](notebooks/2a_dp_theory.ipynb) — why policy iteration and value iteration converge [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/reinforcement-learning/blob/main/notebooks/2a_dp_theory.ipynb)
  - [`2b_dp_practical.ipynb`](notebooks/2b_dp_practical.ipynb) — in-place, asynchronous and prioritised-sweeping updates on a custom GridWorld, benchmarked [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/reinforcement-learning/blob/main/notebooks/2b_dp_practical.ipynb)

#### Tabular Methods

- **Lesson 3**: Monte Carlo Methods
  - [`3a_mc_theory.ipynb`](notebooks/3a_mc_theory.ipynb) — learning values and policies from complete episodes, without a model [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/reinforcement-learning/blob/main/notebooks/3a_mc_theory.ipynb)
  - [`3b_mc_practical.ipynb`](notebooks/3b_mc_practical.ipynb) — Monte Carlo prediction and control on Blackjack, with exploring starts and epsilon-greedy policies [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/reinforcement-learning/blob/main/notebooks/3b_mc_practical.ipynb)
- **Lesson 4**: Temporal-Difference Learning
  - [`4a_td_theory.ipynb`](notebooks/4a_td_theory.ipynb) — bootstrapping, the TD error, Sarsa and Q-learning [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/reinforcement-learning/blob/main/notebooks/4a_td_theory.ipynb)
  - [`4b_td_practical.ipynb`](notebooks/4b_td_practical.ipynb) — Sarsa against Q-learning, TD(0) prediction, expected Sarsa and hyperparameter sensitivity [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/reinforcement-learning/blob/main/notebooks/4b_td_practical.ipynb)
- **Lesson 5**: N-Step Methods and Eligibility Traces
  - [`5a_nstep_eligibility.ipynb`](notebooks/5a_nstep_eligibility.ipynb) — n-step returns, TD(λ) and eligibility traces [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/reinforcement-learning/blob/main/notebooks/5a_nstep_eligibility.ipynb)
  - [`5b_nstep_eligibility_practical.ipynb`](notebooks/5b_nstep_eligibility_practical.ipynb) — Sarsa(λ) on a random walk and on MountainCar [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/reinforcement-learning/blob/main/notebooks/5b_nstep_eligibility_practical.ipynb)

#### Function Approximation and Deep RL

- **Lesson 6**: Function Approximation
  - [`6a_function_approximation.ipynb`](notebooks/6a_function_approximation.ipynb) — from tables to features: linear and neural value functions, and why convergence gets harder [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/reinforcement-learning/blob/main/notebooks/6a_function_approximation.ipynb)
  - [`6b_function_approximation_practical.ipynb`](notebooks/6b_function_approximation_practical.ipynb) — tile coding against a neural-network approximator for on-policy control [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/reinforcement-learning/blob/main/notebooks/6b_function_approximation_practical.ipynb)
- **Lesson 7**: Deep Q-Networks
  - [`7a_deep_q_networks.ipynb`](notebooks/7a_deep_q_networks.ipynb) — experience replay and target networks, the two tricks that stabilise DQN [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/reinforcement-learning/blob/main/notebooks/7a_deep_q_networks.ipynb)
  - [`7b_dqn_practical.ipynb`](notebooks/7b_dqn_practical.ipynb) — a replay buffer, Q-network and DQN agent in PyTorch, trained on CartPole [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/reinforcement-learning/blob/main/notebooks/7b_dqn_practical.ipynb)

#### Policy Optimisation

- **Lesson 8**: Policy Gradient Methods
  - [`8a_policy_gradients_theory.ipynb`](notebooks/8a_policy_gradients_theory.ipynb) — the policy gradient theorem, REINFORCE and actor-critic [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/reinforcement-learning/blob/main/notebooks/8a_policy_gradients_theory.ipynb)
  - [`8b_policy_gradients_practical.ipynb`](notebooks/8b_policy_gradients_practical.ipynb) — an actor-critic and A2C in PyTorch, trained on LunarLander [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/reinforcement-learning/blob/main/notebooks/8b_policy_gradients_practical.ipynb)
- **Lesson 9**: Trust Regions and PPO
  - [`9a_trpo_ppo_theory.ipynb`](notebooks/9a_trpo_ppo_theory.ipynb) — trust-region updates, TRPO and the PPO clipped objective [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/reinforcement-learning/blob/main/notebooks/9a_trpo_ppo_theory.ipynb)
  - [`9b_ppo_practical.ipynb`](notebooks/9b_ppo_practical.ipynb) — PPO from scratch in PyTorch, validated against Stable-Baselines3 [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/reinforcement-learning/blob/main/notebooks/9b_ppo_practical.ipynb)

#### Advanced Topics

- **Lesson 10**: Continuous Control
  - [`10a_continuous_control_theory.ipynb`](notebooks/10a_continuous_control_theory.ipynb) — deterministic policy gradients and entropy-regularised RL [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/reinforcement-learning/blob/main/notebooks/10a_continuous_control_theory.ipynb)
  - [`10b_continuous_control_practical.ipynb`](notebooks/10b_continuous_control_practical.ipynb) — DDPG, TD3 and SAC in PyTorch, validated against Stable-Baselines3 [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/reinforcement-learning/blob/main/notebooks/10b_continuous_control_practical.ipynb)
- **Lesson 11**: Model-Based RL
  - [`11a_model_based_rl_theory.ipynb`](notebooks/11a_model_based_rl_theory.ipynb) — learning a model of the dynamics and planning with it [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/reinforcement-learning/blob/main/notebooks/11a_model_based_rl_theory.ipynb)
  - [`11b_model_based_practical.ipynb`](notebooks/11b_model_based_practical.ipynb) — a learned forward model, Dyna-Q, model-predictive control and Monte Carlo tree search [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/reinforcement-learning/blob/main/notebooks/11b_model_based_practical.ipynb)
- **Lesson 12**: Multi-Agent RL
  - [`12a_marl_theory.ipynb`](notebooks/12a_marl_theory.ipynb) — Markov games, Nash equilibria, credit assignment and centralised training [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/reinforcement-learning/blob/main/notebooks/12a_marl_theory.ipynb)
  - [`12b_marl_practical.ipynb`](notebooks/12b_marl_practical.ipynb) — multi-agent learning in PettingZoo environments [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/reinforcement-learning/blob/main/notebooks/12b_marl_practical.ipynb)
- **Lesson 13**: Exploration Strategies
  - [`13a_exploration_theory.ipynb`](notebooks/13a_exploration_theory.ipynb) — UCB, Thompson sampling and intrinsic motivation [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/reinforcement-learning/blob/main/notebooks/13a_exploration_theory.ipynb)
  - [`13b_exploration_practical.ipynb`](notebooks/13b_exploration_practical.ipynb) — count-based curiosity and RND with PPO on a hard-exploration environment [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/reinforcement-learning/blob/main/notebooks/13b_exploration_practical.ipynb)
- **Lesson 14**: Offline RL and Imitation Learning
  - [`14a_offline_rl_theory.ipynb`](notebooks/14a_offline_rl_theory.ipynb) — learning from a fixed dataset: behaviour cloning and conservative Q-learning [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/reinforcement-learning/blob/main/notebooks/14a_offline_rl_theory.ipynb)
  - [`14b_offline_rl_practical.ipynb`](notebooks/14b_offline_rl_practical.ipynb) — an offline RL library, and combining offline and online learning [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/reinforcement-learning/blob/main/notebooks/14b_offline_rl_practical.ipynb)
- **Lesson 15**: Hierarchical RL
  - [`15a_hierarchical_rl_theory.ipynb`](notebooks/15a_hierarchical_rl_theory.ipynb) — options, semi-MDPs and hindsight experience replay [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/reinforcement-learning/blob/main/notebooks/15a_hierarchical_rl_theory.ipynb)
  - [`15b_hierarchical_rl_practical.ipynb`](notebooks/15b_hierarchical_rl_practical.ipynb) — options and skill chaining from scratch, and goal-conditioned RL with HER [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/reinforcement-learning/blob/main/notebooks/15b_hierarchical_rl_practical.ipynb)

#### Professional Practice

- **Lesson X1**: Debugging RL
  - [`X1_rl_debugging.ipynb`](notebooks/X1_rl_debugging.ipynb) — telling a broken implementation from one that needs more training [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/reinforcement-learning/blob/main/notebooks/X1_rl_debugging.ipynb)
- **Lesson X2**: Evaluating RL
  - [`X2_rl_evaluation.ipynb`](notebooks/X2_rl_evaluation.ipynb) — measuring and comparing agents honestly [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/reinforcement-learning/blob/main/notebooks/X2_rl_evaluation.ipynb)
- **Lesson X3**: Deployment and Safety
  - [`X3_rl_deployment.ipynb`](notebooks/X3_rl_deployment.ipynb) — shipping a trained policy outside the training loop, safely [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/reinforcement-learning/blob/main/notebooks/X3_rl_deployment.ipynb)
- **Lesson X4**: Research Frontiers
  - [`X4_rl_research_frontiers.ipynb`](notebooks/X4_rl_research_frontiers.ipynb) — where the field is heading, and how to keep learning [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/reinforcement-learning/blob/main/notebooks/X4_rl_research_frontiers.ipynb)

## Local use

Start with the [supervised learning](https://github.com/powell-clark/supervised-learning) series if
neural networks and gradient descent are new to you.

```bash
git clone https://github.com/powell-clark/reinforcement-learning.git
cd reinforcement-learning
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/jupyter notebook notebooks/
```

## References

- Sutton and Barto, *Reinforcement Learning: An Introduction* (2nd edition)
- David Silver's UCL reinforcement learning course
- Berkeley CS285, Deep Reinforcement Learning
- OpenAI Spinning Up in Deep RL

## How this repository is built

The curriculum was developed with Claude Code: lessons were drafted by autonomous sessions against
a written syllabus, executed top to bottom and reviewed before they were accepted. The agents'
working state is kept out of this repository.

## Contributing

Spotted a typo, an unclear explanation or a bug? Open an issue or a pull request.

## Licence

Licensed under the Apache License, Version 2.0; see [LICENSE.md](LICENSE.md).
