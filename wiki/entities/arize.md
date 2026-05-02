---
title: "Arize AI"
tags:
  - company
  - ai-observability
  - llm-evaluation
  - agent-monitoring
  - open-source
  - enterprise-ai
created: 2026-04-20
updated: 2026-05-02
type: entity
sources:
  - https://arize.com/
  - https://arize.com/blog/arize-ai-raises-70m-series-c-to-build-the-gold-standard-for-ai-evaluation-observability/
  - https://github.com/Arize-ai/phoenix
  - https://arize.com/author/jason-lopatecki/
  - https://www.prnewswire.com/news-releases/arize-ai-secures-70m-series-c-to-fix-ais-biggest-problem-making-llms-and-ai-agents-work-in-the-real-world-302381601.html
---

# Arize AI

**Arize AI** is an AI observability and LLM evaluation platform headquartered in Berkeley, CA. Co-founded by Jason Lopatecki (CEO) and Aparna Dhinakaran (CPO), Arize provides a unified platform for monitoring, evaluating, and improving AI agents and LLM applications in production. Their open-source project **Phoenix** has over 2M monthly downloads, making it the most widely adopted AI observability library.

Positioned as "Datadog for agents," Arize sits at the observability plane — the top layer of the 5-plane enterprise AI stack — monitoring decision quality, tracing tool use, and evaluating agent performance.

## Company Overview

| Attribute | Detail |
|-----------|--------|
| **Founded** | January 2020 |
| **Founders** | Jason Lopatecki (Co-founder & CEO), Aparna Dhinakaran (Co-founder & CPO) |
| **Headquarters** | Berkeley, CA |
| **Total Funding** | ~$131M (5 rounds) |
| **Latest Round** | $70M Series C (Feb 2025) |
| **Lead Investors** | Adams Street Partners, Battery Ventures, TCV, Foundation Capital |
| **Enterprise Backers** | M12 (Microsoft), Datadog, PagerDuty, OMERS Ventures |
| **Employees** | 101–250 |
| **Key Products** | Arize AX (Enterprise), Phoenix OSS, AI Copilot |
| **Positioning** | "Datadog for agents" — monitoring and improving AI decision quality |

## Founders

### Jason Lopatecki (Co-founder & CEO)
Second-time founder who previously co-founded TubeMogul, scaling it from garage to IPO and eventual acquisition by Adobe. Hands-on expertise in big data architectures, distributed systems, and machine learning. Holds BS in Electrical Engineering & Computer Science from UC Berkeley.

### Aparna Dhinakaran (Co-founder & CPO)
Co-founder and CPO driving product direction for Arize's observability and evaluation platform.

## Funding History

| Date | Round | Amount | Lead Investor | Notable Participants |
|------|-------|--------|---------------|---------------------|
| Feb 2025 | Series C | $70M | Adams Street Partners | M12 (Microsoft), Datadog, PagerDuty, OMERS Ventures, Sinewave Ventures, Industry Ventures, Archerman Capital; existing: Foundation Capital, Battery Ventures, TCV, Swift Ventures |
| Sep 2022 | Series B | $38M | TCV | Battery Ventures, Swift Ventures, Foundation Capital |
| Sep 2021 | Series A | $19M | Battery Ventures | Trinity Ventures, Swift Ventures, Foundation Capital |
| Feb 2020 | Seed | $4M | Foundation Capital | Array Ventures, Battery Ventures, Bloomberg Beta, M12, others |

## Product Suite

### Arize AX (Enterprise)
The leading evaluation and observability platform for AI engineers, spanning generative AI, AI agents, machine learning, and computer vision.

### Phoenix OSS
Open-source AI observability platform (GitHub: Arize-ai/phoenix, 9.5K stars). Key features:
- **Tracing** — OpenTelemetry-based distributed tracing for LLM applications
- **Evaluation** — LLM-based evaluators, code-based checks, human labels
- **Datasets & Experiments** — Versioned datasets for experimentation and fine-tuning
- **Prompt Engineering** — Version, store, deploy prompts; replay LLM calls
- **Integrations** — LlamaIndex, LangChain, DSPy, Mastra, Vercel AI SDK, OpenAI, Anthropic, Bedrock

### AI Copilot
Launched 2024 — first AI assistant for AI engineers, with 50+ built-in skills for debugging agent traces, writing evals, and optimizing prompts.

## Architecture

Built on **OpenTelemetry** (open standard) and powered by **OpenInference** (Arize's instrumentation library):

```
┌──────────────────────────────────┐
│     Arize Platform (Enterprise)   │
│   Monitoring · Evaluation · Alert │
└────────────┬─────────────────────┘
             │
┌────────────▼─────────────────────┐
│      Phoenix OSS (Self-hosted)    │
│   Tracing · Evals · Experiments   │
└────────────┬─────────────────────┘
             │
┌────────────▼─────────────────────┐
│  OpenInference Instrumentation    │
│   Python · JS · Java · Go · R     │
└────────────┬─────────────────────┘
             │
    ┌────────▼────────┐
    │  OpenTelemetry  │
    │  (OTLP Protocol) │
    └─────────────────┘
```

Framework agnostic — treats all integrations equally, enabling swap of approaches at any point.

## Why Agent Observability Is Different from APM

Traditional APM (Datadog, New Relic) monitors applications — request/response, latency, errors. Agent observability requires monitoring **decision quality**:

- **Tool use order and reasoning paths** — Which tools did the agent call, in what sequence, and why
- **Context propagation** — How context changed through the agent's decision loop
- **Evaluation metrics** — Did the agent make the right call? How do you even measure that?
- **Failure modes** — Where do agents systematically fail?

## Enterprise Customers

Serves AI/ML teams at Uber, Chime, eBay, Spotify, PepsiCo, and government agencies. Secured U.S. Air Force (AFWERX) validation.

## Relationship to Context Graphs

Agent observability and context graphs are complementary:

- **Context graphs** capture *what decisions were made and why*
- **Observability** measures *whether those decisions were good decisions*

Together they enable:
1. Full audit trail of agent reasoning (context graph)
2. Evaluation of decision quality over time (observability)
3. Closed-loop feedback — poor decisions → updated policies → better decisions

## See Also

- [[playerzero]] — AI agent startup using context graphs for production engineering.
- [[regie-ai]] — AI-native sales engagement platform using context graphs.
- [[maximor]] — AI agent startup automating finance/accounting workflows.
- [[ai-agents]] — AI agent infrastructure and frameworks.
- [[observability]] — Monitoring and evaluation of AI agent decision quality.