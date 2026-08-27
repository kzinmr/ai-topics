---
title: Meridian Labs
created: 2026-05-11
updated: 2026-08-26
type: entity
tags:
  - nonprofit
  - organization
  - ai-safety
  - evaluation
  - open-source
  - agent-safety
aliases:
  - Meridian Labs
  - meridianlabs
sources:
  - raw/articles/2026-05-08_anthropic_petri-nla-interpretability.md
  - https://meridianlabs.ai/about
  - https://meridianlabs.ai/team
related:
  - entities/inspect-ai
  - entities/jj-allaire
  - entities/anthropic
---

# Meridian Labs

**Meridian Labs** (meridianlabs.ai) is a 501(c)(3) non-profit building open source tools for testing, evaluating, and researching frontier AI models. Its goal: a common evaluation platform shared by governments, non-profits, academia, and model developers, so that AI safety, alignment, and security work advances on neutral infrastructure rather than lab-controlled tooling.

The organization is best known as the home of the **[[entities/inspect-ai|Inspect AI]]** ecosystem — the standard open-source evaluation framework used by the UK AI Safety Institute (UK AISI), the US CAISI, the EU AI Office, Japan AISI, and Korea AISI, as well as research organizations including METR, Apollo, Epoch, SecureBio, Redwood, and RAND. In May 2026, [[entities/anthropic|Anthropic]] transferred its open-source [[concepts/evaluation/petri-alignment|Petri]] alignment auditing tool to Meridian Labs, cementing the lab's role as the independent steward of the industry's core evaluation infrastructure.

## Mission

- Make frontier AI evaluation **broadly available** via open source, so any government, lab, or researcher can run rigorous, repeatable assessments.
- Provide the infrastructure for AI Safety Institutes and lab safety teams to **transfer their internal work into broadly-available open source projects**.
- Conduct **pre-deployment testing** with these tools (e.g., Petri alignment audits are included in recent Anthropic model cards).
- Build tools for **both human researchers and AI agents**, as automated workflows for evaluation, monitoring, and alignment research become standard practice.

## Open Source Projects

| Project | Description | Users |
|---------|-------------|-------|
| **[[entities/inspect-ai\|Inspect AI]]** | Frontier AI evaluation framework: multiple-choice benchmarks to multi-agent tasks with tool use and sandboxing. Built by Meridian's founding team in collaboration with UK AISI. | UK AISI, US CAISI, EU AI Office, Japan AISI, Korea AISI, METR, Apollo, Epoch, SecureBio, Redwood, RAND |
| **Inspect Scout** | Transcript analysis framework for AI agents — LLM-based and pattern-based scanners for refusals, evaluation awareness, and environment errors. | UK AISI, US CAISI, METR, Apollo |
| **[[concepts/evaluation/petri-alignment\|Inspect Petri]]** | Automated alignment auditing tool orchestrating multi-turn interactions between auditor and target models. Originated at Anthropic, now developed at Meridian. | Anthropic model cards, frontier labs, independent evaluators |
| **Inspect Flow** | Configuration and workflow management for AI evaluations — systematic experimentation and large-scale evaluation sets for auditing and pre-deployment testing. | UK AISI, US CAISI |

Adjacent work: Inspect AI underpins control-eval projects like [ControlArena](https://control-arena.aisi.org.uk/) and [LinuxArena](https://www.linuxarena.ai/), and integrates with interpretability libraries such as TransformerLens and nnterp.

## Why Independent Stewardship Matters

In a rapidly maturing AI safety ecosystem, Meridian Labs represents the **institutionalization of independent evaluation**:

- **Trust in the evaluator** is as critical as trust in the evaluated model — a lab evaluating its own models has an inherent conflict of interest.
- **Neutral venue** — moving evaluation tooling into a nonprofit creates a cross-industry standards body, similar to how IETF or ISO handle protocol standards.
- **Sustainability** — open source projects from a single lab risk being abandoned; a nonprofit with a dedicated team ensures long-term maintenance of tools that the entire industry depends on.

## Founding Team (2025)

| Person | Role | Background |
|--------|------|------------|
| **[[entities/jj-allaire\|J.J. Allaire]]** | Co-founder, Principal Engineer | Created RStudio and Quarto; visiting researcher at US CAISI (platform technology, cybersecurity, AI measurement science) |
| **Charles Teague** | Co-founder, CEO | Developed Inspect AI as a Technology & Security Policy Fellow at RAND Corporation; previously created Quarto at Posit; founded Lose It! |
| **Eric Patey** | Co-founder, Principal Engineer | Distinguished Engineer at Sonos; previously Partner SWE Manager at Microsoft (Xbox, Office); co-founded Talko Inc. |
| **Alexandra Abbas** | Technical Program Manager | Co-founded the AI Safety Engineering Taskforce (2024); led Inspect Evals (100+ open-source evals); previously Engineering Lead at Wise |
| **Ransom Richardson** | Principal Engineer | Principal Software Architect at Microsoft (Copilot Pages, Loop Copilot); 20+ patents; previously co-founded Talko Inc. (acquired by Microsoft) |
| **Kai Fronsdal** | Research Engineer (2026) | Developed **Petri** as an Anthropic Fellow and MATS AI Safety Researcher; MSc Stanford (AI safety & alignment); pre-deployment safety audits of frontier models |
| **Matthew Brandly** | Principal Engineer (2026) | Senior Software Engineer at Sonos (5 years, React/TypeScript/Node); previously Freight Farms, Sentenai |

## The Petri Transfer (May 2026)

In May 2026, Anthropic announced two interpretability/safety developments: its **Natural Language Autoencoders (NLA)** breakthrough and the **donation of Petri 3.0 to Meridian Labs**. Petri 3.0 brought architectural improvements (adaptability, realism, depth), a "Dish" add-on that runs tests using a model's real system prompt and scaffold, and Bloom integration for deeper behavior assessments. The transfer explicitly keeps safety testing **independent from any single AI lab**, making results seen as neutral and credible industry-wide.

[Source: AI Dispatch, May 8 2026](raw/articles/2026-05-08_anthropic_petri-nla-interpretability.md)

## Timeline

| Date | Event |
|------|-------|
| 2024 | Alexandra Abbas co-founds AI Safety Engineering Taskforce; Inspect Evals (100+ evals) published |
| 2025 | Meridian Labs founded by J.J. Allaire, Charles Teague, and Eric Patey |
| 2026 (Q1) | Ransom Richardson, Kai Fronsdal, Matthew Brandly join |
| May 2026 | Anthropic donates Petri 3.0 to Meridian Labs; tooling now independent of any single lab |

## Related Pages

- [[entities/inspect-ai]] — The flagship evaluation framework
- [[concepts/evaluation/petri-alignment]] — The alignment auditing tool Meridian now maintains
- [[entities/anthropic]] — Original developer of Petri
- [[entities/jj-allaire]] — Co-founder; author of Inspect AI
- [[concepts/llm-evaluation]] — Evaluation methodologies landscape
- [[concepts/evaluation/ai-evaluation]] — AI evaluation as a discipline

## Sources

- [Meridian Labs — About](https://meridianlabs.ai/about) (scraped 2026-08-26)
- [Meridian Labs — Team](https://meridianlabs.ai/team) (scraped 2026-08-26)
- [Anthropic NLA + Petri donation announcement](raw/articles/2026-05-08_anthropic_petri-nla-interpretability.md)
