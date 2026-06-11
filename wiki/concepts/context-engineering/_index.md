---
title: Context Engineering
created: 2026-05-20
updated: 2026-06-11
type: concept
tags:
  - context-engineering
  - context-management
  - ai-agent-engineering
  - ai-agents
  - prompting
  - architecture
  - memory-systems
  - rag
  - prompt-caching
  - token-economics
  - agentic-engineering
  - progressive-disclosure
  - agent-design-patterns
  - enterprise-agents
  - agent-identity
  - agent-governance
  [context-engineering, context-management, ai-agent-engineering, ai-agents, prompting, agent-architecture, memory-systems, agent-memory, subagents, rag, prompt-caching, token-economics, agentic-engineering, progressive-disclosure, agent-design-patterns, enterprise-agents, agent-identity, agent-governance]
sources:
  [raw/articles/2025-09-29_anthropic_effective-context-engineering-for-ai-agents.md, raw/articles/2025-06-23_lancemartin_context-engineering-for-agents.md, raw/articles/2026-01-09_lancemartin_agent-design-patterns.md, raw/articles/substack.com--redirect-6b46ec4c-ff7c-43b5-9e62-b0d4bf1dca99--bb1f035d.md]
---

# Context Engineering

**Context engineering** is the art and science of curating the optimal set of tokens in an LLM's context window at each inference step. It is the natural evolution of [[prompt-engineering]], shifting focus from crafting one-shot prompts to **continuously managing the entire context state** — system instructions, tools, MCP, external data, message history — across multi-turn, long-horizon agent loops.

> "Context engineering is the delicate art and science of filling the context window with just the right information for the next step."
> — Andrej Karpathy

> "Context engineering … is effectively the #1 job of engineers building AI agents."
> — Cognition

## Why It Matters

LLMs operate under a finite **attention budget** — akin to human working memory. Every new token depletes it. The transformer architecture's **n² attention** means pairwise relationships stretch thin as context length grows, causing **context rot**: a performance gradient (not a cliff) where model recall degrades as token count increases.

Long-running agents exacerbate this. They accumulate tool results, thinking blocks, and conversation turns, leading to:

| Failure Mode | Description |
|---|---|
| **Context Poisoning** | A hallucination enters and propagates through the context |
| **Context Distraction** | Volume overwhelms the model's training distribution |
| **Context Confusion** | Superfluous information influences responses |
| **Context Clash** | Parts of the context contradict each other |
| **Context Rot** | Recall accuracy degrades as token count grows |

These failure modes, identified by Drew Breunig and cited by Lance Martin, make context engineering a **hard requirement** for reliable agents — not an optimization.

## Core Principle

> Find the **smallest possible set of high-signal tokens** that maximize the likelihood of some desired outcome. — Anthropic

Context is a **finite, precious resource**. Every token that enters the window should earn its place.

---

## Taxonomy: Two Complementary Frameworks

The field has converged on two complementary ways to organize context engineering strategies:

### Anthropic's Implementation View

Anthropic's framework (September 2025) is organized around **where context lives and how it flows**:

| Component | Strategy |
|---|---|
| **System Prompts** | Clear, simple language at the "right altitude" — specific enough to guide, flexible enough to adapt. Start minimal, iterate. |
| **Examples (Few-Shot)** | "Pictures worth a thousand words." Too few → hallucination; too many → overfitting. |
| **Tools & MCP** | Tool definitions tax the attention budget. Use consistent naming, progressive disclosure, and omit rarely-used tools. |
| **Just-in-Time Retrieval** | Maintain lightweight identifiers (file paths, queries, links) and dynamically load data via tools at runtime. Mirrors human cognition. |
| **Compaction** | Auto-summarize conversation when context exceeds ~95% of window (Claude Code). Art is in selecting what to keep vs. discard. |
| **Structured Note-Taking** | Persist information to external storage (files, DBs). Enables learning across sessions. |
| **Sub-Agent Delegation** | Isolate context into sub-agents with their own windows, each focused on a narrow sub-task. |

### Source: Anthropic's "Effective Context Engineering for AI Agents" (September 2025)

The Anthropic framework above is derived from the article by Prithvi Rajasekaran, Ethan Dixon, Carly Ryan, and Jeremy Hadfield (Anthropic Applied AI). Key additional insights from the article:

- **Context rot**: The transformer architecture's n² pairwise attention causes performance to degrade as a gradient (not a cliff) as context grows — a finite "attention budget"
- **System prompt altitude**: Finding the "right altitude" — specific enough to guide, flexible enough to adapt. Start minimal, iterate based on observed gaps
- **Just-in-time context**: Agents maintain lightweight references (file paths, queries, links) and dynamically load data at runtime, mirroring human cognition
- **Sub-agent isolation**: Specialized sub-agents with clean context windows return condensed summaries, avoiding context pollution in the parent

> **Source**: [[raw/articles/2026-05-08_anthropic-engineering_effective-context-engineering-for-ai-agents.md]]

### Lance Martin's 4-Strategy Taxonomy

Lance Martin's framework (June 2025) organizes strategies by **what operation they perform on context**:

```
┌─────────────────────────────────────────────────────────┐
│                 CONTEXT ENGINEERING                       │
│                                                          │
│   ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐│
│   │  WRITE   │  │  SELECT  │  │ COMPRESS │  │ ISOLATE  ││
│   │  Save    │  │  Pull    │  │  Keep    │  │  Split   ││
│   │ context  │  │ context  │  │ relevant │  │ context  ││
│   │ outside  │  │ into the │  │ tokens   │  │ across   ││
│   │ the      │  │ window   │  │ only     │  │ agents   ││
│   │ window   │  │          │  │          │  │          ││
│   └──────────┘  └──────────┘  └──────────┘  └──────────┘│
└─────────────────────────────────────────────────────────┘
```

#### 1. Write — Save Context Outside the Window

Persist information so the agent can reference it later without keeping it in the context.

- **Scratchpads**: In-session notes (file-writing tools, runtime state objects). Example: Anthropic's multi-agent researcher saves its plan to avoid truncation.
- **Memories**: Cross-session persistent storage. Three types:
  - **Episodic** — few-shot examples from past interactions
  - **Procedural** — instructions, styles, rules
  - **Semantic** — facts about users, codebases, the world
- Products with memory: ChatGPT, Cursor, Windsurf (auto-generate user-agent memories).

**See also**: [[memory-systems]], [[agent-memory]]

#### 2. Select — Pull Context Into the Window

Choose what context to load at each step, avoiding overwhelming the attention budget.

- **Memory selection**: Simple (always include `CLAUDE.md`) vs. complex (embeddings/knowledge graphs for large collections).
- **Tool selection**: Apply RAG to tool descriptions — reported 3× selection accuracy improvement over loading all tools.
- **Knowledge selection (RAG)**: Windsurf's code indexing pipeline — AST parsing → semantic chunking → grep/file search → knowledge graph retrieval → re-ranking.
- ⚠️ **Trap**: Incorrect selection can feel intrusive (Simon Willison's example of ChatGPT adding his location to an image unprompted).

**See also**: [[rag]], [[embeddings]], [[progressive-disclosure]]

#### 3. Compress — Keep Only What's Needed

Reduce token count while preserving the information necessary for the task.

- **Context summarization**: Claude Code auto-compacts at >95% context usage. Cognition uses a fine-tuned model for summarization. Can be recursive or hierarchical.
- **Context trimming**: Heuristic pruning (remove old messages, old tool results, thinking blocks). Provence is a trained context pruner.
- **Art of compaction**: Overly aggressive summarization can lose subtle but critical context whose importance only becomes apparent later.

**See also**: [[prompt-caching]], [[token-economics]]

#### 4. Isolate — Split Context Across Agents

Separate concerns into independent context windows.

- **Multi-agent isolation**: Each sub-agent gets its own tools, instructions, and context, focused on a narrow sub-task. Anthropic's multi-agent researcher showed isolated sub-agents outperform single-agent approaches. Trade-off: up to 15× more tokens, careful coordination required.
- **Environment isolation (Code Agents)**: Execute code in sandboxes. Only selected return values re-enter the LLM context. HuggingFace's deep researcher uses this pattern.
- **Filesystem isolation**: Agents communicate through the filesystem/git history rather than through shared context windows.

**See also**: [[multi-agent]], [[subagents]], [[ralph-loop]]

---

## Mapping Between Frameworks

Lance Martin's 4 strategies map cleanly onto Anthropic's implementation techniques:

| Lance Martin (2025) | Anthropic (2025) |
|---|---|
| **Write** (scratchpads, memories) | Structured Note-Taking, Memory tool |
| **Select** (memory, tools, knowledge) | Just-in-Time Retrieval, Tool design, Progressive Disclosure |
| **Compress** (summarization, trimming) | Compaction, Context trimming |
| **Isolate** (multi-agent, code agents) | Sub-Agent Delegation |

The Anthropic framework adds **System Prompts** and **Examples (Few-Shot)** as first-class design concerns that sit at a higher altitude — they shape how all four operations behave.

---

## Advanced Patterns

### Give Agents a Computer

Agents direct their own actions. Primitives like a **filesystem** (persistent context) and a **shell** (run built-ins, CLIs, self-written code) are fundamental.

> "The fundamental coding agent abstraction is the CLI … agents need access to the OS layer." — @rauchg

Claude Code and Manus both give agents a computer. This enables offloading context to files, using CLI tools instead of tool-calling-layer tools, and writing code that processes data without loading it into context.

### Enterprise Context Engineering (Box/Aaron Levie, April 2026)

[[entities/aaron-levie|Aaron Levie]] (Box CEO) articulated the enterprise-scale context engineering challenge from the perspective of a platform serving **67% of the Fortune 500** with $1.1B+ ARR:

- **The 60K-Token Problem**: "I have 10 million documents, which maybe is times five pages per document. I'm at 50 million pages of information and I have 60,000 tokens. How do I bridge the 50 million pages with the couple hundred I get to work with?" This is the fundamental enterprise context engineering challenge — selecting from millions of documents what fits in a single context window.

- **Agent Search Limitations**: Frontier models are "not actually that good at searching" — they lack the explore/exploit tradeoff humans use naturally when navigating information spaces. Agents don't know when to stop searching vs. when to give up, leading to the **"stop searching" problem**: lower-tier models return partial results ("I found 6 of 10 addresses") without knowing they're incomplete.

- **Context Pruning from Enterprise Perspective**: Agents repeat mistakes because failed attempts remain in context, effectively becoming few-shot examples — the "Groundhog's Day inside these models" problem. Levie identifies this as a critical barrier to reliable enterprise agent deployment. Better models (Opus 4.5/4.6, Gemini 3.5 Pro) can "smell something fishy" — detecting contradictions and re-ranking search results — but the fundamental pruning challenge remains unsolved at scale.

- **APEX Eval**: Box partnered with Apex (CoreWork) on agent evaluation that tests both the harness and the model, tracking how different professions structure workspaces and measuring model family improvements across Opus 4.5/4.6 and Sonnet 4.5/4.6.

### Progressive Disclosure

Show only essential information upfront; reveal details on demand. Applied at multiple layers:
- **Tool definitions**: Index tool descriptions, retrieve on demand
- **CLI utilities**: Provide command list; agent uses `--help` to learn specifics
- **MCP servers**: Cursor Agent syncs descriptions to a folder; agent reads full descriptions only when relevant
- **Skills (Anthropic standard)**: `SKILL.md` YAML frontmatter loaded into instructions; full content read only if needed

### Prompt Caching

Agents manage context as a linear, append-only message list. **Prompt caching** is critical — without it, costs explode.
- Manus calls **"cache hit rate"** the most important production metric.
- A more expensive model with high cache hit rate can be *cheaper* than a lower-cost model without caching.
- @trq212: coding agents (Claude Code) would be **cost-prohibitive** without caching.

### The Ralph Wiggum Loop

A delegation pattern for long-running tasks:
1. **Initializer agent** sets up environment (plan file, tracking file)
2. **Sub-agents** tackle individual tasks from the plan file, each with isolated context
3. **Stop hooks** verify work after each loop iteration
4. **Context sharing** via filesystem (git history)

### Frequent Intentional Compaction (FIC) — dexhorthy / HumanLayer

[[entities/dex-horthy|Dex Horthy]] (HumanLayer founder) articulated a workflow pattern called **Frequent Intentional Compaction** (August 2025), designed specifically for getting AI coding agents to work in large, brownfield codebases (300K+ LOC). The core thesis: treat the context window as a finite, degrading resource and deliberately manage it through a structured **Research → Plan → Implement** pipeline.

#### The Problem: Brownfield Codebases + Naive Context Use

The [Stanford study on AI developer productivity](https://www.youtube.com/watch?v=tbDDYKRFjhk) found that AI tools work well for greenfield projects but often make developers *less* productive in large established codebases — generating "slop" that requires rework. The naive approach (chat-based coding, accumulating context) fails because:

1. **Context bloat**: Searching files, understanding code flow, test/build logs, and tool responses flood the window
2. **Mental alignment loss**: Team members lose touch with what the codebase does as AI ships large PRs
3. **Compounding errors**: A bad research understanding → bad plan → hundreds of bad lines of code

#### The FIC Pipeline

| Stage | Purpose | Human Leverage Point |
|-------|---------|---------------------|
| **Research** | Understand codebase, relevant files, information flow, potential causes | Human reviews research output, corrects misunderstandings before they propagate |
| **Plan** | Outline exact steps, files to edit, testing/verification per phase | Human reviews plan — highest-leverage review point |
| **Implement** | Execute plan phase-by-phase; compact status back into plan file after each phase | Human verifies each phase before next begins |

#### Key Principles

1. **Compaction as first-class operation**: Deliberately distill context into structured artifacts (research docs, plan files) rather than letting the conversation history accumulate
2. **Sub-agents for context isolation**: Use fresh context windows for finding/searching/summarizing, keeping the parent agent's window clean for implementation
3. **40–60% context utilization**: Keep the context window partially empty to leave room for reasoning; avoid filling it to capacity
4. **Spec-driven development**: Treat specs/plans/research docs as the "real code" — the source of truth for what is being built and why, analogous to source code vs. compiled binary
5. **Human review at highest-leverage points**: A bad line of research can cause thousands of bad lines of code. Review research and plans, not just final code.

#### Concrete Results

- 300K LOC Rust codebase (BAML): bug fix PR approved overnight by maintainer; 35K LOC of cancellation + WASM support shipped in 7 hours (estimated 3–5 days each for senior engineer)
- Team of 3 averaging ~$12K/month on Claude Opus tokens
- One developer shipping 6 PRs in a day, rarely editing non-markdown files by hand

#### Limitations

FIC does not work perfectly for every problem. dexhorthy's team spent 2 weeks stuck on a tricky race condition involving MCP sHTTP keepalives in Go — the research phase didn't go deep enough through the dependency tree. **Lesson**: you need at least one person who is an expert in the codebase for hard problems.

#### Relationship to Other Context Engineering Patterns

| Pattern | Relationship to FIC |
|---------|-------------------|
| [[concepts/context-engineering|Anthropic's Compaction]] | FIC makes compaction explicit, frequent, and human-reviewed rather than automatic at 95% capacity |
| [[concepts/context-engineering|Lance Martin's Write/Select/Compress/Isolate]] | FIC operationalizes all four: Write (research/plan files), Select (sub-agent scoping), Compress (compaction artifacts), Isolate (Research→Plan→Implement stage boundaries) |
| [[ralph-loop|Ralph Wiggum Loop]] | Ralph = infinite loop with simple prompt; FIC = structured multi-stage pipeline with human checkpoints |
| [[concepts/spec-driven-development|Spec-Driven Development]] | Sean Grove's thesis that specs become the real code — FIC implements this via plan/research docs as source of truth |

> **Source**: [[raw/articles/2025-08-29_humanlayer-advanced-context-engineering-coding-agents]] — "Getting AI to Work in Complex Codebases" (August 2025, Y Combinator talk + blog post)

### Multi-Layer Action Space

Keep the tool-calling layer lean (~12 tools for Claude Code, <20 for Manus). Push broad actions to the computer — a single `bash` tool can invoke shell utilities, CLIs, or write/execute arbitrary code (the **CodeAct** pattern). This saves tokens because the agent doesn't process intermediate tool results.

---

## Key Trade-Offs

| Strategy | Benefit | Cost |
|---|---|---|
| **Composition** | Stays within context budget | Irreversible information loss |
| **Sub-agents** | Clean separation of concerns | Up to 15× token overhead |
| **Memory systems** | Learning across sessions | Incorrect selection feels intrusive |
| **Filesystem offload** | Preserves information | Requires agent to know when/where to read |
| **Caching** | Massive cost savings | Constrains message ordering |

---

## The Bitter Lesson Applied

The Bitter Lesson predicts that compute/model scaling often overtakes hand-crafted approaches. Several threads suggest this for context engineering:

- **Recursive Language Models (RLM)**: Work from @lateinteraction, @a1zhang, @primeintellect suggests LLMs can learn to perform their own context management — absorbing much of the scaffolding currently built into agent harnesses.
- **Sleep-time compute**: Agents could reflect on past sessions during "offline" periods and automatically update memories/skills ([[sleep-time-compute]], @Letta_AI).
- **@jeffreyhuber**: Rather than hand-crafted compaction, models might learn to self-manage context through training.

For now, however, **explicit context engineering remains essential** for practical agents. The frameworks above represent the current best practices as of mid-2025.

---

## Practical Checklist

Building an agent? Consider each dimension:

1. **Write**: Does the agent persist plans? Memories? Can it learn across sessions?
2. **Select**: Do you load all tools, or retrieve relevant ones? All documents, or just needed ones? Is selection intrusive?
3. **Compress**: Do you compact at ~95% context? Is the compaction granular enough? Can the agent recover compacted info?
4. **Isolate**: Would sub-agents help? Can tasks be parallelized? Is coordination cost worth it?
5. **System prompt**: Is it at the right altitude? Start minimal, add only for observed gaps.
6. **Tools**: Are descriptions token-efficient? Consistent naming? Progressive disclosure where possible?
7. **Caching**: Is your message ordering cache-friendly? What's your cache hit rate?

---

## Sub-Pages

| Page | Topic |
|---|---|
| [[concepts/context-engineering/context-anxiety|Context Anxiety]] | Agent anxiety from context uncertainty |
| [[concepts/context-engineering/context-compaction|Context Compaction]] | Strategies for compacting context |
| [[concepts/context-engineering/context-compression|Context Compression]] | Token-level compression techniques |
| [[concepts/context-engineering/context-efficiency|Context Efficiency]] | Maximizing information per token |
| [[concepts/context-engineering/context-folding|Context Folding]] | Folding long contexts into summaries |
| [[concepts/context-engineering/context-fragments|Context Fragments]] | Modular context composition |
| [[concepts/context-engineering/context-graph|Context Graph]] | Graph-based context representation |
| [[concepts/context-engineering/context-lock-in|Context Lock-in]] | Vendor/model context lock-in risks |
| [[concepts/context-engineering/context-management|Context Management]] | General context lifecycle management |
| [[concepts/context-engineering/context-management-cognition-claude-models|Context Management Cognition]] | Claude model-specific context cognition |
| [[concepts/context-engineering/context-providers|Context Providers]] | Context data source providers |
| [[concepts/context-engineering/context-repositories|Context Repositories]] | Persistent context storage patterns |
| [[concepts/context-engineering/context-rot|Context Rot]] | Attention degradation over long contexts |
| [[concepts/context-engineering/context-routing|Context Routing]] | Dynamic context routing strategies |
| [[concepts/context-engineering/context-window-management|Context Window Management]] | Window size and memory management |

---

## Related Pages

- [[agent-architecture]] — How these patterns compose into agent systems
- [[prompt-engineering]] — The precursor to context engineering
- [[memory-systems]] — Memory-specific strategies
- [[multi-agent]] — Sub-agent delegation patterns
- [[managed-agents]] — Anthropic's meta-harness architecture
- [[ralph-loop]] — The delegation loop pattern
- [[codeact]] — Code-as-action pattern
- [[progressive-disclosure]] — The progressive disclosure pattern
- [[prompt-caching]] — Token economics and caching strategies

