---
title: "Production-Ready Agent Engineering — Bonus Lesson: GRPO Details"
author: Will Brown
date: 2025-07-03
date_ingested: 2026-06-11
source: https://maven.com/will-brown-kyle-corbitt/agents-mcp-rl
type: article
tags:
  - reinforcement-learning
  - grpo
  - ppo
  - agentic-rl
  - ai-agents
  - vllm
  - lora
  - fine-tuning
  - gpu
  - vram
  - ml-infrastructure
  - async-rl
  - off-policy
  - education
---

# Production-Ready Agent Engineering — Bonus Lesson: GRPO Details

**Lecture transcript:** [[transcripts/2025-07-03_willbrown_agents-mcp-rl-lesson5-5-lecture]]
**Companion course:** [[concepts/agents-mcp-rl-course|Production-Ready Agent Engineering: From MCP to RL]]
**Notebook:** [grpo_details.ipynb](https://raw.githubusercontent.com/willccbb/agent-engineering/refs/heads/main/lectures-1-through-4/lec5-grpo-details/grpo_details.ipynb)
**Instructor:** Will Brown ([[entities/prime-intellect]])

---

## Summary

Bonus lecture surveying GRPO implementation details and the RL infrastructure ecosystem. Less code walkthrough, more strategic overview of the architectural decisions, gotchas, and optimization techniques critical for practical GRPO training. Covers the full stack from VRAM math through GPU orchestration patterns to frontier research directions like VinePPO, test-time training, and RL for non-verifiable domains.

## Key Topics

### RL Infrastructure Ecosystem

- **Ray** (Anyscale): Distributed orchestration layer for multi-machine RL, popular even pre-LLM with OpenAI Gym and Stable Baselines
- **Verl** (formerly OpenRLHF): Default research-paper framework for scalable RL (32+ GPUs), overkill for small scales but standard for PhD/large lab work
- **ART** (OpenPipe): Single-GPU swapping approach — inference and training modes share the same GPUs, hot-swapping weights via vLLM API
- **Verifiers** (Prime Intellect): Overlapping approach — designated inference/training GPUs with cascade scheduling, 1-step async by default
- **Unsloth**: Single-GPU optimization (4090-class hardware), handles fp8/bit-level optimizations, works with ART

### VRAM Napkin Math (7B Model)

| Component | Size |
|-----------|------|
| Model weights (bfloat16) | 14 GB |
| AdamW optimizer (fp32, 2 momentum vectors) | 56 GB |
| Gradients (fp32) | 28 GB |
| Activations | 14+ GB |
| **Rule of thumb** | **~10× model size** |

### PPO vs GRPO

- **PPO**: Actor + Critic model — critic is a full copy trained to estimate per-token advantage; 10× memory footprint
- **GRPO**: Actor only — group sampling replaces critic; advantage = reward normalized within group (mean 0, std 1)
- GRPO is a simplified approximation of PPO; democratized RL by enabling experimentation at smaller scales
- PPO is not dead — credit assignment via token-level critic estimation is still valuable for complex tasks

### GPU Architecture Patterns

- **Pattern A (Swapping/ART):** Same GPUs alternate between inference and training modes; optimizer state can stay in memory or be written to disk (especially with LoRA)
- **Pattern B (Overlapping/Verifiers):** Designated inference + training GPUs run in cascade; training on old batches while inferring next batches; 1-step async by default
- **vLLM hot-swap:** First-class API for swapping LoRA adapters without full weight replacement
- **LoRA advantage:** LoRA adapters are tiny — can be written to disk and reapplied, avoiding GPU-to-GPU weight transfer

### Key GRPO Gotchas

1. **Beta = 0 with LoRA is safe:** LoRA already constrains model drift; reference model not needed for short/medium runs
2. **Temperature 1 mandatory:** Lower temperatures cause mathematical issues in advantage computation
3. **Caching must be off for training:** Multiple rollouts on same model must be independent
4. **Reward std dev collapse:** If it drops to 0, model is output-saturated and stops learning
5. **Off-policy delay:** 1-step async is fine; whether 10+ steps works is task-dependent and open question
6. **bfloat16, not fp8:** fp8 tooling ecosystem is still early; bfloat16 is the safe default

### Frontier Research Directions

- **VinePPO:** Explicit tree search for rollouts — sample, branch, compare, estimate intermediate advantages for better credit assignment
- **REINFORCE batch approach:** Throw all states/rewards into a big batch without explicit grouping; simpler multi-turn training if it scales
- **Think token removal:** Multi-turn training where thinking tokens are stripped between turns to control context length; requires algorithm modification
- **Test-time training:** Generate synthetic Q&A from inputs, train a LoRA at inference time (~few minutes for few hundred examples); deeper than in-context learning ("skimming")
- **LM-as-judge tournaments:** Elo-style pairwise comparisons for non-verifiable domains; DeepSeek inference-time scaling paper + Qwen creative writing application
- **RL for non-verifiable domains:** Core question is "can you evaluate it?"; if evaluation is consistent with human judgment, RL works reliably

## Key Insights

1. **10× rule for VRAM:** Model training requires ~10× the model parameter size in GPU memory
2. **Start small, debug cheap:** 2× L4 or A10 at <$1/hour; iterate on 1B models before scaling up
3. **LoRA is not just memory-saving — it's stability insurance:** Constrains drift, enables safe beta=0, allows disk-based weight management
4. **Async is a feature, not a bug:** 1-step off-policy enables GPU overlap without meaningful quality loss
5. **In-context learning is skimming:** Training creates deeper representations than retrieval-augmented prompting
6. **Be skeptical of RL-as-a-service:** Know GPU market rates (H100: $1-2/hr, H200: ~$3/hr); many services are thin wrappers around TRL

## Companion Resources

- [grpo_details.ipynb](https://raw.githubusercontent.com/willccbb/agent-engineering/refs/heads/main/lectures-1-through-4/lec5-grpo-details/grpo_details.ipynb) — Notebook (topics listed but code not filled in — "see recording for more")
- [Anyscale RL ecosystem blog](https://www.anyscale.com/blog/open-source-rl-libraries-for-llms) — Infrastructure landscape survey
- [Nathan Lambert — Interconnects](https://www.interconnects.ai/) — Weekly RL/AI digest + RLHF book
- [Semi Analysis — Scaling RL](https://newsletter.semianalysis.com/p/scaling-reinforcement-learning-environments-reward-hacking-agents-scaling-data) — Dylan Patel's big-lab RL strategies report

## Related

- [[concepts/agents-mcp-rl-course|Production-Ready Agent Engineering: From MCP to RL]]
- [[transcripts/2025-07-03_willbrown_agents-mcp-rl-lesson5-5-lecture]]
- [[concepts/grpo-rl-training]]
- [[concepts/agentic-rl]]
- [[entities/will-brown]]
- [[entities/prime-intellect]]
- [[raw/articles/2025-07-02_kylecorbitt_agents-mcp-rl-lesson5]]
- [[raw/articles/2024-12-30_corbt_openai-reinforcement-fine-tuning]]
