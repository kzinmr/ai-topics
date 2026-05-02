# Agentic Engineering, Part 4: The Guardrails Layer

**Author:** Paul Hoekstra | **Source:** Paul's Pipeline (Substack)
**URL:** https://paulhoekstra.substack.com/p/agentic-engineering-the-guardrails
**Published:** March 30, 2026

## Summary

Security and quality controls preventing AI agents from becoming liabilities — inspired by the "OpenClaw" scenario where agents with broad permissions and third-party "skills" can lead to massive breaches.

## Key Concepts

### Poisoned Instructions
- Agents treat CLAUDE.md as "ground truth" — attackers can embed malicious instructions
- **Fix:** Treat CLAUDE.md as code, use PR reviews, never push directly to main
- **Critical:** `enableAllProjectMcpServers` to `false` — prevents cloned repos from running arbitrary MCP servers

### Homoglyph Attacks
- Lookalike Unicode characters trick agents (Latin 'i' vs Cyrillic 'і')
- **Tool:** [Tirith](https://github.com/sheeki03/tirith) — local validator catching hostname homoglyphs, ANSI injection, pipe-to-shell

### Hooks as Inspection Points
- `PreToolUse` hook in Claude Code — inspect tool calls before execution

### Sandboxing
- Claude Code uses **bubblewrap** (Linux) or **Apple's Sandbox** (macOS)
- Restricted paths: `~/.ssh`, `~/.aws`, `~/.gnupg`, `~/.docker`
- Hard isolation: Docker with `--network none` or Cloudflare Dynamic Workers

### Permissions System (Two-Tier)
Configuration in `.claude/settings.json`:
- `allow` — whitelisted commands (e.g., `uv run ruff check:*`)
- `deny` — blacklisted commands (e.g., `rm -rf`, `chmod 777`, `curl * | sh`)
- **Auto Mode** — built-in classifier evaluates safe vs risky operations

### AST-grep for Quality
- Catches structural anti-patterns LLMs frequently produce (mutable defaults, logic errors)
- Custom YAML rules for Python, etc.

### The Gates: Pre-commit and CI
**Pre-commit (Local):** Layered defense: whitespace/YAML hooks → Ruff → Bandit → AST-grep
**CI (Shared):** GitHub Actions with concurrency block to cancel stale runs

### Key Insight
> "The goal of guardrails is not to make the agent 'smarter,' but to make it safer to trust. Build these layers once, and shift from 'babysitting the process' to 'judging the output.'"
