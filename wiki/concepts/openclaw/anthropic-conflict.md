---
title: "Anthropic-OpenClaw Conflict"
aliases:
  - anthropic-openclaw-conflict
  - openclaw-ban
  - claude-subscription-cutoff
  - third-party-harness-restriction
created: 2026-04-18
updated: 2026-04-18
tags:
  - concept
  - openclaw
  - anthropic
  - platform-risk
  - subscription-economics
related:
  - concepts/openclaw/_index
  - concepts/openclaw/philosophy
  - entities/peter-steinberger
  - entities/openai
  - concepts/personal-superintelligence
sources:
  - "Anthropic subscription policy changes (April 2026)"
  - "Steinberger X posts and public statements"
  - "Computerworld, TechCrunch, Business Insider coverage (April 2026)"
  - "elvis analysis thread (April 2026)"
---

# Anthropic-OpenClaw Conflict

## 概要

2026年4月、**Anthropic**はClaudeのサブスクリプションプラン（Pro/Max）からサードパーティAIエージェントフレームワーク（OpenClawなど）のアクセスをブロックした。この決定は、プラットフォーム管理、開発者アクセス、AIエージェントインフラの経済学をめぐる重大な論争を引き起こした。

> *"First they copy some popular features into their closed harness, then they lock out open source."* — Peter Steinberger

## タイムライン

| 日付 | イベント |
|------|---------|
| 2026年1月下旬 | "Clawdbot" → Anthropicの商標クレーム → "Moltbot" → "OpenClaw" へ改名 |
| 2026年2月14日 | Peter Steinberger、OpenAI入社を発表 |
| 2026年4月1日 | Claude Codeソースコード（512K行）がnpmパッケージ経由で流出 |
| **2026年4月4日** | **Anthropic、サードパーティツールをClaudeサブスクリプションから排除** |
| 2026年4月4-11日 | Steinberger & Dave Morinが交渉 — 施行を1週間延期 |
| 2026年4月6日 | Computerworldが「Claw Tax」を報道 |
| 2026年4月10日 | Steinbergerのアカウントが「不審なアクティビティ」で一時停止（数時間で復帰） |
| 2026年4月10-12日 | TechCrunch、Business Insiderが報道 |

## 「Claw Tax」の経済学

Anthropicの新たなポリシーにより、OpenClawユーザーは以下のいずれかを選択する必要が生じた：

1. **従量課金APIレート** — $3/百万入力トークン
2. **別個のClaude APIキー** — サブスクリプション制限を回避
3. **使用量バンドルの事前購入** — サブスクリプション会員は最大30%割引

### 計算の現実

| ユーザータイプ | 1日あたりの推定コスト |
|---|---|
| 単一OpenClawインスタンス（Claude Opus） | **$109.55/日**（c't 3003テスト） |
| 一般開発者の平均 | **$6/日** |
| トークンギャップ | **サブスクリプション価値の約9倍** |

1つのOpenClawインスタンスが1全速で動作すると、通常のチャットユーザーの**約300倍**のトークンを消費する。Ban時点で135,000以上のOpenClawインスタンスが稼働していた。

## 競争的文脈

### SteinbergerのOpenAI移籍

- Sam AltmanがSteinbergerを「次世代パーソナルエージェントを牽引する人物」として公然と歓迎
- Anthropicのサブスクリプションブロックは、SteinbergerのOpenAI入社発表から**数週間後**に発生
- OpenClawはOpenAIの支援のもとオープンソース財団へ移行

### Anthropicの立場

Boris Cherny（Claude Code責任者）：
> *"Our subscriptions weren't built for the usage patterns of these third-party tools. Capacity is a resource we manage thoughtfully and we are prioritizing our customers using our products and API."*

AnthropicのClaude Codeは**サブスクリプションに含まれたまま** — サードパーティのみが対象。

## 広範な影響

### 1. フラットレート vs 自律エージェント

サブスクリプションモデルは**会話的ユースケース**を想定して設計されており、自律的なエージェントループ（継続的ツール呼び出し、バックグラウンド処理、マルチステップ推論）のコストを吸収できない。

### 2. プラットフォームロックイン

AI企業がモデルへのアクセスを**いつでも制限できる**という根本的なリスク。OSS開発者はプロプライエタリAPI上に構築する存在リスクに直面する。

### 3. 業界全体のパターン

Anthropicに留まらない：
- GoogleもGeminiのサードパーティエージェントフレームワーク使用に対して行動
- 主要AIプロバイダーは自社のクローズドエージェントエコシステムを優先する方向へ

## OpenClaw哲学との関係

この出来事はOpenClawの**Primitives First**哲学を検証した：

| 側面 | 影響 |
|------|------|
| **Local-First** | API依存を最小化することで、プラットフォームリスクを低減 |
| **Explicit > Implicit** | ユーザーが自らのエージェント環境を完全に制御できる |
| **Ship Beats Perfect** | プラットフォームの制限に縛られず、高速に開発・デプロイ可能 |

## 和解案

Anthropicが提供した措置：
- 月額サブスクリプション相当の一回限りのクレジット（4月17日までに使用、90日有効）
- 最大30%割引のAPI使用量バンドル
- APIキーオプション（フルAPIレート）

## 関連

- [[openclaw]] — OpenClawコンセプト集約
- [[concepts/openclaw/philosophy.md]] — Primitives First哲学
- [[personal-superintelligence]] — データ主権運動
- [[open-source-ai-destruction]] — オープンソースAI破壊
- [[peter-steinberger]] — OpenClaw創設者
- [[openai]] — Steinbergerの新たな所属先
