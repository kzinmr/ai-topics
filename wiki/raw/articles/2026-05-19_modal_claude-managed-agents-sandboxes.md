---
title: "Introducing Claude Managed Agents with Modal Sandboxes"
source: "https://modal.com/blog/introducing-claude-managed-agents-with-modal-sandboxes"
author: "Modal Team"
date: 2026-05-19
source_type: blog
source_domain: modal.com
source_org: Modal Labs
tags: [claude, managed-agents, modal, sandbox, gpu, firecracker]
references:
  - "https://modal.com/blog/introducing-claude-managed-agents-with-modal-sandboxes"
---

# Introducing Claude Managed Agents with Modal Sandboxes

**Source**: [Modal Blog](https://modal.com/blog/introducing-claude-managed-agents-with-modal-sandboxes)
**Published**: May 19, 2026
**Context**: Collaboration announcement between Modal and Anthropic for a first-class integration of Modal Sandboxes with Claude Managed Agents.

---

## Overview

Modal now offers a **first-class integration** that replaces Anthropic's default sandbox with **Modal Sandboxes**, providing fast cold-starts, custom images, snapshotting, and burst pricing while retaining Anthropic's managed agent loop.

> This integration lets you run all tool calls in a self-hosted Modal Sandbox, combining Anthropic's convenient session management with Modal's infrastructure performance and flexibility.

---

## Why This Architectural Approach Matters

- **Security**: Model loop runs outside execution environment → clearer security boundaries.
- **Control**: Teams get better observability, failure handling, and scaling.
- **Simplicity**: Anthropic handles session state; your app sends events/streams results.

> "We believe this approach is likely to emerge as the winning pattern…"

---

## Modal Sandboxes vs. Anthropic's Default Sandbox

### 1. Fast Startup on Custom Images
Fully customizable environments with rapid builds via Modal Images.

### 2. Persistence Options
Volumes, directory snapshots, filesystem snapshots, and memory snapshots to preserve state across runs.

### 3. Cost Efficiency
**Burst pricing**: pay only for what you use, no idle costs. No minimums.

### 4. Network Security
Short-lived connect tokens for authenticated, direct access to sandbox services without public exposure.

### 5. Massive Scale & GPU Access
Up to **100,000 concurrent sandboxes** per customer, with configurable CPU, memory, and GPU resources (up to H100).

---

## Customer Perspectives

### Mason AI
> "Our use cases require secure orchestration of internal tools across a complex product surface. Modal's Sandbox gives us the security boundary our enterprise customers need, and combining it with Claude Managed Agents gave us a powerful harness without hand-rolling extra complexity."

### DoorDash
> "As we scale agentic commerce for local businesses, we need a highly efficient path to production with full harness control, scale, and reliability."

### Blend
> "Having a fully configured environment with the right tooling, context, and credentials already in place is what makes it possible for agents to help engineers reason across all of that faster."

---

## Getting Started

- **Reference examples available**: a CLI agent and a Slack-bot
- **Action**: Clone the example repos, swap in custom image and tools
- **Free compute**: $30/month free compute on Modal
