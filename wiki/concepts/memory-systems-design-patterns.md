---
title: "Memory Systems Design Patterns — Anthropic vs OpenAI vs Cognition"
type: concept
status: draft
created: 2026-04-13
updated: 2026-04-13
sources:
  - "https://www.anthropic.com/engineering/harness-design-long-running-apps"
  - "https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents"
  - "https://www.shloked.com/writing/chatgpt-memory-bitter-lesson"
  - "https://www.shloked.com/writing/claude-memory"
  - "https://www.shloked.com/writing/claude-memory-tool"
  - "https://www.shloked.com/writing/claude-code-source-patterns"
  - "https://www.shloked.com/writing/vajra"
tags:
  - memory-systems
  - context-engineering
  - methodology
  - multi-agent
related: [claude-memory, chatgpt-memory-bitter-lesson, context-engineering, harness-design-long-running-apps, claude-code-source-patterns, vajra-background-agent]
---
# Memory Systems Design Patterns — Anthropic vs OpenAI vs Cognition

Organizing **three approaches** to AI agent memory system design and the patterns the industry is converging on.

## 1. Three Major Approaches to Memory Design

| Dimension | **Anthropic (Claude)** | **OpenAI (ChatGPT)** | **Cognition (Devin)** |
|-----------|------------------------|----------------------|------------------------|
| **Memory format** | File-based (CLAUDE.md, .agent/) | Proprietary database | File-based (copying Anthropic) |
| **Sessions** | Stateless (full context each time) | Stateful (memory persisted) | Stateful→migrating to stateless |
| **Search strategy** | JIT (fetch on demand) | Pre-load (restore from memory) | Hybrid |
| **Versioning** | Git integration (native) | Manual backup needed | Git integration planned |
| **Transparency** | High (human-readable files) | Low (internal database) | Medium |
| **Scalability** | Depends on filesystem | Limited by database schema | Migrating to filesystem |

## 2. Anthropic Memory Design Principles (Extracted from 2 Engineering Blog Posts)

### Principle 1: Context is a Finite Budget
> "Every new token introduced depletes this budget by some amount."

- **Context Rot** is a performance gradient (not a hard cliff)
- Fundamental constraint of Transformer architecture (n² attention)
- **Mitigation**: Select only minimal, high-signal tokens

### Principle 2: File System IS the Memory
- CLAUDE.md + .agent/ + Git = Complete memory system
- No external database needed
- **Anthropic Harness**: Saves sprint contracts as files
- **Claude Code**: Fork primitives for context branching

### Principle 3: JIT > Pre-Load
- Instead of loading all data upfront, **fetch only what's needed, when needed**
- Similar to human cognitive model (rely on indexing, not memorization)
- Dynamic retrieval via `glob`/`grep`/`read`

### Principle 4: Context Reset > Compaction
- Recommends **new agent launch** over in-conversation summarization (compaction)
- Include sufficient state in handoff artifacts
- Maintain coherence by starting fresh

### Principle 5: Evaluator Isolation
- Separate generation from evaluation to avoid self-evaluation bias
- **GAN-inspired loop**: Generator ↔ Evaluator
- Use Evaluator only when tasks exceed model capability

## 3. Connection to Shlok Khemani's "Bitter Lesson" Analysis

Applying Rich Sutton's **Bitter Lesson** (general methods leveraging computation ultimately win) to memory systems:

| Bitter Lesson Lesson | Application to Memory Systems |
|----------------------|-------------------------------|
| Leverage computation | Larger context windows = better recall |
| Eliminate human bias | File-based = transparent, reproducible |
| General methods beat specialized ones | JIT retrieval = universal pattern |

**Khemani's core claim**:
> "The best way to build agent memory is not to build one at all."
> "Stateless agents that receive full context every time are more reliable than stateful agents that try to remember."

## 4. Industry Convergence Patterns

### Converging Designs
| Pattern | Anthropic | OpenAI | Cognition | Vajra |
|---------|-----------|--------|-----------|-------|
| **File-based memory** | ✅ CLAUDE.md | ❌ DB | ✅ Copying | ✅ .vajra/ |
| **JIT context** | ✅ glob/grep | ❌ Pre-load | ⚠️ Migrating | ✅ SKILL.md |
| **Git integration** | ✅ Native | ❌ Proprietary | ✅ Planned | ✅ Native |
| **Stateless sessions** | ✅ | ❌ Stateful | ⚠️ Migrating | ✅ |
| **Context Reset** | ✅ Recommended | ❌ Compaction | ⚠️ Exploring | ✅ Isolated workspaces |
| **Evaluator isolation** | ✅ GAN loop | ❌ Self-evaluation | ⚠️ Planning | ✅ Plan Review + Code Review |

### Not Converging
| Dimension | Anthropic | OpenAI |
|-----------|-----------|--------|
| **Memory persistence** | Files (CLAUDE.md) | Database (Memory feature) |
| **Session management** | Context Reset (new agent) | Compaction (in-conversation summarization) |
| **Evaluation strategy** | Evaluator isolation (GAN) | Self-evaluation (single agent) |

## 5. Impact on Coding Agents (Codex vs Claude Code)

Memory design differences directly shape **agent characteristics**:

| Characteristic | Claude Code | Codex |
|----------------|-------------|-------|
| **Memory format** | CLAUDE.md (file) | Internal state (database) |
| **Sessions** | Stateless (full context each time) | Stateful (memory persisted) |
| **Fork** | ✅ Independent context branching | ❌ Single thread |
| **Cache** | ✅ Prompt cache prioritized | ⚠️ Partial |
| **Transparency** | ✅ Human-readable files | ❌ Internal state |

**Shlok's insight**:
> "Cognition is copying Claude's memory approach" — Anthropic's design is becoming the industry standard

## 6. Practical Memory Design Checklist

Evaluation criteria for designing agent memory systems:

- [ ] **File-based?** — Transparency, Git integration, portability
- [ ] **JIT retrieval?** — Minimal pre-loading, dynamic fetching
- [ ] **Stateless sessions?** — Reproducibility, Context Reset support
- [ ] **Evaluator isolation?** — Avoid self-evaluation bias
- [ ] **Context Rot mitigation?** — Attention budget management
- [ ] **Cache optimization?** — Effective use of prompt caching
- [ ] **Fork/branch support?** — Independent context exploration

## Sources

- [Effective Context Engineering for AI Agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) — Anthropic Engineering, Sep 2025
- [Harness Design for Long-Running Application Development](https://www.anthropic.com/engineering/harness-design-long-running-apps) — Prithvi Rajasekaran, Anthropic Labs, Mar 2026
- [ChatGPT's Memory Problem](https://www.shloked.com/writing/chatgpt-memory-bitter-lesson) — Shlok Khemani, Apr 2026
- [Claude's Memory](https://www.shloked.com/writing/claude-memory) — Shlok Khemani, Apr 2026
- [Why Cognition is Copying Claude's Memory](https://www.shloked.com/writing/claude-memory-tool) — Shlok Khemani, Apr 2026
- [Claude Code Source Patterns](https://www.shloked.com/writing/claude-code-source-patterns) — Shlok Khemani, Apr 2026
- [Vajra: Background Coding Agent](https://www.shloked.com/writing/vajra) — Shlok Khemani, Apr 2026

## See Also

- [[concepts/_index]]
- [[concepts/claude/memory-tool]]
- [[concepts/ai-agent-memory-middleware]]
- [[concepts/knowledge-graph-memory-agents]]
- [[concepts/ai-agent-memory-two-camps]]
