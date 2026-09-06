# 🎮 Reinforcement Learning Curriculum

A complete, university-grade curriculum for learning reinforcement learning from first principles to production deployment. **36 of 36 notebooks built (16 lessons + 4 professional-practice notebooks); awaiting operator sign-off.** Each lesson pairs rigorous theory derivations with hands-on NumPy implementations, reproduced in Stable-Baselines3 for production validation. All notebooks run in Google Colab with no local setup required.

## 🎯 Overview

This curriculum follows the proven pedagogical approach:
- **From First Principles**: Derive every algorithm from MDPs and Bellman equations
- **Dual Approach**: Theory (a) + Practical (b) notebooks for each lesson
- **Interactive Environments**: Hands-on learning with Gymnasium (OpenAI Gym)
- **Story-Driven**: Real-world motivations (games, robotics) before mathematics
- **Complete Implementations**: From-scratch NumPy code + production libraries (Stable-Baselines3)
- **Google Colab Compatible**: Run everything in your browser, no setup required

## 📚 Curriculum Status

**Status**: ✅ Built — 36 of 36 notebooks complete (100%), all lesson features in_review awaiting operator sign-off

**Completed Lessons (0-15)**: All theory and practical notebooks delivered and re-executed with zero error-type output cells
**Professional Series (X1-X4)**: Delivered

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

#### Policy Gradient Methods ✅
- **Lesson 8**: Policy Gradient Methods (REINFORCE, Actor-Critic) (Complete)
- **Lesson 9**: Trust Region & Proximal Methods (TRPO, PPO) (Complete)

#### Advanced Topics ✅
- **Lesson 10**: Continuous Control (DDPG, TD3, SAC) (Complete)
- **Lesson 11**: Model-Based RL (Complete)
- **Lesson 12**: Multi-Agent RL (Complete)
- **Lesson 13**: Exploration Strategies (Complete)
- **Lesson 14**: Offline RL & Imitation Learning (Complete)
- **Lesson 15**: Hierarchical RL (Complete)

#### Professional Practice ✅
- **X1**: RL Debugging & Best Practices (Complete)
- **X2**: RL Evaluation Metrics (Complete)
- **X3**: RL Deployment & Safety (Complete)
- **X4**: RL Research Frontiers (Complete)

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

**Status**: 100% complete (36/36 lessons + professional notebooks); all lesson features in_review awaiting operator sign-off
**Progress**: Lessons 0-15 and X1-X4 (foundation through hierarchical RL, plus professional practice) delivered and verified
**Next**: Operator review of FEAT-RL1 through FEAT-RL20 (must-have gate, human sign-off required to promote to maintained)
**Last Updated**: 2026-09-06
**Author**: Powell-Clark Limited
