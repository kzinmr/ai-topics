---
title: "Execution Plans"
tags: []
created: 2026-04-13
updated: 2026-05-27
type: concept
---

# Execution Plans

A pattern where agents create a plan before executing tasks. Separating planning from execution improves transparency, reproducibility, and debuggability.

## Core Concept

```
User Request → Agent generates Plan → Human reviews (optional) → Agent executes Plan → Results
```

The plan clarifies the agent's intent and provides a checkpoint where users can intervene.

## Plan Structure

A good execution plan includes:

1. **Objective**: Clear definition of the goal to achieve
2. **Steps**: Ordered execution steps
3. **Dependencies**: Relationships between steps
4. **Tool Requirements**: Tools/resources needed for each step
5. **Success Criteria**: Completion criteria for each step
6. **Rollback Strategy**: Recovery procedures on failure

## Benefits

### 1. Transparency

- Users can understand the agent's intent
- Plans and results can be compared during debugging
- Functions as an audit trail

### 2. Error Handling

- Obvious problems can be detected during planning
- Easy to verify completion of each step
- Partial failures can be designed for recovery

### 3. Iteration

- Plans can be reused and modified easily
- Applicable to similar tasks
- Plan improvement through learning

## Implementation

### Implicit Planning

The agent plans internally (invisible to the user):
- Implicit step decomposition for complex tasks
- Optimization of tool call ordering

### Explicit Planning

Present the plan to the user for approval:
```
> I'll need to:
> 1. Read the current config file
> 2. Update the database schema
> 3. Run migrations
> 4. Restart the service
> 
> Should I proceed? [y/n]
```

### Stored Plans

Persist plans for reuse:
- Save as workflows
- Template-ize for customization

## Related

- [[concepts/agent-loop-orchestration]] — Agent Loop Orchestration
- [[concepts/gpt/symphony]] — OpenAI Symphony (WORKFLOW.md-driven)
- [[concepts/harness-engineering/agentic-workflows/compound-engineering-loop]] — Compound Engineering Loop
- [[concepts/closing-agent-loop]] — Closing the Agent Loop
