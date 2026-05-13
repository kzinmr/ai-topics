---
title: Max Rumpf
type: entity
aliases: [Maximilian-David Rumpf, maxrumpf]
created: 2026-05-13
updated: 2026-05-13
status: L2
sources: [https://maxrumpf.com/, https://www.sid.ai/, https://www.sid.ai/research/sid-1, https://www.sid.ai/research/sid-1-technical-report, https://x.com/maxrumpf, https://ycombinator.com/companies/sid]
tags: [person, ai-research, information-retrieval, reinforcement-learning, grpo, blogger, x-account, ycombinator]
---

# Max Rumpf

Max Rumpf（Maximilian-David Rumpf）は SID.ai の CEO / Co-founder。AI検索・情報検索（retrieval）の研究ラボを率い、SID-1 の開発を主導。ETH Zürich で AI アクセラレーター設計の研究者としてキャリアを開始し、YC S23 バッチで起業。SID-1 は agentic retrieval のための最初のエンドツーエンド RL 訓練モデルであり、GRPO を用いた検索特化型モデルとして注目を集めている。

## プロフィール

| 項目 | 内容 |
|------|------|
| 氏名 | Maximilian-David "Max" Rumpf |
| 役職 | CEO / Co-founder, SID.ai |
| 所在地 | San Francisco, CA |
| X | [@maxrumpf](https://x.com/maxrumpf)（1,125 posts, ~2,456 followers） |
| LinkedIn | [/in/maximiliandavid](https://linkedin.com/in/maximiliandavid) |
| 個人サイト | [maxrumpf.com](https://maxrumpf.com/) |

## 経歴

### ETH Zürich（2020-2023）
SAFARI Research Group で研究者として、Google の TPU アーキテクチャを開発した教授の下で AI アクセラレーター設計に従事。Teaching Assistant として情報セキュリティ・暗号研究グループでも活動。CS Master 学生として在籍中に SID を共同創業。

### Studienstiftung des deutschen Volkes（2018-2023）
ドイツ国家優秀奨学金（ドイツ人学生の上位0.5%に授与）を受賞。

### SID.ai（2022-現在）
2022年に Lotte Seifert（COO）、Lukas Ruflair と共同で SID を創業。YC S23 バッチ採択。San Francisco と Zürich にオフィスを構える AI 検索の研究ラボ。

## SID.ai

「検索を1モデルずつ解決する（Solving retrieval one model at a time）」を掲げる AI 研究ラボ。2023年5月に $500K のプレシード調達。投資家：Y Combinator、Canaan、Rebel、General Catalyst。個人投資家/アドバイザーとして Anthropic、DeepMind、OpenAI、MIT、Cognition、Cursor、Applied Compute、Prime Intellect、Standard Intelligence、Jeff Dean の研究者が参加。

### ピボットの歴史
- **2023年初頭**: B2C のパーソナルデータ検索「Sid Search」（「データの Stripe」として位置づけ）
- **2023年半ば（YC前後）**: RAG / データコネクターにピボット — 「Serverless RAG to connect AI to company, industry, or person-specific data」
- **2025年末**: SID-1 発表 — 汎用 RAG プロバイダーから retrieval 特化モデルの研究ラボへ

## SID-1（2025年12月）

SID-1 は **agentic retrieval** のためにエンドツーエンドで強化学習（RL）された最初のモデル。Magistral の修正版 GRPO を SFT なしで使用。

**従来の検索パイプラインとの違い**: クエリ書き換え→検索→リランキングという固定パイプラインではなく、SID-1 は人間のように「検索→結果を読む→クエリを改良」を必要なだけ反復する。

### パフォーマンス比較

| モデル | Recall | 所要時間 | コスト/質問 |
|--------|--------|----------|------------|
| **SID-1 (4x)** | **0.84** | 5.5s | $0.0014 |
| SID-1 | 0.77 | 5.5s | $0.00062 |
| GPT-5.1 (high) | 0.78 | 131s | $0.24 |
| Gemini 3 Pro | 0.66 | 156s | $0.12 |
| Sonnet 4.5 | 0.64 | 35s | $0.54 |
| Reranker @10 | 0.45 | 0.78s | $0.00061 |
| Vector only @10 | 0.44 | 0.15s | $0.0000098 |

**Key metrics**:
- GPT-5.1 比 **24倍高速**（5.5s vs 131s）、**3-4桁低コスト**
- 従来のリランキングパイプライン比で **recall 約2倍**（0.45→0.84）
- 既存検索システムに **ドロップイン互換**、フロンティアモデルのサブエージェントとして動作
- API、AWS Bedrock、セルフホストで提供

## 代表的エッセイ

### Robots Might Be 1000x Harder Than Superintelligence（2024年10月）
Moravec's Paradox の再解釈。人間の脳は数百万年にわたって物体操作と空間移動を最適化してきたが、数学は高々1000年の歴史しかない。機械学習の用語で言えば「数学はモンキーブレインにとって分布外（out-of-distribution）」。ナビゲーションや物体操作という基盤タスクは数学より1000倍難しい可能性があるが、人間があまりに上手いためその複雑さが見えない。

> "A good razor is that if our ancestors were doing it millions of years ago, it could be hard for AI. If the task is only thousands of years old, it's most likely pretty easy."

### Just-In-Time Coding（2024年8月）
JIT コンパイルの概念を AI コード生成に拡張。プログラム実行中に初めてコードが書かれる世界を描く。React ボタンは ~100 tokens、Groq なら TTFT 200ms + 500 tokens/s = 約400ms。Salesforce のボタンより速い。ボタン→ページ→アプリケーションへと拡張可能。

> "The code only gets written during the execution of the program."

### N-of-1 Software（2024年8月）
AI がソフトウェアを「n-of-1-billion」から「n-of-1」へ変えるというビジョン。Excel が SaaS よりも優れている理由はカスタマイズ性 — AI がそれを全ソフトウェアにもたらす。

> "AI lets us create n-of-1 software: Software that only serves a single person."

### Amdahl's Argument for AI（2024年4月、X スレッド）
Amdahl の法則を AI プロダクティビティに適用。AI アプリの生産性向上は、人間が介在しなければならないワークフローの割合によって上限が決まる。人間の処理速度は ~1-3 tokens/sec で事実上高速化できない。

### Arxiv Might Kill Small Universities and Labs（2024年5月、X スレッド）
arXiv のオープンアクセスを評価しつつ、フィルタリングされない出版がアカデミアの信用構造に与える二次的影響を問題提起。

## 発言・思想

### RL フレームワークの不安定性（2025年12月、ピン留め投稿）
> "Most RL frameworks are fundamentally unstable. We wasted more H100 hours on debugging this than any other issue for our multi-turn, multi-env RL run. When using OpenAI-style messages for env interactions, parsing and retokenizing leads to subtly different tokens."

SID-1 の訓練で直面した GRPO マルチターン RL の実践的課題。トークン化の微妙な差異が訓練安定性を損なう問題を指摘。

### エンタープライズAIと検索
Lukas Petersson の Audio Tokens ポッドキャストで「水平AIが垂直AIを置き換える」という議論に関連して、自律型 AI がプライベートデータにアクセスするには効果的な検索システムが不可欠だと論じた。

## ポッドキャスト出演

| 日付 | 番組 | テーマ |
|------|------|--------|
| 2024年7月 | High Agency: The Podcast for AI Builders (Ep.6) | 高度な RAG システムの構築、チャンキング戦略、ハイブリッド検索、知識グラフの限界、リランキング |
| 2025年3月 | Audio Tokens (Ep.9, Lukas Petersson) | AI エージェントのボトルネック、エンタープライズ AI 導入、欧州 vs SF |
| 2023年5月 | Before They Change The World | Stripe for data、YC 以前の創業ストーリー |

## 関連ページ

- [[sid-1]] — SID の最初の agentic retrieval モデル
- [[grpo]] — Group Relative Policy Optimization
- [[agentic-retrieval]] — エージェント型情報検索
- [[magistral]] — SID-1 訓練に使用された GRPO 修正版の開発元
- [[moravecs-paradox]] — 「Robots Might Be 1000x Harder」の基盤概念
- [[amdahls-law]] — Amdahl's Argument for AI の理論的基盤
- [[rag]] — Max が深い専門知識を持つ検索拡張生成
