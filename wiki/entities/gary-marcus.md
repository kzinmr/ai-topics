---
title: "Gary Marcus"
created: 2026-04-09
updated: 2026-04-13
tags: [person, blogger, ai-skeptic, neurosymbolic, cognitive-science, hn-popular]
aliases: ["garymarcus.substack.com", "marcus-on-ai"]
---

# Gary Marcus

| | |
|---|---|
| **Blog** | [Marcus on AI](https://garymarcus.substack.com) |
| **RSS** | https://garymarcus.substack.com/feed |
| **X/Twitter** | [@GaryMarcus](https://x.com/GaryMarcus) |
| **Role** | Professor Emeritus of Psychology and Neural Science, NYU; cognitive scientist; author |
| **Known for** | Critiquing pure deep learning approaches to AI; advocating neurosymbolic AI; books *The Algebraic Mind*, *Rebooting AI*, *Taming Silicon Valley* |
| **Bio** | Cognitive scientist and AI researcher who has studied neural networks for 30+ years. One of the most prominent public critics of current AI approaches, arguing that scaling alone won't produce AGI. Testified before US Senate in 2023 alongside Sam Altman. Advocates for AI regulation and corporate accountability. |

## Core Ideas

Gary Marcus is the **preeminent academic critic of scaling-only AI**. For over three decades, he has argued that neural networks — while powerful pattern recognizers — are constitutionally incapable of causal reasoning, abstraction, and reliable truth-tracking. His position has evolved from a fringe critique (widely ridiculed by AI establishment figures) to a vindicated mainstream view as leading labs themselves adopt hybrid architectures.

### The Neurosymbolic Thesis

Marcus's career-long argument: intelligence requires **two complementary systems** working together:

- **Neural networks** (System I): fast, intuitive pattern recognition from examples. Good at perception, fuzzy matching, and generating fluent output.
- **Symbolic reasoning** (System II): rule-based logic, abstraction, causal chains. Good at planning, verification, and truth-tracking.

Neither alone is sufficient. Neural networks hallucinate because they lack truth-grounding. Symbolic systems are brittle without learned intuition. The path to reliable AI is combining both — what Marcus calls **neurosymbolic AI**, analogous to Kahneman's dual-process theory of human cognition.

> *"The essential premise of neurosymbolic AI is this: the two most common approaches to AI, neural networks and classical symbolic AI, have complementary strengths and weaknesses. Neural networks are good at learning but weak at generalization; symbolic systems are good at generalization, but not at learning."*

### "Deep Learning Is Hitting a Wall"

His widely-ridiculed 2022 essay predicted exactly what unfolded: pure scaling of LLMs would hit **diminishing returns**, requiring new architectures and techniques. Key predictions vindicated:

1. **Scaling laws are empirical, not physical** — adding compute/data won't yield AGI without architectural changes
2. **Test-time compute** (extended reasoning) became the new paradigm, validating that pure pretraining was insufficient
3. **Neurosymbolic integration** — DeepSeek R1, OpenAI o1/o3 all adopted rule-based reward systems and code interpreters
4. **Market commoditization** — LLMs became a price war with no lasting moats

The paper was mocked by Sam Altman, Greg Brockman, Yann LeCun, and Elon Musk. By 2025, the industry had tacitly adopted every major point.

> *"Deep Learning is Hitting a Wall didn't anticipate how well a system like Deep Research might work, but in most other respects... the paper was bang on. The ridicule, on the other hand, was deeply misplaced, and emblematic of a new regime in which oligarchs try to impose their beliefs on a science, moving markets but not actually solving the underlying research challenges."*

### The Interpolation vs. Extrapolation Problem

Marcus identified that neural networks fundamentally operate at the **extensional** level (memorizing and interpolating between examples) but fail at the **intentional** level (abstract understanding of concepts). This explains persistent LLM failures:

- **Hallucinations** — fluent but unfounded outputs, because the model has no concept of truth
- **Reasoning failures** — can't reliably solve novel problems outside training distribution
- **Instruction following** — "don't lie" is an abstract principle, not a pattern to match
- **River-crossing puzzles** — can't maintain stable representations of objects and their relationships

> *"Neural networks basically work at the extensional level, but they don't work at the intentional level. They are not getting the abstract meaning."*

### AI Governance & Corporate Accountability

In *Taming Silicon Valley* (2024, MIT Press), Marcus identifies four systemic failures:

1. **AI Oligarchy** — concentrated power in Big Tech, captured regulation, democratic deficit
2. **Overhyped capabilities** — companies promise future AGI to extract indulgences (copyright exemptions, regulatory forbearance) while delivering flawed products
3. **Responsible AI theater** — lip service to safety without structural accountability
4. **Generative AI's inherent unreliability** — the technology's fundamental architecture prevents truth-grounded outputs

His solutions: data rights legislation, layered independent oversight, meaningful tax reform (incentivize trustworthy AI over raw capability racing), government research investment in alternative architectures, and citizen boycotts of companies that train on copyrighted work without consent.

> *"We aren't passive passengers on this train. The desire to do good decreases with time, in the eternal quest for growth."*

### The Sociology of Scientific Monocultures

A recurring theme: the AI field became an **intellectual monoculture** dominated by connectionist approaches. Alternative research (symbolic AI, neurosymbolic hybrids, innate constraints) was starved of funding and dismissed by a handful of dominant figures (Hinton, LeCun, Sutton). Marcus views this as a failure of scientific diversity, not just technical disagreement.

The vindication came gradually: LeCun acknowledged LLM limitations by late 2022. Demis Hassabis pursued neurosymbolic architectures at DeepMind (AlphaGeometry, AlphaProof). Rich Sutton — the "patron saint of scaling" — conceded the need for world models beyond pure prediction.

> *"When the LLM crowd has lost Sutton — and when Sutton sounds exactly like me — it's game over."*

## Key Quotes

> *"Machine learning... is an amazing field that has changed the world — and will continue doing so. But it is also filled with closed-minded egotists with too much money, and too much power."*

> *"What we have now is a mess, seductive but unreliable. And too few people are willing to admit that dirty truth."*

> *"As with all LLM output, all of these things are presented in the same fluid, confident-sounding style: you have to know the material already to realize when your foot has gone through what was earlier solid flooring. That, to me, is one of their most pernicious features."*

> *"Don't focus on replacing humans. Focus on how you can use AI to help the ones you've got."* — on AI adoption strategy for employers

> *"The field of AI is making a mistake, sacrificing long-term benefit for short-term gain... everybody goes for the trout while they are plentiful, and suddenly there are no trout left at all."* — on the tragedy of the commons in AI development

> *"If some future OpenAI model could enable a massive bioweapon or cyberattack, would you really want [any CEO] deciding, unilaterally, whether or not it is ok to release the model?"*

## Related

- [[concepts/neurosymbolic-ai]] — Marcus's proposed hybrid architecture combining neural networks with symbolic reasoning
- [[concepts/scaling-without-slop]] — related critique of pure scaling approaches
- [[concepts/project-glasswing]] — Anthropic's cybersecurity initiative Marcus has analyzed critically
- [[entities/mitchellh-com]] — also expresses concerns about AI skill formation for junior developers
- [[entities/anthropic]] — company whose models and practices Marcus frequently analyzes

## Sources

- [Marcus on AI (Substack)](https://garymarcus.substack.com)
- [How o3 and Grok 4 Accidentally Vindicated Neurosymbolic AI](https://garymarcus.substack.com/p/how-o3-and-grok-4-accidentally-vindicated)
- [Game Over for Pure LLMs](https://garymarcus.substack.com/p/game-over-for-pure-llms-even-turing) (Sep 2025)
- [Five Ways DeepSeek Era Vindicated "Deep Learning Is Hitting a Wall"](https://garymarcus.substack.com/p/five-ways-in-which-the-last-3-months) (Feb 2025)
- [Taming Silicon Valley](https://mitpress.mit.edu/9780262381567/taming-silicon-valley/) (MIT Press, 2024)
- [Not on the Best Path — CACM Interview](https://cacm.acm.org/opinion/not-on-the-best-path/) (Feb 2025)
- [On Employment, Don't Panic — Yet](https://garymarcus.substack.com/p/on-employment-dont-panic-yet) (Apr 2026)
- [Sam Altman, Unconstrained by the Truth](https://garymarcus.substack.com/p/sam-altman-unconstrained-by-the-truth) (Apr 2026)
- https://garymarcus.substack.com/p/even-more-good-news-for-the-future (Apr 2026) — Apple + Tufts research: neurosymbolic models achieve 95% vs VLA 34% on 3-block Tower of Hanoi
- https://garymarcus.substack.com/p/the-biggest-advance-in-ai-since-the (Apr 2026) — argues Claude Code is neurosymbolic AI, not pure scaling
