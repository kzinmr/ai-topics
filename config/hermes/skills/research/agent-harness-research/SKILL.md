---
name: agent-harness-research
description: Research and compare AI agent harnesses (coding/automation agents like Claude Code, Pi, OpenCode, OpenClaw, Hermes Agent) with model compatibility analysis. Covers the "Harness Effect" — how the same model performs 5-40 percentage points differently depending on the harness.
trigger: |
  When the user asks about:
    - "ハーネス" (harness) in context of AI agents/coding tools
    - Which agent harness works best with which model
    - Harness vs harness comparisons (e.g., "Pi vs OpenCode with Qwen")
    - "Harness Effect" or model-harness compatibility
    - Benchmarks across coding agents
    - agent CLI tools (Claude Code, Codex CLI, OpenCode, Pi, Aider, Cursor)
    - "HarnessとFramework/SDKの違い" (difference between harness and framework/SDK) — see §3b
    - "どのagent frameworkを選ぶべきか" (which agent framework to choose)
    - Agent infrastructure investment decisions (operator workbench vs product runtime)
  Critical trigger: User says "ハーネス" — ALWAYS interpret as AGENT HARNESS (Claude Code, Pi, OpenCode, etc.), NOT inference server (vLLM, llama.cpp, Ollama). The user's domain is coding/automation agent harnesses.
  Secondary trigger: User asks about harness engineering in domain-specific contexts (AEC, engineering report generation, non-coding agent systems). Theodoros Galanos' work on The Harness Blog demonstrates harness engineering extends beyond coding agents into knowledge-work domains.
---

# Agent Harness Research

## Domain Clarification: What "Harness" Means in This Wiki

In this user's context, **"harness" = AI Agent Harness** (coding agent / automation agent framework), NOT inference server.

| ✅ Agent Harnesses | ❌ Not Agent Harnesses |
|---|---|
| Claude Code, Codex CLI, OpenCode, Pi | vLLM, llama.cpp, Ollama (these are inference engines) |
| OpenClaw, Hermes Agent, Aider, Cursor | SGLang, TensorRT-LLM (these are model servers) |
| Cline, Windsurf, Continue | API providers (OpenAI, Anthropic, Google) |

**Why this matters**: If the user asks about "ハーネス" and you start talking about vLLM vs llama.cpp, you will get a correction. The user's interest is in **coding agent frameworks** that harness LLMs to write/edit/run code autonomously.

**Harness vs Runtime distinction (dual-perspective)**:

Within the agent stack, the **harness** and the **runtime** are distinct layers. The wiki now recognizes **two complementary views** of the runtime:

| View | Runtime as... | Key concern | Source |
|---|---|---|---|
| **Infrastructure substrate** | Compute, filesystem, network boundary, isolation primitives | *Where* and *on what* the agent runs | Han Lee (Apr 2026) |
| **Execution semantics** | Lifecycle controller, tool mediator, state keeper, scheduler, event emitter, safety enforcer | *How* execution proceeds safely and continuously | kzinmr (May 2026) |

The harness decides *what the agent attempts* (orchestration: tools, prompts, loops, context, memory, verification). The runtime manages *how execution proceeds* (lifecycle, tool mediation, state continuity, scheduling, events, safety, observability). This makes the runtime analogous to an **OS kernel** — it manages process lifecycle, scheduling, I/O mediation, permissions, eventing, and state, but at the agent execution layer rather than the hardware layer.

Han Lee's formulation: "The agent is the harness plus the model, running inside the runtime."

**Distinction from workflow frameworks**: LangGraph is closer to a **workflow framework** — it describes *execution topology* (what should happen). Claude Agent SDK and PI are closer to **runtimes** — they maintain *execution continuity* (how execution proceeds).

When the user asks about agent infrastructure, sandboxing, runtime architecture, or the harness/runtime boundary, also consult [[concepts/agent-runtime]] (especially §"Execution Semantics: The Control System Layer") and [[concepts/agent-harness]] (§"Harness vs Runtime: The Critical Distinction").

## The Harness Effect (Critical Concept)

The single most important finding in this domain: **the harness is as important as the model.**

Same model, different harness:
- Claude Opus in Claude Code: **77%** (SWE-bench)
- Claude Opus in Cursor: **93%** → +16pp from harness alone
- Claude Opus with minimal scaffold: **42%** (CORE-Bench)
- Claude Opus in full Claude Code: **78%** → +36pp

**General finding**: Multiple independent studies show the harness effect ranges from **5 to 40 percentage points** depending on model and task type.

**The runtime-centric family (kzinmr, 2026-05-15)**: ClaudeCode, Codex CLI, PI, OpenClaw, and Hermes Agent are all **runtime-centric systems** in the same architectural family — they manage *how execution proceeds* rather than describing *what execution topology should be* (workflow-centric). LangGraph and PydanticAI are workflow-centric. The key distinction is not "closed vs open" but "runtime-centric vs workflow-centric." See [[concepts/agent-runtime]] §"Execution Semantics: The Control System Layer" and [[comparisons/open-harness-vs-agent-framework]] §9.

**Root causes of harness effect:**
1. **System prompt size** — Bigger is NOT better. Pi keeps <1K tokens; OpenCode can hit 10K+. Excess system prompt degrades model reasoning.
2. **Context management** — How the harness builds context incrementally vs dumping entire codebase into prompt
3. **Tool surface area** — More tools ≠ better. Pi has only 4 core tools (read/write/edit/bash) and outperforms feature-heavy harnesses
4. **Prompt caching architecture** — Claude Code's static-first layout and cache-aware compaction are major factors
5. **Batching/scheduling** — How requests are queued and scheduled affects tail latency
6. **Reasoning architecture** — Open-ended REPL vs deterministic pipeline can produce 14x token difference +8.4% quality (Lambda-RLM). See also: [[entities/theodoros-galanos]], [[concepts/lambda-rlm]]

### The Harness Effect Beyond Coding Agents

The Harness Effect is not limited to coding agents. Theodoros Galanos demonstrated it in the AEC domain with identical models:

| Metric | Open REPL Harness | Lambda-RLM Harness | Improvement |
|--------|-----------|------------|-------------|
| Total Tokens | 740K | 53K | **14x less** |
| Quality (Reward) | 0.67 | 0.73 | **+8.4%** |

Core thesis: "The agent's reasoning architecture is itself a harness design choice. Agent design and harness design are the same problem." — Galanos argues that the line between model-level reasoning architecture (open REPL vs deterministic pipeline) and harness design dissolves completely.

**Implication**: Harness engineering applies broadly beyond coding agents to any domain-specific agent system (AEC reports, HVAC analysis, document generation). The harness effect magnitude (5-40pp for coding agents, 14x token/8.4% quality for AEC) is comparable or larger in domain-specific work.

## Research Workflow

### 1. Identify the Harnesses in Scope

Major agent harnesses to track as of May 2026. Full wiki entity pages exist for most — see [[concepts/agent-harness-comparison]] for the 9-harness comparison portal.

| Harness | Type | Creator/Org | Model Policy | Wiki Entity |
|---------|------|-------------|--------------|-------------|
| **Claude Code** | Agent orchestrator | Anthropic→OpenAI | Anthropic models ONLY (Opus 4.7, Sonnet 4.6). Subscription $20/mo | [[entities/claude-code]] |
| **OpenCode** | Model-agnostic harness | AnomalyCo/SST | **155K GitHub stars**. 75+ providers; Claude/GPT/Gemini/Grok/local. BYOK or $10/mo OpenCode Go | [[entities/opencode]] |
| **Pi** | Minimalist harness | Mario Zechner | **45.5K GitHub stars**. 20+ providers; optimized for local (MLX/GGUF). BYOK. **Anthropic wall**: Claude Max subscription NOT usable in Pi — double-billing | [[entities/pi]] |
| **Codex CLI** | Universal coding agent | **OpenAI** (Apache-2.0 OSS, 79.3K GitHub stars, Rust 96.2%) | GPT-5.5 (recommended), GPT-5.4, GPT-5.3-Codex-Spark, GPT-OSS (local), **custom providers** (DeepSeek, Qwen, etc. via config.toml), **local** (Ollama/LM Studio/MLX). Included in ChatGPT Plus/Pro/Team/Enterprise ($20-200/mo). MCP dual, sub-agents, image gen, remote TUI, code review. **Most underrated harness — commonly misreported as single-model/closed-source.** | [[entities/codex]] |
| **Copilot CLI** | GitHub-native agent | GitHub/Microsoft | 6 built-in sub-agents (explore/code-review/research/general/rubber-duck/configure). `/fleet` parallel. MCP-powered. BYOK + local models (since Apr 2026). Included in Copilot Free/Pro/Pro+/Business/Enterprise. | [[entities/copilot-cli]] |
| **Droid** | Enterprise multi-platform | Factory AI | CLI/IDE/Slack/Linear/CI/CD. 3-level Auto-Run. Specialized sub-agents (CodeDroid/Review Droid/QA Droid). SOC-2, SSO. $20-50+/mo. | [[entities/droid]] |
| **Cursor** | IDE-integrated | Cursor | Claude Opus, GPT-5, custom. Subscription $20-$200/mo | — |
| **Kilo** | All-in-one platform | Kilo Org (Apache-2.0) | **OpenCode fork** with VS Code + JetBrains + CLI. 500+ models via Kilo Gateway (zero markup). Hosted OpenClaw (KiloClaw). Teams/SSO/Analytics. Inline autocomplete, Cloud Agents, code review. Free tier + pay-as-you-go. | [[entities/kilo]] |
| **OpenClaw** | Always-on Telegram agent | Peter Steinberger / NVIDIA | Built on Pi SDK. Local via Ollama/LM Studio, or any API. MIT license. 145K+ GitHub stars. | [[entities/openclaw]] |
| **Hermes Agent** | Self-improving persistent agent | Nous Research | Multi-model via config; DeepSeek V4, Gemini, Claude, Ollama. Open-source | [[entities/hermes-agent]] |
| **Aider** | Git-first harness | Independent | BYOM (any model). Token-efficient (1/4.2 of Claude Code) | — |

### 2. Determine the Comparison Axes

When comparing harnesses, consider these dimensions:
- **Model compatibility** — which models work, any restrictions (Anthropic wall on Pi)
- **System prompt overhead** — smaller is generally better (Pi <1K, OpenCode ≤10K)
- **Autonomy level** — can it run unattended overnight? (Claude Code yes, Cursor no)
- **Token efficiency** — cost per task (Aider best at 1/4.2 of Claude Code)
- **Local model support** — GGUF, MLX, Ollama, LM Studio
- **Architecture** — CLI vs IDE vs daemon vs Telegram bot
- **Benchmark scores** — SWE-bench, Terminal-Bench, CORE-Bench
- **Runtime ownership** — Closed (vendor-controlled, co-trained with model) vs Open (developer-controlled, runtime portability). See [[concepts/agent-harness]] §"Closed Harness vs Open Harness."
- **Environment type** — Coding (filesystem/shell/git, low entropy) vs Browser (DOM/Web, medium entropy) vs Computer Use (GUI/OS, high entropy). See [[concepts/agent-harness]] §"Harness Type Comparison" for the entropy gradient.
- **Architectural family** — Runtime-centric (manages execution) vs Workflow-centric (describes topology). ClaudeCode/Codex/PI/OpenClaw/Hermes are runtime-centric; LangGraph/PydanticAI are workflow-centric. See [[comparisons/open-harness-vs-agent-framework]] §9.
- **Memory architecture** — How the harness stores and retrieves persistent knowledge across sessions. Compare file-first vs vector DB, synchronous vs async generation, bounded snapshot vs live writes, pre-compaction flush capability. See [[comparisons/agent-memory-systems-comparison]] for the full 4-harness comparison (OpenClaw/Claude Code/Codex/Hermes).

### 3. Key Sources for Harness Research

- **[[concepts/agent-harness-comparison]]** — Wiki internal: 9-harness comprehensive comparison portal with architecture, model matrix, pricing, use cases. First place to check before web searching.
- **[[comparisons/open-harness-vs-agent-framework]]** — Wiki internal: **Harness vs Framework/SDKの本質的差異** (2026-05-14). 10-tool comparison, Operator Workbench vs Product Runtime 2-axis evaluation, 4 lock-in types, 5-layer separation architecture, selection heuristics. Load this when the user asks about "HarnessとFrameworkの違い".
- **[[comparisons/coding-agent-harnesses]]** — Wiki internal: Earlier (May 1) deep-dive comparison with Japanese use-case recommendations, codex fact sheet, and the Anthropic wall analysis.
- **[[comparisons/agent-memory-systems-comparison]]** — Wiki internal: **4-harness memory architecture comparison** (OpenClaw/Claude Code/Codex/Hermes, 2026-05-17). Memory hierarchy, search/recall (vector vs FTS5 vs grep), embedding strategy, memory generation timing, pre-compaction flush, Bustamante's 3-type classification, selection guide. Load when comparing how harnesses handle persistent memory across sessions.
- **thoughts.jock.pl/p/ai-coding-harness-agents-2026** — Best overview of Claude Code vs Codex vs Aider vs OpenCode vs Pi with harness effect data
- **grigio.org/opencode-vs-pi-which-ai-coding-agent-should-you-use** — OpenCode vs Pi comparison (same model, different results)
- **Terminal Trove (terminaltrove.com)** — 43 coding agents indexed with filtering
- **disler/pi-vs-claude-code** (GitHub) — Feature-level comparison Pi vs OpenCode
- **XDA Developers** — "Tested Claude Code against 3 open-source alternatives"
- **Medium: "OpenCode vs Claude Code" by Mohit Aggarwal** — Real user comparison
- **YouTube: "Pi Coding Agent Just Destroyed Claude Code"** — Independent testing
- **MightyBot "Best AI Coding Agents 2026"** — Ranked list with reasoning
- **[[concepts/agent-runtime]]** — Wiki internal: The execution environment where harness + model operate. **Dual perspective**: (1) infrastructure substrate (isolation primitive stack, sandbox-as-a-service, runtime shift, runtime debt — Han Lee, Apr 2026); (2) execution semantics (8 responsibilities: lifecycle, tool mediation, state continuity, environment mediation, scheduling, events, safety/policy, observability — kzinmr, May 2026). Includes Model↔Runtime separation table, Workflow Framework vs Runtime System distinction, completion-centric→agent-centric transition. Load this when the user asks about agent infrastructure, sandboxing, runtime architecture, or why the runtime matters for harness performance. **Wiki**: [[concepts/agent-runtime]], [[concepts/agent-harness]] (§"Harness vs Runtime"), [[entities/han-lee]], [[raw/articles/2026-04-24_leehanchung_hidden-technical-debt-agent-runtime]], [[raw/articles/2026-05-15_kzinmr_agent-runtime-execution-semantics]]\n- **The Harness Blog (theharness.blog)** — Harness engineering and agentic AI for AEC (Architecture, Engineering, Construction). 25+ posts by Theodoros Galanos. Key articles: "Recursive by Design" (Lambda-RLM, 14x token reduction), "The Harness Is All You Need" (domain-specific harnesses > bigger models). Contains concrete production metrics for harness effect outside coding agents. **Wiki entities**: [[entities/the-harness-blog]], [[entities/theodoros-galanos]]
- **[[concepts/why-harness-development-boom]]** — Wiki internal: Five structural forces driving the acceleration of harness development (Harness Effect magnitude, compound advantage, framework ceilings, scale evidence, architectural moat). Includes decision framework for when to build your own. Primary source: Kartik Labhshetwar's article.
- **Kartik Labhshetwar (@code_kartik)** — Key voice on harness engineering at Mem0. Published "Why Everyone Is Suddenly Building Their Own Agent Harness" (May 2026, 164K views) with the deepagents-cli case study: 52.8%→66.5% (+13.7pp) on Terminal-Bench 2.0 by changing only the harness (same GPT-5.2-Codex model). Also "Why Production Agents Read 100 Tokens for Every 1 They Write" (May 2026). **Wiki entity**: [[entities/kartik-labhshetwar]]
- **Hugo Bowne-Anderson (Vanishing Gradients)** — Central hub for harness engineering discourse. Curated the definitive **Agent Harness Reading List** (May 2026) with Doug Turnbull. Hosted critical conversations: Lance Martin (Anthropic) on **Reduce/Offload/Isolate** — Anthropic's playbook for stripping harness complexity as models improve; Jeff Huber (Chroma) on context engineering inner/outer loop; Ivan Leo (ex-Manus, Google DeepMind) on self-extending agents. The reading list is at: https://open-racer-a67.notion.site/The-agent-harness-reading-list-35e14bb7e4a2805d881ae261573ff76f . **Wiki entity**: [[entities/hugo-bowne-anderson]]
- **Lance Martin (LangChain) — Reduce, Offload, Isolate**: Articulated the 3-principle context engineering playbook on High Signal podcast (Dec 2025). Critically, Anthropic *removes* harness features as models get smarter — the Bitter Lesson applied to harness design: "Anthropic rips out Claude Code's harness as models improve." Martin works at LangChain (not Anthropic); he observed and analyzed Anthropic's approach. The three principles: (1) **Reduce** — strip non-essential context from the prompt; (2) **Offload** — move computation outside the prompt (deterministic pre/post-processing, filesystem as external memory, bash terminal over 100 tools); (3) **Isolate** — delegate token-heavy work to sub-agents with independent contexts. Production evidence: Manus re-architected 5x since March 2024, LangChain's Open Deep Research rebuilt multiple times in a year. Martin's earlier framework (Jun 2025) used Write/Select/Compress/Isolate — the Dec 2025 reframing reflects maturing understanding that context is the scarcest resource. **Wiki**: [[concepts/reduce-offload-isolate]] (full concept page), [[entities/lance-martin]] (entity), [[entities/hugo-bowne-anderson]] (Agent Harness Engineering section)
- **Kilo Blog / Kilo Reddit Analysis** — Two-part primary source on OpenClaw vs Hermes Agent: (1) [Hermes vs. OpenClaw - When to Reach for Which Agent](https://blog.kilo.ai/p/hermes-vs-openclaw-when-to-reach) by Brendan O'Leary (May 6, 2026) — design philosophy comparison, pitfalls, cost analysis, and the "use both" orchestrator+executor recommendation; (2) [OpenClaw vs Hermes: 1,300 Reddit Comments Analyzed](https://kilo.ai/openclaw/vs-hermes) — community sentiment breakdown (~35% OpenClaw only, ~30% Hermes only, ~20% both, ~15% distrust Hermes), with direct quotes and architecture validation. **Wiki**: [[raw/articles/2026-05-06_kilo_hermes-vs-openclaw-when-to-reach]], [[comparisons/hermes-vs-openclaw-architecture]] (has full orchestrator+executor evidence section). **Skill reference**: `references/openclaw-orchestrator-evidence-deck.md` — condensed 8-source evidence deck supporting OpenClaw as orchestrator.\n- **popularaitools.ai — Hermes Agent vs OpenClaw** — Confirms speed advantage ("significantly faster than OpenClaw on the same model"), dual-agent recommendation (ACP bridge), and practical multi-agent workflows. Source: https://popularaitools.ai/blog/hermes-agent-vs-openclaw\n- **John Berryman (Arcturus Labs) — Unharnessed Agents**: The anti-harness thesis. Berryman argues "agent harness" is the wrong frame entirely: the agent IS the whole composition (while loop, LLM calls, tool calls, context management, skills, MCP). Agents should leave the IDE and become personal assistants, interface builders, workflow operators. Skills are the new programs; English is the new programming language; agents are the new runtime. We need standardized, pluggable agent primitives (Lego blocks). Source: [Unharnessed Agents Power the Future of AI Products](https://arcturus-labs.com/blog/2026/04/24/unharnessed-agents-power-the-future-of-ai-products/) (April 2026). **Wiki entities**: [[entities/john-berryman]], [[concepts/unharnessed-agents]]

### 3a. The Harness Dialectic: Amp vs Berryman

Two complementary theses define the poles of the harness debate. When researching harness topics, always consider both:

| | Amp / [[entities/thorsten-ball|Thorsten Ball]] | Berryman / [[entities/john-berryman|Arcturus Labs]] |
|---|---|---|
| **Core claim** | Harness differentiation is dead — models absorb harness features | "Harness" is the wrong frame — call them agents |
| **Direction** | Harness → Model (vertical: models eat harnesses from above) | Harness → Agent (horizontal: rename and expand scope) |
| **What dies** | The harness as competitive moat | The term "harness" and IDE-centric mindset |
| **What comes next** | Codebase organization, model-native features | Standardized agent primitives, agents as universal runtime |
| **Convergence** | ✓ Current harness framing is limiting | ✓ Harnesses are too opinionated/opaque |
| **Wiki page** | [[concepts/harness-commoditization]] | [[concepts/unharnessed-agents]] |

Both imply that today's harness products (Claude Code, Cursor, Codex, OpenCode) are **transitional forms** — not the end state.

### 3b. Harness vs Agent Framework/SDK — The Investment Distinction

When the user asks about "HarnessとFrameworkの違い" (difference between Harness and Framework/SDK), consult this section AND the wiki's comprehensive comparison at [[comparisons/open-harness-vs-agent-framework]] (created 2026-05-14 from kzinmr's analysis).

**Core distinction**: These are two different **investment targets**, not two flavors of the same thing.

| | Open Harness | Agent Framework / Runtime |
|---|---|---|
| **Invests in** | Human-facing operation surface (使う面) | System-facing control substrate (組み込む面) |
| **Primary user** | Developer, operator, individual, small team | Product team, enterprise workflow team |
| **Flexibility type** | **Broad** — model switching, channel selection, prompt tweaking | **Deep** — typed state, graph transitions, tenant isolation, durable execution |
| **Security model** | **Operator Safety** — trusted human using agent safely | **Product/Tenant Safety** — untrusted users, multi-tenant isolation |

**Two-axis evaluation framework** (don't use a single "Security/Control/Ops" score):
1. **Operator Workbench Readiness** — How mature is this as a trusted operator's workbench? (OpenClaw, Hermes, OpenCode, Pi rate high here)
2. **Untrusted Product Runtime Readiness** — How mature is this as a multi-tenant SaaS backend? (LangGraph, Pydantic AI, OpenAI Agents SDK rate high here)

**Four lock-in types** to analyze separately, not just "vendor lock-in":
1. **Model lock-in** — Claude Agent SDK (Claude-only), OpenAI Agents SDK (Responses API-dependent)
2. **SDK lock-in** — Framework abstractions (handoff, guardrail, graph state) — acceptable for good abstractions
3. **Harness lock-in** — Open Harness config assets (AGENTS.md, extension, memory, skills, gateway routing) — open source ≠ no lock-in
4. **Cloud lock-in** — Google ADK (GCP), Strands (AWS/Bedrock)

**Recommended architecture**: 5-layer separation (Harness → Tool Boundary → Agent Control → State & Governance → Execution). Design principle: **"Harnessを捨てても業務ロジックが残る"** (business logic survives even if you abandon the harness).

**Selection heuristic**:
- **Open Harness优先**: When putting AI into human workflows (dev productivity, CLI/chat ops, model experimentation)
- **Framework/Runtime优先**: When embedding AI into products/business systems (customer-facing features, audit, state management, production SLA)

**Key wiki pages** for this topic:
- [[comparisons/open-harness-vs-agent-framework]] — Full 10-tool comparison with individual evaluations, lock-in matrix, recommended architecture (PRIMARY)
- [[concepts/agent-harness]] — §"Agent Harness と Agent Framework/SDK の本質的差異" for conceptual distillation
- [[entities/atal-upadhyay]] — Original "Framework ≠ Harness" thesis (building blocks vs working agents)

### 3b. Harness vs Agent Framework/SDK — The Investment Distinction

[...existing content preserved...]

### 3c. Dual-Agent Architecture: Orchestrator + Execution Specialist (OpenClaw + Hermes)

When comparing OpenClaw and Hermes Agent, the most productive conclusion is often **not competitive** — the two harnesses complement each other in a dual-agent architecture validated by community consensus (~20% of users in Kilo Reddit analysis, 1,300+ comments):

- **OpenClaw = Orchestrator** (planning, decomposition, multi-step coordination, scheduling). Justified by gateway-first architecture, multi-agent routing, ACP sub-agent spawning (`sessions_spawn({ runtime: "acp" })`), cron/webhook scheduling, agent-to-agent communication tools.
- **Hermes Agent = Execution Specialist** (fast, repeatable task loops). Justified by learning loop, 5 sandbox backends, checkpoint/rollback, speed advantage on same model.
- **Bridge = ACP (Agent Client Protocol)** — standardized protocol akin to LSP for agents. OpenClaw spawns Hermes as interchangeable ACP execution backend.

**When to recommend this architecture**: Complex multi-agent workflows, production deployments needing external validation (Hermes self-evaluation is unreliable — OpenClaw orchestration validates output quality), any setup where the user can afford running two processes.

**Key wiki pages**: [[comparisons/hermes-vs-openclaw-architecture]] (full evidence section with 8+ sources), [[entities/openclaw]] (§Orchestration Capabilities), [[entities/hermes-agent]] (§Execution Specialist Role).

### 4. Model-Harness Compatibility Analysis

When evaluating a model-harness pairing:

1. **Check provider support** — Does the harness support the model's provider? (Most support OpenAI-compatible API)
2. **Check subscription wall** — Anthropic blocks third-party harnesses from using Max credits
3. **Check system prompt size** — For small/weak models, a large system prompt (10K+) degrades performance significantly
4. **Check local quantization** — For self-hosted: GGUF (llama.cpp, Ollama) vs MLX (Apple Silicon) support
5. **Check tool-calling capability** — Does the model support the harness's tool format?

**General compatibility tiers:**

| Tier | Models | Compatible Harnesses | Notes |
|------|--------|---------------------|-------|
| 🥇 | Claude Opus 4.7 / Sonnet 4.6 | Claude Code (native), Cursor (best score 93%), OpenCode, Aider | Best reasoning, but Anthropic wall on non-Anthropic harnesses |
| 🥇 | GPT-5.4 / GPT-5 | Codex CLI (native), Pi (no wall), OpenCode, Aider, Cursor | No subscription restrictions. App scaffolding specialist |
| 🥇 | Qwen 3.5 Coder 32B | Pi (local GGUF/MLX optimized), OpenCode, Aider | Best open-weight coder. Excellent price-performance |
| 🥇 | DeepSeek V3/V4 | OpenCode (75+ providers), Aider, Pi, OpenClaw (Ollama) | Cost-efficient. Strong at multi-file tasks |
| 🥈 | Gemma 4 26B | Pi + LM Studio (local), OpenCode (Ollama) | 18GB VRAM Q4_K_M; Pi's <1K system prompt compensates for weaker model |
| 🥈 | Gemini 2.5 Pro | Pi, OpenCode, Aider | Large free tier, good at long context |
| 🥉 | Local (7B-14B) | Pi only (minimal overhead), OpenCode (with performance tax) | Smaller models are overwhelmed by large system prompts |

### 5. Presenting Results

Structure comparison responses with:
1. **Quick decision table** — which harness × model pair for which scenario
2. **The Harness Effect** — always mention this if comparing the same model across harnesses
3. **Cost analysis** — subscription vs BYOK vs double-billing traps
4. **Sources** — always cite URLs to benchmark articles

### 6. Incorporating X/Twitter Opinion Leader Data into Wiki

When an opinion leader (0xSero, Karpathy, Simon Willison, etc.) posts a ranking or assessment on X/Twitter:

1. **Fetch the tweet** — Use `web_extract` on the tweet URL (e.g., `https://x.com/handle/status/123456`). This returns plain text of the tweet content. Do NOT use xurl for public tweet content — web_extract works directly.
2. **Parse the opinion** — Extract the ranking list, key endorsements, quotes, and any nuanced commentary. Look for "daily driver" statements and specific model/harness pairings.
3. **Check wiki coverage** — For each tool mentioned, check if an entity page exists in `~/wiki/entities/`. If not, create one via multi-source web research (GitHub, docs, site).
4. **Enrich existing entities** — Add a dedicated section to each existing entity page titled `## [Author]'s Assessment — #[Rank] for [Category]` containing the opinion leader's exact quote and interpretation.
5. **Update concept/comparison pages** — If the opinion adds new perspective (e.g., a local model ranking), add a new section to `concepts/agent-harness-comparison.md` rather than creating a new page. Also update `wiki/log.md` and `wiki/index.md`.
6. **Commit carefully** — Use **single quotes** for git commit messages that contain `&` characters. Double-quoted messages with `&` trigger the terminal tool's background-detection and fail.
7. **Cross-reference** — Add `[[entities/<author>]]` to the cross-references in log.md so the opinion leader's entity page connects to the contribution.

## Key Pitfalls

- **Do NOT confuse agent harnesses with inference servers** — When the user says "ハーネス" they mean Claude Code, Pi, OpenCode, OpenClaw, Hermes Agent, NOT vLLM/llama.cpp/Ollama
- **Check for existing wiki comparison pages before creating new ones** — `comparisons/coding-agent-harnesses.md` (May 1) and `concepts/agent-harness-comparison.md` (May 7) already exist. ALWAYS run session_search for 'agent harness comparison' before building new comparison artifacts. Duplicate comparison pages accumulate quickly.
- **Check for duplicate entity pages before creating new ones** — When creating or enriching entity pages for harness authors/contributors (Hugo Bowne-Anderson, Lance Martin, etc.), search existing entities first with `search_files` in `~/wiki/entities/`. The wiki may have multiple pages for the same person under slightly different filenames (e.g., `hugo-bowne.md` and `hugo-bowne-anderson.md`). Always merge into the older/more complete page.
- **Anthropic wall on third-party harnesses** — Pi and OpenCode users must PAY API RATES even if they have Claude Max subscription. This is a policy restriction, not a technical one
- **Benchmark scores are harness-dependent** — SWE-bench scores for "Claude Opus" alone are meaningless without specifying which harness
- **Harness vs inference server are orthogonal** — You can run Pi on top of Ollama (Ollama provides the inference, Pi provides the agent harness). Don't treat them as competing categories
- **Don't claim consensus without evidence** — different reviewers get different results; multiple sources needed
- **Pi's token efficiency is situational** — The 1K system prompt advantage matters most with small/weak models; large frontier models (Opus, GPT-5) handle 10K prompts fine
- **ALWAYS verify from primary sources before publishing** — Codex CLI is commonly misreported as single-model/closed-source (it's actually Apache-2.0, supports 5+ model types via config.toml + custom providers). Always check: (1) GitHub repo for license, language, features; (2) official docs for model support list; (3) community examples of custom provider configs. Secondary articles frequently get facts wrong about rapidly-evolving tools.
- **Harness engineering != coding agent frameworks** — Theodoros Galanos' work on AEC report generation demonstrates that harness engineering applies broadly to domain-specific knowledge work (engineering documents, HVAC analysis, construction specs). The same principles (Build-Verify Loop, context engineering, loop detection) transfer across domains. Don't limit harness research to CLI coding agents.
- **X/Twitter content extraction** — Use `web_extract` on tweet URLs, NOT xurl. xurl is for the user's own account operations (bookmarks, timeline). `web_extract` returns the plain text of public tweets reliably.
- **Git commit messages with &** — The Hermes terminal tool detects `&` anywhere in the command string (even inside single-quoted strings) and interprets it as backgrounding. **Do NOT use `&` in commit messages at all.** Use `and` or `+` instead. A message like `'wiki: agent-harness & harness-commoditization'` will fail — write `'wiki: agent-harness + harness-commoditization'` instead.
- **Tag taxonomy validation** — When creating entity pages, tags must exist in `wiki/SCHEMA.md`'s canonical taxonomy. The git `pre-commit` hook rejects commits with unknown tags. Check SCHEMA.md before finalizing tags: `grep -n "^-\\s*\\`" wiki/SCHEMA.md` for available categories. Common valid person-entity tags: `person`, `agent-harness`, `ai-agents`, `coding-agents`, `open-source`, `entrepreneur`.
- **Notion pages may truncate on web_extract** — Notion-hosted pages (notion.site) can time out on LLM summarization with `web_extract`. The first 5K+ characters are usually captured but the final ~800 chars may be lost. If the ending is truncated, check if the missing content is critical before re-extracting; browser_navigate is an alternative but requires Chrome installation.
- **web_extract truncation → execute_code httpx fallback**: When `web_extract` consistently truncates long articles (common with blog posts 8K+ chars), use `execute_code` with Python's `httpx` + `BeautifulSoup` as a fallback. Fetch with `httpx.get(url, timeout=30)`, parse with `BeautifulSoup(resp.text, 'html.parser')`, extract the article element (`soup.find('article')` or `soup.find(class_='md-content')` for MkDocs sites), and print the text. This bypasses the LLM summarization timeout and returns the full raw text. Example pattern:
  ```python
  import httpx
  from bs4 import BeautifulSoup
  resp = httpx.get(url, timeout=30)
  soup = BeautifulSoup(resp.text, 'html.parser')
  article = soup.find('article') or soup.find('main') or soup.find(class_='md-content')
  text = article.get_text(separator='\\n', strip=True) if article else soup.get_text(separator='\\n', strip=True)
  print(text[:12000])
  ```
