---
source_url: https://arxiv.org/abs/2610.01415
ingested: 2026-10-02
sha256: 23e40bf778c134e39a8ef82adb31b6b75f74b174e26849201157b5d5526b5a7c
---

# Beyond Memory: Harnessing Long-Horizon Agents with Explicit Belief States

arXiv: 2610.01415 (submitted 2026-10-01)

**Authors:** Yu Luo, Jiamin Jiang, Yimin Zuo, Xidao Wen, Rongchen Gao, Yongqian Sun, Shenglin Zhang, Guiyang Liu, Cheng Zhang, Fang Situ, Qi Zhou, Dan Pei

## Abstract

Large language model (LLM) agents can now undertake increasingly complex tasks, but the way they organize interaction history into memory does not ensure a coherent understanding of the current world. We introduce PoS, an inference-time framework that constructs and continually maintains explicit belief states as the agent's decision context. Each belief combines an estimate of the current world state with unresolved task requirements, making explicit what the agent still needs to learn and accomplish. To keep this belief reliable and actionable, PoS validates its consistency and monitors task progress to detect Belief Trapping, where the agent continues to act without making meaningful progress toward the goal. Recovery is then tailored to both the trapping pattern and the type of unresolved task requirement. Experiments on four benchmarks spanning execution and diagnosis show that PoS achieves the highest overall performance on every benchmark with all three LLM backbones. Ablations demonstrate the importance of consistency validation and recovery, while context-scaling experiments show resilience to context growth. Together, these results support belief construction and continual maintenance as a foundation for long-horizon context management beyond history retention and compression.
