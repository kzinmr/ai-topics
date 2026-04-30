---
title: John D. Cook
type: entity
created: 2026-04-09
updated: 2026-04-19
tags:
- person
- blogger
- hn-popular
- applied-mathematics
- statistics
- ai-reliability
- formal-methods
- data-privacy
aliases:
- johndcook.com
- john-d-cook-applied-mathematics-consulting
sources: []
---

# John D. Cook

| | |
|---|---|
| **Blog** | [johndcook.com/blog](https://www.johndcook.com/blog) |
| **RSS** | https://www.johndcook.com/blog/feed/ |
| **Consulting** | [johndcook.com](https://www.johndcook.com) |
| **X/Twitter** | [@JohnDCook](https://x.com/JohnDCook) |
| **Role** | Consultant in applied mathematics, statistics, and data privacy |
| **Known for** | Deep mathematical blogging, AI reliability analysis, formal methods, HIPAA-compliant AI consulting |
| **Bio** | PhD in applied mathematics (UT Austin), postdoc at Vanderbilt (nonlinear PDEs). Former software development manager and research statistician at MD Anderson Cancer Center (Bayesian statistics, clinical trials, numerical algorithms). Now runs an independent consulting practice serving clients including Amazon, Google, Microsoft, and Amgen. Lives in Houston with wife and four children. |

## Core Ideas

John D. Cook is a **mathematical generalist-practitioner** who bridges the gap between pure mathematics and real-world computation. His blog — updated almost daily with short, dense posts on mathematics, statistics, computing, and AI — represents a rare voice: a professional mathematician who writes for practitioners, engineers, and technically curious generalists. His consulting work sits at the intersection of **applied mathematics, data privacy (HIPAA expert determination), and AI reliability** — precisely where theoretical rigor meets high-stakes decision-making.

### The AI Odyssey: A Mathematician's Framework for AI Reliability

Cook's "An AI Odyssey" series (2026) is arguably the most intellectually rigorous analysis of AI reliability from a working applied mathematician. The trilogy examines agentic AI through three lenses:

**Part 1: Correctness Conundrum** — Cook frames the fundamental problem: AI systems lack the procedural reliability guarantees expected in high-stakes engineering domains. He draws a powerful contrast with **Six Sigma manufacturing** and **formal verification** in computing. The Pentium FDIV bug serves as his key historical analogy — even "rare" errors cause real failures in mission-critical systems, but at least the FDIV error modes were *precisely definable*. AI models are **probabilistic**, making error bounds fundamentally harder.

> *"Anyone who has worked with AI models understands that there is a basic unpredictability to them, that in a purely technical way we have not solved."*

His central prescription: until AI reliability is resolved, these tools must be used in **constrained ways that do not create unnecessary risks** — particularly for financial data, healthcare, and safety-critical applications.

**Part 2: Prompting Peril** — Examines the fragility of prompt-based interfaces and the illusion of control. Small prompt variations produce wildly different outputs, undermining reproducibility.

**Part 3: Lost Needle in the Haystack** — A seemingly mundane observation with deep implications: a RAG-based AI shopping assistant failed to answer a simple product question that a keyword search across reviews answered immediately. Cook's insight: *"Models are capable, but effective integration can be lacking."* The problem isn't the model — it's the **architecture of retrieval and composition**.

Cook's AI analysis is distinctive because it comes from someone who **builds mathematical models for a living**. He doesn't theorize about AI from the outside; he evaluates it against the standards he applies to clinical trial design, numerical algorithm verification, and data privacy compliance.

### Mathematics as a Way of Thinking

Cook's blog posts reveal a mind that finds **unexpected connections** across mathematical domains. Recent posts demonstrate this range:

- **Mendeleev to Markov to Fourier** — Tracing how Dmitri Mendeleev's empirical study of specific gravity led to a polynomial derivative inequality, which Andrey Markov generalized, and which connects to Bernstein's theorem on trigonometric polynomials (derivative bound drops from n² to n)
- **Lebesgue constants and interpolation** — Showing that blindly increasing interpolation order amplifies rounding error exponentially for evenly spaced nodes (λ grows from 155 at order 11 to 10,995,642 at order 29), while Chebyshev spacing keeps λ near 3
- **Binet's formula and certified computation** — Computing Fibonacci numbers via floating-point approximation, then verifying correctness through integer arithmetic certificates (5f² ± 4 must be a perfect square)
- **Gamma function characterizations** — Contrasting Bohr-Mollerup (real axis, log-convexity) with Wielandt (complex plane, boundedness on a strip)

The pattern is consistent: Cook identifies a **practical computational problem**, finds the **elegant mathematical structure** underlying it, and delivers **actionable numerical guidance** — often with code.

### Formal Methods and the Economics of Certainty

Cook's post *"How Much Certainty Is Worthwhile?"* (March 2026) is a nuanced treatment of a question most practitioners avoid: **how much verification is enough?**

His key insight: formally verified systems contain bugs because there's inevitably a gap between what's formally verified and what isn't. He could verify trigonometric identities in Lean, then introduce transcription errors typing LaTeX. The lesson: *"The appropriate degree of testing or formal verification depends on the context."* Software controlling a pacemaker needs more assurance than a blog post diagram.

This **economic view of correctness** — matching verification effort to stakes — reflects his consulting practice. He doesn't advocate for maximum rigor everywhere; he advocates for **proportionate rigor** calibrated to consequences.

### Data Privacy: The HIPAA Expert Determination Niche

Cook's consulting includes **HIPAA expert determination** and **differential privacy** — areas where his statistical expertise meets regulatory compliance. His April 2026 post on HIPAA-compliant AI reveals the institutional complexity that most AI coverage ignores:

- Cloud AI services are "HIPAA eligible," not "HIPAA compliant" — requiring BAAs, configuration, logging, access controls, and internal processes
- OpenAI's consumer ChatGPT Health product explicitly states that HIPAA and BAAs do not apply
- Anthropic's BAA covers only specific "HIPAA-ready" services, excluding Claude Free, Pro, Max, Team, and Claude Code
- Running AI locally on consumer hardware (70B-parameter models on a single high-end GPU or recent Mac) is already practical and may be **the most compliant path for small organizations**

The diseconomies of scale insight is striking: cloud providers achieve lower per-server costs, but HIPAA-compliant cloud AI incurs large bureaucratic overhead. **Smaller companies may benefit more from local AI than larger ones** for compliance-critical workloads.

### The Polymath Blogger

Cook's blog posts span an extraordinary range: number theory (Andrica's conjecture on prime gaps), celestial mechanics (Artemis I's retrograde lunar orbit, Apollo 12's third-stage chaotic trajectory), music theory (twelve-tone composition, tone row operations, Langford series), cryptography (quantum Y2K, OpenSSH hybrid encryption), and computer science (Toffoli gates as universal reversible computing, Z3 SAT/SMT solver optimization).

The common thread is **curiosity-driven mathematical exploration**. He finds something interesting, works through the math, and shares the result — usually with a practical computation angle. This makes his blog uniquely valuable: it's a working notebook of a mathematician who thinks in code.

## Key Quotes

> *"Models are capable, but effective integration can be lacking. Without improvements for cases like this, customers will not be satisfied users of these new AI tools."*

> *"It is not good usability when multiple search mechanisms exist but only one of them is reliable."*

> *"The appropriate degree of testing or formal verification depends on the context."*

> *"There's an interesting interplay between economies of scale and diseconomies of scale."* — on HIPAA-compliant AI

> *"Richard Feynman said that almost everything becomes interesting if you look into it deeply enough."*

## Related

- [[concepts/formal-methods]] — Proving correctness properties for critical systems
-  — The correctness conundrum in AI systems
-  — HIPAA expert determination and differential privacy
-  — Mathematician whose work intersects with Cook's analysis of AI-assisted discovery

## Sources

- [An AI Odyssey, Part 1: Correctness Conundrum](https://www.johndcook.com/blog/2026/03/02/an-ai-odyssey-part-1-correctness-conundrum/) (Mar 2026)
- [An AI Odyssey, Part 3: Lost Needle in the Haystack](https://www.johndcook.com/blog/2026/03/27/an-ai-odyssey-part-3-lost-needle-in-the-haystack/) (Mar 2026)
- [HIPAA Compliant AI](https://www.johndcook.com/blog/2026/04/05/hipaa-compliant-ai/) (Apr 2026)
- [How Much Certainty Is Worthwhile?](https://www.johndcook.com/blog/2026/03/08/how-much-certainty-is-worthwhile/) (Mar 2026)
- [GPT-5 for AI-Assisted Discovery](https://www.johndcook.com/blog/2025/10/10/gpt-5-for-ai-assisted-discovery/) (Oct 2025)
- [johndcook.com/about](https://www.johndcook.com/blog/about/)
- [Gaussian distributed weights for LLMs: NF4 and QLoRA](https://www.johndcook.com/blog/2026/04/18/qlora/) (Apr 2026) — NF4量子化形式はなぜFP4よりLLMの重み分布に適しているかを数学的に分析。QLoRAの非対称量子化がなぜ正確に0を表現できないか、bitsandbytesのα=929/960という設定の由来等问题を追究。

## References

- johndcook.com--blog-2026-03-26-lebesgue-constants--8cd1ea58
- johndcook.com--blog-2026-03-27-an-ai-odyssey-part-3-lost-needle-in-the-hays--47c13835
- johndcook.com--blog-2026-03-27-complex-argument--05a170b3
- johndcook.com--blog-2026-03-31-morse-code-tree--b013ee37
- johndcook.com--blog-2026-03-31-quantum-y2k--5f042224
- johndcook.com--blog-2026-04-01-truncated-triangular-numbers--a9e81223
- johndcook.com--blog-2026-04-02-artemis-apollo--1cd20011
- johndcook.com--blog-2026-04-02-hyperbolic-napier-mnemonic--e623171b
- johndcook.com--blog-2026-04-03-roman-moon-greek-moon--26cebda6
- johndcook.com--blog-2026-04-04-kalman-bayes--8e9eaf78
- johndcook.com--blog-2026-04-05-hipaa-compliant-ai--fc6185f9
- johndcook.com--blog-2026-04-06-tofolli-gates--a34baf8a
- johndcook.com--blog-2026-04-08-andrica--48408185
- johndcook.com--blog-2026-04-08-artemis-1-apollo-12--6b49defd
- johndcook.com--blog-2026-04-09-pyramid-speed-of-light--f08cc138
- johndcook.com--blog-2026-04-09-random-hexagon-fractal--707b68c7
- johndcook.com--blog-2026-04-10-fraction-digits--841bfad8
- johndcook.com--blog-2026-04-12-lunations--7f568bdc
- johndcook.com--blog-2026-04-12-orthodox-western-easter--c88c219b
- johndcook.com--blog-2026-04-13-the-smallest-math-library--eaef31b8
- johndcook.com--blog-2026-04-14-artz-parabola--235220bb
- johndcook.com--blog-2026-04-14-intersecting-spheres-and-gps--0b6e3b99
- johndcook.com--blog-2026-04-16-newton-diameters--ac1ff698
- johndcook.com--blog-2026-04-17-fp4--64365c7c
- johndcook.com--blog-2026-04-18-qlora--d229eb2a
- johndcook.com--blog-2026-04-20-newton-diameter-quintic--213f80cc
- johndcook.com--blog-2026-04-21-an-ai-odyssey-part-4-astounding-coding-agent--85a4b5af
- johndcook.com--blog-2026-04-23-solve-a-right-triangle--db90ef19
- johndcook.com--blog-2026-04-23-solve-an-oblique-triangle--26f8f89a
- johndcook.com--blog-2026-04-24-nonlinear-pendulum--c358c47b
- johndcook.com--blog-2026-04-25-exact-solution-nonlinear-pendulum--82a86f77
- johndcook.com--blog-2026-04-25-nth-derivative-of-a-quotient--1ec0ba72
- johndcook.com--blog-2026-04-28-circular-arc-approximation--73d10e2a
- johndcook.com--blog-2026-04-28-even-series-trick--74cb4171
