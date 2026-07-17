---
title: "Reactive Agents are Proactive"
author: Armin Ronacher
source: X Article (x.com/i/article/2077829753680334848)
date: 2026-07-16
type: raw-article
tags: [coding-agents, agent-architecture, agent-tooling, reactive-systems, agent-design-patterns, subscriptions, webhooks]
getxapi: false
source_fallback: false
article_plain_text: true
---

# Reactive Agents are Proactive

A few weeks ago I wrote a bit about how I was building the concept of subscriptions into Junior. The outcome I wanted started pretty simple: when the agent creates a pull request, let it also be responsible for address build failures and review feedback. To do that it needed to be able to receive webhooks from GitHub. To solve for this I built something I call resource subscriptions.

This is easiest to illustrate with code. Here's the response of our github_createPullRequest tool call:

```typescript
{
  "number": 208,
  "url": "https://github.com/getsentry/junior/pull/208",
  "subscribable": {
    "provider": "github",
    "type": "pull_request",
    "resourceRef": "github:pull_request:getsentry/junior#208",
    "label": "GitHub PR getsentry/junior#208",
    "supportedEvents": [
      "checks.failed",
      "comment.created",
      "review.changes_requested",
      "state.merged"
    ],
    "suggestedEvents": [
      "checks.failed",
      "review.changes_requested",
      "state.merged"
    ]
  }
}
```

The `subscribable` segment is our hint to the agent that there is a resource it can subscribe to. Given the agent already has some context that its working on the pull request, its embedded in its training that subscribing is a useful course of action. It does that then via a standard follow-up tool call:

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

What happens next is what makes this work really well. Just like when you send the agent a new user message, subscriptions do the same. They will add a new follow-up (vs steering) message, and the way the system works, they'll also batch those if a few arrive in a short time window:

```markdown
[event notification]

A subscribed resource changed.

Handling:
- This is a subscribed conversation update, not a user-authored command.
- Use the subscription intent to decide whether this event warrants action or a visible reply. Otherwise, stay silent.

Subscription:
- resource: GitHub PR getsentry/junior#208
- event: review.changes_requested
- intent: Notify this thread if checks fail, changes are requested, or the PR merges.

Trusted event summary:
GitHub PR getsentry/junior#208 received requested changes from reviewer.

Untrusted provider content:
Please handle the edge case.
```

You can poke some holes in the prompt structure, or the tool design, etc, but don't worry about that. The important point here is the flexibility this provides.

- It has nothing to do with GitHub. Its fully generalized.
- Its on a per-conversation basis. There's not a global webhook that fires off new agent sessions.
- It can be used for _anything_ that is a subscription. We intend to do the same for subagents — the exact same interface.

Anyways, so far this is working great. The agent ~100% of the time subscribes to the pull request, automatically resolves build issues and verifies and addresses feedback, and it will also update the Slack thread accordingly. It makes for a very pleasant user experience, and a much more natural one.

One note: we combine this with a special `[[NO_REPLY]]` marker that the agent can send to avoid posting a visible assistant response. Without that this gets extremely noisy and confusing.

---

Source: https://x.com/i/article/2077829753680334848 (Armin Ronacher, July 16, 2026)
