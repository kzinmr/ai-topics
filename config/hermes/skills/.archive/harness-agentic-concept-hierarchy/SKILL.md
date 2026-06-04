---
name: harness-agentic-concept-hierarchy
category: wiki
description: Concept hierarchy and cross-referencing pattern for Harness Engineering, Agentic Engineering, AI Agent Engineering, and Context Engineering in the wiki
created: 2026-04-19
---

# Harness/Agentic Concept Hierarchy

## Architecture Decision (2026-04-19)

These 4 concepts form a cluster frequently co-referenced by the same thought leaders (Karpathy, Willison, Lopopolo). They are NOT at the same level — they have a containment relationship.

## Hierarchy

```
Harness Engineering (最上位の哲学)
"Agent = Model + Harness" — エージェントの性能は環境設計で決まる
│
├── Agentic Engineering (人間側の活用パターン)
│   Willison: TDD、Cognitive Debt、Vibe Coding → "人間がどう使うか"
│
├── AI Agent Engineering (システム側の構築パターン)
│   Anthropic/OpenAI: tool design、evals、loop orchestration → "どう作るか"
│
└── Context Engineering (横断技術)
    Karpathy/DSPy: コンテキストの選択・圧縮・配置 → "何をどう見せるか"
```

## Current File Locations
- `concepts/harness-engineering.md` — active, top-level singleton
- `concepts/agentic-engineering/_index.md` — draft
- `concepts/ai-agent-engineering/_index.md` — draft  
- `concepts/context-engineering.md` — active, singleton

## Structural Rules

1. **Harness is the umbrella** — "Agent = Model + Harness" (Ryan Lopopolo/Symphony) contains all others
2. **Agentic ≠ AI Agent** — Willison's developer workflow patterns vs Anthropic's system design patterns. Keep separate due to different granularity.
3. **Context Engineering is cross-cutting** — applies to both Agentic and AI Agent patterns. Should be unified (currently duplicated in 3 locations).
4. **Maintain separation of concerns** — Don't merge Agentic + AI Agent into one page; their audiences and use cases differ.

## Target Structure (pending implementation)
```
concepts/harness-engineering/_index.md          ← umbrella index (new)
concepts/harness-engineering/agentic-workflows/  ← moved from concepts/agentic-engineering/
concepts/harness-engineering/system-architecture/ ← moved from concepts/ai-agent-engineering/
concepts/harness-engineering/context-engineering.md ← unified version (merge 3 sources)
```

## Key People
- Ryan Lopopolo (@rlopopolo) — Harness Engineering, Symphony
- Simon Willison — Agentic Engineering patterns
- Andrej Karpathy — Context Engineering (Software 3.0)
- DSPy team — Declarative context optimization

## Cross-Reference Pattern
When creating entity pages for people discussing these topics, always:
1. Link to Harness as the parent concept
2. Specify whether the person's work falls under Agentic or AI Agent patterns
3. Note any Context Engineering contributions separately