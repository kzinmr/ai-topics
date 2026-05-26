---
title: browser-use
type: entity
aliases:
- browseruse
- browser-use-oss
created: 2026-04-13
updated: 2026-05-11
tags:
  - entity
  - developer-tooling
  - browser-agent
  - open-source
status: active
sources:
- https://github.com/browser-use/browser-use
- https://browser-use.com
- https://www.fastaijobs.com/companies/browser-use
- raw/articles/2026-05-09_browser-use_production-architecture.md
---

# browser-use

**browser-use** is an open-source browser automation framework developed by ETH Zurich alumni. It enables AI agents to interact with websites via Playwright, with the mission "Make websites accessible for AI agents."

## Overview

| Item | Details |
|---|---|
| Founded | October 2024 (GitHub) |
| Founders | ETH Zurich alumni (MagMueller et al.) |
| HQ | Zurich / San Francisco |
| License | MIT |
| GitHub Stars | 87,300+ |
| Funding | $17M (Seed) |
| Team Size | 1-10 |
| Contributors | 310 |
| Release | v0.12.6 (April 2026) |

## Tech Stack

### Python (Main)
```python
from browser_use import Agent, Browser, ChatBrowserUse

browser = Browser()  # or use_cloud=True for cloud version
agent = Agent(
    task="Execute task in browser",
    llm=ChatBrowserUse(),  # optimized model
    browser=browser,
)
await agent.run()
```

### TypeScript (npm)
- Available since February 2026 (v0.6.0)
- Playwright-based, Node.js >= 18
- 10+ LLM providers supported (OpenAI, Anthropic, Google Gemini, Azure, AWS Bedrock, Groq, Ollama, DeepSeek, OpenRouter)

### Key Features
- **act / extract / observe**: Natural language browser operations
- **Cloud version**: Stealth browser, proxy rotation, scalable execution
- **Claude Code skill**: Direct integration via `~/.claude/skills/browser-use/SKILL.md`
- **MCP Server**: Operate from Claude Desktop via `npx browser-use --mcp`
- **Workflows**: RPA 2.0 patterns via `workflow-use`
- **macOS-use**: AI operation of Mac apps

### Benchmarks (In-House)
- ChatBrowserUse() is 3-5x faster on average (vs. other models)
- Open benchmark published for 100 real-world tasks

## Ecosystem

|| Repository | Description | Stars |
|---|---|---|
| browser-use | Core Python library | 86,454 |
| web-ui | Run AI agents in browser | 15,818 |
| workflow-use | RPA 2.0 workflows | 3,936 |
| macOS-use | Mac app operations | 1,884 |
| awesome-prompts | Prompt collection | 904 |
| vibetest-use | Automated QA testing | 785 |
| agent-sdk | Minimal agent architecture SDK | 661 |
| browser-harness | Self-healing browser harness | 4,200 |
| video-use | Video operation agent | 2,200 |

## Key People

- **Larsen Cundric** (@larsencc) — Founding Engineer. Designed the production architecture ([[concepts/browser-use-production-architecture]]) from 4,000+ commits of experience. Pioneered SQS-to-Lambda, continuation mechanisms, and S3 state management.
- **Gregor Zunic** — Founder. Author of "The Bitter Lesson of Agent Frameworks."

## Key Blog Posts

- [A Production Architecture for the Browser Use Open-Source Library](https://browser-use.com/posts/production-architecture-browser-use) (2026-05-09) — SQS-to-Lambda production architecture. → [[concepts/browser-use-production-architecture]]
- [Everything I Got Wrong in the Last 4,000 Commits](https://browser-use.com/posts/everything-i-got-wrong)
- [The Bitter Lesson of Agent Harnesses](https://browser-use.com/posts/bitter-lesson-agent-harnesses)
- [BUX: Your 24/7 Remote Agent](https://browser-use.com/posts/bux-launch-blog)
- [How We Built Secure, Scalable Agent Sandbox Infrastructure](https://browser-use.com/posts/two-ways-to-sandbox-agents)

## Philosophy: "The Bitter Lesson of Agent Harnesses"

In January 2026, founder Gregor Zunic published **"The Bitter Lesson of Agent Frameworks"** on his blog.

> *"The bitter lesson of agent harnesses. All the value is in the RL-trained model, not in 10,000 lines of abstraction."*

Core claims:
- Traditional frameworks fail due to "incomplete action spaces"
- **Inverse strategy**: Start with maximum capability, then restrict based on evaluation data
- Achieve near-complete action spaces via CDP + Browser Extension APIs
- Use "ephemeral tool" pattern for context management (keep only N most recent outputs)
- Explicit `done()` tool for termination detection
- Core agent loop is a simple for-loop. Retries, rate limiting, connection recovery are "ops" not agent

→ See [[concepts/agent-harnesses]]

## Significance of DOM-Based Approach

In contrast to Anthropic/OpenAI's screenshot-based approach, it **directly understands DOM structure** for operations:
- ✅ Fast, high reproducibility
- ✅ High coordinate accuracy
- ❌ Weak with dynamic UI, Canvas, SPAs
- ❌ Blocked by CAPTCHA/login walls

→ The 2026 trend is **hybrid** (DOM-first + vision fallback)

## Related Entities

- [[entities/anthropic-computer-use]] — Screenshot-based approach
- [[entities/openai-cua]] — OpenAI's Computer-Using Agent
- [[entities/browserbase]] — Reliable browser automation infrastructure
- [[concepts/death-of-browser]] — De-humanization trend of browsers
- [[entities/webmcp]] — Standardized agent-browser interaction

## Sources

- [GitHub: browser-use/browser-use](https://github.com/browser-use/browser-use)
- [browser-use.com](https://browser-use.com)
- [Browser Use Company Profile](https://www.fastaijobs.com/companies/browser-use)
