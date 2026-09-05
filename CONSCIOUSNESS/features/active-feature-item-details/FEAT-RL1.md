# FEAT-RL1: Colab-runnable notebooks with in-browser visualization

## Kano
must-have

## Context
Every notebook in the curriculum must open and run top-to-bottom on Google Colab's free tier, with visualizations rendering inline. This is the accessibility promise of the series.

## Acceptance Criteria
- [ ] **AC-1** — Each notebook runs top-to-bottom on Colab free tier with no local-only dependencies — NOT MET: 7a, 7b, 9b, 13b, X1 (and roughly half the 34-notebook curriculum per repo-wide grep) import gymnasium/stable-baselines3/wandb/mujoco-backed envs with no install cell, so a fresh Colab runtime hits ModuleNotFoundError top-to-bottom.
- [ ] **AC-2** — A pip-install cell provisions Gymnasium, PyTorch, and Stable-Baselines3 as needed — NOT MET: present in 0a/0b/1b/3b but absent in 7a/7b/9b/13b/X1; 9b's SB3 import only prints "Install: pip install stable-baselines3" on failure rather than installing it.
- [ ] **AC-3** — Plots and environment renders display inline in the notebook — NOT MET: matplotlib plots consistently show via plt.show() across the sample, but no notebook actually captures and displays an environment image — 0b sets render_mode='rgb_array' on CartPole but never shows a frame, and other envs render only ASCII text or nothing.
- [ ] **AC-4** — Long-running training cells expose a reduced-timestep quick-run path — NOT MET: no quick-run toggle found anywhere in the sample; 7b (300 episodes + 50k SB3 timesteps), 13b (20k timesteps × 6 seeds × 2 variants), and X1 (9 fixed 8k-timestep runs) all hardcode full-size training with no reduced-timestep parameter.

## Stories
STORY-RL1, STORY-RL2, STORY-RL3, STORY-RL4, STORY-RL5, STORY-RL6, STORY-RL7, STORY-RL8, STORY-RL9, STORY-RL10, STORY-RL11, STORY-RL12, STORY-RL13, STORY-RL14, STORY-RL15, STORY-RL16, STORY-RL17

## Links
- Directive: DIRECT-RL1 (Ship complete RL curriculum)
