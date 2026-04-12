---
title: "Wiki Change Log"
---

# Wiki Change Log

## 2026-04-13

### AI Memory Systems Analysis
- **New concept pages**:
  - `context-anxiety.md` — Sonnet 4.5のコンテキスト不安現象、AnthropicのMemory Tool (6ファイル操作)、Cognitionの戦略的ポジショニング
  - `ai-memory-systems.md` — AIメモリシステムの設計哲学比較（ChatGPT明示的メモリ vs Claude暗黙的メモリ vs Cognitionハイブリッド）、「The Bitter Lesson」の観点からの分析
  - `anthropic-memory-tool-cognition.md` — AnthropicのMemory ToolとCognitionの戦略的追随、「盗む」vs「独自開発」の競争力学
- **Updated**: `ai-agent-engineering/_index.md` — 新概念3件を追加、著者名 typo 修正 (Khemeni → Khemani)
- **Sources**: Shlok Khemani (shloked.com) 3記事、ByteByteGo コンテキストエンジニアリングガイド

### Simon Willison — Agentic Engineering Patterns Guide (L3 Enrichment)
- **simon-willison.md**: L3 Thought Analysisレベルにアップグレード
  - Added: Hoarding（知識の蓄積）哲学 — "productive kind of hoarding"
  - Added: Compound Engineering Loop — Write→Review→Improve→Save→Repeat
  - Added: Git統合の具体的プラクティス — 小さく頻繁なコミット、人間向けのメッセージ
  - Added: Writing Code is Cheap — 新しい習慣の必要性
  - Updated sources: Agentic Engineering Patterns Guideリンクを追加
- **New concept pages**:
  - `agentic-engineering/compound-engineering-loop.md` — 複合エンジニアリングループ
  - `agentic-engineering/code-hoarding.md` — 知識の蓄積と再利用パターン
- **index.md**: Updated with new concept entries


### Agent Team / Swarm Directory Created
- Created `agent-team-swarm/_index.md` — フロントページ: 5レベルモデル（Spicy Autocomplete → Dark Factory）、主要実装比較表
- Enriched `anthropic-managed-agents.md` — 公式ブログ3件（Claude Blog + Engineering Blog + Platform Docs）の情報を反映。Brain/Hands/Session分離アーキテクチャ、Multi-Agent Coordination、Pricing、Enterprise Adoption事例を追加
- New `openai-symphony.md` — WORKFLOW.md駆動のタスクオーケストレーター。SPEC.md解析、アーキテクチャコンポーネント、Symphony Go等のエコシステム、HN議論の洞察
- New `dark-factory-software-factory.md` — Simon Willison + Dan Shapiroの5レベルモデル、StrongDM実践事例、Attractor/CXB、Digital Twin Universe

## 2026-04-12

### Concept Taxonomy Restructure
- **Split `agentic-engineering/` into two directories:**
  - `agentic-engineering/` — Willisonの開発パターン (13 files remain)
  - `ai-agent-engineering/` — Anthropicのシステム構築パターン (11 files moved)
- Created `agentic-engineering/_index.md` (Willison-centric refactor)
- Created `ai-agent-engineering/_index.md` (Anthropic Engineering index)
- Updated tags in 11 moved files: `agentic-engineering` → `ai-agent-engineering`
- Updated `wiki/index.md` with new taxonomy
- **Concept**: Agentic Engineering (開発者ワークフロー) vs AI Agent Engineering (システムアーキテクチャ) vs Harness Engineering (環境設計・共通概念)

### Entity Pages
- Simon Willison entity page enriched with Agentic Engineering guide content
  - Sources: https://simonwillison.net/guides/agentic-engineering-patterns/
  - Added: 7 core patterns, 4 principles, 4 tool references, 4 related concepts
  - Expanded: Cognitive Debt theory, Context Window Management, Multi-agent patterns

### New Concept Pages (from Agentic Engineering guide)
- **context-window-management.md** — コンテキストウィンドウの戦略的管理（圧縮、構造化、優先順位付け）
- **rodney.md** — ブラウザ自動化CLIツール（エージェント向け設計、Showboat連携）
- **subagents.md** — 並列AIエージェント委任パターン（独立性、自己完結性、バッチモード）

### New Concept Pages (from OpenAI Responses API article)
- **agent-loop-orchestration.md** — エージェント実行ループ（モデル提案→シェル実行→結果フィードバック、並列実行、出力キャップ）
- **context-compaction.md** — コンテキスト圧縮（サーバーサイド自動、/compact手動、Codexによる自己改善）
- **container-context.md** — ホスト型コンテナ（永続ファイルシステム、SQLite、サイドカーエグレスプロキシ）
- **agent-skills.md** — SKILL.mdバンドル（再利用可能ワークフロー、バージョン管理、段階的探索）
- **agent-security-patterns.md** — エージェントセキュリティ（エグレスプロキシ、ドメインスコープシークレットインジェクション、許可リスト）

### Enriched
- **ai-agent-engineering/_index.md** — OpenAI Responses API 5概念を追加（エージェント実行基盤、セキュリティセクション新設）
- **wiki/index.md** — AI Agent Engineeringセクションを「Anthropic + OpenAI」に拡張

### Enriched Concept Pages
- **cognitive-debt.md** (1.5KB → 3.5KB): Vibe Coding vs Agentic Engineering対比表、認知負債のメカニズム、返済サイクル図を追加
