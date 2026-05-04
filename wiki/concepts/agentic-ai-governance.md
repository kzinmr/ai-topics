---
title: "Agentic AI Governance"
type: concept
tags:
  - concept
  - governance
  - ai-agents
  - security
  - enterprise
  - safety
status: complete
description: "Frameworks for governing autonomous AI agents in enterprise — identity-based access, three-tiered guardrails, HITL/HOTL patterns, and regulatory alignment."
created: 2026-05-04
updated: 2026-05-04
sources:
  - raw/articles/2026-05-02_yale-celi-agentic-ai-governance-framework.md
related:
  - "[[concepts/agent-governance]]"
  - "[[concepts/ai-safety]]"
  - "[[concepts/agentic-security]]"
  - "[[concepts/agent-iam]]"
  - "[[entities/anthropic]]"
---

# Agentic AI Governance

Governance frameworks for autonomous AI agents — managing risk, identity, and compliance as AI systems transition from passive assistants to proactive digital workers.

## The Shift: Generative → Agentic

Traditional Generative AI responds to prompts; **Agentic AI** possesses agency — the ability to plan, use tools, and execute multi-step workflows autonomously. This shift introduces new governance challenges that static policies cannot address.

- **Economic scale**: McKinsey projects agentic automation will add **$2.6–4.4 trillion annually** to the global economy
- **Operational difference**: An agentic system can autonomously process a refund, update inventory, and notify the customer — without human intervention

## Key Risk Vectors

### Excessive Agency
When autonomous agents perform damaging actions (modifying databases, executing financial transactions) in response to unexpected outputs — a vulnerability category in OWASP Top 10 for LLM Applications.

### Indirect Prompt Injection
Malicious instructions hidden in web content can manipulate agents into exfiltrating sensitive data.

### Regulatory Tension
The **EU AI Act** mandates "effective human oversight" for high-risk systems, creating friction with full autonomy goals.

## Governance Frameworks

### Three-Tiered Guardrail System (EWSolutions / Yale CELI)

| Tier | Scope | Examples |
|------|-------|----------|
| **Foundational** | Non-negotiable standards applied universally | Privacy, transparency, basic security |
| **Risk-Based** | Adjustable controls per application | Stricter review for customer-facing vs. internal agents |
| **Societal** | Ethical alignment | Bias mitigation, fairness |

### Human Oversight Models
- **Human-in-the-Loop (HITL)**: Required for high-risk decisions (healthcare, finance) — human must approve every action
- **Human-on-the-Loop (HOTL)**: Agents act autonomously; humans review logs retrospectively for lower-risk tasks

### Identity & Access
Treat agents as distinct digital identities. Enforce **least-privilege principles** — agents only access data required for specific tasks. See [[concepts/agent-iam]].

### Compliance Standards
- **ISO/IEC 42001**: AI management system standard for documenting oversight and demonstrating control to regulators

## Strategic Framework for Enterprise Leaders

| Step | Action | Description |
|------|--------|-------------|
| 1 | **Risk Maturity Assessment** | Gap analysis of risk teams' understanding of autonomous system behaviors |
| 2 | **Define Rules of Engagement** | Cross-functional councils codifying ethical dilemmas into system logic |
| 3 | **Continuous Monitoring** | Real-time dashboards tracking agent actions, flagging anomalies |

## 2026 Context

The Yale Chief Executive Leadership Institute (CELI) published its governance framework in May 2026, triggered partly by [[entities/anthropic|Anthropic]]'s [[entities/claude-mythos|Mythos]] model exposing a "crisis in corporate governance" — demonstrating that AI capabilities are outpacing organizational readiness for oversight.

Enterprise vendors (e.g., Appier) report blocking 80% of risky agent responses through self-monitoring.

## Related
- [[concepts/agent-governance]] — Broader agent governance concepts
- [[concepts/ai-safety]] — AI safety research and frameworks
- [[concepts/agentic-security]] — Security patterns for agent systems
- [[concepts/agent-iam]] — Identity and access management for agents
- [[concepts/agent-identity-verification]] — Verifying agent identities
