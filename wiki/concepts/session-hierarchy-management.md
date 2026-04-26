---
title: Session Hierarchy Management
type: concept
created: 2026-04-18
updated: 2026-04-18
tags: [session-management, multi-agent, context-engineering, orchestration, claude-code]
aliases: ["session-hierarchy", "context-hierarchy", "multi-level-session-management"]
related: [[context-window-management]], [[back-of-house-patterns]], [[single-agent-ceiling]], [[subagents]]
sources:
  - raw/articles/anthropic-claude-code-session-management-1m-context.md
  - raw/articles/milksandmatcha-0xsero-single-agent-nightmare-2026.md
---

# Session Hierarchy Management

**Session Hierarchy Management** is a three-level framework for organizing AI coding work across session boundaries. It unifies **single-session context hygiene** (trq212/Anthropic) with **multi-agent architecture patterns** (Back of House / @MilksandMatcha + @0xSero) into a coherent strategy for long-horizon development.

The core insight: **context bloat is inevitable at every scale, but each scale requires a different intervention.**

---

## Level 1: Single-Session Context Hygiene

*Source: [[thariq-shihipar]] (Anthropic Claude Code team), "Claude Code Session Management & 1M Context" (April 2026)*

At the individual session level, the challenge is **context rot** — performance degradation as the window fills with stale debugging history, failed attempts, and irrelevant tool outputs.

### The 1M Context Reality

Claude Code now operates with a **1,000,000 token context window**. This changes the economics of session management:

| Before 1M | After 1M |
|-----------|----------|
| Auto-compact triggered near ceiling | Proactive manual compact with steering |
| Lossy summaries by default | Time to specify: `/compact focus on X, drop Y` |
| Fear of losing context | Strategic compression at chosen moments |

### Five Session Branching Primitives

Every completed turn presents a branching point:

| Strategy | Command | When to Use |
|----------|---------|-------------|
| **Continue** | Send next prompt | Context remains fully relevant |
| **Rewind** | `/rewind` or `Esc Esc` | Wrong path taken; preserve useful file reads |
| **Compact** | `/compact` | Session bloated with stale debugging/exploration |
| **Clear** | `/clear` | Genuinely new task; zero rot |
| **Subagents** | Explicit prompt | Heavy intermediate output where only conclusion matters |

### Decision Heuristic

> "The mental test we use at Anthropic: **will I need this tool output again, or just the conclusion?**"
> — Thariq Shihipar

If the answer is "just the conclusion," spawn a subagent. This is the bridge to Level 2.

### Proactive Compaction

With 1M tokens, **manual compaction beats automatic**:

> "Bad compacts can happen when the model can't predict the direction your work is going... With one million context, you have more time to `/compact` proactively with a description of what you want to do."

**Cost/Speed Tradeoff:** Reusing context (`Continue`/`/compact`) avoids re-reading files, saving time and tokens compared to `/clear`. Only clear when the task fundamentally shifts.

---

## Level 2: Multi-Agent Context Separation

*Source: [[back-of-house-patterns]] — @MilksandMatcha + @0xSero (April 2026)*

When a task generates heavy intermediate output (codebase exploration, verification passes, doc generation), **Level 1 primitives are insufficient**. The session accumulates tool-call noise that degrades the model's attention, even within 1M tokens.

### The Back of House Architecture

Instead of one agent doing everything, separate concerns across **fresh context windows**:

```
Human → Head Chef (Orchestrator) → Line Cooks (Subagents) → Results
         [named session]           [fresh context each]     [summaries only]
```

**Head Chef (Orchestrator):**
- Takes human orders, breaks them into scoped, verifiable tickets
- Only tool: `delegate_task`
- Never reads/writes files directly
- Only sees high-level goals + subagent output summaries
- Maintains a **named session** with full project context

**Line Cooks (Subagents):**
- Each gets a **fresh context window** starting only with their assigned prompt
- Can read, write, use MCPs, and any tools needed
- Return results and clock out — no state accumulation
- **Minimum viable context** for one specific dish

### Effective Context Window Expansion

| Metric | Single Agent | Back of House |
|--------|-------------|---------------|
| Context window | ~1M tokens | ~25M+ tokens (N subagents × 1M each) |
| Context rot | Inevitable | Isolated per subagent |
| Manual interventions | High (12+ per task) | Low (2 per task, 84.3% reduction) |
| Success rate | 0% on complex tasks | 100% on first try (Figma MCP benchmark) |

### The State Principle

> **状態はファイルとタスクキューに保存され、会話履歴には保存されない。**
> *(State lives in files and task queues, not in conversation history.)*

This is the unifying principle between Level 1 and Level 2. Whether you're using `/compact` in a single session or spawning subagents, the goal is the same: **keep the conversational context lean, push durable state to the filesystem.**

---

## Level 3: Sequential + Parallel Orchestration

*Source: Synthesis of both frameworks*

The highest level of session hierarchy management combines **sequential discipline** with **parallel execution** across multiple orchestrated sessions.

### Five Orchestration Patterns

#### Pattern 1: The Prep Line (Parallel Exploration)
- Multiple subagents independently explore the same brief
- Human curates the best results
- **No file conflicts, no dependencies** — easiest entry point
- Real example: 5 Codex Spark subagents × 10 mascot variations = 50 options in ~1 minute

#### Pattern 2: The Dinner Rush (Parallel Swarm)
- Multiple subagents fire simultaneously on different tasks
- Each owns a distinct, non-overlapping file set
- **Critical requirement:** Tasks must not share files
- Good for: building multiple independent components, writing tests for different modules

#### Pattern 3: Courses in Sequence (Phased Parallel)
- Project broken into "courses" (waves) with strict dependencies
- Within each course, parallel execution
- Each course's subagents get only the context brief relevant to their ticket
- Good for: full app rebuilds, large refactors

#### Pattern 4: The Prep-to-Plate Assembly (Sequential Pipeline)
- Each subagent does one bounded task, validates, hands off
- **Clean handoffs between phases** — no dragging unrelated history
- Good for: long-horizon tasks, research-heavy workflows, multi-step pipelines
- State lives in files; each phase reads only what it needs

#### Pattern 5: Gordon Ramsay (Build + Verify Separation)
- **Apply this on top of every other pattern.**
- One builder writes code; multiple verifiers run in parallel (code review + functional testing)
- If either verifier flags an issue, the builder gets another pass
- With fast models (~1,200 toks/sec), verification is practically free
- **Single most important rule for avoiding merge conflicts and context drift**

---

## Unified Decision Tree

```
Is this a new task?
├── YES → /clear (Level 1) or new Head Chef session (Level 2)
└── NO → Is the context still relevant?
    ├── YES → Continue (Level 1)
    └── NO → Is it bloated or wrong path?
        ├── Wrong path → Rewind (Level 1)
        └── Bloated → Is it just noisy tool outputs?
            ├── YES → Subagent for the noisy part (Level 1→2 bridge)
            └── NO (too big for subagent) → /compact with steering (Level 1)

Is the task multi-phase with verifiable milestones?
├── YES → Back of House pattern (Level 2/3)
│   ├── Phases depend on each other → Courses in Sequence or Prep-to-Plate
│   ├── Phases are independent → Dinner Rush or Prep Line
│   └── Always → Add Gordon Ramsay verification layer
└── NO → Single session is fine (Level 1)
```

---

## Anti-Patterns and Their Fixes

| Anti-Pattern | Level | Symptom | Fix |
|-------------|-------|---------|-----|
| **The Sloperator** | 2 | One-shot everything, expects agent to do it all | Decompose into tickets, use Head Chef pattern |
| **The Hoarding Session** | 1 | Never compacting, context rots | Proactive `/compact` with steering at 40-60% usage |
| **The Context Dump** | 1 | Pasting entire files into prompts | Use tool-based file reading; subagents for exploration |
| **The Drifting Task** | 1 | Task shifts without session reset | `/clear` or new session for fundamentally different work |
| **The Over-Compact** | 1 | Aggressive compression loses nuance | Use 1M runway to compact manually with specific instructions |
| **The File Collision** | 3 | Two subagents overwrite each other | Use Dinner Rush prerequisites or switch to Prep-to-Plate |
| **The Merge Conflict Cascade** | 3 | Multiple builders write simultaneously | Gordon Ramsay rule: one builder, multiple verifiers |

---

## The Filesystem as Universal Interface

Both frameworks converge on the same insight from [[thariq-shihipar]]:

> "Your Agent should use a File System. This is a hill I will die on. Every agent can use a file system. The file system is an elegant way of representing state that your agent could read into context & allowing it to verify its work."

**Why filesystems work for agents:**
- Unlimited storage capacity (vs. finite context windows)
- Persistent across sessions (vs. ephemeral conversation history)
- Searchable with standard tools (grep, find, SQL)
- Human-readable (JSON, Markdown, code)
- Git-trackable audit trail
- Multiple agents can collaborate without conflicts (with proper scoping)

This makes the filesystem the **coordination layer** between Head Chef and Line Cooks, and between sequential subagent phases.

---

## Related Concepts

- [[context-window-management]] — Level 1: single-session context hygiene
- [[back-of-house-patterns]] — Level 2: multi-agent architecture
- [[single-agent-ceiling]] — The problem this framework solves
- [[subagents]] — The primitive that bridges Level 1 and Level 2
- [[context-engineering]] — Filesystem-as-context methodology
- [[thariq-shihipar]] — Architect of Claude Code session management
- [[milksandmatcha]] — Co-author of Back of House patterns

## Sources

- [Thariq Shihipar: "Using Claude Code: Session Management & 1M Context"](https://claude.com/blog/using-claude-code-session-management-and-1m-context) — Anthropic official blog (April 2026)
- [Sarah Chieng + @0xSero: "Single-agent AI coding is a nightmare for engineers"](https://x.com/milksandmatcha/status/2044863551186309460) — Back of House multi-agent patterns (April 2026)
- Thariq Shihipar X thread: "Your Agent should use a File System" — Filesystem-as-context philosophy
- Claude Code source code analysis — Session branching primitives and compaction behavior
