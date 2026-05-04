---
title: "GPT in 60 Lines of NumPy (picoGPT)"
author: "Jay Mody"
url: "https://jaykmody.com/blog/gpt-from-scratch/"
date: 2023-01-30
tags:
  - gpt
  - transformer
  - from-scratch
  - educational
---

# GPT in 60 Lines of NumPy

A ground-up implementation of GPT-2 using only Python and NumPy.

## Architecture
Three sections: Embeddings, Transformer Decoder Stack, Projection to Vocab.

### Key Code:
```
def gpt2(inputs, wte, wpe, blocks, ln_f, n_head):
    x = wte[inputs] + wpe[range(len(inputs))]
    for block in blocks:
        x = transformer_block(x, **block, n_head=n_head)
    x = layer_norm(x, **ln_f)
    return x @ wte.T
```

### Three Pillars:
1. **Embeddings** — Token + Positional
2. **Decoder Blocks** — Pre-norm, Residual Connections
3. **Projection** — Reuses wte weights (tied embeddings)

### Transformer Block:
- Multi-Head Causal Self-Attention
- Position-wise Feed Forward Network (2-layer MLP, 4x hidden dim)

### Causal Mask:
`(1 - np.tri(n_seq)) * -1e10`

### GPT-2 124M Hyperparams:
| Param | Value |
|-------|-------|
| n_vocab | 50,257 |
| n_ctx | 1,024 |
| n_embd | 768 |
| n_head | 12 |
| n_layer | 12 |

### Next Steps:
- GPU: swap NumPy for JAX
- Inference: KV Cache
- Fine-tuning: classification head, PEFT (Adapters/LoRA)
