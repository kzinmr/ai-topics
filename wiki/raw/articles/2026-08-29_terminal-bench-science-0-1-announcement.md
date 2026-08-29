---
source_url: https://www.terminal-bench-science.ai/announcement
ingested: 2026-08-29
sha256: 855072d6e8a2553f931102037aceacc9d0ae666901900a90927a3c9b237e399d
---

# Terminal-Bench-Science 0.1 — Announcement (fetched 2026-08-29)

URL: https://www.terminal-bench-science.ai/announcement
HN discussion: https://news.ycombinator.com/item?id=49472820 (115 pts, Aug 28 2026)

Terminal-Bench-Science evaluates AI agents on workflows from researchers' own work.
Scientists, not model developers or data vendors, set the bar for scientific capability in AI.

Terminal-Bench-Science is a benchmark led by researchers at Stanford University and built by
the team behind Terminal-Bench in collaboration with domain experts from a range of scientific
disciplines and research institutions around the world. It measures the AI agent capabilities
through a diverse set of challenging, expert-curated workflows drawn from scientific research.
Terminal-Bench-Science is a continuous benchmark that evolves alongside frontier AI, creating a
feedback loop between scientific needs and AI development.

Our first release includes 70 tasks from the life, physical, Earth, mathematical, and
engineering sciences. The strongest model evaluated, Claude Opus 5, achieves a 30% resolution
rate on Terminal-Bench-Science 0.1.

## Terminal-Bench-Science 0.1 Leaderboard (resolution rates, 70 scientific workflow tasks)

| Model / Harness | Resolution rate |
|---|---|
| Claude Opus 5 (Claude Code) | 30.0% |
| GPT-5.6 Sol (Codex) | 22.4% |
| Claude Fable 5 (Claude Code) | 21.4% |
| Claude Opus 4.8 (Claude Code) | 10.5% |
| GPT-5.6 Terra (Codex) | 8.6% |
| GLM 5.3 (Claude Code) | 8.1% |
| Kimi K3 (Claude Code) | 7.1% |
| Grok 4.6 (Grok Build) | 7.1% |
| GPT-5.6 Luna (Codex) | 3.3% |

## Overview (key claims)

- While Terminal-Bench drove progress for software-engineering agents, Terminal-Bench-Science
  brings the same ambition to science: agents that execute technically demanding, time-consuming
  research workflows, freeing scientists for hypothesis formation, interpretation, validation,
  and communication.
- Three design principles:
  1. **Benchmarks drawn from real scientific workflows** — contributed by practicing scientists,
     not textbook questions or standardized exercises. "The stakes in science are too high, and
     its benchmarks must reflect the scientific community's priorities rather than outside interests."
  2. **Verifiable evidence** — agents evaluated in realistic environments; graded on concrete
     artifacts (analyses, simulations, proofs, code, data products) with reproducible,
     task-specific tests.
  3. **Continuous benchmark** — regular releases; scientists contribute new workflows and improve
     tasks, creating a feedback loop between scientific needs and AI development. (Contrast:
     scientific benchmarks are usually "treated as papers to publish", released once and abandoned.)
- Tasks span scientific data analysis, statistical inference, and related workflows across five
  domains: life, physical, Earth, mathematical, and engineering sciences.
