---
title: "DRAM Price-Fixing Lawsuit (2026)"
created: 2026-11-15
updated: 2026-11-15
type: concept
tags: [hardware, ai-industry, law, nvidia, memory-standards]
sources:
  - raw/articles/2026-11-15_dram-price-fixing-lawsuit.md
  - raw/articles/2026-11-15_hn-discussion_dram-price-fixing.md
  - https://litnews.ai/articles/garciaguirre-samsung-sk-hynix-micron-dram-conspiracy-suit-survives-dismissal
  - https://news.ycombinator.com/item?id=50502988
confidence: high
---

# DRAM Price-Fixing Lawsuit (2026)

On **November 14, 2026**, U.S. District Judge **Noël Wise** (N.D. Cal.) **denied in full** the joint motion to dismiss of Samsung, SK Hynix, and Micron in a proposed class action alleging they conspired to restrict conventional DRAM supply while pivoting capacity to HBM for AI accelerators (HN 181 pts). The case is the first serious antitrust reckoning with the 2025–26 memory-price shock that hit consumers and AI-build costs alike.

## Case posture

- Filed **June 25, 2026** by 17 consumers/small businesses from five states; plaintiffs represented by Bathaee Dunne LLP (vs. O'Melveny, Cleary Gottlieb, Gibson Dunn for the three defendants).
- Defendants controlled **>91% of global DRAM revenue** (Q3 2025). Complaint: production cuts from late 2022; capacity shifted to **HBM** from 2023 (HBM needs **3–4× the wafer area per GB** vs DDR5); conventional DRAM prices **+171.8% year-over-year** by Q3 2025 and **+697% over 18 months**, with no meaningful capacity expansion announced.
- Answers due **Dec 7, 2026**; initial case-management conference **Jan 12, 2027**.

## Why it survives DRAM II

The defense argued the suit re-runs *DRAM II* (9th Cir. 2022, dismissal affirmed over the 2016–18 supply restriction). Wise: "The Court finds that it is not." Plus factors credited:

- **Long-term HBM lock-ups**, Samsung/SK Hynix refusals of long-term conventional-DRAM contracts, Micron's **Dec 3, 2025 Crucial closure** — moves "difficult if not impossible to unwind";
- **Fab delays / non-expansion despite record prices** (analogized to *Petroleum Products* (9th Cir. 1990): capacity decisions aren't readily reversible);
- Same-quarter 2025 **DDR4 wind-downs** (DDR4 cost more per GB than DDR5);
- **Near-identical customer-vetting practices** adopted January 2026 — the AI-demand explanation rejected since vetting began *after* the boom;
- The 1998–2002 **criminal DRAM cartel** history counts again (Samsung $300M fine, Hynix $185M, Micron immunity as cooperator).

Not credited: "supply discipline" investor statements, industry-conference meetings, and bare oligopoly structure. The opinion's line: plaintiffs allege "hawks flying in formation – an activity that hawks ordinarily do not do."

## AI-industry context

- The HBM pivot is the demand-side story: AI accelerator builders (NVIDIA, AMD) reserve the wafer capacity, and consumer/commodity DRAM scarcity follows — this suit legalizes a conspiracy narrative for what the industry frames as rational HBM arbitrage.
- Connects to the Nov 2026 memory-price political controversy (Sam Altman's DRAM-to-datacenters remark, [[entities/ed-zitron]]'s systemic-risk framing) and [[concepts/ai-industry-economics]] cost structures.
- If the case proceeds past class certification, memory-capacity allocation decisions by the 91% oligopoly become discovery targets — a governance question for [[concepts/ai-regulation-2026]] adjacent antitrust doctrine.

## Related

- [[concepts/ai-industry-economics]] — memory as AI cost input
- [[entities/ed-zitron]] — memory-price critique of AI capex
- [[concepts/kv-cache-memory-wall]] — the memory-bound economics behind HBM demand
- [[concepts/ai-regulation-2026]] — antitrust/governance adjacency
