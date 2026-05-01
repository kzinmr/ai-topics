---
title: "Chris of Entropic Thoughts"
tags: [person]
created: 2026-04-24
updated: 2026-04-24
type: entity
---

# Chris of Entropic Thoughts

**URL:** https://entropicthoughts.com (formerly two-wrongs.com)
**Blog:** Entropic Thoughts
**Newsletter:** Entropic Thoughts via Buttondown (free + premium tiers)
**Identity:** Chris, based in Stockholm, Sweden
**Themes:** Applied statistics, queueing theory, software delivery, systems thinking, SRE, Haskell, Emacs, forecasting
**Tech Stack:** Emacs + Org mode for authoring and publishing

## Overview

Chris is the author of **Entropic Thoughts**, a blog that applies rigorous quantitative thinking — statistics, queueing theory, information theory, and Bayesian reasoning — to software engineering, product development, and operations. He describes himself as a **quant, systems thinker, and anarchist** (clarifying: "strongly in favour of direct democracy, liberty, non-violence, and solidarity"). His professional background spans software engineering, site reliability engineering, management, and "undercover statistics."

The blog was originally called **Two Wrongs**, named after his first job where he "frequently saw two wrongs conspiring in commits." After years of writing about software delivery and systems thinking, he renamed it to **Entropic Thoughts**, reflecting the broader scope of the content. The canonical URL still redirects from two-wrongs.com — he explicitly keeps old links alive because "good webmasters don't kill links in the wild."

Entropic Thoughts stands out in the tech writing landscape for its **relentless mathematical rigor**. Where most engineering blogs offer opinions, Chris offers proofs, derivations, and empirical analyses. His posts on queueing theory, statistical process control, and the limitations of the Central Limit Theorem are genuinely educational — the kind of material that belongs in a textbook, published for free on a personal site.

His writing philosophy is distinctive:

> "I feel alive when I teach. My most eager and voracious student is myself, a few months or years older."

> "A big reason I publish my ideas is so other people can poke holes in them. I have never learned as much as when I've confidently believed something wrong in conversation with someone who knows better."

This intellectual humility — publishing to be corrected, not to be right — is the defining characteristic of the blog.

## Timeline

| Date | Event |
|------|-------|
| ~2014 | Blog launched as "Two Wrongs" — named after seeing bad practices at first job |
| 2016–2019 | Established pattern of deep technical writing on software delivery, statistics, and systems |
| 2020 | Renames blog to **Entropic Thoughts**; two-wrongs.com redirects to new domain |
| 2022 | Publishes "Tindall on Software Delays" — analysis of 1966 NASA memo; becomes one of the most-read posts |
| 2023 | Publishes "Response Time Is the System Talking" — queueing theory applied to production systems |
| 2023 | Publishes "Statistical Process Control: A Practitioner's Guide" — comprehensive SPC tutorial |
| 2023 | Publishes "It Takes Long to Become Gaussian" — critique of blind CLT application |
| 2024 | Publishes "Are LLMs not getting better?" — statistical analysis of code generation benchmarks |
| 2025 | Launches premium newsletter tier via Buttondown |
| 2025–2026 | Continues publishing on topics including Emacs, Haskell, ZFS, pathfinding algorithms, and forecasting |
| 2026 | Publishes "The MVC Mistake" — architectural critique |

## Core Ideas

### Statistical Process Control as a Universal Tool

Chris's **Statistical Process Control: A Practitioner's Guide** is arguably the most accessible and practical introduction to SPC ever published for a software audience. He identifies three "bad comparisons" that waste engineering time:

| Comparison Type | Why It Fails |
|---|---|
| **vs. Previous** | Week-to-week changes are usually just noise |
| **vs. Average** | Averages naturally sit in the middle — "excess over average" contains zero actionable information |
| **vs. Specification** | Often "wishful thinking" — budgets and goals aren't natural laws |

His method: build an **Individuals & Moving Range (XmR) chart** with exact natural process limits (using the constant 2.66 — "do not adjust it to fit management preferences"). The key insight:

> "You cannot judge the process by a single outcome. Only a long run of outcomes tell you anything about the process."

> "You cannot improve a stable system by tampering with individual outcomes. The only thing tampering accomplishes is destabilising the system."

This is Deming's philosophy applied to software delivery with mathematical precision. The "Report Card Effect" — aggregating too many physical processes into one summary metric — is called out as averaging away useful signals into noise.

### Response Time as a System Diagnostic

In **Response Time Is the System Talking**, Chris applies queueing theory to a practical problem: how do you know when a service is overloaded? The answer: **response time is a function of utilisation**.

He derives the formula:

$$R = 1 - \frac{W_{\mathrm{baseline}}}{W_{\mathrm{loaded}}}$$

And provides a concrete example: if baseline response time is 89ms and loaded response time is 327ms, utilisation is approximately 73% — too high for safe production operation. His recommendation: **aim for under 40% utilisation at all times**, or even 10% for systems with high demand variation.

The appendix provides a complete derivation from first principles of queueing theory, and the caveats section honestly addresses where the approximation breaks down (multi-server systems, heavy-tailed service times). This is the kind of post that turns a vague intuition ("it feels slow") into a quantifiable diagnostic.

### The Central Limit Theorem Converges Slowly (and People Don't Notice)

**It Takes Long to Become Gaussian** is a devastating critique of the blind application of the Central Limit Theorem to real-world data. Chris demonstrates that for heavy-tailed distributions — which dominate real-world systems — convergence to normality is painfully slow even at n=30:

| Scenario | CLT Predicted Risk | Actual Empirical Risk |
|---|---|---|
| 30 files > 16 MB | 0.8% | 4.8% (**6× underestimation**) |
| S&P 500 monthly drop > $1,000 | 0.9% | 1.9% (**2× underestimation**) |
| 30 Finnish lakes > 7,000 km² | 0.4% | 1.4% (**3.5× underestimation**) |

His solution: **use computational resampling instead of theoretical distribution fitting**. "We have computers now, and they are really good at performing the same operation over and over — exploit that." He also introduces **Cantelli's inequality** as a distribution-agnostic upper bound on tail probabilities, showing that "9-sigma" events dismissed as 1-in-100,000-years under Gaussian assumptions can theoretically occur ~4 times/year under absolute bounds.

### LLM Code Generation Hasn't Improved (Statistically)

In **Are LLMs not getting better?**, Chris performs a statistical analysis of the metr dataset comparing LLM code that "passes tests" vs. code that is "mergeable quality." Using leave-one-out cross-validation and Brier scores, he demonstrates:

| Model | Brier Score |
|---|---|
| Gentle upward slope | 0.0129 |
| Piecewise constant | 0.0117 |
| **Constant function** | **0.0100** (best) |

The constant function — predicting no improvement — beats both the linear trend and the step function. His conclusion:

> "This means LLMs have not improved in their programming abilities for over a year. Isn't that wild? Why is nobody talking about this?"

He acknowledges the possibility of a recent capability step but warns: "people made the same claim throughout 2025 as well, and as we see now, it wasn't true then. During 2025, the gap between buzz and actual performance was larger than we thought."

### Tindall's Leadership Framework

Chris's analysis of Bill Tindall's 1966 NASA memo on software delays extracts a **3+1 Leadership Framework**:
1. Trust the people doing the work
2. See the problem for yourself and accept reality
3. Attend to the big picture
4. (Implicit) Work with interactions and trade-offs

The insight that a **2% requirement reduction can save ~10% development time** by avoiding innovation overhead and interaction effects is highlighted as the most effective schedule recovery strategy. The core mantra: *"Don't negotiate reality. Understand it, simplify scope, accept trade-offs, and plan for system-wide interactions."*

### The MVC Mistake

In his most recent architectural post (March 2026), Chris critiques the Model-View-Controller pattern, arguing that the separation it enforces creates more problems than it solves — a position consistent with his general skepticism of abstractions that don't serve a clear operational purpose.

## Key Quotes

> "I feel alive when I teach. My most eager and voracious student is myself, a few months or years older."

> "A big reason I publish my ideas is so other people can poke holes in them."

> "Wishful thinking never improves anything, though it has potential to make things worse."

> "You cannot judge the process by a single outcome. Only a long run of outcomes tell you anything about the process."

> "Don't assume it is Gaussian just because it looks like it... The worse the tail events, the longer it will keep looking like a friendly bell curve."

> "This means LLMs have not improved in their programming abilities for over a year. Isn't that wild? Why is nobody talking about this?"

> "Assuming an inappropriate theoretical distribution shields your reasoning from reality."

> "Good webmasters don't kill links in the wild."

## Writing Style & Philosophy

Chris writes in a **pedagogical, proof-driven style**. Every claim is supported by derivation, empirical data, or explicit logical reasoning. His posts often include:

- Complete mathematical derivations (queueing theory, probability bounds)
- Code examples (Haskell, AWK, shell scripts)
- Concrete numerical examples that readers can replicate
- Honest caveats and limitations sections
- PGP-signed communications for authenticity

He uses Emacs + Org mode for writing and publishing, and has documented the "hacky" process of maintaining his own publishing pipeline. His willingness to say "I don't fully understand how Org publishing works" while still making it work is characteristic of his pragmatic engineering philosophy.

The blog's **premium newsletter** tier offers additional content: forecasting rationales, book reviews, pathfinding tutorials, and ZFS operational notes. This reflects his belief that readers who find value in the free content should have the option to support it financially.

## Technical Breadth

Chris's interests span an unusually wide range:

- **Statistics & Probability**: Bayesian reasoning, queueing theory, statistical process control, forecasting, Cantelli/Chebyshev inequalities
- **Software Engineering**: SRE, software delivery, build vs. buy analysis, handoff waste, toil reduction
- **Programming Languages**: Haskell (Esqueleto, optimized code), AWK (state machine parsers), Emacs Lisp
- **Infrastructure**: ZFS mirroring, multi-criteria pathfinding algorithms
- **Forecasting**: Metaculus participation, ACX prediction contests, options pricing
- **Systems**: Response time analysis, capacity planning, system utilisation monitoring

## Recent Themes (2024–2026)

- **LLM evaluation**: Rigorous statistical analysis of code generation benchmarks, resisting hype narratives
- **Queueing theory in practice**: Making operations research accessible to software engineers
- **Emacs tooling**: Magit workflows, Org mode publishing, personal knowledge management
- **Haskell**: Esqueleto tutorials, performance comparisons with C, functional programming in production
- **Forecasting**: ACX prediction contests, Metaculus, probabilistic reasoning
- **Systems operations**: ZFS, pathfinding algorithms, capacity management
- **Architectural critique**: MVC patterns, abstraction costs, complexity vs. simplicity trade-offs

## Related

- [[concepts/statistical-process-control]] — XmR charts, natural process limits, signal vs. noise
- [[concepts/queueing-theory]] — Response time as utilisation diagnostic
- [[concepts/bayesian-reasoning]] — Odds-form Bayes' rule, forecasting
- [[concepts/software-delivery]] — Tindall framework, handoff waste, toil
- [[concepts/haskell]] — Functional programming, Esqueleto, performance
-  — Org mode publishing, Magit, personal workflow
-  — Statistical analysis of code generation benchmarks-  — CLT limitations, Cantelli bounds

## Influence

- "Tindall on Software Delays" and "It Takes Long to Become Gaussian" are among his most-viewed articles
- "Statistical Process Control: A Practitioner's Guide" is cited as essential reading for SRE practitioners
- His LLM analysis posts challenge prevailing narratives with data-driven counterarguments
- The blog maintains a dedicated readership via its Buttondown newsletter with premium tier
- His approach to publishing — rigorous, self-correcting, mathematically grounded — stands in contrast to the opinion-driven tech blogosphere

## Sources

- entropicthoughts.com — Primary blog, active since ~2014
- entropicthoughts.com/about — Author biography and philosophy
- "Statistical Process Control: A Practitioner's Guide"
- "Response Time Is the System Talking"
- "It Takes Long to Become Gaussian"
- "Are LLMs not getting better?"
- "Tindall on Software Delays"
- "The MVC Mistake" (March 2026)
- "Long Hiatus: Emacs Upgrades"
- Buttondown newsletter: Entropic Thoughts

## References

- entropicthoughts.com--understanding-systems--149e6399
