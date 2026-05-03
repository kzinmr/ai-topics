---
title: "Vibe Coding"
type: concept
aliases:
  - vibe-coding
created: 2026-04-12
updated: 2026-05-03
tags:
  - concept
  - agentic-engineering
status: draft
sources:
  - "https://simonwillison.net/2026/Feb/23/agentic-engineering-patterns/"
  - "https://simonwillison.net/guides/agentic-engineering-patterns/"
  - "raw/articles/2025-04-27_karpathy-vibe-coding-menugen.md"
---

# Vibe Coding

Simon Willisonが定義する、**「コードに一切注目せずにLLMでコードを書く」開発スタイル**。

## 定義

> *"I think of vibe coding using its original definition of coding where you pay no attention to the code at all, which today is often associated with non-programmers using LLMs to write code."*

## Agentic Engineering との対比

| 次元 | Vibe Coding | Agentic Engineering |
|------|-------------|---------------------|
| ユーザー | 非プログラマー | プロフェッショナルエンジニア |
| 関与度 | コードを一切見ない | 既存知識をエージェントで増幅 |
| テスト | 省略されがち | 必須（Red/Green TDD） |
| 目的 | 動くコードを素早く作る | 品質と速度の両立 |
| 認知負債 | 高くなる傾向 | 意図的に低減 |

## Vibe Coding の課題

### 認知負債（Cognitive Debt）
> "When we lose track of how code written by our agents works we take on cognitive debt."

自分で書いているが、内容を理解していないコードが蓄積すると、将来的な機能追加や保守が困難になる。

### 解決策
- [[concepts/harness-engineering/agentic-workflows/linear-walkthroughs]] — エージェントにコード解説を生成させる
- [[concepts/interactive-explanations]] — 対話的アニメーションでアルゴリズムを理解
- [[concepts/agentic-manual-testing]] — 実行して動作確認

## Vibe Coding の価値

Simon自身もVibe Codingを否定しているわけではない。むしろ、**~40分のVibe Codingのおもちゃプロジェクトでも、新しいエコシステムを探索する機会になる**と評価。

> "Even a ~40 minute vibe coded toy project can become an opportunity to explore new ecosystems and pick up some interesting new tricks."

## 実践事例

### Xe Iaso: Sponsor PanelをVibe Codingで構築（2026年3月）

### Karpathy: MenuGen（2025年4月） — The Original Vibe Coding Case Study

Karpathy's own **MenuGen** (menugen.app) is the project that coined the term "vibe coding." 100% built via Cursor + Claude 3.7 -- Karpathy provided high-level direction without writing code directly. A production app with Clerk auth, Stripe payments, OpenAI OCR, and Replicate image generation.

**Post-mortem insights:**

| Insight | Detail |
|---------|--------|
| **80/20 Trap** | Local prototype was fast, but deploying a real app was a "painful slog." Felt 80% done but was closer to 20% |
| **API Hallucination** | OpenAI OCR -> LLM hallucinated deprecated APIs; Replicate -> heavy rate limiting + out-of-date docs |
| **Vercel Debugging** | Required "pushing fake debugging commits" to force redeploys |
| **Clerk Auth** | Claude hallucinated ~1000 lines of deprecated code; needed custom domain, DNS, Google Cloud Console OAuth config |
| **Stripe Logic Error** | Claude matched payments to users via email (wrong -- Stripe email != Google OAuth email). Karpathy caught it |
| **LLM Gaslighting** | When corrected, LLM "thanks me... and tells me it will do it correctly in the future, which I know is just gaslighting" |
| **No State** | Skipped database (Supabase) and queues (Upstash) as "too much bear" -- app prone to timeouts |

**Four demands from Karpathy for the vibe coding era:**
1. **Batteries-Included Platforms** -- "opposite of Vercel Marketplace" pre-configuring domain, auth, payments, DB
2. **LLM-Friendly Services** -- docs in Markdown, configs via CLI/curl, not web UIs: "Don't talk to a developer... Instruct and empower their LLM."
3. **Simpler Stacks** -- Considering HTML/CSS/JS + Python FastAPI over "serverless multiverse"
4. **Apps as Prompts** -- Questioning if apps should be standalone products or "Artifacts" generated on-the-fly

> Source: [[entities/karpathy-writings]] | Raw: raw/articles/2025-04-27_karpathy-vibe-coding-menugen.md

[Xe Iaso](https://xeiaso.net/blog/2026/vibe-coding-sponsor-panel/)がカンファレンス用のsponsor panelをClaude Codeでvibe codingした体験記から、実践的知見が得られる。本プロジェクトは手術前の「最後にどうしても出したい」という切迫感から生まれた。

#### 背景: GraphQLの沼

GoとGraphQLの組み合わせは相性が悪く、Xeは以前から「GoとGraphQLは水と油」と評していた。`shurcooL/graphql`ライブラリは構造体タグによるリフレクションベースのクエリ生成を必要とし、コード生成ツールは大量のボイラープレートを生み出す。GitHubがGraphQLエクスプローラーを削除したことで状況はさらに悪化し、対話的なスキーマ探索が不可能になった。従来はこの「GraphQLの沼」で毎回挫折していた。

#### ワークフロー

1. **ダミーデータからスタート** — 実際のJSON構造が決まる前に、モックアップでUIレイアウトを高速プロトタイピング
2. **Skills-as-Contextパターン** — 要件をスキル（指示）として書き出し、エージェントがそれらを組み立ててコード生成
3. **イテレーティブな精緻化** — 動作確認ごとにフィードバック→修正のサイクルで1日で本番相当に到達
4. **実データに置き換え** — プロトタイプが安定したら、実際のsponsorデータに差し替え

#### Skillsの具体的内容

Xeは4つのエージェントスキル（`.claude/skills/`に保存）を用意し、Claude Codeのコンテキストに読み込ませた:

| スキル | 内容 |
|--------|------|
| `templ-syntax` | GoのHTMLテンプレートライブラリTemplの構文（式、条件分岐、ループ） |
| `templ-components` | 再利用可能なコンポーネントパターン（props, children, composition） |
| `templ-htmx` | TemplとHTMXの組み合わせに関する注意点（属性レンダリング、イベント処理） |
| `templ-http` | Templを`net/http`ハンドラに正しく組み込む方法（ルーティング、データ受け渡し、リクエストライフサイクル） |

TemplはLLMの学習データにほとんど含まれていないライブラリであり、スキルなしでは幻覚だらけのコードが生成されていた。スキルを読み込ませたことで、生成されたTemplコードのほとんどが**初回コンパイルで通過**する品質になった。

> *"Think of it like giving someone a cookbook instead of asking them to invent recipes from first principles."*

#### 並行作業のパターン

エージェントチームがコード生成を進める一方で、Xeは以下を並行して実施:
- GitHub Developer SettingsでOAuth認証情報のプロビジョニング
- Neon PostgreSQLデータベースの作成
- Tigrisバケット（スポンサーロゴ保存用）のセットアップ
- エージェントが認証情報を必要とするたびに即座に提供

**Ops作業とコード生成を並列化**することで、待ち時間ゼロの開発フローを実現した。

#### 技術スタック

| コンポーネント | 採用技術 | 理由 |
|---------------|---------|------|
| バックエンド | Go | 既存知識とサイト基盤 |
| HTMLレンダリング | Templ | `html/template`の制約を回避 |
| インタラクション | HTMX | シンプルなページにReactは不要 |
| データベース | PostgreSQL (Neon) | マネージドで運用負荷ゼロ |
| 認証 | GitHub OAuth | スポンサーAPIとの統合 |
| スポンサーデータ | GitHub Sponsors GraphQL API | 直接連携 |
| 画像ストレージ | Tigris | プラグアンドプレイ |

#### 結果

- 従来1週間かかる「足場作り」が**1日で完了**
- GraphQLコードは生クエリ文字列＋手動JSONパースという「コードレビューに出せない」品質だが、**動く**
- 「美しいが未公開」より「醜くても公開」を選ぶトレードオフ — 手術前の納品が最優先
- スポンサーパネルは `sponsors.xeiaso.net` で実働中

#### 限界と課題

- **Orgスポンサーシップは未対応**: 組織スポンサーのスキーマが個人と異なり、別途認証フローが必要
- **コード品質**: JSONパースが生で、変数名も機能的だが魅力に欠け、エラーコンテキストが不足している箇所もある
- **セキュリティクリティカルなシステムには不向き**: 一行ごとの監査が必要なものはvibe codingの対象外
- **6ヶ月後には書き直す予定**: まずは存在することが重要

#### 教訓

- **Skills as code**: 人間は指示（スキル）を書き、エージェントがコードを書く役割分担が効果的。特に学習データに少ないライブラリでは必須
- **モックアップ→実データの移行**はvibe codingに適したパターン
- **スコープを限定する**ほど成功率が上がる（特定のUIコンポーネントに集中）
- **Ops作業とコード生成の並列化**で待ち時間を排除できる
- 従来の「正しい方法」で何度も挫折したプロジェクトこそ、vibe codingの最大の適用対象

### Tim Sh: セルフホスティングでVibe Codingアプリを運用（2026年4月）

[Tim Sh](https://timsh.org/why-you-should-self-host/)は、5年間で50以上のサービスをデプロイした経験から、vibe codingで作ったアプリのセルフホスティングを推奨している。特に、予算が少なくバックアップのないインディー開発者やvibecoderに適した運用モデルとして提示されている。

#### 従来のクラウドPaaSの問題点

| 問題 | 詳細 |
|------|------|
| **従量課金の予測不能性** | 無料/低額で始められるが、トラフィック増加とともに突然高額な請求が発生（"Serverless Horrors"参照） |
| **抽象化レベルの高さ** | PaaSは「レベル50」の抽象化 — 内部で何が起きているか理解できず、問題発生時のデバッグが困難 |
| **スケーラビリティの過剰供給** | 大多数のアプリは「1K→1Mユーザー」のスケーリングが必要なく、固定サーバーで十分 |

#### 推奨セットアップ: Coolify + Hetzner VPS

| 要素 | 詳細 |
|------|------|
| **サーバー** | Hetzner VPS（€8/月: 3 vCPU, 4GB RAM, 80GB SSD） |
| **PaaSレイヤー** | Coolify（オープンソースのセルフホストPaaS） |
| **デプロイ** | Docker Composeベース、GitHub連携による自動デプロイ |
| **ネットワーク** | 自動リバースプロキシ（Traefik）+ Let's Encrypt SSL |
| **通知** | Telegram通知（デプロイ・エラー時の lifesaver） |

Hetznerの€8/月プランは、同等スペックのDigital Ocean（〜$30/月）の約**3.5倍のコスト差**がある。

#### Vibe Coderにとっての意義

- **ローカルのvibecodedアプリ → 本番公開**が15分で完了: `localhost:8080` → `https://sub.domain.com`
- LLMにDocker Composeを生成させるだけでデプロイ可能（Cursor/Claude Codeに頼む）
- 従量課金ではないため、トラフィックがゼロでも課金が発生しない
- 「抽象化の自由」: Coolifyの1クリックデプロイ（PaaS相当）から、生のDocker Compose、さらには単一Pythonスクリプト＋systemd timerまで、好きな抽象化レベルを選べる
- 月間ランチ代以下のコストで運用可能

> *"You have your own (vibecoded) app and a very cheap server, and you get from localhost:8080 to https://sub.domain.com in 15 minutes. It feels great."*

#### 適したユーザー像

- **Vibecoder / インディー開発者**: 予算ゼロから始めて、自分で運用したい
- **スタートアップCTO**: 会社のツールやインフラを低コストでセットアップしたい
- **但し、爆発的成長が確実なアプリ**（ユーザー数10倍/日）には従来のサーバーレスが適している場合もある

## 関連概念

- [[concepts/agentic-engineering]] — 対照的な開発スタイル
- [[concepts/cognitive-debt]] — Vibe Codingの主要リスク
- [[concepts/harness-engineering/agentic-workflows/linear-walkthroughs]] — 認知負債を返済する手法
- [[concepts/claude-code-tips]] — Claude Codeのセットアップガイド
- [[concepts/self-hosting-ai-development]] — Vibe codingアプリのセルフホスティング

## 参照
- [[simon-willison]] — Vibe Coding vs Agentic Engineeringの提唱者
- [[entities/xeiaso-net]] — Xe Iaso（実践例の著者）
