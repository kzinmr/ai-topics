---
title: "Improving Cursor’s agent for OpenAI Codex models · Cursor"
source: "Cursor Blog"
url: "https://cursor.com/blog/codex-model-harness"
scraped: "2026-05-10T01:19:44.363124+00:00"
lastmod: "2026-05-09T16:09:42.638Z"
type: "sitemap"
---

# Improving Cursor’s agent for OpenAI Codex models · Cursor

**Source**: [https://cursor.com/blog/codex-model-harness](https://cursor.com/blog/codex-model-harness)

Blog
/
product
Dec 4, 2025
·
product
Improving Cursor’s agent for OpenAI Codex models
6 min read
Table of Contents
↑
Building a robust agent harness
Updating for the latest Codex model
A more shell-forward approach
Preambles
Reading lints
Preserving reasoning traces
Biasing the model to take action
Message ordering
Looking forward
Cursor integrates with all frontier AI models for coding.
Each model requires specific instructions and tweaks to our agent harness to improve output quality, prevent laziness, efficiently call tools, and more.
We’ve been partnering with OpenAI to make their models available to developers with Cursor’s agent. This post will cover how we’ve updated our agent harness to support their latest frontier coding model
GPT-5.1-Codex-Max
.
#
Building a robust agent harness
Every model in Cursor’s agent harness has specific instructions and tools made available to optimize that model inside the Cursor environment.
AI labs train new models on a variety of different instructions and tools. In specific domains like coding, models may favor patterns that are more similar to what they’ve already seen in training. When adding new models into Cursor, our job is to integrate familiar instructions and tools alongside Cursor-specific ones, and then tune them based on Cursor Bench, our internal suite of evals.
We measure the quality and robustness of models based on their success rate, ability to call tools, and overall adoption across users. Here are some of the updates we made to our agent harness for Codex.
#
Updating for the latest Codex model
OpenAI’s Codex models are versions of their latest frontier model, trained specifically for agentic coding.
The OpenAI team collaborated closely with us to align the tools and prompts with the Codex CLI harness. Here are some of the changes we’ve made:
#
A more shell-forward approach
OpenAI’s Codex CLI is focused on shell-oriented workflows. As a result, the Codex model receives a limited set of tools during training and learns instead to use the shell to search, read files, and make edits.
If the model is struggling with a difficult edit, it sometimes falls back to writing files using an inline Python script. These scripts are powerful, but tool calling is both safer and a better user experience for edits in Cursor.
To encourage tool calling, we made the names and definitions of tools in Cursor closer to their shell equivalents like
rg
(ripgrep). We made this change for all models in our harness. We also added instructions like:
If a tool exists for an action, prefer to use the tool
instead of shell commands (e.g. read_file over `cat`).
Sandboxing
in Cursor, which prevents unauthorized file access and network activity without requiring users to manually approve every command, also helps improve security here if the model does still choose to run a shell command.
#
Preambles
Unlike the mainline GPT-5 series of models, the Codex model family currently uses reasoning summaries to communicate user updates as it’s working. These can be in the form of one-line headings or a full message.
For these reasoning summaries, we wanted to strike a balance that would let users follow along with the agent’s progress and identify bad trajectories early, without spamming them to the point that they tune out. We gave the model guidelines to limit reasoning summaries to 1 or 2 sentences, note when discovering new information or initiating a new tactic, and to avoid commenting on its own communication (“I’m explaining to the user…”).
Since Codex models cannot “talk” normally until the end of an agent turn, we removed all language in the prompt related to communicating with the user mid-turn. We found that this improved the performance of the model’s final code output.
#
Reading lints
Cursor makes tools available to all models in our harness for reading linter errors (e.g. ESLint, Biome) and allowing the agent to automatically fix them.
We found that providing Codex with the tool definition alone is not enough to make it inclined to call our
read_lints
tool. Instead, Codex benefits significantly from clear and literal instructions for when to call it:
After substantive edits, use the read_lints tool to check
recently edited files for linter errors. If you've introduced
any, fix them if you can easily figure out how.
#
Preserving reasoning traces
OpenAI’s reasoning models emit internal reasoning traces between tool calls, which are effectively a “chain of thought” explaining why the model chooses each action. The
Responses API
is designed to capture and pass along these reasoning items (or encrypted reasoning items in sensitive contexts) so the model can maintain continuity across turns rather than having to reconstruct its plan from scratch.
Codex is especially dependent on this continuity. When reasoning traces are dropped, the model has to infer its previous thought process, which often leads to lost subgoals, degraded planning, misordered tool calls, or repeatedly re-deriving earlier steps. In our Cursor Bench experiments, removing reasoning traces from GPT-5-Codex caused a 30% performance drop. In comparison, OpenAI
observed
a smaller 3% degradation for GPT-5 on SWE-bench when reasoning traces were omitted.
Given the scale of that impact, we added alerting to ensure that reasoning traces are always preserved and forwarded correctly. This keeps the agent’s internal plan intact and prevent the performance regressions that occur when models are forced to “fill in the blanks” between tool calls.
#
Biasing the model to take action
In Cursor's default agent mode, you want the agent to autonomously read and edit files based on the user request. It can be frustrating when you tab away only to find that the agent was waiting to ask for your permission to proceed.
We’ve been experimenting with more specific instructions to help guide Codex:
Unless the user explicitly asks for a plan or some other intent that
makes it clear that code should not be written, assume the user wants
you to make code changes or run tools to solve the user's problem. In
these cases, it's bad to output your proposed solution in a message, you
should go ahead and actually implement the change. If you encounter
challenges or blockers, you should attempt to resolve them yourself.
In
Cloud Agents
, our async remote workflow, we make this language even stronger.
#
Message ordering
OpenAI models are trained to respect and prioritize message ordering. For example, the system prompt always takes precedence over user messages and tool results.
While this is helpful, it means we need to tune our harnesses to ensure the Cursor-provided prompt does not include instructions which could accidentally contradict user messages. Otherwise, Codex could get into a state where it does not want to comply with the user request.
For example, at one point we told Codex that it should take care to preserve tokens and not be wasteful. But we noticed that this message was impacting the model’s willingness to perform more ambitious tasks or large-scale explorations. Sometimes it would stop and stubbornly say,
I’m not supposed to waste tokens, and I don’t think it’s worth continuing with this task!
#
Looking forward
The pace of model releases is increasing. Our goal is to get the most out of every frontier model inside the Cursor agent harness. There’s more work to be done, and we’ll continue to share improvements we’re making to Cursor.
Filed under:
product
Author
:
Cursor Team
