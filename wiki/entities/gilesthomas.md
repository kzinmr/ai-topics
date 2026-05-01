---
title: gilesthomas
description: Machine learning researcher, educator, and software developer. Founder of PythonAnywhere. Publishes detailed technical articles on LLM internals, smolagents, training, and inference optimization. Known for accessible, first-person explanations of complex ML concepts built on hands-on experimentation.
url: https://gilesthomas.com
type: entity
updated: 2026-04-30
aliases: [gpjt, Giles Thomas]
tags:
  - person
  - ml-researcher
  - educator
  - python-developer
  - smolagents
  - huggingface
  - llm
sources:
  - https://www.gilesthomas.com/2024/04/about/
  - https://www.gilesthomas.com/personal
  - https://github.com/gpjt
  - https://huggingface.co/gpjt
  - https://en.wikipedia.org/wiki/PythonAnywhere
  - https://wiki.python.org/python/GilesThomas.html
  - https://x.com/gpjt
---

# Giles Thomas

**Giles Thomas** (handles: `gpjt` on GitHub, Hugging Face, and X/Twitter) is a software developer, machine learning researcher, and entrepreneur. Founding creator of **PythonAnywhere**, the popular browser-based Python IDE and PaaS acquired by Anaconda in 2022. Since mid-2024, Thomas has shifted his focus to deep learning, authoring an extensive body of work documenting the process of building, training, and fine-tuning large language models from scratch.

## Overview

Thomas has been programming since childhood (BASIC, Z80 Assembler) and professionally across C++, Java, JavaScript, C#, and Python. He co-founded **Resolver Systems** in 2005 (building the Python-integrated spreadsheet Resolver One), pivoted through **Dirigible** (a cloud spreadsheet), and ultimately created **PythonAnywhere** in 2011 — a platform serving hundreds of thousands of Python developers. After its acquisition by Anaconda, Thomas remained as team lead through mid-2025 before taking a sabbatical.

Thomas's blog, gilesthomas.com, has been active since November 2006 and spans hundreds of posts across categories including AI (82 posts), Python (71), TIL deep dives (75), and an extensive **LLM from scratch** series (46 posts). Content is licensed under Creative Commons Attribution 4.0.

In late 2024, Thomas began working through Sebastian Raschka's *Build a Large Language Model (from Scratch)*, documenting each chapter on his blog. This evolved into a comprehensive research program: training GPT-2-scale models (163M parameters) across multiple cloud GPU configurations, conducting controlled intervention experiments, releasing trained models to Hugging Face, and becoming one of the most prolific independent smolagents content creators in the Hugging Face ecosystem.

Thomas is active across platforms under the handle `gpjt`: [GitHub](https://github.com/gpjt), [Hugging Face](https://huggingface.co/gpjt), [X/Twitter](https://x.com/gpjt), and [Bluesky](https://bsky.app/profile/gilesthomas.com).

## Core Topics

### smolagents Tutorials

Thomas is one of the most active independent content creators on Hugging Face's **smolagents** library, producing a steady stream of tutorials, comparisons, and deep-dives since December 2025:

- **Beginner's Guide to smolagents** (December 2025 / January 2026) — A two-part introductory series covering the fundamentals of Hugging Face's minimalist agent framework.
- **How smolagents Code Agent Works** (January 2026) — Explores the internals of the `CodeAgent` class, explaining how the library generates and executes Python code as agent actions.
- **smolagents Deepdive: How to Build Tools and Agents** (January 2026) — Comprehensive walkthrough of the tool-building workflow, including the `@tool` decorator, tool specifications, and integration patterns.
- **smolagents vs. LangGraph Comparison** (February 2026) — An independent comparison of the two frameworks covering API design, complexity, and production readiness.
- **smolagents vs. OpenAI Agents SDK: Feature Parity** (April 2026) — Maps features between smolagents and the OpenAI Agents SDK, identifying gaps, overlaps, and integration possibilities.
- **Visualizing smolagents Logs and Traces Using Argilla** (April 2026) — Demonstrates how to use Argilla for monitoring and debugging smolagents agent execution traces.

### Building Tools

Thomas has produced multiple deep-dives on tool creation in the smolagents ecosystem:

- **Turning Vision Transformers into smolagents** (December 2025) — Adapting computer vision models for use as agent tools.
- **Build a Smolagent with Custom Tools** (January 2026) — Step-by-step guide through the custom tool authoring workflow.
- **Building Tools in smolagents v2 from Their Maker** (March 2026) — In-depth coverage of the v2 tool system changes and best practices for tool authors.

### Multi-Agent Systems

- **How to Build a Multi-Agent System with smolagents** (February 2026) — Tutorial on orchestrating multiple specialized agents using smolagents's `managed_agents` pattern, covering manager agent configuration, role assignment, and task delegation.

### LLM from Scratch Series

The most ambitious series on Thomas's blog. Spanning 46+ posts (from December 2024), it documents his journey through Sebastian Raschka's textbook with significant original experimentation.

**Core topics:** Tokenization, embeddings, scaled dot-product and causal attention, multi-head attention, layer normalization, feed-forward networks, residual connections, logit-to-prediction transformation.

**Practical experimentation:**
- Training a GPT-2-small-style model (163M params) across RTX 3090 and cloud 8× A100 / H100 configurations
- **Interventions series** (parts 32a–32h): Controlled experiments on learning rate scheduling, dropout removal, weight decay, QKV bias, gradient clipping, AMP precision, and weight tying
- Key finding: Batch size had more than *double* the loss-reduction impact vs. all other positive interventions combined
- **DistributedDataParallel (DDP)** multi-GPU training, gradient accumulation for consumer hardware
- Fine-tuning for classification/instruction-following, and the "transcript hack" for base-model chatbots

**Model releases:** Thomas has published over 30 GPT-2 architecture models (0.2B parameters) on Hugging Face, all trained on the FineWeb dataset. The collection includes baseline models and "stacked intervention" variants across different GPU configurations (RTX 3090, A100, H100).

**Evaluation methodology:** Developed a side-by-side "LLM-as-a-judge" technique that presents multiple model responses simultaneously for more consistent evaluation, addressing the variance problem of single-model scoring.

### Additional ML Content

- **Messing around with fine-tuning LLMs** (10-part series, 2024) — Fine-tuning experiments covering load balancing, multi-GPU training, Hugging Face Hub integration with `AutoModel`, `pipeline`, and `Trainer`.
- **10Gb/s Home Ethernet** (April 2026) — Technical deep-dive on setting up high-speed wired networking infrastructure at home - two-part series covering theoretical background and practical implementation.
- **LLM Coherence Evolution** (April 2026) — Visualized how a GPT-2-small-style model becomes more coherent over 57 training checkpoints. Key finding: FineWeb-Edu models scored significantly higher on IFT than loss alone would predict, suggesting knowledge density matters separately from raw intelligence.
- **Lambda Labs Instance Automation** (April 2026) — Built `lambda-manager`, a CLI tool for polling Lambda Labs API and automatically launching GPU instances when available, with Telegram notifications.

## Writing Style & Philosophy

Thomas's writing is characterized by a distinctive **first-person, narrative-driven approach** to technical exposition. Rather than presenting polished results, he documents the learning process itself — including dead ends, misunderstandings, surprising failures, and incremental discoveries.

**Key qualities:**

- **Accessibility through transparency:** Thomas shares not just what worked, but what didn't, making complex ML concepts approachable by normalizing the difficulty of learning them. His blog subtitle — "Doing my best to speedrun 20 years of AI research. YMMV" — captures this ethos.
- **Hands-on experimentation:** Every article is grounded in actual code Thomas wrote and ran. Claims are backed by concrete experiments with published results, datasets, and model weights.
- **Intellectual honesty about uncertainty:** Thomas frequently flags when his understanding is provisional, noting "I'm not 100% sure about this" and inviting corrections. He distinguishes between areas where he has direct experimental evidence and areas where he's relying on secondary sources.
- **Comparative analysis:** A recurring pattern is the side-by-side comparison — smolagents vs. LangGraph, smolagents vs. OpenAI Agents SDK, full FP32 vs. AMP, different batch sizes — providing readers with practical decision frameworks.
- **Historical context:** Thomas's writing benefits from nearly two decades of startup and software engineering experience. His analyses of ML frameworks reference real deployment constraints, infrastructure costs, and engineering trade-offs that pure ML researchers might miss.

Thomas's blog has been running since 2006, and his writing voice shows a steady evolution from Python/startup commentary to deep ML technical content without losing its conversational tone. He cites influences including Michael Foord (who inspired his blogging habit) and maintains a blogroll featuring Astral Codex Ten, Simon Willison's Weblog, Hackaday, and technologist peers.

## Entrepreneurial Background

### Resolver Systems (2005–2010)

Co-founded with Robert Smithson and Patrick. Built **Resolver One**, a Python-integrated spreadsheet targeting financial users. The product launched in 2008 — directly into the financial crisis. Thomas candidly characterizes this as a classic startup mistake: building in secret for over a year without user validation.

### PythonAnywhere (2011–2025)

After the Resolver One pivot to **Dirigible** (a cloud-based spreadsheet), Thomas noticed users were ignoring the grid and using the environment as a Python IDE. The team removed the spreadsheet entirely and PythonAnywhere was born.

**Key milestones:**
- 1,000th customer celebrated under London's Smithfield Market
- Grew to cover all costs and became independently sustainable
- **Acquired by Anaconda, Inc. in June 2022** — Thomas stayed on as principal software engineer and team lead for three years post-acquisition
- **Departed June 2025** — took a sabbatical described as "a year off to clear my head, reset, and relax"

Thomas is a **Python Software Foundation (PSF) Fellow** and an advocate of **Extreme Programming** methodology. He holds a Master of Arts from the **University of Cambridge**.

## Cross-References

- **[[Hugging Face]]** — Thomas is deeply embedded in the Hugging Face ecosystem. He publishes models on Hugging Face Hub (`gpjt`), authors extensive tutorials on the smolagents library (a Hugging Face project), and uses Hugging Face infrastructure (fine-tuning, Transformers, datasets) throughout his LLM from scratch work. His smolagents vs. OpenAI Agents SDK comparison (April 2026) positions smolagents within the broader agent framework landscape.
- **smolagents** — Thomas is likely the most prolific independent blogger covering Hugging Face's smolagents library. His content spans the full lifecycle: beginner tutorials, custom tool building, multi-agent orchestration, framework comparisons, and debugging/monitoring with Argilla. His work effectively serves as unofficial third-party documentation for the project.
- **PythonAnywhere** — Thomas's foundational creation. The platform-as-a-service for Python developers shaped his engineering perspective and continues to influence his ML work (cloud GPU usage patterns, platform economics awareness).
- **Anaconda** — Acquired PythonAnywhere in 2022. Thomas worked at Anaconda as team lead through 2025, and his ML research uses Anaconda's Python distribution ecosystem.

## References

- gilesthomas.com--2025-12-beginners-guide-to-smolagents-2--493ac600
- gilesthomas.com--2025-12-turning-vision-transformers-into-smolagents--89a0f31f
- gilesthomas.com--2026-01-beginners-guide-smolagents-code-agent-tutorial--4174b88e
- gilesthomas.com--2026-01-build-smolagent-with-custom-tools--5db354d9
- gilesthomas.com--2026-01-how-smolagents-code-agent-works--3672c22e
- gilesthomas.com--2026-01-smolagents-deepdive-how-to-build-tools-and-agents--c65ce23a
- gilesthomas.com--2026-02-from-scratch-inference-only-smolagent--3b6137d6
- gilesthomas.com--2026-02-how-to-build-a-multi-agent-system-with-smolagents--00b211f6
- gilesthomas.com--2026-02-smolagents-vs-langgraph-comparison--7a2f7102
- gilesthomas.com--2026-03-building-tools-in-smolagents-v2-from-their-maker--6f2a6bbe
- gilesthomas.com--2026-04-smolagents-vs-openai-agents-sdk-feature-parity--4df391fa
- gilesthomas.com--2026-04-visualizing-smolagents-logs-and-traces-using-argilla--cc8f7863
- gilesthomas.com--2026-04-llm-from-scratch-33-what-i-learned-from-the-appendic--383f52a1
- gilesthomas-coherence-2026-04-17.md
- gilesthomas.com--2026-04-automating-starting-lambda-instances--e9d854e4.md
- gilesthomas.com--2026-04-10g-ethernet-what-i-did--89f5510c.md
- gilesthomas.com--2026-04-10g-ethernet-what-i-relearned--8afc5c80.md
