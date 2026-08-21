---
type: x_post
source: https://x.com/ctatedev/status/2090865331862446088
author: "@ctatedev"
date: 2026-08-21
tags: [ai-agents, agent-tooling, web-development, vercel, developer-tools]
related: [entities/chris-tate, entities/vercel]
---

# Is Agentic — @ctatedev tweet

**Tweet (2026-08-21):** "Best part: https://is-agentic.com is itself agentic. Your agent can use it to make your site more agentic." (Quotes @vercel_dev.)

Chris Tate (Vercel) highlighting **Is Agentic by Vercel** — an AI-agent readiness score for websites, and the dogfooding twist that the scorer is itself usable by an agent.

## Is Agentic (is-agentic.com)
- **What:** "Score how ready a website is for AI agents, then get evidence and recommendations to improve it." Part of Vercel.
- **Usage:** `npx is-agentic [domain]`. Scores the public parts of a site that AI agents can **discover, access, understand, and use**. Every scan is run by **Ora** (ora.ai).
- **Scoring model:** "Essential checks" carry most of the score and cover fundamentals — server-rendered content, correct HTTP behavior, clear document structure, recoverable errors, usable controls. "Recommended checks" activate only when scan evidence shows the site offers an API, OAuth flow, GraphQL endpoint, MCP server, developer portal, or commerce surface. Non-applicable checks are excluded (not counted as failures), so a site isn't penalized for an interface it doesn't provide.
- **Sample scores:** is-agentic.com 100/100, vercel.com 89/100, ora.ai 90/100, eve.dev 63/100; openrouter.com 35/100, aistudio.google.com/docs 47/100, aws.com 53/100, autodesk.com 27/100.
- **Workflow advice:** start with failed Essential checks (the baseline an ordinary agent needs), then work through recommended checks.

## Sources
- Tweet: https://x.com/ctatedev/status/2090865331862446088
- Is Agentic: https://is-agentic.com
