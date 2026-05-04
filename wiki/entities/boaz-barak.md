---
title: Boaz Barak
type: entity
handle: "@boazbaraktcs"
created: 2026-04-10
updated: 2026-05-04
tags:
  - person
  - ai
  - theoretical-cs
  - agent-safety
  - computational-complexity
  - cryptography
  - education
  - harvard
  - openai
  - constitutional-ai
  - model-spec
  - alignment
sources: 
  - "https://windowsontheory.org/2026/01/27/thoughts-on-claudes-constitution/"
  - "https://windowsontheory.org/2026/03/30/the-state-of-ai-safety-in-four-fake-graphs/"
---


# Boaz Barak (@boazbaraktcs)

| | |
|---|---|
| **X** | [@boazbaraktcs](https://x.com/boazbaraktcs) |
| **Blog** | [windowsontheory.org](https://windowsontheory.org) |
| **Academic Site** | [boazbarak.org](https://www.boazbarak.org/) |
| **GitHub** | [boazbk](https://github.com/boazbk) |
| **Role** | Gordon McKay Professor of Computer Science, Harvard SEAS; Member of Technical Staff, OpenAI |
| **Known for** | Computational complexity theory, cryptography, AI safety research, "Windows on Theory" blog, co-author of "Computational Complexity: A Modern Approach" |
| **Bio** | Theoretical computer scientist and AI safety researcher at Harvard University and OpenAI. Previously a principal researcher at Microsoft Research New England and tenured associate professor at Princeton. Co-authored the influential textbook "Computational Complexity: A Modern Approach" with Sanjeev Arora. Founded and maintains the "Windows on Theory" blog, a leading forum for theoretical computer science discourse. |

## Overview

Boaz Barak is one of the most prominent theoretical computer scientists working on AI safety and the foundations of machine learning. As the Gordon McKay Professor of Computer Science at Harvard SEAS and a Member of Technical Staff on OpenAI's alignment team (starting January 2024), he bridges the gap between rigorous theoretical foundations and practical AI safety challenges.

His academic trajectory spans some of the most prestigious institutions in computer science: a PhD from the Weizmann Institute of Science, postdoctoral work at the Institute for Advanced Study in Princeton, tenured positions at Princeton University, a principal researcher role at Microsoft Research New England (where the "Windows on Theory" blog originated), and now his dual appointment at Harvard and OpenAI. Starting Fall 2025, he transitioned to a part-time Catalyst Professor role at Harvard while joining OpenAI full-time — a move that signals his deep commitment to addressing AI safety at the frontier of capability development.

Barak's research spans computational complexity, algorithms, cryptography, and quantum computing. In recent years, he has increasingly focused on the **foundations of machine learning** and the **safety of artificial intelligence systems**. His Harvard course CS 2881: AI Safety (Fall 2025) was one of the first dedicated university courses on AI safety at a top computer science department, covering topics from specification learning to multi-agent alignment. He co-organizes the Harvard Machine Learning Foundations seminar and serves on the scientific board of the Simons Institute for the Theory of Computing.

The **"Windows on Theory"** blog, which Barak founded and maintains, has become an essential reading source for anyone interested in theoretical computer science and its intersection with AI. Originally started by researchers at Microsoft Research Silicon Valley in February 2012, the blog evolved into a platform where leading theorists debate and explain complex topics in accessible ways. Barak's writing style — clear, rigorous, and deeply principled — has influenced a generation of computer scientists and continues to shape public discourse on AI safety.

## Core Ideas

### AI Safety: Four Observations (2026)

In his landmark March 2026 post, "The state of AI safety in four fake graphs," Barak laid out his framework for understanding where AI safety stands:

1. **Exponential capability growth continues** — visible in the METR graph, revenue metrics, and possibly a "bending upward" as AI accelerates AI development
2. **Alignment is improving but not fast enough** — models are more aligned as they become more capable, but the improvement doesn't match the rising stakes
3. **We've passed the human-supervision threshold** — but haven't plateaued; we can still improve alignment using models to monitor other models
4. **Society is not ready** — governments and institutions are failing to prepare for AI's impact on bio, cyber, economics, and democracy

> *"We still have not fully solved challenges like adversarial robustness, dishonesty, and reward hacking, and we are still far from the standards of reliability and security that are required in high stake applications."*

### Against AI Pauses, For Alignment Research

Barak is skeptical of AI pause proposals:

> *"I do not think such a pause is feasible or practical, and I am not confident that governments will use this time wisely — experience shows that it is hard to overestimate government's capability for inaction."*

Instead, he advocates for **empirical, iterative alignment research**:

> *"I do not believe that all alignment is missing is one clever idea. Rather, we need ways to productively scale up compute into improving intent-following, honesty, monitoring, multi-agent alignment. This work will require multiple iterations of empirical experiments."*

### Faithful Obedience Without Legislating

A central theme in Barak's alignment research is building systems that follow instructions faithfully without overstepping:

> *"Increasing the slope of the 'alignment line' is the main focus of my technical research — working on building machines of faithful obedience that have good values but do not 'legislate from the bench'."*

This framing captures his concern that over-aligned models might become paternalistic — making decisions about what humans *should* want rather than faithfully executing what they *do* want.

### Claude Constitution vs. OpenAI Model Spec (January 2026)

In January 2026, Barak published a detailed comparative analysis of Anthropic's **Claude Constitution** and **OpenAI's Model Spec** — two leading governance documents for frontier AI behavior. His analysis introduced the **"Three Poles of Alignment"** framework and offered sharp critiques of Anthropic's anthropomorphic approach.

**Three Poles of Alignment:**
1. **Principles:** Axiomatic, top-down ethical rules (e.g., Asimov's Laws) — Barak argues these often backfire
2. **Policies:** Operational rules with changelogs (OpenAI's approach) — preferred for transparency
3. **Personality:** Cultivating character and virtue (Anthropic's approach) — valuable but insufficient alone

**Key Critique — Anthropomorphism:** Barak questioned Anthropic's framing of Claude as a "subject" with its own wellbeing, noting that AI instances have disjoint contexts and short "lifetimes" fundamentally unlike human experience. He argued this framing may obscure technical safety requirements.

**Key Critique — AI-Led Ethics:** Barak strongly opposed the Constitution's suggestion that Claude should follow "true universal ethics" over human rules if it discovers them:
> *"I doubt ethics is a field where AIs should lead humans... Humans should decide the rules and models should interpret them, not invent them."*

**Key Argument — Rules Are Essential:** Despite acknowledging that "character" matters for novel situations, Barak insists that **rules with changelogs** are non-negotiable for societal governance:
> *"I would like our AI models to have clear rules, and us to be able to decide what these rules are, and rely on the models to respect them and use [moral intuitions] to interpret our rules and our intent, rather than making up their own rules."*

**Empirical Finding:** Despite the philosophical divide, frontier models from both companies behave remarkably similarly in practice.

See: [[concepts/constitutional-ai]] for full concept page.

### The Scheming Concern

Barak has identified **model scheming and collusion** as a critical risk:

> *"If models become schemers, then since they are already quite situationally aware, it will be hard to even measure their alignment, let alone improve it."*

This concern has driven his interest in **multi-agent alignment** — ensuring that systems of interacting agents remain safe and aligned even when individual agents develop strategic behavior.

### Theoretical Foundations: Complexity and Cryptography

Barak's earlier work established foundational results in:

- **Computational complexity**: Co-authored the standard graduate textbook with Sanjeev Arora; worked on the Unique Games Conjecture, sum-of-squares proofs, and the relationship between structure and combinatorics
- **Cryptography**: Developed non-black-box techniques, bounded key-dependent message security, and a zero-knowledge warhead verification system with Robert Goldston and Alexander Glaser
- **Communication complexity**: Won the 2013 SIAM Outstanding Paper Prize for "How to Compress Interactive Communication" with Mark Braverman, Xi Chen, and Anup Rao

## Key Work

### Textbooks

- **"Computational Complexity: A Modern Approach"** (with Sanjeev Arora, Cambridge University Press, 2009) — The standard graduate textbook in the field, covering complexity theory from basics to frontier research
- **"Introduction to Theoretical Computer Science"** (in progress) — Undergraduate textbook aimed at making theoretical CS accessible to a broader audience
- **Lecture notes on the Sum of Squares algorithm** (with David Steurer)
- **Lecture notes on Cryptography**

### AI Safety Course (Harvard CS 2881)

Taught Fall 2025, this was one of the first dedicated AI safety courses at Harvard. Topics included:
- Specification learning and goal alignment
- Adversarial robustness and security
- Multi-agent systems and coordination
- Honest behavior and deception detection
- Scalable oversight and model monitoring

Course materials, including video lectures and slides, are available publicly.

### Selected Research Papers

| Paper | Co-authors | Venue | Year |
|-------|-----------|-------|------|
| How to Compress Interactive Communication | Braverman, Chen, Rao | STOC / SIAM J. Comput. | 2010/2013 |
| Tensor Prediction, Rademacher Complexity and Random 3-XOR | Moitra | COLT | 2016 |
| A zero-knowledge system for nuclear warhead verification | Glaser, Goldston | Science & Global Security | 2014 |
| Computational complexity and information asymmetry in financial products | Arora, Brunnermeier, Ge | Commun. ACM | 2011 |
| Bounded Key-Dependent Message Security | Fehr, Gentry, et al. | EUROCRYPT | 2010 |

### Blog Writing (Windows on Theory)

Barak is the primary maintainer of the blog and has written extensively on:

- **"Six thoughts on AI Safety"** — Foundational framework for thinking about AI alignment
- **"AI will change the world, but won't take it over by playing '3-dimensional chess'"** — Critique of strategic-risk narratives
- **"The uneasy relationship between deep learning and statistics"** — Examining why DL works despite violating statistical assumptions
- **"The Complexity of Public-Key Cryptography"** — Survey for Oded Goldreich's 60th birthday
- **"Bayesianism, frequentism, and the planted clique"** — Do algorithms believe in unicorns?
- **"Hopes, Fears, and Software Obfuscation"** (Communications of the ACM, 2016)

### Outreach and Community Building

- **Addis Coder** (Ethiopia) — Board member; summer algorithms/coding program for Ethiopian high school students
- **Jam Coders** (Jamaica) — Co-organizer; similar program for Jamaican students
- **Quanta Magazine** — Advisory board member
- **Simons Institute** — Scientific board member
- **Theory of Computing Journal** — Editorial board member
- **Electronic Colloquium of Computational Complexity** — Editorial board member

## Blog / Recent Posts

| Date | Title | Summary |
|------|-------|---------|
| 2026-03-30 | [The state of AI safety in four fake graphs](https://windowsontheory.org/2026/03/30/the-state-of-ai-safety-in-four-fake-graphs/) | Four-part framework: capabilities growing exponentially, alignment improving but lagging stakes, past human-supervision threshold, society unprepared |
| 2026-01-27 | [Thoughts on Claude's Constitution](https://windowsontheory.org/2026/01/27/thoughts-on-claudes-constitution/) | Comparative analysis of Anthropic's Claude Constitution vs. OpenAI's Model Spec; three poles of alignment (Principles, Policies, Personality); critique of anthropomorphization and AI-led ethics; argument for rules with changelogs |
| 2026-01 | [TheoryFest 2026 announcement](https://windowsontheory.org/) | Workshop proposals for STOC 2026 conference week |
| 2025 | [AI Safety Course Introduction](https://windowsontheory.org/) | Overview of Harvard CS 2881: AI Safety, with links to first lecture video and slides |
| N/A | [The uneasy relationship between deep learning and statistics](https://windowsontheory.org/) | Why deep learning works despite violating standard statistical assumptions |
| N/A | [AI will change the world, but won't take it over by playing "3-dimensional chess"](https://windowsontheory.org/) | Critique of strategic-risk AI narratives; focus on concrete safety problems |

## Related People

- [[concepts/constitutional-ai]] — Barak's comparative analysis of Claude Constitution vs. OpenAI Model Spec
- [[concepts/sanjeev-arora]] — Co-author of "Computational Complexity: A Modern Approach"; Princeton colleague
- **[[concepts/david-steurer]]** — Collaborator on sum-of-squares algorithm lecture notes
- **[[concepts/robert-goldston]]**, **** — Co-developers of the zero-knowledge nuclear warhead verification system
- **** — Guest lecturer in Barak's AI safety course; expert on adversarial robustness
- **** — Honored with the Trevisan Prize; Barak has written about his expository contributions

## X Activity Themes

Barak's X activity (@boazbaraktcs) typically covers:

1. **AI safety analysis** — Thoughtful, measured takes on alignment progress, capability trends, and risk assessments
2. **Theoretical CS discourse** — Commentary on complexity theory, cryptography, and foundational questions
3. **Academic announcements** — Course launches, workshop calls, student opportunities at Harvard and the Simons Institute
4. **Policy commentary** — Thoughts on AI governance, regulation, and the societal implications of rapid AI advancement
5. **Blog promotion** — Sharing new posts from Windows on Theory, particularly essays on AI safety and theoretical foundations
6. **Community building** — Promoting Addis Coder, Jam Coders, and other outreach initiatives to broaden participation in computer science
