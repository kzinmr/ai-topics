---
title: "Agent Security Patterns"
type: concept
created: 2026-04-25
updated: 2026-11-19
tags:
  - concept
  - agent-security
  - security
  - architecture
  - sandbox
  - harness-engineering
aliases:
  - agent-security-patterns
  - agent containment patterns
sources:
  - https://openai.com/index/equip-responses-api-computer-environment/
  - wiki/concepts/harness-engineering/system-architecture/agent-security-patterns.md
related:
  - "[[concepts/ai-agent-security]]"
  - "[[concepts/prompt-injection]]"
status: active
---

# Agent Security Patterns

Operational control patterns for letting AI agents touch real systems — shells, browsers, networks, credentials — without turning a prompt-injection into a breach. The umbrella threat model is the **lethal trifecta**: an agent that (1) sees untrusted content, (2) holds private data or credentials, and (3) can communicate externally is one injection away from exfiltration. Every pattern below breaks at least one leg of that triangle.

> The harness-level implementation detail (sidecar egress proxy, secret injection, container hardening as built in OpenAI's Responses API computer environment) is covered in [[concepts/harness-engineering/system-architecture/agent-security-patterns]]. This page is the catalog and decision framework.

## Pattern Catalog

### 1. Isolation (break the blast radius)

- **Container / microVM per agent session** — ephemeral filesystem, killed after use; snapshots allow rollback ([[concepts/dev-state-sandbox-snapshots-for-coding-agents]]).
- **Read-only mounts + allowlisted writable paths** (e.g., only `/tmp` and the repo worktree).
- **Ephemeral credentials** — short-lived, scoped tokens injected at runtime so nothing secret lives on disk the agent can read.

### 2. Network containment (break external communication)

- **Sidecar egress proxy** — all outbound traffic transits a proxy that enforces a domain allowlist, inspects for secret patterns, and logs every request. Deny-by-default.
- **No direct internet; tool-mediated fetch** — the agent gets content only through a sandboxed fetch tool that sanitizes and attributes it as untrusted.
- **DNS/IP pinning + TLS interception** for high-assurance settings.

### 3. Credential & secret hygiene (break access to private data)

- **Secret injection at the tool boundary** — secrets are attached by the harness when calling an API, never exposed in prompts, environment, or tool output (secrets exfiltration).
- **Token brokerage / least privilege** — agents act via an identity broker that issues per-task scoped tokens (agent identity, agent identity).
- **Output redaction** — scan tool results and model output for secret formats before they re-enter context.

### 4. Untrusted-content handling (break the injection vector)

- **Content quarantine markers** — retrieved/web/tool text is structurally marked untrusted; the harness filters instruction-like payloads (invisible text, "ignore previous instructions", claudefishing, safeguard evasion).
- **Action confirmation for irreversible effects** — human-in-the-loop gates on send-money/delete/publish class tools; capability-based policies rather than per-button prompts ([[concepts/capability-based-security]]).
- **Plan-then-execute with review** — the plan is auditable before any side effect happens.

### 5. Audit & response (assume breach)

- **Full trajectory logging** — every prompt, tool call, and output recorded for forensics (trace analysis).
- **Kill switches & turn budgets** — hard caps on tool calls, spend, and outbound bytes per session.
- **Canaries** — honey tokens in agent-visible data that alert on egress.

## Decision Heuristic

| Agent capability | Minimum required patterns |
|------------------|---------------------------|
| Read-only code Q&A over repo | Quarantine markers, output redaction |
| Shell in sandbox, no network | Container isolation + turn budgets |
| Networked browsing | + egress proxy allowlist + fetch sanitization |
| Acts with user credentials | + secret injection, token brokerage, HITL on irreversible ops |
| Long-running autonomous | + trajectory audit, canaries, kill switch, monitored budgets |

## Known Residual Risks

- **Confused deputy**: allowlisted endpoints can still be abused (e.g., posting exfil to a permitted GitHub/Gist API) — endpoint allowlists are not content controls.
- **Side channels**: timing, DNS, and resource-consumption leaks survive egress allowlists.
- **Model-layer defeats**: jailbreaks (jailbreak bait) and obfuscation shift the fight to model robustness; patterns above limit *impact*, not *influence*.
- **Supply chain**: tool/MCP servers are themselves attack surface ([[concepts/ai-supply-chain-security]], [[concepts/security-and-governance/agent-skill-supply-chain-attacks]]).

## Related

- [[concepts/ai-agent-security]] — threat model overview
- [[concepts/prompt-injection]] — the primary attack class
- [[concepts/harness-engineering/system-architecture/agent-security-patterns]] — Responses-API container implementation
- [[concepts/autonomous-security-agents]] — agents on the defense side
- [[concepts/brazil-court-prompt-injection-sanction]] — legal accountability precedent

## Sources

- OpenAI, "Equipping the Responses API with a computer environment" — https://openai.com/index/equip-responses-api-computer-environment/
- Simon Willison, "The lethal trifecta" — lethal-trifecta framing widely cited across the security pages above.
