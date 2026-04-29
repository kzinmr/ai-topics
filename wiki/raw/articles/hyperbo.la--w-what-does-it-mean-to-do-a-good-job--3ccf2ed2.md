---
title: "What Does It Mean to Do a Good Job?"
url: "https://hyperbo.la/w/what-does-it-mean-to-do-a-good-job/"
fetched_at: 2026-04-29T07:02:14.898473+00:00
source: "hyperbola :: blog"
tags: [blog, raw]
---

# What Does It Mean to Do a Good Job?

Source: https://hyperbo.la/w/what-does-it-mean-to-do-a-good-job/

Verification was always the problem. AI makes that obvious because every real
task is downstream of a question we almost never write down. What does it mean
to do a good job?
Producing an artifact and reviewing it both require hundreds of small decisions
about non-functional requirements: tone, taste, risk tolerance, how much polish
is enough, what shortcuts are acceptable, what counts as done. Historically,
teams wrote almost none of that down. We encoded it in org design, social norms,
hiring loops, onboarding, and repeated exposure to people who already knew the
answer.
That worked well enough when the worker was a coworker. You could hire for
judgment, build trust over time, and let the person absorb the unwritten rules.
You do not get to run your AI through a hiring pipeline. And because models have
seen trillions of documents that embody every possible permutation of those
choices for nonfunctional requirements, basically every task we hand them is
under-specified.
One concrete example from my work at OpenAI: for our code implementation agent
and various reviewer agents, we had to write down choices human reviewers
usually carry in their heads. Implementation agents must acknowledge review
feedback, but they can accept and fix, accept and defer, or push back. Reviewer
agents are told to bias toward merging and only surface P2s and above.
Without that guidance, the reviewers endlessly bully the implementer and nothing
converges. Human reviewers usually know to unblock while still providing
high-signal feedback. The models do not unless you say it.
This is why verification suddenly feels like the whole problem and why
harness
engineering
is a productive area for applied AI
engineering. The missing spec was always there. Humans were just better at
smuggling it in through shared context.
Post-training optimizes these tools to be helpful assistants, not task-specific
experts. The models crave text and they are rewarded for how well they follow
instructions, so there is an inherent tension in RL between
instruction-following fidelity and “creativity” in reasoning. If you want the
models and agents to do a good job, write down what that means, then add nuance
only when the coarse instruction starts to overfit.
