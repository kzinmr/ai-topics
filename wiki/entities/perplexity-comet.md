---
title: Perplexity Comet
aliases:
- comet-browser
- perplexity-ai-browser
- perplexity-computer
created: 2026-04-13
updated: 2026-04-13
tags:
- entity
- product
- browser-agent
- ai-browser
- perplexity
status: active
sources:
- https://en.wikipedia.org/wiki/Perplexity_Comet
- https://www.infoworld.com/article/4081396/when-will-browser-agents-do-real-work.html
- https://till-freitag.com/en/blog/perplexity-comet-ai-browser
---

# Perplexity Comet

**Perplexity Comet**は、Perplexity AIが開発したAIネイティブブラウザ。2025年7月にWindows/macOSでリリースされ、同年11月にAndroid、2026年3月にiOSに対応。「ブラウザをAIエージェントにする」戦略の最前線に位置する製品。

## 概要

| 項目 | 内容 |
|---|---|
| 開発元 | Perplexity AI |
| 初回リリース | 2025年7月9日（Windows/macOS） |
| Android | 2025年11月20日 |
| iOS | 2026年3月18日 |
| エンジン | Blink（Chromiumベース） |
| ライセンス | プロプライエタリ（OSSベース） |
| AIエンジン | Perplexity検索API統合 |
| 価格 | 無料ブラウザ、AI機能はPerplexity Pro（$20/月） |

## アーキテクチャ: Search-First Browser

Cometの核心は**検索ファーストアーキテクチャ**。従来のブラウザが「URLを入力 → ページをレンダリング → ユーザーが読む」というフローだったのに対し、Cometは**ユーザーの意図を直接理解し、エージェントがウェブ上でタスクを代行**する。

### Agentic Browsing機能
1. **自然言語タスク**: 「来週ベルリンへの cheapest flight を探して」→ Cometが検索、比較、結果提示
2. **コンテキストAI**: 任意のテキストをハイライトして質問 → ページ文脈を理解して回答
3. **マルチタブ合成**: 複数タブにまたがる情報収集・要約
4. **フォーム自動入力**: 購入、予約、申込を代行

### Perplexity製品エコシステム
```
┌─────────────────┐
│ Perplexity Search│ ← コアAI検索エンジン（頭脳）
├─────────────────┤
│  Comet Browser  │ ← AIネイティブブラウザ（インターフェース）
├─────────────────┤
│ Perplexity Computer│ ← 自律タスク実行（エージェント）
└─────────────────┘
```

## 競争優位

| 強み | 詳細 |
|---|---|
| 検索統合 | Perplexityの回答ファースト検索をブラウザレベルで統合 |
| 高速性 | ターミナル→検索→結果表示の5ステップを1ステップに圧縮 |
| マルチプラットフォーム | Win/Mac/Android/iOSの4プラットフォーム対応 |
| コスト | ブラウザ自体は無料、AI機能は$20/月 |

## 課題とリスク

1. **セキュリティ**: LayerX Securityが「CometJacking」攻撃ベクターを発見（2025年8月）。悪意あるWebページがAIエージェントに指示を注入可能
2. **プライバシー**: AIが全閲覧を監視するため、データ流出リスク
3. **エコシステムロックイン**: Perplexityサービスへの依存度が高い
4. **自動化の信頼性**: 複雑なタスクでエラー発生

## セキュリティインシデント: CometJacking

2025年、LayerX SecurityはComet特有の攻撃ベクターを発見:
- 悪意あるWebページがAIエージェントに指示を注入
- データ流出、意図しないアクションの実行が可能
- Perplexityは2025年8月に修正パッチをリリース

## 市場ポジション

| 競合 | 特徴 | Cometとの違い |
|---|---|---|
| ChatGPT Atlas | OpenAIのAIブラウザ | GPT統合 vs Perplexity統合 |
| Arc | UI革新 | デザイン中心 vs 検索中心 |
| Brave | プライバシー中心 | ローカルAI vs クラウドAI |
| Kahana Oasis | エンタープライズAIブラウザ | 消費者向け vs 企業向け |

## 関連エンティティ

- [[death-of-browser]] — ブラウザの脱人間化潮流
- [[anthropic-computer-use]] — AnthropicのComputer Use
- [[openai-cua]] — OpenAIのComputer-Using Agent
- [[webmcp]] — 標準化プロトコル
- [[manus]] — ローカルブラウザ統合エージェント

## Sources

- [Wikipedia: Perplexity Comet](https://en.wikipedia.org/wiki/Perplexity_Comet)
- [Perplexity Comet Official Site](https://comet.perplexity.ai/)
- [When will browser agents do real work? (InfoWorld)](https://www.infoworld.com/article/4081396/when-will-browser-agents-do-real-work.html)
- [Perplexity Comet Analysis (Till Freitag)](https://till-freitag.com/en/blog/perplexity-comet-ai-browser)
