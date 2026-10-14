---
title: 'Part II: Building Secure and Reliable Systems'
source_url: https://raw.githubusercontent.com/google/building-secure-and-reliable-systems/2a2ae3e0d4dbd288f9862ed47194f5b1b1ed7c3c/raw/part2.html
license: CC-BY-4.0
license_url: https://creativecommons.org/licenses/by/4.0/
attribution: Heather Adkins, Betsy Beyer, Paul Blankinship, Piotr Lewandowski, Ana
  Oprea, Adam Stubblefield; Google; O’Reilly, 2020
source_revision: 2a2ae3e0d4dbd288f9862ed47194f5b1b1ed7c3c
original_html: original-source.zip!/raw/part2.html
original_sha256: fff03f207365dccf766de8a23c31e2c8cbd060cf0c33458fe4eb0e33bfbcfdf9
created: '2026-10-14'
updated: '2026-10-14'
type: summary
tags:
- reliability
- security
- documentation
sources:
- https://raw.githubusercontent.com/google/building-secure-and-reliable-systems/2a2ae3e0d4dbd288f9862ed47194f5b1b1ed7c3c/raw/part2.html
ingested: '2026-10-14'
sha256: f9074df7c4e09d946b3b4c2914e9b79aa13c7c31e586984999e9a3a8830f0642
content_kind: mechanical_text_extraction
transformation: HTML to plain text in Markdown container; source order retained; no
  translation or abridgment
---
Part II
Designing Systems
Part II
focuses on the most cost-effective way to implement security and reliability requirements: as early as possible in the software development lifecycle, when designing systems.
Although product design should ideally incorporate security and reliability from the start, much of the security- and reliability-related functionality you’ll develop will likely be added to an existing product.
Chapter 3
provides an example of how we’ve made already-operating systems at Google safer and less prone to outages. You can retrofit your systems with many similar enhancements, and they will be much more effective when paired with some of the design principles that follow.
Chapter 4
considers the natural tendency to defer dealing with security and reliability concerns at the expense of sustained velocity. We argue that functional and nonfunctional requirements don’t necessarily need to be at odds.
If you’re wondering where to begin integrating security and reliability principles into your systems,
Chapter 5
—which discusses how to evaluate access based upon risk—is an excellent place to start.
Chapter 6
then looks at how you can analyze and understand your systems through invariants and mental models. In particular, the chapter recommends using a layered system architecture built on standardized frameworks for identity, authorization, and access control.
To respond to a shifting risk landscape, you need to be able to change your infrastructure frequently and quickly while also maintaining a highly reliable service.
Chapter 7
presents practices that let you adapt to short-, medium-, and long-term changes, as well as unexpected complications that might arise as you run a service.
The guidelines mentioned thus far will have limited benefits if a system cannot withstand a major malfunction or disruption.
Chapter 8
discusses strategies for keeping a system running during an incident, perhaps in a degraded mode.
Chapter 9
approaches systems from the perspective of fixing them after breakage. Finally,
Chapter 10
presents one scenario in which reliability and security intersect, and illustrates some cost-effective mitigation techniques for DoS attacks at each layer of the service stack.
