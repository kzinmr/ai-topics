---
title: "Claude Sonnet 4.6"
type: concept
aliases:
  - claude-sonnet-4-6
  - sonnet-4-6
created: 2026-04-25
updated: 2026-05-08
tags:
  - concept
  - anthropic
  - model
  - claude-sonnet
status: complete
sources:
  - url: "https://www.anthropic.com/news"
    title: "Anthropic News (Claude Sonnet 4.6 Announcement, Feb 17, 2026)"
related:
  - "[[concepts/claude-model-family]]"
  - "[[concepts/claude-opus-4-6]]"
  - "[[concepts/claude-opus-4-7]]"
---

# Claude Sonnet 4.6

**Claude Sonnet 4.6** は、[[entities/anthropic]] が **2026年2月17日** にリリースした Claude Sonnet シリーズの最新モデル。Opus 4.6 と同時期にリリースされ、コーディング、Computer Use、長文脈推論、エージェント計画、知識業務、デザインの全スキルにおいて大幅なアップグレードが施された。

## 概要

Sonnet は Claude モデルファミリーの中間階層（バランス型）として位置づけられ、多くの本番ワークロードにおいて推奨モデルとなっている。Sonnet 4.6 は前世代の Sonnet 4.5 からすべての主要ベンチマークで改善。

| 項目 | 内容 |
|------|------|
| リリース日 | 2026年2月17日 |
| ポジション | ミッドレンジ（バランス型） |
| API名 | `claude-sonnet-4-6` |
| コンテキスト | 200K トークン |
| 最大出力 | 64K トークン |
| API価格 | $3.00/MTok（入力）、$15.00/MTok（出力） |

## 主な改善領域

- **コーディング**: SWE-bench スコア向上、マルチファイル編集の正確性改善
- **Computer Use**: スクリーンショット理解とGUI操作精度の向上
- **長文脈推論**: 100K+ トークンコンテキストでの一貫性改善
- **エージェント計画**: マルチステップ計画の信頼性向上
- **知識業務**: 文書分析、要約、情報抽出の精度改善

## 関連ページ

- [[concepts/claude-model-family]] — Claudeモデルファミリー全体
- [[concepts/claude-opus-4-6]] — 同時期リリースのOpus
- [[concepts/claude-opus-4-7]] — Opus 4.7（フラッグシップ最新）
