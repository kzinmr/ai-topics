---
title: "Context Routing — クエリ別コンテキスト振り分け"
type: concept
created: 2026-04-22
updated: 2026-04-22
tags: [concept, optimization, context-management, routing]
status: active
sources:
  - "Vellum AI — Agentic Workflows in 2026 (Dec 2025)"
  - "https://www.vellum.ai/blog/agentic-workflows-emerging-architectures-and-design-patterns"
aliases:
  - context-routing
  - query-routing
  - context-dispatch
---

# Context Routing

> クエリを分類し、コンテキストウィンドウに取り込む前に、適切なコンテキストソースへ振り分けるパターン。

**概要:** 多ドメインエージェントが不要な知識ベース、ツールセット、指示を毎回読み込むのを防ぎ、トークン効率と精度を向上させる。

## 問題

多ドメインエージェントは、すべてのクエリに対してすべてのドメインの知識、ツールセット、指示を読み込む。これはコンテキストの浪費であり、注意力の分散を招く。

## 解決策

クエリを分類し、適切なコンテキストソースに直接送信。これにより、必要な情報だけが届き、コンテキストウィンドウが最小限に保たれる。

## 4つの実装アプローチ

| アプローチ | 速度 | 知能度 | デバッグ性 | 使用例 |
|-----------|------|--------|-----------|--------|
| **ルールベース** | 非常に高速 | 低い | 高い | 固定カテゴリのクエリ |
| **LLMパージ** | 遅い | 高い | 低い | 境界ケースを含む複雑な分類 |
| **階層型** | 中程度 | 中程度 | 中程度 | リードエージェント→サブエージェント |
| **ハイブリッド** | 中程度 | 高い | 中程度 | 本番環境の標準 |

## トークン節約効果

- 分類前のコンテキスト使用量: 通常 30-50% の情報が関係ない
- 分類後: 必要最小限のドコンテキストのみ読み込み
- エージェントの応答品質: 関係ない情報のノイズが除去され向上

## 課題

1. **LLMルーティングの誤分类:** 誤分類すると間違ったコンテキストを読み込む
2. **追加レイヤーのオーバーヘッド:** ルーティング自体がレイテンシとトークンを消費
3. **動的ドメイン対応:** 新しいドメインが増えるとルーティングルールも更新が必要

## Harness Engineeringとの関係

[[context-engineering]] の横断技術として、Context Routingは「エージェントに何を見せるか」の設計判断を自動化するパターン。

## Related Concepts

- [[context-engineering]] — コンテキスト最適化の統合フレームワーク
- [[context-compression]] — コンテキスト圧縮技術
- [[harness-engineering/system-architecture/advanced-tool-use]] — 高度なツール使用
- [[agentic-rag]] — エージェント制御の検索ループ
