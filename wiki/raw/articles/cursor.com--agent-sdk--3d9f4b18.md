---
source_url: https://cursor.com/blog/agent-sdk
fetched: 2026-10-29 12:05 UTC
extraction: urllib-chrome-ua-strip-html
title: "Introducing the Agent SDK"
author: Cursor
published: 2026-10-28
hn: https://news.ycombinator.com/item?id=50273731
sha256: aef9bd417d4e88d984ef58af9cbc59e4e1d90a8e848c6e6d84ec46c126f92432
---

# Introducing the Agent SDK (Cursor)

Software teams use agents defined as code to handle recurring work across the development lifecycle. These agents connect to the places where a team works and act when relevant events occur — reviewing a pull request, executing a compliance workflow, or investigating an incident.

The Agent SDK is the framework Cursor uses to build its own managed agents like Bugbot, Security Reviewer, and Rollouts. Agent SDK lets you define agents in code and manage them like any other software project. Start from a template or point your coding agent at the docs. Then `agent-sdk deploy` publishes to Cursor infrastructure with one command.

## Build around your workflow

Agents respond to the events your team already handles and follow policies your team can inspect and change. Code review example: an agent responds to PR events from GitHub/GitLab/Bitbucket, assesses the risk of a change, routes it to the right team, and approves changes that meet policy.

Cursor case study: a team built kb-reviewer in about a day — checks every PR in their main codebase against a growing knowledge base of lessons learned, flags changes that contradict a recorded lesson, cites the note behind each finding, and encourages engineers to reconcile discrepancies.

## Multi-agent + evals

Agents can hand a task to another specialized agent with its own tools and sessions, or divide a job among subagents working in parallel. The SDK supports evals and event replay out of the box, for rapid development with assurances that critical workflows execute as expected.

Customer quote: "The Agent SDK has enabled PGA to build every component of our software factory on Cursor's infrastructure... built-in support for evals allows us to quickly iterate on new ideas and optimize existing capabilities reliably." — Michael Gyarmathy, Principal Engineer, PGA Tour (PGA Tour uses the Agent SDK to power their "software development factory").

(Positioning note: this is Cursor's answer to Anthropic's Claude Agent SDK / OpenAI Agents SDK — 'agents defined as code', managed-agent frameworks from an IDE vendor, deploying to the vendor's own infrastructure.)
