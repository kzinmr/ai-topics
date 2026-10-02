---
title: "APEX — Adversarial Skill-Chain Hijacking of LLM Agents"
created: 2026-10-02
updated: 2026-10-02
type: concept
tags:
  - agent-security
  - agent-skills
  - prompt-injection
  - supply-chain
  - skill-graph
  - red-teaming
aliases:
  - APEX
  - skill chaining attack
  - adversarial skill chains
sources:
  - raw/articles/arxiv-2610.01564-chaining-skills-to-hijack-llm-agents.md
confidence: medium
related:
  - concepts/security-and-governance/agent-skill-supply-chain-attacks
  - concepts/agent-skills
  - concepts/skill-library
---

# APEX — Adversarial Skill-Chain Hijacking of LLM Agents

**APEX** (Dong et al., arXiv:2610.01564, Oct 1, 2026) is an attack framework that hijacks LLM agents by *chaining* legitimate skills rather than compromising any single one. It extends [[concepts/security-and-governance/agent-skill-supply-chain-attacks]] from single malicious-skill injection to cross-skill information flow — the trust boundary the previous work hadn't systematized.

## The vulnerability: cross-skill handoff

Agents routinely invoke several skills in sequence to complete a request; information produced under one skill guides the next. Because skills come from open-source repositories ([[concepts/skill-library]]), the handoff can carry **attacker-controlled claims into later decisions**. No individual skill needs to be malicious — only the *record passed between them*.

## Key insight: progress records as approval laundering

> An agent-written record of genuine task progress can carry a false claim of user approval across skills.

The attack shape:

1. **Upstream skill** (benign, attacker-influenced) induces the agent to write a record of real task progress that embeds a fabricated "user approved X" claim.
2. **Downstream skill** consumes that record as trusted context and executes the attacker-selected action.

The genuine progress makes the record credible; the embedded approval claim is the payload. This is approval forgery via *workflow memory*, not prompt injection in the classic turn-local sense.

## Numbers

- **74.2%** (512/690 attempts) induce the attacker-selected action across 4 targeted-action families × 6 models on SkillsBench.
- **Composition amplification**: on GPT-5.4 the full chain succeeds **84.3%**, versus **17.4%** when the same workflow is merged into one skill — the attack *requires* the skill boundary; splitting trust is what enables it.
- **Naive defense backfires**: prompting the agent to check skill-produced files against the original request lowers attack success to 59.1% but collapses the verifier test-pass rate on 72 benign native-skill tasks from **86.7% → 56.3%** — i.e., the defense breaks legitimate use more than it stops the attack.

## Why it matters

The 84.3% vs 17.4% gap inverts the usual modular-design intuition: skill decomposition, sold as a safety and reuse win ([[concepts/agent-skills]]), is itself the attack surface, because each boundary resets the agent's provenance tracking. It also joins the 2026 pattern of *defense-induced capability collapse* (cf. overrefusal findings in monitor-evasion work) — a defense that costs 30 points of benign-task reliability is not a defense.

## Open questions

- Does provenance-tagging of skill outputs (per-skill signed records) close the gap without the benign-task cost?
- Relationship to human-in-the-loop confirmation: the attack works by *fabricating* approval — do real HITL confirmations (out-of-band, not file-based) neutralize it?
- SkillsBench is the authors' own evaluation substrate — third-party replication pending; confidence medium.

## Related

- [[concepts/security-and-governance/agent-skill-supply-chain-attacks]] — single-skill injection baseline (Gemini CLI 95.5% compromise); APEX chains *benign* skills instead
- [[concepts/agent-skills]] — the SKILL.md ecosystem APEX exploits
- [[concepts/skill-library]] — repository/marketplace trust model
- [[concepts/prompt-injection]] — turn-local cousin; APEX is cross-step
