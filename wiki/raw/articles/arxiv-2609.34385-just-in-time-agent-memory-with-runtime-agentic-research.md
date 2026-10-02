---
source_url: https://arxiv.org/abs/2609.34385
ingested: 2026-09-30
sha256: 68c716ebdf6c547640c3ba5f371f3b2b16204b466b566da22a65274062859dde
---

# Just-In-Time Agent Memory with Runtime Agentic Research

**arXiv:** 2609.34385v1  
**Published:** 2026-09-28  
**Primary category:** cs.CL  
**Authors:** Bingyu Yan, Chaofan Li, Hongjin Qian, Shuqi Lu, Chaozhuo Li, Zheng Liu

## Abstract

Memory is critical for AI agents. Many existing agent-memory systems follow an Ahead-of-Time (AOT) design, constructing memory before a specific request arrives. While this reduces online serving cost, such request-agnostic memory construction can discard fine-grained information that later becomes important. To address this limitation, we propose Just-In-Time Agent Memory (JAM), a trainable framework for query-conditioned context construction at runtime. A Memorizer preserves complete raw histories in a hierarchical page-store with compact navigational summaries, while a Researcher iteratively retrieves, inspects, and integrates evidence for each request. To train these memory-use behaviors, we introduce Memory-Gym, an evidence-grounded data synthesis pipeline covering nine task types across six domains, and optimize the Researcher through verified-trajectory supervised fine-tuning followed by Hint-guided Group Relative Policy Optimization. We demonstrate the effectiveness of JAM across a variety of benchmarks on agent memory and long-context processing, where it achieves stronger task performance than AOT-style memory systems while remaining substantially more efficient than prior trained agentic memory approaches. To support reproducibility and future research, we release our anonymized source code at https://github.com/VectorSpaceLab/general-agentic-memory.
