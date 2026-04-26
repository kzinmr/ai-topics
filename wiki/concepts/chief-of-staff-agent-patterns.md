---
title: "Chief of Staff Agent Patterns"
tags: [[claude-agent-sdk-orchestration-hooks-subagents-plan-mode-output-styles]]
created: 2026-04-24
updated: 2026-04-24
---

# Chief of Staff Agent Patterns

Anthropic cookbook: [The Chief of Staff Agent](https://platform.claude.com/cookbook/claude-agent-sdk-01-the-chief-of-staff-agent)

## Core Concept

Build a **coordinating agent** for a 50-person B2B SaaS startup that manages specialized subagents, aggregates multi-source insights, and delivers executive summaries with actionable recommendations. Demonstrates 7 foundational SDK patterns in one end-to-end architecture.

> *"The Chief of Staff doesn't execute tasks — it coordinates specialized subagents, aggregates insights, and delivers structured recommendations."*

## Critical SDK Configuration

The SDK operates in **isolation mode by default**. Filesystem-based settings must be explicitly loaded via `setting_sources`:

| Setting Source | Loads From | Required For |
|----------------|------------|--------------|
| `["project"]` | `.claude/settings.json`, `CLAUDE.md`, output styles, slash commands | Features 0, 2, 4, 6 |
| `["project", "local"]` | Adds `.claude/settings.local.json` | Feature 5 (Hooks) |
| `["user"]` | `~/.claude/settings.json` | Global user preferences |

```python
options = ClaudeAgentOptions(
    model="claude-opus-4-6",
    cwd="chief_of_staff_agent",
    setting_sources=["project", "local"],  # REQUIRED for filesystem settings
)
```

## The 7 Patterns

### Pattern 1: CLAUDE.md as Persistent Memory

**What:** Project context and instructions stored in `CLAUDE.md` in the working directory.

**Key Insight:**
> `CLAUDE.md` provides **context and guidance, not hard constraints**. Agents naturally seek the most authoritative data (e.g., CSVs over MD). Use explicit prompts to force high-level context usage.

**Architecture Pattern:** Treat `CLAUDE.md` as an *onboarding document*; detailed files are *source systems* for precision.

### Pattern 2: Bash Tool for Script Execution

**What:** Run Python scripts for procedural knowledge, complex computations, and data analysis.

**How:** Add `allowed_tools=["Bash", "Read"]`. Document scripts in `CLAUDE.md` or agent-specific MD files.

**Example Scripts:**
- `hiring_impact.py` → Models burn/runway impact of new hires
- `talent_scorer.py` → Weighted candidate scoring
- `financial_forecast.py` → ARR growth scenarios (base/optimistic/pessimistic)
- `decision_matrix.py` → Strategic choice evaluation

### Pattern 3: Output Styles

**What:** Tailor response tone/depth for different audiences without creating separate agents.

**How:** Markdown files in `.claude/output-styles/` with frontmatter (`name`, `description`).

```python
settings='{"outputStyle": "executive"}',
setting_sources=["project"]
```

**Impact:** Modifies the underlying system prompt, stripping software-engineering focus for domain-specific use cases.

### Pattern 4: Plan Mode (Strategic Planning Without Execution)

**What:** Generate detailed execution plans for review before taking action. Reduces errors in high-stakes decisions.

**How:** Set `permission_mode="plan"`. Agent stops after planning phase.

**Workflow:** `Plan → Review → Approve → Execute`

**Robust Plan Capture Mechanism:** Multi-source fallback handles varying agent behaviors:
1. **Message Stream** (Preferred): Extract `<plan>` XML tags from response
2. **Write Tool**: Capture `content` parameter if agent saves to file
3. **Claude Internal Dir**: Fallback to `~/.claude/plans/*.md` (<5 min old)

```python
def extract_plan_from_xml(text: str | None, min_length: int = 200) -> str | None:
    match = re.search(r"<plan>(.*?)</plan>", text, re.DOTALL)
    if match:
        extracted = match.group(1).strip()
        return extracted if len(extracted) > min_length else None
    return None
```

**Prompt Engineering:** Explicitly instruct: `DO NOT use the Write tool`, `Wrap ENTIRE plan inside <plan> </plan> XML tags`

**Resume Execution:** Use `continue_conversation=True` and remove plan mode to proceed from the plan.

### Pattern 5: Custom Slash Commands

**What:** Predefined prompt templates for recurring questions. Syntactic sugar for consistency.

**How:** Markdown in `.claude/commands/` with frontmatter. Supports `$ARGUMENTS`, `$1`, `$2`.

```markdown
---
name: budget-impact
description: Analyze the budget impact of a proposed action
---
Analyze the budget impact of $ARGUMENTS. Include burn rate changes, runway implications, and trade-offs.
```

**Usage:** User types `/budget-impact hiring 3 engineers` → Expands to vetted, structured prompt.

### Pattern 6: Hooks (Automated Deterministic Actions)

**What:** Enforce guardrails, create audit trails, run deterministic logic pre/post tool calls.

**How:** Scripts in `.claude/hooks/`, config in `.claude/settings.local.json`.

```json
"hooks": {
  "PostToolUse": [
    {"matcher": "Write", "hooks": [{"type": "command", "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/report-tracker.py"}]},
    {"matcher": "Edit", "hooks": [{"type": "command", "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/edit-audit.py"}]}
  ],
  "PreToolUse": [
    {"matcher": "Bash", "hooks": [{"type": "command", "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/command-logger.py"}]}
  ]
}
```

**Hook Types:**
- `PreToolUse`: Runs BEFORE tool execution. Can block the action (non-zero exit).
- `PostToolUse`: Runs AFTER tool execution. Good for audit logging, notifications.

### Pattern 7: Subagent Orchestration via Task Tool

**What:** Delegate specialized work to subagents running in parallel.

**How:** Use the `Task` tool with custom prompts. Each subagent gets isolated context and tool permissions.

```python
# Chief of Staff delegates to specialists
task_tool.invoke({
    "description": "Analyze hiring impact",
    "prompt": "Run hiring_impact.py with 3 senior engineers...",
    "subagent_type": "code-explorer"
})
```

**Workflow:**
1. Chief receives high-level request
2. Spawns 3-4 subagents for parallel analysis (hiring, finance, product, market)
3. Aggregates results into executive summary
4. Delivers structured recommendation with confidence levels

## Production Architecture

```
Executive Request
    │
    ▼
Chief of Staff Agent (claude-opus-4-6)
    │
    ├── CLAUDE.md → Context & guidance
    ├── Bash → Script execution (Python analysis)
    ├── Task → Subagent delegation (parallel)
    ├── Output Styles → Audience-tailored responses
    ├── Hooks → Audit trails & guardrails
    └── Plan Mode → Strategy before execution
```

## Key Insights

1. **setting_sources is Critical**: Without `["project", "local"]`, the SDK ignores all filesystem settings (CLAUDE.md, hooks, output styles, slash commands).
2. **CLAUDE.md ≠ Hard Constraint**: Agents follow data authority gradients. CSV > MD for facts. Use explicit prompts to enforce context usage.
3. **Plan Mode + XML Tags**: Structured plan extraction requires explicit XML wrapping instructions. Multi-source fallback handles edge cases.
4. **Hooks as Audit Trail**: PreToolUse for validation, PostToolUse for logging. Non-zero exit blocks execution.
5. **Subagent Isolation**: Each Task gets fresh context. The coordinator aggregates results without shared state pollution.

## Comparison: When to Use Which Pattern

| Pattern | Best For | When to Skip |
|---------|----------|-------------|
| Plan Mode | High-stakes decisions, strategy | Simple, low-risk tasks |
| Hooks | Audit requirements, compliance | Rapid prototyping |
| Output Styles | Multi-audience reporting | Single-purpose agents |
| Subagents | Parallel analysis, delegation | Sequential, dependent steps |
| CLAUDE.md | Project-wide context | Single-session tasks |
| Slash Commands | Recurring query patterns | Ad-hoc, unique requests |

## Related

- [[claude-agent-sdk-sre-patterns]] — MCP integration and safety guardrails
- [[managed-agents-sre-incident-response]] — Human-in-the-loop approval patterns
-  — Managing long-running agent context
- [[research-agent-fundamentals]] — Stateless vs stateful agent patterns
