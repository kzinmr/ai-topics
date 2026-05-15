---
title: Randy Olson (Randal S. Olson)
created: 2026-05-14
updated: 2026-05-15
type: person
tags:
  - person
  - ai-agents
  - agent-skills
  - data-visualization
  - verification
  - developer-tooling
  - agent-evaluation
  - evolutionary-algorithms
  - evaluation
  - entrepreneur
  - open-source
  - data-science
  - researcher
aliases:
  - Randy Olson
  - Randal Olson
  - Randal S. Olson
  - Dr. Randal S. Olson
sources:
  - https://www.randalolson.com/
  - https://www.goodeyelabs.com/
  - https://www.goodeyelabs.com/insights/the-tufte-test
  - https://www.linkedin.com/in/randalolson
  - https://github.com/rhiever
  - https://x.com/randal_olson
  - https://www.randalolson.com/beautiful-charts-with-ai/
  - https://truesight.goodeyelabs.com/docs/mcp-integration
  - https://github.com/Goodeye-Labs/truesight-mcp-skills
  - https://www.randalolson.com/2026/03/06/top-tools-to-evaluate-and-benchmark-ai-agent-performance-2026/
description: "Co-Founder & CTO of Goodeye Labs. 15+ years in AI/ML. Data visualization legend, longtime r/DataIsBeautiful moderator. Creator of TPOT AutoML. Pioneer in encoding expert judgment as LLM-evaluable quality standards (Tufte Test), open-source agent skills for AI evaluation (Truesight MCP), and the generator-evaluator workflow pattern."
---

# Randy Olson (Randal S. Olson)

| | |
|---|---|
| **X** | [@randal_olson](https://x.com/randal_olson) (~112K followers) |
| **GitHub** | [rhiever](https://github.com/rhiever) |
| **LinkedIn** | [randalolson](https://www.linkedin.com/in/randalolson) |
| **Website** | [randalolson.com](https://www.randalolson.com/) |
| **Role** | Co-Founder & CTO, [[entities/goodeye-labs|Goodeye Labs]] |
| **Location** | Anacortes, WA (Pacific Northwest, USA) |
| **Known for** | TPOT AutoML, r/DataIsBeautiful moderation, Tufte Test (LLM-as-judge for data viz), Truesight MCP agent skills, generator-evaluator workflow pattern |
| **Education** | Ph.D. Computer Science & Ecology/Evolutionary Biology, Michigan State University (2015); B.S. Computer Science, University of Central Florida (2010) |
| **Publications** | 50+ peer-reviewed, ~6,600 citations, multiple patents |

## Overview

Dr. Randal "Randy" S. Olson is an AI researcher, builder, and entrepreneur with 15+ years in artificial intelligence and machine learning. He is Co-Founder and CTO of **Goodeye Labs**, where he leads product, engineering, and technical execution for [[entities/truesight|Truesight]] — an AI evaluation platform that deploys domain-expert-defined quality standards as API endpoints that any AI agent can call. His career spans evolutionary computation research, open-source AutoML, data visualization, and now frontier AI evaluation infrastructure.

Olson's central thesis is that the bottleneck in production AI is not the models themselves, but the communication gap between domain experts who know what "good" looks like and technical teams who implement AI systems. At Goodeye Labs, he builds tools that make domain experts first-class citizens in AI quality assessment.

Before Goodeye Labs, Olson was Head of AI Strategy at AE Studio, Senior AI Scientist at Absci, and founder of RO Consulting. He created **TPOT** (Tree-based Pipeline Optimization Tool), one of the most widely-used open-source AutoML frameworks (10K+ GitHub stars), and is known for viral data visualization projects including the "Optimal U.S. Road Trip" and gender distribution visualizations covered by the _New York Times_, _Washington Post_, _Wired_, and FiveThirtyEight.

## Core Ideas & Agentic Work

### Generator-Evaluator Workflow

Olson is a vocal advocate for the **generator-evaluator workflow pattern** in AI agent design. The core loop:

1. An AI agent **generates** an output (a chart, a clinical note, a legal brief)
2. An **evaluator** — typically a quality standard encoded as an API endpoint — scores the output against explicit pass/fail criteria
3. The agent **iterates** until the output passes all criteria

> "A quality standard gives an agent something a vague prompt never can: a precise list of exactly what to fix." — Olson, "The Tufte Test" (March 2026)

This pattern shifts AI quality from "prompt and pray" to systematic, measurable improvement loops. It applies anywhere domain experts can articulate what "good" looks like — data visualization, clinical documentation, legal briefs, code review, and beyond.

### The Tufte Test: Encoding Expert Judgment as LLM-Evaluable Standards

Olson's most-cited agentic work is the **Tufte Test** (March 2026), where he encoded Edward Tufte's seven core data visualization principles into a structured quality standard deployed as a Truesight API endpoint:

| Principle | Pass/Fail Condition |
|---|---|
| Data-ink ratio | Maximize data-ink; remove non-data ink |
| No 3D effects | Chart must be 2D only |
| Direct labeling | Labels on data, not in legend boxes |
| Axis readability | Clear, properly scaled axes |
| Muted purposeful color | Colors serve communication, not decoration |
| Integrated annotations | Insight callouts directly on the chart |
| Graphical integrity | No distortion of proportions |

Olson demonstrated the pattern by handing Manus the Tufte Test and a dataset. Manus generated a chart, submitted it to the API, received detailed pass/fail feedback, then autonomously iterated — replacing legend boxes with direct labels, adding annotation callouts, refining colors — until it passed all seven criteria. The entire improvement loop required only two human prompts: one to create, one to evaluate.

The Tufte Test is available as a public API endpoint and a template in Truesight. It represents a broader pattern: **encode expert judgment once, deploy as an API, and every AI agent in your stack builds against it.**

### Truesight MCP & Open Source Agent Skills

In March 2026, Olson shipped the **Truesight MCP** (Model Context Protocol integration) alongside a suite of **open-source agent skills**. These skills are step-by-step workflow playbooks that guide AI assistants through evaluation workflows:

- `evaluate-trace` — Score individual agent traces against quality criteria
- `error-analysis` — Systematic analysis of where and why agents fail
- `generate-synthetic-data` — Create test datasets for evaluation
- `review-and-promote-traces` — Human-in-the-loop review queue with audit provenance
- `bootstrap-template-evaluation` — Quick-start evaluation from templates
- `create-evaluation` — Scope quality requirements into binary pass/fail evals
- `eval-audit` — Audit historical evaluation results
- `build-review-interface` — Generate review UIs for human evaluators

The skills work with [[concepts/claude-code|Claude Code]], [[entities/cursor-ai|Cursor]], ChatGPT, VS Code, Windsurf, and any client supporting the agent skills standard. The skills package is open-source at `github.com/Goodeye-Labs/truesight-mcp-skills`.

> "Nobody ships software without tests anymore." — Olson, announcing Truesight MCP (March 6, 2026)

### "Reflect and Improve" Design Pattern

Olson's work embodies the **reflect-and-improve** agent design pattern, a specific instantiation of the broader [[concepts/reflection-pattern|Reflection Pattern]] in agentic AI. The pattern has three stages:

1. **Generate** — The agent produces an initial output
2. **Evaluate** — A quality standard (encoded as API) scores the output with specific pass/fail feedback
3. **Improve** — The agent addresses each failure, keeping what works and fixing what doesn't

Unlike generic self-reflection approaches, Olson's version ties reflection to **specific, pre-defined expert criteria** — making the improvement loop deterministic and measurable rather than open-ended. This is the key insight: reflection works best when the criteria are explicit and domain-expert-authored, not when the agent invents its own quality standards.

### "Digital Twin" Thought Partner Concept

Olson has articulated the concept of a **"digital twin" thought partner** — an AI system that encodes a domain expert's judgment so precisely that it can serve as a proxy evaluator, scaling expert oversight without requiring the expert to review every output manually.

In this framing, the quality standards deployed through Truesight act as a lightweight "digital twin" of the domain expert's judgment. The expert encodes their criteria once, and the system applies those criteria continuously — evaluating outputs, flagging failures, and guiding agents toward improvement. This is distinct from full [[concepts/digital-twins|Digital Twin]] simulations; it's a pragmatic, evaluation-focused instantiation for AI quality assurance.

### Cron Job Reports for Colleagues

As part of his applied AI automation practice, Olson builds automated cron-based reporting pipelines that monitor AI system quality and deliver structured reports to colleagues. These reports surface evaluation trends, failure patterns, and quality regressions — making AI quality visible and accountable across teams. This reflects his broader philosophy of **calm technology**: automation that reduces cognitive load and compounds over time without demanding constant attention.

## Key Projects

### TPOT: Automated Machine Learning (2015–present)

TPOT (Tree-based Pipeline Optimization Tool) is an open-source Python AutoML tool that uses genetic programming to optimize machine learning pipelines. Built on scikit-learn, it automates feature preprocessing, model selection, and hyperparameter tuning. TPOT has garnered **10,000+ GitHub stars**, **1,600+ forks**, and over **1,000 citations**.

TPOT represents Olson's deep roots in [[concepts/evolutionary-algorithms|evolutionary computation]] — applying genetic algorithms to automate ML workflow design, a precursor to today's agent-driven automation.

### Goodeye Labs & Truesight (2025–present)

Co-founded with Ege Altan, PhD (CEO), Goodeye Labs builds AI evaluation infrastructure. Truesight, the company's first product, enables:

- **No-code evaluation criteria**: Domain experts define what "good" looks like in plain language
- **Live evaluation endpoints**: Quality standards deployed as API endpoints callable by any agent or model
- **Multi-model judge support**: OpenAI, Anthropic, Google, any LiteLLM provider
- **Human review queue**: Frozen config snapshots for audit provenance
- **Systematic error analysis**: Surface patterns in where agents consistently fail
- **MCP integration**: Direct connection from AI assistants to quality standards

The company's thesis: "Intelligence is now abundant. The differentiator is taste, judgment, and business context."

### r/DataIsBeautiful Moderation (2013–present)

Olson has served as head moderator and community leader for **r/DataIsBeautiful**, one of Reddit's largest communities dedicated to data visualization, serving over **2 million unique visitors per month**. Under his stewardship, the subreddit maintains rigorous quality standards for data visualization — principles that later informed the Tufte Test.

### Optimal Road Trip Series (2015)

Olson used genetic algorithms to solve the traveling salesman problem for road trips across the U.S., Europe, South America, and individual states. The "Optimal U.S. Road Trip" — 13,699 miles hitting landmarks in all 48 contiguous states — went viral and was replicated for dozens of countries.

### Women in STEM Visualization (2014)

Olson's visualization of gender distribution across U.S. college majors from 1970–2012 surfaced the persistent engineering gap and became one of the most widely-shared data stories of the decade. This project epitomizes his approach: rigorous data analysis combined with clear, accessible visual storytelling.

## Career Timeline

| Period | Role | Organization |
|---|---|---|
| 2025–present | Co-Founder & CTO | Goodeye Labs |
| 2025–present | Co-Founder | Wyrd Studios (privacy-first AI applications) |
| 2022–present | Founder & Principal Consultant | RO Consulting |
| 2021–2022 | Senior AI Scientist | Absci |
| ~2020–2022 | Head of AI Strategy | AE Studio |
| 2015–2018 | Postdoctoral Researcher | University of Pennsylvania (with Dr. Jason H. Moore) |
| 2011–2015 | Ph.D. Candidate | Michigan State University |
| 2013–present | Head Moderator | r/DataIsBeautiful (Reddit) |

## Published Articles at Goodeye Labs

| Date | Title | Link |
|---|---|---|
| 2026-03-19 | The Tufte Test: Teaching an AI Agent to Make Better Data Visualizations | [goodeyelabs.com](https://www.goodeyelabs.com/insights/the-tufte-test) |
| 2026-03-06 | Top Tools to Evaluate and Benchmark AI Agent Performance in 2026 | [randalolson.com](https://www.randalolson.com/2026/03/06/top-tools-to-evaluate-and-benchmark-ai-agent-performance-2026/) |
| 2026-02-20 | The November 2025 AI Coding Surprise, Model by Model | [goodeyelabs.com](https://www.goodeyelabs.com/insights) |
| 2026-02-17 | Top AI Agent Evaluation Tools in 2026 | [goodeyelabs.com](https://www.goodeyelabs.com/articles/top-ai-agent-evaluation-tools-2026) |
| 2026-02-07 | The "Are You Sure?" Problem: Why Your AI Keeps Changing Its Mind | [randalolson.com](https://www.randalolson.com/) |
| 2026-01-26 | The AI Mirror Effect: Why Your AI Evaluations Need Domain Experts | [goodeyelabs.com](https://www.goodeyelabs.com/insights) |
| 2026-01-14 | Beyond the Demo: Building Reliable AI with LLM Evaluations | Portland AI Engineers talk |
| 2025-12-28 | 2025 Year in Review for LLM Evaluation: When the Scorecard Broke | [goodeyelabs.com](https://www.goodeyelabs.com/insights) |
| 2025-12-22 | Why Custom Evals Matter for Production LLMs | [randalolson.com](https://www.randalolson.com/) |
| 2025-11-25 | How to Choose the Right LLM for AI-Assisted Coding | [randalolson.com](https://www.randalolson.com/) |

## Related Entities & Concepts

- [[entities/goodeye-labs|Goodeye Labs]] — Co-founded with Ege Altan, PhD; AI evaluation infrastructure company
- [[entities/truesight|Truesight]] — Goodeye Labs' AI evaluation platform
- [[concepts/generator-evaluator-workflow|Generator-Evaluator Workflow]] — Core agent design pattern Olson advocates
- [[concepts/reflection-pattern|Reflection Pattern]] — Agent self-improvement via critique-refine loops
- [[concepts/llm-as-judge|LLM-as-Judge]] — Using LLMs to evaluate other AI outputs
- [[concepts/agent-skills|Agent Skills]] — Reusable workflow playbooks for AI assistants
- [[concepts/evolutionary-algorithms|Evolutionary Algorithms]] — Olson's Ph.D. focus area; genetic algorithms for AutoML
- [[concepts/agent-evaluation|Agent Evaluation]] — Multi-step decision chain quality assessment
- [[concepts/mcp|Model Context Protocol (MCP)]] — Protocol enabling AI agents to connect to Truesight quality standards
- [[entities/ian-nuttall]] — MCP server tooling, Claude Code agent-skills, open-source developer tools
- [[entities/ege-altan|Ege Altan]] — Co-Founder & CEO of Goodeye Labs

## X Activity Themes

- **AI evaluation infrastructure** — Shipping Truesight MCP, agent skills, and evaluation endpoints
- **Generator-evaluator patterns** — Demonstrating agent self-improvement loops with concrete quality standards
- **Data visualization** — Sharing data stories, r/DataIsBeautiful highlights, and Tufte-inspired chart design
- **Domain expert empowerment** — Arguing that subject-matter experts must drive AI quality assessment
- **Open-source agent tooling** — Publishing and maintaining TPOT, Truesight skills, and evaluation tools
- **AI coding and productivity** — Commentary on AI-assisted development tools and workflows
- **Calm technology philosophy** — Advocating for automation that reduces cognitive load and compounds over time
