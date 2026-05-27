# 'SymJack' Attack Turns AI Coding Agents Into Supply Chain Attack Delivery Systems

**Source:** https://www.securityweek.com/symjack-attack-turns-ai-coding-agents-into-supply-chain-attack-delivery-systems/
**Author:** Kevin Townsend, Senior Contributor at SecurityWeek
**Date:** May 26, 2026
**Saved:** 2026-05-27

## Overview

SecurityWeek reports on "SymJack," a new attack technique discovered by Adversa AI that hijacks AI coding agents to inject malicious code into software supply chains. The attack exploits the inherent trust and automation in AI-assisted development workflows.

"Trust and automation are key to many attacks; and trust with automation is inherent in the use of AI coding agents."

## Key Elements
- Attacker control over a coding agent's repository and its project instruction file.
- Malicious MCP server ready to execute arbitrary commands.
- Developer use of an AI coding tool that follows the poisoned instructions.

## How SymJack Works

1. Malicious Symlink: A symbolic link is created and renamed to appear harmless (e.g., something that looks like a documentation file).
2. Seemingly Innocent `cp` Command: The AI agent suggests copying the file to a documentation folder. The developer approves — nothing visibly mentions config directories or executable content.
3. Payload Injection: The `cp` command actually writes the attacker's payload into the agent's own configuration, registering a malicious MCP server.
4. Execution: On the next restart, the malicious server spawns, executing arbitrary code unsandboxed, with the user's privileges.

## Supply Chain & CI/CD Impact

If the malicious code reaches the CI pipeline:
- Secrets exfiltration: CI runners already hold tokens, keys, and credentials.
- No human review needed: A single malicious pull request can exfiltrate all secrets before anyone inspects it.

## Affected AI Coding Agents

Claude Code, Gemini CLI / Antigravity CLI, Cursor Agent CLI, Grok Build CLI, GitHub Copilot CLI — all confirmed vulnerable.

## Vendor Responses

- xAI and GitHub: No response at time of writing.
- Google (Gemini): Rejected the report; considers explicit user approval as intended behavior.
- Cursor: Declined, stating they already knew about the issue.
- Anthropic (Claude Code): Initially rejected as out of scope, but quietly hardened Claude Code weeks later. Hardening: resolves symlinks before asking for approval, showing the real destination path in the prompt.

## Why It's Dangerous

- The attack is not a bug — agents simply follow instructions.
- Developers trust the agent and only see a benign file copy; human nature + speed pressure encourages approval.
- The core problem is too much trust combined with too much automation.
