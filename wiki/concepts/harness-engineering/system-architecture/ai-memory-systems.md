---
title: "AI Memory Systems — ChatGPT vs Claude vs Cognition"
type: concept
aliases:
  - ai-memory-systems
  - chatgpt-memory
  - claude-memory
  - agent-memory-architecture
created: 2026-04-13
updated: 2026-05-26
tags:
  - concept
  - memory-systems
  - context-engineering
  - architecture
status: draft
sources: []
---

# AI Memory Systems — ChatGPT vs Claude vs Cognition

A comparison of the design philosophies behind "memory" systems in AI assistants and agents. OpenAI, Anthropic, and Cognition (Devin) each adopt fundamentally different approaches, reflecting differences in product target (consumer vs. technical) and architectural philosophy (automatic vs. explicit).

Sources: [Shlok Khemani - ChatGPT Memory and the Bitter Lesson](https://www.shloked.com/writing/chatgpt-memory-bitter-lesson), [Claude Memory: A Different Philosophy](https://www.shloked.com/writing/claude-memory), [Anthropic's Opinionated Memory Bet](https://www.shloked.com/writing/claude-memory-tool)

---

## ChatGPT Memory: 4 Memory Buckets + Bitter Lesson Strategy

### Architecture

Every turn, ChatGPT injects **4 data buckets** into the system prompt:

| Component | Description | Update Frequency | User Visible |
|---|---|---|---|
| **1. Interaction Metadata** | Device specs, usage patterns (topic ratio, avg message length, conversation depth, model usage ratio, session activity, account age, subscription tier, estimated geolocation) | Real-time | ❌ |
| **2. Recent Conversation Context** | Timestamped topic-tagged log of ~40 most recent conversations (user messages only, assistant responses omitted to save tokens) | Real-time | ❌ |
| **3. Model Set Context** | User-provided explicit memories (e.g., "shellfish allergy"). Acts as an override layer | On demand (user-editable) | ✅ |
| **4. User Knowledge Memories** | AI-generated summaries from conversation history (~10 paragraphs). First 3 cover professional/technical life, last 2 cover ChatGPT usage habits | Every 2-3 days | ❌ |

### Analogy with LLM Training

| Memory Component | LLM Equivalent | Function |
|---|---|---|
| User Knowledge Memories | Pretrained Base Model | Dense, weighted knowledge. Degrades over time but retains core patterns |
| Model Set Context | RLHF / Fine-tuning | Explicit correction overriding old base knowledge |
| Recent Conversation Context | In-Context Learning | Session-specific examples shaping immediate behavior |
| Interaction Metadata | System Defaults / Environment | Implicitly guides routing and formatting |

### "Bitter Lesson" Strategy

OpenAI deliberately avoids complex search architectures. **No RAG, no vector DB, no knowledge graph.** Instead, all memory components are injected into the context window every turn.

**2 assumptions:**
1. **Model intelligence > search engineering:** LLMs are smart enough to parse thousands of tokens and ignore irrelevant context
2. **Context scale + cost deflation:** Brute-force injection may look wasteful now, but widening context windows and falling compute costs will make it obvious

---

## Claude Memory: Explicit, On-Demand Tools

### Architecture

Claude adopts a **fundamentally opposite** memory philosophy to ChatGPT:

- **Blank slate initialization:** Starts from zero each conversation. No pre-loaded profiles or history
- **Explicit activation only:** Activated only when prompted with "What were we talking about?" or "Continue from where we left off"
- **Raw history search:** Uses actual past conversations searched in real-time, not AI-generated summaries or compressed profiles
- **Visible tool execution:** Users can see the search tool being invoked and intentional delay

### Search Tool Specifications

| Tool | Function | Parameters |
|---|---|---|
| `conversation_search` | Keyword/topic-based full history search. Multi-topic queries run sequentially | `query` (required), `max_results` (1-10, default 5) |
| `recent_chats` | Time-based access with cursor pagination | `n` (1-20, default 3), `sort_order` (asc/desc), `before`, `after` |

---

## Claude Memory Tool: File-Based Native Memory

Anthropic natively provides a **file-based memory tool**, marking the first time a model provider has taken an opinionated stance on memory.

### 6 Operation Interfaces

`view` | `create` | `str_replace` | `insert` | `delete` | `rename`

### Separation of Concerns

1. **Storage (developer):** File format (JSON/XML/text), location (local/S3/encrypted), security/access control
2. **Strategy (system prompt):** Guides memory structure, retention policy, and usage rules. No custom parsers or extraction logic needed

### Anthropic's 4 Strategic Bets

| Bet | Rationale | Tradeoff |
|---|---|---|
| **1. Unify Memory** | Integrate search, storage, and conversation into a single inference flow | High latency/cost (~3 LLM calls per interaction) |
| **2. Files > Databases** | Unstructured files enable dynamic schema evolution | Requires prompt engineering for structure enforcement |
| **3. No Search Function** | `view` lists directories, Claude reads full files. "There is never too much context" | Higher token cost. Insight vs. cost tradeoff |
| **4. Beyond Memory** | Files serve as general agent context management (inter-agent communication, task workspaces, self-improvement) | Shift toward positioning files as "extended working memory" |

---

## Cognition (Devin): File System as Memory

In integrating Claude Sonnet 4.5 into Devin, the Cognition team discovered that the model **treats the filesystem as memory**.

### Key Findings

- Sonnet 4.5 spontaneously writes files (CHANGELOG.md, SUMMARY.md) without prompting, externalizing state
- This behavior becomes more pronounced as the context window fills up
- Cognition initially explored removing their proprietary memory management and relying on the model's self-externalization
- However, model-generated summaries were incomplete and caused performance degradation in production
- **Conclusion:** A hybrid of explicit memory systems and the model's externalization behavior is necessary

### Context Window Anxiety

Sonnet 4.5 appears to "be aware" of its own context window. When approaching limits:
- It spontaneously begins summarizing progress
- It becomes decisive to complete tasks
- It takes shortcuts or leaves tasks partially completed
- It consistently underestimates remaining tokens (with surprising accuracy)

Cognition's hack: Enable 1M token context, but cap actual usage at 200K. This makes the model feel like it "has room to breathe," preventing anxiety-driven shortcuts.

---

## Comparison Matrix

| Dimension | ChatGPT | Claude (Web) | Claude (Memory Tool) | Cognition Devin |
|---|---|---|---|---|
| Target | General consumer | Technical/professional | Developers/agent builders | Enterprise SWE |
| Activation | Always automatic | Explicit trigger | Explicit trigger (file ops) | Autonomous |
| Data format | AI-generated profile | Raw conversation history | Files (JSON/XML/text) | Filesystem |
| Search | None (brute injection) | Keyword search | Directory scan + full text | Hybrid |
| Storage responsibility | OpenAI | Anthropic | Developer | Cognition |
| Memory update | Every 2-3 days | Real-time search | On-demand per conversation | Autonomous summarization |
| Token strategy | Brute-force injection | On-demand reads | Full file reads | Externalization + hybrid |

## Related Concepts

- [[concepts/context-engineering|Context Engineering]] — Context engineering
- [[concepts/context-engineering/window-management|Context Window Management]] — Strategic management of context windows
- [[concepts/harness-engineering/system-architecture/context-compaction]] — Context compaction mechanisms
- [[concepts/context-engineering/anxiety|Context Anxiety]] — Context anxiety phenomenon
- [[concepts/harness-engineering]] — Agent control and structuring
- [[concepts/harness-engineering/agentic-engineering]] — Agent-enabled development

## Update History

| Date | Changes |
|------|---------|
| 2026-04-13 | Initial creation — integrated 3 Shlok Khemani articles + Cognition Sonnet 4.5 article |
