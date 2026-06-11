---
title: Eric Ma
type: entity
handle: "@ericmjl"
created: 2026-05-29
updated: 2026-05-29
tags:
  - person
  - ai-agents
  - agent-skills
  - data-science
  - developer-tooling
  - bayesian
  - biotech
  - ai-adoption
  - blogger
  - youtube
sources:
  - transcripts/2026-05-15_vanishing-gradients_show-us-your-agent-skills-ep2.md
---

# Eric Ma (@ericmjl)

| | |
|---|---|
| **X** | [@ericmjl](https://x.com/ericmjl) |
| **Blog** | [ericmjl.github.io](https://ericmjl.github.io) |
| **GitHub** | [ericmjl](https://github.com/ericmjl) |
| **Role** | Senior Principal Data Scientist (Research), Moderna Therapeutics |
| **Known for** | Research Data Science at Moderna, PyMC core contributor, Bayesian methods in drug discovery, Marimo Pair agentic data science, author of pedagogical data science books |
| **Bio** | Eric Ma leads Research Data Science in the Data Science and AI group at Moderna Therapeutics (since July 2021). He earned his PhD in Biological Engineering from MIT (2017), was an Insight Health Data Science Fellow, and previously worked in a special ops data team at Novartis Institutes for Biomedical Research. He is an early core contributor to PyMC, an open source developer, Python conference speaker, and educator. His professional mission: make science run at the speed of thought so we can discover new medicines for patients faster. |

## Overview

Eric Ma is a leading practitioner of agentic data science — using AI coding agents to accelerate scientific research workflows at the intersection of biology, Bayesian statistics, and Python tooling. At Moderna, he leads a team of six building API-callable AI-powered software products for mRNA design, protein engineering, and lipid nanoparticle chemistry. His work spans probabilistic modeling with PyMC, deep neural networks, network science, and LLM-driven automation.

Ma's approach is distinctive for its emphasis on **methodology over models**. Rather than chasing the latest LLM, he focuses on building robust, reproducible workflows that combine the strengths of reactive notebooks (Marimo), coding agents (Cursor), and domain-specific scientific tools. He has authored two pedagogical data science books and is an active open source contributor and educator.

His blog at ericmjl.github.io covers topics ranging from using coding agents to write Marimo notebooks to benchmarking LLMs for data analysis tasks to managing personal knowledge with Obsidian and AI agents. He is also on the Editorial Review Board of the Journal of Machine Learning Research and has served on PyCon and SciPy organizing committees.

## Show Us Your (Agent) Skills Episode 2 (2026-05-15)

Eric appeared on Episode 2 to demonstrate **Marimo Pair**, a skill for agentic data science using reactive notebooks paired with a coding agent. His segment (from approximately 11:35 to 40:44) was the first demo of the episode and set the technical tone.

### Marimo Pair: Reactive Notebooks + Coding Agent

Eric demonstrated a live agentic data science workflow analyzing protein engineering data from his Novartis research. The key innovation is using **Marimo** (reactive notebooks) instead of Jupyter:

- **Reactive notebooks solve stale state**: In Jupyter, cells can go stale when variables are redefined out of order. Marimo notebooks are a deterministic DAG — the agent always knows what's computed and what depends on what.
- **Direct kernel access via bash script**: The Marimo Pair skill includes a bash script that lets the coding agent reach directly into the Python runtime, making the notebook "more like a canvas that you directly manipulate."
- **Markdown auto-generation**: The agent writes markdown cells explaining its own reasoning — literate programming for agent-human collaboration. "I have read and written too many notebooks that are just code after code after code with zero markdown cells explaining what the hell is going on."

### agents.md Rules for Scientific Rigor

Eric enforces scientific best practices through agents.md rules:

- **Cell naming conventions**: Standardized naming patterns for notebook cells
- **Color map standards**: Consistent visualization palettes
- **Literate programming style**: Markdown cells interleaved between code cells, not just a wall of code
- **"If you're going to make a claim, you need a plot"**: The agent must produce visual evidence for any analytical claim
- **`marimo check` enforcement**: The agent must run `uvx marimo check` on every file and fix all issues

### Evolution from UV Scripts to Marimo

Eric traced his journey: in February, his best workflow was writing UV-runnable PEP 723 scripts, producing plots as files, and writing analysis into `journal.md` — because "Jupyter notebooks, there's no good easy way to interact with the kernel from a coding agent." In March, Trevor Manz from the Marimo team showed him Marimo Pair. By April, he had to throw out his entire ODSC workshop curriculum and rebuild it around Marimo Pair.

### anywidget: 3D Protein Viewer

One of the most striking demos: Eric showed the agent building a **3D protein structure viewer** using anywidget, coloring the molecular ribbon by mutational effect. This demonstrated that agents could orchestrate complex scientific visualization libraries — not just create simple matplotlib plots.

### Heatmap Analysis of Protein Mutations

The core demo: analyzing single-point and combinatorial protein mutations. Eric walked through loading two CSV files (enzyme activity and enzyme chirality), creating Plotly heatmaps of mutational effects across amino acid positions, and having the agent generate explanatory markdown throughout. The data came from his published Novartis research on an enzyme that catalyzes conversion of a substrate into R or L form products.

### Two-Bucket Framework for Data Science

Eric articulated a framework for agent-assisted data science with two distinct modes:

1. **Loading context** — Feeding the agent domain knowledge: molecule structures, experimental data, protein engineering semantics, biological priors. This is the "what we know" bucket.
2. **Auto-optimize** — The agent iteratively improves analysis, generates visualizations, discovers patterns. This is the "what we're trying to learn" bucket.

The human stays at the boundary, deciding when to switch between buckets. This framework separates the human's role (providing domain context and evaluating results) from the agent's role (computational exploration and visualization).

### Voice-First Interaction

Eric discussed his experiments with voice-first agent interaction — dictating analysis requests and having the agent work while he steps away. This connects to his broader theme of making "science run at the speed of thought."

### Personal Context

Before the demo, Eric revealed he's a "token maxer" — his Cursor budget usage late last year was jaw-dropping. He also shared that his most embarrassing agent conversations involve "help me resolve merge conflicts on the PR such that I can rebase to merge later" — using agents for git operations he finds tedious.

## Core Ideas

### Making Science Run at the Speed of Thought

Eric's professional mission statement: accelerate scientific discovery by removing the friction between insight and execution. In practice, this means:

- Agents handle routine data manipulation, visualization generation, and code scaffolding
- Scientists focus on hypothesis formation, experimental design, and result interpretation
- The notebook becomes a living document that captures both code and reasoning

### Reactive Notebooks as Agent Substrate

Marimo's reactive execution model solves the fundamental problem of agent-notebook interaction: stale kernel state. When the agent writes a cell, it can be confident about what variables exist and what they contain. The notebook is a deterministic DAG, not an accumulation of side effects.

### Epistemic Preferences in Agent Skills

In his blog writing, Eric has argued there are three layers of implicit assumptions in any workflow skill: tool dependencies, organizational preferences, and **epistemic preferences** — the hardest to see and most important to document. His agents.md rules encode an epistemology: always provide visual evidence, always document reasoning in markdown, always check code quality.

### The Air Gap Problem

Eric has written about "air gaps" — manual steps in business or scientific processes where humans bridge the gap between digital systems. Closing these gaps with automation and coding agents can transform team efficiency and free up mental bandwidth.

## Key Work

### Research Data Science at Moderna (2021–present)
Leads a team of six building AI-powered software for mRNA design, protein engineering, and lipid nanoparticle chemistry. Core maintainer of internal AlphaFold deployment. Architected standardized data science workflows. Drove ~$1M in cost efficiencies in 2025 through software stack optimization. Co-organizer of quarterly "Docathons" promoting documentation culture.

### PyMC Core Contributor
Early contributor to PyMC, the probabilistic programming library. Brought Bayesian methods to Novartis drug discovery workflows.

### SeqLike (Open Source)
Core maintainer of Moderna's first open source project, a toolkit for biological sequence analysis.

### Data Science Books
Author of two pedagogical data science books, focused on making advanced concepts accessible to practitioners.

### Conference Organizing
Editorial Review Board of JMLR. PyCon and SciPy Financial Aid team member.

## Blog / Recent Posts

- **Use coding agents to write Marimo notebooks** (Oct 2025) — How to combine AI coding assistants with Marimo for automated Python development
- **Benchmarking LLMs with the Marimo Pair skill** (2026) — Comparative evaluation of Claude, GLM, and other models for data analysis tasks
- **Workflow-specific agent skills** — Three layers of implicit assumptions: tool dependencies, organizational preferences, and epistemic preferences
- **Air gaps: The manual steps that humans bridge** — Identifying and closing digital gaps in scientific workflows
- **Personal Knowledge Management with Obsidian and AI agents** — Reducing knowledge management overhead from 30-40% to under 10%

## Related Concepts

- [[entities/marimo]] — Reactive notebooks as agent substrate; the platform Eric uses for agentic data science
- [[concepts/multi-agents/agentic-data-science]] — Eric's two-bucket framework and Marimo Pair workflow as a new pattern for agent-assisted science
- [[entities/pymc]] — Probabilistic programming library Eric contributes to; Bayesian methods for drug discovery

## Related People

- **Trevor Manz** — Marimo team member who introduced Eric to Marimo Pair
- **[[entities/hilary-mason]]** — Fellow Episode 2 guest; Hilary praised Eric's workflow as an example of bringing science back into engineering
- **[[entities/bryan-bischof]]** — Fellow Episode 2 guest; both share an emphasis on evaluation and structured agent instructions
- **[[entities/tomasz-tunguz]]** — Fellow Episode 2 guest
