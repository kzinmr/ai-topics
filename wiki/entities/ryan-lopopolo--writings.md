---
title: "Ryan Lopopolo — Writings & Speaking"
type: entity
parent: ryan-lopopolo
created: 2026-04-28
updated: 2026-04-28
tags:
  - person
  - writings
  - blog
  - podcast
  - speaking
sources: []
---

# Ryan Lopopolo: Writings & Speaking

Back to main profile: [[ryan-lopopolo]]

## Blog / Key Writings (hyperbo.la)

### Harness Engineering & Agent Systems

- **[Harness Engineering the Blog Build (Again)](https://hyperbo.la/w/harness-engineering-blog-build/)** (Feb 2026) — Vite-native SSR and assets, MDX posts, typed React composition, and static output that still deploys to GitHub Pages. Demonstrates applying harness principles to blog infrastructure.

- **[What Does It Mean to Do a Good Job?](https://hyperbo.la/w/what-does-it-mean-to-do-a-good-job/)** — Ryan's deepest philosophical post on verification as the central problem of AI-assisted development. Every real task is downstream of unwritten non-functional requirements: tone, taste, risk tolerance, polish level, what counts as done. Historically these were smuggled in through shared context — hiring, onboarding, repeated exposure. But *"you do not get to run your AI through a hiring pipeline."* Concrete example from OpenAI: implementation agents and reviewer agents needed explicit rules (accept and fix, accept and defer, or push back). Without guidance, *"reviewers endlessly bully the implementer and nothing converges."* Key insight: *"If you want the models and agents to do a good job, write down what that means, then add nuance only when the coarse instructions start to overfit."*

- **[Coding Agents for Technical Non-Engineers](https://hyperbo.la/w/coding-agents-for-technical-non-engineers/)** — Practical playbook for enabling scientists, analysts, user ops, and security researchers with coding agents. These folks are *"technical enough to have success"* — they need data-science-quality code, not production-ready. Strategy: (1) One paved lane — Python, with IT deploying `uv` everywhere; (2) Ship enterprise-managed `AGENTS.md`; (3) Provide "boring batteries" by default — pandas, numpy, poppler. *"Domain experts already have the hard part. They know the data, the detection, the investigation, or the support workflow."*

- **[A Lazy Prompt Turned Into a RustSec Advisory](https://hyperbo.la/w/lazy-prompt-rustsec/)** — Security hardening workflow using Codex. Pointed at his Rust crate `intaglio` with a simple red-teaming prompt. Found RUSTSEC-2026-0078 — a cross-cutting unwind-safety bug. Key insight: *"The useful part was the bar: do a complete analysis and prove impact or exploitability."* By forbidding speculative bug reports, the model had to build a reproducer, show bad behavior, and narrow claims. Same prompt found issues in every active Artichoke crate.

- **[Debazeling the Blog](https://hyperbo.la/w/debazeling/)** — Journey away from over-engineered blog builds. Converted from hand-spun JS SSG to Bazel in 2022, but the repo became 25% Starlark. Key lesson: modern frontend tech made the switch take hours instead of days.

- **[Winding Down Artichoke Ruby](https://hyperbo.la/w/winding-down-artichoke-ruby/)** — Reflection on 6 years of building a Ruby implementation in Rust, now archived. Key technical achievements: pure Rust `String` implementation on `bstr` crate (contributed back to Rust ecosystem); modular capability-oriented VM design. Critical insight: the Rust borrow checker forced nearly every API to take `&mut self`, demonstrating why YARV/CPython converge on GIL-shaped designs. *"Build things. Even weird things. Even things that might not last forever. The act of building changes you."*

- **[Agent Utilization Is the New Performance Ceiling](https://hyperbo.la/w/agent-utilization-new-performance-ceiling/)** (Mar 2026) — As implementation ceases to be the bottleneck, the limiting factor shifts to how effectively agents can observe, act, and operate continuously across the entire lifecycle.

- **[Stop Treating Code as the Artifact](https://hyperbo.la/w/stop-treating-code-as-the-artifact/)** (Mar 2026) — When agents write most of the code, review and authorship stop being the right control surfaces. Quality scales only through systems design.

- **[Software Work Is No Longer Scheduled](https://hyperbo.la/w/software-work-is-no-longer-scheduled/)** (Mar 2026) — The production function has changed.

- **[It's Not Codex, It's Codex/GPT-5-Codex](https://hyperbo.la/w/its-not-codex-its-codex-gpt-5-codex/)** (Dec 2025) — Naming clarification for the agent model.

- **[MCP Solves Tool Discovery for LLMs](https://hyperbo.la/w/mcp-solves-tool-discovery-for-llms/)** (Aug 2025) — Coding agents fail on tools they can't see. MCP exposes a model-readable catalog so agents can discover, understand, and safely call your tools on the first try.

- **[Service Meshes Are Organization Tools, Not Technical Ones](https://hyperbo.la/w/service-meshes-are-organization-tools/)** (Aug 2025) — Service meshes are about enforcing org-wide defaults without slowing teams down.

- **[Ruby Enumerable: Manifest Destiny](https://hyperbo.la/w/ruby-enumerable-manifest-destiny/)** (Aug 2025) — Ruby's Enumerable mixin as gold standard for elegant, composable iteration; ECMAScript 2025's new Iterator type finally catching up.

- **[Scaling Myself by Letting My Team Fail](https://hyperbo.la/w/scaling-myself-by-letting-my-team-fail/)** (Jul 2023) — As a Staff+ engineer, learning to delegate by allowing controlled failure.

- **[Do the Simplest Thing That Could Possibly Work](https://hyperbo.la/w/do-the-simplest-thing/)** (Aug 2023) — To build iteratively and shed complexity, start with the simplest possible solution.

### Podcasts & Media Appearances

**Latent Space Podcast Interview** (Apr 2026) — "Extreme Harness Engineering for Token Billionaires" with swyx covering:
- The origin of "harness engineering" and the constraint-driven experiment
- Building Symphony with zero human-written code over 5 months
- Why Elixir/BEAM is ideal for agent orchestration
- The shift from code review to systems design
- Frontier's enterprise vision for safe, observable agent deployment
- Model capabilities and limitations (GPT-5.0 → 5.4)

**InfoQ Feature** (Feb 2026) — "OpenAI Introduces Harness Engineering: Codex Agents Power Large-Scale Software Development" — coverage of Ryan's methodology, including the 7-tier framework for agent-assisted development.

**Engineering.fyi Article** (Mar 2026) — "Harness engineering: leveraging Codex in an agent-first world" — comprehensive guide on structuring repositories and documentation for AI agent legibility using progressive disclosure patterns.

## See Also

- [[ryan-lopopolo--core-ideas|Core Ideas & Philosophy]]
- [[ryan-lopopolo--timeline|Timeline & Career]]
