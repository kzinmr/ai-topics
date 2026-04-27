---
title: "Muratcan Koylan (Koylan AI)"
tags: [- context-engineering]
created: 2026-04-24
updated: 2026-04-10
type: entity
---

# Muratcan Koylan (Koylan AI)

**URL:** https://muratcankoylan.com
**Blog:** muratcankoylan.com
**Twitter/X:** @koylanai
**GitHub:** https://github.com/muratcankoylan
**Company:** Sully.ai (Member of Technical Staff, Research Team)
**Former:** 99Ravens AI (AI Agent Systems Manager), Antler (Entrepreneur in Residence)
**Location:** Toronto, ON (Remote)
**Education:** Özyeğin University — B.A. Communication Design (HCI), 2014–2020

## Overview

Muratcan Koylan is a Context Engineer and open-source contributor working at the intersection of multi-agent systems, context management, and AI persona embodiment. He currently works on the Research Team at Sully.ai, a Y Combinator-backed healthcare AI company building autonomous AI agents for hospitals, where he designs context engineering systems for clinical AI.

Koylan is best known for his open-source project **"Agent Skills for Context Engineering"** — a comprehensive collection of transferable Agent Skills for building production AI agent systems. The repository has amassed 10,000+ GitHub stars, ranked #1 on Replicate Hype, and has been cited in academic research alongside Anthropic's own work.

His career trajectory is notable: transitioning from B2B marketing (seven years across companies like Insider, Tmob, and Jonas Software) to AI engineering, becoming a self-taught developer who now builds production multi-agent systems handling 10,000+ weekly interactions. He was accepted into Antler's Winter 2026 Canada Residency with an auto-evolving Context Engineering Skills MVP before withdrawing to join Sully.ai.

Koylan's writing — particularly "The File System Is the New Database: How I Built a Personal OS for AI Agents" (2M+ views in one week) — has established him as a prominent voice in the agent architecture community. He publishes extensively on context engineering, multi-agent orchestration, and AI persona embodiment, bridging the gap between academic research and production implementation.

## Timeline

| Date | Event |
|------|-------|
| 2014–2020 | Studied Communication Design (HCI) at Özyeğin University, Istanbul |
| 2020–2021 | Marketing Associate at Insider — ran global demand gen campaigns across 25 regions, built automation, launched podcast |
| 2021–2022 | Senior Marketing Specialist at Tmob (Thinks Mobility) — scaled lead gen 40% YoY with ABM and marketing automation |
| 2022–2024 | Marketing Communications & AI Transformation at Jonas Software — built AI agents and generative workflows for marketing, led HubSpot onboarding, grew organic impressions 6x |
| 2024 | Joined 99Ravens AI as first AI hire (Prompt Designer) |
| 2024 | Promoted within 3 months to AI Agent Systems Manager |
| 2024–2026 | Built core multi-agent platform at 99Ravens AI handling 10,000+ weekly interactions using LangGraph/LangChain |
| 2025 | Began publishing Agent Skills for Context Engineering on GitHub |
| Sep 2025 | ActualCode — multi-agent system for generating personalized coding assessments (2nd place, Google Cloud Hackathon) |
| Nov 2025 | ReadWren — adaptive multi-agent literary DNA extraction system launched |
| Dec 2025 | "Agent Skills for Context Engineering" repository hits 10,000+ GitHub stars |
| Jan 2026 | Ralph Wiggum Copywriter — autonomous multi-agent copywriting loop (675+ stars) |
| Jan–Feb 2026 | Entrepreneur in Residence at Antler Winter '26 Canada Residency |
| 2026 | Joins Sully.ai as Member of Technical Staff, Research Team |
| 2026 | Cited in "Meta Context Engineering via Agentic Skill Evolution" (Peking University) alongside Anthropic |

## Core Ideas

### Context Engineering vs. Prompt Engineering

Koylan draws a sharp distinction between prompt engineering and context engineering:

> "Context engineering is the discipline of managing the language model's context window. Unlike prompt engineering, which focuses on crafting individual prompts, context engineering manages the complete state available to the language model at inference time, including system instructions, conversation history, tools, and external data."
> — Agent Skills for Context Engineering, SKILL.md

This reframing elevates context management from a tactical concern (writing better prompts) to a strategic discipline (architecting the entire information environment in which the model operates). His skill collection covers the full context lifecycle: fundamentals, degradation, compression, optimization, and filesystem-backed persistence.

### The File System Is the New Database

In his viral post "The File System Is the New Database: How I Built a Personal OS for AI Agents" (2M+ views in one week), Koylan argued that for AI agent systems, the filesystem provides a superior interface to traditional databases:

> Files are human-readable, version-controllable, and natively compatible with how LLMs process information. They don't require query languages, schema migrations, or connection pools. For agents that read and write text, the filesystem is the most natural persistence layer.

This philosophy underpins his Agent Skills architecture, where each skill is a self-contained directory with a SKILL.md file, configuration, and example implementations. The filesystem becomes both the storage mechanism and the organizational metaphor for agent capabilities.

### Personal OS for AI Agents (April 2026)

In a widely-discussed X thread on April 27, 2026, Koylan shared his vision of a "Personal OS" that coordinates AI agents, memory systems, and web access — turning your phone into a "personal brain." This concept extends his "File System Is the New Database" philosophy into a complete personal computing paradigm where AI agents are first-class citizens of the operating system, not just applications.

Key ideas:
- Your phone as a **personal brain** — not just a communication device but an extension of your cognitive capacity
- AI agents as **first-class OS citizens** — deeply integrated with the operating system rather than bolted-on apps
- **Memory systems** — persistent, structured memory that persists across sessions and agents
- **Web access** — agents that can browse, research, and interact with the web on your behalf
- **Coordination layer** — an orchestrator that manages multiple agents working on different aspects of your life

This thread connects to his broader Agent Skills philosophy and his work at Sully.ai on context engineering for clinical AI.

### Multi-Agent Orchestration Patterns

Koylan's work identifies and codifies three dominant multi-agent coordination patterns:

1. **Supervisor/Orchestrator** — Centralized control where a single agent delegates to specialized sub-agents
2. **Peer-to-Peer** — Decentralized swarm architecture where agents hand off tasks based on capability
3. **Hierarchical** — Multi-level structures for complex tasks requiring both high-level planning and low-level execution

His Agent Skills repository includes complete implementations and decision frameworks for choosing between these patterns based on task complexity, latency requirements, and reliability needs.

### AI Persona Embodiment

At 99Ravens AI, Koylan built a "Persona Layer" that codified expert heuristics and evaluation rubrics for predictable, auditable outputs. This work went beyond simple prompt templates — it involved creating structured persona definitions that agents could load, switch between, and reason about.

The Ralph Wiggum Copywriter project extended this concept: an autonomous multi-agent system that learns a user's voice, critiques its own work, and rewrites until the output matches the desired persona. This represents a significant step toward agents that can adopt and maintain consistent personalities across sessions.

### Defense-in-Depth for Agent Prompts

After discovering a meta-discussion jailbreak at 99Ravens AI, Koylan designed a five-layer prompt defense system:

1. **Instruction precedence** — establishing hierarchy between system, developer, and user instructions
2. **Meta-request gating** — preventing agents from modifying their own instructions
3. **Hard deny-list** — explicit forbidden operations
4. **Tool protocols** — structured access controls for agent tools
5. **Rationale policies** — requiring agents to justify their actions before execution

This work was published as part of his internal guidance on prompt security and has been incorporated into the Agent Skills repository.

### State-Dependent Reasoning Chains

Koylan's writing on state-dependent reasoning describes how agent behavior should vary based on the current context state. Rather than using static prompts, agents should dynamically compose their reasoning process based on available context, detected patterns, and task requirements. This connects to his broader context engineering philosophy — the agent's reasoning should be as adaptive as its context management.

## Key Quotes

> "Context engineering is the discipline of managing the language model's context window."
> — Agent Skills for Context Engineering

> "The file system is the new database."
> — "The File System Is the New Database" (2M+ views)

> "I design context engineering systems for clinical AI."
> — muratcankoylan.com

> "For agents that read and write text, the filesystem is the most natural persistence layer."
> — muratcankoylan.com

> "Self-taught coder who transitioned through LLM-powered automation."
> — GitHub profile

## Key Projects

### Agent Skills for Context Engineering (10,000+ GitHub stars)
A comprehensive, open-source collection of Agent Skills for building production-grade AI agent systems. Includes foundational skills (context-fundamentals, context-degradation, context-compression, context-optimization), architectural skills (multi-agent-patterns, memory-systems, tool-design), and operational skills (evaluation, filesystem-context, hosted-agents). Cited in academic research alongside Anthropic.

### Ralph Wiggum Copywriter (675+ GitHub stars)
A Claude Code plugin that runs an autonomous multi-agent copywriting loop. Learns your voice, critiques its own work, and rewrites until it's actually good. Demonstrates persona embodiment in production.

### ReadWren (Nov 2025)
An adaptive multi-agent system that extracts literary DNA through conversation and generates actionable reading profiles. Built with LangGraph and Kimi K2.

### ActualCode (2nd place, Google Cloud Hackathon)
Multi-agent system that analyzes GitHub repositories and generates personalized, realistic coding assessments using Google's A2A protocol.

### Feed2Context
Chrome extension that converts social media posts into structured research reports for AI agent consumption.

### AI Investigator (650+ GitHub stars)
Autonomous research pipeline using Firecrawl and Claude for enterprise AI case studies.

## Recognition

- **10,000+ GitHub stars** on Agent Skills for Context Engineering
- **#1 on Replicate Hype** for Agent Skills repository
- **Cited in academic research** alongside Anthropic (Peking University, "Meta Context Engineering via Agentic Skill Evolution," 2026)
- **Featured in:** Ben's Bites, TLDR AI, LangChain, The Neuron, Zapier Blog
- **"The File System Is the New Database":** 2M+ views in one week
- **AI Developer Ambassador** at MiniMax
- **Speaker:** Context Engineering Presentation at Toronto B2B Marketing Community
- **Podcast guest:** "AI Career Journey from Turkey to Canada" on Sonraki Adım Podcast

## Related Concepts

- [[concepts/context-engineering]] — Koylan's primary discipline and focus area
- [[concepts/multi-agent-systems]] — His core architectural expertise
- [[concepts/harness-engineering/system-architecture/agent-skills]] — His open-source skill collection
- [[concepts/file-system-as-database]] — His persistence philosophy
- [[concepts/ai-persona-embodiment]] — His work on consistent agent personalities
- [[concepts/personal-os-for-ai-agents]] — His Personal OS vision for AI agents
- [[concepts/defense-in-depth]] — His defense-in-depth approach to agent safety
- [[concepts/langgraph]] — His preferred orchestration framework
- [[concepts/clinical-ai]] — His current domain at Sully.ai

## Sources

- Personal website: https://muratcankoylan.com
- Agent Skills repo: https://github.com/muratcankoylan/agent-skills-for-context-engineering
- Resume: https://muratcankoylan.com/resume/
- For Agents page: https://muratcankoylan.com/for-agents
- Twitter/X: @koylanai
- GitHub: https://github.com/muratcankoylan
- Peking University paper citing his work: "Meta Context Engineering via Agentic Skill Evolution" (2026)
- Playbooks.com skill listing: https://playbooks.com/skills/muratcankoylan/agent-skills-for-context-engineering
