# 🎮 Reinforcement Learning

A comprehensive, hands-on curriculum for learning reinforcement learning from first principles using Python. This repository teaches RL from Markov Decision Processes to modern deep RL algorithms through theory and practical implementation.

## 🎯 Overview

This curriculum follows the proven pedagogical approach:
- **From First Principles**: Derive every algorithm from MDPs and Bellman equations
- **Dual Approach**: Theory (a) + Practical (b) notebooks for each lesson
- **Interactive Environments**: Hands-on learning with Gymnasium (OpenAI Gym)
- **Story-Driven**: Real-world motivations (games, robotics) before mathematics
- **Complete Implementations**: From-scratch NumPy code + production libraries (Stable-Baselines3)
- **Google Colab Compatible**: Run everything in your browser, no setup required

## 📚 Curriculum Status

**Status**: 🚧 Under Development

See [CURRICULUM_PLAN.md](./CURRICULUM_PLAN.md) for the complete planned curriculum.

### Planned Lessons (38 Notebooks)

#### Foundation
- **Lesson 0**: Introduction to Reinforcement Learning

#### Markov Decision Processes
- **Lesson 1**: Markov Decision Processes (MDPs)
- **Lesson 2**: Dynamic Programming

#### Classical RL
- **Lesson 3**: Monte Carlo Methods
- **Lesson 4**: Temporal Difference Learning (Sarsa, Q-Learning)
- **Lesson 5**: N-Step Bootstrapping & Eligibility Traces

#### Function Approximation & Deep RL
- **Lesson 6**: Function Approximation
- **Lesson 7**: Deep Q-Networks (DQN)

#### Policy Gradient Methods
- **Lesson 8**: Policy Gradient Methods (REINFORCE, Actor-Critic)
- **Lesson 9**: Trust Region & Proximal Methods (TRPO, PPO)

#### Advanced Topics
- **Lesson 10**: Continuous Control (DDPG, TD3, SAC)
- **Lesson 11**: Model-Based RL
- **Lesson 12**: Multi-Agent RL
- **Lesson 13**: Exploration Strategies
- **Lesson 14**: Offline RL & Imitation Learning
- **Lesson 15**: Hierarchical RL

#### Professional Practice (X-Series)
- **X1**: RL Debugging & Best Practices
- **X2**: RL Evaluation Metrics
- **X3**: RL Deployment & Safety
- **X4**: RL Research Frontiers

## 🛠️ Technical Stack

- **Core**: NumPy, Pandas, Matplotlib
- **RL Frameworks**:
  - Gymnasium (environments)
  - Stable-Baselines3 (algorithms)
  - RLlib (distributed RL)
- **Deep Learning**: PyTorch
- **Simulators**:
  - MuJoCo (physics)
  - PyBullet (open-source alternative)
  - Arcade Learning Environment (Atari)
- **Visualization**: TensorBoard, Weights & Biases
- **Multi-Agent**: PettingZoo

## 🎮 Environments

Environments include:
- **Classic Control**: CartPole, MountainCar, Pendulum
- **Atari Games**: Pong, Breakout, Montezuma's Revenge
- **Robotics (MuJoCo)**: Reacher, HalfCheetah, Ant, Humanoid
- **Multi-Agent**: PettingZoo, SMAC
- **Goal-Conditioned**: FetchReach, FetchPush

## 🚀 Getting Started

### Prerequisites
Complete these repositories first:
1. [supervised-machine-learning](https://github.com/powell-clark/supervised-machine-learning) - Neural networks, gradient descent
2. [unsupervised-machine-learning](https://github.com/powell-clark/unsupervised-machine-learning) - Optional but helpful

### Installation

```bash
git clone https://github.com/powell-clark/reinforcement-learning.git
cd reinforcement-learning
pip install -r requirements.txt
```

### Running Notebooks

All notebooks are Google Colab compatible. Click the Colab badge in any notebook to run it immediately in your browser.

## 📖 Learning Path

1. **Foundation**: Lesson 0 - Understand the RL paradigm
2. **Mathematical Foundation**: Lessons 1-2 - Master MDPs and Bellman equations
3. **Classical RL**: Lessons 3-5 - Learn tabular methods (MC, TD, traces)
4. **Deep RL**: Lessons 6-7 - Scale to large state spaces with DQN
5. **Policy Methods**: Lessons 8-9 - Learn policy gradients and PPO
6. **Advanced**: Lessons 10-15 - Explore specialized topics
7. **Professional**: X-Series - Production deployment skills

## 📚 Key Concepts Covered

- Markov Decision Processes (MDPs)
- Bellman Equations (expectation & optimality)
- Value Functions: V(s) and Q(s,a)
- Policy Gradient Theorem
- Temporal Difference Learning
- Experience Replay & Target Networks
- Actor-Critic Architectures
- Trust Region Optimization
- Exploration vs. Exploitation

## 🔗 Related Repositories

This is part of a comprehensive machine learning curriculum:
- **[supervised-machine-learning](https://github.com/powell-clark/supervised-machine-learning)** - Foundation (complete)
- **[unsupervised-machine-learning](https://github.com/powell-clark/unsupervised-machine-learning)** - Clustering & dimensionality reduction (in development)
- **reinforcement-learning** - This repository (in development)

## 📚 References

This curriculum is inspired by:
- **Sutton & Barto**: "Reinforcement Learning: An Introduction" (2nd edition)
- **David Silver's RL Course**: DeepMind UCL lectures
- **Berkeley CS285**: Deep Reinforcement Learning
- **OpenAI Spinning Up**: Practical deep RL guide
- **Andrew Ng's ML Specialization**: RL section

## 📄 License

Apache License 2.0 - See LICENSE.md file for details

## 🤝 Contributing

Contributions welcome! Please read CONTRIBUTING.md for guidelines.

## 📧 Contact

Questions or suggestions? Open an issue or reach out!

---

**Status**: Planning complete, implementation in progress
**Created**: 2025
**Author**: Powell-Clark Limited
