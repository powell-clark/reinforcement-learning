# FEAT-RL8: N-Step and Eligibility Traces (Lesson 5)

## Kano
must-have

## Context
Unifying MC and TD along a continuous spectrum. N-step bootstrapping and TD(lambda) enable flexible balance between bias and variance.

## Acceptance Criteria
- [x] **AC-1** — N-step TD prediction and n-step Sarsa implemented (evidence: TASK-RL050 — `n_step_td_prediction`/`td_zero_prediction`, 5a_nstep_eligibility.ipynb cell 11, literal per-episode n-step TD update distinct from the eligibility-trace `SarsaLambda` class; run for n=1/n=4 with n=1 exactly matching TD(0); verified against hand-derived values in verify_nstep_td_logic.py)
- [x] **AC-2** — Forward and backward views of eligibility traces explained and shown equivalent (evidence: TASK-RL050 — `offline_lambda_return_update`/`offline_backward_view_update`, 5a_nstep_eligibility.ipynb cell 13, offline/V-frozen batch update on a fixed trajectory, agreement to 3.47e-18; verified against hand-derived values in verify_forward_backward_equivalence.py)
- [x] **AC-3** — TD(lambda) and Sarsa(lambda) implemented from scratch (evidence: 5a_nstep_eligibility.ipynb SarsaLambda class + 5b_nstep_eligibility_practical.ipynb sarsa_lambda() function, both coded with eligibility-trace updates)

## Stories
STORY-RL6

## Links
- Directive: DIRECT-RL1 (Ship complete RL curriculum)
- Cross-cutting: FEAT-RL1 (Colab), FEAT-RL2 (NumPy+SB3), FEAT-RL3 (Gymnasium)
