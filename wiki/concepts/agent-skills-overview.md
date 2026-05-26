---
title: "Agent Skills Overview — Concept Cluster Map"
created: 2026-05-15
updated: 2026-05-26
type: concept
tags:
  - agent-skills
  - skill-graph
  - ai-agents
  - harness-engineering
  - context-engineering
  - developer-tooling
aliases:
  - agent-skills-overview
  - skills-overview
  - skills-concept-cluster
status: active
---

# Agent Skills Overview — Concept Cluster Map

Agent Skills is the concept of "packaging reusable knowledge, procedures, and tools and giving them to AI agents." Rapidly developed between 2025-2026, it has become a core extension point across major agent platforms including Anthropic Claude Code, OpenAI Codex, Hermes Agent, OpenClaw, and others.

This page is a parent page (cluster hub) that **classifies all Skills-related pages in the Wiki into 4 layers** and maps their interrelationships.

## Skills Concept Cluster Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                    Agent Skills Concept Cluster                       │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  Layer 1: FORMAT & STANDARD                                         │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │  agent-skills  │  markdown-based-skills                       │  │
│  │  SKILL.md      │  YAML frontmatter / file-based design        │  │
│  └───────────────────────────────────────────────────────────────┘  │
│                              ↓                                      │
│  Layer 2: DESIGN PHILOSOPHY                                         │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │  agentic-ai-skills     │  skill-architecture-patterns         │  │
│  │  10 Design Principles  │  Self-Authored vs Governed           │  │
│  │  (Recipe/Thinking)     │  (Hermes vs OpenClaw)               │  │
│  └───────────────────────────────────────────────────────────────┘  │
│                              ↓                                      │
│  Layer 3: IMPLEMENTATION & ARCHITECTURE                             │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │  claude-code-skills    │  skill-graph       │  llm-as-judge   │  │
│  │  Mechanism+9 Roles     │  Interconnected    │  skills         │  │
│  │  (Anthropic)          │  Markdown (Ronin)  │  (Context Eng)  │  │
│  │                       │                    │                 │  │
│  │  harness-engineering/  │  five-tier-skill-  │  evals-skills   │  │
│  │  system-architecture/  │  precedence        │  for-coding-    │  │
│  │  agent-skills          │  (OpenClaw)        │  agents (stub)  │  │
│  │  (OpenAI SKILL.md)     │                    │                 │  │
│  └───────────────────────────────────────────────────────────────┘  │
│                              ↓                                      │
│  Layer 4: RESEARCH & SCALING                                        │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │  skill-retrieval-augmentation (SRA)                           │  │
│  │  Skill Retrieval → Incorporation → Application               │  │
│  │  SRA-Bench (5,400 tasks, 26,262 skills)                      │  │
│  └───────────────────────────────────────────────────────────────┘  │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

## Layer 1: Format & Standard

Definition of "what a Skill is." File format, metadata, discovery mechanisms.

| Page | Focus | Source |
|--------|------|--------|
| **[[concepts/agent-skills]]** | Agent Skills open standard — Anthropic's SKILL.md format, Progressive Disclosure 3-layer design, code execution, development guidelines | Anthropic Engineering |
| **[[concepts/markdown-based-skills]]** | Markdown-Based Skills — `.md` + YAML frontmatter, Shadowing Hierarchy (private/shared/public), SQL-based discovery, "The Model Will Eat Your Scaffolding" principle | Fintool (Nicolas Bustamante) |

**Relationship:** `agent-skills` is Anthropic's format standard, `markdown-based-skills` is Fintool's concrete file priority order and discovery pattern. Both build on the common foundation of YAML frontmatter + .md files, but offer different discovery mechanisms (Progressive Disclosure vs SQL lazy loading).

## Layer 2: Design Philosophy

Principles of "what makes a good Skill." Writing style, structuring, governance.

| Page | Focus | Source |
|--------|------|--------|
| **[[concepts/agentic-ai-skills]]** | Agentic AI Skills Design — 10 design principles. High-level guidance like "Skills Are Recipes, Not Orders", "Teach Thinking, Not Conclusions", "Push Intelligence Up, Push Execution Down" | IntuitMachine (@IntuitMachine) |
| **[[concepts/skill-architecture-patterns]]** | Skill Architecture Patterns: Self-Authored vs Governed — Comparison of Hermes Agent (autonomous skill generation, 123+ bundles, skill explosion problem) vs OpenClaw (control, 5-tier precedence, user governance) | elvis (9-hour source code analysis) |

**Relationship:** `agentic-ai-skills` addresses the design theory of "how to write a single skill," while `skill-architecture-patterns` addresses the governance theory of "how to manage the entire skill ecosystem." The former is micro-design, the latter is macro-design. They are complementary — leading to the practical question of whether individual skills written under the 10 principles should be managed under Self-Authored or Governed frameworks.

The **Five-Tier Skill Precedence** (OpenClaw) mentioned in `skill-architecture-patterns` also exists as an independent page [[concepts/five-tier-skill-precedence]].

## Layer 3: Implementation & Architecture

Concrete implementations and patterns across specific platforms and providers.

| Page | Focus | Source |
|--------|------|--------|
| **[[concepts/claude-code-skills]]** | Claude Code Skills — **Mechanism** (folder structure, Progressive Disclosure, dynamic Hooks, memory persistence) and **9 role patterns** (Library/API Reference, Product Verification, Data Fetching, Business Process, Code Scaffolding, Code Quality, CI/CD, Runbooks, Infrastructure Ops). Design Tips, distribution patterns, marketplace operations | Thariq Shihipar (@trq212), Anthropic |
| **[[concepts/harness-engineering/system-architecture/agent-skills]]** | Agent Skills SKILL.md bundles — OpenAI's SKILL.md. Deterministic 3-stage loading sequence (metadata → bundle retrieval → context update), version management, container-based exploratory execution | OpenAI |
| **[[concepts/skill-graph]]** | Skill Graph — Playbook architecture using interconnected Markdown files. Knowledge nodes joined via `[[wikilinks]]`, agents traverse only needed nodes from index.md. "1 flat .md = TOOL, graph = TEAM". 17-file model (platforms/voice/engine/audience/) | Ronin (@DeRonin_) |
| **[[concepts/llm-as-judge-skills]]** | LLM-as-Judge Skills — Reusable skills for evaluating LLM output with LLMs themselves. Application of Context Engineering (GitHub: muratcankoylan/Agent-Skills-for-Context-Engineering, 15.5k stars) | Murat Can Koylan |
| **[[concepts/evals-skills-for-coding-agents]]** | Evals Skills for Coding Agents — Evaluation skills for coding agents (**stub**) | — |
| **[[concepts/five-tier-skill-precedence]]** | Five-Tier Skill Precedence — OpenClaw's 5-tier priority model (**stub**, details in [[concepts/skill-architecture-patterns]]) | OpenClaw |

**Relationship:** `claude-code-skills` and `harness-engineering/system-architecture/agent-skills` are Anthropic and OpenAI's SKILL.md implementations respectively. The former focuses on role classification and design tips, the latter on version management and container execution. `skill-graph` is orthogonal to both (Claude Code Skills and OpenAI Skills can both be graphed).

## Layer 4: Research & Scaling

Academic challenges accompanying large-scale skill corpora.

| Page | Focus | Source |
|--------|------|--------|
| **[[concepts/skill-retrieval-augmentation]]** | Skill Retrieval Augmentation (SRA) — A 3-stage pipeline (retrieval, incorporation, application) for when skill libraries reach "web scale." SRA-Bench (5,400 tasks, 26,262 skills). Discovery of the Incorporation Bottleneck (LLMs can retrieve but cannot incorporate). | Su, Long, Ai et al. (arXiv:2604.24594) |

**Relationship:** SRA is the academic framework for the scaling problems faced by Layers 1-3 implementations. Claude Code Skills' 9 categories, skill-architecture-patterns' Self-Authored skill explosion problem, and agent-skills' Progressive Disclosure are all directly connected to SRA's Incorporation Bottleneck.

## Cross-Cutting Topics

### Distribution & Marketplace

| Pattern | Description | Reference |
|---------|------|------|
| **Repository check-in** | Direct placement in `./.claude/skills/`. For small teams. | [[concepts/claude-code-skills#Distribution-Patterns]] |
| **Plugin marketplace** | Installation-based selective distribution. For large organizations. | [[concepts/claude-code-skills#Marketplace Operations]] |
| **Sandbox → Traction → PR** | Organic skill discovery flow. | [[concepts/claude-code-skills#Marketplace Operations]] |
| **ClawHub** | OpenClaw's managed plugin hub. | [[concepts/skill-architecture-patterns]] |

### Stub Pages (Need Enrichment)

These pages are stubs — substantive content exists in other pages:

| Stub | Page with Actual Content |
|------|----------------------|
| [[concepts/agent-skills-skillmd]] | [[concepts/agent-skills]] (duplicate stub) |
| [[concepts/evals-skills]] | — (independent stub) |
| [[concepts/evals-skills-for-coding-agents]] | — (independent stub) |
| [[concepts/five-tier-skill-precedence]] | [[concepts/skill-architecture-patterns]] (OpenClaw Five-Tier section) |

## Recommended Reading Path

### Beginners (Basic Understanding)
1. [[concepts/agent-skills]] — What are Skills? (format, standards)
2. [[concepts/agentic-ai-skills]] — 10 design principles for good Skills
3. [[concepts/claude-code-skills]] — How they are actually used (9 role patterns)

### Practitioners (Deployment & Operations)
1. [[concepts/claude-code-skills]] — Inventory your organization's Skills from the 9 role patterns
2. [[concepts/skill-graph]] — Building scalable playbooks with interconnected Markdown
3. [[concepts/markdown-based-skills]] — Skill design editable by non-engineers

### Architects (Infrastructure Design)
1. [[concepts/skill-architecture-patterns]] — Choosing between Self-Authored vs Governed
2. [[concepts/harness-engineering/system-architecture/agent-skills]] — OpenAI implementation details
3. [[concepts/skill-retrieval-augmentation]] — Retrieval and incorporation challenges at scale

## See Also

- [[concepts/agent-harness]] — Agent Harness overview (Skills are a component of Harness)
- [[concepts/harness-engineering]] — Harness Engineering framework
- [[concepts/context-engineering]] — Context Engineering (foundational concept for Skill design)
- [[concepts/mcp]] — Model Context Protocol (complementary tool connection standard to Skills)
- [[entities/thariq-shihipar]] — Proponent of the 9-category Claude Code Skills classification
- [[concepts/content-engine]] — Content generation engine leveraging Skill Graph
