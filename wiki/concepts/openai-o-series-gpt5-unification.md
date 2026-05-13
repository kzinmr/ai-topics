---
title: "OpenAI o-series → GPT-5 統合 (2024-2025)"
created: 2026-05-13
updated: 2026-05-13
type: concept
tags: [concept, openai, model, reasoning, rlvr, timeline]
aliases: [o1-to-gpt5, o3-cancellation, gpt5-unification]
related: [[rlvr]], [[gpt-5]], [[openai]], [[deepseek-r1]]
sources: ["https://openai.com/index/introducing-gpt-5/", "https://x.com/sama/status/1889755723078443244", "https://openai.com/index/introducing-o3-and-o4-mini/"]
---

# OpenAI o-series → GPT-5 統合 (2024-2025)

2024年9月に始まったOpenAIの推論特化型「oシリーズ」モデルラインは、2025年2月のSam Altmanによるロードマップ転換を経て、2025年8月の**GPT-5**でGPTシリーズに統合された。o3はスタンドアロンモデルとしてキャンセルされ、GPT-5の「Thinking」モードとして吸収された。

## フェーズ別タイムライン

### Phase 1: oシリーズ誕生 (2024年9月〜12月)

| 日付 | イベント |
|------|----------|
| **Sep 12, 2024** | **o1-preview & o1-mini** リリース — 初の「推論モデル」。大規模RLで内部CoTを生成（コード名「Strawberry」） |
| **Dec 5, 2024** | **o1 正式版** リリース — 34%エラー削減、画像入力対応 |
| **Dec 20, 2024** | **o3 & o3-mini** 発表 — 12 Days of OpenAI でプレビュー（o2 skip はO2商標回避のため） |

### Phase 2: 拡大と路線転換 (2025年1月〜4月)

| 日付 | イベント |
|------|----------|
| **Jan 31, 2025** | **o3-mini** リリース — 無料ユーザーに初の推論モデル提供 |
| **Feb 2, 2025** | **Deep Research** ローンチ — o3ベースのエージェント機能 |
| **🔴 Feb 12, 2025** | **ロードマップ転換**: Sam Altman が GPT-5 統合を発表。o3 スタンドアロン出荷キャンセル |
| **Feb 27, 2025** | **GPT-4.5 (Orion)** — 「最後のnon-chain-of-thoughtモデル」 |
| **Apr 16, 2025** | **o3 & o4-mini** フルリリース — 自律的ツール使用、マルチモーダル推論、画像思考対応 |

### Phase 3: 吸収と統合 (2025年6月〜8月)

| 日付 | イベント |
|------|----------|
| **Jun 10, 2025** | **o3-pro** リリース — 最終のスタンドアロンoシリーズ |
| **Aug 6, 2025** | **GPT-OSS** — Apache 2.0ライセンスのオープンウェイト推論モデル (120B) |
| **🔴 Aug 7, 2025** | **GPT-5 ローンチ** — GPT + oシリーズ統合完了。o3 はChatGPTモデルピッカーから削除 |
| **Aug 12, 2025** | o3 部分的復活 — ユーザー反発を受け「追加モデルを表示」トグルで復活 |

### Phase 4: 急速なGPT-5.x イテレーション

| 日付 | イベント |
|------|----------|
| **Sep 30, 2025** | **GPT-5.1** — 設定可能な推論努力レベル |
| **Dec 11, 2025** | **GPT-5.2** — プロフェッショナル向け最上位モデル |

## Sam Altman の声明 (Feb 12, 2025)

> *"A top goal for us is to unify o-series models and GPT-series models by creating systems that can use all our tools, know when to think for a long time or not, and generally be useful for a very wide range of tasks."*
>
> *"In both ChatGPT and our API, we will release GPT-5 as a system that integrates a lot of our technology, including o3. We will no longer ship o3 as a standalone model."*
>
> *"We hate the model picker... We want AI to 'just work' for you; we realize how complicated our model and product offerings have gotten."*

## GPT-5 アーキテクチャ

GPT-5は**3コンポーネント統合システム**:

1. **GPT-5 Main** — 高速・効率的な応答（GPT-4o/4.5系譜）
2. **GPT-5 Thinking** — 深い推論が必要な場合（o3/o3-pro系譜、内部CoT）
3. **リアルタイムルーター** — 会話タイプ・複雑さ・ツール必要性・ユーザー意図に基づき、どのバックエンドを使うか自動判断

## 統合の戦略的理由

- モデルピッカーが複雑化しすぎていた（Pro ユーザーは最大10種類のモデル選択肢）
- **DeepSeek R1** (Jan 2025) の登場でオープン推論モデルとの競争が激化
- 「AIは "just work" すべき」という製品哲学の転換

## oシリーズの現在のステータス

- ChatGPT 無料/Plus: GPT-5システムに統合（o3 は隠しトグルで利用可能）
- API: o3, o3-mini, o3-pro, o4-mini は引き続き提供
- Azure OpenAI ドキュメント: GPT-5シリーズと並んでoシリーズを「推論モデル」として記載

## 関連概念

- [[rlvr]] — o1/o3の基盤となったRL訓練パラダイム
- [[grpo]] — o3で使用されたRL最適化アルゴリズム
- [[deepseek-r1]] — 統合を加速させた競合オープンモデル
