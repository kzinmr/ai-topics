---
title: "PyTorch GPU Memory Profiling — Snapshot & Profiler Tools"
type: concept
created: 2026-05-02
updated: 2026-05-02
tags:
  - concept
  - pytorch
  - gpu-memory
  - profiling
  - debugging
  - oom
  - vram
  - infrastructure
status: L1
aliases:
  - pytorch-gpu-memory-profiling
  - pytorch-memory-snapshot
  - pytorch-memory-profiler
  - cuda-oom-debugging
sources:
  - "https://pytorch.org/blog/understanding-gpu-memory-1/"
related:
  - "[[concepts/ai-infrastructure-engineering/gpu-vram-fundamentals]]"
  - "[[concepts/ai-infrastructure-engineering/_index]]"
  - "[[concepts/ai-infrastructure-engineering/llm-observability]]"
  - "[[concepts/llm-inference]]"
  - "[[concepts/kv-cache]]"
---

# PyTorch GPU Memory Profiling

> PyTorch v2.1以降で利用可能な2つのGPUメモリデバッグツール — **Memory Snapshot**（全アロケーションの時系列可視化）と**Memory Profiler**（カテゴリ別メモリ使用量分析）— の使い方と実践的OOMデバッグ手法。

## Why This Matters

GPUメモリ不足（`torch.cuda.OutOfMemoryError`）はLLM訓練・推論における最も頻発する障害。**どのテンソルが、なぜ、いつメモリを確保しているのか**を可視化できないと、原因特定に膨大な試行錯誤が必要になる。PyTorchのビルトインツールを使えば、スタックトレースレベルで原因を特定できる。

## 1. Memory Snapshot Tool（メモリスナップショット）

最も粒度の細かいGPUメモリデバッグ手法。全アロケーション・解放イベントを時系列で記録し、インタラクティブな可視化を提供する。

### 特徴
- **Visual Patterns**: forward passでメモリ上昇、backward passで解放されるパターンを視認できる
- **Stack Traces**: 各アロケーションをクリックすると、その確保を引き起こしたコード行が表示される
- **Granularity**: 一時的な小さなバッファ（tiny spikes）から永続テンソルまで識別可能

### API Usage

```python
# 1. 記録開始（最大100,000イベントのバッファ）
torch.cuda.memory._record_memory_history(max_entries=100000)

# --- 監視したいコードを実行 ---

# 2. スナップショットをpickleに保存
torch.cuda.memory._dump_snapshot("snapshot.pickle")

# 3. 記録停止
torch.cuda.memory._record_memory_history(enabled=None)
```

### 可視化
- **Web Tool**: `.pickle`ファイルを [pytorch.org/memory_viz](https://pytorch.org/memory_viz) にドラッグ＆ドロップ
- **Local HTML変換**:
  `python torch/cuda/_memory_viz.py trace_plot snapshot.pickle -o snapshot.html`

## 2. CUDA OOMデバッグ — 実例ケーススタディ

### The Bug: イテレーション間でメモリが増加し続ける「階段パターン」

勾配テンソルが解放されず、各イテレーションでメモリ使用量が右肩上がりになる。

```
Memory
  ^
  |     ██
  |   ████
  | ██████
  |████████
  +---------> Time (iterations)
```

**The Fix: `optimizer.zero_grad(set_to_none=True)` を忘れずに呼ぶ**

```python
for _ in range(num_iters):
    pred = model(inputs)
    loss_fn(pred, labels).backward()
    optimizer.step()
    # 重要: 勾配テンソルを解放
    optimizer.zero_grad(set_to_none=True)  # set_to_none=Trueがより効率的
```

`set_to_none=True` は値を0にするのではなくテンソルそのものを削除するため、より効率的でメモリ断片化も防ぐ。

## 3. Memory Profiler（メモリプロファイラ）

スナップショットが「どのコード行が」を教えるのに対し、プロファイラは「どのカテゴリ（勾配、最適化状態、活性化値）」にメモリが使われているかを**分類**する。

### 主な知見
- **Optimizer State**: 1イテレーション目以降の永続的なメモリ増加（黄色で表示）
- **Gradients**: 青色で表示。イテレーション間で解放されるべき
- **Activations**: Forward中に増加、backward後に解放

### 実装

```python
import torch.profiler
from torch.profiler import ProfilerActivity, record_function

with torch.profiler.profile(
    activities=[ProfilerActivity.CPU, ProfilerActivity.CUDA],
    schedule=torch.profiler.schedule(wait=0, warmup=0, active=6, repeat=1),
    profile_memory=True,
    with_stack=True,
    on_trace_ready=trace_handler,  # カスタム保存関数
) as prof:
    for _ in range(5):
        prof.step()
        with record_function("## forward ##"):
            pred = model(inputs)
        with record_function("## backward ##"):
            loss_fn(pred, labels).backward()
        with record_function("## optimizer ##"):
            optimizer.step()
            optimizer.zero_grad(set_to_none=True)

# メモリタイムラインをHTML出力
prof.export_memory_timeline("timeline.html", device="cuda:0")
```

### `record_function` によるセクションラベリング

`with record_function("## label ##")` でコードブロックに名前を付け、タイムライン上のメモリ使用量がどのフェーズに属するか一目でわかるようにする。`##` プレフィックスはツリービューでのグルーピングに利用される。

## ツール比較

| ツール | 最適用途 | 主要出力 |
|--------|----------|----------|
| **Memory Snapshot** | OOMデバッグ、特定テンソルのリーク特定 | 全アロケーションのスタックトレース |
| **Memory Profiler** | 高レベルなメモリ分布の理解 | カテゴリ別使用量（Optimizer vs Gradients） |

## 関連リンク

- [連載第1回: Understanding GPU Memory 1 (本記事)](https://pytorch.org/blog/understanding-gpu-memory-1/)
- [Interactive Demo: Snapshot Visualization](https://github.com/pytorch/pytorch.github.io/blob/site/assets/images/understanding-gpu-memory-1/snapshot.html)
- [PyTorch Memory Docs](https://pytorch.org/docs/main/torch_cuda_memory.html)
- [Profiler Docs](https://pytorch.org/docs/main/profiler.html)
- [memory_viz.py](https://github.com/pytorch/pytorch/blob/main/torch/cuda/_memory_viz.py)

## Related Pages

- [[concepts/ai-infrastructure-engineering/gpu-vram-fundamentals]] — GPUメモリ階層の基礎
- [[concepts/ai-infrastructure-engineering/llm-observability]] — LLM観測可能性（TTFT, TPOT等）
- [[concepts/llm-inference]] — Roofline分析、バッチ経済学
- [[concepts/kv-cache]] — VRAMの主要消費源
- [[concepts/ai-infrastructure-engineering/_index]] — Parent page
