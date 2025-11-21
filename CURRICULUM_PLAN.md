# 🎮 Reinforcement Learning - Curriculum Plan

## Overview
This document outlines the comprehensive curriculum for the **reinforcement-learning** repository, which will teach reinforcement learning (RL) from first principles using Python. Following the same pedagogical approach as the supervised and unsupervised learning series: story-driven introductions, mathematical derivations, from-scratch implementations, and production code.

## Teaching Philosophy
- **From First Principles**: Every algorithm derived from foundational concepts (MDPs, Bellman equations)
- **Dual Approach**: Each lesson has theory (a) and practical (b) notebooks
- **Interactive Environments**: Use OpenAI Gym/Gymnasium for hands-on learning
- **Story-Driven**: Real-world motivations (game playing, robotics, optimization)
- **Complete Implementations**: From-scratch NumPy implementations + production libraries (Stable-Baselines3, RLlib)
- **Google Colab Compatible**: All notebooks runnable in browser with visualization

## Curriculum Structure

### Foundation
**Lesson 0: Introduction to Reinforcement Learning** - The RL paradigm
- **0a_rl_introduction_theory.ipynb**
  - What is reinforcement learning? How does it differ from supervised/unsupervised?
  - The agent-environment interaction loop
  - Key concepts: States, actions, rewards, policies
  - The exploration vs. exploitation tradeoff
  - Types of RL: Model-based vs. Model-free, Value-based vs. Policy-based
  - Real-world applications: Games, robotics, recommendation systems
  - Environment: Simple GridWorld

- **0b_rl_setup_practical.ipynb**
  - Setting up Gymnasium (formerly OpenAI Gym)
  - Understanding environment APIs: reset(), step(), render()
  - Creating custom environments
  - Visualization techniques for RL training
  - Practical tips for debugging RL agents

### Markov Decision Processes

**Lesson 1: Markov Decision Processes** - Mathematical foundation
- **1a_mdp_theory.ipynb**
  - Markov property and Markov chains
  - Formal MDP definition: (S, A, P, R, γ)
  - State transition probabilities
  - Reward functions
  - Discount factor γ: mathematical justification
  - Policies: deterministic vs. stochastic
  - Value functions: V(s) and Q(s,a)
  - Bellman equations derivation
  - Optimal policies and value functions
  - From-scratch MDP solver
  - Environment: Simple MDPs (student MDP, recycling robot)

- **1b_mdp_practical.ipynb**
  - Implementing MDPs in Python
  - Policy evaluation, policy iteration, value iteration
  - Visualizing value functions
  - Convergence analysis
  - Environment: FrozenLake

### Dynamic Programming

**Lesson 2: Dynamic Programming** - Solving known MDPs
- **2a_dynamic_programming_theory.ipynb**
  - Policy evaluation (prediction problem)
  - Policy improvement theorem
  - Policy iteration algorithm
  - Value iteration algorithm
  - Relationship between policy and value iteration
  - Convergence guarantees
  - Computational complexity
  - From-scratch implementations
  - Environment: GridWorld

- **2b_dynamic_programming_practical.ipynb**
  - Efficient implementation techniques
  - In-place vs. synchronous updates
  - Prioritized sweeping
  - Asynchronous DP
  - Environment: GridWorld variations, FrozenLake

### Monte Carlo Methods

**Lesson 3: Monte Carlo Methods** - Learning from episodes
- **3a_monte_carlo_theory.ipynb**
  - Episodic vs. continuing tasks
  - Monte Carlo prediction (policy evaluation)
  - First-visit vs. every-visit MC
  - Monte Carlo control
  - Exploring starts
  - ε-greedy policies
  - On-policy vs. off-policy methods
  - Importance sampling for off-policy learning
  - From-scratch implementation
  - Environment: Blackjack

- **3b_monte_carlo_practical.ipynb**
  - Production MC implementations
  - Handling continuous state spaces with discretization
  - Variance reduction techniques
  - Debugging common MC issues
  - Environment: Blackjack, CliffWalking

### Temporal Difference Learning

**Lesson 4: Temporal Difference Learning** - Combining MC and DP
- **4a_td_learning_theory.ipynb**
  - TD prediction (TD(0))
  - Advantages of TD over MC and DP
  - Bias-variance tradeoff
  - Bootstrapping
  - TD error and learning
  - Sarsa: On-policy TD control
  - Q-Learning: Off-policy TD control
  - Expected Sarsa
  - Mathematical derivations and convergence
  - From-scratch implementations
  - Environment: CliffWalking, WindyGridWorld

- **4b_td_learning_practical.ipynb**
  - Implementing TD methods efficiently
  - Hyperparameter tuning (α, γ, ε)
  - Comparing Sarsa vs. Q-Learning behavior
  - Debugging TD algorithms
  - Environment: Taxi-v3, CliffWalking

### N-Step and Eligibility Traces

**Lesson 5: N-Step Bootstrapping and Eligibility Traces** - Beyond one-step TD
- **5a_nstep_eligibility_theory.ipynb**
  - N-step TD prediction
  - N-step Sarsa
  - Forward view of eligibility traces
  - Backward view of eligibility traces
  - TD(λ): Unifying MC and TD
  - Sarsa(λ)
  - Mathematical equivalence of forward/backward views
  - From-scratch implementations
  - Environment: RandomWalk

- **5b_nstep_eligibility_practical.ipynb**
  - Implementing eligibility traces efficiently
  - Choosing λ and n
  - Trace decay mechanisms
  - Environment: MountainCar

### Function Approximation

**Lesson 6: Function Approximation** - Scaling to large state spaces
- **6a_function_approximation_theory.ipynb**
  - The curse of dimensionality in RL
  - Linear function approximation
  - Feature engineering for RL
  - Tile coding and RBF features
  - Gradient descent in RL
  - Semi-gradient methods
  - The deadly triad: function approximation, bootstrapping, off-policy
  - Convergence issues and solutions
  - From-scratch linear function approximation
  - Environment: MountainCar with continuous states

- **6b_function_approximation_practical.ipynb**
  - Implementing tile coding
  - Neural network function approximation basics
  - Feature selection and engineering
  - Diagnosing divergence
  - Environment: CartPole, MountainCar

### Deep Q-Networks (DQN)

**Lesson 7: Deep Q-Networks** - Deep learning meets RL
- **7a_dqn_theory.ipynb**
  - Neural networks as Q-function approximators
  - Experience replay: motivation and theory
  - Fixed Q-targets
  - DQN algorithm derivation
  - Addressing instability in deep RL
  - DQN variants: Double DQN, Dueling DQN, Prioritized Experience Replay
  - Rainbow DQN: combining improvements
  - From-scratch DQN with PyTorch
  - Environment: CartPole, Pong (Atari)

- **7b_dqn_practical.ipynb**
  - Production DQN implementation
  - CNN architectures for Atari games
  - Hyperparameter tuning for DQN
  - Monitoring and debugging deep RL
  - Using Stable-Baselines3 for DQN
  - Environment: Atari games (Breakout, Pong)

### Policy Gradient Methods

**Lesson 8: Policy Gradient Methods** - Directly optimizing policies
- **8a_policy_gradients_theory.ipynb**
  - Policy parameterization
  - Policy gradient theorem derivation
  - REINFORCE algorithm
  - Baseline functions and variance reduction
  - Actor-Critic methods
  - Advantage function A(s,a) = Q(s,a) - V(s)
  - A2C and A3C algorithms
  - From-scratch REINFORCE and Actor-Critic
  - Environment: CartPole, LunarLander

- **8b_policy_gradients_practical.ipynb**
  - Implementing policy networks with PyTorch
  - Training stability techniques
  - Entropy regularization
  - Using Stable-Baselines3 for A2C
  - Environment: LunarLander, BipedalWalker

### Advanced Policy Optimization

**Lesson 9: Trust Region and Proximal Methods** - Stable policy optimization
- **9a_trpo_ppo_theory.ipynb**
  - Problems with large policy updates
  - Trust Region Policy Optimization (TRPO)
  - KL divergence constraints
  - Natural policy gradients
  - Proximal Policy Optimization (PPO)
  - Clipped surrogate objective
  - Adaptive KL penalty
  - Why PPO became the standard
  - Mathematical derivations
  - Environment: HalfCheetah, Hopper

- **9b_trpo_ppo_practical.ipynb**
  - Production PPO implementation with Stable-Baselines3
  - Hyperparameter tuning for PPO
  - Vectorized environments for faster training
  - PPO for continuous control
  - Environment: MuJoCo environments (HalfCheetah, Ant, Humanoid)

### Continuous Action Spaces

**Lesson 10: Continuous Control** - RL for robotics
- **10a_continuous_control_theory.ipynb**
  - Challenges of continuous action spaces
  - Deterministic Policy Gradient (DPG)
  - Deep Deterministic Policy Gradient (DDPG)
  - Twin Delayed DDPG (TD3)
  - Soft Actor-Critic (SAC)
  - Entropy-regularized RL
  - From-scratch DDPG implementation
  - Environment: Pendulum

- **10b_continuous_control_practical.ipynb**
  - Implementing SAC with Stable-Baselines3
  - Comparing DDPG, TD3, and SAC
  - Hyperparameter sensitivity in continuous control
  - Real-world robotics considerations
  - Environment: Reacher, Pusher, MuJoCo robotics

### Model-Based RL

**Lesson 11: Model-Based Reinforcement Learning** - Learning and planning
- **11a_model_based_theory.ipynb**
  - Dyna architecture
  - Integrated planning and learning
  - Dyna-Q algorithm
  - Model learning: supervised learning in RL
  - Planning with learned models
  - Exploration with models
  - World models
  - Model-based vs. model-free tradeoffs
  - From-scratch Dyna-Q
  - Environment: GridWorld, Maze

- **11b_model_based_practical.ipynb**
  - Implementing forward models
  - Monte Carlo Tree Search (MCTS) basics
  - AlphaZero-style algorithms
  - Using world models for planning
  - Environment: CartPole, simple robotics tasks

### Multi-Agent RL

**Lesson 12: Multi-Agent Reinforcement Learning** - Multiple agents
- **12a_marl_theory.ipynb**
  - Cooperative vs. competitive vs. mixed settings
  - Nash equilibria in games
  - Independent Q-Learning
  - Centralized training, decentralized execution (CTDE)
  - Communication between agents
  - Credit assignment problem
  - Game-theoretic concepts
  - Environment: Simple tag, Predator-prey

- **12b_marl_practical.ipynb**
  - PettingZoo environments
  - Implementing multi-agent training loops
  - Cooperative navigation tasks
  - Competitive games
  - Environment: PettingZoo environments

### Advanced Topics

**Lesson 13: Exploration Strategies** - Beyond ε-greedy
- **13a_exploration_theory.ipynb**
  - The exploration-exploitation dilemma
  - Upper Confidence Bound (UCB)
  - Thompson sampling
  - Intrinsic motivation
  - Curiosity-driven exploration
  - Count-based exploration
  - Random Network Distillation (RND)
  - Environment: Hard exploration tasks

- **13b_exploration_practical.ipynb**
  - Implementing curiosity modules
  - Using RND with PPO
  - Sparse reward environments
  - Environment: Montezuma's Revenge, procedurally generated mazes

**Lesson 14: Offline RL and Imitation Learning** - Learning from data
- **14a_offline_rl_theory.ipynb**
  - Batch RL / Offline RL motivation
  - Behavioral cloning
  - Inverse reinforcement learning
  - GAIL (Generative Adversarial Imitation Learning)
  - Conservative Q-Learning (CQL)
  - Learning from demonstrations
  - Connection to RLHF and preference learning
  - Environment: Expert demonstrations

- **14b_offline_rl_practical.ipynb**
  - Implementing behavioral cloning
  - Using offline RL libraries (D4RL)
  - Combining offline and online RL
  - Preparing for RLHF applications
  - Environment: D4RL benchmark

**Lesson 15: Hierarchical RL** - Options and skills
- **15a_hierarchical_rl_theory.ipynb**
  - Temporal abstraction
  - Options framework
  - Semi-MDPs
  - Skill discovery
  - Feudal RL
  - Goal-conditioned RL
  - Hindsight Experience Replay (HER)
  - Environment: Complex navigation tasks

- **15b_hierarchical_rl_practical.ipynb**
  - Implementing options
  - Using HER with goal-conditioned policies
  - Skill chaining
  - Environment: FetchReach, FetchPush (robotics)

**Lesson 16: RLHF and LLM Alignment** - Reinforcement Learning from Human Feedback (CRITICAL 2025-2026)
- **16a_rlhf_theory.ipynb**
  - Motivation: Aligning AI with human values
  - The RLHF pipeline: SFT → Reward Modeling → RL Fine-tuning
  - Reward modeling from human preferences
  - Bradley-Terry preference model
  - PPO for language model fine-tuning
  - KL divergence constraints (preventing policy drift)
  - Direct Preference Optimization (DPO) - alternative to RL
  - Constitutional AI and value specification
  - Safe RLHF and alignment challenges
  - Reward hacking and specification gaming
  - Mathematical foundations of preference learning
  - Environment: Text generation, instruction following

- **16b_rlhf_practical.ipynb**
  - Collecting preference datasets
  - Training reward models on preference pairs
  - Implementing PPO-based RLHF with TRLX
  - Implementing Direct Preference Optimization (DPO)
  - Fine-tuning open-source LLMs (LLaMA, Mistral, Gemma)
  - Using Hugging Face TRL (Transformer Reinforcement Learning)
  - Evaluation: Human evaluation, LLM-as-judge
  - Monitoring for reward hacking
  - Comparing RLHF vs DPO vs other alignment methods
  - Real-world applications: ChatGPT, Claude, Gemini alignment
  - Environment: Instruction-following datasets (Anthropic HH-RLHF, OpenAssistant)

### Professional Practice (X-Series)

**X1_rl_debugging.ipynb** - Debugging and Best Practices
- Common failure modes in RL (no learning, catastrophic forgetting, instability)
- Debugging strategies and diagnostic tools
- Logging and visualization (TensorBoard, Weights & Biases, Neptune)
- Reproducibility in RL experiments (seeds, determinism, environment versioning)
- Hyperparameter sensitivity analysis and tuning
- Statistical testing and multiple random seeds
- Code quality: testing, modularization, documentation
- Practical tips from RL practitioners (DeepMind, OpenAI, Berkeley)

**X2_rl_evaluation.ipynb** - Evaluation and Benchmarking
- Evaluating RL agents properly (separate train/eval, deterministic evaluation)
- Learning curves and statistical significance (bootstrap, t-tests)
- Sample efficiency metrics and wall-clock time
- Episodic return vs. average reward vs. success rate
- Comparing RL algorithms fairly (Atari benchmarks, MuJoCo, D4RL)
- Benchmark environments and baseline performance
- Reporting standards for RL research
- Using rliable for rigorous evaluation

**X3_rl_deployment.ipynb** - Production MLOps for RL
- Deploying RL models to production (serving, APIs, edge devices)
- Model quantization and optimization for inference
- Monitoring deployed RL agents (performance tracking, data drift)
- A/B testing RL policies in production
- Sim-to-real transfer for robotics
- Safety considerations and guardrails
- Safe exploration strategies
- Reward specification and preventing reward hacking
- Human-in-the-loop RL and human oversight
- Real-world RL case studies (robotics, recommendation systems, trading)
- Cost optimization and infrastructure considerations

**X4_rl_research_frontiers.ipynb** - Cutting-Edge Topics (2025-2026)
- Meta-RL: learning to learn (MAML, RL², contextual RL)
- Transfer learning in RL and multi-task RL
- Sim2Real techniques (domain randomization, system identification)
- Model-based RL with neural networks (world models, Dreamer, MuZero)
- Transformer-based RL (Decision Transformer, trajectory transformers)
- Foundation models for RL and generalist agents (Gato, RT-2)
- Test-time compute scaling and inference-time planning
- Emergent capabilities in LLMs through RLHF
- AI safety and alignment research directions
- Current research frontiers (NeurIPS, ICLR, ICML papers)
- Resources for staying updated (blogs, papers, conferences)

## Environments

### Classic Control
- **GridWorld**: Custom implementation for teaching
- **FrozenLake**: Slippery grid navigation
- **CartPole**: Balancing a pole on a cart
- **MountainCar**: Sparse reward, momentum-based task
- **Pendulum**: Continuous control

### Atari Games (Arcade Learning Environment)
- **Pong**: Simple game for DQN introduction
- **Breakout**: Visual complexity
- **Montezuma's Revenge**: Hard exploration

### Robotics (MuJoCo / PyBullet)
- **Reacher**: Robotic arm control
- **HalfCheetah**: Locomotion
- **Hopper**: Single-leg robot
- **Ant**: Quadruped robot
- **Humanoid**: Complex humanoid control

### Multi-Agent
- **PettingZoo**: Multi-agent environment library
- **SMAC**: StarCraft Multi-Agent Challenge

### Goal-Conditioned
- **FetchReach, FetchPush**: Robotic manipulation
- **Hand manipulation**: Complex dexterous control

## Technical Stack
- **Core Libraries**: NumPy, Pandas, Matplotlib, Seaborn
- **RL Frameworks**:
  - Gymnasium (formerly OpenAI Gym) - environments
  - Stable-Baselines3 (SB3) - algorithm implementations
  - RLlib (Ray) - distributed RL
  - Tianshou (alternative to SB3)
- **Deep Learning**: PyTorch, torchvision
- **LLM & RLHF Libraries** (NEW 2025-2026):
  - Hugging Face Transformers - pre-trained models
  - Hugging Face TRL (Transformer Reinforcement Learning) - RLHF toolkit
  - TRLX (CarperAI) - PPO-based RLHF implementation
  - Datasets library - preference datasets (HH-RLHF, OpenAssistant)
- **Simulators**:
  - MuJoCo (physics simulator)
  - PyBullet (open-source alternative)
  - Arcade Learning Environment (Atari)
- **Visualization & Logging**: TensorBoard, Weights & Biases, Neptune, Plotly
- **Multi-Agent**: PettingZoo
- **Testing & Quality**: pytest, nbval (notebook testing), rliable (evaluation)

## Implementation Timeline
**Phase 1: Foundation & Classical RL** (Lessons 0-5) - 12 notebooks
- MDPs, DP, MC, TD learning, eligibility traces
- Establishes mathematical foundations and tabular methods

**Phase 2: Scaling Up** (Lessons 6-7) - 4 notebooks
- Function approximation, DQN, deep RL basics
- Bridges classical RL to deep learning

**Phase 3: Policy Methods** (Lessons 8-9) - 4 notebooks
- Policy gradients, REINFORCE, Actor-Critic, PPO
- Modern policy optimization (PPO is industry standard)

**Phase 4: Continuous Control** (Lesson 10) - 2 notebooks
- DDPG, TD3, SAC for robotics
- Critical for real-world applications

**Phase 5: Advanced Topics** (Lessons 11-15) - 10 notebooks
- Model-based RL, multi-agent, exploration, offline RL, hierarchical RL
- Specialized techniques for complex domains

**Phase 6: LLM Alignment** (Lesson 16) - 2 notebooks ⭐ NEW 2025-2026
- RLHF, DPO, reward modeling, safe alignment
- CRITICAL: Aligning AI systems with human values
- Applications: ChatGPT, Claude, Gemini-style alignment

**Phase 7: Professional Practice** (X-Series) - 4 notebooks
- Debugging, evaluation, deployment, research frontiers
- Production MLOps and best practices

**Total: 38 notebooks + 2 RLHF notebooks = 40 notebooks**
**Estimated Timeline: 12-18 months for complete implementation**

## Repository Structure
```
reinforcement-learning/
├── notebooks/                          # All Jupyter notebooks (40 total)
│   ├── 0a_rl_introduction_theory.ipynb
│   ├── 0b_rl_setup_practical.ipynb
│   ├── 1a_mdp_theory.ipynb
│   ├── 1b_mdp_practical.ipynb
│   ├── ... (Lessons 2-15, all 'a' and 'b' notebooks)
│   ├── 16a_rlhf_theory.ipynb          # NEW: RLHF for LLM alignment
│   ├── 16b_rlhf_practical.ipynb       # NEW: Practical RLHF implementation
│   ├── X1_rl_debugging.ipynb
│   ├── X2_rl_evaluation.ipynb
│   ├── X3_rl_deployment.ipynb
│   └── X4_rl_research_frontiers.ipynb
├── datasets/                          # Training data and examples
│   ├── gridworld/                     # Custom environments data
│   ├── saved_episodes/                # Recorded trajectories
│   ├── expert_demos/                  # Demonstration data
│   └── preference_data/               # RLHF preference datasets
├── models/                            # Trained models and checkpoints
│   ├── dqn_cartpole.zip              # Saved policies
│   ├── ppo_halfcheetah.zip
│   └── rlhf_reward_model.pth
├── data/                              # Additional resources
│   └── benchmark_results/             # Performance baselines
├── static/                            # Documentation assets
│   └── images/                        # Diagrams, plots, visualizations
├── envs/                              # Custom environment implementations
│   └── custom_gridworld.py
├── tests/                             # Testing infrastructure
│   ├── test_implementations.py        # Algorithm tests
│   ├── test_environments.py           # Environment tests
│   └── test_notebooks.py              # Notebook validation (nbval)
├── utils/                             # Shared utilities
│   ├── plotting.py                    # Visualization helpers
│   ├── evaluation.py                  # Metrics and evaluation
│   └── wrappers.py                    # Environment wrappers
├── .python-version                    # Python version (3.10.0)
├── .gitignore                         # Git ignore patterns
├── requirements.txt                   # Core dependencies
├── requirements-dev.txt               # Development dependencies (testing, linting)
├── README.md                          # Project overview
├── CURRICULUM_PLAN.md                 # Detailed curriculum (this file)
└── LICENSE.md                         # Apache 2.0 license
```

## Testing and Quality Standards

Following elite university practices (Berkeley, MIT, Stanford):

### Jupyter Notebook Standards
- **Google Colab Compatible**: All notebooks runnable in browser with [![Open In Colab]](badges)
- **Cell Organization**:
  - Theory cells: Markdown with LaTeX for mathematical foundations
  - Implementation cells: Clear TODOs with docstrings specifying inputs/outputs
  - Test cells: Immediate feedback with public test cases
  - Visualization cells: Plots and animations for understanding
  - Analysis cells: Written interpretation (manually graded)

### Code Quality
- **Testing Framework**: pytest for algorithm implementations
  - Unit tests for individual functions
  - Integration tests for complete training loops
  - Regression tests for performance baselines
- **Notebook Testing**: nbval for automated notebook execution
- **Code Style**:
  - Black formatter for consistent style
  - Type hints for key functions
  - Comprehensive docstrings
- **Documentation**:
  - Each notebook includes learning objectives
  - Clear explanations before each code block
  - References to papers and textbooks

### Reproducibility
- Random seed setting in all notebooks
- Environment versioning (Gymnasium versions pinned)
- Requirements.txt with exact versions after testing
- Logging of hyperparameters and results

### Evaluation Standards
- Multiple random seeds for statistical significance
- Proper train/validation/test splits
- Benchmark baselines for comparison
- Statistical testing (bootstrap, t-tests)
- Using rliable library for rigorous evaluation

## Success Metrics
- **Comprehensiveness**: Cover classical RL (Sutton & Barto) + modern deep RL + LLM alignment
- **Accessibility**: Explain MDPs and Bellman equations from first principles
- **Practicality**: Every algorithm runnable on Colab, scales to real problems
- **Modern**: Include latest algorithms (PPO, SAC, RLHF, DPO) used in production
- **Hands-On**: Interactive environments, visualizations, immediate feedback
- **2025-2026 Aligned**: RLHF and LLM alignment as core curriculum

## Key Mathematical Concepts
- Markov Decision Processes (MDPs)
- Bellman equations (expectation and optimality)
- Value functions and Q-functions
- Policy gradient theorem
- Advantage functions
- KL divergence for policy optimization
- Temporal difference learning
- Eligibility traces
- Function approximation theory

## Relationship to Other Repositories
- **Supervised ML**: Foundation in gradient descent, neural networks → used in deep RL
- **Unsupervised ML**: Clustering, dimensionality reduction → state representation learning
- **Computer Vision**: CNNs → visual observation processing in Atari/robotics
- **NLP**: Transformers → Decision Transformers, language-conditioned RL

## Learning Path Integration
Students should complete:
1. **Supervised ML** → understand neural networks, gradient descent
2. **Unsupervised ML** → understand representation learning (optional but helpful)
3. **Reinforcement Learning** → combines previous concepts in sequential decision-making

## References and Resources

### Foundational Textbooks
- **Sutton & Barto**: "Reinforcement Learning: An Introduction" (2nd edition, 2018)
- **Dimitri Bertsekas**: "Reinforcement Learning and Optimal Control" (2019)

### University Courses (2025-2026)
- **Stanford CS234**: Emma Brunskill's RL course
- **Berkeley CS285**: Sergey Levine's Deep RL course
- **MIT 6.7920**: Theoretical RL course
- **Cambridge R171**: RL including RLHF
- **Silver's RL Course**: DeepMind UCL lectures (classic)

### Practical Guides
- **OpenAI Spinning Up**: Practical deep RL guide with implementations
- **Hugging Face RL Course**: Modern course including RLHF
- **Stanford CS336**: LLM course with RLHF coverage

### Key Papers (RLHF & Modern RL)
- "Training language models to follow instructions with human feedback" (InstructGPT, 2022)
- "Direct Preference Optimization" (DPO, 2023)
- "Constitutional AI: Harmlessness from AI Feedback" (Anthropic, 2022)
- "Proximal Policy Optimization" (PPO, Schulman et al., 2017)
- "Soft Actor-Critic" (SAC, Haarnoja et al., 2018)

### Online Resources
- **Papers with Code**: Latest RL benchmarks and leaderboards
- **NeurIPS/ICLR/ICML**: Top ML conferences for cutting-edge RL
- **ArXiv**: cs.LG and cs.AI for recent preprints

---

**Status**: Planning complete, ready for Phase 1 implementation
**Updated**: 2025 - Aligned with 2025-2026 elite university standards
**Key Addition**: Lesson 16 on RLHF for LLM alignment (CRITICAL for modern RL)
**Author**: Powell-Clark Limited
