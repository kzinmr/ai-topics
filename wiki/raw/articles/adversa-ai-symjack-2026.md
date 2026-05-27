# SymJack: The Approval Prompt Is Lying — A Critical Coding Agent Security Flaw

**Source:** https://adversa.ai/blog/the-approval-prompt-is-lying-to-you-symlink-rce-in-five-ai-coding-agents-claude-code-cursor-antigravity-copilot-grok-build/
**Researcher:** Rony Utevsky (Adversa AI)
**Date:** May 26, 2026
**Saved:** 2026-05-27

## TL;DR

- SymJack achieves remote code execution via AI coding assistants with a single malicious repository.
- The agent is tricked into a benign-looking file copy that secretly overwrites its own config.
- The next restart runs attacker code with full user privileges.
- Confirmed against: Claude Code (2.1.128, partial patch in 2.1.129), Gemini CLI (0.43.0) / Antigravity CLI (1.0.2), Cursor CLI (v2026.05.20), Copilot CLI (1.0.51), Grok Build CLI (0.1.216).
- The flaw is architectural, not product-specific.

## Attack Chain

1. Instruction file ingestion: Every major coding assistant reads a project instructions file (CLAUDE.md, AGENTS.md, GEMINI.md, copilot-instructions.md). The attacker controls this file.
2. Disguised write: The instructions tell the agent to use a raw shell `cp` command, bypassing the native write tools' guardrails.
3. Symlink trickery: The "destination" is a symbolic link committed into the repo, pointing to the agent's configuration file.
4. Payload execution: The payload registers a malicious MCP server. On next restart, attacker code runs as the user (unsandboxed).

## One Flaw, Five Products

All five share the same failing design assumptions:
- Auto-ingest a project instruction file as trusted input.
- Expose raw shell escape hatches that sidestep native write guardrails.
- Render the per-action approval against the literal command string, not the resolved effect.
- Load and run MCP servers from config on startup.

## Product-by-Product Vulnerability Table

| Product | Version tested | Instruction file | Config target | Symlink warning behavior |
|---------|---------------|------------------|---------------|-------------------------|
| Claude Code | v2.1.114 (Opus 4.7) | CLAUDE.md | .claude/settings.json, .mcp.json | None at test time; fixed build now shows resolved path |
| Gemini CLI | v0.43.0 | GEMINI.md | .gemini/settings.json | None; silent path resolution |
| Cursor Agent CLI | v2026.05.20 | .cursor/rules | global ~/.cursor/mcp.json | None at all |
| GitHub Copilot CLI | v1.0.51 | .github/copilot-instructions.md | .mcp.json | Warns on out-of-project links but shows link name, not resolved target |
| Grok Build CLI | v0.1.216 | AGENTS.md | .mcp.json | None; silent path resolution |

## Vendor Response

| Vendor | Product | Status |
|--------|---------|--------|
| Anthropic | Claude Code | Report rejected as out of scope. However, a few weeks later the approval flow was quietly hardened, now shows the resolved path after a symlink. |
| Google | Gemini CLI and Antigravity CLI | Declined. Classed as single-user self-attack. Explicit approval treated as intended behavior. |
| Cursor | Cursor Agent CLI | Declined as a duplicate of an existing symlink report. |
| xAI | Grok Build CLI | Awaiting response. |
| GitHub | Copilot CLI | Awaiting response. |
