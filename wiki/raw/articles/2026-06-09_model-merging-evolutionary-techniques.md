---
date: 2026-06-09
source: synthesized
source_urls:
  - https://huggingface.co/blog/mlabonne/merge-models (community guide)
  - https://sakana.ai/ (Sakana AI evolutionary model merging)
type: research_note
status: synthesized
tags: [model-merging, evolutionary-algorithms, sakana-ai, open-source, foundation-models]
---

# AI Model Merging & Evolutionary Techniques — Research Note

Synthesized research note on model merging techniques that have become a significant trend in open-source AI.

## Background

Model merging allows combining multiple fine-tuned models into a single model without additional training, creating new capabilities from existing weights. Over 1,000 merged models exist on Hugging Face.

## Key Techniques

### Weighted Averaging (Linear)
- **SLERP** (Spherical Linear Interpolation): Smooth interpolation in weight space
- **TIES-Merging**: Trim, Elect Sign, and Merge — resolves parameter interference

### Evolutionary Merging (Sakana AI)
- [[entities/sakana-ai|Sakana AI]] ($2.65B valuation) pioneered evolutionary model merging
- Uses genetic algorithms to discover optimal merge configurations
- **mergekit** library: Popular open-source tool for implementing merges

### Advanced Methods
- **DARE** (Drop And REscale): Prunes redundant delta parameters before merging
- **MixLoRA**: Merging LoRA adapters across different fine-tuned models
- **Model Stock**: Averaging multiple fine-tuned checkpoints

## Applications

- **Cross-domain expertise**: Merge an instruction-tuned model with a code model
- **Language mixing**: Combine English and multilingual models
- **Safety alignment**: Merge a capable model with a safety-tuned model
- **Community experimentation**: Hugging Face's 1,000+ merged models

## See Also

- [[entities/sakana-ai|Sakana AI]]
- [[entities/maxime-labonne|Maxime Labonne]] — mergekit creator
- [[concepts/fine-tuning|Fine-Tuning]]
- [[concepts/lora|LoRA]]
