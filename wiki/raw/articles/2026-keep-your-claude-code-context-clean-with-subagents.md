---
title: "Keep your Claude Code context clean with Subagents"
created: 
author_id: ""
tweet_id: "2048486242321662189"
source: x_article
---

# Keep your Claude Code context clean with Subagents

Long Claude Code sessions get messy fast. Every grep, find, and ls stays in your context, taking up space you'll never read again. Subagents fix this: they run work in their own window and return only the result.
This article goes straight to the point: what subagents are, how to create one, the built-ins that ship with Claude Code, and how to fork the context with CLAUDE_CODE_FORK_SUBAGENT=1
What is a subagent
A subagent is a specialized assistant that runs in its own context window, with its own system prompt, tools, and permissions. 

The main agent calls it, the subagent does the work in isolation, and returns a summary.
 
You create one with a Markdown file and frontmatter:
 
Claude Code picks it up automatically and invokes it when the description matches the task.
Where subagents live
You can save the file in different locations depending on scope. When two subagents share the same name, the higher-priority location wins.
 
For most cases you'll use .claude/agents/ (check it into version control, share with your team) or ~/.claude/agents/ (personal, available everywhere).
 
The problem: one window for everything
Without subagents, the main agent does it all in a single context. You ask it to review a controller, find a pattern, validate something. It fires grep, find, ls, glob, cd, more grep, another find, every call stays in your context.
 
Thirty minutes in, you have 80k tokens of noise you'll never read. 
When Claude compacts the context, that information gets flattened. Important details get lost in the summary
 
Built-in subagents: Explore and Plan
Claude Code ships with subagents for the common cases. The two you'll use most:
Explore: searches the codebase without polluting your main context. Fires all the grep and find calls in its own window and returns only the relevant findings.
Plan: investigates and produces an implementation plan. Reads files, understands the architecture, and returns a step-by-step doc. Your main context never sees the intermediate reads.

The flow looks like this:
 
Instead of 50 tool calls in your window, you get 3 lines with the answer. The rest is discarded.
 
Forking the context: 
By default, a subagent starts with a blank context. Good for cleanliness, bad when you've already invested 100k tokens building understanding of your codebase and you want the subagent to inherit all of it.
 
Forking solves that: the subagent starts with an exact copy of the parent's context at the moment of the fork.
export CLAUDE_CODE_FORK_SUBAGENT=1
How it works
Once CLAUDE_CODE_FORK_SUBAGENT=1 is set, every subagent spawn inherits the full parent context by default.
You can also fork on demand with the /fork slash command:
 
The fork's tool calls stay isolated, only its final result lands back in your conversation.
 
The forked subagent:
Inherits the parent's full conversation at fork time
Shares the prompt cache prefix with the parent (children 2-N are ~10x cheaper on input tokens)
Runs in isolation, its tool calls don't pollute the parent
Returns only the final summary
See it in real time: context-timeline hook
Tracking the main agent's context and the subagents running in parallel is hard to follow from the console. I built a hook to fix this: context-timeline.
Link: https://www.aitmpl.com/component/hook/monitoring/context-timeline
 
Install:
 
What it does: starts the moment you open a session and shows a timeline with the main agent's context window and how subagents start working in their own separate context. 
Every subagent you have running shows up in real time, along with the context it returns to the main agent when it finishes.

