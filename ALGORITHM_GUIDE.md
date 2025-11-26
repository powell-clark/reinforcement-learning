# RL Algorithm Quick Reference Guide

**When to use which algorithm?** This guide helps you choose the right RL algorithm for your problem.

---

## 🎯 Decision Tree: Choose Your Algorithm

```
START
  |
  ├─ Discrete Actions?
  │   ├─ YES → Tabular state space?
  │   │   ├─ YES → Q-Learning or SARSA (Lesson 4)
  │   │   └─ NO → DQN (Lesson 7) or PPO (Lesson 9)
  │   └─ NO (Continuous) → DDPG, TD3, or SAC (Lesson 10)
  │
  ├─ Multiple Agents?
  │   └─ YES → Multi-Agent RL (Lesson 13)
  │       ├─ Independent → IQL
  │       ├─ Cooperative → VDN, QMIX
  │       └─ Competitive → MADDPG
  │
  ├─ Need Model of Environment?
  │   └─ YES → Model-Based RL (Lesson 11)
  │       ├─ Dyna-Q (simple)
  │       ├─ MBPO (complex)
  │       └─ MuZero (no rules)
  │
  ├─ Sparse Rewards?
  │   └─ YES → Exploration or Hierarchical
  │       ├─ Exploration (Lesson 12): ICM, RND
  │       └─ Hierarchical (Lesson 14): HER, Options
  │
  ├─ Few-Shot Learning?
  │   └─ YES → Meta-Learning (Lesson 15)
  │       ├─ MAML
  │       └─ RL²
  │
  ├─ Aligning LLM?
  │   └─ YES → RLHF (Lesson 16) ⭐
  │       ├─ PPO-RLHF (ChatGPT)
  │       ├─ DPO (simpler)
  │       └─ Constitutional AI (Claude)
  │
  └─ Production Deployment?
      └─ YES → Professional Practice (X1-X4)
```

---

## 📊 Algorithm Comparison Table

| Algorithm | Action Space | State Space | Sample Efficiency | Stability | Use Case |
|-----------|--------------|-------------|-------------------|-----------|----------|
| **Q-Learning** | Discrete | Tabular | Medium | High | Small problems, guaranteed convergence |
| **DQN** | Discrete | Large | Medium | Medium | Atari games, discrete action spaces |
| **PPO** | Both | Large | Low | High | General purpose, most popular! |
| **SAC** | Continuous | Large | High | High | Robotics, continuous control |
| **DDPG** | Continuous | Large | Medium | Low | Continuous control (older) |
| **TD3** | Continuous | Large | High | Medium | Improved DDPG |
| **TRPO** | Both | Large | Low | Very High | When stability critical |
| **A3C** | Both | Large | Medium | Medium | Parallel training |

---

## 🏆 Top Recommendations by Domain

### 🎮 Games (Discrete Actions)
**Best:** DQN (Lesson 7) or PPO (Lesson 9)
- **DQN** if Atari-style games (pixel inputs)
- **PPO** if more complex (recommended)
- **AlphaZero** if perfect information games (Lesson X4)

### 🤖 Robotics (Continuous Control)
**Best:** SAC (Lesson 10) or PPO (Lesson 9)
- **SAC** for sample efficiency
- **TD3** as alternative
- **PPO** for stability
- Add **HER** (Lesson 14) if sparse rewards

### 💬 Language Models (LLMs)
**Best:** RLHF (Lesson 16) ⭐ **MOST IMPORTANT**
- **PPO-RLHF** for ChatGPT-style
- **DPO** for simpler training
- **Constitutional AI** for safety

### 📺 Recommendations (YouTube, Netflix)
**Best:** Batch RL with exploration
- Offline RL from logged data
- Contextual bandits (Lesson 12)
- A/B testing framework (Lesson X1)

### 🏢 Finance / Trading
**Best:** Model-Based or Offline RL
- **Dyna-Q** (Lesson 11) for sample efficiency
- **MBPO** for more complex
- Offline RL for safety (no live experiments)

### 🚗 Autonomous Vehicles
**Best:** SAC + Safety Constraints
- **SAC** (Lesson 10) for continuous control
- Safe RL (Lesson X1) for constraints
- Model-based (Lesson 11) for prediction

---

## 🔍 Detailed Algorithm Descriptions

### Value-Based Methods

#### Q-Learning (Lesson 4b)
```python
Q(s,a) ← Q(s,a) + α[r + γ max_a' Q(s',a') - Q(s,a)]
```
**Pros:** Simple, guaranteed convergence, off-policy
**Cons:** Only tabular, overestimates values
**Use when:** Small discrete state/action spaces

#### DQN (Lesson 7b)
```python
Q-network with experience replay + target network
```
**Pros:** Scales to large state spaces, stable
**Cons:** Discrete actions only, sample inefficient
**Use when:** Atari games, large but discrete actions

#### Double DQN (Lesson 7b)
```python
Target = r + γ Q_target(s', argmax_a Q(s',a))
```
**Pros:** Reduces overestimation
**Cons:** Still discrete actions
**Use when:** DQN but need better value estimates

---

### Policy-Based Methods

#### REINFORCE (Lesson 8b)
```python
∇J = E[∇log π(a|s) * G_t]
```
**Pros:** Works with continuous actions, simple
**Cons:** High variance, sample inefficient
**Use when:** Simple baseline, continuous actions

#### Actor-Critic (Lesson 8b)
```python
Actor: π(a|s), Critic: V(s) or Q(s,a)
```
**Pros:** Lower variance than REINFORCE
**Cons:** More complex, two networks
**Use when:** Need balance of policy + value

#### PPO (Lesson 9b) ⭐ **MOST POPULAR**
```python
L = min(r_t * A_t, clip(r_t, 1±ε) * A_t)
```
**Pros:** Stable, general purpose, state-of-the-art
**Cons:** Sample inefficient
**Use when:** Default choice for most problems!

#### TRPO (Lesson 9a)
```python
Constrained: KL(π_old || π_new) ≤ δ
```
**Pros:** Very stable, monotonic improvement
**Cons:** Complex, computationally expensive
**Use when:** Stability is critical

---

### Continuous Control

#### DDPG (Lesson 10b)
```python
Deterministic policy: μ(s), Critic: Q(s,a)
```
**Pros:** Continuous actions, off-policy
**Cons:** Unstable, sensitive to hyperparameters
**Use when:** Continuous control (older baseline)

#### TD3 (Lesson 10b)
```python
DDPG + twin critics + delayed updates + noise
```
**Pros:** More stable than DDPG
**Cons:** Still somewhat sensitive
**Use when:** Improved DDPG

#### SAC (Lesson 10b) ⭐ **BEST FOR ROBOTICS**
```python
Max entropy: J = E[r + α H(π)]
```
**Pros:** Very stable, sample efficient, automatic temp tuning
**Cons:** Complex
**Use when:** Robotics, continuous control (recommended)

---

### Advanced Algorithms

#### Dyna-Q (Lesson 11b)
```python
Model-based: Learn model, plan with model
```
**Pros:** Sample efficient
**Cons:** Model errors compound
**Use when:** Sample efficiency critical

#### ICM / RND (Lesson 12b)
```python
Intrinsic curiosity: r_intrinsic = prediction error
```
**Pros:** Solves exploration
**Cons:** Can be distracted
**Use when:** Sparse rewards, need exploration

#### HER (Lesson 14b)
```python
Hindsight: "What if that was my goal?"
```
**Pros:** Solves sparse rewards in goal-conditioned tasks
**Cons:** Requires goal-based formulation
**Use when:** Robotics with goal states

#### MAML (Lesson 15b)
```python
Meta-learning: Learn to learn quickly
```
**Pros:** Few-shot adaptation
**Cons:** Complex, expensive
**Use when:** Need fast adaptation to new tasks

---

## 🌟 RLHF (Lesson 16) - Most Important for 2025!

### PPO-RLHF (ChatGPT Approach)
```python
Objective: E[r_θ(x,y) - β KL(π || π_ref)]
```
**Use for:**
- ChatGPT-style LLM alignment
- Training helpful, harmless AI
- Learning from human preferences

**Pipeline:**
1. SFT: Supervised fine-tuning on demos
2. Reward Model: Train on preference comparisons
3. PPO: Optimize policy with learned reward

### DPO (Direct Preference Optimization)
```python
Loss = -E[log σ(β log(π/π_ref)[y_w] - β log(π/π_ref)[y_l])]
```
**Use for:**
- Simpler alternative to RLHF
- No separate reward model
- More stable training

**When to use DPO vs PPO-RLHF:**
- **DPO**: Simpler, more stable, easier to implement
- **PPO-RLHF**: More flexible, better for complex rewards

### Constitutional AI (Claude)
**Use for:**
- Principle-based AI safety
- Transparent value alignment
- Scalable oversight with AI feedback

---

## 📚 Learning Path by Goal

### 🎓 Academic / Researcher
1. Start: Lessons 0-5 (Foundations)
2. Deep RL: Lessons 6-7 (DQN)
3. Policy Gradients: Lessons 8-9 (PPO)
4. Pick specialty: 10-15
5. **RLHF: Lesson 16** (Critical for 2025!)

### 🏭 Industry / Engineer
1. Quick foundations: Lessons 0-1
2. Jump to: PPO (Lesson 9) - most used
3. Add: SAC (Lesson 10) if robotics
4. **RLHF (Lesson 16)** if working with LLMs
5. Professional: X1-X4 (deployment)

### 💬 LLM / AI Safety Focus
1. Basic RL: Lessons 0, 4, 8
2. Policy Gradients: Lesson 9 (PPO)
3. **Jump to: Lesson 16 (RLHF)** ⭐
4. Production: X1-X4

### 🤖 Robotics Focus
1. Foundations: Lessons 0-5
2. Continuous: Lesson 10 (SAC)
3. Hierarchical: Lesson 14 (HER)
4. Meta-learning: Lesson 15
5. Sim-to-real: X4

---

## ⚡ Quick Algorithm Selection

### "Just tell me what to use!"

**Default Choice:**
→ **PPO (Lesson 9)** - Works for 80% of problems

**If continuous actions:**
→ **SAC (Lesson 10)** - Best for robotics

**If aligning LLM:**
→ **RLHF (Lesson 16)** ⭐ - ChatGPT approach

**If need sample efficiency:**
→ **SAC or Model-Based (Lesson 11)**

**If multiple agents:**
→ **MADDPG or VDN (Lesson 13)**

**If sparse rewards:**
→ **HER (Lesson 14) or ICM (Lesson 12)**

---

## 🔧 Hyperparameter Importance

### Critical (Tune First!)
1. **Learning rate**: 1e-5 to 1e-3 (log scale)
2. **Entropy coefficient**: Exploration amount
3. **Batch size**: Affects stability
4. **Gamma**: Discount factor (0.95-0.999)

### Important
5. Network size: [64, 128, 256]
6. PPO clip ε: 0.1-0.3
7. GAE λ: 0.9-0.99

See **Lesson X2** for comprehensive tuning guide!

---

## 🐛 Common Issues & Fixes

### "Agent not learning"
→ Check: Learning rate, reward scaling, observations
→ See: **Lesson X3** (Debugging)

### "Training unstable"
→ Try: Lower learning rate, add gradient clipping
→ Use: PPO or SAC (more stable)

### "Sample inefficient"
→ Try: SAC, model-based (Lesson 11)
→ Or: Better exploration (Lesson 12)

### "Policy collapses"
→ Fix: Increase entropy coefficient
→ Or: KL penalty (RLHF)

---

## 📖 Further Reading

- **OpenAI Spinning Up**: Algorithm comparisons
- **Stable Baselines3 Docs**: Implementation details
- **Papers with Code**: Latest benchmarks
- **This Curriculum**: Complete implementations of everything!

---

## 🎯 Summary

**Most Important Algorithms:**
1. **PPO** (Lesson 9) - General purpose ⭐
2. **SAC** (Lesson 10) - Robotics
3. **RLHF** (Lesson 16) - LLM alignment ⭐⭐⭐

**Start Here:**
- Beginner → Lesson 0
- Experienced → Lesson 9 (PPO)
- LLM Focus → Lesson 16 (RLHF)

**Remember:**
- PPO works for 80% of problems
- SAC for continuous control
- RLHF is critical for modern AI (2025)

---

*Last Updated: 2025-01-23*
*See main README.md for complete curriculum*
