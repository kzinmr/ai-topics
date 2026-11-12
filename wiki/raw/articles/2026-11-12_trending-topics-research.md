# Active Crawl Research Note — 2026-11-12

> Trend-gap scan across blogwatcher DB (last 48h), wiki coverage check, and candidate triage.
> Selected 3 FULL-gap topics for page creation; 2 candidates noted as covered/partial.

## Selected topics (FULL gap)

### 1. gVisor donated to CNCF; Modal joins as maintainer
- Source: https://modal.com/blog/modal-gvisor-maintainer (Modal Blog, Ayush Ranjan & Luis Capelo, Nov 11 2026)
- Raw: `raw/articles/2026-11-12_modal_gvisor-cncf-maintainer.md`
- Facts: Google donates gVisor (name + trademarks) to CNCF at KubeCon SLC; maintainer-led governance; Modal + Ant Group + Tines join maintainers; OpenAI, Tencent, NVIDIA continue contributing. Modal runs 40M gVisor containers/day; 25ms boot, 12MB overhead; nvproxy GPU ioctl validation; cuda-checkpoint sandbox checkpoint/restore.
- Gap check: no page matching "gvisor" in concepts/entities/events. Directly relevant to agent sandboxing literature ([[concepts/agent-sandbox-patterns]], CVE-2026-55607 sandbox escape).
- Action: create `concepts/gvisor.md`.

### 2. Anthropic IPO roadshow compute strategy (multi-chip + compute multipliers + Mythos AMD port)
- Source: https://simonwillison.net/2026/Nov/11/anthropic-ipo-roadshow/ (Nov 11 2026; roadshow started Nov 10)
- Raw: `raw/articles/2026-11-12_simonw_anthropic-ipo-roadshow-compute.md`
- Facts: train+serve across 4 chip families (Trainium/TPU/NVIDIA/AMD); Mythos ported Claude to AMD in 3 days ~100% kernels written by Claude; "total effective compute = physical capacity × compute multipliers"; multipliers stack; RSI claim "Claude will be able to discover compute multipliers entirely by itself".
- Gap check: no `anthropic-ipo*` page; Gary Marcus IPO commentary mentioned in log but no page.
- Action: create `events/anthropic-ipo-roadshow-2026.md`.

### 3. Gemini Decision 1 — Google enters the decision-model category
- Source: https://simonwillison.net/2026/Nov/11/gemini-decisions-api/ (Nov 11 2026)
- Facts: Google joins Jev (TypeSafe) and OpenAI GPT-6 Luna in decision models; same 3 question types (yes/no, choice, rubric-scoring); reuses Jev's "Noul" term; priced $0.10/MTok input, output free (same as Luna; Jev cheapest at $0.042/MTok); fully multimodal (text/image/audio/video/PDF) vs Jev text-only and Luna text+image; returns non-saturated probabilities (0.0498/0.9234) vs Jev/Luna 1.0/0.0.
- Gap check: `concepts/system-one-models.md` exists (Jev-class concept, updated Oct 20) — PARTIAL; decision-model family page missing.
- Action: create `entities/gemini-decision-1.md` + enrich `concepts/system-one-models.md` with the three-vendor pricing/capability table.

## Rejected candidates

- **lcamtuf "It came from the token void!"** (blog.coredump.cx, Nov 11) — image-only comic post mocking AI-industry tropes (below-cost tokens, unscanned books, IPO, space data centers). No substantive text; fails Page Thresholds. Skip.
- **Nvidia board / Jensen Huang ouster reports** (Semafor/WSJ/Bloomberg via Daring Fireball, Nov 11-12) — breaking news, paywalled primary sources, unconfirmed single-story; needs confirmation before page. Noted for follow-up in `entities/nvidia` if confirmed.
- **AI Engineer conference talks** (Duolingo 225K agent-written tests; Maersk maintenance costs; Anthropic Claude Code best practices rethink) — YouTube videos; x-accounts/blog pipelines cover transcripts separately. Deferred.
