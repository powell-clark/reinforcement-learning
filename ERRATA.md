# Errata and open findings

These are findings from an independent academic review on 2026-10-22, and the author works through them as he studies the lessons.

Cell numbers are zero-based and retained from the review; grouped findings appear under every affected notebook, while repository documents retain their original line numbers.

Distinct review findings: P1 — 75 open, 4 fixed; P2 — 27 open, 0 fixed; P3 — 4 open, 0 fixed.

## [0a_rl_introduction_theory.ipynb](notebooks/0a_rl_introduction_theory.ipynb)

- [fixed] P1 — cell 7 — Greedifying an arbitrary policy's Q-function is incorrectly said to yield an optimal policy. — Use π*(s) ∈ argmax_a Q*(s,a) and distinguish policy improvement using Q^π from optimality.
- [fixed] P1 — cell 7 — Reward signs are incorrectly equated with good, bad or neutral actions. — Define rewards as task feedback and use negative step costs to show that action quality depends on expected return.
- [fixed] P1 — cell 9 — Exploitation, softmax probabilities and posterior-sampling guarantees are defined incorrectly. — Use estimated return, probabilities proportional to exp(Q/τ), and model-specific regret guarantees with realistic sampling costs.
- [fixed] P1 — cell 7 — Observations are treated as automatically sufficient Markov states. — Distinguish observations from states and include velocity information or chess rights, turn and draw history where needed.
- [open] P1 — cell 18 — External time-limit truncation is treated as terminal for bootstrapping and the introductory task hides a reward-changing horizon. — Separate episode boundaries from bootstrap masks, bootstrap through external truncation, and include remaining time for a task-defined horizon.

## [0b_gymnasium_setup_practical.ipynb](notebooks/0b_gymnasium_setup_practical.ipynb)

- [open] P1 — cell 16 — External time-limit truncation is treated as terminal for bootstrapping and the introductory task hides a reward-changing horizon. — Separate episode boundaries from bootstrap masks, bootstrap through external truncation, and include remaining time for a task-defined horizon.
- [open] P2 — cell 18 — The debugging checker prints success without evaluating most conditions. — Make each verdict depend on an actual check or explain and use the environment checker.
- [open] P2 — cell 12, 19–21 — Environment API conformance is incorrectly said to imply compatibility with any RL algorithm. — Distinguish API conformance from supported observation and action spaces and algorithm assumptions.
- [open] P2 — cell 7, 10 — Random-number generators and library models are not seeded consistently with the reproducibility advice. — Seed every relevant generator and distinguish independent training seeds from evaluation seeds.

## [1a_mdp_theory.ipynb](notebooks/1a_mdp_theory.ipynb)

- [fixed] P1 — cell 4 — Observations are treated as automatically sufficient Markov states. — Distinguish observations from states and include velocity information or chess rights, turn and draw history where needed.
- [open] P1 — cell 4 — The Markov property is incorrectly presented as necessary and sufficient for computational tractability. — Explain its role in state-based value equations and acknowledge histories, recurrent policies and belief states without blanket scalability claims.
- [open] P1 — cell 13 — The worked action backups omit discounting and are both labelled as state values. — Label them Q_V(S,Study) and Q_V(S,Relax), include γ = 0.9, and correct the Study result to −0.145.
- [open] P2 — cell 0–1 — Promised foundational sections, discount justification and the Recycling Robot example are absent. — Supply the material or revise the objectives and contents, explaining bounded rewards and γ < 1 before infinite-return convergence.

## [1b_mdp_practical.ipynb](notebooks/1b_mdp_practical.ipynb)

- [open] P1 — cell 11 — Policy improvement compares against an empty dictionary rather than the previous policy and can falsely announce convergence. — Pass the previous policy, compare its actions, return a convergence flag, and evaluate the returned policy.
- [open] P1 — cell 4 — Slippery FrozenLake is incorrectly described as a one-third chance of random movement. — Describe equal probabilities for intended and perpendicular directions, including boundary collisions.
- [open] P1 — cell 35 — Zero discount is incorrectly said to make any policy reach the goal. — Explain immediate-reward ties and the differing long-term outcomes of tied actions.
- [open] P1 — cell 20 — The neural DQN baseline is misidentified as tabular Q-learning and dynamic programming. — Describe it as model-free learning from sampled transitions and contrast its information with model-based planning.
- [open] P2 — cell 21, 25 — Evaluation measures capped undiscounted success rather than the stationary discounted objective solved by planning. — State the difference, report discounted returns, and match horizons before claiming an empirical optimum.

## [2a_dp_theory.ipynb](notebooks/2a_dp_theory.ipynb)

- [open] P1 — cell 8, 13–14, 19–20 — Dense-MDP storage and backup complexity omit a factor of the number of states. — Use O(nmd) for successor count d, set d = n for dense models, and include evaluation iterations and discount dependence.
- [open] P1 — cell 8 — The policy-iteration linear worst-case bound and bounded-monotone finite-convergence argument are unsupported. — Use the finite deterministic-policy argument with consistent tie handling and remove the claimed O(n) bound.
- [open] P1 — cell 10 — The contraction example understates the iteration count by about twentyfold. — Use k ≥ 6 log(10)/−log(0.9), round up to 132, and distinguish relative error reduction from absolute decimal accuracy.
- [open] P1 — cell 10, 12, 15 — Discounted, undiscounted, asynchronous and approximate convergence conditions are conflated. — State each method's assumptions separately, require γ < 1 for contraction, and remove unnecessary ergodicity and finite-horizon claims.
- [open] P1 — cell 7 — The improvement diagram requires every action to exceed the old state value. — Require Q^π(s,π′(s)) ≥ V^π(s) for the selected new action at every state.
- [open] P1 — cell 16 — The vectorized backup appends an incorrect axis to the transition tensor. — Specify array shapes and compute Q = (P * (R + gamma * V[None, None, :])).sum(axis=2).
- [open] P2 — cell 14 — A synthetic runtime plot is used to support an empirical algorithm crossover threshold. — Label the plot schematic and remove empirical cutoffs or benchmark verified algorithms with specified models and tolerances.

## [2b_dp_practical.ipynb](notebooks/2b_dp_practical.ipynb)

- [open] P1 — cell 9 — Asynchronous value iteration can stop after a single unchanged state and miscomputes global change. — Check a fresh global optimality residual or the maximum change over a complete sweep with every state covered.
- [open] P1 — cell 11 — Prioritized sweeping retains historical maximum residuals and can omit needed updates. — Maintain current residuals, invalidate stale queue entries, and verify termination against a fresh global residual.
- [open] P1 — cell 17 — Approximate policy evaluation stops at policy stability before values have converged. — Require a suitable value or optimality residual and distinguish modified from exact policy iteration.
- [open] P1 — cell 5 — The planner ignores the advertised stochastic slipping dynamics. — Use the same stochastic transition distribution for planning and environment interaction or remove stochastic mode.
- [open] P2 — cell 6, 10, 19 — Runtime percentages and tabular size cutoffs lack an empirical basis. — Tie advice to measured memory, successor counts and backup costs and remove universal crossover numbers.

## [3a_mc_theory.ipynb](notebooks/3a_mc_theory.ipynb)

- [open] P1 — cell 6–7 — Every-visit Monte Carlo is incorrectly described as finite-sample unbiased and uniformly faster. — State consistency assumptions separately from finite-sample bias and avoid universal variance or speed rankings.
- [open] P1 — cell 11 — The ε-greedy performance bound can require values above optimal and fixed ε is said to guarantee coverage. — Remove the false theorem, explain ε-soft optimization, and state explicit GLIE conditions for unrestricted optimality.
- [open] P1 — cell 13 — Self-normalized importance sampling is labelled unbiased and confused with ordinary sampling. — Contrast the two estimators, identify finite-sample bias, and state support and zero-denominator conditions.
- [open] P1 — cell 14 — Blackjack's showing-card range, bust reward and model availability are misstated. — Use showing cards 1–10 and bust reward −1 and distinguish unknown dynamics from a known model deliberately not used.

## [3b_mc_practical.ipynb](notebooks/3b_mc_practical.ipynb)

- [open] P1 — cell 11 — Exploring starts invents Blackjack observations without initializing or resetting the environment. — Implement valid environment initialization or teach ε-soft control without fabricated starts.
- [open] P1 — cell 11, 13 — Monte Carlo control repeatedly adds the final reward instead of accumulating the trajectory's rewards. — Store each transition's reward and reverse-accumulate those actual rewards.
- [open] P1 — cell 17 — The random Blackjack baseline has integer keys while observations are tuples, making it always stick. — Use the existing random-policy callable and reassess comparative claims.
- [open] P1 — cell 5 — Blackjack's showing-card range, bust reward and model availability are misstated. — Use showing cards 1–10 and bust reward −1 and distinguish unknown dynamics from a known model deliberately not used.

## [4a_td_theory.ipynb](notebooks/4a_td_theory.ipynb)

- [open] P1 — cell 6–7 — The DP/MC/TD explanation confuses expected and sampled backups and invents a universal bias–variance sweet spot. — Separate sampling from bootstrapping, qualify conditional target bias, and remove the unsupported curves.
- [open] P1 — cell 8, 11, 13 — TD convergence and rate guarantees are generalized beyond their assumptions. — State separate tabular prediction, Sarsa and Q-learning conditions and remove universal rates and arbitrary-behavior claims.
- [open] P1 — cell 8, 10 — Sarsa is assigned intrinsic safety and systematic underestimation while the optimal cliff route is misdescribed. — Explain exploratory-policy returns and route choice without safety guarantees or a route through the cliff.

## [4b_td_practical.ipynb](notebooks/4b_td_practical.ipynb)

- [open] P1 — cell 0, 13 — Sarsa is assigned intrinsic safety and systematic underestimation while the optimal cliff route is misdescribed. — Explain exploratory-policy returns and route choice without safety guarantees or a route through the cliff.
- [open] P2 — cell 12 — The sensitivity plot measures state zero rather than the actual CliffWalking start. — Use the reset state or documented start index and label the measured value accordingly.

## [5a_nstep_eligibility.ipynb](notebooks/5a_nstep_eligibility.ipynb)

- [open] P1 — cell 4 — Overlapping n-step TD is incorrectly said to update only every n steps. — Distinguish the initial n-step delay from the subsequent one-update-per-timestep frequency.
- [open] P1 — cell 5–6, 20 — Trace recursions are mislabelled and ordinary online TD(λ) is equated exactly with offline λ-returns. — Label the backward view correctly, retain offline equivalence qualifications, distinguish true-online methods, and note γ decay at λ = 1.

## [5b_nstep_eligibility_practical.ipynb](notebooks/5b_nstep_eligibility_practical.ipynb)

- [open] P1 — cell 0, 4, 6, 8 — The supplied true values assume different boundary rewards and discounting from the implemented random walk. — Solve the implemented discounted value equations and recalculate every reported mean-squared error.
- [open] P1 — cell 6 — A state-value prediction function under random actions is called Sarsa(λ). — Rename it TD(λ) prediction or implement action values, selected next actions and state–action traces.
- [open] P1 — cell 10 — MountainCar's greedy action sums all weights and ignores the current state. — Select current and next actions using each action's weights dotted with the corresponding state features.
- [open] P1 — cell 10 — The MountainCar tile coder aliases tilings and scales position and velocity incorrectly. — Normalize coordinates, use offsets in tile widths, and allocate disjoint indices to each tiling.
- [open] P1 — cell 11–13 — Ordinary DQN is conflated with quantile-regression DQN, Double Q-learning and eligibility traces. — Identify the actual baseline and distinguish replay and target networks from quantiles, double estimation and λ-returns.
- [open] P1 — cell 13 — Replacing traces are incorrectly described as permitting only one visit per state per episode. — Explain that revisits reset a trace to one while subsequent visits and updates remain possible.
- [open] P1 — cell 10 — Several interaction loops discard truncation and may step beyond episode boundaries. — Read both termination and truncation flags, stop on either, and preserve their distinct bootstrap treatment.
- [open] P2 — cell 6 — Random-number generators and library models are not seeded consistently with the reproducibility advice. — Seed every relevant generator and distinguish independent training seeds from evaluation seeds.

## [6a_function_approximation.ipynb](notebooks/6a_function_approximation.ipynb)

- [open] P1 — cell 5 — The intermediate semi-gradient derivation has the wrong update sign. — Differentiate the detached-target squared loss and retain the minus sign from differentiating −V to obtain a positive αδ∇V update.
- [open] P1 — cell 0 — The chess game-tree estimate is incorrectly described as a count of states. — Name the quantity as game-tree complexity or provide a sourced state-space estimate.
- [open] P1 — cell 11 — Replay and target networks are presented as removing a deadly-triad ingredient. — Explain empirical stabilization while retaining function approximation, bootstrapping and off-policy learning without a general convergence guarantee.

## [6b_function_approximation_practical.ipynb](notebooks/6b_function_approximation_practical.ipynb)

- [open] P1 — cell 8, 10, 12–13 — The neural Q-learning example substitutes perturbed state coordinates for action values and never trains hidden layers. — Implement action-conditioned or per-action outputs with actual semi-gradient Q-learning and withdraw the claimed divergence demonstration.
- [open] P1 — cell 6, 8, 12 — Several interaction loops discard truncation and may step beyond episode boundaries. — Read both termination and truncation flags, stop on either, and preserve their distinct bootstrap treatment.
- [open] P2 — cell 4 — Tile coding silently wraps nonperiodic CartPole coordinates. — Use offset grids with explicit boundary handling or justify genuinely periodic coordinates.

## [7a_deep_q_networks.ipynb](notebooks/7a_deep_q_networks.ipynb)

- [open] P1 — cell 4–6, 8 — DQN and Double-DQN targets omit terminal-transition handling. — Store termination status and suppress the next-state value only at terminal transitions.
- [open] P1 — cell 0, 9 — Replay and target networks are presented as removing a deadly-triad ingredient. — Explain empirical stabilization while retaining function approximation, bootstrapping and off-policy learning without a general convergence guarantee.
- [open] P2 — cell 8, 10 — Historical, ranking and deployment claims lack usable citations and scope. — Add original-paper and primary deployment references at the claims and specify the task, date and metric for rankings.

## [7b_dqn_practical.ipynb](notebooks/7b_dqn_practical.ipynb)

- [open] P1 — cell 7, 9 — External time-limit truncation is treated as terminal for bootstrapping and the introductory task hides a reward-changing horizon. — Separate episode boundaries from bootstrap masks, bootstrap through external truncation, and include remaining time for a task-defined horizon.
- [open] P2 — cell 15 — Unmatched training and evaluation protocols are presented as implementation validation. — Evaluate frozen policies with matched protocols, call unmatched comparisons demonstrations, and validate implementations independently.
- [open] P2 — cell 7, 16 — Exploration decay is described per episode but applied per optimizer update. — Move decay to episode boundaries or document the actual update-based schedule and its speed.

## [8a_policy_gradients_theory.ipynb](notebooks/8a_policy_gradients_theory.ipynb)

- [open] P1 — cell 3 — The policy-gradient derivation defines Q using whole-trajectory return instead of reward-to-go. — Show cancellation of past rewards and define reward-to-go with the discounted occupancy and objective conventions.
- [open] P1 — cell 4–5 — REINFORCE omits the discounted objective's outer γ^t factor and changes parameters during a rollout's gradient calculation. — Compute and sum discounted score terms using frozen rollout parameters before applying the update.
- [open] P1 — cell 6 — A sampled TD error is equated exactly with the advantage function. — Use a conditional expectation for exact values and an approximation for learned-critic samples.
- [open] P2 — cell 7 — The actor–critic class claims continuous control but implements only discrete softmax actions. — Restrict its description to discrete actions or implement a continuous distribution with its log-density gradient.

## [8b_policy_gradients_practical.ipynb](notebooks/8b_policy_gradients_practical.ipynb)

- [open] P1 — cell 8 — External time-limit truncation is treated as terminal for bootstrapping and the introductory task hides a reward-changing horizon. — Separate episode boundaries from bootstrap masks, bootstrap through external truncation, and include remaining time for a task-defined horizon.
- [open] P1 — cell 5 — The written actor loss penalizes entropy even though the implementation rewards it. — Subtract αH from the minimized actor loss.
- [open] P1 — cell 8 — A2C discards every final partial rollout batch and may never learn from short episodes. — Flush partial batches at episode boundaries or retain a correctly masked buffer across episodes.
- [open] P2 — cell 8–10 — Unmatched training and evaluation protocols are presented as implementation validation. — Evaluate frozen policies with matched protocols, call unmatched comparisons demonstrations, and validate implementations independently.

## [9a_trpo_ppo_theory.ipynb](notebooks/9a_trpo_ppo_theory.ipynb)

- [open] P1 — cell 4, 11 — Practical TRPO is given an unconditional monotonic-improvement guarantee. — Separate the theoretical bound and its assumptions from finite-sample, average-KL and line-search approximations.
- [open] P1 — cell 5–6, 9, 11 — PPO clipping and KL penalties are repeatedly described as hard policy-change constraints. — Explain the objective's one-sided plateaus and the possibility of ratios or KL divergence exceeding nominal bounds.
- [open] P2 — cell 3 — The old-state-distribution surrogate is labelled as the true policy-return objective. — Name it as a surrogate, define its sampling distribution, and explain local agreement with the true objective.

## [9b_ppo_practical.ipynb](notebooks/9b_ppo_practical.ipynb)

- [open] P1 — cell 8, 10 — External time-limit truncation is treated as terminal for bootstrapping and the introductory task hides a reward-changing horizon. — Separate episode boundaries from bootstrap masks, bootstrap through external truncation, and include remaining time for a task-defined horizon.
- [open] P1 — cell 8 — GAE uses the current value at a nonterminal boundary and lacks episode-boundary masks. — Supply next-state values and distinct termination, truncation and trace-continuation masks.
- [open] P1 — cell 10 — PPO counts discarded episodes toward its rollout batch threshold. — Accumulate actual buffered transitions across episodes with boundary masks and final bootstrap values.
- [open] P2 — cell 10–12 — Unmatched training and evaluation protocols are presented as implementation validation. — Evaluate frozen policies with matched protocols, call unmatched comparisons demonstrations, and validate implementations independently.
- [open] P2 — cell 7–8 — GAE is introduced without its defining recurrence or boundary explanation. — Derive the discounted TD-error sum, explain finite-rollout values and masks, and distinguish advantages from value targets.

## [10a_continuous_control_theory.ipynb](notebooks/10a_continuous_control_theory.ipynb)

- [open] P1 — cell 8 — The SAC critic loss differentiates through its bootstrap target. — Use target critics with detached targets and show target-network updates.
- [open] P2 — cell 3–7 — Historical, ranking and deployment claims lack usable citations and scope. — Add original-paper and primary deployment references at the claims and specify the task, date and metric for rankings.
- [open] P2 — cell 3 — The deterministic policy-gradient expression omits evaluation points and occupancy assumptions and misdescribes the action derivative. — State the chain rule at the actor's action with distribution and differentiability assumptions and distinguish practical off-policy updates.

## [10b_continuous_control_practical.ipynb](notebooks/10b_continuous_control_practical.ipynb)

- [open] P1 — cell 10, 12 — External time-limit truncation is treated as terminal for bootstrapping and the introductory task hides a reward-changing horizon. — Separate episode boundaries from bootstrap masks, bootstrap through external truncation, and include remaining time for a task-defined horizon.
- [open] P1 — cell 6 — TD3 target networks start from unrelated random weights. — Copy each online network's initial state into its corresponding target network.
- [open] P1 — cell 6, 8, 10, 12 — Actor optimization, target actions and executed actions use inconsistent bounds and restrict Pendulum differently from the library baseline. — Use bounded actors scaled to the environment's action space consistently throughout training and execution.
- [open] P2 — cell 10–14 — Unmatched training and evaluation protocols are presented as implementation validation. — Evaluate frozen policies with matched protocols, call unmatched comparisons demonstrations, and validate implementations independently.

## [11a_model_based_rl_theory.ipynb](notebooks/11a_model_based_rl_theory.ipynb)

- [open] P1 — cell 5 — PlaNet is incorrectly described as using only deterministic latent dynamics. — Describe its recurrent state-space model's deterministic and stochastic components.
- [open] P2 — cell 7 — The Dyna sketch performs value prediction without defining control or the evaluated policy. — Label it prediction-only with a target policy or implement action-value control as in the practical lesson.
- [open] P2 — cell 8 — Linear model-error accumulation is stated without assumptions. — Specify the error measure and stability assumptions or present linear growth only as a limited heuristic.

## [11b_model_based_practical.ipynb](notebooks/11b_model_based_practical.ipynb)

- [open] P1 — cell 11 — MCTS discards path rewards and backs the same leaf suffix value into every ancestor. — Store traversed transitions and back up ancestor-specific discounted returns along the path.
- [open] P1 — cell 13 — PUCT reuses root action priors at every depth and inherits the incorrect return backup. — Evaluate priors at each parent state, store them on that parent's edges, and correct path-return backup.
- [open] P2 — cell 4 — Random-number generators and library models are not seeded consistently with the reproducibility advice. — Seed every relevant generator and distinguish independent training seeds from evaluation seeds.

## [12a_marl_theory.ipynb](notebooks/12a_marl_theory.ipynb)

- [open] P1 — cell 8, 10 — A centralized critic is said to eliminate learning non-stationarity and credit-assignment problems. — Distinguish stationary conditioned dynamics from changing policy values and explain which difficulties centralization mitigates.

## [12b_marl_practical.ipynb](notebooks/12b_marl_practical.ipynb)

- [open] P1 — cell 10 — Separate actor parameters and no weight sharing are falsely required for CTDE. — Explain that CTDE concerns information available during training and execution and permits shared actor parameters.
- [open] P2 — cell 14–15 — Unmatched training and evaluation protocols are presented as implementation validation. — Evaluate frozen policies with matched protocols, call unmatched comparisons demonstrations, and validate implementations independently.
- [open] P2 — cell 10–11 — CTDE prose describes episodic Monte Carlo updates while the code performs per-step TD updates. — Explain the implemented TD target and centralized baseline and remove the obsolete whole-episode description.
- [open] P3 — cell 10 — Stray generated cell markup appears in teaching prose. — Remove the markup.

## [13a_exploration_theory.ipynb](notebooks/13a_exploration_theory.ipynb)

- [open] P1 — cell 6 — Zero rewards are incorrectly said to provide no information for bandit uncertainty updates. — Show pull-count, empirical-mean and posterior failure-count updates and locate the difficulty in long-horizon stateful exploration.
- [open] P1 — cell 7, 9 — RND is said to guarantee high error on novel states and immunity to noisy observations. — Present prediction error as a learned novelty proxy with generalization, capacity, optimization and noise limitations.

## [13b_exploration_practical.ipynb](notebooks/13b_exploration_practical.ipynb)

- [open] P2 — cell 5, 11–12 — Repeating an identical deterministic evaluation is treated as 100 independent trials. — Report deterministic reachability per trained seed or introduce genuine variation before estimating a success distribution.
- [open] P3 — cell 13 — The summary calls the implemented 14×14 maze a 12×12 maze. — Change the summary to 14×14.

## [14a_offline_rl_theory.ipynb](notebooks/14a_offline_rl_theory.ipynb)

- [open] P1 — cell 3 — Offline policy evaluation is incorrectly ruled out. — Describe logged-data value estimators and their coverage and uncertainty assumptions while distinguishing online validation.
- [open] P1 — cell 6, 9–10 — GAIL is described as avoiding policy optimization and working without further environment access. — Retain its RL rollout requirement, explain what reward-recovery structure it avoids, and remove it from demonstration-only recommendations.
- [open] P2 — cell 5 — Random-number generators and library models are not seeded consistently with the reproducibility advice. — Seed every relevant generator and distinguish independent training seeds from evaluation seeds.
- [open] P2 — cell 5 — Behavioral-cloning underperformance is asserted to prove distribution shift and expert perfection is unchecked. — Measure held-out and on-policy imitation error, check expert quality, and make causal conclusions conditional on evidence.
- [open] P2 — cell 8 — Lower mean Q-values are treated as evidence of improved accuracy or control. — Compare with exact grid values, distinguish supported and unsupported actions, and evaluate policies across seeds.

## [14b_offline_rl_practical.ipynb](notebooks/14b_offline_rl_practical.ipynb)

- [open] P1 — cell 6, 11 — Behavioral cloning is incorrectly assigned a ceiling at demonstration performance. — Explain that imitation loss gives no general improvement guarantee while denoising or generalization can exceed average demonstration performance.
- [open] P1 — cell 4 — Offline collection loses timeout boundaries and misreports terminal counts as episode counts. — Preserve termination and timeout or episode-end information in the supported dataset representation and count actual episodes.
- [open] P1 — cell 10 — Offline optimizer steps and online environment steps are added into one interaction budget. — Report dataset size, gradient updates, online interactions and compute separately and define the fairness criterion.
- [open] P2 — cell 9, 11 — One fine-tuning regression is promoted into a universal mixed-replay requirement. — Report the seed and setup and describe mixed replay as one possible technique without a universal guarantee.

## [15a_hierarchical_rl_theory.ipynb](notebooks/15a_hierarchical_rl_theory.ipynb)

- [open] P1 — cell 5–6 — An immediately terminating option allows zero-duration nonprogress while recorded lengths are called steps to goal. — Restrict initiation sets, exclude immediately terminated options or require positive duration, and report goal success separately.
- [open] P2 — cell 6, 10 — Fixed training budgets and capped failures are presented as convergence measurements. — Report budgets, separate success from truncation, evaluate frozen policies, and define any convergence criterion.

## [15b_hierarchical_rl_practical.ipynb](notebooks/15b_hierarchical_rl_practical.ipynb)

- [open] P1 — cell 3–5 — A scripted sequence of supplied controllers is misrepresented as learned skill chaining. — Label it scripted option composition and explain the missing skill discovery, learning and initiation-region construction.
- [open] P2 — cell 7 — Random-number generators and library models are not seeded consistently with the reproducibility advice. — Seed every relevant generator and distinguish independent training seeds from evaluation seeds.
- [open] P2 — cell 0, 5 — Fixed training budgets and capped failures are presented as convergence measurements. — Report budgets, separate success from truncation, evaluate frozen policies, and define any convergence criterion.
- [open] P3 — cell 8 — The summary says there are two options while the example chains three. — Change two to three.

## [X1_rl_debugging.ipynb](notebooks/X1_rl_debugging.ipynb)

- [open] P2 — cell 10–11 — Statistical inference is reduced to mean-gap versus spread and significance-only decision rules. — Report effects and uncertainty, justify test assumptions, and distinguish inconclusive evidence from no effect or practical importance.

## [X2_rl_evaluation.ipynb](notebooks/X2_rl_evaluation.ipynb)

- [open] P1 — cell 7–8, 11 — CartPole return per step is presented as a quality metric even though it is constant. — Use survival length or return under a fixed horizon, or define a different continuing-task objective explicitly.
- [open] P1 — cell 11 — The summary falsely says all metrics reuse identical training runs. — Identify analyses that share runs and those using separately trained agents.
- [open] P2 — cell 9–11 — Statistical inference is reduced to mean-gap versus spread and significance-only decision rules. — Report effects and uncertainty, justify test assumptions, and distinguish inconclusive evidence from no effect or practical importance.
- [open] P2 — cell 3–6, 9–10 — Promised confidence intervals and equal-budget accounting are absent or unsupported. — Provide intervals for the intended estimand, define smoothing and threshold rules, record actual steps, and describe 195 as a chosen threshold.

## [X3_rl_deployment.ipynb](notebooks/X3_rl_deployment.ipynb)

- [open] P1 — cell 6 — A terminal cliff fall incorrectly bootstraps from the start state's value. — Mask terminal bootstrap values or consistently model falls as nonterminal reset transitions.
- [open] P1 — cell 8 — The masked-action task maximizes its target over unsafe as well as safe actions. — Maximize only over safe next actions and suppress bootstrap at terminal states.
- [open] P1 — cell 9–10 — Preference-based reward learning is falsely said to sidestep reward hacking. — Explain reward-model error, distribution shift and proxy overoptimization.
- [open] P1 — cell 10 — Action masking is falsely called the only route to hard safety and its guarantee is overgeneralized. — Scope the claim to the demonstrated grid and correct hazard mask and acknowledge other verified safety mechanisms.
- [open] P2 — cell 9 — Historical, ranking and deployment claims lack usable citations and scope. — Add original-paper and primary deployment references at the claims and specify the task, date and metric for rankings.

## [X4_rl_research_frontiers.ipynb](notebooks/X4_rl_research_frontiers.ipynb)

- [open] P1 — cell 7, 9, 11 — Return conditioning is presented as a guarantee of requested performance. — Describe conditional behavior and its dependence on dataset coverage, stochasticity and model error.
- [open] P1 — cell 8–9 — Decision Transformer evaluation leaves dropout active because no_grad is mistaken for evaluation mode. — Switch the model to evaluation mode before evaluation and restore training mode if training resumes.

## [README.md](README.md)

- [open] P2 — lines 4–6, 23, 26 — The repository promises derivations and scratch implementations that some lessons do not supply. — Publish method-by-method coverage distinguishing derivations, executable scratch code, conceptual sketches and library examples.

## [CURRICULUM_PLAN.md](CURRICULUM_PLAN.md)

- [open] P3 — lines 27, 60, 71, 81, 93, 103, 116, 126, 146, 168, 223, 253, 500 — The curriculum plan uses mismatched notebook filenames and a status inconsistent with the README. — Reconcile filenames and identify the plan as either a historical proposal or the current curriculum specification.
