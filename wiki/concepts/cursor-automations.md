# Cursor Automations

**Cursor Automations** is a feature introduced by [[entities/anysphere]] (Cursor) that enables always-on AI agents running on schedules or triggered by events. Announced alongside [[concepts/coding-agents/cursor-composer-2-5]] in May 2026, Automations represent Cursor's expansion from interactive coding assistance into autonomous development workflows.

## Overview

Cursor Automations are background agents that spin up a cloud sandbox, follow instructions using configured MCPs and models, and verify their own output. They can be triggered by:

- **Schedules**: Cron-like periodic execution
- **Events**: Slack messages, Linear issue creation, GitHub PR merges, PagerDuty incidents
- **Webhooks**: Custom event sources
- **Memory**: Agents learn from past runs and improve with repetition

## Key Use Cases at Cursor

### Review & Monitoring

| Automation | Trigger | Function |
|-----------|---------|----------|
| **Bugbot** | PR opened/updated | Original automation — runs thousands of times daily, caught millions of bugs |
| **Security review** | Push to main | Audits diffs for vulnerabilities, skips discussed issues, posts findings to Slack |
| **Agentic codeowners** | PR open/push | Classifies risk (blast radius, complexity, infra impact), auto-approves low-risk PRs, assigns reviewers |
| **Incident response** | PagerDuty incident | Investigates logs via Datadog MCP, checks recent code changes, proposes fix PR |

### Productivity & Chores

| Automation | Trigger | Function |
|-----------|---------|----------|
| **Weekly summary** | Schedule (weekly) | Slack digest of meaningful repo changes — PRs, bug fixes, tech debt, security updates |
| **Test coverage** | Schedule (daily) | Reviews merged code, identifies coverage gaps, adds tests following conventions, opens PR |
| **Bug report triage** | Slack message | Checks for duplicates, creates Linear issue, investigates root cause, attempts fix, replies in thread |

## Enterprise Adoption

**Rippling** uses Cursor Automations for:
- Personal assistant aggregating meeting notes, action items, TODOs, and Loom links from Slack
- Cron agent running every 2 hours, deduplicating across GitHub PRs, Jira issues, and Slack mentions
- Slack-triggered Jira issue creation from threads
- Confluence discussion summaries
- Incident triage, weekly status reports, on-call handoff

## Architecture

When an automation is invoked:
1. Cloud sandbox spins up (isolated execution environment)
2. Agent follows configured instructions using MCPs and selected models
3. Agent verifies its own output
4. Results are posted to configured channels (Slack, Linear, GitHub PRs)
5. Memory tool stores learnings for future runs

## Significance

Cursor Automations address a key gap in the agentic coding landscape: while coding agents excel at interactive code generation, the **review, monitoring, and maintenance** phases of the software development lifecycle haven't sped up proportionally. Automations extend the agent paradigm into these asynchronous, always-on workflows, creating a complete development pipeline from ideation through production monitoring.

The memory tool integration enables **progressive improvement** — agents get better at recurring tasks through repetition, rather than starting from scratch each time.

## Related

- [[entities/anysphere]] — Developer
- [[concepts/coding-agents/cursor-composer-2-5]] — Companion model release
- [[concepts/mcp]] — Tool integration protocol
- [[entities/coder]] — Competing self-hosted agent platform
- [[concepts/agentic-engineering]] — Engineering paradigm Automations supports
