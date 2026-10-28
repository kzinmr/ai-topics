---
title: Anthropic Drug Development Program
created: 2026-10-28
updated: 2026-10-28
type: concept
tags: [ai-in-science, biotech, healthcare, drug-discovery, anthropic, ai-agents]
sources: [raw/articles/2026-10-27_anthropic-drug-development.md]
confidence: high
---

# Anthropic Drug Development Program

On **October 27, 2026**, Anthropic's **life sciences team** published its first substantial account of
using Claude to accelerate drug development. Over several months its scientists ran deep research
partnerships with **six organizations** developing new medicines — **BigHat Biosciences, Bristol Myers
Squibb, Divergence Labs, Enveda, Generate Biomedicines, and The Column Group** — and began drug
discovery of its own. The thesis: drug-development bottlenecks are **distributed** across the whole
process (target ID → molecule design → optimization → regulatory filings → trials), so the way to find
and remove them is to embed Claude deeply in many real programs, not to chase one "AI designs
molecules" problem. Anthropic plans to scale this up substantially.

## Case studies

### Generate Biomedicines — modality engineering (CAR T-cell)
Generate is re-engineering **CAR T-cell therapy** (historically for blood cancers) to treat **solid
tumors**, by shortening part of the therapy's genetic instructions to make room for cancer-specific
additions. Six scientists used **Claude Code** to propose designs. One design was **~70% shorter** than
standard and, in lab tests, let immune cells make **~10× as many receptors**, killed tumor cells more
efficiently, and stayed active longer.

### Divergence Labs — hit generation (food allergies)
Divergence is building drugs that **detach IgE from immune cells** entirely (vs standard meds that only
neutralize circulating IgE) — a two-"arm" design: one binds IgE tightly, another pries it off the cell.
Claude converted goals into a detailed design plan and then, **largely autonomously, generated ~35,000
antibody designs in ~a month**. Early tests found hits for both arms: **3** that bind IgE and **20** that
dislodge it (3 of the 20 dislodge better than the standard medication).

### BigHat Biosciences — lead optimization
BigHat pairs AI with an automated lab. Claude, connected to BigHat's lab data system **Reccy**, proposed
molecule changes; the lab made and tested **~1,010 variants in ~10 weeks**. Midway, the team suspected
the standard heat-stability and clumping metrics were misleading — Claude + an Anthropic researcher
reanalyzed raw data, proposed **new metrics + a protocol change**, and the main predictions held. Best
versions bound **>10× more tightly**; the cancer-targeting lead stayed in solution **18°C higher**; the
longer-lasting lead clumped **>100× more slowly**.

### Enveda — manufacturing and filings
Manufacturing chemists spent up to **75% of their time on paperwork**. Enveda connected all
manufacturing documents to Claude to flag issues. Over **1,061 pages**, Claude caught **all 11 issues**
human reviewers found **and flagged 7 they missed**, cutting human review time **89% (25h → <3h)**.
Separately Claude wrote first drafts of two regulatory documents — one took **4 hours vs ~3 months** by
hand.

### The Column Group (TCG) — company creation
TCG is establishing **Pleiades**, a new company that uses Claude to run many more (and more complex) drug
programs than is usual for a small team — a model for cutting both scientific and operational/admin
overhead. Its first Claude **skill** (assessing whether drug targets are worth pursuing) was evaluated on
**45 target-disease pairs**.

### Bristol Myers Squibb — clinical trial planning
BMS uses Claude to assess early-stage drug plans and estimate trial success likelihood from a single
prompt (an analysis that otherwise takes days), on sensitive data.

## Anthropic's own programs: Mithril Medicine

Anthropic acquired **Mithril Medicine**, a **one-person company** developing treatments for two rare
forms of **muscular dystrophy**. Founder **Cody Tranbarger** used Claude to organize contracts,
logistics, and experiments with **11 external labs**, taking a candidate from idea to promising **mouse
results in under 18 months**. Now at Anthropic, Tranbarger plans several new programs; if candidates
hold up, a drug could be ready for **human clinical trials as soon as late 2028**.

## Infrastructure & next steps

Most work is still **preclinical**. Anthropic is extending Claude into clinical trials and rolling out:
**Claude Science** (an AI workbench for researchers), **Claude credits for life scientists**, a **Life
Sciences Verification Program** (trusted orgs get more permissive safeguards to avoid impeding
legitimate bio research), and an **open call for guest investigators**.

## Significance

- Concrete, quantified agentic-AI wins across the *non-design* parts of drug development (docs, filings,
  lab-data reanalysis, hit generation) — the distributed-bottleneck thesis made tangible.
- Complements (and is distinct from) structure-prediction-driven players like [[entities/chai-discovery]]
  — this is **agentic workflow + reasoning** across the pipeline, not a
  structure/affinity foundation model.
- The **Life Sciences Verification Program** is a notable governance move: relaxes safety guardrails for
  vetted researchers, a dual-use trade-off.

## Related

- [[entities/chai-discovery]] — AI-native drug discovery (binding-affinity models)
- [[concepts/claude-science]] — Anthropic's AI workbench for life sciences
- [[entities/anthropic]]
- [[concepts/agent-skills]] — Pleiades' first Claude skill
- [[concepts/agentic-engineering]]
- [[entities/openai]] — parallel frontier-lab science push (offline RL, math)
