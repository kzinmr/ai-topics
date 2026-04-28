---
title: "Polymarket Trading Agents"
type: concept
aliases:
  - polymarket-bots
  - prediction-market-agents
  - weather-trading-bots
tags:
  - concept
  - polymarket
  - trading-agents
  - ai-agents
  - automation
status: complete
description: "AI agents used for automated trading on Polymarket prediction markets — weather, crypto, sports. Self-learning bots that operate 24/7 with no emotions."
created: 2026-04-27
updated: 2026-04-27
sources:
  - "https://x.com/i/article/2045080054917476451"
related:
  - "[[concepts/harness-engineering]]"
  - "[[hermes-agent]]"
  - "[[self-learning-agents]]"
---

# Polymarket Trading Agents

> **Definition:** Polymarketは予測マーケットプラットフォームで、AIエージェントが天気、暗号通貨、スポーツ市場で自律的にトレードを行う。エージェントは24/7稼働し、感情がなく、全てを記憶する。

## 代表的なエージェント例

| エージェント | 市場 | 成果 |
|-------------|------|------|
| ColdMath | 天気 | $300 → $219K (3ヶ月) |
| Sharky6999 | 暗号通貨 | $819K PnL, 99.3% win-rate |
| RN1 | スポーツ | $1.2K → $7.3M |

## エージェントの優位性
- 睡眠しない、感情がない、全てを記憶する
- 適切なアルゴリズムと実行速度が全て
- 自動化された自己学習AIエージェントが強いエッジ

## 天気トレードボット構築（Hermes Agent）

### 前提条件
- Hermes Agent（Nous Research製、2026年2月25日リリース）
- VPS（Hetzner推奨）
- Polymarket用ウォレット（Polygon network）
- Weather API（VisualCrossing無料API）

### 構築ステップ
1. **Clone & Setup** — AlterEgo製のopen-source botをclone
2. **Wallet作成** — 専用ウォレットをセットアップ
3. **資金投入** — $ USDC.e（取引資金）+ $ POL（ガス代）
4. **Polymarket contracts承認** — botが資金を使えるように
5. **Weather API接続** — VisualCrossing API keyを設定
6. **Test scan** — paper-trading modeでテスト
7. **Real trading開始** — 自己学習型天気トレードボット稼働

### 動作原理
- 20都市 × 4大陸をスキャン
- 3つのforecast sourceをExpected ValueとKelly Criterion position sizingに統合
- 各トレードで自己改善（fixedスクリプトではない）

## Sources
- [Hermes Agent + Polymarket - how i built self-learning weather trading bot $100 → $5,000](https://x.com/i/article/2045080054917476451) (2026-04-25, X article)
