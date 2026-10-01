---
source_url: https://arxiv.org/abs/2609.39819
arxiv_id: 2609.39819
ingested: 2026-10-01
sha256: cab2e56da7f1085411e237bc964ec3109f094398bd5acf8c628b6e8565258e34
---

# Capture the lifecycle: KV Cache management in ReAct Agents with KVTether

arXiv:2609.39819v1 (cs.OS), submitted 2026-09-30.
Authors: Kaihua Fu, Yukun Zhou, Chaokun Chang, Yinghao Yu, Luping Wang, Guodong Yang, Jiuchen Shi, Quan Chen, Wei Wang.

## Abstract

Efficient serving of long-context reasoning-and-acting (ReAct) agents relies on KV cache reuse to reduce large language model (LLM) prefill latency and monetary cost. However, a semantic gap exists between agent harnesses and the underlying serving stack. Through context mutation, tool execution, and subagent coordination, context messages may become actively engaged, permanently discarded, and temporarily unused, while the serving stack only observes accesses to the corresponding KV cache. This lifecycle blindness prevents recency-only policies such as LRU from reclaiming dead KV promptly and from preserving older KV that will be reused sooner than newer entries.

We present KVTether, a lifecycle-aware KV cache management framework for ReAct agents. By tracing semantic primitives embedded in agent harnesses, KVTether captures runtime lifecycle semantics during highly dynamic execution. KVTether then translates message-level semantics into KV-level lifecycle states and uses these states to drive state-prioritized cache management without exposing physical complexities to agent harnesses. After reclaiming dead KV, KVTether preferentially preserves live-but-idle KV that is waiting for reuse, reducing premature eviction before reuse.

Across agent benchmarks and production workloads, KVTether reduces end-to-end request latency by up to 26.3% and 17.4% relative to LMCache and MORI, respectively, and lowers estimated task cost by 40.0% and 33.2% on average.
