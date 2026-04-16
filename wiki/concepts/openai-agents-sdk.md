---
title: "OpenAI Agents SDK"
created: 2026-04-16
updated: 2026-04-16
tags: [llm, ai-agents, framework, product, tooling]
aliases: ["Agents SDK", "OpenAI Agent Framework"]
---

# OpenAI Agents SDK

## Overview

OpenAI Agents SDKは、プロダクション対応のエージェント構築のための公式Pythonフレームワーク。2026年4月v0.14.0で**サンドボックス実行機能**をGAリリースし、モデルネイティブなインフラストラクチャを提供。エージェントがファイル検査、コマンド実行、コード編集、長期マルチステップタスクを安全な分離環境で実行可能に。

**設計哲学:** 「Turnkey yet flexible — カスタムインフラのオーバーヘッドを最小化しつつ、ツール、メモリ、サンドボックス環境の完全な制御を維持」

## Key Capabilities

### Standardized Integrations
- **MCP** — ツール使用の標準プロトコル
- **Skills** — プログレッシブディスクロージャー（必要な時に必要なインストラクションをロード）
- **AGENTS.md** — カスタムインストラクションバンドル
- **Shell** — コード実行ツール
- **Apply Patch** — ファイル編集ツール

### Sandbox Execution
- ネイティブサンドボックス実行 — 安全なファイルI/O、依存関係インストール、ツール実行
- ワークスペースポータビリティ (`Manifest`抽象化)
- マルチクラウドストレージ: **AWS S3, GCS, Azure Blob Storage, Cloudflare R2**

### Provider Ecosystem
ビルトイン互換性: **Blaxel, Cloudflare, Daytona, E2B, Modal, Runloop, Vercel**（またはカスタムサンドボックス持込可能）

## Architecture: Harness vs Compute Separation

OpenAI Agents SDKの中心的な設計原則は、**オーケストレーション（Harness）と実行（Compute）の明確な分離**:

> *"The key split is the boundary between the harness and compute. The harness is the control plane around the model... Compute is the sandbox execution plane where model-directed work reads and writes files, runs commands, installs dependencies, uses mounted storage, exposes ports, and snapshots state."*

### Harness (コントロールプレーン)
- モデルへの指示、メモリ管理、ツールルーティング
- 資格情報の管理（モデル生成コードから分離）
- サブエージェントのルーティングと並列実行オーケストレーション
- 状態のスナップショットとリエハイドレーション

### Compute (実行プレーン)
- ファイル読み書き、コマンド実行
- 依存関係インストール、ポート公開
- サンドボックス内の状態保持
- アーティファクト生成（CSV, JSONL, スクリーンショット等）

### Benefits
| 側面 | メリット |
|------|----------|
| **セキュリティ** | 資格情報とモデル生成コードを隔離。プロンプトインジェクション・データ漏洩リスクを軽減 |
| **耐久性** | 外部化されたエージェント状態。サンドボックス障害からのシームレスなリカバリ |
| **スケーラビリティ** | オンデマンド起動、サブエージェント分離、コンテナ間並列実行 |

## Core Components

### SandboxAgent
エージェント定義とデフォルトのサンドボックス設定を組み合わせた単位。

```python
agent = SandboxAgent(
    name="Dataroom Analyst",
    model="gpt-5.4",
    instructions="Answer using only files in data/. Cite source filenames.",
    default_manifest=Manifest(entries={"data": LocalDir(src=dataroom)}),
)
```

### Manifest
新規セッションのワークスペース契約。初期ファイル、ディレクトリ、リポジトリ、マウント、環境変数、ユーザー/グループを定義。

- **パスルール:** ワークスペース相対のみ。絶対パスや`..`エスケープ禁止
- **ベストプラクティス:** リポジトリ、入力アーティファクト、出力ディレクトリをマニフェストに配置
- **セキュリティ:** シークレットはマニフェストに埋め込まず、プロバイダネイティブのシークレット管理を使用

### Capabilities
サンドボックスネイティブの動作を定義:
- **デフォルト:** `Filesystem()`, `Shell()`, `Compaction()`
- **カスタム:** `Skills` (繰り返し可能インストラクション)、`Memory` (クロスランメモリ)

### Session Resolution Order
1. `run_config.sandbox.session` → ライブセッション直接再利用
2. `RunState` からのレジューム → 保存済み状態を使用
3. `run_config.sandbox.session_state` → シリアライズ済み状態からの明示的レジューム
4. フォールバック → 新規セッション作成

## Memory System

クロスランメモリは会話メモリ(`Session`)とは独立し、過去の教訓・好み・修正を読みやすいファイルに要約:

- `Memory()` → 読み取り + 生成（デフォルト）
- `Memory(generate=None)` → 読み取り専用
- `Memory(read=None)` → 生成専用
- **プログレッシブディスクロージャー:** SDKが`memory_summary.md`をインジェクト → エージェントが`MEMORY.md`を検索 → 必要に応じてロールアウトサマリーを展開

ストレージ構成:
```
workspace/
  sessions/<rollout-id>.jsonl
  memories/
    memory_summary.md
    MEMORY.md
    raw_memories.md
    raw_memories/<rollout-id>.md
    rollout_summaries/<rollout-id>_<slug>.md
    skills/
```

## When to Use

### Use Sandbox Agents when:
- ファイル操作やコマンド実行が必要
- 永続ワークスペースが必要（データマウント、アーティファクト生成）
- 人間レビュー/レジュームワークフロー
- ポート公開サービス（ノートブック、プレビュー）

### Skip Sandbox Agents when:
- 短いレスポンスのみ（永続ワークスペース不要）→ Responses APIまたは基本Agents SDK
- 稀なシェルアクセスのみ → ホステッドシェルツール

## Pricing & Availability
- **GA** via API (Python SDK、TypeScriptは予定)
- 標準API価格（トークン + ツール使用ベース）
- 今後の機能: コードモード、サブエージェント、サンドボックスプロバイダ統合拡大

## Customer Validation
> *"The updated Agents SDK made it production-viable for us to automate a critical clinical records workflow that previous approaches couldn't handle reliably enough. For us, the difference was not just extracting the right metadata, but correctly understanding the boundaries of each encounter in long, complex records."*
> — **Rachael Burns**, Staff Engineer & AI Tech Lead, Oscar Health

## Related Concepts
- [[harness-engineering]] — Ryan Lopopolo / OpenAI Symphonyのハーネスエンジニアリング哲学
- [[sandbox/_index]] — AIエージェントのサンドボックス分離技術全般
- [[sandbox/infrastructure]] — コンテナ、microVM、gVisorレベルの分離
- [[sandbox/in-process]] — Monty、capabilities-basedセキュリティ
- [[agent-skills]] — SKILL.mdバンドル
- [[agentic-engineering/how-agents-work]] — コーディングエージェントの動作原理

## Entity Connections
- [[entities/openai]] — 開発元
- [[entities/samuel-colvin]] — Monty（インプロセスサンドボックス）開発者
- [[entities/anthropic]] — 競合（Managed Agents、Computer Use）
- [[entities/cognition]] — 競合（Devin）

## Sources
- [[raw/articles/openai-agents-sdk-next-evolution-2026-04]]
- [[raw/articles/openai-sandbox-agents-api-guide-2026-04]]
- [OpenAI Agents SDK Blog (2026-04-15)](https://openai.com/index/the-next-evolution-of-the-agents-sdk/)
- [OpenAI API Sandbox Docs](https://developers.openai.com/api/docs/guides/agents/sandboxes)
