---
title: Hermes Agent Architecture Analysis
category: other
status: active
---

# Hermes Agent Architecture Analysis

**Author:** Kazuki Inamura
**Date:** 2026-04-16
**Source:** Analysis based on official Hermes Agent v0.9.0 documentation and repository

## 全体像

一番大きな見方をすると、Hermes は
**入力面**（CLI / messaging gateway / ACP / cron / batch）
→ **実行コア**（`run_agent.py` の `AIAgent`）
→ **支援層**（prompt builder、provider resolver、tool registry、compression、memory/session）
→ **外部接続**（terminal backends、platform adapters、MCP、plugins）
という層構造です。

## 1) 中心コアは `AIAgent`

Hermes のアーキテクチャ上の中心は `run_agent.py` の `AIAgent` です。公式 docs では、このクラスの責務として **effective prompt の組み立て、provider/API mode の選択、interruptible な LLM call、tool 実行、session history 維持、compression / retry / fallback model 処理** が挙げられています。

このコアは 3 つの API execution mode を持ちます。`chat_completions`、`codex_responses`、`anthropic_messages` で、provider 選択や base URL の解決に応じて切り替わります。

また、UI や integration は callback surface でコアにぶら下がります。`tool_progress_callback`、`thinking_callback`、`clarify_callback`、`stream_delta_callback` などがあり、CLI、gateway、ACP がこの面から進捗表示や承認フローを実現します。

## 2) 1ターンの実行フロー

1. ユーザーメッセージを履歴へ追加
2. 必要なら preflight compression
3. cached system prompt をロードまたは構築
4. API 用の messages を作り、ephemeral layer を注入
5. prompt caching を適用して LLM を呼ぶ
6. 返答が tool call なら tool を実行して履歴へ結果を戻し、最終テキストなら session を保存して返す

Hermes は **interruptible call** を標準で持ち、実行中にユーザーから新しい入力が来たら停止・割り込みできる。複数 tool call が返った場合は **single/interactive tool は逐次**, **non-interactive tool 群は並列** という使い分け。

親子 agent 間で **shared iteration budget** を持ち、fallback model もサポート。

## 3) Prompt Assembly

**cached system prompt** と **ephemeral additions** を明確に分離。

cached system prompt の組み立て順:
1. `SOUL.md` 由来の agent identity
2. tool-aware behavior guidance
3. Honcho static block
4. optional system message
5. frozen MEMORY snapshot
6. frozen USER snapshot
7. skills index
8. context files
9. timestamp / optional session ID
10. platform hint

memory も context files も mid-session では基本的に固定。prompt caching は Anthropic native と Claude-via-OpenRouter 系で **system prompt + 直近3つの non-system messages** を対象 (TTL デフォルト 5 分)。

## 4) 永続 State: Sessions, Memory, Search

**二層の永続化:**
- `~/.hermes/state.db` (SQLite + FTS5) — session ID, platform, user ID, title, model, system prompt snapshot, message history, token counts, timestamps
- `~/.hermes/sessions/` (JSONL) — raw transcripts

**三層の記憶:**
- built-in memory (MEMORY.md + USER.md)
- searchable session archive
- external memory provider (Honcho, RetainDB, ByteRover)

compression 後は session lineage が分岐し、親 session ID を DB に保持。

## 5) Tool Runtime

**self-registering registry:** 各 tool module が import 時に `registry.register()` を呼び、AST で発見。

toolsets: web, terminal, file, browser, vision, image_gen, skills, memory, session_search, cronjob, code_execution, delegation, clarify, MCP

実行時: plugin pre-hook → registry dispatch → plugin post-hook

安全面: terminal tool が `DANGEROUS_PATTERNS` による approval flow

## 6) Subagent Delegation vs `execute_code`

**delegate_task:** child `AIAgent` を起動。goal + context だけ。最大 3 並列。

**execute_code:** Python script を書き、RPC で tool call。機械的 multi-step pipeline 用。

## 7) Gateway

**常駐フロントエンド層:** 14+ messaging platform を統一アーキテクチャ。

**two-level message guard:** 実行中 session への新規入力は queue + interrupt event。

background maintenance: cron ticking, session expiry, memory flush, cache refresh

## 8) Provider Runtime

解決優先度: 明示指定 > config.yaml > environment variables > provider defaults/auto

auxiliary task は main model と独立。fallback model は main agent loop 用。

## 9) Extension Model

3 種の plugin: general, memory provider, context engine

hooks: pre_tool_call, post_tool_call, pre_llm_call, post_llm_call, on_session_start, on_session_end

## 設計上の特徴

1. **AIAgent中心主義** — 重心はコアに集約
2. **prompt-cache-aware な state 設計** — cache stability を制約として組み込み
3. **三層の記憶** — durable facts と履歴資産を分離
4. **実行 primitive の分離** — 様式ごとに primitive を分け、token cost と isolation の哲学も異なる

## トレードオフ

- `AIAgent` の責務が広い → コア実装の複雑性が高い
- memory の安定性優先 → 即時性より整合性
- subagent の blank-slate → 親コンテキスト汚染防止だが goal/context の質が重要

## コードを読む順番

`run_agent.py` → `agent/prompt_builder.py` → `agent/context_compressor.py` → `model_tools.py` / `tools/registry.py` → `hermes_state.py` → `gateway/run.py` → `gateway/session.py`
