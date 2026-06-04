# A Unified Model and Document Representation for On-Device Retrieval-Augmented Generation

**Source**: https://arxiv.org/abs/2604.14403
**Authors**: Julian Killingback (UMass Amherst), Ofer Meshi (Google), Henry Li (Google), Hamed Zamani (UMass Amherst), Maryam Karimzadehgan (Google)
**Date**: 2026-04-15
**Type**: Research Paper (Preprint)

## Abstract

Traditional Retrieval-Augmented Generation (RAG) approaches generally assume that retrieval and generation occur on powerful servers removed from the end user. While this reduces local hardware constraints, it introduces significant drawbacks: privacy concerns regarding data access, recurring maintenance and storage costs, increased latency, and the necessity of an internet connection. On-device RAG addresses these challenges by executing the entire pipeline locally, making it ideal for querying sensitive personal information such as financial documents, contact details, and medical history. However, on-device deployment necessitates a delicate balance between limited memory and disk space. Specifically, the context size provided to the generative model must be restricted to manage KV cache and attention memory usage, while the size of stored embeddings must be minimized to preserve disk space. In this work, we propose a unified model that compresses the RAG context and utilizes the same representations for retrieval. This approach minimizes disk utilization compared to using separate representations, while significantly reducing the context size required for generation. With an average of 1/10 of the context, our model matches the performance of a traditional RAG reader without increasing storage requirements compared to a multi-vector retrieval model. This approach represents the first model to unify retrieval and context compression using a shared model and representation.

## Key Contributions

1. **Unified ECG Model**: A single model that performs three roles - encoding for retrieval, compressing text into vector representations, and generating responses from compressed contexts
2. **Shared Representations**: Uses the same vectors for both retrieval and generation, eliminating the need to encode and store separate retrieval and compression representations
3. **On-Device Optimization**: Significantly reduces context size (up to 16× compression) while maintaining performance comparable to standard RAG readers
4. **First-of-its-kind**: First model to unify retrieval and context compression using a shared model and representation

## Technical Approach

### ECG (Embed, Compress, Generate) Architecture
- Adapts a pretrained decoder transformer to also act as an encoder
- Prepends task prompt and appends special embedding tokens
- Two projection blocks:
  - θret: produces retrieval representations optimized for MaxSim similarity
  - θcomp: transforms retrieval representations into compressed context representations

### Training Recipe
1. **Self-Supervised Pretraining**: 
   - Uses unlabeled passage collection (Wikipedia)
   - Two strategies: reconstruction and neighboring text prediction
   - In-batch contrastive loss for retrieval representations
   - Dynamic variation of embedding tokens during training

2. **RAG-Specific Fine-tuning**:
   - Uses Natural Questions and Trivia QA datasets
   - Knowledge distillation from teacher models (not next-token prediction)
   - Joint optimization of generation and retrieval
   - Learned scaling for retrieval labels

### Key Technical Innovations
- **Mean-pooled MaxSim similarity**: Adapted from ColBERT for variable-length query representations
- **Gated residual connections**: In projection blocks for training stability
- **Dynamic loss scaling**: Learned temperature and teacher score scale for balancing retrieval and generation objectives
- **Weighted negative sampling**: Probability-based hard negative selection during training

## Experimental Results

### Models Evaluated
- SmolLM-v2 135M (small, on-device plausible)
- Gemma 3 1B (larger, on-device plausible)

### Key Findings

#### RQ1: Performance Under Constrained Context Budgets
- ECG models substantially outperform all baselines under strict active memory constraints
- With budget of 32 representations (SmolLM) and 16 (Gemma):
  - ECG achieves over 3× the Exact Match score of best standard RAG models on NQ
  - 0.343 vs 0.106 for SmolLM; 0.361 vs 0.104 for Gemma

#### RQ2: Context Efficiency and Disk Space
- Standard RAG with ColBERT retrieval requires 5×-16× the context budget to match ECG performance
- ECG cuts disk space requirement in half compared to separate retrieval and compression systems
- Uses slightly less space than ColBERT alone while solving context-length memory issues

#### RQ3: Unified vs Isolated Modeling
- Unifying retrieval and compression improves both efficiency and effectiveness
- ECG's multi-task training objective acts as regularization, yielding richer representations
- Performance gap: 0.224 vs 0.297 on NQ and 0.386 vs 0.485 on Trivia QA

#### RQ4: Drivers of Performance
- Excellent retrieval quality bolsters overall performance
- Dynamic loss scaling is critical (without it, NQ performance drops from 0.343 to 0.173)
- Generative distillation crucial for high-quality outputs
- Hard negatives significant for robust retrieval capabilities

## Implications

### For On-Device AI
- Enables practical on-device RAG for sensitive personal information (financial, medical, contacts)
- Reduces memory and storage requirements while maintaining performance
- Can be combined with existing low-level optimizations (quantization, speculative decoding)

### For AI Architecture
- Provides blueprint for "everything-models" that consolidate multiple functions
- Demonstrates viability of unified representations for different tasks
- Shows that multi-task training can improve rather than degrade individual task performance

### Future Directions
- Extending to larger models and more complex tasks
- Combining with other on-device optimizations
- Applying unified representation approach to other multi-task scenarios

## Related Work

### Context Compression
- Hard compression: Selective Context, LLMLingua, Nano-Capsulator, RECOMP
- Soft compression: ICAE, 500xCompressor, COCOM, PISCO, ACC-RAG

### Unified Retrieval and Generation
- Models that combine embedding and generation (e.g., GRIT, OneGen)
- xRAG: uses fixed retrieval embeddings but maintains separate models
- CLaRa: concurrent work unifying context and retrieval representations (limited evaluation)

### On-Device LLMs and RAG
- Hardware-level optimizations for local deployment
- Local index management approaches (MobileRAG, Pocket RAG)
- Memory management and efficiency improvements
