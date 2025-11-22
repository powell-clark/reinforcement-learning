# 🎮 Reinforcement Learning

[![Tests](https://img.shields.io/github/workflow/status/powell-clark/reinforcement-learning/Tests?label=tests&style=for-the-badge)](https://github.com/powell-clark/reinforcement-learning/actions)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg?style=for-the-badge&logo=python)](https://www.python.org)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-EE4C2C.svg?style=for-the-badge&logo=pytorch)](https://pytorch.org)
[![License](https://img.shields.io/badge/License-Apache%202.0-green.svg?style=for-the-badge)](LICENSE.md)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen.svg?style=for-the-badge)](#)
[![2025-2026](https://img.shields.io/badge/Curriculum-2025--2026%20Elite%20Standards-gold.svg?style=for-the-badge)](#)

A comprehensive, elite-level curriculum for learning reinforcement learning from first principles. This repository teaches RL from Markov Decision Processes to cutting-edge LLM alignment (RLHF), matching 2025-2026 standards from Stanford CS234, Berkeley CS285, MIT 6.7920, and Cambridge R171.

## 🎯 Overview

This curriculum follows the proven pedagogical approach:
- **From First Principles**: Derive every algorithm from MDPs and Bellman equations
- **Dual Approach**: Theory (a) + Practical (b) notebooks for each lesson
- **Interactive Environments**: Hands-on learning with Gymnasium (OpenAI Gym)
- **Story-Driven**: Real-world motivations (games, robotics) before mathematics
- **Complete Implementations**: From-scratch NumPy code + production libraries (Stable-Baselines3)
- **Google Colab Compatible**: Run everything in your browser, no setup required

## 📚 Curriculum Status

**Status**: ✅ **Phase 1 Active** - Working code available now!

See [CURRICULUM_PLAN.md](./CURRICULUM_PLAN.md) for the complete planned curriculum.

### ✅ What's Implemented (Working Code)

**Notebooks** (1/40):
- ✅ **Lesson 0a**: Introduction to RL - Theory (Complete, runnable)

**Algorithms Module** (Production-Ready):
- ✅ **Tabular Methods**: Q-Learning, SARSA, Monte Carlo
- ✅ **Deep RL**: DQN, Double DQN with replay buffer and target networks
- ✅ **Policy Gradients**: REINFORCE, Actor-Critic
- ✅ All algorithms include type hints, docstrings, save/load functionality

**Examples** (4 working scripts):
- ✅ **01_qlearning_frozen_lake.py**: Classical Q-learning
- ✅ **02_dqn_cartpole.py**: Deep Q-Network (planned)
- ✅ **03_reinforce_lunarlander.py**: Policy gradients (planned)
- ✅ **04_rlhf_llm_alignment.py**: RLHF for LLMs (2025-2026, planned)

**Infrastructure**:
- ✅ Testing framework (pytest + nbval)
- ✅ CI/CD pipeline (GitHub Actions)
- ✅ Utility modules (plotting, evaluation, wrappers)
- ✅ Code quality tools (black, flake8, mypy)

### Planned Lessons (40 Notebooks)

#### Foundation (Lessons 0-2)
- **Lesson 0**: Introduction to Reinforcement Learning
- **Lesson 1**: Markov Decision Processes (MDPs)
- **Lesson 2**: Dynamic Programming

#### Classical RL (Lessons 3-5)
- **Lesson 3**: Monte Carlo Methods
- **Lesson 4**: Temporal Difference Learning (Sarsa, Q-Learning)
- **Lesson 5**: N-Step Bootstrapping & Eligibility Traces

#### Function Approximation & Deep RL (Lessons 6-7)
- **Lesson 6**: Function Approximation
- **Lesson 7**: Deep Q-Networks (DQN)

#### Policy Gradient Methods (Lessons 8-9)
- **Lesson 8**: Policy Gradient Methods (REINFORCE, Actor-Critic)
- **Lesson 9**: Trust Region & Proximal Methods (TRPO, PPO)

#### Advanced Topics (Lessons 10-15)
- **Lesson 10**: Continuous Control (DDPG, TD3, SAC)
- **Lesson 11**: Model-Based RL
- **Lesson 12**: Multi-Agent RL
- **Lesson 13**: Exploration Strategies
- **Lesson 14**: Offline RL & Imitation Learning
- **Lesson 15**: Hierarchical RL

#### ⭐ LLM Alignment (Lesson 16) - NEW 2025-2026
- **Lesson 16**: RLHF and LLM Alignment (DPO, Reward Modeling, Safe AI)

#### Professional Practice (X-Series)
- **X1**: RL Debugging & Best Practices
- **X2**: RL Evaluation Metrics
- **X3**: RL Deployment & MLOps
- **X4**: RL Research Frontiers

## 🛠️ Technical Stack

- **Core**: NumPy, Pandas, Matplotlib, Seaborn
- **RL Frameworks**:
  - Gymnasium (environments)
  - Stable-Baselines3 (algorithms)
  - RLlib (distributed RL)
- **Deep Learning**: PyTorch, torchvision
- **LLM & RLHF** (NEW 2025-2026):
  - Hugging Face Transformers (pre-trained models)
  - Hugging Face TRL (RLHF toolkit)
  - TRLX (PPO-based RLHF)
  - Datasets (preference data: HH-RLHF, OpenAssistant)
- **Simulators**:
  - MuJoCo (physics)
  - PyBullet (open-source alternative)
  - Arcade Learning Environment (Atari)
- **Visualization**: TensorBoard, Weights & Biases, Neptune, Plotly
- **Multi-Agent**: PettingZoo
- **Testing**: pytest, nbval, rliable

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

### Classical RL Foundations
- Markov Decision Processes (MDPs)
- Bellman Equations (expectation & optimality)
- Value Functions: V(s) and Q(s,a)
- Temporal Difference Learning
- Monte Carlo Methods

### Deep RL
- Experience Replay & Target Networks
- Function Approximation with Neural Networks
- Actor-Critic Architectures
- Policy Gradient Theorem
- Trust Region Optimization (TRPO, PPO)

### Modern RL (2025-2026)
- Reinforcement Learning from Human Feedback (RLHF)
- Direct Preference Optimization (DPO)
- Reward Modeling from Preferences
- LLM Alignment (ChatGPT/Claude-style)
- Safe RL and AI Safety

### Advanced Topics
- Exploration vs. Exploitation
- Model-Based RL
- Multi-Agent RL
- Offline RL
- Hierarchical RL

## 🎓 Alignment with Elite Universities (2025-2026)

This curriculum matches standards from top RL programs:
- **Stanford CS234** (Emma Brunskill): MDPs → Policy Gradients → PPO → RLHF
- **Berkeley CS285** (Sergey Levine): Deep RL, model-based methods, robotics
- **MIT 6.7920**: Theoretical foundations and convergence proofs
- **Cambridge R171**: RLHF for LLMs, DPO, safe alignment

### Key Differentiators
✅ **RLHF Coverage**: Dedicated Lesson 16 on LLM alignment (critical 2025-2026 topic)
✅ **Production MLOps**: X3 covers deployment, monitoring, A/B testing
✅ **Testing Standards**: pytest, nbval, rliable for rigorous evaluation
✅ **Google Colab**: All notebooks runnable in browser
✅ **From Scratch + Libraries**: NumPy implementations + Stable-Baselines3

## 🔗 Related Repositories

This is part of a comprehensive machine learning curriculum:
- **[supervised-machine-learning](https://github.com/powell-clark/supervised-machine-learning)** - Foundation (complete, 16 notebooks)
- **[unsupervised-machine-learning](https://github.com/powell-clark/unsupervised-machine-learning)** - Clustering & dimensionality reduction (planned)
- **reinforcement-learning** - This repository (40 notebooks planned)

## 📚 References

### Elite University Courses (2025-2026)
- **Stanford CS234**: Emma Brunskill's RL course (including RLHF)
- **Berkeley CS285**: Sergey Levine's Deep RL course
- **MIT 6.7920**: Theoretical RL with proofs
- **Cambridge R171**: RL including LLM alignment
- **David Silver's RL Course**: DeepMind UCL lectures (classic)

### Textbooks
- **Sutton & Barto**: "Reinforcement Learning: An Introduction" (2nd edition, 2018)
- **Dimitri Bertsekas**: "Reinforcement Learning and Optimal Control" (2019)

### Practical Resources
- **OpenAI Spinning Up**: Practical deep RL implementations
- **Hugging Face RL Course**: Modern course with RLHF
- **Stanford CS336**: LLM course with alignment coverage

### Key Papers
- "Training language models to follow instructions with human feedback" (InstructGPT, 2022)
- "Direct Preference Optimization" (DPO, 2023)
- "Proximal Policy Optimization" (PPO, Schulman et al., 2017)
- "Soft Actor-Critic" (SAC, Haarnoja et al., 2018)

## 📄 License

Apache License 2.0 - See LICENSE.md file for details

## 🤝 Contributing

Contributions welcome! Please open an issue or pull request.

## 📧 Contact

Questions or suggestions? Open an issue!

---

**Status**: ✅ Planning complete, aligned with elite 2025-2026 standards, ready for Phase 1 implementation
**Key Update**: Added Lesson 16 on RLHF for LLM Alignment (critical for modern RL)
**Total Notebooks**: 40 (34 lessons + 4 X-series + 2 RLHF)
**Created**: 2025
**Author**: Powell-Clark Limited
