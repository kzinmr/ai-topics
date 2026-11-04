---
title: Addy Osmani
type: entity
created: 2026-04-10
updated: 2026-11-04
source: "x-account"
tags:
  - person
  - x-account
  - model
  - coding-agents
  - web-development
  - developer-experience
  - google
sources: [raw/articles/2026-06-19_omarsar0_from-prompting-agents-to-loop-engineering.md, raw/articles/2026-07-21_addyosmani_software-factories-light-and-dark.md, raw/articles/2026-08-03_addyosmani_taste-judgment-and-ai.md, raw/articles/2026-08-27_addyosmani_do-you-need-a-software-factory.md, raw/articles/2026-09-14_addyosmani_brownfield-agentic-engineering.md, raw/articles/2026-09-28_addyosmani_the-code-nobody-reads.md, raw/articles/2026-10-14_addyosmani_agentic-verification.md, raw/articles/2026-10-26_addyosmani_claude-code-team-code-review.md, raw/articles/2026-10-28_addyosmani_claude-code-mods.md, raw/articles/2026-10-29_addyosmani_overprompting-claude.md]
---


# Addy Osmani

| | |
|---|---|
| **X/Twitter** | [@addyosmani](https://x.com/addyosmani) |
| **Blog** | [addyosmani.com](https://addyosmani.com/) |
| **Role** | Director, Google Cloud AI (Gemini & Vertex AI) |
| **Previously** | Engineering Lead, Google Chrome & Web Platform |

## Bio

Addy Osmani is a Director at Google Cloud AI, working on Gemini and Vertex AI. Previously, he was Engineering Lead for Chrome & Web Platform at Google, where he became one of the most prolific writers and speakers on web performance, developer experience, and AI-assisted coding. He has 86K+ followers on Medium and regularly speaks at major conferences including O'Reilly CodeCon.

Osmani is the most **prolific systematizer** of agentic coding patterns — he doesn't just use AI coding tools, he builds frameworks, taxonomies, and playbooks for how teams should adopt them.

## Core Ideas

### Conductor → Orchestrator Framework

Osmani's signature contribution is the distinction between two modes of AI-assisted development:

| Mode | Description | Tools |
|------|-------------|-------|
| **Conductor** | Working closely with a *single* AI agent on a specific task. Synchronous, real-time guidance. Micro-level control. | Claude Code CLI, Gemini CLI, Cursor inline |
| **Orchestrator** | Coordinating *multiple* AI agents working in parallel. Asynchronous, macro-level oversight. Planning, task decomposition, output verification. | Agent Teams, Conductor by Melty Labs, Codex Web, Jules |

> "You used to pair with one AI. Now you manage an agent team."

### 8 Levels of AI-Assisted Coding

Adapted from Steve Yegge's developer evolution framework, Osmani maps the progression:

- **L1-L4 (IDE Era)**: No AI → Agent with permissions → YOLO mode → Agent-assisted
- **L5-L8 (Agentic Era)**: Subagents → Agent teams → Orchestration at scale → Full autonomous pipelines

Most developers are stuck at L3-L4. The orchestration tier starts at L6.

### Agent Teams (Swarms)

Osmani was an early advocate of **multi-agent coordination patterns** and documented Claude Code's Agent Teams feature when it launched:

- **Core insight**: LLMs perform worse as context expands — splitting work across specialized agents is more effective than one giant context window
- **Sweet spot**: 3-5 teammates per task; beyond that, coordination overhead dominates
- **Quality gates**: Plan approval → hooks → token budgets → human review
- **Pattern**: Dedicated @reviewer agent per 3-4 builders; lead only sees green-reviewed code

### The Factory Model

Osmani's production-line approach to agentic development:

1. **Plan** — Write specs, define acceptance criteria
2. **Decompose** — Break into self-contained units with clear boundaries
3. **Assign** — Delegate to specialized agents (frontend, backend, tests)
4. **Review** — Automated quality gates + human oversight
5. **Compound** — Learnings feed back into the system for continuous improvement

### Self-Improving Coding Agents

Osmani documented the "Ralph Wiggum technique" — setting up agents to iteratively improve code while the human sleeps:

- Break development into small, self-contained tasks
- Run AI agents asynchronously in parallel
- Validate outputs with automated tests
- Feed failures back as new tasks

### AGENTS.md Critique

In "Stop Using /init for AGENTS.md" (Mar 2026), Osmani argued that:

- Auto-generated AGENTS.md files **hurt agent performance** and inflate costs by 20%+
- They encode noise as signal — directory structures and file listings are redundant with what agents can read
- AGENTS.md should be a **living list of codebase smells you haven't fixed yet**, not permanent configuration
- Before adding any line: "Can the agent find this by reading the code? If yes, don't write it"
- Treat context engineering as **agile** — prune aggressively, encode only non-obvious conventions

### The 70% Problem

Osmani identified a critical limitation of AI-generated code, popularized in Tim O'Reilly's landmark 2025 article: AI can handle the first 70% of a project (scaffolding, documentation, initial prototype) but the final 30% requires "hard-won engineering wisdom" to prevent "house of cards code" that collapses under real-world pressure.

This framing has become a widely cited cautionary concept in the vibe coding debate — the gap between AI's impressive initial output and production-grade quality.

| Phase | AI's Role | Human's Role |
|-------|-----------|-------------|
| First 70% | Scaffolding, documentation, prototyping | Direction setting, requirements |
| Final 30% | Limited (edge cases struggle) | Engineering judgment, architecture decisions, quality assurance |

### Comprehension Debt

Osmani identified a hidden cost of AI-generated code:

- **Comprehension debt** accumulates when developers can't understand code they didn't write
- The risk of multi-agent systems is producing large quantities of code *very quickly* — but that code still needs to be right, maintainable, and actually solving the problem
- **Activity ≠ value** — commits per minute is a vanity metric
- "Let the problem guide the tooling, not the other way around"

### The High-Leverage Developer of 2026

> "The high-leverage developer of 2026 is an async-first manager running parallel AI agents. The developers who will be most productive aren't the ones who write the most code — they're the ones who best decompose problems, specify intent, and verify outcomes."

## Agent Harness Engineering (April 2026)

Osmani published a comprehensive synthesis of the harness engineering movement in "[Agent Harness Engineering](https://addyosmani.com/blog/agent-harness-engineering/)" (April 2026), pulling together threads from multiple voices (Vivek Trivedy, Dex Horthy, HumanLayer, Anthropic Engineering, Birgitta Böckeler) into a unified framework.

Key contributions from this article:

| Concept | Description |
|---------|-------------|
| **The Ratchet** | Every agent mistake becomes a permanent fix — constraints are added on real failures, removed when models internalize the capability |
| **Working Backwards from Behavior** | Design methodology: "Behavior we want → Harness design to achieve it" — every component must trace to a specific behavioral requirement |
| **Hooks as Enforcement Layer** | Before-tool-call, after-file-edit, and before-commit hooks that block destructive actions silently but inject errors verbosely |
| **Tool Discipline** | Ten focused tools beat fifty overlapping ones — sloppy external integrations (unverified MCP servers) inject bad prompts before the agent starts |
| **Harness-as-a-Service (HaaS)** | Industry transition from LLM APIs (completions) to Harness APIs (runtimes) — select, configure, focus on domain logic |
| **Convergence Dynamic** | Top coding agents look more like each other than their underlying models do — harness patterns are converging on load-bearing scaffolding |
| **Harnesses Don't Shrink, They Move** | Better models don't eliminate scaffolding — outdated complexity is replaced with new scaffolding for newly-reachable tasks |
| **Post-Training Feedback Loop** | Models are post-trained with specific harnesses, creating tight coupling between model and harness design |

## Critical Thinking in the Agentic Era (Nov 2026)

X Article *"Critical thinking when agents do the work"* (2026-11-03, ~17K bookmarks / 1.1M impressions): Osmani's manifesto on maintaining critical thinking when agents do most of the work. Core contributions:

- **Three-step spectrum**: cognitive offloading → **deferral** (output becomes your input; ceases to be a hypothesis) → cognitive surrender. Drift is invisible because each step is individually reasonable.
- **Improving models raise the surrender risk**: fewer obvious errors means outputs "won't demand a second look"; pleasantness relaxes vigilance.
- **Verification can be surrendered too**: green checks inflate when agents write tests cheaply; "Did the check turn green?" replaces "Is there evidence?" Define "verified" upfront — post-facto you'll rationalize any outcome.
- **Answerability bar**: "Would I bet on this in front of the person who has to maintain it?"
- **Good prompting = critical thinking skill**: your prompt reflects your understanding; intent debt can only be fixed by you. Andy Clark's delegation-vs-collaboration distinction (mutual amplification loop).
- **Accountability is non-offloadable**: even if models out-detect humans, "someone is responsible for what ships" — cites Anthropic's *paradox of supervision*.
- **Calibration practices**: weekly agent-free coding, monthly skill-audit, quiz-yourself-before-merge, read command output before the summary, always ask "Did I miss anything?"

See [[concepts/cognitive-surrender]] for the full breakdown.

### The Code Nobody Reads (Sep 2026)

Substack *"The Code Nobody Reads"* (2026-09-28): Osmani reverses his own 2024 "review every line" advice. Line-by-line human reading is going away for most code — but **review (someone deciding what ships and being answerable for it) is not**. Two contrasting posts framed the debate: Thorsten Ball's "code review will die" (the destination) vs. the viral "pressing enter on code nobody reads" engineer post (8M+ views; what happens when a company drives there without building the road). His position: every industry will stop reading most code line by line *once it has some other good reason to trust that code*; how fast depends on two costs — the cost of checking work nobody read, and the cost of undoing a failure the checks miss. Cites Madeleine Clare Elish's **moral crumple zone** (the human nearest an automated system absorbs blame they had no power to prevent) and the Teleport case study (13 engineers + frontier models found two years' worth of security bugs in one quarter; discovery got cheap, triage didn't). Advice: know what's worth reading; build checks independent of whatever wrote the code; write down what you're building before an agent builds it; be able to explain everything you ship; give people authority matching their accountability.

### Brownfield Agentic Engineering (Sep 2026)

Blog *"Brownfield Agentic Engineering"* (2026-09-14): running agents in a codebase older than the team. Core ideas:
- **Zones**: green (good tests, isolated → tight agent loop), yellow (mixed → characterization tests first), red (auth/billing/payroll → human pairing or no go). Three rules: a person draws the map (not the agent — agents gravitate to the scariest file); zones only move when earned; the zone sets the verbs.
- **Write down what the code can't say, and nothing else** — agents infer most from code; supply only team nuance, trade-off rationale, unenforced conventions, historical context.
- **Autonomy follows blast radius, observability, recoverability** — model confidence is a poor guide.
- **Parallelize last** — parallelism multiplies the bottleneck you already have; copy the software-factory parallelism only after one unit has a dependable judge, recovery path, and review format.
- **Agents put a price on ambiguity** — tribal conventions become recurring review comments; track lead time, review minutes, escaped defects, oracle mismatches — not lines generated.

### Agentic Verification (Oct 2026)

Substack *"Agentic Verification"* (2026-10-14): "To make your agent produce high-quality output, equip it with a way to check its work." The shift is from "review every line" to "build loops the agent can run itself" — the "at scale" in agent code quality comes from verification, because agents make checking cheap (tests, benchmarks, specs, e2e runs become low-cost asks). Invest in: e2e tests as ground truth, property-based tests ("examples say what should happen; properties say what must not"), differential testing for replacements, fast deterministic test loops (slow loops teach the agent to retry, not to fix). Compound taste: when the agent gets something wrong, write it down (config, hook, test) so it never happens twice. The human still owns what ships — but reviews **evidence, not just diffs**.

## Software Factories, Light and Dark (July 2026)

X Article *"Software Factories, Light and Dark"* (2026-07-21, 1.6M impressions): a software factory is **harnessed loops at scale**, tracing the dream back to Bob Bemer's 1968 "The Economics of Program Production." The stack is three layers: **the loop, the harness, the factory** — "the loop is the atom, the factory is the loop at scale." A **light factory** keeps humans in the loop (trading judgment/concentration against speed/breakage); a **dark factory** ignores them — "if people stop reading, they'll stop understanding your software." Cites Dex Horthy's AIEWF talk "Harness Engineering is not Enough: Why Software Factories Fail." Engineers must own the **outer loop** (decide the right fix, verify soundness, approve, carry consequences); the boundary between inner and outer loops is evidence — diffs, tests, logs, a connecting explanation. "Robots are fine operating in the dark, but humans need to see what they're doing."

## Taste, Judgment and AI (Aug 2026)

X Article *"Taste, Judgment and AI"* (2026-08-03): **Taste** = recognizing quality/greatness in the absence of all the evidence; **judgment** = committing to it in the presence of risk. Taste is built by reps — enough exposure to the best human work to pick the best of a dozen ambiguous options. Practice: move past "I like/hate this," ask *why* something succeeds or fails; study different versions of the same thing; for judgment, make the hard calls, write down your prediction, and stay close enough to the outcome to learn from being wrong.

## Do You Need a Software Factory? (Aug 2026)

X Article *"Do you need a software factory?"* (2026-08-27): before building a factory, keep humans upfront on **product intent, system design, and quality bar**. Review code (lights-on factory) but intentionally — watch where automated back-pressure breaks and where maintainability trade-offs need humans. Get quality checks as early and continuous as possible (types, tests, mutation testing, security scanners, architecture lint); **number of checks ≠ quality** — tune for signal-to-noise, tighten/relax deliberately. Encode human taste in the environment, have the agent produce evidence, and keep a human owner of what ships. "The best software factories will not be defined by how completely they eliminate human involvement — they will be defined by how intelligently they place it."

## Claude Code Team Practice (Oct 2026)

Three X Articles from Osmani's move to Anthropic working on Claude Code:

- **"How the Claude Code team does code review"** (2026-10-26, 34.7K bookmarks / 2.6M impressions): Claude writes ~90% of Claude Code's code. June–Sep 2026: merged PRs more than doubled while the revert share **fell 40%+**; monorepo merges went from ~2,500/day (May) to 30,000+/day (Sep). They didn't stop review — they **automated the majority of reading**, optimized for human time, and invested heavily in fast/easy reverts. Every reviewer miss becomes a CLAUDE.md entry, skill, or new check ("what wasn't in the model's context?"). Owners now decide which low-risk changes auto-merge when checks pass.
- **"Getting started with Claude Code Mods"** (2026-10-28): Mods are small JS/TS files run inside a Claude Code session — react to events, modify/override Claude Code behavior, render custom interfaces (terminal + desktop). Create one by simply describing it to Claude (no API learning needed); hot-reload, persist, distribute via marketplaces. Beyond config/permissions/slash commands/skills/status lines.
- **"You're probably overprompting Claude"** (2026-10-29): newer models (Opus 5.5) need far less prompting — one prompt with a clear goal + how to verify it, start `/effort medium`. If you don't know what you want, have Claude interview you into a spec, then build in a fresh session. `/goal` attaches a separate checker model per turn for long background tasks. Audit your workflow every few months: "make sure you aren't building for how older models used to work."

## Key Publications

| Title | Date | Platform |
|-------|------|----------|
| Agent Harness Engineering | Apr 2026 | addyosmani.com |
| The Future of Agentic Coding: Conductors to Orchestrators | Nov 2025 | O'Reilly Radar + addyosmani.com |
| Claude Code Swarms | Feb 2026 | addyosmani.com |
| The Code Agent Orchestra | Mar 2026 | O'Reilly CodeCon + addyosmani.com |
| Self-Improving Coding Agents | 2026 | addyosmani.com |
| Your AI Coding Agents Need a Manager | 2026 | addyosmani.com |
| Stop Using /init for AGENTS.md | Mar 2026 | Medium + addyosmani.com |
| Orchestrating Coding Agents (talk) | Mar 2026 | O'Reilly CodeCon 2026 |
| 2026 Agentic Coding Trends Guide | 2026 | addyosmani.com |
| From Prompting Agents to Loop Engineering (cited) | Jun 2026 | DAIR.AI Academy |
| Loop Engineering (Orange Book v260615) | Jun 2026 | huasheng.ai/orange-books |
| Agentic Code Quality | Aug 2026 | X Article |
| Software Factories, Light and Dark | Jul 2026 | X Article + addyosmani.com |
| Taste, Judgment and AI | Aug 2026 | X Article |
| Do you need a software factory? | Aug 2026 | X Article |
| Brownfield Agentic Engineering | Sep 2026 | addyosmani.com + Substack |
| The Code Nobody Reads | Sep 2026 | addyo.substack.com |
| Agentic Verification | Oct 2026 | addyo.substack.com |
| How the Claude Code team does code review | Oct 2026 | X Article |
| Getting started with Claude Code Mods | Oct 2026 | X Article |
| You're probably overprompting Claude | Oct 2026 | X Article |

## Speaking

- **O'Reilly CodeCon 2026** (Mar 26) — "Orchestrating Coding Agents: Patterns for Coordinating Agents in Real-World Software Workflows"
- Regular speaker on AI-assisted development, web performance, and developer experience

## X/Twitter Activity Pattern

Osmani uses X to:
- Announce new **frameworks and patterns** for agentic coding
- Share **practical tips** from his daily work with Claude Code, Gemini, and other tools
- Engage with the **developer community** on tool adoption, quality concerns, and productivity metrics
- Cross-post his **blog articles** with distilled takeaways
- Respond to **emerging trends** (agent swarms, AGENTS.md debate, multi-agent coordination)

His posting style is **educational and systematic** — he builds frameworks, creates cheat sheets, and produces structured guides rather than hot takes.

## AI Engineer World's Fair 2026: Agency Ladder

At the AI Engineer World's Fair (July 2026), Osmani delivered a talk that directly challenged the fully autonomous software factory vision. His core framing:

> "Agents can run much more of the inner execution loop. But that outer loop is still engineering."

Osmani introduced the **Agency Ladder** concept to distinguish capability from agency:

| Level | Description |
|-------|-------------|
| **Inner execution loop** | What agents do — write code, run tests, fix bugs. **Capability.** |
| **Outer loop (engineering)** | What humans must retain — setting goals, evaluating results, making architectural decisions. **Agency.** |

> *"That inner loop is capability. The outer loop is agency."* — Addy Osmani, AIEWF 2026

This framing positions Osmani in the "human outer loop" camp, alongside Geoffrey Litt (anti-factory thread) and Paul Bakaus (Impeccable — "there is no auto"), as opposed to the autonomous factory vision of Introspection and Cursor.

## Recent X Shares (Aug 2026)

- **Lars Faye, "AI Coding will Prevent Expertise"** (shared Aug 26, 2026, [larsfaye.com](https://larsfaye.com/articles/ai-coding-will-prevent-expertise)): Osmani's one-liner — *"Friction is what builds taste and mastery. The tools that remove it also remove what made us good enough to use them well. Worth reading if you're leading teams or are an early-career engineer."* The article argues the **Expert Novice paradox** (AI coding demands the expertise that AI-assisted learning suppresses), cites the JetBrains "Widening Gap" novice study (heavy AI users developed an "illusion of competence"; those who mitigated AI use performed best via "negative expertise") and UPenn's 1,000-student math study (unassisted LLM use → 17% worse results, self-assessments inverted), and prescribes **Friction First**: use LLMs as Socratic tutors/documentation rather than code generators. A sharp counterweight to Osmani's own productivity-leaning agentic-coding content — he's curating the skeptic case for his audience. Full notes: [[raw/articles/2026-08-26_larsfaye_ai-coding-will-prevent-expertise]].

## Open Source & Projects

- Extensive contributions to **Chrome DevTools** and web performance tooling
- Author of **Learning JavaScript Design Patterns** (O'Reilly)
- Contributor to numerous open-source web development tools

## Related

- [[entities/lester-solbakken]] — Search infrastructure researcher; HORNET founder
- [[entities/elvis-sun]] — Fellow agentic engineering commentator; shared harness-engineering and vibe-coding interests
- [[concepts/harness-engineering]]
- [[concepts/multi-agents/multi-agent-autonomy-scale]]
- [[concepts/context-engineering|Context Engineering]]
- [[entities/boris-cherny]]
- [[entities/ryan-lopopolo]]
- [[concepts/karpathy]]
- [[entities/simon-willison]]

## Sources

- [The Future of Agentic Coding](https://addyosmani.com/blog/future-agentic-coding/) (Nov 2025)
- [Claude Code Swarms](https://addyosmani.com/blog/claude-code-agent-teams/) (Feb 2026)
- [The Code Agent Orchestra](https://addyosmani.com/blog/code-agent-orchestra/) (Mar 2026)
- [Stop Using /init for AGENTS.md](https://medium.com/@addyosmani/stop-using-init-for-agents-md-3086a333f380) (Mar 2026)
- [O'Reilly CodeCon 2026 Talk Slides](https://talks.addy.ie/oreilly-codecon-march-2026/) (Mar 2026)
- [Addy Osmani's Blog](https://addyosmani.com/)
- [[raw/articles/2026-06-19_omarsar0_from-prompting-agents-to-loop-engineering]] — Elvis Saravia (DAIR.AI), "From Prompting Agents to Loop Engineering" (Jun 19, 2026). References Osmani on AI-assisted coding loops.
- [[raw/articles/2026-08-12_addyosmani_agentic-code-quality]] — "Agentic Code Quality" (Aug 12, 2026). X Article on quality gates, constraints, and back-pressure as the foundation of agentic code quality.
- [[raw/articles/2026-11-03_addyosmani_critical-thinking-when-agents-do-the-work]] — "Critical thinking when agents do the work" (Nov 3, 2026). X Article on offloading→deferral→surrender spectrum and verification habits.
- [[raw/articles/2026-09-14_addyosmani_brownfield-agentic-engineering]] — "Brownfield Agentic Engineering" (Sep 14, 2026). Zones, blast radius, and cheap-trustworthy changes in old codebases.
- [[raw/articles/2026-09-28_addyosmani_the-code-nobody-reads]] — "The Code Nobody Reads" (Sep 28, 2026). Substack on the end of line-by-line review and what replaces it.
- [[raw/articles/2026-10-14_addyosmani_agentic-verification]] — "Agentic Verification" (Oct 14, 2026). Substack on building verification loops agents can run themselves.
- [[raw/articles/2026-07-21_addyosmani_software-factories-light-and-dark]] — "Software Factories, Light and Dark" (Jul 21, 2026). X Article on loop/harness/factory stack and light vs dark factories.
- [[raw/articles/2026-08-03_addyosmani_taste-judgment-and-ai]] — "Taste, Judgment and AI" (Aug 3, 2026). X Article on taste as reps-built recognition and judgment under risk.
- [[raw/articles/2026-08-27_addyosmani_do-you-need-a-software-factory]] — "Do you need a software factory?" (Aug 27, 2026). X Article on where to place humans in a factory.
- [[raw/articles/2026-10-26_addyosmani_claude-code-team-code-review]] — "How the Claude Code team does code review" (Oct 26, 2026). X Article: 30K merges/day, revert rate -40%, automated reading.
- [[raw/articles/2026-10-28_addyosmani_claude-code-mods]] — "Getting started with Claude Code Mods" (Oct 28, 2026). X Article on JS/TS mods for Claude Code.
- [[raw/articles/2026-10-29_addyosmani_overprompting-claude]] — "You're probably overprompting Claude" (Oct 29, 2026). X Article on minimal prompting for Opus 5.5.
