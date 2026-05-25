---
title: "Agent-native Architectures"
author: "Dan Shipper (co-authored with Claude)"
source: "every.to/guides/agent-native"
date: "2026-01-17"
tags: ["agent-architecture", "agent-native", "sdk", "tool-design"]
---

# Agent-native Architectures

Co-authored by Dan Shipper and Claude. Synthesizes principles from Every apps (Reader, Anecdote).

## Core Principles

### 1. Parity
Whatever user can do through UI, agent should achieve through tools.
Test: Pick any UI action → Can agent accomplish it?

### 2. Granularity
Tools = atomic primitives. Features = outcomes achieved by agent in a loop.
Test: To change behavior, do you edit prompts or refactor code?

### 3. Composability
With atomic tools + parity, new features = new prompts.
Example: "weekly review" feature is just a prompt using list_files, read_file, judgment.

### 4. Emergent Capability
Agent accomplishes things not explicitly designed for.
Flywheel: Build atomic tools → Users request unanticipated things → Agent composes tools → Observe patterns → Add domain tools → Repeat.

### 5. Improvement Over Time
Agent-native apps improve through accumulated context + prompt refinement, not code changes.
- Accumulated context: State persists via context files
- Developer refinement: Ship updated prompts for all users
- User customization: Users modify prompts for their workflow

## Implementation Patterns
- Agent-to-UI communication
- iOS storage architecture
- Checkpoint and resume
- Dynamic capability discovery
- CRUD completeness

## Success Criteria
- Agent achieves UI parity
- Tools are atomic primitives; domain tools are shortcuts not gates
- New features = new prompts
- Agent handles open-ended requests in domain
- Behavior changes via prompt edits, not code refactoring
