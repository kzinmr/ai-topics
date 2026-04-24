---
title: "Evals Skills for Coding Agents"
type: comparison
created: 2026-04-12
tags: [evaluation, coding-agents, mcp, automation, harness-engineering]
sources:
  - "https://hamel.dev/blog/posts/evals-skills/"
  - "https://hamel.dev/blog/posts/field-guide/"
---

# Evals Skills for Coding Agents

A set of skills/plugins for AI coding agents to perform product-level AI evaluations. Published by **Hamel Husain** as [evals-skills](https://github.com/hamelsmu/evals-skills).

## Philosophy

> "Coding agents now instrument applications, run experiments, analyze data, and build interfaces. I've been pointing them at evals."

> "An agent with an eval platform still needs to know what to do with it."

The tedious parts of evaluation — instrumenting your app, orchestrating experiments, building annotation tools — now fall to coding agents. All major eval vendors (Braintrust, LangSmith, Phoenix, Truesight) ship an MCP server. **Skills complement vendor MCP servers**: those give your agent access to traces and experiments, these teach it *what to do* with them.

## Connection to Harness Engineering

OpenAI's Harness Engineering article demonstrates this approach: three engineers built a product in five months with ~1 million lines of code using Codex agents. The key insight: **improving the infrastructure around the agent mattered more than improving the model**. The agents queried traces to verify their own work.

> "Documentation tells the agent what to do. Telemetry tells it whether it worked. Evals tell it whether the output is good."

## Available Skills

| Skill | Purpose |
|-------|---------|
| **eval-audit** | Inspects current eval setup (or lack thereof), runs diagnostic checks across six areas, produces prioritized list of problems with next steps |
| **error-analysis** | Reads traces, categorizes failures, builds a vocabulary of what's broken |
| **generate-synthetic-data** | Creates diverse test inputs when real data is sparse |
| **write-judge-prompt** | Designs binary Pass/Fail LLM-as-Judge evaluators |
| **validate-evaluator** | Calibrates judges against human labels using TPR/TNR and bias correction |
| **evaluate-rag** | Evaluates retrieval and generation quality separately |
| **build-review-interface** | Generates annotation interfaces for human trace review |

## Recommended Workflow

### For Beginners
If you're new to evals or inheriting an existing eval pipeline, start with `eval-audit`:

```
Install the eval skills plugin from https://github.com/hamelsmu/evals-skills,
then run /evals-skills:eval-audit on my eval pipeline. Investigate each diagnostic
area using a separate subagent in parallel, then synthesize the findings into a
single report. Use other skills in the plugin as recommended by the audit.
```

### For Experienced Practitioners
Skip the audit and pick the skill you need directly.

## Key Insight

These skills are a **starting point** and only encode common mistakes that generalize across projects. Skills grounded in your stack, your domain, and your data will outperform them. Start here, then write your own.

## Related Concepts

- [[ai-evals]] — Main evaluation framework
- [[harness-engineering]] — OpenAI's approach to AI-assisted development
- [[llm-as-judge]] — Using LLMs to evaluate AI outputs
-  — Systematic categorization of failure modes

## Sources

- [Evals Skills for Coding Agents](https://hamel.dev/blog/posts/evals-skills/) — Hamel Husain
- [evals-skills GitHub Repository](https://github.com/hamelsmu/evals-skills)
