---
title: "Using Codex Goals Effectively"
author: Chris Hayduk (@ChrisHayduk)
date: 2026-05-11
source: https://x.com/ChrisHayduk/status/2053807198870880743
x_article_id: "2053705681614536704"
getxapi: false
source_fallback: web_extract
tags: [codex, /goal, coding-agents, prompting, ai-agents, agentic-engineering]
engagement: {likes: 858, bookmarks: 1934, impressions: 109081}
---

# Using Codex Goals Effectively

Chris Hayduk (FDE, Life Sciences @ OpenAI) shares practical tips for using the Codex `/goal` command effectively, based on his experience using goal mode internally at OpenAI and in side projects.

## Key Insight: Different Prompting Model

Perceptive Codex users have noticed that the `/goal` command is now available in the Codex app — just start your prompt with `/goal`, and specify what you want your agent to do. This triggers Codex to loop continuously until it achieves your goal.

But in order for the agent to do this effectively, we need to think about prompting the model in **slightly different ways** than you may be used to.

## Specify A Clear, Quantitative Goal

Models have gotten so good over the past ~6 months that many of us have gotten lazy as prompters in our everyday workflows. We can vaguely gesture at what we want GPT-5.5 to build, and it's pretty good at inferring the rest.

However, when you're writing a goal prompt for autonomous codex loops, it's **really important** to be:

- **Quantitative** — Specify exactly what "done" looks like. "Make the app faster" is bad. "Reduce Time to Interactive (TTI) from 3.2s to under 1.5s while maintaining Lighthouse scores > 90" is good. Without a clear metric, the agent cannot self-verify and will either stop early or loop forever.
- **Explicit about constraints** — What NOT to change, what's off-limits, what architectural patterns to follow
- **Clear about the definition of done** — Include specific test criteria, acceptance tests, or verification steps

## Meta-Prompting for Better Goals

Given the importance of high-quality goal prompts, a meta-prompting approach is highly effective:

1. Open a fresh Codex session with full project context
2. Ask it to research what `/goal` actually does and how it works
3. Have it inspect your codebase for high-leverage missions
4. Ask it to produce complete goal prompts with scope, constraints, files, and definitions of done

This technique (using AI to write prompts for AI) consistently produces better goals than hand-written ones and prevents the agent from going off-track during long autonomous runs.

→ See [[concepts/codex-goal-meta-prompting]] (Aditya Bawankule's detailed meta-prompting workflow)

## Additional Tips

- **Start small** — Don't jump to "rebuild the entire frontend." Start with a well-scoped goal and iterate.
- **Define file scope** — Specify which files/directories the agent can modify. This prevents sprawling changes.
- **Use test suites as guardrails** — If you have a test suite, instruct the agent to keep all tests passing. Tests function as an objective "did you break anything" check.
- **Set clear budget limits** — Configure token budgets in `~/.codex/config.toml` so the agent doesn't burn through credits on marginal improvements.
- **Review agent commits** — After a goal run, review the commit log. The agent's iterative changes often reveal valid optimizations alongside hacks that need reverting.

## Author

Chris Hayduk — FDE on the Life Sciences team at OpenAI. Previously MLE at Meta (ads ranking, GNNs), Lead ML Engineer at Deloitte (drug discovery AI). Cross-disciplinary writing on AI at chrishayduk.com.
