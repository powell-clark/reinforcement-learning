# STORY-RL20: README lockstep across the four ML repos

## User Story
I want the four ML repos to share one README shape and one status line so that the curriculum reads as one coherent syllabus rather than four independently-drifted repos.

## Context
Operator charge, verbatim: "the four ML repos share one README shape and status line (the kernel measured they do not today)." The sibling repos are supervised-machine-learning, unsupervised-machine-learning, reinforcement-learning (this repo), and a fourth in the series. No shared template exists today; each repo's README evolved independently.

## Acceptance Criteria
- [ ] A single README section shape (section order and headings) is defined and documented once, referenced by all four repos rather than copy-pasted independently
- [ ] A single status-line format is defined (the pattern this repo's README already uses at the top: "N of M notebooks built" style) and applied identically across all four repos
- [ ] This repo's own README is brought into conformance with the shared shape as the reference implementation
- [ ] The other three repos' non-conformance (or conformance) is recorded with evidence — this repo cannot rewrite sibling repos unilaterally, so the acceptance criterion here is verified drift plus a filed cross-repo task, not a direct edit to repos this session cannot reach

## Dependencies
- Blocked by: none
- Blocks: none

## Links
- Directive: DIRECT-RL2 (Maintain the curriculum as a living Feynman-style corpus)
- Features: none yet
