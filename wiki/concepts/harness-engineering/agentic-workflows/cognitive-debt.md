---
title: "Cognitive Debt"
aliases:
  - cognitive-debt
created: 2026-04-12
updated: 2026-04-12
tags:
  - concept
  - agentic-engineering
status: draft
sources:
  - "https://simonwillison.net/guides/agentic-engineering-patterns/interactive-explanations/"
  - "https://simonwillison.net/guides/agentic-engineering-patterns/"
  - "https://simonwillison.net/2025/Oct/30/linear-walkthrough/"
---

# Cognitive Debt

AIエージェントが生成したコードの動作理解を失うことで蓄積する**認知的負債**。技術的負債の認知版。[[vibe-coding]]によって加速度的に増加する。

## 定義

> "When we lose track of how code written by our agents works we take on cognitive debt."

## 技術的負債との比較

| | 技術的負債 | 認知負債 |
|--|-----------|---------|
| 対象 | コード構造 | 開発者の理解度 |
| 原因 | 妥協した設計 | エージェント生成コードのブラックボックス化 |
| 影響 | 保守性低下 | 新機能計画の困難化 |
| 返済方法 | リファクタリング | 対話的解説・ウォークスルー |
| 可視化 | コードメトリクス | **Linear Walkthrough** |

## なぜ問題か

> "If the core of our application becomes a black box that we don't fully understand we can no longer confidently reason about it, which makes planning new features harder and eventually slows our progress in the same way that accumulated technical debt does."

Willisonは認知負債を**Vibe Codingの最大の問題**と位置付けている。Vibe Codingでは開発者が「自然言語で依頼→エージェントがコード生成→即デプロイ」のサイクルで作業するため、コードの詳細な動作を理解しないまま累積していく。

> "The problem with vibe-coding is that it leads to cognitive debt."

## 認知負債のメカニズム

1. **プロンプトで依頼** → エージェントがコード生成
2. **コードをレビューせずにテスト実行** → 動いているからOK
3. **次に機能追加時** → 既存コードの動作がわからない
4. **新しいプロンプトで修正依頼** → さらに理解不能なコードが追加
5. **ループ継続** → コアアプリケーションがブラックボックス化

### Vibe CodingとAgentic Engineeringの対比

| | Vibe Coding | Agentic Engineering |
|--|------------|-------------------|
| 速度 | 最速 | 中程度 |
| 認知負債 | **高く累積** | 管理・返済 |
| テスト | なし or 最小限 | 体系的 |
| 品質 | 低（長期的） | 高 |
| 持続性 | 短期的 | 長期的 |

> "The key distinction between vibe-coding and agentic engineering: vibe coding produces speed at the cost of cognitive debt, agentic engineering manages that debt."

## 返済方法

### 1. [[linear-walkthroughs]] — 構造化コード解説
Willisonが自作したCLIツールで、コードの処理フローをツリー表示し、どの関数がどのパスで呼ばれるかを**視覚的に理解可能**にする。

```
$ llm --plugin llm-linear-walkthrough explain --file src/app.py
```

### 2. [[interactive-explanations]] — 対話的アニメーション
ブラウザ上でコードの動作をステップ実行し、変数の変化をリアルタイムで可視化する。

### 3. [[agentic-manual-testing]] — 実行による動作確認
[[rodney]]等のCLIブラウザツールで実際にUIをテストし、エージェントが生成した機能が本当に動くかを検証。

### 4. [[showboat]] — テストの記録と共有
検証結果をMarkdownドキュメントとして保存し、チーム全員が確認できるようにする。

## 返済サイクル

認知負債の返済は**一度きりではない**。Agentic Engineeringでは継続的な返済サイクルが必要:

```
コード生成 → テスト → Linear Walkthroughで理解 → 
  不明点を対話的解説で深掘り → 検証結果をShowboatで記録 → 
    次のコード生成
```

## 参照
- [[simon-willison]] — 概念提唱者
- [[vibe-coding]] — 認知負債の主要発生源
- [[linear-walkthroughs]] — 主要な返済ツール
- [[interactive-explanations]] — 対話的理解ツール
- [[agentic-manual-testing]] — 検証ツール
