---
title: "Tuning Deep Agents to Work Well with Different Models"
source: "https://x.com/i/article/2049535740233523600"
date: 2026-04-30
type: x_article
tweet_id: "2049535740233523600"
---

TL;DR: Deep Agents was previously designed in a generic way to work well across model families. Today we’re adding model-specific profiles to adjust prompts, tools, and middleware. This allows us to better conform to prompting guides specific to model families. We ship profiles for OpenAI, Anthropic, and Google models out of the box, which we see leads to a 10–20 point jump on a subset of tau2-bench over the default harness.
Until today, deepagents shipped with a single set of prompts, tools, and middleware aimed to work well across all Large Language Models. Builders could swap in different models or extend the harness with additional tools extensions to the system prompt. But the base prompts, tools, and middleware were fixed and not optimized per model.
As of today, we’re excited to launch harness profiles as a way to control these parameters on a per-model basis. This matters because:
Prompting guides differ per model. OpenAI's Codex Prompting Guide prescribes specific tool implementations and names (apply_patch, shell_command) that move the needle on Codex models. Anthropic's Claude prompting guidance emphasizes a different set of conventions. Even within a family, the Opus 4.6 → 4.7 migration guide flags prompt-level changes worth making.
Eval leaderboards show that the same model in a different harness can yield much different performance. Terminal-Bench 2.0 is the cleanest public example. The Claude Code harness ranks last among Opus 4.6 submissions.  We saw similar effects of careful harness engineering in previous work: Improving Deep Agents with harness engineering. Here we took gpt-5.2-codex from 52.8% to 66.5% on Terminal-Bench 2.0 (Top 30 → Top 5 at the time of publishing) just by applying harness layer changes like prompts and middleware hooks.
A single harness can't be optimal for every model. So we make it easy to support varying the harness per model.
How much does this matter?
Results on measuring the effect of profiles
In order to judge how much this matters, we measured performance on a subset of tau2-bench (multi-turn tool use + instruction following). We use a curated subset of more difficult tasks that frontier models haven’t yet saturated so we can better measure the impacts of harness level changes on agents.
 
What changed per model
We use the Codex and Claude prompting guides as the source for what changes we applied per profile.
For Codex the main changes included:
Tool changes: overriding the default file_edit implementation in deepagents with the recommended apply_patch tool, and aliasing the execute tool name in deepagents as shell_command
Prompt changes: largely around tool calling and planning using details from the prompting guide
Before any tool call, decide ALL files and resources you will need. Batch reads, searches, and other independent operations into parallel tool calls instead of issuing them one at a time.
For Opus the main changes were all prompting focused on tool usage and planning. For example, below are two snippets that were added to the prompt.
<tool_result_reflection>
After receiving tool results, carefully reflect on their quality and determine optimal next steps before proceeding. Use your thinking to plan and iterate based on this new information, and then take the best next action.
</tool_result_reflection>
<tool_usage>
When a task depends on the state of files, tests, or system output, use tools to observe that state directly rather than reasoning from memory about what it probably contains. Read files before describing them. Run tests before claiming they pass. Search the codebase before asserting a symbol does or does not exist. Active investigation with tools is the default mode of working, not a fallback.
</tool_usage>
Our takeaway is that exposing an interface for customizing the harness per model is a helpful primitive for builders to manage profiles per agent, version them, and easily test differences in configurations.
Try it today
To use this today, simply start using deepagents: uv add deepagents
