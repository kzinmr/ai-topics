---
title: "Thariq Shihipar"
created: 2026-06-02
updated: 2026-06-03
type: entity
tags:
  - person
  - anthropic
  - claude-code
  - harness-engineering
  - agent-communication
  - developer-tooling
  - developer-experience
  - html
  - agent-skills
  - agent-orchestration
  - interpretability
  - activation-steering
  - entrepreneur
aliases:
  - trq212
  - Thariq
sources:
  - raw/articles/2026-06-02_trq212_dynamic-workflows-claude-code.md
  - raw/articles/2026-05-08_trq212_unreasonable-effectiveness-html.md
  - raw/articles/2026-03-17_trq212_lessons-building-claude-code-skills.md
  - raw/articles/2026-01-29_trq212_making-playgrounds-using-claude-code.md
  - raw/articles/thariq-shihipar-interpretability.md
  - raw/articles/thariq-shihipar-entropix.md
  - raw/articles/2024-10-11_thariq-entropix-explained.md
  - raw/articles/thariq-shihipar-claude-computer-use-is-vision-the-ultimate-api.md
  - raw/articles/thariq-shihipar-llm-powered-sorting-with-trueskill.md
  - raw/articles/thariq-shihipar-fast.md
  - raw/articles/thariq-shihipar-sparse-rewards.md
  - raw/articles/thariq-shihipar-spiritual-technology.md
  - raw/articles/thariq-shihipar-intention.md
  - raw/articles/thariq-shihipar-clay-and-light.md
  - raw/articles/thariq-shihipar-the-thing.md
  - raw/articles/thariq-shihipar-a-lovely-autumn-night.md
x_handle: trq212
x_id: "352806502"
---

# Thariq Shihipar

**Thariq Shihipar** (@trq212) is a Member of Technical Staff at [[entities/anthropic|Anthropic]] working on [[entities/claude-code|Claude Code]]. He is a builder, writer, and reflective practitioner — simultaneously a core engineer of Anthropic's flagship agent product and one of its most articulate advocates, writing deeply about agent communication design (HTML-first output), the Claude Code Skills system, dynamic agent workflows, interpretability for developers, and the craft of building with AI.

## Overview

Shihipar occupies a distinctive position in the AI engineering world. Few engineers at major labs both build production-scale agent infrastructure AND publish at the frequency and quality he does across his personal blog (thariq.io). His writing spans hard technical topics (Entropix adaptive sampling, TrueSkill-powered LLM evaluation, activation steering) and philosophical reflection (minimalism, intention, the nature of courage), earning him a broad and engaged following on X (@trq212, 10M+ impressions on a single post).

He co-authored two landmark Claude Code articles in rapid succession: "Using Claude Code: The Unreasonable Effectiveness of HTML" (May 2026, 14K+ likes, 10M+ impressions) and "A Harness for Every Task: Dynamic Workflows in Claude Code" (June 2026). Both were endorsed by major figures — Andrej Karpathy positioned the HTML thesis as step 3 in a progression (text → markdown → HTML → neural video), and Simon Willison reconsidered his long-held Markdown default after reading it.

## Background

- **Current role**: Member of Technical Staff at Anthropic, working on Claude Code (2024–present)
- **Previous**: Y Combinator Winter 2020 (YC W20), South Park Commons, MIT Media Lab
- **X/Twitter**: [@trq212](https://x.com/trq212) (account since 2011)
- **Blog**: [thariq.io](https://www.thariq.io)
- **GitHub**: [thariqs](https://github.com/thariqs) — companion site for HTML effectiveness demos

## Key Contributions

### Dynamic Workflows in Claude Code (June 2026)
Co-authored "A Harness for Every Task: Dynamic Workflows in Claude Code" with Sid Bidasaria (@sidbid). This introduced the ability for Claude to dynamically generate custom agent harnesses (JavaScript files) at runtime, enabling patterns like classify-and-act, fan-out-and-synthesize, adversarial verification, generate-and-filter, tournament, and loop-until-done. The article identified three core failure modes that dynamic workflows address: **agentic laziness** (stopping before finishing multi-part tasks), **self-preferential bias** (preferring its own results when asked to verify), and **goal drift** (loss of fidelity to original objectives across compaction cycles).

### HTML-First Agent Output (May 2026)
Published "Using Claude Code: The Unreasonable Effectiveness of HTML" on both X and the official Anthropic blog. The thesis: HTML is the right medium for the agent-to-human output surface, replacing Markdown as the default. Five arguments: (1) information density (tables, CSS, SVG, JS, interactive elements), (2) visual clarity and ease of reading, (3) ease of sharing via links, (4) two-way interactions (sliders, knobs, copy-buttons), and (5) rich data ingestion from Claude Code's context sources. Companion site: [thariqs.github.io/html-effectiveness/](https://thariqs.github.io/html-effectiveness/) with 20 self-contained HTML demos across 8 categories. Endorsed by Andrej Karpathy and Simon Willison.

### Claude Code Skills System (March 2026)
Published "Lessons from Building Claude Code: How We Use Skills" (16K+ likes, 6.8M+ views). Cataloged hundreds of skills in active use at Anthropic into 9 role patterns: Library/API Reference, Product Verification, Data Fetching, Business Process, Code Scaffolding, Code Quality, CI/CD, Runbooks, Infrastructure Ops. Emphasized that skills are not "just markdown files" — they are folders with scripts, assets, and configuration options including dynamic hooks.

### Playgrounds Plugin (January 2026)
Co-created and published the Claude Code Playgrounds plugin, which helps Claude generate standalone HTML files for interactive visualization and problem-solving. Demonstrated use cases: architecture diagrams with comments, component design tweaking, game balance adjustment, writing critique interfaces. The "disposable micro-app" pattern — throwaway UIs with an export button to copy results back into Claude Code.

### Interpretability for Developers (November 2024)
Published "Should Developers Care about Interpretability?" (thariq.io). Argued that activation steering offers developers fine-grained control over model behavior at inference time — going beyond prompting and RLHF. Identified four applications: style capture beyond text description, RLHF-reduction via targeted feature steering, persistent user preference memory, and cheap reproducible classification.

### Entropix Explainer (October 2024)
Wrote "Detecting when LLMs are Uncertain — Entropix Explained," the definitive explainer of XJDR's (@_xjdr) Entropix project. Introduced the entropy/varentropy quadrant framework for adaptive sampling: (1) low ent/low vent → argmax, (2) low ent/high vent → branching, (3) high ent/low vent → thinking tokens, (4) high ent/high vent → high-temp resampling.

### Claude Computer Use & Vision API (October 2024)
Published "Claude Computer Use — Is Vision the Ultimate API?" exploring computer use capabilities and the thesis that vision-based interaction may supersede traditional APIs for agent-computer interaction.

### LLM Evaluation with TrueSkill (February 2025)
Published "LLM-Powered Sorting with TrueSkill" exploring the use of Microsoft's TrueSkill ranking algorithm for comparative LLM evaluation via pairwise comparison tournaments.

## Blog Overview (thariq.io)

Shihipar maintains a personal blog at [thariq.io](https://www.thariq.io) with articles spanning technical AI engineering and personal philosophy:

| Date | Article | Theme |
|------|---------|-------|
| 2026-06-02 | A Harness for Every Task: Dynamic Workflows in Claude Code | Agent orchestration |
| 2026-05-08 | Using Claude Code: The Unreasonable Effectiveness of HTML | Agent output design |
| 2026-03-28 | Clay and Light | Two modes of being |
| 2026-03-17 | Lessons from Building Claude Code: How We Use Skills | Agent skill engineering |
| 2026-02-22 | A Lovely Autumn Night | Ambition shift |
| 2026-02-14 | The Thing | Courage bottleneck |
| 2026-01-29 | Making Playgrounds using Claude Code | Interactive agent UIs |
| 2026-01-20 | I can think. I can wait. I can fast. | Minimalism, wanting less |
| 2025-12-06 | Sparse Rewards: Enlightenment and Reinforcement Learning | RL parallels to life |
| 2025-12-06 | Spiritual Technology | Systematic self-improvement |
| 2025-11-17 | Intention | Nature of intention, accountability |
| 2025-02-11 | LLM-Powered Sorting with TrueSkill | LLM evaluation |
| 2024-11-04 | Should Developers Care about Interpretability? | AI interpretability & steering |
| 2024-10-24 | Claude Computer Use — Is Vision the Ultimate API? | Computer use, vision API |
| 2024-10-11 | Detecting when LLMs are Uncertain (Entropix) | Adaptive sampling |

## Lenny's Podcast Appearance (May 2026)

Appeared on Lenny's Podcast (live at Anthropic) with the segment title "HTML is the New Markdown." Key takeaways included:

- **Compute allocator paradigm**: ~1% of tokens go to production code; the vast majority go to dashboards, custom interfaces, weekly status updates, and tools for understanding what to build
- **The output surface as a first-class design problem** — not an afterthought to agent engineering
- **Micro software on top of micro software** — agents building disposable UIs for specific tasks, then discarding them
- **Simple prompts over elaborate system prompts** — "Create an HTML file with a plan. Help me visualize. Include excerpts, mockups, code, whatever is needed to give me maximum context"

## Writing Style & Philosophy

Shihipar's writing is distinguished by a rare combination of deep technical substance and reflective, almost meditative clarity. His technical articles (Entropix, interpretability, Skills) are thorough and code-grounded, while his philosophical pieces (Clay and Light, Sparse Rewards, Spiritual Technology) draw on Islamic philosophy, Zen Buddhism, and his own experiences as an entrepreneur and engineer. This dual nature — hard engineering and philosophical introspection — gives his writing unusual breadth and authenticity.

His technical philosophy centers on **trusting the agent with more creative freedom** rather than constraining it: "I've found that the real ceiling on what a model can produce is not the model's capabilities — it's the space I give it to explore." This manifests in his HTML-first advocacy (giving the agent richer output modalities), dynamic workflows (letting Claude design its own harness), and the disposability ethic (throwaway micro-apps are better than perfect reusable tools).

## Related Entities

- [[entities/trq212]] — Sub-entity page focused on his HTML-first philosophy (launched May 2026)
- [[entities/anthropic]] — Employer
- [[entities/claude-code]] — The agent platform he builds on
- [[entities/andrej-karpathy]] — Endorsed HTML thesis; proposed text→markdown→HTML→neural video progression
- [[entities/simon-willison]] — Reconsidered Markdown default after reading Shihipar's article
- Sid Bidasaria (@sidbid) — Co-author on dynamic workflows
- [[entities/xjdr]] — Creator of Entropix, which Shihipar explained and popularized

## Related Concepts

- [[concepts/dynamic-workflows]] — Co-created the capability and published the defining article
- [[concepts/ai-output-format-progression]] — HTML as the next evolution in agent output formats
- [[concepts/claude-code-skills]] — Cataloged 9 role patterns from hundreds of internal Anthropic skills
- [[concepts/entropix]] — Authored the definitive explainer of adaptive sampling via entropy/varentropy
- [[concepts/activation-steering]] — Wrote "Should Developers Care about Interpretability?" bridging research and practice
- [[concepts/agent-communication]] — Output surface as a first-class design problem
- [[concepts/llm-core]] — TrueSkill-powered LLM evaluation technique
- [[concepts/harness-engineering]] — His work on dynamic workflows is a direct expression of harness engineering ("Agent = Model + Harness")

## Graph Structure Query

```
[thariq-shihipar] ──works-at──→ [entity: anthropic]
[thariq-shihipar] ──builds──→ [entity: claude-code]
[thariq-shihipar] ──coauthors──→ [entity: sid-bidasaria]
[thariq-shihipar] ──wrote──→ [concept: dynamic-workflows]
[thariq-shihipar] ──wrote──→ [concept: ai-output-format-progression]
[thariq-shihipar] ──wrote──→ [concept: claude-code-skills]
[thariq-shihipar] ──explains──→ [concept: entropix]
[thariq-shihipar] ──embodies──→ [concept: harness-engineering]
[thariq-shihipar] ──influenced──→ [entity: simon-willison]
[thariq-shihipar] ──influenced──→ [entity: andrej-karpathy]
```

## Sources

- [raw/articles/2026-06-02_trq212_dynamic-workflows-claude-code.md] — "A Harness for Every Task: Dynamic Workflows in Claude Code"
- [raw/articles/2026-05-08_trq212_unreasonable-effectiveness-html.md] — "Using Claude Code: The Unreasonable Effectiveness of HTML"
- [raw/articles/2026-03-17_trq212_lessons-building-claude-code-skills.md] — "Lessons from Building Claude Code: How We Use Skills"
- [raw/articles/2026-01-29_trq212_making-playgrounds-using-claude-code.md] — "Making Playgrounds using Claude Code"
- [raw/articles/thariq-shihipar-interpretability.md] — "Should Developers Care about Interpretability?"
- [raw/articles/thariq-shihipar-entropix.md] / [2024-10-11_thariq-entropix-explained.md] — "Detecting when LLMs are Uncertain (Entropix)"
- [raw/articles/thariq-shihipar-claude-computer-use-is-vision-the-ultimate-api.md] — "Claude Computer Use — Is Vision the Ultimate API?"
- [raw/articles/thariq-shihipar-llm-powered-sorting-with-trueskill.md] — "LLM-Powered Sorting with TrueSkill"
- [thariq.io](https://www.thariq.io) — Personal blog
- [trq212 X/Twitter](https://x.com/trq212) — @trq212
- [HTML Effectiveness Companion Site](https://thariqs.github.io/html-effectiveness/) — 20 self-contained HTML demos
