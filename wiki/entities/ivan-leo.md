---
title: "Ivan Leo"
created: 2026-05-13
updated: 2026-09-05
type: entity
status: L3
tags:
  - person
  - ai-agents
  - harness-engineering
  - coding-agents
aliases: [ivan-leo,'@ivanleomk']
sources:
  - raw/articles/2026-02-28_substack_agents-that-build-themselves.md
  - raw/articles/2026-02-28_youtube_openclaw-from-scratch-workshop.md
  - raw/articles/2026-03-28_youtube_deep-research-agent-workshop.md
  - raw/articles/2026-09-05_ivanleo_blog-scrape.md
  - transcripts/2026-02-28_youtube_openclaw-from-scratch-workshop.md
  - transcripts/2026-03-28_youtube_deep-research-agent-workshop.md
---

# Ivan Leo

**AI engineer and educator.** Formerly at **Manus** (the viral general-purpose AI agent startup later acquired by Meta). Currently at **Google DeepMind**. Co-hosts live coding workshops with Hugo Bowne-Anderson on Vanishing Gradients, teaching practical AI agent construction from first principles.

## Basic Info

| Field | Value |
|---|---|
| Current | Google DeepMind |
| Previous | Manus (acquired by Meta, 2026) |
| Known For | Self-extending agents, agent architecture, live coding workshops |
| Collaborators | [[entities/hugo-bowne-anderson|Hugo Bowne-Anderson]] |
| Blog | [ivanleo.com](https://ivanleo.com) |

## Key Contributions

### "Building Agents That Build Themselves" Workshop (Feb 2026)

Co-hosted a 96-minute live build session with Hugo Bowne-Anderson, reconstructing Pi/OpenClaw design patterns in pure Python:

- **Factory pattern for tools**: Designed the `AgentTool` base class + `AgentRuntime` that auto-generates function calling schemas from Pydantic type hints
- **Hot reload mechanism**: `importlib.reload()` triggered by `st_mtime` checks — agent writes a new tool class, runtime detects it, tool is registered instantly
- **Hooks architecture**: `on_model_response` / `on_tool_call` / `on_tool_result` event system that decouples I/O from core agent logic
- **Memory compaction**: Timestamped Markdown summaries — no vector DB, no embeddings

> *"All you need to implement a new tool is define the parameters you want. These are automatically converted into a schema. And you can test your execute function independently of your model being called."*

### Deep Research Agent Workshop (Mar 2026)

Co-hosted a separate 89-minute workshop with Hugo Bowne-Anderson, building a deep research agent from raw Gemini API calls through 10 progressive steps:

1. Raw API call → 2. Single tool → 3. Tool runtime → 4. State & context → 5. Hooks → 6. Agent loop → 7. Subagents (parallel Exa search) → 8. Beautiful outputs → 9. Plan generation (phase swapping) → 10. OpenTelemetry

Key patterns introduced:
- **Phase swapping** — `mode: "plan" | "execute"` in RunState. Plan mode restricts tools to `generate_plan` only; execute mode unlocks the full tool set
- **Deterministic guardrails** — `state.is_incomplete()` check forces the agent to finish todos before responding
- **Dynamic subagent spawning** — parent agent spawns arbitrary child agents with independent RunState and iteration budgets

> *"Manus had no choice but to build their own runtime. When you're shipping to millions of users, you need control over every layer."*

See [[concepts/deep-research-agent-from-scratch]] for the full 10-step pipeline.

## Career Trajectory

Ivan's path through the AI agent ecosystem, as described across both Vanishing Gradients workshops:

1. **567 / Jason Liu** — Early work on voice AI and the `instructor` library. Ivan credits Jason Liu for the foundational **"context vs. capabilities"** framework that shaped his agent design thinking
2. **Cura** — Built agent trace observability tooling: clustering agentic traces to extract signal. Hugo Bowne-Anderson: *"Cura in terms of clustering and having observability into agentic traces was super powerful"*
3. **Manifold** — Built Manifold Agent and Manifold Mail (email agent product)
4. **Manus** — General-purpose AI agent startup (later acquired by Meta). Built production agent runtime serving millions of users; went through 5+ runtime re-architectures
5. **Google DeepMind** — Joined March 2026 (started on a Monday, the day before the deep research workshop). Focused on spreading adoption of Gemini for agentic use cases. *"I started on Monday and it's been absolutely incredible. I think everyone is so friendly and I'm just really hoping to spread the good word about Gemini."*

Ivan was introduced to Hugo by **Swyx** from Latent Space when Hugo visited Singapore.

## Teaching Style & Philosophy

Across both workshops, Ivan demonstrates a consistent pedagogical approach:

- **"Start with the best model, then optimize down"** — Verify the task is achievable with the most capable model first; cost-optimize later. *"Spend today for the models of tomorrow. If you spend money for the models of tomorrow, you just want to use the best models to make sure it's possible."*
- **First-principles deconstruction** — Deliberately avoids frameworks; builds everything from raw SDK + Pydantic + FastAPI so viewers understand each layer
- **Context vs. capabilities** — His key mental model (attributed to Jason Liu): context = information in the prompt; capabilities = tools the model can call. *"If you ask the model 'what's the date today?' and it doesn't have the date in the prompt or a bash tool, it can never answer. That's a capability. A capability is a tool it can execute."*
- **Meta-prompting** — Uses the LLM to improve its own prompts: asked Gemini to rewrite system prompts based on initial input/output pairs, then iterated. *"A lot of it was me just asking Gemini, 'Hey, here are some examples of writing I like. You try to do a simple rewrite.' And then I would say, 'Based on the initial information that you understood, the final result that I wanted, how could we make our instructions clearer?'"*
- **"Don't break your cache"** — Production lesson from Manus: changing a tool's `description` invalidates cached function calling schemas and breaks model behavior
- **Meta-prompting for tool design** — *"You can do things like ask models, 'How should we describe tools? What sort of tools do you need? What are the descriptions of tools that you want? And what sort of information are you not getting in your system prompt?'"*

> *"The scene has just shifted so fast. What was an agent just a year ago or six months ago has just changed tremendously."* — Ivan Leo, Feb 2026 workshop

### Notable Quotes

- *"Instead of just a single run of sub-agents, really what we've done is written a way that the model can just spawn as many sub-agents as it needs on demand."*
- *"A lot of times when you work with a base model, you want to see how good the model is at its core, then you start thinking about extending in terms of capabilities, then in terms of context."*
- *"If you spend enough tokens, you let the model run long enough, either it goes into a doom loop or it finds your answer."*
- *"These models are good enough now whereby you can basically do a lot of meta prompting."*

### Blog (ivanleo.com)

Technical deep-dives on agent architecture published at [ivanleo.com](https://ivanleo.com). Full essay inventory scraped 2026-09-05 ([[raw/articles/2026-09-05_ivanleo_blog-scrape]]):

- [Value Maxxing](https://ivanleo.com/blog/value-maxxing) (Sep 2026) — Anti token-burn-anxiety: "burning tokens is just a byproduct"; start from small everyday friction, encode "good" into prompts/skills/scripts, and customize software to your exact routine (his Korean-learning workflow: Grokbot Telegram vocab drills, generated quiz web apps, Gemini TTS audio lessons)
- [How Simple Grep Beats Naive SQL](https://ivanleo.com/blog/grep-beats-sqlite-fts) (Jun 2026) — Benchmark: raw bash (grep/view_file) beat naive SQLite FTS on 300k-token / 94-file Google API docs corpus — 29.6% cheaper, 33.8% fewer conversation steps on multi-hop retrieval. Code: `ivanleomk/agent-search`; traces on Harbor Hub
- [Three Lessons I've Learned at Manus](https://ivanleo.com/blog/three-lessons-manus) (Dec 2025) — See Manus section below
- [Agentic Search](https://ivanleo.com/blog/agentic-search) (Oct 2025) — Building self-sufficient context gathering: Exa web search + grep/glob + bash; "what separates a command-line tool from a true AI assistant? the ability to find its own answers"
- [Building a Coding CLI with React Ink](https://ivanleo.com/blog/migrating-to-react-ink) (Jul 2025) — readlines → React Ink migration with streaming and tool-call refactoring
- [Building Reliable LLM Applications](https://ivanleo.com/blog/building-reliable-llm-applications) (Jan 2025, NUS talk write-up) — deploy-first paradigm inversion, structured outputs beyond raw JSON, Kura for query understanding, synthetic-data validation
- Eval trilogy (Nov–Dec 2024): [Write Stupid Evals](https://ivanleo.com/blog/write-stupid-evals), [Simplify your LLM Evals](https://ivanleo.com/blog/writing-extraction-evals) (binary evals for subjective tasks), [Are your eval improvements just pure chance?](https://ivanleo.com/blog/report-error-bars) (error bars for LLM evals), plus [You're probably not doing experiments right](https://ivanleo.com/blog/running-better-experiments) (Nov 2024)
- [How Instructor Works](https://ivanleo.com/blog/how-does-instructor-work) (Sep 2024) — from_openai / AsyncOpenAI / response_model internals

### Manus tenure (Jul–Mar 2026) — from "Three Lessons I've Learned at Manus" (Dec 22, 2025)

Joined Manus July 27, 2025; on Dec 17, 2025 Manus announced **$100M ARR in 8 months** — the fastest startup ever to that milestone. Ivan's shipped artifacts from this period: Mail Manus (with demo video), the Manus API (became its main developer after weekend bug-fixes), a Stripe integration he validated with real charges on his personal credit card, file suggestions (UX rework: sequential 7s spinner → instant-feel flow with content-type discovery), an AI Engineer Summit NY talk, and internal use of **Kura** (a clustering library he brought with him) to analyze failure modes across Manus's 17+ locales.

Three lessons:
1. **Your responsibility doesn't end when you ship** — ownership spans first commit to last user: demos, docs with marketing, answering support on X, watching non-engineers use the product to find where it breaks
2. **Prototypes over plans** — first-day task: email-trigger demo shipped live by Friday ("if it's not real, what's the point?" — boss Panpan); working prototypes buy investment decisions better than documents; scaffolding-balance discovery only comes from fast prototyping against model base tendencies
3. **Don't pigeonhole yourself** — job title is "AI engineer," actual job is achieving the desired effect: wrote production Go learned by immersion (read PRs, use models to parse unfamiliar patterns, "be wrong fast" with small PRs, ask well-framed questions)

Bar for shipping: a feature has to be "fucking sick or it doesn't ship. Any model with a basic harness can build a landing page. We're chasing the tasks that make you go 'holy shit.'"

## Google DeepMind (Mar 2026–present)

Announced via X on **2026-03-25**: "Life update — I've moved to San Francisco and joined @GoogleDeepMind," joining a developer-relations/DevRel orbit around Logan Kilpatrick, Philipp Schmid, Clemencia Serejo Paige, Thorin Kliesath, and others. Role emphasis per his own posts: spreading Gemini for agentic use cases and developer evangelism.

Observed activities (2026):
- **Vanishing Gradients deep-research workshop** (Mar 28, 2026) delivered two days after starting — built on Exa + Gemini 3 models
- **Developer hackathons**: Google DeepMind hackathons including a Stanford edition; recruiting posts ("Join the @GoogleDeepMind team and hack with us")
- **Science Skills**: `ivanleomk/science-skills` — "GDM Science Skills to speed up agentic scientific workflows with better grounding"; promoted in Value Maxxing alongside Antigravity + AlphaGenome/UniProt literature-lookup workflows
- **Antigravity demos** (`ivanleomk/Antigravity-Demo`) and **Kaggle benchmark hosting** (`kaggle-benchmark-starter-template`)
- **FDE-style tooling**: `gdm-trace-analysis` — support-agent traces → loss-pattern analysis take-home (Sep 2026)
- Also active as an **angel investor** in the agent space ("Looking to angel invest in a few more startups this year," 2026)

## Open-Source Footprint

GitHub ([@ivanleomk](https://github.com/ivanleomk), Singapore-based, 212 public repos):
- **Core contributor to `instructor`** (structured LLM outputs) and **Kura** (embedding clustering library) — his GitHub bio: "Full Stack programmer turned LLM affectionado"
- **`gil`** (Apr 2026, ⭐35) — zero-ceremony ergonomic HTTP client for Zig 0.16 (JSON structs in/out, automatic gzip/deflate/zstd) — reflects his systems-side interests beyond Python
- **`agent-search`** — corpus/code for the grep-vs-FTS benchmark; **`harbor`** — port of the agent-evals/RL-environments framework; **`building-an-agent`** — Claude-based coding agent tutorial


## Design Philosophy

- **Composability over monoliths**: Hooks and factory patterns enable the agent to grow organically rather than being designed upfront
- **Async from day one**: *"When you're interfacing with databases, logging, etc., a lot of these are async. If you don't have async built in from the beginning, it's complicated down the line."*
- **Primitives over frameworks**: The workshop deliberately avoids frameworks — everything is built from `google-genai` SDK + Pydantic + FastAPI
- **Self-extension as first principle**: The agent should be able to bridge its own capability gaps

## Related

- [[entities/hugo-bowne-anderson]] — Primary collaborator
- [[concepts/agents-that-build-themselves]] — Core concept from the workshop
- [[entities/openclaw]] — OpenClaw architecture explored in the workshop
- [[entities/pi]] — Pi coding agent philosophy
- [[entities/manus]] — Former employer (Jul 2025 – Mar 2026, $75M → $100M ARR)
- [[entities/deepmind]] — Current employer (Mar 2026–present, SF)
- [[entities/logan-kilpatrick]] — DeepMind colleague / DevRel orbit
- [[concepts/self-evolving-agents]] — Related concept

## Sources

- [[raw/articles/2026-09-05_ivanleo_blog-scrape]] — Full blog essay inventory + "Three Lessons I've Learned at Manus" (scraped 2026-09-05)
- [X: @ivanleomk](https://x.com/ivanleomk) — Bio, DeepMind joining post (2026-03-25), Manus/launch posts
- [GitHub: @ivanleomk](https://github.com/ivanleomk) — 212 repos incl. instructor/Kura contributions, `gil`, `agent-search`, `science-skills`
