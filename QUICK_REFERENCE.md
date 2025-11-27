# ⚡ Quick Reference Cheat Sheet

Ultra-condensed reference for experienced practitioners. For details, see full notebooks.

---

## 🎯 Algorithm Selection (30-Second Decision)

```
Problem → Algorithm

Discrete actions, small state space     → Q-Learning (Lesson 4)
Discrete actions, large state space     → DQN (Lesson 7) or PPO (Lesson 9)
Continuous actions                      → SAC (Lesson 10) or PPO (Lesson 9)
Multiple agents                         → MADDPG (Lesson 13) or VDN
Sparse rewards                          → HER (Lesson 14) or ICM (Lesson 12)
Need sample efficiency                  → SAC or Model-Based (Lesson 11)
LLM alignment                          → RLHF (Lesson 16) ⭐⭐⭐
Don't know                             → PPO (Lesson 9) - works 80% of time
```

---

## 📋 Algorithm Quick Facts

### Q-Learning (Lesson 4b)
```python
Q(s,a) ← Q(s,a) + α[r + γ max Q(s',a') - Q(s,a)]
```
✅ Guaranteed convergence | ✅ Off-policy | ❌ Tabular only

---

### DQN (Lesson 7b)
```python
Q-network + Experience Replay + Target Network
Loss = (r + γ max Q_target(s',a') - Q(s,a))²
```
✅ Scales to large states | ✅ Stable | ❌ Discrete actions only

**Variants:** Double DQN, Dueling DQN, Rainbow

---

### PPO (Lesson 9b) ⭐ **DEFAULT CHOICE**
```python
L = E[min(r_t·A_t, clip(r_t, 1±ε)·A_t)]
where r_t = π_new(a|s) / π_old(a|s)
```
✅ Stable | ✅ General purpose | ✅ Continuous or discrete | ❌ Sample inefficient

**Hyperparams:** ε=0.2, lr=3e-4, batch=2048

---

### SAC (Lesson 10b) ⭐ **BEST FOR ROBOTICS**
```python
J = E[r + α·H(π)]  (max entropy)
Q-function + Policy network
```
✅ Very stable | ✅ Sample efficient | ✅ Auto-tuning | ❌ Complex

**Hyperparams:** lr=3e-4, τ=0.005, auto α

---

### PPO-RLHF (Lesson 16b) ⭐ **CHATGPT METHOD**
```python
J = E[r_θ(x,y) - β·KL(π || π_ref)]
Pipeline: SFT → Reward Model → PPO
```
✅ LLM alignment | ✅ Human preferences | ❌ Complex pipeline

**Hyperparams:** β=0.02, KL target=0.01

---

### DPO (Lesson 16b) ⭐ **SIMPLER RLHF**
```python
L = -E[log σ(β·log(π/π_ref)[y_w] - β·log(π/π_ref)[y_l])]
```
✅ No reward model | ✅ More stable | ✅ Simpler | ❌ Less flexible

**Use for:** LLM alignment without complexity

---

## 🔢 Key Equations

### Bellman Equations
```
V(s) = E[r + γ·V(s')]
Q(s,a) = E[r + γ·max Q(s',a')]
V*(s) = max_a Q*(s,a)
```

### Policy Gradient Theorem
```
∇J(θ) = E[∇log π(a|s)·Q(s,a)]
      = E[∇log π(a|s)·A(s,a)]  (with baseline)
```

### TD Error
```
δ = r + γ·V(s') - V(s)
```

### Advantage (GAE)
```
A(s,a) = Q(s,a) - V(s)
GAE: A_t = Σ(γλ)^k δ_{t+k}
```

---

## 🎨 Network Architectures

### Value Network (DQN)
```python
state → [64] ReLU → [64] ReLU → [n_actions]
```

### Actor-Critic (PPO/SAC)
```python
# Actor (Policy)
state → [64] ReLU → [64] ReLU → [n_actions] Softmax/Tanh

# Critic (Value)
state → [64] ReLU → [64] ReLU → [1]
```

### Reward Model (RLHF)
```python
(prompt, response) → LM backbone → [1] (scalar reward)
```

---

## ⚙️ Critical Hyperparameters

| Param | Range | Importance | Notes |
|-------|-------|------------|-------|
| Learning rate | 1e-5 to 1e-3 | ⭐⭐⭐ | Most critical, tune first |
| Gamma (γ) | 0.95 to 0.999 | ⭐⭐⭐ | Higher for long horizon |
| Batch size | 32 to 512 | ⭐⭐ | Affects stability |
| Network size | [64,128,256] | ⭐⭐ | Bigger ≠ better |
| Entropy coef | 1e-4 to 1e-1 | ⭐⭐ | Higher = more exploration |
| PPO ε | 0.1 to 0.3 | ⭐⭐ | Trust region size |
| GAE λ | 0.9 to 0.99 | ⭐ | Bias-variance tradeoff |

**Pro tip:** Start with defaults, tune learning rate first!

---

## 🐛 Debugging Quick Fixes

| Symptom | Fix |
|---------|-----|
| Not learning | ↑ learning rate, check reward scaling |
| Unstable training | ↓ learning rate, add gradient clipping |
| Policy collapse | ↑ entropy coefficient |
| Value divergence | Normalize rewards, clip value loss |
| Slow convergence | ↑ network size or learning rate |
| Overexploration | ↓ entropy coefficient |

**See Lesson X3 for systematic debugging**

---

## 📊 Performance Baselines

### CartPole-v1 (500 max)
- Random: ~20
- DQN: ~500 (solved)
- PPO: ~500 (solved)

### LunarLander-v2 (200 = solved)
- Random: ~-200
- DQN: ~200
- PPO: ~250

### HalfCheetah-v3 (higher = better)
- Random: ~-300
- SAC: ~12,000
- TD3: ~10,000

---

## 💻 Code Snippets

### Quick DQN
```python
# See Lesson 7b for full implementation
model = nn.Sequential(
    nn.Linear(state_dim, 64), nn.ReLU(),
    nn.Linear(64, 64), nn.ReLU(),
    nn.Linear(64, action_dim)
)
optimizer = optim.Adam(model.parameters(), lr=1e-3)

# Training loop
for step in range(num_steps):
    action = epsilon_greedy(model(state))
    next_state, reward, done = env.step(action)
    replay_buffer.add(state, action, reward, next_state, done)

    batch = replay_buffer.sample(32)
    loss = compute_dqn_loss(model, target_model, batch)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
```

### Quick PPO
```python
# See Lesson 9b for full implementation
policy = Actor(state_dim, action_dim)
value_fn = Critic(state_dim)

# Training loop
for iteration in range(num_iterations):
    states, actions, rewards, advantages = collect_rollouts(policy)

    for epoch in range(ppo_epochs):
        ratio = policy.get_ratio(states, actions)
        loss = -torch.min(
            ratio * advantages,
            torch.clamp(ratio, 1-epsilon, 1+epsilon) * advantages
        ).mean()

        update(policy, loss)
```

### Quick RLHF Reward Model
```python
# See Lesson 16b for full implementation
reward_model = RewardModel(vocab_size)

# Training
for batch in preference_dataset:
    seq1, seq2, preference = batch
    r1 = reward_model(seq1)
    r2 = reward_model(seq2)

    # Bradley-Terry model
    loss = -log_sigmoid((r2 - r1) if preference == 1 else (r1 - r2))
    loss.backward()
    optimizer.step()
```

---

## 🚀 Quick Start Commands

### Run Notebook
```bash
jupyter notebook notebooks/9b_ppo_practical.ipynb
```

### Train Agent (example)
```python
import gymnasium as gym
env = gym.make('CartPole-v1')
# See lesson notebooks for complete training scripts
```

### Install Requirements
```bash
pip install numpy torch gymnasium matplotlib
```

---

## 📚 When to Use Which Lesson

**Learning Goal → Lesson**

| Goal | Go To |
|------|-------|
| Understand RL basics | Lesson 0-1 |
| Implement Q-Learning | Lesson 4 |
| Deep RL (Atari) | Lesson 7 (DQN) |
| Most useful algorithm | Lesson 9 (PPO) ⭐ |
| Robotics | Lesson 10 (SAC) ⭐ |
| LLM alignment | Lesson 16 (RLHF) ⭐⭐⭐ |
| Production deployment | Lesson X1 |
| Hyperparameter tuning | Lesson X2 ⭐ |
| Debugging issues | Lesson X3 ⭐ |
| Real-world examples | Lesson X4 |

---

## 🎯 Production Checklist

Before deploying RL to production:

- [ ] Tested on held-out evaluation set
- [ ] Hyperparameters tuned systematically (Lesson X2)
- [ ] Safety constraints implemented (Lesson X1)
- [ ] Monitoring and alerting set up (Lesson X1)
- [ ] A/B test framework ready (Lesson X1)
- [ ] Rollback plan prepared
- [ ] Performance baselines established
- [ ] Edge cases tested
- [ ] Documentation complete

**See Lesson X1 for full production guide**

---

## 📖 Paper References (Essentials)

1. **DQN**: Mnih et al. (2015) - Playing Atari with Deep RL
2. **PPO**: Schulman et al. (2017) - Proximal Policy Optimization
3. **SAC**: Haarnoja et al. (2018) - Soft Actor-Critic
4. **InstructGPT**: Ouyang et al. (2022) - Training LMs with RLHF
5. **DPO**: Rafailov et al. (2023) - Direct Preference Optimization

**Full references in each lesson notebook**

---

## 🔗 Quick Links

- **README**: Full curriculum overview
- **ALGORITHM_GUIDE**: Detailed algorithm selection
- **NOTEBOOK_INDEX**: All 40 notebooks described
- **COMPLETION_SUMMARY**: Achievement summary
- **BUILD_LOG**: Progress tracking

---

## 💡 Pro Tips

1. **Start Simple**: Random agent → Baseline → Full algorithm
2. **Tune Learning Rate First**: Most important hyperparameter
3. **Monitor Everything**: Not just reward (see Lesson X3)
4. **Use PPO by Default**: Works for 80% of problems
5. **RLHF is Critical**: Essential for LLMs in 2025
6. **Don't Skip X-Series**: Production skills matter
7. **Visualize Behavior**: Don't just look at numbers
8. **Test Early, Test Often**: Catch bugs before scaling

---

## ⚡ Ultra-Quick Algorithm Picker

**30-Second Decision Tree:**

1. Working with LLM? → **Lesson 16 (RLHF)**
2. Continuous actions? → **Lesson 10 (SAC)**
3. Discrete actions? → **Lesson 9 (PPO)**
4. Multiple agents? → **Lesson 13**
5. Not sure? → **Lesson 9 (PPO)**

**That's it!** See full notebooks for implementations.

---

## 📞 Need Help?

- **Beginner**: Start with Lesson 0a
- **Stuck**: Check Lesson X3 (Debugging)
- **Not converging**: See Lesson X2 (Tuning)
- **Production issues**: Lesson X1 (Deployment)
- **LLM alignment**: Lesson 16 (RLHF) ⭐

---

*Quick Reference v1.0*
*Last Updated: 2025-01-23*
*See full notebooks for complete implementations*
*40/40 Notebooks • 35,000+ Lines • Legendary Status 🏆*
