---
title: "Introducing Warp: The Terminal for the 21st Century"
source: "Warp Blog"
url: "https://www.warp.dev/blog/introducing-warp-ai"
scraped: "2026-05-10T01:27:45.655350+00:00"
lastmod: "2026-04-24T14:39:41.000Z"
type: "sitemap"
---

# Introducing Warp: The Terminal for the 21st Century

**Source**: [https://www.warp.dev/blog/introducing-warp-ai](https://www.warp.dev/blog/introducing-warp-ai)

Product
Introducing Warp AI
Zach Lloyd
March 16, 2023
Today I’m excited to share
Warp AI,
AI that's built into the terminal to make you more powerful as you work. Currently in beta and available for free preview, Warp AI is available to try today in the latest version of Warp.
Download warp
Watch this demo video to see it in action:
The fastest way to become a terminal power user
The terminal is a powerful platform for all sorts of developer workflows – from building, running, and testing code, to interacting with your cloud or building internal tools. However, that power is hidden behind a notoriously difficult interface.
Traditionally, the way developers have mastered the tool is through some combination of Googling, Stack-Overflowing, and, in days past, leaning over the shoulders of other CLI experts, picking up their tips and tricks along the way. I remember this is how I learned
sed
– watching our tech lead instantly slice and dice user logs to find what I was looking for after I’d spent hours mucking around myself to no avail.
As of today, developers can master the terminal by asking Warp AI how to get stuff done.
AI as a core part of the terminal
The key advantage of Warp AI is the way it interacts with terminal inputs and outputs.  A typical loop starts with asking it to explain an error or suggest a fix from the command line.  When you get a response from Warp AI, you can run that AI-generated command without copy/paste or context switching.
Ask Warp AI to write you a script to connect to a cloud instance and you can run it directly without leaving the terminal. Ask Warp AI to install the latest version of postgres and it will walk you through each step, one command at a time.
Chat with Warp AI about how to complete a setup.
Because Warp groups outputs and inputs together as blocks, you can ask AI for help on a specific command's output. This is especially useful for errors, but it can also explain anything that a public terminal program is outputting that you don’t understand –
git, I’m looking at you
…
Ask Warp AI to suggest fixes for errors.
If you need to be more precise than a whole block, you can also feed any text selection directly into Warp AI.
Select a string of text. Ask Warp AI to debug.
Privacy and security
We realize that the terminal is a very sensitive environment and so we want to be explicit and transparent around what’s leaving your local machine when you use Warp AI.
Only what you explicitly enter into the Warp AI chat input ever leaves your computer. Since Warp AI is built on OpenAI, OpenAI’s servers will receive this input. We have not opted-in to allow OpenAI to train their models on this data.
Warp itself does not store any of this info and only passes it through our servers when we proxy requests to OpenAI.
What’s next?
While Warp AI is a powerful integration today, we can take it much further. We believe there are opportunities for AI to help both individuals and teams at work.
For example, one of the first things we plan to ship is a new AI command prediction feature using a local-first Bayesian model.
AI is so well suited to the terminal. It’s an extreme power tool whose limiting factor has always been that it’s hard to use well. It’s the perfect use case for a built-in AI assistant.
Available now in free preview
Warp AI is available today for all users as a free preview.  You can make up to 100 requests per day during this preview period.
In the future, this feature will be part of a paid plan, but for now we want to let you experience its power while we continue to tweak and improve the integration.
Please check it out and let us know how it goes in
our Discord
and
on Twitter.
 Download warp
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
