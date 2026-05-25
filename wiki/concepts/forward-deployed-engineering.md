---
title: "Forward Deployed Engineering (FDE)"
created: 2026-05-18
updated: 2026-05-25
tags:
  - company
  - strategy
  - ecosystem
  - enterprise-ai
sources:
  - raw/newsletters/2026-05-17-anthropic-pulls-away-openai-strikes-back-and-google-s-gemini-rising.md
  - raw/articles/2026-05-20_varick_forward-deployed-engineering-101.md
  - raw/articles/2026-05-25_saas-fde-ai-agent-era_career-strategy.md
---

# Forward Deployed Engineering (FDE)

## Overview

Forward Deployed Engineering (FDE) is the emerging industry paradigm where frontier AI labs embed engineers directly into enterprise customer environments to build custom AI solutions, rather than selling model API access alone. As models commoditize, the **deployment layer becomes the new moat**.

> "Every AI lab is becoming Palantir." — The Signal, May 2026

## The Shift from API Sales to Service Delivery

In 2025-2026, all three major frontier labs made structural moves toward the FDE model:

| Lab | FDE Initiative | Scale | Details |
|-----|---------------|-------|---------|
| **OpenAI** | "The Deployment Company" JV | $4B raise, $10B pre-money | Tomoro providing 150 FDEs; backed by TPG, Bain Capital, SoftBank, 19 investors |
| **Anthropic** | Blackstone/Goldman Sachs JV | $1.5B | Claude-powered enterprise deployment systems; Blackstone, Hellman & Friedman, Goldman Sachs each contributing $300M |
| **Google** | Internal hiring | Hundreds of FDEs | Building deployment engineering teams alongside Gemini model development |

## Why FDE Is Emerging Now

1. **Model commoditization**: GPT-5.5, Claude Opus 4.7, Gemini 3.1 are converging on capability — differentiation shifts to integration
2. **Enterprise complexity**: Real-world deployment requires understanding legacy systems, compliance, and organizational workflows that models alone can't navigate
3. **Revenue scale**: Service delivery generates far higher per-customer revenue than API tokens
4. **Lock-in**: FDE relationships create switching costs that model quality alone cannot

## Relationship to AI Services Joint Ventures

FDE is the operational model behind the wave of AI services joint ventures. See [[concepts/ai-services-joint-ventures]] for the financial structure comparison.

## The FDE Job: Audit → Evals → Deployment

Varickによる実践的FDEガイド（2026年5月）では、FDEの仕事は3つのフェーズに分解される:

### 1. Audit（監査）
顧客の現場に入り、各チームのワークフローをマッピング。**自動化すべき/すべきでない**を判断する3原則:
| 条件 | 判断 |
|------|------|
| ルール化可能だが入力が変動（メール→PDF→画像） + ツール呼び出し必要 | **エージェント**を使う |
| ルールも入力も予測可能 | **コード**の方が速く安い |
| パターン認識 + ドメイン専門知識が必要 | **手動**のまま |

重要なポイント:
- **高頻度・高ボリュームの自動化を狙う** — 月5回しか動かないエージェントはROIが出ない
- **AIを使いすぎない** — ほとんどの自動化は一連のツール呼び出し + 1回のLLMオーケストレーションで十分

### 2. Evals（評価）
数百万ドルのAI導入には、それが機能していることを証明する評価が必要:
1. **人間のステップをトレースし、AIを各ステップで採点する**: 人間は一度に問題を解決しない。各チェックポイントでAIが正しく判断しているか検証
2. **少数の優れた事例から始めて基準を作る**: 人間と一緒に「完璧な回答」を定義し、それを基準にエージェントを評価

### 3. Deployment（展開）
- **大規模データ移行を避ける**: 既存データレイヤー（SharePoint/DB）の上にAPIを構築し、その上にオーケストレーターとしてモデルを置く
- **サンドボックス実行環境**を顧客インフラ内に作成し安全にテスト
- **小さく始める**: バグ検出→調査→チケット作成のAgentから始め、成功したらコード修正・PR作成能力を追加
- **最小単位の自律性から始め、段階的に行動権限を付与**

## How to Become an FDE (30-Day Roadmap)

Varickの30日間ロードマップ:

| チェックポイント | 日数 | 内容 |
|----------------|------|------|
| CP1 | 7日 | Agent loop、ツール呼び出し、ガードレール（入力検証・最大ステップ制限・出力フィルタリング）、コンテキストウィンドウvs外部メモリの使い分け、監査証跡 |
| CP2 | 14日 | 構造化出力（常にJSON）、デモ→本番で壊れるもの（Agents 102参照）、チェックポイント（nステップごとに状態保存→再開可能） |
| CP3 | 21日 | リトライロジック＋指数バックオフ、コスト最適化（安いモデルで安いサブタスク・キャッシュ・max tokens）、ゴールデンデータセット（20実クエリ＋手動ラベル）、マルチエージェントパイプライン |
| CP4 | 最終週 | 全復習＋声に出して説明＋ビジネス指標に紐付け |

**3つの成功バックグラウンド**: コンサルタント、プロダクトマネージャー、ソフトウェアエンジニア。
- **コンサル/PM**: データ→ROI変換能力はある。エンジニアリング経験の不足をポートフォリオで補う（本番対応Agent・RAGパイプライン・Evalフレームワーク・MCP）
- **SWE**: コミュニケーション能力が最重要。作ったものをビジネス価値に翻訳して説明できること

> **最重要スキル**: 「非技術系の意思決定者にAIができること・できないことを説明できるか」。これができないとFDEにはなれない。

## FDE-SaaS合成：最も価値のあるポジション

### 「FDE vs SaaS」という誤った二分法

FDEとSaaSを対立軸として捉えるのは危険なバイナリ思考である。最も勝てるポジションは、純粋なFDEでも純粋なSaaSでもない。それは**FDEが現場で発見したパターンを、再利用可能なプロダクト・プラットフォームのプリミティブへと迅速に変換する能力**だ。

### 業界リーダーが示す方向性

- **OpenAI FDE求人要項**: 「実用的なパターンをツール・プレイブック・ビルディングブロックとして体系化（codify）する」
- **Anthropic FDE求人要項**: 「再現可能なデプロイメントパターンを特定・体系化し、Product/Engineeringへフィードバックする」

トップレベルのFDEとは、「個別顧客向けに何でも作れる人」ではない。**現場でしか見えない要件を発見し、それを再利用可能な抽象化へと変換できる人**である。

### 最も価値の高いキャリアタイトル

| タイトル | 特徴 |
|----------|------|
| **Forward Deployed Product Engineer** | FDEの現場感覚 + プロダクト構築の両輪 |
| **AI Agent Platform Engineer** | エージェント基盤そのものを設計・汎用化 |
| **Agentic Product Engineer** | 自律エージェントを製品に組み込む |
| **Applied AI Product Engineer** | 応用AI領域でプロダクトを主導 |

### 避けるべきポジション

- **純粋FDE**: コンサルティング比重が高く、プロダクト構築の時間が少ない。現場のパターンをコード化しても、それが再利用される仕組みがない
- **旧来型SaaS開発者**: 共有画面・機能を作るだけ。AIエージェント時代のパラダイムシフトに乗り遅れる

### アクションプラン

| 時期 | アクション |
|------|-----------|
| **3ヶ月** | 現職でFDE的な仕事を始める。顧客1社のワークフローを選び、Agentを構築し、効果を測定する |
| **6ヶ月** | 2〜3社に拡大。共通パターンと差異パターンを特定し、再利用可能な抽象化の種を見つける |
| **12ヶ月** | 決断 — 現職がFDE-プロダクト合成モデルを受け入れるなら留まる。そうでなければFDE/Applied AI側へ移る |

> FDEとSaaSの境界に立つ人材が、AIエージェント時代の最も希少で価値のあるポジションである。

## Open Questions

- Does FDE scale linearly with headcount, or can tooling make it self-service?
- Will FDE become a permanent organizational function or a transitional phase before models handle integration autonomously?
- How does this affect the open-source AI ecosystem, where no FDE layer exists?

## See Also

- [[concepts/ai-services-joint-ventures]] — Joint venture structures for AI service delivery
- [[entities/openai]] — OpenAI's Deployment Company strategy
- [[entities/anthropic]] — Anthropic's enterprise JV
- [[entities/google]] — Google's compute advantage and enterprise push
