---
title: "OpenAI: Working with academic communities to build scientific understanding"
url: "https://openai.com/index/building-scientific-understanding-with-academic-communities/"
fetched_at: 2026-10-27T11:00:00+00:00
source: "openai.com"
date: 2026-10-26
tags: [blog, raw]
---

# OpenAI: Working with academic communities to build scientific understanding

Source: https://openai.com/index/building-scientific-understanding-with-academic-communities/

Title: Working with academic communities to build scientific understanding

URL Source: https://openai.com/index/building-scientific-understanding-with-academic-communities/

Markdown Content:
We are announcing three new discoveries in mathematics, computer science, and physics about harmonic analysis, complexity theory, and quantum field theory.

Our release process continues to evolve in response to feedback from the associated academic communities. In our view, these manuscripts are best understood as a form of raw research data. To convert this raw research data into scientific understanding, in this release we are experimenting with a new approach. We reached out to external experts and asked them to act as shepherds, organizing groups to understand the new results. They advised three different release strategies:

*   For the math result, release the AI output, leaving researchers free to organize their own efforts to explain the result.

*   For the computer science result, form an external group of collaborators to explain the result, while making the AI output publicly available for anyone to examine and build on.

*   For the physics result, form an external group of collaborators and defer to them on the release of materials.

We do not yet know which of these three approaches will be most useful, and we welcome feedback on what works and what we can improve.

The external collaborations will follow four principles:

1.   **Transparency.** We are transparent about the existence of our collaborations. Participants will not be asked to sign nondisclosure agreements and will be free to discuss the work, share intermediate products, and publish their conclusions.

2.   **No Academic Credit.** We do not seek academic credit for the discoveries produced by our internal models. Inviting a researcher to help steward a collaboration also does not imply that they or their working group made the original discovery.

3.   **Recognition.**This group should receive recognition for the understanding they develop, the writeups they author, and the other materials they create. The group will also help ensure that the work appropriately credits researchers, techniques, and ideas that it draws on.

4.   **Independence.**Participation is voluntary and unpaid. Working-group members participate independently, and their conclusions are their own. They do not speak on behalf of OpenAI, and OpenAI does not speak on their behalf.

We will turn over materials and artifacts related to these results to the collaborations. For the computer science collaboration, the group has decided to make the natural language proof and Lean formalization public immediately, and we are publishing them directly to our GitHub repository. For the physics collaboration, the group has decided to hold off on releasing the AI-produced artifacts and instead work on writing it up themselves.

All of these approaches involve tradeoffs. On the one hand, the collaborations empower experts to foster unpacking the results and contextualizing them in the broader academic community. On the other hand, choosing initial shepherds necessarily shapes who gets involved first and creates asymmetry of information. We welcome feedback on how to broaden participation and make this process more useful.

## Local smoothing and the Kakeya conjecture

The result in mathematics concerns harmonic analysis. In 1991, Sogge proposed the local smoothing conjecture, which concerns the behavior of waves as they become focused. In particular, the conjecture states that the most extreme focusing must be short-lived. The amount of focusing at a typical random time is always much smaller than what can happen at the worst-case time. This is a familiar pattern throughout mathematics: what can happen in the worst case is more extreme than what is observed after averaging. Because of how fundamental this conjectured phenomenon is, it also has wide ranging implications throughout mathematical analysis. For instance, it implies the Kakeya conjecture and Stein’s restriction conjecture.

In 2019, [Guth, Wang, and Zhang⁠(opens in a new window)](https://annals.math.princeton.edu/2020/192-2/p06) proved the local smoothing conjecture in two spatial dimensions. In 2025, [Wang and Zahl⁠(opens in a new window)](https://www.ias.edu/news/once-century-proof-settles-maths-kakeya-conjecture) proved the Kakeya conjecture in three dimensions. Our models produced a proof of the local smoothing conjecture in every dimension and therefore also resolve the Kakeya conjecture and Stein’s restriction conjecture in all dimensions. The new proof is based on a novel auxiliary partial differential equation.

We obtained our AI output on October 18th, 2026, which was formalized in Lean the following day, and then we reached out to an expert to discuss forming a collaboration around this result. Following their recommendation, we decided to release the AI output publicly, following the same strategy for this result as our October 6th, 2026 [release⁠](https://openai.com/index/sharing-ai-progress-in-mathematics/). We have released both an [AI natural language output writeup⁠(opens in a new window)](https://github.com/openai/math/blob/main/preprints/Local-smoothing-for-the-Euclidean-wave-equation-October-25-2026/paper.pdf) produced by our models and a[Lean proof ⁠(opens in a new window)](https://github.com/openai/math/blob/main/lean/docs/079.md)in our public GitHub repository.

## The Exponential Time Hypothesis is false

The computer science collaboration will understand and explain a result concerning the Exponential Time Hypothesis (ETH), a longstanding conjecture about the computational complexity of Boolean formula satisfiability, a problem deeply related to the P vs. NP problem. The ETH has been widely believed to be true, and has been used in hundreds of papers to derive conditional computational hardness results across a wide variety of fields including graph theory, computational biology, databases, computational geometry, and more. Surprisingly, our system has recently proved that the ETH is false, a result that was subsequently verified in Lean. The refutation of the ETH reopens questions about how much faster these tasks could become, and may help guide the search for better algorithms. Finding such algorithms, and turning theoretical advances into practical improvements, will require significant further research.

This work will be verified and shepherded by a group led by Russell Impagliazzo (UC San Diego), Ramamohan Paturi (UC San Diego), and Ryan Williams (MIT). All three are experts in algorithm design and complexity theory.

We have agreed to the group’s requests that all raw data of the results be made public to facilitate independent verification by the community, and that OpenAI commit to funding a conference to understand the implications of this work on the field as a whole. The group invites the community to help organize an open examination of the ETH claim and to discuss the broader questions that AI-generated breakthroughs raise about verification, access, credit, and the future of research.

Our AI found its natural language disproof for the ETH on October 16th, 2026 and then subsequently we formalized the result in Lean on October 17th, 2026, which led us to develop the collaboration described here. To that end, we have released both an [AI natural language output writeup⁠(opens in a new window)](https://github.com/openai/math/blob/main/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/paper.pdf) produced by our models and a [Lean proof ⁠(opens in a new window)](https://github.com/openai/math/blob/main/lean/docs/378.md)in our public GitHub repository.

Computational complexity has many open questions and conjectures, whose proofs or refutations have so far eluded the best efforts of scientists. We hope that humans with AI can provide new understanding in this field, and shed light on the inherent capabilities and limits of efficient computation.

## Existence of quantum chromodynamics and completions of the Standard Model

The physics collaboration will understand and explain a result that gives a mathematically rigorous existence proof of certain interacting quantum field theories containing gauge fields and fermions in four dimensions, including Quantum Chromodynamics (QCD) and a unified completion of the Standard Model of particle physics. Our work builds on [Balaban’s approach⁠(opens in a new window)](https://www.worldscientific.com/doi/abs/10.1142/S0129055X13300100) in constructive quantum field theory. As a subproblem, this work also includes a proof of the existence of pure Yang–Mills theory, which is part of the [Quantum Yang–Mills Theory Clay Mathematics Institute Millennium Prize problem⁠(opens in a new window)](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf).

The Standard Model describes the interaction of fundamental subatomic particles for three of the four fundamental forces, excepting gravity. The existence proof pertains to the simplest grand unified theory that includes the gauge fields and fermions of the Standard Model (as the Standard Model itself cannot be extrapolated to arbitrarily short distances). QCD describes the interaction of particles such as quarks and gluons via the strong force. Pure Yang–Mills theory only describes the self-interactions of the gluons, the force carriers, rather than matter such as quarks.

David Gross will lead a group including Michael Douglas, Arthur Jaffe, Igor Klebanov, and Nikita Nekrasov that will shepherd this work.

*   Gross’s 1973 work on asymptotic freedom in Yang-Mills theories helped establish QCD as the theory of the strong interactions and earned him a share of the [2004 Nobel Prize in Physics⁠(opens in a new window)](https://www.nobelprize.org/prizes/physics/2004/gross/facts/). Asymptotic freedom is also the key mechanism underlying the existence of these theories as mathematically rigorous objects.

*   Jaffe formulated the [Quantum Yang-Mills Theory Millenium Prize problem⁠(opens in a new window)](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf) with Witten and also envisioned the idea of Millennium Prize problems and co-founded the Clay Mathematics Institute.

*   Douglas has already been a steward of this problem over the last 20 years, [reporting on its status in 2004⁠(opens in a new window)](https://www.claymath.org/library/annual_report/douglas_quantum_yang_mills.pdf) and then providing a [comprehensive update on the progress⁠(opens in a new window)](https://www.nature.com/articles/s42254-025-00909-2) at the beginning of this year.

*   Klebanov helped pioneer the application of gauge–string duality to confinement, an important property of QCD, and now directs the [Simons Collaboration on Confinement and QCD Strings⁠(opens in a new window)](https://simonsconfinementcollaboration.org/),

*   Nekrasov has done groundbreaking work on exact methods for generalizations of Yang–Mills theory and won the Dannie Heineman Prize for Mathematical Physics in 2023.

The group requests that all communications with any and all members of the group regarding this effort be directed to the following email account: YANGMILLS4D@gmail.com.

Our models produced a natural language proof for Yang–Mills existence on September 9th, 2026, and then subsequently produced a proof for QCD on September 18th, 2026. Given the length and complexity of the work, we postponed release until the Lean formalization completed. We finished our formalization of Yang–Mills’ existence on October 16th, 2026, which led us to develop the collaboration described here.

We hope that these results mark the beginning of a transition in which quantum field theory, the most important framework in modern theoretical physics, becomes a mathematically rigorous field. We are excited to provide resources for academic-led progress towards that goal.

## Supporting scientists

We are committed to supporting the broader work of understanding and building on these results. These collaborations complement our recently announced [$5 million contribution⁠(opens in a new window)](https://www.simonsfoundation.org/news/simons-foundation-launches-15m-effort-to-help-mathematicians-navigate-ai-era/) to the Simons Foundation. Managed and awarded by the Simons Foundation, that funding will support workshops, conferences, and special programs to help researchers understand and build on results produced by AI. We are committed to ensuring funding for researchers to independently examine, explain, and build on the results above.

We continue to invite feedback on the best way to disclose results and engage with scientists to accelerate discovery.
