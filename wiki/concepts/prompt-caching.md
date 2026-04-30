---
title: "Prompt Caching Strategies"
tags: [caching-performance-cost-optimization]
created: 2026-04-13
updated: 2026-04-24
type: concept
---

# Prompt Caching Strategies

LLM API呼び出しにおけるキャッシングの設計パターン。コスト削減とレイテンシ改善のために、どの部分をキャッシュし、いつ無効化するかを体系的に扱う。

## Core Concept

LLMのAPI呼び出しには**静的部分**と**動的部分**が存在する：

```
[Static: システムプロンプト, few-shot例, ドメイン知識]
+
[Dynamic: ユーザー入力, 最新コンテキスト]
→
キャッシュ可能な部分 = Static
```

## Caching Levels

### Level 1: Static Prefix Caching

システムプロンプトやテンプレートをキャッシュ：
- 同一プロンプトの再利用
- バージョン管理で更新検知
- TTL（Time To Live）で鮮度管理

### Level 2: Semantic Caching

意味的に類似した入力をキャッシュ：
- 埋め込みベースの類似度検索
- 閾値（例: 0.9以上）でキャッシュヒット判定
- 微妙な違いでも別のキャッシュエントリ

### Level 3: Partial Response Caching

応答の一部を再利用：
- 共通の出力的構造をキャッシュ
- 動的部分のみ再生成
- テンプレート+穴埋めパターン

### Level 4: Tool Call Caching

ツールの実行結果をキャッシュ：
- 同一パラメータの呼び出し結果
- 外部APIの応答キャッシュ
- ファイルI/Oの結果保持

## Invalidation Strategies

| Strategy | When to Use | Trade-off |
|----------|-------------|-----------|
| TTLベース | 時間経過で陳腐化するデータ | 期限前に更新される可能性 |
| バージョンベース | プロンプト変更時 | 厳密だが管理コスト |
| LRU | メモリ制限がある場合 | 古い有用なデータが消える |
| 意味的変更検知 | ドリフトが重要な場合 | 検知アルゴリズムが必要 |

## Implementation Patterns

### Cache Key Design

```
cache_key = hash(
    prompt_template_version +
    system_prompt_hash +
    few_shot_examples_hash +
    tool_definitions_hash
)
```

### Cache Storage

- **インメモリ**: 高速だが永続化されない
- **ディスク**: 永続化だが遅い
- **Redis/外部ストア**: 分散環境向け
- **階層キャッシュ**: ホットはメモリ、コールドはディスク

### Cache Hit Optimization

- プロンプトの正規化（空白・改行の統一）
- 意味的等価性の判定
- キャッシュウォーミング（事前ロード）

## Metrics to Track

1. **Cache Hit Rate**: どの程度キャッシュが再利用されているか
2. **Cost Savings**: キャッシングによる費用削減額
3. **Latency Reduction**: 応答時間の改善
4. **Stale Cache Rate**: 古いキャッシュが使用された割合

## Related

- [[concepts/evaluation-flywheel]] — Evaluation Flywheel
- [[concepts/context-window-management]] — Context Window Management
- [[concepts/inference-speed-development]] — Inference Speed Development
- [[concepts/agentic-scaffolding]] — Agentic Scaffolding

## Claude Code Production Caching Lessons (Anthropic, 2026)

Claude Code builds its entire harness around prompt caching. A high cache hit rate decreases costs and enables generous rate limits — they run alerts on cache hit rate and declare SEVs if it's too low. Key production lessons:

### Static First, Dynamic Last — Order Is Everything

Prompt caching works by prefix matching — the API caches everything from the start of the request up to each `cache_control` breakpoint. For Claude Code:

```
Static system prompt & Tools (globally cached)
→ Claude.MD (cached within a project)
→ Session context (cached within a session)
→ Conversation messages (dynamic)
```

**Fragility alert**: This ordering can break from: putting a timestamp in the static system prompt, shuffling tool order non-deterministically, updating tool parameter definitions, etc.

### Use Messages for Updates, Not Prompt Changes

When information becomes stale (time changes, user edits a file), do NOT update the prompt — that causes a cache miss. Instead, insert `<system-reminder>` tags in the next user message or tool result (e.g., "it is now Wednesday"). This preserves the cache.

### Never Change Models Mid-Session

Prompt caches are unique to models. If you're 100K tokens into a conversation with Opus and want a simple question answered, switching to Haiku is **more expensive** because the cache must be rebuilt. If you need model switching, use subagents with handoff messages.

### Never Add or Remove Tools Mid-Session

Changing the tool set invalidates the cache for the entire conversation — one of the most common cache-breaking mistakes.

### Plan Mode — Design Around the Cache

Instead of swapping tool sets when entering plan mode (which breaks cache), Claude Code keeps ALL tools in the request at all times and uses `EnterPlanMode`/`ExitPlanMode` as tools themselves. The model can autonomously enter plan mode when it detects a hard problem — no cache break.

### Tool Search — Defer Instead of Remove

For dozens of MCP tools: send lightweight stubs (`defer_loading: true`) that stay in the prefix. The model discovers full schemas via a `ToolSearch` tool when needed. Same stubs, same order → stable cache.

### Cache-Safe Forking (Compaction)

When compacting the context window, use the **exact same system prompt, tools, and history** as the parent conversation. Append the compaction prompt as a new user message at the end. From the API's perspective, this looks nearly identical to the parent's last request — cached prefix is reused. The only new tokens are the compaction prompt itself.

### Monitor Cache Hit Rate Like Uptime

Claude Code treats cache breaks as incidents. A few percentage points of cache miss rate can dramatically affect cost and latency. **Build your agent around prompt caching from day one.**

Source: [[entities/claude-code]] engineering team, "Lessons from Building Claude Code: Prompt Caching Is Everything" (April 2026)

