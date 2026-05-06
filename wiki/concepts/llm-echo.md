---
title: "llm-echo"
type: concept
created: 2026-05-06
updated: 2026-05-06
status: L1
tags:
  - llm-tools
  - echo
  - simon-willison
sources:
  - https://simonwillison.net/2026/May/5/llm-echo/
---

# llm-echo 0.5a0

**llm-echo** is a plugin for [[entities/llm]] (Simon Willison's LLM CLI tool) that records and replays LLM API interactions. Released May 5, 2026 as v0.5a0.

## Core Purpose

The plugin addresses a common need in LLM development workflows: **deterministic testing and debugging**. It works by:

1. **Recording**: Captures the exact request/response pairs when calling an LLM API
2. **Replaying**: Returns the recorded response instead of making a live API call
3. **Diffing**: Compares responses across different model versions or prompts

## Use Cases

- **Prompt engineering iteration**: Test prompt changes without burning API credits
- **Model comparison**: Compare outputs from different models on the same input
- **Regression testing**: Ensure prompt changes don't break expected behavior
- **Demo preparation**: Run deterministic demos that don't depend on API availability
- **Cost reduction**: Avoid repeated API calls during development

## How It Works

The plugin intercepts LLM CLI calls, checks if a matching recording exists, and either replays it or records a fresh response. Recordings are stored as structured files (JSON/YAML) that capture the full request context including model, temperature, prompt, and response.

## Relationship to Simon's Agentic Engineering Pattern

llm-echo embodies the principle of **"evaluation first"** that Simon advocates in his [[concepts/agentic-engineering]] work. By making it cheap and easy to replay LLM interactions, it encourages systematic testing over trial-and-error development.

## Related

- [[entities/llm]] — CLI tool that llm-echo extends
- [[entities/simon-willison]] — Creator
- [[concepts/agentic-engineering]] — Evaluation-first development philosophy
- [[concepts/llm-evaluation-harness]] — Related evaluation concepts

## Sources

- [llm-echo 0.5a0 release notes](https://simonwillison.net/2026/May/5/llm-echo/)
- [llm GitHub repository](https://github.com/simonw/llm)

## References

- simonwillison.net--2026-may-5-llm-echo--6fa00161
