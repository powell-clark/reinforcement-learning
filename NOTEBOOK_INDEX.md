# 📚 Notebook Index - Quick Reference

Complete guide to all 40 notebooks with descriptions, key algorithms, and learning paths.

---

## 🗺️ Navigation by Topic

**Quick Links:**
- [Foundation (0-1)](#foundation-lessons-0-1) - Start here!
- [Classical RL (2-5)](#classical-rl-lessons-2-5) - Tabular methods
- [Deep RL (6-7)](#deep-rl-lessons-6-7) - Neural networks
- [Policy Gradients (8-10)](#policy-gradients-lessons-8-10) - Modern methods
- [Advanced (11-12)](#advanced-topics-lessons-11-12) - Specialized techniques
- [Cutting Edge (13-15)](#cutting-edge-lessons-13-15) - Research frontier
- [RLHF (16)](#rlhf-lesson-16-) - ChatGPT techniques ⭐
- [Professional (X1-X4)](#professional-practice-x1-x4) - Production skills

---

## Foundation (Lessons 0-1)

### 📘 Lesson 0a: Introduction to RL (Theory)
**File:** `notebooks/0a_rl_introduction_theory.ipynb` (500+ lines)

**What you'll learn:**
- What is reinforcement learning?
- Agent-environment interaction
- Markov Decision Processes (MDPs)
- Bellman equations introduction
- Value functions and policies

**Key Concepts:**
- States, actions, rewards
- Episode vs continuing tasks
- Return and discounting
- Optimal policy

**When to study:** First notebook - essential foundation

---

### 💻 Lesson 0b: RL Setup (Practical)
**File:** `notebooks/0b_rl_setup_practical.ipynb` (600+ lines)

**What you'll learn:**
- Setting up RL environment
- Using Gymnasium (OpenAI Gym)
- First RL agent implementation
- Environment wrappers
- Visualization basics

**Implementations:**
- Random agent baseline
- Simple policy evaluation
- Episode runner
- Reward plotting

**When to study:** After 0a - hands-on introduction

---

### 📘 Lesson 1a: MDPs (Theory)
**File:** `notebooks/1a_mdp_theory.ipynb` (800+ lines)

**What you'll learn:**
- Formal MDP definition
- State transition probabilities
- Reward function
- Bellman expectation equations
- Bellman optimality equations
- Policy iteration proof
- Value iteration proof

**Mathematical Depth:**
- Complete Bellman derivations
- Convergence proofs
- Optimality conditions

**When to study:** After 0b - deep mathematical foundation

---

### 💻 Lesson 1b: MDPs (Practical)
**File:** `notebooks/1b_mdp_practical.ipynb` (900+ lines)

**What you'll learn:**
- GridWorld environment
- Policy evaluation (exact)
- Policy iteration algorithm
- Value iteration algorithm
- Visualizing value functions
- Visualizing policies

**Implementations:**
- Full policy iteration
- Full value iteration
- Comparison on multiple environments
- Heatmap visualizations

**When to study:** After 1a - implement theoretical concepts

---

## Classical RL (Lessons 2-5)

### 📘 Lesson 2a: Dynamic Programming (Theory)
**File:** `notebooks/2a_dynamic_programming_theory.ipynb` (700+ lines)

**What you'll learn:**
- DP requirements (perfect model)
- Policy evaluation
- Policy improvement
- Policy iteration theorem
- Value iteration convergence
- Generalized policy iteration

**Key Algorithms:**
- Iterative policy evaluation
- Policy iteration
- Value iteration

**When to study:** After Lesson 1

---

### 💻 Lesson 2b: Dynamic Programming (Practical)
**File:** `notebooks/2b_dynamic_programming_practical.ipynb` (800+ lines)

**What you'll learn:**
- Implementing DP algorithms
- Convergence analysis
- Performance comparison
- In-place vs sweep updates
- Asynchronous DP

**Implementations:**
- Policy evaluation (iterative)
- Policy iteration (complete)
- Value iteration (complete)
- Multiple environments

**When to study:** After 2a

---

### 📘 Lesson 3a: Monte Carlo (Theory)
**File:** `notebooks/3a_monte_carlo_theory.ipynb` (750+ lines)

**What you'll learn:**
- MC vs DP (model-free!)
- First-visit MC
- Every-visit MC
- MC prediction
- MC control
- Exploring starts
- ε-greedy policies

**Key Insight:** Learn from complete episodes, no model needed

**When to study:** After Lesson 2 - first model-free method

---

### 💻 Lesson 3b: Monte Carlo (Practical)
**File:** `notebooks/3b_monte_carlo_practical.ipynb` (1000+ lines)

**What you'll learn:**
- MC prediction implementation
- MC control with exploring starts
- On-policy MC (ε-greedy)
- Off-policy MC with importance sampling
- Blackjack example

**Implementations:**
- First-visit MC prediction
- MC control (on-policy)
- MC control (off-policy)
- Importance sampling

**When to study:** After 3a

---

### 📘 Lesson 4a: Temporal Difference (Theory)
**File:** `notebooks/4a_temporal_difference_theory.ipynb` (900+ lines)

**What you'll learn:**
- TD(0) algorithm
- TD vs MC vs DP
- SARSA (on-policy TD)
- Q-Learning (off-policy TD)
- Expected SARSA
- Double Q-Learning
- TD error and bootstrapping

**Key Algorithms:**
- TD(0), SARSA, Q-Learning

**When to study:** After Lesson 3 - most important classical method

---

### 💻 Lesson 4b: Temporal Difference (Practical)
**File:** `notebooks/4b_temporal_difference_practical.ipynb` (1100+ lines)

**What you'll learn:**
- TD(0) implementation
- SARSA implementation
- Q-Learning implementation
- Expected SARSA
- Double Q-Learning
- Cliff Walking environment
- Comparison of all methods

**Implementations:**
- TD prediction
- SARSA (complete)
- Q-Learning (complete)
- Expected SARSA
- Double Q-Learning
- Performance analysis

**When to study:** After 4a - master TD methods

---

### 📘 Lesson 5a: N-Step Methods (Theory)
**File:** `notebooks/5a_nstep_methods_theory.ipynb` (1000+ lines)

**What you'll learn:**
- N-step TD prediction
- N-step SARSA
- N-step Q-Learning
- TD(λ) - forward view
- TD(λ) - backward view
- Eligibility traces
- Online λ-return

**Key Concept:** Bridge between MC and TD

**When to study:** After Lesson 4 - unify MC and TD

---

### 💻 Lesson 5b: N-Step Methods (Practical)
**File:** `notebooks/5b_nstep_methods_practical.ipynb` (900+ lines)

**What you'll learn:**
- N-step TD implementation
- N-step SARSA
- TD(λ) with eligibility traces
- Choosing n and λ
- Performance comparison

**Implementations:**
- N-step TD prediction
- N-step SARSA
- TD(λ) with traces
- Trace decay visualization

**When to study:** After 5a

---

## Deep RL (Lessons 6-7)

### 📘 Lesson 6a: Function Approximation (Theory)
**File:** `notebooks/6a_function_approximation_theory.ipynb` (770+ lines)

**What you'll learn:**
- Why function approximation?
- Linear function approximation
- Feature construction
- Semi-gradient methods
- Coarse coding
- Tile coding
- Neural network approximation
- Deadly triad

**Key Transition:** From tabular to large state spaces

**When to study:** After Lesson 5 - scale to large problems

---

### 💻 Lesson 6b: Function Approximation (Practical)
**File:** `notebooks/6b_function_approximation_practical.ipynb` (950+ lines)

**What you'll learn:**
- Linear value functions
- Polynomial features
- RBF features
- Neural network value functions
- Semi-gradient TD
- Mountain Car example

**Implementations:**
- Linear function approximation
- Feature engineering
- Neural network Q-function
- Gradient-based learning

**When to study:** After 6a - implement approximation

---

### 📘 Lesson 7a: DQN (Theory)
**File:** `notebooks/7a_dqn_theory.ipynb` (850+ lines)

**What you'll learn:**
- Deep Q-Networks (DQN)
- Experience replay
- Target networks
- Double DQN
- Dueling DQN
- Prioritized experience replay
- Rainbow DQN
- Atari game benchmarks

**Key Papers:**
- Mnih et al. (2015) - DQN
- Van Hasselt et al. (2016) - Double DQN
- Wang et al. (2016) - Dueling DQN

**When to study:** After Lesson 6 - deep learning meets RL

---

### 💻 Lesson 7b: DQN (Practical)
**File:** `notebooks/7b_dqn_practical.ipynb` (1050+ lines)

**What you'll learn:**
- DQN implementation
- Experience replay buffer
- Target network updates
- Double DQN implementation
- Dueling architecture
- CartPole and Atari examples

**Implementations:**
- Complete DQN
- Replay buffer
- Double DQN
- Dueling DQN
- Training visualization

**When to study:** After 7a - master deep Q-learning

---

## Policy Gradients (Lessons 8-10)

### 📘 Lesson 8a: Policy Gradients (Theory)
**File:** `notebooks/8a_policy_gradients_theory.ipynb` (730+ lines)

**What you'll learn:**
- Policy gradient theorem
- REINFORCE algorithm
- Baseline functions
- Actor-Critic architecture
- Advantage function
- A2C, A3C algorithms

**Key Insight:** Optimize policy directly, not value function

**When to study:** After Lesson 7 - alternative to value-based

---

### 💻 Lesson 8b: Policy Gradients (Practical)
**File:** `notebooks/8b_policy_gradients_practical.ipynb` (850+ lines)

**What you'll learn:**
- REINFORCE implementation
- Baseline variance reduction
- Actor-Critic implementation
- A2C implementation
- CartPole and LunarLander

**Implementations:**
- REINFORCE (complete)
- REINFORCE with baseline
- Actor-Critic
- A2C
- Performance comparison

**When to study:** After 8a

---

### 📘 Lesson 9a: PPO & TRPO (Theory)
**File:** `notebooks/9a_ppo_trpo_theory.ipynb` (810+ lines)

**What you'll learn:**
- Trust region methods
- TRPO (Trust Region Policy Optimization)
- PPO (Proximal Policy Optimization) ⭐
- Clipped surrogate objective
- GAE (Generalized Advantage Estimation)
- KL divergence constraint

**Key Algorithm:** PPO - most popular RL algorithm!

**When to study:** After Lesson 8 - state-of-the-art policy gradients

---

### 💻 Lesson 9b: PPO (Practical)
**File:** `notebooks/9b_ppo_practical.ipynb` (850+ lines)

**What you'll learn:**
- Complete PPO implementation
- PPO-Clip algorithm
- GAE implementation
- Value function clipping
- Multiple environments

**Implementations:**
- PPO-Clip (complete)
- GAE advantage estimation
- Multi-environment training
- Hyperparameter analysis

**When to study:** After 9a - implement most important algorithm

---

### 📘 Lesson 10a: Continuous Control (Theory)
**File:** `notebooks/10a_continuous_control_theory.ipynb` (810+ lines)

**What you'll learn:**
- Deterministic policy gradients
- DDPG algorithm
- TD3 (Twin Delayed DDPG)
- SAC (Soft Actor-Critic) ⭐
- Maximum entropy RL
- Continuous action spaces

**Key Algorithms:** DDPG, TD3, SAC

**When to study:** After Lesson 9 - for robotics/continuous control

---

### 💻 Lesson 10b: Continuous Control (Practical)
**File:** `notebooks/10b_continuous_control_practical.ipynb` (1000+ lines)

**What you'll learn:**
- DDPG implementation
- TD3 implementation
- SAC implementation
- Automatic temperature tuning
- Pendulum and HalfCheetah

**Implementations:**
- DDPG (complete)
- TD3 (complete)
- SAC (complete) ⭐ Best for robotics
- Comparison on continuous tasks

**When to study:** After 10a - master continuous control

---

## Advanced Topics (Lessons 11-12)

### 📘 Lesson 11a: Model-Based RL (Theory)
**File:** `notebooks/11a_model_based_rl_theory.ipynb` (850+ lines)

**What you'll learn:**
- Model-based vs model-free
- Dyna-Q architecture
- PETS (Probabilistic Ensembles)
- MBPO (Model-Based Policy Optimization)
- MuZero
- World Models
- Planning vs learning

**Key Insight:** Learn environment model for sample efficiency

**When to study:** After Lesson 10 - when samples are expensive

---

### 💻 Lesson 11b: Model-Based RL (Practical)
**File:** `notebooks/11b_model_based_rl_practical.ipynb` (950+ lines)

**What you'll learn:**
- Dyna-Q implementation
- Dynamics model learning
- Ensemble models
- Model-based planning
- MBPO framework

**Implementations:**
- Dyna-Q (complete)
- Ensemble dynamics models
- CEM planner
- Model-based + model-free hybrid

**When to study:** After 11a - sample-efficient RL

---

### 📘 Lesson 12a: Exploration (Theory)
**File:** `notebooks/12a_exploration_theory.ipynb` (900+ lines)

**What you'll learn:**
- Exploration vs exploitation
- Multi-armed bandits
- UCB (Upper Confidence Bound)
- Thompson Sampling
- Count-based exploration
- ICM (Intrinsic Curiosity Module)
- RND (Random Network Distillation)
- NGU (Never Give Up)

**Key Concept:** Solve sparse reward problems

**When to study:** After Lesson 11 - when rewards are sparse

---

### 💻 Lesson 12b: Exploration (Practical)
**File:** `notebooks/12b_exploration_practical.ipynb` (1000+ lines)

**What you'll learn:**
- UCB implementation
- Thompson Sampling
- Count-based bonuses
- ICM implementation
- RND implementation
- Sparse reward environments

**Implementations:**
- UCB bandit algorithm
- Thompson Sampling
- Count-based exploration
- ICM (curiosity)
- RND (novelty)

**When to study:** After 12a - master exploration

---

## Cutting Edge (Lessons 13-15)

### 📘 Lesson 13a: Multi-Agent RL (Theory)
**File:** `notebooks/13a_multi_agent_rl_theory.ipynb` (890+ lines)

**What you'll learn:**
- Multi-agent settings
- Nash equilibrium
- IQL (Independent Q-Learning)
- MADDPG (Multi-Agent DDPG)
- VDN (Value Decomposition Networks)
- QMIX
- COMA
- CTDE paradigm

**Key Concept:** Multiple agents learning together

**When to study:** After Lesson 12 - for multi-agent systems

---

### 💻 Lesson 13b: Multi-Agent RL (Practical)
**File:** `notebooks/13b_multi_agent_rl_practical.ipynb` (910+ lines)

**What you'll learn:**
- IQL implementation
- MADDPG implementation
- VDN implementation
- Multi-agent environments
- Cooperative vs competitive

**Implementations:**
- IQL (complete)
- MADDPG (complete)
- VDN (complete)
- Multi-agent environments

**When to study:** After 13a - build multi-agent systems

---

### 📘 Lesson 14a: Hierarchical RL (Theory)
**File:** `notebooks/14a_hierarchical_rl_theory.ipynb` (700+ lines)

**What you'll learn:**
- Options framework
- Feudal Reinforcement Learning
- Goal-conditioned RL
- HER (Hindsight Experience Replay)
- Temporal abstraction

**Key Concept:** Decompose complex tasks

**When to study:** After Lesson 13 - for complex tasks

---

### 💻 Lesson 14b: Hierarchical RL (Practical)
**File:** `notebooks/14b_hierarchical_rl_practical.ipynb` (800+ lines)

**What you'll learn:**
- Options implementation
- Feudal Networks
- Goal-conditioned policies
- HER implementation
- Sparse reward robotics

**Implementations:**
- Options framework
- Feudal Networks
- Goal-conditioned RL
- HER (complete)

**When to study:** After 14a - for robotics with sparse rewards

---

### 📘 Lesson 15a: Meta-Learning (Theory)
**File:** `notebooks/15a_meta_learning_theory.ipynb` (750+ lines)

**What you'll learn:**
- Meta-learning (learning to learn)
- MAML (Model-Agnostic Meta-Learning)
- RL² (Fast RL via Slow RL)
- Meta-gradients
- Transfer learning in RL
- Few-shot adaptation

**Key Concept:** Learn to learn quickly

**When to study:** After Lesson 14 - for fast adaptation

---

### 💻 Lesson 15b: Meta-Learning (Practical)
**File:** `notebooks/15b_meta_learning_practical.ipynb` (700+ lines)

**What you'll learn:**
- MAML implementation
- RL² with recurrent policies
- Transfer learning
- Few-shot RL
- Task distribution

**Implementations:**
- MAML (complete)
- RL² (complete)
- Transfer learning agent
- Multi-task evaluation

**When to study:** After 15a - for adaptation to new tasks

---

## RLHF (Lesson 16) ⭐

### 📘 Lesson 16a: RLHF (Theory)
**File:** `notebooks/16a_rlhf_theory.ipynb` (950+ lines)

**What you'll learn:**
- Reinforcement Learning from Human Feedback
- Bradley-Terry preference model
- Reward model training
- PPO-RLHF (ChatGPT approach)
- DPO (Direct Preference Optimization)
- Constitutional AI (Claude approach)
- AI alignment and safety
- Red teaming

**Key Papers:**
- InstructGPT (OpenAI, 2022)
- DPO (2023)
- Constitutional AI (Anthropic, 2022)

**CRITICAL FOR 2025:** Powers ChatGPT, GPT-4, Claude, all major LLMs

**When to study:** After any earlier lesson - most important modern RL!

---

### 💻 Lesson 16b: RLHF (Practical)
**File:** `notebooks/16b_rlhf_practical.ipynb` (1000+ lines)

**What you'll learn:**
- Reward model implementation
- PPO-RLHF complete pipeline
- DPO implementation
- Constitutional AI with principles
- Preference dataset collection
- Full RLHF workflow

**Implementations:**
- Reward model training
- PPO-RLHF (ChatGPT-style)
- DPO (simpler alternative)
- Constitutional AI
- Preference learning
- Safety constraints

**When to study:** After 16a - implement ChatGPT-style alignment

---

## Professional Practice (X1-X4)

### 💻 X1: Deployment & Production
**File:** `notebooks/X1_deployment_production.ipynb` (850+ lines)

**What you'll learn:**
- Model versioning and serialization
- Production serving infrastructure
- Online learning systems
- Safety constraints and guardrails
- A/B testing framework
- Monitoring and alerting
- Distribution shift detection

**Implementations:**
- Model manager
- Serving infrastructure
- Online RL system
- Safe RL wrapper
- A/B testing
- Monitoring dashboard

**When to study:** After completing main curriculum - for production

---

### 💻 X2: Hyperparameter Tuning
**File:** `notebooks/X2_hyperparameter_tuning.ipynb` (900+ lines)

**What you'll learn:**
- Critical RL hyperparameters
- Random search
- Bayesian optimization
- Population-Based Training (PBT)
- ASHA/Hyperband
- Complete tuning workflow

**Implementations:**
- Random search
- Bayesian optimization
- PBT (complete)
- ASHA (complete)
- Workflow automation

**When to study:** After main curriculum - essential for good results

---

### 💻 X3: Debugging & Monitoring
**File:** `notebooks/X3_debugging_monitoring.ipynb` (800+ lines)

**What you'll learn:**
- Common RL failure modes
- Debugging checklist
- Comprehensive logging
- Failure mode diagnosis
- Systematic troubleshooting
- Automated sanity checks

**Implementations:**
- Failure mode catalog
- RL logger
- Debugging checklist
- Automated checks
- Visualization tools

**When to study:** When things don't work - essential debugging guide

---

### 💻 X4: Real-World Applications
**File:** `notebooks/X4_real_world_applications.ipynb` (950+ lines)

**What you'll learn:**
- AlphaGo/AlphaZero case study
- ChatGPT RLHF case study
- Recommendation systems (YouTube, Netflix)
- Robotics sim-to-real
- Finance, healthcare, autonomous vehicles
- Production lessons learned

**Implementations:**
- MCTS (AlphaGo-style)
- Self-play training
- Recommendation system
- Sim-to-real pipeline

**When to study:** Throughout or at end - see real-world impact

---

## 📖 Recommended Learning Paths

### 🎓 Complete Beginner Path
1. Lesson 0a → 0b (Introduction)
2. Lesson 1a → 1b (MDPs)
3. Lesson 2a → 2b (Dynamic Programming)
4. Lesson 4a → 4b (TD Learning - skip 3 initially)
5. Lesson 7a → 7b (DQN)
6. Lesson 9a → 9b (PPO)
7. **Lesson 16a → 16b (RLHF)** ⭐
8. X1-X4 (Professional Practice)

### 🏃 Fast Track (Experienced ML)
1. Lesson 0a-0b (Quick foundation)
2. Lesson 1a (MDP theory)
3. Lesson 4a-4b (TD Learning)
4. **Lesson 9a-9b (PPO)** - Most important!
5. Lesson 10a-10b (Continuous control)
6. **Lesson 16a-16b (RLHF)** ⭐ Critical!
7. X1-X4 (Professional)

### 💬 LLM / AI Safety Focus
1. Lesson 0a (RL basics)
2. Lesson 4a (Q-Learning concepts)
3. Lesson 8a-9b (Policy Gradients & PPO)
4. **Jump to Lesson 16a-16b (RLHF)** ⭐⭐⭐
5. X1 (Deployment)
6. X3 (Debugging)

### 🤖 Robotics Focus
1. Lessons 0-5 (Foundation)
2. Lesson 6a-7b (Function approximation)
3. **Lesson 10a-10b (Continuous control - SAC)** ⭐
4. Lesson 14a-14b (Hierarchical - HER)
5. Lesson 15a-15b (Meta-learning)
6. X1-X4 (Professional)

### 🎮 Game AI Focus
1. Lessons 0-4 (Foundation)
2. Lesson 7a-7b (DQN for Atari)
3. Lesson 9a-9b (PPO)
4. Lesson 11b (Model-based - MCTS)
5. Lesson 13a-13b (Multi-agent)
6. X4 (AlphaGo case study)

---

## 📊 Notebook Statistics

| Category | Theory Notebooks | Practical Notebooks | Total Lines |
|----------|------------------|---------------------|-------------|
| Foundation | 2 | 2 | 2,800+ |
| Classical RL | 4 | 4 | 6,350+ |
| Deep RL | 2 | 2 | 3,620+ |
| Policy Gradients | 3 | 3 | 5,060+ |
| Advanced | 2 | 2 | 3,700+ |
| Cutting Edge | 3 | 3 | 4,360+ |
| RLHF | 1 | 1 | 1,950+ |
| Professional | 0 | 4 | 3,450+ |
| **TOTAL** | **17** | **21** | **35,000+** |

---

## 🎯 Key Takeaways

### Most Important Notebooks
1. **Lesson 9b (PPO)** - Most widely used algorithm
2. **Lesson 16a-16b (RLHF)** - Critical for 2025, powers ChatGPT
3. **Lesson 10b (SAC)** - Best for robotics
4. **Lesson 7b (DQN)** - Foundation of deep RL
5. **X2 (Tuning)** - Make anything work better

### By Use Case
- **General Purpose:** Lesson 9 (PPO)
- **LLM Alignment:** Lesson 16 (RLHF) ⭐⭐⭐
- **Robotics:** Lesson 10 (SAC) + 14 (HER)
- **Games:** Lesson 7 (DQN) + 11 (MCTS)
- **Production:** X1-X4

### Time Estimates
- **Quick Survey:** 0a, 4a, 9a, 16a (20 hours)
- **Foundations:** Lessons 0-5 (60 hours)
- **Complete Curriculum:** All 40 notebooks (200+ hours)
- **Professional Ready:** + X1-X4 (250+ hours)

---

## 🚀 Getting Started

**First Time Learner:**
1. Start with `0a_rl_introduction_theory.ipynb`
2. Do `0b_rl_setup_practical.ipynb`
3. Continue sequentially through lessons

**Experienced Practitioner:**
1. Review `0a` for notation
2. Jump to `9b_ppo_practical.ipynb` (most important!)
3. Do `16a-16b_rlhf` if working with LLMs
4. Use X2-X3 for tuning/debugging

**LLM Engineer:**
1. Quick review: `0a`, `9a` (PPO theory)
2. **Focus on: `16a-16b` (RLHF)** ⭐
3. Production: `X1` (Deployment), `X3` (Debugging)

---

*Last Updated: 2025-01-23*
*All 40 notebooks complete with 35,000+ lines of production code*
*See README.md for installation and setup*
