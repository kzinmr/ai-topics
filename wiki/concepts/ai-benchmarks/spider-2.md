---
title: "Spider 2.0"
type: concept
created: 2026-06-26
updated: 2026-06-26
tags:
  - benchmark
  - evaluation
  - coding-agents
  - software-engineering
sources:
  - title: "Spider 2.0: Real-World Enterprise Text-to-SQL Workflows"
    arxiv: "2411.07763"
    year: 2024
related_concepts:
  - concepts/ai-benchmarks/swe-bench
  - concepts/ai-benchmarks/livecodebench
  - concepts/ai-benchmarks/multi-swe-bench
  - concepts/evaluation/ai-benchmarks-and-evals
---

# Spider 2.0

Spider 2.0 is a benchmark for **real-world enterprise text-to-SQL workflows**. It evaluates AI agents' ability to generate complex SQL queries from natural language descriptions using actual enterprise database schemas and data.

## What It Measures

Spider 2.0 measures:

- **Complex SQL generation** — producing correct, efficient SQL from natural language specifications
- **Enterprise database understanding** — navigating large, real-world database schemas with hundreds of tables
- **Multi-step reasoning** — decomposing complex analytical questions into multi-part SQL queries
- **Domain knowledge application** — understanding business context and data semantics
- **SQL fluency across dialects** — handling dialect-specific syntax and features

## Data/Methodology

- **Source**: Real enterprise database environments and workflows
- **Scale**: Complex enterprise-level database schemas with large numbers of tables and columns
- **Task format**: Natural language questions paired with expected SQL outputs
- **Difficulty**: Significantly harder than original Spider — enterprise schemas, complex joins, nested queries, and advanced SQL features
- **Evaluation**: Execution-based accuracy (does the generated SQL produce correct results?) and exact match metrics
- **Dialects**: Multiple SQL dialects including BigQuery, Snowflake, and other enterprise platforms

## Key Results

- Enterprise-level text-to-SQL remains extremely challenging for current models
- Performance degrades significantly compared to academic benchmarks like original Spider
- Complex schema understanding and multi-table reasoning are primary failure points
- SQL dialect-specific features cause additional errors
- Results indicate a substantial gap between academic and enterprise SQL generation capabilities

## Related Benchmarks

| Benchmark | Relationship |
|-----------|-------------|
| [[concepts/ai-benchmarks/swe-bench\|SWE-bench]] | Both evaluate coding agents on real-world tasks, different domains |
| [[concepts/ai-benchmarks/livecodebench\|LiveCodeBench]] | Both provide challenging, evolving coding evaluation |
| [[concepts/ai-benchmarks/multi-swe-bench\|Multi-SWE-bench]] | Both extend evaluation to cover more real-world coding scenarios |
| [[concepts/ai-benchmarks/appworld\|AppWorld]] | Both evaluate agents on complex, realistic data interaction tasks |

## Connections to Other Wiki Concepts

- **[[concepts/ai-benchmarks/swe-bench]]**: Spider 2.0 applies the "real-world benchmark" philosophy to SQL generation, similar to how SWE-bench applies it to software bug resolution
- **[[concepts/evaluation/ai-benchmarks-and-evals]]**: Demonstrates the importance of domain-specific benchmarks — SQL generation has unique evaluation needs
- **[[concepts/ai-benchmarks/livecodebench]]**: Both address the gap between academic and real-world coding evaluation
- Spider 2.0 complements [[concepts/ai-benchmarks/multi-swe-bench|Multi-SWE-bench]] by covering SQL as an additional important programming language for agent evaluation
