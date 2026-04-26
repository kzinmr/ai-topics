---
title: "Prompt Caching Strategies"
tags: [[caching-performance-cost-optimization]]
created: 2026-04-13
updated: 2026-04-24
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

- [[evaluation-flywheel]] — Evaluation Flywheel
- [[context-window-management]] — Context Window Management
- [[inference-speed-development]] — Inference Speed Development
- [[agentic-scaffolding]] — Agentic Scaffolding
