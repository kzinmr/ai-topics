---
title: "Claude Certified Architect — 5 Domain Knowledge"
created: 2026-05-11
updated: 2026-05-26
type: concept
tags:
  - claude-code
  - anthropic
  - mcp
  - prompting
  - multi-agent
  - orchestration
  - context-engineering
  - education
sources:
  - raw/articles/2026-03-15_hooeem_claude-certified-architect-full-course.md
aliases:
  - Claude Architect Exam
  - Claude Certified Architect
  - Claude Certification
related:
  - "[[concepts/claude-code-best-practices]]"
  - "[[concepts/claude/agent-sdk-sre-patterns]]"
  - "[[concepts/subagents]]"
  - "[[concepts/claude-md-rules]]"
  - "[[concepts/multi-agent-orchestration]]"
  - "[[entities/claude-code]]"
---

# Claude Certified Architect — 5 Domain Knowledge

Knowledge system for all 5 domains of the Claude Certified Architect (Foundations) certification exam. While the exam is limited to partners, this knowledge directly applies to production-grade Claude application development. Passing score: 720/1000. **Tends to prioritize deterministic solutions over probabilistic ones.**

Exam scenarios: Customer Support Resolution Agent, Code Generation with Claude Code, Multi-Agent Research System, Developer Productivity Tools, Claude Code for CI/CD, Structured Data Extraction.

## Domain 1: Agentic Architecture & Orchestration (27%)

### 1.1 Agentic Loop — stop_reason Mechanics

Complete lifecycle of the agent loop:

```
Send request to Messages API
  → Inspect stop_reason field
    → "tool_use": Execute tool → add result to conversation history → resend
    → "end_turn": Agent complete → present final response
```

**3 Anti-patterns (should be immediately eliminated in the exam):**
1. **Natural language termination detection**: Checking if the assistant says "I'm done" → ambiguous and unreliable. The `stop_reason` field is the only correct method.
2. **Arbitrary iteration limit**: "Stop after 10 loops" → either cuts off useful work or runs unnecessary iterations. The model signals completion via `stop_reason`.
3. **Text content checking**: `response.content[0].type == "text"` → models can return text simultaneously with tool_use blocks.

**Model-driven vs Pre-configured**: The exam favors model-driven approaches for flexibility, but **programmatic enforcement for critical business logic** (see 1.4).

### 1.2 Multi-Agent Orchestration — Hub-and-Spoke

Coordinator-centric hub-and-spoke architecture:

- **Coordinator**: Task decomposition, sub-agent selection, context passing, result aggregation, error handling, information routing
- **Sub-agents**: Specialized task spokes. **Do not communicate directly with each other.** All communication is through the coordinator.

**Isolation principle (the most misunderstood concept):**
- Sub-agents **do not automatically inherit** the coordinator's conversation history
- Sub-agents **do not share memory** between invocations
- All necessary information must be explicitly passed in the prompt

**Narrow decomposition failure (exam-specific problem)**: The coordinator decomposes "AI's impact on creative industries" into only visual arts, completely overlooking music, writing, and film. Root cause is the coordinator's decomposition, not the downstream agents. **The exam expects you to trace failures to their source.**

### 1.3 Subagent Invocation — Task Tool & Context Passing

**Task Tool**: The mechanism for spawning sub-agents from the coordinator. The coordinator must have `"Task"` included in its `allowedTools`. Each sub-agent has an `AgentDefinition` (description, system prompt, tool restrictions).

**Context passing principles:**
- Include the complete discovery results from preceding agents directly in the sub-agent's prompt
- Use structured data formats with separated content and metadata (source URL, document name, page number)
- Specify **research goals and quality standards** rather than step-by-step procedural instructions (enabling sub-agent adaptability)

**Parallel generation**: Issue multiple Task tool calls in a single coordinator response for parallel sub-agent generation. Faster than sequential calls.

**fork_session**: Creates independent branches from a shared analysis baseline. After branching, each fork operates independently (e.g., comparing two testing strategies from the same codebase analysis).

### 1.4 Workflow Enforcement — Programmatic vs Prompt

**Enforcement Spectrum:**

| Method | Reliability | When to Use |
|--------|------------|-------------|
| Prompt-based instructions | Works most of the time. Non-zero failure rate | Low risk (formatting, style guidelines) |
| Programmatic enforcement (Hooks/Gates) | Works every time | **Finance, Security, Compliance** |

**Exam decision rule**: If the outcome involves **finance, security, or compliance** → use programmatic enforcement. When the exam presents prompt-based solutions for high-risk scenarios → **reject them**.

**Structured handoff protocol**: When escalating to a human agent:
- Customer ID, conversation summary, root cause analysis, refund amount (if applicable), recommended actions
- Human agents **cannot access** conversation transcripts → handoff summary must be self-contained

**Sample problem**: A customer support agent processes refunds without account ownership verification in 8% of cases. Options: A) Programmatic precondition gate, B) Enhanced system prompt, C) Few-shot examples, D) Routing classifier. **Correct answer is A.** B/C/D are insufficient.

### 1.5 Agent SDK Hooks

**PostToolUse Hook**: Intercepts tool results after execution, before the model processes them.
- Use cases: Normalizing heterogeneous data formats from different MCP tools (Unix timestamps → ISO 8601, numeric status codes → human-readable strings)
- The model receives clean, consistent data regardless of the tool

**Tool Call Interception Hook**: Intercepts outgoing tool calls before execution.
- Use cases: Blocking refunds over $500 and redirecting to human escalation
- Use cases: Enforcing compliance rules (requiring manager approval for specific operations)

**Decision framework:**
- Hooks = deterministic guarantees. Use for business rules requiring 100% compliance.
- Prompts = probabilistic guidance. Use for configuration and soft rules.
- If a single failure causes financial loss or legal risk → use hooks.

### 1.6 Task Decomposition — Sequential vs Adaptive

| Pattern | Description | Best For | Advantages | Limitations |
|---------|-------------|----------|------------|-------------|
| **Fixed Sequential Pipeline** | Pre-determined sequential steps | Code review, document processing | Consistency, reliability | Cannot adapt to unexpected findings |
| **Dynamic Adaptive Decomposition** | Sub-task generation based on each step's findings | Open-ended research tasks | Adapts to the problem | Lower predictability |

**Attention dilution problem**: Processing many files in a single pass results in uneven depth.
- Fix: Split into **per-file local analysis pass + cross-file integration pass**
- Missing obvious bugs in some files during a 14-file code review, while inconsistently accepting/rejecting the same pattern in other files → cause is attention dilution in single-pass review

### 1.7 Session State & Resumption

| Method | When to Use |
|--------|-------------|
| `--resume <session-name>` | Previous context is mostly valid, no major file changes |
| `fork_session` | Exploring different approaches from a shared analysis point |
| New start with summary injection | Tool results are stale, files have changed, long session with degraded context |

**Stale context problem**: When resuming after code modifications, **notify the agent about specific file changes** and perform targeted re-analysis. No need to have it re-explore everything. Starting fresh with summary injection is more reliable than resuming with stale tool results.

## Domain 2: Tool Design & MCP Integration (18%)

### Importance of Tool Descriptions

Tool descriptions are the **primary mechanism** Claude uses for tool selection. If descriptions are vague or overlapping, selection becomes unreliable.

- Sample problem: `get_customer` and `lookup_order` have nearly identical descriptions and constantly mis-route → fix is better descriptions (not few-shot examples, not routing classifiers, not tool consolidation)
- Giving 18 tools reduces selection reliability → scope to 4-5 tools relevant to each sub-agent's role

### tool_choice Options

| Option | Behavior | When to Use |
|--------|----------|-------------|
| `"auto"` | Model may return text | Default. When tool calls are not required |
| `"any"` | Tool call required, model chooses | When some tool use is needed but which one is up to the model |
| Force selection | Must call a specific tool | When a specific tool execution is absolutely required |

## Domain 3: Claude Code Configuration & Workflows (20%)

### CLAUDE.md Hierarchy (3 Levels)

| Level | Location | Characteristics |
|-------|----------|-----------------|
| User-level | `~/.claude/CLAUDE.md` | Not version-controlled, not shared |
| Project-level | `.claude/CLAUDE.md` | Version-controlled, team-shared |
| Directory-level | Files within subdirectories | Directory-bound |

**Exam trap**: Team members miss instructions because they're in user-level settings (not version-controlled, not shared).

### Path-Specific Rules (Most Important Concept)

Rule files in `.claude/rules/` with YAML frontmatter glob patterns (e.g., `**/*.test.tsx`). Apply conventions across the entire codebase. Directory-level CLAUDE.md cannot do this (directory-bound).

### Plan Mode vs Direct Execution

| Plan Mode | Direct Execution |
|-----------|-----------------|
| Monolith restructuring, multi-file migration, architecture decisions | Single-file bug fix, one validation check, clear scope |

### Other Important Concepts
- **context: fork** in skill frontmatter (isolates verbose output)
- **`-p` flag**: Non-interactive CI/CD
- **Independent review instance**: Catches more issues than self-review in same session

## Domain 4: Prompt Engineering & Structured Output (20%)

### Core Principle: Be Explicit

"Be conservative" does not improve accuracy. "Only report high-confidence findings" does not reduce false positives.
**What works**: Precisely define what to report and what to skip, with concrete code examples for each severity level.

### Few-Shot Examples (Highest Leverage Technique)

2-4 targeted examples. Show edge case handling, include **reasoning for why the chosen action was selected over alternatives**.

### tool_use with JSON Schemas

- Syntax errors are eliminated, but **semantic errors are not**
- Schema design best practices:
  - **Nullable fields** when source data may not exist (prevents fabricated values)
  - **"unclear" enum values**
  - **"other" + detail string**

### Message Batches API

- 50% cost reduction, up to 24-hour processing, no latency SLA, no multi-turn tool calls
- Use Batch for nightly reports, Synchronous for blocking pre-merge checks

## Domain 5: Context Management & Reliability (15%)

### 5.1 Context Preservation — Progressive Summarization Trap

Condensing conversation history compresses **numbers, dates, percentages, and customer expectations** into vague summaries:
- "Customer wants a refund of $247.83 for order #8891 from March 3rd" → "Customer wants a refund for a recent order"
- **Fix**: Extract transactional facts into a persistent "case facts" block. Include in every prompt. **Never summarize it.**

### "Lost in the Middle" Effect

Models reliably process the **beginning and end** of long inputs, but may miss findings buried in the middle.
- **Fix**: Place key findings summary at the top. Use explicit section headers.

### Tool Result Trimming

An order search returns 40+ fields. Only 5 are needed.
- Trim redundant results to only relevant fields **before** adding to context
- Prevents token budget exhaustion from accumulated irrelevant data

### 5.2 Escalation Triggers

**3 Valid Escalation Triggers:**

| Trigger | Action |
|---------|--------|
| Customer explicitly requests a human | Respond immediately. Do not try to resolve first |
| Policy exception or gap | Outside documented policy scope (e.g., competitor price matching against a policy covering only own site) |
| Inability to make meaningful progress | Agent cannot move resolution forward |

**2 Unreliable Triggers** (the exam will tempt you with these):
1. **Sentiment analysis-based escalation**: Frustration does not correlate with case complexity
2. **Self-reported confidence scores**: Models tend to be overconfident on hard cases and uncertain on easy ones

### 5.3 Structured Error Propagation

Information to pass during errors:
- Failure type (transient, validation, business, permission)
- What was attempted (specific queries, parameters used)
- Partial results collected before failure
- Potential alternative approaches

**2 Anti-patterns:**
1. **Silent suppression**: Returning empty results as success. Non-recoverable.
2. **Workflow termination**: Forcing entire pipeline shutdown on single failure. Discarding partial results.

**Access failure vs Valid empty result**: Access failure (consider retry) ≠ Valid empty result (that is the answer, no retry needed).

### 5.4 Codebase Exploration & Context Degradation

Context degradation over long sessions: The model begins referencing "typical patterns" rather than specific classes previously discovered.

**Mitigation strategies:**
- **Scratchpad files**: Write key findings to a file, reference in subsequent questions
- **Sub-agent delegation**: Spawn sub-agents for specific investigations, main agent maintains high-level coordination
- **Summary injection**: Summarize one phase's findings before spawning the next phase's sub-agent
- **/compact**: Use when context is full of verbose discovery output

**Crash recovery**: Each agent exports structured state to a known file location (manifest). On resumption, the coordinator loads the manifest and injects it into the agent prompt.

### 5.5 Human Review & Confidence Calibration

**Aggregate metrics trap**: 97% overall accuracy may hide a 40% error rate on specific document types. Always verify accuracy **by document type and field segment** before automation.

**Stratified random sampling**: Sample high-confidence extractions for continuous verification. Detects new error patterns that are easily overlooked.

**Field-level confidence calibration:**
- Model outputs confidence per field
- Calibrate thresholds using a labeled validation set (ground truth data)
- Route low-confidence fields to human review
- Prioritize limited reviewer capacity toward the highest-uncertainty items

### 5.6 Information Provenance

**Structured Claim-Source Mapping:**
Each finding: claim + source URL + document name + relevant excerpt + publication date
Downstream agents must preserve and merge these mappings through synthesis. Without this, attribution disappears during summarization.

**Conflict handling**: Two reliable sources report different statistics → do not arbitrarily choose one. Annotate with both values and source attributes. Let the consumer decide.

**Temporal awareness**: Require publication/data collection dates in structured output. Different dates explain different numbers (not a contradiction).

**Content-appropriate rendering**: Financial data → tables, news → prose, technical findings → structured lists. Do not flatten everything into a single uniform format.

## Reference Links from the Article

- [Claude Agent SDK Overview](https://platform.claude.com/docs/en/agent-sdk/overview)
- [Building Agents with the Claude Agent SDK](https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk)
- [Claude Agent SDK Python](https://github.com/anthropics/claude-agent-sdk-python)
- [Claude Code Official Docs](https://code.claude.com/docs/en/mcp)
- [Claude Code CLI Cheatsheet](https://shipyard.build/blog/claude-code-cheat-sheet/)
- [Creating the Perfect CLAUDE.md](https://dometrain.com/blog/creating-the-perfect-claudemd-for-claude-code/)
- [Everything Claude Code](https://github.com/affaan-m/everything-claude-code)
- [Anthropic Prompt Engineering Docs](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview)
- [MCP Specification](https://github.com/modelcontextprotocol)
- [Claude Code in Action (Anthropic Skilljar)](https://anthropic.skilljar.com/claude-code-in-action)
