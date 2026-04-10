---
title: "Peter Steinberger"
created: 2026-04-10
updated: 2026-04-10
tags: [person, ios, developer-tools, ai-agents, startups, agentic-engineering, vibe-coding]
aliases: ["@steipete", "steipete", "Peter Steinberger"]
---

# Peter Steinberger (@steipete)

| | |
|---|---|
| **X** | [@steipete](https://x.com/steipete) |
| **Blog** | [steipete.me/posts](https://steipete.me/posts) |
| **GitHub** | [github.com/steipete](https://github.com/steipete) |
| **Role** | Founder, OpenClaw (previously PSPDFKit) |
| **Previously** | CEO/Founder PSPDFKit (13 years, sold 2021) |
| **Known for** | "Vibe coding" pioneer, agentic engineering workflow, AI-powered solo development |
| **Bio** | Austrian developer who bootstrapped PSPDFKit into a global PDF SDK company over 13 years, then pivoted to pioneering AI-driven solo development. Based between Vienna and London, he now builds products entirely with AI agents, shipping code he doesn't read himself. |

## Overview

**Peter Steinberger** is one of the most visible practitioners and evangelists of **agentic engineering** — the practice of building software primarily through AI coding agents rather than manual coding. After founding and running **PSPDFKit**, a successful PDF SDK company, for 13 years, he sold his shares and embarked on an experimental journey that has become a case study in AI-native software development.

Peter's transformation from elite iOS engineer to AI-powered solo builder is dramatic. He now describes himself as "addicted to agentic engineering," building products like **OpenClaw** (an AI agent platform), **Vibe Meter** (a macOS menu bar app for tracking AI spending), **Clawdis** (an AI assistant with full access to his computers and home), and **Arena** — all shipped by a single person working with a fleet of AI agents.

What makes Peter's perspective uniquely valuable is that he documents his workflow **publicly and transparently**. His blog posts at [steipete.me](https://steipete.me/posts) include real configuration files, honest failures ("watched it fail spectacularly"), and quantitative data about productivity gains. He represents the practical, shipping-focused edge of the AI coding revolution — not theorizing about the future, but living it today.

His journey mirrors the broader transformation happening across the developer community. As he wrote in December 2025: *"The amount of software I can create is now mostly limited by inference time and hard thinking. And let's be honest — most software does not require hard thinking."*

## Core Ideas

### "Vibe Coding" and the AI Slot Machine

Peter coined and popularized several terms that have entered the developer lexicon:

**Vibe Coding**: *"I am addicted to agentic engineering. Sometimes I just 'vibe-code' — throwing ideas at the model and watching the application materialize in real-time."* This isn't about being casual or unserious — it's about the fundamental shift from writing code to directing AI to write it, then evaluating whether the result works.

**The Slot Machine Metaphor**: Peter describes AI coding as a slot machine — you pull the lever with a prompt, and the reward is a working piece of code. The psychological hook is real: *"Hi, my name is Peter and I'm a Claudoholic"* — an honest admission of the addictive feedback loop that AI-assisted development creates.

**Shipping at Inference-Speed**: His December 2025 blog post documents the evolution from amazement ("some prompts produce code that works out of the box") to expectation. The bottleneck is no longer typing code — it's waiting for model inference.

### The Fundamental Developer Role Shift

Peter's most provocative claim: *"I ship code I don't read."* This represents a complete inversion of traditional software engineering values:

- **Before**: Every line of code is read, reviewed, understood
- **Now**: The system as a whole is tested and verified; individual code inspection is secondary
- **The trade-off**: Speed and output volume vs. deep understanding of implementation details

He's explicit about this being a real shift, not hype: *"From the commits, it might appear like it's a company. But it's not. This is one dude sitting at home having fun with a fleet of AI agents."*

### Engineering Codebases for Agents, Not Humans

Peter has developed specific practices for making codebases AI-friendly:

1. **CLI-first development**: Build core logic as a command-line tool first, then wrap with UI. Example: his `summarize` CLI (local transcription + model summarization) was built first, then the Chrome extension was completed in one day.

2. **`docs/` folders and `AGENTS.md`**: Maintain explicit documentation files that force context loading for AI agents. Cross-reference projects via relative paths to scaffold or replicate patterns.

3. **Atomic commits**: *"Every change, no matter how small, should be an atomic git commit. This makes it possible for agents to revert and iterate without losing context."*

4. **Engineer for agents**: *"I don't design codebases to be easy to navigate for me, I engineer them so agents can work in it efficiently. Fighting the model is often a waste of time and tokens."*

### Model Selection: GPT-5.2 Codex vs. Claude Opus

Peter provides specific, data-backed comparisons:

| Aspect | GPT-5.2 Codex | Claude Opus |
|--------|---------------|-------------|
| Behavior | Reads extensively (10-15 min) before writing | Eager to write immediately |
| Context | ~5x more output per session | Good for small edits |
| Knowledge | Up-to-date (August cutoff) | ~5 months behind |
| Best for | Large refactors, complex features | Quick patches, automation |

His recommendation: *"Default to `gpt-5.2-codex` high. `xhigh` is slower with negligible gains. Use Opus for automation/personality-driven tasks."*

### Plan Mode Is Dead

Peter argues that planning modes are obsolete with modern models: *"Plan mode feels like a hack that was necessary for older generations of models that were not great at adhering to prompts, so we had to take away their edit tools."* His workflow is direct — prompt, iterate, commit.

### The Multi-Machine Agent Fleet

Peter runs a distributed development setup:
- **MacBook Pro** (primary development machine)
- **Mac Studio** (remote via Jump Desktop, handles UI/browser automation and long-running tasks)
- Synced via `git` on `main` branch
- Custom **Poltergeist** build watcher that auto-detects and rebuilds any project (Swift, Rust, Node.js, CMake)
- Custom **skills** for domain registration, frontend generation, and Tailscale routing

### Language Choices in the AI Era

Peter's language preferences have shifted dramatically:
- **TypeScript** for web applications
- **Go** for CLIs (favored because *"agents are really great at writing it, and its simple type system makes linting fast"*)
- **Swift** for macOS/iOS UI
- **No Xcode needed**: *"Swift's build infra is good enough for most things these days. codex knows how to run iOS apps and how to deal with the Simulator."*

### Business Lessons Applied to AI Development

Peter's 13 years running PSPDFKit inform his current AI-native approach:

- **Niche selection**: *"Success often lies in tackling the problems that are 'hard and not interesting.'"* He chose PDFs because he saw a need for professional solutions where others found the complexity too tedious.
- **Customer-centricity**: *"The best feature requests come from people who are already paying you."*
- **Bootstrapping reality**: *"It took me 13 years to become an overnight success."*
- **Knowing when to exit**: Selling PSPDFKit was about recognizing when "building" became "managing" and no longer fueled his passion.
- **Remote-first advantage**: PSPDFKit was remote from the start, allowing access to global talent — a practice that now enables solo AI-powered development.

### When AI Isn't Enough

Peter is honest about the limits:
- **Picking the right dependency and framework** still requires human judgment
- **Architecture decisions** need human thought
- **Starting with the model and CLI first** is still the best approach
- **Context management** via `docs/` folders remains essential

## Key Work

### Current Projects (2025-2026)

| Project | Description | Stack |
|---------|-------------|-------|
| **OpenClaw** | AI agent platform for building and deploying autonomous agents | AI/ML, agentic workflows |
| **Vibe Meter** | macOS menu bar app for real-time AI spending tracking | Swift, AI API integration |
| **Clawdis** | AI assistant with full access to computers, messages, home automation | AI agents, multi-system |
| **Arena** | Real-time collaborative coding environment | AI-powered development |
| **Poltergeist** | Universal build watcher for any project type | Go, multi-language support |
| **Oracle** | CLI tool for routing stuck agents to GPT-5 Pro for deep research | Go, API routing |
| **summarize** | Local transcription + AI summarization CLI with Chrome extension | Go, web extension |

### PSPDFKit (2008-2021)

- Bootstrapped PDF SDK company serving enterprise customers globally
- Remote-first team with engineers across multiple countries
- Cross-platform C++ codebase shared across iOS, Android, and Web
- Sold in 2021 after 13 years of growth
- Notable for pioneering PDF text selection (3 months of engineering effort due to character positioning complexity)

### Blog & Thought Leadership

Peter's blog at [steipete.me](https://steipete.me/posts) is one of the most practical resources on AI-native development:

- **"Shipping at Inference-Speed"** (Dec 2025) — The evolution from amazed to expecting working code from AI
- **"Just Talk To It — the no-bs Way of Agentic Engineering"** (Oct 2025) — Practical guide to AI coding agents
- **"Claude Code Anonymous"** (Sep 2025) — Meetup format for full-breadth developers
- **"My Current AI Dev Workflow"** (Aug 2025) — Ghostty + VS Code + Claude Code setup
- **"Essential Reading for Agentic Engineers"** (monthly series) — Curated AI dev perspectives
- **"Migrating 700+ Tests to Swift Testing"** (Jun 2025) — Real-world AI-assisted migration
- **"Self-Hosting AI Models After Claude's Usage Limits"** (Jul 2025) — Practical infrastructure guide

## Blog / Recent Posts

| Post | Date | Summary |
|------|------|---------|
| **OpenClaw, OpenAI and the future** | Feb 2026 | Joining OpenAI to work on agents; OpenClaw moves to a foundation |
| **Shipping at Inference-Speed** | Dec 2025 | How vibe coding matured from amazement to expectation; GPT 5.2 vs. Claude comparison |
| **The Signature Flicker** | Dec 2025 | UI/UX observation on digital signatures |
| **Just Talk To It — the no-bs Way of Agentic Engineering** | Oct 2025 | 23-minute practical guide to working with AI coding agents without hype |
| **Claude Code Anonymous** | Sep 2025 | New meetup format for developers exploring AI agents |
| **Live Coding Session: Building Arena** | Sep 2025 | Real-time collaborative coding with AI agents |
| **My Current AI Dev Workflow** | Aug 2025 | Ghostty + VS Code + Claude Code setup details |
| **Just One More Prompt** | Aug 2025 | Reflection on AI addiction and extreme work culture |
| **Poltergeist** | Aug 2025 | AI-friendly universal build watcher for any project |
| **Essential Reading for Agentic Engineers** | Jul/Aug 2025 | Monthly curated reading list for AI-assisted development |
| **Migrating 700+ Tests to Swift Testing** | Jun 2025 | AI-assisted test migration with real failure documentation |
| **VibeTunnel's first AI-anniversary** | Jun 2025 | One year of building with AI agents |
| **Don't read this Startup Slop** | May 2025 | Website banned from Lobsters for using AI agents to write blog posts |
| **Self-Hosting AI Models After Claude's Usage Limits** | Jul 2025 | Practical guide to running local AI models |

## Related People

- [[andrej-karpathy]] — Fellow AI-native developer advocate; both explore agent-based workflows
- [[boris-cherny]] — Claude Code creator; Peter's primary tool for agentic engineering
- [[daniel-han]] — Unsloth CEO; both focus on democratizing powerful tools (fine-tuning vs. coding)
- [[antirez-com]] — Salvatore Sanfilippo's practical, shipping-first philosophy mirrors Peter's approach
- [[simon-willison]] — Fellow practical AI tooling advocate and blogger
- [[sebastien-ramirez]] — Python developer whose OSS challenges parallel Peter's community experience

## X Activity Themes

Peter (@steipete) is one of the most active and followed voices in the agentic engineering community:

- **Workflow documentation** — Detailed posts about his AI development setup, configs, and daily practices
- **Product launches** — OpenClaw, Vibe Meter, Clawdis, Arena — all announced and documented on X
- **Tool comparisons** — GPT vs. Claude vs. open-source models for specific tasks
- **Vibe coding philosophy** — Honest takes on the psychological and practical aspects of AI-assisted development
- **AI spending transparency** — Real numbers on API costs, usage patterns, and optimization strategies
- **Community building** — Claude Code Anonymous meetups, Essential Reading series, mentorship content
- **iOS/macOS development** — Still active in Apple developer community, Swift Testing migration, Xcode alternatives
- **Open-source advocacy** — Everything he builds is on GitHub for others to fork and remix

His posting style is **raw, practical, and quantitative** — he shares actual config files, real numbers, and honest failures rather than polished success stories. This transparency has made him one of the most trusted voices in the agentic engineering movement.
