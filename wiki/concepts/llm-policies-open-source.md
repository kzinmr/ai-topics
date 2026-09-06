---
title: LLM Contribution Policies in Open-Source Projects
created: 2026-08-07
updated: 2026-09-06
type: concept
tags: [open-source, ai-governance, policy, rust, coding-agents]
sources:
  - raw/articles/2026-08-05_lwn_rust-llm-contribution-policy.md
  - raw/articles/openjdk.org--legal-ai--7752a6b0.md
related:
  - concepts/ai-code-provenance-in-open-source
  - concepts/open-source-llm-governance-debian-gr.md
  - concepts/open-source-ai.md
  - concepts/coding-agents/coding-agents.md
  - concepts/ai-governance-political-pressure.md
---

# LLM Contribution Policies in Open-Source Projects

As LLM-powered coding tools become ubiquitous, major open-source projects are grappling with a governance question: **should AI-generated code be allowed as contributions, and under what conditions?** This is not a theoretical debate — in 2026, several flagship OSS projects have adopted formal policies.

## The Stakes

LLM-generated contributions raise concerns across multiple dimensions:

| Concern | Description |
|---|---|
| **Copyright and Licensing** | Who owns AI-generated code? Does it inherit licenses from training data? Can it be cleanly licensed under OSS terms? |
| **Code Quality** | LLMs produce superficially correct but subtly wrong code. Maintainers cannot review AI output at the same trust level as human-written code. |
| **Security** | LLMs may introduce vulnerabilities that are hard to spot in code review, especially in systems programming contexts. |
| **Maintainer Burden** | Reviewing LLM-generated contributions requires more effort — the code looks plausible but may contain non-obvious errors. |
| **Attribution and Trust** | The social contract of OSS assumes human authorship. Undisclosed AI contributions violate this trust. |
| **Training Data Contamination** | LLMs trained on OSS code may reproduce it verbatim, creating copyleft violations. |

## Major Project Policies

### OpenJDK / Oracle (August 2026) — interim ban

OpenJDK's [Interim Policy on Generative AI](https://openjdk.org/legal/ai), approved by the Governing Board, is the most restrictive formal policy of the 2026 wave: contributions "must not include content generated, in part or in full, by large language models, diffusion models, or similar deep-learning systems" — covering source, text, and images in repos, PRs, email, wiki, and JBS issues. Rationale is a risk triad: reviewer burden, safety/security (JDK underpins mission-critical systems), and IP (the Oracle Contributor Agreement requires contributors to own contribution IP; AI output can reproduce training data, and user IP rights in AI output are in active litigation).

Key mechanics: private use of GenAI for comprehension/debugging/review is explicitly permitted; light human editing does not launder AI output ("100 lines generated, 10 edited → No"); Skara PR tooling adds a mandatory affirmation checkbox. The policy concedes AI-vs-human detection is "impossible," so it substitutes attestation for detection. A full policy is to be proposed to the Governing Board later. See [[concepts/ai-code-provenance-in-open-source]] for the provenance-mechanism analysis.

### Rust Language Project (August 2026)

In August 2026, the Rust language project became the latest major OSS project to adopt a formal LLM contribution policy, as reported by LWN.net. The policy:

- Establishes **guidelines for when LLM-assisted contributions are acceptable**
- Requires **disclosure** of LLM use in contributions
- Places the burden of verification on the **contributor** (not the reviewer)
- Distinguishes between LLM-assisted (human-directed, human-verified) and LLM-generated (autonomous output)
- Acknowledges the **productivity benefits** while establishing guardrails

This is significant because Rust is a systems programming language where correctness is critical — memory safety bugs introduced by LLM-generated code could have severe consequences.

### Debian General Resolution (July 2026)

The Debian project proposed a General Resolution with three options for LLM governance in the distribution. See [[concepts/open-source-llm-governance-debian-gr]] for full details.

The three options under consideration:
1. **Total ban** on LLM usage
2. **Reject LLMs "as far as practical"**
3. **Allow with conditions** — disclosure and quality requirements

### Linux Kernel

The Linux kernel community has been discussing LLM contributions since 2024. While no formal policy exists as of mid-2026, key maintainers (including Linus Torvalds) have expressed skepticism about AI-generated patches, citing the kernel's stringent quality requirements and the difficulty of verifying AI output in a codebase where bugs can have system-wide consequences.

### Other Notable Projects

- **Gentoo Linux**: Banned AI-generated contributions in 2024, citing copyright concerns
- **NetBSD**: Maintainers have expressed strong preference for human-authored contributions
- **FreeBSD**: Ongoing discussion, no formal policy yet

## Policy Design Patterns

Examining the emerging policies reveals common design patterns:

### Disclosure Requirements
The minimum common denominator: contributors must disclose LLM use. This preserves trust while allowing tool-assisted development.

### Contributor Responsibility
LLM policies universally place verification burden on the contributor. "I asked ChatGPT and it gave me this" is not an acceptable defense for buggy code.

### Distinction Between Assistance and Generation
Most policies differentiate between:
- **LLM-assisted**: Human writes code, uses LLM for suggestions/completions, verifies output
- **LLM-generated**: LLM produces autonomous output, human performs minimal or no verification

The former is generally tolerated; the latter is restricted or prohibited.

### Domain-Specific Strictness
Policies may vary by subsystem. Security-critical code, cryptographic implementations, and kernel code may have stricter rules than documentation or test code.

## Implications

### For Open-Source Sustainability
If LLM tools reduce the barrier to contribution, OSS projects may see increased participation. But if those contributions are low-quality, maintainer burnout could accelerate.

### For Code Provenance
The "Chain of Custody" problem: as LLM-generated code enters OSS codebases, downstream consumers may unknowingly incorporate AI-generated code with unclear provenance. This is especially concerning for:
- **Supply chain security**: Malicious code hidden in LLM output
- **License compliance**: Copyleft code reproduced by LLMs
- **Regulatory compliance**: Industries requiring human authorship certification

### For AI Coding Tool Design
These policies create pressure on AI coding tool vendors to:
- Provide **provenance tracking** — which parts of code were AI-generated
- Support **license-aware generation** — respecting copyleft boundaries
- Enable **verifiable attribution** — cryptographic proof of human authorship

## See Also

- [[concepts/open-source-llm-governance-debian-gr]] — Debian's General Resolution on LLM use
- [[concepts/open-source-ai]] — Broader open-source AI landscape
- [[concepts/coding-agents/coding-agents]] — Coding agent ecosystem
- [[concepts/ai-governance-political-pressure]] — Governance and policy pressures on AI
- [[concepts/shadow-ai-governance]] — Unauthorized AI use in organizations
