# Reinforcement Learning Examples

This directory contains working examples demonstrating RL algorithms from classical to cutting-edge.

## Quick Start

All examples are self-contained Python scripts that can be run directly:

```bash
# Example 1: Q-Learning on FrozenLake
python 01_qlearning_frozen_lake.py

# Example 2: DQN on CartPole
python 02_dqn_cartpole.py

# Example 3: REINFORCE on LunarLander
python 03_reinforce_lunarlander.py

# Example 4: RLHF for LLM Alignment (2025-2026)
python 04_rlhf_llm_alignment.py
```

## Examples Overview

### Classical RL (Tabular Methods)

#### 01_qlearning_frozen_lake.py
- **Algorithm**: Q-Learning (Off-policy TD Control)
- **Environment**: FrozenLake-v1 (4x4 grid world)
- **Key Concepts**: Q-values, Bellman equation, ε-greedy exploration
- **Runtime**: ~30 seconds
- **Expected Performance**: 95-100% success rate

**What you'll learn:**
- How Q-learning discovers optimal paths
- The importance of exploration vs exploitation
- Tabular value functions for discrete spaces

### Deep RL

#### 02_dqn_cartpole.py
- **Algorithm**: Deep Q-Network (DQN)
- **Environment**: CartPole-v1
- **Key Concepts**: Neural networks, experience replay, target networks
- **Runtime**: ~2-5 minutes
- **Expected Performance**: 450+ average reward

**What you'll learn:**
- Scaling Q-learning to continuous state spaces
- Experience replay for breaking correlations
- Target networks for stable training

### Policy Gradients

#### 03_reinforce_lunarlander.py
- **Algorithm**: REINFORCE (Monte Carlo Policy Gradient)
- **Environment**: LunarLander-v2
- **Key Concepts**: Policy gradient theorem, baseline, return computation
- **Runtime**: ~5-10 minutes
- **Expected Performance**: 200+ average reward

**What you'll learn:**
- Direct policy optimization
- Policy gradient theorem in practice
- Variance reduction with baselines

### ⭐ Modern RL (2025-2026)

#### 04_rlhf_llm_alignment.py
- **Algorithm**: RLHF (Reinforcement Learning from Human Feedback)
- **Task**: Text summarization with preference learning
- **Key Concepts**: Reward modeling, PPO, DPO, constitutional AI
- **Runtime**: ~10-15 minutes (CPU), ~2-3 minutes (GPU)
- **Libraries**: Hugging Face Transformers, TRL

**What you'll learn:**
- How ChatGPT/Claude-style alignment works
- Reward modeling from human preferences
- PPO-based LLM fine-tuning
- Direct Preference Optimization (DPO)
- Safe RLHF and alignment challenges

**This is the cutting-edge content that distinguishes elite 2025-2026 curricula!**

## Requirements

```bash
# Install all dependencies
pip install -r requirements.txt

# For RLHF example, also install:
pip install transformers[torch] trl datasets accelerate peft
```

## Running on Google Colab

All examples can run on Google Colab (free tier):

1. Upload the example to Colab
2. Install dependencies in the first cell
3. Run all cells

## Expected Outputs

Each example produces:
- **Console output**: Training progress, metrics
- **Visualizations**: Training curves, performance plots
- **Saved plots**: PNG files in current directory
- **Learned policies**: Can be visualized or saved

## Troubleshooting

### Example fails with import errors
```bash
# Ensure you're in the repo root
cd /path/to/reinforcement-learning

# Install dependencies
pip install -r requirements.txt
```

### RLHF example runs slowly
- Use GPU for 5-10x speedup (Colab: Runtime → Change runtime type → GPU)
- Reduce model size in the script (use smaller LLMs)

### Training doesn't converge
- Increase number of episodes
- Tune hyperparameters (learning rate, epsilon decay)
- Check random seed is set for reproducibility

## Next Steps

After running examples:
1. **Modify hyperparameters**: See how performance changes
2. **Try different environments**: Apply algorithms to new domains
3. **Study notebooks**: Deep dive into theory in `notebooks/`
4. **Implement variants**: Extend algorithms with advanced techniques

## Example Progression

**Recommended order:**
1. Start with 01_qlearning (simplest)
2. Progress to 02_dqn (neural networks)
3. Try 03_reinforce (policy gradients)
4. Finish with 04_rlhf (cutting-edge 2025-2026)

This progression mirrors the course structure and builds intuition incrementally.

## Contributing

Have a great example? Submit a pull request! We welcome examples demonstrating:
- Advanced algorithms (PPO, SAC, TD3)
- Real-world applications (robotics, trading, games)
- Novel environments
- Research implementations

---

**Status**: 4 working examples demonstrating classical → modern RL
**Updated**: 2025
**Aligned with**: Elite 2025-2026 university standards
