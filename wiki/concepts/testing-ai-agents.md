---
title: "Testing AI Agents"
created: 2026-05-10
updated: 2026-05-10
type: concept
tags: [testing, ai-agents, mcp, tool-use, evaluation]
sources:
  - raw/articles/merge.dev--blog-testing-ai-agents--8daf268c.md
---

# Testing AI Agents

AI agents require systematic testing approaches due to their non-deterministic nature and reliance on LLM tool calling.

## Core Challenges

1. **Non-determinism**: LLM responses vary between runs even with identical inputs
2. **Open-ended prompts**: Impossible to predict every scenario agents will encounter
3. **Semantic failures**: Agents can produce well-formed but incorrect outputs
4. **Exponential complexity**: Testing effort scales with agent and connector complexity

## Key Testing Measures

### Hit Rate Analysis
- **Hit rate**: Percentage of time an agent calls the correct tool for a given scenario
- Requires defining reference scenarios with expected tool calls
- Semantic equivalence checking (not just exact matches) is important
- Reveals whether MCP server tools have exhaustive, appropriate names and descriptions

### Pass/Fail Checks
- Define specific prompts and expected output labels
- Mark certain labels as passing, others as failing
- Example: "Website is down" → expected: "Create Jira issue, High Priority" = pass

### Model Change Re-testing
- Re-run all existing tests when underlying models change
- Newer models may phrase tool arguments differently or interpret instructions more loosely
- Identifies where certain models underperform (e.g., invoke wrong tools)

### Multi-Model Testing
- Test every LLM your agents might use
- Isolate potential issues by model
- Enable comparison across different model capabilities

### MCP Server Testing
- Official MCP servers often deployed with gaps (missing/inconsistent tool metadata, weak auth)
- Test against projected prompts including edge cases, malformed inputs, permission constraints
- Include adversarial scenarios (e.g., prompt injection attempts)

## Testing Tools

| Tool | Purpose |
|------|---------|
| **Merge Agent Handler** | Tests agent interaction with external APIs and tools |
| **Composio** | MCP server integration testing |
| **Arcade.dev** | API/tool call validation for agents |
| **LangChain** | Agentic workflow design and simulation |
| **CrewAI** | Multi-agent workflow debugging |
| **TruLens** | Automated evals and constraint assessment |
| **Guardrails** | Output enforcement and compliance boundaries |

## Metrics

| Metric | Description |
|--------|-------------|
| **Hit rate** | % of correct tool calls for a scenario |
| **Success rate** | % of tool calls that complete successfully |
| **Latency** | End-to-end time for agent tool call completion |

## Related
- [[concepts/agent-evaluation]]
- [[entities/merge-dev]]
- [[concepts/mcp]]
