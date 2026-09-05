# FEAT-RL8: N-Step and Eligibility Traces (Lesson 5)

## Kano
must-have

## Context
Unifying MC and TD along a continuous spectrum. N-step bootstrapping and TD(lambda) enable flexible balance between bias and variance.

## Acceptance Criteria
- [ ] **AC-1** — N-step TD prediction and n-step Sarsa implemented — NOT MET: n-step returns/TD/Sarsa appear only as formulas in 5a_nstep_eligibility.ipynb; both notebooks jump straight to eligibility-trace (λ) code with no literal n-step update ever implemented.
- [ ] **AC-2** — Forward and backward views of eligibility traces explained and shown equivalent — NOT MET: both views are stated with formulas but equivalence is only asserted ("The Key Theorem") with no derivation or empirical comparison; only the backward view is ever implemented.
- [x] **AC-3** — TD(lambda) and Sarsa(lambda) implemented from scratch (evidence: 5a_nstep_eligibility.ipynb SarsaLambda class + 5b_nstep_eligibility_practical.ipynb sarsa_lambda() function, both coded with eligibility-trace updates)

## Stories
STORY-RL6

## Links
- Directive: DIRECT-RL1 (Ship complete RL curriculum)
- Cross-cutting: FEAT-RL1 (Colab), FEAT-RL2 (NumPy+SB3), FEAT-RL3 (Gymnasium)
