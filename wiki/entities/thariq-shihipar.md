---
title: Thariq Shihipar
type: entity
handle: "@trq212"
created: 2026-04-10
updated: 2026-05-09
tags:
  - person
  - anthropic
  - ai-agents
  - interpretability
  - company
---
---


# Thariq Shihipar (@trq212)

| | |
|---|---|
| **X** | [@trq212](https://x.com/trq212) |
| **Blog** | [thariq.io](https://www.thariq.io) |
| **GitHub** | [tshihpar](https://github.com/tshihpar) |
| **Role** | Member of Technical Staff @ Anthropic (Claude Code team); Founder @ Multiverse |
| **Known for** | Claude Agent SDK architecture, "Skills" system design, agent harness engineering, interpretability research, YC-backed startups |
| **Bio** | Engineer and serial entrepreneur currently on the Claude Code team at Anthropic. Previously founded Multiverse (YC W20, raised $17M), sold a SaaS startup (Edgeout.gg → blitz.gg), co-founded Pubpub.org (non-profit academic publishing), and studied at the MIT Media Lab. Writes thoughtfully about AI interpretability, agent architecture, spirituality, and the craft of building. |

## Notable Writing

- **"[Detecting when LLMs are Uncertain](https://www.thariq.io/blog/entropix/)"** (Oct 2024) — The canonical explainer of [[entities/xjdr|xjdr's]] entropix project. Breaks down the entropy/varentropy quadrant, 4 adaptive sampling strategies, and the "thinking token" insight. [[concepts/entropix]]

## Overview

Thariq Shihipar occupies a unique position in the AI engineering world — he is simultaneously a **core builder of production AI systems** (Claude Code at Anthropic) and a **reflective practitioner** who writes deeply about the philosophical and spiritual dimensions of technology. This combination of deep technical chops and introspective analysis makes his blog one of the most distinctive in the AI space.

At Anthropic, Shihipar is a Member of Technical Staff on the **Claude Code** team and was a key architect of the **Claude Agent SDK** (formerly Claude Code SDK). His January 2026 workshop on the Claude Agent SDK — "Learn to use Anthropic's Claude Agent SDK for AI-powered development workflows" — attracted nearly 100,000 views on YouTube and has been described by developers as "the Agent builder's bible." In this workshop, he built an agent harness from scratch, implementing the core Agent Loop (Context → Thought → Action → Observation), integrating the Bash tool for general computer use, and demonstrating context engineering via the filesystem.

His work on **Skills** — Anthropic's modular mechanism for extending Claude's capabilities — has been particularly influential. A February 2026 article, "Lessons from Building Claude Code: How We Use Skills," went viral with over 6 million views and 15,000 likes on X. The article detailed how Anthropic's team uses Skills as modular "smart folders" containing scripts, knowledge bases, and documentation to make Claude behave like a specialized professional assistant.

Before Anthropic, Shihipar's entrepreneurial track record includes:
- **Multiverse** (YC W20) — A gaming company that raised $17M and scaled to over a million users, going viral on TikTok
- **Edgeout.gg** — A bootstrapped gaming analytics platform sold to blitz.gg
- **Quick Edit** — AI copyediting with great UX
- **Sherpa** — An AI email assistant that prioritizes emails based on contacts and goals
- **Pubpub.org** — A non-profit academic publishing platform (co-founded)
- **LatentLit** — A tool for creating and sharing LLM-powered AI agents
- **Chime** — An undergrad startup

He also holds a graduate degree from the **MIT Media Lab**, where he explored the intersection of technology, creativity, and human-computer interaction.

## Core Ideas

### The Harness Concept

Shihipar's work on the Claude Agent SDK is grounded in the idea that **agents need more than just a model** — they need a "harness" containing:

- **Tools**: Capabilities the agent can invoke (Bash, file operations, web browsing)
- **Prompts**: Behavioral constraints and instructions
- **File System**: Durable state and context engineering surface (`CLAUDE.md`)
- **Skills**: Modular capability packages
- **Sub-agents**: Delegated agents for specialized tasks
- **Memory**: Cross-session state and learning

> *"Agents build their own context, like decide their own trajectories, are working very very autonomously."*

This framing aligns closely with [[entities/varun-trivedy]]'s "Agent = Model + Harness" equation and [[entities/philipp-schmid]]'s analysis of agent harnesses as the key infrastructure layer for 2026.

### The Power of the Bash Tool

One of Shihipar's key technical insights is that the **Bash tool** is often the most powerful tool for agent workflows:

> *"The Bash tool is the ultimate API — it gives agents general-purpose access to the computer, rather than being limited to specific pre-built integrations."*

This insight has influenced how the Claude Agent SDK is designed — prioritizing general-purpose computer access over domain-specific tool integrations.

### Context Engineering via Filesystem

Shihipar introduced the concept of **Context Engineering** — using the filesystem as the primary medium for maintaining agent state across long-running tasks:

- `CLAUDE.md` files ground future actions with persistent context
- The filesystem serves as a shared workspace between humans and agents
- Git provides versioning, rollback, and branching capabilities
- Skills can be stored as files and discovered dynamically

> *"One of the key insights we had building Claude Code is that people were using it for non-coding tasks. The filesystem turned out to be the universal interface."*

### Interpretability and Steering → [[concepts/interpretability]] / [[concepts/activation-steering]]

In **"Should Developers Care about Interpretability?"** (Nov 2024), Shihipar made the case that interpretability is not just an academic concern but a practical engineering tool that promises developers "a level of control over their models that has not been possible thus far."

**Key arguments:**

1. **Style capture beyond words**: Steering allows control that natural language can't express — e.g., "70% friendly, 50% concise, 80% professional." Examples span text (Goodfire.ai, Prism), voice (Hume), and images (Featurelab.xyz).

2. **RLHF alternative**: Steering happens at **inference time**, giving API developers per-request control vs. RLHF's provider-imposed, one-size-fits-all post-training. This avoids RLHF's side effects (false refusals, quality degradation).

3. **Persistent user preferences**: Preferences like "respond briefly" are lost from the context window — steering can make them permanent by amplifying the relevant feature.

4. **Cheap classification without separate models**: Find "spam features" from a few examples and classify at inference time — no separate classifier training needed.

**His cautionary notes** foreshadow the [[concepts/scaling-hypothesis|performance-controllability tradeoff]]:
> "Steering is like brain surgery, prompting is like asking politely."

- Over-amplification can push the model out-of-distribution (Golden Gate Claude thinking it *is* the bridge)
- Feature labeling is still unreliable (humans + machines, disagreeable labels)
- Feature circuits create unpredictable side effects, much like RLHF

**Shihipar's prediction**: "Next-gen model APIs will get a lot more powerful but also more complicated — requiring more than just prompting and RAG to get the outputs we want."

### Entropix and Uncertainty Detection

In "Detecting when LLMs are Uncertain" (Oct 2024), Shihipar provided an accessible deep-dive into **Entropix**, a technique developed by XJDR for improving reasoning through adaptive sampling:

- **Entropy** measures how spread out the model's predictions are
- **Varentropy** measures the "shape" of uncertainty
- Different uncertainty states suggest different actions (branching, thinking tokens, standard sampling)
- Inference-time techniques are accessible to open-source hackers without huge budgets

### Spiritual Technology

Shihipar's blog extends beyond pure technical content into deeply personal reflections on spirituality, intention, and character development:

- **"Spiritual Technology"** — On systematized ways of improving character and soul, inspired by Ghazali
- **"Intention"** — On the nature of intention, accountability, and why he writes publicly about spirituality
- **"I can think. I can wait. I can fast."** — On not needing anything, and the freedom that comes from wanting less
- **"Clay and Light"** — On the two modes of being — driven by desire or moved by something inexplicable

## Key Work

### Claude Agent SDK Workshop (Jan 2026)

A comprehensive 1h53m workshop that became one of the most-viewed technical tutorials on AI agent development:
- Built an agent harness from scratch live on camera
- Implemented the core Agent Loop (Context → Thought → Action → Observation)
- Demonstrated context engineering via the filesystem
- Showed how the Bash tool enables general-purpose computer use
- Explained the evolution from LLM features to LLM agents

### "Lessons from Building Claude Code: How We Use Skills" (Feb 2026)

A viral article (6M+ views, 15K+ likes on X) detailing:
- 9 real-world application scenarios for Skills
- High-level design principles for modular AI capabilities
- Common pitfalls and how to avoid them
- How Skills became the most flexible and shareable AI tooling mechanism at Anthropic

### Multiverse (YC W20)

A Y Combinator-backed gaming company that:
- Raised $17M in funding
- Scaled to over 1 million users
- Went viral on TikTok
- Ran for 5 years before transitioning

### Entropix Analysis (Oct 2024)

An accessible explanation of XJDR's uncertainty detection technique:
- Mapped entropy and varentropy combinations to specific sampling actions
- Compared branching (MCTS) vs. thinking tokens approaches
- Argued for inference-time optimization as a low-budget path to improved reasoning

### Other Notable Projects

| Project | Description |
|---------|-------------|
| **LatentLit** | Tool for creating and sharing LLM-powered AI agents |
| **Sherpa** | AI email assistant that prioritizes based on contacts and goals |
| **Quick Edit** | AI copyediting with great UX |
| **AI Worldbuilding** | Experiment in AI-aided world building for RPGs |
| **Edgeout.gg** | Bootstrapped gaming analytics (sold to blitz.gg) |
| **Pubpub.org** | Non-profit academic publishing platform (co-founded) |
| **LLM-Powered Sorting with TrueSkill** | Sorting large datasets using LLMs and TrueSkill ranking |

### HTML Artifacts Advocacy (May 2026)

Shihipar has been advocating for **HTML as the primary output format for AI agents** rather than Markdown, with his May 2026 X article "The Unreasonable Effectiveness of HTML" and a companion site ([thariqs.github.io/html-effectiveness/](https://thariqs.github.io/html-effectiveness/)) featuring 20 self-contained `.html` files organized into 8 categories:

| # | Category | Demos | Key Insight |
|---|----------|-------|-------------|
| 1 | **Exploration & Planning** | 3 | Side-by-side code approach comparisons, visual design directions, implementation plans with timelines — point at one instead of juggling three walls of text |
| 2 | **Code Review & Understanding** | 3 | Annotated PRs with severity tags, PR writeups for reviewers, module maps as boxes-and-arrows — spatial information needs spatial rendering |
| 3 | **Design** | 2 | Living design system swatches, component variant contact sheets — HTML is the medium design ships in |
| 4 | **Prototyping** | 2 | Animation sandboxes with sliders, clickable interaction flows — motion can't be described, only felt |
| 5 | **Illustrations & Diagrams** | 2 | SVG figure sheets, annotated flowcharts — inline SVG gives the agent a real pen |
| 6 | **Decks** | 1 | Arrow-key slide decks from `<section>` tags + 20 lines of JS — no Keynote, no export step |
| 7 | **Research & Learning** | 2 | Feature explainers with collapsible sections, concept explainers with live interactive rings |
| 8 | **Reports** | 2 | Weekly status with charts, incident timelines with color-coded severity |

His key arguments:

- **Rich, self-contained outputs**: HTML allows LLMs to embed SVG diagrams, interactive widgets, in-page navigation, and color-coded severity annotations directly in their responses
- **Token efficiency is less relevant now**: With modern large context windows, the token cost difference between HTML and Markdown is negligible compared to the expressive benefits
- **Better for code review and technical explanations**: HTML artifacts can render actual diffs with inline margin annotations, making complex technical concepts clearer
- **Spatial information needs spatial rendering**: Diffs and call-graphs are spatial; Markdown flattens them — HTML preserves the shape of the code

Simon Willison noted this caused him to reconsider his default Markdown preference (from the GPT-4/8K context era), and demonstrated the approach with a `curl https://copy.fail/exp | llm -m gpt-5.5 -s 'Explain this code... Output HTML...'` experiment on a Linux security exploit, producing an [interactive HTML explanation](https://gisthost.github.io/?ae53e3461ffdbfd0826156aacf025c7e).

**Andrej Karpathy** endorsed the article (May 11, 2026) with a broader framework: he positioned HTML as step 3 in a progression from raw text → markdown → HTML → interactive neural videos/simulations. Karpathy argues vision is the "10-lane superhighway" of information into the brain, and that the "input/output mind meld" between humans and AIs is still in early stages — with significant progress possible well before neuralink-style BCIs. His simple advice: "hot tip try ask for HTML." (3,350 likes, 3,339 bookmarks). [[raw/articles/2026-05-11_karpathy_html-and-vision-progression]]

This represents a broader shift in AI engineering toward richer output formats, challenging the default assumption that Markdown is always optimal for LLM responses. The approach complements his earlier work on **Skills** and **Context Engineering** by providing a more expressive medium for agent outputs. The progression framework (Karpathy) and practical use cases (Shihipar's 8 categories) together form a comprehensive case for [[concepts/ai-output-format-progression|HTML as the next default output modality for AI agents]].

## Blog / Recent Posts

| Date | Title | Theme |
|------|-------|-------|
| 2026-05-08 | The Unreasonable Effectiveness of HTML (via Simon Willison) | Technical — Advocating for HTML over Markdown for rich AI agent outputs |
| 2026-03-28 | ✦ Clay and Light | Spiritual — Two modes of being: driven by desire or moved by inexplicability |
| 2026-02-22 | A Lovely Autumn Night | Reflection — How ambition changes shape from climbing towers to caring for people |
| 2026-02-14 | The Thing | Courage — We're all bottlenecked by courage; being smart rarely helps |
| 2026-01-20 | I can think. I can wait. I can fast. | Minimalism — Freedom from wanting less |
| 2026-01-16 | Strangers & Travelers | Connection — Being a stranger in the world and changing without changing yourself |
| 2025-12-06 | Spiritual Technology | Character — Systematized ways of improving character, inspired by Ghazali |
| 2025-12-06 | Intention | Purpose — Nature of intention, accountability, public writing on spirituality |
| 2025-11-17 | LLM-Powered Sorting with TrueSkill | Technical — Sorting large datasets using LLMs and TrueSkill ranking |
| 2024-11-04 | Should Developers Care about Interpretability? | Technical — Breakdown of interpretability and steering, why it matters |
| 2025-10-24 | AI & Product Strategy Consulting through Multiverse Inc. | Business — Consulting services for AI product development |
| 2024-11-04 | Detecting when LLMs are Uncertain (Entropix) | Technical — Accessible deep-dive into Entropix reasoning techniques |
| 2024-10-11 | Crypto ELI5 | Education — Explaining cryptocurrency intuition through a "toy crypto" currency |
| 2024-10-11 | How Modding Games Changed My Life | Personal — The impact of game modding on creative development |

## Related People

- **[[entities/varun-trivedy]]** — Both work on agent harness engineering; Trivedy's "Agent = Model + Harness" framework parallels Shihipar's SDK architecture
- **[[entities/philipp-schmid]]** — Both write about agent infrastructure; Schmid's "2026 will be around Agent Harnesses" aligns with Shihipar's Claude Agent SDK work
- **[[entities/florian-brand]]** — Both interested in interpretability and understanding how AI systems work under the hood

## X Activity Themes

Shihipar's X activity (@trq212) typically covers:

1. **Claude Code & Agent SDK** — Technical deep-dives into agent architecture, Skills design, and harness engineering
2. **Interpretability research** — Accessible explanations of how LLMs work internally and why developers should care
3. **Startup lessons** — Reflections on building, scaling, and selling companies; practical advice for founders
4. **Spiritual and philosophical content** — Thoughtful posts on intention, character development, and the meaning of technology in human life
5. **AI product strategy** — Insights on building AI products that users actually want, drawing from extensive startup experience
6. **Community engagement** — Active participation in AI developer communities, workshop presentations, and knowledge sharing

## References

- thariq-shihipar-a-lovely-autumn-night
- thariq-shihipar-claude-computer-use-is-vision-the-ultimate-api
- thariq-shihipar-clay-and-light
- thariq-shihipar-entropix
- thariq-shihipar-fast
- thariq-shihipar-intention
- thariq-shihipar-interpretability
- thariq-shihipar-llm-powered-sorting-with-trueskill
- thariq-shihipar-sparse-rewards
- thariq-shihipar-spiritual-technology
- thariq-shihipar-the-thing
- trq212_unreasonable-effectiveness-html
- simonwillison_unreasonable-effectiveness-html
