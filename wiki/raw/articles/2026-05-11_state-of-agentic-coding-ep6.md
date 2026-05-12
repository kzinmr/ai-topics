---
title: "State of Agentic Coding #6 — Armin Ronacher & Ben Vinegar"
created: 2026-05-11
author: Armin Ronacher (@mitsuhiko), Ben Vinegar (@bentlegen)
guest: Ben Vinegar
source: YouTube
url: https://youtu.be/JM1sIVIZYRg
type: talk
duration: "98:22"
tags: [coding-agents, agentic-engineering, software-engineering, prediction, platform, security, economics]
---

# Episode 6 Overview

Published May 11, 2026. Covers the AI pricing correction ("end of subsidies"), Pi's acquisition by Earendil, Cursor's acquisition by xAI, coding traces as training gold, the GitHub exodus movement, and a plea for principled products.

## Key Topics

### AI Engineer Europe and Miami Recap
- European attendees more grounded and older than expected — contrast with Miami's energy
- Armin and Cristina's talk on agentic coding at AI Engineer Europe

### RAM, SSDs, and the Rising Cost of Compute
- NVMe drive prices doubling, helium shortages affecting hard drive manufacturing
- Energy prices and prompt caching all driving infrastructure costs up
- Maxed-out 128GB+ Macs becoming entry-level for competitive agentic development

### AI Security Harnesses and Slop Vulnerabilities
- Tools like **Warden** and **Copyfail** finding real root-access vulnerabilities at scale
- AI-generated vulnerability reports may look like slop but deliver critical exploits
- Dismissing AI-output on stylistic grounds is a losing strategy when it works

### Enterprises Clamp Down on Token Spend
- "Companies don't want to spend $250,000 per engineer"
- OpenAI engineer's talk: "just don't worry about token spend" vs. Mario's efficiency-focused talk — **incentive misalignment between providers and users**

### The Beginning of the End of Subsidies
- Claude Code restricting Opus from cheaper plans
- SaaS products switching from seat-based to per-use pricing — bills multiplying 5x
- Downstream AI companies have no margins; inference providers have healthy ones
- The economics trap: users cycling out of products because agents can build alternatives in an afternoon

### Why Pi Got Acquired
- Armin's journey from Pi user to owner — acquired by **Earendil** (Armin's company)
- The long-game relationship with Mario, Pi's creator
- Pi as a responsible open-source coding harness
- Mario sharing Pi coding traces on HuggingFace to help open-weight models

### xAI, Cursor, and Why Traces Are Gold
- xAI/SpaceX acquires Cursor for ~$10B with $60B option — a **data-for-compute trade**
- Coding traces are the best RL training data: start with human input, contain iterative human feedback, mechanically verifiable reward signal (did the user commit?)
- Dangerous concentration of power: traces go to Anthropic and OpenAI by default
- Open-weight models locked out unless developers intentionally share traces

### GitHub Outages and Leaving the Platform
- Mitchell Hashimoto (Ghostty) quitting GitHub
- Former GitHub CEO raising funds for a competitor (Tangled.org, Pierre as alternatives)
- The paradox: Git won because of distributed version control, but GitHub won by being centralized

### History Lesson: How GitHub Won
- CVS → Subversion → Git/Mercurial battle → GitHub's social features as killer differentiator
- GitHub became the "centralized commercial service" that won distributed version control
- AI ecosystem's gravitational pull made leaving nearly impossible — until now

### Data Moats, Consent, and Training-Set Deals
- Old companies sitting on data treasure troves, selling to model labs
- Microsoft training on GitHub data with only "half a day of outrage"
- Societal numbness to data exploitation

### A Plea for Principled Products
- Ben: "I want the slow, painful, hard work to be rewarded, not the bullshit"
- Armin: hopes open-source LLMs win and copyrights become worth less
- The industrial revolution analogy: unsustainable capital expenditure for factories that couldn't forecast demand

## Key Quotes

> "This idea that we have to piggyback on top of GitHub, I think everybody's rejecting that increasingly. Companies don't want to spend $250,000 per engineer."

> "The incentives couldn't be any different between the providers and the users." — on OpenAI's "don't worry about spend" vs. Mario's efficiency message

> "I'm calling it the end of subsidies. It's not like truly the end... but it feels like the beginning of the end."

> "Coding traces are just great because they start with human input, they contain a little bit more human input, and they have a very easy to measure signal at the end: did the user commit?"

> "I want the slow, painful, hard work to be rewarded. Not the [bullshit]." — Ben's closing plea

## Connection to Wiki Concepts
- [[concepts/state-of-agentic-coding]] — Series overview, episode 6 addition
- [[concepts/harness-engineering]] — Traces as training data, Pi acquisition
- [[entities/pi]] — Acquired by Earendil, tracing sharing initiative
- [[entities/cursor]] — Acquired by xAI for $10B+
- [[concepts/agent-security]] — AI security harnesses finding real vulnerabilities
- [[concepts/subscription]] — End of subsidies, pricing model collapse
