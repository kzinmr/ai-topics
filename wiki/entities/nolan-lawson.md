---
title: "Nolan Lawson"
created: 2026-05-26
updated: 2026-05-26
type: person
tags:
  - person
  - open-source
  - web-development
  - optimization
  - ai-agents
  - coding-agents
aliases:
  - nolanlawson
  - Read the Tea Leaves
social:
  github: nolanlawson
  mastodon: "@nolan@toot.cafe"
  blog: "https://nolanlawson.com"
  npm: "~nolanlawson"
  website: "https://nolanlawson.com"
role: "Web Developer, Open Source Contributor"
organization: "Socket (2025–present), formerly Salesforce (2018–2025), Microsoft Edge, Squarespace"
sources:
  - https://nolanlawson.com/about/
  - https://nolanlawson.com/2025/01/18/goodbye-salesforce-hello-socket/
  - raw/articles/2026-05-25_nolanlawson_using-ai-to-write-better-code-slowly.md
---

# Nolan Lawson

**Nolan Lawson** is a web developer and open-source contributor based in Seattle, known for his work on web performance, accessibility, offline-first architectures, and JavaScript framework design. He writes the long-running blog "Read the Tea Leaves" at [nolanlawson.com](https://nolanlawson.com).

## Background

- **Education:** University of Washington (linguistics, computational linguistics)
- **Career:** Squarespace → Microsoft Edge → Salesforce (2018–2025, 6 years) → Socket (2025–present)
- **Early focus:** NLP and machine learning; later pivoted to web frontend performance and standards
- **Blog:** Running for 14+ years through 6 different jobs, covering NLP, Android, and web development

## Notable Open Source Work

### Pinafore
Alternative web client for Mastodon, focused on speed and simplicity. A Progressive Web App (PWA) built with Svelte. ~1,000 stars on GitHub, maintained 2018–2023 before being marked unmaintained.

### PouchDB Contributions
Major contributor to [PouchDB](https://pouchdb.com), the JavaScript database that syncs with CouchDB. Created several ecosystem projects:
- **socket-pouch:** PouchDB over WebSockets using Engine.io
- **pouchdb-replication-stream:** Streaming replication for PouchDB

### 100+ npm Packages
Published over 100 packages on npm, spanning database adapters, Android libraries, and web tooling.

## Professional Work

### Salesforce (2018–2025)
- Performance team on UI Platform, working on **Lightning Web Components (LWC)** — Salesforce's internal JavaScript framework
- Modernized LWC architecture and improved its performance on js-framework-benchmark
- Worked as a paid open-source maintainer on LWC (open-sourced by Salesforce)
- Heavy involvement in the **Accessibility Object Model (AOM)** working group with Igalia, Microsoft, Apple
- Discovered and fixed CSS-related performance bottlenecks; filed browser bugs that improved CSS performance for all developers
- Identified widespread SPA memory leak patterns across the industry

### Socket (2025–present)
- Working on software supply chain security
- Colleagues include John-David Dalton and Feross Aboukhadijeh

## AI and Code Quality

In May 2026, Lawson published "[Using AI to Write Better Code More Slowly](https://nolanlawson.com/2026/05/25/using-ai-to-write-better-code-more-slowly/)," articulating a philosophy of using LLMs for quality rather than speed. Key contributions:

- **Multi-agent parallel bug review:** Orchestrating Claude sub-agents, Codex, and Cursor Bugbot simultaneously on each PR
- **Slow coding methodology:** Deliberately using AI to find bugs rather than generate code fast — a deliberate counterpoint to "vibe coding" and "slop cannons"
- **Advocacy for context clearing:** Waiting for all sub-agents to finish before doing independent review to prevent anchoring bias

His approach aligns with [[concepts/agentic-engineering]] and extends [[concepts/code-review-agents]] patterns into practical multi-agent workflows.

## Writing and Influence

Lawson's blog has been a consistent source of deep technical writing on:
- **Web performance** — CSS selectors, SPA memory leaks, browser internals
- **Web Components** — Shadow DOM, accessibility in web components, framework design
- **Open source sustainability** — Experiences as a paid maintainer, open-source at large companies
- **AI-assisted development** — Slow coding, multi-agent review, quality-first AI usage

## Related Entities

- [[concepts/agentic-engineering]] — Lawson's slow-coding approach is a methodology within agentic engineering
- [[concepts/code-review-agents]] — Multi-agent parallel review technique
- [[concepts/web-performance]] — Core area of Lawson's professional expertise
