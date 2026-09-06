# FEAT-RL1: Colab-runnable notebooks with in-browser visualization

## Kano
must-have

## Context
Every notebook in the curriculum must open and run top-to-bottom on Google Colab's free tier, with visualizations rendering inline. This is the accessibility promise of the series.

## Acceptance Criteria
- [ ] **AC-1** — Each notebook runs top-to-bottom on Colab free tier with no local-only dependencies — PARTIAL (TASK-RL044 fixed 7a/7b/9b/13b/X1, commit 6fce882457be1430db49670c6a2be04494ee960e); original finding hedged "roughly half the 34-notebook curriculum" — remaining notebooks beyond these 5 not yet re-verified. Follow-up: TASK-RL057.
- [ ] **AC-2** — A pip-install cell provisions Gymnasium, PyTorch, and Stable-Baselines3 as needed — PARTIAL (TASK-RL044 fixed 7a/7b/9b/13b/X1 including 9b's silent-degrade SB3 import, commit 6fce882457be1430db49670c6a2be04494ee960e); full-curriculum coverage beyond these 5 not yet re-verified. Follow-up: TASK-RL057.
- [x] **AC-3** — Plots and environment renders display inline in the notebook — MET (TASK-RL044): 7b cell 13 executes an `rgb_array` render and displays the captured frame inline via matplotlib imshow, with retained image/png output. Evidence: commit 6fce882457be1430db49670c6a2be04494ee960e.
- [x] **AC-4** — Long-running training cells expose a reduced-timestep quick-run path — MET (TASK-RL044): 7b, 13b, and X1 each gained a `QUICK_RUN` toggle (default off, full-size run preserved) letting the long training cell complete in under a minute for smoke-testing. Evidence: commit 6fce882457be1430db49670c6a2be04494ee960e.

## Stories
STORY-RL1, STORY-RL2, STORY-RL3, STORY-RL4, STORY-RL5, STORY-RL6, STORY-RL7, STORY-RL8, STORY-RL9, STORY-RL10, STORY-RL11, STORY-RL12, STORY-RL13, STORY-RL14, STORY-RL15, STORY-RL16, STORY-RL17

## Links
- Directive: DIRECT-RL1 (Ship complete RL curriculum)
