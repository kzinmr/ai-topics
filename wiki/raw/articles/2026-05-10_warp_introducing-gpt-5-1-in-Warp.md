---
title: "Introducing support for GPT-5.1 in Warp"
source: "Warp Blog"
url: "https://www.warp.dev/blog/introducing-gpt-5-1-in-Warp"
scraped: "2026-05-10T01:27:41.422197+00:00"
lastmod: "2026-04-19T15:37:21.000Z"
type: "sitemap"
---

# Introducing support for GPT-5.1 in Warp

**Source**: [https://www.warp.dev/blog/introducing-gpt-5-1-in-Warp](https://www.warp.dev/blog/introducing-gpt-5-1-in-Warp)

Product
Introducing support for GPT-5.1 in Warp
Suraj Gupta
November 13, 2025
We’re excited to roll out support for OpenAI’s latest model, GPT-5.1, inside Warp. After weeks of testing, benchmarking, and tuning, GPT-5.1 has proven so capable that we’ve made it the default model for all new users starting today.
Under the hood of GPT-5.1
GPT-5.1 builds on what we liked about GPT-5. It's very smart and efficient, but notably GPT-5.1 is much faster due to adaptive reasoning. Under the hood, GPT-5.1 adjusts its reasoning automatically based on the complexity of your task. You still always get a smart answer, but you also usually get a much faster answer.
Here’s what stood out most in testing:
Latency:
GPT-5.1 consistently delivers faster results— 15% faster time to first token, and 40% faster task completion (measured on a subset of SWE-bench Verified)
Quality:
Maintains the high bar set by GPT-5
Deep debugging:
GPT-5.1 excels at root-causing and fixing tough, multi-layered problems. The kind that require tracing issues across files, dependencies, and environments.
Zach shows how GPT-5.1 performs on a real coding task.
Working with OpenAI
We worked closely with the OpenAI team to make sure GPT-5.1 performs well with Warp. This included optimizing prompt structure, tool definitions, and the balance between planning and execution. The collaboration helped us achieve a combination of speed, accuracy, and context awareness that feels natural inside the terminal.
Warp's collaboration and feedback has been invaluable in shaping GPT-5.1 to excel even more on coding. With significant gains in code quality, steerability, and speed, GPT-5.1 is performing exceptionally well inside Warp, and we’re thrilled to see it becoming the default experience for new users.
Try 5.1 in Warp
To give developers the chance to experience GPT-5.1 firsthand, we’re offering a limited-time promotion. Use the code
BUILD510
to get your first month of Warp Build for $5.10. The code is valid for the first 510 users.
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
