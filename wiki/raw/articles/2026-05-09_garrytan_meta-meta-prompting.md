---
type: x_article
title: "Meta-Meta-Prompting: The Secret to Making AI Agents Work"
author: Garry Tan
author_handle: garrytan
author_id: "11768582"
date: 2026-05-09
created_at: "2026-05-09T14:58:40.000Z"
source_url: https://x.com/garrytan/status/2053127519872614419
article_url: https://x.com/i/article/2052898104039657472
tweet_id: "2053127519872614419"
article_id: "2052898104039657472"
public_metrics:
  retweet_count: 437
  reply_count: 119
  like_count: 3262
  quote_count: 103
  bookmark_count: 10284
  impression_count: 1212854
tags: [agentic-engineering, harness-engineering, personal-ai, workflow, multi-agent, agent-architecture]
summary_source: abmedia.io (GetXAPI unavailable; Chinese-language detailed summary used)
summary_url: https://abmedia.io/garry-tan-meta-meta-prompting
---

# Meta-Meta-Prompting: The Secret to Making AI Agents Work

*Original by Garry Tan (@garrytan), CEO of Y Combinator. Published 2026-05-09. ~1.2M impressions, 10K+ bookmarks.*

*Note: Full article body unavailable (X Article auth wall, GetXAPI key not set). This is a reconstructed summary based on web_extract preview and the detailed Chinese-language summary by ABMedia (abmedia.io).*

---

## 概要

Garry Tan は、AI を「チャットウィンドウ」としてではなく「オペレーティングシステム」として扱うことで、5ヶ月前から再び builder に戻ったと語る。彼は現在、100以上の AI skills と約10万ページの構造化 knowledge base を運用し、AI agent が継続的に記憶・蓄積・更新・連携する「複利システム（compound AI system）」を構築している。

## コア概念

### Fat Skills, Fat Code, Thin Harness

Garry Tan の AI agent アーキテクチャ哲学：

- **Harness（runtime/router）** — 薄くあるべき（thin）
- **Skills** — 太くあるべき（fat）。再利用可能・テスト可能・組み合わせ可能なワークフローモジュール
- **Code** — 太くあるべき（fat）。実際のロジックと知識の集積
- **モデルはエンジン、残りが車** — モデル選択は重要だが、真の価値は知識・ワークフロー・データにある

### Personal AI OS（個人用 AI オペレーティングシステム）

- 各人物・会社・会議・書籍・Podcast・記事・アイデアごとに専用ページを作成
- 会議後は AI が自動で transcript 作成、サマリー生成、人物ページ更新、会社ページ更新、タイムライン更新、open threads 更新、relationship context 更新
- AI は「ファイルキャビネット」ではなく「神経システム」として機能

### Skillify — Meta-Skill

最も重要な技能：

1. 繰り返し発生するワークフローを発見
2. `skillify this` と指示
3. システムが操作を分析し、再利用可能パターンを抽出
4. skill file を作成し、resolver routing system に追加
5. 以降の全ワークフローに蓄積

### 複利効果（Compound Effect）

- 各書籍、各会議、各 skill 改善、各データ更新が継続的に蓄積
- システム全体が複利的に成長し、時間とともに加速度的に賢くなる
- Tan は「未来は集中型 AI ツールを使う人ではなく、compound AI systems を構築する人に属する」と主張

## Book Mirror プロセスの事例

Pema Chödrön の *When Things Fall Apart* を読んだ際のワークフロー：

1. 全22章を分解
2. 複数 sub-agent が並列実行:
   - 著者の視点を要約
   - 各視点を Garry Tan 自身の人生にマッピング（家族背景、起業歴、YC 仕事、深夜ノート、読書記録、セラピストの議論、起業家との対話）
3. 3万語の「brain page」を出力
4. 所要時間：約40分

## マルチモデルアーキテクチャ

| モデル | 用途 |
|--------|------|
| Claude Opus 4.7 | 精密作業（precision） |
| GPT-5.5 | 想起・抽出（recall & extraction） |
| DeepSeek V4-Pro | 創造的作業（creative work） |
| Groq + Llama | 高速推論 |
| OpenClaw + Hermes Agent | ルーティング（routing） |

## 主要 Skills 例

- meeting-ingestion
- media-ingest
- enrich
- perplexity-research
- investor-update-ingest
- email-triage
- calendar-check
- Skillify（meta-skill）

## 重要な引用

- 「未来は compound AI systems を構築する人に属する」
- 「モデルはエンジン。他の部分が車だ」
- 「AI は builder の喜びを私に返してくれた」
- 「今はほとんど AI に prompt を書かない。本当に重要なのは skill system」

## Hermes Agent との関連性

この記事が説明するアーキテクチャは、Hermes Agent の設計思想と深く共鳴する：

- **Thin Harness** = Hermes Agent の軽量ランタイム
- **Fat Skills** = Hermes のスキルシステム
- **Fat Code** = wiki の知識ベースとツール群
- **Skillify** = Hermes の `skill_manage(action='create')` による自動スキル化
- **10万ページ knowledge base** = wiki の構造化ナレッジベース
- **Multi-model routing** = Hermes のマルチプロバイダ対応
