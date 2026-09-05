# FEAT-RL3: Gymnasium environment integration across all lessons

## Kano
must-have

## Context
All practical work uses the Gymnasium (formerly OpenAI Gym) environment API plus a custom GridWorld for teaching, giving learners a single consistent interface across the curriculum.

## Acceptance Criteria
- [ ] **AC-1** — Notebooks use the Gymnasium reset()/step()/render() API consistently — NOT MET: the modern 5-tuple reset()/step() API is consistent from 0b onward, but 0a's custom GridWorld uses the old 4-tuple gym API (reset() returns bare state; step() returns (state, reward, done, info)); render() itself is essentially unused across the sample.
- [ ] **AC-2** — A custom GridWorld environment is provided for tabular lessons — NOT MET: the tabular lessons sampled (1b uses FrozenLake, 3b uses Blackjack) use built-in Gymnasium environments, not the custom GridWorld, which appears only as a plain non-gym.Env class in the theory notebook 0a.
- [ ] **AC-3** — Environments are registered and reproducible with seeds — NOT MET: seeding is pervasive and solid (env.reset(seed=...), algorithm seed= params), but a repo-wide grep across all 34 notebooks found zero gym.register()/registry calls for any custom environment (TreasureHuntEnv, SparseMaze, GridWorld) — none are ever registered.
- [ ] **AC-4** — Rendering works within Colab (rgb_array / inline display) — NOT MET: no notebook in the sample captures and displays an rgb_array frame; 0b sets render_mode='rgb_array' on CartPole but never uses it, and custom envs render only ASCII text (0a, 0b) or have no render() at all (13b's SparseMaze).

## Stories
STORY-RL1, STORY-RL2, STORY-RL3, STORY-RL4, STORY-RL5, STORY-RL6, STORY-RL7, STORY-RL8, STORY-RL9, STORY-RL10, STORY-RL11, STORY-RL12, STORY-RL13, STORY-RL14, STORY-RL15, STORY-RL16, STORY-RL17

## Links
- Directive: DIRECT-RL1 (Ship complete RL curriculum)
