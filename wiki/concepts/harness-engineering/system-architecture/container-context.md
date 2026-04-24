---
title: "Container Context"
type: concept
aliases:
  - hosted-container
  - agent-container
  - container-workspace
created: 2026-04-12
updated: 2026-04-12
tags:
  - concept
  - system-architecture
  - harness-engineering
  - infrastructure
status: draft
sources:
  - "https://openai.com/index/equip-responses-api-computer-environment/"
---

# Container Context

エージェントに**永続的な実行環境**を提供するホスト型コンテナ。ファイルシステム、データベース、ネットワークアクセスを統合した「モデルの作業スペース」。

## 3つの柱

### 1. ファイルシステム
- `/workspace` ディレクトリで永続化
- 入力リソースをコンテナにステージング
- **アンチパターン**: 大きなファイル/テーブルをプロンプトに直接貼り付け
- **ベストプラクティス**: リソースをコンテナに配置、モデルが必要なものを選択的に開く

> "Much like humans, models work better with organized information."

### 2. データベース（SQLite）
- 構造化データの保存とクエリ
- スプレッドシート全体をプロンプトにコピーする代わりに、テーブル構造を説明
- モデルが必要な行だけをクエリ可能

**例**:
```
プロンプト: "Which products had declining sales this quarter?"
→ モデルは関連行だけをクエリ（全スキャン不要）
→ より高速、より安価、大規模データセットに拡張可能
```

### 3. ネットワークアクセス
- ライブデータ取得、外部API呼び出し、パッケージインストール
- **サイドカーエグレスプロキシ**で制御
- ドメインスコープのシークレットインジェクション

## コンテナ仕様（2026年3月時点）

| リソース | 値 |
|----------|-----|
| vCPU | 4 |
| RAM | 8GB |
| ワークスペース | 最大10GB |
| プリインストール | Python 3.12, Node.js 22, Go 1.24, Java 21 |
| ストレージコスト | $0.03/GB-hour |

## セッション管理

```bash
# 永続コンテナセッションの作成
session = client.responses.sessions.create(
    model="gpt-5.4",
    tools=[{"type": "shell"}],
    container_config={
        "persist_workspace": True
    }
)
```

## 設計哲学

OpenAIは「開発者が独自の実行環境を構築するのではなく、マネージドコンテナを提供する」アプローチを選択。これは**Anthropicの「開発者がharnessを設計する」**アプローチと対照的。

| | OpenAI | Anthropic |
|--|--------|-----------|
| 実行環境 | マネージドコンテナ | 開発者実装 |
| 柔軟性 | 制限付き（サンドボックス内） | 最大限の制御 |
| 開発者負担 | 最小 | 中〜高 |
| ポータビリティ | OpenAI依存 | モデル非依存 |

## 関連概念

- [[agent-loop-orchestration]] — コンテナ内でのループ実行
- [[concepts/harness-engineering/system-architecture/agent-security-patterns.md]] — ネットワーク制御とシークレット管理
- [[harness-engineering]] — 実行環境設計の上位概念

## 参照

- [OpenAI: Equipping the Responses API with a computer environment](https://openai.com/index/equip-responses-api-computer-environment/)
- [[openai]] — OpenAI
