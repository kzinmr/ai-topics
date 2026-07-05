---
title: "Muratcan Koylan"
handle: "@koylanai"
created: 2026-05-17
updated: 2026-05-17
type: entity
tags:
  - person
  - context-engineering
  - open-source
  - ai-agents
aliases: ["muratcan-koylan", "koylan-ai", "koylanai"]
sources:
  - https://muratcankoylan.com
  - https://github.com/muratcankoylan
  - https://x.com/koylanai
related:
  - riley-walz
  - peoplereadmes
  - context-engineering
  - agent-skills
---

# Muratcan Koylan (@koylanai)

| | |
|---|---|
| **X** | [@koylanai](https://x.com/koylanai) |
| **Website** | [muratcankoylan.com](https://muratcankoylan.com) |
| **GitHub** | [muratcankoylan](https://github.com/muratcankoylan) |
| **Role** | Context Engineer, Research Team at Sully.ai |
| **Former** | AI Agent Systems Manager at 99Ravens AI; Entrepreneur in Residence at Antler |
| **Location** | Toronto, ON, Canada |
| **Education** | B.A. Communication Design (HCI), Özyeğin University (2014–2020) |
| **Known for** | Agent Skills for Context Engineering (15.6k GitHub stars), peoplereadmes, Personal Brain OS |
| **Bio** | Context engineer and open-source contributor working on multi-agent systems, context management, and AI persona embodiment. Self-taught developer who transitioned from 7 years in B2B marketing to building production AI systems. Currently building context engineering systems for clinical AI at Sully.ai. |

## Overview

Muratcan Koylan is a context engineer and open-source contributor at the forefront of agent architecture design. His work centers on a single insight: **context engineering is more important than prompt engineering**. While prompt engineering focuses on crafting individual prompts, context engineering manages the complete state available to the language model at inference time — system instructions, conversation history, tools, external data, and the filesystem itself.

Koylan's career trajectory is itself a case study in AI-assisted transformation. After seven years in B2B marketing (Insider, Tmob, Jonas Software), he taught himself to code by automating his own marketing workflows with LLMs. Within three years, he was designing production multi-agent systems handling 10,000+ weekly interactions at 99Ravens AI, and his open-source work has been cited in academic research alongside Anthropic.

He currently works on the Research Team at **Sully.ai**, a Y Combinator-backed healthcare AI company, where he designs context engineering systems for clinical AI agents — including AI Scribe, a multi-agent, multi-modal clinical system.

## Core Ideas

### Context Engineering as a Discipline

Koylan draws a sharp distinction between prompt engineering and context engineering:

> "Context engineering is the discipline of managing the language model's context window. Unlike prompt engineering, which focuses on crafting individual prompts, context engineering manages the complete state available to the language model at inference time."

This reframing elevates context management from a tactical concern to a strategic discipline. His Agent Skills repository covers the full context lifecycle: fundamentals, degradation, compression, optimization, and filesystem-backed persistence.

### The File System Is the New Database

In his viral essay "The File System Is the New Database: How I Built a Personal OS for AI Agents" (2M+ views in its first week), Koylan argued that for AI agent systems, the filesystem provides a superior interface to traditional databases:

- Files are human-readable, version-controllable, and natively compatible with how LLMs process information
- No query languages, schema migrations, or connection pools required
- For agents that read and write text, the filesystem is the most natural persistence layer

### Personal Brain OS

Koylan built **Personal Brain OS** — a file-based personal operating system living inside a Git repository with 80+ files in markdown, YAML, and JSONL. The system uses a three-level **Progressive Disclosure** architecture:

1. **Level 1**: Lightweight routing file always loaded — tells the AI which module is relevant
2. **Level 2**: Module-specific instructions (40-100 lines each) loaded only when that domain is needed
3. **Level 3**: Actual data files (JSONL logs, YAML configs) loaded only when the task requires them

Eleven isolated modules manage: Personal Brand, Content Creation, Knowledge Base, Network, Operations, and more. The agent instruction hierarchy spans three layers: `CLAUDE.md` (repo-level onboarding), `AGENT.md` (core rules + decision table), and module-specific instruction files.

### Multi-Agent Orchestration Patterns

Koylan's work identifies three dominant coordination patterns:

1. **Supervisor/Orchestrator** — Centralized control with delegation to specialized sub-agents
2. **Peer-to-Peer** — Decentralized swarm where agents hand off tasks based on capability
3. **Hierarchical** — Multi-level structures for complex tasks requiring both high-level planning and low-level execution

### AI Persona Embodiment

At 99Ravens AI, Koylan built a "Persona Layer" that codified expert heuristics and evaluation rubrics for predictable, auditable outputs. This work extended beyond simple prompt templates to structured persona definitions that agents could load, switch between, and reason about. The peoplereadmes project (see below) is the open-source evolution of this work.

### Defense-in-Depth for Agent Prompts

After discovering a meta-discussion jailbreak at 99Ravens AI, Koylan designed a five-layer prompt defense system:

1. Instruction precedence — hierarchy between system, developer, and user instructions
2. Meta-request gating — preventing agents from modifying their own instructions
3. Hard deny-list — explicit forbidden operations
4. Tool protocols — structured access controls
5. Rationale policies — requiring agents to justify actions before execution

## Key Projects

### Agent Skills for Context Engineering (15.6k+ GitHub stars)
A comprehensive, open-source collection of Agent Skills for building production-grade AI agent systems. Includes foundational skills (context-fundamentals, context-degradation, context-compression, context-optimization), architectural skills (multi-agent-patterns, memory-systems, tool-design), and operational skills (evaluation, filesystem-context, hosted-agents). Cited in academic research from Peking University alongside Anthropic. Ranked #1 on Replicate Hype.

### peoplereadmes (2026)
An open-source framework for creating structured "persona context systems" to study how exceptional technical builders operate. NOT for impersonation. Pipeline: public evidence → source map → project analysis → tacit-knowledge extraction → technical model → prompt system → eval rubric → reusable context package. First persona: [[entities/riley-walz]]. See [[concepts/peoplereadmes]] for full concept page.

### Personal Brain OS
File-based personal operating system for AI agents using progressive disclosure architecture. 80+ files across 11 modules. Uses `CLAUDE.md` → `AGENT.md` → module instructions hierarchy.

### Ralph Wiggum Copywriter (675+ GitHub stars)
A Claude Code plugin that runs an autonomous multi-agent copywriting loop. Learns your voice, critiques its own work, and rewrites until the output matches the desired persona.

### ReadWren
An adaptive multi-agent system that extracts literary DNA through conversation and generates actionable reading profiles. Built with LangGraph and Kimi K2.

### AI Investigator (650+ GitHub stars)
Autonomous research pipeline using Firecrawl and Claude for enterprise AI case studies.

### Other Projects
- **ActualCode** — Multi-agent system for generating personalized coding assessments (2nd place, Google Cloud Hackathon)
- **Feed2Context** — Chrome extension converting social media posts into structured research reports for AI agent consumption
- **The-Rosetta-Prompt** — Prompt translation and adaptation system
- **Food-tour-planner-agent** — Multi-agent food tour planning system

## Recognition

- **15.6k+ GitHub stars** on Agent Skills for Context Engineering
- **Cited in academic research** alongside Anthropic (Peking University, "Meta Context Engineering via Agentic Skill Evolution," 2026)
- **"The File System Is the New Database"** — 2M+ views in one week
- **Featured in**: Ben's Bites, TLDR AI, LangChain, The Neuron, Zapier Blog
- **MiniMax Developer Ambassador** — Early access to MiniMax M2's Interleaved Thinking
- **2nd place**, Google Cloud × AI Tinkerers Hackathon

## Career Timeline

| Date | Event |
|------|-------|
| 2014–2020 | Studied Communication Design (HCI) at Özyeğin University, Istanbul |
| 2020–2021 | Marketing Associate at Insider — global demand gen across 25 regions |
| 2021–2022 | Senior Marketing Specialist at Tmob — scaled lead gen 40% YoY |
| 2022–2024 | Marketing Communications & AI Transformation at Jonas Software — built AI agents, grew organic impressions 6x |
| 2024 | Joined 99Ravens AI as first AI hire; promoted to AI Agent Systems Manager within 3 months |
| 2024–2026 | Built core multi-agent platform handling 10,000+ weekly interactions |
| Dec 2025 | Agent Skills for Context Engineering hits 10k+ GitHub stars |
| Jan–Feb 2026 | Entrepreneur in Residence at Antler Winter '26 Canada Residency (withdrew to join Sully.ai) |
| 2026–Present | Context Engineer, Research Team at Sully.ai |

## Related Pages

- [[entities/riley-walz]] — First subject of the peoplereadmes framework
- [[concepts/peoplereadmes]] — Koylan's open-source persona context systems framework
- [[concepts/context-engineering|Context Engineering]] — His primary discipline
- [[concepts/agent-skills]] — His open-source skill collection
- [[concepts/evaluation/llm-as-judge-skills]] — His evaluation skills (part of Agent Skills repo)

## Sources

- [muratcankoylan.com](https://muratcankoylan.com)
- [GitHub: muratcankoylan](https://github.com/muratcankoylan)
- [Agent Skills for Context Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering)
- [peoplereadmes](https://github.com/muratcankoylan/peoplereadmes)
- [@koylanai on X](https://x.com/koylanai)
- "The File System Is the New Database: How I Built a Personal OS for AI Agents" (Feb 2026)
- "Meta Context Engineering via Agentic Skill Evolution" — Peking University (2026)
