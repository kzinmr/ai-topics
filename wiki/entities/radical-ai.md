---
title: Radical AI
type: entity
created: 2026-06-18
updated: 2026-06-18
tags:
  - entity
  - company
  - materials-science
  - ai-in-science
  - self-driving-labs
  - open-source
related:
  - ai-in-science
  - automated-lab
  - materials-discovery
sources:
  - raw/newsletters/2026-06-17-the-self-driving-lab-joseph-krause-radical-ai.md
---

# Radical AI

| | |
|---|---|
| **Type** | Materials Science AI Company |
| **Founded** | ~2024 (est.) |
| **Founder** | Joseph Krause |
| **Key Technology** | Self-Driving Lab (SDL), AI Scientist |
| **Open-Source** | TorchSim, MATRIX/MATRIX-PT |
| **Interview** | [[entities/latent-space]] podcast (June 17, 2026, by Brandon Anderson) |

## Overview

Radical AI is a materials science company founded by Joseph Krause that accelerates materials discovery through an automated self-driving laboratory. The company's core innovation is the **Self-Driving Lab (SDL)**, which combines scientific knowledge, computational techniques, and human intuition in a closed-loop system where an AI scientist generates and tests hypotheses autonomously.

As Joseph Krause articulated in his [[entities/latent-space]] podcast interview: *"In materials, the ground truth is the material itself. You have to be able to test it and characterize it."*

The company sits at the intersection of AI and experimental materials science, tackling the fundamental bottleneck in materials discovery: the slow, serial process of hypothesis generation, synthesis, and characterization that has historically limited the pace of innovation. See also [[concepts/ai-in-science]].

## Technology

### Self-Driving Lab Concept

The Self-Driving Lab (SDL) functions as a **closed-loop system** that integrates three components:

1. **AI Scientist** -- Generates hypotheses about novel materials formulations
2. **Automated Robotics** -- Synthesizes candidate materials in parallel
3. **Characterization Systems** -- Tests and evaluates material properties automatically

Unlike traditional materials research, where experiments run serially with significant human overhead between steps, the SDL runs multiple research campaigns **in parallel**, dramatically compressing discovery timelines.

### AI Scientist

The AI Scientist combines:
- **Scientific knowledge** -- Domain expertise in materials science and metallurgy
- **Computational techniques** -- Simulations and AI-driven prediction models
- **Human intuition** -- Curated priors and expert guidance integrated into hypothesis generation

The AI Scientist proposes candidate materials, the automated lab synthesizes and characterizes them, and the results feed back into the AI's models for the next round of hypotheses.

### Alloy Discovery Pipeline

Radical AI's primary focus is on alloy discovery. The system can autonomously propose, synthesize, and characterize new metallic alloys, exploring compositional spaces that would be impractical with traditional brute-force methods.

## Key Achievements

- **1200 alloys produced and characterized in six months** -- a nearly 10x speedup over the DARPA/GE MACH program, which aimed to create 500 new alloys in a year
- **300 new materials proposed and tested by the AI scientist**, of which **ten were found to have novel state-of-the-art properties** already being developed for commercial applications
- **Scalable throughput** -- can produce, test, and characterize a hundred new alloys in a single day

These results demonstrate that AI-driven autonomous labs can operate at a scale and speed that materially accelerates the materials discovery pipeline, moving from academic proof-of-concept to industrially relevant throughput.

## Open-Source Contributions

### TorchSim

TorchSim is an open-source PyTorch-based molecular dynamics (MD) simulation framework developed by Radical AI. It has been spun off into its own non-profit organization to support broader community development. TorchSim makes MD simulations accessible within the PyTorch ecosystem, enabling tighter integration between learned models and physics-based simulation.

### MATRIX / MATRIX-PT

The MATRIX dataset (Materials Ancillary Testing and Research Information Xchange) is an open-source dataset for benchmarking autonomous self-driving labs. It provides standardized test cases for evaluating how well AI systems can navigate materials discovery tasks.

**MATRIX-PT** is an open-source model trained on this dataset, providing a baseline that other researchers can build upon and compare against. Together, MATRIX and MATRIX-PT aim to establish a common benchmark for the self-driving lab community, analogous to how ImageNet or GLUE accelerated progress in computer vision and NLP.

## Geopolitical Context

Joseph Krause spent time in Washington, D.C. before founding Radical AI, focused on the geopolitical competition in materials science. A central dynamic is the contrast between:

- **China's centralized model** -- State-directed materials research with coordinated funding and national-level priorities
- **US approach** -- Decentralized innovation through startups, universities, and DARPA-style programs

The speed of Radical AI's SDL -- achieving 10x improvement over a DARPA benchmark -- is framed as evidence that AI-driven automation can give the US a strategic advantage in this critical domain, where materials innovation underpins competitiveness in semiconductors, batteries, aerospace, and defense.

## Team

### Joseph Krause (Founder)

Joseph Krause is a materials scientist who founded Radical AI after recognizing that the pace of materials discovery was being held back not by scientific understanding, but by the throughput of experimental workflows. Before founding Radical AI, he spent time in D.C. working on materials science policy and geopolitical strategy.

### Brandon Anderson (Interviewer)

Brandon Anderson conducted the interview with Joseph Krause for the [[entities/latent-space]] podcast, published June 17, 2026. The conversation covered the technical architecture of the Self-Driving Lab, Radical AI's open-source philosophy, and the geopolitical stakes of AI-accelerated materials discovery.

## See Also

- [[concepts/ai-in-science]] -- AI applications in scientific research
- [[entities/latent-space]] -- Podcast that featured Radical AI
- [[concepts/automated-lab]] -- Broader category of automated scientific laboratories
