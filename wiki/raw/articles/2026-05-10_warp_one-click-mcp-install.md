---
title: "Introducing One-Click MCP Install"
source: "Warp Blog"
url: "https://www.warp.dev/blog/one-click-mcp-install"
scraped: "2026-05-10T01:27:57.348040+00:00"
lastmod: "2026-04-19T15:37:21.000Z"
type: "sitemap"
---

# Introducing One-Click MCP Install

**Source**: [https://www.warp.dev/blog/one-click-mcp-install](https://www.warp.dev/blog/one-click-mcp-install)

Product
Introducing One-Click MCP Install
Alanna Eybel
Pei Li
December 2, 2025
Warp now supports one-click MCP install for a simplified installation flow for MCP. You can install MCP servers from:
Shared MCPs from your team:
Anyone on your team can publish an MCP server, and Warp automatically redacts secrets before sharing. Teammates (or your second laptop) can install it instantly, only entering the values they personally need.
Warp’s curated list:
A built-in selection of popular MCP servers chosen based on what Warp users actually use. Install them directly—no config hunting, no JSON copying, no external docs.
Custom JSON configs:
The original flow remains unchanged for internal, experimental, or any server that isn’t shared or curated.
All three paths now live in one place, making MCP setup dramatically easier.
Collaboration and MCP
For teams this launch makes it easier to standardize processes and share knowledge. Admins can publish the MCP servers the team should rely on, ensuring every engineer starts with the same configuration and stays aligned when URLs, tokens, or versions change.
Developers can still add any servers. But now there’s a clear default path, cleaner onboarding, and a shared foundation that doesn’t depend on Slack threads or tribal knowledge.
When sharing, sensitive values in the env configuration will be automatically scrubbed and replaced with variables.
Using MCP
Check out the following walkthroughs to see examples of how to use MCP.
Get started
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
