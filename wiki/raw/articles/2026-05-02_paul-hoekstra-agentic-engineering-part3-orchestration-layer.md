# Agentic Engineering, Part 3: The Orchestration Layer

**Author:** Paul Hoekstra | **Source:** Paul's Pipeline (Substack)
**URL:** https://paulhoekstra.substack.com/p/agentic-engineering-the-orchestration
**Published:** March 30, 2026

## Summary

Scaling AI agent performance beyond single agents through orchestration — managing context quality and enabling parallel work.

## Key Concepts

### The Bottleneck: Context Quality
- Context windows fill with "stale reasoning and dead ends"
- **The Ralph Loop:** Agent runs in loop with fresh context each iteration, tracking progress in external files/git
- **Compression via Subagents:** Side quests stay in subagent's context; only results return to main thread

### Subagents vs Agent Teams
**Subagents (Recommended):**
- Fire-and-forget workers with specific job, limited tools, clean context
- Results flow back to parent only (no subagent-to-subagent communication)
- Defined via YAML frontmatter in `.claude/agents/`

**Agent Teams (Experimental):**
- Long-running instances that persist and communicate directly
- Set `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`
- Best for: Complex work requiring ongoing negotiation (frontend↔backend API changes)

### Git Worktrees for Parallel Isolation
- Separate checkouts sharing `.git` directory with unique branches
- `claude --worktree` or `isolation: "worktree"` in subagent definition

### Orchestration Tools
- **JetBrains Air & Conductor** — UIs for Docker/worktree isolation with diff viewers
- **Vibekanban & Cline Kanban** — visual task management with auto-commits
- **Paperclip** — orchestration for zero-human companies with org charts, budget ceilings
- **Claude Managed Agents** — Anthropic's cloud-hosted alternative (sandboxed containers via API)

### Design Strategy: Context over Roles
- Common mistake: splitting by role (Planner→Implementer→Tester) → "telephone game"
- **Sweet spot: read-heavy delegation** — exploration, analysis, summarization, tests
- Keep write-heavy work sequential — parallel writing creates incompatible assumptions
- Agent implementing a feature should usually write its tests (avoids handoff friction)
