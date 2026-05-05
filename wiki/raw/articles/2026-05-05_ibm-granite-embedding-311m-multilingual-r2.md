---
title: "IBM Granite Embedding 311M Multilingual R2"
source: https://huggingface.co/ibm-granite/granite-embedding-311m-multilingual-r2
date: 2026-05-05
scraped: 2026-05-05
tags: [ibm, granite, embedding, multilingual, modernbert, matryoshka, open-source, apache-2]
---

# Granite-Embedding-311M-Multilingual-R2

**Granite-Embedding-311M-Multilingual-R2** is a high-performance, dense embedding model developed by IBM. It is designed for multilingual information retrieval, code search, and long-document processing. It utilizes the **ModernBERT** architecture and supports **Matryoshka Representation Learning (MRL)**.

## Key Specifications
- **Parameters:** 311 Million
- **Embedding Dimensions:** 768 (supports truncation down to 128)
- **Context Length:** 32,768 tokens
- **Architecture:** ModernBERT (Alternating attention, GeGLU, Rotary Position Embeddings)
- **License:** Apache 2.0 (Enterprise-friendly)
- **Vocabulary:** 262K tokens (derived from Gemma 3)

## Major Improvements in R2
The R2 model represents a significant leap over the previous 278M version:
- **Performance:** +14.2 point gain on average retrieval benchmarks; +11.8 points on Multilingual MTEB.
- **Context Window:** Increased from 512 to **32,768 tokens**.
- **Matryoshka Support:** Allows dimension reduction (512, 384, 256, 128) with minimal performance loss.
- **Deployment:** Native support for ONNX, OpenVINO, vLLM, and llama.cpp (GGUF).

## Language & Code Support
The model supports **200+ languages** generally, with **enhanced support for 52 languages** and **9 programming languages**: Python, Go, Java, JavaScript, PHP, Ruby, SQL, C, C++.

## Performance Benchmarks
| Benchmark | Granite-311M-R2 Score |
| :--- | :--- |
| **MTEB ML Retrieval (18 tasks)** | **64.0** |
| **MTEB Retrieval (English v2)** | 52.6 |
| **MTEB Code (v1)** | 63.9 |
| **LongEmbed (Long Doc)** | 71.7 |
| **RaR-b (Reasoning)** | 28.0 |

### Matryoshka Efficiency
Truncating the 768-dim vector to 256-dim only reduces the English MTEB score from 52.6 to 51.6, offering massive storage savings for a ~2% performance trade-off.
