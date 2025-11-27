# Contributing to Reinforcement Learning Curriculum

Thank you for your interest in contributing to this comprehensive RL curriculum! This guide will help you get started.

---

## 🌟 Ways to Contribute

### 1. **Report Issues**
- Found a bug in the code?
- Noticed an error in the documentation?
- Have a suggestion for improvement?

**Please open an issue** with:
- Clear description of the problem
- Steps to reproduce (for bugs)
- Expected vs actual behavior
- Your environment (Python version, OS, etc.)

### 2. **Improve Documentation**
- Fix typos or unclear explanations
- Add examples or clarifications
- Improve code comments
- Update outdated references

### 3. **Add Examples**
- Create new example scripts demonstrating algorithms
- Add real-world applications
- Implement variants of existing algorithms
- Contribute visualizations

### 4. **Enhance Code**
- Optimize algorithm implementations
- Add type hints and docstrings
- Improve test coverage
- Fix bugs

### 5. **Extend Curriculum**
- Add new algorithms or techniques
- Create supplementary materials
- Develop interactive visualizations
- Add benchmarking results

---

## 🚀 Getting Started

### 1. Fork and Clone

```bash
# Fork the repository on GitHub, then:
git clone https://github.com/YOUR_USERNAME/reinforcement-learning.git
cd reinforcement-learning

# Add upstream remote
git remote add upstream https://github.com/powell-clark/reinforcement-learning.git
```

### 2. Set Up Development Environment

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in editable mode with dev dependencies
pip install -e ".[dev]"

# Or install requirements directly
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### 3. Create a Branch

```bash
# Fetch latest changes
git fetch upstream
git checkout main
git merge upstream/main

# Create feature branch
git checkout -b feature/your-feature-name
# Or for bug fixes:
git checkout -b fix/issue-description
```

---

## 📝 Contribution Guidelines

### Code Style

We follow **PEP 8** with these specifics:

```python
# Good example
def train_agent(
    env_name: str,
    n_episodes: int = 1000,
    learning_rate: float = 1e-3,
) -> tuple[Agent, list[float]]:
    """
    Train RL agent on specified environment.

    Args:
        env_name: Gymnasium environment name
        n_episodes: Number of training episodes
        learning_rate: Optimizer learning rate

    Returns:
        Trained agent and list of episode rewards
    """
    # Implementation here
    pass
```

**Key points:**
- Use type hints for all functions
- Write comprehensive docstrings (Google style)
- Keep functions focused (single responsibility)
- Use descriptive variable names
- Add comments for complex logic
- Maximum line length: 100 characters

### Testing

All new code should include tests:

```python
# tests/test_algorithms.py
import pytest
from algorithms.tabular import QLearning

def test_qlearning_initialization():
    """Test Q-Learning agent initializes correctly."""
    agent = QLearning(n_actions=4, alpha=0.1, gamma=0.99)
    assert agent.alpha == 0.1
    assert agent.gamma == 0.99

def test_qlearning_update():
    """Test Q-Learning update rule."""
    agent = QLearning(n_actions=4, alpha=0.1, gamma=0.99)
    # Test update logic
    ...
```

**Run tests before submitting:**
```bash
pytest tests/
```

### Commit Messages

Use clear, conventional commit messages:

```
feat: Add SAC implementation for continuous control
fix: Correct Q-value update in DQN
docs: Update README with RLHF examples
test: Add tests for PPO clipping
refactor: Optimize replay buffer sampling
```

**Format:**
- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation
- `test:` Tests
- `refactor:` Code refactoring
- `perf:` Performance improvement
- `chore:` Maintenance

---

## 🔬 Notebook Contributions

If contributing new notebooks:

### Structure
- Theory notebook (Xa): Mathematical foundations, derivations, intuitions
- Practical notebook (Xb): Implementation, experiments, visualizations

### Quality Standards
- 700-1100 lines of content
- Complete working code (no TODOs)
- Comprehensive explanations
- Mathematical rigor with intuitive explanations
- Visualizations and plots
- Exercises with solutions
- References to papers

### Testing Notebooks
```bash
# Test notebook execution
jupyter nbconvert --to notebook --execute notebooks/your_notebook.ipynb
```

---

## 📚 Example Contributions

Good examples should:
- Be self-contained (single file)
- Include clear documentation
- Have reasonable runtime (< 10 minutes)
- Produce visualizations
- Follow existing example patterns

See `examples/` directory for templates.

---

## 🔍 Pull Request Process

### 1. Ensure Quality
- [ ] Code follows style guidelines
- [ ] All tests pass
- [ ] New tests added for new code
- [ ] Documentation updated
- [ ] No merge conflicts

### 2. Submit PR
```bash
# Push your branch
git push origin feature/your-feature-name

# Create pull request on GitHub
```

**PR Description should include:**
- What changes were made
- Why the changes are needed
- Any breaking changes
- Screenshots (if UI changes)
- Related issues

### 3. Code Review
- Address reviewer feedback
- Make requested changes
- Keep discussion professional and constructive

### 4. Merge
Once approved:
- Squash commits if needed
- Merge to main
- Delete feature branch

---

## 🎓 Curriculum Standards

This curriculum maintains **elite university standards** (Stanford CS234, Berkeley CS285, MIT 6.7920).

When contributing, ensure:
- Mathematical rigor (with intuitive explanations)
- Production-quality code
- Comprehensive documentation
- Real-world applicability
- Cutting-edge content (2025-2026 standards)

### Key Topics to Maintain
1. Classical RL foundations (Q-Learning, SARSA, MC)
2. Deep RL (DQN, PPO, SAC)
3. **RLHF** (ChatGPT-style alignment) ⭐ **Critical for 2025**
4. Professional practices (deployment, tuning, debugging)
5. Real-world applications

---

## ❓ Questions?

- **General questions**: Open a GitHub Discussion
- **Bug reports**: Open an Issue
- **Feature requests**: Open an Issue with "enhancement" label
- **Security issues**: Email contact@powell-clark.com

---

## 🏆 Recognition

Contributors will be:
- Listed in CONTRIBUTORS.md
- Acknowledged in release notes
- Credited in relevant documentation

---

## 📜 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

## 🙏 Thank You!

Your contributions help make RL education accessible and high-quality for everyone.

**Current Status**: 40/40 notebooks complete (Legendary 2025-2026)
**Next Frontiers**: Your ideas and contributions!

---

*Last Updated: 2025-01-26*
*Maintained by: Powell-Clark Limited*
