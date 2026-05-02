# Agentic Engineering, Part 1: The Configuration Layer

**Author:** Paul Hoekstra | **Source:** Paul's Pipeline (Substack)
**URL:** https://paulhoekstra.substack.com/p/agentic-engineering-the-configuration
**Published:** March 30, 2026

## Summary

Core philosophy of Agentic Engineering: the difference between mediocre and elite results using coding agents (Claude Code, Codex) lies in the **Configuration Layer** — structured project-level instructions that prevent agents from defaulting to "sycophantic" behavior and low-quality code.

## Key Concepts

### CLAUDE.md as Behavioral Baseline
- Acts as `.editorconfig` for agent behavior
- Read automatically at start of every session
- Stateless: sent with every tool call/retry
- Prompt caching reduces cost of stable prefix to ~10%
- **Keep it short** — every token competes for attention (context rot)

### Recommended Configuration
- Hard Limits: functions <= 100 lines, cyclomatic complexity <= 8
- Python Tooling: uv, ruff
- Behavioral Rules: NEVER create files unnecessarily, ALWAYS read before editing

### Skills (`.claude/skills/`)
- Task-specific Markdown files loaded on demand
- Claude Haiku + human-curated skills (27.7%) > Opus without skills (22.0%) per SkillsBench
- Human-curated > AI-generated instructions
- **Enforcement:** `<HARD-GATE>` XML tags, Anti-Rationalization Tables

### Workflow Frameworks
- [superpowers](https://github.com/obra/superpowers) — TDD/debugging/verification plugin
- [Get Shit Done](https://github.com/gsd-build/get-shit-done) — slash commands + meta-prompting
- [Compound Engineering](https://github.com/EveryInc/compound-engineering-plugin) — Plan → Work → Review → Compound

### Division of Labor
- CLAUDE.md: Always-relevant project rules
- Skills: Task-specific procedures
- Live Prompt: Current task details

### Prompt Caching Note
Cache expires after 5 minutes of inactivity — long pauses trigger full-price context rewrite.
