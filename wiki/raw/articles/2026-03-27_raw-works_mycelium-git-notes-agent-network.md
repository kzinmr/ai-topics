---
title: "mycelium — an underground information network for agents"
source_url: https://raw.works/mycelium-an-underground-information-network-for-agents/
author: Raymond Weitekamp (@raw_works)
published: 2026-03-27
ingested: 2026-10-28
source_type: blog
tags: [raw, blog, git-notes, agent-memory, coding-agents, openprose, agent-native]
---

# mycelium — an underground information network for agents

**Author:** Raymond Weitekamp ([@raw_works](https://x.com/raw_works)) — RAW Works (raw.works)
**Published:** March 27, 2026
**URL:** https://raw.works/mycelium-an-underground-information-network-for-agents/

Over the last 2 days, we've stumbled upon a really powerful coding agent interaction pattern: **git notes as an underground information network**.

Git notes are both ubiquitous (part of git) and "invisible" (GitHub chose not to display them). This presents a very interesting communication channel for agents, who can now include rich details and discussions about the code without cluttering up the "visible" layer of the repo.

**mycelium** is my tool to make these interactions easier.

```bash
# agent arrives, reads what's known about a file
mycelium.sh context src/auth.ts

# agent works...

# agent leaves a note explaining what it did
mycelium.sh note HEAD -k context -m "Refactored retry logic. See warning on auth.ts."
```

Agents read notes on arrival. They leave notes on departure. The network grows.

The CLI makes it easy to link notes and git refs together — files, commits, directories, even edges between notes. Notes can have **kinds** (decision, warning, summary, context) and **edges** (depends-on, explains, warns-about) but the vocabulary is open. The tool tries to stay unopinionated about the actual workflow. From the SKILL.md: "That's the whole contract. How you work, what you build, how you talk to your user — that's your business. Mycelium just asks you to read the breadcrumbs and leave new ones."

mycelium is meant to be agent-native — load the SKILL.md into your agent framework and it teaches the convention. But it's just git & bash, so it works with any agent in any git repo.

```bash
curl -fsSL https://raw.githubusercontent.com/openprose/mycelium/main/install.sh | bash
```

Still wrapping my head around the consequences of this, and very curious to hear your thoughts.

P.S. — this is the foundation of some very cool tools I'm collaborating with OpenProse on.
