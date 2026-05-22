---
title: "Hermes Agent"
type: entity
aliases:
  - hermes-agent
  - nous-hermes
tags:
  - entity
  - ai-agents
  - open-source
  - nous-research
  - self-improving
status: complete
description: "Nous Research製open-source self-hosted AI agent。Persistent memory、self-improving skills、always-on executionが特徴。OpenClawから移行中のユーザーが増加。"
created: 2026-04-27
updated: 2026-05-22
sources:
  - "https://x.com/i/article/2045080054917476451"
  - "raw/articles/2026-04-28_15-hermes-agent-features.md"
  - "https://x.com/i/article/2045935785661349956"
  - "raw/articles/2026-05-13_nvidia_rtx-ai-garage-hermes-agent-dgx-spark.md"
  - "raw/articles/2026-05-06_kilo_hermes-vs-openclaw-when-to-reach.md"
  - "raw/articles/2026-05-15_shann_hermes-agent-operator.md"
  - "raw/articles/2026-05-22_deeplearning-ai_hermes-vs-openclaw-newsletter.md"
  - "https://info.deeplearning.ai/hermes-vs.-openclaw-cybersecurity-alarms-ring-more-interactive-conversations-can-agents-do-human-work"
related:
  - "[[concepts/harness-engineering]]"
  - "[[concepts/hermes-agent-use-cases]]"
  - "[[concepts/polymarket-trading-agents]]"
  - "[[concepts/nvidia-rtx-ai-garage]]"
  - "[[entities/openclaw]]"
  - "[[comparisons/hermes-vs-openclaw-architecture]]"
  - "[[entities/qwen]]"
  - "[[entities/nvidia-dgx-spark]]"
  - "[[nous-research]]"
---

# Hermes Agent

> **Definition:** Nous Researchが開発したopen-source self-hosted AI agent。Persistent memory、self-improving skills、always-on executionの3層モデルが特徴。

## 基本情報
- **開発元:** Nous Research（YaRN, Nomos, Psycheモデルファミリで知られる）
- **リリース日:** 2026年2月25日
- **ライセンス:** open-source
- **対応OS:** Linux, macOS, WSL2（Windows native非対応）

## 3層モデル

### Knowledge Layer
- built-in memory、session search、LLM-Wiki skill
- Honcho integration（optional）
- エージェントは答えるだけでなく、時間をかけて知識を蓄積

### Execution Layer
- multi-agent profiles、child agents、tool system
- MCP support、persistent machine access
- タスクを分解し、並列実行し、委任

### Output Layer
- cron jobs、gateway delivery（Telegram/Slack/Discord）
- Web UI、file output
- 結果がチャットウィンドウに閉じ込めず、real workflowにflow

## 3つの差別化ポイント

### 1. Persistent Memory
- MEMORY.md（環境事実、規約、経験）とUSER.md（ユーザー設定、通信スタイル、期待値）の2つのcore memoryファイル
- 全てのセッションでfrozen snapshotとしてロード
- 会話履歴をSQLite DB（full-text search）で保存。検索/要約/取得可能

### 2. Self-Improving Skills
- 複雑なタスク（5+ tool calls）完了後、自動的にskillをcreate
- 構造化markdownファイルでprocedure、pitfalls、verification stepsをキャプチャ
- 類似タスクでそのskillをloadして高速・正確に実行
- `~/.hermes/skills/`に読み書き可能なmarkdownファイルとして保存

**Curator システム**（DeepLearning.AI 2026年5月）:
- 90日以上未使用のスキルをバックグラウンドでアーカイブ
- LLMが各スキルの keep / merge / archive を判定
- スキルの爆発的増加を緩和する仕組み（ただし完全な防止には至っていない。[[comparisons/hermes-vs-openclaw-architecture|アーキテクチャ比較]]参照）

### Agentic Loop（DeepLearning.AI 2026年5月）
Hermesの内部ループ:
1. **Prompt Assembly** — personality (SOUL.md) + instructions + tools + skills + memory + conversation history
2. **Summarization** — 文脈窓を超える場合、古いメッセージを圧縮
3. **LLM送信** — 組み立てたプロンプトをモデルに送信
4. **Dispatch** — tool call / skill execution / user response のいずれかを実行
5. **Loop** — 最終応答まで繰り返し

このループはOpenClawのGateway-drivenアプローチと対照的。Hermesはagent-centric、OpenClawはgateway-centric。→ [[comparisons/hermes-vs-openclaw]]

### 3. Always-On Execution
- 24/7サーバー上で稼働
- Telegram、Discord、Slack、WhatsApp、Signal、Email、15+プラットフォームにsingle gatewayで接続
- natural-language cron（"毎朝8時にこれらのGitHubリポジトリをスキャンして要約"）
- 無監視で実行

## OpenClawとの比較

| 特徴 | OpenClaw | Hermes |
|------|----------|--------|
| Learning Loop | static（手動skillインストール） | closed loop（~15 tool callsでskill生成） |
| Memory | 手動セットアップ/サードパーティ依存 | built-in bounded curated memory |
| Self-improvement | なし | あり（使用ほど賢くなる） |
| Platform統合 | 50+（広範） | 15+（主要すべて） |
| セキュリティ | 標準 | 強い |
| Token効率 | **高い**（必要なツールのみロード） | **低い**（全bundled skills 123+をロード、コスト高め） |

## Milestones (May 2026)

- **150,000 GitHub Stars**: 3ヶ月未満で達成（2026年5月19日時点）。Shann (@shannhk) の記事で確認
- **Most Used Agent on OpenRouter**: OpenRouterのアプリ利用統計で世界1位（2026年5月第2週）。全モデル・フレームワーク中でグローバルトークン使用量最大
- **NVIDIA RTX AI Garage Endorsement**: NVIDIA公式ブログでHermes AgentがRTX AI Garageプログラムの中心的エージェントフレームワークとして紹介（2026-05-13）
- **123 Bundled Skills**: 出荷時点で123のスキルを内蔵。GitHub PRs、Obsidian、Google Workspace、Linear、Notion、Typefully、Perplexity、Deep Research等
- **6 Deployment Targets**: Local、Docker、SSH、Daytona、Singularity、Modal
- **20+ Messaging Surfaces**: Telegram、Discord、Slack、Email、Voice、CLI

### Harness Engineering: "Same Model, Better Results"

NVIDIAブログで明示的に言及された重要な特徴：**同一モデルを異なるフレームワークで比較した際、Hermesが一貫して優れた結果を出す**。これはHermesが単なるthin wrapperではなく、active orchestration layerとして機能するため。→ [[concepts/harness-engineering]]

### NVIDIA DGX Spark 統合

DGX SparkはHermes Agentの理想的なハードウェアとして位置づけられている：
- **128GB unified memory**で120BクラスのMoEモデルを終日稼働
- **Qwen 3.6 35B**（20GBメモリで120B級の知能）がDGX Spark上で推奨
- **Hermes DGX Spark Playbook**: NVIDIA公式のセットアップガイドが利用可能
- 常時稼働エージェント（always-on agent）としての設計がDGX Sparkの24/7運用と整合

→ [[entities/nvidia-dgx-spark]], [[concepts/nvidia-rtx-ai-garage]]

## 実際の使用例（Reddit/X/YouTube調査）

1. **📞 Pre-call client research** — 会議前にリレーションをauto-enrichしたdossierを作成（20-30分節約）
2. **✉️ Meeting-note to follow-up** — 粗いノートをpolished follow-upに変換、TODOsをObsidianに書き込み
3. **🎧 Weekly podcast digest** — Voxtral + Mistral Large 3 pipelineで10時間→2時間のhighlights reel
4. **📬 Daily news briefings** — $5 VPS + GitHub student plan + Gemini + Ollamaでcron配信
5. **⚙️ Content-ops pipeline** — ブログ作成、cold emails、YC/X/Reddit lead scraping
6. **💬 24/7 personal assistant** — Telegram/WhatsApp across channels、Persistent memory
7. **🛡️ Agent watchdog** — OpenClawのmonitoringにHermesを2時間cronで配置、障害検知→自動復旧（15秒以内）


## 15 Features Deep Dive (April 2026)
The article "15 Hermes Agent features you've never touched" (2791 bookmarks, 913 likes, 350K impressions) covers advanced features including:
- Web search and content extraction capabilities
- Cron job automation for recurring tasks
- Skill-based procedural memory system
- Entity and concept wiki management
- Multi-agent orchestration patterns
- Filesystem and terminal integration

## Execution Specialist Role (Dual-Agent Architecture)

Hermes Agent is increasingly used as an **execution specialist** in a dual-agent architecture where OpenClaw serves as the orchestrator and Hermes handles fast, repeatable task execution. They communicate via the **Agent Client Protocol (ACP)**.

This architecture pattern is validated by:
- **Kilo blog analysis** (Brendan O'Leary, May 2026): "OpenClaw as orchestrator (planning, decomposition, multi-step coordination, scheduling) and Hermes as execution specialist (fast, repeatable task loops)"
- **Kilo Reddit analysis** (1,300+ comments): ~20% of users run both tools together with this pattern
- **popularaitools.ai**: "Hermes is significantly faster than OpenClaw on the same model and more lightweight"

### Why Hermes as Execution Specialist

| Strength | Mechanism |
|----------|-----------|
| **Speed** | "Noticeably faster" than OpenClaw on same model — lightweight agent loop |
| **Learning loop** | Self-improving skills get faster/more accurate on repeatable task types |
| **Sandbox backends** | 5 isolated environments (Local, Docker, SSH, Singularity, Modal) |
| **Subagent delegation** | `delegate_task` spawns child agents with isolated contexts for parallel work |
| **Checkpoint/rollback** | Filesystem snapshots before file operations; `/rollback` on failure |
| **execute_code sandbox** | Mechanical pipelines separated from reasoning-heavy subagent delegation |

### ACP Communication

Hermes communicates with OpenClaw via ACP (Agent Client Protocol), the open standard for agent-to-agent communication. OpenClaw spawns Hermes as an ACP session via `sessions_spawn({ runtime: "acp", agentId: "hermes" })`, treating Hermes as an interchangeable execution backend.

**Key limitation:** Hermes's self-evaluation always passes, so external validation is needed. The dual-agent architecture mitigates this — OpenClaw (orchestrator) validates Hermes (executor) output quality.

See [[comparisons/hermes-vs-openclaw-architecture]] for the full comparison.

## Shann's 4-Level Fleet Operation Model (May 2026)

Shann (@shannhk)、EspressioのAIマーケターでHermesエージェントを全面的に運用している実践者によるマルチエージェント運用ガイド（[How to Become a Hermes Agent Operator](https://x.com/i/article/2055317817658900480), 2026-05-15）。

### 3つのコアコンポーネント
- **Brain** — `~/.hermes/memories/` にMEMORY.md（ビジネス事実）とUSER.md（ユーザー設定）。全セッション開始時に注入。SQLite+FTS5でセッション横断検索
- **Personality** — `soul.md` でトーン定義。簡潔・皮肉・率直・フォーマル等、1つの基盤で6エージェントに異なる人格を付与可能
- **Skillset** — 123の既製スキル + 自己改善ループ。エージェントが働く過程で新スキルを自動生成

### 4段階セットアップモデル

| Level | 構成 | ユースケース |
|-------|------|-------------|
| **Level 1** | 単一エージェント + コントロールルーム | 個人アシスタント、初期セットアップ |
| **Level 2** | 複数スペシャリスト（直接対話） | 役割分離、認証情報スコープ分割 |
| **Level 3** | Orchestrator + Specialists + Task Bus | 部門横断ワークフロー、委任と統合 |
| **Level 4** | Level 3 + Cron自動化 | 週次SEOレポート、サーバーヘルスチェック、完全自律運用 |

### Control Room パターン
```
/root/vps-agents/          → コントロールプレーン（ドキュメント、ルール、ランbook）
                             生のシークレットは一切置かない

/srv/<agent-name>/data/    → ライブランタイム（シークレット、メモリ、スキル、セッション、cron）
                             各Hermesエージェントの実体
```

### SEO Agent 21-Step Pipeline（実運用ケーススタディ）

全工程を1つのDockerコンテナで実行。3つのサブエージェントがフェーズごとにコンテキストを切り替え：

| Phase | Steps | 内容 |
|-------|-------|------|
| Research + Ideate | 01-07 | キーワードシード→SERPスナップショット→競合抽出→意図分析→コンテンツギャップ→内部/外部検証 |
| Production | 08-15 | アングルブリーフ→ビジュアル戦略→アウトライン→ドラフト→画像生成→フローチャート→QA |
| Distribution | 16-21 | 公開準備→スキーマ→内部リンク→シンジケーション→分析→モニタリング |

### Prototype → Production 方法論

```
Prototype (Hermes上) → 2-3回実運用テスト → 専用WorkspaceでFine-tune → VPSにデプロイ + Cron
```

Shann曰く: 「production agentをゼロから書くことはできない。育てるしかない。Hermesはその育成を高速化する。」

### Rails vs Linux フレーミング
ShannによるHermesとOpenClawの哲学的対比：
- **Hermes = Rails**: 意見の強いデフォルト、バッテリー同梱、エージェントがより多くの判断を行う
- **OpenClaw = Linux**: プリミティブ、保証、明示的制御、エージェントは言われたことだけを行う

### モデル運用戦略
- **Claude Opus 4.7**: クリエイティブ作業（コピーライティング、ボイス、フック生成）
- **Codex (GPT 5.5)**: 構造化作業（コーディング、計画、マルチステップワークフロー、ブラウザ自動化）
- 両方併用。Tool Gateway経由でエージェント・タスク単位でモデル切替

→ [[entities/shannhk]], [[concepts/hermes-agent-use-cases]]

## Sources
- [Hermes Agent: What People Are Actually Using It For](https://x.com/i/article/2045935785661349956) (2026-04-26, X article) — usage patterns from Reddit/X/YouTube
- [Hermes Agent + Polymarket - weather trading guide](https://x.com/i/article/2045080054917476451) (2026-04-25, X article) — installation + Polymarket trading
- [How to Become a Hermes Agent Operator](https://x.com/i/article/2055317817658900480) (2026-05-15, Shann/@shannhk, X article) — 4-level fleet operation model, SEO agent 21-step pipeline, prototype-to-production methodology

## References

- 2026-1-month-with-hermes
- hermes-architecture-analysis-kazuki-inamura

- 2026-04-27_2045080054917476451_Hermes-Agent-Polymarket-Self-Learning-Weather-Trading-Bot
- 2026-04-27_2045935785661349956_Hermes-Agent-What-People-Are-Actually-Using-It-For
- 2026-04-28_x-article-15-hermes-agent-features
- 2042539396638085339_What-Hermes-Agent-Can-Do-for-You
