---
title: "Shifting structures in a software world dominated by AI. Some first-order reflec..."
source: "https://x.com/i/status/2023387043967959138"
date: 2026-04-30
type: x_tweet
tweet_id: "2023387043967959138"
author: "unknown"
---

Shifting structures in a software world dominated by AI. Some first-order reflections (TL;DR at the end):

Reducing software supply chains, the return of software monoliths – When rewriting code and understanding large foreign codebases becomes cheap, the incentive to rely on deep dependency trees collapses. Writing from scratch ¹ or extracting the relevant parts from another library is far easier when you can simply ask a code agent to handle it, rather than spending countless nights diving into an unfamiliar codebase. The reasons to reduce dependencies are compelling: a smaller attack surface for supply chain threats, smaller packaged software, improved performance, and faster boot times. By leveraging the tireless stamina of LLMs, the dream of coding an entire app from bare-metal considerations all the way up is becoming realistic.

End of the Lindy effect – The Lindy effect holds that things which have been around for a long time are there for good reason and will likely continue to persist. It's related to Chesterton's fence: before removing something, you should first understand why it exists, which means removal always carries a cost. But in a world where software can be developed from first principles and understood by a tireless agent, this logic weakens. Older codebases can be explored at will; long-standing software can be replaced with far less friction. A codebase can be fully rewritten in a new language. ² Legacy software can be carefully studied and updated in situations where humans would have given up long ago.

The catch: unknown unknowns remain unknown. The true extent of AI's impact will hinge on whether complete coverage of testing, edge cases, and formal verification is achievable. In an AI-dominated world, formal verification isn't optional—it's essential.

The case for strongly typed languages – Historically, programming language adoption has been driven largely by human psychology and social dynamics. A language's success depended on a mix of factors: individual considerations like being easy to learn and simple to write correctly; community effects like how active and welcoming a community was, which in turn shaped how fast its ecosystem would grow; and fundamental properties like provable correctness, formal verification, and striking the right balance between dynamic and static checks—between the freedom to write anything and the discipline of guarding against edge cases and attacks. As the human factor diminishes, these dynamics will shift. Less dependence on human psychology will favor strongly typed, formally verifiable and/or high performance languages.³ These are often harder for humans to learn, but they're far better suited to LLMs, which thrive on formal verification and reinforcement learning environments. Expect this to reshape which languages dominate.

Economic restructuring of open source – For decades, open-source communities have been built around humans finding connection through writing, learning, and using code together. In a world where most code is written—and perhaps more importantly, read—by machines, these incentives will start to break down.⁴ Communities of AIs building libraries and codebases together will likely emerge as a replacement, but such communities will lack the fundamentally human motivations that have driven open source until now. If the future of open-source development becomes largely devoid of humans, alignment of AI models won't just matter—it will be decisive.

The future of new languages – Will AI agents face the same tradeoffs we do when developing or adopting new programming languages? Expressiveness vs. simplicity, safety vs. control, performance vs. abstraction, compile time vs. runtime, explicitness vs. conciseness. It's unclear that they will. In the long term, the reasons to create a new programming language will likely diverge significantly from the human-driven motivations of the past. There may well be an optimal programming language for LLMs—and there's no reason to assume it will resemble the ones humans have converged on.

TL; DR:
- Monoliths return – cheap rewriting kills dependency trees; smaller attack surface, better performance, bare-metal becomes realistic
- Lindy effect weakens – legacy code loses its moat, but unknown unknowns persist; formal verification becomes essential
- Strongly typed languages rise – human psychology mattered for adoption; now formal verification and RL environments favor types over ergonomics
- Open source restructures – human connection drove the community; AI-written/read code breaks those incentives; alignment becomes decisive
- New languages diverge – AI may not share our tradeoffs; optimal LLM programming languages may look nothing like what humans converged on

¹ https://t.co/0gO5TUwguU
² https://t.co/oN0PnPr1dF
³ https://t.co/nWKSw0m2Ct
⁴ https://t.co/ZrH3fhzQD4
