---
title: byterover
type: entity
created: 2026-05-03
updated: 2026-05-03
tags:
  - entity
  - product
  - memory
  - ai-agent
  - open-source
  - devtools
aliases:
  - brv
  - byterover-cli
  - ByteRover CLI
  - Cipher
sources:
  - raw/articles/2026-05-03_ByteRover-overview.md
  - https://www.byterover.dev/
  - https://github.com/campfirein/byterover-cli
  - https://arxiv.org/abs/2604.01599
  - https://docs.byterover.dev/
---

# ByteRover

**ByteRover** (formerly **Cipher**) is a portable, file-based memory layer for autonomous coding agents. It provides persistent, structured, evolving knowledge that travels with developers across tools — from OpenClaw to Claude Code to Cursor. Built in TypeScript (98.2%) by the Vietnam-based campfirein team, ByteRover achieves market-best 92-96% retrieval accuracy on long-term memory benchmarks without any vector database, graph database, or embedding service.

[GitHub: 4.2k+ stars](https://github.com/campfirein/byterover-cli) | [arXiv:2604.01599](https://arxiv.org/abs/2604.01599) | [npm: byterover-cli](https://www.npmjs.com/package/byterover-cli)

## Architecture

ByteRover inverts the traditional memory pipeline. Instead of delegating storage to an external vector/graph database, the **same LLM** that reasons about the task also curates and structures knowledge. All memory is stored as human-readable Markdown files on the local filesystem.

### Hierarchical Context Tree

Knowledge is organized into a four-tier hierarchy:

| Tier | Level | Description |
|------|-------|-------------|
| 1 | **Domain** | Broadest category |
| 2 | **Topic** | Specific area of interest |
| 3 | **Subtopic** | Granular focus |
| 4 | **Entry** | Individual knowledge unit with relations, provenance, and lifecycle management |

Each Entry carries:
- **Explicit relations** to other entries
- **Provenance** (source tracking)
- **Adaptive Knowledge Lifecycle (AKL)**: importance scoring, maturity tiers, and recency decay

### 5-Tier Progressive Retrieval

ByteRover resolves most queries in **<100ms** using file-based hierarchy traversal. It only escalates to expensive agentic LLM reasoning for novel or complex questions that cannot be answered by lower tiers.

```
User Query
    │
    ▼
┌─────────────────────────┐
│ Tier 1: Fuzzy Text Match│  ← <100ms (most queries)
├─────────────────────────┤
│ Tier 2: File Tree Navig.│
├─────────────────────────┤
│ Tier 3: Keyword Search  │
├─────────────────────────┤
│ Tier 4: Pattern Match   │
├─────────────────────────┤
│ Tier 5: LLM Agentic     │  ← only for novel/complex
└─────────────────────────┘
```

### Key Innovation: No Vector DB

ByteRover operates with **zero external infrastructure** — no vector database, no graph database, no embedding service. This eliminates semantic drift (pipeline doesn't understand what the agent intended to remember), context loss (coordination context between agents), and infrastructure overhead.

## Benchmark Performance

ByteRover leads the LoCoMo benchmark and performs competitively on LongMemEval:

| Benchmark | ByteRover 2.0 | #2 Competitor | Metric |
|-----------|---------------|---------------|--------|
| **LoCoMo (Overall)** | 92.2% (later 96.1%) | 89.6% (Hindsight) | Accuracy |
| **LoCoMo Temporal** | **94.4%** | 83.8% (Hindsight) | Accuracy |
| **LoCoMo Multi-hop** | **85.1%** | 70.8% (Hindsight) | Accuracy |
| **LoCoMo Single-hop** | **95.4%** | 86.2% (Hindsight) | Accuracy |
| **LongMemEval-S** | **92.8%** | — | Accuracy, ~23,867 docs |

> **Key Insight:** ByteRover achieved 90.9% on LoCoMo even with lightweight *Gemini-3-flash*, proving the architecture (not just the model) drives results. Standard LLMs without a memory system score only 32.1 F1 vs humans at 87.9 F1.

### Benchmark Comparison Table

| System | Single-Hop | Multi-Hop | Temporal | **Overall** |
|--------|-----------|-----------|----------|-------------|
| **ByteRover 2.0** | **95.4%** | **85.1%** | **94.4%** | **92.2%** |
| Hindsight | 86.2% | 70.8% | 83.8% | 89.6% |
| Memobase | 85.1% | 46.9% | 85.1% | 75.8% |
| Zep | 74.1% | 55.3% | 79.8% | 75.1% |
| Mem0 | 67.1% | 51.2% | 55.5% | 66.9% |
| OpenAI Memory | 58.2% | 42.6% | 48.3% | 52.9% |

## Key Features

### Interactive TUI (REPL)
React/Ink-powered REPL interface for direct interaction with an AI agent. Run `brv` in any project directory.

### Git-like Version Control for Context
Full branching workflow (`branch`, `commit`, `merge`, `push/pull`) specifically for project knowledge — treat memory like code.

### Broad LLM Support
18 providers: Anthropic, OpenAI, Google, Groq, Mistral, xAI, and local/OpenAI-compatible APIs.

### Extensive Tooling
24 built-in tools for code execution, file operations, and memory management.

### Agent Ecosystem Compatibility
Works with 22+ AI agents: Cursor, Claude Code, Windsurf, Cline, Codex, Claude Desktop, Gemini CLI, AWS's Kiro, Roo Code, Trae, Amp Code, Warp, and more.

### MCP Integration
Model Context Protocol server enables integration with any MCP-compatible client (Zed editor, VS Code, etc.).

### Cloud Sync (Optional)
ByteRover Cloud provides team collaboration, multi-machine sync, shared workspaces, built-in hosted LLM, SOC 2 Type II certified security with privacy mode.

### Enterprise Features
SOC 2 Type II compliance, proxy support, RBAC, AES-256 at rest, TLS 1.2+ in transit, data residency controls.

## Integrations

### Native Plugins
- **Claude Code Plugin** — Native & long-term memory for Claude Code
- **Hermes Agent Plugin** — Open-source native memory (4k+ stars)
- **OpenClaw Plugin** — Structured, long-term memory for OpenClaw

### MCP-based (Cipher)
The legacy **Cipher** MCP server provides memory compatibility across Cursor, Wind surf, Claude Desktop, Gemini CLI, VS Code, Roo Code, Kimi K2, and Warp. Dual memory layers:
- **System 1 Memory**: Programming concepts, business logic, past interactions
- **System 2 Memory**: AI reasoning steps during code generation

### Zed Extension
ByteRover MCP server integration for the Zed AI assistant, with custom `.rules` files for memory usage.

## Concepts

ByteRover embodies the [[concepts/harness-engineering]] philosophy: the agent memory layer is a critical component of the harness, not an external service. Its agent-native architecture (same LLM curates + retrieves) aligns with the "Agent = Model + Harness" framework.

## Creator

Built by **Duy Anh "Andy" Nguyen** (@kevinnguyendn, @byteroverdev), Founder & CEO of ByteRover. Based in Da Nang, Vietnam. Former Machine Learning Engineer at OpenLab JSC. Started ByteRover in September 2024.

See: [[entities/andy-nguyen]]

## Team

- **Danh Doan** (@danhdoan)
- **Hoang Pham**
- Contributors: ncnthien, DatPham-6996, cuongdo-byterover, bao-byterover, RyanNg1403, AmElmo, zeki893, leehpham, hieuntg81

## Community

- **Website**: https://www.byterover.dev/
- **Docs**: https://docs.byterover.dev/
- **App**: https://app.byterover.dev/
- **GitHub**: https://github.com/campfirein/byterover-cli
- **Discord**: https://discord.com/invite/UMRrpNjh5W
- **X/Twitter**: @byteroverdev, @kevinnguyendn
- **LinkedIn**: https://www.linkedin.com/company/byterover/
- **Product Hunt**: https://www.producthunt.com/products/byterover
- **arXiv**: https://arxiv.org/abs/2604.01599

## Related Pages
- [[entities/andy-nguyen]] — Founder & CEO
- [[entities/hermes-agent]] — Has native ByteRover integration
- [[entities/claude-code]] — Has native ByteRover plugin
- [[entities/openclaw]] — Has native ByteRover plugin
- Mem0 — Competitor memory system
- [[concepts/harness-engineering]] — ByteRover embodies the harness philosophy

## Sources
- [ByteRover Homepage](https://www.byterover.dev/) — Scraped 2026-05-03
- [GitHub: campfirein/byterover-cli](https://github.com/campfirein/byterover-cli)
- [arXiv:2604.01599](https://arxiv.org/abs/2604.01599) — ByteRover: Agent-Native Memory Through LLM-Curated Hierarchical Context
- [docs.byterover.dev](https://docs.byterover.dev/)
- [ByteRover Benchmark Blog](https://www.byterover.dev/blog/benchmark-ai-agent-memory)
- [campfirein/cipher](https://github.com/campfirein/cipher)
- [Product Hunt: byterover](https://www.producthunt.com/products/byterover)
- [Tracxn: ByteRover Profile](https://platform.tracxn.com/a/d/company/6734efec6a865a7ccdb3ab64/byterover)
