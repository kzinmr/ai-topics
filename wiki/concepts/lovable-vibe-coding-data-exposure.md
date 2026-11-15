---
title: "Lovable vibe-coding data exposure (Crissy Field / Handelsblatt, Nov 2026)"
created: 2026-11-15
updated: 2026-11-15
type: concept
tags: [vibe-coding, data-exposure, security-audit, web-security, pii, ai-coding, ai-safety, case-study, controversy]
sources:
  - raw/articles/2026-11-15_crissyfield-lovable-data-exposure.md
  - https://www.crissyfield.de/research/lovable-en/
  - https://news.ycombinator.com/item?id=50499017
---

# Lovable vibe-coding data exposure (November 2026)

## Overview

On November 13-14, 2026 the German security consultancy **Crissy Field** (research.crissyfield.de), in collaboration with *Handelsblatt*, published the largest public audit yet of applications built on the AI app builder **Lovable** — and it became one of the most discussed AI stories of the weekend (HN 851 points).

The researchers crawled **159,041 public Lovable projects** (December 2025 - September 2026, via Common Crawl). Of these, **34,545 used Supabase** as their backing database; **24,664 websites returned database records at page load without any login**. Additional read-only requests using the same exposed API key retrieved further table contents, including records with email addresses in **10,560 tables across 7,403 sites (30%)**. Reported exposures included **passport details and more than 200,000 private messages**.

## Why it happened

The failure is not a Lovable platform bug but an **incentive-and-literacy gap**:

- Lovable's marketing repeatedly states that **no technical knowledge is needed**, while its Terms & Conditions place full responsibility for data handling on the customer.
- Supabase integration is easy to wire up; row-level security (RLS) is off by default unless the builder configures it, and the target user has no reason to know RLS exists.
- Lovable's own first-party database (introduced late 2025) was too little-used to audit; the authors expect similar misconfigurations there.

## Assessment

The report is methodologically careful (it flags that email-bearing rows may be test data or public contacts, and that non-email PII is missed by the detector) and is the strongest empirical artifact so far for the "vibe-coding ships vulnerable software" critique. It is single-source; Lovable had not published a substantive response at time of writing. HN reception split three ways: (1) this is what happens when "move fast and break things" meets non-programmer builders; (2) pre-AI software was never safe either — tech companies have always treated customers as KPIs; (3) forward-looking warning that frontier abliterated models at thousands of tokens/second will find this class of issue faster than anyone can remediate, and that formal verification is not a rescue.

One practitioner thread noted the mirror-image incident a few days earlier: **Railway** compromised with reportedly ~$740k in AI service charges, allegedly using stolen keys and abliterated models — i.e. the exposed-app attack surface is being actively monetized.

## Related

- [[entities/lovable]] — the platform audited
- [[concepts/ai-slop]] — quality-degradation critique of AI-generated artifacts
- [[concepts/coding-agents/ai-coding-reliability]] — reliability of AI-assisted code
- [[concepts/ai-adoption-barbell]] — why non-expert builders never reach the security configuration layer

## Sources

- Raw: `raw/articles/2026-11-15_crissyfield-lovable-data-exposure.md` (full report + HN thread highlights)
- https://www.crissyfield.de/research/lovable-en/
- https://news.ycombinator.com/item?id=50499017
