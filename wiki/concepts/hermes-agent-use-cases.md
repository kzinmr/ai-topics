---
title: "Hermes Agent Use Cases — 7 Canonical Workflows"
created: 2026-05-09
updated: 2026-05-09
type: concept
tags:
  - ai-agents
  - ai-agent-engineering
  - workflow
  - automation
  - cron
  - agentic-engineering
  - multi-agent
  - nous-research
  - comparison
sources:
  - raw/articles/2026-04-19_mvanhorn_hermes-agent-use-cases-30days.md
related:
  - "[[entities/hermes-agent]]"
  - "[[concepts/agentic-engineering]]"
  - "[[concepts/cron-job-patterns]]"
---

# Hermes Agent Use Cases — 7 Canonical Workflows

> **Source:** Matt Van Horn (@mvanhorn) による Reddit/X/YouTube 直近30日間コミュニティ分析（2026年4月19日）。90 Reddit threads、80 X posts、55 YouTube videos、計350万ビュー超のデータから抽出された7つの標準ワークフロー。

## 7 Canonical Use Cases

### 1. 📞 Pre-call Client Research
**ビジネス最高シグナルのユースケース。** 会議前に相手の情報を自動収集し dossier を作成。1回あたり20-30分節約。
- ソース: r/hermesagent "How are you actually using Hermes for your business?" (19 comments)
- 派生: LinkedIn research, company-news digests, "what did they ship recently"

### 2. ✉️ Meeting-note to Follow-up Drafting
粗いノートを polished follow-up に変換。TODOs を Obsidian の TODOS.md に既存タグスタイルで書き込み。
- Integration 不要 — agent + notes file + draft のみ
- キー要件: セッションを跨いだタグ規則の記憶（persistent memory）

### 3. 🎧 Weekly Podcast Digest
Voxtral で文字起こし → Mistral Large 3 で関心領域にランク付け → ハイライトリールに編集。
- 10時間のポッドキャスト視聴 → 2時間のハイライトに圧縮 (r/MistralAI, 39 upvotes)
- 亜種: 10分クリップ/ポッドキャスト (r/openclaw)、長尺YouTube処理

### 4. 📬 Daily News Briefings (Telegram/Discord)
最も一般的なエントリーポイント。
- $5 VPS + GitHub student plan + Gemini API + Ollama で稼働
- DevOps派生: SSLチェック、uptime監視、サーバーステータスのDiscord通知

### 5. ⚙️ Content-Ops Pipeline
ブログ作成、cold emails、YC/X/Reddit lead scraping。OpenClaw からの移行動機。
- マルチエージェント Telegram チェーン: リサーチ→ドラフト→レビュー→公開 (r/AISEOInsider)
- 共有フォルダ経由の調整

### 6. 💬 24/7 Personal Assistant (Telegram/WhatsApp)
最大のコンシューマー用途。
- 1つのHermesインスタンス、全チャンネル、セッション跨ぎのpreference記憶
- 廉価版: Raspberry Pi + Qwen 3.5 (4B) で $10/月 (r/hermesagent 160 upvotes)
- 上級版: 複数インスタンス + カスタム Obsidian メモリレイヤー (Alex Finn, 105K views)

### 7. 🛡️ Agent Watchdog & Auto-Healer
上級運用パターン。
- HermesがOpenClawを2時間cronで監視、異常検知→config修復→再起動 (11秒ダウンタイム)
- リアルタイム版: Codex + GPT-5.4 を Hermes-driven workflow の監視役に (@gkisokay, 70 likes)

## 🧵 The Three Shared Properties

すべての成功ワークフローに共通する3つの設計原則：

| 原則 | 意味 |
|------|------|
| **Scheduled** | cron または event-driven。対話的に使われることは稀 |
| **File-based** | Markdown、JSON、プレーンテキストの読み書きが中心 |
| **Pushes to messenger** | 結果はダッシュボードではなく Telegram/Discord 等に配信 |

### なぜこれが重要なのか
- これらの原則は **agent-first architecture** の自然な帰結である
- 対照的に、OpenClaw の gateway-first 設計では messenger が push 元であり、受信がデフォルト
- 「ダッシュボードを開かせる」のではなく「結果を届ける」パラダイム

## 🔄 The Self-Evolving Skill Loop

| 実行回数 | Tool Calls | 説明 |
|----------|-----------|------|
| 1回目 | 23 | 探索的、非効率 |
| 3回目 | 6 | skill化により74%削減 |
| それ以降 | 3-6 | 安定、compound効果 |

**重要な洞察:** ほとんどのユーザーは学習ループのために Hermes をセットアップしない。朝7時の digest が欲しくてセットアップする。学習ループは「なぜ止めないのか」の理由である。

## 📊 Data Sources (30-day window ending 2026-04-19)

| Platform | Volume | Key Metric |
|----------|--------|------------|
| Reddit | 90 threads | 3,012 upvotes, 2,437 comments |
| X | 80 posts | 8,442 likes, 519 reposts |
| YouTube | 55 videos | 3,502,384 views |
| TikTok | 90 videos | 1,545,693 views |
| Instagram | 65 reels | 55,172 views |
| GitHub | 40 items | 308,612 reactions |
| Hacker News | 4 stories | 13 points |

### Top Voices
- **X:** @NousResearch, @AlexFinn, @gkisokay
- **Reddit:** r/hermesagent, r/openclaw, r/LocalLLaMA

## 📎 See Also

- [[entities/hermes-agent]] — Hermes Agent の基本情報と3層モデル
- [[concepts/hermes-agent-architecture]] — AIAgent中心のアーキテクチャ詳細
- [[comparisons/hermes-vs-openclaw-architecture]] — OpenClawとの比較
- [[concepts/agentic-engineering]] — Agentic Engineeringの方法論
- [[concepts/cron-job-patterns]] — Cron jobによる自動化パターン
