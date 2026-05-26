---
title: "Claude Code Best Practices"
type: concept
aliases:
  - claude-code-best-practices
  - claude-code-tips
created: 2026-04-25
updated: 2026-04-29
tags:
  - concept
  - anthropic
status: complete
sources:
  - url: "https://code.claude.com/docs/en/best-practices"
    title: "Official Claude Code Best Practices (Anthropic)"
  - url: "https://aiorg.dev/blog/claude-code-best-practices"
    title: "Claude Code Best Practices: 15 Tips from 6 Projects (aiorg.dev, 2026)"
  - url: "https://smartscope.blog/en/generative-ai/claude/claude-code-best-practices-advanced-2026"
    title: "Claude Code Advanced Best Practices 2026 (SmartScope)"
  - url: "https://ranthebuilder.cloud/blog/claude-code-best-practices-lessons-from-real-projects"
    title: "Claude Code Best Practices: Lessons from Real Projects (Ran Isenberg, 2026)"
---
# Claude Code Best Practices

**Claude Code Best Practices** is a collection of design patterns and operational knowledge for maximizing Anthropic's AI coding agent, Claude Code. It is organized into three categories: **CLAUDE.md setup**, **prompting patterns**, and **workflow habits**.

## Three Basic Categories

### 1. Project Setup

#### CLAUDE.md (Most Important)
A project's "memory card." A single setup saves 20–30% tokens per session:
```
# Project overview and target audience
# Tech stack and framework versions
# Key build, test, and deploy commands
# Project structure
# Coding conventions
# Important rules (no committing secrets, accessibility requirements, etc.)
```
**Important**: Keep under 200 lines. Bloating is counterproductive.

#### CLAUDE.md Hierarchy (3 Levels)
The Claude Certified Architect exam frequently tests the 3-level hierarchy of CLAUDE.md (Domain 3, 20%):

| Level | Location | Characteristics |
|--------|------|------|
| User level | `~/.claude/CLAUDE.md` | Not version-controlled, not shared |
| Project level | `.claude/CLAUDE.md` | Version-controlled, team-shared |
| Directory level | Files in subdirectories | Directory-bound |

**Exam trap**: Team members miss instructions → because they are in user-level settings (not version-controlled, not shared).

#### Path-Specific Rules (`.claude/rules/`)
Apply conventions to the **entire codebase** via YAML frontmatter glob patterns (e.g., `**/*.test.tsx`). Directory-level CLAUDE.md cannot do this (directory-bound). Key concept tested in exams.

#### .claudeignore
Like `.gitignore`, specifies files Claude Code should skip:
```
node_modules/
.next/
dist/
*.lock
*.log
coverage/
.env*
```
Can reduce token consumption by 50–70%.

#### Rules (`.claude/rules/*.md`)
Modular, topic-specific configuration:
- Test guidelines
- Data visualization conventions
- API design rules

### 2. Prompting Patterns

| Pattern | Description | When to Use |
|---------|------|--------------|
| **Plan Mode** | Review plan before execution | Changes affecting 3+ files |
| **Feedback Loops** | 2–3x quality improvement | Code review, refactoring |
| **Pattern Reference** | Reference existing patterns | Creating new API routes, etc. |
| **One Task Per Session** | 1 session = 1 task | Complex multi-step work |

### 3. Workflow Habits

- **/compact**: Context compression (200K window management)
- **Hooks**: Deterministic quality gates (always executed)
- **Slash Commands**: Custom commands (git, test, PR)
- **Git Worktrees**: Run 5 Claude agents in parallel
- **Subagents**: Delegate specialized tasks (security review, etc.)

## Advanced Techniques

| Technique | Description |
|-----------|------|
| **Hooks are mandatory, CLAUDE.md is advisory** | Hooks execute deterministically; CLAUDE.md is reference info |
| **Subagents have separate context** | Sub-agents operate in independent context windows |
| **Skills auto-fire** | `SKILL.md` in `.claude/skills/` auto-applies based on context |
| **Approval fatigue mitigation** | Streamline frequent approvals with Allowlist + Sandbox |
| **2 failures = /clear** | Reset session after 2 consecutive failures |
| **1 session = 1 task** | Focused context for best performance |

## Common Pitfalls

| Pitfall | Countermeasure |
|---------|------|
| CLAUDE.md too long | Keep under 200 lines, externalize with links |
| Multiple tasks in one session | Use /compact or new session per task |
| Requesting approval every time | Configure Allowlist + Sandbox |
| Not using Hooks | Set up deterministic quality gates |
| Executing without planning | Verify upfront with Plan Mode |

## Related Concepts

- [[concepts/claude-perfect-memory]] — Claude Code's persistent memory design
- [[concepts/agent-loop-orchestration]] — Agent loop patterns
- [[concepts/monty-sandbox]] — Code execution sandbox
- [[concepts/claude-certified-architect-domains]] — Claude Certified Architect's 5 domain knowledge (agentic loop, hooks, hub-and-spoke, context management)

## Sources

- [Official Claude Code Best Practices (Anthropic)](https://code.claude.com/docs/en/best-practices)
- [Claude Code Best Practices: 15 Tips from 6 Projects](https://aiorg.dev/blog/claude-code-best-practices)
- [Claude Code Advanced Best Practices 2026](https://smartscope.blog/en/generative-ai/claude/claude-code-best-practices-advanced-2026)
- [Lessons from Real Projects (Ran Isenberg, 2026)](https://ranthebuilder.cloud/blog/claude-code-best-practices-lessons-from-real-projects)