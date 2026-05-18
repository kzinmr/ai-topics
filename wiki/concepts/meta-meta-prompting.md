---
title: "Meta-Meta-Prompting"
aliases: ["Fat Skills Fat Code Thin Harness", "Personal AI OS", "Compound AI System"]
type: concept
created: 2026-05-11
tags:
  - agentic-engineering
  - harness-engineering
  - personal-ai
  - workflow
  - multi-agent
  - architecture
related:
  - concepts/harness-engineering
  - concepts/agent-sandboxing
sources:
  - raw/articles/2026-05-09_garrytan_meta-meta-prompting.md
---

# Meta-Meta-Prompting

**Meta-Meta-Prompting** とは、Garry Tan（YC CEO）が提唱する AI agent 設計哲学。AI に直接 prompt を書くのではなく、AI が自分自身に prompt を書けるような **skill system** と **knowledge graph** を構築し、システム全体が複利的に成長していくアプローチ。

> 「今はほとんど AI に prompt を書かない。本当に重要なのは skill system だ」 — Garry Tan

## なぜ「Meta-Meta」か

1. **Level 1: Prompt** — 人間が AI に指示を書く
2. **Level 2: Meta-Prompt** — AI が自分への prompt を生成する（system prompt, chain-of-thought など）
3. **Level 3: Meta-Meta-Prompt** — AI が「いつ・どの skill を使うか」「どのモデルにルーティングするか」「結果を knowledge base のどこに統合するか」を自律的に決定する

Level 3 では、人間はもはや個別の prompt を書かない。代わりに、再利用可能な skill を構築し、AI がそれらを組み合わせて自律的に実行する。

## Fat Skills, Fat Code, Thin Harness

Meta-Meta-Prompting を実現するアーキテクチャパターン：

```
┌─────────────────────────────────────────────────┐
│                  Thin Harness                     │
│  ┌─────────────────────────────────────────┐    │
│  │          Router / Orchestrator            │    │
│  │  (OpenClaw, Hermes Agent, Claude Code)   │    │
│  └─────────────────────────────────────────┘    │
│                      │                            │
│         ┌────────────┼────────────┐              │
│         ▼            ▼            ▼              │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐        │
│  │  Skill A  │ │  Skill B  │ │  Skill C  │  ...  │
│  │ (meeting) │ │ (enrich)  │ │ (triage)  │        │
│  └──────────┘ └──────────┘ └──────────┘        │
│         │            │            │              │
│         ▼            ▼            ▼              │
│  ┌─────────────────────────────────────────┐    │
│  │            Fat Code / Knowledge           │    │
│  │    (10万ページ structured knowledge base)   │    │
│  └─────────────────────────────────────────┘    │
└─────────────────────────────────────────────────┘
```

| 層 | 役割 | 特徴 |
|----|------|------|
| **Thin Harness** | ルーティング・オーケストレーション | 軽量、交換可能、汎用的 |
| **Fat Skills** | 再利用可能なワークフローモジュール | 独立してテスト可能、組み合わせ可能、蓄積する |
| **Fat Code** | 知識・データ・ロジックの集積 | 人物・会社・会議・書籍・記事ごとの構造化ページ |

### Thin Harness の原則

- Harness は「どのモデルを使うか」「どの skill を呼ぶか」のルーティングのみを担当
- ビジネスロジックや知識は持たない
- 交換可能（Claude Code → Hermes Agent → OpenClaw と移行しても Fat Skills は生き残る）

### Fat Skills の原則

- 各 skill は**独立してテスト可能**
- skill 同士は**組み合わせ可能**（meeting-ingestion → enrich → investor-update-ingest）
- 一度作った skill は**永続的に蓄積**する
- **Skillify** — 繰り返しパターンを発見したら自動的に skill 化する meta-skill

## 複利効果（Compound Effect）

Meta-Meta-Prompting の最大の価値は**複利性**にある：

```
Week 1:  5 skills,  1,000 pages → 基本的な会議サマリー
Week 4:  20 skills, 5,000 pages → 人物間の関係性を理解し始める
Week 12: 60 skills, 30,000 pages → 過去の会議と新しい書籍を横断的に接続
Week 24: 100+ skills, 100,000 pages → Book Mirror のような高度な合成が可能に
```

- 各書籍、各会議、各 skill 改善が**減衰せず蓄積**する
- ナレッジベースは「ファイルキャビネット」（静的ストレージ）ではなく「神経システム」（動的接続・更新・推論）として機能
- **時間とともにシステム全体が賢くなる**唯一の AI アーキテクチャ

## 実装パターン

### 1. Knowledge Graph の自動更新

```yaml
会議終了後:
  - transcript 生成
  - サマリー作成
  - 人物ページ更新（参加者の最新の発言・関心を反映）
  - 会社ページ更新
  - タイムライン更新
  - open threads 更新
  - relationship context 更新
```

### 2. マルチモデルルーティング

| タスク種別 | モデル | 理由 |
|-----------|--------|------|
| 精密作業 | Claude Opus 4.7 | 正確性重視 |
| 想起・抽出 | GPT-5.5 | 検索・要約性能 |
| 創造的作業 | DeepSeek V4-Pro | 発散的思考 |
| 高速推論 | Groq + Llama | レイテンシ最小化 |
| ルーティング判断 | OpenClaw / Hermes Agent | Harness 層 |

### 3. Skillify — 自動スキル化

```
人間: "skillify this"
システム:
  1. 直近の操作パターンを分析
  2. 再利用可能なワークフローを抽出
  3. skill file を生成
  4. resolver routing system に登録
  5. 以降の全ワークフローで利用可能に
```

## Hermes Agent との対応関係

Garry Tan のアーキテクチャは Hermes Agent の設計と深く対応する：

| Meta-Meta-Prompting | Hermes Agent |
|---------------------|--------------|
| Thin Harness | Hermes Agent コアランタイム |
| Fat Skills | スキルシステム（`skill_manage`） |
| Skillify | スキル自動生成（`skill_manage(action='create')`） |
| Knowledge Graph | wiki（構造化ナレッジベース） |
| Multi-model routing | マルチプロバイダ対応 |
| 100+ skills | 利用可能な全スキル群 |
| ~100K pages | wiki エンティティ・コンセプトページ |

## 参考文献

- Garry Tan. "Meta-Meta-Prompting: The Secret to Making AI Agents Work" (2026-05-09). X Article. [[raw/articles/2026-05-09_garrytan_meta-meta-prompting]]
- Garry Tan. "Fat Skills, Fat Code, Thin Harness" (preceding article in series). [[entities/garry-tan]]
- YC Lightcone Podcast. "Tokenmaxxing: How Top Builders Use AI To Do The Work Of 400 Engineers" (2026-05-08)
