---
title: "Agent Resource Subscriptions"
created: 2026-07-17
updated: 2026-07-17
type: concept
tags:
  - agent-architecture
  - agent-design-patterns
  - coding-agents
  - reactive-systems
  - event-driven-architecture
  - subscriptions
  - agent-tooling
  - proactive
  - ai-agents
sources: [raw/articles/2026-07-16_armin-ronacher_reactive-agents-are-proactive.md]
---

# Agent Resource Subscriptions

## Definition

Agent resource subscriptions are a design pattern for AI coding agents that enables an agent to subscribe to external resource events (CI checks, PR reviews, merges, subagent completions) and receive them as follow-up messages within an ongoing conversation session. The pattern was first publicly documented by [[entities/armin-ronacher|Armin Ronacher]] in the context of [[entities/junior|Junior]], Sentry's coding agent, but is designed as a fully generalized, provider-agnostic mechanism.

The central insight: **reactive agents (responding to external events) are actually proactive agents** — they drive work forward autonomously without requiring human prompting at each step.

## Core Interface

The pattern centers on a `subscribeToResourceEvents` tool with the following conceptual shape:

```
subscribeToResourceEvents(
  resourceRef: provider-qualified resource identifier,
  provider: event source provider name,
  resourceType: type of resource being subscribed to,
  label: human-readable description,
  events: array of event types to listen for,
  intent: natural language description of what the agent should do with these events
)
```

When a tool creates a subscribable resource (e.g., `github_createPullRequest`), it returns a `subscribable` hint:

```
subscribable: {
  provider: string,
  type: string,
  resourceRef: string,
  label: string,
  supportedEvents: string[],
  suggestedEvents: string[]
}
```

This hint is embedded in the tool response and the agent's training steers it toward subscribing when appropriate.

## Key Architectural Properties

### 1. Generalized, Provider-Agnostic Interface

The subscription mechanism is not tied to any specific provider or event source. The same `subscribeToResourceEvents` interface handles GitHub events, Slack notifications, subagent completions, and any future resource type. This is achieved through:

- **Provider-qualified resource references** (`github:pull_request:getsentry/junior#208`) that encode provider and type information
- **Provider field** that routes events from the correct source
- **Event type strings** defined per provider, not hardcoded globally

### 2. Per-Conversation Subscriptions (Not Global Webhooks)

Subscriptions are scoped to individual agent conversation sessions. This is a critical design choice with several implications:

- **Context preservation**: The agent maintains the full conversation history, understanding where the PR came from and what the user asked for originally
- **No session orchestration**: There is no need for an external orchestration layer to match incoming webhooks to the correct agent session
- **Natural closure**: When the conversation ends or the subscription expires, the subscription is cleaned up naturally

Contrast this with a global webhook model where each event triggers a new agent session that must reconstruct context from scratch.

### 3. Follow-Up vs Steering Messages

Subscription notifications are injected into the conversation as **follow-up messages**, not steering/user messages. In agent conversation models:

- **Steering messages** are treated as user commands — they direct the agent's behavior
- **Follow-up messages** are informational updates that the agent processes autonomously

This distinction allows the agent to decide whether an event warrants action or a visible response. The subscription carries an `intent` field (natural language) that the agent uses to interpret the event, rather than being explicitly steered by it.

### 4. NO_REPLY Marker

To prevent noisy visible responses when the agent handles events silently, the pattern uses a `[[NO_REPLY]]` marker that the agent can emit. Without this, every handled event would produce a visible assistant message, making conversations confusing and cluttered. This is especially important for automated workflows like:

- Auto-fixing a CI failure (the fix is the response, not a chat message)
- Noting a successful check (no action needed)
- Processing batched events where only the final outcome matters

### 5. Event Batching

Multiple events arriving within a short time window are batched into a single notification message. This prevents:

- Message flooding when multiple CI checks complete simultaneously
- Redundant agent processing of related events
- Noisy conversation threads

## Production Behavior

As documented by Ronacher for Junior:

- **~100% subscription rate**: The agent nearly always subscribes to PRs it creates
- **Autonomous resolution**: Build failures are automatically addressed
- **Review feedback handling**: Requested changes and comments are processed without user intervention
- **Cross-channel coordination**: Slack threads are updated with progress
- **Natural developer experience**: The result is described as "much more natural" — the agent behaves like a proactive team member rather than a tool waiting for commands

## Design Implications

### Proactive Through Reactivity

The pattern upends the conventional framing of "proactive vs. reactive" agents. An agent that subscribes to events and acts on them autonomously is exercising agency — it is proactive precisely because it is reactive to the right signals. The subscription model transforms reactive infrastructure (webhooks, events) into proactive behavior.

### Conversation as Persistent Context

Per-conversation subscriptions make the agent session a long-lived, context-rich environment. Unlike stateless function calls that start fresh each time, the subscription model treats the conversation as the agent's working memory — events arrive into an existing understanding rather than creating a new one.

### Extensibility to Subagents

Ronacher explicitly notes that the same `subscribeToResourceEvents` interface will be used for subagents. When a parent agent delegates work to a subagent, it can subscribe to the subagent's completion events using the identical mechanism — no special subagent communication protocol needed.

## Comparison to Other Patterns

| Pattern | Subscription Model | Context | Orchestration |
|---------|-------------------|---------|---------------|
| **Resource Subscriptions (Junior)** | Per-conversation follow-up messages | Preserved in session | Self-contained in agent |
| **Global Webhooks** | New session per event | Must be reconstructed | External orchestrator |
| **Polling** | Agent repeatedly checks status | Preserved in session | Agent-managed loops |
| **Callback URLs** | External system calls back | Varies | External system |

## Known Implementations

- **[[entities/junior|Junior]]** (Sentry): The reference implementation. GitHub PR lifecycle management with resource subscriptions. Open source at github.com/getsentry/junior.

## Related Concepts

- [[entities/armin-ronacher]] — architect and primary documenter of the pattern
- [[entities/junior]] — reference implementation
- [[concepts/agent-harnesses]] — the harness-level infrastructure that delivers subscription events
- [[concepts/coding-agents/agentic-coding]] — broader context of autonomous coding agents
- [[concepts/agent-security-patterns]] — security implications of autonomous event handling
- [[concepts/agent-skills]] — skills as a complementary agent capability mechanism

## Sources

- [[raw/articles/2026-07-16_armin-ronacher_reactive-agents-are-proactive]] — "Reactive Agents are Proactive" by Armin Ronacher (July 16, 2026)
