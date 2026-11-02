---
title: "China MOFCOM Announcement No. 48 — First Frontier AI Export Controls"
type: concept
created: 2026-11-02
updated: 2026-11-02
confidence: medium
tags:
  - geopolitics
  - china
  - policy
  - governance
  - ai-governance
  - agent-safety
sources:
  - raw/articles/2026-11-02_csa_china-frontier-ai-export-controls-48.md
related:
  - concepts/us-china-ai-competition
  - concepts/claude/fable-5
  - concepts/sovereign-ai
---

# China MOFCOM Announcement No. 48 — First Frontier AI Export Controls

On **October 16, 2026**, China's Ministry of Commerce (MOFCOM) and Ministry of Science and Technology (MOST) issued **Announcement No. 48 of 2026**, proposing to add 40 technologies to the Catalogue of Technologies Prohibited or Restricted from Export — **23 of them in AI** — and imposing an interim pre-export registration requirement that is **already in effect**. The catalogue draft is open for comment until **November 15, 2026** [1][2].

This is China's first time placing frontier AI itself (model weights, agent architectures, AI-enabled offensive cyber capability) under outbound export control. Combined with U.S. measures (see the June 12, 2026 Fable 5 suspension directive in [[concepts/claude/fable-5]]), **frontier AI supply chains now face formal outbound controls from both of the largest AI-producing jurisdictions** — with each regime drawing its lines at different control points: the U.S. at compute and service access, China at weight custody and local deployment.

> Confidence note: this page summarizes the Cloud Security Alliance AI Safety Initiative research note (Oct 23, 2026), which cites the official MOFCOM annex [1], the MOFCOM spokesperson Q&A [2], and analyses from ChinaTalk [3], Geopolitechs [4], and Ray Sun / Ctrl+AI+Reg [5]. Legal interpretations (especially ChinaTalk's reading of the registration form) are analyst inference, not official statements.

## Two instruments, two legal statuses

| Instrument | Status | Scope |
|---|---|---|
| Catalogue additions (40 items: 14 prohibited, 26 restricted — 23 AI, 5 biomedicine, 12 photovoltaics) | **Draft**, comment window until 2026-11-15 | Future licenses for restricted tech; ban for prohibited tech |
| Interim pre-export registration | **In effect since Oct 16**, including exports started but not completed | Register via MOFCOM platform before exporting listed technology |

Registration triggers: (1) transfer of technology ownership abroad, (2) licensing domestic technology for overseas use, (3) change of ownership/control making a foreign entity owner/controller, (4) other cases MOFCOM designates. Exporters self-scope whether a technology falls in scope [2][4].

## What the AI annex controls

| Category | Control | Key thresholds (draft) |
|---|---|---|
| Large models trained on China's "core data" | Prohibited | Scope per Data Security Law |
| Large models trained on "important data" | Restricted | De minimis carve-out: ≤0.1% trace use of desensitized data that doesn't materially improve capability |
| **Core large-model tech** (weights, checkpoints, source code, architecture, training/inference know-how) | Restricted | Any ONE of: ≥10²⁶ FLOPs training compute; ≥2T parameters; **global top-10** on public eval rankings or call volume at time of export |
| **Agents** (planning, multi-agent coordination, tool use, game-theoretic decision) | Restricted | Above set benchmarks; defined by **system behavior, not the model** |
| High-performance agents for critical infrastructure / defense / core government | Prohibited | Meets restricted-agent thresholds + specially designed for those uses |
| AI red-teaming / vulnerability discovery / offensive code generation | Restricted–Prohibited | Offensive code generation could not be exported at all |
| AI detection (deepfake, steganography, voiceprint) | Restricted/Prohibited | e.g. ≥95% accuracy+recall for cross-border data-security detection; ≥98% deepfake detection |
| AI/memory chip design; large compute clusters | Restricted | Process ≤14 nm; interconnect ≥800 GB/s; clusters >10,000 accelerators |
| Already public via open source or academic publication | **Outside management** | — |

Three structural features matter:

1. **The "global leading" test is dynamic.** A model below compute/parameter thresholds becomes restricted if its eval rank or call volume is top-10 at export time. ChinaTalk calls this "by far the most up-for-interpretation" — the rule names no ranking body [3]. Compliance status of a deployed model version can change after deployment.
2. **Agent items are defined by system behavior** (planning depth, concurrency, tool count), not the underlying model. An orchestration framework integrating hundreds of tools could be controlled even running a sub-frontier model — an issue Ray Sun flags as unresolved [5].
3. **The cyber items carry direct security consequences**: Chinese-origin AI red-teaming/vuln-discovery tools meeting thresholds need a license to leave China.

The 10²⁶ FLOP threshold mirrors the 2023 U.S. executive order and the since-rescinded 2025 U.S. AI Diffusion rule; ChinaTalk estimates **no released Chinese model currently exceeds it** [3].

## The custody line: service vs. self-hosting

MOFCOM's central test is whether restricted technology moves from inside China to overseas. The practical consequence: **API/SaaS access is uncontrolled; local deployment of weights is controlled** — inverting the U.S. pattern.

| Deployment scenario | Treatment |
|---|---|
| API calls, apps/websites, SaaS for overseas customers | Not in export management |
| Lightweight on-device deployment | Not in export management |
| **Local deployment of a restricted model outside China** | **Within export management; license required** |
| Chinese company's self-operated overseas cloud | Automatic licensing ("report and export") may apply |
| Open-sourcing a newly developed restricted technology | Automatic licensing after reporting |
| Already public (open source / papers) | Outside scope |

The captured scenario — self-hosting — is precisely the one enterprises chose for data-protection reasons. Because licenses can be revoked or conditioned, ChinaTalk suggests non-Chinese users may reconsider such dependencies [3]. "Open source" is undefined; restricted-use license treatment is unclear — organizations depending on successive Chinese open-weight releases should treat **release cadence, not just current availability, as a variable outside their control**.

## Corporate-structure exposure

The most surprising exposure for multinationals sits in org charts: registration is triggered by licensing and changes of control, not only third-party sales. China-based R&D teams sharing agent frameworks or fine-tuned models with overseas affiliates may need registration — ChinaTalk reads the form's "exports made outside formal contracts" field as potentially capturing **intra-group code sharing** [3] (analyst inference). Precedent: MOFCOM's January 2026 assessment of Meta's acquisition of Manus (Singapore-registered, China-developed) examined whether relocating staff/technology required export authorization [7]; Announcement No. 48 now gives that scrutiny explicit agent-specific thresholds.

## Enterprise implications (from the CSA note)

- Inventory every Chinese-origin model/agent framework/security tool and record **how it is consumed** (API/SaaS vs. on-device vs. locally deployed weights); local deployment is the priority category.
- Ask suppliers in writing whether they registered under Announcement No. 48 and whether a license will be needed once the catalogue is final.
- Review all technology flows out of China-based subsidiaries/R&D since Oct 16, including code repos, checkpoints, agent frameworks.
- Treat restricted-category Chinese models as regulated dependencies with documented fallbacks; allocate registration/license responsibility in vendor contracts (including whether updates and new checkpoints are covered).
- Extend Data Security Law classification to training/fine-tuning datasets, not just data transfers.
- Model export-control disruption **from either jurisdiction** as a standing risk scenario; design architectures that can swap models without rebuilding agent workflows.

Timing note: the comment window closes shortly before an expected leaders' meeting at APEC, which could bear on final scope [3] — revisit once MOFCOM publishes the final text.

## Related

- [[concepts/us-china-ai-competition]] — the bilateral competition frame; this is China's first symmetric outbound-control instrument
- [[concepts/claude/fable-5]] — the U.S. precedent: June 12, 2026 export-control directive suspending a deployed commercial frontier model worldwide
- [[concepts/sovereign-ai]] — the sovereignty-risk framing of frontier-model access as a contingent dependency
- [[concepts/china-agentic-coding-sprint]] — Chinese agent ecosystem now subject to agent-specific outbound thresholds

## Sources

- Cloud Security Alliance AI Safety Initiative, "China's First Frontier AI Export Controls: MOFCOM Announcement No. 48" (2026-10-23) — raw: `raw/articles/2026-11-02_csa_china-frontier-ai-export-controls-48.md` (HN 41, 2026-11-02)
- Primary: MOFCOM/MOST Announcement No. 48 of 2026 + Annex 1 (draft); MOFCOM spokesperson Q&A (Oct 16, 2026)
- Secondary: ChinaTalk (Ennis, Zhang, Ottinger, Zakaria, Oct 21); Geopolitechs (Oct 16); Ray Sun, Ctrl+AI+Reg (Oct 19)
