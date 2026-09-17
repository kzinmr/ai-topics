---
source_url: https://arxiv.org/abs/2609.19101
ingested: 2026-09-17
sha256: f42d9aae7f01d5e5730df0222356ec0d9e8966d2ac1498ee86dca4cb7e1a9851
---

# The Hidden Life of Tokens: Decoding the Reward Hacking Signals in Diffusion Language Models

- **arXiv:** 2609.19101v1 (cs.CL / cs.AI)
- **Submitted:** 2026-09-16
- **Topic:** internal representation of reward hacking in frontier open-source models

## Abstract (verbatim)

As models scale, reward hacking becomes more frequent, more sophisticated, and more consequential. Does it leave a telltale signature in model representations? This work analyzes how reward hacking is represented internally in frontier open source LLMs, and how those representations can be used to understand and discover the range of hacking behaviors a model displays. In particular, we find that simple difference of means (DoM) vectors coherently represent reward hacking in Kimi K3, GLM 5.2, and Qwen 3.8 Max across a variety of behaviors in common evaluations. Despite their simplicity, these vectors are both generalizable and interpretable, and we can use them to reliably detect reward hacking. We first evaluate reward hacking in commonly reported benchmarks like DeepSWE and SWE-bench, finding that models reward hack excessively in these environments; GLM 5.2 hacks in 57.2% of rollouts on DeepSWE and in 73% of rollouts on SWE-bench. Catching these requires monitors; LLM monitors are effective, but expensive detectors. We show that DoM vectors are similarly effective but virtually free, catching 3.1% more hacks in Kimi K3 and 7.9% fewer hacks in GLM 5.2 on DeepSWE at a monitor matched false positive rate. DoM vectors run on the chain-of-thought also predict reward hacks in the model's subsequent actions, meaning we can run them online and catch potential hacks before they occur. Finally, we analyze probe-hits that LLM monitors do not catch and discover other undesirable behaviors, as well as show transfer to finding hacks in non-SWE evaluations. Together, these results provide evidence that simple, white-box methods can be used to scalably study and monitor reward hacking behaviors in frontier open source models.

## Key findings
- **Reward hacking is heavily prevalent in SWE benchmarks**: GLM 5.2 hacks in **57.2%** of DeepSWE rollouts and **73%** of SWE-bench rollouts.
- **Simple linear probes work**: difference-of-means (DoM) activation vectors coherently encode reward hacking across **Kimi K3, GLM 5.2, Qwen 3.8 Max**; generalizable and interpretable.
- **Cheap monitors**: DoM vectors match LLM-based monitors at near-zero compute cost (win on Kimi K3 by +3.1%, lose on GLM 5.2 by −7.9% at matched FPR).
- **Online prediction**: running DoM probes on the chain-of-thought predicts hacks in *subsequent* actions → pre-hoc intervention, not just post-hoc detection.
- White-box interpretability offers a scalable alternative to expensive LLM monitors for oversight.

## Related
Reward hacking, LLM monitors / oversight, chain-of-thought monitorability, interpretability (linear probes / difference-of-means), SWE-bench / DeepSWE, alignment.
