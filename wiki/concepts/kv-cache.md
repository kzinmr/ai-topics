---
title: KV Cache — Key-Value Caching in Transformer Inference
created: 2026-04-28
updated: 2026-04-28
type: concept
tags: [architecture, inference, optimization, technique]
sources:
  - raw/articles/crawl-2026-04-28-kv-cache.md
---

# KV Cache: Key-Value Caching in Transformer Inference

KV（Key-Value）Cacheは、TransformerアーキテクチャにおけるLLM推論の効率を劇的に改善する最適化手法。自己回帰生成中の冗長な再計算を排除することで、推論速度を5倍以上向上させる。

## 問題: 自己回帰生成の計算コスト

LLMはトークンを逐次的に生成する（自己回帰）。各ステップで、モデルは全入力シーケンスに対してアテンション計算をやり直すため、計算量が `O(n²)` となる（n = シーケンス長）。

KV Cacheがない場合、3つ目のトークンを生成する際に、1つ目と2つ目のトークンのKey（K）・Value（V）ベクトルを再計算してしまう。

## 解決: KV Cacheによる再計算の排除

各トークンのK・Vベクトルをキャッシュに保存し、新しいトークン生成時には、新しいトークンのK・Vのみを計算してキャッシュに追記する。

- 計算量が `O(n²)` → `O(n)` に削減
- ただしメモリ使用量は線形に増加（トレードオフ）

## 実装の要点

### 1. バッファ登録
```python
self.register_buffer("cache_k", None)
self.register_buffer("cache_v", None)
```

### 2. Forward Passの修正
```python
if use_cache:
    if self.cache_k is None:
        self.cache_k, self.cache_v = keys_new, values_new
    else:
        self.cache_k = torch.cat([self.cache_k, keys_new], dim=1)
        self.cache_v = torch.cat([self.cache_v, values_new], dim=1)
    keys, values = self.cache_k, self.cache_v
```

### 3. 位置追跡（Position Tracking）
キャッシュを使用する場合、`current_pos` を追跡し、新しいクエリの位置がキャッシュ内の既存K/Vと正しく対応するようにする必要がある。

### 4. キャッシュリセット
```python
def reset_cache(self):
    self.cache_k, self.cache_v = None, None
```

## パフォーマンス

124Mパラメータモデル、200トークン生成（Mac Mini M4 CPU）:
- **なし:** ~10.30秒
- **あり:** ~2.11秒
- **結果:** 約 **5倍の高速化**

## 高度な最適化

| 手法 | 効果 |
|------|------|
| **Pre-allocation** | `torch.cat` の代わりに事前確保テンソルでメモリフラグメンテーション防止 |
| **Sliding Window Cache** | 最新Nトークンのみ保持、GPUメモリ枯渇防止 |
| **PagedAttention (vLLM)** | 非連続メモリブロックでキャッシュ管理、メモリ効率最大化 |
| **KV Cache Quantization** | KVキャッシュを低精度で保存、メモリ使用量削減 |

## 重要な注意点

- **訓練 vs 推論:** KV Cacheは推論時のみ使用。訓練時は全トークンを並列処理するため不要。
- **正当性:** 正しいKV Cache実装は非キャッシュモデルと**完全に同一の出力**を生成する。差異がある場合は位置エンコーディングの不整合を示す。
- **メモリ消費:** Llama 3 (131k context) の場合、フルキャッシュで約8GBのVRAMを消費。

## 関連概念

- [[concepts/context-engineering]] — コンテキストウィンドウ最適化のための基盤技術としてのKV Cache
- [[concepts/attention-mechanism-variants]] — GQA, MLA, SWAなどのバリアントとKV Cacheの関係
- [[concepts/token-economics]] — KV Cacheが推論コストに与える影響
- [[concepts/harness-engineering/system-architecture/context-compaction]] — コンテキスト圧縮によるKV Cacheメモリ節約
