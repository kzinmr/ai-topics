---
title: "Warp scores 75.8% on SWE-bench Verified!"
source: "Warp Blog"
url: "https://www.warp.dev/blog/swe-bench-verified-update"
scraped: "2026-05-10T01:28:11.197013+00:00"
lastmod: "2026-04-19T15:37:21.000Z"
type: "sitemap"
---

# Warp scores 75.8% on SWE-bench Verified!

**Source**: [https://www.warp.dev/blog/swe-bench-verified-update](https://www.warp.dev/blog/swe-bench-verified-update)

Engineering
Warp scores 75.8% on SWE-bench Verified!
Suraj Gupta
Daniel Peng
September 1, 2025
Our approach
We built on the same production-grade, single-agent system we used in our previous
SWE-bench Verified
submission. The agent and tools are the same ones we ship in Warp, which keeps our results representative of real-world usage.
We used a single‑agent architecture powered by GPT‑5 as the primary model, equipped with a focused toolset:
Editing and file‑creation tools for precise changes.
Code‑understanding tools (grep/find/cat analogues) for targeted, windowed reads.
A command execution tool to run builds/tests.
Lightweight planning via TODO generation to structure multi‑step fixes.
We built a custom evaluation harness that can launch and control Warp, a desktop application. We submit each SWE-bench instance as a user prompt and inspect application state to validate behaviour. To reduce run-to-run variability inherent in long agent coding tasks, we added a light best@k wrapper around the core single-agent flow. For each instance, the agent proposes a small number of candidate patches and then selects the most promising one. This is used to smooth over non-determinism rather than change capabilities, and every result produced by this harness reflects an outcome that’s achievable in Warp today.
For more details on our architecture and evaluation harness, read the
blog post for our original submission
.
Most of our quality gains in this submission come from strengthening the primary agent's quality and reliability, which benefits both benchmark performance and everyday developer experience.
What we’ve improved since last time
Maintaining a task list
One of the most significant updates to our agent infrastructure since our last SWE-bench submission is the introduction of task lists. Warp’s agent now automatically creates a task list whenever a problem benefits from being broken into steps. These lists require no user input—they’re generated when useful and continuously updated by the agent. Since rolling them out, we’ve seen a 2% improvement in our baseline SWE-bench score.
An example of a task list created by Warp’s agent for a SWE-bench eval.
Our planning feature is also now powered by task lists. Previously, plans were rigid: once generated, the agent would follow them exactly, even if new information suggested a better path. With task lists, each planned step becomes a dynamic TODO item. This allows the agent to adapt as it works, much like how humans adjust their problem-solving approach.
See our
docs
for more details about the task list feature.
Improving quality of longer conversations
As conversations grow and the context window becomes saturated, Warp automatically summarizes earlier turns so you can continue seamlessly. Our initial summarization approach often fell short: key details were sometimes lost, forcing the LLM to regather context before continuing a topic.
We recently revisited this approach and made several improvements:
Model-aligned summarization
: summaries are generated using the same model that the conversation was carried out with, rather than reformatting the conversation trace to be summarized by an auxiliary LLM.
Stronger prompt design
: the summarization prompt clearly defines what makes an effective summary, giving the LLM a structure to follow.
Protected content
: critical elements (e.g., TODO state, rules) are deterministically preserved post-summarization.
Natural continuity
: the summary is seeded with the most recent user–agent turn to maintain flow.
With these changes, we’ve seen improved performance on SWE-bench evaluations involving summarization. While this work isn’t limited to SWE-bench, we’re developing a dedicated set of evals to measure summarization quality more broadly. We expect to roll out these improvements into our production agent  in the coming weeks and hope to share more quantitative results about these improvements!
Improving our file editing tool
When Warp’s agent makes a file edit that gets accepted, we return the updated contents back to the agent. Previously, we always sent the entire file, even if only a single line had changed. In large files (e.g., 5,000 lines), this meant the agent would receive thousands of redundant lines when only one was actually updated. This quickly consumed the LLM’s context window.
We’ve since improved this by returning only the modified section of the file plus ± k surrounding lines. Using SWE-bench, we validated that this approach yields better results while significantly reducing token usage—improving quality while reducing costs for our users.
Long running command support
In our previous submission, we introduced long‑running command support in the
run_command
tool. The agent can interact with alt‑screen or pager processes (like REPLs,
git log
, or even vim) using a specialized tool mode that sends input and consumes incremental output. We've seen our agents use this capability to do things like read docs via the
help
builtin, interrupt slow tests with
ctrl-c
, and inspect repository history.
This is a feature still under active development. Running SWE-bench at scale was valuable in helping us identify real-world issues with the tool. For example, we discovered an edge case that would cause our agent to get stuck in a long-running command. We were able to iron out these issues and make long-running command support much more robust.
Debugging instructions
To improve fix accuracy, we added explicit debugging guidance to the agent’s prompt for SWE-bench. After reproducing a failure, the agent is instructed to launch and control a debugger using our long‑running command tool. The agent can set breakpoints, step through failing tests, and inspect variables and stack frames. The goal is to capture the problematic runtime state, confirm the hypothesis behind the failure, and then target the minimal, correct change.
Looking ahead, we’re exploring adding a dedicated debugging/research agent into Warp that has its own context window. This agent would incorporate lessons learned from our SWE-bench testing and provide similar instructions for debugging.
Conclusions
Our improved performance on SWE-bench Verified demonstrates that:
A single-agent architecture with focused tools remains a highly effective setup for coding tasks. There’s headroom for improvement through agent quality and reliability even without introducing more complex architectures.
GPT-5 can compete with the state of the art on real-world coding tasks. It’s an effective model to use as a primary model within Warp.
Improving long, multi-step coding tasks remains a major lever for boosting overall agent quality. Our introduction of task-list tracking to keep the agent on task and improved long-context summarization delivered sizable gains, and there’s still meaningful work to be done here.
We're excited to continue improving Warp and to see what our users build with it!
Related articles
May 4, 2026  ·  9 min
Open-sourcing our docs and the agents that maintain them
Today, we’re moving our product documentation at docs.warp.dev onto a stack we control end-to-end, and open-sourcing it at github.com/warpdotdev/docs.
Apr 29, 2026  ·  16 min
The Block Model Behind Warp's Agentic Development Environment
Warp has come a long way since it initially set out to modernize the terminal. In the screenshot above, an agent is working through a plan alongside a developer's own shell commands — running its own commands, reasoning, proposing a diff — all in the same scroll stream. Five years ago, none of that would have had a place in Warp; today it's a core part of how people use it.
Apr 16, 2026  ·  2 min
Introducing Claude Opus 4.7 in Warp
Claude Opus 4.7 is now available in Warp on paid plans and is the new default model for auto (genius), bringing stronger performance on multi-step coding tasks, debugging, and agent workflows.
