---
title: "Best Practices for Multi-Turn RL"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/best-practices-for-multi-turn-RL"
scraped: "2026-05-10T01:27:58.384176+00:00"
lastmod: "2026-01-16T21:10:49.000Z"
type: "sitemap"
---

# Best Practices for Multi-Turn RL

**Source**: [https://fireworks.ai/blog/best-practices-for-multi-turn-RL](https://fireworks.ai/blog/best-practices-for-multi-turn-RL)

DeepSeek V4 Pro is Live → Try it now.
Platform
Models
Developers
Pricing
Training
Partners
Resources
Company
Log In
Get Started
Blog
Best Practices For Multi Turn Rl
Best Practices for Multi-Turn RL
PUBLISHED
12/10/2025
Impact at a Glance
2X
Faster Proposal Assistance
0.75s
Sub-second first-token latency
125%
Increase in Engagement
Table of Contents
Introduction
From Single-Turn to Multi-Turn
Why RL Beats SFT for Multi-Turn Agents
Anatomy of a Multi-Turn RL System
Reward Design: Partial vs Trajectory-Level
Building a Reward Function that Survives Contact with Reality
Practical Recipes: Making Multi-Turn RL Work
Case Study: A Deep Research Agent
Summary
Table of Contents
Table of Contents
Introduction
From Single-Turn to Multi-Turn
Why RL Beats SFT for Multi-Turn Agents
Anatomy of a Multi-Turn RL System
Reward Design: Partial vs Trajectory-Level
Building a Reward Function that Survives Contact with Reality
Practical Recipes: Making Multi-Turn RL Work
Case Study: A Deep Research Agent
Summary
Table of Contents
How to train LLM agents that can reliably plan, call tools, and recover from their own mistakes.
Introduction
In the evolution of AI agents, we are witnessing a distinct phase shift. We are moving past the era of simple, single-turn query-response interactions implemented in simple assistants into a domain defined by sequential agency. We are no longer just asking models to answer a question; we are asking them to interface with an environment through multiple interactions to complete complex tasks that are multi-step, open-ended, and tool-heavy – e.g.,:
•
Planning a trip: search, filter options, compare itineraries, book flights, reserve hotels, and monitor changes.
•
Data investigations: run SQL queries, inspect anomalies, call monitoring dashboards, and generate follow-up hypotheses.
•
Research workflows: search, read, summarize, cross-check, and synthesize across multiple sources.
These are multi-turn, sequential decision problems: the agent must decide which tool to call, when, and with what arguments, potentially dozens of times before the task is complete. The environment state evolves with every tool call.
In this regime, Supervised Fine-Tuning (SFT) on “golden traces” is often not enough. We need agents that learn from interaction – from success, failure, and everything in between. That is exactly what Reinforcement Learning (RL) provides.
This post lays out how to think about multi-turn RL for sequential tool use, how to design reward functions that don’t explode in your face, and a set of practical recipes that we have found to work in real systems.
From Single-Turn to Multi-Turn
Before we talk about training, it’s worth contrasting the single-turn and multi-turn settings.
Feature
Single Turn
Multi Turn
Interaction space
Interaction space Small, fairly predictable (e.g., “call one API once”)
Combinatorial explosion of tool sequences and arguments
Credit assignment
Trivial: the one call was right or wrong
Hard: final failure may come from any earlier decision
Training method
SFT usually works quite well
SFT struggles; RL is typically needed
Example
“Use search once and answer”
“Perform deep research with many calls, cross-checks, and revisions”
A common workaround is to approximate multi-turn tasks by decomposing them into single-turn subproblems – for example, treat each retrieval call as an independent “episode” with its own label (“did we retrieve a relevant document?”). This is viable only if you can define good partial rewards on each step.
As tasks become longer-horizon and more open-ended, decomposition breaks down: what matters is whether the final outcome is good, not whether each individual step looks locally reasonable.
That’s where full multi-turn RL comes in.
Why RL Beats SFT for Multi-Turn Agents
What SFT gives you
Supervised Fine-Tuning takes a dataset of expert trajectories – “golden paths” where a human or stronger model has already solved the task – and trains the model to imitate those traces token-by-token.
This has clear benefits:
•
It jump-starts the agent with reasonable behavior.
•
It can teach non-obvious tool usage patterns when those examples appear in the data.
•
It is stable and easy to scale.
But SFT has equally clear limitations in the multi-turn setting:
•
It sees only a small subset of the state space. Once the agent deviates from the golden path – because the environment changed, a tool failed, or the user asked something novel – it has no guidance.
•
It cannot learn to recover. Failures in intermediate steps are rarely labeled with what to do next. The model simply never sees those trajectories.
•
It requires fully labeled trajectories. For complex tool chains, generating high-quality supervised traces is expensive and brittle.
In other words, SFT learns a
map of known roads
, but not
how to navigate
when you miss a turn or a road is blocked.
What RL adds
RL, in contrast, optimizes the policy to maximize expected cumulative reward in the actual environment:
•
It encourages exploration, discovering new strategies that were never present in the supervised data.
•
It learns from interaction rather than from static logs: every rollout is a new training example.
•
It naturally supports error recovery: if taking a corrective action after a mistake leads to higher final reward, the policy can learn to do that.
Crucially, RL is not purely an alternative to SFT; it is usually stacked on top of an SFT-ed model. SFT gives you a warm start; RL teaches the model to adapt, generalize, and self-correct.
In multi-turn, tool-heavy settings, RL is usually the way to go. SFT alone quickly hits a ceiling.
Anatomy of a Multi-Turn RL System
A realistic multi-turn RL training loop for LLM agents looks more like a distributed systems diagram than a simple “environment + agent” cartoon.
The slide deck shows a helpful schematic: prompts flow into a
trajectory generator
, which talks to an
inference service
(the LLM), an
environment
(the tools), and a
trainer
, forming a closed loop.
Let’s unpack the key components.
Key Components Block Diagram
Trajectory generator
The trajectory generator:
•
Takes initial prompts (tasks).
•
Calls the policy (LLM) via the inference service to obtain the next action (e.g., a tool call).
•
Executes that action against the environment (APIs, databases, search).
•
Captures the output of the action (tool call results).
•
Terminates the episode when some stopping condition is met (success, failure, timeout, max steps).
The output is a trajectory (a rollout): a sequence of user-assistant-tool messages capturing the interactions between different roles in the conversation.
Environment and tools
The environment is everything outside the LLM:
•
Tool backends (search APIs, booking systems, code execution sandboxes, etc.).
•
State that evolves over time (e.g., a simulated calendar, a running browser, a research scratchpad).
•
Any side effects of tool calls (creating tasks, sending emails, placing orders).
In production-adjacent settings, environment issues are a major pain point:
•
APIs change, rate-limit, or fail.
•
Latencies vary wildly, affecting throughput.
•
Deterministic evaluation is hard when tools are non-deterministic or rely on external data sources.
Part of making multi-turn RL work in practice is stabilizing the environment: pinning versions, caching tool calls where possible, and standardizing error handling.
Rewards
Rewards are applied to trajectories to score their quality. They can be specified in several ways, including:
•
Programmatic function – for example, a Python function that parses the trajectory and evaluates whether the tool calls are correct.
•
Model-based reward – either
•
a general-purpose model, prompt-tuned to judge trajectory quality, or
•
a specialized reward model trained explicitly for reward attribution.
Trainer and policy updates
Given batches of trajectories and associated rewards, the trainer performs policy gradient updates with some form of KL-regularization to avoid catastrophic drift from the base model.
In practice, this often looks like a PPO-style or GRPO-style objective of the form:
max
⁡
π
E
τ
∼
π
o
l
d
[
w
(
τ
)
⋅
A
(
τ
)
−
β
K
L
(
π
(
⋅
∣
τ
)
∥
π
r
e
f
(
⋅
∣
τ
)
)
]
\max_{\pi} \mathbb{E}_{\tau \sim \pi_{old}} \left[ w(\tau) \cdot A(\tau) - \beta KL(\pi(\cdot \mid \tau) \| \pi_{ref}(\cdot \mid \tau)) \right]
max
π
​
E
τ
∼
π
o
l
d
​
​
[
w
(
τ
)
⋅
A
(
τ
)
−
β
K
L
(
π
(
⋅
∣
τ
)
∥
π
r
e
f
​
(
⋅
∣
τ
))
]
where
•
A
(
τ
)
A(\tau)
A
(
τ
)
is some advantage estimate derived from the rewards,
•
w
(
τ
)
w(\tau)
w
(
τ
)
is an importance-weight factor with clipping,
•
π
r
e
f
\pi_{ref}
π
r
e
f
​
ref is a frozen reference model (often the SFT checkpoint),
•
β
\beta
β
is a KL term.
Why it gets complicated
Putting this all together, we now have quite a few components to juggle. Yet once you have this loop working, you gain a very powerful capability: end-to-end optimization of agent behavior in realistic environments.
Reward Design: Partial vs Trajectory-Level
Reward design is where most agentic RL projects succeed or fail. A core axis is partial (step-level) vs. trajectory-level (episodic) rewards.
Partial rewards (dense / shaping)
Here we assign rewards to intermediate steps, such as:
•
“Retrieval hit”: +0.2 if a retrieved document is relevant.
•
“Unit test passed”: +0.3 when a test suite succeeds.
•
“Tool called with valid parameters”: +0.1.
This yields dense signal, which is good for exploration and sample efficiency: the agent does not need to stumble upon a full successful trajectory to start receiving gradient signals.
However, partial rewards come with serious downsides:
•
Myopia
: the agent optimizes for the proxy (“pass unit tests”) rather than the real goal (“solve the user’s problem”).
•
Reward hacking
: the agent exploits loopholes - e.g., overfitting to trivial tests, spamming retrieval calls that look “good” according to the shaping term.
Trajectory-level rewards (episodic)
At the other extreme, we assign reward only at the end:
•
Success: +1.0
•
Failure: −1.0
This directly optimizes what we care about: did the agent solve the task? It is robust to many forms of proxy gaming, since there are no intermediate targets to overfit.
The downside is that the signal is sparse and high-variance:
•
Many trajectories have the same zero or negative reward.
•
Credit assignment over long horizons is difficult; learning can be slow.
Trade-offs in practice
•
Signal density:
partial rewards are dense; trajectory-level are sparse.
•
Alignment:
trajectory-level is best aligned to the actual objective.
•
Robustness:
partial rewards are more hackable; trajectory-level less so.
•
Engineering overhead:
partial rewards require crafting proxies at each step; trajectory-level “only” needs a reliable success metric.
In real-world deployments, trajectory-level rewards tend to be more practical, precisely because defining robust partial rewards across a complex multi-turn workflow is extremely difficult. It is already a non-trivial challenge to define “success” at the end; doing so at every intermediate step can quickly become intractable.
A useful pattern is:
Start with a pure episodic signal: success vs failure, possibly with a small step penalty.
Once that is working, optionally layer in light shaping terms that you have high confidence in.
Building a Reward Function that Survives Contact with Reality
Given the above, a pragmatic reward function for a multi-turn agent often looks like a weighted sum of a few components:
Final outcome
(dominant term)
•
Large positive reward for success, large negative for failure (e.g., +1.0 / −1.0).
•
Anchors the agent to the real goal; everything else is secondary.
Step penalty
•
Small negative per step (e.g., −0.05).
•
Encourages efficiency, avoids infinite loops, and discourages pathological “stalling” behaviors.
Tool call validity
•
Penalty for syntactically invalid or semantically absurd tool calls (e.g., −0.2 per error).
•
Teaches the model the “rules of the game” without needing to explicitly label each failure.
Progress shaping (optional, advanced)
•
Small positive rewards for clearly helpful intermediate results (e.g., returning a relevant evidence chunk, successfully executing a query that moves the task forward).
•
Can speed up learning but carries an elevated risk of reward hacking.
A critical design principle is: The final outcome reward must dominate. If an intermediate metric – like “successful search call” – is rewarded too heavily, the agent may converge to a degenerate policy: repeatedly call search in ways that look locally good to the heuristic, without ever finishing the task.
The safe recipe is “start simple”:
•
Begin with (1) + (2) + (3), tune magnitudes until behavior is reasonable.
•
Only add (4) if learning is clearly bottlenecked by sparsity, and monitor closely for emergent hacks.
Practical Recipes: Making Multi-Turn RL Work
Training LLM agents with multi-turn RL is fragile. Over time, a few heuristics have emerged as consistently useful.
Choose the right base model
You need a base model that has
non-trivial zero-shot success
on the task—on the order of ~20% success out-of-the-box.
•
If the baseline is much lower, exploration becomes too difficult; the agent rarely experiences success and gradients are dominated by noise.
•
If the baseline is too high, you may see diminishing returns from RL; SFT or prompting might be sufficient.
If your current model is below that threshold, you have two options:
•
Move to a
larger or better pre-trained model
, or
•
Use
SFT
on curated trajectories to lift the baseline before applying RL.
Snapshot selection: latest is not always greatest
When running RL for many thousands of updates,
the final checkpoint is often not the best
. RL can over-optimize for quirks of the training distribution or reward function.
A better practice is to:
•
Periodically evaluate checkpoints on a
held-out episodic benchmark
that matches your deployment distribution.
•
Select the snapshot with the highest
trajectory-level success rate
, not the lowest training loss or highest shaping reward.
Environment stability and reproducibility
Many mysterious RL failures are actually
environment failures
:
•
A tool version was silently upgraded.
•
A third-party API started returning different schemas.
•
Random seeds differ across rollouts, making evaluation noisy.
To mitigate this:
•
Pin versions
of all tools, models, and dependencies during training.
•
Cache tool responses
whenever possible, especially for static queries.
•
Standardize error handling and timeouts so that failures are predictable.
Encourage exploration: temperature, top-p, and rollouts per prompt
Exploration is crucial: the agent must try sufficiently diverse trajectories to find successful ones.
Practical knobs include:
•
Increasing temperature and top-p during rollout generation.
•
Sampling more trajectories per prompt.
The goal is to expand the support of behavior while keeping it within a manageable KL radius of the base model.
Keep tasks in the “learnable band”
If tasks are too easy, you don’t need RL; if they are too hard, RL won’t help because the agent never sees reward.
A simple curriculum strategy:
•
Start with simplified versions of the task (shorter horizons, fewer tools, more forgiving success criteria).
•
Once the agent performs well, gradually increase difficulty toward the real deployment regime.
Train close to production
Large discrepancies between training and production environments are a recipe for disappointment. Whenever feasible:
•
Use the same tool backends, schemas, and error conditions.
•
In some setups, you can even plug RL directly into a production-like sandbox environment with anonymized or synthetic tasks.
First principles: data, rewards, environment > algorithm
It is tempting to obsess over algorithmic variants (PPO vs GRPO vs RLOO, etc.). While these matter, in practice:
•
Quality and coverage of tasks (data),
•
Fidelity of reward to true utility, and
•
Stability and realism of the environment
dominate overall performance. Algorithm choice is second-order.
Case Study: A Deep Research Agent
To make this concrete, consider training a
deep research agent
: given a complex query (“Summarize the current state of X and compare approaches A, B, C”), the agent:
Issues multiple search queries.
Retrieves candidate documents.
Skims and filters them.
Cross-checks facts.
Synthesizes a structured answer.
Training Progress Chart
Training such an agent with multi-turn RL yields a learning curve like the one shown in the plot above: starting from a baseline performance somewhere around 0.5 reward, steadily climbing, and eventually surpassing a frontier model baseline (shown as a dashed red line). The improvement is asymptotically monotonic but noisy: there are plateaus and small regressions as the policy explores and the reward landscape shifts.
This illustrates the main value proposition of multi-turn RL for tool use: you can turn a weaker LLM into a specialized agent that outperforms frontier models on specific complex workflows, purely by optimizing how it interacts with tools and structures its reasoning over multiple turns.
Summary
If you’re thinking about building multi-turn, tool-using agents, here are the main lessons:
Use RL or SFT + RL, not SFT alone.
SFT gives you reasonable behavior; RL makes it robust and adaptive in open-ended environments.
Favor trajectory-level rewards with minimal shaping.
It’s easier to define “success or failure” at the end than reliably judge every intermediate step – and much harder to hack.
Invest in environment engineering.
Most “RL bugs” are actually environment or integration bugs. Make tool usage deterministic where possible, pin versions, and log everything.
Start with a strong base model.
Aim for ~20% zero-shot success before RL; if you’re far below that, fix the model or data first.
Prod parity
: keep the training environment close to production (or plug into production when feasible).
Expect complexity.
A production-grade multi-turn RL system is a distributed system plus an ML training stack. Hosted providers that specialize in this can abstract away much of the infrastructure and algorithmic complexity.
We are still early in understanding the full design space of long-horizon LLM agents. But the pattern is already clear: as we move from “models that answer questions” toward agents that act, multi-turn RL for sequential tool use will be one of the central levers for pushing capabilities forward.
Platform
AI Native
Enterprise
Customers
Use Cases
Code Assistance
Conversational AI
Agentic Systems
Search
Multimodal
Enterprise RAG
Developers
Model Library
Docs
CLI
API
Changelog
Pricing
Serverless
On-Demand
Fine Tuning
Enterprise
Partners
Cloud and Infrastructure
Consulting and Services
Technology
Fireworks for Startups
Resources
Blog
Demos
Cookbooks
Company
Leadership
Investors
Careers
Trust Center
© 2026 Fireworks AI, Inc. All rights reserved.
