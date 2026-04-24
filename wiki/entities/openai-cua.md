---
title: OpenAI CUA (Computer-Using Agent)
type: entity
aliases:
- openai-cua
- cua-model
- openai-operator
- computer-using-agent
created: 2026-04-13
updated: 2026-04-13
tags:
- entity
- technology
- computer-use
- browser-agent
- openai
status: active
sources:
- https://openai.com/blog/introducing-operator
- https://openai.com/index/operator-system-card/
- https://www.libertify.com/interactive-library/openai-operator-system-card-cua-safety/
---

# OpenAI CUA (Computer-Using Agent)

OpenAIの**CUA（Computer-Using Agent）**モデルは、GPT-4oのビジョン機能と強化学習を組み合わせて、スクリーンショットを見てGUIを操作するエージェント。2025年1月に「Operator」として公開され、2025年7月にChatGPTエージェントに完全統合された。

## 概要

| 項目 | 内容 |
|---|---|
| 発表日 | 2025年1月23日（Operator研究プレビュー） |
| ベースモデル | GPT-4o + 強化学習 |
| アプローチ | スクリーンショットベースのビジョン認識 + RL |
| 提供形態 | ChatGPT Pro ($200/月) → ChatGPTエージェント統合 |
| API | CUAモデル（2025年3月よりTiers 3-5の開発者に公開） |
| OSWorldスコア | 38.1% |
| WebArenaスコア | 58.1% |
| WebVoyagerスコア | 87% |

## 技術アーキテクチャ

### 二段階トレーニング
1. **教師あり学習**: スクリーンショットの読み取り、UI要素の認識、入力制御の基本能力
2. **強化学習**: 推論、エラー修正、予期せぬ事態への適応能力

```
タスク指示 → スクリーンショット取得 → GPT-4oビジョン解析 →
アクション決定（クリック/タイピング/スクロール） → 実行 →
次のスクリーンショットで状態確認 → 自己修正 → 繰り返し
```

### セーフガード（3層）
- **モデル層**: 97%の有害タスク拒否率
- **プロンプトインジェクション対策**: 99%の検出率、98.4%の精度
- **プロダクト層**: 重要操作は人間の確認必須、1クリックでセッション停止

### Preparedness Framework評価
| カテゴリ | リスクレベル |
|---|---|
| 説得（Persuasion） | Medium（GPT-4oから継承） |
| サイバーセキュリティ | Low |
| CBRN | Low（タスク成功率1%） |
| モデル自律性 | Low |

## タイムライン

| 日付 | マイルストーン |
|---|---|
| 2025年1月 | Operator研究プレビュー公開（ChatGPT Pro限定） |
| 2025年3月 | CUAモデルをAPIで公開（Tiers 3-5開発者） |
| 2025年7月 | ChatGPTエージェントに完全統合 |
| 2026年 | Plus/Team/Enterpriseユーザーへの拡大予定 |

## 課題と制約

1. **複雑なタスク**: 不慣れなUIや複雑なテキスト編集で成功率40%に低下
2. **OSWorld 38.1%**: 高い信頼性には至っていない
3. **プライバシー**: スクリーンショット送信、閲覧履歴の扱い
4. **非ブラウザ環境**: OSレベルの操作でエラー発生率上昇

## Anthropic Computer Useとの比較

| 次元 | OpenAI CUA | Anthropic Computer Use |
|---|---|---|
| ベースモデル | GPT-4o + RL | Claude Sonnet/Opus |
| OSWorld | 38.1% | 14.9% → 22.0%+ |
| WebArena | 58.1% | 58.1% |
| トレーニング | 教師あり + 強化学習 | スクリーンショットベース |
| 提供形態 | ChatGPT統合 + API | API + Claude App |
| 有害タスク拒否 | 97% | N/A |

## 関連エンティティ

- [[anthropic-computer-use]] — AnthropicのComputer Use
- [[death-of-browser]] — ブラウザの脱人間化潮流
- [[browser-use]] — オープンソースDOMベース自動化
- [[harness-engineering]] — エージェント環境設計

## Sources

- [Introducing Operator (OpenAI, 2025-01)](https://openai.com/blog/introducing-operator)
- [Operator System Card (OpenAI)](https://openai.com/index/operator-system-card/)
- [CUA API Launch (2025-03)](https://cdn.openai.com/operator_system_card.pdf)
