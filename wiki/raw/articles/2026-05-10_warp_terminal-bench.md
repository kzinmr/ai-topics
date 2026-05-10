---
title: "How we scored #1 on Terminal-Bench (52%)"
source: "Warp Blog"
url: "https://www.warp.dev/blog/terminal-bench"
scraped: "2026-05-10T01:28:11.523052+00:00"
lastmod: "2026-04-19T15:37:21.000Z"
type: "sitemap"
---

# How we scored #1 on Terminal-Bench (52%)

**Source**: [https://www.warp.dev/blog/terminal-bench](https://www.warp.dev/blog/terminal-bench)

Engineering
How we scored #1 on Terminal-Bench (52%)
Jack Nichols
June 25, 2025
To see how we achieved 71% (top 5) on SWE-bench Verified, see
this post
.
Terminal-Bench
is an open-source benchmark for evaluating how well AI agents perform on complex tasks that are rooted in the terminal. The tests range from resolving mangled Python dependencies, removing all API keys from a codebase, and training a text classification model against real Yelp review data, to mention a few. Generally, the tasks require the agent to learn about a unique shell environment, complete the specification of the test, and validate its solution robustly, all within some timeframe ranging from a few minutes to around an hour.
Warp succeeds on 52% of Terminal-Bench tests (v0.1.1), which is state of the art and over 20% (almost 9 percentage points) ahead of the next top submission. Our agent passed around 65% of the test suite across all runs and, on any given run, Warp performs differently depending on a range of factors like which models are specified, whether the agent is told to create a plan at the outset of the task, or - unpredictably - what approach the agent decides is optimal and therefore chooses to attempt first.
We built our agent backend to support rapid experimentation. A few of the features we found particularly helpful for the Terminal-Bench suite were:
configuring our model fallback chain optimally
granting the agent control over long-running commands, and
forcing the agent to maintain a todo list throughout the duration of the task.
Integrating with Terminal-Bench
We run the test suite completely through the Terminal-Bench
harness
and expose Warp via its
AbstractInstalledAgent
class. Every Terminal-Bench test is a single task specification that we feed to Warp as a CLI argument and is then passed as the opening user query in a fresh Agent Mode task. During task execution, the mocked user is exempt from AI request limits and all permissions settings are configured to “Always Allow” - meaning, all agent actions like shell commands and file edits are applied without user confirmation.
Some test environments in Terminal-Bench force a specific architecture. For example, the test
get-bitcoin-nodes
specifies x64, whereas other tests fallback to the host architecture. Because Warp is a standalone application (rather than an invoked CLI tool like Claude Code), this means we have to cross-compile and serve a build of Warp that matches the given test environment.
We also set up window forwarding through X11 so every test opens a new Warp window and we can watch as the agent makes progress. Though, we found running as headless - and thereby avoiding occasional X11 errors - to be a more reliable approach.
How we got to 52%
Model experimentation
All the runs that comprised our 52% average used Claude Sonnet 4 as the primary model and Claude Opus 4 as a planning model, leveraging the intelligence of Opus to provide a high-level strategy to the problem and then relying on the speed of Sonnet to execute on said strategy. In the rare case a request fails –  be it an outage, a rate limit, a malformed tool call, etc. – we use a fallback mechanism to retry the request with a different model. Approximately 2% of all the tests we submitted to Terminal-Bench involved a request to a non-Anthropic model (Gemini 2.5 Pro or OpenAI GPT-4.1).
We were excited to experiment with Opus 4 as the base model in our requests, given that Claude Code reported an 8% performance bump between Sonnet 4 and Opus 4, but we unfortunately weren’t able to reproduce a similar benefit ourselves. Even when we tried to increase the speed of Opus 4 by allowing it to make tool calls in parallel, we still observed slightly worse performance on the test suite relative to our baseline with Sonnet 4.
Long-running command support
Allowing the agent to control long-running commands like REPLs, interactive shell scripts, and vim was a major bump for us. Previously, when the agent ran a long-running shell command (imagine it invoking vim), we relied on the user to manually quit the command and restore control to the agent. Under this approach, any Terminal-Bench test that runs a command requiring some control sequence to exit (e.g., ctrl-c) fails by timeout.
We built a solution that periodically sends the output of commands to the agent and permits the agent to optionally write bytes to the
pty
. While a long-running command is running, we remove certain tool calls from the supported set, so the agent can’t make a file edit or run a new shell command while one is already in progress. We built this in a day, realized it potentially provides a lot of user value, and plan to ship it to users in the coming weeks.
Planning
As mentioned before, our most successful test runs also used a planning step. The agent creates a list of todos that it then updates as it proceeds. We found this forces the agent to perform more reasoning at the very beginning of a task before it begins implementation. In addition, making the todo list editable allows the agent to revisit previous assumptions if the execution of the original plan doesn’t go as intended or new information is uncovered.
We also experimented with
extended thinking
to fulfill a similar role but, based on initial results, we decided to focus more attention on the explicit planning step. Separately, we experimented with conditional planning - the agent can decide itself whether the task merits a plan or not - but we didn’t end up using that in our most successful runs either.
Conclusion
We’re grateful to the Terminal-Bench maintainers for their benchmark and all their help! The project accepts submissions for new tasks if you’ve encountered any challenging terminal workflows of late!
We’re also excited to continue pushing on what our agent can do. We’re confident that these benchmarks show, at least in part, the real value our tool is able to provide for developers, and we hope you’ll give Warp a try!
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
