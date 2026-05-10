---
title: "Making AI usage more transparent"
source: "Warp Blog"
url: "https://www.warp.dev/blog/credits-transparency"
scraped: "2026-05-10T01:27:16.830391+00:00"
lastmod: "2026-04-19T15:37:21.000Z"
type: "sitemap"
---

# Making AI usage more transparent

**Source**: [https://www.warp.dev/blog/credits-transparency](https://www.warp.dev/blog/credits-transparency)

Product
Making AI usage more transparent
Zach Lloyd
October 10, 2025
We want every Warp user to get the most out of our agents. As part of that, we are always trying to make our agents more efficient, but also want to provide users with clear data on credit usage so they can build intuition and use our agents most effectively.
Whether you’re running quick commands, editing files, or orchestrating multi-agent workflows, our goal is to provide tools for you to understand how those actions translate into credit usage.
Today, we are announcing a few updates designed to make AI usage in Warp more transparent, predictable, and efficient. Some are product improvements, others are messaging updates to make our credit system more comprehensible.
From Requests to Credits
First, we’ve updated our terminology to be more familiar and intuitive. Instead of “
requests
,” we now use the term “
credits
.”
Most developers already think in terms of credits when using APIs and developer platforms, so this shift makes it easier to understand and track AI usage in Warp. There’s no product change here – just a change in how we talk about usage.
Warp’s requests have already functionally been “credits” for some time – we recommend checking out this
post
on how they work.
Credit transparency in the UX
Developers can now see a clear, high-level breakdown of their AI usage directly in Warp, helping them build intuition on how to get the most out of Warp’s agents.
1. Conversation AI usage summaries
Each conversation now includes an inline footer summarizing how many credits were used, the context window consumed, which tools and models were invoked, relative model cost indicator, and the diffs or commands executed.
Harry gives a demo on the conversation AI usage summaries in the footer of each conversation.
2. Billing page conversation AI usage summaries
The billing page will soon aggregate your total credit usage across all conversations, making it easy to spot patterns and trends over time.
You’ll be able to see which workflows are more credit-intensive and which are more efficient, for example, when larger context windows or multi-agent actions are involved. This visibility gives developers both a quick snapshot and the ability to drill down into details, helping them make smarter choices about how they work.
These updates will roll out in the coming weeks, and we look forward to hearing your feedback.
Improving Agent Efficiency
As part of these transparency updates, we're also beginning to roll out improvements to how Warp's agents manage credit consumption. In the latest Warp release, you'll see two new
Auto
models in the model selector designed to balance performance and credit usage.
Auto (Performance)
optimizes for the highest quality output and selects the best available model for each request. It may consume credits faster, but delivers the most advanced results.
Auto (Efficient)
extends your credits further by using more resource-conscious model selections while maintaining strong output quality.
Both Auto models work well across all agent tasks - from coding to command generation - and help you choose the balance that best fits your workflow.
We'd love to hear what you think. Let us know any feedback at feedback@warp.dev or in our
Slack community
.
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
