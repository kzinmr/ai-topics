---
title: Browserbase
type: entity
aliases:
- browserbase-hq
- stagehand
created: 2026-04-13
updated: 2026-04-13
tags:
- entity
- technology
- browser-agent
- infrastructure
- dom-based
status: active
sources:
- https://www.browserbase.com/
- https://www.browserbase.com/blog/stagehand-v3
- https://docs.browserbase.com/introduction/stagehand
- https://www.browserbase.com/blog/introducing-the-stagehand-api
---

# Browserbase

**Browserbase**は、AIエージェント向けの信頼性の高いブラウザ自動化インフラを提供するプラットフォーム。「the where（どこで実行するか）」を担当し、Stagehand（the what）とStagehand API（the how）と統合された3層アーキテクチャを構築している。

## 概要

| 項目 | 内容 |
|---|---|
| 評価額 | $300M（Series B） |
| 主要顧客 | Vercel, Perplexity, Clay |
| オープンソース | Stagehand（22k+ GitHub stars, 700k+ weekly downloads） |
| コアバリュー | セキュアなブラウザフリート管理、スケーラビリティ |

## 3層プラットフォームアーキテクチャ

```
┌─────────────────────────────────────────────┐
│  Stagehand（the what）                       │
│  オープンソースAI自動化フレームワーク          │
│  自然言語コマンド: act(), extract(), observe()│
├─────────────────────────────────────────────┤
│  Stagehand API（the how）                    │
│  ホスト型インテリジェンスエンジン               │
│  プロンプト → CDPアクション変換・最適化        │
├─────────────────────────────────────────────┤
│  Browserbase（the where）                    │
│  クラウドブラウザインフラ                      │
│  セキュア、スケーラブル、ステルス               │
└─────────────────────────────────────────────┘
```

## Stagehand v3（2025年10月）

### Playwrightからの卒業
- Playwright依存を排除、プロトコルレベルで動作
- モジュラードライバーシステム導入
- Bunを含む複数環境でネイティブ動作
- iframes/shadow DOMのトラバースを強化

### 性能改善
- v2比で全ベンチマークで44%+高速
- 深くネストされたiframe/shadow DOMで顕著な改善
- CI/CD統合の最適化

### 対応言語
- **TypeScript/Node.js**: `npx create-browser-app`
- **Python**: `uv run` + stagehand SDK
- **Java / Go / Ruby**: SDK対応

## 主要機能

1. **ホストブラウザフリート**: スケール対応のセキュアなブラウザ環境
2. **Session Inspector**: 全てのAI決定を可視化・デバッグ
3. **Model Gateway**: LLMリクエストをBrowserbase APIキーでルーティング
4. **MCP Server**: インフラ上で直接実行（2026年3月）
5. **Fetch API**: ブラウザベースのデータ取得（2026年3月）
6. **Search**: ブラウザ内検索機能（2026年3月）
7. **Concurrency**: フリープランで1→3に拡張（2026年3月）
8. **Prime Intellect連携**: ブラウザエージェントのトレーニング・評価（2026年3月）

## browser-useとの違い

| 次元 | Browserbase | browser-use |
|---|---|---|
| 焦点 | インフラ（ホスティング） | フレームワーク（操作ロジック） |
| Stagehand | 自然言語コマンド | Agentループ |
| 提供 | マネージドブラウザ | ローカル/クラウドどちらでも |
| OSS | Stagehandのみ | コアライブラリ全体 |
| 補完 | 併用可能 | Browserbase Cloudと連携可能 |

## 関連エンティティ

- [[browser-use]] — オープンソースブラウザ自動化
- [[concepts/death-of-browser]] — ブラウザの脱人間化潮流
- [[webmcp]] — 標準化プロトコル
- [[anthropic-computer-use]] — スクリーンショットベースアプローチ

## Sources

- [Stagehand v3 Announcement](https://www.browserbase.com/blog/stagehand-v3)
- [Stagehand API](https://www.browserbase.com/blog/introducing-the-stagehand-api)
- [Stagehand Documentation](https://docs.browserbase.com/introduction/stagehand)
