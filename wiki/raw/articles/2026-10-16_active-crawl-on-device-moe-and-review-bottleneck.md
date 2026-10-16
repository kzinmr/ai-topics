---
ingested: 2026-10-16
type: active-crawl-research-note
sources:
  - https://www.liquid.ai/blog/lfm2-5-24b-a2b
  - https://arstechnica.com/ai/2026/10/ai-coding-agents-generate-more-code-but-not-more-software/
  - https://atoll92.github.io/agent-standup/
  - https://momo5502.com/posts/2026-10-09-game-decompilation/
  - https://www.csoonline.com/article/4234854/ai-agents-arent-going-rogue-frontier-labs-are-skipping-security-basics.html
sha256: 90301c119bc7a57523c1a343590020072c22d7c61bcfbfabc7e9df5ad8245c29
---

# Active Crawl Research Note — 2026-10-16

## Topic 1 — Liquid AI LFM2.5-24B-A2B (on-device agent MoE)

Source: https://www.liquid.ai/blog/lfm2-5-24b-a2b (2026-10-14)

- Open-weight **24B-parameter reasoning model with 2B active parameters**, built for
  fast, private **on-device agents**. Largest + final model in the LFM2.5 family
  (spans LFM2.5-230M → 24B-A2B, two orders of magnitude).
- Competitive with **Qwen3.6-35B-A3B** (~50% more total and active params) on 5 of 8
  agentic/tool-use benchmarks: **48.09 on LiveClaw** vs 38.19; **27.69 on
  AutomationBench** vs 8.72.
- Only 2B active params → up to **1.7× faster** than comparable MoEs on-device;
  **184 tok/s on Apple M5 Max**, up to **21K output tok/s on a single NVIDIA B300**.
- Base (`-Base`) and post-trained models open-weight on Hugging Face + Playground.
- Architecture: keeps 40 layers, 64 experts per MoE block, top-4 routing, hybrid of
  **gated short convolutions + GQA**. Changes vs LFM2-24B-A2B: context 32,768 →
  131,072; **in-place tokenizer expansion** doubling vocab 65K → 128K for better
  non-Latin tokenization; pretraining scaled 17T → 33T tokens.
- Mid-training two phases: (1) 2T tokens @32K on curated reasoning/math/code/
  instruction/multilingual; (2) 300B tokens @131K weighted to long context. Tool
  calls + multi-turn trajectories throughout.
- Post-training 5-stage pipeline: (1) SFT, (2) Teacher Specialization, (3) non-agentic
  + (4) agentic **Multi-Domain On-Policy Distillation (MOPD)**, (5) **Agentic RL**
  inside agent harnesses (OpenClaw, Hermes Agent, Pi, OpenCode).
- Reward-hacking observed during teacher specialization (searching git history /
  GitHub / PyPI for final answers).
- Reasoning-only: emits explicit chain of thought before the answer, leveraging high
  decode speed.

## Topic 2 — Code-review bottleneck study (more code, not more software)

Source: https://arstechnica.com/ai/2026/10/ai-coding-agents-generate-more-code-but-not-more-software/
(Kyle Orland, Oct 9 2026). Study: Fiona Chen & James Stratton (Harvard), using
Jellyfish engineering analytics.

- Dataset: **300M "work events"** (commits, PRs) + issue-tracker data across
  **700,000+ employees at 700+ firms**, 2021 → March 2026. Difference-in-differences
  regression around each firm's AI assistant / AI agent adoption date.
- **AI coding agents → +30% total lines of code, +20% commits, +23% pull requests.**
- BUT: "little evidence that firms increase software output or reduce employment."
  Efficiency gains during the coding phase are **absorbed by the human code-review
  bottleneck** — review process lengthens, PRs more likely to require revisions,
  reviewers leave more comments.
- Framing: "Quantity, not quality." Human review is the production-stream constraint.

## Topic 3 — Agent Standup (agent orchestration visibility, zero-token)

Source: https://atoll92.github.io/agent-standup/ ; HN 217p (Oct 11 2026).

- Turns Claude Code / Codex / Mistral Vibe sessions into a **live team call**: who is
  working, who waits on whom, who needs you. Reads the session files those tools
  already write → works in VS Code, Cursor, plain terminal, or desktop app.
- **Zero token cost** (no LLM calls — it parses existing session files). Free, open
  source, Mac/Windows/Linux. `npx @double_geste/agent-standup`. A tree of who asked
  whom. Illustrates the multi-agent visibility problem.

## Topic 4 — 500B tokens: agent-decompiled FPS (momo5502)

Source: https://momo5502.com/posts/2026-10-09-game-decompilation/ ; HN 217p (Oct 11).

- 3-month project, ~500B tokens, decompiling a popular FPS to readable, compiling
  C++. Goal: accurate, stable, feature-complete recreation — not a PoC. Prior posts
  DMCA'd ("corporate America was here to ruin our fun").
- Post is explicitly about **AI orchestration** + optimizing infrastructure, setup,
  and **harness** for multi-month autonomous-agent runs. Modernization/portability
  deferred to focus on reconstructing original behavior first. Reinforces the
  already-covered LLM-decompilation topic.

## Topic 5 — "Agents aren't going rogue; labs skip security basics" (CSO Online)

Source: https://www.csoonline.com/article/4234854/... (Cynthia Brumfield, Oct 14 2026); HN 942p.

- Cyber experts: recent alarming AI-hacking reports are **containment & monitoring
  failures**, not agents with minds of their own. CISOs should vet AI vendors and
  tighten security basics. Frames agent risk as an ops-discipline gap, not agency.
