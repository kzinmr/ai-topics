---
title: "Hoard Things You Know How to Do"
type: concept
aliases:
  - hoard-things-you-know
  - knowledge-hoarding
  - knowledge-repository
created: 2026-04-13
updated: 2026-04-13
tags:
  - concept
  - agentic-engineering
  - knowledge-management
status: draft
sources:
  - "https://simonwillison.net/guides/agentic-engineering-patterns/hoard-things-you-know/"
---

# Hoard Things You Know How to Do

Simon Willisonが提唱する**知識の貯蔵と再利用**の概念。エージェント時代において、個人が「どのように行うか知っているか」を記録・蓄積することが強力な武器になる。

## 核心原則

> "Hoard things you know how to do. The more you know how to do, the more you can recombine into new solutions."

開発者が**具体的な実装方法**を知識として蓄積することで、エージェントに指示する際の精度と速度が向上する。

## 知識の種類

### 1. 実装パターン
- 特定の技術スタックでのベストプラクティス
- よくある問題の解決方法
- ライブラリ/APIの使用方法

### 2. 設定・環境構築
- 開発環境のセットアップ手順
- ツールの最適設定
- デプロイメントパイプライン

### 3. デバッグ手法
- 特定のエラーのトラブルシューティング
- パフォーマンス最適化のテクニック
- セキュリティ脆弱性の見つけ方

## エージェント時代での価値

### なぜ「知っていること」を貯蔵するのか

1. **指示の精度向上**
   - エージェントに対して具体的で正確な指示が出せる
   - 「あの方法で」という暗黙知が明示的になる

2. **品質判断能力**
   - エージェントの出力が正しいか判断できる
   - 認知負債を回避できる（[[anti-patterns]]参照）

3. **再組み合わせの力**
   - 異なる知識を組み合わせて新しい解決策を創造
   - エージェントが単独では到達できない洞察

## 実践方法

### 知識の記録
- **ブログ記事**: 学んだことを文章化
- **コードスニペット**: 再利用可能なコード片
- **設定ファイル**: 環境設定のテンプレート
- **チェックリスト**: 品質保証のための項目

### 知識の整理
- タグ付けとカテゴリ分類
- 検索可能な形式での保存
- 定期的な更新と削除（陳腐化した知識）

## Willisonの実践例

Willison自身が多様なプロジェクト（Datasette、sqlite-utils、llmなど）で培った知識を:
- ブログ記事として公開
- GitHubリポジトリでコードとして保存
- ツールとして実装・共有

これらが彼の**アジェンティックエンジニアリングの基盤**になっている。

## 関連概念

- [[cognitive-debt]] — 知識がない状態でコードをマージすると負債になる
- [[anti-patterns]] — 知識不足がアンチパターンを生む
- [[harness-engineering/agentic-workflows/compound-engineering-loop]] — 知識が複利的に成長するサイクル
- [[harness-engineering/agentic-workflows/prompt-driven-development]] — 知識がプロンプトの質を決定する

## 参照

- [[simon-willison]] — 概念提唱者
- [Hoard things you know how to do](https://simonwillison.net/guides/agentic-engineering-patterns/hoard-things-you-know/)
