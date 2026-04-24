---
title: "Managed Agents — SRE Incident Response Pattern"
tags: [[managed-agents, sre, human-in-the-loop, webhook, automation]]
created: 2026-04-24
updated: 2026-04-24
---

# Managed Agents — SRE Incident Response Pattern

Anthropic cookbook: [Build an SRE Incident Response Agent with Claude Managed Agents](https://platform.claude.com/cookbook/managed-agents-sre-incident-responder)

## Core Concept

Automate 3 a.m. incident triage by investigating logs, applying team runbooks, drafting infrastructure fixes, and **gating deployment behind human approval**. The agent runs in a sandboxed cloud environment, triggered by a single webhook, with full auditability via the Anthropic Console.

> *"An agent can take that first pass for you and have a fix waiting for review by the time you're at your keyboard — as long as it has the right context and a human makes the final call."*

## Architecture Flow

```
PagerDuty Webhook
    │
    ▼
Session Creation (cloud sandbox)
    │
    ▼
Skill + Mounted Resources (logs, infra YAML, runbooks)
    │
    ▼
Sandbox Investigation (bash/read/edit via agent_toolset)
    │
    ▼
Custom Tool Calls (open_pull_request → request_approval)
    │
    ▼
Human Approval Gate (Slack button interaction)
    │
    ▼
merge_pull_request (only if approved) → Terminate
```

## Key Components

### 1. Runbook Skill (Progressive Disclosure)

Skills mount as filesystem bundles. The agent sees only the description upfront and reads the full content when relevant:

```python
RUNBOOK_SKILL = """\
---
name: incident-runbooks
description: How to triage production incidents using the team runbooks.
---
 
# Incident runbooks
When an alert references a service, locate that service's recent logs
and identify the failure signature...
Consult the team runbooks before proposing any fix...
Any fix must be opened as a pull request that cites the runbook followed.
Do not patch live resources directly.
"""
```

### 2. Agent System Prompt

```python
SRE_SYSTEM_PROMPT = """\
You are an on-call SRE agent. Each user message is a PagerDuty alert
payload. Triage to root cause and ship the minimal safe fix.

Workflow:
1. Read logs, identify failure signature
2. Find root cause in infrastructure repo, produce unified diff (diff -u)
3. open_pull_request(title, body, diff)
4. request_approval(summary) — wait for human decision
5. Only if "approved": merge_pull_request(pr_number)

Never call merge_pull_request unless request_approval returned "approved".
Keep the fix minimal — do not refactor unrelated config.
"""
```

### 3. Custom Tools (Human-in-the-Loop Gate)

```python
tools=[
    {"type": "agent_toolset_20260401", "default_config": {"enabled": True, "permission_policy": {"type": "always_allow"}}},
    {"type": "custom", "name": "open_pull_request", "input_schema": {...}},
    {"type": "custom", "name": "request_approval", "input_schema": {...}},
    {"type": "custom", "name": "merge_pull_request", "input_schema": {...}}
]
```

### 4. Slack Approval Handler

```python
def post_for_approval(session_id, event_id, summary):
    slack.client.chat_postMessage(
        channel=ONCALL_CHANNEL,
        blocks=[
            {"type": "section", "text": {"type": "mrkdwn", "text": summary}},
            {"type": "actions", "elements": [
                {"type": "button", "text": "Approve", "action_id": "approve",
                 "value": f"{session_id}:{event_id}"},
                {"type": "button", "text": "Reject", "action_id": "reject",
                 "value": f"{session_id}:{event_id}"},
            ]},
        ],
    )
```

## Implementation Workflow

| Step | Action | Key API |
|------|--------|---------|
| **1. Upload Skill** | Package `SKILL.md` + helpers → zip → upload | `client.beta.skills.create()` |
| **2. Create Agent** | Attach system prompt, skill, built-in toolset, & custom tools | `client.beta.agents.create()` |
| **3. Environment & Mount** | Create `cloud` env with `limited` networking. Upload logs, infra YAML, runbooks | `client.beta.files.upload()` → `resources` mount list |
| **4. Trigger Session** | Webhook handler creates session, sends alert JSON as first `user.message` | `client.beta.sessions.create()` + `events.send()` |
| **5. Poll & Service Tools** | Loop through `events.list()`. Auto-handle `open_pull_request`/`merge_pull_request`. Pause on `request_approval` | `stop_reason.type == "requires_action"` |

### Serving Custom Tool Calls

```python
def handle_custom_tool(session_id, event_id, tool_name, tool_input):
    if tool_name == "open_pull_request":
        result = github.create_pr(tool_input["title"], tool_input["body"], tool_input["diff"])
    elif tool_name == "request_approval":
        # Post to Slack, return "pending", Slack handler sends "approved"/"rejected"
        result = post_for_approval(session_id, event_id, tool_input["summary"])
    elif tool_name == "merge_pull_request":
        result = github.merge_pr(tool_input["pr_number"])
    
    client.beta.sessions.events.send(
        session_id=session_id,
        events=[{"type": "tool_result", "tool_use_id": event_id, "content": json.dumps(result)}],
    )
```

### Session Event Loop

```python
with client.beta.sessions.events.stream(session.id) as stream:
    client.beta.sessions.events.send(
        session_id=session.id,
        events=[{"type": "user.message", "content": [{"type": "text", "text": prompt}]}],
    )
    for ev in stream:
        if ev.type == "agent.tool_use" and ev.tool_name == "request_approval":
            # Pause, wait for Slack callback
            pass
        elif ev.type == "session.status_idle":
            break
        elif ev.type == "session.status_terminated":
            raise RuntimeError(f"Session terminated: {session.trace_url()}")
```

### GitHub MCP Integration (Production)

```python
agent = client.beta.agents.create(
    ...,
    mcp_servers=[{"type": "url", "name": "github", "url": "https://api.githubcopilot.com/mcp/"}],
    tools=[{"type": "agent_toolset_20260401", ...}, {"type": "mcp_toolset", "server_name": "github"}],
)
session = client.beta.sessions.create(..., vault_ids=[github_vault.id])
```

## Comparison: Managed Agents vs Claude Agent SDK for SRE

| Aspect | Managed Agents | Claude Agent SDK |
|--------|---------------|------------------|
| **Execution** | Anthropic-hosted cloud sandbox | Local subprocess or custom hosting |
| **MCP** | MCP toolsets + Vault-backed credentials | Self-hosted MCP servers via stdio |
| **Tools** | agent_toolset_20260401 (8 tools) + custom tools | Full SDK toolset, Bash, custom MCP tools |
| **Safety** | Custom tools with requires_action gate | PreToolUse hooks, command allowlists |
| **Audit** | Anthropic Console event log | Local transcript (JSONL) |
| **Best for** | Webhook-triggered, multi-tenant workflows | Infrastructure you control directly |

## Key Insights

1. **Skills as Progressive Disclosure**: Skills mount as filesystem bundles; agent sees only descriptions until context requires full content. Encodes institutional knowledge as Markdown.
2. **Human-in-the-Loop via Custom Tools**: `request_approval` creates a natural pause point. The session waits for external callback (Slack button) before continuing.
3. **Sandbox Isolation**: Cloud environments provide `limited` networking by default — only necessary endpoints exposed.
4. **Webhook-Driven Architecture**: Single PagerDuty webhook triggers full investigation → fix → approval flow. No polling needed.
5. **Audit Trail**: Every tool call, file read, and decision logged to Anthropic Console. Session trace URLs accessible for post-incident review.

## Related

- [[claude-agent-sdk-sre-patterns]] — The same pattern on Claude Agent SDK
- [[chief-of-staff-agent-patterns]] — Hooks, subagents, and plan mode
-  — Managing long-running agent context
