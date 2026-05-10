---
title: "GPT-5.2 Support in Warp & New Terminal-Bench Score"
source: "Warp Blog"
url: "https://www.warp.dev/blog/gpt-5-2-support-terminal-bench-improvement"
scraped: "2026-05-10T01:27:29.372243+00:00"
lastmod: "2026-04-19T15:37:21.000Z"
type: "sitemap"
---

# GPT-5.2 Support in Warp & New Terminal-Bench Score

**Source**: [https://www.warp.dev/blog/gpt-5-2-support-terminal-bench-improvement](https://www.warp.dev/blog/gpt-5-2-support-terminal-bench-improvement)

Product
GPT-5.2 Support in Warp & New Terminal-Bench Score
Suraj Gupta
December 11, 2025
Today we’re excited to roll out full support for OpenAI’s GPT-5.2 across Warp. After extensive benchmarking, tuning, and real-world stress testing, GPT-5.2 is now available to all Warp users, and it consistently delivers the best end-to-end coding performance we have seen yet.
Alongside the release, Warp’s agent achieved a new score on Terminal Bench 2.0, ranking #2 overall and setting a new high watermark for terminal-native agentic coding performance.
Under the Hood: Why GPT-5.2 Feels Different
GPT-5.2 improves across every dimension developers care about: planning, speed, reliability, and the ability to “close the loop” on complex tasks.
In testing, we saw several standout improvements:
Stronger planning with less guidance. In Warp’s planning mode, GPT-5.2 now proposes coherent multi-step approaches without requiring highly precise instructions, even for design or structural changes.
Closes the loop with higher reliability. Agents have long been able to verify their own changes, but GPT-5.2 makes this behavior significantly more reliable, reducing dead-ends and producing cleaner end-to-end workflows.
Fast execution. Lower latency and adaptive reasoning make interactions feel more fluid inside the terminal.
Parallel tool use. GPT 5.2 more intelligently uses parallel tool calling to improve the efficiency of open-ended search and multi-file edits.
Noticeably better UX. The team described GPT-5.2 as a smoother, more predictable interaction pattern compared to previous GPT-5 models.
Across the board, Warp’s agent became far more reliable at handling long-horizon tasks that require sustained reasoning and verification, a key ingredient in agentic development.
Warp's strongest Terminal-Bench Score
Paired with Warp, GPT-5.2 achieved a best-in-class score of 61.14% on Terminal Bench, marking Warp’s strongest performance to date.
This reflects not just raw model quality, but the depth of integration between Warp’s agent platform and OpenAI’s latest model.
Partnering with OpenAI
We partnered closely with OpenAI to optimize GPT-5.2 for Warp—fine-tuning prompt structure, tool definitions, and planning heuristics to balance speed, accuracy, and context awareness inside the terminal.
We’re thrilled to see Warp reach another best in class terminal bench score, hitting 61.14% with GPT-5.2! We love how Warp supports builders through the entire software development cycle and are excited to see them continue to push the frontier.
Try 5.2 in Warp
Give GPT-5.2 a try in Warp, we’re excited to hear your feedback!
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
