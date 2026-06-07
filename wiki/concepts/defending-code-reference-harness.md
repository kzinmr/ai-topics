---
title: "Defending Code Reference Harness"
created: 2026-06-07
updated: 2026-06-07
type: concept
tags: [ai-safety, coding-agents, security, vulnerability, open-source, anthropic, model]
sources:
  - https://claude.com/blog/using-llms-to-secure-source-code
  - https://github.com/anthropics/defending-code-reference-harness
  - raw/articles/2026-06-03_eugeneyan_defending-code-reference-harness.md
---

# Defending Code Reference Harness

The **Defending Code Reference Harness** is an open-source reference implementation by [[entities/anthropic|Anthropic]] for autonomous vulnerability discovery and remediation using [[entities/claude|Claude]] (particularly Claude Opus). Authored by [[entities/eugene-yan|Eugene Yan]], Henna Dattani, and others based on learnings from partnering with security teams since launching Claude Mythos Preview.

**Core thesis:** Discovery is now straightforward to parallelize with strong models; the bottleneck has shifted to verification, triage, and patching. As of May 22, 2026, Anthropic had disclosed 1,596 vulnerabilities in open source software—only 97 had been patched.

The repo is not maintained and not accepting contributions. Anthropic offers a managed alternative: **Claude Security**, a hosted product for agentic vulnerability detection and patching.

## The Find-and-Fix Loop

The harness operationalizes a six-step loop distilled from best practices of the most successful security teams:

| Step | Phase | Description | Skill |
|------|-------|-------------|-------|
| 1 | **Threat Model** | Define what counts as a vulnerability before scanning | `/threat-model` |
| 2 | **Sandbox** | Build isolated environment (gVisor) to run agents and prove exploits | `/customize` |
| 3 | **Discovery** | Models look for vulnerabilities in source code | `/vuln-scan` |
| 4 | **Verification** | Independently confirm which findings are actually exploitable | (built into pipeline) |
| 5 | **Triage** | Deduplicate findings, assign severity, prioritize fixes | `/triage` |
| 6 | **Patching** | Apply fix, confirm nullification, search for variants | `/patch` |

Steps 1-2 are one-time setup per codebase. Steps 3-6 form the iterative scanning loop.

## Architecture: The 7-Stage Pipeline

The autonomous reference pipeline (`harness/`) implements seven stages, each run in isolated containers:

1. **Build** — Compiles target into Docker image with ASAN (Address Sanitizer for C/C++)
2. **Recon** — Lightweight agent reads source, proposes a partition of attack surfaces
3. **Find** — N agents run in parallel, each crafting malformed inputs to trigger crashes
4. **Verify** — Independent grader agent reproduces each crash in fresh container
5. **Dedupe** — Judge agent compares verified crashes against already-reported bugs
6. **Report** — Report agent writes structured exploitability analysis
7. **Patch** — Patch agent proposes fix; grader confirms build, regressions, and adversarial resilience

Each agent runs inside a gVisor container with egress restricted to the Claude API.

## Key Design Principles

### Discovery Optimizes for Recall; Verification for Precision

A critical finding from the research: when discovery agents also try to verify findings, they self-censor and filter out true positives. Separation is essential.

### Adversarial Verification

Adding an adversarial verifier roughly halved the rate of non-exploitable findings. Requiring the verifier to also build a proof of concept brought the false positive rate to near zero.

### Short Prompts Over Checklists

Counterintuitively, frontier models perform better in discovery with simple prompts. Long prescriptive checklists reduce the model's creativity and generate fewer novel bugs.

### Sandbox as Proof Engine

Teams found that "the biggest efficacy lever has been giving the model test beds, live systems, and running the PoCs." Building a sandbox where agents can compile, run tests, and detonate PoCs dramatically reduced non-exploitable findings.

### Threat Model as Prophylactic

The most common cause of false positives is the model lacking understanding of trust boundaries. A well-documented threat model (`THREAT_MODEL.md`) improved exploitable finding rates to 90%.

## Ramp-Up Plan

| Step | When | Description |
|------|------|-------------|
| Step 1 | Day 1 | Build threat model + first static scan + triage |
| Step 2 | Day 2 | Run reference pipeline on a C/C++ library |
| Step 3 | Days 3-5 | Customize pipeline for your target |
| Step 4 | Week 2 | Start autonomous scanning, triage, and patching |

## Repository Stats (as of June 2026)

- **Stars:** 5,100+
- **Forks:** 330+
- **Languages:** Python (92.7%), Shell (3.5%), C (2.5%), Dockerfile (1.3%)
- **Key files:** Claude Code skills (`.claude/skills/`), harness pipeline (`harness/`), sandbox setup (`scripts/setup_sandbox.sh`)

## Triaging Bottleneck

With models capable of finding 100+ candidates before lunch, triage has become the critical bottleneck. The harness addresses this with:

- **Deterministic dedup:** Same file, same category, lines within 10 of each other
- **Qualitative rules:** Root cause analysis, distinguishing duplicates from distinct bugs
- **Severity rubric:** Reachability, attacker control, preconditions, authentication, read vs. write, blast radius

Multiple teams reported: sending untriaged findings to engineers causes alert fatigue and trust erosion.

## Patching Validation Ladder

Each patch is validated through increasingly expensive checks:
1. **Build** — Patch compiles, new tests pass
2. **Reproduce** — Original PoC should stop working
3. **Regressions** — Original test suite still passes
4. **Re-attack** — Fresh discovery agent probes for completeness

Models tend to write overly restrictive patches; minimal, root-cause fixes are preferred over defensive rewrites.

## Related Concepts

- [[concepts/agent-sandboxing]] — Sandbox isolation patterns for AI agents
- [[concepts/claude-code]] — Claude Code, the coding agent platform that runs these skills
- [[concepts/threat-modeling]] — Threat modeling in AI/security contexts
- [[entities/anthropic]] — Anthropic, the company behind this harness
- [[entities/eugene-yan]] — Eugene Yan, co-author of the blog post and harness
- [[concepts/vulnerability-detection]] — AI-driven vulnerability detection
- [[concepts/llm-evaluation-harness]] — Eugene Yan's broader work on eval-driven development
