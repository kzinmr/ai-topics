---
title: Claude Perfect Memory
type: concept
created: 2026-04-27
updated: 2026-04-27
status: L2
sources: [https://x.com/i/article/2044531930671288320, https://code.claude.com/docs/en/memory, https://milvus.io/blog/claude-code-memory-memsearch.md]
tags: [claude-code, memory-systems, claude-md, auto-memory, context-engineering, agent-architecture]
aliases: [claude-memory, claude-code-memory]
---

# Claude Perfect Memory

Claude Code（AnthropicのAIコーディングエージェント）が持つ**多層記憶システム**の完全指南。Gul Jabeen（@techwithgul.ai）が2026年3月にMediumで公開し、8,194件のブックマーク、170万インプレッションを記録した。

## Core Problem: Stateless AI

Claudeのコンテキストウィンドウは**ホワイトボード**のようなもの。毎セッション、クリアされる。これはバグではなくLLMの基本原理。記憶システムの本質は一つ:

> 自分で記憶を構築する以外、セッション間の文脈保持は不可能。

## 4-Layer Memory Architecture

Claude Codeの記憶システムは4層で構成される:

### 1. CLAUDE.md — 手動ルールファイル

| スコープ | パス | 説明 |
|----------|------|------|
| **Managed Policy** | `/Library/.../CLAUDE.md` (macOS) | 組織全体 |
| **Project** | `./CLAUDE.md` | リポジトリ共用 |
| **User** | `~/.claude/CLAUDE.md` | 個人（全プロジェクト） |
| **Local** | `./CLAUDE.local.md` | 個人（gitignore済み） |

**ベストプラクティス**:
- 150行以内（短いが忠実に従われる）
- 箇条書き（段落より速く解析）
- 重要パスの明示（500ファイル超で検索50%削減）
- コード例（3-5個、修正依頼を大幅削減）
- 禁止事項の明示（ポジティブ推奨より効果的）

### 2. Auto Memory — 自動ノート

| 設定 | 値 |
|------|------|
| **場所** | `~/.claude/projects/<project>/memory/` |
| **エントリーポイント** | `MEMORY.md` |
| **ロード制限** | 最初200行または25KB |
| **カテゴリ** | user / feedback / project / reference |
| **ロード方式** | 最初の200行が全セッションで自動ロード、トピックファイルはオンデマンド |

```
~/.claude/projects/<project>/memory/
├── MEMORY.md              ← index (1行≤150文字)
├── feedback_testing.md
├── project_auth_rewrite.md
└── reference_linear.md
```

**自動制御**:
- 無効化: `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1 claude`
- 有効化: `CLAUDE_CODE_DISABLE_AUTO_MEMORY=0 claude`

### 3. Auto Dream — 自動クリーンアップ

- **目的**:  staleな記憶を整理
- **処理内容**:
  - 「昨日のdeploy問題」→「2026-03-28 deploy問題」に置換
  - 矛盾の解決（PostgreSQL→MySQL）
  - 削除されたファイル参照の削除
- **トリガー**: 24時間以上経過 + MEMORY.mdが200行超
- **限界**: 数日のクラッターは処理可能、数ヶ月は跨げない

### 4. KAIROS — 未公開の常時デーモン

- Claude Codeの漏洩ソース（v2.1.88のsource map）に含まれる
- **常にオン**のメモリデーモンモード
- 2026年4月時点で**未公開ビルド**
- 長期間の記憶跨ぎを可能にする可能性

## Modular Rules (`.claude/rules/`)

パス特異的なルールをYAML frontmatterで指定:

```yaml
---
paths: ["src/api/**/*.ts"]
---
# API Development Rules
- All API endpoints must include input validation
- Use Zod for schema validation
```

**パフォーマンス改善**:
- コンテキストトークン: 2,000 → 1,200 (-40%)
- 指示関連性: +35%
- 修正数: 5 → 3 (-40%)
- レスポンスタイム: 45s → 30s (-33%)

## Key Commands

| コマンド | 用途 |
|----------|------|
| `/init` | プロジェクト記憶の初期化 |
| `/memory` | 記憶ファイルの直接編集 |
| `/config` | 設定変更（settings.jsonに永続化） |
| `@path/to/file` | 外部ファイルのインポート（最大5階層再帰） |

## Limitations

1. **200行制限**: MEMORY.mdは200行までしかロードされない
2. **完全キーワードマッチ**: 意味ベースの検索は不可（「ポート衝突」で「docker-composeマッピング」はヒットしない）
3. **ローカル限定**: 記憶はClaude Code内から外に出ない
4. **他エージェントに継承不可**: 他のエージェントに切り替えたらゼロから

## External Solutions

- **claude-mem** ([thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)): Open標準AI agent memory — RAG + RAD（Retrieval Augmented Discovery）
- **Milvus Memsearch**: クラウドベースのセマンティック検索でClaude Codeの記憶ギャップを補完

## Significance

Claude Perfect Memoryは、**「エージェントのセッション間記憶」の重要性を広く認識させるきっかけ**となった。8,194件のブックマークは、ソロファウンダー・AIエンジニアにとって「コンテキストエンジニアリング」がコアスキルへ成長していることを示す。

## Related Concepts

- [Solo Founder Stack](solo-founder-stack.md) — コンテキストエンジニアリングはソロfounderの核心スキル
- [CLAUDE.md](claude-md-pattern.md) — 構造化記憶ファイルパターン
- [Context Engineering](context-engineering.md) — 情報環境の設計
