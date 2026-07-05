---
title: On-Device RAG
created: 2026-06-04
updated: 2026-06-04
type: concept
tags:
  - rag
  - on-device
  - edge-ai
  - context-compression
  - model
  - privacy
  - local-llm
sources:
  - raw/articles/2026-04-15_killingback_unified-model-document-representation-on-device-rag.md
---

# On-Device RAG

On-Device RAG (Retrieval-Augmented Generation) refers to executing the entire RAG pipeline locally on user devices rather than on remote servers. This approach addresses critical limitations of server-based RAG systems, particularly for applications involving sensitive personal information.

## Core Challenges

### Memory and Storage Constraints
- **KV Cache Management**: Large text contexts balloon the KV cache, leading to out-of-memory errors or excessive battery drain
- **Disk Space**: Storing multiple retrieval and context representations exhausts precious device storage
- **Compute Limitations**: Mobile devices operate with shared, limited unified memory

### Performance Trade-offs
- **Context Size vs Quality**: Smaller context reduces memory usage but may degrade generation quality
- **Retrieval vs Compression**: Traditional approaches use separate models for retrieval and compression, doubling storage requirements
- **Latency Requirements**: On-device processing must be fast enough for interactive use

## Technical Approaches

### Context Compression
Two main strategies for reducing context size:

**Hard Compression**:
- Filters or rewrites text to remove irrelevant tokens
- Methods: Selective Context, LLMLingua, Nano-Capsulator, RECOMP
- Limitations: Can introduce grammatical errors, constrained by natural language bounds

**Soft Compression**:
- Encodes context into continuous vectors
- Methods: ICAE, 500xCompressor, COCOM, PISCO, ACC-RAG
- Advantages: More flexible, can achieve higher compression ratios

### Unified Representation Models
Recent work combines multiple RAG functions into single models:

**ECG (Embed, Compress, Generate) Model** (Killingback et al., 2026):
- First model to unify retrieval and context compression using shared representations
- Uses same vectors for both retrieval and generation
- Achieves 16× compression while matching standard RAG reader performance
- Reduces disk space by 50% compared to separate retrieval and compression systems

**Key Innovation**: 
- Single model acts as encoder, compressor, and generator
- Shared multi-vector representations for retrieval and generation
- Joint training with dynamic loss scaling for balanced optimization

## Performance Characteristics

### Compression Ratios
- Standard RAG with ColBERT requires 5×-16× more context to match ECG performance
- ECG achieves comparable accuracy with 1/10 of the context on average
- Storage requirements equivalent to ColBERT alone while solving context-length issues

### Accuracy Trade-offs
- Under strict context budgets (16-32 representations), ECG outperforms standard RAG by 3×
- Unified representations improve both efficiency and effectiveness
- Multi-task training acts as regularization, yielding richer context representations

### Resource Requirements
- Preprocessing can be scheduled opportunistically (e.g., while device charging)
- Reduces computational burden during latency-sensitive user queries
- Compatible with existing low-level optimizations (quantization, speculative decoding)

## Implementation Considerations

### Model Architecture
- Adapts pretrained decoder transformers for encoding tasks
- Special tokens for embedding sequences
- Projection blocks for retrieval and compression representations
- Gated residual connections for training stability

### Training Pipeline
1. **Self-Supervised Pretraining**:
   - Unlabeled passage collection (e.g., Wikipedia)
   - Reconstruction and neighboring text prediction tasks
   - In-batch contrastive loss for retrieval representations
   - Dynamic variation of embedding tokens

2. **RAG-Specific Fine-tuning**:
   - Question-answer datasets with retrieved documents
   - Knowledge distillation from teacher models
   - Joint optimization of generation and retrieval
   - Weighted negative sampling for hard examples

### Deployment Optimization
- **Indexing**: Preprocess documents during device idle time
- **Retrieval**: Fast similarity search with multi-vector representations
- **Generation**: Compressed contexts reduce KV cache memory usage
- **Storage**: Unified representations minimize disk footprint

## Applications

### Personal Information Retrieval
- **Financial Documents**: Bank statements, investment records, tax documents
- **Medical Records**: Health history, prescriptions, test results
- **Communication**: Emails, messages, contact information
- **Legal Documents**: Contracts, agreements, personal records

### Offline Scenarios
- **Remote Areas**: Poor or no internet connectivity
- **Travel**: International roaming without data access
- **Privacy-Sensitive**: Locations where data transmission is restricted
- **Reliability**: Critical applications requiring constant availability

### Edge Computing
- **Mobile Devices**: Smartphones, tablets with limited resources
- **IoT Devices**: Smart home, wearable technology
- **Embedded Systems**: Specialized hardware with strict constraints
- **Automotive**: In-vehicle information systems

## Comparison with Server-Based RAG

| Aspect | Server-Based RAG | On-Device RAG |
|--------|------------------|---------------|
| **Privacy** | Data sent to servers | Data stays local |
| **Connectivity** | Requires internet | Works offline |
| **Latency** | Network dependent | Local processing |
| **Cost** | Recurring server costs | One-time device cost |
| **Scalability** | Shared resources | Device-specific |
| **Updates** | Centralized updates | Manual updates |
| **Performance** | Higher compute limits | Limited by device |

## Current Limitations

### Technical Constraints
- **Model Size**: Limited by device memory and storage
- **Compute Power**: Mobile processors have lower throughput
- **Battery Life**: Continuous processing drains battery
- **Index Size**: Large corpora may not fit on device

### Practical Challenges
- **Cold Start**: Initial indexing requires significant time and resources
- **Updates**: Document changes require reindexing
- **Quality**: Compression may lose nuanced information
- **Complexity**: Multi-task training is difficult to optimize

## Future Directions

### Model Improvements
- **Larger Models**: Scaling to more capable on-device models
- **Better Compression**: Higher compression ratios with less quality loss
- **Multi-Modal**: Extending to images, audio, and video
- **Specialization**: Domain-specific optimizations

### System Optimizations
- **Hardware Acceleration**: NPU and GPU optimizations for mobile
- **Distributed Processing**: Split workloads across device components
- **Adaptive Quality**: Dynamic adjustment based on available resources
- **Incremental Updates**: Efficient handling of document changes

### Application Expansion
- **Real-Time Processing**: Streaming document analysis
- **Collaborative RAG**: Sharing insights across devices without data transfer
- **Federated Learning**: Improving models while preserving privacy
- **Edge-Cloud Hybrid**: Optimal workload distribution

## Key Research Papers

- **ECG Model** (Killingback et al., 2026): First unified model for on-device RAG with shared representations
- **COCOM** (Rau et al., 2024): Context embeddings for efficient answer generation
- **xRAG** (Cheng et al., 2024): Extreme context compression with one token
- **MobileRAG** (Park et al., 2025): Fast, memory-efficient on-device RAG
- **Pocket RAG** (Kang et al., 2026): On-device RAG for first aid guidance

## Related Concepts

- [[concepts/context-engineering/context-compression|Context Compression]]: Techniques for reducing context size in RAG systems
- [[concepts/edge-ai]]: Deploying AI models on edge devices with resource constraints
- [[concepts/local-llm/_index]]: Running large language models locally on consumer hardware
- [[entities/embeddings]]: Vector representations used for retrieval and compression
- [[concepts/colbert]]: Late interaction retrieval model using multi-vector representations
- [[privacy-preserving-ai]]: AI techniques that protect user data privacy
- [[mobile-ai]]: AI applications optimized for mobile devices

## Open Questions

1. **Scaling Laws**: How do on-device RAG performance characteristics change with larger models?
2. **Multi-Modal Integration**: Can unified representations work across text, image, and audio modalities?
3. **Dynamic Corpora**: How to efficiently handle frequently changing document collections?
4. **User Adaptation**: Can on-device models personalize to individual user needs without compromising privacy?
5. **Hardware Co-Design**: What hardware optimizations would best support on-device RAG workloads?
