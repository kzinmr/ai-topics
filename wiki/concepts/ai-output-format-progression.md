---
title: "AI Output Format Progression"
tags:
  - concept
  - agent-communication
  - developer-tooling
  - human-in-the-loop
created: 2026-05-11
updated: 2026-05-11
type: concept
parent_concepts: [agent-communication, human-ai-interaction]
---

# AI Output Format Progression

A framework by **Andrej Karpathy** (May 2026) describing the evolution of AI output modalities, from raw text to neural-generated interactive simulations. The framework positions **HTML as the emerging next default output format** for AI agents — moving beyond Markdown's limitations.

## The Progression Ladder

| Stage | Format | Characteristics | Status |
|-------|--------|----------------|--------|
| 1 | **Raw text** | Hard/effortful to read; no formatting | Legacy |
| 2 | **Markdown** | Bold, italic, headings, tables; ASCII diagrams | **Current default** |
| 3 | **HTML** | Rich graphics, layout, interactivity, SVG, two-way interaction | **Emerging new default** |
| ... | Intermediate stages | Gradual blending of procedural and neural | Future |
| n | **Interactive neural videos/simulations** | Diffusion-generated, fully interactive | Extrapolated endpoint |

## Core Thesis: Audio In, Vision Out

Karpathy's framing: **audio is the human-preferred input** to AIs (speaking is faster than typing), while **vision is the preferred output** — roughly one-third of the human brain is a massively parallel processor dedicated to vision, making it the "10-lane superhighway" of information into the brain.

As AI capabilities improve, output modalities should leverage this visual bandwidth more effectively.

## The Case for HTML (Stage 3)

**Thariq Shihipar** (Claude Code team, Anthropic) provided the practical case in "The Unreasonable Effectiveness of HTML" (May 2026):

- **Information density**: HTML can represent tabular data, SVG diagrams, interactive widgets, design data, code snippets, spatial data, and images — all in a single self-contained file
- **Visual clarity**: Complex plans and specs are actually read when rendered as HTML vs ignored as 100+ line Markdown files
- **Shareability**: HTML files render natively in any browser; Markdown requires special viewers
- **Two-way interaction**: Sliders, knobs, draggable cards, copy-to-clipboard — the document becomes an editing interface
- **Data ingestion**: Claude Code can pull context from the file system, MCPs (Slack, Linear), browser, and git history to enrich HTML output
- **Token efficiency**: With 1M+ context windows (Opus 4.7), HTML's token overhead is negligible compared to the expressiveness gain

**Trade-off**: HTML generation takes 2-4x longer than Markdown, and version control diffs are noisy.

## Shihipar's 8 Use Case Categories

1. **Exploration & Planning** — Side-by-side code approach comparisons, visual design directions, implementation plans with timelines
2. **Code Review & Understanding** — Annotated PRs with severity tags, PR writeups, module maps as boxes-and-arrows
3. **Design** — Living design system swatches, component variant contact sheets
4. **Prototyping** — Animation sandboxes with sliders, clickable interaction flows
5. **Illustrations & Diagrams** — SVG figure sheets, annotated flowcharts
6. **Decks** — Arrow-key slide decks from `<section>` tags + 20 lines of JS
7. **Research & Learning** — Feature explainers with collapsible sections, concept explainers with live rings
8. **Reports** — Weekly status with charts, incident timelines

## "Software 1.0" + Neural Artifacts (Stage n)

Karpathy's extrapolated endpoint involves blending **procedural "Software 1.0" artifacts** (interactive simulations, deterministic logic) with **neural artifacts** (diffusion grids, learned patterns). This represents a fundamental shift from discrete output formats to continuous, interactive neural experiences.

Key open question: how to weave together exact/procedural elements with neural/diffusion elements in a coherent output.

## Input Gap

Karpathy notes that current input modalities (audio, text, video) are insufficient alone — pointing, gesturing, and screen-sharing are natural human collaboration behaviors that haven't been well-integrated into AI interfaces yet. Addressing these gaps is achievable well before neuralink-style BCIs.

## Practical Adoption

**Simon Willison** demonstrated the approach with a GPT-5.5 experiment: `curl https://copy.fail/exp | llm -m gpt-5.5 -s 'Explain this code... Output HTML...'` — producing an interactive HTML explanation of a Linux kernel exploit.

Shihipar emphasizes that no special skill or tool is needed — just ask the LLM to "make a HTML file" or "structure your response as HTML."

## Related Concepts

- [[concepts/agent-communication]] — How AI agents communicate with humans and each other
- [[concepts/prompt-engineering]] — Prompting techniques, including output format specification
- [[concepts/vibe-coding]] — Natural language as programming interface (Karpathy)
- [[concepts/agentic-engineering]] — Managing multiple AI agents (Karpathy)

## Key People

- [[entities/thariq-shihipar]] — Originated the practical HTML advocacy for Claude Code
- [[entities/andrej-karpathy]] — Provided the progression framework and "audio in, vision out" thesis
- [[entities/simon-willison]] — Early adopter and demonstrator

## References

- [[raw/articles/2026-05-08_trq212_unreasonable-effectiveness-html]] — Shihipar's full X Article
- [[raw/articles/2026-05-11_karpathy_html-and-vision-progression]] — Karpathy's Note Tweet response
- [[raw/articles/2026-05-08_simonwillison_unreasonable-effectiveness-html]] — Willison's blog post
- Companion site: https://thariqs.github.io/html-effectiveness/ (20 self-contained .html demos)
