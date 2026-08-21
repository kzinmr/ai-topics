---
type: x_post
source: https://x.com/ctatedev/status/2090108489901240808
author: "@ctatedev"
date: 2026-08-19
tags: [coding-agents, harness-engineering, open-source, zig, glm]
related: [entities/chris-tate, entities/glm-5-zai]
---

# fx — Tiny, open, native coding agent — @ctatedev tweet

**Tweet (2026-08-19):** "Free, open source harness¹ / Free, open weights model thru Aug 27² / What a time to be alive. ¹ https://fx.sh ² GLM-5.2 via @blackboxai"

Chris Tate (Vercel) pointing out a pairing: **fx** (a free open-source coding-agent harness) + **GLM-5.2** (a free open-weights model, free via BlackboxAI through Aug 27). A fully open stack for agentic coding.

## fx (fx.sh)
- **What:** a coding agent **harness and CLI written in Zig**, "tiny, open, native." Apache-2.0. Model-agnostic; works for local and cloud inference.
- **Design goal:** minimalism + performance. 6.39 MiB binary, cold start ~10 µs, "no unnecessary" work. CLI output form factor is closer to a **Unix shell** than a heavy "IDE-in-the-terminal" TUI.
- **Optimized for research and embeddability** as part of larger systems; SDK aspects fully configurable.
- **v0.0.5** at time of post — marked *experimental* ("use at your own risk, frequent changes").
- Browser demo runs the full fx CLI compiled to **WebAssembly** (Zig toolchain); a browser workspace powered by `just-bash`, networking via `browser fetch`. Default model in demo: `glm-5.2`.
- Install: `curl -fsSL https://fx.sh/setup.sh | bash`.

## Sources
- Tweet: https://x.com/ctatedev/status/2090108489901240808
- fx.sh: https://fx.sh
- GLM-5.2: [[entities/glm-5-zai]]
