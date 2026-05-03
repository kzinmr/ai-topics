---
title: "ByteRover Overview"
source: https://www.byterover.dev/blog
source_type: homepage
date_accessed: 2026-05-03
---

# ByteRover Overview

ByteRover is a portable, file-based memory layer for autonomous coding agents. It provides persistent, structured, evolving knowledge across AI agents, with up to 92.19% retrieval accuracy (best on market as of 2026). 

Formerly known as "Cipher", the project was rebranded to ByteRover CLI (brv).

## Key Facts

- **Website**: https://www.byterover.dev/
- **GitHub**: https://github.com/campfirein/byterover-cli (4.2k+ stars)
- **Docs**: https://docs.byterover.dev/
- **App**: https://app.byterover.dev/
- **Paper**: arXiv:2604.01599 — "ByteRover: Agent-Native Memory Through LLM-Curated Hierarchical Context"
- **License**: Elastic License 2.0
- **Language**: TypeScript (98.2%)
- **Organization**: campfirein (GitHub org)

## Core Architecture

ByteRover replaces vector-based memory with a tiered file-search retrieval pipeline. Knowledge is organized as a **Hierarchical Context Tree** with four tiers:
1. Domain (broadest category)
2. Topic
3. Subtopic
4. Entry (individual knowledge unit with relations, provenance, and Adaptive Knowledge Lifecycle)

### Adaptive Knowledge Lifecycle (AKL)
- Importance Scoring
- Maturity Tiers
- Recency Decay

### 5-Tier Progressive Retrieval
Most queries resolved in <100ms; expensive agentic reasoning only for novel/complex questions.

## Benchmark Results
- **LoCoMo**: 92.2% overall accuracy (later updated to 96.1% per GitHub README)
- **LongMemEval-S**: 92.8% accuracy (~23,867 docs)
- Multi-hop recall: 85.1% (14.3 points ahead of next competitor)
- Temporal reasoning: 94.4%

## Key Features
- Interactive TUI with REPL (React/Ink)
- Context tree knowledge storage
- Git-like version control (branch, commit, merge, push/pull)
- 18 LLM providers supported
- 24 built-in agent tools
- Cloud sync with push/pull
- MCP integration
- Works with 22+ AI coding agents (Cursor, Claude Code, Windsurf, Cline, etc.)
- SOC 2 Type II certified cloud
- Enterprise proxy support

## Integrations
- Native plugins for Hermes Agent, Claude Code, OpenClaw
- MCP server for Zed editor
- Cipher: MCP-based memory layer compatible with Cursor, Codex, Claude Desktop, Gemini CLI, VS Code, Roo Code, etc.

## Creator

**Andy Nguyen** (Duy Anh Nguyen, @kevinnguyendn) — Founder & CEO of ByteRover. Based in Da Nang, Vietnam. Previously Machine Learning Engineer at OpenLab JSC. Started ByteRover in September 2024.

## Team
- Danh Doan (@danhdoan)
- Hoang Pham
- Contributors: ncnthien, DatPham-6996, cuongdo-byterover, bao-byterover, RyanNg1403, AmElmo, zeki893
