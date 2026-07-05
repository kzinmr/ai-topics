---
title: "Promptfoo"
type: entity
created: 2026-05-25
updated: 2026-05-26
tags:
  - promptfoo
  - evaluation
  - tool
  - testing
  - security
  - open-source
sources:
  - https://www.promptfoo.dev/
  - https://www.promptfoo.dev/docs/intro/
  - https://github.com/promptfoo/promptfoo
  - https://www.promptfoo.dev/blog/promptfoo-joining-openai/
  - raw/articles/2026-05-19_openai_macro-evals-for-agentic-systems.md
related:
  - macro-evals-for-agentic-systems
  - evals-for-ai-agents
  - evals-skills
---

# Promptfoo

**Promptfoo** is an open-source CLI and library for evaluating and red-teaming LLM applications. Founded by **Ian Webster** and **Michael D'Angelo** in 2024, it was acquired by OpenAI in 2026 and remains MIT-licensed. With 350K+ developers, 130K monthly active users, and adoption by 25%+ of the Fortune 500, it is the most widely used AI evaluation and security testing platform.

## Overview

Promptfoo is an open-source tool for developers that integrates **Evaluation** and **Red Teaming** for LLM applications. Instead of traditional "trial-and-error prompt engineering," it enables **Test-Driven LLM Development**.

| Aspect | Details |
|------|------|
| **Creators** | Ian Webster (typpo) & Michael D'Angelo |
| **Language** | TypeScript (96.7%), Python SDK |
| **License** | MIT |
| **GitHub Stars** | 19.6K |
| **Contributors** | 260 |
| **npm Weekly DL** | 302.7K |
| **First Release** | 2023-05-03 |
| **Latest Version** | v0.121.12 (2026-05-21) |
| **Releases** | 410+ |
| **Enterprise Adoption** | 156 of Fortune 500 |

## Acquisition by OpenAI

In 2026, Promptfoo was acquired by OpenAI. Terms were not disclosed, but it was explicitly stated that the **MIT open-source license would continue** and support for all providers and all models would be maintained.

- **Pre-acquisition Team**: 23 people (Engineering, GTM, Operations)
- **Investors**: Insight Partners (Ganesh Bell), a16z (Zane Lackey)
- **Post-acquisition Role**: Integrated into OpenAI's model/infrastructure layer, strengthening security and evaluation capabilities
- **Continued Development**: Surviving as both a standalone product and open-source project

## Key Features

### 1. LLM Evaluations

Runs automated evaluations of prompts, models, and RAG pipelines with YAML-based declarative configuration:

```yaml
prompts:
  - "Translate to French: {{input}}"
  - "You are a translator. Output: {{input}}"

providers:
  - openai:gpt-4o
  - anthropic:claude-sonnet-4

tests:
  - vars:
      input: "Hello world"
    assert:
      - type: contains
        value: "Bonjour"
```

- **Multi-Provider Comparison**: OpenAI, Anthropic, Azure, Google, AWS Bedrock, Ollama, HuggingFace, custom APIs
- **Auto-scoring**: Pass/Fail judgment based on rubric definitions
- **Caching & Concurrency**: High-speed execution engine
- **Live Reload**: Instant feedback during development
- **Web UI**: Matrix view for result comparison and sharing

### 2. Red Teaming

Automated security vulnerability scanning for AI applications:

- **Prompt Injection** (direct and indirect)
- **Jailbreak** (guardrail circumvention)
- **Data Leakage / PII Exposure**
- **Business Rule Violations**
- **Unsafe Agent Tool Usage**
- **Harmful Content Generation**
- Covers **50+ vulnerability types**

```bash
npx promptfoo@latest redteam setup
```

Automatically generates custom attack vectors and continuously tests in CI/CD pipelines.

### 3. CI/CD Integration

- Native integration with GitHub Actions, GitLab CI, Jenkins
- **Security Feedback in PRs**: Code scan results displayed directly in pull requests
- **Continuous Monitoring**: Security monitoring in production environments

### 4. MCP (Model Context Protocol) Support

Supports integration with MCP servers and agent frameworks.

## Architecture

```
┌──────────────────────────────────────┐
│          CLI / Library API            │
│   (npx promptfoo, Node.js, Python)   │
└────────┬─────────────────────────────┘
         │
┌────────▼─────────────────────────────┐
│        Evaluation Engine              │
│   Caching · Concurrency · Matrix     │
└──┬──────────┬───────────┬────────────┘
   ▼          ▼           ▼
┌──────┐ ┌──────────┐ ┌──────────┐
│Evals │ │Red Team  │ │Code Scan │
│Bench │ │Attack Gen│ │Static    │
└──────┘ └──────────┘ └──────────┘
         │
┌────────▼─────────────────────────────┐
│          Provider Layer               │
│ OpenAI · Anthropic · Azure · Google   │
│ Bedrock · Ollama · HF · Custom API    │
└──────────────────────────────────────┘
```

## Usage in OpenAI Macro Evals

In the [[concepts/evaluation/macro-evals-for-agentic-systems]] Cookbook, five lower-level rubrics (`final_decision_quality`, `policy_compliance_correctness`, `routing_specialist_activation`, `market_drift_awareness`, `review_appropriateness`) are implemented in Promptfoo, generating pass/fail on 1,000 synthetic traces. These lower-level signals feed into a BERTopic-style macro discovery pipeline.

## Competitors & Related Tools

| Tool | Key Difference |
|--------|---------|
| **LangSmith** | Evaluation and tracing within the LangChain ecosystem. Higher-level observability |
| **Weights & Biases** | ML experiment management focused. Prompt evaluation is secondary |
| **DeepEval** | Python-native evaluation framework. Specialized in CI/CD integration |
| **Arize AI** | Specialized in production monitoring. Development-time evaluation led by Promptfoo |
| **Custom evaluation scripts** | 10x faster feedback loop than manual implementation |

## Creators

**Ian Webster** (@typpo) — Co-founder and CEO of Promptfoo. Former engineering leader at Google and Twitter.

**Michael D'Angelo** — Co-founder of Promptfoo. Responsible for technology and product leadership.

## Community

- **Web**: [promptfoo.dev](https://www.promptfoo.dev/)
- **GitHub**: [github.com/promptfoo/promptfoo](https://github.com/promptfoo/promptfoo)
- **npm**: [npmjs.com/package/promptfoo](https://www.npmjs.com/package/promptfoo)
- **Discord**: Promptfoo Discord server
- **License**: MIT

## See Also

- [[concepts/evaluation/macro-evals-for-agentic-systems]]
- [[concepts/evaluation/evals-for-ai-agents]]
- [[concepts/evals-skills]]
