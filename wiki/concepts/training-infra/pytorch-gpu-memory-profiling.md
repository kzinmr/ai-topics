---
title: "PyTorch GPU Memory Profiling — Snapshot & Profiler Tools"
type: concept
created: 2026-05-02
updated: 2026-05-02
tags:
  - concept
  - pytorch
  - hardware
  - developer-tooling
  - infrastructure
status: L1
aliases:
  - pytorch-gpu-memory-profiling
  - pytorch-memory-snapshot
  - pytorch-memory-profiler
  - cuda-oom-debugging
  - pytorch-fake-tensor
  - memory-tracking-mode
  - fake-tensor-mode
sources:
  - "https://pytorch.org/blog/understanding-gpu-memory-1/"
  - "https://dev-discuss.pytorch.org/t/how-to-measure-memory-usage-from-your-model-without-running-it/"
related:
  - "[[concepts/training-infra/gpu-vram-fundamentals]]"
  - "[[concepts/training-infra/_index]]"
  - "[[concepts/training-infra/llm-observability]]"
  - "[[concepts/llm-inference]]"
  - "[[concepts/kv-cache]]"
---

# PyTorch GPU Memory Profiling

> Two GPU memory debugging tools available since PyTorch v2.1 — **Memory Snapshot** (time-series visualization of all allocations) and **Memory Profiler** (category-based memory usage analysis) — usage guide and practical OOM debugging techniques.

## Why This Matters

GPU out-of-memory errors (`torch.cuda.OutOfMemoryError`) are the most frequent failure mode in LLM training and inference. Without the ability to visualize **which tensors are allocating memory, why, and when**, root cause identification requires extensive trial and error. PyTorch's built-in tools enable stack-trace-level root cause identification.

## 1. Memory Snapshot Tool

The most granular GPU memory debugging approach. Records all allocation and deallocation events in a timeline, providing interactive visualization.

### Features
- **Visual Patterns**: See memory rising during forward pass and being freed during backward pass
- **Stack Traces**: Click each allocation to see the code line that triggered it
- **Granularity**: Distinguishes temporary small buffers (tiny spikes) from persistent tensors

### API Usage

```python
# 1. Start recording (buffer up to 100,000 events)
torch.cuda.memory._record_memory_history(max_entries=100000)

# --- Run the code you want to monitor ---

# 2. Save snapshot to pickle
torch.cuda.memory._dump_snapshot("snapshot.pickle")

# 3. Stop recording
torch.cuda.memory._record_memory_history(enabled=None)
```

### Visualization
- **Web Tool**: Drag-and-drop `.pickle` files onto [pytorch.org/memory_viz](https://pytorch.org/memory_viz)
- **Local HTML Conversion**:
  `python torch/cuda/_memory_viz.py trace_plot snapshot.pickle -o snapshot.html`

## 2. CUDA OOM Debugging — A Real-World Case Study

### The Bug: "Staircase Pattern" — Memory Keeps Growing Between Iterations

Gradient tensors are not freed, causing memory usage to rise monotonically with each iteration.

```
Memory
  ^
  |     ██
  |   ████
  | ██████
  |████████
  +---------> Time (iterations)
```

**The Fix: Don't forget to call `optimizer.zero_grad(set_to_none=True)`**

```python
for _ in range(num_iters):
    pred = model(inputs)
    loss_fn(pred, labels).backward()
    optimizer.step()
    # Important: free gradient tensors
    optimizer.zero_grad(set_to_none=True)  # set_to_none=True is more efficient
```

`set_to_none=True` removes the tensor itself rather than zeroing its values, making it more efficient and preventing memory fragmentation.

## 3. Memory Profiler

While the snapshot tells you "which code line" allocated memory, the profiler **categorizes** memory by usage category (gradients, optimizer states, activations).

### Key Insights
- **Optimizer State**: Persistent memory increase after the first iteration (shown in yellow)
- **Gradients**: Shown in blue. Should be freed between iterations
- **Activations**: Increase during forward pass, freed after backward pass

### Implementation

```python
import torch.profiler
from torch.profiler import ProfilerActivity, record_function

with torch.profiler.profile(
    activities=[ProfilerActivity.CPU, ProfilerActivity.CUDA],
    schedule=torch.profiler.schedule(wait=0, warmup=0, active=6, repeat=1),
    profile_memory=True,
    with_stack=True,
    on_trace_ready=trace_handler,  # Custom save function
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

# Export memory timeline to HTML
prof.export_memory_timeline("timeline.html", device="cuda:0")
```

### Section Labeling with `record_function`

`with record_function("## label ##")` names code blocks so you can instantly see which phase a memory allocation belongs to on the timeline. The `##` prefix is used for grouping in tree view.

## 4. Measuring Memory Without Running the Model — FakeTensorMode + MemoryTrackingMode

Estimate how much VRAM a model consumes **without executing code**, even without a physical GPU. A ~30-line implementation contributed by Alban Desmaison (albanD).

### How It Works

- **`FakeTensorMode`**: A context that only holds tensor metadata (shape, dtype, device) without actual data allocation
- **`MemoryTrackingMode`**: Inherits `TorchDispatchMode`, hooks all tensor creation via `__torch_dispatch__` to aggregate memory usage
- **`WeakIdKeyDictionary`**: Maintains weak references to tensor storage, automatically removes tensors freed by GC from tracking

### Implementation Code

```python
import math
import weakref
from torch.utils.weak import WeakIdKeyDictionary
from torch.utils._python_dispatch import TorchDispatchMode
from torch.utils._pytree import tree_map_only

MEMORY_USE = WeakIdKeyDictionary()
MEMORY_MAX = 0
PYTORCH_MIN_ALLOCATE = 2 ** 9  # Minimum alignment size (512 bytes)

def update_stats():
    global MEMORY_MAX
    curr_use = 0
    for k, v in MEMORY_USE.items():
        # Account for PyTorch allocator minimum alignment
        aligned = math.ceil(k.size() * k.element_size() / PYTORCH_MIN_ALLOCATE)
        curr_use += aligned * PYTORCH_MIN_ALLOCATE
    if MEMORY_MAX < curr_use:
        MEMORY_MAX = curr_use

def track(t: torch.Tensor):
    def cb(_):
        update_stats()
    st = t.untyped_storage()
    wt = weakref.ref(st, cb)
    MEMORY_USE[st] = wt
    update_stats()

class MemoryTrackingMode(TorchDispatchMode):
    def __torch_dispatch__(self, func, types, args, kwargs=None):
        res = func(*args, **kwargs or {})
        tree_map_only(torch.Tensor, track, res)
        return res
```

### Usage Example

```python
with FakeTensorMode(), MemoryTrackingMode():
    def f(a):
        b = a * 10
        d = b + 3
        return d

    a = torch.rand(100, device="cuda")
    f(a)
    print(f"Max Memory: {MEMORY_MAX}")  # The actual allocated memory amount
```

**Important**: `FakeTensorMode()` and `MemoryTrackingMode()` must be used **together** in the same `with` block. FakeTensorMode suppresses actual allocation while MemoryTrackingMode computes the memory amount from shape information.

### Module-Level Memory Tracking (In Development)

- **PR [#124688](https://github.com/pytorch/pytorch/pull/124688)**: Feature to aggregate memory usage at the module level. Shares a common base class design with `FlopCounterMode`
- **Implementation Approach**: Uses `all-module hooks` to provide a simple API where users don't need to manually pass modules

### Reserved Memory vs Allocated Memory

Simple tensor tracking only measures **allocated memory** (memory actually used by tensors). On real GPUs, the difference from **reserved memory** (pre-allocated by the cache allocator) is crucial:

| Type | Description | Measurement Method |
|------|------|----------|
| **Allocated Memory** | Memory actually used by tensors | Measurable via MemoryTrackingMode |
| **Reserved Memory** | Memory pre-allocated from GPU by CUDA cache allocator | `reserved_bytes.all.current` from `torch.cuda.memory_stats()` |
| **Fragmentation** | Reserved but unused fragmented memory | Reserved - Allocated |

**NCCL Special Case**: Distributed training libraries (Megatron-LM, etc.) sometimes allocate NCCL buffers directly through the cache allocator, which may not be recognized as `torch.Tensor` and can thus leak from MemoryTrackingMode measurements.

### Future Roadmap

The PyTorch team is planning a major refactoring of the device cache allocator:
1. **Custom Allocators**: Make `malloc`/`free` functions swappable even from Python
2. **Device Independence**: Use Generic Stream/Event/Sync API to handle non-CUDA devices with the same allocator
3. **Feature Cleanup**: Make `cudaGraph` pools and expandable segments optional

### Key Contributors
- **albanD** (Alban Desmaison): Initial implementation, design guidance
- **rawwds**: Module-wise tracking integration
- **guangyey**: Cache allocator refactoring
- **matthewygf**: Distributed training (Megatron-LM) memory tracking inconsistency investigation

## Tool Comparison

| Tool | Best Use Case | Primary Output |
|--------|----------|----------|
| **Memory Snapshot** | OOM debugging, identifying specific tensor leaks | Stack traces for all allocations |
| **Memory Profiler** | Understanding high-level memory distribution | Category-based usage (Optimizer vs Gradients) |

## Related Links

- [Understanding GPU Memory 1](https://pytorch.org/blog/understanding-gpu-memory-1/)
- [How to measure memory usage without running your model (PyTorch Dev Discuss)](https://dev-discuss.pytorch.org/t/how-to-measure-memory-usage-from-your-model-without-running-it/)
- [Interactive Demo: Snapshot Visualization](https://github.com/pytorch/pytorch.github.io/blob/site/assets/images/understanding-gpu-memory-1/snapshot.html)
- [PyTorch Memory Docs](https://pytorch.org/docs/main/torch_cuda_memory.html)
- [Profiler Docs](https://pytorch.org/docs/main/profiler.html)
- [memory_viz.py](https://github.com/pytorch/pytorch/blob/main/torch/cuda/_memory_viz.py)
- [PR #124688 - Module-wise Memory Tracker](https://github.com/pytorch/pytorch/pull/124688)

## Related Pages

- [[concepts/training-infra/gpu-vram-fundamentals]] — GPU memory hierarchy fundamentals
- [[concepts/training-infra/llm-observability]] — LLM observability (TTFT, TPOT, etc.)
- [[concepts/llm-inference]] — Roofline analysis, batch economics
- [[concepts/kv-cache]] — Primary VRAM consumer
- [[concepts/training-infra/_index]] — Parent page
