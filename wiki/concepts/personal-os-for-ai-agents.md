---
title: "Personal OS for AI Agents"
created: 2026-04-27
updated: 2026-04-27
tags: [personal-os, context-engineering, file-system, git-based]
aliases: [personal-brain-os, file-based-ai-os]
related: [[concepts/context-engineering]], [[concepts/agentic-ai-skills]], [[concepts/context-management]], [[concepts/harness-engineering]]
sources: [
  "https://x.com/koylanai/status/2025286163641118915"
]
---

# Personal OS for AI Agents

## Summary

A file-based personal operating system that lives inside a Git repository. Instead of databases, vector stores, or API keys, it uses 80+ files in markdown, YAML, and JSONL — formats that both humans and language models read natively. The system provides context (voice, brand, goals, contacts, research, failures) to AI assistants without the degradation of massive system prompts.

## Core Architecture

### Progressive Disclosure (3-Level Loading)
- **Level 1**: Lightweight routing file (SKILL.md) — always loaded, tells AI which module is relevant
- **Level 2**: Module-specific instructions (CONTENT.md, OPERATIONS.md, NETWORK.md) — 40-100 lines each, load only when needed
- **Level 3**: Actual data files (JSONL, YAML, research docs) — loaded only when the task requires them

This creates a funnel: broad routing → module context → specific data. Maximum two hops to any piece of information.

### Agent Instruction Hierarchy (3 Layers)
- **Repository level**: CLAUDE.md — onboarding document, full project map
- **Brain level**: AGENT.md — seven core rules, decision table mapping requests to action sequences
- **Module level**: Directory-specific instruction files with domain-specific behavioral constraints

### Format-Function Mapping
| Format | Purpose | Rationale |
|--------|---------|-----------|
| JSONL | Logs (contacts, interactions, bookmarks, etc.) | Append-only, stream-friendly, each line self-contained |
| YAML | Configuration (goals, values, circles) | Hierarchical data, comments supported, human-readable |
| Markdown | Narrative (voice guides, research, templates) | Native LLM reading, universal rendering, clean Git diffs |

### Episodic Memory
Three append-only logs storing judgment, not just facts:
- `experiences.jsonl` — Key moments with emotional weight scores (1-10)
- `decisions.jsonl` — Key decisions with reasoning, alternatives, outcomes
- `failures.jsonl` — What went wrong, root cause, prevention steps

## Key Ideas

- **Context engineering > Prompt engineering** — Design information architecture, not just optimize individual interactions
- **File system as memory** — No database needed; files + Git versioning provides full traceability
- **Cross-module references** — Flat-file relational model (contact_id links across JSONL files) enables knowledge graph traversal
- **Skill system** — Auto-loading reference skills + manual invocation task skills
- **Voice encoding** — Structured attributes (1-10 scales) + banned word lists + quality gates
- **Automation chains** — Scripts output to stdout in agent-readable format, closing the data-action loop

## Lessons Learned (What Went Wrong)

1. **Over-engineered schemas** — Initial JSONL schemas had 15+ fields per entry; cut to 8-10 essential fields
2. **Voice guide too long** — 1,200 lines caused lost-in-middle drift; restructured to front-load distinctive patterns in first 100 lines
3. **Module boundaries matter** — Splitting identity and brand modules cut token usage by 40% for voice-only tasks
4. **Append-only is non-negotiable** — Agent accidentally overwrote JSONL data; JSONL's append-only pattern prevents data destruction

## Results

- AI assistant knows who the user is, how they write, what they're working on
- Writes in the user's voice because it's encoded as structured data
- Manages relationships because contacts and interactions are in queryable files
- Runs on any machine with any AI tool — zero dependencies, full portability
- Every change versioned, every decision traceable, nothing ever truly lost

## Related Concepts
- [[concepts/context-engineering]] — The broader discipline this falls under
- [[concepts/agentic-ai-skills]] — Skill design principles used in this system
- [[concepts/context-management]] — Managing context windows and attention
- [[entities/koylanai]] — Creator: Muratcan Koylan, Context Engineer at Sully.ai
