---
title: "Introducing AlphaProof Code: a breakthrough in verifying complex software at depth"
source: https://deepmind.google/blog/introducing-alphaproof-code/
author: Pushmeet Kohli and Swarat Chaudhuri (Google DeepMind)
published: 2026-11-10
ingested: 2026-11-11
type: vendor-blog
hn: https://news.ycombinator.com/item?id=50439193
sha256: 1e70180ed910ddc1a0175a7e91ec79afff6f3896c7eafac53bbbfa70b491f7fc
---

Introducing AlphaProof Code: a breakthrough in verifying complex software at depth

November 10, 2026 — Research. Pushmeet Kohli and Swarat Chaudhuri.

Today, we're sharing a milestone in software security long considered to be a grand challenge: Google DeepMind researchers guided AI agents to mathematically prove key security properties of the actual code underlying the Signal protocol, the technology that protects billions of private conversations in apps like Signal and Google Messages.

This breakthrough discovery was made using AlphaProof Code, a novel agentic framework for formal verification at unprecedented depth that combines human expertise with AI agents. Formal verification — mathematically proving code runs correctly without flaws — is the highest standard of security assurance; however, it is difficult and often labor-intensive. Our work marks the first time AI has been used to formally verify a widely deployed cryptographic protocol at this depth. It's also the first time the implementation of a widely deployed protocol like this has been formally verified by any method, with or without AI.

How we verified Signal: AlphaProof Code is a multi-LLM agentic framework that splits the work of formal verification the way a research team would: human experts work with AI to decide what to prove, and a group of AI agents does it. First, our researchers collaborated with a mix of models to translate Signal's security goals into formal mathematical specifications, with human experts reviewing every one. From there, agents powered by Gemini Carbon did the proofs, generating over six million lines of Lean, a computer language that mathematically proves the accuracy of code. Next, the agents audited the proof and highlighted areas that needed a second look by a human — just one percent of the codebase, a massive time savings. Because Lean automatically checks the rest, our experts could focus their review where human judgment matters most.

Cryptographic protocols underpin nearly all digital communication, from online banking to web browsing, and a single flaw can expose millions of people at once. That's why experts have spent decades formally analyzing them. But most protocol verification stops at the design level. Our agents went further, proving that the compiled code fulfills the key security properties — such as keeping messages protected before and after a device is temporarily compromised — down to the exact code running on devices. Because real-world vulnerabilities often hide in the gap between design and implementation, bridging this gap makes these proofs vastly more complex. Even at this complexity, our verification process took just four weeks — a task that historically takes expert teams years — proving that Signal's core cryptographic code delivers the security protections our experts specified.

To confirm that AlphaProof Code can tell correct code from buggy code, we reintroduced two real, previously fixed bugs into an isolated version of Signal's code. In both cases, the system produced a machine-checked proof that the buggy version was insecure.

In AlphaProof Code, AI agents help users write a specification, then autonomously prove that the implementation meets it. Every proof is checked by Lean to verify the agents' work.

"While prior formal verification work has necessarily focused on smaller scopes, this new approach enables a significant expansion. Traditionally, verifying that production code strictly matches its cryptographic design required extensive manual effort, making the use of AI agents to automatically translate live code into valid Lean theorems a great breakthrough. As AI-driven security threats grow, having the core Signal protocol rigorously verified with automated theorem proving gives us even greater confidence that our code delivers on its privacy guarantees." — Ehren Kret, Chief Technology Officer of Signal

The future of security: Achieving this long-standing challenge demonstrates how AI can bring elite security assurance to businesses, governments, and critical infrastructure, helping defend against agent-driven cyber threats. Verifying Signal's core cryptography lays the groundwork to secure other vital systems, from medical device firmware to power grid software. Scaling these techniques requires continued research. Paired with automated defense agents like CodeMender, formal verification can help counter the speed and scale of modern cyber threats to create software with mathematical proof that its protections work.

We are open-sourcing our formal verification artifacts for community use.

Authors: Swarat Chaudhuri, Andrew Ferraiuolo, Anton Kovsharov, Tej Chajed, Sam Schlesinger, Karn Seth, Jonathan Katz, Charles Sutton, and Pushmeet Kohli. Thanks to Signal's Rolfe Schmidt, Michael Rosenberg, and Ehren Kret for feedback on methodology.

## HN discussion highlights (item 50439193, 647pts, 186c)

- [p-e-w] It's nothing short of amazing that a huge codebase like Signal's is apparently not only secure in a practical sense, but secure even in a strict formal sense. The people who wrote the Signal code must be engineers of the highest caliber.
- [xrisk] lean has no relation to the halting problem; you can think of it as a language that allows proofs to be encoded as code, and the compiler that runs that code as knowing how to enforce mathematical constraints appropriately.
- [sebzim4500] Solving the halting problem means writing a program which can tell whether an arbitrary other program will halt or not. Proving that a particular program will or won't halt can still be easy. The halting problem does imply that there exist programs which are entirely correct that lean will never be able to prove the correctness of, but this is not really relevant in practice.
- [bbor] "proving" and "without flaws" are just words in a language game and might not mean the absolute things we expect them to as laypeople.
- [lifeisloving] none of this really matters if the OS isn't secure and the OS is much more complex and less verifiable.
- [contravariant] Dijkstra's approach would be to prove there is a strictly decreasing natural number associated to the loop. This limits programs to the ones that can be formally shown to terminate. Which is good enough for most purposes.
