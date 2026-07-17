---
title: "Junior"
created: 2026-07-17
updated: 2026-07-17
type: entity
tags:
  - coding-agents
  - agent-architecture
  - agent-design-patterns
  - agent-tooling
  - open-source
  - developer-tooling
  - reactive-systems
  - sentry
  - ai-agents
  - proactive
sources: [raw/articles/2026-07-16_armin-ronacher_reactive-agents-are-proactive.md]
---

# Junior

## Overview

Junior is Sentry's open-source AI coding agent, built by [[entities/armin-ronacher|Armin Ronacher]] and the Sentry team. Junior is designed to autonomously manage the full pull request lifecycle — from creation through CI resolution, review feedback, and merge — using a novel **resource subscription** architecture that allows the agent to react to external events within an ongoing conversation.

Junior is available on GitHub at [github.com/getsentry/junior](https://github.com/getsentry/junior).

## Architecture

### Resource Subscriptions

Junior's defining architectural feature is its **resource subscription** system, documented by Ronacher in "Reactive Agents are Proactive" (July 16, 2026). Unlike traditional coding agents that operate in request-response cycles, Junior can subscribe to external resource events (CI checks, PR reviews, merges) and receive them as follow-up messages within an existing conversation session.

The core interface is `subscribeToResourceEvents`, a generalized, provider-agnostic mechanism:

```typescript
subscribeToResourceEvents({
  resourceRef: "github:pull_request:getsentry/junior#208",
  provider: "github",
  resourceType: "pull_request",
  label: "GitHub PR getsentry/junior#208",
  events: ["checks.failed", "review.changes_requested", "state.merged"],
  intent: "Notify this thread if checks fail, changes are requested, or the PR merges.",
});
```

When a tool (such as `github_createPullRequest`) returns a response, it includes a `subscribable` hint that tells the agent a resource is available for subscription, along with `supportedEvents` and `suggestedEvents` fields.

### Key Design Decisions

- **Per-conversation, not global**: Subscriptions fire within an existing agent session, not as new sessions. The agent maintains context across the full PR lifecycle.
- **Follow-up messages, not steering**: Subscription notifications are injected as follow-up messages (not steering/user messages), allowing the agent to act autonomously without user prompting.
- **`[[NO_REPLY]]` marker**: The agent can emit a special marker to suppress visible assistant responses when handling events silently (e.g., auto-fixing a CI failure). Without this, the conversation becomes extremely noisy.
- **Event batching**: Multiple events arriving within a short time window are batched into a single notification, reducing message noise.
- **Provider-agnostic**: The subscription interface is fully generalized. The same mechanism will be used for subagents — not just GitHub events.

### Production Behavior

In production, Junior ~100% subscribes to pull requests it creates. It automatically:

- Resolves build failures detected by CI checks
- Addresses review feedback (requested changes, comments)
- Updates Slack threads with progress
- Handles merge events

Ronacher describes this as producing a "much more natural" developer experience. The central insight: agents that react to events are actually **proactive** agents — they drive work forward without waiting for human intervention.

## Related Concepts

- [[concepts/agent-resource-subscriptions]] — the generalized design pattern
- [[entities/armin-ronacher]] — creator and primary architect
- [[entities/sentry]] — parent company
- [[concepts/coding-agents/agentic-coding]] — broader agentic coding context
- [[entities/pi]] — Pi coding agent (Earendil), another minimal agent design

## Sources

- [[raw/articles/2026-07-16_armin-ronacher_reactive-agents-are-proactive]] — "Reactive Agents are Proactive" (July 16, 2026)
- https://github.com/getsentry/junior — Junior GitHub repository
