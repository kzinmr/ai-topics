---
title: "Kyle Jeong"
type: entity
aliases:
  - kylejeong
  - "@kylejeong"
created: 2026-05-13
updated: 2026-08-02
tags:
  - person
  - browserbase
  - browser-agent
  - infrastructure
  - sandbox
  - agent-harness
  - context-engineering
status: L3
sources:
  - raw/articles/2026-05-11_kylejeong_firecracker-agent-infra.md
  - raw/articles/2026-05-18_browse-sh-browserbase_agent-skills-catalog.md
  - raw/articles/2026-06-03_kylejeong_browser-agent-harness.md
  - raw/articles/2026-07-17_kylejeong_what-is-cdp.md
  - https://kylejeong.com
  - https://browserbase.com
---

# Kyle Jeong

Kyle Jeong (@kylejeong) is a **Growth Engineer at [Browserbase](https://browserbase.com)** and a 2026 UCLA graduate (Mathematics & Computer Science). He writes about AI infrastructure, browser automation, and agent sandboxing, and has become a leading public explainer of the browser-agent harness stack.

## Background

- **Education**: UCLA, Mathematics & Computer Science (graduated June 2026; wrote about the $82,394 cost of his college experience)
- **Current**: Growth Engineer at Browserbase (building infrastructure for agents to access the web)
- **Past**: Kleiner Perkins Fellow, Engineer at Pace (web agents for insurance), founded VEST at UCLA (startup/builder community)
- **Notable projects**: Built a website tracking LA wildfires (40K users in a day), SalesBench (adaptive social intelligence benchmark)
- **Personal**: 21 years old, lives in San Francisco; wrestled NCAA D2 as a UCLA freshman; enjoys the gym, magic tricks, and house music

## Key Contributions

### Writing & Education

Kyle writes technical deep-dives that bridge infrastructure concepts with AI agent use cases:

- **"What is CDP (Chrome DevTools Protocol)?"** (July 2026) — The definitive explainer of the control surface behind browser agents: commands/events, sessions/targets, Site Isolation, flat mode, and why raw CDP is hard (state management, lifecycle tracking). "Humans talk to humans using english, programs talk to other programs using protocols, and agents talk to browsers using CDP."
- **"The great (fire)wall: how China's internet works"** (July 2026) — Networking explainer from a trip through China.
- **"I think college was worth the $82,394 it cost me"** (June 2026) — Personal essay on his UCLA experience, written the day he graduated.
- **"Why no one cares about your Twitter posts"** (June 2026) — Essay on distribution vs product in the AI era: "building things got cheap. Distribution didn't."
- **"The web wasn't built for agents, here's how we built a harness to make it work."** (June 2026) — His most significant technical contribution to date; the browser agent harness essay (see below).
- **"What is Firecracker, and why do all the Agent Infra companies care about it?"** (May 2026) — Explains Firecracker microVM architecture and why agent infrastructure companies (Browserbase, E2B, Daytona, Modal) need VM-level isolation for running untrusted code
- **"How we build Agents at Browserbase"** (April 2026) — Internal agent development practices at Browserbase
- **"Introducing BrowserEnv: Train browser agents on real websites"** (May 2026) — With Shubhankar Srivastava
- **"Browse.sh, a catalog of browser skills for the Agentic future"** (May 2026) — Launch article for Browse.sh, an open catalog of 100+ curated browser skills with Autobrowse system. Demonstrates 45% cost reduction on Craigslist ($0.22 → $0.12/run)
- **"Transformers, more than meets the eye"** (January 2026) — Transformer architecture explainer
- **"What on earth is Kubernetes?"** (December 2025) — Kubernetes fundamentals explainer
- **"What's the big deal about computer-use?"** (December 2025) — History and evolution of computer-use AI

### The Browser Agent Harness Essay (June 2026)

His most-cited piece, arguing the **browser agent harness** — not raw CDP — is what separates demos from production agents:

- **Harness = rebranded context engineering**: "An 'agent harness' is just rebranded context engineering," popularized by LangChain and operationalized by Claude Code (Read/Write/Edit/Bash + CLAUDE.md + skills + sandbox).
- **Four failures a raw model in a raw terminal hits**: (1) tools not shaped to pre-training knowledge, (2) context bloat, (3) no reasoning loop for accuracy, (4) no guardrails.
- **Four production problems raw CDP doesn't solve**: the DOM is adversarial input (prompt-injection vector), relearning site navigation wastes tokens, production browsers need identity (fingerprinting/captchas), and you can't show the model customer passwords (credential brokering).
- **The six-layer harness**: (1) security layer between DOM and model (parse → project → validate → prompt), (2) caching layer (page snapshots, action cache, skill cache), (3) identity layer (residential/mobile proxies, real fingerprints, captcha solving, signed agent identity), (4) credential brokering (harness holds secrets, agent gets short-lived tokens), (5) skill memory, (6) filesystem.
- **Decision tree**: credentials it can't see → harness; untrusted text → harness; many sites/times → harness; single sandboxed task → raw CDP (Autobrowse-style).
- **Claude Code analogy**: "A coding agent harness has Read/Write/Edit/Bash plus a sandbox plus a skill folder. A browser agent harness has simple primitives + an identity layer + a skill folder + a credential broker + a cache + a filesystem. Same shape, harder problem."

### Style

Kyle's writing is characterized by:
- Deep technical explanations made accessible
- Connecting infrastructure primitives (Firecracker, KVM, containers) to AI agent use cases
- Practical, hands-on perspective from working at an agent infrastructure company

## Related Pages

- [[entities/browserbase]] — Employer; Stagehand is the harness he writes about
- [[entities/browse-sh]] — Browse.sh browser skills catalog (launched by Browserbase)
- [[concepts/agent-harnesses]] — The broader agent harness philosophy his essay extends to browsers
- [[concepts/browser-agent/death-of-browser]] — Browser agent debates he participates in
- [[concepts/firecracker]] — Firecracker microVMs
- [[concepts/sandbox]] — AI agent sandboxing
- [[concepts/browser-use-production-architecture]] — Production browser agent architecture
- [[concepts/computer-use]] — Computer-use AI agents
- Context Engineering (concepts/context-engineering/) — The paradigm he argues harnesses rebrand

## Sources

- [kylejeong.com](https://kylejeong.com) — Homepage, blog, RSS
- [What is CDP (Chrome DevTools Protocol)?](https://www.browserbase.com/blog/what-is-cdp) (July 2026)
- [The web wasn't built for agents](https://www.browserbase.com/blog/what-is-a-browser-agent-harness) (June 2026)
- Raw articles in `wiki/raw/articles/` (2026-05-11, 2026-05-18, 2026-06-03, 2026-07-17)
