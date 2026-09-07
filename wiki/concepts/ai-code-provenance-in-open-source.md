---
title: "AI Code Provenance in Open Source"
created: 2026-09-06
updated: 2026-09-06
type: concept
tags: [open-source, policy, ai-governance, transparency, supply-chain, copyright]
sources:
  - raw/articles/openjdk.org--legal-ai--7752a6b0.md
  - raw/articles/2026-08-05_lwn_rust-llm-contribution-policy.md
  - raw/articles/lwn.net--articles-1085314--ea0bdeff.md
related:
  - concepts/llm-policies-open-source
  - concepts/open-source-llm-governance-debian-gr
  - concepts/ai-generated-issues-in-oss
  - concepts/open-source-sustainability
  - concepts/agent-security
confidence: medium   # single primary policy source + one secondary (LWN Rust); claims traceable but thinly corroborated
---

# AI Code Provenance in Open Source

**AI code provenance** is the question of *where contributed code came from* — human, AI-generated, or AI-assisted — and what mechanisms projects use to establish and enforce that lineage. As of September 2026 this has moved from philosophical debate to enforceable policy in flagship projects, with OpenJDK's interim ban (August 2026) marking the first time a major foundation-backed project drew a bright, verifiable line.

This page focuses on the **provenance mechanism** layer — disclosure, attestation, and detection — while [[concepts/llm-policies-open-source]] surveys the policies themselves and [[concepts/open-source-llm-governance-debian-gr]] covers Debian's democratic process.

## The OpenJDK Interim Policy: the "affirmation checkbox" model

OpenJDK's [Interim Policy on Generative AI](https://openjdk.org/legal/ai) (Oracle as corporate sponsor, approved by the Governing Board, ~August 2026) is the most operationally complete policy so far. Three design choices matter for provenance:

1. **Total content ban, private-use allowance.** Contributions "must not include content, generated, in part or in full, by large language models, diffusion models, or similar deep-learning systems" — source code, text, and images across git repos, PRs, email, wiki, and JBS. But contributors *may* use GenAI privately to comprehend, debug, and review. The line is drawn at the artifact, not at the tool.
2. **Skara PR affirmation checkbox.** OpenJDK reconfigured its Skara GitHub tooling so every pull request body carries a checkbox the contributor must check to affirm policy compliance — a lightweight *attestation* mechanism. The policy explicitly acknowledges "reliably distinguishing human-generated content from AI-generated content is impossible," so it substitutes attestable commitment for detection.
3. **No partial credit.** "If I use a generative AI tool to create 100 lines of code, and then edit ten of those lines myself, may I contribute the result? No." This rejects the "wash" pattern where light human editing is used to launder AI output.

The stated rationale is a risk triad: reviewer burden (plausible-looking code/tests that are wrong or unmaintainable), safety/security (the JDK underpins mission-critical systems), and intellectual property (the Oracle Contributor Agreement requires contributors to *own* IP in contributions; AI output that reproduces training data can't satisfy that, and user IP rights in AI output remain in active litigation).

## The disclosure model: Rust and the assistance/generation split

The Rust project's policy (reported by LWN, August 2026 — see [[concepts/llm-policies-open-source]]) takes the opposite mechanism: **disclosure plus contributor-borne verification burden**, tolerating LLM-*assisted* work while restricting LLM-*generated* output. The assistance/generation distinction is the conceptual load-bearing wall of every disclosure-style policy, and its weakness is that it relies on honest self-reporting — exactly the assumption the OpenJDK checkbox formalizes but cannot verify.

## Why provenance is hard: detection is (mostly) impossible

OpenJDK's own FAQ states the core problem plainly: distinguishing human from AI content is unreliable. Consequences visible across the 2026 policy wave:

- **Attestation replaces detection** — OpenJDK checkbox, Rust disclosure, Debian GR option 3's disclosure conditions ([[concepts/open-source-llm-governance-debian-gr]]).
- **Volume as attack** — AI-generated issue/PR spam against maintainers ([[concepts/ai-generated-issues-in-oss]]) makes provenance a *triage* problem before it is a legal one.
- **Downstream chain-of-custody** — once AI-generated code merges, downstream consumers inherit unverifiable lineage (see supply-chain angle in [[concepts/open-source-sustainability]]).

## A spectrum, mid-2026

| Project | Mechanism | Stance (as of Sep 2026) |
|---|---|---|
| OpenJDK | Artifact ban + PR attestation checkbox | Ban generated content; permit private use |
| Rust | Disclosure + contributor verification | Assisted OK, generated restricted |
| Debian | Democratic GR (ban / as-far-as-practical / conditional) | Three-way vote, see GR page |
| Gentoo | Ban (2024) | Early mover, copyright rationale |
| Linux kernel | Informal maintainer skepticism | No formal policy |

The pattern: **foundation-backed, legally-exposed projects (OpenJDK, Gentoo) converge on bans; community-governed projects (Rust, Debian) converge on disclosure/democracy.** Legal exposure — contributor agreements, copyright litigation risk — appears to predict policy strictness better than technical risk does.

## Open questions

- Do attestation checkboxes change behavior at all, or only create a paper trail for post-hoc blame?
- Can license-aware generation or provenance watermarking (C2PA-style for code) make verification possible, restoring "detection" to the toolkit?
- Will the full OpenJDK policy (promised to replace the interim one) relax toward disclosure once reviewers gain experience, as the interim policy's "gain further experience" framing hints?

## See Also

- [[concepts/llm-policies-open-source]] — the policy landscape this page's mechanisms come from
- [[concepts/open-source-llm-governance-debian-gr]] — Debian's General Resolution process
- [[concepts/ai-generated-issues-in-oss]] — AI-generated contribution spam as the triage failure mode
- [[concepts/open-source-sustainability]] — maintainer burden economics
- [[concepts/agent-security-patterns]] — agentic contributors and the trust model
