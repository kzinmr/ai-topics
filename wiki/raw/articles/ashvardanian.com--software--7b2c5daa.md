---
title: "My Open Software"
url: "https://ashvardanian.com/software/"
fetched_at: 2026-05-05T07:01:52.152688+00:00
source: "Ash Vardanyan"
tags: [blog, raw]
---

# My Open Software

Source: https://ashvardanian.com/software/

All of my software is hosted on GitHub, mostly under the
Apache-2.0
permissive license.
Free for commercial and non-commercial use, modification, and distribution.
Major Projects
#
USearch
- a universal search engine powering many databases, AI labs, and experiments in Natural Sciences. Compact C++ core with 10+ language bindings — 10–100× faster than Meta FAISS for vector search and far beyond Apache Lucene.
StringZilla
- SIMD, SWAR, and CUDA-accelerated string algorithms for search, matching, hashing, and sorting at Web Scale and Bioinformatics scale. Hundreds of hand-tuned kernels with manual multi-versioning, exposed to C, C++, Rust, Python, Swift, and JavaScript, up to 10× faster on CPUs and 100× faster on GPUs.
SimSIMD
- an extensive collection of mixed-precision vector math kernels for C, Python, Rust, and JavaScript. Designed for linear algebra, scientific computing, statistics, information retrieval, and image processing, delivering consistent SIMD speedups over BLAS and NumPy on both x86 and ARM architectures.
UCall
- a kernel-bypass web server backend for C and Python built on io_uring. Achieves 70× higher throughput and 50× lower latency than FastAPI for real-time workloads, including serving compact AI models.
UForm
- tiny multimodal AI models with state-of-the-art parameter and data efficiency. Compatible with Python, JS, and Swift, serving as a lightweight alternative to OpenAI CLIP for on-device and server inference.
ForkUnion
- ultra-low-latency parallelism library for Rust and C++. Avoids allocations, mutexes, and even Compare-And-Swap atomics — achieving up to 10× speedups over Rayon and TaskFlow.
Some of those are used in open-source databases, like
ClickHouse
,
DuckDB
,
TiDB
,
ScyllaDB
,
yugabyteDB
,
DragonflyDB
,
MemGraph
,
Vald
,
Turso
, LLM toolchains, like
LangChain
,
LlamaIndex
,
Microsoft SemanticKernel
,
Nomic AI GPT4All
,
Surf
, and many other less “open” systems, such as backend infrastructure of major AI labs, government intelligence agencies, Hyper-scale cloud companies, Fortune 500, iOS and Android apps with 100M-1B MAU.
Tutorials & Datasets
#
less_slow.cpp
- teaches a performance oriented mindset for C++, CUDA, PTX, and ASM
less_slow.rs
- Rust adaptation with a focus on higher-level abstractions
less_slow.py
- Python adaptation with a focus on scripting & data-management
SpaceV
- 1 billion vectors from Microsoft SpaceV extended for usability
USearchMolecules
- 28 billion fingerprints for drug discovery, published with AWS
Demos & Benchmarks
#
UStore
- multimodal embedded database for C, C++, and Python designed around key-value stores
StringWars
- micro-benchmarking StringZilla against the best Rust tools
HashEvals
- testing avalanche effect & differential patterns of string hash functions
ScalingElections
- parallel combinatorial voting in CUDA and Mojo for H100 GPUs
TinySemVer
- semantic versioning GitHub CI tool that doesn’t take 300K lines of JavaScript
SwiftSemanticSearch
- example of on-device real-time AI using UForm and USearch on iOS
ParallelReductionsBenchmark
- GPGPU benchmarks for SyCL, CUDA, OpenCL, Vulkan, etc.
LibSee
- non-intrusively profiling LibC calls with
LD_PRELOAD
tricks
PyBindToGPUs
- C++ and CUDA starter kit for Python developers avoiding CMake
StringTape
- Apache Arrow compatible tapes for space-efficient string arrays
JaccardIndex
- exploring CPU port utilization with Carry-Save Adders & Lookups
USearchBench.py
- Billion-scale search benchmarks against FAISS, Weaviate, and Qdrant
USearchBench.java
- Billion-scale search scaling benchmarks against Lucene, using Spark
ucsb
- parallel benchmarks for ACID-compliant key-value stores, like RocksDB
affine-gaps
- “less wrong” local and global Gotoh sequence alignments in one NumBa Python file
faster-fasta
- CLI tool for to parse, sort, dedup, and translate DNA, RNA, & protein sequences
