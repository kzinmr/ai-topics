---
title: "Context Engineering — Unified Framework for Context Optimization"
type: concept
aliases:
  - context-engineering
  - コンテキストエンジニアリング
created: 2026-04-13
updated: 2026-05-13
tags:
  - concept
  - harness-engineering
  - context-management
  - prompting
  - optimization
status: active
sources:
  - "OpenAI Cookbook — Context engineering patterns"
  - "Andrej Karpathy, X/Twitter, June 25, 2025"
  - "Anthropic — Effective context engineering for AI agents"
  - "DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines (Khattab et al., 2023)"
  - "Khairallah AL-Awady — How to Master Context Engineering & Build AI Systems That Actually Understand You (Full Course), May 2026"
  - "[[raw/articles/2025-06-23_rlancemartin_context-engineering-for-agents]] — Lance Martin, Context Engineering for Agents (Write/Select/Compress/Isolate), June 2025"
  - "[[raw/articles/2026-01-09_rlancemartin_agent-design-patterns]] — Lance Martin, Agent design patterns (7 patterns extending context engineering), Jan 2026"
  - "[[raw/articles/2026-05-13_anthropic_claude-code-agent-sdk-sessions]] — Anthropic, Work with sessions (Claude Code Agent SDK), 2026"
---

# Context Engineering

A systematic approach to effectively utilizing the context window and maximizing LLM performance. Positioned as a **cross-cutting technical component of Harness Engineering**.

> "Context engineering is the delicate art and science of filling the context window with just the right information for the next step." — Andrej Karpathy

> "Building with language models is becoming less about finding the right words and phrases for your prompts, and more about answering the broader question of 'what configuration of context is most likely to generate our model's desired behavior?'" — Anthropic

## Relationship to Harness Engineering

| Layer | Concept | Focus |
|---------|------|------|
| **Top-level** | Harness Engineering | Agent = Model + Harness (environment design philosophy) |
| **Cross-cutting** | Context Engineering | Context selection, compression, placement (finite resource management) |
| **Application (human side)** | Agentic Engineering | Patterns for developers to "leverage" agents |
| **Application (system side)** | AI Agent Engineering | Patterns for "building" agents |

Context Engineering is a **sub-component** of Harness Engineering — within the design of "what to show agents and what to hide," it specifically handles context window optimization.

## Karpathy's Definition and Software 3.0

Karpathy proposed a paradigm shift in "Software 2.0" (2017) treating neural networks as "optimizable parameters." This thinking directly connects to "context engineering" in the LLM era:

| Paradigm | Programming Target | Optimization Method |
|------------|-------------------|-----------|
| Software 1.0 | Explicit code (Python, C++, etc.) | Hand-written logic |
| Software 2.0 | Neural network weights | Gradient descent |
| Software 3.0 | Prompts/context for LLMs | Context engineering |

### Relationship to Autoresearch
Karpathy's autoresearch (March 2026):
1. Fix an immutable evaluator (prepare.py)
2. Agent modifies one editable file (train.py)
3. Run overnight, retain improvements, discard regressions

This pattern is structurally identical to DSPy's "optimize prompts as hyperparameters."

## Relationship to DSPy

DSPy (Declarative Self-improving Python) is a framework that treats prompts as learnable parameters and automatically improves them through optimization:

| Perspective | Karpathy's Context Engineering | DSPy |
|------|------------------------------|------|
| Focus | Overall context design | Prompt optimization |
| Method | Information selection, organization, compression | Declarative programming, compilation |
| Goal | Maximize LLM performance | Self-improving pipelines |
| Paradigm | Software 3.0 | Extension of Software 2.0 |

DSPy optimization patterns:
- **MIPROv2**: Bayesian optimization for prompt improvement
- **BootstrapFewShot**: Self-generated demonstration example optimization
- **GEPA**: Reflective evolution for prompt optimization

## Anthropic: Context Engineering vs Prompt Engineering

| Dimension | Prompt Engineering | Context Engineering |
|------|-------------------|---------------------|
| Focus | Creating optimal system prompts (one-shot) | Iterative, comprehensive management of **all tokens** passed during inference |
| Scope | System instructions | System instructions, tools, MCP, external data, message history |
| Nature | Discrete task-oriented | Continuous, cyclical curation |

### Attention Budget Constraints
Transformer architecture requires `n²` pairwise relationships:
- **Context Rot**: LLM recall accuracy degrades gradient-wise as context length increases
- **Position Encoding Interpolation**: Enables longer sequences but degrades token position understanding

### Component-Specific Best Practices

| Component | Best Practice |
|--------------|-------------------|
| **System Prompt** | Target the "Goldilocks zone" — not too specific, not too vague |
| **Tools** | Self-contained, token-efficient, clear contracts |
| **Few-Shot Examples** | Curate diverse, canonical examples. Avoid dumping edge cases |
| **External Data** | JIT loading — incrementally discover as needed |
| **Message History** | Compaction — remove iterative tool calls, retain decisions |

## Core Techniques

### 1. Context Compression
- Remove redundant information
- Extract and summarize key facts
- Prioritize keywords/entities

### 2. Context Ordering
- Place important information first and last (recency/primacy effect)
- Group related information
- Organize chronologically or by logical structure

### 3. Dynamic Context Management
- Adjust context volume based on task complexity
- Dynamically eliminate unnecessary information
- Monitor and optimize context usage

### 4. Context Chunking
- Split large documents into meaningful chunks
- Attach metadata to each chunk
- Combine chunks as needed

## Three Strategic Approaches (Anthropic)

### 1. Compaction
When approaching context window limits, summarize the conversation and resume.
- **What to keep**: Architectural decisions, unresolved bugs, implementation details
- **What to discard**: Redundant tool calls/results, intermediate thinking

### 2. Structured Note-Taking
Maintain persistent notes outside the context window, reloading as needed.
- Enables tracking across thousands of steps
- Claude Sonnet 4.5 includes file-based memory tools

### 3. Sub-Agent Architectures
Main agent coordinates high-level planning. Specialized sub-agents handle focused tasks with clean context.
- Sub-agents return condensed summaries (~1,000–2,000 tokens)

## Lance Martin: Write / Select / Compress / Isolate — 4-Bucket Classification

Lance Martin ([[entities/lance-martin]]) extended Anthropic's 3 strategies, classifying Context Engineering techniques into **Write, Select, Compress, Isolate** — 4 buckets ([Context Engineering for Agents](https://rlancemartin.github.io/2025/06/23/context_engineering/), June 2025). This classification structurally corresponds to Anthropic's Compaction/Structured Note-Taking/Sub-Agent while providing a more granular framework.

### 4-Bucket Overview

| Bucket | Definition | Anthropic Equivalent | Key Techniques |
|---------|------|--------------|--------------|
| **Write** | Store information outside the context window | Structured Note-Taking | Scratchpads, long-term memory (Reflexion, Generative Agents), CLAUDE.md / Cursor Rules |
| **Select** | Bring needed information into the context window | — (new) | Memory retrieval (embeddings + knowledge graph), tool-selection RAG, semantic search |
| **Compress** | Keep only needed tokens | Compaction | Summarization (recursive/hierarchical), trimming, fine-tuned pruning (Provence) |
| **Isolate** | Split and manage context separately | Sub-Agent Architectures | Multi-agent, code agents + sandbox, State object separation |

### Write (External Storage of Context)

**Scratchpad**: Like Anthropic's Think Tool, agents write information to files or State objects during task execution. Typical pattern: saving plans to Memory before Claude Code's auto-compact.

**Memories**: Knowledge persisting across sessions.
- **Reflexion** (Shinn et al., 2023): Generate reflections each turn, reuse as self-generated memory
- **Generative Agents** (Park et al., 2023): Periodically synthesize memories from past feedback
- **Product implementations**: ChatGPT Memory, Cursor Memories, Windsurf Memories — auto-generating long-term memory from user interactions

### Select (Selective Context Retrieval)

**Tool Selection as RAG**: As tool counts grow, duplicate tool descriptions confuse models. Apply RAG to tool descriptions, using semantic search to retrieve only task-relevant tools. Reported 3× accuracy improvement (arXiv:2505.03275, 2025).

**Knowledge Selection in Code Agents**: Windsurf's Varun's practical insight:
> "Indexing code ≠ context retrieval … embedding search loses reliability as a search heuristic as codebases grow larger. You need a combination of grep/file search, knowledge graph-based search, and reranking."

**Memory Selection Challenges**: Simon Willison reported at AIEngineer World's Fair — ChatGPT unintentionally retrieved location info from Memory and injected it into image generation. Unnecessary memory retrieval gives users the sense that "the context window is no longer theirs."

### Compress (Context Compression)

**Summarization**:
- Claude Code's auto-compact: When exceeding 95% of context window, summarize the entire user-agent dialogue
- **Recursive summarization** (arXiv:2308.15022): Progressively compress lengthy dialogues
- **Hierarchical summarization** (Anthropic Alignment, 2025): Applied to Computer Use capability monitoring
- Cognition: Summarize during knowledge handoffs between agents. Uses fine-tuned models — demonstrating this step's importance

**Trimming**: Hard-coded heuristic filtering (e.g., removing old messages). **Provence** (arXiv:2501.16214) is a context pruner trained for QA.

### Isolate (Context Separation)

**Multi-Agent**: OpenAI Swarm's "separation of concerns," Anthropic's multi-agent researcher — sub-agents operate in parallel with independent context windows. Higher performance than single agent but up to 15× token consumption.

**Code Agent + Sandbox**: HuggingFace's Deep Researcher — CodeAgent outputs code with tool calls executed in E2B sandbox. Token-heavy objects (images, audio, etc.) are kept as variables, returned to LLM only when needed.

**State Objects**: LangGraph's State schema — only the `messages` field is exposed to the LLM; other fields are selectively used. Context separation through schema design.

### Mapping to Anthropic

| Anthropic Strategy | Martin Classification | Extension Points |
|--------------|-----------|--------|
| Compaction | **Compress** | Adds trimming (Provence) beyond summarization |
| Structured Note-Taking | **Write** + **Select** | Separates storage (Write) and retrieval (Select). Adds RAG-based memory search and knowledge graphs |
| Sub-Agent | **Isolate** | Beyond sub-agents, includes code agents+sandbox and State separation |

Martin's framework innovation lies in **separating Write and Select** — treating storage and retrieval as independent concerns, each with its own technology stack.

### Evolution to Reduce/Offload/Isolate

Six months after this article (June 2025), Martin condensed and reorganized the framework into **Reduce / Offload / Isolate** — 3 principles (High Signal podcast, Dec 2025). See [[concepts/reduce-offload-isolate]] for mapping and details.

| 4 Buckets (Jun 2025) | 3 Principles (Dec 2025) | Change |
|---------------------|-----------------|------|
| Write + Select | → **Offload** | Integrated storage and retrieval. Unified to file system as external memory with selective retrieval |
| Compress | → **Reduce** | Redefined trajectory summarization/compaction as "reduction." Cache hit rate as the most important metric |
| Isolate | → **Isolate** | Unchanged, but Ralph Wiggum loop and fresh context importance strengthened |

This evolution reflects deepened understanding from operational experience: **"Context is the scarcest resource."**

### Claude Code Agent SDK: Context Engineering as SDK Implementation

Lance Martin's 4-bucket classification and Reduce/Offload/Isolate are materialized as SDK primitives in Anthropic's own **Claude Code Agent SDK** ([[entities/claude-code]]). In particular, **session management** ([Work with sessions](https://code.claude.com/docs/en/agent-sdk/sessions)) is a design that translates Context Engineering patterns into APIs developers can directly call.

**Sessions** are conversation histories containing "prompt + all tool calls + all tool results + all responses," automatically persisted to `~/.claude/projects/<encoded-cwd>/*.jsonl`. This is the **Write** pattern itself, providing a mechanism to externally store raw conversation state before Claude Code's `auto-compact` operates as **Compress**.

#### Continue / Resume / Fork — 3 Session Operations

| Operation | Behavior | Martin Classification | Use Case |
|------|------|-----------------|------|
| **Continue** | Auto-detects and appends to the latest session in the current directory | **Write + Select** | Multi-turn conversations within a single process. Transparently managed via `ClaudeSDKClient` (Python) or `continue: true` (TypeScript) |
| **Resume** | Resumes conversation from a specified session ID | **Select** (precision retrieval) | Recovery after process restart, returning to specific sessions, session isolation in multi-user apps |
| **Fork** | Creates a new session as a copy of the original. Original remains immutable | **Isolate** (branching) | Trying alternative approaches. E.g., trying OAuth2 while keeping JWT implementation |

#### Mapping to Context Engineering Frameworks

```
Martin 4 Buckets              Claude Code Session API
─────────────────────────────────────────────────
Write (external storage)   →  Automatic session persistence (JSONL)
Select (selective retrieval) →  Resume: precise context restoration by session ID
Compress (compression)     →  auto-compact: automatic summarization at 95% threshold
Isolate (separation)       →  Fork: conversation history branching + Sub-agents: independent sessions

Martin 3 Principles (Dec 2025)
──────────────────────
Reduce                    →  Compaction + session size management
Offload                   →  Session persistence + File Checkpointing (separate management of file changes)
Isolate                   →  Fork + Sub-agents (Ralph Wiggum loop)
```

**Key design decision**: Sessions persist **conversation**, not file system state. File change tracking and rollback is handled separately by **File Checkpointing**. This **separation of concerns** between "conversation state" and "file state" is an SDK-level implementation of Martin's **Offload** pattern (using the file system as external memory, but separated from conversation context).

**Cross-host sessions**: Moving JSONL files under `~/.claude/projects/` or mirroring to shared storage via `SessionStore` adapters enables session restoration across CI workers and serverless environments. This is the infrastructural backing for Martin's "Give Agents A Computer" pattern ([Agent design patterns](https://rlancemartin.github.io/2026/01/09/agent_design/), Jan 2026).

**Implication**: Context Engineering is no longer ad-hoc prompt design but is becoming **programmatically manageable** as SDK typed APIs. As the counterpoint to the Bitter Lesson Martin foresaw — "as models get smarter, harnesses get stripped down" — foundational primitives like session management are instead absorbed into SDKs and standardized.

## Just-in-Time (JIT) Context

A paradigm shift from pre-computed embedding retrieval to runtime JIT loading.

**Progressive Disclosure**: Agents incrementally discover needed context, maintaining only the minimum necessary information in working memory.

**Hybrid Strategy**:
- Pre-load static, high-value context like `CLAUDE.md`
- JIT explore using shell primitives like `glob`, `grep`, `head`, `tail`

## Strategy Selection Matrix

| Task Profile | Recommended Technique |
|-------------------|--------------|
| Bidirectional / conversational flow | **Compaction** |
| Iterative development with clear milestones | **Structured notes** |
| Complex exploration / parallel investigation | **Sub-agents** |
| Static domains (legal, financial) | **Hybrid (CLAUDE.md + JIT)** |

## Anti-Patterns
- **Context Overflow**: Feeding information beyond maximum token count
- **Context Dilution**: Burying important facts under irrelevant information
- **Static Context**: Failing to update context as conversation progresses
- **Prompt-only Focus**: Optimizing only the prompt, neglecting the overall context

## Practitioner Framework: Khairallah's 4-File Architecture (2026)

Khairallah AL-Awady ([[entities/khairallah-al-awady]]) proposes a **4-file architecture** and **dynamic context loading** as a practitioner framework for Context Engineering. It complements Anthropic/Karpathy's technical perspectives with concrete methods that individuals and teams can adopt today.

### Core Thesis

> "Prompt engineering is the syntax. Context engineering is the infrastructure. And infrastructure beats syntax every single time."

> "A perfectly worded prompt inside a poorly designed context will produce average results every time. A basic prompt inside a perfectly designed context will produce exceptional results every time."

### 3-Layer Context Model

| Layer | Description | Adoption Rate |
|---------|------|--------|
| **Layer 1: Immediate Context** | The prompt itself | 99% of people stop here |
| **Layer 2: Session Context** | Uploaded files, conversation history, system instructions | Partially used, without intentional design |
| **Layer 3: Persistent Context** | Memory systems, context files, KBs, saved settings | Almost unused, maximum leverage |

### 4-File Architecture

Four context files every professional should prepare. Loading them at session start transforms AI from "generic assistant" to "context-aware collaborator":

| File | Content | Role |
|---------|------|------|
| **Identity File** | Expertise, background, communication style | AI's "onboarding document" |
| **Audience File** | Target audience demographics, knowledge level, pain points, goals, language | Ensures output targeting precision |
| **Standards File** | Quality standards, formatting, tone guidelines, anti-patterns, success and failure examples | Quality management system |
| **Project File** | Current goals, active projects, recent decisions, open issues, deadlines | Dynamic layer updated weekly/monthly |

**Constraint**: Each file under 2,000 words (easily fits in context window)

### Dynamic Context Loading

"Loading everything" causes token waste and attention dilution. Load only needed files based on task type:

| Task Type | Context to Load |
|-------------|----------------------|
| **Writing** | Identity + Audience + Standards + deliverable success examples |
| **Analysis** | Identity + Project + raw data + past analyses |
| **Research** | Project + research methodology documents + existing research on the subject |
| **Strategy** | All 4 files + competitive analysis + industry data |

### Memory Evolution Ladder

| Stage | Method | When to Apply |
|------|------|--------------|
| **Manual** | Running document tracking decisions and learnings | < 20 documents |
| **Structured KB** | Structured Markdown folders (Obsidian, etc.) | 20+ documents |
| **Vector DB + RAG** | Automatic retrieval via embeddings, handles thousands of documents | When manual management limits are exceeded |

### Context-MCP Integration Pattern

> "Context without tools is knowledge without hands."

**Context-first, tools-second** pattern:
1. System prompt establishes context ("who you are, what you know")
2. MCP servers provide capabilities ("what you can do")
3. Task prompt binds both ("what to do now")

**Context is WHY and WHAT. Tools are HOW. Task is WHEN and WHERE.**

### Production Deployment

Evolution from personal productivity to business infrastructure:
- AI workflow audit → Context architecture design → Memory system implementation → MCP connectivity → Production system delivery
- Market value: **$5,000–$25,000/project** (as of 2026)
- Demand continuously exceeds supply — Context Engineering is not a trend but a **foundational infrastructure layer** that improves all AI applications

### Integration with Technical Perspectives

Khairallah's practitioner framework translates existing technical insights (Anthropic's Compaction/Structured Note-Taking/Sub-Agent, Karpathy's Software 3.0, DSPy optimization) into the **human-side adoption process**:

| Technical Concept | Khairallah's Practical Counterpart |
|---------|----------------------|
| Compaction (Anthropic) | Dynamic context loading — load only what's needed |
| Structured Note-Taking (Anthropic) | Memory evolution ladder — Manual → KB → RAG |
| Sub-Agent (Anthropic) | Context-MCP integration — functionality extension via tool connectivity |
| Software 3.0 (Karpathy) | 4-file architecture — "programming" context |
| Attention Budget constraints | 2,000-word limit + per-task loading to prevent attention dilution |

## Related Concepts

- [[concepts/context-engineering|Context Engineering]] — Parent concept: Harness Engineering
- [[concepts/reduce-offload-isolate]] — Lance Martin's evolution from 4 buckets to 3 principles
- [[concepts/harness-engineering/agentic-workflows/context-window-management]] — Willison's context management patterns
- [[concepts/harness-engineering/system-architecture/context-compaction]] — OpenAI Responses API compression mechanism
- [[concepts/harness-engineering/system-architecture/context-anxiety]] — Claude Sonnet 4.5 context anxiety phenomenon
- [[concepts/harness-engineering/system-architecture/harness-design-long-running-apps]] — GAN loop for long-running agents
- [[concepts/token-economics]] — Token cost analysis
- [[concepts/attention-mechanism-variants]] — KV cache and attention efficiency
- [[entities/dspy]] — DSPy: Declarative Self-improving Python
- [[entities/khairallah-al-awady]] — Khairallah AL-Awady: Proponent of practitioner-oriented 4-file architecture
