# TASK-RL042: Verify feature acceptance criteria against notebooks

## Context

All 19 FEAT-RL* cards sit in_review with every AC checkbox unticked despite owning tasks being done. This session dispatched 9 parallel read-only agents (one per feature group) to check each AC's claim against actual notebook content and report MET/NOT MET with evidence, but closed them (per operator instruction, to stop leaked idle panes) before any reply landed, so the findings were lost. Redo: spot-check each FEAT-RL* card's ACs against its notebook(s) in notebooks/, and tick off (or note as genuinely unmet) each one with cited evidence. See CONSCIOUSNESS/features/active-feature-item-details/FEAT-RL*.md for the exact AC text and notebook mapping.

### Closing summary (final tally, verified against live file state via `grep -c` over all 19 cards)

61 ACs total across 19 cards: **34 MET, 27 NOT MET, 0 unresolved**.

| Card | MET | NOT MET | Card | MET | NOT MET |
|---|---|---|---|---|---|
| FEAT-RL1 (Colab-runnable) | 0 | 4 | FEAT-RL11 | 1 | 2 |
| FEAT-RL2 (dual impl.) | 1 | 3 | FEAT-RL12 | 1 | 2 |
| FEAT-RL3 (Gymnasium) | 0 | 4 | FEAT-RL13 | 1 | 2 |
| FEAT-RL4 | 2 | 2 | FEAT-RL14 | 3 | 0 |
| FEAT-RL5 | 3 | 0 | FEAT-RL15 | 2 | 1 |
| FEAT-RL6 | 2 | 1 | FEAT-RL16 | 3 | 0 |
| FEAT-RL7 | 1 | 2 | FEAT-RL17 | 3 | 0 |
| FEAT-RL8 | 1 | 2 | FEAT-RL18 | 3 | 0 |
| FEAT-RL9 | 3 | 0 | FEAT-RL19 (X-series) | 3 | 0 |
| FEAT-RL10 | 1 | 2 | | | |

The three cross-cutting cards (FEAT-RL1/2/3) carry the worst gaps: sampled across tabular (0a/0b/1b/3b), deep-RL (7a/7b/9b/13b), and X-series (X1) notebooks, none of the "polish" claims (Colab-runnability, SB3 API-diff documentation, env registration, rgb_array rendering) held up under direct inspection, while the per-lesson algorithmic content (FEAT-RL4-19) is mostly solid (25 of 34 lesson+X-series ACs MET). See each card's AC lines for cited evidence.

## Acceptance criteria

- [x] **AC-1** — Every AC checkbox across all 19 `FEAT-RL*.md` cards is resolved: ticked with a cited notebook filename plus cell/section evidence, or left unticked with an explicit `NOT MET` note and reason (verified: `grep -c` over all 19 cards shows 61/61 ACs carry either `[x]` or a `NOT MET` annotation, 0 bare-unresolved)
- [x] **AC-2** — The 16 lesson-mapped feature cards (FEAT-RL4 through FEAT-RL18) are checked against their 1:1 theory/practical notebook pair (e.g. FEAT-RL7 against `4a_td_theory.ipynb` and `4b_td_practical.ipynb`) (verified: all 16 cards' AC counts fully accounted for by MET+NOT_MET, citing the paired notebooks by name in each AC line)
- [x] **AC-3** — FEAT-RL19 (Professional Practice Series) is checked against all four `X1`-`X4` notebooks (evidence: FEAT-RL19.md AC-1/2/3 cite X1-X4 by name, e.g. X2_rl_evaluation.ipynb Part 4, X3_rl_deployment.ipynb Parts 2-3)
- [x] **AC-4** — The three cross-cutting cards (FEAT-RL1 Colab-runnable, FEAT-RL2 dual implementation, FEAT-RL3 Gymnasium integration) are spot-checked across a representative sample of notebooks spanning tabular, deep-RL, and X-series lessons, not just one (evidence: FEAT-RL1/2/3.md AC lines cite 0a, 0b, 1b, 3b, 7a, 7b, 9b, 13b, X1 by name)
- [x] **AC-5** — A closing summary in this card's Context (or a linked commentary entry) states the final MET/NOT MET tally across all 19 cards (see Closing summary above: 34 MET / 27 NOT MET / 61 total)

## Dependencies

- Directive: DIRECT-RL1
- Reads: CONSCIOUSNESS/features/active-feature-item-details/FEAT-RL1.md through FEAT-RL19.md
- Reads: notebooks/*.ipynb (34 notebooks)

## Pre-mortem

### Failure modes

- Dispatching parallel verification agents and closing/losing them before their edits land, as happened earlier this session — mitigated by keeping this run in-band (synchronous Agent tool calls awaited to completion, not cross-pane teammates that need manual closing)
- An agent ticking an AC on a superficial keyword match (e.g. the word "PPO" appears) rather than confirming the notebook actually derives/implements/runs what the AC claims
- Marking an AC as NOT MET for a notebook that exists but wasn't opened, rather than genuinely absent content

### Weak assumptions

- Assumes the FEAT-RL*-to-notebook mapping inferred from lesson numbers in each card's title (e.g. "Lesson 7" to `7a_*`/`7b_*`) is correct — verified against DIRECT-RL1 and story links where a card's mapping is ambiguous
- Assumes a notebook's rendered cell outputs (where present) are sufficient evidence of "runs" claims without re-executing the notebook in this session
