# Comprehensive Author Entity Page — Density Gradient Pattern

**Observed**: June 2026, blog triage session
**Author**: Gary Marcus (entity page: 310 lines, 15+ sections)
**Article**: "China catches up" — a short restatement of the "no moat" thesis
**Verdict**: Correctly skipped as already covered

## The Pattern

When an author's entity page is **300+ lines across a dozen sections** covering the same core thesis from multiple angles, the bar for "new content" from that author becomes very high. A new article repeating the same thesis with no new empirical data, even if the framing angle differs slightly, is almost certainly skip.

### Concrete Example

Gary Marcus's entity page covers the "no moat / AI is overhyped / margins are unsustainable" thesis through these distinct sections:
- Enterprise Tokenmaxxing Backlash
- Generative AI Fizzle™
- Why Things Will Eventually Fall Apart
- GPU Rental Price Collapse
- AI's Black Friday — Market Crash
- Anthropic RSI Response: "No need to panic"
- Jensen Huang IPO Math & Wachter Productivity Paper
- Leiden Declaration & AI Slop in Research
- S&P 500 Rule Change / IPO Index Fund Risk
- The Illusion of Generative AI (World Science Festival, Web Summit)
- Trump AI Preflight Checks
- Commerce Export Control Critique
- Generative AI: The Tech Industry's Vietnam?

A new article titled "China catches up" (28 lines) argued that Chinese AI catching up validates the "no moat" thesis. The entity page had already documented this argument across 5+ sections with specific data points (FT ROI projections, GPU rental prices, tokenmaxxing backlash data).

## Detection Rule

If grep'ing the entity page for the article's key claim phrase returns **5+ section headings** covering the same argument, the density gradient is high — only genuinely novel data (new numbers, new sources, new empirical findings, new policy developments) warrants a reference. A new article from the same author restating a well-documented thesis is: **★★☆☆☆ skip**.

## Contrast with Other Patterns

| Pattern | Issue | Action |
|---------|-------|--------|
| "Mentioned ≠ covered" | Entity page lists article URL but lacks substance | **Enrich** — genuine gap |
| "Partial coverage" | Concept page covers product family but misses specific variant | **Enrich** — genuine gap |
| **Density gradient (this)** | Entity page is saturated on a thesis | **Skip** — article adds nothing new |

## When to Apply

Only applies when:
1. The candidate is from the **same author** whose entity page documents their views
2. The entity page has **200+ lines** of body content
3. The entity page has **3+ sections** on the same broad thesis
4. The article provides no new empirical data (no new numbers, sources, or specific claims)
