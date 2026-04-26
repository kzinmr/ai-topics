---
title: Mitchell Hashimoto
type: entity
handle: "@mitchellh"
created: 2026-04-13
updated: 2026-04-14
depth: 22000
status: L3
tags:
  - person
  - x-account
  - ai
  - agentic-engineering
  - harness-engineering
  - ghostty
  - zig
  - hashicorp
  - terraform
  - terminal-emulator
  - building-block-economy
  - libghostty
  - vibe-coding
sources: []
---


# Mitchell Hashimoto

| | |
|---|---|
| **X/Twitter** | [@mitchellh](https://x.com/mitchellh) |
| **Blog** | [mitchellh.com](https://mitchellh.com/writing/) |
| **GitHub** | [mitchellh](https://github.com/mitchellh) |
| **Role** | Co-founder of HashiCorp; creator of Ghostty terminal emulator |
| **Known for** | Terraform, Vagrant, Packer, Vault; "Harness Engineering" terminology; Ghostty terminal |
| **Bio** | Infrastructure engineer and entrepreneur who built the tools powering modern cloud infrastructure. Co-founded HashiCorp (Terraform, Vault, Consul, Nomad, Packer), which went public in 2021. Now focused full-time on Ghostty, a next-generation terminal emulator written in Zig. Pioneered the term "Harness Engineering" for the practice of building systematic prevention mechanisms around AI agent mistakes. |

## Overview

Mitchell Hashimoto is one of the most influential infrastructure engineers of the modern era. As co-founder of HashiCorp (with Armon Dadgar), he built **Terraform** (downloaded 100M+ times), **Vagrant**, **Packer**, **Vault**, **Consul**, and **Nomad** — the foundational tooling stack for cloud-native infrastructure. After HashiCorp's IPO in 2021, Mitchell stepped back from executive duties to focus on building software, creating **Ghostty** — a terminal emulator written from scratch in Zig.

In **February 2026**, Mitchell crystallized a concept that would reshape how the industry thinks about AI-assisted development. In his blog post ["My AI Adoption Journey"](https://mitchellh.com/writing/my-ai-adoption-journey), he coined the term **"Harness Engineering"**:

> "I don't know if there is a broad industry-accepted term for this yet, but I've grown to calling this 'harness engineering.' It is the idea that anytime you find an agent makes a mistake, you take the time to engineer a solution such that the agent never makes that same mistake again."

A few days later, OpenAI published their own "Harness engineering" field report, and the term spread across the industry. Ryan Lopopolo at OpenAI had independently arrived at the same concept from the enterprise direction. Martin Fowler subsequently endorsed it on LinkedIn:

> "Harness Engineering is a valuable framing of a key part of AI‑enabled software development. Harness includes context engineering, architectural constraints, and garbage collection."

## Core Ideas

### Harness Engineering — Systematizing Agent Improvement

Mitchell's definition is elegant and practical: **every agent mistake becomes a permanent system improvement**.

> "I'm making an earnest effort whenever I see an agent do a Bad Thing to prevent it from ever happening again."

This differs from prompt engineering (improving instructions) and context engineering (improving information):
- **Prompt engineering**: "How do I ask better?"
- **Context engineering**: "What does the agent need to know?"
- **Harness engineering**: "How do I build a system that prevents this class of error forever?"

The harness includes:
- Custom linters and validators for agent-generated code
- AGENTS.md rules accumulated from past mistakes
- CI/CD guardrails that catch agent-specific failure modes
- Structured feedback loops that turn agent mistakes into training data
- Architectural constraints that make certain errors impossible

### Building Block Economy — Software Composition in the AI Era

Mitchell's April 2026 essay articulates a fundamental shift in how software should be built when AI agents are the primary consumers:

> "The most effective way to build software and get massive adoption is no longer high quality mainline apps but via building blocks that enable and encourage others to build quantity over quality."

Key insights:
- **AI as assembly layer** — Agents excel at gluing together proven, well-documented components rather than building from scratch
- **Outsourced R&D** — Maintainers observe working PoCs in the wild and cherry-pick the best ideas for mainline
- **Reduced maintenance burden** — Provide the means to production, not the final product; easier to decline feature requests
- **Open source advantage** — "Agents will more readily pick open and free software over closed and commercial"

### Anti-Slop Pattern — Human-in-the-Loop Quality Control

From the "Vibing a Non-Trivial Feature" post, Mitchell demonstrates a critical pattern:

1. **Plan first** — Create a comprehensive plan interactively with an agent, save to spec.md
2. **Execute via agent** — Let the agent fill in the details (Scaffold + TODO pattern)
3. **Anti-slop session** — When agent gets stuck, step back, manually restructure, force deep understanding
4. **Final manual review** — "Never ship AI-written code without a thorough manual review"

This pattern ensures quality while maximizing the benefits of AI assistance. Mitchell's rule: **never ship code you don't understand**.

### Transcription as External Memory

Mitchell uses Wispr Flow (voice transcription) to narrate his thought process while coding, creating a searchable log of design decisions. This compounds over time as a form of "external working memory" that bridges sessions and prevents knowledge loss.

### On Diminishing Returns in LLM Progress

> "I don't see life-changing improvements anymore. The delta between models is getting smaller. You notice it, but it's not the same leap we saw before."

The biggest gains now come from **workflow design** rather than model capability. Being able to consult a slower, more expensive model on demand rather than paying that cost for every little thing — that's where the real leverage is.

### The 6-Step AI Adoption Journey

Mitchell documented his systematic path from AI skeptic to productive agent user:

**Step 1: Drop the Chatbot**

> "Immediately cease trying to perform meaningful work via a chatbot (e.g. ChatGPT, Gemini on the web, etc.). Chatbots are inherently stateless, lack tool access, and force you to be the runtime."

His first experience trying to code with a chatbot was typical: "I got a color palette that ships for macOS in Ghostty today that is only very lightly modified from what Gemini produced for me in one shot. But when I tried to reproduce that behavior for other tasks, I was left disappointed."

**Step 2: Reproduce Your Own Work**

> "In the context of brownfield codebases, you're never going to get great results unless you can get the agent to reproduce what you already know how to do."

Force yourself to use agents for tasks you already know how to solve manually. This builds intuition for what agents can and cannot do.

**Step 3: End-of-Day Agents**

Kick off long-running agent tasks before leaving your desk. Let them work overnight. Review results in the morning.

**Step 4: Outsource the Slam Dunks**

Identify tasks where agents are reliably good: boilerplate generation, refactoring, documentation, test writing. Offload these completely.

**Step 5: Engineer the Harness**

> "Anytime you find an agent makes a mistake, you take the time to engineer a solution such that the agent never makes that same mistake again."

This is where real leverage begins. Each prevented mistake compounds.

**Step 6: Always Have an Agent Running**

> "If an agent isn't running, I ask myself 'is there something an agent could be doing for me right now?'"

Mitchell runs slower, more thoughtful models (like deep-thinking modes) in the background while he works on other tasks. The agent doesn't interrupt him — he checks on it when he's ready to context-switch.

### Agent Competition — Multi-Model Validation

From his session with Zed's Richard Feldman:

> "Sometimes I actually have multiple checkouts of Ghostty — ghostty, ghostty2, ghostty3, ghostty4. I will run different models and different agents on the different code bases on the same task with the same prompt. It's a competition."

He caps it at two competing agents. More than that and the cleanup becomes the bottleneck.

### The "Senior Quality" Philosophy

> "Most of the work I do right now with LLMs is just getting it to more of a senior quality point of view. When I think about the code I write, a lot of what I'm doing is making sure that the team is going to understand this — it's not very good at that."

Agents handle implementation well but struggle with team-readability, architectural judgment, and cross-cutting concerns. That's where the human adds value.

### Architect — Not Coder

> "My approach is that I'm more or less the architect of the software project. I still like to come up with the code myself. But I've realized that my value is higher when I'm thinking about the system as a whole rather than typing out individual functions."

The role shift from "person who writes code" to "person who designs the environment in which agents write code."

### On Git's Future in the Agentic Era

From the Pragmatic Engineer podcast (Feb 2026):

> "Git and GitHub may not survive the agentic era in their current form. Agents cause so much churn that merge queues can't handle 10–100x the volume. Branches don't capture failed experiments. The 'Gmail moment' for version control — never delete anything, build better search — hasn't arrived yet."

### On Open Source and AI

> "Open source is moving from 'default trust' to 'default deny' — and Mitchell thinks that's how it should be. This is because AI makes it trivial to create plausible looking but incorrect and low-quality contributions."

### Current Limitations with AI Agents

Mitchell is candid about what agents still struggle with:

**Zig Language:**
> "Anything more than trivial changes to Zig code bases is still hopeless with that language. The workaround I found is when it's helpful, I have it rewrite its solution in another language that it's good at, whether that's C or Rust or Swift or Python, and then I'll do the conversion back to Zig myself."

**Architectural Problems:**
> "I think it's pretty bad at architectural problems. I think it's still very bad at high performance data structure type work. It's so knowledgeable on standard data structures, but it doesn't understand the data structure in the context of what you're trying to achieve."

**Senior-Quality Thinking:**
> "Most of the work I do right now with LLMs is just getting it to more of a senior quality point of view."

## Key Work

### HashiCorp (Co-founder, 2012–2021)
Built the foundational infrastructure tools for modern cloud-native development:

- **Terraform** — Infrastructure as Code (100M+ downloads), the de facto standard for provisioning cloud resources
- **Vagrant** — Revolutionized local development environments for developers
- **Packer** — Machine image building across platforms
- **Vault** — Secrets management and data protection
- **Consul** — Service networking and discovery
- **Nomad** — Container and non-container workload orchestration

HashiCorp IPO'd in 2021. Mitchell stepped back from executive duties to focus on building software.

### Ghostty Terminal Emulator (2023–Present)
A next-generation terminal emulator written from scratch in **Zig**:

- Native macOS (AppKit) and Linux (GTK/GObject) implementations
- GPU-accelerated rendering
- True color support, splits, vim compatibility
- Zig as the primary language for performance and safety
- libghostty — embeddable terminal library for other applications
- Closed beta since 2023, public release planned

**Notable technical work:**
- Full GTK rewrite using GObject type system from Zig (Aug 2025)
- Every PR run through Valgrind for memory safety verification
- Zig debug allocator for leak detection
- 5 complete GUI rewrites, each carrying forward lessons learned

### Zed Agentic Engineering Session (Jun 2025)
Mitchell walked Richard Feldman through his actual AI-assisted workflow on a Ghostty commit. Key patterns demonstrated:

- Using agents for refactoring and cleanup while focusing human effort on architecture
- "I very easily could have done these cleanups in the prior three prompts, but I couldn't do those cleanups and [the architecture changes] at the same time."
- Agents are "really good at refactoring. If they're not fixing bugs or introducing new functionality, they're [doing cleanup]."
- "The bug is fixed, but now let's massage this into what I actually want to see."

### Pragmatic Engineer Podcast (Feb 2026)
2-hour deep-dive with Gergely Orosz covering:
- HashiCorp origin story and business challenges
- AI's impact on open source and development workflows
- Why Mitchell built Ghostty and chose Zig
- His "always have an agent running" philosophy
- The future of version control in the agentic era

## Blog / Key Writings

### Harness Engineering & AI Adoption

- **[My AI Adoption Journey](https://mitchellh.com/writing/my-ai-adoption-journey)** (Feb 5, 2026) — The defining post. Mitchell's 6-step path from AI skeptic to productive harness engineer. Contains the original definition of "Harness Engineering."

- **Zed Agentic Engineering Session** (Jun 19, 2025) — Live walkthrough of AI-assisted development on Ghostty with Richard Feldman. Shows practical patterns for architect-agent collaboration.

### Ghostty Development

- **[We Rewrote the Ghostty GTK Application](https://mitchellh.com/writing/ghostty-gtk-rewrite)** (Aug 14, 2025) — Deep technical post on interfacing GObject type system from Zig and verifying with Valgrind. "Our Zig codebase had one leak and one undefined memory access. That was really surprising to me (in a good way)."

- **[Talk: Introducing Ghostty and Some Useful Zig Patterns](https://mitchellh.com/writing/ghostty-and-useful-zig-patterns)** (Sep 12, 2023) — Zig Showtime talk covering comptime interfaces, Swift integration, and Ghostty's architecture.

### Performance Work

- **Render Thread Optimization** (Nov 2023, X post) — "Love doing highly targeted performance work. I've been working the past few days on changing the way the render thread in Ghostty reads the terminal data (which requires a lock that blocks IO). I've got lock held time down 2.4x so far."

### "Vibing" a Non-Trivial Feature — Full Session Transparency (Oct 2025)

Mitchell published a remarkably transparent account of shipping a real Ghostty feature using AI agentic coding tools. The feature: **unobtrusive macOS automatic update notifications** — triggered after a high-profile OpenAI keynote demo was rudely interrupted by a Ghostty update prompt.

> "I recently shipped a non-trivial Ghostty feature that was largely developed with AI. I'm regularly asked to share non-trivial examples of how I use AI and agentic coding tools and this felt like a golden opportunity to walk through my process with a well-scoped, real-world, shipping feature. This post will share every single agentic coding session I had on the path to shipping this feature, unedited and in full."

**Key workflow patterns demonstrated:**

1. **Plan First, Code Second** — "Tip: Creating a comprehensive plan interactively with an agent is a really important first-step for anything non-trivial. I usually also save it out to something like `spec.md` and in future sessions I can say 'Consult the @spec.md and work on some task.'"

2. **The "Anti-Slop Session"** — When AI gets stuck or produces messy code, Mitchell steps back and manually restructures. "I sometimes tongue-in-cheek refer to this as the 'anti-slop session'." He switched from optional-heavy struct to a tagged union pattern for the view model.

3. **Scaffold + TODO Pattern** — "AI is very good at fill-in-the-blank or draw-the-rest-of-the-owl." Create the structure, leave TODOs, let the agent fill in.

4. **Simulation Testing** — AI generates multiple test scenarios (happy path, errors, not found). This became a high-value use case.

5. **Final Manual Review** — "Final manual review is super super super important. This probably shouldn't be a footnote, but I couldn't find a better place to emphasize it. Please don't ever ship AI-written code without a thorough manual review."

**Cost & Time:** 16 sessions, $15.98 in token spend on Amp (using GPT-5.2-Codex), ~8 hours of wall-clock time over 3 calendar days. "I spent more than that in coffee shops in the two calendar days I spent on this feature."

> "Many people on the internet argue whether AI enables you to work faster or not. In this case, I think I shipped this faster than I would have if I had done it all myself, in particular because iterating on minor SwiftUI styling is so tedious and time consuming for me personally and AI does it so well."

### The Building Block Economy (Apr 2026)

Mitchell's most recent philosophical essay marks a significant shift in how he views software development in the AI era. **Written entirely by hand, without AI assistance**, it articulates a new paradigm:

> "The most effective way to build software and get massive adoption is no longer high quality mainline apps but via building blocks that enable and encourage others to build quantity over quality."

**Key metrics cited:**
- Ghostty: 1 million daily macOS update checks in 18 months
- libghostty: Multiple millions of daily users in just 2 months
- Similar trajectories: Pi Mono, Next.js, Tailwind

> "AI is okay at building everything from scratch, but it is really good at gluing together high quality, well documented, and proven components. And, AI prefers to do this when it can unless explicitly prompted otherwise."

**Strategic implications Mitchell identifies:**

1. **Outsourced R&D** — Maintainers can observe working PoCs in the wild and cherry-pick the best ideas. "There's way less talk and way more walk."
2. **Reduced Maintenance Burden** — Easier to decline feature requests since you provide the means to production, not the final product.
3. **Lower Quality Bar for Niche Artifacts** — Niche implementations don't need to balance millions of use cases.
4. **Mainline Becomes More Stable** — High-quality apps serve specific user groups while leveraging ecosystem-driven R&D.

> "We have to accept that building blocks and software factories rule everything around us and accept and internalize the consequences of that. We can choose to run the other direction and create enclaves where we fight against it. Or we can choose to submit ourselves completely to the chaos."

**On open source vs. commercial in the agentic era:**
> "Agents will more readily pick open and free software over closed and commercial. At the time of writing this article, independent lab experiments confirm this trend."

Mitchell acknowledges this creates a challenge for commercial software but notes the answer is nuanced and avoids prescribing definitive strategies without direct commercial product experience.

### Ghostty Non-Profit Transition (Dec 2025)

Ghostty is now fiscally sponsored by **Hack Club**, a registered 501(c)(3) non-profit. This represents a significant commitment to open-source sustainability:

**Mitchell's rationale:**
> "I want to lay bricks for a sustainable future for Ghostty that doesn't depend on my personal involvement technically or financially."

> "I want to squelch any possible concerns about a 'rug pull'. A non-profit structure provides enforceable assurances: the mission cannot be quietly changed, funds cannot be diverted to private benefit, and the project cannot be sold off or repurposed for commercial gain."

**Financial commitment:**
- Mitchell's family donating $150,000 directly to Hack Club (separate from Ghostty)
- $50,000 personal donation to Ghostty non-profit
- 7% of donations go to Hack Club for administrative overhead
- All financial transactions publicly viewable via Hack Club Bank ledger
- **Zero** funds will go to Mitchell personally — legally guaranteed

> "My ultimate goal with this initiative is to free Ghostty from its dependence on me, not just financially but eventually also as project lead and BDFL."

Simon Willison noted on his blog: "I have been enjoying hitting refresh on the Hack Club Bank transactions throughout today and watching the number grow — it's up to $2,000 now which would fund 33 hours of contributor time based on Ghostty's announced $60/hour standard."

Mitchell responded: "We're up to almost 200 paid developer hours at the time of posting this. Almost everyone who has given today is an individual. Individuals make a big difference."

### libghostty — Embeddable Terminal Emulation (Sep 2025)

Mitchell announced **libghostty**, a zero-dependency library extracted from Ghostty's production core:

> "My answer to this is libghostty: a cross-platform, minimal dependency library that exposes a C API so feature-rich, correct, and fast terminal functionality can be embedded by any application anywhere."

**Why it matters:** Hundreds of programs implement some form of terminal emulation — multiplexers (tmux, zellij), editors (JetBrains' jediterm, VS Code's xterm.js, Zed/Alacritty), web consoles (GitHub Actions, Vercel, Render). Each builds their own, often buggy and incomplete.

**Technical highlights:**
- Zero dependencies (doesn't even require libc)
- SIMD-optimized parsing
- Supports Kitty Graphics Protocol and Tmux Control Mode
- Target: macOS, Linux, Windows, embedded, WASM
- Initial Zig module available; C API in development

> "Terminal emulation is a classic problem that appears simple on the surface but is riddled with unexpected complexities and edge cases."

### Vouch — Community Trust Management System

Beyond Ghostty, Mitchell created **Vouch** ([github.com/mitchellh/vouch](https://github.com/mitchellh/vouch)), a community trust management system based on explicit vouches. Written in Nushell, it has 4,000+ GitHub stars and represents his continued interest in decentralized trust models for open-source communities.

### Technical Philosophy: Transcription as Memory

Mitchell uses **Wispr Flow** (transcription tool) extensively to capture thoughts during coding sessions:

> From Software Unscripted podcast: Mitchell uses voice transcription to narrate his thought process while working, creating a searchable log of design decisions and reasoning. This creates a form of "external working memory" that compounds over time.

### On Diminishing Returns in LLM Progress

From the Software Unscripted podcast (Feb 2026):
> "I've never been the person who says AI will replace all developers. I've always viewed it pragmatically — it's clearly good at what it does. But I don't see life-changing improvements anymore. The delta between models is getting smaller. You notice it, but it's not the same leap we saw before."

He notes that the biggest gains now come from **workflow design** rather than model capability:
> "Being able to consult a slower, more expensive model on demand rather than paying that cost for every little thing — that's where the real leverage is."

## X Activity Themes

- **Harness Engineering patterns** — Systematic agent improvement, error prevention
- **Ghostty development** — Terminal emulator architecture, Zig patterns, GTK/GObject work
- **AI agent workflows** — Multi-agent competition, background agents, delegation discipline
- **Open source philosophy** — Default trust → default deny, AI-generated contributions
- **Infrastructure engineering** — Cloud-native patterns, Terraform, HashiCorp legacy
- **Performance optimization** — Targeted profiling, Valgrind verification, lock contention
- **Version control future** — Git limitations in the agentic era, new paradigms needed

## Key Quotes

> "I don't know if there is a broad industry-accepted term for this yet, but I've grown to calling this 'harness engineering.' It is the idea that anytime you find an agent makes a mistake, you take the time to engineer a solution such that the agent never makes that same mistake again."

> "If an agent isn't running, I ask myself 'is there something an agent could be doing for me right now?'"

> "My approach is that I'm more or less the architect of the software project. I still like to come up with the code myself. But I've realized that my value is higher when I'm thinking about the system as a whole rather than typing out individual functions."

> "Most of the work I do right now with LLMs is just getting it to more of a senior quality point of view."

> "Anything more than trivial changes to Zig code bases is still hopeless with that language."

> "Git and GitHub may not survive the agentic era in their current form."

> "Open source is moving from 'default trust' to 'default deny.'"

> "I really don't care one way or the other if AI is here to stay, I'm a software craftsman that just wants to build stuff for the love of the game."

> "If you can't be embarrassed about your past self, you're probably not growing."

## Related People

- **[[ryan-lopopolo]]** — Both independently arrived at "Harness Engineering"; Ryan from OpenAI enterprise scale, Mitchell from individual developer experience
- **[[boris-cherny]]** — Both work on AI-assisted developer workflows; Boris's parallel agent patterns complement Mitchell's background agent approach
- **[[karpathy]]** — Shared interest in making AI accessible to individual developers; Mitchell's harness philosophy aligns with Software 2.0/3.0 thinking
- **[[simon-willison]]** — Willison covers agentic engineering patterns; Mitchell's practical approach resonates with Simon's philosophy
- **Richard Feldman** — Zed engineer who hosted Mitchell's agentic engineering session
- **Gergely Orosz** — Pragmatic Engineer podcast host who interviewed Mitchell on AI workflows
- **Armon Dadgar** — HashiCorp co-founder; built the Hashi stack together

## Sources

- [mitchellh.com/writing/my-ai-adoption-journey](https://mitchellh.com/writing/my-ai-adoption-journey) — Original harness engineering definition
- [Zed Blog: Agentic Engineering in Action](https://zed.dev/blog/agentic-engineering-with-mitchell-hashimoto) — Session transcript with Richard Feldman
- [The Pragmatic Engineer: Mitchell Hashimoto's New Way of Writing Code](https://podscan.fm/podcasts/the-pragmatic-engineer/episodes/mitchell-hashimotos-new-way-of-writing-code) — Full podcast episode (Feb 2026)
- [Ghostty GTK Rewrite](https://mitchellh.com/writing/ghostty-gtk-rewrite) — Technical deep-dive
- [Ghostty Zig Patterns Talk](https://mitchellh.com/writing/ghostty-and-useful-zig-patterns) — Architecture overview
- [GitHub: mitchellh](https://github.com/mitchellh) — Open source projects
