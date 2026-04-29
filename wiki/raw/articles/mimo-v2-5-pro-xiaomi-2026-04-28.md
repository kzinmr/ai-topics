---
title: "Xiaomi MiMo-V2.5-Pro: 1T MoE Model for Agentic Coding"
created: 2026-04-28
updated: 2026-04-28
type: summary
tags: [model, ai-agents, coding-agents, inference, benchmark]
sources: [raw/articles/mimo-v2-5-pro-xiaomi-2026-04-28.md]
---

# Xiaomi MiMo-V2.5-Pro

## 概要
Xiaomiが2026年4月27日にリリースしたオープンソースの大規模言語モデル。1.02Tパラメータ（アクティブ42B）のMixture-of-Expertsアーキテクチャを採用。

## 主要仕様
- **パラメータ**: 1.02T総数 / 42Bアクティブ
- **コンテキストウィンドウ**: 最大1Mトークン
- **アーキテクチャ**: ハイブリッドアテンション（ローカルスライディングウィンドウとグローバルアテンションを6:1でインターリーブ）
- **訓練データ**: 27Tトークン
- **Multi-Token Prediction (MTP)**: 出力スループットを3倍化、RLロールアウトを高速化
- **KVキャッシュ**: 学習可能なattention-sinkバイアスにより長期コンテキストで約7倍削減
- **精度**: FP8 (E4M3) Mixed

## 主な成果
- **SysYコンパイラ（Rust）**: 672回のツール呼び出し、4.3時間で233/233テスト合格
- **動画編集アプリケーション**: 1,868回のツール呼び出し、11.5時間で8,192行のコード生成
- **アナログEDA（回路設計）**: 1時間で6つの複合メトリクスを達成
- **ClawEvalベンチマーク**: Claude Opus 4.6、Gemini 3.1 Pro、GPT-5.4と比較して40〜60%少ないトークンで同等性能

## 訓練方法
1. SFTによる基本的な指示理解
2. ドメイン特化訓練（数学、安全性、ツール使用の個別教師モデル）
3. Multi-Teacher On-Policy Distillation (MOPD) による統合

## 提供形態
- Hugging Face、AI Studio、Xiaomi APIで公開
- SGLangおよびvLLM対応
