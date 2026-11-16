---
title: "NVIDIA serves GLM-5.3 at 607.8 tok/s across two DGX stations with vLLM"
source: https://developer.nvidia.com/blog/when-one-gpu-isnt-enough-serving-glm-5-3-across-two-nvidia-dgx-stations-with-vllm/
collected: 2026-11-16
hn_item: https://news.ycombinator.com/item?id=50497155
sha256: ae04391d33887012342bf179104acccbd0c76a9d79396c28c7850036bace1d5c
---

# Serving GLM-5.3 at 607.8 tok/s across two Nvidia DGX stations with vLLM

NVIDIA Developer Blog, 2026-11-14 (HN 147 pts / 70 comments,
https://news.ycombinator.com/item?id=50497155). NVIDIA benchmarked **GLM-5.3** served across **two
NVIDIA DGX stations** using **vLLM**, reporting aggregate system throughput **peaking at 607.8
tokens/s** on SPEED-Bench Coding with prefix caching enabled, alongside mean per-user throughput as
concurrency rises.

## HN discussion highlights (item 50497155)

- [boodleboodle] "Whats the best model i should be runnning with two dgxs? Is there a reason they chose
  glm and not deepseek"
- [gpugreg] "GLM-5.3's architecture (same as GLM-5.2) is simpler and it came out earlier. Hybrid
  attention and Manifold-Constrained Hyper-Connections only arrived with GLM-5.3-Flash. Also, NVIDIA
  acquired HuggingFace, who used GLM-5.2 for their forensic analysis when they got hacked, so I presume
  that they have more familiarity with that model. And DeepSeek-V4.1-Flash is more memory-efficient, so
  it'd sell fewer GPUs."
- [frogblast] "DeepSeek's claim to fame is massively shrinking the per-user memory footprint, enabling
  many more concurrent users in your fixed hardware footprint. Having more concurrent users leads to
  much higher overall throughput on that same hardware. That's why DS is so cheap to host."
- [mapontosevenths] "Having used both, they really are comparable for most things, which leaves the
  cheaper Deepseek a better choice for most folks. The one area that I've found GLM to be a clear winner
  is in offensive Cyber. If you run a red team GLM is hard to beat."
- [meatmanek] "Deepseek-v4.1-Flash [...] spends 20 minutes thinking about relatively basic prompts, so
  even if it's cheaper that GLM, the time saved by GLM-5.3's much more reasonable thinking time/tokens
  means you end up ahead if you value your own time."
