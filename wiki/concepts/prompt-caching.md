---
title: "Prompt Caching (Paged Attention & Automatic Prefix Caching)"
type: concept
created: 2026-05-09
updated: 2026-05-09
status: L2
tags:
  - kv-cache
  - inference
  - optimization
  - infrastructure
sources:
  - "[[raw/articles/2025-11-30_sankalp_prompt-caching-internals]]"
related:
  - "[[concepts/kv-cache]]"
  - "[[concepts/vllm]]"
  - "[[concepts/speculative-decoding]]"
  - "[[concepts/llm-inference]]"
---

# Prompt Caching (Paged Attention & Automatic Prefix Caching)

Prompt caching（プロンプトキャッシング）は、LLMプロバイダーが同一のプロンプトプレフィックスに対して事前計算されたKVキャッシュを再利用し、冗長な計算をスキップする最適化技術。

## なぜ重要なのか

- **コスト削減**: キャッシュヒット時はprefill計算が不要 → トークンあたりのコストが大幅に低下（Anthropicではキャッシュ書き込みは25%増、読み取りは90%減）
- **レイテンシ低減**: prefillフェーズをスキップ → 初回トークンまでの時間（TTFT）が短縮
- **エージェントのシステムプロンプト最適化**: 長いシステムプロンプト + ツール定義をキャッシュさせることで、エージェントのセッション全体で高速化

## 内部動作

### KVキャッシュの基本

デコーダートランスフォーマーでは、各トークン生成時に過去の全トークンのKey/Valueテンソルを再利用する。これがKVキャッシュ。

```
prefill phase: 全プロンプトトークンを並列処理 → KVキャッシュ生成 (compute-bound)
decode phase:   1トークンずつ自己回帰生成 → KVキャッシュ参照 (memory-bound)
```

### Paged Attention (vLLM)

従来のKVキャッシュ割り当ての問題:
- 各シーケンスに最大長分の連続メモリを事前確保 → **断片化と無駄**
- 可変長シーケンスに非効率

Paged Attentionの解決策（OSの仮想メモリに着想）:
- KVキャッシュを**固定サイズのブロック**に分割
- **ブロックテーブル**で論理→物理ブロックをマッピング
- 必要に応じてブロックを動的割り当て → メモリ無駄ゼロ

```
シーケンス: [tok1, tok2, tok3, tok4, tok5]
ブロック (size=2): [Block A: tok1-2] [Block B: tok3-4] [Block C: tok5]
ブロックテーブル: [A, B, C]
```

### Automatic Prefix Caching (APC)

Paged Attentionのブロック構造を活用:
1. 各ブロックの内容をハッシュ化
2. 新しいリクエストのプレフィックスブロックを既存キャッシュと照合
3. **最長共通プレフィックス（Longest Common Prefix）**までキャッシュヒット
4. 残りのみprefill

```
Request 1: [sys prompt] [user: "translate A"] [assistant: "翻訳A"]
Request 2: [sys prompt] [user: "translate B"]
→ sys prompt部分がキャッシュヒット
```

## 最適化のヒント

1. **静的な部分を前方に**: システムプロンプト、ツール定義、静的コンテキストは常にメッセージ配列の先頭に配置
2. **動的コンテンツを後方に**: ユーザー固有データ、検索結果など変動する部分は末尾に
3. **同じシステムプロンプトを全セッションで共有**: 異なるユーザー間でもキャッシュが共有される
4. **画像/ファイルはキャッシュを破壊**: マルチモーダルコンテンツはプレフィックスに配置しない

## 主要プロバイダーの対応

| プロバイダー | 方式 | 特徴 |
|-------------|------|------|
| Anthropic | 独自実装 | キャッシュ書き込み25%増/読み取り90%減、最小1024トークン |
| OpenAI | 自動キャッシュ | 直近のリクエストと重複するプレフィックスを自動検出、50%割引 |
| DeepSeek | ディスクキャッシュ | KVキャッシュをSSDにオフロード、超長コンテキスト対応 |
| GoogleGemini | コンテキストキャッシュ | 明示的なキャッシュ作成API、TTLベース |

## 参照

- [How prompt caching works — sankalp's blog](https://sankalp.bearblog.dev/how-prompt-caching-works/) (2025-11-30) — Paged Attention + APCの詳細解説
- vLLM論文: [Efficient Memory Management for Large Language Model Serving with PagedAttention](https://arxiv.org/abs/2309.06180) (Kwon et al., 2023)
