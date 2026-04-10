# Realmcore (Mihir Chintawar & Kiran)

**URL:** https://randomlabs.ai
**Blog:** randomlabs.ai/blog
**Twitter/X:** @realmcore_ (Mihir Chintawar)
**GitHub:** github.com/xjdr-alt (note: distinct from Jeff Rose's xjdr)
**Role:** Co-founders of Random Labs (YC S24); builders of Slate
**Projects:** Slate (swarm-native coding agent), open-source IDE agent tooling

## Overview

Realmcore is the online identity of Mihir Chintawar, co-founder and CTO of Random Labs, a Y Combinator S24 startup based in San Francisco. Random Labs was co-founded in 2024 by Mihir Chintawar and Kiran Chintawar with the mission of building "long running autonomous coding agents" — software engineering tools that can work with developers for hours on complex, multi-file tasks rather than providing only point-in-time autocomplete suggestions.

The company's flagship product, Slate, launched in March 2026 as the industry's first "swarm-native" coding agent. Slate is distinguished by its novel architecture called "Thread Weaving," which uses multiple specialized AI models running in parallel, coordinated through a central orchestration thread. Instead of a monolithic agent trying to do everything, Slate treats different models as specialized workers: Claude Sonnet for orchestration, GPT-5.4 for code execution, GLM for agentic search — each selected for the task at hand.

Random Labs emerged from open beta with a strong technical thesis: the real bottleneck in AI coding agents is not model intelligence but context management. Their argument is that existing approaches — ReAct agents, Recursive Language Models (RLM), and markdown planning — all "paper over" context limitations rather than solving them. Slate's approach maintains persistent, structured knowledge of a codebase throughout long autonomous sessions.

The company positions itself against the narrative of "AI replacing developers." Instead, they aim to "bridge the global engineering shortage by positioning Slate as a collaborative tool for the next 20 million engineers." Their approach is open-source-first: the Slate CLI is available via `npm i -g @randomlabs/slate`, and they've built their agent to work directly inside existing IDEs.

Mihir Chintawar studied Computer Science at Cal Poly San Luis Obispo (2020–2024) and previously worked as a software developer at Amazon (2021–2023). His technical interests span operating systems, database systems, compilers, and functional programming.

## Timeline

| Date | Event |
|------|-------|
| 2020 | Mihir Chintawar begins Computer Science studies at Cal Poly San Luis Obispo |
| 2021 | Mihir joins Amazon as a software developer while studying |
| 2023 (Nov) | Mihir leaves Amazon to focus on startup |
| 2024 | Random Labs founded by Mihir and Kiran Chintawar in San Francisco |
| 2024 (Summer) | Random Labs accepted into Y Combinator S24 batch |
| Early 2024 | Released open-source agent pitched as living "inside your codebase" |
| Mid 2024 (May) | Built one of the first instances of a sliding window-based agent capable of running for up to 2 days (deprecated, available as `npm i -g @randomlabs/slatecli`) |
| 2024–2025 | Open beta development of Slate with Thread Weaving architecture |
| 2026 (March 12) | Slate V1 officially launches from open beta; announced as first "swarm-native" coding agent |
| 2026 (March 13) | Published technical blog post: "Slate: moving beyond ReAct and RLM" — articulating their architectural thesis |
| 2026 (March) | VentureBeat covers Slate V1 launch; ComputerTech publishes hands-on review (rating: 7.4/10) |
| 2026 (Upcoming) | Direct support for OpenAI Codex and Anthropic Claude Code integration planned |

## Core Ideas

### Swarm-Native Architecture

Slate's central innovation is the concept of "swarm-native" coding — rather than a single LLM trying to handle an entire engineering task, Slate orchestrates multiple specialized models working in parallel. This is not multi-agent prompting; it's a fundamentally different architecture where:

- Each thread runs a single action or tactic through a highly expressive interface (DSL)
- Threads pause after each action and return control to the orchestrator
- Episodes (compressed representations of completed thread actions) are composed as inputs for subsequent threads
- The system supports cross-model composition with zero context coherence loss

The result is that a developer can have Claude Sonnet orchestrating a complex refactor while GPT-5.4 executes code and GLM simultaneously researches library documentation — each model doing what it does best, coordinated by the swarm architecture.

### Thread Weaving and Episodes

Thread Weaving is Slate's key architectural primitive. It solves three compounding problems in modern LLM agents:

1. **Long-horizon tasks** — Path-dependent tasks exceeding minimal tool-calling loops, requiring working memory and strategic/tactical balance
2. **The "Dumb Zone"** — Dex Horthy's term for the part of the context window where retrieval quality drops as context fills
3. **Strategy vs. Tactics** — Strategy is open-ended planning and knowledge retrieval; tactics are learned, local action sequences

The approach: instead of letting the context window fill until the process crashes (the "Ralph Wiggum loop"), each thread return is a natural opportunity to decide what gets retained, what gets compressed, and what gets discarded. Episodes act as natural compaction boundaries.

### The LLM OS Framing

Random Labs explicitly models Slate's architecture on operating system concepts and Andrej Karpathy's "LLM OS" idea:

| OS Component | Slate Equivalent |
|---|---|
| Kernel | Orchestration LLM |
| RAM | Context Window (scarce, actively managed) |
| Processes | Threads (isolated execution units) |
| Return Values | Episodes (compressed state committed back to kernel) |
| Peripherals | Filesystem, Terminal, Web APIs |

This framing isn't just metaphorical — it drives concrete architectural decisions about how memory is managed, how processes are isolated, and how the system handles resource constraints.

### Knowledge Overhang

A key concept in Random Labs' thinking is "knowledge overhang" — the latent intelligence a model possesses but cannot effectively access when it is tactically overwhelmed. Most agent architectures force models to juggle high-level planning and low-level implementation simultaneously, creating a cognitive bottleneck. Slate solves this by using a central orchestration thread that "programs in action space" — deciding what to do and delegating the how to worker threads.

> "Models naturally route context throughout the system in ways that are useful and appropriate, without being explicitly trained to do so."

### Context Management > Model Intelligence

Random Labs' fundamental thesis is that the real bottleneck for long-horizon software engineering tasks is systems design, not model capability. Proper routing and memory management unlock the model's latent knowledge. This is why they criticize approaches that focus on bigger models rather than better orchestration.

Their technical blog post "Moving Beyond ReAct and RLM-Based Coding Agents" (March 2026) argues that both dominant paradigms — ReAct (Reasoning + Acting) and RLM (Recursive Language Models) — treat context management as an afterthought. ReAct agents interleave reasoning traces with action steps, while RLMs externalize data into a Python REPL. Both end up papering over context limitations rather than fixing them.

### Open Source and the "Next 20 Million Engineers"

Random Labs positions itself as building tools that democratize software engineering, not replace developers. Their stated goal is to make it "possible for the next 20 million engineers to come online." They believe AI tools should create jobs rather than replace them, and that open-source tools are essential to this mission.

The Slate CLI is available via npm, and the company has built their agent to work directly inside existing IDEs, making it accessible to developers who are already comfortable with their current workflows.

## Key Quotes

> "Most software agent companies have deeply optimized for swe-bench. However, this is not a representative task. We are building tooling we actually use. It's written parts of itself already and we are extremely excited to share it with you."

> "We believe that software development should stay in the hands of people. We believe that there is near infinite software the world needs and that there are not enough developers to build it."

> "Models naturally route context throughout the system in ways that are useful and appropriate, without being explicitly trained to do so."

> "Slate doesn't need to compact its memory." — Social media positioning

> "By selecting the right model for the job, Slate ensures that users aren't overspending on intelligence for simple tasks."

## Related Wikilinks

- [[AI Agent Architecture]] — Slate's Thread Weaving and swarm-native approach
- [[LLM OS]] — Andrej Karpathy's concept that informs Slate's OS-style framing
- [[Context Management]] — The central problem Slate's architecture addresses
- [[Coding Agents]] — The broader category of tools Slate competes in (Devin, SWE-agent, Cursor, Claude Code, Codex)
- [[ReAct]] — The reasoning-acting paradigm that Slate argues against
- [[Open Source Software]] — Random Labs' commitment to open development
- [[Y Combinator]] — The accelerator that backed Random Labs (S24)
- [[Thread Weaving]] — Slate's novel architectural primitive for context management

## Influence Metrics

- Slate V1: Launched March 12, 2026; covered by VentureBeat, ComputerTech (7.4/10 rating), Agent Wars
- Real-world benchmark: $58.32 cost for a complete library porting task (open-source to TypeScript)
- Y Combinator S24 backing with institutional validation
- Technical blog post "Moving Beyond ReAct and RLM" sparked industry discussion on agent architecture
- Open beta with active community of users providing feedback
- Slate's architecture comparison table has become a reference point in agent design discussions
- Direct integrations planned with OpenAI Codex and Anthropic Claude Code

## Sources

- [Random Labs](https://randomlabs.ai) — Company website
- [Random Labs Blog: "Slate: moving beyond ReAct and RLM"](https://randomlabs.ai/blog/slate) — Technical architecture report
- [Y Combinator: Random Labs](https://www.ycombinator.com/companies/random-labs) — Company profile
- [VentureBeat: "Y Combinator-backed Random Labs launches Slate V1"](https://venturebeat.com/orchestration/y-combinator-backed-random-labs-launches-slate-v1-claiming-the-first-swarm) (March 13, 2026)
- [TechBuddies.io: "Random Labs' Slate V1 Bets on Swarm-Native Agents"](https://www.techbuddies.io/2026/03/16/random-labs-slate-v1-bets-on-swarm-native-agents-to-fix-ais-systems-problem/) (March 16, 2026)
- [Agent Wars: "Random Labs says coding agents are patching over a problem"](https://agent-wars.com/news/2026-03-13-moving-beyond-rlm-and-react-based-coding-agents) (March 13, 2026)
- [ComputerTech: "SLATE V1 Review 2026"](https://computertech.co/slate-v1-review/) (March 14, 2026)
- [Random Labs Documentation](https://docs.randomlabs.ai/) — Slate docs
- [Mihir Chintawar LinkedIn](https://www.linkedin.com/in/mihir-chintawar-95008a1b9) — Professional background
