# Writing an LLM from scratch, part 32l — Interventions: updated instruction fine-tuning results

- **Source:** Giles Thomas (gilesthomas.com)
- **Date:** 2026-04-21
- **URL:** https://www.gilesthomas.com/2026/04/llm-from-scratch-32l-interventions-instruction-fine-tuning-tests
- **Tags:** [training, instruction-fine-tuning, gpjt, llm-from-scratch]

## Summary

Part 32l of Giles' "LLM from scratch" series. Working on a GPT-2-small-style LLM based on Sebastian Raschka's "Build a Large Language Model (from Scratch)". After achieving test loss close to OpenAI GPT-2-small, he returns to instruction-following tests with a corrected methodology.

Previous IFT test methodology flaw: LLM-as-judge scoring was done in isolation per model, so natural randomness made results incomparable. Fixed by: (1) generating all model responses to a file, then (2) presenting all files together to the judge LLM for consistent relative scoring.

Previous results showed loose correlation between test loss and IFT score, with FineWeb-Edu models as notable exceptions (higher IFT than loss predicted, suggesting knowledge density is separate from raw intelligence).

## Key Excerpts

> "The idea behind this was that the loss on the test set was an interesting technical measure of the quality of a model, but it didn't really tell us much about how useful it might be in reality."

## Related Pages
- [[entities/gpjt]]
- [[concepts/llm-training-coherence-evolution]]
- [[concepts/fine-tuning/axolotl]]
