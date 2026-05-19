---
title: "Claude Managed Agents"
type: concept
created: 2026-04-27
updated: 2026-05-19
tags:
  - anthropic
  - ai-agents
  - memory-systems
  - orchestration
aliases: [claude-managed-agents, claude-platform-agents]
sources:
  - https://platform.claude.com/docs/en/managed-agents/multi-agent
  - https://platform.claude.com/docs/en/managed-agents/define-outcomes
  - https://platform.claude.com/docs/en/managed-agents/webhooks
  - https://platform.claude.com/docs/en/managed-agents/dreams
  - raw/articles/2026-05-07_claude-managed-agents-multi-agent-orchestration.md
  - raw/articles/2026-05-07_claude-managed-agents-outcomes.md
  - raw/articles/2026-05-07_claude-managed-agents-webhooks.md
  - raw/articles/2026-05-07_claude-managed-agents-dreams.md
  - raw/articles/2026-05-19_claude-managed-agents-sandbox-mcp-tunnels.md
---


# Claude Managed Agents

**Claude Managed Agents** is Anthropic's enterprise-grade AI agent platform available on the Claude Platform. Agents run continuously with governance, observability, and guardrails.

> **Beta Header:** All Managed Agents API requests require the `managed-agents-2026-04-01` beta header.

---

## Architecture: Session Log + Memory Store

Managed Agents use a two-component context model:

1. **Session log** — Claude fetches and transforms session context over the course of a task. The session lives outside the context window, with benefits outlined by [a1zhang](https://x.com/a1zhang) and [lateinteraction](https://x.com/lateinteraction).

2. **Memory store** — Persistent, workspace-scoped collections of text documents that outlive any single session. Claude can write files to persist context across sessions.

---

## 1. Multi-Agent Orchestration (GA)

Multi-agent orchestration allows a single **coordinator agent** to manage multiple specialized agents within a single session. Enables parallel task execution, domain specialization, and isolated context management.

### Core Mechanics

| Feature | Detail |
|---------|--------|
| **Shared Environment** | All agents share the same container and filesystem |
| **Isolated Contexts** | Each agent runs in its own **session thread** with independent conversation history |
| **Persistence** | Threads are persistent; agents retain context across turns if recalled by the coordinator |
| **No Sharing** | Tools, system prompts, and specific contexts are NOT shared between agents |
| **Depth Limit** | Coordinator can only delegate to one level of agents (depth > 1 is ignored) |

### Delegation Patterns

- **Parallelization** — Fanning out independent subtasks (e.g., searching multiple sources simultaneously)
- **Specialization** — Routing to agents with domain-specific tools (e.g., a "Security Agent")
- **Escalation** — Using a more capable model for complex subtasks (e.g., Sonnet → Opus)

### Configuration

Enable multi-agent by setting the `multiagent` property on an agent with the `agent_toolset_20260401` tool:

```python
coordinator = client.beta.agents.create(
    name="Engineering Lead",
    model="claude-opus-4-7",
    system="You coordinate engineering work...",
    tools=[{"type": "agent_toolset_20260401"}],
    multiagent={
        "type": "coordinator",
        "agents": [
            {"type": "agent", "id": reviewer_agent.id},
            {"type": "agent", "id": test_writer_agent.id, "version": "v1"},
            {"type": "self"},  # Coordinator can spawn copies of itself
        ],
    },
)
```

### Constraints
- **Roster limit:** Maximum **20 unique agents**
- **Concurrency limit:** Maximum **25 concurrent threads** per session

### Thread Types & Monitoring

| Thread Type | Description |
|-------------|-------------|
| **Primary Thread** | Session-level stream (`/v1/sessions/:id/events/stream`). High-level summary of all activity |
| **Session Threads** | Individual streams per agent. Detailed reasoning and specific tool calls |

**Key events:** `session.thread_created`, `session.thread_status_idle`, `agent.thread_message_received`, `agent.thread_message_sent`

### Operations
- **Interrupt** — Send `user.interrupt` with `session_thread_id` to stop a specific agent
- **Archive** — Use `archive` on an `idle` thread to free up space against the 25-thread limit
- **Tool permissions** — Sub-agent tool requests (e.g., `always_ask`) are cross-posted to the **primary thread** for handling

---

## 2. Outcomes Loop: Rubric-Driven Self-Improvement (GA)

The `outcome` feature transitions a Managed Agent session from conversation to goal-oriented work. Users define a target result and quality rubric; the agent self-evaluates and iterates until criteria are met.

### Core Mechanism: The Grader

An independent **grader** sub-agent evaluates the agent's output:
- **Independent context window** — prevents influence from the main agent's implementation choices
- **Feedback loop** — per-criterion breakdown; unmet requirements trigger revision iterations

### Creating a Rubric

A mandatory Markdown document describing scoring criteria. Pass as inline text or upload via the Files API.

```markdown
# DCF Model Rubric
## Revenue Projections
- Uses historical revenue data from the last 5 fiscal years
- Projects revenue for at least 5 years forward
## Output Quality
- All figures are in a single .xlsx file
- Key assumptions are on a separate "Assumptions" sheet
```

### Starting an Outcome Session

Send a `user.define_outcome` event after creating a session. The agent begins immediately.

```python
client.beta.sessions.events.send(
    session_id=session.id,
    events=[{
        "type": "user.define_outcome",
        "description": "Build a DCF model for Costco in .xlsx",
        "rubric": {"type": "text", "content": RUBRIC},
        "max_iterations": 5,  # Default 3, Max 20
    }],
)
```

### Evaluation Results

| Result | Meaning |
|--------|---------|
| `satisfied` | Criteria met; session transitions to `idle` |
| `needs_revision` | Gaps found; agent starts a new iteration |
| `max_iterations_reached` | Limit hit; one final revision before idling |
| `failed` | Rubric/description contradiction; session stops |
| `interrupted` | User sent a `user.interrupt` event |

### Constraints
- **Max iterations:** Capped at 20 (default 3)
- **Sequential chaining:** Only one outcome at a time; chain by sending new `user.define_outcome` after completion
- **Persistence:** Sessions retain history of prior outcomes
- **Deliverables:** Agent writes outputs to `/mnt/session/outputs/`; fetch using the Files API scoped to the `session.id`

---

## 3. Dreams: Memory Curation (Research Preview)

**Dreams** is a Research Preview feature that allows Claude to reflect on past sessions to curate, deduplicate, and reorganize an agent's memory store.

### Overview

While agents write to memory stores incrementally, stores can become cluttered with duplicates, contradictions, or stale data. **Dreams** solves this by reading an existing memory store and past session transcripts to produce a new, optimized output memory store.

> **Required Headers:** `managed-agents-2026-04-01` + `dreaming-2026-04-21`

### Key Benefits
- **Deduplication** — Merges redundant entries
- **Conflict Resolution** — Replaces stale/contradicted entries with latest values
- **Insight Extraction** — Surfaces new patterns and insights from session transcripts
- **Non-Destructive** — Input store is never modified; separate output store created for review

### Creating a Dream

An asynchronous job taking a memory store + up to 100 optional session transcripts:

```python
dream = client.beta.dreams.create(
    inputs=[
        {"type": "memory_store", "memory_store_id": store_id},
        {"type": "sessions", "session_ids": [session_a, session_b]},
    ],
    model="claude-opus-4-7",
    instructions="Focus on coding-style preferences; ignore one-off debugging notes.",
)
```

### Dream Lifecycle

Dreams typically take **minutes to tens of minutes** to complete.

| Status | Meaning |
|--------|---------|
| `pending` | Successfully queued |
| `running` | Pipeline processing; `usage` updates real-time |
| `completed` | Finished; `outputs[]` contains new memory store ID |
| `failed` | Terminated with error; partial data in output store |
| `canceled` | User-stopped; partial data in output store |

### Using the Output

The output memory store is a standard resource attachable to future sessions:

```python
output_store_id = next(
    o.memory_store_id for o in dream.outputs if o.type == "memory_store"
)
session = client.beta.sessions.create(
    agent=agent_id,
    environment_id=environment_id,
    resources=[{"type": "memory_store", "memory_store_id": output_store_id}],
)
```

### Limits & Billing
- **Sessions per dream:** Max 100
- **Instructions:** Max 4,096 characters
- **Billing:** Standard API token rates. Cost scales linearly with input sessions
- **Recommendation:** Start with a small batch to verify curation quality before scaling

### Common Errors
| Error | Cause |
|-------|-------|
| `timeout` | Pipeline exceeded runtime budget |
| `memory_store_org_limit_exceeded` | Organization hit memory-store cap |
| `input_memory_store_too_large` | Input exceeds pipeline size limits |
| `input_memory_store_unavailable` | Store deleted/archived during run |

---

## 4. Webhooks: Push Notifications (GA)

Webhooks provide a push-based notification system for major state changes in long-running interactions, complementing the real-time SSE event stream.

### Architecture

- **Payload Design:** Webhooks return only the event `type` and `id`, not the full object
- **Action Required:** Upon receiving an event, perform a `GET` to fetch the object (ensures fresh data, keeps payloads small)
- **Uniqueness:** Top-level `event.id` is unique; duplicate IDs = retries (discard)

### Session Events

| Event | Trigger |
|-------|---------|
| `session.status_run_started` | Agent execution began (every `running` transition) |
| `session.status_idled` | Agent awaiting input (tool approval, user message) |
| `session.status_rescheduled` | Automatic retry after transient error |
| `session.status_terminated` | Terminal error reached |
| `session.thread_created` | New multi-agent thread opened |
| `session.thread_idled` | Multi-agent interaction waiting for input |
| `session.thread_terminated` | Multi-agent thread archived |
| `session.outcome_evaluation_ended` | Single outcome evaluation iteration completed |

### Vault Events
- `vault.created` / `archived` / `deleted`
- `vault_credential.created` / `archived` / `deleted` / `refresh_failed`

### Implementation

**Endpoint Requirements:** HTTPS, Port 443, publicly resolvable hostname
**Signing Secret:** 32-byte `whsec_`-prefixed secret (shown once — store securely)
**Verification:** Use SDK `unwrap()` helper (throws on invalid signature or payload >5 min old)

**Python:**
```python
event = client.beta.webhooks.unwrap(
    request.get_data(as_text=True),
    headers=dict(request.headers),
)
```

**TypeScript (critical: use `express.raw()`, NOT `express.json()`):**
```typescript
app.post("/webhook", express.raw({ type: "application/json" }), (req, res) => {
    const event = client.beta.webhooks.unwrap(req.body.toString("utf8"), {
        headers: req.headers as Record<string, string>
    });
});
```

### Reliability
- **Ordering:** Not guaranteed; use `created_at` for sorting
- **Retries:** At least one retry on failure
- **Redirects:** `3xx` treated as failures; redirects not followed
- **Auto-disable:** ~20 consecutive failures or private IP hostname → endpoint disabled; manual re-enable in Console

---

## Memory Stores

### How They Work

- Memory stores are mounted into the agent container as directories at `/mnt/memory/<store-name>/`
- A short note about the mount is automatically injected into the system prompt
- Multiple agents can access the same memory store simultaneously
- Real-time sync: edits by one agent are reflected in all other agents' filesystems
- Concurrency handling prevents agents from overwriting each other's memory updates

### Benefits

- **Files are interpretable and sharable** — memory folders can be downloaded and shared externally
- **Export via API** — memories can be exported programmatically
- **Cross-session learning** — agents learn from experience across sessions
- **General tooling** — Claude uses standard file tools (read/write/create/delete) rather than specialized memory APIs

### Scaling Intelligence for Memory

The filesystem-as-memory approach was validated through [DavidSHershey's Claude Plays Pokémon experiment](https://x.com/DavidSHershey):

| Model | Step Count | Memory Files | Organization | Progress |
|-------|-----------|--------------|-------------|----------|
| Sonnet 3.5 | 14,000 | 31 files | Transcript-style (NPC dialogue) | Stuck in second town |
| Opus 4.6 | 14,000 | 10 files | Directory-organized, gym badges, learnings file | Significant progress |

Later models learned to use the filesystem to organize memory much better, demonstrating that with scaling intelligence, general file management tools are sufficient — Claude learns what to save and how to organize its own memories.

### Related Approaches

Several research projects have explored specialized memory tools for agents:
- **CoALA** (tedsumers) — cognitive science-inspired memory management
- **memGPT** (sarahwooders, charlespacker) — operating system models for agent memory
- **Letta.AI** — filesystem-based memory that outperforms specialized tools

The trend shows that general tools (filesystem) with scaling intelligence can match or exceed specialized memory tooling.

---

## Public Beta Launch (Apr 2026)

Anthropic launched Managed Agents in **public beta** in April 2026, marking the transition from private/preview to generally available platform feature:
- **Platform-level agent orchestration**: Complete execution environment with built-in monitoring, audit trails, and security controls
- **Brain/Hands/Session separation**: Architectural pattern where planning (Brain), execution (Hands), and context management (Session) are independently managed components
- **Enterprise-ready**: Designed for production workloads with governance and compliance features
- **MCP Integration**: Full Model Context Protocol support for external tool integration

This represents a significant shift toward **platform-provided agent infrastructure** rather than developers building custom harnesses. Compare with OpenAI's Symphony approach.

## Self-Hosted Sandboxes (Public Beta) + MCP Tunnels (Research Preview) — May 2026

Announced live at **Code with Claude London** on May 19, 2026, these two features address enterprise security and connectivity requirements:

### Self-Hosted Sandboxes (Public Beta)
Agents can now run inside the **user's own infrastructure perimeter**, with the user's security controls applied by default. Key implications:
- **Security-first enterprise deployment**: Organizations can run agents without sending code/data to Anthropic-managed cloud sandboxes
- **Data residency compliance**: Addresses regulatory requirements where data must stay within customer-controlled infrastructure
- **Authentication boundary**: Sandboxes inherit the customer's existing IAM, network policies, and security controls
- **No trust boundary change**: Agents execute where the rest of the enterprise workload already runs

This is a significant differentiator vs. competitors that require all agent execution in vendor-managed cloud environments.

### MCP Tunnels (Research Preview)
Allows Claude Managed Agents to connect to **local MCP servers** behind firewalls/NAT via secure tunnels:
- **Expanded tool surface**: Agents can access internal APIs, databases, and services that are not exposed to the public internet
- **Secure connectivity**: Tunnel-based approach maintains enterprise network security posture without requiring port forwarding or VPN configuration
- **Local development workflows**: Developers can connect agents to local MCP servers running on their development machines
- **MCP ecosystem growth**: Lowers the barrier for enterprises to integrate existing internal tools as MCP servers

### Combined Impact
Together, these features transform Claude Managed Agents from a cloud-only platform into a **hybrid deployment model** where:
- **Compute** runs in customer-controlled sandboxes (not Anthropic cloud)
- **Tools** connect via MCP Tunnels into private networks
- **Security controls** are applied at the customer perimeter, not at Anthropic's boundary

This addresses the #1 enterprise objection to agent platforms — "we can't send our code/data to a third-party sandbox."

→ Source: [@claudeai announcement](https://x.com/claudeai/status/2056645485696315581), Code with Claude London, May 19, 2026

## Significance & Harness Engineering Context

Claude Managed Agents represents Anthropic's answer to the **Harness Effect** (same model, 5-40pp performance difference by harness architecture). Key differentiators:
- **Deep orchestration** — Multi-agent with shared filesystem but isolated contexts balances collaboration and isolation
- **Outcomes loop** — First platform-native rubric-driven self-improvement cycle (vs. manual prompting patterns elsewhere)
- **Dreams** — Novel approach to memory curation inspired by ML model training patterns (epochs/consolidation), applied to agent memory
- **Webhooks** — Push-based architecture avoids polling overhead for long-running agent tasks

## Getting Started

- [Claude Managed Agents docs](https://platform.claude.com/docs/en/managed-agents)
- Use the `claude-api` skill (built into Claude Code, triggered by `/claude-api`)

## Sources

- [Multi-agent Sessions](https://platform.claude.com/docs/en/managed-agents/multi-agent) (May 2026)
- [Define Outcomes](https://platform.claude.com/docs/en/managed-agents/define-outcomes) (May 2026)
- [Webhooks](https://platform.claude.com/docs/en/managed-agents/webhooks) (May 2026)
- [Dreams](https://platform.claude.com/docs/en/managed-agents/dreams) (May 2026)
- [Memory in Claude Managed Agents](https://x.com/RLanceMartin/status/2047720067107033525) — Lance Martin (@RLanceMartin), April 2026
- [Claude Plays Pokémon](https://x.com/DavidSHershey) — David Hershey's memory experiment
- [Anthropic Managed Agents announcement](https://www.anthropic.com/managed-agents) — Jaya Gupta analysis
- [Self-hosted sandboxes + MCP tunnels](https://x.com/claudeai/status/2056645485696315581) — @claudeai, Code with Claude London, May 19, 2026
