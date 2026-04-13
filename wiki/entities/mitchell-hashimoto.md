---
title: "Mitchell Hashimoto"
handle: "@mitchellh"
created: 2026-04-13
updated: 2026-04-13
tags: [person, x-account, ai, agentic-engineering, harness-engineering, ghostty, zig, hashicorp, terraform, terminal-emulator]
aliases: ["mitchell hashimoto harness engineering", "mitchellh ghostty", "hashicorp founder AI agents", "always have an agent running"]
depth: 14000
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
