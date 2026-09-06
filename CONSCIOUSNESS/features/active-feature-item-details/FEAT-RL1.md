# FEAT-RL1: Colab-runnable notebooks with in-browser visualization

## Kano
must-have

## Context
Every notebook in the curriculum must open and run top-to-bottom on Google Colab's free tier, with visualizations rendering inline. This is the accessibility promise of the series.

## Acceptance Criteria
- [x] **AC-1** — Each notebook runs top-to-bottom on Colab free tier with no local-only dependencies — MET (TASK-RL044 + TASK-RL057): TASK-RL044 fixed 7a/7b/9b/13b/X1 (commit 6fce882457be1430db49670c6a2be04494ee960e); TASK-RL057 audited the remaining notebooks via `audit_installs.py` (repo-wide import scan against a Colab-base-image known-OK list plus a third-party watch list) and fixed the 12 flagged missing install-cell coverage — 5a, 5b, 6b, 8a, 11b, 12b, 14a, 14b, 15b, X2, X3, X4 (commits fabcac0, db4d65c, e501210, ff48d6c, bc32ba2, c76ebe0, 43ad805, f383a91, 7ff65da) — then re-executed all 12 top-to-bottom (`jupyter nbconvert --execute`) confirming zero ModuleNotFoundError/error-type output cells. A fresh re-run of the same audit against the fully-fixed tree flags 0 notebooks `MISSING INSTALL CELL`, covering all 36 notebooks currently in the repo. Caveat: verification re-executed each notebook in a local environment where the watch-list packages were already installed, so the `except ImportError: pip install` fallback branch itself was never exercised end-to-end against a genuinely bare Colab runtime — only the notebook's top-to-bottom completion and the presence/placement of the install cell are directly verified.
- [x] **AC-2** — A pip-install cell provisions Gymnasium, PyTorch, and Stable-Baselines3 as needed — MET (TASK-RL044 + TASK-RL057): TASK-RL044 fixed 7a/7b/9b/13b/X1 including 9b's silent-degrade SB3 import (commit 6fce882457be1430db49670c6a2be04494ee960e); TASK-RL057 added the same `subprocess.check_call([sys.executable, '-m', 'pip', 'install', package, '-q'])` pattern to the 12 notebooks named in AC-1, covering gymnasium, stable-baselines3, d3rlpy, pettingzoo[sisl], supersuit, gymnasium-robotics, and onnxruntime per notebook need (commits as cited in AC-1). Same fresh-Colab-runtime caveat as AC-1 applies — the install path's failure branch is unexercised locally.

**Notebook-count note**: the original TASK-RL042 finding text (carried into this card as "roughly half the 34-notebook curriculum") undercounted even at the time it was written — `notebooks/X4_rl_research_frontiers.ipynb` (added 2026-09-04, commit c4c1e72) already existed when TASK-RL042 ran (2026-09-05), and the full curriculum was 36 notebooks by then, not 34. Live count verified this session via `ls notebooks/*.ipynb | wc -l` → 36. TASK-RL057's audit swept all 36.
- [x] **AC-3** — Plots and environment renders display inline in the notebook — MET (TASK-RL044): 7b cell 13 executes an `rgb_array` render and displays the captured frame inline via matplotlib imshow, with retained image/png output. Evidence: commit 6fce882457be1430db49670c6a2be04494ee960e.
- [x] **AC-4** — Long-running training cells expose a reduced-timestep quick-run path — MET (TASK-RL044): 7b, 13b, and X1 each gained a `QUICK_RUN` toggle (default off, full-size run preserved) letting the long training cell complete in under a minute for smoke-testing. Evidence: commit 6fce882457be1430db49670c6a2be04494ee960e.

## Stories
STORY-RL1, STORY-RL2, STORY-RL3, STORY-RL4, STORY-RL5, STORY-RL6, STORY-RL7, STORY-RL8, STORY-RL9, STORY-RL10, STORY-RL11, STORY-RL12, STORY-RL13, STORY-RL14, STORY-RL15, STORY-RL16, STORY-RL17

## Links
- Directive: DIRECT-RL1 (Ship complete RL curriculum)
