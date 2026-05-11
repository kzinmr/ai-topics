---
title: "Garry Tan"
aliases: ["@garrytan"]
type: person
x_handle: garrytan
x_id: "11768582"
created: 2026-05-11
tags:
  - personal-ai
  - agentic-engineering
  - harness-engineering
  - ai-agents
  - workflow
roles:
  - President & CEO, Y Combinator (2023–present)
  - Co-founder, Initialized Capital (2015–2023)
  - Partner, Y Combinator (2011–2015)
  - Co-founder, Posterous (2008–2012)
  - Early employee, Palantir Technologies
education:
  - BS Computer Systems Engineering, Stanford University
related:
  - entities/openclaw
  - entities/hermes-agent
  - concepts/meta-meta-prompting
  - concepts/harness-engineering
sources:
  - raw/articles/2026-05-09_garrytan_meta-meta-prompting.md
  - https://en.wikipedia.org/wiki/Garry_Tan
  - https://www.ycombinator.com/people
---

# Garry Tan

Garry Tan（@garrytan）は Y Combinator の President & CEO。エンジニア・デザイナー出身のベンチャーキャピタリストであり、AI agent 時代における **Personal AI OS** と **Meta-Meta-Prompting** の提唱者として知られる。

## 経歴

| 時期 | 役割 |
|------|------|
| 2005–2008 | Microsoft → Palantir Technologies（10人目の従業員、デザイナー・エンジニアリングマネージャー） |
| 2008–2012 | Posterous 共同創業（YC S08、2012年に Twitter が $20M で買収） |
| 2011–2015 | Y Combinator パートナー（Bookface・Demo Day サイト構築） |
| 2013– | Posthaven 共同創業 |
| 2015–2023 | Initialized Capital 共同創業・マネージングパートナー |
| 2023–現在 | Y Combinator President & CEO |

## AI Builder としての側面

Tan は VC でありながら現役の builder であることを重視し、**深夜までコードを書く CEO** として知られる。

### G Stack

YC の枠を超えて個人開発した AI agent システム。Claude Code 上に構築され、以下の機能を持つ：

- `/office-hours` — YC の創業者評価プロセスをシミュレートする skill
- 製品スコーピングからデプロイまでの AI エンジニアリングチーム
- 構造化プロセス、定義された役割、厳格なレビュー

### 「Meta-Meta-Prompting」フレームワーク（2026年5月）

2026年5月9日に公開した長文 X Article で提唱した AI agent 設計哲学。[[concepts/meta-meta-prompting]] に詳細。

**核心的主張**:
- AI に prompt を書く時代は終わり、**skill system** を構築する時代へ
- **Fat Skills, Fat Code, Thin Harness** — harness は薄く、skill と知識は厚く
- モデルはエンジンであり、真の価値は知識・ワークフロー・データにある
- 100以上の AI skills と約10万ページの knowledge base を個人で運用
- **Skillify** — 繰り返しワークフローを自動的に skill 化する meta-skill

### 先行記事: 「Fat Skills, Fat Code, Thin Harness」

Meta-Meta-Prompting の前段となる記事で、harness architecture の基本原則を解説。

### マルチモデル戦略

| モデル | 用途 |
|--------|------|
| Claude Opus 4.7 | 精密作業 |
| GPT-5.5 | 想起・抽出 |
| DeepSeek V4-Pro | 創造的作業 |
| Groq + Llama | 高速推論 |
| OpenClaw + Hermes Agent | ルーティング |

### 主要 Skills

- `meeting-ingestion` — 会議の自動取り込み・構造化
- `media-ingest` — メディアコンテンツの取り込み
- `enrich` — 既存 knowledge base の強化
- `perplexity-research` — 調査 research
- `investor-update-ingest` — 投資家向けアップデート処理
- `email-triage` — メールの自動仕分け
- `calendar-check` — カレンダー管理
- `Skillify` — meta-skill（ワークフローの自動 skill 化）

## Hermes Agent との関係

Garry Tan のシステムは **OpenClaw と Hermes Agent をルーティング層として使用**している。彼の「Fat Skills, Fat Code, Thin Harness」アーキテクチャは Hermes Agent の設計思想と以下のように対応する：

| Tan の概念 | Hermes Agent での実装 |
|-----------|----------------------|
| Thin Harness | コアランタイム |
| Fat Skills | スキルシステム |
| Skillify | `skill_manage(action='create')` |
| Knowledge Graph | wiki |
| Multi-model routing | マルチプロバイダ対応 |

## 参考リンク

- X: [@garrytan](https://x.com/garrytan)
- Y Combinator: [ycombinator.com](https://www.ycombinator.com/)
- Wikipedia: [Garry Tan](https://en.wikipedia.org/wiki/Garry_Tan)
- YouTube: [Garry Tan](https://www.youtube.com/@garrytan) — スタートアップ戦術の教育コンテンツ
