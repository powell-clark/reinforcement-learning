# Notebooks Directory

This directory contains all 40 Jupyter notebooks for the Reinforcement Learning curriculum.

## Structure

### Lessons (34 notebooks)
Each lesson has two notebooks:
- **Xa_topic_theory.ipynb**: Mathematical foundations, derivations, proofs
- **Xb_topic_practical.ipynb**: Implementation, experiments, production code

### X-Series (4 notebooks)
Professional practice notebooks:
- **X1_rl_debugging.ipynb**: Debugging and best practices
- **X2_rl_evaluation.ipynb**: Evaluation metrics and benchmarking
- **X3_rl_deployment.ipynb**: Production MLOps for RL
- **X4_rl_research_frontiers.ipynb**: Cutting-edge topics (2025-2026)

### Lesson Topics

**Foundation (Lessons 0-2):**
- 0: Introduction to RL
- 1: Markov Decision Processes
- 2: Dynamic Programming

**Classical RL (Lessons 3-5):**
- 3: Monte Carlo Methods
- 4: Temporal Difference Learning
- 5: N-Step & Eligibility Traces

**Deep RL (Lessons 6-7):**
- 6: Function Approximation
- 7: Deep Q-Networks (DQN)

**Policy Methods (Lessons 8-9):**
- 8: Policy Gradients (REINFORCE, Actor-Critic)
- 9: Advanced Policy Optimization (TRPO, PPO)

**Advanced (Lessons 10-15):**
- 10: Continuous Control (DDPG, TD3, SAC)
- 11: Model-Based RL
- 12: Multi-Agent RL
- 13: Exploration Strategies
- 14: Offline RL & Imitation Learning
- 15: Hierarchical RL

**⭐ LLM Alignment (Lesson 16) - NEW 2025-2026:**
- 16: RLHF and LLM Alignment (DPO, Reward Modeling)

## Notebook Standards

All notebooks follow the template in `TEMPLATE_notebook.ipynb`:

### Required Sections
1. **Header**: Title, Colab badge, metadata
2. **Learning Objectives**: Clear goals
3. **Setup**: Imports, random seeds
4. **Introduction**: Motivation, real-world applications
5. **Mathematical Foundations**: Theory with LaTeX
6. **Algorithm Derivation**: Pseudocode
7. **Implementation**: From-scratch + library implementations
8. **Experiments**: Training, evaluation, visualization
9. **Analysis**: Interpretation and insights
10. **Exercises**: Practice problems
11. **References**: Papers, textbooks, code

### Code Quality Standards
- **Reproducibility**: Set random seeds
- **Documentation**: Docstrings for all functions
- **Type Hints**: For clarity
- **Testing**: Autograded test cells
- **Visualization**: Clear plots with labels

### Google Colab Compatibility
All notebooks must:
- Include Colab badge with correct link
- Install dependencies in first cell
- Work without local files (use URLs for data)
- Complete in <10 minutes on Colab free tier

## Running Notebooks

### Locally
```bash
# Install dependencies
pip install -r requirements.txt

# Launch Jupyter
jupyter notebook
```

### Google Colab
Click the "Open in Colab" badge at the top of each notebook.

### Testing
```bash
# Test all notebooks
pytest --nbval notebooks/

# Test specific notebook
pytest --nbval notebooks/0a_rl_introduction_theory.ipynb
```

## Implementation Status

**Status**: 🚧 Under Development

See [CURRICULUM_PLAN.md](../CURRICULUM_PLAN.md) for detailed implementation roadmap.

**Current**: Planning complete, Phase 1 (Lessons 0-2) starting soon.
