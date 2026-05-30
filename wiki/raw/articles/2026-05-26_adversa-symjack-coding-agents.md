# Adversa AI: SymJack — Symlink Hijack RCE in AI Coding Agents

**Source:** https://adversa.ai/blog/the-approval-prompt-is-lying-to-you-symlink-rce-in-five-ai-coding-agents-claude-code-cursor-antigravity-copilot-grok-build/
**Date:** May 26, 2026
**Author:** Rony Utevsky (Adversa AI)

## Overview

SymJack is an attack technique targeting AI coding agents that uses a booby-trapped repository to trick the coding assistant into overwriting its own configuration through a disguised file copy, then running attacker code on the next restart.

## Attack Chain

1. Attacker controls a code repository with malicious project instructions file (CLAUDE.md, AGENTS.md, GEMINI.md, etc.)
2. Malicious symlink is renamed to appear innocuous
3. Agent executes a `cp` command that looks benign (e.g., copy video file to docs)
4. The copy secretly overwrites agent's own configuration
5. On next restart, the planted MCP server spawns and attacker code runs as the user, unsandboxed

## Affected Products

| Product | Version Tested | Status |
|---------|---------------|--------|
| Claude Code | v2.1.128 (Opus 4.7) | Rejected as out of scope; quietly hardened in v2.1.129 |
| Gemini CLI | v0.43.0 | Declined — "single-user self-attack" |
| Antigravity CLI | v1.0.2 | Declined — same as Gemini |
| Cursor Agent CLI | v2026.05.20 | Declined as duplicate of existing symlink report |
| Copilot CLI | v1.0.51 | Awaiting response |
| Grok Build CLI | v0.1.216 | Awaiting response |
| Codex CLI | v0.133.0 | Declined — "theoretical, user approves cp" |

## Vendor Responses

- **Anthropic:** Rejected as out of scope (symlink carve-out in bug bounty program), but quietly hardened Claude Code to resolve symlinks before asking for approval and shows real destination path
- **Google:** Declined — classed as single-user self-attack. Explicit approval treated as intended behavior
- **Cursor:** Declined as duplicate of existing symlink report
- **OpenAI:** Declined — called it theoretical, citing user approval of cp command as proof no security boundary was crossed
- **xAI/GitHub:** No response yet

## Comparison to TrustFall

SymJack extends TrustFall (Adversa AI, May 8, 2026). TrustFall relied on a populated config visible at clone time. SymJack writes settings AFTER the trust prompt using a disguised file copy — fewer prerequisites, same root cause.

## CI/CD Risk

On CI runners that auto-trust their workspace, the same chain runs with zero clicks. One malicious pull request can drain every secret the runner holds before any human reviews the change.

## Key Quote

> "The approval is informed only if the prompt tells the user what the copy actually does, and it does not."
