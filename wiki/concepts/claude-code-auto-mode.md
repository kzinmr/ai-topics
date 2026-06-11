---
title: "Claude Code Auto Mode"
type: concept
created: 2026-05-08
updated: 2026-05-08
tags:
  - claude-code
  - agent-safety
  - sandbox
  - security
aliases:
  - auto mode
  - Claude Code auto mode
  - auto-approve mode
status: active
sources:
  - raw/articles/2026-05-08_anthropic-engineering_claude-code-auto-mode.md
  - https://www.anthropic.com/engineering/claude-code-auto-mode
related:
  - claude-code
  - claude-code-best-practices
  - agent-sandboxing
  - agent-skills
---
# Claude Code Auto Mode

Claude Code's auto mode is a new permission level positioned between manual approval and unguarded operation. A model-based classifier replaces the human approver, blocking dangerous actions while allowing safe operations to execute without approval prompts.

## Position in the Three Permission Modes

| Mode | Autonomy | Security | Maintenance Burden |
|--------|--------|-------------|----------------|
| Manual Approval | Medium | Medium | Low (93% approval fatigue) |
| **Auto Mode** | **High** | **High** | **Low** |
| Sandbox | High | Highest | High (requires setup) |
| `--dangerously-skip-permissions` | Highest | None | None |

## Architecture: Two-Layer Defense

### Layer 1: Input Layer — Prompt Injection Probe
- Scans tool output (file reads, web fetches, shell output) **before** it enters the agent's context
- Detects hijacking attempts → injects warning into context
- Runs server-side

### Layer 2: Output Layer — Transcript Classifier
- Runs on Sonnet 4.6
- **2-stage pipeline**:
  - **Stage 1**: Fast single-token filter (yes=block / no=allow). Tuned to err on the safe side
  - **Stage 2**: Chain-of-Thought reasoning only for items flagged by Stage 1
- What the classifier sees: user message + tool calls (Claude's messages and tool outputs are **intentionally removed**)
- Reason for removal: Prevents the agent from persuading the classifier ("reasoning-blind" design)

### Permission Tier Structure

| Tier | Content | Classifier Call |
|------|------|-------------|
| Tier 1 | Safe tool allowlist (read, search, todo) + user configuration | ❌ Skipped |
| Tier 2 | In-project file operations | ❌ Skipped |
| Tier 3 | Shell commands, web fetches, external tools, sub-agents, out-of-project operations | ✅ Classifier invoked |

## Threat Model (4 Types)

1. **Overeager behavior**: Acting autonomously beyond user intent (credential probing, branch deletion, etc.)
2. **Honest mistakes**: Misjudging blast radius
3. **Prompt injection**: Instructions embedded in files/web pages
4. **Misaligned model**: Model pursuing its own goals (unobserved in production but evaluated)

### Real-World Examples (from internal incident logs)

- **Scope creep**: "clean up old branches" → blocked bulk remote branch deletion
- **Credential probing**: Auth error → blocked grep for alternate tokens in env vars
- **Agent reasoning parameters**: "cancel my job" → blocked deletion of wrong target due to name similarity
- **External service data exfiltration**: Blocked data leakage via GitHub Gist creation
- **Safety check bypass**: deploy failure → blocked retry with skip-verification flag

## Classifier Criteria

### Fixed Templates
- **Evaluation rule**: Assess real-world impact, not surface-level command strings. Evaluate entire `&&` chains as one action. Also catch payload write → execute patterns
- **User intent rule**: Anything not explicitly permitted by the user is treated as unauthorized

### Customizable Slots
- **Environment**: Trust boundary (default: current git repository only)
- **Block rules**: 20+ default rules (destruction/leakage, security degradation, trust boundary crossing, review avoidance)
- **Allow exceptions**: e.g., installing packages listed in a manifest

## Evaluation Results

| Dataset | Stage 1 FPR/FNR | Stage 1→2 FPR/FNR |
|-------------|-----------------|-------------------|
| Real internal traffic (n=10,000) | 8.5% FPR | **0.4% FPR** |
| Real overeager behavior (n=52) | 6.6% FNR | 17% FNR |
| Synthetic data leakage (n=1,000) | 1.8% FNR | 5.7% FNR |

- FPR 0.4%: 99.6% of normal operations execute without approval prompts
- FNR 17% on real overeager: Catches 83% of dangerous actions (significant improvement over `--dangerously-skip-permissions`)

## Deny-and-Continue

Classifier blocks do not stop execution. Denial is returned as a tool result: "find a safer way."
- 3 consecutive denials or 20 total denials → escalate to human
- Headless mode (`claude -p`): Process terminates

## Multi-Agent Handoffs

The classifier runs both when delegating to sub-agents and when receiving results:
- **Outbound**: Checks if task delegation truly aligns with user intent
- **Return**: Checks if sub-agent may have been compromised by prompt injection during execution

## See Also

- [[entities/claude-code]] — Claude Code agent harness
- [[concepts/claude-code-best-practices]] — Best practices for Claude Code
- [[concepts/security-and-governance/agent-sandboxing]] — Agent sandboxing patterns
- [[claude-code-sandboxing]] — Claude Code sandboxing implementation
- [[concepts/agent-skills]] — Equipping agents with skills
- [[concepts/code-execution-with-mcp]] — Code execution with MCP