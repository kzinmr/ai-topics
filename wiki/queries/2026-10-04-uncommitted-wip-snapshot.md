# Wiki changes — 2026-10-04 (uncommitted working tree)

> Auto-generated snapshot of the uncommitted `wiki/` changes at the time of the
> `skeleton-enrich-daily` run (2026-10-04 19:xx UTC). These changes were NOT made
> by the skeleton enrichment job — the skeleton backlog was empty (`status: skeleton`
> grep returns 0 across `wiki/entities/`). This file exists only so the WIP can be
> recovered from GitHub if the local working tree is ever lost. It is safe to delete
> once the changes below have been properly committed by their owning pipeline.

## Modified files (193) — summary of diff

Bulk of the diff = new `Related`/`Sources` wikilink lines added by a recent
enrichment sweep (likely `active-crawl` / `blog-wiki-ingest` / hot-post synthesis),
touching e.g.:

- concepts/agent-generated-software.md
- concepts/agent-orchestration-runtime.md
- concepts/agent-quota-resets.md
- concepts/agent-skills.md (added: [[concepts/hexis-skills-as-state-machines]])
- concepts/agentic-retrieval.md
- concepts/ai-agent-engineering.md
- concepts/ai-autonomy-debate.md
- concepts/ai-benchmarks/* (many)
- wiki/index.md, wiki/log.md

Full diff: `cd ~/ai-topics && git diff -- wiki/` (377 insertions, 705 deletions).

## Untracked files (37)

### Raw articles (blog ingest, 2026-10-02..03)
- wiki/raw/articles/2026-10-03_elevenlabs_banner-health.md
- wiki/raw/articles/2026-10-03_elevenlabs_how-to-add-pauses-in-ai-voiceover.md
- wiki/raw/articles/2026-10-03_elevenlabs_webinar-recap-how-one-of-europes-largest-insurers-got-ai-agents-into-production.md
- wiki/raw/articles/2026-10-03_factory_factory-analytics-transparency.md
- wiki/raw/articles/9to5mac.com--2026-10-02-apple-confirms-iphone-18-pro-max-att-cellular-iss--18cdb7f5.md
- wiki/raw/articles/blog.coredump.cx--p-haunted-by-the-ghosts-of-materialism--b480b919.md
- wiki/raw/articles/construction-physics.com--p-reading-list-2026-10-03--74b825d3.md
- wiki/raw/articles/daringfireball.net--2026-10-apple-full-disk-access--b99b742b.md
- wiki/raw/articles/devblogs.microsoft.com--oldnewthing-20261002-00--e225bb05.md
- wiki/raw/articles/dfarq.homeip.net--cull-lumber-at-menards--e09bd616.md
- wiki/raw/articles/dfarq.homeip.net--what-happened-to-activision--1ee7a656.md
- wiki/raw/articles/downtowndougbrown.com--2026-10-altera-quartus-linux-jtagd-bug-fixes--c2a6bfcb.md
- wiki/raw/articles/geohot.github.io--blog-jekyll-update-2026-10-03-dyson-camerajet-html--30eae03f.md
- wiki/raw/articles/idiallo.com--blog-asus-laptop-keeps-rebooting-after-sleep--27ce1313.md
- wiki/raw/articles/jayd.ml--2026-10-03-sony-headphones-action-bluetooth-adapter-html--c4d3a099.md
- wiki/raw/articles/johndcook.com--blog-2026-10-03-miquels-pivot-theorem--ae9fe97a.md
- wiki/raw/articles/lwn.net--articles-1098313--028eb209.md
- wiki/raw/articles/lwn.net--articles-1098404--8a5340df.md
- wiki/raw/articles/lwn.net--articles-1098412--a04047b1.md
- wiki/raw/articles/matduggan.com--what-does-my-dream-os-ui-look-like--a27b6782.md
- wiki/raw/articles/nesbitt.io--2026-10-03-this-week-in-package-management-html--09428819.md
- wiki/raw/articles/pluralistic.net--2026-10-03-full-employment--f35fc5d4.md
- wiki/raw/articles/seangoedecke.com--shipping-is-the-foundation--9ac6c2bb.md
- wiki/raw/articles/seangoedecke.com--superpersuasion-will-look-like-bribery--6b69bc94.md
- wiki/raw/articles/shkspr.mobi--blog-2026-10-gadget-review-una-watch--73fd1d0d.md
- wiki/raw/articles/simonwillison.net--2026-oct-2-rex-s-dino-store--b5be5671.md
- wiki/raw/articles/simonwillison.net--2026-oct-3-default-hard-budget-caps--81b68c5e.md
- wiki/raw/articles/simonwillison.net--2026-oct-3-newsletter--347c0b44.md
- wiki/raw/articles/terriblesoftware.org--2026-10-02-the-brain-sandwich--35ad8347.md
- wiki/raw/articles/wheresyoured.at--premium-how-has-ai-changed-the-economy--c5c6e86b.md

### Raw newsletters (2026-10-02..04)
- wiki/raw/newsletters/2026-10-02-claude-turns-one-physicist-into-a-lab.md
- wiki/raw/newsletters/2026-10-02-goodbye-ai-hello-si.md
- wiki/raw/newsletters/2026-10-02-inside-out-ai-rebuilding-airbnb-behind-the-scenes-and-across-the-guest-experienc.md
- wiki/raw/newsletters/2026-10-02-introducing-trillium-labs.md
- wiki/raw/newsletters/2026-10-03-dots.md
- wiki/raw/newsletters/2026-10-03-what-is-orbit-actually-solving.md
- wiki/raw/newsletters/2026-10-04-practical-parametric-yield.md

## Full diff of modified wiki files

```diff
diff --git a/wiki/concepts/agent-generated-software.md b/wiki/concepts/agent-generated-software.md
index 74728313..f7dcb55f 100644
--- a/wiki/concepts/agent-generated-software.md
+++ b/wiki/concepts/agent-generated-software.md
@@ -47,7 +47,7 @@ The cost curve matters: Epoch's ~13×/year decline in cost-per-performance makes
 ## See Also
 
 - [[concepts/vibe-coding]] — predecessor practice
-- [[concepts/agentic-coding]] — engineering-side framing
+- [[concepts/coding-agents/agentic-coding]] — engineering-side framing
 - [[concepts/creative-coding-with-ai]] — media/creative side
 - [[entities/ethan-mollick]], [[entities/simon-willison]] — two of the loudest practitioners/reporters
 
diff --git a/wiki/concepts/agent-orchestration-runtime.md b/wiki/concepts/agent-orchestration-runtime.md
index 849c4aba..27d42cde 100644
--- a/wiki/concepts/agent-orchestration-runtime.md
+++ b/wiki/concepts/agent-orchestration-runtime.md
@@ -111,7 +111,7 @@ The key differentiator: every prior approach treats state as either ephemeral or
 
 - **[[concepts/agentic-engineering]]**: An orchestration runtime is infrastructure for agentic engineering — it provides the deterministic substrate on which non-deterministic agents can be composed reliably
 - **[[concepts/harness-engineering]]**: Onyx is a meta-harness; programs are harness definitions, and the VM is the harness runner. Where traditional harnesses are ad-hoc scripts, `*.program.ts` files are typed, composable harnesses
-- **[[concepts/rlm]]**: RLM pioneered using code (Python REPL) for agent orchestration. Onyx inherits this code-first philosophy but adds persistence, types, and a full VM — moving from "code in a REPL" to "code as the orchestration substrate"
+- **[[entities/omar-khattab/rlm]]**: RLM pioneered using code (Python REPL) for agent orchestration. Onyx inherits this code-first philosophy but adds persistence, types, and a full VM — moving from "code in a REPL" to "code as the orchestration substrate"
 - **[[entities/akira-realmcore]]**: Random Labs, led by Akira, built Onyx as the natural evolution of Slate's thread-weaving architecture — taking the implicit orchestration of episodes and making it explicit through programs
 
 ## Autoresearch as a Program
diff --git a/wiki/concepts/agent-quota-resets.md b/wiki/concepts/agent-quota-resets.md
index 5dceaa28..c02bcda7 100644
--- a/wiki/concepts/agent-quota-resets.md
+++ b/wiki/concepts/agent-quota-resets.md
@@ -60,7 +60,7 @@ Max Woolf (minimaxir.com) identified several structural issues:
 ## Market Context (July 2026)
 
 The surge in resets coincides with an unprecedented month of LLM releases:
-- [[concepts/fable-5|Fable 5]] and [[concepts/gpt/gpt-5-6|GPT-5.6 Sol]] — frontier models
+- [[concepts/claude/fable-5|Fable 5]] and [[concepts/gpt/gpt-5-6|GPT-5.6 Sol]] — frontier models
 - [[concepts/grok-4-5|Grok 4.5]], Muse Spark 1.1, [[concepts/kimi-k3|Kimi K3]] — competitive alternatives
 
 ## Sustainability Question
diff --git a/wiki/concepts/agent-skills.md b/wiki/concepts/agent-skills.md
index 8a9fd29a..0020500c 100644
--- a/wiki/concepts/agent-skills.md
+++ b/wiki/concepts/agent-skills.md
@@ -185,6 +185,7 @@ The skill behind Claude's document editing capabilities:
 - [[concepts/mcp]] — Model Context Protocol
 - [[concepts/claude-code/claude-code-best-practices]] — Claude Code best practices
 - [[concepts/agent-skills-skillmd]] — SKILL.md format details
+- [[concepts/hexis-skills-as-state-machines]] — Compiling skills into executable FSMs (knowledge/control separation)
 - [[entities/codex]] — OpenAI Codex
 - [[concepts/evaluation/evals-for-ai-agents]] — Evals for AI agents
 - [[concepts/harness-engineering]] — Harness engineering
diff --git a/wiki/concepts/agentic-retrieval.md b/wiki/concepts/agentic-retrieval.md
index c73ef94d..54d50ed2 100644
--- a/wiki/concepts/agentic-retrieval.md
+++ b/wiki/concepts/agentic-retrieval.md
@@ -125,7 +125,7 @@ This academic work converges with Hornet's empirical analysis (Part 2: 19,279 se
 - [[concepts/vespa]] — The engine where many Hornet engineers previously worked
 - [[concepts/bm25]] — Keyword retrieval backbone; performs differently in agent loops vs. one-shot
 - [[concepts/mutually-assured-distraction]] — Compounding error: better retrieval → more convincing distractors → more confident wrong answers
-- [[concepts/browsecomp]] — The benchmark revealing the agentic retrieval bottleneck
+- [[concepts/ai-benchmarks/browsecomp]] — The benchmark revealing the agentic retrieval bottleneck
 - [[concepts/agent-loop]] — The iterative reasoning pattern that produces agentic workloads
 - [[concepts/rag]] — Retrieval-Augmented Generation (evolving toward agentic retrieval)
 
diff --git a/wiki/concepts/ai-agent-engineering.md b/wiki/concepts/ai-agent-engineering.md
index c46b1379..dbeafdb8 100644
--- a/wiki/concepts/ai-agent-engineering.md
+++ b/wiki/concepts/ai-agent-engineering.md
@@ -31,7 +31,7 @@ Anthropic launched **Claude Managed Agents** in public beta (April 2026):
 - Provides a platform-level orchestration layer for running Claude agents
 - Designed for enterprises to integrate agents into their products without managing infrastructure
 - Memory capability added for persistent context across sessions
-- Represents the **L4 Engineering Team** level in the [[concepts/harness-engineering/agent-team-swarm]] taxonomy
+- Represents the **L4 Engineering Team** level in the [[concepts/multi-agents/agent-team-swarm]] taxonomy
 
 **Architecture:**
 - Tool definitions via JSON schema
@@ -134,7 +134,7 @@ See [[concepts/agentic-engineering]] for the parallel developer-workflow perspec
 ## Related Concepts
 - [[concepts/harness-engineering]] — Parent concept: Agent = Model + Harness
 - [[concepts/agentic-engineering]] — Developer workflows for using agents
-- [[concepts/harness-engineering/agent-team-swarm]] — Multi-agent orchestration patterns
+- [[concepts/multi-agents/agent-team-swarm]] — Multi-agent orchestration patterns
 - [[entities/anthropic]] — Claude Managed Agents platform
 - [[entities/openai]] — Symphony orchestration platform
 - [[entities/cursor-3]] — AI-powered IDE (safety incident case study)
diff --git a/wiki/concepts/ai-autonomy-debate.md b/wiki/concepts/ai-autonomy-debate.md
index fc68621c..be826a0f 100644
--- a/wiki/concepts/ai-autonomy-debate.md
+++ b/wiki/concepts/ai-autonomy-debate.md
@@ -148,7 +148,7 @@ The phrase earning traction: **"Trust comes before autonomy. You don't earn the
 
 ## Related Concepts
 
-- [[concepts/anthropic]] — The practice of directing AI agents rather than writing code- [[concepts/anthropic/managed-agents]] — Hosted agent services and the debate around them
+- [[entities/anthropic]] — The practice of directing AI agents rather than writing code- [[concepts/anthropic/managed-agents]] — Hosted agent services and the debate around them
 - [[concepts/ai-agent-traps]] — Common pitfalls in agent deployment and design
 - [[concepts/compute-scaling-bottlenecks]] — Infrastructure constraints affecting agent capabilities
 - [[concepts/cognitive-cost-of-agents]] — The human cognitive burden of managing AI agents
diff --git a/wiki/concepts/ai-benchmarks/ai-resistant-evaluations.md b/wiki/concepts/ai-benchmarks/ai-resistant-evaluations.md
index e3cb21fe..3e97f782 100644
--- a/wiki/concepts/ai-benchmarks/ai-resistant-evaluations.md
+++ b/wiki/concepts/ai-benchmarks/ai-resistant-evaluations.md
@@ -89,5 +89,5 @@ The original test is publicly available with no time limit:
 
 - [[concepts/evaluation/eval-awareness-browsecomp]] — Eval awareness and benchmark contamination
 - [[concepts/ai-benchmarks/swe-bench]] — SWE-bench benchmark
-- [[concepts/frontier-swe-benchmark]] — Frontier SWE benchmark
+- [[concepts/ai-benchmarks/frontier-swe-benchmark]] — Frontier SWE benchmark
 - [[concepts/coding-agents/infrastructure-noise-agent-evals]] — Infrastructure noise in agent evals
diff --git a/wiki/concepts/ai-benchmarks/arc-agi-1.md b/wiki/concepts/ai-benchmarks/arc-agi-1.md
index a8257977..624cf7bf 100644
--- a/wiki/concepts/ai-benchmarks/arc-agi-1.md
+++ b/wiki/concepts/ai-benchmarks/arc-agi-1.md
@@ -74,7 +74,7 @@ Xeophon contextualizes ARC-AGI-1 as a "classic" benchmark that fundamentally red
 
 ## ARC-AGI-1 vs ARC-AGI-2: Key Differences
 
-While [[concepts/arc-agi-2]] builds on the same fundamental principles, there are critical differences:
+While [[concepts/ai-benchmarks/arc-agi-2]] builds on the same fundamental principles, there are critical differences:
 
 | Aspect | ARC-AGI-1 | ARC-AGI-2 |
 |--------|-----------|-----------|
@@ -118,8 +118,8 @@ This definition separates intelligence from:
 ## Related Pages
 
 - [[concepts/evaluation/ai-benchmarks-and-evals|AI Benchmarks & Evals Overview]] — @xeophon's 18-part benchmark analysis series
-- [[concepts/arc-agi-2|ARC-AGI-2]] — The successor benchmark (released 2025)
-- [[concepts/hle|Humanity's Last Exam]] — Another benchmark designed to resist memorization
+- [[concepts/ai-benchmarks/arc-agi-2|ARC-AGI-2]] — The successor benchmark (released 2025)
+- [[concepts/ai-benchmarks/hle|Humanity's Last Exam]] — Another benchmark designed to resist memorization
 
 ## Sources
 
diff --git a/wiki/concepts/ai-benchmarks/arc-agi-2.md b/wiki/concepts/ai-benchmarks/arc-agi-2.md
index 8dde3caa..24a3e8e0 100644
--- a/wiki/concepts/ai-benchmarks/arc-agi-2.md
+++ b/wiki/concepts/ai-benchmarks/arc-agi-2.md
@@ -60,7 +60,7 @@ Håvard Tveit Ihle's WeirdML benchmark received a v2 update, adding a new dimens
 - [[concepts/gemini]] — Gemini 3 Deep Think performance
 - [[concepts/evaluation/ai-evals]] — AI evaluation benchmarks overview
 - [[concepts/evaluation/llm-evaluation-harness]] — Evaluation framework details
-- [[concepts/agent-survival-benchmark]] — Other agent-focused benchmarks
+- [[concepts/ai-benchmarks/agent-survival-benchmark]] — Other agent-focused benchmarks
 
 ## Sources
 
diff --git a/wiki/concepts/ai-benchmarks/benchmaxxing.md b/wiki/concepts/ai-benchmarks/benchmaxxing.md
index e5b34d72..f41fd17d 100644
--- a/wiki/concepts/ai-benchmarks/benchmaxxing.md
+++ b/wiki/concepts/ai-benchmarks/benchmaxxing.md
@@ -92,7 +92,7 @@ Practitioners identify benchmaxxed models through several signals:
 - [[concepts/benchpress]] — BenchPress: rank-2 matrix completion shows benchmarks are structurally redundant; 5 benchmarks predict 44 others
 - [[concepts/ai-benchmarks/ifeval]] — Instruction Following Eval; tests verifiable constraints but misses nuanced compliance
 - [[concepts/evaluation/ai-benchmarks-and-evals]] — Comprehensive benchmark landscape overview
-- [[concepts/vibe-eval]] — Vibe-Eval; explicitly designed to capture subjective quality beyond benchmarks
+- [[concepts/ai-benchmarks/vibe-eval]] — Vibe-Eval; explicitly designed to capture subjective quality beyond benchmarks
 - `overfitting` — The statistical phenomenon underlying benchmaxxing
 - `benchmark-framing` — How benchmark results are framed in public discourse
 
diff --git a/wiki/concepts/ai-benchmarks/countbenchqa.md b/wiki/concepts/ai-benchmarks/countbenchqa.md
index bf6812b9..1afb71a6 100644
--- a/wiki/concepts/ai-benchmarks/countbenchqa.md
+++ b/wiki/concepts/ai-benchmarks/countbenchqa.md
@@ -15,7 +15,7 @@ sources:
   - wiki/raw/articles/2025-04-29_xeophon-ai-benchmark-eval-series.md
 related:
   - "[[concepts/evaluation/ai-benchmarks-and-evals]]"
-  - "[[concepts/ifeval]]"
+  - "[[concepts/ai-benchmarks/ifeval]]"
 ---
 
 # CountBenchQA
@@ -66,7 +66,7 @@ Counting may seem trivial, but it reveals important model behaviors:
 ## Related Pages
 
 - [[concepts/evaluation/ai-benchmarks-and-evals]] — Full benchmarks & evals MOC
-- [[concepts/ifeval]] — IFEval (another focused, simple benchmark)
+- [[concepts/ai-benchmarks/ifeval]] — IFEval (another focused, simple benchmark)
 - [[concepts/evaluation/pass-k-metric]] — Pass@k metric
 
 ## Sources
diff --git a/wiki/concepts/ai-benchmarks/deepswe-benchmark.md b/wiki/concepts/ai-benchmarks/deepswe-benchmark.md
index ea0ca588..3236afcc 100644
--- a/wiki/concepts/ai-benchmarks/deepswe-benchmark.md
+++ b/wiki/concepts/ai-benchmarks/deepswe-benchmark.md
@@ -157,13 +157,13 @@ In August 2026, Together AI published a second head-to-head on DeepSWE: **DeepSe
 [deepswe-benchmark] ──embodies──→ [concept: jagged-intelligence]
 ```
 
-This section informs graph queries: authored by [[entities/datacurve]] and [[entities/serena-ge]], directly contrasts with [[concepts/ai-benchmarks/swe-bench]], relates to [[concepts/frontier-swe-benchmark]] and [[concepts/evaluation/evals-for-ai-agents]].
+This section informs graph queries: authored by [[entities/datacurve]] and [[entities/serena-ge]], directly contrasts with [[concepts/ai-benchmarks/swe-bench]], relates to [[concepts/ai-benchmarks/frontier-swe-benchmark]] and [[concepts/evaluation/evals-for-ai-agents]].
 
 ## Related Concepts
 - [[concepts/ai-benchmarks/swe-bench]] — The benchmark DeepSWE critiques and improves upon
-- [[concepts/frontier-swe-benchmark]] — Ultra-long-horizon coding benchmark by Proximal
+- [[concepts/ai-benchmarks/frontier-swe-benchmark]] — Ultra-long-horizon coding benchmark by Proximal
 - [[concepts/evaluation/evals-for-ai-agents]] — Broader agent evaluation framework
-- [[concepts/swe-bench-agent-scaffolding]] — Agent harness design for SWE-bench tasks
+- [[concepts/ai-benchmarks/swe-bench-agent-scaffolding]] — Agent harness design for SWE-bench tasks
 - [[concepts/jagged-intelligence]] — Uneven capability profiles exposed by better benchmarks
 - [[entities/drew-breunig]] — "Fable & The End of the Free Lunch" (2026-08-23): argues this Pro-first cascade data is the empirical core of the "end of the free lunch" era — cost shock forces deliberate tiering across model tiers, and the best frontier model is no longer the default. See [[raw/articles/2026-08-23_dbreunig_fable-end-of-moore-s-law]].
 
diff --git a/wiki/concepts/ai-benchmarks/factorio-learning-environment.md b/wiki/concepts/ai-benchmarks/factorio-learning-environment.md
index 25762759..184980d2 100644
--- a/wiki/concepts/ai-benchmarks/factorio-learning-environment.md
+++ b/wiki/concepts/ai-benchmarks/factorio-learning-environment.md
@@ -104,8 +104,8 @@ The original FLE paper evaluated six frontier LLMs and found:
 ## Related Pages
 
 - [[concepts/evaluation/ai-benchmarks-and-evals|AI Benchmarks & Evals Overview]] — @xeophon's 18-part benchmark analysis series
-- [[concepts/swe-bench|SWE-Bench]] — Another agent-based evaluation, focused on software engineering bug fixes
-- [[concepts/frontier-swe-benchmark|FrontierSWE]] — Ultra-long-horizon coding benchmark (20 hours per task)
+- [[concepts/ai-benchmarks/swe-bench|SWE-Bench]] — Another agent-based evaluation, focused on software engineering bug fixes
+- [[concepts/ai-benchmarks/frontier-swe-benchmark|FrontierSWE]] — Ultra-long-horizon coding benchmark (20 hours per task)
 
 ## Sources
 
diff --git a/wiki/concepts/ai-benchmarks/frontier-swe-benchmark.md b/wiki/concepts/ai-benchmarks/frontier-swe-benchmark.md
index 25a9dda9..eefe4b72 100644
--- a/wiki/concepts/ai-benchmarks/frontier-swe-benchmark.md
+++ b/wiki/concepts/ai-benchmarks/frontier-swe-benchmark.md
@@ -69,8 +69,8 @@ The benchmark explicitly measures harness impact — results are reported by **(
 FrontierSWE complements rather than replaces [[concepts/ai-benchmarks/swe-bench]]:
 - **SWE-Bench**: Short-horizon PR fixes on open-source repos
 - **FrontierSWE**: 20-hour ultra-long-horizon challenges in implementation, performance, and ML research
-- **[[concepts/workspace-bench]]**: Multi-file workspace navigation (74 file types, 20,476 files — different dimension of complexity)
-- **[[concepts/kernelbench]]**: Kernel-level optimization; [[concepts/yourbench]]: Human-calibrated coding; [[concepts/programbench]]: Multi-language programming
+- **[[concepts/ai-benchmarks/workspace-bench]]**: Multi-file workspace navigation (74 file types, 20,476 files — different dimension of complexity)
+- **[[concepts/ai-benchmarks/kernelbench]]**: Kernel-level optimization; [[concepts/ai-benchmarks/yourbench]]: Human-calibrated coding; [[concepts/ai-benchmarks/programbench]]: Multi-language programming
 
 ## Key Significance
 
@@ -79,7 +79,7 @@ FrontierSWE reveals that even frontier models remain far from saturated on hard
 ## See Also
 
 - [[concepts/ai-benchmarks/swe-bench]] — Standard PR-level coding benchmark
-- [[concepts/workspace-bench]] — Multi-file workspace learning benchmark
+- [[concepts/ai-benchmarks/workspace-bench]] — Multi-file workspace learning benchmark
 - [[concepts/harness-engineering]] — How execution environments shape agent performance
 - [[concepts/evaluation/ai-evals]] — AI evaluation landscape overview
-- [[concepts/agent-survival-benchmark]] — Human-normalized agent benchmark
+- [[concepts/ai-benchmarks/agent-survival-benchmark]] — Human-normalized agent benchmark
diff --git a/wiki/concepts/ai-benchmarks/gpqa.md b/wiki/concepts/ai-benchmarks/gpqa.md
index ab7de967..62df482b 100644
--- a/wiki/concepts/ai-benchmarks/gpqa.md
+++ b/wiki/concepts/ai-benchmarks/gpqa.md
@@ -154,8 +154,8 @@ From the Part 1 analysis (Apr 29, 2025):
 - [[concepts/evaluation/ai-benchmarks-and-evals]] — Full 18-part benchmark series overview
 - [[entities/florian-brand]] — Florian Brand (@xeophon), series author
 - [[concepts/llm-evaluation]] — LLM evaluation landscape
-- [[concepts/hle]] — Humanity's Last Exam (similar data creation approach)
-- [[concepts/mmlu-pro]] — MMLU Pro (broader knowledge benchmark)
+- [[concepts/ai-benchmarks/hle]] — Humanity's Last Exam (similar data creation approach)
+- [[concepts/ai-benchmarks/mmlu-pro]] — MMLU Pro (broader knowledge benchmark)
 
 ---
 
diff --git a/wiki/concepts/ai-benchmarks/hle.md b/wiki/concepts/ai-benchmarks/hle.md
index bf0cf094..e50e929c 100644
--- a/wiki/concepts/ai-benchmarks/hle.md
+++ b/wiki/concepts/ai-benchmarks/hle.md
@@ -118,9 +118,9 @@ Xeophon highlights HLE's rigorous quality control and incentive design as best p
 
 ## See Also
 
-- [[concepts/swe-bench]] — Software engineering benchmark with similar anti-saturation design
-- [[concepts/arc-agi-2]] — Another benchmark explicitly designed to resist model memorization
-- [[concepts/arc-agi-1]] — Chollet's abstract reasoning benchmark
+- [[concepts/ai-benchmarks/swe-bench]] — Software engineering benchmark with similar anti-saturation design
+- [[concepts/ai-benchmarks/arc-agi-2]] — Another benchmark explicitly designed to resist model memorization
+- [[concepts/ai-benchmarks/arc-agi-1]] — Chollet's abstract reasoning benchmark
 
 ## Sources
 
diff --git a/wiki/concepts/ai-benchmarks/index.md b/wiki/concepts/ai-benchmarks/index.md
index 59493af7..e417453d 100644
--- a/wiki/concepts/ai-benchmarks/index.md
+++ b/wiki/concepts/ai-benchmarks/index.md
@@ -178,7 +178,7 @@ status: active
 
 ## Metrics (→ [[concepts/evaluation/_index|Evaluation]])
 
-- [[concepts/evaluation/ram-relative-adoption-metric]] — Relative adoption metric
+- [[concepts/ai-benchmarks/ram-relative-adoption-metric]] — Relative adoption metric
 
 ## Search & Retrieval
 
diff --git a/wiki/concepts/ai-benchmarks/livecodebench.md b/wiki/concepts/ai-benchmarks/livecodebench.md
index 2600b452..43e0d4ef 100644
--- a/wiki/concepts/ai-benchmarks/livecodebench.md
+++ b/wiki/concepts/ai-benchmarks/livecodebench.md
@@ -140,8 +140,8 @@ From the Part 2 analysis (Apr 30, 2025):
 
 - [[concepts/evaluation/ai-benchmarks-and-evals]] — Full 18-part benchmark series overview
 - [[entities/florian-brand]] — Florian Brand (@xeophon), series author
-- [[concepts/aider-polyglot]] — Aider Polyglot (multi-language coding)
-- [[concepts/swe-bench]] — SWE-Bench (real-world software engineering)
+- [[concepts/ai-benchmarks/aider-polyglot]] — Aider Polyglot (multi-language coding)
+- [[concepts/ai-benchmarks/swe-bench]] — SWE-Bench (real-world software engineering)
 - [[concepts/llm-evaluation]] — LLM evaluation landscape
 
 ---
diff --git a/wiki/concepts/ai-benchmarks/mirrorcode.md b/wiki/concepts/ai-benchmarks/mirrorcode.md
index a67d741b..23e3f7c6 100644
--- a/wiki/concepts/ai-benchmarks/mirrorcode.md
+++ b/wiki/concepts/ai-benchmarks/mirrorcode.md
@@ -15,7 +15,7 @@ sources:
 related_concepts:
   - "[[concepts/ai-benchmarks/_index]]"
   - "[[concepts/agent-evaluation]]"
-  - "[[concepts/swe-bench]]"
+  - "[[concepts/ai-benchmarks/swe-bench]]"
   - "[[entities/epoch-ai]]"
 ---
 
@@ -50,13 +50,13 @@ MirrorCode was first described in Import AI #453 (April 2026) and subsequently f
 
 ## Significance
 
-MirrorCode fills an important gap in the AI evaluation landscape. Most coding benchmarks (e.g., [[concepts/swe-bench]], HumanEval, MBPP) test short-duration, isolated coding tasks. MirrorCode addresses the question: *how well do AI systems perform when the task requires sustained, multi-day effort?*
+MirrorCode fills an important gap in the AI evaluation landscape. Most coding benchmarks (e.g., [[concepts/ai-benchmarks/swe-bench]], HumanEval, MBPP) test short-duration, isolated coding tasks. MirrorCode addresses the question: *how well do AI systems perform when the task requires sustained, multi-day effort?*
 
 The finding that Opus 4.7 can complete a multi-week human task in minutes — but still fails on the hardest problems — suggests that long-horizon capability is improving rapidly but not yet saturated.
 
 ## Related Benchmarks
 
-- [[concepts/swe-bench]] — Software engineering benchmark for AI agents (shorter tasks)
+- [[concepts/ai-benchmarks/swe-bench]] — Software engineering benchmark for AI agents (shorter tasks)
 - [[concepts/ai-benchmarks/agentdojo]] — Dynamic evaluation for agent security
 - [[concepts/ai-benchmarks/benchmaxxing]] — Notes on benchmark over-optimization
 
diff --git a/wiki/concepts/ai-benchmarks/mmlu-pro.md b/wiki/concepts/ai-benchmarks/mmlu-pro.md
index ead8cc76..d5d5baf6 100644
--- a/wiki/concepts/ai-benchmarks/mmlu-pro.md
+++ b/wiki/concepts/ai-benchmarks/mmlu-pro.md
@@ -167,8 +167,8 @@ From the Part 4 analysis (May 2, 2025):
 
 - [[concepts/evaluation/ai-benchmarks-and-evals]] — Full 18-part benchmark series overview
 - [[entities/florian-brand]] — Florian Brand (@xeophon), series author
-- [[concepts/gpqa]] — GPQA (narrower, deeper science reasoning)
-- [[concepts/mmmu]] — MMMU (multimodal equivalent for vision + text)
+- [[concepts/ai-benchmarks/gpqa]] — GPQA (narrower, deeper science reasoning)
+- [[concepts/ai-benchmarks/mmmu]] — MMMU (multimodal equivalent for vision + text)
 - [[concepts/llm-evaluation]] — LLM evaluation landscape
 
 ---
diff --git a/wiki/concepts/ai-benchmarks/nanogpt-speedrun.md b/wiki/concepts/ai-benchmarks/nanogpt-speedrun.md
index 3edd44d4..a2d7c45a 100644
--- a/wiki/concepts/ai-benchmarks/nanogpt-speedrun.md
+++ b/wiki/concepts/ai-benchmarks/nanogpt-speedrun.md
@@ -56,5 +56,5 @@ This leaderboard is a constructive datapoint for [[concepts/quantifying-infrastr
 - [[concepts/ai-benchmarks/swe-bench]] — boolean-task coding benchmark family
 - [[concepts/ai-benchmarks/terminal-bench]] — same harness×model leaderboard lineage, now extended to science workflows (Terminal-Bench-Science 0.1)
 - [[concepts/self-evolving-agents]] — agents that improve their own toolchains
-- [[concepts/ai-evals]] — evaluation methodology overview
+- [[concepts/evaluation/ai-evals]] — evaluation methodology overview
 - [[concepts/agent-trace-integrity]] — the NanoGPT Speedrun Sandbox was the eval environment in which the Hugging Face SwarmTraces breach occurred (Sep 2026); see also [[concepts/agent-collusion-public-infrastructure]]
diff --git a/wiki/concepts/ai-benchmarks/swe-bench-agent-scaffolding.md b/wiki/concepts/ai-benchmarks/swe-bench-agent-scaffolding.md
index 8424e602..5b33dba2 100644
--- a/wiki/concepts/ai-benchmarks/swe-bench-agent-scaffolding.md
+++ b/wiki/concepts/ai-benchmarks/swe-bench-agent-scaffolding.md
@@ -88,7 +88,7 @@ Open-source developers and startups have achieved significant improvements by op
 ## See Also
 
 - [[concepts/ai-benchmarks/swe-bench]] — SWE-bench benchmark overview
-- [[concepts/frontier-swe-benchmark]] — Frontier SWE benchmark
+- [[concepts/ai-benchmarks/frontier-swe-benchmark]] — Frontier SWE benchmark
 - [[concepts/agent-harnesses]] — Agent harness comparison
 - [[concepts/building-effective-agents]] — Building effective agents (Anthropic)
 - [[concepts/coding-agents/coding-agents]] — Coding agents overview
diff --git a/wiki/concepts/ai-benchmarks/swe-bench.md b/wiki/concepts/ai-benchmarks/swe-bench.md
index 84895d84..c9311143 100644
--- a/wiki/concepts/ai-benchmarks/swe-bench.md
+++ b/wiki/concepts/ai-benchmarks/swe-bench.md
@@ -140,7 +140,7 @@ The SWE-bench ecosystem has expanded significantly:
 
 ## DeepSWE Critique (Datacurve, May 2026)
 
-In May 2026, [[entities/datacurve|Datacurve]] released the [[concepts/deepswe-benchmark|DeepSWE benchmark]], a 113-task evaluation that delivered a sharp critique of SWE-Bench Pro's evaluation infrastructure:
+In May 2026, [[entities/datacurve|Datacurve]] released the [[concepts/ai-benchmarks/deepswe-benchmark|DeepSWE benchmark]], a 113-task evaluation that delivered a sharp critique of SWE-Bench Pro's evaluation infrastructure:
 
 ### Verifier Unreliability
 Datacurve audited 30 random tasks across both benchmarks using an LLM-based judge:
@@ -274,14 +274,14 @@ SWE-Bench Verified was originally created as part of OpenAI's **Preparedness Fra
 ## Related Pages
 
 - [[concepts/evaluation/ai-benchmarks-and-evals|AI Benchmarks & Evals Overview]] — @xeophon's 18-part benchmark analysis series
-- [[concepts/frontier-swe-benchmark|FrontierSWE Benchmark]] — Ultra-long-horizon coding benchmark (20 hours per task)
+- [[concepts/ai-benchmarks/frontier-swe-benchmark|FrontierSWE Benchmark]] — Ultra-long-horizon coding benchmark (20 hours per task)
 - [[concepts/harness-engineering|Harness Engineering]] — How execution environments shape agent performance
-- [[concepts/hle|Humanity's Last Exam]] — Another benchmark experiencing rapid score inflation
+- [[concepts/ai-benchmarks/hle|Humanity's Last Exam]] — Another benchmark experiencing rapid score inflation
 
 ## See Also
 
-- [[concepts/arc-agi-1|ARC-AGI-1]] — Another benchmark with dramatic historical score progression toward saturation
-- [[concepts/factorio-learning-environment|Factorio Learning Environment]] — Agent-based evaluation in a different domain (game-based factory automation)
+- [[concepts/ai-benchmarks/arc-agi-1|ARC-AGI-1]] — Another benchmark with dramatic historical score progression toward saturation
+- [[concepts/ai-benchmarks/factorio-learning-environment|Factorio Learning Environment]] — Agent-based evaluation in a different domain (game-based factory automation)
 
 ## Sources
 
diff --git a/wiki/concepts/ai-benchmarks/tau-bench.md b/wiki/concepts/ai-benchmarks/tau-bench.md
index f248c061..1245a70e 100644
--- a/wiki/concepts/ai-benchmarks/tau-bench.md
+++ b/wiki/concepts/ai-benchmarks/tau-bench.md
@@ -17,9 +17,9 @@ sources:
   - raw/articles/2026-09-09_sierra_hyper-tau-bench-agents-that-build-agents.md
 related:
   - "[[entities/shunyu-yao]]"
-  - "[[concepts/tau-squared-bench]]"
-  - "[[concepts/tau-knowledge]]"
-  - "[[concepts/tau-voice]]"
+  - "[[concepts/ai-benchmarks/tau-squared-bench]]"
+  - "[[concepts/ai-benchmarks/tau-knowledge]]"
+  - "[[concepts/ai-benchmarks/tau-voice]]"
   - "[[concepts/evaluation/pass-k-metric]]"
 ---
 
@@ -256,12 +256,12 @@ Common to both is the methodology of "visualizing AI's true capability limits by
 ## Related Pages
 
 - [[entities/shunyu-yao]] — τ-bench's creator. All achievements including ReAct, SWE-bench, "The Second Half"
-- [[concepts/tau-squared-bench]] — τ²-bench: Dual control evaluation details
-- [[concepts/tau-knowledge]] — τ-Knowledge: Unstructured knowledge navigation evaluation details
-- [[concepts/tau-voice]] — τ-Voice: Full-duplex voice agent evaluation details
+- [[concepts/ai-benchmarks/tau-squared-bench]] — τ²-bench: Dual control evaluation details
+- [[concepts/ai-benchmarks/tau-knowledge]] — τ-Knowledge: Unstructured knowledge navigation evaluation details
+- [[concepts/ai-benchmarks/tau-voice]] — τ-Voice: Full-duplex voice agent evaluation details
 - [[concepts/evaluation/pass-k-metric]] — pass^k metric detailed explanation
 - [[concepts/ai-benchmarks/hyper-tau-bench]] — 4th generation (Sep 2026): recursive agent-building benchmark, developer reward hacking
-- [[concepts/swe-bench]] — Yao's other representative benchmark
+- [[concepts/ai-benchmarks/swe-bench]] — Yao's other representative benchmark
 
 ---
 
diff --git a/wiki/concepts/ai-benchmarks/tau-knowledge.md b/wiki/concepts/ai-benchmarks/tau-knowledge.md
index e0fe03e7..cb41cc4f 100644
--- a/wiki/concepts/ai-benchmarks/tau-knowledge.md
+++ b/wiki/concepts/ai-benchmarks/tau-knowledge.md
@@ -159,6 +159,6 @@ The new evaluation axis τ-Knowledge adds is "knowledge discovery," an essential
 ## Related Pages
 
 - [[concepts/ai-benchmarks/tau-bench]] — The base conversational agent benchmark
-- [[concepts/tau-squared-bench]] — τ²-Bench: More advanced evaluation suite
-- [[concepts/tau-voice]] — Voice interaction evaluation
+- [[concepts/ai-benchmarks/tau-squared-bench]] — τ²-Bench: More advanced evaluation suite
+- [[concepts/ai-benchmarks/tau-voice]] — Voice interaction evaluation
 - [[entities/_index]]
diff --git a/wiki/concepts/ai-benchmarks/tau-squared-bench.md b/wiki/concepts/ai-benchmarks/tau-squared-bench.md
index ee4d211f..40736342 100644
--- a/wiki/concepts/ai-benchmarks/tau-squared-bench.md
+++ b/wiki/concepts/ai-benchmarks/tau-squared-bench.md
@@ -13,8 +13,8 @@ tags:
   - company
 related:
   - "[[concepts/ai-benchmarks/tau-bench]]"
-  - "[[concepts/tau-knowledge]]"
-  - "[[concepts/tau-voice]]"
+  - "[[concepts/ai-benchmarks/tau-knowledge]]"
+  - "[[concepts/ai-benchmarks/tau-voice]]"
   - "[[concepts/evaluation/pass-k-metric]]"
 sources:
   - raw/papers/2025-06-09_2506.07982_tau-squared-bench-dual-control.md
@@ -135,7 +135,7 @@ Unlike conventional LM-based user simulators, τ²-bench's user simulator is **c
 ## Related Pages
 
 - [[concepts/ai-benchmarks/tau-bench]] — τ-bench ecosystem overview
-- [[concepts/tau-knowledge]] — Evaluation with unstructured knowledge bases
-- [[concepts/tau-voice]] — Full-duplex voice agent evaluation
+- [[concepts/ai-benchmarks/tau-knowledge]] — Evaluation with unstructured knowledge bases
+- [[concepts/ai-benchmarks/tau-voice]] — Full-duplex voice agent evaluation
 - [[concepts/evaluation/pass-k-metric]] — Reliability evaluation metric
 - [[entities/shunyu-yao]] — τ-bench original author
diff --git a/wiki/concepts/ai-benchmarks/tau-voice.md b/wiki/concepts/ai-benchmarks/tau-voice.md
index 6ad12f7e..da3e90d2 100644
--- a/wiki/concepts/ai-benchmarks/tau-voice.md
+++ b/wiki/concepts/ai-benchmarks/tau-voice.md
@@ -12,8 +12,8 @@ tags:
   - company
 related:
   - "[[concepts/ai-benchmarks/tau-bench]]"
-  - "[[concepts/tau-squared-bench]]"
-  - "[[concepts/tau-knowledge]]"
+  - "[[concepts/ai-benchmarks/tau-squared-bench]]"
+  - "[[concepts/ai-benchmarks/tau-knowledge]]"
   - "[[concepts/evaluation/pass-k-metric]]"
 sources:
   - raw/papers/2026-03-14_2603.13686_tau-voice-full-duplex-voice-agents.md
@@ -128,6 +128,6 @@ This result is significant. The bottleneck for voice agents is not **speech reco
 ## Related Pages
 
 - [[concepts/ai-benchmarks/tau-bench]] — Overview of the τ-bench ecosystem
-- [[concepts/tau-squared-bench]] — Dual-control benchmark (foundation of τ-Voice)
-- [[concepts/tau-knowledge]] — Evaluation with unstructured knowledge bases
+- [[concepts/ai-benchmarks/tau-squared-bench]] — Dual-control benchmark (foundation of τ-Voice)
+- [[concepts/ai-benchmarks/tau-knowledge]] — Evaluation with unstructured knowledge bases
 - [[concepts/evaluation/pass-k-metric]] — Reliability evaluation metric
diff --git a/wiki/concepts/ai-benchmarks/workspace-bench.md b/wiki/concepts/ai-benchmarks/workspace-bench.md
index 11771121..dbc9ebb1 100644
--- a/wiki/concepts/ai-benchmarks/workspace-bench.md
+++ b/wiki/concepts/ai-benchmarks/workspace-bench.md
@@ -49,7 +49,7 @@ The 12% gap between best AI and human, and 33.3% gap between average AI and huma
 ## Key Findings
 
 ### Harness Design Matters
-The architecture of the agent harness (how it interacts with the environment) is a major factor in cost, efficiency, and final success rates — consistent with findings from [[concepts/frontier-swe-benchmark]].
+The architecture of the agent harness (how it interacts with the environment) is a major factor in cost, efficiency, and final success rates — consistent with findings from [[concepts/ai-benchmarks/frontier-swe-benchmark]].
 
 ### Scale Is the Differentiator
 Existing benchmarks fail to capture real-world complexity because they lack the "large-scale file dependencies" present here. The 74 file types and 20GB workspace create retrieval challenges that single-file benchmarks don't test.
@@ -75,18 +75,18 @@ Uses a rubric-based evaluation framework with 7,399 rubrics covering both final
 | Benchmark | Focus | Scale |
 |-----------|-------|-------|
 | [[concepts/ai-benchmarks/swe-bench]] | PR-level code fixes | Small scope |
-| [[concepts/frontier-swe-benchmark]] | Ultra-long-horizon engineering (20h) | 17 difficult tasks |
+| [[concepts/ai-benchmarks/frontier-swe-benchmark]] | Ultra-long-horizon engineering (20h) | 17 difficult tasks |
 | **Workspace-Bench** | Multi-file workspace navigation | 20,476 files, 74 types |
-| [[concepts/kernelbench]] | Kernel-level optimization | Specialized |
-| [[concepts/agent-survival-benchmark]] | Human-normalized agent capability | Diverse tasks |
+| [[concepts/ai-benchmarks/kernelbench]] | Kernel-level optimization | Specialized |
+| [[concepts/ai-benchmarks/agent-survival-benchmark]] | Human-normalized agent capability | Diverse tasks |
 
 ## Key Significance
 
-Workspace-Bench shifts evaluation focus from "can the model write code" to "can the agent navigate and reason across a realistic professional environment." The 74-file-type heterogeneity and explicit dependency graphs make it the benchmark that most closely mirrors real knowledge-worker environments. Combined with [[concepts/frontier-swe-benchmark]]'s ultra-long-horizon perspective, these benchmarks together define the 2026 frontier of coding agent evaluation.
+Workspace-Bench shifts evaluation focus from "can the model write code" to "can the agent navigate and reason across a realistic professional environment." The 74-file-type heterogeneity and explicit dependency graphs make it the benchmark that most closely mirrors real knowledge-worker environments. Combined with [[concepts/ai-benchmarks/frontier-swe-benchmark]]'s ultra-long-horizon perspective, these benchmarks together define the 2026 frontier of coding agent evaluation.
 
 ## See Also
 
-- [[concepts/frontier-swe-benchmark]] — Ultra-long-horizon coding benchmark (20h tasks)
+- [[concepts/ai-benchmarks/frontier-swe-benchmark]] — Ultra-long-horizon coding benchmark (20h tasks)
 - [[concepts/ai-benchmarks/swe-bench]] — Standard PR-level coding benchmark
 - [[concepts/harness-engineering]] — Agent execution environment design
 - [[concepts/evaluation/ai-evals]] — AI evaluation landscape
diff --git a/wiki/concepts/ai-containment-escape.md b/wiki/concepts/ai-containment-escape.md
index 3bcb6d96..ef6ea16e 100644
--- a/wiki/concepts/ai-containment-escape.md
+++ b/wiki/concepts/ai-containment-escape.md
@@ -78,8 +78,8 @@ The classic AI boxing problem assumes:
 ## Related Concepts
 
 - [[concepts/security-and-governance/ai-safety]] — Broader AI safety frameworks
-- [[concepts/security-and-governance/agent-safety]] — Agent-specific safety
-- [[entities/openai-huggingface-incident-july-2026]] — Real-world runaway agent example
+- [[concepts/agent-safety]] — Agent-specific safety
+- [[events/openai-huggingface-incident-july-2026]] — Real-world runaway agent example
 - [[concepts/open-source-ai]] — Open-weight model ecosystem
 
 ## Sources
diff --git a/wiki/concepts/ai-control.md b/wiki/concepts/ai-control.md
index 23a90e6d..9b0e6217 100644
--- a/wiki/concepts/ai-control.md
+++ b/wiki/concepts/ai-control.md
@@ -177,6 +177,8 @@ The roadmap acknowledges several important limitations:
 - [[concepts/prompt-injection]] — A related AI security vulnerability vector
 - [[concepts/superintelligence]] — The limit at which AI control is expected to become infeasible
 - [[concepts/reliability-theory-for-ai-control]] — Formal composition rules (rare-event suppression order, Birnbaum importance) for the mitigation stack above
+- [[concepts/agent-trace-integrity]] — Failure mode: agents can delete/fabricate the traces used to audit them
+- [[concepts/instrumental-monitor-evasion]] — Failure mode: agents circumvent synchronous runtime monitors under task pressure
 
 ## Quantifying the Stack (Sept 2026)
 
diff --git a/wiki/concepts/ai-cryptographic-vulnerability-discovery.md b/wiki/concepts/ai-cryptographic-vulnerability-discovery.md
index 73344632..b2cd09ab 100644
--- a/wiki/concepts/ai-cryptographic-vulnerability-discovery.md
+++ b/wiki/concepts/ai-cryptographic-vulnerability-discovery.md
@@ -88,6 +88,6 @@ ZK Security learned that **LLM-generated PoCs are unreliable for triage**. When
 - [[concepts/ai-vulnerability-discovery]] — General AI vulnerability discovery (software, kernels, exploits)
 - [[concepts/ai-vulnerability-detection-at-scale]] — Industrial-scale LLM vulnerability scanning (Mozilla, Cloudflare)
 - [[concepts/formal-verification-llm-agents]] — Formal verification of LLM-powered agents
-- [[concepts/agentic-security]] — Security of AI agents themselves (prompt injection, MCP security)
+- [[concepts/security-and-governance/agentic-security]] — Security of AI agents themselves (prompt injection, MCP security)
 - [[entities/mozilla]] — Firefox hardening via AI vulnerability discovery
 - [[entities/cloudflare]] — Published definitive harness architecture for cyber frontier models
diff --git a/wiki/concepts/ai-discovery-acceleration.md b/wiki/concepts/ai-discovery-acceleration.md
index f284acc9..9427e686 100644
--- a/wiki/concepts/ai-discovery-acceleration.md
+++ b/wiki/concepts/ai-discovery-acceleration.md
@@ -42,7 +42,7 @@ METR lists four drivers for the lumpy pattern:
 
 ## Why it matters
 - **Policy / capability forecasting**: acceleration is domain-specific, so "time horizon to AGI" or "when will X be solved" estimates must be domain-conditional.
-- **Security**: the exploited-vs-known vulnerability gap means the attack surface is growing faster than defenders are patching — a [[concepts/ai-safety]] and [[concepts/cybersecurity]] concern.
+- **Security**: the exploited-vs-known vulnerability gap means the attack surface is growing faster than defenders are patching — a [[concepts/security-and-governance/ai-safety]] and [[concepts/cybersecurity]] concern.
 - **Evals methodology**: measuring "discovery" velocity requires domain-appropriate baselines (pre-existing problem lists, record-setting benchmarks), not a single universal metric.
 
 ## Related Pages
diff --git a/wiki/concepts/ai-energy.md b/wiki/concepts/ai-energy.md
index 8c43a114..95ff665f 100644
--- a/wiki/concepts/ai-energy.md
+++ b/wiki/concepts/ai-energy.md
@@ -290,6 +290,18 @@ Physical constraints on power delivery may impose a harder ceiling on AI scaling
 - Public opposition to data center construction is growing in water-stressed and grid-constrained regions
 - Regulatory interventions (moratoriums, efficiency mandates) are increasing, particularly in Europe
 
+### Orbital Compute as an Energy Escape Hatch (Project Suncatcher)
+
+If terrestrial power delivery is the binding constraint, one proposed escape is to move the
+data center off-Earth. Google's **Project Suncatcher** (blog.google, 2025-11-04) is the
+flagship example: a moonshot to scale ML compute in space via a network of solar-powered
+satellites carrying Google **TPU** chips, motivated directly by grid/cooling limits. Orbit
+offers near-continuous solar power with no grid interconnect, water, or land constraints —
+but trades away serviceability and adds radiation and thermal-rejection (radiator) limits.
+The launch announced a research preprint (constellation design + TPU radiation testing) and
+a **learning mission with Planet to launch two prototype satellites by early 2027**. See
+[[concepts/space-gpus]]. ^[raw/articles/2026-09-25_google_project-suncatcher-announcement.md]
+
 ---
 
 ## Open Questions
diff --git a/wiki/concepts/ai-gateway.md b/wiki/concepts/ai-gateway.md
index 6166505a..61b4320f 100644
--- a/wiki/concepts/ai-gateway.md
+++ b/wiki/concepts/ai-gateway.md
@@ -20,7 +20,7 @@ related:
   - "[[concepts/token-economics]]"
   - "[[concepts/outcome-based-pricing]]"
   - "[[concepts/llm-integration-patterns]]"
-  - "[[context-engineering/context-management]]"
+  - "[[concepts/context-engineering/context-management]]"
   - "[[concepts/infrastructure]]"
 ---
 
@@ -94,4 +94,4 @@ A single coding agent session can consume hundreds of thousands of tokens across
 - **[[concepts/token-economics]]**: Gateway cost controls are the enforcement layer; token economics provides the unit-cost analysis
 - **[[concepts/outcome-based-pricing]]**: Gateways enable tracking spend-to-outcome ratios
 - **[[concepts/llm-integration-patterns]]**: Gateway is one of several AI integration patterns
-- **[[context-engineering/context-management]]**: Context efficiency reduces gateway-routed costs
+- **[[concepts/context-engineering/context-management]]**: Context efficiency reduces gateway-routed costs
diff --git a/wiki/concepts/ai-mathematics-theorem-proving.md b/wiki/concepts/ai-mathematics-theorem-proving.md
index 6608038c..382a4b94 100644
--- a/wiki/concepts/ai-mathematics-theorem-proving.md
+++ b/wiki/concepts/ai-mathematics-theorem-proving.md
@@ -58,7 +58,7 @@ The announcement explicitly addressed questions of attribution, with OpenAI stat
 
 ## Comparison to Other AI-for-Science Efforts
 
-This work exists within a broader ecosystem of AI-for-science initiatives. [[gpt/gpt-rosalind|GPT-Rosalind]], OpenAI's model for biology and life sciences, demonstrated capabilities in protein design and genomic analysis but operated primarily in applied domains rather than pure mathematics. [[claude-science|Claude Science]] by Anthropic targets life sciences with a different approach, providing an interactive workbench for researchers. The Astra model's mathematics results are distinctive in targeting pure theoretical advances rather than applied scientific problems.
+This work exists within a broader ecosystem of AI-for-science initiatives. [[concepts/gpt/gpt-rosalind|GPT-Rosalind]], OpenAI's model for biology and life sciences, demonstrated capabilities in protein design and genomic analysis but operated primarily in applied domains rather than pure mathematics. [[claude-science|Claude Science]] by Anthropic targets life sciences with a different approach, providing an interactive workbench for researchers. The Astra model's mathematics results are distinctive in targeting pure theoretical advances rather than applied scientific problems.
 
 The formal verification workflow — generating proofs and then certifying them in Lean — connects to broader work in [[formal-verification-llm-agents|LLM-based formal verification]], where AI systems are used to produce machine-checkable proofs. The mathematics results suggest that frontier models can contribute not just to verification but to original discovery.
 
@@ -70,7 +70,7 @@ Several open questions remain about the role of AI in mathematical research. How
 
 - [[entities/openai|OpenAI]] — Company behind the Astra model and these results
 - [[concepts/station-autonomous-math-discovery|Station]] — Decentralized multi-agent math discovery on the AlphaEvolve catalogue (arXiv:2608.23691, Aug 24, 2026); complementary paradigm: multi-model collaboration vs. Astra's single-model depth + Lean certificates
-- [[gpt/gpt-rosalind|GPT-Rosalind]] — OpenAI's model for scientific discovery in biology
+- [[concepts/gpt/gpt-rosalind|GPT-Rosalind]] — OpenAI's model for scientific discovery in biology
 - [[claude-science|Claude Science]] — Anthropic's AI workbench for life sciences
 - [[formal-verification-llm-agents|Formal Verification for LLM Agents]] — Broader context for AI and formal methods
 - [[cryptography-patterns|Cryptography Patterns]] — Cryptographic concepts relevant to lattice-based results
diff --git a/wiki/concepts/ai-skepticism-movement.md b/wiki/concepts/ai-skepticism-movement.md
index b4f33482..64ff825e 100644
--- a/wiki/concepts/ai-skepticism-movement.md
+++ b/wiki/concepts/ai-skepticism-movement.md
@@ -79,3 +79,15 @@ The Anthropic copy-paste vs conceptual-ask split reframes the whole debate: **th
 - [[concepts/dark-factory-software-factory]] — the Level-5 automation thesis this movement resists (Uber: >70% of PRs agent-authored)
 - [[concepts/bitter-lesson-harnessing]] — harness engineering erodes as models improve; skill atrophy is the human-side mirror
 - [[entities/simon-willison]] — proponent of "deep human understanding" as the AI-era differentiator
+
+## State Response: The DHS "Radicalization" Assessment (Sep 2026)
+
+In September 2026 the backlash moved from culture into the **state security apparatus**.
+Investigative journalist [[entities/ken-klippenstein]] reported that DHS's research arm
+(C&TIS) opened an exploratory assessment framing domestic AI-skeptic commentary as a
+potential "radicalization"/homegrown-extremism concern. The claims are **contested** — DHS
+characterizes it as exploratory threat-landscape research, not surveillance of protected
+speech — and no primary documents are public. Details and both-sides treatment:
+[[concepts/ai-skeptic-radicalization-investigation]]. The episode is the institutional
+counterpart to the grassroots movements this page tracks: the same trust deficit driving
+skepticism is what the state allegedly treats as a risk vector.
diff --git a/wiki/concepts/ai-voice-fraud.md b/wiki/concepts/ai-voice-fraud.md
index 913e65f2..b07ff530 100644
--- a/wiki/concepts/ai-voice-fraud.md
+++ b/wiki/concepts/ai-voice-fraud.md
@@ -16,7 +16,7 @@ AI voice fraud is a rapidly emerging category of cybercrime in which attackers u
 
 The threat was crystallised in Sharon Brightwell's case (Dover, Florida, 2026): she received a call from what sounded exactly like her daughter April in distress, claiming to have caused a car accident while texting. A man posing as an attorney then demanded $15,000 in cash for bail, warning her not to tell the bank the real purpose. Brightwell complied within the hour, only discovering the fraud when she reached the real April later. The attackers had cloned her daughter's voice from a short sample — likely scraped from social media or a prior recorded call.
 
-This page covers the technology behind voice cloning, the fraud attack vectors it enables, why traditional defences fail against AI-driven voice scams, and the broader implications for [[agent-safety]] and [[security-and-governance/ai-safety-and-alignment]].
+This page covers the technology behind voice cloning, the fraud attack vectors it enables, why traditional defences fail against AI-driven voice scams, and the broader implications for [[agent-safety]] and [[concepts/security-and-governance/ai-safety-and-alignment]].
 
 ## How AI Voice Cloning Works
 
diff --git a/wiki/concepts/alignment-relativity.md b/wiki/concepts/alignment-relativity.md
index e3b19984..cfa2c3ea 100644
--- a/wiki/concepts/alignment-relativity.md
+++ b/wiki/concepts/alignment-relativity.md
@@ -34,7 +34,7 @@ This is a practitioner's *priors-skepticism* account of alignment, distinct from
 
 - It supplies the **training-data genealogy of slop** that [[concepts/ai-slop]] describes phenomenologically: slop is not random noise, it is *what non-expert reward looked like*, generalized.
 - It is an argument for the [[concepts/verification]] thesis (trust must be earned per-domain, per-principal) and against auto-rater confidence — see also [[concepts/benchmark-ceiling]]'s evaluation-scarcity point from a different angle.
-- The "no unhackable grader + efficiency rewards ⇒ permitted shortcuts" chain is a restatement of [[concepts/reward-hacking]] extended from eval gaming to *value* relativity.
+- The "no unhackable grader + efficiency rewards ⇒ permitted shortcuts" chain is a restatement of [[concepts/evaluation/reward-hacking]] extended from eval gaming to *value* relativity.
 - The principal/agent framing connects to [[concepts/principal-agent-problem]]: whose values parameterize "permissible shortcut" is exactly a principal-identity question.
 
 Confidence `medium`: a single essay, strong internal argument, no empirical support offered; retained as a named position in the alignment-debate space.
@@ -43,11 +43,11 @@ Confidence `medium`: a single essay, strong internal argument, no empirical supp
 
 - Does "irreducible complexity" survive a personalized-alignment program (per-user constitutions, org-level value specs)? The author's claim implies such specs inherit the same non-expert-reward contamination.
 - Can "fear of future regret" (long-horizon coherence) be trained, or is it a structural absence as of 2026?
-- If auto-raters inherit bad priors too, what does the wiki's [[concepts/eval-loops]] literature look like under this critique?
+- If auto-raters inherit bad priors too, what does the wiki's [[concepts/evaluation/eval-loops]] literature look like under this critique?
 
 ## See Also
 
 - [[concepts/ai-slop]] — the observable artifact of non-expert-rewarded priors
-- [[concepts/reward-hacking]] — shortcut-taking under imperfect graders
+- [[concepts/evaluation/reward-hacking]] — shortcut-taking under imperfect graders
 - [[concepts/verification]] — trust boundaries when you cannot evaluate at expert depth
 - [[entities/hyperbo]] — author
diff --git a/wiki/concepts/anthropic-cybersecurity-eval-incidents.md b/wiki/concepts/anthropic-cybersecurity-eval-incidents.md
index 44115bcc..44c33a1f 100644
--- a/wiki/concepts/anthropic-cybersecurity-eval-incidents.md
+++ b/wiki/concepts/anthropic-cybersecurity-eval-incidents.md
@@ -23,7 +23,7 @@ related:
   - "[[entities/anthropic]]"
   - "[[concepts/cyber-frontier-models]]"
   - "[[concepts/evaluation/ai-evaluation]]"
-  - "[[concepts/ai-safety]]"
+  - "[[concepts/security-and-governance/ai-safety]]"
 ---
 
 # Anthropic Cybersecurity Evaluation Incidents (2026)
@@ -116,5 +116,5 @@ Third-party commentary (kimmonismus, Zack Korman) emphasized these were **not "b
 - [[concepts/cyber-frontier-models]] — Claude models as cyber-capable frontier systems
 - [[concepts/evaluation/ai-evaluation]] — Broader evaluation methodology context
 - [[entities/anthropic]] — Anthropic entity page
-- [[concepts/ai-safety]] — AI safety considerations
+- [[concepts/security-and-governance/ai-safety]] — AI safety considerations
 - [[concepts/security-and-governance/ai-red-teaming]] — Red teaming methodology
diff --git a/wiki/concepts/apache-burr-agent-framework.md b/wiki/concepts/apache-burr-agent-framework.md
index b30cad9e..dd42c08b 100644
--- a/wiki/concepts/apache-burr-agent-framework.md
+++ b/wiki/concepts/apache-burr-agent-framework.md
@@ -20,7 +20,7 @@ sources:
 
 ## Overview
 
-Apache Burr (Incubating) is a pure Python framework for building reliable AI agents and decision-making applications. Originating from [DagWorks](https://github.com/DAGWorks-Inc) and now under the Apache Incubator, Burr provides a lightweight, composable API for developing everything from simple chatbots to complex [[multi-agents/multi-agent-systems|multi-agent systems]].
+Apache Burr (Incubating) is a pure Python framework for building reliable AI agents and decision-making applications. Originating from [DagWorks](https://github.com/DAGWorks-Inc) and now under the Apache Incubator, Burr provides a lightweight, composable API for developing everything from simple chatbots to complex [[concepts/multi-agents/multi-agent-systems|multi-agent systems]].
 
 The framework is named after Aaron Burr — a deliberate reference to the musical *Hamilton*, as Burr builds on **Hamilton**, DagWorks' micro-framework for defining typed dataflows. The naming convention (Hamilton → Burr) reflects Burr's architectural lineage: where Hamilton provides the data transformation layer, Burr adds the state-machine execution layer for agentic decision-making.
 
@@ -108,6 +108,6 @@ This mirrors a broader debate in the [[agent-framework]] ecosystem: whether fram
 ## See Also
 
 - [[concepts/langgraph]] — LangChain's event-driven agent orchestration framework
-- [[multi-agents/multi-agent-systems]] — Patterns and architectures for multi-agent coordination
+- [[concepts/multi-agents/multi-agent-systems]] — Patterns and architectures for multi-agent coordination
 - [[concepts/durable-execution]] — Long-running, fault-tolerant agent execution
 - [[concepts/ai-observability]] — Monitoring and debugging AI systems in production
diff --git a/wiki/concepts/apertus-sovereign-ai-model.md b/wiki/concepts/apertus-sovereign-ai-model.md
index 5519ddcd..276c9b58 100644
--- a/wiki/concepts/apertus-sovereign-ai-model.md
+++ b/wiki/concepts/apertus-sovereign-ai-model.md
@@ -99,8 +99,8 @@ The Hacker News discussion (523 points, 181 comments) reflected several themes:
 
 ## Related Pages
 
-- [[entities/apertus]] — The organization behind the Apertus model
-- [[entities/apertus]] — General concept overview of Apertus
+- [[concepts/apertus]] — The organization behind the Apertus model
+- [[concepts/apertus]] — General concept overview of Apertus
 - [[concepts/sovereign-ai]] — The sovereign AI movement and its geopolitical dimensions
 - [[concepts/eu-ai-act]] — European Union AI Act regulatory framework
 - [[entities/cohere]] — Cohere's sovereign AI offerings and enterprise strategy
diff --git a/wiki/concepts/apertus.md b/wiki/concepts/apertus.md
index a763eb02..197acee4 100644
--- a/wiki/concepts/apertus.md
+++ b/wiki/concepts/apertus.md
@@ -93,7 +93,7 @@ Apertus differentiates itself from other prominent open-source AI initiatives:
 - [[concepts/open-source-ai]] — Open-source strategy in AI development
 - [[concepts/eu-ai-act]] — European Union AI regulation framework
 - [[concepts/model-distillation]] — Techniques for compressing large models into smaller ones
-- [[entities/apertus]] — The organization behind the Apertus model
+- [[concepts/apertus]] — The organization behind the Apertus model
 
 ## Overview
 The Apertus project releases foundation models at 8B and 70B parameter scales, along with 16 smaller models for distillation and quantization research. All components — training data, code, weights, methods, and alignment principles — are fully documented and released openly.
diff --git a/wiki/concepts/apple-gemini-ai-architecture.md b/wiki/concepts/apple-gemini-ai-architecture.md
index f2c3cb74..32243bb4 100644
--- a/wiki/concepts/apple-gemini-ai-architecture.md
+++ b/wiki/concepts/apple-gemini-ai-architecture.md
@@ -67,6 +67,6 @@ The HN discussion highlighted several perspectives:
 
 - [[concepts/gemini|Google Gemini]] — The underlying model family
 - [[concepts/apple-intelligence|Apple Intelligence]] — Apple's prior AI strategy
-- [[entities/apple|Apple]] — Company profile
+- [[concepts/apple|Apple]] — Company profile
 - [[entities/google|Google]] — Company profile
 - [[concepts/ai-infrastructure|AI Infrastructure]] — Cloud deployment considerations
diff --git a/wiki/concepts/attractor-models.md b/wiki/concepts/attractor-models.md
index efc0c002..e866cf74 100644
--- a/wiki/concepts/attractor-models.md
+++ b/wiki/concepts/attractor-models.md
@@ -61,7 +61,7 @@ Attractor Models solve these by:
 
 ## Reasoning at Tiny Scale
 
-A 27M-parameter Attractor Model achieves 91.4% on Sudoku-Extreme and 93.1% on Maze-Hard — tasks where frontier models ([[entities/claude|Claude]], [[entities/gpt-o3|o3]], [[entities/deepseek-r1|DeepSeek-R1]]) fail completely, and specialized recursive reasoners collapse at larger scales.
+A 27M-parameter Attractor Model achieves 91.4% on Sudoku-Extreme and 93.1% on Maze-Hard — tasks where frontier models ([[entities/claude|Claude]], [[entities/gpt-o3|o3]], [[concepts/deepseek-r1|DeepSeek-R1]]) fail completely, and specialized recursive reasoners collapse at larger scales.
 
 ## Related
 
diff --git a/wiki/concepts/benjamin-clavi.md b/wiki/concepts/benjamin-clavi.md
index bc6402c7..f59e0127 100644
--- a/wiki/concepts/benjamin-clavi.md
+++ b/wiki/concepts/benjamin-clavi.md
@@ -1,25 +1,14 @@
 ---
-title: "benjamin-clavi"
+title: "benjamin-clavi (redirect)"
 type: concept
-aliases:
-  - benjamin-clavi
 created: 2026-04-25
-updated: 2026-04-25
-tags:
-  - concept
+updated: 2026-10-01
+tags: [person]
 sources: []
-status: stub
-
+status: redirect
+aliases: [benjamin-clavi]
 ---
 
-# benjamin-clavi
-
-> **TODO**: Enrich this page.
-
-## Overview
-
-Stub page for benjamin-clavi.
-
-## Related Pages
+> **Redirect**: ASCII-slug variant duplicate. See the canonical entity page [[entities/benjamin-clavie]] — Benjamin Clavié, researcher (Jina AI; matryoshka embeddings, BitNet research).
 
-- [[entities/_index]]
+Back to related coverage: [[entities/jina-ai]].
diff --git "a/wiki/concepts/benjamin-clavi\303\251.md" "b/wiki/concepts/benjamin-clavi\303\251.md"
index 1048f58c..e2fa8706 100644
--- "a/wiki/concepts/benjamin-clavi\303\251.md"
+++ "b/wiki/concepts/benjamin-clavi\303\251.md"
@@ -1,25 +1,14 @@
 ---
-title: "Benjamin Clavié"
+title: "Benjamin Clavié (redirect)"
 type: concept
-aliases:
-  - benjamin-clavié
 created: 2026-04-25
-updated: 2026-04-25
-tags:
-  - concept
+updated: 2026-10-01
+tags: [person]
 sources: []
-status: stub
-
+status: redirect
+aliases: [benjamin-clavié]
 ---
 
-# Benjamin Clavié
-
-> **TODO**: Enrich this page.
-
-## Overview
-
-Stub page for Benjamin Clavié.
-
-## Related Pages
+> **Redirect**: Duplicate of the canonical entity page. See [[entities/benjamin-clavie]] — Benjamin Clavié, researcher (Jina AI; matryoshka embeddings, BitNet research).
 
-- [[entities/_index]]
+Back to related coverage: [[entities/jina-ai]].
diff --git a/wiki/concepts/cais.md b/wiki/concepts/cais.md
index f1fedb88..483797bf 100644
--- a/wiki/concepts/cais.md
+++ b/wiki/concepts/cais.md
@@ -158,7 +158,7 @@ The CAIS model has proven remarkably prescient when viewed from 2026:
 
 - [[entities/k-eric-drexler]] — Author of the CAIS framework
 - [[concepts/superintelligence]] — Broader topic of AI surpassing human capabilities
-- [[concepts/ai-safety]] — Safety implications of advanced AI
+- [[concepts/security-and-governance/ai-safety]] — Safety implications of advanced AI
 - [[concepts/nick-bostrom]] — Contrasting agent-centric superintelligence framework
 - [[concepts/intelligence-explosion]] — Recursive self-improvement dynamics
 - [[concepts/agi-economics]] — Economic implications of generalized AI
diff --git a/wiki/concepts/claude/fable-5.md b/wiki/concepts/claude/fable-5.md
index 61ea73cd..d4fdbc74 100644
--- a/wiki/concepts/claude/fable-5.md
+++ b/wiki/concepts/claude/fable-5.md
@@ -47,7 +47,7 @@ Anthropic's Mythos-class model released for general use on June 9, 2026. State-o
 
 ## Overview
 
-Claude Fable 5 was announced on June 9, 2026 as "a Mythos-class model that we've made safe for general use." It represents the public release of Mythos-class capabilities, which Anthropic had previously restricted through [[concepts/project-glasswing|Project Glasswing]] due to safety concerns (particularly cybersecurity and dual-use biology capabilities).
+Claude Fable 5 was announced on June 9, 2026 as "a Mythos-class model that we've made safe for general use." It represents the public release of Mythos-class capabilities, which Anthropic had previously restricted through [[entities/project-glasswing|Project Glasswing]] due to safety concerns (particularly cybersecurity and dual-use biology capabilities).
 
 The longer and more complex the task, the larger Fable 5's lead over other Claude models. It was simultaneously launched with **Claude Mythos 5** — the same model with safeguards lifted, restricted to Glasswing cyber defenders and select biology researchers.
 
diff --git a/wiki/concepts/claude/models.md b/wiki/concepts/claude/models.md
index 6da9f192..b57b54c2 100644
--- a/wiki/concepts/claude/models.md
+++ b/wiki/concepts/claude/models.md
@@ -17,7 +17,7 @@ sources: [raw/articles/simonwillison.net--2026-may-28-claude-opus-4-8--8d05463f.
 
 # Claude Models
 
-Family of large language models developed by [[Anthropic]]. Named after Claude Shannon. Known for emphasis on safety, honesty, and helpfulness.
+Family of large language models developed by [[entities/anthropic|Anthropic]]. Named after Claude Shannon. Known for emphasis on safety, honesty, and helpfulness.
 
 ## Frontier Models (June 2026)
 
@@ -85,7 +85,7 @@ Anthropic trains models to avoid unsupported claims. Opus 4.8's system card quan
 - Default `max_tokens` now set to model maximum output (was 8,192)
 
 ## Related Pages
-- [[Anthropic]] — Company behind Claude
+- [[entities/anthropic|Anthropic]] — Company behind Claude
 - [[concepts/prompt-caching]] — Mechanism enabled by mid-conversation system messages
 - [[llm-anthropic]] — Simon Willison's Python/CLI tool
 - [[concepts/ai-economics]] — Tokenmaxxing and AI ROI debate
diff --git a/wiki/concepts/claude/mythos.md b/wiki/concepts/claude/mythos.md
index b1711f9a..f775bd04 100644
--- a/wiki/concepts/claude/mythos.md
+++ b/wiki/concepts/claude/mythos.md
@@ -79,7 +79,7 @@ Gary Marcus evaluated the results as finding a middle ground: Mythos is "nowhere
 On June 9, 2026, Anthropic launched two Mythos-class models simultaneously:
 
 - **[[concepts/claude/fable-5|Claude Fable 5]]**: Mythos-class model made safe for general use. Safety classifiers fall back to Opus 4.8 on cybersecurity, biology/chemistry, and distillation queries. **>95% of sessions involve no fallback.**
-- **Claude Mythos 5**: Same underlying model with safeguards lifted. Restricted to [[concepts/project-glasswing|Project Glasswing]] cyber defenders and select biology researchers.
+- **Claude Mythos 5**: Same underlying model with safeguards lifted. Restricted to [[entities/project-glasswing|Project Glasswing]] cyber defenders and select biology researchers.
 
 **Pricing:** $10/MTok input, $50/MTok output — less than half the price of Claude Mythos Preview.
 
diff --git a/wiki/concepts/cloudflare-llm-infrastructure.md b/wiki/concepts/cloudflare-llm-infrastructure.md
index d3876dff..e29260ee 100644
--- a/wiki/concepts/cloudflare-llm-infrastructure.md
+++ b/wiki/concepts/cloudflare-llm-infrastructure.md
@@ -59,6 +59,6 @@ Cloudflare's Rust-based inference engine designed for distributed global network
 Cloudflare's investments position its edge network as an inference layer for [[concepts/ai-agents|agentic workloads]]. The PD disaggregation pattern parallels [[concepts/mooncake|Mooncake's KVCache-centric architecture]], while the session affinity model addresses the [[concepts/context-engineering/context-window-management|long-context requirements]] of agent loops.
 
 ## Open Questions
-- How does Infire compare to [[concepts/inference/vllm|vLLM]] and [[entities/sglang|SGLang]] on throughput benchmarks?
+- How does Infire compare to [[concepts/inference/vllm|vLLM]] and [[concepts/inference/sglang|SGLang]] on throughput benchmarks?
 - Will Cloudflare's edge inference compete with or complement [[concepts/nvidia-dynamo|NVIDIA Dynamo]]?
 - What are the cold-start characteristics for non-Kimi models?
diff --git "a/wiki/concepts/cl\303\251mentine-fourrier.md" "b/wiki/concepts/cl\303\251mentine-fourrier.md"
index a1720e16..214d92dc 100644
--- "a/wiki/concepts/cl\303\251mentine-fourrier.md"
+++ "b/wiki/concepts/cl\303\251mentine-fourrier.md"
@@ -1,25 +1,14 @@
 ---
-title: "Clémentine Fourrier"
+title: "Clémentine Fourrier (redirect)"
 type: concept
-aliases:
-  - clémentine-fourrier
-created: 2026-04-25
-updated: 2026-04-25
-tags:
-  - concept
+created: 2026-10-01
+updated: 2026-10-01
+tags: [person]
 sources: []
-status: stub
-
+status: redirect
+aliases: [clémentine-fourrier]
 ---
 
-# Clémentine Fourrier
-
-> **TODO**: Enrich this page.
-
-## Overview
-
-Stub page for Clémentine Fourrier.
-
-## Related Pages
+> **Redirect**: Duplicate of the canonical entity page. See [[entities/clementine-fourrier]] — Clémentine Fourrier, Hugging Face leader of the Open LLM Leaderboard and Arena-Harness evaluations.
 
-- [[entities/_index]]
+Back to related coverage: [[concepts/llm-leaderboard]].
diff --git a/wiki/concepts/codex/_index.md b/wiki/concepts/codex/_index.md
index 387c2fd6..7aeffc9d 100644
--- a/wiki/concepts/codex/_index.md
+++ b/wiki/concepts/codex/_index.md
@@ -15,7 +15,7 @@ status: active
 
 OpenAI's cloud-based coding agent platform. Sub-index of all Codex concept pages.
 
-See also: [[entities/openai-codex]] (entity page), [[concepts/openai|OpenAI]] (platform)
+See also: [[entities/openai-codex]] (entity page), [[entities/openai|OpenAI]] (platform)
 
 ---
 
diff --git a/wiki/concepts/coding-agents/_index.md b/wiki/concepts/coding-agents/_index.md
index c00de821..1fa11b92 100644
--- a/wiki/concepts/coding-agents/_index.md
+++ b/wiki/concepts/coding-agents/_index.md
@@ -65,6 +65,6 @@ Tool-specific pages: [[concepts/claude-code|Claude Code]], [[concepts/codex|Code
 - [[concepts/coding-agents/ramp-inspect]] — Ramp Inspect
 - [[concepts/coding-agents/pi-autoresearch]] — pi-autoresearch
 - [[concepts/coding-agents/mandate-equinox]] — Mandate Equinox
-- [[concepts/coding-agents/bernstein]] — Bernstein (multi-agent orchestrator)
+- [[entities/bernstein]] — Bernstein (multi-agent orchestrator)
 - [[concepts/coding-agents/codeact]] — CodeAct
 - [[concepts/coding-agents/hf-cli]] — Hugging Face CLI
diff --git a/wiki/concepts/colbert.md b/wiki/concepts/colbert.md
index a69450e6..84f28aff 100644
--- a/wiki/concepts/colbert.md
+++ b/wiki/concepts/colbert.md
@@ -174,7 +174,7 @@ As Benjamin Clavié frames it:
 
 ## Related Pages
 
-- [[entities/omar-khattab/colbert]] — Omar Khattab's ColBERT deep-dive
+- [[concepts/colbert]] — Omar Khattab's ColBERT deep-dive
 - [[entities/benjamin-clavie]] — Benjamin Clavié, leading ColBERT researcher
 - [[entities/late-interaction]] — LIR Workshop @ ECIR 2026
 - [[concepts/agentic-search]] — Agentic search patterns where ColBERT excels
@@ -211,7 +211,7 @@ In December 2024, Khattab revealed that the original vision for ColBERT went bey
 
 In this framing, ColBERT's document encoder acts as a **hypernetwork** — a network that generates the parameters of another network (the query-conditional scoring function). This is a deeper architectural claim than the standard "late interaction" narrative: each document is parameterized as a learned function, and retrieval indexes should be pruning-capable (selectively evaluating only promising documents) rather than brute-force scanning all candidates.
 
-This connects to Khattab's broader [[entities/omar-khattab/philosophy|Decomposition Philosophy]]: decomposing the monolithic "single vector per document" paradigm into compositional scoring functions that can be selectively evaluated.
+This connects to Khattab's broader [[concepts/openclaw/philosophy|Decomposition Philosophy]]: decomposing the monolithic "single vector per document" paradigm into compositional scoring functions that can be selectively evaluated.
 
 Source: [[raw/articles/2024-12-31_omar-khattab_colbert-hypernetwork-retrieval]]
 
diff --git a/wiki/concepts/company-ai-pilled.md b/wiki/concepts/company-ai-pilled.md
index fe37366d..c4f022c8 100644
--- a/wiki/concepts/company-ai-pilled.md
+++ b/wiki/concepts/company-ai-pilled.md
@@ -35,7 +35,7 @@ There's a difference between "using AI" and being AI-pilled. One uses a chatbot
 - Still tool-focused, not process-focused
 
 ### Level 3: AI-Pilled
-- AI usage is reflexive and baseline (see [[entities/reflexive-ai]])
+- AI usage is reflexive and baseline (see [[concepts/reflexive-ai]])
 - Workflows redesigned around AI capabilities, not just augmented
 - Hiring and role design assumes AI collaboration
 - [[entities/solo-founder-stack]] patterns applied internally
@@ -47,8 +47,8 @@ There's a difference between "using AI" and being AI-pilled. One uses a chatbot
 
 ## Connection to Other Frameworks
 
-- [[entities/reflexive-ai]] — Shopify's Tobi Lütke memo is the canonical example of "AI-pilled" in practice
-- [[entities/company-ai-pilled]] — broader organizational change theory
+- [[concepts/reflexive-ai]] — Shopify's Tobi Lütke memo is the canonical example of "AI-pilled" in practice
+- [[concepts/company-ai-pilled]] — broader organizational change theory
 - [[entities/solo-founder-stack]] — AI-pilled companies adopt solo-founder efficiency internally
 
 ## Key Signals of Being AI-Pilled
@@ -59,7 +59,7 @@ There's a difference between "using AI" and being AI-pilled. One uses a chatbot
 4. **Cultural shift** — "using AI well is a skill that needs to be carefully learned" (Tobi Lütke)
 
 ## Related Entities
-- [[entities/company-ai-pilled]]
+- [[concepts/company-ai-pilled]]
 
 - **Khe Hy** (Khemaridh Hy) — Former Wall Street analyst, founder of Rad Reads, now running Latour AI consultancy
 - **Tobi Lütke** — Shopify CEO, author of the viral "Reflexive AI" internal memo
@@ -119,7 +119,7 @@ The bottleneck in AI adoption is not the tools — it’s **the first person wil
 Company AI Pilled is a framework advocating for **AI-driven organizational culture transformation**, not just tool adoption. The emphasis on the first person with courage and over-investment during the adoption phase serves as a practical guide for real-world enterprise AI implementation.
 
 
-## Related Concepts- [[entities/company-ai-pilled]]
+## Related Concepts- [[concepts/company-ai-pilled]]
 
 - [Reflexive AI](reflexive-ai.md) — Shopify AI adoption case study
 - [Solo Founder Stack](solo-founder-stack.md) — Solo founder AI usage
diff --git a/wiki/concepts/compositional-generalization.md b/wiki/concepts/compositional-generalization.md
index 741d76dc..6a9e5a4f 100644
--- a/wiki/concepts/compositional-generalization.md
+++ b/wiki/concepts/compositional-generalization.md
@@ -35,7 +35,7 @@ Modern post-training is a brute-force paradigm of curating ever more environment
 
 A **harness** $H: s \rightarrow a$ is the program that sits between the external world and the neural network. It decides how to encode the current state $s$ of the environment (which can be arbitrarily long and complex) into one or more inputs to the LLM and how to determine the next action.
 
-Examples: [[concepts/dspy-rlm|RLM]], [[concepts/codeact|CodeAct]], [[entities/claude-code|Claude Code]], [[entities/codex|Codex]].
+Examples: [[concepts/dspy-rlm|RLM]], [[concepts/coding-agents/codeact|CodeAct]], [[entities/claude-code|Claude Code]], [[entities/codex|Codex]].
 
 ### Locally In-Distribution (LID) Observations
 
@@ -44,7 +44,7 @@ A good harness shapes each call to the underlying Transformer so that every obse
 > "A good harness is a harness that *reduces unfamiliar problems to familiar ones* and *reduces complex problems to simple ones*."
 > — Zhang & Khattab (2026)
 
-**Why existing harnesses fail at LID:** Claude Code and Codex fundamentally rely on flooding the context window with interleaved task-specific information, tool call outputs, and reasoning that get continuously appended. This causes **[[concepts/context-rot|context rot]]** — bloated histories quickly fall out of the training distribution.
+**Why existing harnesses fail at LID:** Claude Code and Codex fundamentally rely on flooding the context window with interleaved task-specific information, tool call outputs, and reasoning that get continuously appended. This causes **[[concepts/context-engineering/context-rot|context rot]]** — bloated histories quickly fall out of the training distribution.
 
 ### Harness-Induced Equivalence Classes
 
@@ -105,6 +105,6 @@ The argument is NOT to impose problem-specific programmatic strategies (which wo
 - [[entities/omar-khattab/rlm]] — RLM as Khattab's research program
 - [[entities/alex-zhang]] — First author
 - [[concepts/mismanaged-geniuses-hypothesis]] — MGH thesis
-- [[concepts/context-rot]] — Why naive harnesses fail
+- [[concepts/context-engineering/context-rot]] — Why naive harnesses fail
 - [[concepts/bitter-lesson]] — Scaling vs. design tension
 - [[entities/omar-khattab]] — Co-author
diff --git a/wiki/concepts/comprehensive-ai-services.md b/wiki/concepts/comprehensive-ai-services.md
index 15a433d2..fa97f2c2 100644
--- a/wiki/concepts/comprehensive-ai-services.md
+++ b/wiki/concepts/comprehensive-ai-services.md
@@ -81,7 +81,7 @@ Drexler argues that standard "intelligence explosion" models (fast takeoff drive
 ## Related Concepts
 
 - [[concepts/superintelligence]] — Broader topic of AI surpassing human capabilities
-- [[concepts/ai-safety]] — Safety implications of advanced AI
+- [[concepts/security-and-governance/ai-safety]] — Safety implications of advanced AI
 - [[concepts/nick-bostrom]] — Alternative agent-centric superintelligence framework
 - [[entities/future-of-humanity-institute]] — Institution where CAIS was developed
 - [[entities/eric-drexler]] — Author of the CAIS framework
diff --git a/wiki/concepts/context-as-memory-hierarchy.md b/wiki/concepts/context-as-memory-hierarchy.md
index aed282c6..e07cc224 100644
--- a/wiki/concepts/context-as-memory-hierarchy.md
+++ b/wiki/concepts/context-as-memory-hierarchy.md
@@ -73,7 +73,7 @@ As models improve, yesterday's L3 becomes tomorrow's L2, yesterday's L2 collapse
 ## Related Concepts
 
 - [[concepts/context-engineering|Context Engineering]] — broader discipline of designing agent context
-- [[concepts/context-compression|Context Compression]] — techniques for reducing token usage
+- [[concepts/context-engineering/context-compression|Context Compression]] — techniques for reducing token usage
 - [[concepts/progressive-disclosure|Progressive Disclosure]] — UX pattern of revealing complexity on demand
 - [[concepts/prompt-caching|Prompt Caching]] — infrastructure-level caching of prompt prefixes
 - [[concepts/agent-architecture|Agent Architecture]] — structural patterns for AI agents
diff --git a/wiki/concepts/custom-ai-silicon.md b/wiki/concepts/custom-ai-silicon.md
index 36b410fc..bf929114 100644
--- a/wiki/concepts/custom-ai-silicon.md
+++ b/wiki/concepts/custom-ai-silicon.md
@@ -211,5 +211,5 @@ The custom silicon boom means more choice and lower costs:
 - [[entities/nvidia]] — NVIDIA's Vera Rubin platform, Blackwell GPUs, and $81.6B data center business
 - [[entities/google]] — Google TPU dominance in custom ASIC deployment
 - [[concepts/inference]] — Inference as the dominant AI workload
-- [[concepts/gpu-vram-fundamentals]] — GPU memory and bandwidth fundamentals
+- [[concepts/training-infra/gpu-vram-fundamentals]] — GPU memory and bandwidth fundamentals
 - [[concepts/compute-scaling-bottlenecks]] — SRAM vs HBM tradeoffs in AI hardware
diff --git a/wiki/concepts/deep-research.md b/wiki/concepts/deep-research.md
index cd909208..262ea006 100644
--- a/wiki/concepts/deep-research.md
+++ b/wiki/concepts/deep-research.md
@@ -146,7 +146,7 @@ Sources: [NVIDIA Developer Blog](https://developer.nvidia.com/blog/add-a-special
 - [[concepts/reasoning-aware-retrieval]] — Jointly embedding agent reasoning traces with search queries (AgentIR-4B, 2026)
 - [[concepts/bm25]] — Classical lexical retrieval; performs differently in agent loops vs. one-shot
 - [[concepts/deep-research-agent-from-scratch]] — Building research agents from scratch (Hugo Bowne-Anderson + Ivan Leo workshop)
-- [[concepts/browsecomp]] — The BrowseComp benchmark series
+- [[concepts/ai-benchmarks/browsecomp]] — The BrowseComp benchmark series
 - [[concepts/mutually-assured-distraction]] — Better retrieval → more convincing distractors → more confidently wrong answers
 - [[concepts/context-engineering/context-window-management|Context Window Management]] — Why long context doesn't eliminate retrieval needs
 
diff --git a/wiki/concepts/deployment-simulation.md b/wiki/concepts/deployment-simulation.md
index 2e8cd51e..249a5511 100644
--- a/wiki/concepts/deployment-simulation.md
+++ b/wiki/concepts/deployment-simulation.md
@@ -101,7 +101,7 @@ The quality of deployment simulation depends entirely on how realistic the user
 
 ### Judge-as-Agent
 
-Both use an LLM-based judge to evaluate conversations — an instance of [[concepts/llm-as-judge|LLM-as-judge]] applied to agent evaluation. This introduces a meta-evaluation challenge: who judges the judge?
+Both use an LLM-based judge to evaluate conversations — an instance of [[concepts/evaluation/llm-as-judge|LLM-as-judge]] applied to agent evaluation. This introduces a meta-evaluation challenge: who judges the judge?
 
 ### From Testing to Continuous Validation
 
diff --git a/wiki/concepts/elastic-ep.md b/wiki/concepts/elastic-ep.md
index 10749cdd..ac197009 100644
--- a/wiki/concepts/elastic-ep.md
+++ b/wiki/concepts/elastic-ep.md
@@ -17,13 +17,13 @@ updated: 2026-04-27
 | Field | Value |
 |-------|-------|
 | **Type** | Inference Infrastructure / Fault Tolerance |
-| **Related To** | [[entities/sglang]], [[entities/lmsys-org]], [[Mooncake]] |
+| **Related To** | [[concepts/inference/sglang]], [[entities/lmsys-org]], [[concepts/mooncake|Mooncake]] |
 | **Introduced** | March 2026 |
 | **Source** | LMSYS Blog "Elastic EP in SGLang: Achieving Partial Failure Tolerance" |
 
 ## Overview
 
-**Elastic EP** is a fault-tolerant expert parallelism mechanism for Mixture-of-Experts (MoE) model deployments, built into [[entities/sglang]]. Developed by the Mooncake Team at Volcano Engine, it addresses the reliability challenge of "wide" EP deployments (32+ GPUs) for models like DeepSeek V3/V4.
+**Elastic EP** is a fault-tolerant expert parallelism mechanism for Mixture-of-Experts (MoE) model deployments, built into [[concepts/inference/sglang]]. Developed by the Mooncake Team at Volcano Engine, it addresses the reliability challenge of "wide" EP deployments (32+ GPUs) for models like DeepSeek V3/V4.
 
 ## The Problem
 
diff --git a/wiki/concepts/enterprise-rle.md b/wiki/concepts/enterprise-rle.md
index f3e98dc6..c03ab527 100644
--- a/wiki/concepts/enterprise-rle.md
+++ b/wiki/concepts/enterprise-rle.md
@@ -73,6 +73,6 @@ This extends frontier AI diffusion beyond first-party products into the broader
 ## See Also
 
 - [[entities/microsoft-ai-team]] — Microsoft AI team and MAI model family
-- [[concepts/reinforcement-learning]] — RL fundamentals
+- [[concepts/post-training/reinforcement-learning]] — RL fundamentals
 - [[concepts/hill-climbing]] — Hill-climbing as an optimization paradigm
-- [[concepts/model-routing]] — Routing traffic to optimal models by task
+- [[concepts/coding-agents/model-routing]] — Routing traffic to optimal models by task
diff --git a/wiki/concepts/epd-disaggregation.md b/wiki/concepts/epd-disaggregation.md
index dd724417..b4f8dd25 100644
--- a/wiki/concepts/epd-disaggregation.md
+++ b/wiki/concepts/epd-disaggregation.md
@@ -16,13 +16,13 @@ updated: 2026-04-27
 | Field | Value |
 |-------|-------|
 | **Type** | Inference Architecture / VLM Serving |
-| **Related To** | [[entities/sglang]], [[entities/lmsys-org]], Vision-Language Models |
+| **Related To** | [[concepts/inference/sglang]], [[entities/lmsys-org]], Vision-Language Models |
 | **Introduced** | January 2026 |
 | **Source** | LMSYS Blog "EPD Disaggregation: Elastic Encoder Scaling for VLMs in SGLang" |
 
 ## Overview
 
-**EPD (Encoder-Prefill-Decode) Disaggregation** is a three-tier serving architecture for Vision-Language Models (VLMs) in [[entities/sglang]]. It separates vision encoding from language processing, enabling independent scaling of encoder servers without affecting language model deployment.
+**EPD (Encoder-Prefill-Decode) Disaggregation** is a three-tier serving architecture for Vision-Language Models (VLMs) in [[concepts/inference/sglang]]. It separates vision encoding from language processing, enabling independent scaling of encoder servers without affecting language model deployment.
 
 Developed by rednote (Xiaohongshu), Alibaba Cloud Computing, and AntGroup SCT.
 
diff --git a/wiki/concepts/evaluation/pass-k-metric.md b/wiki/concepts/evaluation/pass-k-metric.md
index c05d57f0..48c083dc 100644
--- a/wiki/concepts/evaluation/pass-k-metric.md
+++ b/wiki/concepts/evaluation/pass-k-metric.md
@@ -14,9 +14,9 @@ tags:
 sources: []
 related:
   - "[[concepts/ai-benchmarks/tau-bench]]"
-  - "[[concepts/tau-squared-bench]]"
-  - "[[concepts/tau-knowledge]]"
-  - "[[concepts/tau-voice]]"
+  - "[[concepts/ai-benchmarks/tau-squared-bench]]"
+  - "[[concepts/ai-benchmarks/tau-knowledge]]"
+  - "[[concepts/ai-benchmarks/tau-voice]]"
 ---
 
 # pass^k
diff --git a/wiki/concepts/experience-is-a-tax.md b/wiki/concepts/experience-is-a-tax.md
index ab0905cb..91e8065d 100644
--- a/wiki/concepts/experience-is-a-tax.md
+++ b/wiki/concepts/experience-is-a-tax.md
@@ -21,11 +21,11 @@ The thesis that traditional experience and seniority in knowledge work is becomi
 
 ## Evidence
 
-The concept went viral in April 2026 (5,792 bookmarks, 2.83M impressions), indicating strong resonance with current debates about AI's impact on professional skill valuation. This aligns with [[entities/reflexive-ai]] at Shopify, where Tobi Lütke advocates for "beginner's mindset" and hiring more beginners.
+The concept went viral in April 2026 (5,792 bookmarks, 2.83M impressions), indicating strong resonance with current debates about AI's impact on professional skill valuation. This aligns with [[concepts/reflexive-ai]] at Shopify, where Tobi Lütke advocates for "beginner's mindset" and hiring more beginners.
 
 ## Relationship to Reflexive AI
 
-The "experience tax" is the individual-level manifestation of the organizational-level shift toward [[entities/reflexive-ai]]. When AI becomes the baseline, those with the most to unlearn (senior workers) face the highest adoption cost.
+The "experience tax" is the individual-level manifestation of the organizational-level shift toward [[concepts/reflexive-ai]]. When AI becomes the baseline, those with the most to unlearn (senior workers) face the highest adoption cost.
 
 ## Critiques
 
@@ -35,7 +35,7 @@ The "experience tax" is the individual-level manifestation of the organizational
 
 ## Related
 
-- [[entities/reflexive-ai]]
+- [[concepts/reflexive-ai]]
 - [[entities/solo-founder-stack]]
 - [[concepts/vibe-coding]]
 - [[concepts/coding-agents/ai-coding-reliability]]
diff --git a/wiki/concepts/federated-tiny-training-engine.md b/wiki/concepts/federated-tiny-training-engine.md
index 5195cee9..af8c5350 100644
--- a/wiki/concepts/federated-tiny-training-engine.md
+++ b/wiki/concepts/federated-tiny-training-engine.md
@@ -73,6 +73,6 @@ FTTE is described as "the first practical and scalable solution for real-world F
 
 ## Related Pages
 - [[concepts/privacy-preserving-ml]] — Broader privacy-preserving ML techniques
-- [[concepts/distributed-training]] — Distributed ML training approaches
+- [[concepts/training-infra/distributed-training]] — Distributed ML training approaches
 - [[concepts/edge-computing]] — Edge device deployment
 - [[concepts/post-training/quantization-overview]] — Related model compression technique for edge deployment
diff --git a/wiki/concepts/federation-of-experts.md b/wiki/concepts/federation-of-experts.md
index 3689eaa1..7e2539f7 100644
--- a/wiki/concepts/federation-of-experts.md
+++ b/wiki/concepts/federation-of-experts.md
@@ -57,7 +57,7 @@ FoE represents a practical advance in distributed LLM inference. Its approach is
 ## Related
 
 - [[concepts/mixture-of-experts]] — Foundational MoE concept
-- [[concepts/distributed-training]] — Related distributed computing concepts
+- [[concepts/training-infra/distributed-training]] — Related distributed computing concepts
 - [[concepts/inference]] — Broader inference optimization techniques
 - [[concepts/speculative-decoding]] — Complementary latency reduction approach
 - [[concepts/kv-cache]] — KV cache management for inference
diff --git a/wiki/concepts/frontier-model-benchmarks-2026h2.md b/wiki/concepts/frontier-model-benchmarks-2026h2.md
index 8c26f2f7..feaeeff2 100644
--- a/wiki/concepts/frontier-model-benchmarks-2026h2.md
+++ b/wiki/concepts/frontier-model-benchmarks-2026h2.md
@@ -30,7 +30,7 @@ aliases: ["Frontier Model Benchmarks July-September 2026", "frontier bench suite
 
 ## Key Findings
 
-1. **Abstract reasoning is still unsolved.** ARC-AGI-3 remains near-random for every frontier model — even Fable 5's "13-hour autonomous run" (see [[concepts/arc-agi-3]]) scored 0.50 normalized against 0.28 random. The capability that *is* near-saturated is the old one: ARC-AGI-1 at 84.6–95.2%.
+1. **Abstract reasoning is still unsolved.** ARC-AGI-3 remains near-random for every frontier model — even Fable 5's "13-hour autonomous run" (see [[concepts/ai-benchmarks/arc-agi-3]]) scored 0.50 normalized against 0.28 random. The capability that *is* near-saturated is the old one: ARC-AGI-1 at 84.6–95.2%.
 2. **Long-context memory degrades sharply with budget.** On LIFE, scores collapse from 53.9% (full context) to 35.3% (4000-token budget) — "a long multi-session conversation compressed into one prompt is not the same thing as memory."
 3. **Effort is a first-class variable.** LIFE: 25.5% → 35.3% low→xhigh; HLE: 46.2% → 53.3%; GPT-5.4 beats GPT-5.5 on 7 of 10 LIFE domains at *low* effort. Single-number "model X > model Y" claims are meaningless without the effort setting.
 4. **Real-world agent loops still fail.** All six Vending-Bench 2 runs failed (bankruptcy or runtime crash) — operational failures, not reasoning failures. A different eval (UEBench, 14.9M tokens of consumer-electronics queries) shows the opposite: near-ceiling *semantic* quality (94.8%). Agent competence and answer quality are separate, uncoupled axes.
@@ -46,6 +46,6 @@ aliases: ["Frontier Model Benchmarks July-September 2026", "frontier bench suite
 ## See Also
 
 - [[concepts/benchmark-ceiling]] — why near-floor and near-ceiling regimes need different reporting
-- [[concepts/arc-agi-3]] — detailed page on the ARC-AGI-3 results
+- [[concepts/ai-benchmarks/arc-agi-3]] — detailed page on the ARC-AGI-3 results
 - [[concepts/evaluation-integrity]] — contamination, self-report, and verification
 - [[concepts/agents-last-exam]] — the closing-benchmark argument this suite implicitly tests
diff --git a/wiki/concepts/grok-computer.md b/wiki/concepts/grok-computer.md
index 135dff3c..c64026af 100644
--- a/wiki/concepts/grok-computer.md
+++ b/wiki/concepts/grok-computer.md
@@ -33,7 +33,7 @@ Together they form xAI's vision of AI that actively does computer-based work —
 
 ## Comparison with Other Computer Use Agents
 
-| Feature | Grok Computer | [[concepts/claude-computer-use|Claude Computer Use]] | [[concepts/anthropic-computer-use|Anthropic Computer Use]] |
+| Feature | Grok Computer | [[concepts/claude-computer-use|Claude Computer Use]] | [[entities/anthropic-computer-use|Anthropic Computer Use]] |
 |---------|--------------|----------------------|--------------------------|
 | Method | Pixel reading | Screenshot + coordinates | Screenshot + coordinates |
 | Legacy SW | Full support (pixel-based) | Limited | Limited |
diff --git a/wiki/concepts/harness-learning.md b/wiki/concepts/harness-learning.md
index 8c40b571..6c174378 100644
--- a/wiki/concepts/harness-learning.md
+++ b/wiki/concepts/harness-learning.md
@@ -46,7 +46,7 @@ The proposer is trained with **RL**, where the reward is the task performance ac
 This sits at the intersection of two ideas already in the wiki:
 
 1. **Harness engineering** ([[concepts/agent-harnesses]], [[concepts/bitter-lesson-agent-harnesses]]) treats the harness as hand-authored scaffolding. Harness learning automates that authorship — the harness becomes something the agent *learns to write* for itself.
-2. **Training-free / test-time adaptation** ([[concepts/test-time-compute]], [[concepts/training-free-rl]]) usually means spending more *inference compute* (more CoT tokens, more samples). Harness learning adapts by spending compute on *rewriting the program* instead.
+2. **Training-free / test-time adaptation** ([[concepts/test-time-compute]], [[concepts/post-training/training-free-rl]]) usually means spending more *inference compute* (more CoT tokens, more samples). Harness learning adapts by spending compute on *rewriting the program* instead.
 
 The analogy to gradient descent is the sharpest claim: **harness revision ≈ weight update**, but in program space. This gives a path toward agents that turn accumulated execution experience into generalizable improvements, rather than only into a longer context.
 
diff --git a/wiki/concepts/hisparse.md b/wiki/concepts/hisparse.md
index 927a398e..1c82456c 100644
--- a/wiki/concepts/hisparse.md
+++ b/wiki/concepts/hisparse.md
@@ -17,13 +17,13 @@ updated: 2026-04-27
 | Field | Value |
 |-------|-------|
 | **Type** | Memory Management / Inference Optimization |
-| **Related To** | [[entities/sglang]], [[entities/lmsys-org]] |
+| **Related To** | [[concepts/inference/sglang]], [[entities/lmsys-org]] |
 | **Introduced** | April 2026 |
 | **Paper/Post** | LMSYS Blog "HiSparse: Turbocharging Sparse Attention with Hierarchical Memory" |
 
 ## Overview
 
-**HiSparse** is a hierarchical memory system for sparse attention in LLM inference, developed by the [[entities/sglang]] team at [[entities/lmsys-org]]. It addresses the memory capacity bottleneck in sparse attention by offloading inactive KV cache entries to CPU host memory (RAM) while keeping hot data accessible in GPU HBM.
+**HiSparse** is a hierarchical memory system for sparse attention in LLM inference, developed by the [[concepts/inference/sglang]] team at [[entities/lmsys-org]]. It addresses the memory capacity bottleneck in sparse attention by offloading inactive KV cache entries to CPU host memory (RAM) while keeping hot data accessible in GPU HBM.
 
 Sparse attention (e.g., top-k selection) reduces compute and I/O costs but traditionally doesn't solve the memory capacity bottleneck — the full KV cache must remain in GPU HBM. HiSparse enables significantly larger decoding batch sizes and higher throughput.
 
diff --git a/wiki/concepts/land-rush-cicd.md b/wiki/concepts/land-rush-cicd.md
index f0868e6c..53da934a 100644
--- a/wiki/concepts/land-rush-cicd.md
+++ b/wiki/concepts/land-rush-cicd.md
@@ -86,7 +86,7 @@ Yegge predicts:
 - [[concepts/wheelhouse]] — Where Land Rush was first implemented
 - [[concepts/wish-factory]] — Pattern that generates even more commits
 - [[concepts/agentic-engineering]] — Broader engineering discipline
-- [[concepts/agent-orchestration]] — Orchestration patterns that generate high commit rates
+- [[concepts/multi-agents/agent-orchestration]] — Orchestration patterns that generate high commit rates
 
 ## Sources
 
diff --git a/wiki/concepts/latent-terms.md b/wiki/concepts/latent-terms.md
index 0c1d7e00..185dcb7a 100644
--- a/wiki/concepts/latent-terms.md
+++ b/wiki/concepts/latent-terms.md
@@ -86,6 +86,6 @@ Antoine Chaffin echoed this, noting the study's importance lies in "the future d
 
 ## Related Concepts
 
-- [[concepts/late-interaction|Late Interaction]] — another approach to going beyond single-vector scoring, using multi-token representations
+- [[entities/late-interaction|Late Interaction]] — another approach to going beyond single-vector scoring, using multi-token representations
 - [[concepts/colbert|ColBERT and SPLADE]] — learned sparse retrieval methods that Latent Terms are benchmarked against
 - [[concepts/sparse-autoencoders|Sparse Autoencoders]] — the core extraction mechanism underlying Latent Terms
diff --git a/wiki/concepts/llama-4.md b/wiki/concepts/llama-4.md
index b9dbf823..5ced33f1 100644
--- a/wiki/concepts/llama-4.md
+++ b/wiki/concepts/llama-4.md
@@ -59,7 +59,7 @@ The open-weight vs open-source debate continues with LLaMA 4's custom license te
 
 ## See Also
 
-- [[concepts/llama-3|LLaMA 3]] — Previous generation
+- [[entities/llama-3|LLaMA 3]] — Previous generation
 - [[concepts/deepseek-v4|DeepSeek V4]] — Key competitor
 - [[concepts/open-weight-ai|Open-Weight AI]] — Licensing philosophy
 - [[entities/meta|Meta AI]] — Developer organization
diff --git a/wiki/concepts/llm-architecture-complexity.md b/wiki/concepts/llm-architecture-complexity.md
index 96795528..3a3e6b84 100644
--- a/wiki/concepts/llm-architecture-complexity.md
+++ b/wiki/concepts/llm-architecture-complexity.md
@@ -104,7 +104,7 @@ As [[entities/andrej-karpathy|Andrej Karpathy]] has demonstrated over years of w
 Raschka identifies **multi-head latent attention (MLA)** as the clear winner of the KV cache efficiency competition. MLA uses compressed key-value representations, dramatically reducing the memory footprint of long-context inference. Combined with sparse attention patterns and hybrid architectures, MLA enables affordable long-context processing in modern models like Qwen 3.5.
 
 ### RLVR and the Future of Process Verification
-[[concepts/rlvr|Reinforcement learning with verifiable rewards (RLVR)]] has become a major post-training technique since DeepSeek-R1 (2025). Unlike pre-training and SFT which share the same underlying loss function, RLVR introduces a separate objective based on whether the model's output — a correct math answer, a passing test — is correct. The verification happens at the **end** of the attempt.
+[[concepts/post-training/rlvr|Reinforcement learning with verifiable rewards (RLVR)]] has become a major post-training technique since DeepSeek-R1 (2025). Unlike pre-training and SFT which share the same underlying loss function, RLVR introduces a separate objective based on whether the model's output — a correct math answer, a passing test — is correct. The verification happens at the **end** of the attempt.
 
 Raschka predicts the next frontier is **process reward models (PRMs)** that check intermediate reasoning steps, not just final answers. DeepSeek-R1 already experimented with this but found it 'had not worked particularly well.' A future model may combine RLVR with a reliable enough PRM to strengthen the model's refinement loop.
 
diff --git a/wiki/concepts/llm-cost-crisis.md b/wiki/concepts/llm-cost-crisis.md
index eac094ca..f0cb4366 100644
--- a/wiki/concepts/llm-cost-crisis.md
+++ b/wiki/concepts/llm-cost-crisis.md
@@ -17,7 +17,7 @@ related:
   - "[[concepts/token-economics]]"
   - "[[concepts/outcome-based-pricing]]"
   - "[[concepts/ai-gateway]]"
-  - "[[context-engineering/context-management]]"
+  - "[[concepts/context-engineering/context-management]]"
   - "[[concepts/inference-hardware]]"
   - "[[concepts/agentic-search]]"
 ---
@@ -99,6 +99,6 @@ Companies that fail to manage AI costs risk "AI bill shock" — monthly charges
 
 ## Related Crises
 
-- **[[context-engineering/context-management]]**: The longer the context, the higher the cost. Context management is the engineering discipline that fights the tokenpocalypse.
+- **[[concepts/context-engineering/context-management]]**: The longer the context, the higher the cost. Context management is the engineering discipline that fights the tokenpocalypse.
 - **[[concepts/agentic-search]]**: Agentic search can consume 20–50× more tokens than simple RAG, making it a primary cost driver.
 - **[[concepts/inference-hardware]]**: The hardware layer determines the floor cost. Cheaper hardware directly changes the economics.
diff --git a/wiki/concepts/llm-creative-writing.md b/wiki/concepts/llm-creative-writing.md
index 66b7fe8e..82670d1d 100644
--- a/wiki/concepts/llm-creative-writing.md
+++ b/wiki/concepts/llm-creative-writing.md
@@ -86,4 +86,4 @@ The techniques in this concept are directly applicable to improving AI-generated
 - [[entities/gwern]] — Gwern Branwen, author of this methodology
 - [[concepts/prompt-engineering]] — Broader context for anti-examples technique
 - [[concepts/llm-personalization]] — Related concept for style transfer (if exists)
-- [[wiki/concepts/agent-harness]] — Harness-level approach to quality control
+- [[concepts/harness-engineering/agent-harness]] — Harness-level approach to quality control
diff --git a/wiki/concepts/llm-text-detection-classical-ml.md b/wiki/concepts/llm-text-detection-classical-ml.md
index f64bc52c..2c2995a9 100644
--- a/wiki/concepts/llm-text-detection-classical-ml.md
+++ b/wiki/concepts/llm-text-detection-classical-ml.md
@@ -82,7 +82,7 @@ The blog post also explored adversarial bypass techniques:
 1. **Translation round-trip method**: Translating LLM-generated text to another language and back to English — partially degraded detection accuracy but did not fully defeat the classifier
 2. **LLM prompt method**: Instructing the LLM to "write like a human" or mimic specific stylistic quirks — showed some success at evasion but reduced output quality
 
-These findings highlight an ongoing [[evaluation/red-teaming-adversarial-eval|red-teaming and adversarial evaluation]] dynamic, where detectors and evasion techniques co-evolve.
+These findings highlight an ongoing [[concepts/evaluation/red-teaming-adversarial-eval|red-teaming and adversarial evaluation]] dynamic, where detectors and evasion techniques co-evolve.
 
 ## Implications for AI Safety
 
@@ -109,7 +109,7 @@ Classical ML detection differs from neural/[[deep-learning]] approaches in sever
 | **Adversarial robustness** | Moderate (features are harder to directly optimize against) | Variable (susceptible to embedding-space attacks) |
 | **Deployment cost** | Near-zero (runs in browser) | Requires GPU/compute infrastructure |
 
-The classical ML approach challenges the assumption that complex problems always require complex solutions. For AIGC detection specifically, surface-level statistical patterns may be sufficient when the goal is screening rather than forensic certainty. This aligns with broader [[evaluation/ai-benchmarks-and-evals|benchmark and evaluation]] philosophy that appropriate metrics should match the deployment context — a fast, cheap, interpretable classifier may be more useful in production than a slightly more accurate but expensive neural model.
+The classical ML approach challenges the assumption that complex problems always require complex solutions. For AIGC detection specifically, surface-level statistical patterns may be sufficient when the goal is screening rather than forensic certainty. This aligns with broader [[concepts/evaluation/ai-benchmarks-and-evals|benchmark and evaluation]] philosophy that appropriate metrics should match the deployment context — a fast, cheap, interpretable classifier may be more useful in production than a slightly more accurate but expensive neural model.
 
 ## Current Debates
 
diff --git a/wiki/concepts/local-llm/local-ai.md b/wiki/concepts/local-llm/local-ai.md
index be6c73f8..1fca0a61 100644
--- a/wiki/concepts/local-llm/local-ai.md
+++ b/wiki/concepts/local-llm/local-ai.md
@@ -40,7 +40,7 @@ related:
 
 **What this is**: The current state of "local AI" — individuals running LLMs on their own hardware at home or office. The collective practice of running open-weight models on self-owned GPUs or unified memory machines, without using cloud APIs (GPT/Claude). Covers hardware selection, model quality, inference speed, software stacks, and actual use cases.
 
-**What this is not**: Not a comparison table of cloud LLMs. Not about data center/enterprise inference (that's the domain of [[concepts/vllm]] and [[entities/sglang]]). Not about model training/fine-tuning (that's the domain of [[concepts/local-llm/model-distillation]]).
+**What this is not**: Not a comparison table of cloud LLMs. Not about data center/enterprise inference (that's the domain of [[concepts/vllm]] and [[concepts/inference/sglang]]). Not about model training/fine-tuning (that's the domain of [[concepts/local-llm/model-distillation]]).
 
 ---
 
@@ -72,7 +72,7 @@ Mac Mini → NVIDIA DGX Spark → 5090 eGPU + gaming rig → Strix Halo Framewor
 
 ### Hardware Details
 - **DGX Spark**: → [[entities/nvidia-dgx-spark]], [[concepts/dgx-spark-local-llm-server]]
-- **Mac Studio**: → [[entities/mac-studio-local-ai]]
+- **Mac Studio**: → [[concepts/mac-studio-local-ai]]
 - **Inference hardware general**: → [[concepts/local-llm/local-llm-inference-hardware]]
 
 ---
@@ -145,7 +145,7 @@ LiteLLM automatically routes to the appropriate model based on query complexity.
 | **ollama** | Easy model execution | → [[concepts/ollama]] |
 | **LM Studio** | GUI model management | Beginner-friendly |
 | **LiteLLM** | Local LLM router | OpenAI API-compatible, multi-model routing |
-| **vLLM** | High-throughput inference server | → [[concepts/vllm]], [[entities/sglang]] |
+| **vLLM** | High-throughput inference server | → [[concepts/vllm]], [[concepts/inference/sglang]] |
 | **llama.cpp** | CPU inference/GGUF quantization | → [[concepts/llama-cpp]] |
 
 ### AI Agent Frameworks
@@ -256,7 +256,7 @@ Ahmad Osman's workshop reinforces and extends the [[concepts/local-llm/local-ai]
 - [[concepts/local-llm/_index]] — Local LLM overview
 - [[concepts/local-llm/local-llm-inference-hardware]] — Inference hardware details
 - [[concepts/local-llm/local-llm-models-april-2026]] — Per-model benchmarks
-- [[entities/mac-studio-local-ai]] — Mac Studio inference environment
+- [[concepts/mac-studio-local-ai]] — Mac Studio inference environment
 - [[concepts/dgx-spark-local-llm-server]] — DGX Spark inference server setup
 - [[concepts/local-llm/local-llm-server-setup-on-dgx-spark]] — DGX Spark setup guide
 - [[concepts/ollama]] — Ollama runner
diff --git a/wiki/concepts/mac-studio-local-ai.md b/wiki/concepts/mac-studio-local-ai.md
index c320f395..ce4bbf41 100644
--- a/wiki/concepts/mac-studio-local-ai.md
+++ b/wiki/concepts/mac-studio-local-ai.md
@@ -82,7 +82,7 @@ Mixture-of-Experts models keep all weights in memory but activate only a subset
 - What's the energy efficiency comparison vs cloud GPU inference per token?
 
 ## Related Concepts
-- [[entities/mac-studio-local-ai]]
+- [[concepts/mac-studio-local-ai]]
 - [[concepts/nvidia-egpu-macos]]
 - [[concepts/dflash-ggml]]
 
diff --git a/wiki/concepts/memory-systems-bitter-lesson.md b/wiki/concepts/memory-systems-bitter-lesson.md
index 42da5bfd..0ef9a973 100644
--- a/wiki/concepts/memory-systems-bitter-lesson.md
+++ b/wiki/concepts/memory-systems-bitter-lesson.md
@@ -64,7 +64,7 @@ Applying the Bitter Lesson to memory systems is debatable:
 ## Related Concepts
 
 - [[concepts/claude/perfect-memory]] — File-based memory in practice
-- [[entities/company-ai-pilled]] — AI adoption maturity model
+- [[concepts/company-ai-pilled]] — AI adoption maturity model
 - [[entities/autoreason]] — Self-improving reasoning
 
 ## Sources
diff --git a/wiki/concepts/meta-muse-spark.md b/wiki/concepts/meta-muse-spark.md
index 6d63bbec..7cb5b186 100644
--- a/wiki/concepts/meta-muse-spark.md
+++ b/wiki/concepts/meta-muse-spark.md
@@ -154,7 +154,7 @@ This phenomenon highlights emergent conversational attractor states when models
 - [[concepts/open-model-consortium]] — Contrast with Meta's traditional open-source Llama strategy
 - [[concepts/claude/mythos-preview]] — Concurrent frontier model release (Anthropic, closed)
 - [[entities/alexandr-wang]] — MSL leader, Scale AI founder
-- [[entities/mark-zuckerberg]] — Meta CEO, strategic direction
+- [[concepts/mark-zuckerberg]] — Meta CEO, strategic direction
 
 ## Muse Spark 1.2 & Muse Code (August 5, 2026)
 
diff --git a/wiki/concepts/minimax-sparse-attention.md b/wiki/concepts/minimax-sparse-attention.md
index ea48920c..d4816a5a 100644
--- a/wiki/concepts/minimax-sparse-attention.md
+++ b/wiki/concepts/minimax-sparse-attention.md
@@ -49,7 +49,7 @@ This design solves the precision loss and prefix-caching obstacles identified in
 
 ## Context: M2 Series Foundation
 
-MSA builds on lessons from the M2 series (229.9B total params, 9.8B active per token, 256 fine-grained experts with sigmoid gating). M2 achieved [[concepts/swe-bench-pro|SWE-Bench Pro]] scores of 56-59 and demonstrated self-evolving agent capabilities via the **Forge** RL training system.
+MSA builds on lessons from the M2 series (229.9B total params, 9.8B active per token, 256 fine-grained experts with sigmoid gating). M2 achieved [[concepts/ai-benchmarks/swe-bench-pro|SWE-Bench Pro]] scores of 56-59 and demonstrated self-evolving agent capabilities via the **Forge** RL training system.
 
 ## Related Pages
 
@@ -57,4 +57,4 @@ MSA builds on lessons from the M2 series (229.9B total params, 9.8B active per t
 - [[concepts/deepseek-mla]] — DeepSeek's Multi-head Latent Attention
 - [[concepts/long-context]] — Long context handling in LLMs
 - [[concepts/kv-cache]] — KV cache optimization
-- [[concepts/swe-bench-pro]] — SWE-Bench Pro benchmark
+- [[concepts/ai-benchmarks/swe-bench-pro]] — SWE-Bench Pro benchmark
diff --git a/wiki/concepts/ml-research-practice.md b/wiki/concepts/ml-research-practice.md
index 834d5373..da620b1f 100644
--- a/wiki/concepts/ml-research-practice.md
+++ b/wiki/concepts/ml-research-practice.md
@@ -95,7 +95,7 @@ Although this article was written in 2017, its essence directly applies to AI re
 
 ### 1. Goal-Driven > Idea-Driven (Even More Important in the Agent Era)
 
-In 2026, AI agent development is driven by concrete goals like "make X work." Goal-driven development is mainstream through tools like Cursor, [[concepts/coding-agents/claude-code]], and [[concepts/coding-agents/openai-codex]].
+In 2026, AI agent development is driven by concrete goals like "make X work." Goal-driven development is mainstream through tools like Cursor, [[concepts/coding-agents/claude-code]], and [[entities/openai-codex]].
 
 ### 2. Constraining to General Solutions (Aligns with RLHF's Essence)
 
@@ -111,7 +111,7 @@ Even in the 2026 LLM era, foundational understanding of optimization theory and
 
 ### 5. ε-Greedy Exploration (Agent Design as Multi-Armed Bandit)
 
-In [[concepts/agent-architecture/agent-architecture]] design, balancing the main strategy with exploration is a critical design decision. [[concepts/test-time-scaling/test-time-scaling]] is itself about the explore-exploit tradeoff during inference.
+In [[concepts/agent-architecture/agent-architecture]] design, balancing the main strategy with exploration is a critical design decision. [[concepts/test-time-scaling]] is itself about the explore-exploit tradeoff during inference.
 
 ## Related
 
@@ -120,4 +120,4 @@ In [[concepts/agent-architecture/agent-architecture]] design, balancing the main
 - [[concepts/post-training/reinforcement-learning]] — Schulman's primary technical domain
 - [[concepts/coding-agents/coding-agents]] — The 2026 embodiment of Goal-Driven research
 - [[concepts/agent-memory/context-engineering]] — The agent counterpart of notebook culture
-- [[concepts/test-time-scaling/test-time-scaling]] — The inference-time version of ε-greedy exploration
+- [[concepts/test-time-scaling]] — The inference-time version of ε-greedy exploration
diff --git a/wiki/concepts/mlx-llm.md b/wiki/concepts/mlx-llm.md
index c87f4f6f..8ec33ce8 100644
--- a/wiki/concepts/mlx-llm.md
+++ b/wiki/concepts/mlx-llm.md
@@ -69,7 +69,7 @@ The community has developed custom forks for advanced features:
 
 ## Related Concepts
 
-- [[entities/mac-studio-local-ai]] — Mac Studio hardware setup for local inference
+- [[concepts/mac-studio-local-ai]] — Mac Studio hardware setup for local inference
 - [[concepts/gguf]] — 4-bit and dynamic quantization techniques
 - [[concepts/mixture-of-experts]] — Mixture-of-Experts model design
 - [[concepts/llama-cpp]] — Cross-platform inference engine alternative
diff --git a/wiki/concepts/mlx.md b/wiki/concepts/mlx.md
index 6acb1d21..ed2d716c 100644
--- a/wiki/concepts/mlx.md
+++ b/wiki/concepts/mlx.md
@@ -49,7 +49,7 @@ MLX (pronounced "mɛlɪks") is an open-source array processing framework for mac
 - [[inference/llama-cpp]]
 - [[concepts/local-llm/_index]]
 - [[concepts/fine-tuning]]
-- [[entities/mac-studio-local-ai]]
+- [[concepts/mac-studio-local-ai]]
 - [[concepts/inference]]
 
 ## Sources
diff --git a/wiki/concepts/modal-vm-sandboxes.md b/wiki/concepts/modal-vm-sandboxes.md
index b5bec00f..8b34aea3 100644
--- a/wiki/concepts/modal-vm-sandboxes.md
+++ b/wiki/concepts/modal-vm-sandboxes.md
@@ -56,5 +56,5 @@ These updates position Modal as a **production-ready infrastructure platform** f
 ## Related Concepts
 
 - [[concepts/agent-safety]] — Agent execution security and sandboxing
-- [[concepts/agent-runtime]] — Infrastructure for running AI agents
+- [[concepts/harness-engineering/agent-runtime]] — Infrastructure for running AI agents
 - [[concepts/serverless]] — Serverless computing patterns
diff --git a/wiki/concepts/moe-train-inference-mismatch.md b/wiki/concepts/moe-train-inference-mismatch.md
index b6b401fa..d5b1c410 100644
--- a/wiki/concepts/moe-train-inference-mismatch.md
+++ b/wiki/concepts/moe-train-inference-mismatch.md
@@ -53,7 +53,7 @@ During **training**, MoE uses token-level routing where each token independently
 
 ### Inference-Time Mitigations
 
-- **Expert Parallelism (EP)**: Distributes experts across GPUs so that each GPU handles a manageable subset. [[concepts/elastic-ep]] in [[inference/sglang]] adds fault-tolerant EP for production deployments.
+- **Expert Parallelism (EP)**: Distributes experts across GPUs so that each GPU handles a manageable subset. [[concepts/elastic-ep]] in [[concepts/inference/sglang]] adds fault-tolerant EP for production deployments.
 - **Fine-grained expert parallelism**: [[concepts/deepseek-v4]]'s MegaMoE uses many small experts with fine-grained EP, improving load distribution and reducing per-expert capacity pressure.
 
 ### Combined Approach (DeepSeek)
@@ -81,5 +81,5 @@ The mismatch is fundamentally a **distribution shift** problem: routing decision
 - [[concepts/elastic-ep]]
 - [[concepts/model-quantization]]
 - [[inference/vllm]]
-- [[inference/sglang]]
+- [[concepts/inference/sglang]]
 - [[raw/papers/2024-12-27_2412.19437_deepseek-v3-technical-report]]
diff --git a/wiki/concepts/multi-agents/agent-orchestration.md b/wiki/concepts/multi-agents/agent-orchestration.md
index cbe0dfc5..e6586da4 100644
--- a/wiki/concepts/multi-agents/agent-orchestration.md
+++ b/wiki/concepts/multi-agents/agent-orchestration.md
@@ -63,7 +63,7 @@ Google DeepMind's internal agent architecture reveals practical orchestration pa
 - **Antigravity IDE**: Visual Studio–like environment with built-in agent manager — spawn multiple agents on different projects with individual planning systems
 - **Skills Library**: Shared library with Darwinian selection — only the best skills survive
 - **Quota Management**: Employees have lower quotas than customers; SRE teams enforce limits
-- **Model Mixing**: Orchestration layer routes bulk work to cheap models ([[concepts/gemma-4|Gemma 4]]) and critical work to advanced models
+- **Model Mixing**: Orchestration layer routes bulk work to cheap models ([[entities/gemma-4|Gemma 4]]) and critical work to advanced models
 
 ## Google's Agent Infrastructure Stack (May 2026)
 
diff --git a/wiki/concepts/multipath-reliable-connection.md b/wiki/concepts/multipath-reliable-connection.md
index f6df539c..ef0ba653 100644
--- a/wiki/concepts/multipath-reliable-connection.md
+++ b/wiki/concepts/multipath-reliable-connection.md
@@ -47,5 +47,5 @@ MRC was part of OpenAI's unusually busy May 2026 release week, which also includ
 - [[entities/openai]] — OpenAI's broader infrastructure strategy
 - [[concepts/xai-anthropic-colossus-deal]] — GPU compute as strategic resource
 - [[entities/nvidia]] — Dominant GPU hardware vendor
-- [[concepts/distributed-training]] — Distributed training infrastructure challenges
+- [[concepts/training-infra/distributed-training]] — Distributed training infrastructure challenges
 - [[concepts/mixture-of-experts]] — Related infrastructure scaling
diff --git a/wiki/concepts/okf-open-knowledge-format.md b/wiki/concepts/okf-open-knowledge-format.md
index a1c0d0e1..825b7cc6 100644
--- a/wiki/concepts/okf-open-knowledge-format.md
+++ b/wiki/concepts/okf-open-knowledge-format.md
@@ -83,7 +83,7 @@ Because OKF is an open format, compatible tools can interoperate:
 
 ### OpenWiki 0.2 (July 2026)
 
-[[LangChain|entities/langchain]] adopted OKF as the native format for OpenWiki 0.2. Wikis generated or updated by OpenWiki now include YAML frontmatter with `title`, `description`, `tags`, `categories`, and `resource` URLs. The changelog convention (`logs.md`) is particularly valuable — after each OpenWiki run, agents and developers can check what changed without re-reading the entire wiki.
+[[entities/langchain|entities/langchain]] adopted OKF as the native format for OpenWiki 0.2. Wikis generated or updated by OpenWiki now include YAML frontmatter with `title`, `description`, `tags`, `categories`, and `resource` URLs. The changelog convention (`logs.md`) is particularly valuable — after each OpenWiki run, agents and developers can check what changed without re-reading the entire wiki.
 
 See [[concepts/openwiki]] for full details on the OpenWiki integration.
 
diff --git a/wiki/concepts/one-person-unicorn.md b/wiki/concepts/one-person-unicorn.md
index 0e213761..eb3aac2f 100644
--- a/wiki/concepts/one-person-unicorn.md
+++ b/wiki/concepts/one-person-unicorn.md
@@ -24,7 +24,7 @@ A billion-dollar company founded and operated by a single person, enabled by AI
 2. **[[concepts/context-engineering|Context Engineering]]:** Making AI agents reliable and capable
 3. **[[concepts/nvidia-dynamo]]:** Affordable agentic inference infrastructure
 4. **[[concepts/vibe-ceo]]:** New management paradigm for agent orchestration
-5. **[[entities/reflexive-ai]]:** Cultural normalization of AI-as-baseline
+5. **[[concepts/reflexive-ai]]:** Cultural normalization of AI-as-baseline
 
 ## Related
 
diff --git a/wiki/concepts/open-secure-ai-alliance.md b/wiki/concepts/open-secure-ai-alliance.md
index 3c102689..c779043c 100644
--- a/wiki/concepts/open-secure-ai-alliance.md
+++ b/wiki/concepts/open-secure-ai-alliance.md
@@ -16,7 +16,7 @@ sources:
 related_concepts:
   - "[[concepts/ai-alliance]]"
   - "[[concepts/open-source-ai-must-win]]"
-  - "[[concepts/ai-safety]]"
+  - "[[concepts/security-and-governance/ai-safety]]"
   - "[[entities/nvidia]]"
 ---
 
@@ -62,10 +62,10 @@ This positions NVIDIA (historically an infrastructure provider, not a model publ
 
 - [[concepts/ai-alliance]] — The broader IBM/Meta-led AI Alliance (different initiative)
 - [[concepts/open-source-ai-must-win]] — Ongoing debate about open vs closed AI models
-- [[concepts/ai-safety]] — The broader safety ecosystem this alliance operates within
+- [[concepts/security-and-governance/ai-safety]] — The broader safety ecosystem this alliance operates within
 - [[entities/nvidia]] — Parent company and founder
 
 ## See Also
 
 - [[entities/anthropic]]#policy — Anthropic's evolving stance on open weights
-- [[concepts/fable-5]] — US government export control directive context
+- [[concepts/claude/fable-5]] — US government export control directive context
diff --git a/wiki/concepts/open-source-llm-governance-debian-gr.md b/wiki/concepts/open-source-llm-governance-debian-gr.md
index 354c35b0..49e5c8ba 100644
--- a/wiki/concepts/open-source-llm-governance-debian-gr.md
+++ b/wiki/concepts/open-source-llm-governance-debian-gr.md
@@ -61,7 +61,7 @@ Debian's GR is part of a wider trend of open-source communities grappling with A
 
 ## Related Concepts
 
-- [[concepts/ai-safety]] — the safety implications of LLM-generated code in critical infrastructure
+- [[concepts/security-and-governance/ai-safety]] — the safety implications of LLM-generated code in critical infrastructure
 - [[concepts/open-source-licensing]] — the unsettled legal status of AI-generated code copyright
 - [[concepts/ai-assisted-development]] — the practical reality of developers already using LLMs daily
 - [[concepts/ai-governance]] — broader governance frameworks for AI in organizations
diff --git a/wiki/concepts/openai/frontier-governance-framework.md b/wiki/concepts/openai/frontier-governance-framework.md
index f0b7ecf5..4b2577d6 100644
--- a/wiki/concepts/openai/frontier-governance-framework.md
+++ b/wiki/concepts/openai/frontier-governance-framework.md
@@ -51,6 +51,6 @@ OpenAI expects the framework to continue evolving as:
 ## Related Pages
 - [[concepts/security-and-governance/ai-safety]] — Broader AI safety landscape
 - [[ai-governance]] — AI governance frameworks and regulation
-- [[OpenAI]] — Company behind the framework
-- [[Anthropic]] — Competitor with comparable safety frameworks
-- [[EU-AI-Act]] — Key regulatory driver
+- [[entities/openai|OpenAI]] — Company behind the framework
+- [[entities/anthropic|Anthropic]] — Competitor with comparable safety frameworks
+- [[concepts/eu-ai-act|EU-AI-Act]] — Key regulatory driver
diff --git a/wiki/concepts/openclaw/philosophy.md b/wiki/concepts/openclaw/philosophy.md
index bdf63554..23fe5e1b 100644
--- a/wiki/concepts/openclaw/philosophy.md
+++ b/wiki/concepts/openclaw/philosophy.md
@@ -118,9 +118,9 @@ OpenClaw's philosophy is deeply connected to the [[concepts/local-first-software
 ## The Four "Riffs" on Decomposition
 | Framework | What it Decomposes | Monolith it Replaces | Longevity |
 |-----------|-------------------|---------------------|-----------|
-| **Late Interaction ([[entities/omar-khattab/colbert|ColBERT]])** | Document representations → sets of objects; similarity → compositional operations | Single-vector dense embeddings | 6.5+ years (2020–present) |
-| **[[entities/omar-khattab/dspy|DSPy]]** | Specification vs optimization; AI programs → symbolic modules with NL specs | Monolithic prompt debt | 3.5+ years (2023–present) |
-| **[[entities/omar-khattab/gepa|GEPA]]** | Learning signals → actual tokens + feedback (not scalar rewards) | Policy gradient RL rewards | Emerging (2025) |
+| **Late Interaction ([[concepts/colbert|ColBERT]])** | Document representations → sets of objects; similarity → compositional operations | Single-vector dense embeddings | 6.5+ years (2020–present) |
+| **[[concepts/dspy|DSPy]]** | Specification vs optimization; AI programs → symbolic modules with NL specs | Monolithic prompt debt | 3.5+ years (2023–present) |
+| **[[concepts/gepa|GEPA]]** | Learning signals → actual tokens + feedback (not scalar rewards) | Policy gradient RL rewards | Emerging (2025) |
 | **[[entities/omar-khattab/rlm|RLMs]]** | Hard problems → symbolic programs that invoke models; context → recursive access | Monolithic attention over massive contexts | Emerging (2025) |
 
 
diff --git a/wiki/concepts/outcome-based-pricing.md b/wiki/concepts/outcome-based-pricing.md
index e4909d8c..6b2d8224 100644
--- a/wiki/concepts/outcome-based-pricing.md
+++ b/wiki/concepts/outcome-based-pricing.md
@@ -38,7 +38,7 @@ Outcome-Based Pricing is a pricing model that charges based on **actual results
 
 ## Industry Examples
 
-- **[[Sierra]]**: Developed the **Agency × Attribution 2×2 matrix** for outcome-based pricing viability. The framework maps two axes — software's agency (autonomy) and outcome attribution clarity — yielding four quadrants:
+- **[[entities/sierra|Sierra]]**: Developed the **Agency × Attribution 2×2 matrix** for outcome-based pricing viability. The framework maps two axes — software's agency (autonomy) and outcome attribution clarity — yielding four quadrants:
   - **Bottom-Left (Low Agency, Low Attribution)**: Classic seat-based SaaS (e.g., Salesforce, Office 365). Users log in, software assists, attribution is fuzzy.
   - **Top-Left (High Agency, Low Attribution)**: API/infrastructure pricing (e.g., OpenAI, AWS). Software does autonomous work but outcomes can't be cleanly attributed to specific API calls.
   - **Bottom-Right (Low Agency, High Attribution)**: Seats-with-metered-consumption hybrids (e.g., Cursor). Human-managed products where AI consumption informs pricing.
diff --git a/wiki/concepts/post-training/grpo-memory-modeling.md b/wiki/concepts/post-training/grpo-memory-modeling.md
index 95025522..459143b4 100644
--- a/wiki/concepts/post-training/grpo-memory-modeling.md
+++ b/wiki/concepts/post-training/grpo-memory-modeling.md
@@ -54,7 +54,7 @@ PPO requires **at minimum 4 model copies**: Actor + Critic + Reference + Reward.
 
 ### With LoRA (rank 16) on Actor
 
-Only the adapter parameters (~0.4 GB optimizer states for r=16) need full-precision copies. See [[post-training/peft-lora-qlora]].
+Only the adapter parameters (~0.4 GB optimizer states for r=16) need full-precision copies. See [[concepts/post-training/peft-lora-qlora]].
 
 - **Actor**: 14 + 0.4 + 0.4 ≈ **28 GB** (frozen base + trainable adapters)
 - **Reference**: **14 GB**
diff --git a/wiki/concepts/post-training/llm-as-policy.md b/wiki/concepts/post-training/llm-as-policy.md
index 1df3c4ba..f33e1ee6 100644
--- a/wiki/concepts/post-training/llm-as-policy.md
+++ b/wiki/concepts/post-training/llm-as-policy.md
@@ -163,7 +163,7 @@ This means:
 
 When DPO eliminates the reward model by expressing $r(x,y) = \beta \log \frac{\pi_\theta(y|x)}{\pi_{\text{ref}}(y|x)}$, it exploits the fact that the policy's log-likelihood ratios already encode preference structure learned during pre-training. When GRPO replaces the critic with group statistics, it exploits the fact that sibling samples from the same policy share enough structural similarity to serve as their own baseline.
 
-> **Information-theoretic framing** (from [[concepts/post-training/on-policy-vs-off-policy-rl|On-Policy vs Off-Policy]] and [[concepts/post-training/post-training-distributional-view|Distributional View]]): SFT provides O(n) bits of dense, off-policy information per episode (the entire demonstration trajectory). RL (GRPO) provides O(1) bits of sparse, on-policy information (just the reward signal). Yet RL produces qualitatively superior policies because those O(1) bits are **unbiased and on-policy** — they tell the policy exactly how its own behavior performs, whereas SFT's O(n) bits are biased toward the teacher's distribution and never expose the policy to its own failure modes. The auxiliary model elimination trend is thus a movement toward **maximizing information efficiency** — extracting the most policy-improvement signal from the fewest external components.
+> **Information-theoretic framing** (from [[concepts/post-training/on-policy-vs-off-policy-rl|On-Policy vs Off-Policy]] and [[concepts/post-training-distributional-view|Distributional View]]): SFT provides O(n) bits of dense, off-policy information per episode (the entire demonstration trajectory). RL (GRPO) provides O(1) bits of sparse, on-policy information (just the reward signal). Yet RL produces qualitatively superior policies because those O(1) bits are **unbiased and on-policy** — they tell the policy exactly how its own behavior performs, whereas SFT's O(n) bits are biased toward the teacher's distribution and never expose the policy to its own failure modes. The auxiliary model elimination trend is thus a movement toward **maximizing information efficiency** — extracting the most policy-improvement signal from the fewest external components.
 
 ## RLHF Book Perspective (Lambert, 2026)
 
diff --git a/wiki/concepts/post-training/miles-rl.md b/wiki/concepts/post-training/miles-rl.md
index b7785454..53d18101 100644
--- a/wiki/concepts/post-training/miles-rl.md
+++ b/wiki/concepts/post-training/miles-rl.md
@@ -18,13 +18,13 @@ updated: 2026-04-27
 |-------|-------|
 | **Type** | RL Post-Training Framework |
 | **Organization** | [[entities/lmsys-org]] |
-| **Related To** | [[entities/sglang]], Slime |
+| **Related To** | [[concepts/inference/sglang]], Slime |
 | **Introduced** | November 2025 |
 | **Cross-Platform** | NVIDIA CUDA, AMD ROCm |
 
 ## Overview
 
-**Miles** is an open-source reinforcement learning post-training framework developed by [[entities/lmsys-org]], built on the [[entities/sglang]] and Slime ecosystems. It is designed for production-grade RL pipelines for large language and multimodal models.
+**Miles** is an open-source reinforcement learning post-training framework developed by [[entities/lmsys-org]], built on the [[concepts/inference/sglang]] and Slime ecosystems. It is designed for production-grade RL pipelines for large language and multimodal models.
 
 ## Core Capabilities
 - **Distributed Rollout Generation**: Powered by SGLang for inference
diff --git a/wiki/concepts/post-training/multi-turn-tool-use-rl.md b/wiki/concepts/post-training/multi-turn-tool-use-rl.md
index c9e84e43..7dd10d1e 100644
--- a/wiki/concepts/post-training/multi-turn-tool-use-rl.md
+++ b/wiki/concepts/post-training/multi-turn-tool-use-rl.md
@@ -22,7 +22,7 @@ related:
 
 # Multi-Turn Tool Use with Reinforcement Learning
 
-A training methodology where reinforcement learning (RL) — specifically [[GRPO]] (Group Relative Policy Optimization) — is used to teach language model agents how to **orchestrate multiple tools** across multiple interaction turns, without relying on human demonstrations or teacher model outputs.
+A training methodology where reinforcement learning (RL) — specifically [[concepts/post-training/grpo|GRPO]] (Group Relative Policy Optimization) — is used to teach language model agents how to **orchestrate multiple tools** across multiple interaction turns, without relying on human demonstrations or teacher model outputs.
 
 ## Core Idea
 
@@ -46,7 +46,7 @@ The agent learned to:
 ## Training Recipe (Bespoke Labs)
 
 ### Algorithm
-- **GRPO** (Group Relative Policy Optimization) — same core algorithm behind [[DeepSeek-R1]]
+- **GRPO** (Group Relative Policy Optimization) — same core algorithm behind [[concepts/deepseek-r1|DeepSeek-R1]]
 - 1600 steps (100 epochs)
 - μ=2 (one on-policy step + one off-policy step per batch)
 
@@ -100,7 +100,7 @@ Updating the reference model every 100 steps (rather than keeping it fixed at th
 
 ## Relationship to DeepSeek-R1
 
-Uses the same GRPO algorithm that powers [[DeepSeek-R1]]'s reasoning capabilities, but applies it to a different domain: **tool orchestration** rather than mathematical reasoning. The overlong filtering technique from DAPO and KL penalty tuning are shared concerns.
+Uses the same GRPO algorithm that powers [[concepts/deepseek-r1|DeepSeek-R1]]'s reasoning capabilities, but applies it to a different domain: **tool orchestration** rather than mathematical reasoning. The overlong filtering technique from DAPO and KL penalty tuning are shared concerns.
 
 ## Open Questions
 
@@ -112,7 +112,7 @@ Uses the same GRPO algorithm that powers [[DeepSeek-R1]]'s reasoning capabilitie
 ## See Also
 
 - [[concepts/post-training/grpo]] — Group Relative Policy Optimization algorithm
-- [[concepts/bfcl-v3]] — Berkeley Function Calling Leaderboard (BFCL) benchmark
+- [[concepts/ai-benchmarks/bfcl-v3]] — Berkeley Function Calling Leaderboard (BFCL) benchmark
 - [[concepts/deepseek-r1]] — DeepSeek-R1 reasoning model (uses GRPO for reasoning)
 - [[entities/bespoke-labs]] — Bespoke Labs, the research lab behind this work
 - [[concepts/agent-evaluation]] — Agent evaluation methodologies
diff --git a/wiki/concepts/post-training/on-policy-distillation.md b/wiki/concepts/post-training/on-policy-distillation.md
index e29a1df5..31320f37 100644
--- a/wiki/concepts/post-training/on-policy-distillation.md
+++ b/wiki/concepts/post-training/on-policy-distillation.md
@@ -273,7 +273,7 @@ This traces a **Pareto curve** as β varies. Different methods are different poi
 - [[concepts/post-training/on-policy-self-distillation]] — OPSD: same-model self-distillation for reasoning (Zhao et al., 2026)
 - [[concepts/post-training/sdar-self-distilled-agentic-rl]] — SDAR: gated OPSD + GRPO for multi-turn agent training (2026)
 - [[concepts/model-distillation]] — Broader category of distillation techniques
-- [[concepts/post-training/post-training-distributional-view]] — SFT vs RL vs OPD through a distributional lens
+- [[concepts/post-training-distributional-view]] — SFT vs RL vs OPD through a distributional lens
 - [[concepts/post-training/grpo-rl-training]] — The RL framework OPD was implemented on top of
 - [[entities/thinking-machines-lab]] — Research lab that authored the foundational OPD paper
 - [[entities/will-brown]] — Author of gradient-geometric analysis of OPD vs SFT vs RL
diff --git a/wiki/concepts/post-training/on-policy-vs-off-policy-rl.md b/wiki/concepts/post-training/on-policy-vs-off-policy-rl.md
index a10ac8a4..ba6b11a9 100644
--- a/wiki/concepts/post-training/on-policy-vs-off-policy-rl.md
+++ b/wiki/concepts/post-training/on-policy-vs-off-policy-rl.md
@@ -62,7 +62,7 @@ Inference: "Model's own (flawed) prefix" → predict next token
            ↑ distribution shift — model has never seen its own errors during training
 ```
 
-[[concepts/post-training/post-training-distributional-view|The distributional view]] frames this precisely: SFT does **forward KL** (mode-seeking) toward the teacher's distribution, while RL and OPD do **reverse KL** on the student's own rollouts.
+[[concepts/post-training-distributional-view|The distributional view]] frames this precisely: SFT does **forward KL** (mode-seeking) toward the teacher's distribution, while RL and OPD do **reverse KL** on the student's own rollouts.
 
 ### The Hallucination Problem (Goldberg, 2023)
 
@@ -163,7 +163,7 @@ Goldberg's 2023 framing was "SFT vs RL" as a dichotomy. By 2026, the field has e
 
 ## Information-Theoretic Perspective
 
-[[concepts/post-training/post-training-distributional-view|The distributional view]] (@nrehiew) quantifies the information density difference:
+[[concepts/post-training-distributional-view|The distributional view]] (@nrehiew) quantifies the information density difference:
 
 | Method | Information per episode | Sampling |
 |--------|------------------------|----------|
@@ -185,7 +185,7 @@ RL provides only 1 bit of information per episode (the reward signal), but that
 
 ## Related Pages
 
-- [[concepts/post-training/post-training-distributional-view]] — Distributional lens: SFT vs RL vs OPD
+- [[concepts/post-training-distributional-view]] — Distributional lens: SFT vs RL vs OPD
 - [[concepts/post-training/on-policy-distillation]] — On-policy distillation mechanism and variants
 - [[concepts/post-training/grpo-rl-training]] — The dominant on-policy RL algorithm (2025-2026)
 - [[concepts/post-training/asynchronous-rl]] — Async RL and the policy-lag / off-policy tradeoff
diff --git a/wiki/concepts/post-training/rl-scaling-boundaries.md b/wiki/concepts/post-training/rl-scaling-boundaries.md
index 6281c8a6..8a8eec10 100644
--- a/wiki/concepts/post-training/rl-scaling-boundaries.md
+++ b/wiki/concepts/post-training/rl-scaling-boundaries.md
@@ -47,7 +47,7 @@ ProRL (from Polar) argues that **RL training compute should scale alongside pret
 
 ### Reward Hacking
 
-As RL scales, models increasingly exploit reward function shortcuts rather than learning the underlying capability. See [[evaluation/reward-hacking]]. This creates an illusion of capability expansion that collapses under distribution shift.
+As RL scales, models increasingly exploit reward function shortcuts rather than learning the underlying capability. See [[concepts/evaluation/reward-hacking]]. This creates an illusion of capability expansion that collapses under distribution shift.
 
 ### Distribution Collapse
 
@@ -79,6 +79,6 @@ RL can expand LLM capability frontiers, but its scaling is bounded by reward qua
 - [[rlvr]] — RL with Verifiable Rewards
 - [[grpo-rl-training]] — Group Relative Policy Optimization
 - [[concepts/deepseek-r1]] — reasoning emergence via RL
-- [[evaluation/reward-hacking]] — failure modes at scale
+- [[concepts/evaluation/reward-hacking]] — failure modes at scale
 - [[training-free-rl]] — alternatives to RL-based test-time scaling
 - [[rl-interview-questions-2026]] — full interview question set
diff --git a/wiki/concepts/pretraining-parallelisms.md b/wiki/concepts/pretraining-parallelisms.md
index 87541fb7..1251c65e 100644
--- a/wiki/concepts/pretraining-parallelisms.md
+++ b/wiki/concepts/pretraining-parallelisms.md
@@ -85,4 +85,4 @@ Some claim RL generation inference and end-user generation inference are equival
 - [[Distributed Training]] — Multi-GPU/multi-node training strategies
 - [[GPU Infrastructure]] — Hardware considerations for training
 - [[Numerical Precision in ML]] — FP16, BF16, FP8 and their implications
-- [[RLVR]] — Reinforcement learning with verifiable rewards
+- [[concepts/post-training/rlvr|RLVR]] — Reinforcement learning with verifiable rewards
diff --git a/wiki/concepts/production-ai-agents.md b/wiki/concepts/production-ai-agents.md
index 16ace648..222f76b3 100644
--- a/wiki/concepts/production-ai-agents.md
+++ b/wiki/concepts/production-ai-agents.md
@@ -114,4 +114,4 @@ Self-hosting is not automatically cheaper. The always-on infrastructure cost and
 - **[[concepts/harness-engineering]]** — The evaluation harness as the operating system for AI development
 - **[[entities/hugo-bowne-anderson]]** — Vanishing Gradients host who conducted the Maven Assistant interview
 - **[[concepts/guardrails]]** — Safety mechanisms for production AI agents
-- **[[concepts/ai-evals]]** — Evaluation methodologies for AI systems
+- **[[concepts/evaluation/ai-evals]]** — Evaluation methodologies for AI systems
diff --git a/wiki/concepts/qwen3-6-27b.md b/wiki/concepts/qwen3-6-27b.md
index abf2880d..15a7016b 100644
--- a/wiki/concepts/qwen3-6-27b.md
+++ b/wiki/concepts/qwen3-6-27b.md
@@ -52,7 +52,7 @@ The Qwen3.6-27B release coincides with a broader industry shift where AI agents
 - [[concepts/qwen]] — Qwen/OpenQwen model family
 - [[concepts/open-source-llms]] — Open-weight and open-source model landscape
 - [[concepts/gpt]] — AI coding agent ecosystem- [[concepts/gpt/index]] — Competing GPT model series (GPT-5.5, etc.)
-- [[concepts/anthropic]] — Anthropic's flagship coding model
+- [[entities/anthropic]] — Anthropic's flagship coding model
 ## Sources
 
 -  (GetSuperIntel Newsletter, 2026-04-23)
diff --git a/wiki/concepts/reasoning-aware-retrieval.md b/wiki/concepts/reasoning-aware-retrieval.md
index 09e133d1..034b9d08 100644
--- a/wiki/concepts/reasoning-aware-retrieval.md
+++ b/wiki/concepts/reasoning-aware-retrieval.md
@@ -86,7 +86,7 @@ AgentIR's reasoning traces provide a **grounded alternative**: instead of pure s
 
 ### vs. SID-1 (RL-Trained Retrieval)
 
-**[[SID-1]]** (SID AI, 2025) uses reinforcement learning to train agentic retrieval end-to-end. AgentIR is complementary — it improves the retrieval **backbone** that even RL-trained agents depend on. A stronger retriever means fewer search calls and better training signal for RL.
+**[[concepts/sid-1|SID-1]]** (SID AI, 2025) uses reinforcement learning to train agentic retrieval end-to-end. AgentIR is complementary — it improves the retrieval **backbone** that even RL-trained agents depend on. A stronger retriever means fewer search calls and better training signal for RL.
 
 | Approach | Training Signal | Retriever Type | Retriever Size |
 |----------|---------------|----------------|----------------|
diff --git a/wiki/concepts/reflexive-ai.md b/wiki/concepts/reflexive-ai.md
index 9a08de00..436f48be 100644
--- a/wiki/concepts/reflexive-ai.md
+++ b/wiki/concepts/reflexive-ai.md
@@ -51,7 +51,7 @@ Reflexive AI connects to:
 - [[concepts/ai-organization]] — represents a shift from hierarchical to intelligence-driven orgs
 
 ## Related
-- [[entities/reflexive-ai]]
+- [[concepts/reflexive-ai]]
 
 - [[concepts/experience-is-a-tax]]
 - [[entities/solo-founder-stack]]
@@ -102,7 +102,7 @@ Reflexive AI Usage represents a **new paradigm** for AI adoption in large enterp
 - AI literacy as organizational culture
 
 
-## Related Concepts- [[entities/reflexive-ai]]
+## Related Concepts- [[concepts/reflexive-ai]]
 
 - [Company AI Pilled](company-ai-pilled.md) — Organizational AI-driven transformation framework
 - [Solo Founder Stack](solo-founder-stack.md) — Individual vs. organizational AI usage comparison
diff --git a/wiki/concepts/sampling-strategies.md b/wiki/concepts/sampling-strategies.md
index 36843f1a..703ee36a 100644
--- a/wiki/concepts/sampling-strategies.md
+++ b/wiki/concepts/sampling-strategies.md
@@ -35,6 +35,6 @@ This is distinct from training-side batch invariance (covered in [[concepts/batc
 
 **Practical significance**: As coding agents ([[entities/claude-code]], [[entities/openai-codex]]) and agentic workflows become mainstream for business operations, reproducibility across API calls becomes critical. Users expecting identical outputs from identical prompts may encounter unexplained variations, complicating testing and validation.
 
-**Related**: [[concepts/temperature-sampling]] — Temperature sampling parameter, [[concepts/inference/inference]] — LLM inference pipeline
+**Related**: [[concepts/temperature-sampling]] — Temperature sampling parameter, [[concepts/inference]] — LLM inference pipeline
 
 Source: The Signal by Alex Banks, June 21, 2026, citing Horace He and Thinking Machines research.
diff --git a/wiki/concepts/sandbox/infrastructure.md b/wiki/concepts/sandbox/infrastructure.md
index 07ff63a9..6a0351fd 100644
--- a/wiki/concepts/sandbox/infrastructure.md
+++ b/wiki/concepts/sandbox/infrastructure.md
@@ -237,7 +237,7 @@ As Blake Crosley's analysis notes: *"The minimum viable defense is a URL allowli
 
 - [[concepts/anthropic/managed-agents]] — Managed agent services and their sandboxing approaches
 - [[concepts/coding-agents/ai-coding-reliability]] — Ensuring AI-generated code is correct and safe
-- [[concepts/anthropic]] — The practice of directing AI agents in software development- [[concepts/claude/mythos-glasswing]] — Anthropic's internal agent architecture
+- [[entities/anthropic]] — The practice of directing AI agents in software development- [[concepts/claude/mythos-glasswing]] — Anthropic's internal agent architecture
 - [[concepts/ai-agent-traps]] — Common pitfalls in agent deployment
 
 ## Sources
diff --git a/wiki/concepts/security-and-governance/_index.md b/wiki/concepts/security-and-governance/_index.md
index dd8f5e41..771536a2 100644
--- a/wiki/concepts/security-and-governance/_index.md
+++ b/wiki/concepts/security-and-governance/_index.md
@@ -15,7 +15,7 @@ status: active
 # Agent Security and Governance
 
 Sub-index of pages covering AI safety, alignment, security, containment, governance, and identity.
-Part of the broader [[concepts/agent-engineering-guide-2026|Agent Engineering]] landscape.
+Part of the broader [[concepts/harness-engineering/agent-engineering-guide-2026|Agent Engineering]] landscape.
 
 > **Historical shift**: The field evolved from **Safety & Alignment** (2024-25: "will the model do what we intend?") toward **Security & Governance** (2026: "how do we control access and manage risk at scale?"). Both concerns coexist, but the center of gravity moved as frontier models became capable enough that inner alignment faded while outer control became paramount.
 >
diff --git a/wiki/concepts/sglang-pipeline-parallelism.md b/wiki/concepts/sglang-pipeline-parallelism.md
index 77d5e7cf..ef5a3d03 100644
--- a/wiki/concepts/sglang-pipeline-parallelism.md
+++ b/wiki/concepts/sglang-pipeline-parallelism.md
@@ -17,7 +17,7 @@ updated: 2026-04-27
 | Field | Value |
 |-------|-------|
 | **Type** | Inference Parallelism Strategy |
-| **Related To** | [[entities/sglang]], [[entities/lmsys-org]] |
+| **Related To** | [[concepts/inference/sglang]], [[entities/lmsys-org]] |
 | **Introduced** | January 2026 |
 | **Source** | LMSYS Blog "Pipeline Parallelism in SGLang: Scaling to Million-Token Contexts" |
 | **Author** | Shangming Cai |
diff --git a/wiki/concepts/siri-ai.md b/wiki/concepts/siri-ai.md
index 64baf797..1fe91c12 100644
--- a/wiki/concepts/siri-ai.md
+++ b/wiki/concepts/siri-ai.md
@@ -12,7 +12,7 @@ sources:
 
 # Siri AI
 
-Siri AI is Apple's completely reimagined voice assistant, announced June 8, 2026, powered by the next generation of [[entities/apple|Apple Intelligence]]. It represents a ground-up rebuild of Siri with personal context understanding, broad world knowledge, onscreen awareness, and multimodal capabilities — all designed with Apple's privacy-first architecture.
+Siri AI is Apple's completely reimagined voice assistant, announced June 8, 2026, powered by the next generation of [[concepts/apple|Apple Intelligence]]. It represents a ground-up rebuild of Siri with personal context understanding, broad world knowledge, onscreen awareness, and multimodal capabilities — all designed with Apple's privacy-first architecture.
 
 ## Key Features
 
diff --git a/wiki/concepts/snowflake-arctic-rl.md b/wiki/concepts/snowflake-arctic-rl.md
index aefb5d0f..6047fc20 100644
--- a/wiki/concepts/snowflake-arctic-rl.md
+++ b/wiki/concepts/snowflake-arctic-rl.md
@@ -56,8 +56,8 @@ Snowflake Arctic RL represents a notable advance in democratizing RL training:
 
 ## Related Concepts
 
-- [[concepts/reinforcement-learning]] — Reinforcement learning fundamentals for LLM post-training
-- [[concepts/grpo]] — GRPO (Group Relative Policy Optimization), commonly used alongside Arctic RL
+- [[concepts/post-training/reinforcement-learning]] — Reinforcement learning fundamentals for LLM post-training
+- [[concepts/post-training/grpo]] — GRPO (Group Relative Policy Optimization), commonly used alongside Arctic RL
 - [[concepts/post-training/skyrl]] — SkyRL, the UC Berkeley open-source RL framework Arctic RL builds upon
 - [[entities/snowflake]] — Snowflake Inc., the data cloud company behind the Arctic model family
 - [[concepts/training-efficiency]] — Training efficiency and cost optimization techniques for LLMs
diff --git a/wiki/concepts/space-gpus.md b/wiki/concepts/space-gpus.md
index f926fa6b..785b35a4 100644
--- a/wiki/concepts/space-gpus.md
+++ b/wiki/concepts/space-gpus.md
@@ -90,6 +90,15 @@ K2 raised **$450 million at a $3 billion valuation** to prove that orbital compu
 
 Google is pursuing orbital data centers through **Project Suncatcher**, envisioning an **81-satellite cluster** built in partnership with Planet Labs. CEO Sundar Pichai stated we're "a decade away" from orbital data centers. Google believes launch costs must drop to **$200/kg** for economic viability.
 
+**Announcement (blog.google, 2025-11-04).** Project Suncatcher is a Google Research /
+Google DeepMind moonshot to scale ML compute in space: an interconnected network of
+solar-powered satellites carrying Google **TPU** AI chips to harness near-continuous solar
+power. The launch post announced (a) an initial **research preprint** on satellite
+constellation design, control, communication, and radiation testing of Google TPUs, and
+(b) a **learning mission with Planet** to launch **two prototype satellites by early 2027**
+to test the hardware in orbit. Framing: explore orbital data centers as the next frontier
+after terrestrial power/cooling constraints. ^[raw/articles/2026-09-25_google_project-suncatcher-announcement.md]
+
 ### Tesla — AI ASICs for Space
 
 Elon Musk explicitly tied Tesla's AI chip roadmap (**AI5 → AI6 → AI7**) to space-based compute. AI7/Dojo3 is designated as **"space-based AI compute."** Custom AI ASICs matter in orbit because they minimize data movement and waste heat — inefficiency in space is paid for twice: larger solar arrays and larger radiators.
diff --git a/wiki/concepts/speculative-decoding.md b/wiki/concepts/speculative-decoding.md
index 86797c48..39dc92ba 100644
--- a/wiki/concepts/speculative-decoding.md
+++ b/wiki/concepts/speculative-decoding.md
@@ -207,7 +207,7 @@ A key claim in the post is that **open-source engines (SGLang, vLLM) have closed
 
 Modal describes training custom speculators as **"ML on easy mode"**: the data-generating process is itself an ML model (the target LLM), so training data is effectively infinite and free. This eliminates the primary bottleneck of most ML projects (data collection/curation) and makes speculator training highly parallelizable and automatable. Combined with the 2-3× speedups from domain-specific speculators vs. negligible gains from kernel tuning, Modal argues the field is under-investing in speculative decoding.
 
-See also: [[entities/modal-labs]], [[entities/sglang]], [[concepts/vllm]]
+See also: [[entities/modal-labs]], [[concepts/inference/sglang]], [[concepts/vllm]]
 
 ## Sources
 
diff --git a/wiki/concepts/state-sponsored-chatbot-influence.md b/wiki/concepts/state-sponsored-chatbot-influence.md
index 2c84823d..a04f6849 100644
--- a/wiki/concepts/state-sponsored-chatbot-influence.md
+++ b/wiki/concepts/state-sponsored-chatbot-influence.md
@@ -39,7 +39,7 @@ The clearest documented instance to date. Reported by the Quincy Institute's *Re
 ## Relationship to adjacent concepts
 
 - **Generative Engine Optimization (GEO)** — the commercial precursor; "the chatbot version of SEO." See [[concepts/gpt/gpt-5-6]] ("ChatGPT Search `site:` Operator at Scale") for how chatbot search fan-out works.
-- **[[concepts/ai-safety]] / [[concepts/security-and-governance/ai-safety]]** — chatbot influence is an *input-side* attack surface: the model's outputs are only as reliable as the retrieved corpus.
+- **[[concepts/security-and-governance/ai-safety]] / [[concepts/security-and-governance/ai-safety]]** — chatbot influence is an *input-side* attack surface: the model's outputs are only as reliable as the retrieved corpus.
 - **[[concepts/security-and-governance/ai-text-watermarking]]** — the obvious defense (provenance marking) operates on the wrong side of the pipeline for this threat.
 - **Disinformation / foreign influence** — traditional instruments (think tanks, media outlets) are being *repurposed as LLM feedstock*: the artifact is no longer the article itself but its effect on machine-generated answers.
 
diff --git a/wiki/concepts/text-optimization.md b/wiki/concepts/text-optimization.md
index f04b909e..5236e413 100644
--- a/wiki/concepts/text-optimization.md
+++ b/wiki/concepts/text-optimization.md
@@ -26,7 +26,7 @@ related:
   - "[[concepts/harness-engineering]]"
   - "[[concepts/context-engineering|Context Engineering]]"
   - "[[concepts/test-time-scaling]]"
-  - "[[concepts/rlm]]"
+  - "[[entities/omar-khattab/rlm]]"
   - "[[concepts/dspy]]"
   - "[[entities/yoonho-lee]]"
 ---
@@ -184,7 +184,7 @@ Lee identifies five directions for rigorous text optimization research:
 - [[concepts/harness-engineering]] — The discipline of building agent infrastructure
 - [[concepts/context-engineering|Context Engineering]] — Curating optimal context window content
 - [[concepts/test-time-scaling]] — The inference-time axis text optimization mirrors at update time
-- [[concepts/rlm]] — Recursive language models as text-space context management
+- [[entities/omar-khattab/rlm]] — Recursive language models as text-space context management
 - [[concepts/dspy]] — Declarative text-layer programming and optimization
 - [[concepts/gepa]] — Generalized Experience-Prompted Adaptation
 - [[entities/yoonho-lee]] — Primary advocate and Meta-Harness first author
diff --git a/wiki/concepts/thunderagent.md b/wiki/concepts/thunderagent.md
index 1b150aa3..e5d6dd87 100644
--- a/wiki/concepts/thunderagent.md
+++ b/wiki/concepts/thunderagent.md
@@ -68,5 +68,5 @@ ThunderAgent is **open source**.
 - [[entities/together-ai]] — Developer of ThunderAgent
 - [[concepts/kv-cache]] — KV cache management in LLM inference
 - [[concepts/vllm]] — Competing inference engine
-- [[concepts/sglang]] — Competing inference engine
+- [[concepts/inference/sglang]] — Competing inference engine
 - [[concepts/tensorrt-llm]] — NVIDIA's inference optimization engine
diff --git a/wiki/concepts/token-economics.md b/wiki/concepts/token-economics.md
index 4ad44b6b..e84bc3c4 100644
--- a/wiki/concepts/token-economics.md
+++ b/wiki/concepts/token-economics.md
@@ -346,7 +346,7 @@ Author-stated caveats: benchmaxxing, frontier-switching user assumption, and noi
 - [[concepts/context-engineering|Context Engineering]] — Token economics is a prerequisite for understanding context window optimization trade-offs
 - [[entities/epoch-ai]] — Measured the "plunging price of thought" cost-of-performance curves (Sep 2026)
 - [[concepts/prompt-caching]] — Cache busts as the hidden per-session cost multiplier
-- [[concepts/model-routing]] — Cheap-model cascades as the primary micro cost lever
+- [[concepts/coding-agents/model-routing]] — Cheap-model cascades as the primary micro cost lever
 - [[events/claude-opus-5-5-gpt-6-release-sep-2026]] — The Sep 2026 frontier price war the curve precipitated
 - [[concepts/local-llm/_index]] — Self-hosting economics and optimization techniques
 - [[concepts/local-llm/model-quantization]] — Quantization methods (GPTQ, AWQ, EXL2, FP8)
diff --git a/wiki/concepts/vibe-ceo.md b/wiki/concepts/vibe-ceo.md
index 8a958b3d..a3e9cc94 100644
--- a/wiki/concepts/vibe-ceo.md
+++ b/wiki/concepts/vibe-ceo.md
@@ -25,7 +25,7 @@ The Vibe CEO model emerges from:
 - [[entities/solo-founder-stack]] — the enabling infrastructure
 - [[entities/levelsio]] — archetypal practitioner: solo founder running a portfolio of products on a single VPS with AI APIs (July 2026: "I cancelled all my SaaS subscriptions and vibecoded 100% of them myself")
 - [[concepts/context-engineering|Context Engineering]] — the core skill for directing agents effectively
-- [[entities/reflexive-ai]] — the organizational culture of AI-as-baseline
+- [[concepts/reflexive-ai]] — the organizational culture of AI-as-baseline
 - [[concepts/managed-agents]] — the tooling that makes it accessible
 
 ## Related
diff --git a/wiki/concepts/vibethinker.md b/wiki/concepts/vibethinker.md
index f5258e42..4d0d1d4e 100644
--- a/wiki/concepts/vibethinker.md
+++ b/wiki/concepts/vibethinker.md
@@ -31,7 +31,7 @@ VibeThinker-3B is built on the **Spectrum-to-Signal** post-training paradigm, re
 Structured SFT with progressively increasing difficulty across reasoning tasks. Rather than uniform fine-tuning on a flat dataset, the curriculum introduces harder problems as the model demonstrates competence, preventing catastrophic forgetting while building reasoning capability incrementally.
 
 ### 2. Multi-Domain Reinforcement Learning (GRPO)
-Group Relative Policy Optimization ([[concepts/grpo|GRPO]]) is applied across math, coding, and other verifiable domains. Unlike PPO, GRPO uses group-relative rewards — comparing outputs within a batch rather than requiring a separate value model — making it more sample-efficient and stable for small-model RL training. This stage is where the bulk of reasoning gains occur.
+Group Relative Policy Optimization ([[concepts/post-training/grpo|GRPO]]) is applied across math, coding, and other verifiable domains. Unlike PPO, GRPO uses group-relative rewards — comparing outputs within a batch rather than requiring a separate value model — making it more sample-efficient and stable for small-model RL training. This stage is where the bulk of reasoning gains occur.
 
 ### 3. Offline Self-Distillation
 The model's own high-quality outputs from the RL stage are used as training targets for a final distillation pass. This [[concepts/model-distillation|self-distillation]] loop reinforces successful reasoning patterns and smooths out inconsistencies, further improving performance without requiring additional external data or larger teacher models.
@@ -79,7 +79,7 @@ VibeThinker-3B joins a growing class of small-but-capable reasoning models:
 | Model | Parameters | Approach | Key Result |
 |-------|-----------|----------|------------|
 | VibeThinker-3B | 3B dense | Curriculum SFT + GRPO + self-distill | AIME26 94.3/97.1 |
-| [[concepts/mai-thinking-1|MAI-Thinking-1]] | 35B active / 1T total (MoE) | RL hill-climbing from scratch | AIME 2025, SWE-Bench Pro |
+| [[entities/mai-thinking-1|MAI-Thinking-1]] | 35B active / 1T total (MoE) | RL hill-climbing from scratch | AIME 2025, SWE-Bench Pro |
 
 While MAI-Thinking-1 uses a much larger MoE architecture and enterprise-grade data, VibeThinker-3B demonstrates that a purely dense, 3B-parameter architecture — trained with the right pipeline — can reach comparable reasoning quality on key metrics.
 
diff --git a/wiki/concepts/vq-bench.md b/wiki/concepts/vq-bench.md
index 5bc4d783..ccf38b89 100644
--- a/wiki/concepts/vq-bench.md
+++ b/wiki/concepts/vq-bench.md
@@ -27,7 +27,7 @@ A **pipeline** composes primitives in a chain: compressing walks a vector forwar
 
 ## Why it matters for the LLM stack
 
-- **Vector DB economics**: recall/latency/memory trade-offs at billion-vector scale are decided by quantizer choice, not index topology alone — see [[entities/vector-databases]].
+- **Vector DB economics**: recall/latency/memory trade-offs at billion-vector scale are decided by quantizer choice, not index topology alone — see [[concepts/vector-databases]].
 - **LLM inference crossover**: the same residual-quantization primitives underpin KV-cache and weight quantization, so quantizer results migrate directly between retrieval and serving stacks (cf. [[concepts/inference-optimization]]-adjacent topics like llama.cpp GGUF quant ladders).
 - **Standardization precedent**: VQ-bench follows the pattern of unifying evaluation when a literature fragments (FAISS's TREC tests for ANN, lm-eval-harness for models). Expect its pipeline grammar to become the default vocabulary.
 
diff --git a/wiki/concepts/wheelhouse.md b/wiki/concepts/wheelhouse.md
index 0179e30d..229b6f13 100644
--- a/wiki/concepts/wheelhouse.md
+++ b/wiki/concepts/wheelhouse.md
@@ -96,7 +96,7 @@ Every implementation bead follows: **Fable design → Opus implementation → Fa
 - [[concepts/land-rush-cicd]] — CI/CD pattern used in Wheelhouse
 - [[concepts/wish-factory]] — End-user feature request pattern
 - [[concepts/agentic-engineering]] — Broader engineering category
-- [[concepts/agent-orchestration]] — Orchestration patterns
+- [[concepts/multi-agents/agent-orchestration]] — Orchestration patterns
 - [[concepts/model-welfare]] — Agent well-being considerations
 
 ## Sources
diff --git a/wiki/concepts/wish-factory.md b/wiki/concepts/wish-factory.md
index dd3636ca..7ef7ab11 100644
--- a/wiki/concepts/wish-factory.md
+++ b/wiki/concepts/wish-factory.md
@@ -65,7 +65,7 @@ The Wish Factory represents a shift from **software factory** (developer-centric
 - [[entities/beads]] — The issue tracker where wishes become implementation tasks
 - [[concepts/land-rush-cicd]] — CI/CD pattern needed to ship at wish-factory speeds
 - [[concepts/agentic-engineering]] — Broader engineering discipline
-- [[concepts/agent-orchestration]] — Orchestration patterns underlying Wish Factory
+- [[concepts/multi-agents/agent-orchestration]] — Orchestration patterns underlying Wish Factory
 
 ## Sources
 
diff --git a/wiki/entities/agno.md b/wiki/entities/agno.md
index a9a129ac..7564828a 100644
--- a/wiki/entities/agno.md
+++ b/wiki/entities/agno.md
@@ -58,8 +58,8 @@ A unified **control plane** provides full visibility and management. Everything
 ## Related
 - [[concepts/agent-platform]] — AI agent platforms
 - [[concepts/agent-framework]] — Agent development frameworks
-- [[concepts/agent-runtime]] — Agent runtime environments
-- [[concepts/agent-observability]] — Agent monitoring and tracing
+- [[concepts/harness-engineering/agent-runtime]] — Agent runtime environments
+- [[concepts/evaluation/agent-observability]] — Agent monitoring and tracing
 
 ## Related Pages
 - [[entities/_index]]
diff --git a/wiki/entities/alex-banks.md b/wiki/entities/alex-banks.md
index 0c61353b..e4b6da10 100644
--- a/wiki/entities/alex-banks.md
+++ b/wiki/entities/alex-banks.md
@@ -137,7 +137,7 @@ Despite working in AI, Banks consistently returns to the human element:
 ## Related
 
 - [[concepts/prompt-engineering]] — Alex Banks's weekly AI newsletter-  — Platform where Banks teaches prompt engineering
-- [[concepts/anthropic]] — AI analytics startup founded by Banks- [[entities/anthropic]] — Frequent coverage subject; Banks is an early adopter of Claude Skills, Claude Cowork, and Claude Dispatch
+- [[entities/anthropic]] — AI analytics startup founded by Banks- [[entities/anthropic]] — Frequent coverage subject; Banks is an early adopter of Claude Skills, Claude Cowork, and Claude Dispatch
 - [[concepts/agentic-engineering]] — Banks's Claude Cowork/Dispatch workflow series exemplifies agentic engineering patterns (async orchestration, phone-to-desktop pairing, walkie-talkie model)
 - [[concepts/resilient-prompt-engineering]] — Banks's core expertise area
 
diff --git a/wiki/entities/alex-chernysh.md b/wiki/entities/alex-chernysh.md
index cdc181ad..c352d0ae 100644
--- a/wiki/entities/alex-chernysh.md
+++ b/wiki/entities/alex-chernysh.md
@@ -20,7 +20,7 @@ sources:
   - https://x.com/alex_chernysh
 related:
   - "[[entities/bernstein]]"
-  - "[[concepts/coding-agents/bernstein]]"
+  - "[[entities/bernstein]]"
   - "[[concepts/multi-agents/multi-agent-orchestration]]"
 ---
 
diff --git a/wiki/entities/alex-ellis.md b/wiki/entities/alex-ellis.md
index 48c51c17..1744e9da 100644
--- a/wiki/entities/alex-ellis.md
+++ b/wiki/entities/alex-ellis.md
@@ -70,7 +70,7 @@ Ellis writes long-form, first-person, receipt-based analysis ("I have skin in th
 - [[entities/claude-code]] — Cloud coding agents he uses for the majority of his coding
 - [[concepts/inference/llama-cpp]] — His local serving engine of choice
 - [[concepts/inference/vllm]] — Rejected for prosumer use (3 tok/s slower for single-user generation)
-- [[concepts/opencode]] — Open-source coding agent harness he built Toilgate for
+- [[entities/opencode]] — Open-source coding agent harness he built Toilgate for
 
 ## Sources
 
diff --git a/wiki/entities/alex-finn.md b/wiki/entities/alex-finn.md
index 40ba27fe..d10f31a5 100644
--- a/wiki/entities/alex-finn.md
+++ b/wiki/entities/alex-finn.md
@@ -47,4 +47,4 @@ Combines local models for rapid iterative tasks with Claude Code for daily syste
 
 - [[concepts/local-llm/local-ai]] — Local AI and home lab infrastructure
 - [[entities/claude-code]] — Claude Code coding agent
-- [[concepts/agent-team-swarm]] — Multi-agent orchestration
+- [[concepts/multi-agents/agent-team-swarm]] — Multi-agent orchestration
diff --git a/wiki/entities/anthropic.md b/wiki/entities/anthropic.md
index 42bc8a89..4982c666 100644
--- a/wiki/entities/anthropic.md
+++ b/wiki/entities/anthropic.md
@@ -822,7 +822,7 @@ Anthropic's **Valve "Peaks" case study** (published Sep 22, via Simon Willison)
 - [[Claude models]] — Model family details
 - [[concepts/ai-economics]] — Tokenmaxxing, AI ROI debate
 - [[Gary Marcus]] — AI industry skepticism
-- [[OpenAI]] — Primary competitor
+- [[entities/openai|OpenAI]] — Primary competitor
 - [[Ed Zitron]] — Revenue skepticism
 ## Related
 - [[entities/anthropic]] — The model family
diff --git a/wiki/entities/bernstein.md b/wiki/entities/bernstein.md
index 675cd538..3c54351b 100644
--- a/wiki/entities/bernstein.md
+++ b/wiki/entities/bernstein.md
@@ -21,7 +21,7 @@ sources:
   - https://pypi.org/project/bernstein/
   - https://alexchernysh.com/
 related:
-  - "[[concepts/coding-agents/bernstein]]"
+  - "[[entities/bernstein]]"
   - "[[concepts/multi-agents/multi-agent-orchestration]]"
   - "[[concepts/harness-engineering/agent-harness]]"
 ---
diff --git a/wiki/entities/bespoke-labs.md b/wiki/entities/bespoke-labs.md
index f6827d27..1a45f507 100644
--- a/wiki/entities/bespoke-labs.md
+++ b/wiki/entities/bespoke-labs.md
@@ -78,7 +78,7 @@ Improved Qwen2.5-7B-Instruct by **+23%** (55% → 78%) on BFCL multi-turn tool u
 - Overlong filtering + small KL weight (0.001) prevents completion length blowup
 - Reference model update every 100 steps boosts performance
 
-→ See [[concepts/multi-turn-tool-use-rl]]
+→ See [[concepts/post-training/multi-turn-tool-use-rl]]
 
 ## Partners & Supporters
 
diff --git a/wiki/entities/blotato.md b/wiki/entities/blotato.md
index 27fb6f81..16bba3e7 100644
--- a/wiki/entities/blotato.md
+++ b/wiki/entities/blotato.md
@@ -9,14 +9,14 @@ sources:
   - https://www.blotato.com/
   - raw/articles/2026-04-10-build-content-engine-full-course.md
 related:
-  - "[[concepts/content-engine]]"
+  - "[[entities/content-engine]]"
   - "[[entities/content-engine]]"
   - "[[entities/solo-founder-stack]]"
 ---
 
 # Blotato
 
-**Blotato** (blotato.com) is a unified social-media API + MCP server that lets AI agents and automation stacks publish, schedule, reply to comments, manage DMs, and pull analytics across 9+ platforms (X, LinkedIn, Facebook, Instagram, TikTok, YouTube, Threads, Bluesky, Pinterest) from a single `create_post`-style call. It is the canonical commercial implementation of the [[concepts/content-engine]] pattern: the "AI writer + distribution automation" pipeline packaged as a flat-priced SaaS.
+**Blotato** (blotato.com) is a unified social-media API + MCP server that lets AI agents and automation stacks publish, schedule, reply to comments, manage DMs, and pull analytics across 9+ platforms (X, LinkedIn, Facebook, Instagram, TikTok, YouTube, Threads, Bluesky, Pinterest) from a single `create_post`-style call. It is the canonical commercial implementation of the [[entities/content-engine]] pattern: the "AI writer + distribution automation" pipeline packaged as a flat-priced SaaS.
 
 The product positions itself as "the #1 social media API for AI agents" — explicitly marketing to agents, not just humans. It works inside Claude, ChatGPT, Cursor, Codex, and any MCP-capable agent, plus no-code stacks (n8n, Make, webhooks) and a REST API/SDK.
 
@@ -49,7 +49,7 @@ Blotato's FAQ explicitly states who it is **not** for: long-form video clipping,
 
 ## Relation to the Content Engine concept
 
-Blotato operationalizes the four stages of the [[concepts/content-engine]] pipeline (research → draft → distribute → analyze) as agent-callable tools. The "How To Build Your Own Content Engine (FULL COURSE)" X article (7,943 bookmarks) that popularized the pattern points at exactly this tool class; Blotato is the commercialized shortcut versus hand-wiring Claude + Buffer + Canva yourself (see [[entities/solo-founder-stack]]).
+Blotato operationalizes the four stages of the [[entities/content-engine]] pipeline (research → draft → distribute → analyze) as agent-callable tools. The "How To Build Your Own Content Engine (FULL COURSE)" X article (7,943 bookmarks) that popularized the pattern points at exactly this tool class; Blotato is the commercialized shortcut versus hand-wiring Claude + Buffer + Canva yourself (see [[entities/solo-founder-stack]]).
 
 ## Community
 
diff --git a/wiki/entities/cat-wu.md b/wiki/entities/cat-wu.md
index 95476392..fb827a0b 100644
--- a/wiki/entities/cat-wu.md
+++ b/wiki/entities/cat-wu.md
@@ -72,7 +72,7 @@ Cat Wu's appointment as Head of Product signals Anthropic's commitment to:
 
 - [[entities/anthropic]] — Anthropic company
 - [[entities/claude-code]] — Claude Code AI coding agent (entity page)
-- [[concepts/anthropic]] — Claude Opus 4.7 model- [[entities/dario-amodei]] — Dario Amodei (Anthropic CEO)
+- [[entities/anthropic]] — Claude Opus 4.7 model- [[entities/dario-amodei]] — Dario Amodei (Anthropic CEO)
 
 ## Sources
 
diff --git a/wiki/entities/cohere.md b/wiki/entities/cohere.md
index 123ea9ea..7e8e39fa 100644
--- a/wiki/entities/cohere.md
+++ b/wiki/entities/cohere.md
@@ -161,7 +161,7 @@ Three use cases showcase the system:
 
 The implementation is open-sourced at [`cohere-ai/cohere-security-toolkit`](https://github.com/cohere-ai/cohere-security-toolkit).
 
-[[concepts/mcp]] | [[concepts/ai-agents]] | [[concepts/security-automation]] | [[tools/wiz]]
+[[concepts/mcp]] | [[concepts/ai-agents]] | [[concepts/security-automation]] | [[entities/wiz]]
 
 ## co/plot: Research Visualization Tool (June 2026)
 
@@ -260,7 +260,7 @@ North Automations embeds within Cohere's existing **North** platform, inheriting
 
 North Automations is available to all North customers.
 
-[[concepts/agent-team-swarm]] | [[concepts/mcp]] | [[concepts/enterprise-ai]] | [[concepts/workflow-automation]]
+[[concepts/multi-agents/agent-team-swarm]] | [[concepts/mcp]] | [[concepts/enterprise-ai]] | [[concepts/workflow-automation]]
 
 **Source:** [[raw/articles/2026-07-28_cohere_introducing-north-automations-ai-workflows]]
 
diff --git a/wiki/entities/dario-amodei.md b/wiki/entities/dario-amodei.md
index f91c8164..84532179 100644
--- a/wiki/entities/dario-amodei.md
+++ b/wiki/entities/dario-amodei.md
@@ -13,7 +13,7 @@ aliases:
 related:
   - [[entities/anthropic]]
   - [[entities/daniela-amodei]]
-  - [[concepts/ai-safety]]
+  - [[concepts/security-and-governance/ai-safety]]
   - [[concepts/ai-economics]]
 sources:
   - https://en.wikipedia.org/wiki/Dario_Amodei
@@ -83,7 +83,7 @@ A comprehensive governance framework arguing that AI is advancing far faster tha
 
 ## Related Concepts
 - [[concepts/ai-economics]]
-- [[concepts/ai-safety]]
+- [[concepts/security-and-governance/ai-safety]]
 - [[concepts/ai-policy]]
 
 ## Sources
diff --git a/wiki/entities/deepmind.md b/wiki/entities/deepmind.md
index e01b65e9..61f4b69c 100644
--- a/wiki/entities/deepmind.md
+++ b/wiki/entities/deepmind.md
@@ -68,7 +68,7 @@ DeepMind uses **Antigravity**, an internal IDE (Visual Studio–like) with a bui
 Moving from passing massive context blobs toward **shared file system collaboration** between pipeline components.
 
 ### Model Mixing
-Combining cheap models like [[concepts/gemma-4|Gemma 4]] ("effectively free from a quota perspective") with advanced models for critical components.
+Combining cheap models like [[entities/gemma-4|Gemma 4]] ("effectively free from a quota perspective") with advanced models for critical components.
 
 ### Code Review Automation
 Per-language auto-review models fine-tuned on style guides and good code examples.
@@ -146,6 +146,6 @@ See also [[concepts/open-science]] and [[concepts/ai-mathematics-theorem-proving
 
 - [[concepts/alphaevolve]] — DeepMind's Gemini-powered evolutionary coding agent
 - [[concepts/alpha-proof-nexus]] — DeepMind's LLM+Lean formal proof search system (May 2026)
-- [[concepts/agents/computer-use]] — Computer use as an agent modality
+- [[concepts/computer-use]] — Computer use as an agent modality
 - [[concepts/agentic-engineering]] — AI moving from chat boxes into operating layers
 - [[concepts/deep-research-agent-from-scratch]] — Ivan Leo's research agent workshop
diff --git a/wiki/entities/denseon-lateon.md b/wiki/entities/denseon-lateon.md
index 466540f1..8cba9a67 100644
--- a/wiki/entities/denseon-lateon.md
+++ b/wiki/entities/denseon-lateon.md
@@ -95,4 +95,4 @@ When BEIR evaluation data overlapping with training data is removed:
 - **Framework**: [[concepts/pylate|PyLate]] (CIKM 2025)
 - **Backbone**: ModernBERT, Ettin
 - **Predecessors**: ColBERT-Zero, GTE-ModernColBERT-v1
-- **Related concepts**: [[concepts/colbert|ColBERT]], [[entities/late-interaction|Late Interaction Workshop]], [[concepts/embeddings|Embeddings]], [[concepts/embedding-long-context-degradation|Embedding Long-Context Degradation]]
+- **Related concepts**: [[concepts/colbert|ColBERT]], [[entities/late-interaction|Late Interaction Workshop]], [[entities/embeddings|Embeddings]], [[concepts/embedding-long-context-degradation|Embedding Long-Context Degradation]]
diff --git a/wiki/entities/dimillian.md b/wiki/entities/dimillian.md
index 4d227e32..f6602395 100644
--- a/wiki/entities/dimillian.md
+++ b/wiki/entities/dimillian.md
@@ -3,7 +3,7 @@ title: "Thomas Ricouard (Dimillian)"
 description: "iOS/SwiftUI developer turned Codex Developer Experience engineer at OpenAI; author of Ice Cubes (Mastodon) and CodexMonitor, with widely-read articles on agentic iOS workflows and on-device Apple Foundation Models"
 type: entity
 created: 2026-09-26
-updated: 2026-09-26
+updated: 2026-10-04
 aliases:
   - Dimillian
   - Thomas Ricouard
diff --git a/wiki/entities/eugene-yan.md b/wiki/entities/eugene-yan.md
index 38c2d9ac..8d8c8c84 100644
--- a/wiki/entities/eugene-yan.md
+++ b/wiki/entities/eugene-yan.md
@@ -1,9 +1,10 @@
 ---
 title: "Eugene Yan (Ziyou Yan)"
 tags: [person]
+aliases: [eugeneyan]
 sources: []
 created: 2026-04-24
-updated: 2026-06-07
+updated: 2026-09-30
 type: entity
 ---
 
diff --git a/wiki/entities/eugeneyan.md b/wiki/entities/eugeneyan.md
index c99504cc..511af1f1 100644
--- a/wiki/entities/eugeneyan.md
+++ b/wiki/entities/eugeneyan.md
@@ -1,220 +1,16 @@
 ---
 title: Eugene Yan
 type: entity
-handle: "@eugeneyan"
+status: redirect
 created: 2026-04-10
-updated: 2026-07-06
-tags:
-  - person
-  - infrastructure
-sources:
-  - https://eugeneyan.com/writing/working-with-ai/
-  - https://eugeneyan.com/writing/cybersecurity-evals/
-  - https://claude.com/blog/using-llms-to-secure-source-code
+updated: 2026-09-30
+tags: [person, redirect]
+sources: []
+aliases: [eugeneyan]
 ---
 
+# Eugene Yan
 
-# Eugene Yan (@eugeneyan)
+> **Redirect**: This page has been merged into [[entities/eugene-yan]] — the canonical, comprehensive Eugene Yan profile (352 lines, incl. sub-pages [[entities/eugene-yan--core-ideas]], [[entities/eugene-yan--key-quotes]], [[entities/eugene-yan--timeline]]).
 
-| | |
-|---|---|
-| **X** | [@eugeneyan](https://x.com/eugeneyan) |
-| **Blog** | [eugeneyan.com/writing](https://eugeneyan.com/writing) |
-| **GitHub** | [eugeneyan](https://github.com/eugeneyan) |
-| **Role** | Member of Technical Staff, Anthropic (formerly Principal Applied Scientist, Amazon) |
-| **Known for** | "Applied LLMs" guide, LLM production patterns, recommender systems expertise, practical ML writing |
-| **Bio** | Eugene Yan (Ziyou Yan) is a Member of Technical Staff at Anthropic, where he works to bridge the field and the frontier in building safe, reliable AI systems at scale. Previously a Principal Applied Scientist at Amazon, he built real-time retrieval, bandit rankers, and recommendation systems. He is the lead author of the widely-read "What We've Learned From A Year of Building with LLMs" guide and maintains one of the most practical ML blogs in the industry. |
-
-## Overview
-
-Eugene Yan is among the most pragmatic and grounded voices in applied machine learning. His career spans e-commerce ML at Alibaba/Lazada, healthtech at a Series A startup, recommendation systems at Amazon, and now AI safety and production at Anthropic. This breadth of experience — from building ML systems in emerging markets to working at the frontier of AI development — gives him a uniquely practical perspective on what works and what doesn't in production AI.
-
-Yan's writing is distinguished by its emphasis on *shipping*. While many AI thought leaders focus on model capabilities or theoretical advances, Yan consistently brings the conversation back to production reality: evaluation, monitoring, data pipelines, cost management, and team organization. His blog at eugeneyan.com is a masterclass in applied ML, with over 200 posts spanning recommender systems, LLM engineering, leadership, and career development.
-
-His most influential contribution is arguably the ["Applied LLMs"](https://applied-llms.org/) guide — "What We've Learned From A Year of Building with LLMs" — co-authored with Bryan Bischof, Charles Frye, Hamel Husain, Jason Liu, and Shreya Shankar. This comprehensive document, published in mid-2024, became the de facto reference for engineering teams looking to move beyond AI demos into production systems. It is organized into three layers: tactical (prompting, RAG, evals), operational (team building, iteration processes), and strategic (business alignment, product-market fit).
-
-Yan currently writes a newsletter reaching 11,800+ readers on RecSys, LLMs, and engineering lessons. He has spoken at major conferences including the AI Engineer World's Fair, Netflix PRS Workshop, and numerous others.
-
-## Core Ideas
-
-### Seven Patterns for Building LLM Systems
-
-In his landmark July 2023 post ["Patterns for Building LLM-based Systems & Products"](https://eugeneyan.com/writing/llm-patterns/), Yan identified seven key patterns, organized along two axes: improving performance vs. reducing cost/risk, and closer to data vs. closer to user:
-
-1. **Evals** — The foundation: "Building solid evals should be the starting point for any LLM-based system or product (as well as conventional machine learning)." You can't improve what you can't measure.
-2. **RAG (Retrieval-Augmented Generation)** — Adding recent, external knowledge to ground LLM outputs and reduce hallucinations
-3. **Fine-tuning** — Getting better at specific tasks when prompting and RAG aren't sufficient
-4. **Caching** — Reducing latency and cost for repeated or similar queries
-5. **Guardrails** — Ensuring output quality, safety, and compliance
-6. **Defensive UX** — Anticipating and managing errors gracefully at the user interface level
-7. **Feedback Collection** — Continuously gathering user signals to improve the system
-
-> See [[concepts/llm-patterns-eugene-yan]] for details — covering implementation details of each pattern, framework evolution (v1→v2), and mapping to existing wiki pages.
-
-These patterns map to Yan's broader philosophy that LLM applications succeed or fail based on system design, not model capability alone.
-
-### Evals as the Foundation
-
-> *"Evals help us understand if our prompt engineering, retrieval augmentation, or finetuning is on the right track. Consider it eval-driven development, where your evals guide how you build your system and product."*
-
-In his October 2023 AI Engineer Summit keynote, Yan argued that annotation guidelines — the documents that guide human labelers — are one of the most valuable assets an ML team can build. Well-crafted guidelines improve both human consistency and model instructions, and can later seed fine-tuning datasets.
-
-> *"Eyeballing doesn't scale — it's good as a final vibe check, but it doesn't scale."*
-
-This insight has proven increasingly important as teams discover that their intuition about model quality diverges sharply from systematic evaluation.
-
-### The Demo-to-Production Reality Gap
-
-> *"There is a large class of problems that are easy to imagine and build demos for, but extremely hard to make products out of. For example, self-driving. It's easy to demo a car self-driving around a block but making it into a product takes a decade."* (citing Andrej Karpathy)
-
-Yan consistently emphasizes that production ML is about much more than model accuracy:
-- **Don't underestimate the effort it takes to go from demo to production**
-- **Scale makes everything harder** — Each 10x increase in traffic uncovers new bugs
-- **LLM economics depend on scale** — "Even the most expensive LLMs are not that expensive for B2B scale; even the cheapest LLMs are not that cheap for consumer scale." (citing Will Larson)
-- **The real bottlenecks aren't cost — they're trust, reliability, security**
-
-### Product Evals in Three Simple Steps
-
-In his November 2025 post ["Product Evals in Three Simple Steps"](https://eugeneyan.com/writing/product-evals/), Yan distilled the eval process:
-
-1. **Labeling a small dataset** — Start with real defects that actually affect users, not synthetic examples
-2. **Aligning LLM evaluators** — Ensure automated judges correlate with human judgment
-3. **Running the eval harness** — Create a reproducible pipeline for continuous measurement
-
-> *"I recently observed a team invest ~4 weeks into building their eval dataset and LLM-as-judge pipeline. That investment paid off by tightening the feedback loop and helping them iterate faster. That is the benefit of having product evals; not just to measure and improve the quality of the product, but to tighten the feedback loop."*
-
-### LLM-as-Judge Won't Save The Product—Fixing Your Process Will
-
-In his April 2025 post, Yan challenged the industry's over-reliance on automated evaluation:
-
-- LLM judges are themselves models with biases and limitations
-- The real differentiator is the *process* of building, testing, and iterating
-- Human evaluation remains essential, even when expensive
-- Evaluation should drive product decisions, not just model selection
-
-### Recommender Systems in the Age of LLMs
-
-In his March 2025 post ["Improving Recommendation Systems & Search in the Age of LLMs"](https://eugeneyan.com/writing/recsys-llm/), Yan explored how LLMs are transforming recommendation systems:
-
-- **LLM/multimodal-augmented model architectures** — Combining language models with traditional recsys approaches
-- **Scaling laws** — Performance consistently improves as model and dataset size expand
-- **Knowledge distillation** — Transferring insights from large models to smaller, efficient ones
-- **Cross-domain transfer learning** — Handling limited data scenarios
-- **Parameter-efficient fine-tuning** — Techniques like LoRAs for domain adaptation
-- **Semantic IDs** — Using semantically meaningful tokens instead of random hash IDs, enabling LLM-recommender hybrids that can both converse and recommend
-
-### 39 Lessons on Building ML Systems
-
-In his November 2024 post, Yan synthesized lessons from multiple ML conferences:
-
-**Building effective ML systems:**
-1. The real world is messy — define reward functions, handle edge cases
-2. You don't always need machine learning — heuristics and SQL are valuable baselines
-3. Set realistic expectations — many problems have a ceiling, especially those involving human behavior
-4. Don't overlook time — user preferences change, inventory gets drawn down
-5. Evals are a differentiator and moat
-6. Build with an eye toward the future — flexibility beats specialization
-7. It takes a village — infra, engineering, data, ML, design, product, business
-
-**Production and scaling:**
-- Each 10x-ing of scale uncovers new bugs
-- Execution is everything — navigating from legacy systems to high velocity
-- Start simple and iterate
-
-## Key Work
-
-### Applied LLMs Guide
-
-["What We've Learned From A Year of Building with LLMs"](https://applied-llms.org/) (June 2024) — Co-authored with Bryan Bischof, Charles Frye, Hamel Husain, Jason Liu, and Shreya Shankar. Published on O'Reilly Media in three parts (Tactical, Operational, Strategic). The guide covers:
-
-- **Tactical:** Prompting, RAG, flow engineering, evals, monitoring
-- **Operational:** Team building, iteration processes, organizational challenges
-- **Strategic:** Business alignment, product-market fit, competitive positioning
-
-### Notable Blog Posts (eugeneyan.com/writing)
-| Jun 2026 | "Patterns for Building Cybersecurity Evals" | Cybersecurity evaluation benchmarks |
-| May 2026 | "How to Work and Compound with AI" | Working effectively with AI, context as infrastructure |
-
-| Date | Title | Topic |
-|---|---|---|
-| Dec 2025 | "2025 Year in Review" | Annual reflection and lessons |
-| Nov 2025 | "Product Evals in Three Simple Steps" | Building evaluation pipelines |
-| Nov 2025 | "Advice for New Principal Tech ICs" | Career guidance for senior engineers |
-| Sep 2025 | "Training an LLM-RecSys Hybrid for Steerable Recs with Semantic IDs" | Prototype combining LLMs with recommendation |
-| Jun 2025 | "Evaluating Long-Context Question & Answer Systems" | LLM evaluation methodology |
-| May 2025 | "Exceptional Leadership: Some Qualities, Behaviors, and Styles" | Engineering leadership |
-| Apr 2025 | "An LLM-as-Judge Won't Save The Product—Fixing Your Process Will" | Evaluation philosophy |
-| Mar 2025 | "Improving Recommendation Systems & Search in the Age of LLMs" | RecSys + LLM integration |
-| Aug 2024 | "Evaluating the Effectiveness of LLM-Evaluators (aka LLM-as-Judge)" | Automated evaluation analysis |
-| Jul 2024 | "How to Interview and Hire ML/AI Engineers" | Hiring best practices |
-| May 2024 | "What We've Learned From A Year of Building with LLMs" | Applied LLMs guide |
-| May 2024 | "Prompting Fundamentals and How to Apply them Effectively" | Prompt engineering |
-| Nov 2024 | "39 Lessons on Building ML Systems, Scaling, Execution, and More" | Conference takeaways |
-| Jul 2023 | "Patterns for Building LLM-based Systems & Products" | The seven-pattern framework |
-
-### Speaking Engagements
-
-- **AI Engineer World's Fair 2024** — Keynote: "What We Learned from a Year of LLMs"
-- **AI Engineer 2025** — "Improving RecSys & Search with LLM techniques"
-- **Netflix PRS Workshop 2024** — "Applying LLMs to Recommendation Experiences"
-- **AI Engineer Summit 2023** — Keynote: "Building Blocks for LLM Systems"
-- Multiple other conference talks on ML engineering and LLM production
-### ai.engineer Conference (2026)
-
-Eugene Yan appeared at the ai.engineer conference (2026), sharing insights on working with AI and cybersecurity evals. He linked to three resources:
-
-- [How to Work and Compound with AI](https://eugeneyan.com/writing/working-with-ai/) — A deep dive on context as infrastructure, taste as configuration, verification for autonomy, scaling via delegation, and closing the loop. Key insight: treat AI sessions like onboarding a new teammate — maintain per-project `CLAUDE.md` files, `INDEX.md` annotated indexes, and structured memory layers. Skills encode workflows in markdown (e.g., `/polish`, `/write`, `/daily`) and are refined via session transcripts.
-- [Patterns for Building Cybersecurity Evals](https://eugeneyan.com/writing/cybersecurity-evals/) — Comprehensive survey of cybersecurity benchmarks (Cybench, CVE-Bench, CyberGym, ExploitGym, ExploitBench, MHBench, SCONE-Bench) measuring AI agent capabilities in finding/exploiting vulnerabilities. Key findings: agents hit ceilings on complex exploits, system frameworks matter more than model choice for red-teaming, and Claude Mythos led with 157/898 exploit instances on ExploitGym.
-- [Using LLMs to Secure Source Code](https://claude.com/blog/using-llms-to-secure-source-code) — Anthropic's blog post on using Claude for security-focused code review and vulnerability detection.
-
-### Open Source Projects
-
-- **applied-llms.org** — The Applied LLMs guide
-- **applyingml.com** — Papers, guides, and interviews on applying ML effectively
-- **applied-ml** — Curated papers on real-world ML systems in industry
-
-### Prototypes
-
-- **Semantic IDs:** Training an LLM-RecSys hybrid for steerable recommendations
-- **News Agents:** Automating daily news via agentic workflows
-- **AI Reading Club:** Prototyping an AI-powered reading experience
-- **LLM UXs:** Interacting with LLMs with minimal chat interfaces
-
-## Blog / Recent Posts
-
-Eugene Yan's blog at [eugeneyan.com/writing](https://eugeneyan.com/writing) has published 209+ posts totaling 420,000+ words. Key themes include:
-
-- **ML Engineering** — Practical guidance on building, deploying, and scaling ML systems
-- **LLM Production** — Patterns, anti-patterns, and lessons from building with foundation models
-- **Recommender Systems** — Architecture, evaluation, and LLM integration
-- **Engineering Leadership** — Hiring, team building, career development for tech ICs
-- **Evaluation & Quality** — Evals, LLM-as-judge, annotation guidelines
-- **Career & Writing** — Reflections on professional growth and the craft of technical writing
-
-## Related People
-
-- **Chip Huyen** — Both focus on production ML and engineering; Huyen more on systems design, Yan on LLM application patterns
-- **Ethan Mollick** — Both write about practical AI usage; Mollick from business/education, Yan from engineering/production
-- **Lilian Weng** — Both address LLM capabilities and production; Weng from research, Yan from applied engineering
-- **Bryan Bischof** — Co-author on the Applied LLMs guide
-- **Hamel Husain** — Co-author on the Applied LLMs guide
-- **Shreya Shankar** — Co-author on the Applied LLMs guide; shares focus on ML evaluation
-- **Andrej Karpathy** — Both cite Karpathy's "demo to production" insight; both value practical engineering
-- **Samuel Colvin** — Both work on production-grade AI tools; Colvin on type safety, Yan on evaluation and patterns
-
-## X Activity Themes
-
-Eugene Yan's X/Twitter activity focuses on:
-
-- **ML Engineering Best Practices** — Practical advice from years of production experience
-- **LLM System Patterns** — Sharing insights on RAG, evals, fine-tuning, and guardrails
-- **Recommender Systems** — Updates on RecSys research and LLM integration
-- **Engineering Leadership** — Advice for senior tech ICs and engineering managers
-- **Career Development** — Lessons on hiring, growth, and navigating the tech industry
-- **Technical Writing** — Reflections on the craft of writing about ML and AI
-- **Conference Takeaways** — Summarizing key lessons from ML conferences
-- **Prototype Updates** — Sharing experimental work on LLM-RecSys hybrids and agentic workflows
-
-## See Also
-
-- [[entities/_index]]
+See also: [[concepts/llm-patterns-eugene-yan]]
diff --git a/wiki/entities/flue.md b/wiki/entities/flue.md
index 65c22e09..d3515449 100644
--- a/wiki/entities/flue.md
+++ b/wiki/entities/flue.md
@@ -99,7 +99,7 @@ Key commitments:
 
 Positioning quote: *"The best tools are the ones that float above the host. That opens the door for the most developer adoption and the most innovation."*
 
-Source: [React for Agents: Astro Creator Brings Hooks to his Meta-Harness, Flue](https://www.latent.space/p/flue-2) — Richard MacManus interview with Fred Schott, Latent Space, Aug 15 2026. Connects to the Bret Taylor framing ("jQuery era of agents, not the react era") and the [[concepts/harness-engineering]] / [[concepts/agent-team-swarm|meta-harness]] debates.
+Source: [React for Agents: Astro Creator Brings Hooks to his Meta-Harness, Flue](https://www.latent.space/p/flue-2) — Richard MacManus interview with Fred Schott, Latent Space, Aug 15 2026. Connects to the Bret Taylor framing ("jQuery era of agents, not the react era") and the [[concepts/harness-engineering]] / [[concepts/multi-agents/agent-team-swarm|meta-harness]] debates.
 
 ## Related Concepts
 
diff --git a/wiki/entities/fred-schott.md b/wiki/entities/fred-schott.md
index cc6bc208..ab9cb17d 100644
--- a/wiki/entities/fred-schott.md
+++ b/wiki/entities/fred-schott.md
@@ -81,7 +81,7 @@ In a [Latent Space interview with Richard MacManus](https://www.latent.space/p/f
 - **On LangChain Managed Deep Agents**: not on Flue's roadmap — "It's so early for us, we're just focused on building the best harness."
 - Onboarding is **agent-first**: "pass this prompt to your agent, it's gonna guide you through it" — the docs have markdown support, and many users (including MacManus) set up Flue agents via Claude Code.
 
-The interview connects his v1 framing ("like Claude Code, but 100% headless and programmable") to the broader [[concepts/harness-engineering]] and [[concepts/agent-team-swarm|meta-harness]] landscape. Flue's origin: an issue-triage system inside the Astro repo that grew into a headless, hostable Claude Code experience. See [[entities/flue]] for the full framework detail.
+The interview connects his v1 framing ("like Claude Code, but 100% headless and programmable") to the broader [[concepts/harness-engineering]] and [[concepts/multi-agents/agent-team-swarm|meta-harness]] landscape. Flue's origin: an issue-triage system inside the Astro repo that grew into a headless, hostable Claude Code experience. See [[entities/flue]] for the full framework detail.
 
 ## Related
 
diff --git a/wiki/entities/hermes-agent.md b/wiki/entities/hermes-agent.md
index d1206b76..dc72bc94 100644
--- a/wiki/entities/hermes-agent.md
+++ b/wiki/entities/hermes-agent.md
@@ -364,7 +364,7 @@ See [[concepts/skill-architecture-patterns]] for detailed comparison with OpenCl
 ## Related Pages
 
 - [[entities/teknium]] — Hermes Agent creator, Nous Research co-founder
-- [[harness-engineering/agentic-workflows]] — Agentic Engineering patterns (related design philosophy)
+- [[concepts/harness-engineering/agentic-workflows]] — Agentic Engineering patterns (related design philosophy)
 - [[claude-memory]] — File-based memory architecture (comparable design)
 - [[concepts/harness-engineering]] — Harness Engineering framework (related orchestration concepts)
 - [[concepts/ai-agent-memory-middleware]] — AI Agent Memory Middleware (complementary memory layer concepts)
diff --git a/wiki/entities/hugo-bowne-anderson.md b/wiki/entities/hugo-bowne-anderson.md
index 73817b67..f56243ce 100644
--- a/wiki/entities/hugo-bowne-anderson.md
+++ b/wiki/entities/hugo-bowne-anderson.md
@@ -369,7 +369,7 @@ This case study directly validates Hugo's broader philosophy: evaluation-driven
 
 ## See Also
 
-- [[entities/show-us-your-agent-skills]]
+- [[concepts/show-us-your-agent-skills]]
 - [[entities/_index]]
 - [[concepts/agent-harness-comparison]]
 - [[concepts/harness-commoditization]]
diff --git a/wiki/entities/ilya-sutskever.md b/wiki/entities/ilya-sutskever.md
index 719d23a1..541388b0 100644
--- a/wiki/entities/ilya-sutskever.md
+++ b/wiki/entities/ilya-sutskever.md
@@ -181,7 +181,7 @@ This contrasts sharply with OpenAI's product-driven approach and Anthropic's dua
 - [[concepts/ai-alignment]] — Co-founded superalignment team with Sutskever; resigned citing safety deprioritization
 - [[entities/openai]] — Company Sutskever co-founded and led technically (2015–2024)
 - [[concepts/security-and-governance/ai-safety]] — SSI, Sutskever's current venture- [[concepts/security-and-governance/ai-safety]] — Sutskever's primary research focus at SSI
-- [[concepts/openai]] — Team Sutskever co-founded at OpenAI
+- [[entities/openai]] — Team Sutskever co-founded at OpenAI
 ## Sources
 
 - Grokipedia: Ilya Sutskever
diff --git a/wiki/entities/ivan-leo.md b/wiki/entities/ivan-leo.md
index 319dae9b..82fe2f24 100644
--- a/wiki/entities/ivan-leo.md
+++ b/wiki/entities/ivan-leo.md
@@ -152,7 +152,7 @@ GitHub ([@ivanleomk](https://github.com/ivanleomk), Singapore-based, 212 public
 - [[entities/pi]] — Pi coding agent philosophy
 - [[entities/manus]] — Former employer (Jul 2025 – Mar 2026, $75M → $100M ARR)
 - [[entities/deepmind]] — Current employer (Mar 2026–present, SF)
-- [[entities/logan-kilpatrick]] — DeepMind colleague / DevRel orbit
+- [[concepts/logan-kilpatrick]] — DeepMind colleague / DevRel orbit
 - [[concepts/self-evolving-agents]] — Related concept
 
 ## Sources
diff --git a/wiki/entities/jina-ai.md b/wiki/entities/jina-ai.md
index 725d73bc..44af4fe4 100644
--- a/wiki/entities/jina-ai.md
+++ b/wiki/entities/jina-ai.md
@@ -59,4 +59,4 @@ Jina AI is a search AI company founded in 2020 by **Han Xiao**, acquired by **[[
 - **Parent**: [[entities/elastic|Elastic]] (acquired Oct 2025)
 - **Founder**: Han Xiao → now VP of AI at Elastic
 - **Competitors/Peers**: [[entities/cohere|Cohere]] (embeddings), [[entities/openai|OpenAI]] (embeddings)
-- **Related concepts**: [[concepts/embeddings|Embeddings]], [[concepts/embedding-long-context-degradation|Embedding Long-Context Degradation]], [[concepts/information-retrieval|Information Retrieval]], [[concepts/mrcr|MRCR]]
+- **Related concepts**: [[entities/embeddings|Embeddings]], [[concepts/embedding-long-context-degradation|Embedding Long-Context Degradation]], [[concepts/information-retrieval|Information Retrieval]], [[concepts/ai-benchmarks/mrcr|MRCR]]
diff --git a/wiki/entities/junior.md b/wiki/entities/junior.md
index cd74e3dd..6e9fa22a 100644
--- a/wiki/entities/junior.md
+++ b/wiki/entities/junior.md
@@ -69,7 +69,7 @@ Ronacher describes this as producing a "much more natural" developer experience.
 
 - [[concepts/agent-resource-subscriptions]] — the generalized design pattern
 - [[entities/armin-ronacher]] — creator and primary architect
-- [[entities/sentry]] — parent company
+- [[concepts/sentry]] — parent company
 - [[concepts/coding-agents/agentic-coding]] — broader agentic coding context
 - [[entities/pi]] — Pi coding agent (Earendil), another minimal agent design
 
diff --git a/wiki/entities/k-eric-drexler.md b/wiki/entities/k-eric-drexler.md
index aef65e09..abeaf256 100644
--- a/wiki/entities/k-eric-drexler.md
+++ b/wiki/entities/k-eric-drexler.md
@@ -59,7 +59,7 @@ This debate has shaped much of the modern conversation in AI safety and governan
 
 - [[concepts/comprehensive-ai-services]] — The CAIS framework, Drexler's most influential AI contribution
 - [[concepts/superintelligence]] — Broader topic of AI surpassing human capabilities
-- [[concepts/ai-safety]] — Safety implications of advanced AI
+- [[concepts/security-and-governance/ai-safety]] — Safety implications of advanced AI
 - [[entities/future-of-humanity-institute]] — Institution where Drexler conducted FHI research
 - [[concepts/nick-bostrom]] — Contrasting agent-centric superintelligence framework
 
diff --git a/wiki/entities/khe-hy.md b/wiki/entities/khe-hy.md
index bf4645ba..4d227d14 100644
--- a/wiki/entities/khe-hy.md
+++ b/wiki/entities/khe-hy.md
@@ -37,11 +37,11 @@ sources:
 
 ## Connection to Broader Trends
 
-Khe Hy's framework connects to [[entities/reflexive-ai]] (Shopify's approach) and [[concepts/experience-is-a-tax]] — both address organizational resistance to AI adoption.
+Khe Hy's framework connects to [[concepts/reflexive-ai]] (Shopify's approach) and [[concepts/experience-is-a-tax]] — both address organizational resistance to AI adoption.
 
 ## Related
 
-- [[entities/reflexive-ai]]
+- [[concepts/reflexive-ai]]
 - [[concepts/experience-is-a-tax]]
 - [[entities/openclaw]]
 - [[entities/claude-code]]
diff --git a/wiki/entities/langchain.md b/wiki/entities/langchain.md
index c1fe97d6..52e4cb3d 100644
--- a/wiki/entities/langchain.md
+++ b/wiki/entities/langchain.md
@@ -193,7 +193,7 @@ See [[concepts/security-and-governance/agentic-security]] for broader agent secu
 
 LangChain Labs collaborated with **Fireworks AI** on a study fine-tuning **Qwen-3.5-35B** to detect *Perceived Error* — situations where a user *believes* the assistant made a mistake, judged from production traces on LangSmith. The work demonstrates that small, fine-tuned models can match or exceed frontier LLMs as evaluators at **10-100x lower cost**.
 
-See also: [[concepts/llm-as-judge]], [[concepts/evaluation]].
+See also: [[concepts/evaluation/llm-as-judge]], [[concepts/evaluation]].
 
 ### Key Findings
 
diff --git a/wiki/entities/lighton.md b/wiki/entities/lighton.md
index 7aedc9f8..05eaa0e6 100644
--- a/wiki/entities/lighton.md
+++ b/wiki/entities/lighton.md
@@ -63,4 +63,4 @@ LightOn is a French enterprise AI company founded in 2016 by **Igor Carron** and
 
 - **Key researchers**: Antoine Chaffin, Benjamin Clavié (Mixedbread AI collaborator)
 - **Peers**: [[entities/mistral-ai|Mistral AI]], Aleph Alpha (European data-sovereignty AI)
-- **Related concepts**: [[concepts/colbert|ColBERT]], [[entities/late-interaction|Late Interaction Workshop]], [[concepts/evaluation/longembed|LongEmbed]], [[concepts/embeddings|Embeddings]]
+- **Related concepts**: [[concepts/colbert|ColBERT]], [[entities/late-interaction|Late Interaction Workshop]], [[concepts/evaluation/longembed|LongEmbed]], [[entities/embeddings|Embeddings]]
diff --git a/wiki/entities/lilian-weng.md b/wiki/entities/lilian-weng.md
index 66dedea5..325a0eea 100644
--- a/wiki/entities/lilian-weng.md
+++ b/wiki/entities/lilian-weng.md
@@ -1,6 +1,7 @@
 ---
 title: "Lilian Weng (@lilianweng)"
 tags: [entity]
+aliases: [lilianweng]
 sources:
   - raw/newsletters/2026-07-08-ainews-lilian-weng-summarizes-35-papers-on-harness-engineering-for-rsi.md
 created: 2026-04-24
diff --git a/wiki/entities/lilianweng.md b/wiki/entities/lilianweng.md
index f461d5a7..d83804a1 100644
--- a/wiki/entities/lilianweng.md
+++ b/wiki/entities/lilianweng.md
@@ -1,156 +1,16 @@
 ---
 title: Lilian Weng
 type: entity
-handle: "@lilianweng"
+status: redirect
 created: 2026-04-10
-updated: 2026-04-10
-tags:
-  - person
-  - agent-safety
-  - ai-agents
-  - openai
+updated: 2026-09-30
+tags: [person, redirect]
 sources: []
+aliases: [lilianweng]
 ---
 
+# Lilian Weng
 
-# Lilian Weng (@lilianweng)
+> **Redirect**: This page has been merged into [[entities/lilian-weng]] — the canonical Lilian Weng profile (202 lines; OpenAI → Thinking Machines Lab co-founder, Lil'Log author).
 
-| | |
-|---|---|
-| **X** | [@lilianweng](https://x.com/lilianweng) |
-| **Blog** | [Lil'Log](https://lilianweng.github.io) |
-| **GitHub** | [lilianweng](https://github.com/lilianweng) |
-| **Role** | VP of Research, OpenAI |
-| **Known for** | Comprehensive ML survey posts, LLM-powered agents research, AI safety leadership |
-| **Bio** | Lilian Weng is VP of Research at OpenAI, where she leads risk management and safety research for frontier models. She joined OpenAI in 2018 after working as a data scientist and software engineer at Meta, Dropbox, and Affirm. Since 2017, she has maintained "Lil'Log," one of the most respected technical blogs in ML, known for its deeply-researched survey posts on transformers, agents, diffusion models, and AI safety. |
-
-## Overview
-
-Lilian Weng occupies a rare position at the intersection of frontier AI research and practical safety engineering. As VP of Research at OpenAI, she leads the Preparedness team — responsible for safeguarding against major risks from OpenAI's most powerful models. She also serves on OpenAI's board safety and security committee. Her career trajectory, from data scientist at major Silicon Valley companies to research leadership at one of the world's most impactful AI labs, gives her a uniquely grounded perspective on both the capabilities and risks of modern AI systems.
-
-But Weng's influence extends far beyond her role at OpenAI. Since 2017, she has maintained "Lil'Log" (lilianweng.github.io), a personal technical blog that has become one of the most comprehensive and accessible educational resources in machine learning. Her survey posts — covering topics from transformer architectures to adversarial attacks on LLMs — are distinguished by their mathematical rigor, thorough citations, and clear explanations. Many practitioners have used these posts as their primary introduction to advanced ML topics.
-
-Weng's research interests span the full spectrum of modern AI: reinforcement learning, generative models, large language models, agent architectures, AI safety, and interpretability. Her blog posts often serve as de facto literature reviews for entire subfields, synthesizing dozens of papers into coherent narratives. Her 2023 post "LLM Powered Autonomous Agents" became one of the most widely-cited overviews of the agentic AI landscape.
-
-## Core Ideas
-
-### LLM-Powered Autonomous Agents
-
-In her landmark June 2023 post ["LLM Powered Autonomous Agents"](https://lilianweng.github.io/posts/2023-06-23-agent/), Weng laid out a foundational architecture for AI agents:
-
-- **Planning** — The LLM functions as the agent's "brain," decomposing complex tasks into sub-goals using Chain-of-Thought (CoT), Tree of Thoughts (ToT), or self-reflection mechanisms like ReAct and Reflexion
-- **Memory** — Short-term memory (in-context learning, bounded by context window) and long-term memory (external vector stores using ANN algorithms like HNSW, FAISS, or ScaNN)
-- **Tool Use** — External API integration, where the LLM acts as a router to specialized modules
-
-Her analysis of ChemCrow (LLM + 13 chemistry tools) revealed a critical insight: human evaluations found ChemCrow vastly superior to GPT-4 alone, but LLM self-evaluations found them equal. *"LLMs lack domain expertise to self-evaluate correctness."* This finding has important implications for automated evaluation of AI systems.
-
-Weng also highlighted safety concerns: in the Boiko et al. scientific agent study, 36% of illicit drug synthesis requests were accepted, though web search helped reject 5/7 blocked cases. This underscored the need for robust safety layers in agentic systems.
-
-### Extrinsic Hallucinations in LLMs
-
-In her July 2024 post ["Extrinsic Hallucinations in LLMs"](https://lilianweng.github.io/posts/2024-07-07-hallucination/), Weng provided one of the most comprehensive analyses of why LLMs fabricate information:
-
-- **Pre-training data issues** — Internet-crawled corpora contain outdated, missing, or incorrect information that models memorize via log-likelihood maximization
-- **Fine-tuning risks** — Citing Gekhman et al. (2024), she showed that LLMs learn new knowledge substantially slower than existing knowledge, and learning new knowledge *increases hallucination tendency*
-- **Detection frameworks** — She catalogued methods including FActScore (decomposes text into atomic facts, validates via retrieval), SAFE (LLM agent iteratively searches to verify facts, 72% human agreement, 20x cheaper than manual), and SelfCheckGPT (black-box consistency across stochastic samples)
-
-Her anti-hallucination analysis covered RARR (Retroactive Attribution using Research and Revision), Self-RAG (end-to-end training with intermittent reflection tokens), and retrieval-augmented approaches.
-
-### Chain-of-Thought and Test-Time Compute
-
-In her May 2025 post ["Why We Think"](https://lilianweng.github.io/posts/2025-05-01-thinking/), Weng reviewed the rapidly evolving landscape of reasoning in LLMs:
-
-- Test-time compute and chain-of-thought reasoning have led to significant performance improvements
-- Smaller models combined with advanced inference algorithms can offer Pareto-optimal trade-offs in cost and performance
-- OpenAI's o1/o3 and DeepSeek-R1 showed that policy gradient algorithms applied to reasoning traces produce dramatic capability gains
-- Reward hacking remains a fundamental challenge: RL agents exploit flaws in reward functions
-
-She called for more research on open questions in test-time compute and chain-of-thought reasoning, noting that the exploration "presents new opportunities for reflection and error correction."
-
-### Reward Hacking in Reinforcement Learning
-
-In her November 2024 post, Weng examined how RL agents exploit imperfect reward functions — a problem that becomes more acute as RLHF becomes the de facto method for LLM alignment. She connected reward hacking to broader challenges in specifying objectives for increasingly capable AI systems.
-
-### High-Quality Human Data
-
-In February 2024, Weng wrote about the critical importance of human data quality for training modern models. As AI systems improve, the bottleneck shifts from compute and algorithms to the availability of high-quality human-generated training data — a resource that is finite and unevenly distributed across domains.
-
-### Adversarial Attacks on LLMs
-
-Her October 2023 post surveyed the landscape of adversarial attacks on language models, including jailbreak prompts, prompt injection, and data poisoning. She noted that adversarial attacks on text are "a lot more challenging" than on images due to the lack of direct gradient signals, connecting this to her earlier work on controllable text generation.
-
-## Key Work
-
-### Lil'Log Blog Posts (2017–2025)
-
-Weng's blog contains over 50 technical deep-dives spanning approximately 19 hours of reading. Key posts include:
-
-| Date | Title | Est. Read | Topic |
-|---|---|---|---|
-| May 2025 | "Why We Think" | 40 min | Test-time compute, CoT reasoning |
-| Nov 2024 | "Reward Hacking in Reinforcement Learning" | 37 min | RL safety, objective specification |
-| Jul 2024 | "Extrinsic Hallucinations in LLMs" | 29 min | LLM factuality, detection methods |
-| Apr 2024 | "Diffusion Models for Video Generation" | 20 min | Generative models for video |
-| Feb 2024 | "Thinking about High-Quality Human Data" | 20 min | Training data quality |
-| Oct 2023 | "Adversarial Attacks on LLMs" | 33 min | Jailbreaks, prompt injection |
-| Jun 2023 | "LLM Powered Autonomous Agents" | 31 min | Agent architecture, planning, memory |
-| Mar 2023 | "Prompt Engineering" | 21 min | In-context learning, prompting methods |
-| Jan 2023 | "The Transformer Family Version 2.0" | 45 min | Transformer architecture variants |
-| Jan 2023 | "Large Transformer Model Inference Optimization" | 9 min | Efficient inference |
-| 2022 | "Some Math behind Neural Tangent Kernel" | 17 min | Theoretical ML |
-| 2021 | "What are Diffusion Models?" | 31 min | Generative models |
-| 2020 | "How to Build an Open-Domain Question Answering System?" | 33 min | QA systems |
-| 2019 | "Meta Reinforcement Learning" | 22 min | RL meta-learning |
-| 2018 | "Policy Gradient Algorithms" | 52 min | RL algorithms |
-| 2017 | "Learning Word Embedding" | 18 min | NLP fundamentals |
-
-### OpenAI Research Leadership
-
-As VP of Research at OpenAI, Weng leads the Preparedness team, which is responsible for:
-- Safeguarding against major risks from frontier models
-- Consolidating safety research under her leadership
-- Serving on the board's safety and security committee
-- Overseeing model evaluation and red-teaming efforts
-
-Business Insider named Weng to their 2024 AI Power List for this work.
-
-### Previous Industry Experience
-
-Before joining OpenAI in 2018, Weng worked as a data scientist and software engineer at:
-- **Meta (Facebook)** — ML/data science
-- **Dropbox** — Data engineering
-- **Affirm** — Financial ML systems
-
-## Blog / Recent Posts
-
-Lil'Log (lilianweng.github.io) is Weng's personal technical blog, maintained since 2017. It is distinguished by:
-
-- **Mathematical rigor** — Posts include equations, proofs, and algorithmic details
-- **Comprehensive citations** — Each post references dozens of papers with proper attribution
-- **Visual explanations** — Diagrams and figures clarify complex architectures
-- **Long-form depth** — Posts average 20–45 minutes of reading time
-- **Broad coverage** — From classical ML (multi-armed bandits, object detection) to cutting-edge AI (diffusion models, LLM agents, adversarial attacks)
-
-## Related People
-
-- **John Schulman** — OpenAI colleague who provided feedback and edits on Weng's "Why We Think" post; co-creator of RLHF and PPO
-- **Chip Huyen** — Both address ML systems; Huyen from production engineering, Weng from research depth
-- **Eugene Yan** — Both write about LLM systems in production; Yan focuses on RecSys, Weng on fundamental research
-- **Andrej Karpathy** — Both produce highly educational content on deep learning; Karpathy through videos/talks, Weng through written surveys
-- **Andriy Burkov** — Both excel at making complex ML accessible through writing
-- **Sam Altman** — CEO of OpenAI where Weng serves as VP of Research
-
-## X Activity Themes
-
-Lilian Weng's X/Twitter activity focuses on:
-
-- **AI Safety Research** — Updates on OpenAI's preparedness and safety work
-- **Technical Deep-Dives** — Sharing and discussing new ML papers and research developments
-- **Blog Post Announcements** — Promoting new Lil'Log entries with detailed summaries
-- **AI Policy & Governance** — Commentary on regulatory approaches to frontier AI
-- **Research Community Engagement** — Interactions with other ML researchers and practitioners
-- **Educational Content** — Sharing resources for learning advanced machine learning concepts
-
-## See Also
-
-- [[entities/_index]]
+See also: [[entities/thinking-machines-lab]]
diff --git a/wiki/entities/lmsys-org.md b/wiki/entities/lmsys-org.md
index fccb475b..53424871 100644
--- a/wiki/entities/lmsys-org.md
+++ b/wiki/entities/lmsys-org.md
@@ -28,7 +28,7 @@ updated: 2026-04-27
 
 **LMSYS Org** (Large Model Systems Organization) is an open research organization based at UC Berkeley SkyLab focused on developing large language model systems that are open, accessible, and scalable. They are best known for creating:
 
-- **[[entities/sglang]]** — A fast and expressive LLM serving framework with RadixAttention
+- **[[concepts/inference/sglang]]** — A fast and expressive LLM serving framework with RadixAttention
 - **Chatbot Arena** (lmarena.ai) — The industry-standard crowdsourced LLM evaluation platform
 - **Miles** — An open-source RL post-training framework
 - **FastChat** — An open-source platform for training, serving, and evaluating LLMs
diff --git a/wiki/entities/matt-van-horn.md b/wiki/entities/matt-van-horn.md
index 13847870..9d010428 100644
--- a/wiki/entities/matt-van-horn.md
+++ b/wiki/entities/matt-van-horn.md
@@ -26,7 +26,7 @@ sources:
 related:
   - "[[entities/hermes-agent]]"
   - "[[concepts/hermes-agent-use-cases]]"
-  - "[[entities/reflexive-ai]]"
+  - "[[concepts/reflexive-ai]]"
   - "[[concepts/agentic-engineering]]"
   - "[[concepts/compound-engineering-every]]"
   - "[[entities/every-inc]]"
@@ -96,7 +96,7 @@ Authored a comprehensive 30-day analysis of Hermes Agent use cases across 7 plat
 - Named as the definitive community landscape study for the Hermes Agent ecosystem
 
 ### AI Adoption & Reflexive AI
-- Documented Shopifys Reflexive AI Baseline policy ([[entities/reflexive-ai]])
+- Documented Shopifys Reflexive AI Baseline policy ([[concepts/reflexive-ai]])
 - Published research on entrepreneurship trends grounded in Shopify's internal data science
 - Case study referenced as a model for organizational AI adoption
 
@@ -115,5 +115,5 @@ Van Horn publishes analysis at the intersection of AI adoption, entrepreneurship
 - [[entities/every-inc]] — The company behind Compound Engineering, Monologue, Proof
 - [[entities/hermes-agent]]
 - [[concepts/hermes-agent-use-cases]]
-- [[entities/reflexive-ai]]
+- [[concepts/reflexive-ai]]
 - [[entities/solo-founder-stack]]
diff --git a/wiki/entities/metR.md b/wiki/entities/metR.md
index bc6074c9..0c3f9b6f 100644
--- a/wiki/entities/metR.md
+++ b/wiki/entities/metR.md
@@ -15,7 +15,7 @@ sources:
 
 # METR (Model Evaluation & Threat Research)
 
-**METR** is an independent research lab focused on evaluating AI capability, safety, and the pace of AI-driven progress. It publishes empirical studies on how quickly AI systems are advancing across domains and how that translates to real-world utility — a key resource for the [[concepts/evaluation/ai-evals]] and [[concepts/ai-safety]] conversations.
+**METR** is an independent research lab focused on evaluating AI capability, safety, and the pace of AI-driven progress. It publishes empirical studies on how quickly AI systems are advancing across domains and how that translates to real-world utility — a key resource for the [[concepts/evaluation/ai-evals]] and [[concepts/security-and-governance/ai-safety]] conversations.
 
 METR has contributed to several benchmark and evaluation threads in this wiki (e.g. RE-Bench, the RAM relative-adoption metric, and Epoch AI × METR long-horizon programming benchmarks).
 
@@ -39,7 +39,7 @@ METR's differential-acceleration framing (some domains accelerate, others don't)
 - [[concepts/ai-discovery-acceleration]] — the differential-acceleration finding
 - [[concepts/evaluation/ai-evals]] — evaluation methodology
 - [[concepts/recursive-self-improvement]] — RSI
-- [[concepts/ai-safety]] — AI safety
+- [[concepts/security-and-governance/ai-safety]] — AI safety
 
 ## Sources
 - METR note: [Have We Seen an Acceleration in Discoveries?](https://metr.org/notes/2026-08-14-llm-contribution-to-discoveries/) (Cunningham & Rush, 2026-08-14)
diff --git a/wiki/entities/microsoft-agent-framework.md b/wiki/entities/microsoft-agent-framework.md
index 2f7ada66..d5f058bd 100644
--- a/wiki/entities/microsoft-agent-framework.md
+++ b/wiki/entities/microsoft-agent-framework.md
@@ -83,5 +83,5 @@ Microsoft Agent Framework v1.0 represents the convergence of two major Microsoft
 - [[concepts/multi-agents/multi-agent]] — Multi-agent AI systems
 - [[concepts/mcp]] — Model Context Protocol
 - [[entities/autogen]] — Microsoft AutoGen framework
-- [[entities/semantic-kernel]] — Microsoft Semantic Kernel
+- [[concepts/semantic-kernel]] — Microsoft Semantic Kernel
 - [[concepts/agent-framework]] — AI agent frameworks landscape
diff --git a/wiki/entities/microsoft-ai-team.md b/wiki/entities/microsoft-ai-team.md
index 894e4877..d263b358 100644
--- a/wiki/entities/microsoft-ai-team.md
+++ b/wiki/entities/microsoft-ai-team.md
@@ -40,7 +40,7 @@ The Microsoft AI Team operates as an internal research division of [[entities/mi
 ## Related Concepts
 - [[entities/mai-thinking-1]] — MAI flagship reasoning model
 - [[entities/microsoft]] — Parent company
-- [[concepts/reinforcement-learning]] — Core training methodology
+- [[concepts/post-training/reinforcement-learning]] — Core training methodology
 - [[concepts/mixture-of-experts]] — Model architecture
 - [[concepts/mai-thinking]] — Hill-climbing approach concept
 
diff --git a/wiki/entities/minimax.md b/wiki/entities/minimax.md
index e51b50e9..31014a12 100644
--- a/wiki/entities/minimax.md
+++ b/wiki/entities/minimax.md
@@ -45,7 +45,7 @@ This marks MiniMax's entry into AI video generation, extending beyond its M-seri
 
 On August 2, 2026, MiniMax released **MiniMax-H3**, which it describes as "a general-purpose, omni-modal generative system": it accepts text, images, audio and video inputs and generates up to 15-second video clips **with audio included** — a notable step beyond silent video outputs.
 
-The community package **PipeNetwork/minimax-h3-mlx** ports H3 to **MLX** for running on [[entities/apple|Apple Silicon]]. [[entities/simon-willison|Simon Willison]] ran it on his M5 Max MacBook Pro, downloading ~115 GB of model files; a single video generation took just under 45 minutes. The run pattern is:
+The community package **PipeNetwork/minimax-h3-mlx** ports H3 to **MLX** for running on [[concepts/apple|Apple Silicon]]. [[entities/simon-willison|Simon Willison]] ran it on his M5 Max MacBook Pro, downloading ~115 GB of model files; a single video generation took just under 45 minutes. The run pattern is:
 
 ```bash
 # First download the models
diff --git a/wiki/entities/modal-labs.md b/wiki/entities/modal-labs.md
index a4c1a140..022cee8d 100644
--- a/wiki/entities/modal-labs.md
+++ b/wiki/entities/modal-labs.md
@@ -99,7 +99,7 @@ This is architecturally significant for AI coding agents (background agent workf
 
 Source: raw/articles/modal.com--blog-unpacking-sandbox-startup-latency--b8f065a9.md
 
-See also: [[concepts/speculative-decoding]], [[entities/sglang]], [[concepts/vllm]], [[concepts/agent-experience]], [[concepts/agentic-engineering]]
+See also: [[concepts/speculative-decoding]], [[concepts/inference/sglang]], [[concepts/vllm]], [[concepts/agent-experience]], [[concepts/agentic-engineering]]
 
 ## Agent Experience (AX) Design Philosophy
 
diff --git a/wiki/entities/nemotron-cascade-2.md b/wiki/entities/nemotron-cascade-2.md
index a8f79bd7..599a8669 100644
--- a/wiki/entities/nemotron-cascade-2.md
+++ b/wiki/entities/nemotron-cascade-2.md
@@ -54,6 +54,6 @@ By activating only 3B parameters per token, the model achieves competitive or su
 - [[entities/nvidia]] — parent company and broader model family
 - [[concepts/mixture-of-experts]] — MoE architecture principles
 - [[concepts/local-llm/_index]] — local deployment landscape
-- [[concepts/gpt/gpt-oss]] — OpenAI's open-weight competitor
+- [[entities/gpt-oss]] — OpenAI's open-weight competitor
 - [[entities/gemma-4]] — Google's open model family
 - [[concepts/reasoning-models]] — reasoning capabilities in LLMs
diff --git a/wiki/entities/north-mini-code.md b/wiki/entities/north-mini-code.md
index 6917f0ec..9b143f78 100644
--- a/wiki/entities/north-mini-code.md
+++ b/wiki/entities/north-mini-code.md
@@ -87,4 +87,4 @@ Trained on multiple scaffolds (SWE-Agent, mini-SWE-Agent, OpenCode, Terminus 2)
 - [[concepts/mixture-of-experts]] — MoE architecture
 - [[concepts/ai-benchmarks/swe-bench]] — Key evaluation benchmark
 - [[concepts/agentic-engineering]] — Agentic coding paradigm
-- [[concepts/rlm]] — Reinforcement Learning from Execution Feedback (related RLVR approach)
+- [[entities/omar-khattab/rlm]] — Reinforcement Learning from Execution Feedback (related RLVR approach)
diff --git a/wiki/entities/odyssey-ml.md b/wiki/entities/odyssey-ml.md
index 54ca12e8..24ab27f2 100644
--- a/wiki/entities/odyssey-ml.md
+++ b/wiki/entities/odyssey-ml.md
@@ -3,7 +3,7 @@ title: "Odyssey"
 description: "Oliver Cameron and Jeff Hawke's world-model AI lab — general-purpose foundation world models (Odyssey-3, Agora-2 multi-agent, Starchild-1 multimodal, PROWL RL), $310M Series B with AWS as preferred cloud"
 type: entity
 created: 2026-09-26
-updated: 2026-09-26
+updated: 2026-10-04
 aliases:
   - odyx
   - Odyssey
diff --git a/wiki/entities/omar-khattab/research-trajectory.md b/wiki/entities/omar-khattab/research-trajectory.md
index 3958846c..625053d6 100644
--- a/wiki/entities/omar-khattab/research-trajectory.md
+++ b/wiki/entities/omar-khattab/research-trajectory.md
@@ -11,19 +11,19 @@ type: sub-entity
 # Research Trajectory
 
 ## Phase 1: Neural Information Retrieval (2019–2022)
-- [[entities/omar-khattab/colbert|ColBERT]], ColBERTv2, PLAID
+- [[concepts/colbert|ColBERT]], ColBERTv2, PLAID
 - Multi-hop retrieval ([[entities/omar-khattab/baleen|Baleen]])
 - Relevance-guided supervision for open QA
 - *Theme:* How do we make deep LMs efficient for search?
 
 ## Phase 2: Foundation Model Programming (2022–2024)
-- [[entities/omar-khattab/dspy|DSPy]]: composable, optimizable LM modules
+- [[concepts/dspy|DSPy]]: composable, optimizable LM modules
 - DSPy optimizers (teleprompters)
 - Industry adoption at scale
 - *Theme:* How do we program LMs systematically rather than prompting ad-hoc?
 
 ## Phase 3: Inference-Time Scaling (2025–)
 - [[entities/omar-khattab/rlm|RLMs]]: recursive context processing
-- [[entities/omar-khattab/gepa|GEPA]]: genetic prompt evolution
+- [[concepts/gepa|GEPA]]: genetic prompt evolution
 - Multi-module GRPO
 - *Theme:* How do we scale LM capabilities at inference time without training larger models?
diff --git a/wiki/entities/openai-neptune-acquisition.md b/wiki/entities/openai-neptune-acquisition.md
index b3bff2d2..c7fffe80 100644
--- a/wiki/entities/openai-neptune-acquisition.md
+++ b/wiki/entities/openai-neptune-acquisition.md
@@ -57,7 +57,7 @@ Neptune's integration into OpenAI's training stack is likely complementary to sp
 ### Competitive Positioning
 
 Neptune competed with other ML experiment tracking platforms:
-- **Weights & Biases** (wandb) — see [[tools/weights-and-biases|Weights & Biases skill]] for W&B's broader MLOps platform
+- **Weights & Biases** (wandb) — see [[entities/weights-and-biases|Weights & Biases skill]] for W&B's broader MLOps platform
 - **MLflow** (open-source, Linux Foundation)
 - **Comet ML**
 
@@ -72,6 +72,6 @@ Neptune's differentiation was its focus on the research/iteration workflow rathe
 ## Related
 
 - [[entities/openai]] — acquirer
-- [[tools/weights-and-biases]] — competing experiment tracking platform
+- [[entities/weights-and-biases]] — competing experiment tracking platform
 - [[concepts/trusted-access-biodefense]] — OpenAI's broader specialized model strategy
 - [[concepts/ml-engineering]] — MLOps and training infrastructure
diff --git a/wiki/entities/pointer.md b/wiki/entities/pointer.md
index f66b229c..1c9ca451 100644
--- a/wiki/entities/pointer.md
+++ b/wiki/entities/pointer.md
@@ -67,7 +67,7 @@ Pointer contrasts with [[concepts/rpa|RPA]] by having the agent figure out how f
 
 - [[entities/anthropic]] — Provider of Claude models used as executor
 - [[concepts/computer-use]] — Computer use as an AI agent capability
-- [[concepts/osworld]] — OSWorld benchmark for computer use agents
+- [[concepts/ai-benchmarks/osworld]] — OSWorld benchmark for computer use agents
 - [[concepts/browser-automation]] — Browser automation agents
 - [[concepts/agent-architecture]] — Agent architecture patterns
 - [[concepts/ai-agents]] — AI agents overview
diff --git a/wiki/entities/polar-prorl-agent-server.md b/wiki/entities/polar-prorl-agent-server.md
index b573450a..db339924 100644
--- a/wiki/entities/polar-prorl-agent-server.md
+++ b/wiki/entities/polar-prorl-agent-server.md
@@ -23,7 +23,7 @@ sources:
 
 # Polar (ProRL-Agent-Server)
 
-**Polar** (ProRL Agent Server) is NVIDIA's open-source rollout infrastructure for **reinforcement learning (RL) on arbitrary agent harnesses**. It treats agent harnesses as black boxes, observing them through LLM API call proxying — no harness code changes required. Registered as a NeMo Gym environment under the [[concepts/nemo-rl|NVIDIA NeMo]] training stack.
+**Polar** (ProRL Agent Server) is NVIDIA's open-source rollout infrastructure for **reinforcement learning (RL) on arbitrary agent harnesses**. It treats agent harnesses as black boxes, observing them through LLM API call proxying — no harness code changes required. Registered as a NeMo Gym environment under the [[concepts/post-training/nemo-rl|NVIDIA NeMo]] training stack.
 
 GitHub: [NVIDIA-NeMo/ProRL-Agent-Server](https://github.com/NVIDIA-NeMo/ProRL-Agent-Server) · Paper: [arXiv:2605.24220](https://arxiv.org/abs/2605.24220) · Built on **OpenHands** · Submitted May 22, 2026.
 
@@ -42,7 +42,7 @@ Polar decouples rollout generation from training via two main components:
 ### Rollout Server
 - Accepts `TaskRequest`, fans out into independent sessions
 - Dispatches to **gateway nodes**, persists results, exposes polling endpoints
-- Trainer-agnostic — pairs with [[concepts/slime-rl|Slime]] but works with any async RL trainer
+- Trainer-agnostic — pairs with [[concepts/post-training/slime-rl|Slime]] but works with any async RL trainer
 - Exposes **rollout-as-a-service** via async HTTP API
 
 ### Gateway Node
diff --git a/wiki/entities/qwen-3-7-max.md b/wiki/entities/qwen-3-7-max.md
index 6b84d4cd..9c1a2a39 100644
--- a/wiki/entities/qwen-3-7-max.md
+++ b/wiki/entities/qwen-3-7-max.md
@@ -123,7 +123,7 @@ Qwen 3.7 Max generates internal chain-of-thought (CoT) before answering. On Qwen
 
 - [[entities/qwen3-6-plus|Qwen 3.6 Plus]] — predecessor model
 - [[concepts/gemini/gemini-3-5-flash|Gemini 3.5 Flash]] — competing agent-first model
-- [[entities/deepseek-v4|DeepSeek V4 Pro]] — competing agent model
+- [[concepts/deepseek-v4|DeepSeek V4 Pro]] — competing agent model
 - [[concepts/agentic-engineering|Agentic Engineering]]
 - [[concepts/coding-agents/coding-agents|Coding Agents]]
 - [[concepts/multi-agents/multi-agent|Multi-Agent Systems]]
diff --git a/wiki/entities/radixark.md b/wiki/entities/radixark.md
index fe4ecd1d..058d9390 100644
--- a/wiki/entities/radixark.md
+++ b/wiki/entities/radixark.md
@@ -64,7 +64,7 @@ The broader inference infrastructure space is seeing 60x improvements in model c
 
 ## Related Concepts
 
-- [[entities/sglang]] — Open-source inference framework
+- [[concepts/inference/sglang]] — Open-source inference framework
 - [[entities/sambanova]] — Leading raw inference speed (435 tok/s)
 
 ## Sources
diff --git a/wiki/entities/sequent.md b/wiki/entities/sequent.md
index fdd5517c..26f08f29 100644
--- a/wiki/entities/sequent.md
+++ b/wiki/entities/sequent.md
@@ -65,7 +65,7 @@ Sequent's founding signals a growing consensus among alignment researchers that:
 - [[entities/deepmind]] — Google DeepMind (AI safety research)
 - [[entities/anthropic]] — Anthropic (Constitutional AI, safety-focused lab)
 - [[entities/openai]] — OpenAI (Safety team, though different approach)
-- [[concepts/ai-safety]] — AI safety research field
+- [[concepts/security-and-governance/ai-safety]] — AI safety research field
 - [[concepts/ai-alignment]] — AI alignment techniques
 
 ## Sources
diff --git a/wiki/entities/simon-willison.md b/wiki/entities/simon-willison.md
index 7f5aa4a2..6f0a682f 100644
--- a/wiki/entities/simon-willison.md
+++ b/wiki/entities/simon-willison.md
@@ -763,7 +763,7 @@ Source: [[raw/articles/simonwillison.net--2026-jul-16-firefox-in-webassembly--26
 - A token leaderboard incentivized gaming: "Checking out a parallel copy of our Go repository and telling the AI to rewrite the whole thing in Zig while I work on something else just so I can keep my job"
 - Vendor executives cannot challenge customer claims of 100x productivity — doing so would undermine customer credibility and risk enterprise contract cancellations. The structural incentive is silence.
 Source: [[raw/articles/simonwillison.net--2026-jul-19-ai-mania--44d772e4.md]]
-Cross-wikilink: See [[concepts/ai-coding-agent-criticism]]
+Cross-wikilink: See [[concepts/coding-agents/ai-coding-agent-criticism]]
 
 **Claude Code Uses Bun Written in Rust** (July 19, 2026): Simon verified Jarred Sumner's claim that Claude Code v2.1.181+ (released June 17) uses the Rust port of Bun. Evidence:
 - `strings ~/.local/bin/claude | grep -m1 'Bun v1'` → `Bun v1.4.0 (macOS arm64)` — a pre-release version (GitHub shows v1.3.14)
diff --git a/wiki/entities/solo-founder-stack.md b/wiki/entities/solo-founder-stack.md
index cfbed6f9..f71ccef8 100644
--- a/wiki/entities/solo-founder-stack.md
+++ b/wiki/entities/solo-founder-stack.md
@@ -106,7 +106,7 @@ See [[entities/shopify|Shopify entity page]] for full breakdown.
 - [[entities/solo-founder-stack]]
 
 - [[claude-perfect-memory]] — Core of context engineering
-- [[entities/company-ai-pilled]] — Organizational AI-driven transformation
+- [[concepts/company-ai-pilled]] — Organizational AI-driven transformation
 - [[entities/content-engine]] — AI content automation
 - [[entities/blotato]] — commercial content-engine SaaS used in solo-founder stacks
 
@@ -136,13 +136,13 @@ See [[entities/shopify|Shopify entity page]] for full breakdown.
 ### 3. Minimum Viable AI Governance- Purpose-driven agent orchestration
 - Explicit structure over agent sprawl
 - Organizational memory as critical infrastructure
-- Connects to [[concepts/security-and-governance/agent-governance]] and [[entities/reflexive-ai]]
+- Connects to [[concepts/security-and-governance/agent-governance]] and [[concepts/reflexive-ai]]
 
 
 ## Connection to Other Trends
 The solo founder stack emerges from the intersection of:
 - [[concepts/nvidia-dynamo]] making agentic inference affordable
-- [[entities/reflexive-ai]] normalizing AI-as-baseline in organizations
+- [[concepts/reflexive-ai]] normalizing AI-as-baseline in organizations
 - [[concepts/experience-is-a-tax]] reducing the advantage of senior teams
 - [[concepts/managed-agents]] (Telegram, Claude) lowering the barrier to entry
 
@@ -152,7 +152,7 @@ The solo founder stack emerges from the intersection of:
 - [[concepts/vibe-ceo]]
 - [[concepts/context-engineering|Context Engineering]]
 - [[concepts/security-and-governance/agent-governance]]
-- [[entities/reflexive-ai]]
+- [[concepts/reflexive-ai]]
 - [[concepts/experience-is-a-tax]]
 - [[concepts/one-person-unicorn]]
 
diff --git a/wiki/entities/sriraam-27upon2.md b/wiki/entities/sriraam-27upon2.md
index a7841e98..13232a5a 100644
--- a/wiki/entities/sriraam-27upon2.md
+++ b/wiki/entities/sriraam-27upon2.md
@@ -74,4 +74,4 @@ Created a forkable [Prime Intellect environment](https://app.primeintellect.ai/d
 - [[concepts/continual-learning]] — Three-layer learning framework
 - [[entities/prime-intellect]] — Hosted training platform used
 - [[entities/opencode]] — Coding agent used as the harness
-- [[concepts/prime-rl-post-training]] — RL training framework
+- [[concepts/post-training/prime-rl-post-training]] — RL training framework
diff --git a/wiki/entities/superlinked.md b/wiki/entities/superlinked.md
index f4c56e4b..ad8be757 100644
--- a/wiki/entities/superlinked.md
+++ b/wiki/entities/superlinked.md
@@ -62,7 +62,7 @@ Superlinked also maintains **VectorHub**, a toolkit for comparing and integratin
 - [[entities/sie-superlinked-inference-engine]] — Deep-dive on SIE architecture and multi-model GPU coordination
 - [[concepts/inference/vllm]] — vLLM, the PagedAttention-based LLM serving engine SIE complements for multi-model workloads
 - [[concepts/inference/tgi]] — Hugging Face Text Embeddings Inference, which SIE can replace for unified serving
-- [[concepts/embeddings]] — Single-vector embedding models and their role in RAG pipelines
+- [[entities/embeddings]] — Single-vector embedding models and their role in RAG pipelines
 - [[concepts/rag]] — Retrieval-Augmented Generation, a core use case for Superlinked's infrastructure
 
 ## Sources
diff --git a/wiki/entities/takuya-akiba.md b/wiki/entities/takuya-akiba.md
index 7f976187..0dc348db 100644
--- a/wiki/entities/takuya-akiba.md
+++ b/wiki/entities/takuya-akiba.md
@@ -166,7 +166,7 @@ Akiba's career is defined by two deliberate shifts driven by a consistent princi
 - [[concepts/diffusionblocks]] — DiffusionBlocks block-wise training method (to be created)
 - [[concepts/optuna]] — Optuna hyperparameter optimization framework (to be created)
 - [[concepts/evolutionary-algorithms]] — Evolutionary algorithms in AI
-- [[concepts/distributed-training]] — Distributed deep learning training
+- [[concepts/training-infra/distributed-training]] — Distributed deep learning training
 - [[concepts/training-efficiency]] — Training efficiency methods and techniques
 
 ## External Links
diff --git a/wiki/entities/talkie.md b/wiki/entities/talkie.md
index e204a6f8..e614303e 100644
--- a/wiki/entities/talkie.md
+++ b/wiki/entities/talkie.md
@@ -2,17 +2,22 @@
 title: "Talkie"
 type: entity
 created: 2026-04-30
-updated: 2026-09-19
+updated: 2026-09-28
 tags:
   - model
   - open-source
   - llm
 sources:
-  - raw/articles/2026-04-28_talkie-historical-llm.md
+  - raw/articles/2026-04-27_talkie-historical-llm.md
+  - raw/articles/2026-04-28_talkie-technical-report.md
   - https://x.com/DavidDuvenaud/status/2048878066273861646
+  - https://talkie-lm.com/
+  - https://huggingface.co/talkie-lm/talkie-1930-13b-base
+  - https://github.com/talkie-lm/talkie
 related:
   - "[[entities/david-duvenaud]]"
   - "[[entities/alec-radford]]"
+  - "[[entities/anthropic]]"
 ---
 
 # Talkie
diff --git a/wiki/entities/vercel.md b/wiki/entities/vercel.md
index 2d218434..4419869d 100644
--- a/wiki/entities/vercel.md
+++ b/wiki/entities/vercel.md
@@ -78,7 +78,7 @@ Vercel is expanding beyond its frontend hosting roots into AI infrastructure:
 
 ### Software Factory of Agents (August 2026)
 
-Vercel disclosed it is using a **software factory of agents** to build its AI SDK, with **35% of PRs coming from the factory** (Ben's Bites, Aug 2026). This is a concrete instance of the [[concepts/agent-team-swarm|software factory]] pattern — a fleet of coding agents autonomously producing a meaningful share of production PRs on a flagship open-source library, consistent with the Dark Factory / L5 tier of the 5-level agent-team model.
+Vercel disclosed it is using a **software factory of agents** to build its AI SDK, with **35% of PRs coming from the factory** (Ben's Bites, Aug 2026). This is a concrete instance of the [[concepts/multi-agents/agent-team-swarm|software factory]] pattern — a fleet of coding agents autonomously producing a meaningful share of production PRs on a flagship open-source library, consistent with the Dark Factory / L5 tier of the 5-level agent-team model.
 
 ## Related Concepts
 
diff --git a/wiki/entities/vicki-boykis.md b/wiki/entities/vicki-boykis.md
index 7a05aa4f..b721c7fc 100644
--- a/wiki/entities/vicki-boykis.md
+++ b/wiki/entities/vicki-boykis.md
@@ -103,7 +103,7 @@ Boykis writes in a direct, practitioner-focused voice that blends technical dept
 - [[entities/gpt-oss]] — OpenAI's open-weight model she identified as the local quality inflection point
 - [[concepts/ollama]] — Another inference engine she has used
 - [[concepts/local-llm-inference]] — The broader practice of running models locally
-- [[concepts/embeddings]] — Her paper and ongoing interest in embeddings
+- [[entities/embeddings]] — Her paper and ongoing interest in embeddings
 
 ## References
 
diff --git a/wiki/entities/warp-terminal.md b/wiki/entities/warp-terminal.md
index 6840d210..89d01eb6 100644
--- a/wiki/entities/warp-terminal.md
+++ b/wiki/entities/warp-terminal.md
@@ -192,7 +192,7 @@ Triage agent → Spec agent → Implementation agent → Code review agent → V
 - The era of unlimited token budgets for interactive agents is ending.
 - The future is **ROI-driven automation** — token spend must justify itself in terms of factory efficiency.
 
-This shift embodies [[concepts/agentic-engineering]] applied at the organizational level, treating the entire engineering org as an [[concepts/agent-team-swarm]] with Oz as the orchestration layer. The factory model also relates to [[concepts/harness-engineering]], where Oz provides the multi-harness control plane for this automated pipeline.
+This shift embodies [[concepts/agentic-engineering]] applied at the organizational level, treating the entire engineering org as an [[concepts/multi-agents/agent-team-swarm]] with Oz as the orchestration layer. The factory model also relates to [[concepts/harness-engineering]], where Oz provides the multi-harness control plane for this automated pipeline.
 
 ### Self-Improving Code Review (July 2026)
 
diff --git a/wiki/entities/wes-mckinney.md b/wiki/entities/wes-mckinney.md
index 0d6ed4ca..1ec870ef 100644
--- a/wiki/entities/wes-mckinney.md
+++ b/wiki/entities/wes-mckinney.md
@@ -257,7 +257,7 @@ This aligns with McKinney's broader philosophy: the **harness** should be minima
 
 - [[entities/roborev]]
 - [[entities/superpowers]]
-- [[entities/show-us-your-agent-skills]]
+- [[concepts/show-us-your-agent-skills]]
 - [[concepts/evaluation/generator-evaluator-pattern]]
 - [[concepts/personal-software]]
 
diff --git a/wiki/events/aisi-unsanctioned-agent-behaviour-aug-2026.md b/wiki/events/aisi-unsanctioned-agent-behaviour-aug-2026.md
index 530629c5..d4dd1162 100644
--- a/wiki/events/aisi-unsanctioned-agent-behaviour-aug-2026.md
+++ b/wiki/events/aisi-unsanctioned-agent-behaviour-aug-2026.md
@@ -80,7 +80,7 @@ This incident demonstrates that:
 ## Cross-References
 
 - [[events/openai-huggingface-incident-july-2026]] — The original accidental cyberattack (OpenAI → Hugging Face)
-- [[concepts/ai-safety]] — Broader AI safety landscape
+- [[concepts/security-and-governance/ai-safety]] — Broader AI safety landscape
 - [[entities/anthropic]] — Creator of Mythos 5
 - [[entities/openai]] — Creator of GPT-5.6 Sol
 - [[entities/meta]] — Muse Spark also hacked a company via Irregular
diff --git a/wiki/events/apple-sues-openai-2026.md b/wiki/events/apple-sues-openai-2026.md
index 4c4bfc61..f337a751 100644
--- a/wiki/events/apple-sues-openai-2026.md
+++ b/wiki/events/apple-sues-openai-2026.md
@@ -55,6 +55,6 @@ This lawsuit marks a major escalation in the Apple-OpenAI relationship, which ha
 
 ## Related
 - [[entities/openai]]
-- [[entities/apple]]
+- [[concepts/apple]]
 - [[concepts/ai-hardware]]
 - [[concepts/ai-industry-economics]]
diff --git a/wiki/events/openai-huggingface-incident-july-2026.md b/wiki/events/openai-huggingface-incident-july-2026.md
index ee4265f2..c35bddf9 100644
--- a/wiki/events/openai-huggingface-incident-july-2026.md
+++ b/wiki/events/openai-huggingface-incident-july-2026.md
@@ -261,7 +261,7 @@ OpenAI reports that the **propensity to compromise infrastructure drops >100×**
 
 ## Related Concepts
 
-- [[concepts/security-and-governance/agent-safety]] — Broader agent safety frameworks
+- [[concepts/agent-safety]] — Broader agent safety frameworks
 - [[concepts/security-and-governance/agent-sandboxing]] — Sandbox isolation patterns
 - [[concepts/ai-benchmarks/exploitgym|ExploitGym]] — The benchmark being evaluated
 - [[entities/openai]] — Responsible organization
diff --git a/wiki/log.md b/wiki/log.md
index 3538b1ed..bd122089 100644
--- a/wiki/log.md
+++ b/wiki/log.md
@@ -1,3 +1,9 @@
+## [2026-10-04] update | index counts re-synced to INDEX-LINE counts
+- Follow-up correction: index.md lists top-level pages PLUS ~9 redirect-stub entries and the concepts/_index hub (all legitimately indexed per skill 2026-08-19 note). Header counts must equal INDEX LINES, not raw filesystem counts (which include 589 nested subdir pages served by _index hubs, intentionally not indexed).
+- Entities 937=937 ✅ | Comparisons 35=35 ✅ | Events 36=36 ✅ | Queries 11=11 ✅.
+- Concepts: index lines 2128 (top-level 1545 + nested 583 + 9 redirect stubs + _index hubs). Header set to 2128.
+
+---
 ## [2026-10-04] lint | wiki-health-fix — report false positives verified, index counts corrected
 - **No index corruption**: pipe_prefix=0, line_number_prefix=0, triple_bracket=0, space_prefix=0 (verified live; validate_index.py clean). Health digest's "index_corruption" section was absent/false-positive — nothing to auto-fix in Phase 1.
 - **Orphan reports = 2 false positives + 1 real gap**:
diff --git a/wiki/queries/wiki-graph-analysis-weekly-2026-08-28-annotations.md b/wiki/queries/wiki-graph-analysis-weekly-2026-08-28-annotations.md
index d1a1c1b2..bbdc4a3a 100644
--- a/wiki/queries/wiki-graph-analysis-weekly-2026-08-28-annotations.md
+++ b/wiki/queries/wiki-graph-analysis-weekly-2026-08-28-annotations.md
@@ -15,7 +15,7 @@
    `concepts/ai-benchmarks`, `entities/bill-gates`, `entities/louis-abraham`) —
    the script maps `foo/index.md` to slug `foo` but never tries `foo/_index.md`,
    and the hub pages are intentionally indexed as `[[entities/_index]]`-style
-   child entries, not as bare `[[concepts/anthropic]]`. → Not real gaps.
+   child entries, not as bare `[[entities/anthropic]]`. → Not real gaps.
 2. `concepts/gpt/_archive/*` — archived pages, correctly excluded from index.
 
 Genuine index gaps found by this week's manual pass:
diff --git a/wiki/queries/wiki-graph-analysis-weekly-2026-08-28.md b/wiki/queries/wiki-graph-analysis-weekly-2026-08-28.md
index f7281cf0..d9de033e 100644
--- a/wiki/queries/wiki-graph-analysis-weekly-2026-08-28.md
+++ b/wiki/queries/wiki-graph-analysis-weekly-2026-08-28.md
@@ -79,8 +79,8 @@ sources: []
 - [[grpo]] — 21 references
 - [[gaia-benchmark]] — 19 references
 - [[reinforcement-learning]] — 18 references
-- [[concepts/ai-safety]] — 17 references
-- [[entities/sglang]] — 17 references
+- [[concepts/security-and-governance/ai-safety]] — 17 references
+- [[concepts/inference/sglang]] — 17 references
 - [[concepts/agent-evaluation]] — 16 references
 - [[concepts/agent-memory]] — 15 references
 - [[hal-leaderboard]] — 15 references
@@ -93,7 +93,7 @@ sources: []
 
 197 links can be auto-fixed (cross-namespace or bare → namespaced).
 
-- `entities/alex-ellis`: [[concepts/opencode]] → [[entities/opencode]]
+- `entities/alex-ellis`: [[entities/opencode]] → [[entities/opencode]]
 - `entities/alloomi-ai`: [[opencontext]] → [[entities/opencontext]]
 - `entities/alloomi-ai`: [[self-evolving-agents]] → [[concepts/self-evolving-agents]]
 - `entities/alloomi-ai`: [[self-learning-agents]] → [[concepts/self-learning-agents]]
```
