---
title: "Ramp Inspect (Background Coding Agent)"
type: concept
created: 2026-05-09
updated: 2026-05-09
status: L2
tags:
  - coding-agents
  - ai-agents
  - sandbox
  - infrastructure
  - developer-tooling
sources:
  - "[[raw/articles/2026-05-xx_ramp_background-agent-inspect]]"
related:
  - "[[concepts/background-agents]]"
  - "[[concepts/autonomous-agents]]"
  - "[[concepts/coding-agents/closing-the-software-loop]]"
  - "[[entities/ramp]]"
---

# Ramp Inspect (Background Coding Agent)

Ramp's internally built **background coding agent** "Inspect". Beyond standard coding agent capabilities, it is characterized by its ability to **autonomously close the verification loop**.

## Key Metrics

- **Adoption Rate**: Approximately 30% of all PRs created by Inspect (achieved in just a few months)
- **Runtime Environment**: Modal sandbox VMs (with Vite, Postgres, Temporal)
- **Supported Models**: All frontier models, MCP, custom tools
- **Interfaces**: Slack, Chrome Extension, Web, VS Code, Pull Request — all bidirectional sync

## Architecture

### Sandbox (Modal)

```
Image Registry → Build every 30 minutes
  ├── Clone repository
  ├── Install dependencies
  └── Save Snapshot

Session start → Instant VM from Snapshot → Start working immediately
```

- GitHub App authentication (user-independent)
- git config user.name/email set at session start

### Verification Loop

Key differences from standard coding agents:

| Standard Agent | Inspect |
|-------------------|---------|
| Code generation only | Code generation + **Autonomous Verification** |
| Test execution requires explicit instruction | Automatic test execution |
| Human performs confirmation | Autonomous confirmation via screenshots + live preview |
| Constrained by insufficient context | Connected to Sentry, Datadog, LaunchDarkly, Braintrust, GitHub, Slack, Buildkite |

### Multimodal Interfaces

- **Slack**: Chat by sending screenshots
- **Chrome Extension**: Highlight page elements to request changes
- **Web Interface**: Conversation in browser
- **Pull Request**: Discussion on PRs
- **Web-based VS Code**: For manual editing when needed
- **All Sessions are Multiplayer**: Just share the session URL with colleagues for collaboration

## Design Philosophy

> "Session speed should be limited only by the model provider's TTFT. Everything else (cloning, installation) should be completed before the session starts."

- **Unlimited Concurrent Sessions**: Try multiple versions with the same prompt, select the most successful one
- **Instant Idea Capture**: Find a bug at night → Start a session via Slack → Review PR in the morning
- Voice input support

## References

- [Why We Built Our Background Agent — Ramp Builders](https://builders.ramp.com/post/why-we-built-our-background-agent)
- [Modal Sandboxes](https://modal.com/docs/guide/sandboxes)
