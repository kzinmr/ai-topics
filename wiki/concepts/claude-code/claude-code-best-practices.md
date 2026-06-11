---
title: "Claude Code Best Practices"
type: concept
created: 2026-06-02
updated: 2026-06-02
tags:
  - claude-code
  - coding-agents
  - agentic-engineering
  - ai-agent-engineering
  - context-engineering
  - developer-tooling
  - ci-cd
  - agent-safety
  - harness-engineering
sources:
  - raw/articles/2026-05-08_anthropic-engineering_claude-code-best-practices.md
  - https://www.anthropic.com/engineering/claude-code-best-practices
related:
  - claude-code
  - claude-code-auto-mode
  - claude-code-sandboxing
  - context-engineering
  - agent-skills
status: active
---

# Claude Code Best Practices

Practical patterns for effective [[entities/claude-code|Claude Code]] usage, compiled from Anthropic's internal teams and engineers across diverse codebases. The overarching constraint driving most best practices: **the context window fills up fast, and performance degrades as it fills**. See [[concepts/context-engineering|Context Engineering]] for the theoretical foundations of context management.

## CLAUDE.md Configuration

CLAUDE.md is a special file Claude reads at the start of every conversation. Run `/init` to generate a starter file, then refine over time.

### Placement Hierarchy

| Location | Scope | Shared? |
|----------|-------|---------|
| `~/.claude/CLAUDE.md` | All sessions globally | No |
| `./CLAUDE.md` (project root) | Project-wide | Yes (git) |
| `./CLAUDE.local.md` | Project-wide personal | No (`.gitignore`) |
| Child directories | On-demand per subdirectory | Yes (git) |

### What to Include vs Exclude

**Include**: Bash commands Claude cannot guess, non-default code style rules, testing instructions, repo etiquette, architecture decisions, environment quirks, common gotchas.

**Exclude**: Anything inferable from code, standard language conventions, detailed API docs (link instead), frequently changing info, long tutorials, self-evident practices.

> **Key rule**: For each line, ask "Would removing this cause Claude to make mistakes?" If not, cut it. Bloated CLAUDE.md files cause Claude to ignore actual instructions. Treat it like code — prune regularly, test changes by observing behavioral shifts.

CLAUDE.md supports file imports via `@path/to/file` syntax and can reference parent/child CLAUDE.md files in monorepo setups. Add emphasis (e.g., "IMPORTANT", "YOU MUST") to improve adherence on critical rules.

## Common Workflows

### Explore → Plan → Implement → Commit

The recommended four-phase workflow separates research from execution:

1. **Explore** (plan mode): Claude reads files and answers questions without making changes
2. **Plan** (plan mode): Claude creates a detailed implementation plan; press `Ctrl+G` to edit the plan directly
3. **Implement** (default mode): Claude codes against the plan, runs tests, fixes failures
4. **Commit** (default mode): Descriptive commit message and PR creation

> **When to skip planning**: If you could describe the diff in one sentence (typo fix, log line, rename), ask Claude directly. Planning is most valuable when the approach is uncertain or changes span multiple files.

### Bug Fixing

Provide the symptom, likely location, and what "fixed" looks like. Example: "Users report login fails after session timeout. Check src/auth/, especially token refresh. Write a failing test that reproduces the issue, then fix it."

### Codebase Exploration

Ask Claude the same questions you'd ask a senior engineer: "How does logging work?", "What edge cases does this flow handle?", "Why does this call `foo()` instead of `bar()`?" This is an effective onboarding workflow requiring no special prompting.

### Spec-Driven Development

For larger features, have Claude interview you first using `AskUserQuestion`. Claude asks about implementation details, UI/UX, edge cases, and tradeoffs you might not have considered. Once the spec is complete (written to `SPEC.md`), start a fresh session to execute it with clean context.

## Multi-Claude Patterns

### Git Worktrees for Parallel Agents

Run 3–5 Claude sessions simultaneously using git worktrees so edits don't collide. Example: one agent reads logs in an analysis worktree, multiple agents implement features in parallel feature worktrees, human acts as coordinator.

### Writer/Reviewer Pattern

Use two sessions for quality: one implements, the other reviews with fresh context (unbiased by code it just wrote). Session A writes the rate limiter; Session B reviews for edge cases and race conditions.

### Non-Interactive Mode (`claude -p`)

Run Claude programmatically in CI, hooks, or scripts:

```bash
# One-off queries
claude -p "Explain what this project does"

# Structured output for scripts
claude -p "List all API endpoints" --output-format json

# Streaming for real-time processing
claude -p "Analyze this log file" --output-format stream-json
```

### Fan-Out Across Files

For large migrations, generate a task list, write a loop calling `claude -p` per file with `--allowedTools` to scope permissions. Test on 2–3 files first, refine the prompt, then run at scale.

## GitHub Actions / CI Integration

Claude Code integrates into CI pipelines via non-interactive mode. Use `claude -p` in GitHub Actions workflows for automated code review, migration validation, and test generation. Combine with `--output-format json` for programmatic result parsing.

## Security and Permissions

Three approaches to reduce approval fatigue while maintaining safety:

- **[[concepts/claude-code/claude-code-auto-mode|Auto mode]]**: Classifier model reviews commands, blocks risky actions (0.4% false positive rate), lets routine work proceed unattended
- **Permission allowlists**: Permit specific known-safe commands (e.g., `npm run lint`, `git commit`) via `/permissions`
- **[[concepts/claude-code/claude-code-sandboxing|Sandboxing]]**: OS-level isolation (Linux bubblewrap / macOS seatbelt) restricting filesystem and network access

See [[concepts/claude-code/claude-code-auto-mode]] for the two-layer defense architecture and [[concepts/claude-code/claude-code-sandboxing]] for sandbox implementation details.

## Context Management Techniques

- **`/clear` between unrelated tasks**: Resets context entirely; long sessions with irrelevant context reduce performance
- **Auto-compaction**: Triggered at ~95% context usage; customize preservation rules in CLAUDE.md (e.g., "always preserve modified file list and test commands")
- **`/compact <instructions>`**: Manual compaction with focus guidance (e.g., `/compact Focus on the API changes`)
- **Subagents for investigation**: Delegate research to subagents running in separate context windows; they report summaries without cluttering the main conversation
- **`/btw` for quick questions**: Answers appear in a dismissible overlay, never entering conversation history
- **Checkpoints**: Every action creates a checkpoint; double-tap `Esc` or `/rewind` to restore conversation, code, or both

For deeper context engineering theory, see [[concepts/context-engineering|Context Engineering]].

## Environment Configuration

- **CLI tools**: Install `gh` (GitHub), `aws`, `gcloud`, and other CLIs — they are the most context-efficient way to interact with external services
- **[[concepts/agent-skills|Skills]]**: Create `SKILL.md` files in `.claude/skills/` for domain knowledge and reusable workflows; loaded on demand without bloating every conversation
- **Hooks**: Deterministic scripts that run at specific workflow points (unlike CLAUDE.md which is advisory); e.g., run eslint after every file edit
- **MCP servers**: Connect external tools (Notion, Figma, databases) via `claude mcp add`
- **Subagents**: Define specialized assistants in `.claude/agents/` with isolated context and restricted tools

## Common Failure Patterns

| Pattern | Fix |
|---------|-----|
| Kitchen sink session (unrelated tasks mixed) | `/clear` between tasks |
| Repeated correction loops (context polluted with failures) | After 2 failed corrections, `/clear` and write a better prompt |
| Over-specified CLAUDE.md (rules get lost in noise) | Ruthlessly prune; convert recurring rules to hooks |
| Trust-then-verify gap (plausible but broken output) | Always provide verification: tests, screenshots, scripts |
| Infinite exploration (unscoped investigation fills context) | Scope narrowly or use subagents |

## See Also

- [[entities/claude-code]] — Claude Code entity page (metrics, architecture, history)
- [[concepts/claude-code/claude-code-auto-mode]] — Auto mode permission classifier
- [[concepts/claude-code/claude-code-sandboxing]] — OS-level sandboxing implementation
- [[concepts/context-engineering|Context Engineering]] — Context management theory and frameworks
- [[concepts/agent-skills]] — Skills standard and progressive disclosure
- [[concepts/harness-engineering]] — Harness engineering discipline
