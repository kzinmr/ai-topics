---
title: "Anthropic $1.5B Copyright Settlement"
created: 2026-07-24
updated: 2026-07-24
type: concept
tags:
  - anthropic
  - law
  - policy
  - governance
  - regulation
  - ethics
  - legal-tech
  - event
sources: [raw/articles/2026-07-21_apnews-anthropic-copyright-settlement.md]
---

# Anthropic $1.5B Copyright Settlement

## Overview

In July 2026, a federal judge granted final approval to a **$1.5 billion settlement** in _Bartz v. Anthropic PBC_, the first major resolution among dozens of AI copyright lawsuits. [[entities/anthropic|Anthropic]] agreed to pay approximately **$3,000 per book** to authors whose works were downloaded from pirate sites and used to train the Claude chatbot. The settlement covers roughly 482,000 titles, with a 91%+ claim rate.

The case produced a landmark **dual ruling** in summer 2025: training AI on copyrighted books is fair use, but pirating the books to build the training corpus is willful infringement. Because Anthropic settled, the fair-use ruling never reached an appeals court and does not create binding precedent, though it carries persuasive weight.

## What Happened

Bestselling thriller novelist **Andrea Bartz** and two other authors filed the class-action lawsuit in 2024 in the U.S. District Court for the Northern District of California. Anthropic had built its training library from two sources: books it purchased and scanned (legal), and books downloaded from pirate sites like **Library Genesis** and **Pirate Library Mirror** (illegal).

Judge William Alsup handled the case until retirement, issuing the pivotal fair-use / piracy distinction ruling. Judge Araceli Martinez-Olguin presided over final approval on July 20, 2026.

## The Dual Ruling

| Aspect | Ruling |
|--------|--------|
| Training AI on copyrighted books | **Fair use** — a landmark finding for the AI industry |
| Pirating books to build training corpus | **Willful infringement** — illegal acquisition method |

This distinction is now central to [[concepts/ai-inventorship-patent-law|AI intellectual property law]] debates. It means AI companies can train on copyrighted material under fair use but must acquire that material through legal channels.

## Settlement Details

- **Total amount:** $1.5 billion
- **Per-book payout:** ~$3,000 (roughly 2% of the statutory maximum of $150,000 per willful infringement)
- **Books covered:** ~482,000 titles (down from an initial class of up to 7 million after deduplication)
- **Claim rate:** 91%+
- **Class counsel fees:** Slashed from 12.5% ($187.5M) to 6.8% ($101M) after objections
- **Class representatives:** $15,000 each for the three named plaintiffs
- **Payment structure:** Installments, making class members effectively Anthropic creditors

Anthropic is not required to delete scanned physical copies, retrain models, or admit wrongdoing.

## Controversy and Criticism

### Judge Alsup's Objections (September 2025)

At a September 8, 2025 hearing, Judge Alsup blasted the proposed settlement as "nowhere close to complete," citing unresolved claims processes and notification issues. He granted preliminary approval only after revisions in October 2025.

### Objector Concerns (May 2026)

Class member objections led Judge Martinez-Olguin to delay final approval in May 2026. Critics noted:
- Attorneys sought 320+ million in fees (estimated at 10-12K per hour) while each author received only $3,000
- The $3,000 per book represents just 2% of the statutory maximum of $150,000
- No requirement to retrain models or delete pirated data
- Some objectors reported difficulty filing through court systems

### Authors Guild Defense

The Authors Guild defended the settlement as avoiding years of litigation, achieving a certain immediate result that "sends a powerful signal" to the industry, and pushing AI companies toward licensing rather than pirating content.

## Legal Implications

The case sits at the intersection of several active [[concepts/ai-regulation-2026|AI regulation]] and [[concepts/ai-policy|AI policy]] debates:

1. **No binding precedent**: The fair-use ruling is persuasive but not precedential since the case settled
2. **Piracy firewall**: Using pirated sources for training data is illegal even if training itself is fair use
3. **Industry template**: Other lawsuits continue against Google, Meta, Midjourney, and OpenAI. In July 2026, publishers including Hachette, Cengage, and Elsevier filed a new class action against Google over Gemini training
4. **The $1.5B moat theory**: Anthropic effectively paid to resolve liability while establishing that training on books is fair use — creating a financial barrier for future entrants. At Anthropic's ~$183B valuation at the time, the settlement represented less than 1% of total value

## Community Reactions (HN: 1,549 pts, 1,357 comments)

- **Settlement too small**: Dominant sentiment — "$3k a book is so cheap," "seems squarely in the cost of doing business category"
- **Corporate vs. individual justice**: Multiple commenters drew parallels to Aaron Swartz, who faced 50 years for downloading academic articles; companies pay fines, individuals go to jail
- **Structural critiques**: Calls for ongoing royalties rather than one-time payment; some argued the penalty should be releasing the model as public domain
- **Copyright philosophy debate**: Split between "death to copyright, harmful to small authors" and support for Anthropic's position that publishers would shut down public libraries if they could

The Free Software Foundation issued a statement in March 2026 on the case's implications for freedom of information.

## Timeline

| Date | Event |
|------|-------|
| 2024 | Bartz + 2 authors file class-action lawsuit |
| Summer 2025 | Judge Alsup issues dual fair-use / piracy ruling |
| Sep 5, 2025 | Anthropic agrees to $1.5B settlement |
| Sep 8-9, 2025 | Alsup blasts settlement as incomplete |
| Oct 2025 | Preliminary approval granted after revisions |
| Mar 2026 | FSF issues statement on the case |
| May 2026 | Final approval delayed due to objector concerns |
| Jul 20, 2026 | Judge Martinez-Olguin grants final approval |
| Pending | 25 opt-out class members file separate lawsuit |

## Related Pages

- [[entities/anthropic]] — Anthropic company overview
- [[concepts/ai-inventorship-patent-law]] — AI intellectual property and patent law precedents
- [[concepts/ai-regulation-2026]] — Current landscape of AI regulation
- [[concepts/ai-policy]] — Broader AI policy context
- [[concepts/ai-governance-political-pressure]] — AI governance under political pressures, including Anthropic-related cases
- [[events/apple-sues-openai-2026]] — Another major AI legal action in 2026
- [[concepts/open-source-licensing]] — Licensing models in AI, contrasted with unlicensed data acquisition
