---
title: "Reverse Engineering"
type: concept
aliases:
  - reverse-engineering
  - RE
created: 2026-04-25
updated: 2026-04-29
tags:
  - concept
  - reverse-engineering
  - security
  - analysis
status: complete
sources:
  - url: "https://github.com/pydantic/monty"
    title: "Monty Sandbox Security Model"
  - url: "https://pydantic.dev/articles/hack-monty"
    title: "Hack Monty Bounty Program"
---

# Reverse Engineering

**Reverse Engineering（リバースエンジニアリング）** は、既存のシステムやソフトウェアの構造、動作、設計を分析して理解するプロセス。AI の文脈では、モデルの内部動作の解析、サンドボックスの回避、トレーニングデータの推測など、幅広い応用がある。

## AI 分野でのリバースエンジニアリング

### モデル解析
- **モデル抽出攻撃**: 公開 API を通じてモデルの知識や重みを推測
- **アーキテクチャ推定**: レイテンシ、応答パターンからモデル構造を推定
- **プロンプト抽出**: システムプロンプトのリーク攻撃
- **メンバーシップ推測**: 特定のデータが学習に使われたか判定

### サンドボックス回避
- AI エージェントのコード実行サンドボックス（[[concepts/monty-sandbox]] など）のセキュリティテスト
- **Hack Monty**: Pydantic が $5,000 の報奨金プログラムを実施
- コンテナエスケープ、ファイルシステムアクセス、環境変数リークの試行

### プロトコル解析
- プロプライエタリ API のリバースエンジニアリング
- モデル応答パターンの統計的分析
- レート制限・負荷分散の推測

## 主要テクニック

| テクニック | 説明 | AI 分野での応用 |
|-----------|------|----------------|
| **静的解析** | バイナリ/コードの静的構造分析 | モデルファイル形式の解析 |
| **動的解析** | 実行時の挙動観察 | API 応答パターンの分析 |
| **フォールトインジェクション** | エラーを意図的に発生させて挙動を観察 | サンドボックス限界の特定 |
| **サイドチャネル攻撃** | タイミング、消費電力、EM放射の分析 | モデルサイズ・構造の推定 |
| **グレーボックス解析** | 部分的に既知の情報と観測を組み合わせ | プロンプトインジェクション脆弱性の発見 |

## AI セキュリティとの関係

リバースエンジニアリングは AI セキュリティの両面を持つ：
- **攻撃側**: モデルの弱点発見、ジェイルブレイク、プロンプトインジェクション
- **防御側**: 脆弱性の発見と修正、レッドチーミング、報奨金プログラム

## 倫理的考慮事項

- **利用規約の遵守**: 多くの AI サービスはリバースエンジニアリングを禁止
- **責任ある開示**: 発見した脆弱性は適切に報告
- **教育的文脈**: セキュリティ研究と学習目的での使用

## 関連概念

- [[concepts/monty-sandbox]] — サンドボックスセキュリティモデル
- [[concepts/claude-code-best-practices]] — セキュアなコード実行
- [[concepts/agent-loop-orchestration]] — エージェントセキュリティ

## ソース

- [Monty Sandbox (Pydantic)](https://github.com/pydantic/monty)
- [Hack Monty Bounty Program](https://pydantic.dev/articles/hack-monty)
