---
title: "Agent Credential Leasing (lend)"
created: 2026-11-17
updated: 2026-11-17
type: concept
tags:
  - agent-security
  - agent-safety
  - secrets-exfiltration
  - agent-infrastructure
  - coding-agents
  - agent-tooling
status: L3
confidence: medium
aliases: [lend, credential leasing, remote agent credentials]
sources:
  - raw/articles/2026-11-17_antonio-cx_running-agents-without-credentials.md
  - https://news.ycombinator.com/item?id=50526152
---

# Agent Credential Leasing (lend)

**Agent credential leasing** is a sandboxing-adjacent security pattern in which a coding agent running on a remote, disposable machine is granted *time-limited, approved access* to tools that hold the operator's real credentials, rather than the credentials themselves. The term and reference implementation here is **lend**, built by Antonio (antonio.cx, pico.sh) and posted to Hacker News on 2026-11-17 (116 points).

## The problem it addresses

The author runs multiple [[concepts/coding-agents/coding-agents|coding agents]] (Claude Code, Codex, long-running background agents) in parallel on throwaway VMs via `pico.sh`'s `picd` hosting. The VMs are disposable — but the agents still need to act as *him*: monitor CI with `gh`, call APIs with tokens from 1Password, and SSH into other hosts. The two conventional answers are unsatisfying:

1. **Copy credentials onto the VM** — every secret is now resident on a remote, agent-accessible host; a prompt-injected agent (or a leaked VM) exposes everything.
2. **Run everything locally with a human in the loop** — defeats the point of parallel, remote, always-on agents.

## How lend works

The article describes a tool with the following properties:

- **Socket-forwarded access, not copied secrets.** The agent's tool invocations are forwarded over a socket back to the laptop, where the real credentials live. The agent process never reads the token or key material — "secrets the agent never sees."
- **Stable socket across reconnects.** The forwarding socket is kept stable across SSH reconnects so long-running agents don't break when the connection drops.
- **SSH keys handled out-of-band.** SSH key material stays on the laptop; the agent borrows the capability to authenticate, not the key.
- **Leases.** Access is granted as a time-bounded *lease* that the operator approves, rather than a standing grant.
- **Audit.** The operator can see what the agent did with the borrowed capability ("seeing what happened").
- **Remote approvals.** The author's companion tools `herdr` (agent-aware terminal multiplexer) and `Ovis` (phone/browser client) surface approval prompts and agent questions as push-notification cards, so leases can be approved from a phone.

The article is explicit about what lend does *not* protect against (the "What lend doesn't protect against" section), and situates itself against prior art.

## Position in the design space

Credential leasing is a **capability-based** alternative to credential injection: the agent holds a *request to use* rather than the secret itself. This puts it in the same family as [[concepts/capability-based-security]] and the token/capability direction described in [[concepts/sandbox]] ("capability-based security — an agent can only perform actions for which it possesses an unforgeable capability token"), but with an *operator-in-the-loop approval* and *out-of-band secret custody* element that runtime sandboxing alone does not provide.

It is complementary to runtime isolation: sandboxes constrain what agent code can touch on its own host; leasing governs what the agent can do *as the operator* on external systems. An agent on a fully isolated VM with no network access is also useless for CI monitoring and deployments — leasing is the controlled opening of that egress.

## Open questions

- **Approval fatigue**: leases + per-action approvals compete with the autonomy that makes parallel agents valuable; the article mitigates with phone approvals but does not quantify approval load.
- **Trust in the broker**: lend (and the laptop's agent-broker daemon) becomes a new critical component with full operator privilege; its own compromise restores the original threat model.
- **Single-source maturity**: as of first crawl, lend is one developer's tool with one write-up; confidence is bounded by that single source until independent adoption or a second implementation appears.

## Related

- [[concepts/sandbox]] — runtime isolation vs. credential custody
- [[concepts/capability-based-security]] — theoretical frame
- [[concepts/ai-agent-safety-incidents]] — incidents where resident credentials turned prompt injection into account compromise
- [[concepts/prompt-injection]] — the attack class leasing limits the blast radius of
- [[concepts/agent-selected-hardware]] — companion 2026 thesis on agent-era infrastructure choices

## Sources

- antonio, "Running coding agents without handing them my credentials," antonio.cx, 2026-11-13. `raw/articles/2026-11-17_antonio-cx_running-agents-without-credentials.md`
- Hacker News discussion, 116 points, 2026-11-17: <https://news.ycombinator.com/item?id=50526152>
