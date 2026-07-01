# 🎮 Reinforcement Learning Curriculum

A complete, university-grade curriculum for learning reinforcement learning from first principles to production deployment. **16 of 36 lessons complete.** Each lesson pairs rigorous theory derivations with hands-on NumPy implementations, reproduced in Stable-Baselines3 for production validation. All notebooks run in Google Colab with no local setup required.

## 🎯 Overview

This curriculum follows the proven pedagogical approach:
- **From First Principles**: Derive every algorithm from MDPs and Bellman equations
- **Dual Approach**: Theory (a) + Practical (b) notebooks for each lesson
- **Interactive Environments**: Hands-on learning with Gymnasium (OpenAI Gym)
- **Story-Driven**: Real-world motivations (games, robotics) before mathematics
- **Complete Implementations**: From-scratch NumPy code + production libraries (Stable-Baselines3)
- **Google Colab Compatible**: Run everything in your browser, no setup required

## 📚 Curriculum Status

**Status**: ✅ In Progress — 16 of 36 lessons complete (44%)

**Completed Lessons (0-7)**: All theory and practical notebooks delivered
**In Development (8-15)**: Queued for implementation
**Professional Series (X1-X4)**: Queued for implementation

See [CURRICULUM_PLAN.md](./CURRICULUM_PLAN.md) for the complete planned curriculum.

### Lesson Catalog (36 Notebooks + 4 Professional Practice)

#### Foundation ✅
- **Lesson 0**: Introduction to Reinforcement Learning (Complete)

#### Markov Decision Processes ✅
- **Lesson 1**: Markov Decision Processes (MDPs) (Complete)
- **Lesson 2**: Dynamic Programming (Complete)

#### Classical RL ✅
- **Lesson 3**: Monte Carlo Methods (Complete)
- **Lesson 4**: Temporal Difference Learning (Sarsa, Q-Learning) (Complete)
- **Lesson 5**: N-Step Bootstrapping & Eligibility Traces (Complete)

#### Function Approximation & Deep RL ✅
- **Lesson 6**: Function Approximation (Complete)
- **Lesson 7**: Deep Q-Networks (DQN) (Complete)

#### Policy Gradient Methods 🚧
- **Lesson 8**: Policy Gradient Methods (REINFORCE, Actor-Critic) (In Development)
- **Lesson 9**: Trust Region & Proximal Methods (TRPO, PPO) (In Development)

#### Advanced Topics 🚧
- **Lesson 10**: Continuous Control (DDPG, TD3, SAC) (In Development)
- **Lesson 11**: Model-Based RL (In Development)
- **Lesson 12**: Multi-Agent RL (In Development)
- **Lesson 13**: Exploration Strategies (In Development)
- **Lesson 14**: Offline RL & Imitation Learning (In Development)
- **Lesson 15**: Hierarchical RL (In Development)

#### Professional Practice 🚧
- **X1**: RL Debugging & Best Practices (Queued)
- **X2**: RL Evaluation Metrics (Queued)
- **X3**: RL Deployment & Safety (Queued)
- **X4**: RL Research Frontiers (Queued)

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

**Status**: 44% complete (16/36 lessons + 0/4 professional notebooks)
**Progress**: Lessons 0-7 (foundation through DQN) delivered and verified
**Next**: Lessons 8-15 (policy methods and advanced topics) in queue
**Last Updated**: 2026-07-01
**Author**: Powell-Clark Limited
