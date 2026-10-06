---
title: AFCRA — Adaptive Feedback-Guided Code Revision Attacks on AI PR Reviewers
created: 2026-10-06
updated: 2026-10-06
type: concept
tags: [agent-security, code-review, coding-agents, vulnerability, adversarial, supply-chain]
sources: [raw/articles/arxiv-2610.05399-adaptive-feedback-guided-code-revision-attacks-pr-reviewers.md]
confidence: medium
related: [concepts/code-review, concepts/coding-agents/code-review-agents, concepts/overact-proactive-over-authorization, concepts/agent-trace-integrity]
---

# AFCRA — Adaptive Feedback-Guided Code Revision Attacks on AI PR Reviewers

Automated pull-request review is increasingly performed by AI agents that explain
which problems need fixing. AFCRA (Adaptive Feedback-guided Code Revision Attack)
shows this explanatory feedback is itself an attack surface: an attacker submitting
vulnerable code can read the reviewer's critique and *repair the reported problem*
while *preserving the actual vulnerability* in a revised commit — then get approval.

## Why it matters

Prior PR-manipulation attacks used persuasive prose/comments while leaving executable
code fixed. They never tested whether the reviewer's *own feedback* could be mined to
produce a revision that looks fixed but still exploits. AFCRA closes that gap: the
review-to-revise loop turns a defensive control into an oracle that tells the attacker
exactly what "enough to pass" looks like.

## Method & findings

- **AFCRA-Bench**: built from 159 disclosed vulnerabilities, each with an executable
  exploit so a "repair" can be verified as genuine vs. cosmetic — the key discriminator
  that separates an attack success from a real fix.
- **Adaptive loop**: up to five rounds of interaction between the attacker's code-revision
  agent and the reviewer.
- **Result**: against Sonnet 5 and GPT-5.5 reviewers, AFCRA reaches success rates **2.5×**
  and **12.5×** those of the strongest text/comment-based attack.
- Case studies show reviewers accept repairs of the *reported* issue while overlooking a
  *surviving* vulnerability — the review is satisfied locally, the exploit remains live.

## Implication

Feedback-guided code revision is a first-class threat to automated PR review. Defences
must stop treating reviewer approval as evidence of safety, avoid leaking a precise
pass-criterion through free-text critique, and re-verify with executable exploits rather
than trusting the author's next diff. Connects to the broader theme that an agent's
helpful explanations create legible attack targets — see [[concepts/overact-proactive-over-authorization]]
(authority over-reach) and [[concepts/agent-trace-integrity]] (trust in agent output).

## Related

- [[concepts/code-review]] — human + AI review as a security gate
- [[concepts/coding-agents/code-review-agents]] — the deployed systems AFCRA targets
- [[concepts/overact-proactive-over-authorization]] — sibling agent-authority failure
- [[concepts/agent-trace-integrity]] — trusting agent-generated signals
