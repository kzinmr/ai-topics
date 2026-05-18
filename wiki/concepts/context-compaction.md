---
title: "Context Compaction"
type: concept
aliases:
  - context-compaction
  - pre-compaction-flush
created: 2026-04-25
updated: 2026-05-17
tags:
  - concept
  - context-engineering
  - memory-systems
  - agent-architecture
status: complete
sources:
  - https://snowan.gitbook.io/study-notes/ai-blogs/openclaw-memory-system-deep-dive
  - https://github.com/openclaw/openclaw/blob/f99e3ddd6d6fc59173f7260c5d2ae0cffa4e30e0/docs/concepts/memory.md
---

# Context Compaction

AIエージェントが長時間の会話でコンテキストウィンドウ制限に達した際、古いメッセージを要約・切り詰めて新しい会話のためのスペースを確保するプロセス。

---

## 基本的メカニズム

コンテキストコンパクションは以下のパターンで動作する:

1. 会話がコンテキストウィンドウの閾値（例: 80%）に達する
2. システムが古いメッセージをLLM経由で要約
3. 要約をコンテキストの「圧縮表現」として注入し、生メッセージを解放
4. 新しいメッセージのためのスペースを確保

**根本的問題**: コンパクション時に要約されなかった情報は **永久に失われる**。これに対処するため、一部のハーネスはコンパクション **前** にメモリ保存をトリガーする。

---

## Pre-Compaction Flush（コンパクション前フラッシュ）

OpenClawが実装する革新的なアプローチ。会話がコンテキスト制限に近づくと、**サイレントなエージェントターン** を発動し、コンパクション **前** に永続メモリへの書き込みを促す。

### 発動条件

- コンテキスト使用率が約80%に達した時点
- コンパクションサイクルごとに1回のみ（スパム防止）
- Read-onlyサンドボックスモードではスキップ

### 動作

- 通常は **`NO_REPLY`**（保存すべき重要事項がない場合は無言で通過）
- 重要な文脈がある場合のみ、エージェントが `memory/` または `MEMORY.md` に書き込み
- 人間の介入なしで自動動作

### 設計意図

> 「コンパクションは不可避。だが、コンパクション **前** にエージェントに最後の発言権を与えることで、貴重なコンテキストを救出できる。」 — OpenClaw Memory Docs

---

## ハーネス別コンパクションアプローチ

| ハーネス | コンパクション方式 | Pre-Compaction Flush | コンパクション後メモリ |
|---|---|---|---|
| **OpenClaw** | Markdown要約を `memory/` に追記 | ✅ 自動（~80%使用時） | 今日+昨日の日次ログ読み込み |
| **Claude Code** | 5層コンパクションパイプライン（段階的要約） | ❌ | CLAUDE.md + MEMORY.md 再読み込み |
| **Codex CLI** | 抽出→統合の2フェーズ非同期パイプライン | ❌（非同期生成のため不要） | `memory_summary.md` 読み込み |

---

## Related

- [[comparisons/agent-memory-systems-comparison]] — OpenClaw/Claude Code/Codexメモリシステム比較
- [[entities/openclaw]] — OpenClaw entity（Memory SystemセクションにPre-Compaction Flush詳細あり）
- [[entities/claude-code--architecture]] — Claude Code 5層コンパクションパイプライン
- [[concepts/claude-perfect-memory]] — Claude Codeのメモリ設計哲学
- [[raw/articles/2026-01-25_snowan-gitbook_openclaw-memory-system-deep-dive]] — 元記事
