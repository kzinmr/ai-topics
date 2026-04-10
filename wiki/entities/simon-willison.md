---
title: "Simon Willison"
created: 2026-04-09
updated: 2026-04-10
tags: [person, blogger, hn-popular, ai-engineering, open-source, llm]
aliases: ["simonwillison.net"]
---

# Simon Willison

| | |
|---|---|
| **Blog** | [simonwillison.net](https://simonwillison.net) |
| **RSS** | https://simonwillison.net/atom/everything/ |
| **About** | [https://simonwillison.net/about](https://simonwillison.net/about) |
| **Social** | [@simonw](https://twitter.com/simonw), [GitHub](https://github.com/simonw) |
| **Newsletter** | Weekly (free), Monthly ($10 sponsor) |

## Bio

Simon Willison is an independent open-source developer focused on data journalism tools built around Datasette and SQLite. Co-creator of the Django Web Framework. Previously engineering director at Eventbrite (via acquisition of Lanyrd, Y Combinator 2010). Blogging about web development since 2002.

> "I send out a newsletter version of this blog once every week or so... At the end of every month I send out a much shorter newsletter to anyone who sponsors me for $10 or more on GitHub. It's intended to be a ten minute read that catches you up on the most important developments from the past month in LLMs and my other projects and research."

## Core Philosophy

### 1. Open Source as Public Infrastructure
Simon views open-source tools (Datasette, SQLite, llm) as shared public infrastructure that should be accessible, transparent, and community-driven. He actively builds and maintains over 500 projects on GitHub.

### 2. Agentic Engineering: AI as Collaborator, Not Replacement
From his Lenny's Podcast appearance (April 2026):

> "Agentic engineering is the practice of using AI agents as software engineering collaborators rather than just code completion tools."

Key aspects:
- AI agents should handle **complex multi-step work** (planning, execution, verification)
- **Human-in-the-loop** workflows where agents assist but humans direct
- Beyond code completion — agents as **thinking partners** in development

### 3. Pragmatic Tool Building
Simon's approach to AI is deeply practical — he builds tools to solve real problems, then shares them openly:

- **scan-for-secrets 0.3**: Secret scanning with redaction capabilities
- **asgi-gzip 0.3**: Extracted and maintained middleware from Starlette
- **llm CLI**: Unified interface for interacting with multiple LLM providers
- **GitHub Repo Size**: Simple tool addressing a common UI gap

> "GitHub doesn't tell you the repo size in the UI, but it's available in the CORS-friendly API."

### 4. AI Safety and Responsible Disclosure
Simon supports Anthropic's Project Glasswing approach:

> "Saying 'our model is too dangerous to release' is a great way to build buzz... but in this case I expect their caution is warranted."

He advocates for controlled rollout of powerful AI capabilities, particularly in cybersecurity, to allow industry preparation before proliferation.

### 5. Hands-On Research Methodology
Simon demonstrates empirical rigor in his technical analysis:

- **SQLite WAL in Docker**: Verified shared memory semantics experimentally
- **GLM-5.1 testing**: Ran actual prompts to verify SVG+HTML generation capabilities
- **Meta Muse Spark**: Analyzed 16-tool harness through direct interaction

## Recent Thought Evolution (2026)

### The Shift from AI Hype to Critical Assessment
Simon's content reveals a maturing perspective:

**Early 2026**: Enthusiastic about AI capabilities (GLM-5.1's impressive SVG generation)
**Mid 2026**: More nuanced, recognizing both power and risks (Project Glasswing support, AI safety concerns)

### Key Quotes and Positions

> "AI is destroying Open Source, and it's not even good yet." — *Discussing AI slop in open source projects*

> "The problem is the humans who review the code—who are responsible for the useful software that keeps our systems going—don't have infinite resources."

> "If you're running a personal weather dashboard or building a toy server for your Homelab, fine. But I wouldn't run my production apps—that actually make money or could cause harm if they break—on unreviewed AI code."

## Related Concepts
- [[agentic-engineering]]
- [[open-source-sustainability]]
- [[ai-safety-responsible-disclosure]]
- [[pragmatic-ai-development]]

## Sources
- [simonwillison.net/about](https://simonwillison.net/about)
- [Lenny's Podcast highlights](https://simonwillison.net/2026/Apr/2/highlights-from-lenny-podcast-agentic-engineering/)
- [Project Glasswing analysis](https://simonwillison.net/2026/Apr/7/project-glasswing/)
- [GLM-5.1 testing](https://simonwillison.net/2026/Apr/7/glm-51/)
- [AI destroying Open Source](https://simonwillison.net/2026/Apr/6/scan-for-secrets/)
