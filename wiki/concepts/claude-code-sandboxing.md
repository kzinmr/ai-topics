---
title: "Claude Code Sandboxing"
type: concept
created: 2026-05-08
updated: 2026-05-26
tags:
  - claude-code
  - sandbox
  - agent-safety
  - security
aliases:
  - Claude Code sandbox
  - Claude sandboxed bash
status: active
sources:
  - raw/articles/2026-05-08_anthropic-engineering_claude-code-sandboxing.md
  - https://www.anthropic.com/engineering/claude-code-sandboxing
related:
  - claude-code
  - agent-sandboxing
  - claude-code-auto-mode
  - code-execution-with-mcp
---

# Claude Code Sandboxing

Claude Code's sandboxing feature. It uses OS-level isolation (Linux bubblewrap / macOS seatbelt) to restrict both filesystem and network access, improving security while reducing approval prompts by 84%.

## Core Design

### Two Isolation Boundaries

| Boundary | Function | Protection |
|------|------|---------|
| **Filesystem isolation** | Only specified directories readable/writable | Prevents tampering with sensitive system files |
| **Network isolation** | Only approved servers connectable | Prevents data leakage and malware downloads |

**Key principle**: Both must be present to be effective. Network isolation alone cannot prevent file exfiltration, and filesystem isolation alone cannot prevent sandbox escape.

## Two Delivery Forms

### 1. Sandboxed Bash Tool (Beta, Research Preview)

- Restricts directories and network hosts without container overhead
- Uses OS primitives: Linux bubblewrap + macOS seatbelt
- **Open-sourced** ([GitHub](https://github.com/anthropics/claude-code))
- Can sandbox arbitrary processes, agents, and MCP servers
- Custom proxy enables arbitrary rules for outbound traffic

**Architecture**:
```
[Claude Code] → [Sandboxed Bash]
                    ├── FS isolation: cwd only rw, external blocked
                    └── Network isolation: Unix domain socket → Proxy → approved domains only
```

### 2. Claude Code on the Web

- Run Claude Code sessions in **cloud-based isolated sandboxes**
- Sensitive credentials (git auth, signing keys) are **never stored** inside the sandbox
- Custom Git proxy handles authentication transparently:
  - Sandboxed git client → proxy authentication with scoped credentials
  - Proxy validates branch/repo → issues actual auth token → forwards to GitHub

## Security Model

- Restrictions apply to **all** scripts, programs, and subprocesses launched within the sandbox
- Even if prompt injection succeeds, the agent remains fully isolated — SSH key theft or communication with attacker servers is impossible
- Access attempts outside sandbox scope → immediate notification + user decision

## Impact

- **84% reduction in approval prompts** (Anthropic internal usage data)
- Eliminates "approval fatigue" from manual approvals
- Accelerates development cycles

## Permission Mode Comparison

| Feature | Sandbox | Auto Mode | Manual |
|------|---------|-----------|--------|
| Security | Highest (OS isolation) | High (classifier) | Medium (human judgment) |
| Autonomy | High | High | Low |
| Maintenance | High (requires setup) | Low | Low |
| External Access | Restricted | Classifier-dependent | Manual approval |

## See Also

- [[entities/claude-code]] — Claude Code agent harness
- [[claude-code-auto-mode]] — Auto mode permission classifier
- [[concepts/agent-sandboxing]] — General agent sandboxing patterns
- [[concepts/claude-code-best-practices]] — Claude Code best practices
- [[concepts/code-execution-with-mcp]] — Code execution with MCP
