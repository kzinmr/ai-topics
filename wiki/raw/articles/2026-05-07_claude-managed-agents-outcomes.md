---
source: https://platform.claude.com/docs/en/managed-agents/define-outcomes
title: "Define Outcomes: Claude Managed Agents"
author: Anthropic
date: 2026-05-07
tags: [claude, managed-agents, outcomes, rubric, evaluation]
---

# Define Outcomes: Claude Managed Agents

The `outcome` feature transitions a Claude Managed Agent session from a simple conversation to a goal-oriented work session. Users define a target result and a quality rubric; the agent then self-evaluates and iterates until the criteria are met.

## Core Mechanism: The Grader
When an outcome is defined, the system provisions an independent **grader** to evaluate the agent's work.
- **Independence:** The grader uses a separate context window to ensure it is not influenced by the main agent's implementation choices.
- **Feedback Loop:** The grader provides a per-criterion breakdown. If requirements aren't met, specific feedback is sent back to the agent for the next iteration.

## Creating a Rubric
A rubric is a mandatory Markdown document describing scoring criteria. It can be passed as inline text or uploaded via the Files API.

## Initiating an Outcome Session
To start work, send a `user.define_outcome` event after creating a session. The agent begins immediately without needing a separate user message.

### Max Iterations
- Default: 3
- Maximum: 20

## Monitoring Progress (Outcome Events)
- `span.outcome_evaluation_start` — Triggered when the grader begins a loop (0-indexed).
- `span.outcome_evaluation_ongoing` — A heartbeat indicating the grader is still processing.
- `span.outcome_evaluation_end` — Contains the final result and explanation.

### Evaluation Results
- `satisfied` — Criteria met; session transitions to `idle`.
- `needs_revision` — Gaps found; agent starts a new iteration cycle.
- `max_iterations_reached` — Limit hit; agent may run one final revision before idling.
- `failed` — Rubric/description contradiction; session stops.
- `interrupted` — User sent a `user.interrupt` event.

## Key Constraints
- **Max Iterations:** Capped at 20.
- **Persistence:** Sessions retain history of prior outcomes, allowing for conversational follow-ups or new outcome definitions.
- **Sequential Chaining:** Only one outcome is supported at a time.
