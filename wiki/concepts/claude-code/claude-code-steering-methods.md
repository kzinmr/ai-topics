---
title: "Claude Code Steering Methods"
created: 2026-06-21
updated: 2026-06-21
type: concept
tags:
  - claude-code
  - coding-agents
  - ai-agents
  - customization
  - hooks
  - skills
  - rules
  - claudefile
  - developer-tooling
sources: [raw/articles/2026-06-18_anthropic_steering-claude-code-skills-hooks-rules-subagents-and-more.md]
---

# Claude Code Steering Methods

Claude Code provides seven distinct methods for instructing and customizing Claude's behavior, each with different characteristics regarding when instructions load, how they persist through sessions, and what authority they carry. Understanding these methods is essential for effective [[entities/claude-code]] customization and [[concepts/agentic-engineering]].

## The Seven Methods

### 1. CLAUDE.md Files

**CLAUDE.md** is a markdown file at the root of your project that loads into context at session start and stays there for the entire session. This is the primary method for project-specific instructions.

**Two types with different loading behavior:**
- **Always loaded**: Root CLAUDE.md files (shared repository or local personal preferences) load at session start and persist through compaction
- **On-demand**: Subdirectory CLAUDE.md files load only when Claude reads files within that directory

**Best for:** Build commands, directory layout, monorepo structure, coding conventions, team norms

**Key considerations:**
- Every line loads into every session for every engineer, consuming tokens regardless of relevance
- Keep under 200 lines, give it an owner, review changes like code
- In monorepos, use subdirectory CLAUDE.md files for team-specific conventions
- For organization-wide standards (security, compliance), deploy centrally via MDM

### 2. Rules

**Rules** are markdown files in `.claude/rules/` that provide specific constraints or conventions. They can be unscoped (always loaded) or path-scoped (loaded only when relevant files are accessed).

**Path-scoped rules example:**
```yaml
---
paths:
  - "src/api/**"
  - "**/*.handler.ts"
---
All API handlers must validate input with Zod before processing.
```

**Best for:** File-specific constraints (e.g., "migrations are append-only"), cross-cutting concerns that appear in multiple but not all corners of the codebase

**Key considerations:**
- Unscoped rules behave like CLAUDE.md (always loaded, re-injected on compaction)
- Path-scoped rules stay out of context until relevant files are touched
- Prefer path-scoped rules over nested CLAUDE.md for targeted instructions

### 3. Skills

**Skills** live in `.claude/skills/` as folders containing `SKILL.md` files with name, description, and body. Only name and description load at session start; the full body loads when invoked via slash command or auto-matching.

**Compaction behavior:** Invoked skills re-inject up to a shared budget; oldest dropped first

**Best for:** Procedural workflows (deploy checklists, release processes, review procedures)

**Key considerations:**
- Low context cost—full body loads only when invoked
- Claude Code ships with built-in skills (`/code-review`, etc.)
- Custom skills can be created for team-specific procedures
- Skills are triggered via the system prompt

### 4. Subagents

**Subagents** are markdown files in `.claude/agents/` defining isolated assistants for side tasks. They use YAML frontmatter (name, description, model, tool access) followed by a system prompt body.

**Key characteristics:**
- Name, description, and tool list load at session start
- Body loads only when called via the Agent tool
- Runs in its own fresh context window
- Only final message (summary + metadata) returns to main session
- Can nest up to five levels deep

**Best for:** Deep search, log analysis, dependency audit—any side task that would clutter main conversation with intermediate results

**Key considerations:**
- Zero cost in main context until called
- Isolation prevents intermediate results from polluting main thread
- Dynamic workflows can orchestrate tens to hundreds of background agents
- Use skills when you want to see and steer each step; use subagents for isolation

### 5. Hooks

**Hooks** are user-defined commands, HTTP endpoints, or LLM prompts that fire on specific lifecycle events (file edits, tool calls, session start). Registered in `settings.json`, managed policy settings, or skill/agent frontmatter.

**Hook types:** command, HTTP, mcp_tool, prompt, agent

**Key characteristics:**
- Deterministically triggered (first three types execute deterministically; prompt/agent use Claude's judgment)
- Low context cost—configuration lives outside main context
- Bypass compaction entirely
- Some output may return to context (e.g., blocking errors)

**Best for:** Deterministic automation—running linters after edits, posting to Slack on completion, blocking specific commands, backing up chat history on PreCompact

**Key considerations:**
- `PreToolUse` hook can inspect any tool call and exit code 2 to deny it
- Managed settings provide organization-wide guardrails that can't be overridden locally
- Hooks are code that the harness runs, not instructions loaded into context

### 6. Output Styles

**Output styles** are files in `.claude/output-styles/` that inject instructions into the system prompt. They never get compacted, load at session start, and are cached after first request.

**Key characteristics:**
- Highest instruction-following weight of any method
- Changes replace default output style (unless `keep-coding-instructions: true`)
- Moderate context cost—occupies context window but overwrites default system prompt

**Best for:** Significant role changes (code assistant to general assistant)

**Key considerations:**
- Default Claude Code instructions (scoping changes, code comments, security concerns, verification habits) are removed with custom styles
- Built-in styles (`Proactive`, `Explanatory`, `Learning`) cover most common needs
- Use judiciously due to high authority

### 7. Appending the System Prompt

The `append-system-prompt` flag adds instructions to Claude's default role without modifying it. Passed at invocation time, applies only to that invocation.

**Key characteristics:**
- Never compacted; applies only to that invocation
- Moderate context cost—cached after first request in session
- Only additive to original system prompt

**Best for:** Adding specific coding standards, output formatting, domain-specific knowledge

**Key considerations:**
- Diminishing returns for adherence with more instructions
- Contradicting instructions reduce effectiveness
- Higher input tokens (though prompt caching reduces cost)

## Method Comparison

| Method | When Loaded | Compaction | Context Cost | Best Use Case |
|--------|-------------|------------|--------------|---------------|
| CLAUDE.md (root) | Session start | Memoized, re-read after compaction | High | Build commands, conventions, team norms |
| CLAUDE.md (subdir) | On-demand | Lost until directory touched | Low | Subdirectory-specific conventions |
| Rules | Session start or path-triggered | Re-injected on compaction | Medium | Specific constraints, cross-cutting concerns |
| Skills | Name/desc at start; body on invoke | Re-injected up to shared budget | Low | Procedural workflows |
| Subagents | Name/desc/tools at start; body on call | Only final message returns | Low | Isolated side tasks |
| Hooks | Lifecycle events | Bypass compaction | Low | Deterministic automation |
| Output styles | Session start | Never compacted | High | Role changes |
| System prompt append | Session start (CLI flag) | Never compacted | Moderate | Tone, formatting preferences |

## Quick Decision Guide

**"Every time X, always do Y" in CLAUDE.md** → Use a hook in `settings.json` instead. The model choosing to run a formatter is different from the formatter running automatically.

**"Never do this" in CLAUDE.md** → Use hooks and permissions. A `PreToolUse` hook can inspect calls and block them deterministically. Managed settings provide organization-wide guardrails.

**A 30-line procedure in CLAUDE.md** → Move to a skill. CLAUDE.md is for facts Claude should hold all the time; procedures belong in skills where they load only when invoked.

**An API-specific rule without paths** → Scope with `paths:` to keep it out of context during unrelated work.

**Personal preferences in project-level CLAUDE.md** → Use local files for personal preferences; keep project-level files for team-wide but codebase-specific preferences.

## Related Concepts

- [[entities/claude-code]] — Claude Code as a coding agent
- [[concepts/agentic-engineering]] — Patterns for building agent-based systems
- [[entities/coding-agents]] — AI agents for software development
- [[concepts/mcp]] — Model Context Protocol for tool integration
- [[agent-orchestration]] — Coordinating multiple agents
- [[concepts/context-engineering]] — Managing context windows effectively

## Further Reading

- [CLAUDE.md files: Customizing Claude Code for your codebase](https://claude.com/blog/claude-md-files)
- [Best practices for Claude Code](https://docs.anthropic.com/en/docs/claude-code/best-practices)
- [How to configure hooks](https://docs.anthropic.com/en/docs/claude-code/hooks)
- [Complete guide to building skills for Claude](https://docs.anthropic.com/en/docs/claude-code/skills)