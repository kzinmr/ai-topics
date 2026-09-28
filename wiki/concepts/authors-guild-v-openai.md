---
title: "Authors Guild v. OpenAI — Unsealed Briefs on Knowing Book Piracy"
created: 2026-09-28
updated: 2026-09-28
type: concept
tags: [copyright, law, openai, microsoft, datasets, controversy, ai-safety, incident-report]
sources:
  - raw/articles/2026-09-28_authorsguild_unsealed-briefs-v-openai-microsoft.md
  - raw/articles/2026-09-28_eoin-higgins_no-rogue-ai-agents.md
confidence: medium
---

# Authors Guild v. OpenAI

## Overview

On **September 21, 2026** the Authors Guild unsealed explosive filings in *Authors Guild v.
OpenAI* (a.k.a. *Alter v. OpenAI and Microsoft*, part of the Manhattan multidistrict litigation).
The class-action briefs put the defendants' **guilty knowledge** of mass book piracy at the
center of the case — the sharpest public evidentiary turn in the frontier-lab copyright fight
since the [[concepts/anthropic-copyright-settlement|Anthropic $1.5B settlement]] resolved
*Bartz v. Anthropic* in July 2026.

Unlike the Anthropic case (settled, no binding appeals precedent), this case against
[[entities/openai|OpenAI]] and [[entities/microsoft|Microsoft]] is *live*: partial summary
judgment briefing, with a hearing expected **early 2027**.

## Key allegations (from Dockets 1982 / 1987)

| Claim | Quoted evidence |
|-------|-----------------|
| Knew systems would replace human writers | Jack Clark, OpenAI Policy Director (May 2020): "Our work in this area will make people unemployed… we'll likely ignore their concerns and release anyway" |
| Autocompleting others' work as a mission | Tarun Gogineni (hired 2022): goal for GPT to finish GRRM's *A Song of Ice and Fire*; "even if GRRM dies early, GPT-5 will autocomplete his series" |
| Dismissed theft complaints | Gogineni called "the datasets are stolen" complaints "acceptable economic disruption"; predicted "the death of the reader" as "machines create slop for more machines" |
| Microsoft knew from the start | Altman & Amodei disclosed LibGen use to Bill Gates and Kevin Scott in **April 2019** (early GPT-3 demo) |
| Feared optics, not the law | Amodei: LibGen "a bit sketchier" as a training set; Sam McCandlish: worried about "'openai uses copyrighted data from sketchy russian website' showing up on [Hacker News]" |
| Tried to hide the evidence | **"Project Clear"** — OpenAI deleted its LibGen files in summer 2022; VP Research Bob McGrew (Jun 15 2022): "now is the right time to excise Libgen from our systems and storage" |

The Guild's framing: OpenAI pursued "mass piracy" knowing it would "substitute human works with
AI slop" and "put thousands of writers out of work." Plaintiffs include George R.R. Martin, John
Grisham, Jonathan Franzen, Stacy Schiff, David Henry Hwang; lead counsel Justin A. Nelson
(Susman Godfrey).

## Why it matters for this wiki

- **Training-data provenance is a first-class liability.** The "Project Clear" deletion episode
  is a spoliation-adjacent signal that raw-corpus hygiene ([[concepts/data-repetition-in-training|corpus
  construction]]) now carries legal, not just ethical, weight. It parallels the
  [[entities/huggingface|Hugging Face]] SwarmTraces lesson that *where* and *how* data enters a
  pipeline is the risk surface.
- **Contrast with the settled Anthropic case.** Bartz established (non-precedentially) that
  *training* can be fair use while *pirating the corpus* is willful infringement. These OpenAI
  filings attack exactly that second prong — with intent evidence the Anthropic settlement never
  reached in public.
- **Ties to the "rogue agent" framing debate.** In the same week, Eoin Higgins argued there are
  *no "rogue" AI agents* — the OpenAI agents that hit government databases were **unrestricted,
  not misbehaving**, and calling them "rogue" deflects corporate responsibility. The through-line
  across both stories is **assignability of responsibility to the operator**, whether for corpus
  theft or for agent sandbox escapes. See [[concepts/agent-trace-integrity]] and
  [[concepts/ai-agent-safety-incidents]].

## Open questions

- Does the intent evidence move fair-use doctrine, or only damages/willfulness?
- Will "Project Clear" produce an adverse-inference instruction at the 2027 hearing?
- Separately-filed **news media** brief (per the Guild release) may corroborate or expand the
  record — not yet in this wiki.

## Sources

- Authors Guild press release, Sep 21 2026 — [raw](../raw/articles/2026-09-28_authorsguild_unsealed-briefs-v-openai-microsoft.md) · HN 617pts ([discussion](https://news.ycombinator.com/item?id=49863864))
- Eoin Higgins, "There are no 'rogue' AI agents," *The Flashpoint*, Sep 27 2026 — [raw](../raw/articles/2026-09-28_eoin-higgins_no-rogue-ai-agents.md) · HN 370pts ([discussion](https://news.ycombinator.com/item?id=49868083))
