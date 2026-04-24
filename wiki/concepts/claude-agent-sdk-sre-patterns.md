---
title: "Claude Agent SDK — SRE Agent Pattern"
tags: [[claude-agent-sdk, mcp, sre, automation, safety-guardrails]]
created: 2026-04-24
updated: 2026-04-24
---

# Claude Agent SDK — SRE Agent Pattern

Anthropic cookbook: [The Site Reliability Agent](https://platform.claude.com/cookbook/claude-agent-sdk-03-the-site-reliability-agent)

## Core Concept

Build an autonomous SRE agent using the **Claude Agent SDK** + **MCP (Model Context Protocol)** that handles the full incident lifecycle: investigation → root cause identification → safe remediation → documentation.

Unlike read-only monitoring agents, this pattern enables **scoped read-write actions** on production infrastructure with multiple safety layers.

## Architecture

```
Claude Agent SDK (query() loop)
    │
    ▼
MCP Server (subprocess via stdio/JSON-RPC)
    │
    ├── Prometheus → query_metrics, list_metrics, get_service_health
    ├── Docker     → run_shell_command, get_container_logs
    ├── Config     → read_config_file, edit_config_file
    └── Diagnostics→ get_logs, get_alerts, get_recent_deployments, execute_runbook
```

### Why Subprocess?

- **Crash isolation**: Agent survives tool crashes/hangs
- **Clean separation**: Reasoning loop vs infrastructure access
- **Protocol**: JSON-RPC over `stdin`/`stdout` — SDK sends request → Server dispatches → Handler returns

## Tool Design Principle

> *"Invest in giving Claude access to the right tools and environment. The MCP server's tool definitions tell Claude what each tool does, what inputs it expects, and when to use it. Given that context and an agentic loop, Claude autonomously forms hypotheses, selects the right tools, interprets results, and adapts its investigation."*

**Tool Descriptions > Prompts**: Clear, detailed JSON Schema descriptions enable autonomous tool selection without hardcoding steps.

## Three-Layer Safety Guardrails

Giving agents write access requires strict scoping. The implementation uses:

### 1. Directory Restrictions
```python
# edit_config_file locked to config/ only
# The MCP server validates the path before execution
```

### 2. Command Allowlists
```python
# run_shell_command only permits docker / docker-compose prefixes
# Validates against known service names for get_container_logs
```

### 3. PreToolUse Hooks
Shell scripts run **before** tool execution. Non-zero exit code blocks the action:

```python
options = ClaudeAgentOptions(
    hooks={
        "PreToolUse": [
            {"matcher": "mcp__sre__edit_config_file",
             "hooks": [{"type": "command", "command": "bash hooks/validate_pool_size.sh"}]},
            {"matcher": "mcp__sre__run_shell_command",
             "hooks": [{"type": "command", "command": "bash hooks/validate_config_before_deploy.sh"}]},
        ]
    },
    permission_mode="acceptEdits"
)
```

Example validation (`validate_pool_size.sh`):
- Blocks `DB_POOL_SIZE` outside safe range (5–100)
- Blocks redeploy if config is unsafe

## Agent Workflow

### Phase 1: Baseline (Healthy System)
Agent queries `get_service_health`, confirms nominal operation. Notes minor outliers but takes no action.

### Phase 2: Investigation (Read-Only)
Prompt: *"We're getting reports of API errors... Investigate thoroughly but do NOT apply fixes yet."*

Agent autonomously:
1. Starts with broad health check → narrows to failing service
2. Crafts PromQL queries based on tool descriptions
3. Correlates error rates, latency, DB metrics, and logs
4. Identifies root cause (e.g., recent deployment misconfigured `DB_POOL_SIZE`)
5. Outputs detailed incident report with impact assessment

### Phase 3: Remediation (Write-Approved)
Prompt: *"Fix the configuration... Redeploy... Verify... Write a post-mortem."*

Agent executes:
1. `edit_config_file` → restores correct value
2. `run_shell_command` → `docker-compose up -d`
3. `get_service_health` → confirms recovery
4. `write_postmortem` → generates structured markdown with timeline, root cause, and action items

## Key Configuration

```python
options = ClaudeAgentOptions(
    system_prompt=SYSTEM_PROMPT,
    mcp_servers={"sre": {"command": sys.executable, "args": [str(MCP_SERVER_PATH)]}},
    allowed_tools=[
        "mcp__sre__query_metrics",
        "mcp__sre__get_service_health",
        "mcp__sre__edit_config_file",
        "mcp__sre__run_shell_command",
        "mcp__sre__write_postmortem",
        # ... other scoped tools
    ],
    hooks={...},
    permission_mode="acceptEdits",
    model="claude-opus-4-6"
)
```

## Production Extensions

### Skills & Runbooks
Encode institutional knowledge as Markdown files triggered by symptom patterns:
```markdown
---
name: runbook
description: Execute documented runbooks for common SRE incidents.
---
## When to Use
Trigger when: db_connections_active > 90 OR P99 latency > 1000ms
## Workflow
1. Identify incident type → 2. Call execute_runbook (phase="investigate")
3. Follow diagnostics → 4. Call execute_runbook (phase="remediate")
```

### Platform Integrations
Tools auto-register when API keys are present (PagerDuty, Datadog, GitHub, etc.). Agent discovers them via `tools/list`.

## Comparison: SDK vs Managed Agents for SRE

| Aspect | Claude Agent SDK | Managed Agents |
|--------|-----------------|----------------|
| **Execution** | Local subprocess + stdio | Anthropic-hosted cloud sandbox |
| **Control** | Full loop control, custom MCP servers | API-driven, managed infrastructure |
| **Safety** | PreToolUse hooks, command allowlists | Custom tools with requires_action gate |
| **MCP** | Self-hosted MCP servers | MCP toolsets + Vault-backed credentials |
| **Audit** | Local transcript (JSONL) | Anthropic Console event log |
| **Best for** | Infrastructure you control directly | Multi-tenant, credential-isolated workflows |

## Key Insights

1. **Agentic Loop Power**: `Observe → Reason → Act → Repeat` enables multi-step reasoning impossible in single LLM calls
2. **Tool Descriptions > Prompts**: Well-structured tool schemas drive autonomous behavior better than elaborate system prompts
3. **Human-in-the-Loop**: Write operations always gated behind approval mechanisms
4. **Context Engineering**: Long investigations benefit from tool clearing and compaction primitives (see )

## Related

- [[managed-agents-sre-incident-response]] — The same pattern on Managed Agents API
- [[chief-of-staff-agent-patterns]] — Hooks, subagents, and plan mode
-  — Managing long-running agent context
