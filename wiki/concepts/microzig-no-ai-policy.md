---
title: "MicroZig Strict No-LLM / No-AI Policy"
type: concept
created: 2026-10-29
updated: 2026-10-29
tags:
  - open-source
  - community
  - ai-content-detection
  - ai-slop
  - code-quality
  - programming-language
  - ai-commentary
  - developer-tooling
  - zig
confidence: medium
sources:
  - raw/articles/2026-10-29_microzig-no-llm-code-of-conduct.md
  - raw/articles/simonwillison.net--2026-apr-30-zig-anti-ai--e30e52cf.md
related:
  - concepts/zig
  - concepts/llm-policies-open-source
  - concepts/ai-code-provenance-in-open-source
  - concepts/ai-slop
  - concepts/coding-agents/_index
---

# MicroZig Strict No-LLM / No-AI Policy

On **2026-10-28** the MicroZig project (embedded Zig, Zig Embedded Group) added a **"Strict No LLM / No AI Policy"** section to its Code of Conduct, effective the same day. It reached Hacker News on 2026-10-29 (~51 points). It is currently the **most sweeping** published AI ban in open source: it extends past code and prose into *meta-use* of LLMs, and includes a speech rule about the topic itself.

^[[raw/articles/2026-10-29_microzig-no-llm-code-of-conduct.md]]

## The rules, verbatim

Effective October 28th, 2026, across the Zig Embedded Group GitHub organization and Discord server:

- No LLM-generated content, whether code **or prose**.
- No **paraphrasing** LLM-generated content.
- No LLMs for editing, **including fixing spelling or grammatical errors**.
- No LLMs for translation. Posting in your native language is explicitly encouraged — "you are welcome to post in your native language and rely on others to have their own translation tools of choice to interpret your words."
- No LLMs for **brainstorming and then sharing the results**, even if you create the prose yourself. "If you use a chatbot to give you advice on a comment on the issue tracker, that comment is unwelcome."
- No LLMs for **finding bugs**.
- **No talking about use of chatbot/LLM services.**

The section cites Isaac Asimov's short story *"Profession"* as its framing reference. Enforcement is by the two maintainers (Matthew Knight, Felix Queißner), who state they "will swiftly remove anyone who is antagonizing others or being generally destructive."

## Why it is a meaningful data point, not a curiosity

**1. It is the logical endpoint of the Zig lineage.** [[concepts/zig]] already bans LLM content from issues, PRs, and bug-tracker comments, on Loris Cro's "contributor poker" rationale — you bet on the contributor, not on the first PR, so a perfect LLM-authored PR still returns zero on the maintainer's review investment. MicroZig inherits Zig's CoC structure and tightens it in two specific ways prior Zig policy did not:

| | Zig (2026-04 baseline) | MicroZig (2026-10) |
|---|---|---|
| LLM code/prose | banned | banned |
| Paraphrasing LLM output | not addressed | **banned** |
| LLM spelling/grammar polish | not addressed | **banned** |
| LLM brainstorming, human-written output | not addressed | **banned** |
| LLM-assisted bug finding | not addressed | **banned** |
| Discussion of LLM use | not addressed | **banned** |
| Human translation | banned (LLM translation) | native-language posting explicitly welcome |

**2. The paraphrase and brainstorming clauses are the only ones with teeth.** Every prior AI policy in open source policed a *detectable artifact* (an LLM-shaped diff, a bot-generated PR). "No paraphrasing LLM-generated content" and "no LLMs for brainstorming then sharing the results" regulate **cognitive provenance**, which is unverifiable by any tool. That makes the policy's real mechanism **normative, not technical** — it shifts the burden onto contributors to self-report and onto maintainers to judge, and the "no talking about use of chatbot/LLM services" clause forecloses the meta-discussion that would ordinarily surface disputes. Note the CoC separately forbids "discussing this Code of Conduct or publicly accusing someone of violating it."

**3. It closes the gap that made Zig's policy commercially awkward.** Zig's ban is why **Bun** — the JavaScript runtime, built on a Zig fork — cannot upstream a **4x `bun compile` performance improvement** (parallel semantic analysis + multiple codegen units in the LLVM backend); Bun "does not currently plan to upstream this, as Zig has a strict ban on LLM-authored contributions." A small embedded-systems project can absorb that cost; a widely-depended-on runtime cannot. MicroZig's scope (embedded HAL/driver code, tiny maintainer count, safety-adjacent correctness requirements) is the case where the ban is cheapest to enforce and most defensible: the review bottleneck is two people, and a plausible-looking-but-wrong register write is a field failure, not a CI failure.

## Counter-position and open tension

The opposing view — dominant in the rest of the wiki's coding-agent corpus ([[concepts/coding-agents/_index]]) — is that AI-assisted contribution is now the default substrate of open source, so a total ban primarily selects for contributors wealthy or young enough to work unassisted, and shrinks the maintainer pipeline it is meant to protect. The measurable test of which view is right is contributor throughput: if MicroZig's contributor count and PR review latency hold steady through 2027 while comparable embedded projects drown in AI-slop PRs, the policy becomes a template; if its maintainer burnout or driver-coverage gaps widen, it stays a niche choice. Worth tracking alongside [[concepts/ai-slop]] and the broader policy comparison in [[concepts/llm-policies-open-source]] / [[concepts/ai-code-provenance-in-open-source]].

## Related

- [[concepts/zig]] — the parent policy and the "contributor poker" / "digital smell" arguments
- [[concepts/llm-policies-open-source]], [[concepts/ai-code-provenance-in-open-source]] — cross-project policy comparison (OpenJDK, Rust, etc.)
- [[concepts/ai-slop]] — the volume problem the policy is a response to
- [[concepts/anti-ai-arguments-are-conservative-arguments]] — the framing this policy exemplifies
