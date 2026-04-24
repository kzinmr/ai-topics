# How an LLM becomes more coherent as we train it

- **Source:** Giles Thomas (gilesthomas.com)
- **Date:** 2026-04-17
- **URL:** https://www.gilesthomas.com/2026/04/how-an-llm-becomes-more-coherent-over-training
- **Tags:** [training, coherence, llm-training-coherence-evolution, gpjt]

## Summary

Giles Thomas trained a GPT-2-small-style LLM (163M params, 3.2B tokens from FineWeb) and saved 57 checkpoints over two days. He generated completions to "Every effort moves you" at each checkpoint to visualize coherence evolution.

Key observations:
- **Pre-training:** Content-free token salad with no structure (already has words unlike Karpathy's RNNs)
- **Step 617:** Learned most common tokens ("and to was, in the, a, The")
- **Step 1234:** "glimmering of meaning" - grammatical but nonsensical
- **Step 2468:** Actually makes some sense
- **Step 9255 (1/3 trained):** Coherent business/self-help text
- **Step 14191:** Started using bullet points
- **Later steps:** Repetition tics similar to early ChatGPT

Two key exceptions in IFT scores: FineWeb-Edu models got much higher IFT than expected from loss alone, suggesting knowledge density matters separately from raw intelligence.

## Key Excerpts

> "There's a loose correlation where lower loss means a higher IFT score, with two weird exceptions: the two FineWeb-Edu training runs, where they got much higher results than you'd expect from the loss."

## Related Pages
- [[concepts/llm-training-coherence-evolution]]
- [[entities/gpjt]]
- [[concepts/karpathy]]
