---
title: Geoffrey Litt
handle: "@geoffreylitt"
created: 2026-04-10
updated: 2026-04-10
tags:
  - person
  - ai
  - end-user-programming
  - malleable-software
  - dynamic-documents
  - local-first
  - crdt
  - notion
---


# Geoffrey Litt (@geoffreylitt)

| | |
|---|---|
| **X** | [@geoffreylitt](https://x.com/geoffreylitt) |
| **Blog** | [geoffreylitt.com](https://www.geoffreylitt.com) |
| **GitHub** | [geoffreylitt](https://github.com/geoffreylitt) |
| **Role** | Researcher (formerly at Ink & Switch; now at Notion) |
| **Known for** | Malleable software, Potluck, Riffle, Wildcard, dynamic documents |
| **Bio** | Geoffrey Litt is a researcher and builder focused on making software more malleable — environments where anyone can adapt their tools to meet their needs. He was a senior researcher at Ink & Switch, where he led projects like Potluck, Riffle, Wildcard, and the malleable software essay series. He holds a PhD in HCI from MIT (advised by Daniel Jackson), previously worked at Autodesk Research, and now works at Notion. |

## Overview

Geoffrey Litt is one of the most thoughtful voices on **malleable software** — the idea that computing environments should let users adapt, reshape, and extend their tools with minimal friction. This vision stands in contrast to the modern software paradigm where users are locked into prefabricated applications and can only shape their workflows around what developers have anticipated.

His career spans academic HCI research and independent lab work. He completed a PhD at MIT's Computer Science department under Daniel Jackson, where his work focused on programming interfaces and dynamic documents. Before that, he worked at Autodesk Research on creative tools. Since 2019, he has been a core researcher at **Ink & Switch**, an independent research lab exploring the future of computing. At Ink & Switch, Geoffrey led or co-led several landmark projects including Potluck, Riffle, Wildcard, and the comprehensive "Malleable Software" essay. In 2024–2025, he transitioned to Notion, where he continues to work on making productivity software more flexible and user-adaptable.

Geoffrey's writing has been particularly influential in shaping the discourse around AI and end-user programming. His March 2023 essay "Malleable Software in the Age of LLMs" was one of the first comprehensive articulations of how large language models could fundamentally change the relationship between users and software — not just as chatbot interfaces, but as engines for generating and modifying personal tools. His "Code like a surgeon" essay and the "AI HUDs" concept have been widely discussed in the developer tooling community.

## Core Ideas

### Malleable Software

Geoffrey's central thesis is that **software should be malleable** — users should be able to reshape, adapt, and extend their computing environments to match their specific needs, rather than being constrained by rigid application boundaries. In the 2025 Ink & Switch essay "Malleable Software: Restoring User Agency in a World of Locked-Down Apps," he and co-authors (Josh Horowitz, Peter van Hardenberg, and Todd Matthews) articulate this vision:

> *"These days, we spend much of our time in software spaces that are — ironically — less flexible than our physical environment. Software is shipped to us as prefabricated applications built by developers far away. When we wish something worked differently, we can only submit feedback and work around the issue. We shape our workflows to match the available tools, rather than molding our tools to the way we want to think."*

The malleable software vision includes several key principles:
- **Universal version control** for all user artifacts, enabling safe experimentation and rollback.
- **Live collaboration** across different tools working on shared data.
- **Gradual enrichment** — starting with free-form text and progressively adding structure, interactivity, and automation.
- **AI-assisted development** within the malleable environment, where generated code inherits the platform's persistence, collaboration, and composition capabilities.

### Dynamic Documents as Personal Software

A key exploration in Geoffrey's work is the concept of **dynamic documents** — artifacts that start as ordinary text or notes but can be gradually enriched with computation, interactivity, and structured data. Projects like **Potluck** (2022) and **Embark** (2023) demonstrate this vision:

- **Potluck** let users write notes in any format, then define detectors to parse meaningful structure from the text and add interactive behaviors. For example, a recipe could gain a scaling slider and cooking timers. The key insight was that users could represent information with any text syntax they found natural, rather than being forced into rigid form structures.

- **Embark** extended this to travel planning, where informal notes could be progressively enriched with live data, maps, itineraries, and collaborative features.

As Geoffrey noted: *"A malleable environment can also provide platform capabilities that make AI-generated software more useful. For example: we have an interface for making small software tools from an AI chat. While this UI superficially resembles existing products like Claude Artifacts, the generated tools gain capabilities from existing inside of Patchwork. They automatically support persistence and multi-user collaboration, and can compose with existing tools for editing existing data."*

### LLMs and End-User Programming

In his influential March 2023 post "Malleable software in the age of LLMs," Geoffrey argued that large language models would represent a step change in tool support for end-user programming:

> *"All computer users may soon have the ability to author small bits of code. What structural changes does this imply for how we think about software?"*

His key arguments:
- **LLMs lower the barrier** to writing and modifying code, making it feasible for non-programmers to customize their tools.
- **The interaction model matters** — chat is one option, but malleable environments that produce spreadsheets, GUIs, or other structured outputs can be more useful for many tasks.
- **Iterative refinement is essential** — software created with LLM assistance must be tweakable by the user after generation. The model shouldn't just create a solution; it should teach the user how to create it themselves next time.
- **Platform context amplifies AI** — AI-generated tools gain additional value when they inherit platform capabilities like persistence, collaboration, and composition with existing tools.

### AI HUDs Over Copilots

Geoffrey has been a vocal advocate for **AI HUDs** (Heads-Up Displays) as an alternative to the chat-centric copilot paradigm. In his post "Enough AI copilots! We need AI HUDs," he argues that AI should provide contextual, glanceable information and suggestions integrated into the user's existing workflow — rather than requiring users to switch to a chat interface.

This connects to his broader theme of malleability: AI should augment the tools users already have and love, not replace them with a new interaction paradigm. His "Is chat a good UI for AI? A Socratic dialogue" essay explores this question in depth, weighing the trade-offs between conversational interfaces and structured tool manipulation.

### Code Like a Surgeon

In "Code like a surgeon," Geoffrey advocates for a more precise, targeted approach to AI-assisted coding. Rather than asking AI to generate entire programs from scratch, users should use AI as a precision tool — identifying specific lines or sections that need modification and requesting surgical changes. This approach preserves the user's understanding of the codebase while leveraging AI for the tedious or complex parts.

### Bring Your Own Client

In "Bring Your Own Client," Geoffrey explores how local-first software and malleable environments enable users to choose their own interfaces for accessing and manipulating data, rather than being locked into a single application's UI. This connects directly to his work on **Riffle**, a reactive relational database designed for building local-first data-centric applications.

## Key Work

### Research Projects

- **Potluck** (Ink & Switch, 2022) — Dynamic documents as personal software. Users enrich text notes with interactive behaviors (scaling, timers, etc.) using a formula language. AI can draft detectors and computations. Explored how gradual enrichment of informal text can lead to structured, interactive tools.
- **Embark** (Ink & Switch, 2023) — Dynamic documents for travel planning. Extended Potluck concepts to a specific domain, showing how informal travel notes can be progressively enriched with live data, maps, and itineraries.
- **Riffle** (Ink & Switch, 2021) — Building data-centric apps with a reactive relational database. A local-first database designed to make it easier to build applications that work offline and sync when connected.
- **Wildcard** (Ink & Switch, 2020) — Customize a web app with a spreadsheet. Demonstrates how users can extend web applications by linking them to spreadsheet-like data structures.
- **Patchwork** (Ink & Switch, 2024–2026) — Version control software for writers, developers, and other creatives. Builds on Automerge CRDTs to support live collaboration on both data and code. Enables AI-generated tools to inherit persistence and multi-user capabilities.
- **Peritext** (Ink & Switch) — A CRDT for rich text, enabling async collaborative writing with fine-grained formatting support.
- **Cambria** (Ink & Switch) — Better cross-app data compatibility using bidirectional lenses. Enables data migration and schema evolution across malleable applications.
- **Ambsheets** (Ink & Switch, 2025) — Research project exploring spreadsheet-like interfaces augmented with AI capabilities.

### AI Assistant Projects

- **Stevens** — A hackable AI assistant built using a single SQLite table and a handful of cron jobs. Demonstrates Geoffrey's philosophy of simple, transparent, user-modifiable AI tools over black-box platforms.
- **Fuzzy API Composition** — Querying NBA stats with GPT-3 + Statmuse + LangChain. Early exploration of composing multiple APIs with LLM assistance for dynamic data queries.
- **Codifying a ChatGPT workflow into a malleable GUI** — Turning a conversational AI workflow into an interactive, persistent application.

### Blog Posts & Essays

| Date | Title | Topic |
|------|-------|-------|
| 2025 | Code like a surgeon | Precision AI-assisted coding; surgical edits over wholesale generation |
| 2025 | AI as teleportation | Metaphor for how AI changes the nature of computational work |
| 2025 | Enough AI copilots! We need AI HUDs | Alternative interaction models for AI integration |
| 2025 | Is chat a good UI for AI? A Socratic dialogue | Deep exploration of conversational vs. structured AI interfaces |
| 2025 | Stevens: a hackable AI assistant using SQLite and cron | Simple, transparent, user-modifiable AI tools |
| 2025 | AI-generated tools can make programming more fun | Malleable environments for AI-generated code |
| 2024 | Your pie doesn't need to be original (unless you claim it so) | Philosophy on originality and derivative work in software |
| 2023 | Malleable software in the age of LLMs | How LLMs change end-user programming dynamics |
| 2023 | ChatGPT as muse, not oracle | Using LLMs for creative inspiration rather than authoritative answers |
| 2023 | Dynamic documents // LLMs + end-user programming | Combining document malleability with AI assistance |
| 2023 | Bring Your Own Client | Local-first software and user-chosen interfaces |
| 2023 | How tweet threads cured my writer's block | Twitter as a medium for sketching ideas |
| 2022 | Foam: Software as Curation | Curation as a software paradigm |

### Academic & Conference Work

- **PhD in HCI, MIT** (advised by Daniel Jackson) — Research on programming interfaces, dynamic documents, and end-user software engineering.
- **Dynamic Documents as Personal Software** (Causal Islands 2023) — Keynote presentation on the vision for dynamic documents augmented with AI.
- **Margin Notes** — Automatic code documentation with recorded examples from runtime.
- **Ladybug** — A Ruby debugger backend for the Chrome DevTools UI.
- **Experiments in Dynamicland** — Exploring the dynamic medium concept at Bret Victor's research lab.
- **ENHANCE!** (BangBangCon 2017) — Explaining Generative Adversarial Neural Networks using CSI-style image upscaling.

## Blog / Recent Posts

| Date | Title | Summary |
|------|-------|---------|
| 2025 | Code like a surgeon | Advocates for precision AI-assisted coding — using AI for targeted edits rather than wholesale generation. Preserves user understanding while leveraging AI for complex parts. |
| 2025 | AI as teleportation | Explores the metaphor of AI as teleportation — moving computation and creativity across boundaries rather than generating from scratch. |
| 2025 | Enough AI copilots! We need AI HUDs | Argues for heads-up display style AI integration over chat-based copilots. AI should augment existing workflows, not replace them. |
| 2025 | Is chat a good UI for AI? | Socratic dialogue exploring the trade-offs between conversational and structured AI interfaces for different tasks. |
| 2025 | Stevens: a hackable AI assistant | Demonstrates building an AI assistant using SQLite and cron jobs — emphasizing transparency and user modifiability. |
| 2024 | Codifying a ChatGPT workflow into a malleable GUI | Converting a conversational AI workflow into an interactive, persistent application with editable components. |
| 2023 | Malleable software in the age of LLMs | Seminal essay on how LLMs represent a step change in end-user programming capabilities. |

## Related People

- **[[Simon Willison]]** — Fellow thinker on AI tooling and practical applications; both explore how LLMs can augment existing workflows rather than replace them.
- **[[Hamel Husain]]** — Both advocate for transparent, hackable AI tools over black-box platforms; share interest in practical developer tooling.
- **Peter van Hardenberg** — Ink & Switch collaborator; co-author on the Malleable Software essay.
- **Josh Horowitz** — Ink & Switch collaborator; co-author on the Malleable Software essay.
- **Todd Matthews** — Ink & Switch collaborator; co-author on the Malleable Software essay.
- **Daniel Jackson** — PhD advisor at MIT; known for work on software design and formal methods.
- **[[Mark Saroufim]]** — Both interested in making AI tools more accessible and hackable for developers.
- **Bret Victor / Dynamicland** — Geoffrey conducted experiments in Dynamicland's research environment exploring dynamic media.

## X Activity Themes

Geoffrey's X activity (@geoffreylitt) centers on:

1. **Malleable Software** — Sharing ideas, prototypes, and essays about making software more adaptable and user-extensible.
2. **AI Interaction Design** — Critiquing current AI product paradigms (especially chat-based interfaces) and proposing alternatives like HUDs, dynamic documents, and surgical editing.
3. **End-User Programming** — Advocating for tools that let non-programmers customize and extend their computing environments.
4. **Local-First Software** — Promoting architectures where user data and computation happen locally, with optional cloud sync.
5. **Developer Tooling Philosophy** — Essays and threads on how AI should augment rather than replace existing developer workflows.
6. **Ink & Switch Research** — Sharing prototypes, findings, and essays from the lab's research into the future of computing.
7. **Notion & Productivity Software** — Discussing ideas around making productivity tools more flexible and user-adaptable.
