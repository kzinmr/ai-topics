---
title: "Agent Skills Overview — 概念クラスターマップ"
created: 2026-05-15
updated: 2026-05-15
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

# Agent Skills Overview — 概念クラスターマップ

Agent Skillsは「AIエージェントに再利用可能な知識・手順・ツールをパッケージ化して与える」概念。2025-2026年に急速に発展し、Anthropic Claude Code・OpenAI Codex・Hermes Agent・OpenClaw他、主要エージェントプラットフォームで中核的拡張ポイントとなっている。

本ページはWiki内の全Skills関連ページを**4層に分類**し、相互関係をマッピングする親ページ（クラスターハブ）である。

## Skills概念クラスターの全体像

```
┌─────────────────────────────────────────────────────────────────────┐
│                    Agent Skills 概念クラスター                        │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  Layer 1: FORMAT & STANDARD（フォーマット層）                        │
│  ┌───────────────────────────────────────────────────────────────┐ │
│  │  agent-skills  │  markdown-based-skills                       │ │
│  │  SKILL.md構造  │  YAML frontmatter / ファイルベース設計        │ │
│  └───────────────────────────────────────────────────────────────┘ │
│                              ↓                                      │
│  Layer 2: DESIGN PHILOSOPHY（設計思想層）                            │
│  ┌───────────────────────────────────────────────────────────────┐ │
│  │  agentic-ai-skills     │  skill-architecture-patterns         │ │
│  │  10 Design Principles  │  Self-Authored vs Governed           │ │
│  │  (Recipe/Thinking)     │  (Hermes vs OpenClaw)               │ │
│  └───────────────────────────────────────────────────────────────┘ │
│                              ↓                                      │
│  Layer 3: IMPLEMENTATION & ARCHITECTURE（実装・アーキテクチャ層）    │
│  ┌───────────────────────────────────────────────────────────────┐ │
│  │  claude-code-skills    │  skill-graph       │  llm-as-judge   │ │
│  │  機序＋9役割パターン    │  相互接続Markdown   │  skills         │ │
│  │  (Anthropic)          │  (Ronin)           │  (Context Eng)  │ │
│  │                       │                    │                 │ │
│  │  harness-engineering/  │  five-tier-skill-  │  evals-skills   │ │
│  │  system-architecture/  │  precedence        │  for-coding-    │ │
│  │  agent-skills          │  (OpenClaw)        │  agents (stub)  │ │
│  │  (OpenAI SKILL.md)     │                    │                 │ │
│  └───────────────────────────────────────────────────────────────┘ │
│                              ↓                                      │
│  Layer 4: RESEARCH & SCALING（研究・スケーリング層）                  │
│  ┌───────────────────────────────────────────────────────────────┐ │
│  │  skill-retrieval-augmentation (SRA)                           │ │
│  │  Skill Retrieval → Incorporation → Application               │ │
│  │  SRA-Bench (5,400 tasks, 26,262 skills)                      │ │
│  └───────────────────────────────────────────────────────────────┘ │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

## Layer 1: Format & Standard — フォーマット層

「Skillとは何か」の定義。ファイル形式・メタデータ・発見メカニズム。

| ページ | 焦点 | 提供元 |
|--------|------|--------|
| **[[concepts/agent-skills]]** | Agent Skills オープン標準 — AnthropicによるSKILL.mdフォーマット、Progressive Disclosure 3層設計、コード実行、開発ガイドライン | Anthropic Engineering |
| **[[concepts/markdown-based-skills]]** | Markdown-Based Skills — `.md` + YAML frontmatter、Shadowing Hierarchy (private/shared/public)、SQL-based discovery、\"The Model Will Eat Your Scaffolding\"原則 | Fintool (Nicolas Bustamante) |

**関係**: `agent-skills`はAnthropic版のフォーマット標準、`markdown-based-skills`はFintool実装での具体的なファイル優先順位と発見パターン。両者はYAML frontmatter + .mdファイルという共通基盤の上に、異なる発見メカニズム（プログレッシブ開示 vs SQL lazy loading）を提供する。

## Layer 2: Design Philosophy — 設計思想層

「良いSkillとは何か」の原則論。書き方・構造化・ガバナンス。

| ページ | 焦点 | 提供元 |
|--------|------|--------|
| **[[concepts/agentic-ai-skills]]** | Agentic AI Skills Design — 10の設計原則。「Skills Are Recipes, Not Orders」「Teach Thinking, Not Conclusions」「Push Intelligence Up, Push Execution Down」等の抽象度の高い設計指針 | IntuitMachine (@IntuitMachine) |
| **[[concepts/skill-architecture-patterns]]** | Skill Architecture Patterns: Self-Authored vs Governed — Hermes Agent（自律的スキル生成・123+バンドル・スキル爆発問題） vs OpenClaw（統制・5段階優先順位・ユーザーガバナンス）の比較 | elvis (9時間ソースコード分析) |

**関係**: `agentic-ai-skills`が「単一スキルの書き方」の設計論であるのに対し、`skill-architecture-patterns`は「スキル群全体をどう管理するか」のガバナンス論。前者はミクロ設計、後者はマクロ設計。両者は補完的で、10原則で書かれた個々のスキルをSelf-Authored/Governedどちらの枠組みで管理するかという実践的判断につながる。

`skill-architecture-patterns`内で言及される**Five-Tier Skill Precedence**（OpenClaw）は独立ページ [[concepts/five-tier-skill-precedence]] としても存在する。

## Layer 3: Implementation & Architecture — 実装・アーキテクチャ層

特定のプラットフォーム・プロバイダでの具体的実装とパターン。

| ページ | 焦点 | 提供元 |
|--------|------|--------|
| **[[concepts/claude-code-skills]]** | Claude Code Skills — **機序**（フォルダ構造・Progressive Disclosure・動的Hooks・メモリ永続化）と **9つの役割パターン**（Library/API Reference, Product Verification, Data Fetching, Business Process, Code Scaffolding, Code Quality, CI/CD, Runbooks, Infrastructure Ops）。設計Tips・配布パターン・マーケットプレイス運用 | Thariq Shihipar (@trq212), Anthropic |
| **[[concepts/harness-engineering/system-architecture/agent-skills]]** | Agent Skills SKILL.md bundles — OpenAI版SKILL.md。決定論的3段階読み込みシーケンス（メタデータ→バンドル取得→コンテキスト更新）、バージョン管理、コンテナ内探索的実行 | OpenAI |
| **[[concepts/skill-graph]]** | Skill Graph — 相互接続Markdownファイルによるプレイブックアーキテクチャ。`[[wikilinks]]`で知識ノードを結合し、エージェントがindex.mdから必要なノードだけを辿る。「1 flat .md = TOOL, graph = TEAM」。17ファイルモデル（platforms/voice/engine/audience/） | Ronin (@DeRonin_) |
| **[[concepts/llm-as-judge-skills]]** | LLM-as-Judge Skills — LLMの出力をLLM自身で評価する再利用可能スキル。Context Engineeringの応用（GitHub: muratcankoylan/Agent-Skills-for-Context-Engineering, 15.5k stars） | Murat Can Koylan |
| **[[concepts/evals-skills-for-coding-agents]]** | Evals Skills for Coding Agents — コーディングエージェントの評価用スキル（**stub**） | — |
| **[[concepts/five-tier-skill-precedence]]** | Five-Tier Skill Precedence — OpenClawの5段階優先順位モデル（**stub**、本文は[[concepts/skill-architecture-patterns]]に詳述） | OpenClaw |

**関係**: `claude-code-skills`と`harness-engineering/system-architecture/agent-skills`はそれぞれAnthropicとOpenAIのSKILL.md実装。前者は役割分類と設計Tipsに焦点、後者はバージョン管理とコンテナ実行に焦点。`skill-graph`は`[[wikilinks]]`による相互接続という点で両者と直交する（Claude Code SkillsもOpenAI Skillsもグラフ化可能）。

## Layer 4: Research & Scaling — 研究・スケーリング層

スキルコーパスの大規模化に伴う学術的課題。

| ページ | 焦点 | 提供元 |
|--------|------|--------|
| **[[concepts/skill-retrieval-augmentation]]** | Skill Retrieval Augmentation (SRA) — スキルライブラリが\"web scale\"化する際の検索・組み込み・適用の3段階パイプライン。SRA-Bench（5,400タスク、26,262スキル）。Incorporation Bottleneck（検索できてもLLMは組み込めない）の発見 | Su, Long, Ai et al. (arXiv:2604.24594) |

**関係**: SRAはLayer 1-3の実装が直面するスケーリング問題の学術的フレームワーク。`claude-code-skills`の9分類・`skill-architecture-patterns`のSelf-Authoredスキル爆発問題・`agent-skills`のProgressive DisclosureはいずれもSRAのIncorporation Bottleneckと直結する。

## 横断的トピック

### 配布・マーケットプレイス

| パターン | 説明 | 参照 |
|---------|------|------|
| **リポジトリチェックイン** | `./.claude/skills/` に直接配置。小規模チーム向け | [[concepts/claude-code-skills#配布パターン-distributing-skills]] |
| **Pluginマーケットプレイス** | インストールベースの選択的配布。大規模組織向け | [[concepts/claude-code-skills#マーケットプレイス運用]] |
| **Sandbox→トラクション→PR** | 有機的スキル発見フロー | [[concepts/claude-code-skills#マーケットプレイス運用]] |
| **ClawHub** | OpenClawの統制型プラグインハブ | [[concepts/skill-architecture-patterns]] |

### Stubページ（要Enrich）

これらのページはstub状態で、実質的な内容は他ページに存在:

| Stub | 実質的内容のあるページ |
|------|----------------------|
| [[concepts/agent-skills-skillmd]] | [[concepts/agent-skills]]（重複stub） |
| [[concepts/evals-skills]] | —（独立stub） |
| [[concepts/evals-skills-for-coding-agents]] | —（独立stub） |
| [[concepts/five-tier-skill-precedence]] | [[concepts/skill-architecture-patterns]]（OpenClaw Five-Tier部） |

## 読み筋（Recommended Reading Path）

### 初心者向け（基本理解）
1. [[concepts/agent-skills]] — Skillsとは何か（フォーマット・標準）
2. [[concepts/agentic-ai-skills]] — 良いSkillsの設計原則10カ条
3. [[concepts/claude-code-skills]] — 実際にどう使われているか（9役割パターン）

### 実践者向け（導入・運用）
1. [[concepts/claude-code-skills]] — 9役割パターンから自組織のSkills棚卸し
2. [[concepts/skill-graph]] — 相互接続Markdownによるスケーラブルなプレイブック構築
3. [[concepts/markdown-based-skills]] — 非エンジニアでも編集可能なSkills設計

### アーキテクト向け（基盤設計）
1. [[concepts/skill-architecture-patterns]] — Self-Authored vs Governedの選択
2. [[concepts/harness-engineering/system-architecture/agent-skills]] — OpenAIの実装詳細
3. [[concepts/skill-retrieval-augmentation]] — スケーリング時の検索・組み込み問題

## See Also

- [[concepts/agent-harness]] — Agent Harness全体像（SkillsはHarnessの構成要素）
- [[concepts/harness-engineering]] — Harness Engineeringフレームワーク
- [[concepts/context-engineering]] — Context Engineering（Skills設計の基盤概念）
- [[concepts/mcp]] — Model Context Protocol（Skillsと相補的なツール接続標準）
- [[entities/thariq-shihipar]] — Claude Code Skillsの9分類の提唱者
- [[concepts/content-engine]] — Skill Graphを活用したコンテンツ生成エンジン
