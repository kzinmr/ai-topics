---
title: "Monty Sandbox"
type: concept
aliases:
  - monty-sandbox
  - pydantic-monty
created: 2026-04-25
updated: 2026-04-29
tags:
  - concept
  - sandbox
  - pydantic
  - code-execution
  - agent-safety
status: complete
sources:
  - url: "https://github.com/pydantic/monty"
    title: "Pydantic Monty — GitHub Repository"
  - url: "https://pydantic.dev/articles/pydantic-monty"
    title: "Pydantic Monty: You probably don't need a full sandbox (Samuel Colvin, 2026-02)"
  - url: "https://pydantic.dev/articles/hack-monty"
    title: "Hack Monty: Win $5000 Breaking Pydantic's Python Sandbox"
  - url: "https://simonwillison.net/2026/Feb/6/pydantic-monty/"
    title: "Running Pydantic's Monty Rust Sandboxed Python Subset in WebAssembly (Simon Willison, 2026)"
---

# Monty Sandbox

**Monty** は、Pydantic（Samuel Colvin）が開発した、Rust で書かれたミニマルでセキュアな Python インタプリタ。AI エージェントが生成したコードを安全に実行するために設計されている。従来のコンテナベースのサンドボックス（Docker, E2B など）と比較して、起動時間が **マイクロ秒単位** と圧倒的に高速。

## 定義 / コアアイデア

Monty は「フルサンドボックスは必要ない」という哲学に基づく。コンテナ全体を起動する代わりに、ホスト環境へのアクセスを完全にブロックした**カスタム Python ランタイム**を提供する。外部とのやり取りは、開発者が明示的に公開した関数経由のみ許可される。

## アーキテクチャ

```
LLM が生成した Python コード
        ↓
    Monty (Rust 製 インタプリタ)
        ↓
   Ruff パーサ → バイトコードコンパイル → 実行
        ↓
   外部関数コール → ホストの Python/Rust/JS コード
```

### 技術的特徴
- **Rust 製の独自バイトコード VM** — CPython の制限版ではなく、スクラッチから実装
- **Ruff パーサ**（Astral）を使って Python ソースをパース
- **型チェック内蔵** — `ty`（Ruff の型チェッカー）を同梱
- **スナップショット可能** — 外部関数コール時に状態をバイト列化して保存・復元可能
- **依存関係ゼロ** — 単一の Rust バイナリで動作

## パフォーマンス

| 指標 | 値 |
|------|------|
| 起動時間（型チェックなし） | **4.5μs**（マイクロ秒） |
| 起動時間（型チェックあり） | ~4.8ms |
| コンテナサンドボックス比 | 100〜10,000 倍高速 |
| ランタイム速度 | CPython の 0.2〜5 倍（タスク依存） |

## セキュリティモデル

Monty は「許可リスト（allowlist）」アプローチを採用：
- **ファイルシステム**: デフォルトで完全ブロック
- **環境変数**: デフォルトで完全ブロック
- **ネットワーク**: デフォルトで完全ブロック
- **外部関数**: ホストが明示的に渡した関数のみ実行可能
- **$5,000 バグ報奨金**プログラム（Hack Monty）運用中

### できること / できないこと

| カテゴリ | ✅ サポート | ❌ 未サポート |
|----------|-----------|-------------|
| 制御フロー | if/else, for, while, try/except | — |
| データ構造 | dict, list, set, tuple, str, int, float | クラス定義（近日対応予定） |
| 関数 | 関数定義・呼び出し、λ式（制限あり） | — |
| モジュール | ホスト提供の外部関数のみ | import 文 |
| 並行処理 | async/await（一部） | スレッド・プロセス |

## ユースケース

1. **AI エージェントのコード実行** — LLM が生成した Python コードを安全に実行
2. **コードモード（CodeMode）** — Cloudflare が提唱する「LLM にツール単位ではなくコードを書かせる」方式
3. **エッジデバイス** — Rust バイナリなので組み込みシステムや宇宙機でも動作可能
4. **ブラウザ内実行** — WebAssembly にコンパイルしてブラウザ内サンドボックスとしても利用可能（Simon Willison が実証）

## 関連概念

- [[concepts/agent-loop-orchestration]] — エージェントループ内でのコード実行
- [[concepts/claude-code-best-practices]] — Claude Code のベストプラクティス
- [[concepts/reverse-engineering]] — サンドボックス回避とセキュリティ研究
- [[concepts/agent-orchestration-frameworks]] — エージェントフレームワークでのコード実行

## ソース

- [Pydantic Monty GitHub](https://github.com/pydantic/monty)
- [Pydantic Monty: You probably don't need a full sandbox](https://pydantic.dev/articles/pydantic-monty)
- [Hack Monty Bounty Program](https://pydantic.dev/articles/hack-monty)
- [Simon Willison: Running Pydantic's Monty in WebAssembly](https://simonwillison.net/2026/Feb/6/pydantic-monty/)
