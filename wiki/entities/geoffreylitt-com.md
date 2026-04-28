---
title: "Geoffrey Litt"
tags: [person]
created: 2026-04-24
updated: 2026-04-24
type: entity
---

# Geoffrey Litt

**URL:** https://geoffreylitt.com
**Blog:** geoffreylitt.com
**Twitter/X:** @geoffreylitt
**Mastodon:** @geoffreylitt@mastodon.social
**Bluesky:** @geoffreylitt.com
**Current:** Engineer/Researcher @ **Notion**
**Previous:** Senior Researcher @ **Ink & Switch** | PhD in HCI @ **MIT** (Advisor: Daniel Jackson) | Panorama Education (YC S13)
**Newsletter:** https://buttondown.com/geoffreylitt

## Overview

Geoffrey Litt is a design engineer and researcher focused on **malleable software** — computing environments where anyone can adapt their tools to their needs with minimal friction. His work spans end-user programming, AI-assisted development, local-first software architecture, and dynamic documents.

After completing his PhD at MIT's Software Design Group under Daniel Jackson and spending five years at Panorama Education, Litt joined the independent research lab **Ink & Switch** as a senior researcher leading the Malleable Software track. In 2025, he published a landmark essay with collaborators arguing for software ecosystems that restore user agency in a world of locked-down applications. He now works at **Notion**, where he continues exploring the intersection of AI and end-user programming.

## Core Ideas

### Malleable Software: Restoring User Agency

Litt's central thesis is that modern software has become too rigid — we shape our workflows to match the available tools rather than molding our tools to the way we want to think. He defines malleable software as systems that allow users to dynamically customize interfaces and workflows with minimal technical barriers, enabling end-user programming without requiring advanced coding skills.

> "I work on malleable software: computing environments where anyone can adapt their software to meet their needs with minimal friction."

His 2025 essay with Ink & Switch argues that the "application" model is fundamentally flawed — software should be more like a physical workspace that can be rearranged to suit the inhabitant, not a prefabricated room you can only complain about to the landlord.

### AI HUDs Over AI Copilots

In "Enough AI copilots! We need AI HUDs" (July 2025), Litt made one of his most distinctive contributions to AI interface design. Drawing on Mark Weiser's 1992 critique of the "copilot" metaphor for AI, Litt argues that **Head-Up Displays** — interfaces that augment human perception and understanding — are often more valuable than interfaces that automate tasks.

> "Routine predictable work might make sense to delegate to a virtual copilot / assistant. But when you're in the thick of a complex problem, what you need is better perception, not delegation."

He demonstrated this with a custom debugger UI for a Prolog interpreter that Claude generated for him — rather than asking AI to write his code, he asked AI to build tools that made him a better programmer. This embodies his "code like a surgeon" philosophy: precision and deep understanding over automation.

### ChatGPT as Muse, Not Oracle

Litt is skeptical of treating AI as an authoritative source. His "ChatGPT as muse, not oracle" post advocates for using AI as a creative partner that generates possibilities, not as an oracle that provides answers. This connects to his broader view that **the human should remain in the loop**, maintaining understanding and agency even when using AI tools.

### Twitter as a Medium for Sketching

In a uniquely personal essay, Litt analyzed tweet threads as a "medium for sketching" — a tool for fluidly developing ideas in realtime. He identified three key properties:

1. **The right constraints** — Twitter's character limit prevents perfectionism and keeps ideas flowing
2. **Low barrier to starting** — Just click and type, no blog server setup
3. **Low barrier to finishing** — A single sentence is an acceptable unit of publication

> "Writing a blog can feel like a lonely one-way mirror. On Twitter, a sketch is understood to be incomplete, and that's the point."

This reflects his broader interest in **tools that support the thinking process itself**, not just the final output.

### Dynamic Documents as Personal Software

Through projects like **Potluck** (gradually enriching text documents into interactive applications) and **Embark** (dynamic documents for travel planning), Litt has explored how documents can evolve from static text into interactive, computational artifacts. The key insight: documents should be **live** — connected to data, computation, and other users — rather than frozen snapshots.

### Hackable Side-Project Tools

Litt practices what he preaches by building hackable personal tools. **Stevens**, his AI assistant built with a single SQLite table and cron jobs, exemplifies his philosophy: simple, transparent, modifiable. **Wildcard** lets users customize web apps using spreadsheets. These projects demonstrate that powerful tools don't need complex architectures — they need the right level of abstraction for the user.

### Local-First and Data Architecture

His technical work includes significant contributions to local-first software patterns:
- **Riffle** — Data-centric apps using a reactive relational database
- **Peritext** — CRDT implementation for async collaborative rich-text editing
- **Cambria** — Cross-app data compatibility via bidirectional lenses
- **Postgres BSON** — Extending PostgreSQL for faster JSON queries

The underlying theme: data should be portable, locally accessible, and resilient.

## Key Quotes

> "I work on malleable software: computing environments where anyone can adapt their software to meet their needs with minimal friction."

> "Enough AI copilots! We need AI HUDs."

> "ChatGPT as muse, not oracle."

> "Code like a surgeon."

> "The dream of malleable software: editing software at the speed of thought."

> "A tool that's molded to our needs like a leather shoe, not some complicated generic thing designed for a million users."

> "Writing a blog can feel like a lonely one-way mirror: release something into the world, maybe get a few comments back."

> "Twitter is a medium for sketching — for playing with ideas, on the fly."

> "The best framework is the one you don't need."

> "AI-enhanced development made me more ambitious with my projects."

## Recent Themes (2024–2026)

- **Malleable software manifesto** — Published comprehensive essay at Ink & Switch (June 2025) on restoring user agency
- **AI HUD design** — Arguing for perceptual augmentation over task delegation in AI interfaces
- **Custom tool generation** — Using AI to build personal development tools (debuggers, visualizers) rather than writing code
- **Notion-based AI workflows** — Introduced AI agent management via Notion Kanban boards (2026)
- **Dynamic documents** — Potluck and Embark projects exploring live, computational documents
- **Patchwork** — Version control for non-engineers (2024–2026)
- **Browser extension philosophy** — Advocating for extensions as the path to hackable software
- **Sketching as thinking** — Twitter threads, low-friction idea development, constraint-driven creativity
- **SQLite-first architecture** — Personal systems built on simple, transparent data stores

## Related

- [[concepts/ink-switch]] — Independent research lab where Litt led Malleable Software track
- [[concepts/daniel-jackson]] — PhD advisor at MIT; author of "The Day the World Went Quiet"
- [[concepts/malleable-software]] — Litt's central research area
- [[concepts/end-user-programming]] — The broader field Litt works within
- [[concepts/local-first-software]] — Software that prioritizes user data control and offline capability
-  — Conflict-free replicated data types; central to Peritext
-  — Ubiquitous computing pioneer; source of the HUD metaphor
- [[simon-willison]] — Fellow AI tooling enthusiast; Litt references his "yak-shaving intern" framing
- [[max-bernstein]] — Compiler engineer with complementary focus on systems-level tooling

## Sources

- "Malleable software: Restoring user agency in a world of locked-down apps" (Ink & Switch, 2025)
- "Enough AI copilots! We need AI HUDs" (geoffreylitt.com, July 2025)
- "AI-generated tools can make programming more fun" (geoffreylitt.com, December 2024)
- "ChatGPT as muse, not oracle" (geoffreylitt.com)
- "Stevens: a hackable AI assistant using a single SQLite table and a handful of cron jobs" (geoffreylitt.com)
- "How tweet threads cured my writer's block: Twitter as a medium for sketching" (geoffreylitt.com, 2020)
- "Malleable software in the age of LLMs" (geoffreylitt.com)
- "Foam: Software as Curation" (geoffreylitt.com)
- "Codifying a ChatGPT workflow into a malleable GUI" (geoffreylitt.com)
- "Browser extensions are underrated: the promise of hackable software" (geoffreylitt.com)
- Dialectic Podcast: "Software You Can Shape"
- Metamuse Podcast: "Bring your own client | Dynamic documents"
- Causal Islands 2023: "Dynamic Documents as Personal Software"
