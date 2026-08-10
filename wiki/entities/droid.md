---
title: Droid (Factory)
type: entity
aliases: [factory-droid, factory-ai, factory-droid-cli]
created: 2026-05-07
updated: 2026-08-10
status: L3
tags:
  - entity
  - coding-agent
  - company
  - developer-tooling
  - ai-agents
sources:
  - https://github.com/Factory-AI/factory
  - https://factory.ai/
  - https://docs.factory.ai/pricing
  - https://docs.factory.ai/integrations/github-app
  - https://docs.z.ai/devpack/tool/droid
  - https://factory.ai/product/cli
  - https://factory.ai/product/ide
  - https://x.com/0xsero/status/2040445532171108375
  - raw/articles/2026-06-15_factory-ai_software-factory-2.0.md
  - raw/articles/2026-06-03_factory_factory-router.md
  - raw/articles/2026-07-02_factory_droid-shield-2-0.md
  - raw/articles/2026-05-21_factory_deferred-context-engine.md
  - raw/articles/2026-05-16_factory_lumetric.md
  - raw/articles/2026-06-12_factory_automated-security-review.md
  - raw/articles/2026-05-10_factory_announcing-our-5m-fundraise.md
related:
  - "[[entities/claude-code]]"
  - "[[entities/copilot-cli]]"
  - "[[entities/opencode]]"
  - "[[entities/codex]]"
  - "[[concepts/agent-harnesses]]"
  - "[[concepts/context-engineering/context-management]]"
---

# Droid (Factory)

> **Droid** is Factory's enterprise-grade AI coding agent that lives across your terminal, IDE, Slack, Linear/Jira, and CI/CD pipelines. The "agent-native development platform" — top-performing in terminal benchmarks, with specialized sub-agents (CodeDroid, Review Droid, QA Droid) for the full SDLC. In June 2026 Factory expanded the vision beyond individual coding agents to the **Software Factory** — an interconnected, agent-native, end-to-end system covering the entire SDLC feedback loop.

## Basic Information

| Field | Details |
|---|---|
| Developer | Factory AI (San Francisco; offices in London, New York, Sydney) |
| Repository | [Factory-AI/factory](https://github.com/Factory-AI/factory) (placeholder; product is closed-source) |
| Official Site | [factory.ai](https://factory.ai) |
| Initial Release | 2025 |
| Supported Environments | CLI, Desktop (Mac/Windows), Web, Mobile, VS Code, JetBrains, Vim, Zed, Slack/Teams, Linear/Jira |
| Pricing | Free tier / Pro $20/mo / Team $50/mo / Enterprise custom |
| X/Twitter | [@FactoryAI](https://x.com/FactoryAI) |
| Founding | 2023; $5M seed from Sequoia + Lux (Nov 2023) |
| Enterprise customers | NVIDIA, EY, Adobe, Palo Alto Networks, Adyen, Blackstone, Wipro, Comarch, You.com, Groq, Chainguard, Podium |

## Key Features

### Specification Mode
- Press **Shift+Tab** to activate
- Describe features in plain language
- Get automatic planning before implementation
- Approve plans before any code changes

### Auto-Run Mode (3 levels)
| Level | Permissions | Use Case |
|-------|-------------|----------|
| **Low** | Edits and read-only commands | Safe exploration |
| **Medium** | Reversible commands (package installs, builds, git) | Development |
| **High** | All commands except explicitly dangerous | Autonomous execution |

### Multi-Platform Presence
- **CLI** — Terminal-native with slash commands, custom sub-agents, native diff viewing
- **IDE** — Works across VS Code (forks), JetBrains, Vim, Zed (ACP support)
- **Slack/Teams** — In-chat agent invocation for incident response
- **Linear/Jira** — Auto-trigger from issue assignment, implement + create PRs
- **Desktop/Web** — Full standalone app

### Enterprise Features
- SOC-2 compliant
- SSO/SAML
- Dedicated compute
- Compliance auditing
- Cost tracking with `/cost` command
- MCP (Model Context Protocol) support

### Droid Sub-Agent Ecosystem
- **CodeDroid** — Implementation agent
- **Review Droid** — Automated code review (GitHub/GitLab PRs)
- **QA Droid** — Testing agent
- **Custom sub-agents** — Via `/install-code-review`, droid-factory packages

### CI/CD Integration
- **Droid Action** — AI-powered code reviews, security scans, PR descriptions on GitHub Actions
- **Massively parallel execution** — Launch hundreds of agents with single command
- **Self-healing builds** — Agents diagnose failures and fix tests
- **JSON event streams** — Full observability for every automated task

## Model Support

| Models | How |
|--------|-----|
| Claude, GPT, Gemini | Default premium models |
| **Droid Core** (open-weight) | Free pool — smaller models for cost efficiency |
| **BYOK** | Bring your own API keys |
| Any model per task | Switch based on performance or cost |

## 0xSero's Assessment — #1 for Local Models

From 0xSero's ranking of best harnesses for local models (April 4, 2026):

> **1. Droid:**
> - Very good performance, forces the models to behave, you can wire in all your local LLMs very easily with BYOK
> - Allows you to use your local models as orchestrators/subagents so you can benefit from Cloud models as well
> - Practically everything you need is already in Droid
> - **"This is my daily driver, I use Qwen3.5 models in it very happily"**

This endorsement positions Droid as the **top-tier choice for local model users**, especially those who want to hybridize local + cloud models in a single workflow.

### Local Model Differentiators
- **BYOK** — Wire in local LLMs (Ollama, LM Studio, etc.) alongside premium APIs
- **Hybrid orchestration** — Use local models as orchestrators/sub-agents while leveraging cloud models for heavy lifting
- **Qwen 3.5 Coder 32B** — Confirmed working well via local setup
- **"Forces models to behave"** — Droid's structure keeps even weaker local models on track

## Pricing

| Plan | Price | Key Features |
|------|-------|-------------|
| Free | $0 | Basic usage, Droid Core models |
| Pro | $20/mo | Desktop/CLI/SDK, cloud background agents, usage tracking |
| Team | $50/mo | Team features, shared billing |
| Enterprise | Custom | SOC-2, SSO, dedicated compute, compliance |

**Droid Core**: Free pool of leading open-weight models that kick in when premium model rate limits are exhausted.

## Software Factory Vision (Factory 2.0, June 2026)

In June 2026 Factory announced the **Software Factory** ([raw article](raw/articles/2026-06-15_factory-ai_software-factory-2.0.md)) — the strategic shift from "coding agents" to an interconnected, agent-native, end-to-end system. The framing: *"Improving the productivity of individual engineers is no longer enough. Unlocking organization-wide productivity requires an interconnected, agent-native, end-to-end system."*

The software factory is a continuous feedback loop: external signals (bug reports, customer feedback, business requirements) → triage → planned changes → build → test → review → secure → ship → monitor → new signals.

Three pillars:

| Pillar | Description |
|--------|-------------|
| **Model Independence** | Deliberately choose different models per task, or rely on the Router to auto-select the best model. No one model fits every enterprise need. |
| **Sovereign Intelligence** | Fully hosted, BYOK, self-hosted data plane, EU-specific, or air-gapped. The system learns from itself — every session, review, and incident feeds back into the loop, and that capability stays inside the enterprise. |
| **Continual Learning / Self-Improvement** | All SDLC stages share the same agent core, model router, and organizational context — a security finding informs code review, a deployment triggers doc updates, an incident correlates with its PR. |

Production deployments cited: NVIDIA, EY, Adobe, Palo Alto Networks, Adyen, Blackstone, Wipro, Comarch. Autonomy is rolled out gradually per organization readiness (Shadow → Draft → Assisted → Full, echoing [[entities/antoine-buteau|Buteau's]] launch strategy).

## Factory Router (June 2026)

**Factory Router** ([raw article](raw/articles/2026-06-03_factory_factory-router.md)) is an automatic model-selection layer that cuts token spend **20–25% while maintaining frontier performance**:
- **Terminal-Bench 2**: 99% of Claude Opus 4.7's pass rate at **20% lower cost per session**
- **Legacy-Bench**: 96% of Opus 4.7's pass rate at **25% lower cost per session**
- Routes across providers if an endpoint degrades; rule-based or automatic selection
- In private research preview as of June 2026; supports the model-independence pillar of the Software Factory

## Droid Shield 2.0 (July 2026)

**Droid Shield 2.0** ([raw article](raw/articles/2026-07-02_factory_droid-shield-2-0.md)) is learned secret detection that augments the deterministic scanner. When Droids commit autonomously at enterprise volume, deterministic scanning suffers from false positives (placeholders, examples, fixtures) and false negatives (real secrets not matching fixed patterns). Shield 2.0 adds two fine-tuned models flanking the deterministic scanner:

| Gate | Role | Model |
|------|------|-------|
| **Risk** | Runs when scanner did *not* fire — catches real secrets the scanner missed | Fine-tuned Qwen 3.6 35B A3B, rank-16 LoRA |
| **Downgrade** | Runs on scanner hits — decides whether a flagged line is a real secret or false alarm | Fine-tuned Qwen 3.6 35B A3B, rank-64 LoRA |

**Results** (repo-level holdout, trained on Samsung's CredData benchmark):
- **Risk gate at FPR ≤ 0.05**: fine-tuned LoRA recall 0.698 vs GPT-5.5 0.588 and Opus 4.8 0.574 (non-overlapping 95% CIs)
- **Risk gate at FPR ≤ 0.10**: LoRA 0.878, statistically tied with Opus 4.8 (0.852), ahead of GPT-5.5 (0.707)
- **Downgrade gate at λ=5**: LoRA recall 0.856 vs GPT-5.5 0.800, Opus 4.8 0.767

Both adapters are **open-weight** on Hugging Face (`factoryai/shield-risk-r16-c15`, `factoryai/shield-dg-r64-c15`) — a deliberate contribution to open software security. Currently in research preview.

## Deferred Context Engine (May 2026)

The **Deferred Context Engine** ([raw article](raw/articles/2026-05-21_factory_deferred-context-engine.md)) addresses context bloat from MCP/skill/plugin proliferation. Instead of loading every tool schema and skill instruction into every prompt, Droid keeps a compact capability index (names, short descriptions, hints) and defers full schemas until a task needs them — progressive disclosure for tooling.

**Production telemetry** (first 5 days):
- **15.1% average input-token reduction** across measured turns with MCP tools
- **39.4% p90 reduction**; **50.8% average reduction** in sessions with 100+ hidden deferred tools
- Enterprise MCP stacks (~330 public tools ≈ 47K schema tokens) become affordable to keep reachable

This is the harness-side complement to [[concepts/context-engineering/context-management]]: keep the full context graph reachable, but only pay for what the current task loads.

## Company Timeline

| Date | Event |
|------|-------|
| 2023 | Factory founded; $5M seed from Sequoia + Lux (Nov 2023) |
| 2025 | Droid launched across CLI/IDE/Slack/Linear/CI surfaces |
| 2026-04-22 | **Droid Computers** — cloud session sync; sessions available from any browser at app.factory.ai |
| 2026-05-15 | **Acquires Lumetric** (raw: 2026-05-16_factory_lumetric.md) |
| 2026-05-20 | **Deferred Context Engine** announced (research) |
| 2026-06-01 | **Factory Router** announced (research preview) |
| 2026-06-08 | **Marcello Gallo** appointed Chief Revenue Officer |
| 2026-06-10 | **Sydney office** expansion |
| 2026-06-11 | **Automated Security Review** product launch |
| 2026-06-15 | **Factory 2.0 / Software Factory** vision announced |
| 2026-06-17 | **AutoWiki** — automated documentation product |
| 2026-07-01 | **Droid Shield 2.0** learned secret detection (research preview) |
| 2026-07-10 | **Incident Response** — Droid turns Slack alerts into autonomous incident handling |
| 2026-07-28 | Joins the **Open Secure AI Alliance** |
| 2026-08-03 | **Enterprise Organization Model** — centralized governance with org boundaries for access, integrations, policy, spend, data residency |
| 2026-08-04 | Signs the **Open Weights and American AI Leadership** letter (with Microsoft, NVIDIA, 230+ orgs) |

## Positioning

Factory positions Droid as the **most comprehensive agent-native platform** — covering the entire SDLC from IDE to CI/CD, with special attention to enterprise requirements. Unlike Claude Code (single-surface CLI) or Copilot CLI (GitHub-only), Droid aims to be everywhere developers work.

**Key differentiator**: Multi-agent architecture (specialized Droids per task type) rather than one monolithic agent — plus the 2026 platform layer (Router, Shield, Deferred Context, Software Factory) that turns individual sessions into an organization-wide, self-improving system.

## Related

- [[entities/claude-code]] — primary competitor (terminal-first)
- [[entities/copilot-cli]] — GitHub-native competitor
- [[entities/opencode]] — open-source terminal agent
- [[entities/codex]] — OpenAI's terminal agent
- [[entities/antoine-buteau]] — automation launch-strategy framework echoed by Factory's gradual autonomy rollout
- [[concepts/agent-harnesses]] — harness engineering context
- [[concepts/context-engineering/context-management]] — Deferred Context Engine as context-management practice

## Sources

- [factory.ai](https://factory.ai) — product site
- [docs.factory.ai](https://docs.factory.ai) — documentation
- [Factory News](https://factory.ai/news) — company announcements (Software Factory 2.0, Router, Shield 2.0, Deferred Context, timeline items)
- [GitHub: Factory-AI](https://github.com/Factory-AI) — open-source releases (Shield models on Hugging Face: `factoryai/shield-risk-r16-c15`, `factoryai/shield-dg-r64-c15`)
- 0xSero harness ranking for local models (Apr 2026) — Droid ranked #1 for BYOK/local model workflows
