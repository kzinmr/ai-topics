# Taxonomy buckets & OpenAI-vs-Anthropic platform comparison

Moved from SKILL.md "Key Patterns to Recognize" (2026-11-15 slim-down) to keep SKILL.md
under the 100 KB limit. This is the canonical routing taxonomy for `recommended_action`
and `candidate_wiki_path` when a new concept page is a candidate. Match keywords to a
bucket FIRST — do NOT create a new concept page when a bucket page exists.

## Engineering Paradigms — TAXONOMY RULES (CRITICAL)

**Agentic Engineering** (`concepts/agentic-engineering/`) = 開発者のワークフロー
- Keywords: "how to use agents", "developer patterns", "TDD with agents", "cognitive debt"
- Sources: Simon Willison guides, practitioner blogs, developer workflow tips
- Focus: "人間がエージェントをどう活用するか"
- Examples: Red/Green TDD, First Run the Tests, Showboat, Cognitive Debt, Context Window Management

**AI Agent Engineering** (`concepts/ai-agent-engineering/`) = システムアーキテクチャ
- Keywords: "orchestration", "execution loop", "harness", "sandbox", "tool design", "computer environment"
- Sources: OpenAI Engineering blog, Anthropic Engineering blog, platform architecture docs
- Focus: "エージェント実行基盤をどう構築するか"
- Examples: Agent Loop Orchestration, Context Compaction, Container Context, Agent Skills, Security Patterns

**Harness Engineering** (`concepts/harness-engineering/`) = 制御・構造化（共通概念）
- Bridges both: how execution environments are designed to constrain and guide agents
- Sources: Ryan Lopopolo/Symphony, OpenAI Codex architecture
- Keywords: "generator-evaluator loop", "critique shadowing", "evaluation-first"

**Agent Team / Swarm** (`concepts/agent-team-swarm/`) = 複数Agent協調・オーケストレーション
- Keywords: "multi-agent", "agent team", "swarm", "orchestration platform", "managed agents", "autonomous runs", "work management", "dark factory", "software factory"
- Sources: OpenAI Symphony, Anthropic Managed Agents, StrongDM Attractor, Dan Shapiro's 5-level model
- Focus: "複数Agentをどう協調させ、作業を自律管理するか"
- Examples: OpenAI Symphony (WORKFLOW.md駆動), Anthropic Managed Agents (Brain/Hands/Session分離), StrongDM Dark Factory (完全自律開発)
- **5-Level Model**: L1 Spicy Autocomplete → L2 Chat-Assisted → L3 Agent-Assisted → L4 Engineering Team → L5 Dark Factory
- **Key distinction**: L4 manages agents (Symphony/Managed Agents), L5 eliminates human review entirely (Dark Factory)

## Model Releases
- Company + model name + "launches", "releases", "announces"
- Group by company: OpenAI, Anthropic, Meta, Mistral, Google
- Before a `take`, check `raw/articles/` for a sitemap-monitor scrape of the same release (see SKILL.md cross-pipeline dedup) — downgrade to `reference` if the core release is already a raw article.

## Security / Events
- Leaks, controversies, policy changes → connect to existing safety concepts (e.g. `concepts/agent-safety-incidents-*`, `events/*`).

## Tool Ecosystem
- New frameworks, libraries, platforms → connect to existing entity pages rather than minting new concepts.

## OpenAI vs Anthropic Platform Comparison

When analyzing platform articles, note the architectural approach:

| Dimension | OpenAI | Anthropic |
|-----------|--------|-----------|
| 実行環境 | マネージドコンテナ提供 | 開発者自前のharness設計 |
| スキル | SKILL.mdバンドル（公式API） | ツール定義（JSON schema） |
| コンテキスト | ネイティブcompaction | 開発者実装 |
| セキュリティ | サイドカーエグレスプロキシ | 開発者責任 |
