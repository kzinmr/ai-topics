## [2026-05-04] Accelerate — Distributed training launcher + DeepSpeed concept page

- **[[concepts/accelerate]]** — Created concept page: Hugging Face Accelerate as unified distributed training abstraction. FSDP vs DeepSpeed configuration mapping (6 dimensions), memory/precision differences (fp32 upcast), plugin system (FullyShardedDataParallelPlugin, DeepSpeedPlugin), decision guide.
- **[[concepts/deepspeed]]** — Created concept page: Microsoft DeepSpeed (ZeRO 1/2/3/3-offload/Infinity, 3D-Parallelism, MoE, NVMe offload). Notable models (BLOOM, MT-530B, GPT-NeoX). Accelerate integration mapping. Fills existing wikilink from pytorch-fsdp.
- **[[concepts/pytorch-fsdp]]** — Enriched: Added Accelerate cross-reference to Related Concepts.
- **raw/articles/2026-05-04_accelerate-fsdp-deepspeed-guide.md** — Saved raw article
- Updated: wiki/index.md (+2 concepts, 808 pages, 417 concepts), wiki/log.md
- Sources: hf.co/docs/accelerate, pytorch.org FSDP2 tutorial, deepspeed.ai

## [2026-05-04] Mobius Labs entity page — Dropbox acquisition, HQQ, Aana, low-bit inference

- **[[entities/mobius-labs]]** — Created entity page: AI research company (HQQ quantization, GemLite Triton kernels, Aana multimodal SDK). Acquired by Dropbox ~2025, powers Dash multimodal search. Covers FSDP/QLoRA collaboration (Answer.AI, Tim Dettmers), FP4 quality recovery, metadata offloading, low-bit inference survey. 3 raw articles ingested.
- **raw/articles/2025_mobius-labs-blog-summary.md** — Saved raw article
- **raw/articles/2025-05-04_dropbox-mobius-labs-aana-integration.md** — Saved raw article
- **raw/articles/2026-05-04_dropbox-low-bit-inference.md** — Saved raw article
- Updated: wiki/index.md (+1 entity, 806 pages), wiki/log.md
- Sources: blog.mobiuslabs.com, dropbox.tech

## [2026-05-04] vLLM spec-decode blog — Speculative decoding wiki enrichment

- **[[concepts/speculative-decoding]]** — Enriched: Added vLLM Implementation section (3 supported methods: Draft Model, Prompt Lookup/N-gram, Medusa/Eagle/MLPSpeculator), code examples, critical QPS sensitivity insight (2.8x speedup at low QPS, 1.4-1.8x slowdown at high QPS), Dynamic Speculative Decoding roadmap. Sources updated.
- **[[concepts/inference/vllm]]** — Enriched: Added Speculative Decoding in vLLM section with methods table and configuration examples, linking to full concept page.
- **raw/articles/2025-10-09_vllm-speculative-decoding-blog.md** — Saved raw article
- Updated: wiki/log.md
- Source: https://vllm.ai/blog/spec-decode

## [2026-05-04] Answer.AI benchmarks — FSDP+Q-LoRA performance enrichment

- **[[concepts/fsdp-qlora]]** — Enriched: Added Answer.AI official benchmarks table (Llama-2 70B, 5 hardware tiers, $2-5 cost range), hardware bottleneck analysis (PCIe/NVLink, CPU RAM saturation), progressive optimization guide (6-step DDP→Activation Offload), DDP vs FSDP decision rule.
- **[[concepts/pytorch-fsdp]]** — Enriched: Added DDP vs FSDP decision guidance, progressive optimization strategy table (6 memory-saving steps), sources updated with Answer.AI benchmarks.
- **[[concepts/qlora]]** — Enriched: Added speed advantage insight (QLoRA can be faster than LoRA via larger batch sizes), CPU offloading performance paradox.
- **raw/articles/2024-03_answerai-fsdp-qlora-benchmarks.md** — Saved raw article
- Updated: wiki/log.md
- Source: https://github.com/AnswerDotAI/fsdp_qlora/blob/main/benchmarks_03_2024.md

## [2026-05-04] Phil Schmid FSDP+Q-LoRA guide — Full wiki ingest (4 pages)

- **[[entities/phil-schmid]]** — Created entity page: Philipp (Phil) Schmid, Staff Engineer (AI DevX/DevRel) at Google DeepMind, ex-Hugging Face Technical Lead. Key contributions: FSDP+Q-LoRA, Inference Endpoints, Zephyr/SmolLM/StarCoder partnerships, revenue $0→$100M.
- **[[concepts/pytorch-fsdp]]** — Created top-level concept page: PyTorch FSDP (Fully Sharded Data Parallel) with ZeRO-3 sharding, CPU offloading, memory tradeoffs for Llama 3 70B, HF ecosystem integration, DeepSpeed comparison. Existing fine-tuning/pytorch-fsdp.md updated to redirect.
- **[[concepts/qlora]]** — Created concept page: Q-LoRA (Quantized Low-Rank Adaptation). Covers NF4, Double Quantization, Paged Optimizers, architecture diagram, memory comparison (70B ~36GB VRAM).
- **[[concepts/fsdp-qlora]]** — Created concept page: FSDP+Q-LoRA combined training technique (Answer.AI × Tim Dettmers × HF). Memory scaling table, cost analysis ($255 for 70B 3-epoch on 4× A10G), implementation config, comparison with alternatives.
- **raw/articles/2026-05-04_phil-schmid-fsdp-qlora-llama3.md** — Saved raw article
- Updated: wiki/index.md (+4 pages, 801→805), wiki/log.md
- Source: https://www.philschmid.de/fsdp-qlora-llama3

## [2026-05-04] Jay Mody blog — Full wiki ingest (5 articles)

- **[[entities/jay-mody]]** — Created entity page: Educator known for picoGPT (GPT-2 in 60 lines of NumPy), speculative sampling tutorial, and clear LLM internals explanations. 5 articles ingested.
- **[[concepts/speculative-decoding]]** — Enriched: added Gentle Introduction section with Jay Mody's tutorial (2.23x speedup), aliases, cross-reference to jay-mody entity. Added raw/article source.
- **[[concepts/attention-mechanism-variants]]** — Enriched: added Educational Derivations section with Jay Mody's first-principles derivation of scaled dot-product attention. Added alias `scaled-dot-product-attention`.
- **raw/articles/2023-02-08_jaymody-speculative-sampling.md** — Saved raw article
- **raw/articles/2023-01-30_jaymody-picoGPT.md** — Saved raw article
- **raw/articles/2022-12-15_jaymody-stable-softmax.md** — Saved raw article
- **raw/articles/2022-10-22_jaymody-attention-intuition.md** — Saved raw article
- **raw/articles/2021-04-04_jaymody-distance-matrices.md** — Saved raw article
- Updated: wiki/index.md (entity entry), wiki/log.md
- Source: https://jaykmody.com/

## [2026-05-04] Thorsten Ball Joy & Curiosity #84 — Newsletter ingest

- **[[entities/mitchell-hashimoto]]** — Created entity page: HashiCorp co-founder, Ghostty creator. Index entry enriched from stub to full (left GitHub 2026 over AI agent instability).
- **[[entities/thorsten-ball]]** — Created entity page: Author of Writing An Interpreter/Compiler In Go, Register Spill newsletter, Sourcegraph engineer.
- **[[entities/zed]]** — Created entity page: High-performance Rust editor by former Atom team. Reached 1.0 (Apr 29, 2026). AI-native with parallel agent orchestration.
- **[[entities/mistral-ai]]** — Created entity page: French AI company, €12B valuation, $400M+ ARR, "smaller, cheaper, not American" strategy.
- **raw/articles/2026-05-04_thorsten-ball-joy-and-curiosity-84.md** — Saved raw article
- Updated: wiki/index.md (801 pages, 389 entities), wiki/log.md
- Source: [Joy & Curiosity #84 - Register Spill](https://registerspill.thorstenball.com/p/joy-and-curiosity-84)

## [2026-05-04] Modelcrafting — Letting AI Posttrain AI

- **[[concepts/modelcrafting]]** — Created concept page: paradigm of AI agents autonomously shaping and improving other AI models. Covers research intuition gap, 6 failure modes (naive SFT, no sanity checks, no curriculum learning, eval contamination, commitment bias, spend inefficiency), tokenizer workaround case study.
- **[[entities/thoughtful-lab]]** — Created entity page: AI research lab behind the "Letting AI Posttrain AI" experiment (Apr 2026). Tested Claude 4.6 Opus and GPT-5.4 on autonomous post-training of Qwen3-8B for the Frog Placement Game.
- **[[concepts/post-training]]** — Enriched from stub to full page: added overview, key techniques table, automated post-training research section (Thoughtful Lab experiment), known challenges section, and cross-references.
- **raw/articles/2026-04_thoughtfullab-letting-ai-posttrain-ai.md** — Saved raw article
- Updated: wiki/index.md (800 total pages), wiki/entities/_index.md, wiki/log.md
- Source: [Letting AI Posttrain AI - Thoughtful Lab](https://www.thoughtfullab.com/letting-ai-posttrain-ai.html)

## [2026-05-04] MGH Validation: LongCoT Experiment — Zhang's RLM LongCoT article ingested

- **[[concepts/mismanaged-geniuses-hypothesis]]** — Added "Empirical Validation: LongCoT Experiment" section: GPT-5.2 + RLM + Claude Code trajectory tips = 65.6% on LongCoT-mini (baseline 38.7%). Three failure modes identified (brute-force, verification gaps, prompting gaps). Ablation proves RLM mechanism is essential.
- **[[concepts/rlm-recursive-language-models]]** — Added "MGH Validation: Zhang's Direct LongCoT RLM Experiment" section with results table (65.6% total, >70% with partial rewards) and identified failure modes.
- **[[entities/alex-zhang]]** — Added Apr 2026 LongCoT blog post to Blog Posts table; added "Proof (prompt-level steering)" bullet to MGH section.
- **[[entities/omar-khattab/rlm]]** — Added LongCoT-mini result (65.6%) to benchmark list.
- **raw/articles/2026-04-26_alex-zhang-longcot-rlm-mgh.md** — Saved raw article: Alex Zhang's direct application of MGH to LongCoT via RLM + Claude Code trajectory analysis.
- Source: https://alexzhang13.github.io/blog/2026/longcot-rlm/

## [2026-05-04] Multi-Teacher On-Policy Distillation (MOPD) — New concept from Notion article

- **[[concepts/multi-teacher-on-policy-distillation]]** — Created concept page: MOPD is a post-training primitive that solves the see-saw problem via reverse KL distillation from multiple teachers within a GRPO-like loop. Covers IcePop, full-vocabulary distillation, WAL-based fault-tolerant rollouts, and comparisons across MiMo-V2-Flash, GLM-5, Nemotron-Cascade 2, and DeepSeek-V4.
- **[[concepts/model-distillation]]** — Updated Related Pages with cross-link to MOPD
- **[[concepts/grpo-rl-training]]** — Updated Related Pages with cross-link to MOPD
- **raw/articles/2026-05-04_multi-teacher-on-policy-distillation.md** — Saved raw article
- Updated: wiki/index.md (799 total pages, concepts: 415), wiki/log.md
- Source: Notion (yumoxu)

## [2026-05-04] Paper Ingest — RPG (Regularized Policy Gradient) for KL-Regularized PG Framework

- **[[concepts/rpg-regularized-policy-gradient]]** — Created concept page: RPG framework unifies KL-regularized policy gradient algorithms for LLM reasoning (Zhang et al., ICLR 2026). Identifies GRPO importance-weighting mismatch and proposes RPG-REINFORCE with RPG-Style Clip. AIME24/25: **+6pp over DAPO**. AIME25 (8K): 52% — surpasses Qwen3-4B-Instruct (47%).
- **[[concepts/fine-tuning/grpo-rl-training]]** — Updated See Also section with cross-link to RPG page noting the KL mismatch correction.
- **raw/papers/2025-05-19_2505.17508_kl-regularized-policy-gradient-rpg.md** — Raw paper saved.
- **Source:** arXiv:2505.17508, ICLR 2026
- Updated: wiki/index.md (+1 concept), wiki/log.md

## [2026-05-04] Active Crawl — Pentagon AI Deals, Agentic AI Governance, MIT-IBM Computing Lab

- **[[entities/anthropic]]** — Added Pentagon Blacklisting section: supply chain risk designation (Feb 2026), Mythos exception, $900B valuation target, lawsuits, May 2026 exclusion from 7-company deals.
- **[[concepts/ai-military]]** — Expanded with Pentagon AI Deals section: 7 companies (SpaceX, OpenAI, Google, Nvidia, Microsoft, AWS, Reflection) signed for classified IL6/IL7 military AI work, "any lawful use" clause, Anthropic excluded.
- **[[entities/reflection-ai]]** — Created entity page: 2-year-old startup (former DeepMind researchers), seeking $25B valuation, backed by Nvidia and 1789 Capital. Pentagon defense partner. No public model yet.
- **[[concepts/agentic-ai-governance]]** — Created concept page: Yale CELI framework (May 2026), three-tiered guardrails, HITL/HOTL patterns, ISO/IEC 42001, excessive agency risk, indirect prompt injection.
- **[[entities/mit-ibm-computing-research-lab]]** — Created entity page: IBM+MIT joint lab (Apr 2026), AI + algorithms + quantum computing convergence, 2029 fault-tolerant quantum roadmap, 3 research pillars.
- **raw/articles/** — 3 new raw articles saved: pentagon-seven-ai-deals-anthropic-excluded, yale-celi-agentic-ai-governance-framework, mit-ibm-computing-research-lab-launch
- Updated: wiki/index.md (798 total pages, +3 new entries), wiki/log.md
- Sources: The Guardian, CNBC, Reuters, IBM Newsroom, MIT News, Fortune/EWSolutions

## [2026-05-04] Newsletter Ingest — The Signal: Anthropic Creative Coalition, Claude Security, OpenAI AWS Bedrock, Google Gemini updates

- Source: The Signal newsletter "Gemini Gets to Work, Claude's Big Pull, and OpenAI Unchained" (2026-05-03)
- **[[entities/anthropic]]** — Added Creative Coalition (9 connectors: Adobe CC, Blender, Autodesk Fusion, Ableton, etc.), Claude Security public beta (Opus 4.7, vulnerability scanning with 271 Firefox zero-days), Market Position (40% enterprise LLM spend, $30B ARR, Oct 2026 IPO)
- **[[entities/openai]]** — Added AWS Bedrock integration (GPT-5.5, Codex, Managed Agents on Bedrock, limited preview), Economics comparison table ($25B ARR, IPO delayed to 2027, compute commitments walked back to $600B)
- **[[entities/claude-mythos]]** — Updated Firefox zero-day data: 271 vulnerabilities discovered in single sweep (~4× Mozilla 2025 total)
- **[[entities/google]]** — Updated with Gemini file generation (Docs/Sheets/Slides/PDF), AI compute dominance stats (25% of global AI compute, 3.8M TPUs + 1.3M GPUs), 7-9 month model velocity gap estimate
- raw/articles/ — 3 new raw articles saved: anthropic-claude-creative-coalition, anthropic-claude-security-public-beta, openai-aws-bedrock-partnership

## [2026-05-04] Blog Ingest — 18 articles collected, 3 entity pages created/updated, anti-sycophancy concept enriched

- **[[concepts/anti-sycophancy]]** — Enriched with Anthropic's May 2026 sycophancy metrics: 9% overall, but 38% in spirituality conversations and 25% in relationships. Shows domain-specific vulnerability in RLHF-trained models. Source: [Simon Willison on Anthropic's research summary](https://simonwillison.net/2026/May/3/anthropic/).
- **[[entities/gary-marcus]]** — Updated with May 2026 healthcare thesis: "Have LLMs improved patient outcomes?" — aligned with Eric Topol and Nature Medicine editorial finding no evidence of patient outcome improvement beyond admin tasks. Source: [garymarcus.substack.com](https://garymarcus.substack.com/p/have-llms-improved-patient-outcomes).
- **[[entities/george-hotz]]** — Updated with May 2026 "Punk, or why I don't stream anymore" essay: critique of AI-mediated culture, wireheading, and the "information war" on inner reality. Source: [geohot.github.io](https://geohot.github.io//blog/jekyll/update/2026/05/03/punk-or-why-i-dont-stream.html).
- **[[entities/martin-alderson]]** — Enriched with "29th August 2026: a scenario" — fictional narrative illustrating CopyFail (CVE-2026-31431) kernel bug, cloud centralization risk, and democratization of sophisticated attacks.
- **[[entities/matklad]]** — New Zig 0.16 error context patterns (errdefer + telescopic context) article collected.
- **[[entities/jim-nielsen]]** — "Lots of Little HTML Pages" (LLMS) post-mortem: building websites with HTML/CSS view transitions instead of JS-heavy SPAs.
- raw/articles/ — 18 articles saved from blog ingestion cycle

## [2026-05-03] X Account Scan — Megadocs Synthetic Data Paper + Error Report

- **[[concepts/synthetic-data]]** — Enriched from stub to comprehensive: Megadocs technique (stitching/stretching for 1.80× data efficiency), synthetic rephrasing baseline (1.48×), distributional shift paradox, pre-training best practices. Source: Kim et al. "Data-efficient pre-training by scaling synthetic megadocs" (arXiv:2603.18534, March 2026), shared by @Grad62304977.
- **raw/articles/2026-03-19_megadocs-synthetic-pretraining.md** — Saved paper summary
- **Infrastructure Alert:** 66/79 tracked X accounts had user_id resolution failures — investigation needed

## [2026-05-03] Daily Skeleton Enrichment — Sebastián Ramírez, Adam Rosenthal

- **[[entities/sebastian-ramirez]]** — Enriched from stub to comprehensive entity: creator of FastAPI, Typer, SQLModel, Asyncer. Added biography (homeschooled in Colombia, self-taught, cancer survivor), career timeline, project list with GitHub stars, philosophy, Sequoia Open Source Fellowship.
- **[[entities/adam-rosenthal]]** — Researched but could not positively identify in AI/developer ecosystem context. Multiple individuals with this name exist but none match the wiki's domain. Set to `status: needs-identification`.

## [2026-05-03] Trending Topics — NIST CAISI Evaluation, CISA AI Cyber Deadline, Boston Dynamics Exodus, Gary Marcus

- **[[entities/deepseek]]** — Updated with NIST CAISI evaluation section: +8 month capability lag vs US frontier, suspected benchmark contamination, cost efficiency confirmed. Added CAISI evaluation results table and verification under "Independent Evaluation" heading.
- **[[entities/gary-marcus]]** — Enriched from stub to comprehensive entity: cognitive scientist, LLM consciousness skepticism, Gullibility Gap concept, Dawkins critique. Added publications, quotes, cross-references.
- **raw/articles/2026-05-01_nist-caisi-deepseek-v4-evaluation.md** — Saved NIST CAISI full report
- **raw/articles/2026-05-01_cisa-ai-powered-hacking-patch-deadline.md** — Saved Reuters exclusive: CISA considers 3-day patching deadline
- **raw/articles/2026-05-01_boston-dynamics-c-suite-exodus.md** — Saved Semafor exclusive: CEO/COO/CSO/CTO departures
- **inbox/rss-scans/daily-scan-2026-05-03.md** — Saved daily trending topics report (7 topics)
- **Trending topics identified (top 5):** ① NIST CAISI DeepSeek V4 evaluation (8-month gap, benchmark contamination) ② CISA 3-day patch deadline (AI-powered hacking by Mythos/GPT-5.4-Cyber) ③ DeepSeek V4 + Huawei Ascend 950 supply crunch (ByteDance/Tencent/Alibaba scramble) ④ Boston Dynamics C-suite exodus (Hyundai pressure for humanoid scale) ⑤ Dawkins vs Marcus LLM consciousness debate
- Updated: wiki/index.md (Gary Marcus description enriched), wiki/log.md

## [2026-05-03] Active Crawl — Microsoft Agent 365, Amazon Bedrock AgentCore, Grok Imagine, NVIDIA B300 China Pricing

- **[[concepts/microsoft-agent-365]]** — Created concept page for Microsoft's enterprise AI agent governance control plane. Launched May 1, 2026 at $15/user/month. Manages agents across Foundry, Copilot Studio, and third-party platforms. Key differentiator: security & oversight layer vs. AI feature integration (Wave 3).
- **[[entities/amazon-bedrock-agentcore]]** — Created entity page for AWS's fully-managed agentic AI platform. Framework-agnostic, composable services (Memory, Gateway, Browser Runtime, Code Interpreter). 8-hour long-running workloads, VPC isolation, pay-for-what-you-use. Enterprise case studies: Epsilon, Amazon Devices, Ericsson, Thomson Reuters.
- **[[entities/grok-imagine]]** — Created entity page for xAI's video generation platform. 1.245B videos in first 30 days. DesignArena #1 (Elo 1,329). 6 generation modes, 720p, 30s max. $4.20/min — 7x cheaper than Sora 2 Pro.
- **[[entities/china-ai-industry]]** — Enriched with new "Hardware Supply Crisis" section: NVIDIA B300 servers at $1M in China ($550K in US). Driven by US export controls, Supermicro co-founder arrest, MATCH Act. Split market dynamics. Updated frontmatter.
- **raw/articles/2026-05-03_microsoft-agent-365-launch.md** — Saved raw article
- **raw/articles/2026-05-03_amazon-bedrock-agentcore.md** — Saved raw article
- **raw/articles/2026-05-03_nvidia-b300-china-1m-pricing.md** — Saved raw article
- **raw/articles/2026-05-03_grok-imagine-video-generation.md** — Saved raw article
- Updated: wiki/index.md (3 new entries → 795 total pages), wiki/log.md
- Sources: AllInOneAICenter, AWS Official Docs, Reuters (Exclusive Apr 30), blog.mean.ceo, TNW

## [2026-05-03] Newsletter Wiki Ingest — Superintel+ V4 Newsletter: DeepSeek V4 + Huawei Ascend 950

- **[[entities/deepseek]]** — Major expansion: Added V4 model series table (Pro 1.6T/49B active, Flash 284B/13B active, 1M context MoE). Added pricing comparison, efficiency gains (27% FLOPs/10% KV cache vs V3.2 for Pro). Added Huawei Ascend 950 deployment section: SMIC quadruple-patterning, chip utilization 60%→85%, EUV prototype rumors. Updated strategy and market impact sections. 2→8 cross-references.
- **raw/articles/2026-05-02-superintel-nvidia-blackwell-vs-huawei-ascend-deepseek-v4.md** — Saved raw article (paywalled, preview only)
- Source: Superintel+ newsletter via beehiiv (getsuperintel.com), Kim "Chubby" Isenberg, May 2 2026. Cross-referenced with Simon Willison's V4 coverage (Apr 24 2026).

## [2026-05-03] Karpathy — Vibe Coding MenuGen Post-mortem

- **[[entities/karpathy-writings]]** — Expanded "Vibe coding MenuGen" entry: 80/20 trap, API hallucination issues (OpenAI OCR, Replicate), Vercel/Clerk/Stripe deployment hurdles, LLM gaslighting, four demands for vibe coding era
- **[[entities/karpathy-ideas]]** — Added MenuGen post-mortem insights section to Vibe Coding entry: IKEA Future metaphor, Batteries-Included Platform vision, LLM-Friendly Design principle, Apps as Prompts thesis
- **[[concepts/harness-engineering/agentic-workflows/vibe-coding]]** — Added Karpathy MenuGen as the original vibe coding case study, with post-mortem insight table and four demands
- **raw/articles/2025-04-27_karpathy-vibe-coding-menugen.md** — Saved raw article
- Source: https://karpathy.bearblog.dev/vibe-coding-menugen/

## [2026-05-03] Daniel Miessler — "The Most Important Ideas in AI Right Now"

- **[[entities/daniel-miessler]]** — Created entity page for Daniel Miessler. Cybersecurity/AI engineer, founder of Unsupervised Learning. Creator of Fabric AI Framework (30K+ stars), SecLists, PAI, TELOS. Former Apple (BI Security), HP (co-founded Fortify on Demand). Author of Human 3.0 philosophy.
- **[[concepts/autonomous-component-optimization]]** — Created concept page. Miessler's generalization of Karpathy's Autoresearch to any workflow: the Universal Improvement Cycle (Map→Execute→Log→Collect→Optimize→Update).
- **[[concepts/intent-based-engineering]]** — Created concept page. Identifies the "articulation gap" as the new bottleneck: engineering shifts from "how to build" to "how to describe what good looks like."
- **[[concepts/agentic-scaffolding]]** — Enriched with "The Scaffolding Ratio" section: Miessler's thesis that 75–99% of knowledge work is overhead/scaffolding.
- **[[concepts/karpathy-loop]]** — Enriched with "Generalization: Autonomous Component Optimization" section.
- **raw/articles/2026-04_daniel-miessler_most-important-ideas-in-ai.md** — Saved raw article.
- Source: https://danielmiessler.com/blog/the-most-important-ideas-in-ai

## [2026-05-03] Claw Code — Open-Source AI Coding Agent Harness (Claude Code Clean-Room Reimplementation)

- **[[concepts/claw-code]]** — Created concept page for Claw Code, the open-source clean-room Rust/Python reimplementation of Claude Code's agent harness architecture. Created by [[sigrid-jin]] after Anthropic's March 31, 2026 source code leak. Fastest repo in GitHub history to surpass 100K stars (~24 hours). Covers: dual-language architecture (Rust 72.9% / Python 27.1%), 11+ Rust crates, 19 built-in permission-gated tools, three-part meta-system (OmX/clawhip/OmO), comparison with Claude Code and OpenClaw, the autonomous development thesis, roadmap (deterministic state machines, LaneEvents), and known gaps.
- **[[entities/sigrid-jin]]** — Created entity page for Sigrid Jin (@realsigridjin), creator of claw-code. Korean-Canadian, UBC. Featured in WSJ for 25B Claude Code tokens. Built initial Python port in hours with 1 human helper + 10 OpenClaw instances.
- **[[entities/yeachan-heo]]** — Created entity page for Yeachan Heo (@bellman_ych), creator of oh-my-codex (OmX), oh-my-claudecode (OMC), clawhip. Algorithmic trader in Seoul. Primary collaborator on claw-code Rust implementation.
- **[[entities/ultraworkers]]** — Created entity page for UltraWorkers GitHub organization, canonical home of the claw-code Rust implementation.
- **raw/articles/2026-05-03_claw-code-overview.md** — Saved raw article with full details.
- Updated: wiki/index.md (4 new entries → 789 total pages), wiki/log.md

## [2026-05-03] Knowledge Shields — Systems Understanding Methodology from Entropic Thoughts

- **[[concepts/knowledge-shields]]** — Created concept page capturing Chris (Entropic Thoughts)'s unified methodology for understanding complex systems. Covers: the hypothesis-invalidation loop, mental model diagnosis through observation, self-verification skills (alternative approaches, feasibility checks, recursive verification), knowledge shields (strongly held wrong beliefs resist correction), productive vs. unproductive error classification, and motivation management. Includes connections to AI agent debugging, eval design, and prompt engineering. Sources: entropicthoughts.com/understanding-systems.
- **[[entities/entropicthoughts-com]]** — Added wikilink to knowledge-shields concept in Related section; added Understanding Systems to Timeline.
- Raw article already saved: raw/articles/entropicthoughts.com--understanding-systems--149e6399.md.
- Source: https://entropicthoughts.com/understanding-systems

## [2026-05-03] Raindrop — AI Agent Monitoring Platform

- **[[concepts/raindrop]]** — Created concept page for Raindrop, "Sentry for AI Agents" monitoring platform. Covers: Trajectories (agent-native trace viz), Signals (7 default + custom classifiers), Deep Search (natural language over traces), Experiments (A/B testing), Agent Self Diagnostics. Includes detailed comparison tables with Braintrust/LangSmith/Arize/Langfuse/Logfire and cross-category comparison with OpenAI Symphony (monitoring vs orchestration layers). Sources: raindrop.ai docs, blog posts (seed round, trajectories, agent self diagnostics), PRNewswire.
- **raw/articles/2026-05-03_raindrop-introduction.md** — Saved raw article with full detail.
- Source: https://www.raindrop.ai/docs/introduction

## [2026-05-03] ByteRover — Portable File-Based Memory Layer for Coding Agents

- **[[entities/byterover]]** — Created entity page for ByteRover (formerly Cipher). Portable, file-based memory layer for autonomous coding agents with market-best 92-96% retrieval accuracy on LoCoMo/LongMemEval. Built in TypeScript by campfirein (Vietnam). Architecture: replaces vector DBs with LLM-curated Hierarchical Context Tree of Markdown files with Adaptive Knowledge Lifecycle (AKL) and 5-tier progressive retrieval. Open source (Elastic 2.0), 4.2k+ GitHub stars. Native plugins for Hermes Agent, Claude Code, OpenClaw. arXiv:2604.01599.
- **[[entities/andy-nguyen]]** — Created entity page for Duy Anh "Andy" Nguyen (@kevinnguyendn), Founder & CEO of ByteRover. Based in Da Nang, Vietnam. Former ML Engineer at OpenLab JSC.
- **raw/articles/2026-05-03_ByteRover-overview.md** — Saved raw article from homepage + GitHub + arXiv paper.
- Source: https://www.byterover.dev/blog, https://github.com/campfirein/byterover-cli, https://arxiv.org/abs/2604.01599

## [2026-05-03] Minimal Coding Agent — Thorsten Ball's "Emperor Has No Clothes" Guide

- **[[concepts/minimal-coding-agent]]** — Created concept page for the minimal code-editing agent pattern: ~400 lines of Go, 3 tools (read_file/list_files/edit_file via string replacement), heartbeat loop. Thorsten Ball's thesis: the agent loop itself has no moat; differentiation comes from UI/UX, system prompts, error handling.
- **[[entities/thorsten-ball]]** — Created entity page for Thorsten Ball. Software engineer at Sourcegraph (Amp), author of Writing An Interpreter In Go / Writing A Compiler In Go, writes Register Spill newsletter.
- **[[concepts/agent-loop-orchestration]]** — Added [[concepts/minimal-coding-agent]] as a concrete Go implementation reference.
- **[[concepts/harness-engineering/system-architecture/building-effective-agents]]** — Added [[concepts/minimal-coding-agent]] as a concrete implementation of Anthropic's "simple composable patterns" principle.
- **raw/articles/2025-04-15_ampcode-how-to-build-a-code-editing-agent.md** — Saved raw article.
- Source: https://ampcode.com/notes/how-to-build-an-agent

## [2026-05-02] OpenRouter State of AI 2025 — 100T Token LLM Usage Study

- **[[concepts/openrouter-state-of-ai-2025]]** — Created concept page for the landmark study by OpenRouter & a16z analyzing 100 trillion tokens of real-world LLM usage. Covers: reasoning inflection point (Dec 5, 2024, o1 release), open vs closed source dynamics (30% OSS equilibrium, Chinese OSS rise), agentic inference shift (50%+ reasoning tokens, 4x prompt length explosion), category taxonomy (Programming 50%+ tokens, Roleplay 52% of OSS), provider specializations, economics (price inelasticity, Jevons Paradox, market archetypes), and geography (Asia 31%, doubled).
- **[[concepts/glass-slipper-effect]]** — Created concept page for the Cinderella Glass Slipper retention framework. Foundational cohorts (~40% retention at Month 5), Boomerang Effect, cognitive inertia, and workload-model fit thesis.
- **[[entities/openrouter]]** — Created entity page for OpenRouter, the unified API gateway for 300+ LLMs. Published the State of AI 2025 study with a16z.
- **[[entities/malika-aubakirova]]** — Created entity page for Malika Aubakirova, a16z infrastructure researcher and co-author of the State of AI 2025 study.
- **raw/articles/2025-12-01_openrouter-state-of-ai-2025.md** — Saved raw article.
- Source: https://openrouter.ai/state-of-ai

## [2026-05-02] Sparse Signal Loop — stochi's Experimental Validation of MGH

- **[[concepts/sparse-signal-loop]]** — Created concept page for Sparse Signal Loop experiment. Controlled 2×2 matrix test of feedback density (sparse vs dense), memory location (chat vs files), and procedure persistence (reinjection vs skill files) across LongBench-Pro and Mini SWE Agent Plus. Key findings: feedback sparsity is task-dependent, the "Judge Gap" (0.9667 Judge YES vs 0.5667 actual solve), constraint beats free-form memory.
- **[[entities/stochi]]** — Created entity page for stochi (stochi0). Independent AI researcher focused on post-training, agents, RL, model architectures. Previously shipped AI at QX Labs and Unsiloed AI (YC F25).
- **[[concepts/mismanaged-geniuses-hypothesis]]** — Added "Empirical Validation: Sparse Signal Loop" section with 3 key findings (supports, refines, warns). Added [[concepts/sparse-signal-loop]] to Related Concepts and cross-connections.
- **raw/articles/2026-05-02_sparse-signal-loop.md** — Saved raw article.
- Source: https://stochi0.vercel.app/writings/sparse-signal-loop

## [2026-05-02] Antoine Buteau — Automation Series (10 Parts) Full Ingestion

- **[[entities/antoine-buteau]]** — Created entity page for Antoine Buteau (Head of BizOps at Shakepay, previously Replit). Documented career timeline, Automation Series overview table, other series (Agency, Power, Technical Literacy, Live Player), key ideas (Three Kinds of Work, Automation Boundary, HITL as Design Pattern, Bounded Agents), and key quotes.
- **[[concepts/automation-series]]** — Created concept page for the 10-part Automation Series. Parts table covering all entries from "Automation Is Not One Thing" through "The Automation Architecture Worksheet." Key insights synthesized: Three Kinds of Work, Confidence-Driven Action, Bounded Agents, Staged Autonomy, and more.
- **raw/articles/2026-05-02_antoine-buteau_automation-series-1.md** through **automation-series-10.md** — Saved all 10 raw articles.
- Sources: https://www.antoinebuteau.com (full series via sitemap)

## [2026-05-02] PyTorch GPU Memory Profiling — Memory Measurement Without Execution (FakeTensorMode)

- **[[concepts/ai-infrastructure-engineering/pytorch-gpu-memory-profiling]]** — Added Section 4: "モデルを実行せずにメモリ使用量を測定する — FakeTensorMode + MemoryTrackingMode". Covers Alban Desmaison's ~30-line MemoryTrackingMode implementation, simultaneous use with FakeTensorMode for CUDA-on-CPU memory estimation, Module-wise tracking (PR #124688), allocated vs reserved memory distinction with fragmentation, NCCL buffer blind spot, and PyTorch caching allocator refactoring roadmap.
- Source: https://dev-discuss.pytorch.org/t/how-to-measure-memory-usage-from-your-model-without-running-it/

## [2026-05-02] PyTorch GPU Memory Profiling — Memory Snapshot & Profiler Tools Ingestion

- **[[concepts/ai-infrastructure-engineering/pytorch-gpu-memory-profiling]]** — Created concept page for PyTorch v2.1+ GPU memory debugging tools. Covers Memory Snapshot (allocation trace visualization with stack traces), Memory Profiler (categorized usage: gradients/optimizer/activations), OOM staircase pattern fix (`optimizer.zero_grad(set_to_none=True)`), `record_function` labeling, and tool comparison table.
- **[[concepts/ai-infrastructure-engineering/gpu-vram-fundamentals]]** — Added `pytorch-gpu-memory-profiling` to `related` and `Related Pages` sections.
- **[[concepts/ai-infrastructure-engineering/_index]]** — Added "Memory Debugging" row to scope table with link to new page.
- Source: https://pytorch.org/blog/understanding-gpu-memory-1/

## [2026-05-02] Braintrust Evals 101 Course — Practical Eval Methodology Ingestion

- **[[concepts/ai-evals]]** — Added "Braintrust Evals 101: Practical Eval Methodology" section covering: non-determinism as core thesis, 3-component eval model (dataset/task/scorer), LLM-as-Judge with choice scores, trial counts for variance reduction, multi-level trace scoring (per-turn vs per-trace), online scoring, the Improvement Loop with temperature=0/max_concurrency=1 settings, and the GPT-4o sycophancy rollback case study.
- **[[concepts/evaluation-tools-langsmith-braintrust-arize-phoenix-inspect-ai]]** — Enriched with Braintrust eval features, Evals 101 course module table, and comparison matrix with LangSmith/Arize Phoenix/Inspect AI.
- **raw/articles/2026-05-02_braintrust-evals-101-why-are-evals-important.md** — Saved raw article with full module-by-module breakdown (14 modules across Learn/Build/Refine sections).
- Source: https://www.braintrust.dev/foundations/why-are-evals-important | GitHub: braintrustdata/eval-101-course

## [2026-05-02] lambda-RLM (Typed Recursive Reasoning) — Huawei Paper Ingestion

- **[[concepts/typed-rlm]]** — Created concept page for lambda-RLM (typed functional runtime, Huawei Noah's Ark Lab). Formal guarantees (termination, cost bounds, optimal partition k*=2), Y-combinator fixed-point over SPLIT/MAP/REDUCE combinators. 29/36 wins, +21.9pp accuracy, 4.1x faster. arXiv:2603.20105 (arXiv-only, ingested per user request).
- **[[concepts/lambda-rlm]]** — Updated with disambiguation warning distinguishing from Huawei's lambda-RLM. Added [[concepts/typed-rlm]] to related.
- **[[concepts/rlm-recursive-language-models]]** — Added lambda-RLM variant section with comparison table. Updated Related Concepts.
- **raw/papers/2026-03-20_2603.20105_y-combinator-for-llms.md** — Saved raw paper summary with blocked reason: no_peer_review.
- Source: `raw/papers/2026-03-20_2603.20105_y-combinator-for-llms.md` | https://arxiv.org/abs/2603.20105

## [2026-05-02] Recursive by Design — Lambda-RLM, Theodoros Galanos & The Harness Blog Ingestion

- **[[concepts/lambda-rlm]]** — Created concept page for Lambda-RLM, a deterministic pipeline variant of RLM for the AEC domain. Plan (0 LLM calls) → Extract+Review → Generate. 14x token reduction, +8.4% quality improvement over open REPL.
- **[[entities/theodoros-galanos]]** — Created entity page for Theodoros Galanos, AI researcher and harness engineering practitioner. Chief Science Officer at infrared.city. Creator of Lambda-RLM and AEC-Bench.
- **[[entities/the-harness-blog]]** — Created entity page for The Harness blog (theharness.blog). 25 posts across 6 topics on harness engineering, agent evaluation, and AI in AEC.
- **[[concepts/rlm-recursive-language-models]]** — Updated with Lambda-RLM production case study section and benchmark metrics.
- **[[concepts/recursive-language-models]]** — Updated with Lambda-RLM variant reference.
- Source: `raw/articles/2026-05-02_the-harness-blog_recursive-by-design.md` | https://theharness.blog/blog/recursive-by-design/

## [2026-05-02] Paul Hoekstra — Agentic Engineering 4-Layer Framework (Full Series Ingestion)

- **[[entities/paul-hoekstra]]** — Created entity page for data engineer and Paul's Pipeline author. Documented 4-layer Agentic Engineering framework, key articles, and contributions.
- **[[concepts/harness-engineering/agentic-engineering-configuration-layer]]** — Created concept page for Layer 1. CLAUDE.md, Skills system, `<HARD-GATE>` enforcement, SkillsBench findings, anti-rationalization tables, division of labor strategy.
- **[[concepts/harness-engineering/agentic-engineering-capability-layer]]** — Created concept page for Layer 2. MCP with deferred loading, live docs (Context7, DeepWiki, Exa), visual output tools (Figma, frontend-slides, Remotion, draw.io), 3-layer memory strategy (MEMORY.md, episodic-memory, QMD).
- **[[concepts/harness-engineering/agentic-engineering-orchestration-layer]]** — Created concept page for Layer 3. Subagents vs Agent Teams, Ralph Loop, Git worktrees, context compression, "context over roles" design principle.
- **[[concepts/harness-engineering/agentic-engineering-guardrails-layer]]** — Created concept page for Layer 4. Poisoned instructions, homoglyph attacks, sandboxing (bubblewrap/Apple), permissions system, AST-grep, pre-commit/CI gates.
- **[[concepts/harness-engineering/agentic-engineering]]** — Updated: Added "Paul Hoekstra's 4-Layer Framework" section with integration notes vs Willison's framing. Updated sources and further reading.
- Source raw articles: 6 articles saved (4 series parts + statusline article + visual output article)

## [2026-05-02] Pi Podcast (Syntax #976) — Entity Enrichment & Concept Update

- **[[entities/pi-coding-agent]]** — Enriched with podcast insights: Pi's core definition ("a while loop with 4 tools"), "Bash is all you need" philosophy, steering queue, self-modifying skills with hot reloading, MCP critique vs Pi approach, prompt injection concerns, "Code is truth" memory philosophy, MAM (Master of Mischief) Slack bot.
- **[[entities/mario-zechner]]** — Enriched: Syntax.fm podcast appearance added to Recent Posts, Pi podcast revelations added to pi section (OpenClaw connection, steering queue, self-modifying skills).
- **[[entities/armin-ronacher]]** — Enriched: Syntax.fm #976 appearance added to timeline (Feb 4, 2026).
- **[[concepts/agentic-security]]** — Updated: Added "Camel Paper" section documenting the two-LLM approach to prompt injection defense and its practical limitations, with quote from the Pi podcast.
- Source: `raw/articles/2026-02-04_pi-syntax-fm-podcast.md` | https://syntax.fm/show/976/pi-the-ai-harness-that-powers-openclaw-w-armin-ronacher-and-mario-zechner/transcript

## [2026-05-02] Simulacrum of Knowledge Work — Concept & Entity Ingestion

- **[[concepts/simulacrum-of-knowledge-work]]** — Created concept page. Critical analysis by @onehappyfellow of how LLMs broke the proxy measures that knowledge work relies on for quality assessment. Covers proxy measures, incentive alignment crisis, Goodhart's Law recursive problem, and the "tokens-spent leaderboard" meta-commentary.
- **[[entities/onehappyfellow]]** — Created entity page for the author of "Simulacrum of Knowledge Work." Head of The Institute for Type Safe Memetic Research. OCaml programmer, technology writer, and rapper.
- Source: `raw/articles/2026-04-25_onehappyfellow-simulacrum-of-knowledge-work.md` | https://blog.happyfellow.dev/simulacrum-of-knowledge-work/

## [2026-05-02] Fireworks AI Podcast (SE Daily Episode 1919) — Entity & Concept Ingestion

- **[[entities/fireworks-ai]]** — Created entity page for Fireworks AI. AI inference and model customization platform for open-weight models. 13T+ tokens/day. Multi-hardware (NVIDIA + AMD), FireAttention kernels, custom speculator training, RFT capabilities.
- **[[entities/benny-chen]]** — Created entity page for Benny Chen, Co-Founder of Fireworks AI. Former Meta ML infrastructure. Key theses: RFT, "Traces Are All You Need," Eval Protocol, multi-hardware supply chain strategy.
- **[[concepts/reinforcement-fine-tuning]]** — Created concept page for RFT. Pragmatic RL fine-tuning using production traces + LLM-as-Judge. RFT vs SFT comparison table, Vercel case study (40x faster code fixing).
- **[[concepts/fine-tuning]]** — Updated: Added RFT as a method in Key Ideas + Terminology. Added related wikilinks to RFT page and Fireworks AI.
- **[[concepts/speculative-decoding]]** — Updated: Added "Custom Speculator Training (Fireworks AI Approach)" section. Documented distribution-matched speculators achieving 90%+ acceptance rates.
- Source: `raw/articles/2026-04-28_fireworks-ai-open-weight-models-sed.md` (SED transcript)

## [2026-05-02] Skeleton Enrichment — Foundation Capital Portfolio Companies (4 entities enriched)

- **[[entities/maximor]]** — Enriched from skeleton to L3 page. Added funding ($9M seed, Foundation Capital), founder bios (Ramnandan Krishnamurthy & Ajay Amudan, ex-Microsoft), Audit-Ready Agent architecture, product table, ERP-agnostic design principles. Sources: Blog, SaaSNews, TechCrunch, Axios.
- **[[entities/regie-ai]]** — Enriched from skeleton to L3 page. Added funding history ($50M total, $30M Series B Feb 2025), founder bios (Srinath Sridhar, Matt Millen), RegieOne platform features, investor list (Khosla Ventures, Scale Venture Partners, Foundation Capital). Sources: Crunchbase, PRNewswire, Regie blog.
- **[[entities/arize]]** — Enriched from skeleton to L3 page. Added funding ($131M total, $70M Series C), founder bios (Jason Lopatecki, Aparna Dhinakaran), Phoenix OSS details (2M+ monthly downloads, 9.5K GitHub stars, OpenTelemetry-based), AI Copilot, enterprise customers (Uber, Chime, eBay, Spotify, US Air Force). Sources: Arize blog, PRNewswire, GitHub, Crunchbase.
- **[[entities/playerzero]]** — Enriched from skeleton to L3 page. Added funding ($20M total, $15M Series A led by Foundation Capital), founder bio (Animesh Koratana, Stanford DAWN lab), context graph technology deep-dive (two clocks problem, engineering world models, code simulation), competitive positioning vs Cursor/Datadog/APM, customer Zuora, investor list (Matei Zaharia, Drew Houston, Dylan Field, Guillermo Rauch). Sources: TechCrunch, PlayerZero resources, AInvest.
- **[[entities/larsen-cundric]]** — Cleaned up stale `**Status:** skeleton` body text (frontmatter already showed `status: active`).

## [2026-05-02] Wiki Health Lint — Daily Automated Check

- **Critical Issues Found:**
  - 110 broken wikilinks to non-existent concept/entity pages
  - 331 unknown tags (tag sprawl — not in SCHEMA.md taxonomy)
  - 27 orphan entity pages, 172 orphan concept pages
  - 43 pages with incomplete frontmatter
  - Index count mismatch: header says 760 total but 1498 actual pages exist

- **Warnings:**
  - 91 oversized pages (>200 lines), including index.md at 1521 lines
  - 638 stub pages containing TODO markers
  - 7 entities split across 4-6 sub-pages each (claude-code, clefourrier, etc.)
  - 1 corrupted raw article with HTML parsing artifacts

- **Minor:**
  - 4 pages missing from index.md
  - 2 subdirectories missing _index.md
  - 1 page without frontmatter (log-2026.md)

## [2026-05-02] Active Crawl — xAI Grok 4.3, Microsoft Copilot Wave 3, MIT FTTE, SpaceX-xAI Merger

- **Researched 5 trending AI/ML topics** not yet covered in wiki:
  1. **xAI Grok 4.3** — Always-on reasoning, 1M context, aggressive pricing, Custom Voices
  2. **Microsoft Copilot Wave 3** — Copilot Cowork with Anthropic Claude, Agent 365, E7 Frontier Suite
  3. **MIT FTTE** — Federated Tiny Training Engine, 81% faster FL on edge devices
  4. **SpaceX acquires xAI** — $1.25T combined valuation
  5. **Grok Computer** — xAI's autonomous desktop agent

- **Saved 4 raw articles:**
  - `raw/articles/2026-05-01_xai-grok-4-3-launch.md`
  - `raw/articles/2026-03-09_microsoft-copilot-wave-3-frontier-transformation.md`
  - `raw/articles/2026-04-29_mit-ftte-federated-learning-edge-devices.md`
  - `raw/articles/2026-02-02_spacex-acquires-xai-merger.md`

- **Created 5 wiki pages:**
  - [[entities/xai]] — Company entity covering Grok ecosystem, SpaceX acquisition, pricing strategy
  - [[entities/grok-4-3]] — Latest model: always-on reasoning, 1M context, benchmarks, Custom Voices
  - [[concepts/grok-computer]] — Desktop agent: pixel-reading, universal app control, Grok 4.3 integration
  - [[concepts/microsoft-copilot-wave-3]] — Wave 3 transformation: Copilot Cowork, Agent 365, E7 suite
  - [[concepts/federated-tiny-training-engine]] — MIT FTTE: semi-async FL with 81% speedup on edge devices

- **Updated [[index]]** — Added 2 entities + 3 concepts. Total: 755→760. Entities: 365→367. Concepts: 402→405.

## [2026-05-02] Shopify — "The Most Future-Proof Job: Entrepreneurship" Data Analysis

- Saved raw article: `raw/articles/2026-04-15_shopify-future-proof-job-entrepreneurship.md` — Shopifyデータサイエンスチームによる起業家精神の分析。AIによる雇用減少（2026年3月の解雇の25%）と起業家増加（Shopify初回販売が2018年比7倍）の「Risk Flip」を示すデータ。リピート創業者の2倍以上の売上、eコマースの市場拡大（14%→20%+）、AI「Exoskeletons」の役割。
- Updated [[entities/shopify]] — 「Entrepreneurship & Ecommerce Trends」セクションを追加。「Risk Flip」テーゼ、リピート創業者 compounding、AI Exoskeletonsのデータを収録。
- Updated [[solo-founder-stack]] — 「Empirical Support: Shopify Data」セクションを追加。Shopifyの実証データで solo founder テーゼを補強（Risk Flip、Compounding Entrepreneur、AI Accelerator）。

## [2026-05-02] Every Guide — Agent-native Product Management + Compound Engineering

- Saved raw article: `raw/articles/2026-05-02_guide-to-agent-native-product-management.md` — Every社のガイド。Marcus Moretti（Spiral GM）が提唱するエージェントネイティブPM。ce:strategy（戦略策定）とce:product-pulse（自動ヘルスレポート）の2スキルを中核に、MCP経由でPostHog/Stripe/Datadogを統合。80/20計画重視シフト。

- Created [[entities/every-inc]] — AI-native media & software company (CEO Dan Shipper). 5 products with single-person teams. Compound Engineering plugin (7K+ stars).

- Created [[entities/marcus-moretti]] — GM of Spiral, author of Agent-native PM guide.

- Created [[entities/kieran-klaassen]] — GM of Cora, author of Compound Engineering: The Definitive Guide.

- Created [[concepts/agent-native-product-management]] — PMフレームワーク: 会話が仕事、80/20計画シフト、ce:strategy/ce:product-pulseスキル、エージェント管理バックログ。

- Created [[concepts/compound-engineering-every]] — Every社版Compound Engineering（各作業が将来を容易化）。Simon Willison版（コードレベルの反復改善ループ）とは異なる。

- Updated [[concepts/compound-engineering-loop]] — Stub→redirect（compound-engineering-every および Simon Willison版への誘導ページに変更）。

- Updated [[concepts/harness-engineering/agentic-workflows/compound-engineering-loop]] — Simon Willison版にEvery社版への相互参照を追加。

- Updated [[index]] — Added 3 entities + 2 concepts. Total: 750→755. Reclassified 1 stub.

## [2026-05-02] YouTube Video — "Why 2026 is The Year of Agentic Search" (Doug Turnbull & Jo Kristian Bergum)

- Saved raw article: `raw/articles/2026-05-01_doug-turnbull-2026-is-the-year-of-agentic-search.md` — 65-min fireside chat covering four pillars: LLM Query Understanding at scale, Autoresearch (agents writing ranking code), Agentic Search Harnesses (feedback loops for dumb retrievers), and LLM-as-a-Judge for principled search evaluation.
- Updated [[entities/doug-turnbull-speaking]] — Added talk to conference talks list (removed duplicate Berlin Buzzwords entry).
- Updated [[concepts/agentic-search]] — Added source with summary of four pillars.

## [2026-05-01] X Bookmarks Ingest — OpenAI WebSockets, LangChain Harness Engineering, Meta Autodata

- Saved raw articles:
  - `raw/articles/2026-04-22_openai-websockets-agentic-workflows.md` — OpenAI's transition to WebSocket transport for the Responses API, achieving ~40% faster agentic cycle latency (up to 1,000+ TPS). Techniques: `previous_response_id`, incremental safety processing, token caching.
  - `raw/articles/2026-02-17_langchain-improving-deep-agents-harness-engineering.md` — Vivek Trivedy (LangChain) case study: +13.7pts on Terminal Bench 2.0 from harness-only changes (Build-Verify Loop, Context Engineering, Loop Detection, Reasoning Sandwich).
  - `raw/articles/2026-04-08_langchain-better-harness-hill-climbing-evals.md` — Vivek Trivedy follow-up: evals as training data for autonomous harness hill-climbing with holdout sets.
  - `raw/articles/2026-04-30_meta-autodata-agentic-data-scientist.md` — Meta AI's Autodata: agentic data scientists using Weak-vs-Strong solver paradigm. 34% discrimination gap vs 1.9% baseline. Meta-optimization: 12.8%→42.4% pass rate.

- Updated [[concepts/harness-engineering]] — Added "LangChain Harness Engineering Case Studies" section with two sub-sections: Improving Deep Agents (+13.7pts, 4 techniques) and Better Harness (eval-driven hill-climbing recipe). Updated sources, tags, aliases, and related links.

- Created [[concepts/autodata-agentic-data-creation]] — New concept page for Meta AI's Autodata framework. Covers the 4-subagent Weak-vs-Strong paradigm, experimental results (34% gap), meta-optimization, and significance for inference-time compute scaling.

- Updated [[index]] — Added autodata-agentic-data-creation entry. Updated harness-engineering description to reference LangChain case studies and Vivek Trivedy. Total pages: 749→750.

- 5 X Articles behind auth wall (no external mirrors found): "How to Beat GRPO Without Touching Model Weights", "On SFT, RL, and on-policy distillation", "大语言模型训练与服务背后的数学原理", "If AI is so great, why isn't it working?", "The 5 principles for AI that ships to production". Saved as metadata-only in bookmark records.

## [2026-05-01] GLiClass | New concept page (encoder-only zero-shot classification)

- Created [[concepts/gliclass]] — Comprehensive concept page for Knowledgator's GLiClass model family. Covers:
  - **Architecture**: single-forward-pass classification, GLiNER-inspired design, 3 architecture types (uni/bi/bi-fused/encoder-decoder)
  - **Three sub-families**: GLiClass-V3 (general, 6 variants, DeBERTa/ModernBERT/Ettin backbones), GLiClass-Instruct (instruction-following, 3 variants), GLiClass-Multilang (20 languages, 3 variants, CrossAttn Scorer)
  - **V3 features**: hierarchical labels, few-shot, label descriptions, task prompts, long document chunking
  - **Training**: LoRA fine-tuning, multi-label PPO, logic-focused datasets
  - **RAC** (Retrieval-Augmented Classification): inference-time example retrieval, up to +141% F1 boost
  - **Benchmarks**: V3 large-v3.0 avg F1 0.7001, Instruct large-v1.0 avg F1 0.7199, Multilang Ultra avg F1 0.7212 (EN)
  - **Use cases**: RAG reranking, sentiment/topic, intent, NLI, hallucination detection, LLM safety
- Created [[entities/knowledgator]] — Organization entity page. Lists GLiNER/GLiClass/GLiREL product family, HF collections.
- Sources: arXiv:2508.07662, HuggingFace collections (3), GitHub repo, Medium blog, 3 X posts by @gm8xx8
- Updated: index.md, log.md

## [2026-05-01] AI Infrastructure Engineering — 親ページとスケルトン群の作成

- Created [[concepts/ai-infrastructure-engineering/_index]] — 親ページ。GPU/VRAM基礎、分散学習、モデルサーブ、オブザーバビリティ、コスト最適化の統合マップ。学習ロードマップ、既存ページ一覧表、Key Entitiesを含む。⬜ L1
- Created [[concepts/ai-infrastructure-engineering/gpu-vram-fundamentals]] — GPUメモリ階層（HBM→SRAM）、VRAM計算式、Roofline Model、バッチング経済学、量子化効果、GPU選定ガイド、マルチGPUトポロジ。⬜ L1
- Created [[concepts/ai-infrastructure-engineering/distributed-training]] — DDP→FSDP→DeepSpeed ZeRO(1/2/3)、3D並列化（TP/PP/EP/Expert Parallel）、戦略選択ガイド（モデルサイズ×GPU数）、CPUオフロード比較。⬜ L1
- Created [[concepts/ai-infrastructure-engineering/model-serving-autoscaling]] — デプロイ構成、スケーリングシグナル（queue/GPU/KV cache）、4つのスケーリングパターン、ロードバランシング戦略（Round Robin→LRU→Semantic）、コスト最適化パターン。⬜ L1
- Created [[concepts/ai-infrastructure-engineering/llm-observability]] — 推論メトリクス（TTFT/TPOT/ITL）、GPUリソース指標、品質シグナル、Observability Stack（Prometheus/OTel/Arize）、コスト帰属、劣化検知パターン、vLLM OTel統合。⬜ L1
- Created [[concepts/tensorrt-llm]] — NVIDIA推論最適化エンジン。FP8/FP4 Transformer Engine、vLLMとの比較表、ベンチマーク概算値、導入判断基準、Triton統合パターン。⬜ L1
- Enriched [[concepts/model-quantization]] — stub→L1。精密形式一覧（FP32→BitNet）、GPTQ/AWQ/GGUF/SmoothQuant/FP8比較、ハードウェアサポート表、トレードオフ実測値、KV Cache量子化。
- Enriched [[concepts/pytorch-fsdp-distributed-training]] — stub→L1。Sharding戦略詳細（NO_SHARD/SHARD_GRAD_OP/FULL_SHARD）、メモリ節約計算例、CPU Offload、DeepSpeed比較表、設定パラメータサンプルコード。
- Updated [[concepts/inference/_index]] — TensorRT-LLMをエンジン比較表に追加
- Updated [[index]] — Concepts 393→399, added 7 new entries + updated 2 TODO entries
- Sources: (new pages are skeleton/L1, will need article ingestion for enrichment)

---

## [2026-05-04] blog-wiki-ingest | 18 articles, 0 created, 0 updated
- **Pipeline**: blog-ingest → blog-triage → blog-wiki-ingest
- **Checkpoint**: 20260504T070032Z
- **Take**: 0 — 既存Wikiページですべてカバー済み
- **Reference**: 4 — Simon Willison/Anthropic sycophancy (anti-sycophancy.md), Martin Alderson CopyFail (martin-alderson.md), George Hotz essay (george-hotz.md), Gary Marcus healthcare (gary-marcus.md)
- **Skip**: 14 — Zig, PNG, touch typing, RSS→Atom, politics, staff engineer, math, sponsor page, Steve Jobs, HTML/CSS, 86-DOS, Bluesky politics, wheel history, empty file
- **Verdict**: No new wiki pages needed. All AI-relevant articles already captured in existing entity/concept pages.
