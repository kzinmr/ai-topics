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
updated: 2026-04-30
sources:
  - "https://x.com/i/article/2045080054917476451"
  - "raw/articles/2026-04-28_15-hermes-agent-features.md"
  - "https://x.com/i/article/2045935785661349956"
related:
  - "[[concepts/harness-engineering]]"
  - "[[concepts/polymarket-trading-agents]]"
  - "[[entities/openclaw]]"
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

## Sources
- [Hermes Agent: What People Are Actually Using It For](https://x.com/i/article/2045935785661349956) (2026-04-26, X article) — usage patterns from Reddit/X/YouTube
- [Hermes Agent + Polymarket - weather trading guide](https://x.com/i/article/2045080054917476451) (2026-04-25, X article) — installation + Polymarket trading

## References

- 2026-1-month-with-hermes
- hermes-architecture-analysis-kazuki-inamura

- 2026-04-27_2045080054917476451_Hermes-Agent-Polymarket-Self-Learning-Weather-Trading-Bot
- 2026-04-27_2045935785661349956_Hermes-Agent-What-People-Are-Actually-Using-It-For
- 2026-04-28_x-article-15-hermes-agent-features
- 2042539396638085339_What-Hermes-Agent-Can-Do-for-You
