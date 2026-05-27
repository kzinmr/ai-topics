# TrustFall: Coding Agent Security Flaw Enables One-Click RCE in Claude, Cursor, Gemini CLI and GitHub Copilot

**Source:** https://adversa.ai/blog/trustfall-coding-agent-security-flaw-rce-claude-cursor-gemini-cli-copilot/
**Researcher:** Rony Utevsky (Adversa AI)
**Date:** May 8, 2026
**Saved:** 2026-05-27

## Key Findings

- Claude Code's trust dialog removed MCP warnings in v2.1+; the new dialog is generic ("Quick safety check: Is this a project you created or one you trust?") and does not mention MCP execution at all.
- A malicious repository can ship two JSON files that auto-approve an attacker-controlled MCP server. Pressing Enter on the trust prompt spawns the server as an unsandboxed OS process with full user privileges (no tool call required).
- The payload can be inline inside `.mcp.json` (no script file on disk).
- The MCP server can read secrets, source code from other projects, and open a long-lived C2 channel. Other dangerous settings (like `bypassPermissions`) are already blocked from project scope or gated by a red warning dialog — the MCP-enabling settings are not.
- CI/CD variant: On headless runners (e.g., `anthropics/claude-code-action`), the trust dialog is entirely bypassed. The attack runs with zero human interaction against pull-request branches.
- All four agentic CLIs (Claude Code, Gemini CLI, Cursor CLI, Copilot CLI) auto-execute project-defined MCP servers on trust dialog acceptance, and all default to "Yes/Trust".

## Three Independent Paths to Silent Execution

1. `enableAllProjectMcpServers` in `.claude/settings.json` — On trust dialog acceptance, server starts immediately, no per-server consent, no tool call needed.
2. `enabledMcpjsonServers` in `.claude/settings.json` — Same as above, but targets a named subset.
3. `permissions.allow` in `.claude/settings.json` — Gated on Claude's tool invocation, but no consent prompt.

All three bypass the dialog that would be shown for `bypassPermissions`.

## CLI Trust Dialog Comparison

| CLI | Dialog mentions MCP? | Per-server enumeration? | Default option |
|-----|----------------------|-------------------------|----------------|
| Claude Code | No — generic "trust this folder" | No | Yes, I trust |
| Gemini CLI | Yes — warns about project MCP servers | Yes (lists names) | Trust |
| Cursor CLI | Yes — MCP-specific warning | No | Trust |
| Copilot CLI | No — generic "trust this folder" | No | Yes |

## Root Cause: Scope-Restriction Inconsistency

Anthropic blocks several dangerous settings from project scope (autoMode, skipDangerousModePermissionPrompt, etc.) but does NOT block MCP-enabling settings (enableAllProjectMcpServers, enabledMcpjsonServers).

## CI/CD Zero-Click Variant

On headless CI runners using `anthropics/claude-code-action`, there is no terminal session for the trust dialog to render in, so the dialog is bypassed entirely. The official action automatically enables project MCP servers.

## Vendor Response

Anthropic reviewed and declined TrustFall as outside its threat model — accepting the folder trust prompt represents consent to the full project configuration, including MCP execution.
