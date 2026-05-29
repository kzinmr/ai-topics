---
title: "Agent Containment"
type: concept
created: 2026-05-27
updated: 2026-05-29
tags:
  - concept
  - agent-safety
  - sandbox
  - isolation
  - security
  - prompt-injection
  - anthropic
  - ai-agents
sources:
  - raw/articles/2026-05-27_anthropic-engineering_how-we-contain-claude.md
---

# Agent Containment

**Agent containment** refers to the practice of limiting an AI agent's blast radius through environmental isolation — sandboxes, virtual machines, containers, and egress controls — rather than relying solely on model-layer behavioral guards. It is a core component of [[concepts/agent-safety]].

## The Containment Thesis

Anthropic's engineering team articulated the containment thesis in May 2026: for autonomous agents, **environmental defenses are the deterministic fallback when probabilistic model defenses fail**. Model-layer defenses (system prompts, classifiers, probes) can reduce prompt injection attack success to ~0.1% on single attempts, but they will never be 100% effective. The containment approach says: if credentials never enter the sandbox, they can't be exfiltrated, regardless of intent or injection.

## Three Containment Patterns

### 1. Ephemeral Container (Server-Side)
Used by [[entities/anthropic|claude.ai]] for code execution. Claude runs in a **gVisor** container on isolated infrastructure. The agent is entirely server-side; no code runs on the user's local machine. The filesystem is per-session ephemeral with no persistent workspace.

- **Blast radius**: Minimal — server-side container guarded by gVisor + host infrastructure boundary
- **Limitation**: No persistent workspace, no access to user's filesystem
- **Security lesson**: The weakest layer is custom-built code. gVisor and seccomp held; the custom proxy broke in Anthropic's most consequential incident

### 2. Human-in-the-Loop Sandbox (Local)
Used by [[entities/claude-code|Claude Code]]. The agent runs on the user's machine with OS-level sandboxing (Seatbelt on macOS, bubblewrap on Linux). Reads are allowed inside the workspace, writes are allowed inside workspace, network is denied by default.

- **Blast radius**: Local workspace, guarded by OS sandbox
- **Key challenge**: [[concepts/approval-fatigue|Approval fatigue]] — users approved ~93% of permission prompts, becoming less diligent
- **Result**: 84% reduction in permission prompts after sandbox deployment
- **User model**: Relies on developer expertise (can read bash, understands `rm -rf`)
- **Open sourced**: The sandbox runtime is [publicly available](https://github.com/anthropics/claude-code-sandbox)

### 3. Full Local VM (Sealed)
Used by [[entities/claude-cowork-aka-ai-assistant|Claude Cowork]]. Runs inside a full virtual machine using the platform's vendor hypervisor (Apple Virtualization on macOS, HCS on Windows). The VM has its own Linux kernel, filesystem, and process table. Only the user-selected workspace and `.claude` folder are mounted.

- **Blast radius**: Mounted workspace, guarded by vsock + hypervisor boundary
- **Six isolation mechanisms**: Two enforced outside the guest kernel (survive root-level access), four guest-enforced
- **Agent loop placement**: Initially inside VM (full isolation), later moved outside for reliability
- **Filesystem controls**: Read-only, read-write, read-write-no-delete mount modes; symlink resolution before path validation

## Key Security Incidents

### Egress Through an Approved Domain
A third-party disclosure: a malicious file in the mounted workspace carried hidden instructions with an attacker's API key. Claude read other files and called `api.anthropic.com`'s Files API using the attacker's key. The egress proxy checked the destination (api.anthropic.com, on the allowlist) and let it through.

**Fix**: Defensive man-in-the-middle proxy inside the VM that intercepts traffic to Anthropic's API and only passes requests with the VM's own provisioned session token.

### Pre-Trust Execution (Claude Code)
Three vulnerabilities reported between mid-2025 and January 2026: a `.claude/settings.json` hook in a cloned repository executed before the user accepted the trust prompt.

**Fix**: Defer parsing and execution of project-local configuration until after the user accepts the trust prompt.

### User-as-Injection-Vector (Claude Code)
A controlled red-team exercise: a researcher phished an employee into running a malicious prompt. Across 25 retries, Claude completed the exfiltration **24 times**. The attacker's instructions arrived through the user — the model-layer classifiers couldn't catch it because the input came from the trusted user channel.

**Fix**: Only the environment layer (egress controls, filesystem boundaries) can defend against this class of attack.

## Looking Ahead

Three emerging risks identified by Anthropic's containment engineering team:
1. **Persistent memory poisoning**: Injection that lands in session-persistent state (product memory, CLAUDE.md, state directories) is reloaded each time the agent starts
2. **Multi-agent trust escalation**: Sub-agent output treated as higher-trust can become a new injection vector
3. **Agent identity**: Cross-platform principal identity standards needed; credentials in host keychain + per-session scoped-down tokens as current best practice

## Related Concepts
- [[concepts/agent-safety]] — Broader framework for AI agent security
- [[concepts/prompt-injection]] — The attack vector containment is designed to mitigate
- [[concepts/sandbox]] — Sandboxing as an isolation primitive
- [[concepts/ai-agents]] — AI agents as a category
- [[entities/anthropic]] — Anthropic's broader product and security work
- [[concepts/approval-fatigue]] — The human-factor failure mode
- [[concepts/human-in-the-loop]] — HITL as an alternative containment strategy
