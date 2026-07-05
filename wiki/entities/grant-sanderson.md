---
title: "Grant Sanderson"
type: entity
created: 2026-07-01
updated: 2026-07-05
aliases:
  - 3Blue1Brown
  - 3b1b
  - "Grant Sanderson (3Blue1Brown)"
tags:
  - person
  - educator
  - mathematics
  - youtube
  - ai-in-science
  - open-source
sources:
  - raw/articles/dwarkesh.com--p-grant-sanderson-2--960d89cd.md
  - https://www.dwarkesh.com/p/grant-sanderson-2
  - https://www.3blue1brown.com/about
  - https://en.wikipedia.org/wiki/3Blue1Brown
  - https://github.com/3b1b/manim
  - https://github.com/ManimCommunity/manim
---

# Grant Sanderson

**Grant Sanderson** is the creator of [3Blue1Brown](https://www.3blue1brown.com/), one of the most popular mathematics education channels on YouTube (8.35M+ subscribers, 747M+ total views, 235+ videos). His visual explanations of linear algebra, calculus, neural networks, and other mathematical topics have made him a leading voice in mathematics communication.

## Biography

Sanderson studied mathematics and computer science at Stanford University. After graduating, he worked for Khan Academy producing videos, articles, and exercises — primarily focused on multivariable calculus. Since the end of 2016, his primary focus has been on 3Blue1Brown and its associated projects.

The channel name "3Blue1Brown" is a self-reference to the color of his right eye, which has sectoral heterochromia — blue with a wedge of brown.

In 2020, Sanderson co-created and lectured for an MIT course on **Introduction to Computational Thinking** alongside Alan Edelman, David Sanders, James Schloss, and Benoit Forget. The course uses the Julia programming language and Manim-based animations to cover convolutions, image processing, COVID-19 data visualization, epidemic modelling, ray tracing, climate modelling, and ocean modelling.

He has also contributed to a Netflix documentary about infinity and writes for Quanta Magazine.

As of 2026, Sanderson has become an early and prominent voice on the intersection of AI and mathematics, arguing that AI is making faster progress in mathematics than in most other fields and that math serves as a **leading indicator** of what AI progress will look like elsewhere.

## YouTube Channel: 3Blue1Brown

| Metric | Value |
|--------|-------|
| **Subscribers** | 8.35M (as of May 2026) |
| **Total Views** | 747M+ |
| **Videos** | 235+ |
| **Joined** | March 2015 |
| **Funding** | Patreon (7,000+ supporters) |

### Key Video Series

| Series | Topics | Impact |
|--------|--------|--------|
| **Linear Algebra** | Vectors, matrices, eigenvalues, change of basis | Foundational visualization for ML practitioners |
| **Neural Networks** | Backpropagation, gradient descent, chain rule, cross-entropy | Most-watched NN explainer series; directly relevant to AI/ML wiki |
| **Calculus** | Derivatives, integrals, limits, Taylor series | Supplemental intuition builder for ML math |
| **Fourier Transform** | Complex numbers, DFT, convolution | Applied to signal processing and ML |
| **Differential Equations** | ODEs, PDEs, numerical methods | Applied to physics simulations |
| **Probability & Bayes** | Bayes theorem explained visually | Foundation for probabilistic ML |
| **Higher-Dimensional Geometry** | High-dimensional spheres, neural network geometry | 2025 Stanford MRC public lecture |

### Neural Networks Coverage

Sanderson's visual breakdown of **backpropagation** and **gradient descent** (2017) remains one of the most accessible explanations of these foundational ML algorithms. In 2025-2026, he gave public lectures connecting high-dimensional geometry to modern machine learning -- explaining the linear algebra and multidimensional calculus that allow neural networks to navigate abstract representation spaces and predict the next token.

## Manim (Mathematical Animation Engine)

**Manim** is a cross-platform, free and open-source animation engine released under the MIT License, initially developed by Grant Sanderson in early 2015. It provides a Python library for creating precise, programmatic animations of mathematical concepts.

The **Manim Community** ([ManimCommunity/manim](https://github.com/ManimCommunity/manim)) forked the original project and maintains a better-documented, more beginner-friendly version that has become the standard for educational math animations. Manim is adopted by educators worldwide for creating animated math lessons.

## AI and ML Relevance

While primarily a mathematics educator, several aspects of Sanderson's work are directly relevant to AI/ML:

1. **Neural Network Visualization Series** -- Most-watched backpropagation/gradient descent explainers on YouTube
2. **High-Dimensional Geometry Lectures** -- Applied to understanding ML embedding spaces (Stanford MRC 2025)
3. **Computational Thinking MIT Course** -- Covers algorithms applicable to ML
4. **Manim in ML Education** -- Used to visualize training dynamics, loss landscapes, and attention mechanisms
5. **UC Santa Cruz Talk** (Feb 2026) -- Math behind neural networks and high-dimensional geometry in modern ML platforms

## AI and Mathematics

### Mathematics as a Leading Indicator
Sanderson argues that AI has been making faster progress in mathematical problem-solving than in any other domain, making mathematics a "crystal ball" for how AI progress will unfold across the economy. The jagged frontier of AI capabilities is acutely visible in math — geometry is largely solved (AI solves IMO geometry problems in 19 seconds), combinatorics remains hard, and the spikiness is fractal (zooming in reveals further variation within subfields).

### The Fractal Frontier
In his June 2026 conversation with [[entities/dwarkesh-patel|Dwarkesh Patel]], Sanderson detailed how AI's capabilities in mathematics are not uniform:

- **Geometry**: AI has attained near-perfect performance (cold-solved in 19 seconds since 2024), essentially a brute-force capability
- **Combinatorics**: Remains the "wild card" — more playful, puzzly-seeming problems that resist pattern-matching approaches
- **The IMO ceiling**: AI would have gotten IMO gold in 2024 if the test had included more geometry problems instead of combinatorics — highlighting how benchmark design determines which capabilities appear "solved"

### Conceptual Breakthroughs vs. Pattern Matching
The key distinction Sanderson draws is between two types of mathematical intelligence:

1. **Pattern matching on existing solutions** — What current AIs excel at; matching known patterns to solve structured problems
2. **Conceptual breakthroughs** — Creating new objects, definitions, or fields (e.g., Galois creating group theory, Einstein developing general relativity)

He highlights the quote from Polylog: *"good mathematicians prove theorems, great mathematicians come up with conjectures, and the greatest mathematicians come up with definitions."* Current AIs are firmly in the first category.

### The Verification Loop Problem
Sanderson's most pointed observation concerns the **hundred-year verification loop** for conceptual breakthroughs. Galois theory, created in the 1830s, took nearly a century to be recognized as foundational — it required the development of cryptography, quantum physics, and group-theoretic symmetry analysis before its value was fully understood. This makes RLVR-style training impossible for conjecture generation: how do you build a verifiable reward signal for an idea whose value may take a century to manifest?

### Hidden Bridges Between Fields
Sanderson uses the Montgomery-Dyson story (1970s) to illustrate a capability that LLMs may be uniquely suited for: finding connections between disparate fields. Montgomery discovered a formula about the statistical distribution of Riemann zeta zeros that Dyson, a physicist, recognized as matching the eigenvalue statistics of random Hermitian matrices from nuclear physics. This cross-field connection — discovered by chance conversation — is precisely the kind of pattern matching across vast knowledge bases that AI excels at.

## Philosophy on AI and Education

### Human Curation Still Matters
Sanderson argues that learning will still depend on human curation — AI may generate vast amounts of correct mathematical content, but the selection, framing, and narrative structure that makes knowledge accessible remains a human skill requiring theory of mind that AI still lacks.

### Advice for Students
For students in AI-transformed fields, Sanderson's guidance emphasizes:
- Developing conceptual understanding, not just technical skill acquisition
- Understanding the deep structure of problems, not just solution patterns
- Building the ability to frame and select interesting problems — a capability that may remain human for longer

## Key Works

### 3Blue1Brown (YouTube)
- **Essence of linear algebra** — The most-watched linear algebra visualization series
- **Essence of calculus** — Visual approach to calculus fundamentals
- **Neural networks** — Accessible visual explanations of deep learning
- **AI and mathematics series** (forthcoming, 2026) — Multi-part project documenting AI progress in mathematics through interviews with mathematicians and demonstrations

### Notable Ideas
- **The fractal frontier**: AI capabilities in math are spiky at every scale — solving some sub-problems perfectly while failing at closely related ones
- **Hundred-year verification loops**: The fundamental obstacle to RLVR-based math AI training for conceptual contributions
- **Mathematics as leading indicator**: Math is not an isolated domain but a preview of how AI will transform knowledge work across fields

## Related Entities
- [[entities/dwarkesh-patel]] — Interviewer; discusses AI economics and cognition
- [[entities/jay-alammar]] — Fellow ML/visual educator
- [[entities/3blue1brown]] — Sanderson's YouTube channel

## References
- [Dwarkesh Podcast: Grant Sanderson — AI and the future of math (June 2026)](https://www.dwarkesh.com/p/grant-sanderson-2)
- [3Blue1Brown YouTube Channel](https://www.youtube.com/@3blue1brown)
