---
title: "Introducing Warp Code: the fastest way from Prompt to Production"
source: "Warp Blog"
url: "https://www.warp.dev/blog/introducing-warp-code-prompt-to-prod"
scraped: "2026-05-10T01:27:46.520343+00:00"
lastmod: "2026-04-07T02:46:45.000Z"
type: "sitemap"
---

# Introducing Warp Code: the fastest way from Prompt to Production

**Source**: [https://www.warp.dev/blog/introducing-warp-code-prompt-to-prod](https://www.warp.dev/blog/introducing-warp-code-prompt-to-prod)

Product
Introducing Warp Code: the fastest way from prompt to production
Zach Lloyd
September 3, 2025
Today, we’re launching Warp Code — a suite of features for shipping agent-generated code all the way from prompt to production.
With
Warp Code
you get:
Top-rated coding agent:
#1 on Terminal-bench (52%) and top three on SWE-bench Verified (75.8%, scored with GPT-5) as of Sep 2nd 2025. We built the UI from the ground up to be the best experience for agentic coding.
Code review:
Review open changes, ask for modifications, and line-edit code diffs in a dedicated panel
Code editing:
A lightweight file viewing and editing experience in Warp with tabbed file viewing, a file tree, and syntax highlighting
Projects in Warp:
Initialize projects with their own WARP.md files (compatible with Agents.MD, Claude.MD and cursor rules). You can also define agent profiles to launch agents with different default settings, and global slash commands.
Demo of Warp Code features
Why we built Warp Code
In June, we launched
Warp 2.0, the Agentic Development Environment
. Our thesis: development is shifting from coding by hand to coding by prompt. The workflow of opening a file and hand-writing code is becoming obsolete. Instead, developers will start with a prompt – tell an agent to fix a bug, build a feature, debug a server crash in prod… and watch it work.
The vision resonated: since the ADE launch, we’ve seen faster growth than ever before in Warp’s history. We've onboarded hundreds of thousands of users, and revenue is up 30x this year.
I used to be sold on Cursor—after using Warp, I understand what the development flows of the future look like. Warp is unlike any other tool I’ve used, and I’ll never go back.
However, even as agents improve, there’s still a big gap in getting from prompt all the way to prod. Even the most powerful agents like Warp still benefit from the knowledge, context, and guidance of experienced engineers.
Too often agents write code that almost works, but has subtle issues that end up taking a lot of time to understand, debug, and commit.
66% of respondents cited "AI responses that are almost right, but not quite" as their biggest frustration with agentic coding. (
Stack Overflow 2025 Developer Survey, AI
)
The solution is not to back away from developing by prompt – instead it’s to improve the prompting workflow so that developers have more comprehension and control.
We call this process “agent steering” and our goal with Warp Code is to ship the most “steer”-able coding agent around.
What’s in Warp Code
Because of where Warp sits in the application stack compared to tools like Claude Code and Gemini CLI, we can offer a richer UX for steering agents. Features like code review and file editing support a tight feedback loop between developer and agent: prompt, review, edit, and ship.
Number one coding agent
Most importantly, we continue to improve the quality of our coding agent. We are #1 on Terminal-Bench, and continue to climb the leader board on SWE-bench Verified, now clocking in at 75.8%, which is #3 overall.
Since June, Warp’s SWE-bench Verified score has increased nearly 5%. The improvement is due to two key changes. First, we used GPT-5 high-reasoning as the primary model. GPT-5 high reasoning is available to all Warp users. Second, we made a lot of improvements at the app layer to optimize agents: to do lists, file editing, long-conversation management, and more.
Read more about the improvements
.
We’re excited to see Warp and GPT-5 set a new bar hitting 75.8% on SWE-Bench Verified. This milestone shows how far agentic coding has come, and how Warp is pushing the boundaries of what developers can achieve from prompt to production.
Our agent always includes access to the top models even as they change, and we will continue to improve the behind-the-scenes context and prompt engineering that makes Warp’s agent the most powerful around.
Code review
There are lots of code review products on the market, but Warp’s is unique because it is built for humans reviewing agent-generated code. In a world where agents write more and more code, we think this is the flow that actually matters most (not agents reviewing human generated code, although that’s cool too).
So in Warp, you can now view your agent’s changes as they are written, and steer the agent as it works. Our diff view works against your current branch or main and allows you to easily reprompt by referencing specific diffs and lines. It also allows hand editing right in the diff view.
All this saves you from having to context switch to Github just to see what an agent’s done. It increases your comprehension and makes it easier to ship correct, maintainable agent-generated code.
Native file editor
You can now open and edit files directly in Warp — complete with features like syntax highlighting, a tabbed file viewer, and find and replace (and, of course, vim keybindings).
The primary use case here is small edits to agent-generated code – because sometimes a hand-edit is faster than re-prompting; like when you just want to change a variable name, edit a bit of copy, or rewrite a small function.
We also shipped a simple file tree for browsing, opening, and adding files as context, as well as file opening and creation using the file palette (cmd-O).
We aren’t trying to rebuild an IDE here – we think the ADE approach is where things are headed. But, we do see the value in having just enough code editing capabilities to get an agent’s changes over the line.
Projects: WARP.md, slash commands, and agent profiles
You’ll notice a new zero state and welcome screen in Warp that allows you to quickly start new projects, navigate to existing ones or resume prior conversations. This makes it faster to get going on something new or pick up right where you left off.
If you’re starting a new project, Warp will set up for you with project rules and codebase indexing.
If you have an existing project, you can now run /init (and a host of other slash commands) to bootstrap it with a version-controlled WARP.md file. Warp also supports AGENTS.md, CLAUDE.md and Cursor rules.
Beyond /init, slash commands also allow you to quickly add global rules, MCP servers, and execute saved prompts. All of this makes agents much more context-aware and powerful.
Finally, we introduced Agent Profiles in this release, which let you specify a model + set of permissions for an agent. Profiles allow you to run different types of agents for different tasks with confidence the agent won’t do more than it's allowed to.
Suggested code diffs
We included one other special feature in the code launch, which is that our coding agent can now proactively suggest fixes so you don’t even need to invoke it.
If you have a compiler error or merge conflict, the agent just tries to fix it for you on the spot – you can always dismiss, reprompt, or start a conversation from the suggestion if you need to refine it.
Early feedback
A subset of Warp users have been testing Warp Code for weeks. Some early results from their testing include:
150M lines of code per week, 97% acceptance rate
Users have been generating over 150M lines of code each week in Warp. More exciting, over 97% of code diffs generated by Warp are accepted by end users.
1 hour saved each day
We surveyed our Warp Code users and learned that they save, on average one hour a day. 25% of respondents said Warp saved over two hours each day.
What comes next
Warp Code is just the beginning. We’re building for a future where Warp is the primary tool developers need to ship software, but there’s work to be done to get us there. In the coming months, look forward to product updates including:
Further editor improvements like LSP support, symbol navigation
More intelligent and streamlined code review
Remote environment support
To those who have been using Warp already, thank you for your role in our journey. For those joining with this launch, welcome to the community.
Give Warp Code a try, and let us know what you think.
Related articles
Apr 28, 2026  ·  7 min
Warp is now open-source
Warp is now open-source, and the community can participate in building it using an agent-first workflow managed by Oz, our cloud agent orchestration platform.
Apr 14, 2026  ·  2 min
Introducing Universal Agent Support: level up any coding agent with Warp
Warp now supports the most popular CLI coding agents — including Claude Code, Codex, Gemini CLI, and OpenCode — with vertical tabs, notifications, native code review, rich input, and remote control, making it the best terminal for multi-threaded agentic development.
Mar 24, 2026  ·  7 min
Build vs buy: how to deploy coding agents at scale
Should you build an in-house agent orchestration system or buy one off the shelf? Here's how to think about the decision and where the real complexity lies.
