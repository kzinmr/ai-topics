## [2026-05-01] Dolt & Beads — エージェント向けデータベース/イシュートラッカーのwiki取り込み

- Created [[entities/dolt]] — Version-controlled SQL database ("Git for Data") by DoltHub Inc. MySQL/Postgres/SQLite-compatible. Prolly Trees storage engine, branches/merges/diffs, Dolt MCP for AI agents, Hosted Dolt/DoltHub/DoltLab ecosystem.
- Created [[entities/beads]] — Distributed graph issue tracker for AI coding agents by Steve Yegge (Gastown Hall). Powered by Dolt. Dependency-aware graph, memory compaction, hash-based IDs, MCP integration, formulas/molecules/gates.
- Updated [[index]] — Entities 356→358, Total pages 741→743
- Sources: dolthub.com, docs.dolthub.com, gastownhall.github.io/beads, github.com/steveyegge/beads, steve-yegge.medium.com (Beads Best Practices)

## [2026-05-01] Coding Agent Harnesses Comparison 作成

- Created [[comparisons/coding-agent-harnesses]] — コーディングエージェントハーネス比較：Claude Code vs OpenCode vs Pi vs Aider vs Codex CLI vs Cursor。ハーネス効果（Harness Effect）の概念、モデル×ハーネス相性マトリックス、実測ベンチマーク、Anthropicのサードパーティハーネス制限を含む。出典: thoughts.jock.pl, grigio.org, disler/pi-vs-claude-code GitHub, Terminal Trove。
- Updated [[index]] — Comparisons 11→12 pages

## [2026-05-01] Blog Wiki Ingest — Reiner Pope, LLM 0.32a0, Codex /goal, Zig Anti-AI, GPT-5.5 Cyber Eval

- Created [[entities/reiner-pope]] — CEO of MatX, former Google TPU architect. Expert on full-stack AI from chip design to model architecture. Known for roofline analysis framework.
- Created [[entities/matx]] — AI chip startup founded by Reiner Pope.
- Enriched [[concepts/llm-inference]] — Expanded from stub to L2 page with Reiner Pope's roofline analysis framework: batch size economics, KV cache bandwidth, MoE hardware topology, pipeline parallelism tradeoffs, 20ms batch train scheduling, RL overtraining implications.
- Enriched [[concepts/zig]] — Expanded from stub to L2 page. Documented Zig's anti-LLM contribution policy, "contributor poker" rationale by Loris Cro, Andrew Kelley's "digital smell" concept, Bun fork implications.
- Enriched [[concepts/llm-security]] — Expanded from stub to L2 page with AISI evaluation of GPT-5.5 cyber capabilities: 71.4% CTF pass rate, 10-min rust_vm solve (vs 12 human hours), universal jailbreak in 6 hours, TLO range solution.
- Updated [[entities/simon-willison]] — Added LLM 0.32a0 section documenting messages-based input and streaming typed parts architecture. Added raw article references.
- Updated [[entities/dwarkesh-patel]] — Added Reiner Pope blackboard lecture to timeline and related entities.
- Updated [[concepts/openai-codex-superapp]] — Added /goal command section (Codex CLI 0.128.0), Ralph loop pattern implementation.
- Updated index: wiki/index.md, wiki/log.md
- Sources:
  - raw/articles/dwarkesh.com--p-reiner-pope--11ee10e4.md
  - raw/articles/simonwillison.net--2026-apr-29-llm--dff2021f.md
  - raw/articles/simonwillison.net--2026-apr-30-codex-goals--b85bdf73.md
  - raw/articles/simonwillison.net--2026-apr-30-zig-anti-ai--e30e52cf.md
  - raw/articles/simonwillison.net--2026-apr-30-andrew-kelley--7be6c476.md
  - https://www.aisi.gov.uk/blog/our-evaluation-of-openais-gpt-5-5-cyber-capabilities

## [2026-05-01] Cloudflare Project Think: PTCの4次元拡張（Execution Ladder, Durable Execution, Self-Authored Extensions, Hibernation Economics）

- Expanded [[concepts/programmatic-tool-calling]] — Added "Cloudflare Project Think: PTCの次元拡張" section with 4 new dimensions:
  1. **Execution Ladder** — 5-tier capability escalation (Workspace → Dynamic Worker → npm → Browser → Sandbox), each tier maps to PTC environment capability vs isolation tradeoff
  2. **Durable Execution (Fibers)** — `stash()` checkpointing for crash recovery, comparison with Anthropic's 30-day container limit, connection to RLM's implicit statefulness
  3. **Self-Authored Extensions (Meta-PTC)** — PTC as Autogenesis: agents write TypeScript tools at runtime (git extension → Dynamic Worker load → persistent tool), 3-layer recursion with PTC in RLM (案A)
  4. **Hibernation Economics** — Zero-idle-cost Durable Objects vs always-on containers, implications for PTC granularity design and long-running RLM context exploration
- Expanded [[concepts/code-mode]] — Added "言語選択の二分性: JavaScript vs Python" section (Cloudflare V8 JS vs Pydantic Monty Python vs Anthropic Container Python: runtime, package management, type safety, model affinity) and "MCP-based vs Native API: トランスポート層の設計選択" section (MCP-based vs Anthropic native `code_execution_20260120`: protocol standardization, security, portability, convergence prediction)
- Saved raw article: raw/articles/2026-04-15_cloudflare-project-think.md
- Sources:
  - https://blog.cloudflare.com/project-think/
  - https://blog.cloudflare.com/code-mode/

## [2026-05-01] Audio Tokenizer Comparison — SoundStream / EnCodec / DAC / SpeechTokenizer / Mimi

5つの音声トークナイザの比較分析を作成・取り込み：

- Created [[concepts/audio-tokenizer-comparison]] — Concept page with comparison table (architecture, token rate, bitrate, semantic separation, streaming, domain coverage), detailed breakdown of each model, practical selection guide, and caveats on sample rate / causality differences
- Created [[entities/soundstream]] — Foundational Google neural audio codec (2021), fully convolutional + RVQ, 3–18 kbps
- Created [[entities/encodec]] — Meta's production-standard codec (2022), 24/48 kHz, 1.5–24 kbps, de facto standard
- Created [[entities/descript-audio-codec]] — High-fidelity universal codec by Descript (2024), 44.1 kHz / 8 kbps, speech/music/environment
- Created [[entities/speech-tokenizer]] — Unified semantic+acoustic tokenizer by Fudan (2023), HuBERT-distilled layer separation, ~50 Hz / ~4 kbps
- Created [[entities/mimi]] — Kyutai's ultra-low-rate streaming codec (2024), 12.5 Hz / 1.1 kbps, WavLM-distilled, for Moshi
- Updated [[concepts/speech-audio-asr-tts-voice]] — Added Neural Audio Tokenizers section with links to the comparison and all 5 entities
- Saved raw article: `raw/articles/2026-05-01_audio-tokenizer-comparison.md`
- Updated index: wiki/index.md, wiki/log.md

---

- Created [[entities/vibevoice]] — Entity page for Microsoft's open-source TTS model. Combines Qwen2.5 LLM with continuous speech tokenizers (7.5 Hz, 3200× compression) and diffusion head for up to 90 min, 4-speaker generation. ICLR 2026 Oral. GitHub repo disabled due to misuse concerns.
- Saved raw article: `raw/articles/vibevoice-technical-report.md`
- Updated [[concepts/speech-audio-asr-tts-voice]] — Added VibeVoice as a key player (Microsoft section), updated competitive positioning table with multi-speaker/max-duration columns, added to open-vs-closed section
- Updated [[concepts/speech]] — Added VibeVoice to related concepts
- Updated index: wiki/index.md, wiki/log.md

---

## [2026-04-30] Skill Retrieval Augmentation (SRA) — Academic framework for agent skill retrieval at scale

- Created [[concepts/skill-retrieval-augmentation]] — Concept page synthesizing Su, Long, Ai et al. (2026) arXiv:2604.24594. Three-stage SRA pipeline (Retrieve→Incorporate→Apply), SRA-Bench (5,400 tasks, 26,262 skills), "incorporation bottleneck" finding, and connection to harness engineering (progressive disclosure).
- Saved raw paper: `raw/papers/2026-04-27_2604.24594_skill-retrieval-augmentation-for-agentic-ai.md` (user override — arXiv only, no venue found)
- Cross-referenced with [[concepts/agentic-search]] (Level 2: skill/tool discovery), [[concepts/skill-architecture-patterns]] (Hermes vs OpenClaw skill management), [[concepts/harness-engineering]] (outer loop gating of skill selection)
- Updated index files: wiki/index.md, wiki/log.md.

---

## [2026-04-30] The Revenge of the Data Scientist — Hamel Husain's Foundational Essay on Harness Engineering

- Created [[concepts/harness-engineering]] — Concept page synthesizing Hamel Husain's "Harness is Data Science" thesis: the 5 Eval Pitfalls, the mapping of modern LLM tasks to classic DS practices, binary-over-Likert principle, and vibe-based engineering critique.
- Enriched [[entities/hamel-husain]] — Added "The Revenge of the Data Scientist" (Mar 2024) to timeline, expanded Harness Engineering section with the 5 Eval Pitfalls and DS mapping table, added source link.
- Saved raw article: `raw/articles/2024-03-26_hamel-revenge-data-scientist.md`
- Sources: https://hamel.dev/blog/posts/revenge/
- Updated index files: wiki/index.md, wiki/log.md.

---

## [2026-04-30] RAG Is Not Dead — Added Part 5: Multiple Representations ("The Map is Not the Territory")

- Created [[concepts/multiple-representations-rag]] — Bryan Bischof & Ayush Chaurasia. Core thesis: "The Map is Not the Territory" — create multiple specialized maps instead of one universal embedding. Detailed Bischof's unique framework: curving space, buzzword deconstruction, bicycle analogy, three IR responsibilities.
- Updated [[concepts/rag-not-dead-series]] — Added Part 5 detail section, wikilink, graph query, and source.
- Saved raw article: `raw/articles/2026-04-30_hamel-husain-rag-p5-map.md`
- Sources: https://hamel.dev/notes/llm/rag/p5_map.html
- Updated index files: wiki/index.md, wiki/log.md.

---

## [2026-04-30] RAG Is Not Dead — Added Part 4: Late-Interaction Retrieval (ColBERT)

- Created [[concepts/late-interaction-retrieval]] — Antoine Chaffin's ColBERT/MaxSim. 150M parameter model beats 7B dense on BRIGHT. PyLate tooling. Three adoption barriers now resolved (storage, VectorDB, tooling).
- Updated [[concepts/rag-not-dead-series]] — Added Part 4 detail section, wikilink, graph query, and source.
- Saved raw article: `raw/articles/2026-04-30_hamel-husain-rag-p4-late-interaction.md`
- Sources: https://hamel.dev/notes/llm/rag/p4_late_interaction.html
- Updated index files: wiki/index.md, wiki/log.md.

---

## [2026-04-30] RAG Is Not Dead — Added Parts 2 & 3: FreshStack + Reasoning Retrieval

- Created [[concepts/freshstack-benchmark]] — Nandan Thakur's modern RAG evaluation benchmark. Three metrics (Coverage@20, Diversity, Recall@50). Replaces contaminated BEIR/MTEB with real-time data.
- Created [[concepts/reasoning-retrieval]] — Orion Weller's Promptriever (instruction-aware bi-encoder) + Rank1 (reasoning-based reranker with CoT). 10-point gain from reasoning traces.
- Updated [[concepts/rag-not-dead-series]] — Added detailed P2/P3 sections, fixed ben-clavie → benjamin-clavie reference, added new concept wikilinks and sources.
- Saved raw articles: `raw/articles/2026-04-30_hamel-husain-rag-p2-evals.md`, `raw/articles/2026-04-30_hamel-husain-rag-p3-reasoning.md`
- Sources: https://hamel.dev/notes/llm/rag/p2-evals.html, https://hamel.dev/notes/llm/rag/p3_reasoning.html
- Updated index files: wiki/index.md, wiki/log.md.

---

## [2026-04-30] Hamel Husain — RAG Is Not Dead Series & Part 1 Modern Retrieval Toolkit

- Created [[concepts/rag-not-dead-series]] — Hamel Husain & Ben Clavié's open 7-part series arguing RAG is not dead. Covers all 7 parts from naive single-vector myth through context rot to graph DB over-engineering.
- Created [[concepts/modern-retrieval-toolkit]] — Ben Clavié's thesis that naive single-vector RAG is dead but retrieval itself is more essential. Covers modern retrieval toolkit (BM25, ColBERT, agentic search) and why long context windows won't kill retrieval.
- Updated [[entities/hamel-husain]] — Added 2025 timeline entries for RAG Is Not Dead series launch and Part 1 hosting. Added sources and related entities (benjamin-clavie, rag-not-dead-series, modern-retrieval-toolkit).
- Updated [[entities/benjamin-clavie]] — Added 2026 timeline entries for RAG Is Not Dead series and Part 1 presentation. Added sources and related concepts.
- Saved raw articles: `raw/articles/2026-04-30_hamel-husain-rag-not-dead.md`, `raw/articles/2026-04-30_hamel-husain-rag-p1-retrieve-documents.md`
- Sources: https://hamel.dev/notes/llm/rag/not_dead.html, https://hamel.dev/notes/llm/rag/p1-intro.html
- Updated index files: wiki/index.md, wiki/log.md.

---

## [2026-04-30] Daily Skeleton Enrichment — 8 Entity Pages Enriched

- Enriched [[entities/coding-agents]] — LLM-powered coding agents ecosystem (Claude Code, Cursor, Copilot, Warp). Eric Zakariasson's optimization framework.
- Enriched [[entities/block-ai]] — Block Inc. (Square) AI transformation "From Hierarchy to Intelligence" by Jack Dorsey.
- Enriched [[entities/mathematical-methods]] — Terence Tao & Tanya Klowden's philosophical paper on AI and mathematical thought (arXiv:2603.26524).
- Enriched [[entities/embeddings]] — Single-vector embedding limitations (LIMIT dataset, drowning-in-documents paradox). arXiv:2603.29519.
- Enriched [[entities/zakirullin]] — Artem Zakirullin, author of "Cognitive load is what matters" (12K+ GitHub stars).
- Enriched [[entities/lora-fine-tuning]] — LoRA fine-tuning plus Sakana AI's Doc-to-LoRA and Text-to-LoRA hypernetwork paradigm.
- Enriched [[entities/thin-bi-tool]] — 薄くなるBIツール — BI tools transitioning from comprehensive platforms to lightweight, DWH-native visualization tools.
- Enriched [[entities/akshay-pachaar]] — Senior AI Engineer at Lightning AI, Co-Founder of Daily Dose of Data Science, author of "Anatomy of an Agent Harness".
- Updated index files: wiki/index.md, entities/_index.md.
- Sources: Combination of raw articles, web research (arXiv, Wikipedia, GitHub, LinkedIn, blog posts).

---

## [2026-04-30] Hamel Husain & Jo Kristian Bergum — "P7: You Don't Need a Graph DB (Probably)"

- Created [[concepts/graph-db-overengineering-rag]] — Core thesis: GraphRAG is a technique, not a technology. Covers silver bullet trap, context stuffing (Floppy Disk Rule), HNSW as hidden graph, evaluation-first approach. Designed with structured graph query cross-references for wiki knowledge base traversal.
- Updated [[entities/hamel-husain]] — Added 2026 publication to timeline, wikilink to new concept, source reference.
- Updated [[concepts/knowledge-graph-memory-agents]] — Added "You Don't Need a Graph DB" Constraint section referencing this article.
- Saved raw article: raw/articles/2026-04-30_hamel-husain-p7-graph-db-rag.md
- Source: https://hamel.dev/notes/llm/rag/p7-graph-db.html

---

## [2026-04-30] Doug Turnbull — "How To Build Your First Agentic Search Application" (Feb 2026, Vanishing Gradients)

- Expanded [[concepts/agentic-search]] — Added "Practitioner Implementation: The Tool-Calling Loop" section under Level 2 (Harness Engineering). Concrete 6-step implementation loop connecting the harness layer to Fintool's SQL-based skill discovery pattern.
- Expanded [[entities/doug-turnbull-core-ideas]] — Added "The Agentic Search Implementation Loop" section with core tool-calling loop, harness validation loop ("try harder" pattern), long-running agents & memory compaction direction, and build-vs-buy guidance (Pydantic AI vs hand-rolling). Also added "Passive → Proactive → Active (Agentic) Spectrum" framework.
- Enriched [[entities/doug-turnbull-speaking]] — Added interview to Conference Talks list.
- Saved raw article: raw/articles/2026-02-20_doug-turnbull-build-first-agentic-search-app.md
- Source: https://www.youtube.com/watch?v=AJPH9kpN3Sc

---

## [2026-04-30] Doug Turnbull — "RAG Users Want Affordances, Not Vectors" (Dec 2025)

- Expanded [[concepts/agentic-search]] — Added cross-reference to foundational article in Level 1 (IR Research): Turnbull's practitioner critique of vector-centric RAG embedding crowding, threshold problem, in-domain nuance echoes the academic findings. Added raw article to sources frontmatter and sources section.
- Expanded [[entities/doug-turnbull-core-ideas]] — "RAG Isn't a Vector Search Problem" section enriched with three failure modes, the affordances solution (structured schema extraction via LLMs), the tiered strategy, and diversity-for-agentic-loops principle.
- Expanded [[entities/doug-turnbull]] — Added "Affordances Not Vectors" to Recent Blog Posts list. Cleaned up duplicate entries.
- Saved raw article: raw/articles/2025-12-09_doug-turnbull-rag-users-want-affordances.md
- Source: https://softwaredoug.com/blog/2025/12/09/rag-users-want-affordances-not-vectors

---

## [2026-04-30] Doug Turnbull — "Rag is the What. Agentic search is the How." Talk (April 2026)

- Expanded [[concepts/agentic-search]] — Added "Talk: 'Rag is the What. Agentic search is the How.'" section under Level 3 (Practitioner Perspective). Four-stage unwinding framework (Structured Attributes → Tool Calling → Reasoning → Dumb Retrievers). Complexity migration thesis: retrieval → agent+harness. Explicit SID-1 endorsement. This talk is the live-recorded version of the "Grep Moment" thesis, extended to a full architectural critique of the RAG paradigm.
- Enriched [[entities/doug-turnbull-speaking]] — Added this 54-minute talk to Conference Talks list with wikilink to raw article.
- Saved raw article: raw/articles/2026-04-22_doug-turnbull-rag-is-the-what-agentic-search-is-the-how.md
- Source: https://www.youtube.com/watch?v=UXQ916WRK0A

---

## 2026-05-01 — Final review: cross-reference all PTC×RLM insights across remaining pages

- Updated [[concepts/rlm-recursive-language-models]] — Added "Relation to Programmatic Tool Calling (PTC): 2-Axis Complementarity" section with comparison table, decomposition strategy analysis (4-level spectrum), and architectural fusibility code example. Fixed broken wikilinks in Related Concepts (> code-execution-with-mcp, programmatic-tool-calling, code-mode, agentic-search). Updated frontmatter with sources and tags.
- Updated [[concepts/harness-engineering/system-architecture/code-execution-with-mcp]] — Added cross-references to programmatic-tool-calling (upper concept) and code-execution-with-mcp (root level). Fixed broken frontmatter (duplicate updated field, lost sources key).

- Updated [[concepts/dspy-rlm]] — Added 3 new subsections under "補完する2軸" framing:
  1. "方向性の対称性: PTCは統合(merge)、RLMは分解(split)" — PTC merges N tool calls into 1 code block; RLM splits 1 huge context into N pieces. Mirror symmetry.
  2. "RLM = 文脈の分割統治/MapReduceをLLMで柔らかく行う" — RLM as soft MapReduce: MAP = context exploration/code, SHUFFLE = llm_query extraction, REDUCE = SUBMIT/synthesis. Contrast with rigid MapReduce.
  3. "文脈の分割戦略はLLM自身が決める——そして自由だ" — YES, the LLM decides decomposition strategy end-to-end. Spectrum from manual (raw Python) to delegated (PTC tools) to recursive (llm_query). 4 levels of decomposition freedom (method, granularity, depth, tool delegation). Tool-Augmented RLM code examples for each strategy.
- Source: RLM paper §5 ("unlike prior agentic methods... defer decisions to the LM").

---

## 2026-05-01 — PTC × RLM: 補完する2軸（関数軸 vs データ軸）に再フレーミング

- Rewrote [[concepts/dspy-rlm]] section "RLM × Programmatic Tool Calling" — Added "補完する2軸（関数軸 vs データ軸）" framing. PTC solves tool execution (function axis), RLM solves context management (data axis). Both apply code execution to fundamentally different problems. Added comparison table, axis diagram, concrete code examples for each axis and their integration. Reorganized existing DSPy implementation analysis + first-principles design under the new framing.
- Rewrote [[concepts/programmatic-tool-calling]] section "Relation to RLM" — Same 2-axis framing. Confirmed user's insight: PTC = deterministic execution via code vs tool calling, RLM = context scaling/selection via code vs RAG/long-context. Cross-reference to dspy-rlm for full analysis.

---

## 2026-05-01 — RLM × PTC first-principles re-analysis: architecturally fusible

- Updated [[concepts/dspy-rlm]] — Added "第一原理からの再検討: PTC統合のための環境拡張設計" subsection. RLM論文の環境抽象化（Environment = {REPL, context, llm_query, SUBMIT}）は任意の記号的操作対象に拡張可能であり、PTCツールを第一級市民としてホストする設計が自然であることを論証。3つの統合アーキテクチャ（案A: PTC in RLM★推奨 / 案B: RLM as PTC Tool / 案C: Dual Environment）を提案。4つの設計課題と解決方針を明示。
- Updated [[concepts/programmatic-tool-calling]] — Rewrote "Relation to RLM" section. Added first-principles compatibility table (REPL, variable space, sandboxed builtins, llm_query all align with PTC). Added recommended architecture diagram (PTC in RLM). Conclusion: DSPy does NOT incorporate PTC, but architectural necessity is different — RLM's environment abstraction is naturally compatible with PTC tools.
- Source: https://arxiv.org/abs/2512.24601v1 (RLM paper, full reading)

---

## 2026-05-01 — RLM × PTC analysis: independent paradigms sharing code-execution substrate

- Added [[concepts/dspy-rlm]] section "RLM × Programmatic Tool Calling: 独立した2つのパラダイム" — RLM does NOT explicitly incorporate PTC. They evolved independently solving different problems (context rot vs tool definition bloat) with the same substrate (sandboxed code execution). RLM's `llm_query` is recursive sub-LM calling, not tool calling. RLM's `tools` parameter is architectural freedom (accidental extensibility), not designed integration. 4 specific limitations listed.
- Added [[concepts/programmatic-tool-calling]] section "Relation to RLM: Same Substrate, Different Problems" — comparison table and cross-reference to dspy-rlm analysis.
- Updated See Also in programmatic-tool-calling.md to include dspy-rlm and rlm-recursive-language-models.

---

## 2026-05-01 — Monty README positioning: designed for Programmatic Tool Calling

- Updated [[concepts/monty-sandbox]] — Added "設計思想: Programmatic Tool Calling のランタイム" section with direct README quote ("Monty avoids the 'faff' of containers"). Added Monty vs Docker/Pyodide/WASI comparison table. Added 3-layer hierarchy positioning (Programmatic Tool Calling → Monty → CodeMode). Updated Related Concepts and sources.
- Updated [[concepts/programmatic-tool-calling]] — Added "Reference Runtime: Monty (Pydantic)" section. Monty feature-to-PTC requirement mapping table. Updated See Also with monty-sandbox and pydantic-ai-harness.
- Source: https://raw.githubusercontent.com/pydantic/monty/refs/heads/main/README.md

---

## 2026-05-01 — Programmatic Tool Calling & Code Execution with MCP

- Created [[concepts/programmatic-tool-calling]] — New highest-level concept: Anthropic's API mechanism (`code_execution_20260120` tool, `allowed_callers` field). Defines the 3-layer hierarchy: Programmatic Tool Calling → Code Execution with MCP → CodeMode. Covers container lifecycle, token optimization (98.7% reduction), async tool interface, advanced patterns (batch, early termination, conditional). Cross-references to CodeMode, RLM, agentic-search Externalized Processing.
- Enriched [[concepts/code-execution-with-mcp]] — Upgraded from stub to full concept page. Architectural pattern: MCP servers as filesystem of TypeScript wrappers, progressive disclosure, PII tokenization, skills persistence. Middle layer between Programmatic Tool Calling and CodeMode.
- Updated [[concepts/code-mode]] — Added "Positioning in the Hierarchy" section with 3-layer diagram. Updated "Related Patterns" with cross-references to both higher-level pages.
- Saved raw articles referenced (Anthropic platform docs + engineering blog)
- Sources:
  - https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling
  - https://www.anthropic.com/engineering/code-execution-with-mcp

---

## 2026-04-30 — Cloudflare Code Mode MCP

- Expanded [[concepts/code-mode]] — Added "Cloudflare Server-Side Code Mode (MCP)" section with 2-tool interface (search/execute), V8 sandbox, 99.9% token reduction from ~1.17M to ~1K tokens. Added context reduction approaches comparison table. Added "CodeMode × RLM: 並行する文脈爆縮の2つのアプローチ" section with architectural comparison, tradeoff analysis, and convergence prediction. Updated frontmatter with Cloudflare sources.
- Saved raw article: raw/articles/2026-04-30_cloudflare-code-mode-mcp.md
- Source: https://blog.cloudflare.com/code-mode-mcp/

---

## [2026-04-30] Doug Turnbull — Can Agents Replace the Search Stack?

- Expanded [[concepts/agentic-search]] — Added "Benchmarking Agents vs Search Stack: Amazon ESCI" section under Level 1 (after SID-1). Key results: GPT-5 + BM25 + embeddings achieves 0.453 NDCG (+56.7% vs BM25 baseline). Agents naturally refine queries (emerging Q2Q behavior). Encouraged exploration (min 4 calls + diversity) improves NDCG from 0.410 → 0.4308. Key boundary: agentic search works for "finding things" but not "deep research." Connected findings back to all three levels via validated patterns table.
- Saved raw article: raw/articles/2026-04-28_softwaredoug-can-agents-replace-search-stack.md
- Fixed: cleaned up duplicate entries in agentic-search.md frontmatter sources.

## [2026-04-30] Anthropic Dynamic Web Search Filtering — Production externalized processing

- Expanded [[concepts/agentic-search]] — Added "Production Implementation: Claude's Dynamic Web Search Filtering (Anthropic)" section under Level 3. Filter-before-reasoning flow: Claude writes code to extract relevant data from web results before context loading. ~11% accuracy gain, ~24% token reduction. Validates all three levels: code as re-ranker (L1), harness orchestration (L2), externalized processing (L3). Cross-referenced with Cao et al. paper (same paradigm, web layer instead of filesystem layer).
- Saved raw article: raw/articles/2026-03-30_claude-web-search-dynamic-filtering.md
- Source: https://www.gend.co/blog/claude-web-search-dynamic-filtering

## [2026-04-30] Doug Turnbull — Agentic Search Is Having a Grep Moment

- Expanded [[concepts/agentic-search]] — Added "Practitioner Perspective: Doug Turnbull's 'Grep Moment'" section under Level 3. Two-loop architecture (inner agent loop + outer harness validation), deconstructing the search stack (ranking logic moves from search engine to harness), why dumb tools work (constraints budget creativity, code navigation training data), three limits of grep (actionable feedback, complexity, token cost). Cross-references SID-1 and the externalized processing paradigm.
- Saved raw article: raw/articles/2026-04-06_softwaredoug-agentic-search-grep-moment.md
- Source: https://softwaredoug.com/blog/2026/04/06/agentic-search-is-having-a-grep-moment

## [2026-04-30] SID-1 — First RL-Trained Agentic Retrieval Model

- Expanded [[concepts/agentic-search]] — Added "RL-Trained Agentic Retrieval: SID-1" section under Level 1 (IR Research Perspective). SID-1 (SID AI, Dec 2025, Qwen3-14B + GRPO): 0.84 recall (near-doubled vs reranker @10), 24× faster than GPT-5.1, 374× cheaper than Sonnet 4.5. Key insights: document-centric reward (NDCG), TI/TO pipeline (message abstractions cause model collapse), length scheduling. Emergent capabilities: parallel tool use, hierarchical retrieval with `read` tool, RRF fusion.
- Saved raw article: raw/articles/2025-12-04_sid-1-agentic-retrieval.md
- Source: https://www.sid.ai/research/sid-1-technical-report

## [2026-04-30] Coding Agents are Effective Long-Context Processors — Cao, Yin, Dhingra, Zhou

- Expanded [[concepts/agentic-search]] — Added Level 3: "Coding Agents as Retrieval/Processing Interface" (Duke & CMU, arXiv:2603.20432). Key findings: coding agents outperform SOTA by 17.3% on long-context tasks by using file system tools (grep, sed, ripgrep, Python scripts). BrowseComp-Plus score of 88.50 vs 80.00 baseline. Retrieval tools *harm* performance when agents can use file system exploration. Folder structure (89.0%) beats single file (83.0%). Cost: ~$0.19–$0.70/query. Paradigm shift: externalized processing as alternative to context window scaling.
- Saved raw paper: raw/papers/2026-03-20_2603.20432_coding-agents-effective-long-context-processors.md
- Source: https://arxiv.org/abs/2603.20432 (arXiv-only, ingested per user request)

## [2026-04-30] Revisiting Text Ranking in Deep Research — Meng, Ou, MacAvaney, Dalton

- Expanded [[concepts/agentic-search]] — Restructured to two-level definition (IR/Retrieval Layer + Harness Engineering Layer). Added comprehensive section on University of Glasgow study (arXiv:2602.21456): BM25 dominance over neural rankers, passage-level retrieval, Q2Q reformulation (7.95% accuracy gain), re-ranking depth (BM25–monoT5-3B at 0.716 recall), reasoning re-rankers underperform.
- Saved raw paper: raw/papers/2026-02-25_2602.21456_revisiting-text-ranking-in-deep-research.md
- Source: https://arxiv.org/abs/2602.21456 (arXiv-only, ingested per user request)

## [2026-04-30] Bulk c3afd19 — 解決完了: 未作成48件の全件対応 + 3 Skeleton Enrich

- **48件の「ファイル未作成」全件対応完了**
  - ✅ 新規Entity/Concept作成: shuvendu, devin, kimi, lenny, databricks, contextarena, agentcraft, concepts/korean-ai
  - ✅ 既存Entityにマッピング確認: wheresyoured→ed-zitron, mariozechner→mario-zechner, 0xsero→sero, kleppmann→martin-kleppmann, ysymyth
  - ✅ 既存Conceptでカバー: llamacpp, vllm, a2a, acp, swarm, vellum, openlayer
  - 🗑️ スキップ（一般メディア・非AI）: the-verge, fortune, cnbc, cnn, theregister等 25件
  - 🗑️ arXiv-onlyスキップ: agentprm, merge-models
  - 詳細: wiki/bulk-processing/bulk-c3afd19.md
- ✅ Skeleton Enrich: refactoring-english (Michael Lynch, 11.8KB), gilesthomas (Giles Thomas/PythonAnywhere, 12.5KB), mahadk (Mahad Kalam, 12.4KB)

## [2026-04-30] AgentCraft Wiki Entity Page

- [[entities/agentcraft]] — New entity page: open-source AI agent orchestrator with RTS game interface. Built by Ido Salomon (@idosal1). Single-pane command center where AI agents appear as hero units on a 3D map. Supports Claude Code, OpenCode, Cursor. Key features: multi-agent heroes, fog of war, alliance hall, isolated containers, remote access, voice input, git worktrees.
- Raw article: raw/articles/2026-04-25-agentcraft-rts-agent-orchestration.md
- Sources: getagentcraft.com, getagentcraft.com/docs, Google Cloud Next speaker profile, X pinned post

## [2026-04-30] Will Brown — RL-Harness Lifecycle Thesis

- [[concepts/rl-harness-lifecycle]] — New concept page: the co-evolutionary cycle of harnesses and RL training. Strong agents emerge from: harnesses create training environments → RL produces capable models → models internalize harness patterns → more ambitious harnesses become possible.
- [[concepts/rl-harness-lifecycle]] — Key claims: "Harness paradigms evolve half a model generation at a time", "The best harness ideas don't work yet (but would be amazing if RL-trained)", bearish on "bolt-on memory" due to lack of clean rollout loop.
- [[concepts/rl-harness-lifecycle]] — CoT, ReAct, parallel tools, Claude Code, compaction, subagents, RLMs as historical examples of harness→RL internalization pipeline.
- [[concepts/rl-harness-lifecycle]] — "OpenClaw envs" interpreted as RL training environments modeled on real-world agent platforms.
- [[entities/will-brown]] — Added "The RL-Harness Lifecycle" section under Key Quotes with full analysis and cross-reference.
- [[entities/will-brown]] — Related links updated: added rl-harness-lifecycle concept, fixed broken wikilinks for agent-harness, prime-intellect, morgan-stanley.
- **Key architectural insight**: Products like Claude Code and OpenClaw are not final applications but prototypes for future training environments. The current awkward usage patterns are scaffolding for next-generation model capabilities. Bolt-on memory fails because "memory written → later used correctly → reward increased" causality is too noisy for RL.

## [2026-04-30] Agent around REPL: RLM Patterns on Pydantic AI

- [[concepts/code-mode]] — Added "Agent around REPL: 3つの実装パターン" (minimal CodeMode+output function, DSPy-compatible explicit loop, graph-native durable execution), "Agent around REPL vs Agent on REPL" architectural principle, and "Deferred Tool Calls" status update (HandleDeferredToolCalls in v0.2.0)
- [[concepts/pydantic-ai-harness]] — Added "公式インキュベータ兼roadmap" positioning, v0.x versioning policy details, CodeMode as RLM Foundation section, and deferred tool calls current status
- [[concepts/dspy-rlm.md]] — Added comparison table (DSPy.RLM vs pydantic-ai native RLM), cross-references to CodeMode/Monty/harness pages
- **Key architectural insight**: Monty is a REPL sandbox solution, not an agent host. The cleanest RLM implementation on pydantic-ai follows "Agent around REPL" — conversation control, output validation, approval, history management, and durability on the Pydantic AI side; code execution inside Monty. Three maturity tiers: (1) CodeMode + output function (recommended, minimal), (2) RunCode|FinalAnswer explicit loop (DSPy-compatible), (3) pydantic-graph nodes + Monty snapshots (production-grade, durable).

## [2026-04-30] Pydantic AI Harness — Runtime + Harness Full Stack Investigation

- [[concepts/pydantic-ai-harness]] — Fully expanded: capability model abstraction (`AbstractCapability`), full capability matrix (CodeMode ✅, FileSystem 🚧, Memory 🚧, Sub-agents 🚧, Guardrails 🚧, etc.), graduation model (harness → core), AICA "Ralph loop" workflow
- [[concepts/agent-architecture-decomposition]] — Added "Pydantic: The Full Stack (Runtime + Harness)" section: Monty as Open Runtime + pydantic-ai-harness as Open Harness, analogous to Kubernetes/containerd coupling
- [[concepts/code-mode]] — Added "Official Implementations" section with pydantic-ai-harness CodeMode details
- Raw article: raw/articles/2026-04-30_pydantic-ai-harness_capability-library.md

**Key finding**: Pydantic uniquely provides both Open Runtime (Monty) and Open Harness (pydantic-ai-harness) as an integrated stack. CodeMode requires Monty — the Harness decides *when* to write code, the Runtime executes it safely. Samuel Colvin's *"Start from nothing, then selectively grant capabilities"* applies to both layers.

## [2026-04-30] Harrison Chase's "Open Models / Open Runtime / Open Harness" Framework

- [[entities/harrison-chase]] — New entity page: LangChain CEO who articulated the three-layer agent architecture decomposition
- [[entities/nvidia-openshell]] — New entity page: NVIDIA OpenShell as the reference implementation of "Open Runtime"
- [[concepts/agent-architecture-decomposition]] — New concept page: Model/Runtime/Harness framework with detailed runtime→tool-use mapping
- [[concepts/harness-engineering]] — Updated with Open Models/Runtime/Harness section, runtime determines tool-use pattern table, heterogeneous agents + MCP as universal adapter

**Key architectural insight**: Runtime choice determines the native function-calling interface:
- **Agent on bash** → CLI tools are the natural function-calling mechanism
- **Agent on Python REPL** → Python functions are the natural mechanism (RLM, Pydantic AI)
- **Micro-VM Interpreter** → Dedicated bytecode VM with capability grants (Pydantic Monty)
- **Heterogeneous agents** → (Remote) MCP absorbs differences and bundles them, analogous to microservices with an API gateway

**Monty (Pydantic)**: Rust製ミニマルPythonインタープリタ。0.004ms起動、Deny-by-defaultセキュリティ。エージェントのために作られたRuntime — Tool CallingとSandboxの間に位置し、CodeMode（エージェントが1回のコード生成でループ・条件分岐・並列呼び出しを表現）を実現。

- Updated: wiki/index.md (3 new entries), wiki/log.md
- Sources: [Harrison Chase's X post](https://x.com/hwchase17/status/2034297125417460044), [LangChain Deep Agents](https://blog.langchain.dev/deep-agents/), NVIDIA OpenShell, [Pydantic Monty](https://pydantic.dev/articles/pydantic-monty), [RLM](https://alexzhang13.github.io/blog/2025/rlm/)

## [2026-04-30] Dropbox Dash Relevance Judge with DSPy

- **Source:** [How we optimized Dash's relevance judge with DSPy](https://dropbox.tech/machine-learning/optimizing-dropbox-dash-relevance-judge-with-dspy) — Dropbox Tech Blog, April 2026
- **Key findings:**
  - Dropbox Dash uses a relevance judge to score file/message relevance (1–5 scale)
  - **GEPA optimizer** for gpt-oss-120b adaptation: NMSE dropped 45% (8.83 → 4.86), adaptation time 2 weeks → 2 days
  - **MIPROv2** for gemma-3-12b: malformed JSON reduced 97% (358 → 9 invalid), NMSE 46.88 → 17.26
  - **Instruction Library Layer** for o3: human-curated rules + DSPy optimizer selection for safe incremental improvements
  - Key pattern: NMSE (Normalized Mean Squared Error) as metric for human-LLM alignment
- Raw article: raw/articles/2026-04-30_dropbox-tech-optimizing-dash-relevance-judge-with-dspy.md
- Updated: wiki/concepts/dspy.md (added Dropbox case study to Production Users), wiki/index.md, wiki/log.md

## [2026-04-30] Rivet — Docker Sandbox MicroVM API Research

- [[concepts/docker-sandbox-microvm-api]] — New concept page: reverse-engineered Docker Sandbox undocumented `sandboxd` API for kernel-isolated MicroVM execution
- [[entities/rivet-dev]] — New entity page: AI agent infrastructure company (agentOS, Sandbox Agent SDK)
- [[entities/nathan-flurry]] — New entity page: Co-founder & CTO of Rivet
  - **Source:** [We Reverse-Engineered Docker Sandbox's Undocumented MicroVM API](https://www.rivet.dev/blog/2026-02-04-we-reverse-engineered-docker-sandbox-undocumented-microvm-api/) — Nathan Flurry, 2026-02-04
  - **Key findings:** Docker Sandboxes use per-VM Docker daemons via Unix socket (`sandboxd.sock`), kernel isolation via MicroVMs (Apple Virtualization.framework / Hyper-V), outbound traffic through MITM filtering proxy at port 3128
  - **Sandbox Agent SDK:** Universal API for coding agents (Claude Code, Codex, OpenCode, Cursor, Amp, Pi) — write once, swap with config
  - **Comparison:** Related to [[concepts/agent-sandboxing-patterns]] (Browser Use's Unikraft approach) but different runtime target (Docker Desktop vs Unikraft/AWS)
  - New pages: concepts/docker-sandbox-microvm-api.md, entities/rivet-dev.md, entities/nathan-flurry.md
  - Raw article: raw/articles/2026-02-04_rivet-docker-sandbox-microvm-api.md
  - Updated: wiki/index.md (3 new entries), wiki/log.md

## [2026-04-30] ai-consulting-playbook | New concept page created
- [[concepts/ai-consulting-playbook]]
  - **Source**: https://567-labs.github.io/consulting/ (The AI Consulting Playbook by Jason Liu / 567 Studios)
  - **Key concepts**: Consulting flywheel (Content → Calls → Proof → Content), value-based pricing, situational assessment proposals, buyer qualification framework, content-as-strategic-friction
  - **Structure**: 7 parts covering mindset, content/lead gen, pricing, sales/discovery, proposals, engagement/scaling, business operations
  - New page: concepts/ai-consulting-playbook.md
  - Updated: wiki/index.md, wiki/log.md

## [2026-04-30] Agent Client Protocol (ACP)

- Created [[concepts/agent-client-protocol]]: Open standard (JSON-RPC 2.0) for editors/IDEs to interact with AI coding agents. Covers protocol lifecycle (initialize, session/new, session/prompt), methods (fs/read, fs/write, terminal/*, request_permission), notification types (plan, agent_message_chunk, tool_call, thought_message_chunk), and key implementations (Hermes ACP mode, Toad by Will McGugan). Updated [[concepts/agent-communication-protocols]] to distinguish Agent **Client** Protocol from Agent **Communication** Protocol (same acronym, different purpose).
- Raw article: https://www.philschmid.de/acp-overview

## [2026-04-30] ACP Naming Resolution + A2A Merger Documentation

- Renamed `agent-communication-protocols.md` → MCP vs A2A (removed ACP column)
- Merged former Agent Communication Protocol (IBM/I Am Bee) content into A2A section with merger details, timeline, and TSC members
- Updated `agent-client-protocol.md` with naming conflict warning and corrected comparison table
- Updated `agent-team-swarm/_index.md` and `agent-identity-verification.md` to replace ACP references with A2A
- Updated `entities/will-mcgugan.md` to correct ACP protocol reference
- Saved raw article: `2025-08-25_i-am-bee_acp-joins-a2a.md`
- Sources: https://github.com/orgs/i-am-bee/discussions/5, https://agentcommunicationprotocol.dev/introduction/welcome

## [2026-04-30] db9: Filesystem + Postgres for Agent Workflows

- Created [[concepts/db9-fs-sql-pattern]]: PostgreSQL distribution for agentic workloads that unifies file-based artifacts and relational metadata using SQL as the glue. Covers fs9 filesystem integration (read/write files, query CSV/JSONL/Parquet as relations), server-side embedding + pgvector HNSW search, and the compact RAG pipeline (source → chunk → retrieve → generate → output). Key benefit: "Why did the agent do that?" becomes a standard SQL query.
- Raw article: raw/articles/db9-fs-sql-patterns.md

## [2026-04-30] Zero Disk Architecture — Avi Kivity's database design paradigm

- Created [[concepts/zero-disk-architecture]]: Database design paradigm where all persistent state is offloaded to managed object storage (S3), achieving infinite scalability and serverless elasticity. Covers the LCD Model trade-off (Latency/Cost/Durability), enabling technologies (LSM Trees, Conditional Writes, S3 Express One Zone), and industry adoption (Snowflake, Neon, SlateDB, WarpStream).
- Created [[entities/avi-im]]: Avi Kivity — creator of KVM, QEMU contributor, systems infrastructure blogger. Key ideas: Zero Disk Architecture, S3 as "malloc of the web."
- Raw article: raw/articles/2024_avi-im_zero-disk-architecture.md

## [2026-04-30] Agent Sandbox Architecture — Browser Use production patterns

- Created [[concepts/agent-sandboxing-patterns]]: Browser Use's production agent sandboxing architecture (millions of concurrent web agents). Two patterns: isolate the tool vs. isolate the agent with control plane architecture and zero-secret sandboxes using Unikraft micro-VMs.
- Created [[entities/larsen-cundric]]: Browser Use's Founding Engineer, sole infrastructure engineer, authored the sandbox architecture article. Key achievement: migrated to AWS-native infra with 80% cost reduction and 3× latency improvement.
- Raw article: raw/articles/two-ways-to-sandbox-agents-2026-02-25.md

## [2026-04-29] Skeleton enrichment cycle — enriched 12 concept pages from skeleton/placeholder status to complete with research content and cross-links
|- Enriched [[concepts/agent-loop-orchestration]]: Added detailed content on reasoning-action loops, ReAct/plan-execute patterns, observability, and framework implementations
|- Enriched [[concepts/agent-orchestration-frameworks]]: Added comprehensive comparison of LangChain, AutoGen, CrewAI, Semantic Kernel, and Google ADK
|- Enriched [[concepts/ai-image-generation]]: Added evolution from GANs/VAEs to diffusion models (Stable Diffusion, DALL-E, Midjourney, Flux)
|- Enriched [[concepts/claude-code-best-practices]]: Added Anthropic's official best practices and community-accumulated patterns
|- Enriched [[concepts/claude-opus-4-7]]: Added model specs, benchmarks, architecture details, and context window information
|- Enriched [[concepts/local-llm/inference-hardware]]: Added consumer GPU guide with VRAM requirements and throughput comparisons
|- Enriched [[concepts/local-llm/ollama]]: Added full feature documentation, API reference, model management, and Ollama Python/Eino integration
|- Enriched [[concepts/monty-sandbox]]: Added Pydantic's Python sandbox by Samuel Colvin, code execution security model
|- Enriched [[concepts/nano-banana-2]]: Added Google's ultra-efficient image model (2B params), architecture and performance
|- Enriched [[concepts/openclaw-ecosystem]]: Added OpenClaw's open-source agent framework with ClawDBot and MoltBot
|- Enriched [[concepts/reverse-engineering]]: Added definition, tools (Ghidra, IDA Pro, Binary Ninja), and AI-RE convergence
|- Enriched [[concepts/memory-systems-bitter-lesson]]: New page on Rich Sutton's Bitter Lesson applied to agent memory systems
|- Updated index.md: +12 full entries, -4 stub entries (total: 671 pages, 642 full, 619 stubs)
|- Updated skeleton header count: 640 → 636

## [2026-04-29] dreaming | Consolidation cycle — updated gpjt.md with Part 32l IFT results and Landscape Hypothesis, added project-prometheus to index
- Updated [[entities/gpjt]]: Added Part 32l Instruction Fine-Tuning results, GPT-5.4 judge transition, and Landscape Hypothesis
- Added [[entities/project-prometheus]] to index.md (page created by Daily Active Knowledge Crawl but not yet indexed)
- Themes below threshold skipped (gumloop 0.48, ai-coding-best-practices 0.46, google-photo-scanning 0.42, bezos-project-prometheus 0.40)

### Created
- [[entities/alex-volkov]]: AI Evangelist at Weights & Biases, ThursdAI host
- [[entities/gergely-orosz]]: The Pragmatic Engineer newsletter author, Big Tech insights

### Updated
- [[entities/gpjt]]: Added Part 32l IFT results, GPT-5.4 judge transition, and Landscape Hypothesis (from dreaming cycle 2026-04-29T18:17)
- [[concepts/chatgpt-images-2.0]]: Updated with reasoning-before-generation feature
- [[concepts/google-photo-scanning-ai]]: Verified existing coverage of Personal Intelligence update
- [[entities/google-tpu]]: Already has TPU 8t/8i deep dive coverage
- [[concepts/tokenmaxxing]]: Cross-referenced with AINews Tasteful Tokenmaxxing coverage

### Articles Processed
- 17 newsletter articles collected (2026-04-22 to 2026-04-29)
- 2 new entity pages created
- 4 existing pages verified/updated

# Change Log

## [2026-04-30] X bookmarks ingest | Batch from 2026-04-28/29

### New Entity Pages Created:
- **entities/palantir.md** — AI-powered decision infrastructure. Palantir Ontology as enterprise agent workflow framework.
- **entities/mistral-ai.md** — French AI company. Workflows (enterprise orchestration) and Voxtral TTS releases.
- **entities/talkie.md** — Open-weight 13B historical LLM trained exclusively on pre-1930 data.
- **entities/david-duvenaud.md** — AI researcher, co-announced Talkie with Alec Radford and @status_effects.
- **entities/periodic-ai.md** — AI research company with physical lab for RL scaling (1T+ parameters).
- **entities/mimo.md** — Xiaomi's open-source LLM. MiMo-V2.5-Pro: 1.02T MoE (42B active), 1M context.
- **entities/supermemory.md** — Company building SMFS, agent-optimized filesystem replacing RAG pipelines.

### New Concept Pages Created:
- **concepts/smfs.md** — Supermemory Filesystem: mountable FS for AI agents, replaces UNIX ops with agent-aware alternatives.
- **concepts/mesa-filesystem.md** — Enterprise AI agent filesystem for artifacts beyond chat history.

### Pages Updated:
- **entities/hermes-agent.md** — Added "15 Features Deep Dive" section from viral X article (2791 bookmarks, 350K impressions)
- **entities/nvidia.md** — Updated Nemotron 3 Nano Omni details (30B params, 256K context, multimodal)
- **concepts/harness-engineering.md** — Added iii platform "The Harness Is the Backend" thesis (Worker/Trigger/Function primitives)

### Raw Articles Saved:
- 14 files in wiki/raw/articles/ (4 X-native articles + 7 tweet metadata + 3 external articles)

### Index Updated:
- Total pages: 671 → 678 (+7 new)
- Full entries: 642 → 649


> Chronological record of wiki changes, updates, and additions.
> See [[log-2026]] for entries before the rotation.

## [2026-04-29] blog-triage ingest | Batch from 20260427T081429Z checkpoint

- **Source:** [The Signal: OpenAI Is Cooking, The Anthropic Sweep, and SpaceX Courts Cursor](https://open.substack.com/pub/thesignal/p/openai-is-cooking-the-anthropic-sweep) — Updated [[openai-workspace-agents]] (GPT-5.5/Codex unification, World ID integration), updated [[openai]] entity (World ID, Codex merge)
- **Source:** [Xe Iaso: I don't know if I like working at higher levels of abstraction](https://xeiaso.net/blog/2026/ai-abstraction/) — Already covered in [[cognitive-debt]] (enriched with Xe Iaso source)
- **Source:** [Xe Iaso: Vibe Coding Trip Report](https://xeiaso.net/blog/2026/vibe-coding-sponsor-panel/) — Already covered in [[vibe-coding]]
- **Source:** [timsh.org: Switching to Claude Code + VSCode inside Docker](https://timsh.org/claude-inside-docker/) — Created [[ai-coding-workflows]] (Docker dev container patterns, security, credential management, Claude Code vs Cursor cost comparison)
- **Source:** [Simon Willison: Romain Huet quote](https://simonwillison.net/2026/Apr/25/romain-huet/) — Updated [[openai]] entity
- **Source:** [timsh.org: Why you should self-host your vibecoded app](https://timsh.org/why-you-should-self-host/) — Already covered in [[vibe-coding]]
- **Index:** Updated total pages (658 → 659)

## [2026-04-29] Symphony blog article ingestion

- **Source:** [OpenAI Engineering Blog: Open-Source Codex Orchestration — Symphony](https://openai.com/index/open-source-codex-orchestration-symphony/)
- **Updated:** concepts/openai-symphony.md (added 500% PR increase data, Codex App Server mode, economic shift analysis, lessons learned, updated status/frontmatter)
- **Saved:** wiki/raw/articles/openai-codex-orchestration-symphony.md (structured raw article)
- **Index:** Updated concepts/openai-symphony entry with Linear control plane and 500% PR increase summary
- **Created skill:** openai-blog-article-ingestion (standardized workflow for OpenAI blog ingestion)

## [2026-04-28] skeleton enrichment | 21 concept pages: skeleton→full (L3)
- **Batch:** Enriched 21 concept pages with substantive content via web research
- **Fixed broken frontmatter:** fine-tuning, multimodal, openclaw, sandbox, speech
- **Enriched 17-line skeletons:** mlx, langgraph, rags, cursor-ide, context-management, defense-in-depth, durable-execution, human-in-the-loop, self-learning-agents, tool-orchestration, dual-process-theory, clinical-ai, cloud-data-warehouses, data-engineering
- **Consolidated:** agent-memory.md → [[ai-agent-memory]] (redirect). Created comprehensive ai-agent-memory.md with two-camps framework
- **Sources:** Apple MLX docs, LangChain docs, Cursor docs, Anthropic engineering blog, Temporal docs, Kahneman dual process, FDA AI medical devices, Snowflake/BigQuery docs, Letta/Anthropic memory docs
- **Index:** Updated counts (stubs: 644→623, full entries: 604→625)

## [2026-04-28] blog-triage recovery | Batch from 2026-04-28_07-34-28 checkpoint

Previous triage agent had JSON parse error — recovered and processed directly.

**Take decisions:**
- Updated: concepts/harness-engineering/agentic-workflows/red-green-tdd.md (Martin Alderson's agentic TDD re-evaluation)
- Updated: concepts/cognitive-debt.md (Xe Iaso's AI abstraction cost essay — full enrichment)
- Created: concepts/agentic-sysadmin.md (Claude Code as sysadmin assistant pattern)
- Updated: concepts/agent-sandboxing.md (Docker isolation pattern from timsh.org)
- Updated: concepts/agentic-security.md (Nesbitt.io package security for AI agents)
- Updated: index.md (+1 new page entry, updated 3 existing entries)

**Reference decisions:**
- blog-34 (Telegram scam investigation) — interesting security methodology, skip
- blog-39 (Xe vibe coding sponsor panel) — already captured in vibe-coding.md
- blog-44 (Xe Claude Code April Fools) — already captured in xeiaso-net.md
- Various personal posts, non-AI tech content — skipped

**Skip decisions:**
- Joan Westenberg essays (general tech commentary, no specific AI relevance)
- Hugo Tunius privacy posts (pre-2026, historical only)
- Filfre.net gaming history (off-topic)
- John D. Cook math posts (peripheral AI interest only)
- Paul Graham essay archive dumps (already ingested via other means)
- Rakhim.exotext.com general software essays (no direct AI agent relevance)
- Miguel Grinberg SQLAlchemy series (off-topic)
- Giles Thomas LLM from scratch (interesting but peripheral)

- Sources: timsh.org (Docker isolation), martinalderson.com (agentic TDD, sysadmin pattern), xeiaso.net (abstraction costs), nesbitt.io (package security)

## [2026-04-28] newsletter ingest | Batch 2026-04-27/28

- Updated: concepts/gpt-5.5.md (agentic patterns: "I trust you" prompt, zero follow-up runs, Codex personality issues)
- Created: concepts/physical-ai.md (Physical AI vs Screen AI thesis, Applied Intuition platform, onboard vs offboard)
- Updated: entities/anthropic.md (Claude Design tool review, iteration speed vs Figma, GPT-Image-2 + Codex threat)
- Updated: entities/google.md (TPU v8 "Ironwood" chip independence, 8i vs 8t split, edge inference strategy)
- Updated: concepts/openai-symphony.md (OSS pipeline: Issue → Agent → PR → Human Review)
- Updated: concepts/agent-team-swarm.md (Sakana Conductor 7B, Kimi K2.6 300 parallel agents, 5-level autonomy model, orchestration patterns, agent economics)
- Created: concepts/agent-economics.md (1000x token multiplier, cost structure by autonomy level, value drivers)
- Updated: index.md (+2 new pages, counts updated)
- Sources: "How I AI" newsletter (GPT 5.5, Claude Design), AINews (ImageGen/AGI), Applied Intuition (Physical AI), Google (AI chip independence)

## [2026-04-28] Active Crawl [prerequisites + laterals] | context-engineering → kv-cache / harness-engineering → process-supervision / sandbox → capability-based-security

**Scope:** Daily active knowledge crawl based on hot-topics.yaml. Selected topics with last_crawled ≥ 3 days: context-engineering (prerequisites), harness-engineering (prerequisites), sandbox (laterals).

### Created: concepts/kv-cache.md
- **Parent topic:** context-engineering (prerequisites policy)
- **What:** KV Cache is the foundational optimization technique in transformer inference that stores intermediate attention computations, avoiding redundant recomputation. Understanding KV cache mechanics — size scaling (batch × layers × heads × d_k × sequence_length × precision), memory bandwidth bottleneck, and cache-aware scheduling — is a prerequisite for context engineering, prompt caching, and inference optimization.
- **Sources:** Sebastian Raschka (coding the KV cache from scratch), vLLM blog (KV cache crunching)

### Created: concepts/process-supervision.md
- **Parent topic:** harness-engineering (prerequisites policy)
- **What:** Process supervision is the infrastructure discipline of managing long-running AI agent processes — automatic restart on failure, health monitoring, supervised process trees, and cgroup-based resource control. A prerequisite for building reliable agent harnesses that must supervise subprocesses (tool execution, sandboxed code).
- **Sources:** Brightlume AI (long-running agents), OmniDaemon (PyPI), s6/skarnet documentation

### Enriched: concepts/capability-based-security.md (skeleton → full)
- **Parent topic:** sandbox (laterals policy)
- **What:** Capability-based security is an alternative security paradigm to ACLs/RBAC where authority is transmitted via unforgeable capabilities rather than identity-based checks. Applied to agent sandboxing, it enables fine-grained permissions without ambient authority. Merged from old skeleton (capabilities-based-security.md) into complete page.
- **Sources:** Wikipedia (capability-based security), Cowork Security Architecture (Medium)

### Files affected:
- Created: concepts/kv-cache.md
- Created: concepts/process-supervision.md
- Enriched: concepts/capability-based-security.md
- Deleted: concepts/capabilities-based-security.md (merged)
- Updated: index.md (+3 factual entries, -1 stub)
- Updated: hot-topics.yaml (last_crawled for context-engineering, harness-engineering, sandbox)
- Added: raw/articles/crawl-2026-04-28-kv-cache.md
- Added: raw/articles/crawl-2026-04-28-process-supervision.md
- Added: raw/articles/crawl-2026-04-28-capability-based-security.md

## [2026-04-29] newsletter ingest | Batch 2026-04-28/29

Processed triage checkpoint from newsletters dated 2026-04-28 and 2026-04-29.

### New Pages Created:
- **entities/gpt-5.5.md** — GPT-5.5 model entity (benchmarks, token efficiency, agentic patterns)
- **entities/poolside.md** — Poolside company entity with Laguna XS.2 and M.1 models (MoE architecture, open-weight release)
- **concepts/ai-agent-engineering.md** — Platform architecture for agent execution (Anthropic Managed Agents vs OpenAI Symphony)

### Pages Updated:
- **entities/openai.md** — Microsoft deal "breakup" details, new sources
- **entities/microsoft.md** — New entity page created (previously didn't exist)
- **entities/cursor-3.md** — SpaceX/xAI $60B option deal, funding round pause
- **entities/nvidia.md** — Nemotron 3 Nano Omni release details
- **concepts/gpt-5.5.md** — Benchmarks (Epoch Capabilities Index: 159, FrontierMath Tier 4), VibeBench, ParseBench
- **concepts/claude-managed-agents.md** — Public beta launch (April 2026), platform-level orchestration
- **concepts/harness-engineering.md** — Mistral Workflows public preview, Agentic Literacy section
- **concepts/serving-llms-vllm.md** — vLLM v0.20.0 TurboQuant 2-bit KV cache, DeepGEMM MoE kernels
- **index.md** — Added new entries, updated total page counts
- **log.md** — Appended this entry

### Sources Processed:
- [OpenAI Breaks Free From Microsoft](https://link.mail.beehiiv.com/v1/c/...) (2026-04-28)
- [Ben's Bites - Builders](https://substack.com/home/post/p-195538456) (2026-04-28)
- [AINews - Not Much Happened Today](raw/newsletters/2026-04-29-ainews-not-much-happened-today.md) (2026-04-29)

### Skipped:
- Couch-to-5K for AI (behavioral/habit content, not technical AI)
- Substack UI noise (like buttons, comment links, share links)

## [2026-04-29] Active Crawl [deepdive + deepdive + prerequisites] | ai-agent-engineering → Engineering Discipline Patterns / dspy → Khattab's Law / ai-memory-systems → Memory Scaling

**Scope:** Daily active knowledge crawl based on hot-topics.yaml. Selected topics with last_crawled ≥ 3 days:
- ai-agent-engineering (deepdive, high) — last_crawled 2026-04-25
- dspy (deepdive, high) — last_crawled 2026-04-25
- ai-memory-systems (prerequisites, medium) — last_crawled 2026-04-25

### Enriched: concepts/ai-agent-engineering.md (deepdive)
- **Parent topic:** ai-agent-engineering (deepdive)
- **Added:** "Engineering Discipline Patterns for AI Agents" section — Paul Duvall's 5 patterns (Specification-Driven, Codified Rules, Atomic Decomposition, Observable Development, Ralph Loops), XP revival in AI workflows (Red/Green/Refactor, trunk-based dev, plan mode), Shift-Left/Shift-Right feedback loops, evolution of engineering role toward "one pizza teams"
- **Source:** InfoQ / Paul Duvall (March 2026) — raw/articles/crawl-2026-04-29-paul-duvall-agentic-patterns.md

### Enriched: concepts/dspy.md (deepdive)
- **Parent topic:** dspy (deepdive)
- **Added:** "Khattab's Law: The Production Adoption Gap (2026)" section — the observation that any complex AI system rebuilds DSPy's abstractions ad hoc; canonical seven-stage evolution; production users (JetBlue, Databricks, Replit); download gap (4.7M vs 222M); adoption barriers (labeled data requirement, exploratory friction, lighter alternatives like LiteLLM, academic roots)
- **Source:** Agent Wars / Skylar Payne (March 24, 2026) — raw/articles/crawl-2026-04-29-dspy-adoption-gap-khattabs-law.md

### Created: concepts/memory-scaling.md (prerequisites)
- **Parent topic:** ai-memory-systems (prerequisites policy)
- **What:** Memory Scaling is a third scaling axis (alongside parametric and inference-time scaling) where agent performance improves via accumulated external memory. Introduced by Databricks AI Research (April 2026). The MemAlign framework distills episodic interactions into semantic rules, enabling smaller models with rich memory stores to outperform larger models.
- **Why it's a prerequisite:** Understanding why memory systems matter requires understanding the scaling dynamics they unlock — memory scaling explains the ROI of building persistent memory for AI agents.
- **Source:** Databricks Engineering Blog (April 10, 2026) — raw/articles/crawl-2026-04-29-databricks-memory-scaling.md

### Files affected:
- Created: concepts/memory-scaling.md
- Updated: concepts/ai-agent-engineering.md (added Engineering Discipline Patterns section)
- Updated: concepts/dspy.md (added Khattab's Law section, frontmatter sources)
- Created: raw/articles/crawl-2026-04-29-databricks-memory-scaling.md
- Created: raw/articles/crawl-2026-04-29-paul-duvall-agentic-patterns.md
- Created: raw/articles/crawl-2026-04-29-dspy-adoption-gap-khattabs-law.md
- Updated: index.md (+1 entry, total 660)
- Updated: config/hot-topics.yaml (last_crawled for ai-agent-engineering, dspy, ai-memory-systems)

## [2026-04-30] Slack historical message extraction (pre-3/30) — 6 AI Agent Architecture concepts

Processed Slack channel C077ACXR5UY messages from March 2026. Extracted 6 major architectural concepts and created/updated wiki pages.

### New Concept Pages Created:
- **[[concepts/functional-core-imperative-shell]]** — Architecture pattern separating deterministic, verifiable processing (functional core) from validation, evaluation, and strategic decision-making (imperative shell). As AI agents improve, work migrates from shell to core. Source: 3/30 23:54 "検証や評価や意思決定という、外界のモデリングしか残ってない"
- **[[concepts/reasoning-compression]]** — The principle that software complexity and reasoning requirements compress over time as models improve. Reasoning currently expanded across time as exploration will compress into direct solutions. Source: 3/30 23:56-57 "reasoningが時間軸方向に展開された探索空間として圧縮され"
- **[[concepts/agent-serverless]]** — Serverless deployment pattern for AI agents with built-in SaaS integration, permissions, and security. Enterprise tiers monetize log persistence and audit trails. Source: 3/24 19:06 "エージェントのサーバレスが今後育つとしたら、SaaS連携と権限とセキュリティの完備されたマネージド環境"

### Existing Pages Updated:
- **[[concepts/bitter-lesson-harnessing]]** — Added exact Slack quotes about harness complexity decreasing as models improve, and human role shifting from coder to PM
- **[[concepts/agent-iam]]** — Already had content from 3/24 message about Astrix Security, Zenity, WorkOS FGA
- **[[concepts/generative-app-evolution]]** — Already covered

### Index Updates:
- Added new "AI Agent Architecture Patterns" section to concepts/_index.md with all 6 concepts
- Cross-linked all 6 concepts to each other

## [2026-04-30] ingest | AINews: The Inference Inflection

**Source:** raw/newsletters/2026-04-30-ainews-the-inference-inflection.md ([AINews](https://www.latent.space/) by swyx)

Significant newsletter covering the industry-wide shift from training-dominant to inference-dominant AI workloads.

### Files updated:
- [[concepts/inference]] — Added "The Inference Inflection" section: Sam Altman "inference company" quote, Noam Brown "inference compute as strategic resource" quote, Jensen Huang's GTC 2026 inference inflection keynote, Intel CPU renaissance, FlashQLA linear attention, vLLM on Blackwell (230 tok/s DeepSeek V3.2)
- [[concepts/harness-engineering]] — Added "Agentic Harness Evolution" section: Terminal-Bench 2 69.7→77.0%, HALO recursive self-improvement (AppWorld 73.7→89.5), LangChain Deep Agents Harness Profiles, Cloudflare agents-as-customers
- [[concepts/openai-codex-superapp]] — Added Codex Platform Evolution: WebSocket mode (40% faster), $0 seat fee promotion, Auto-Review Mode (guardian agent), expansion to general work surface (research, spreadsheets, decision tracking)
- [[entities/cursor-3]] — Added Cursor SDK section: programmable agent infrastructure, CI/CD integration, embedded products
- [[entities/noam-brown]] — Added inference compute quote from GTC 2026
- [[entities/langchain]] — Updated Deep Agents section with Harness Profiles detail

### Other newsletters triaged (no wiki action taken):
- **"The Trial That Could Break OpenAI"** (beehiiv) — General news coverage of Musk v. OpenAI trial; journalistic, not wiki-worthy
- **"The product skill you must now master: Reinvention"** (The Skip by Nikhyl Singhal) — Career advice for product managers; outside wiki scope

- **Broken wikilinks:** 72 unique broken links detected (top offenders: agent-engineering, boris-cherny subpages, concepts/dspy-architecture/*, drew-breunig subpages, harness-engineering subpages)
- **Orphan pages:** 75 pages with zero inbound links (includes _index.md files, agent-memory.md, clinical-ai.md, etc.)
- **Missing from index:** 103 pages exist on disk but are not listed in index.md
- **Frontmatter issues:** 1 file missing frontmatter entirely (log-2026.md), 16 files missing `type` field
- **Stale raw articles:** 124 articles >30 days old by filename date; 1,950 total raw articles (32 berthub.eu political articles likely need cleanup)
- **Fixed:** Added `coding-agent` and `memory-system` to canonical tag taxonomy in SCHEMA.md (were being used but not declared)
- **Tag sprawl:** 1,524 tag uses not matching canonical taxonomy — need bulk cleanup or taxonomy expansion

## [2026-04-30] ingest | Tim Sh — AI Coding Workflows

**Source:** raw/articles/timsh.org--claude-inside-docker--6842418e.md, raw/articles/timsh.org--how-i-created-an-ethereum-proof-of-stake-demo-entirely-with---3d132b24.md

Processed two articles from timsh.org covering Claude Code in Docker isolation and Multi-LLM workflows.

### Files created:
- [[entities/tim-sh]] — Rewritten for timsh.org author (Tim Sh, PM/AI-coder). Covers Multi-LLM Role Separation, Docker isolation patterns, Ethereum PoS demo with Claude Code.
- [[entities/tim-sherratt]] — Created from old tim-sh.md content. Covers historian, GLAM hacker, GLAM Workbench creator. Moved to disambiguate from tim-sh.

### Files updated:
- [[concepts/ai-coding-workflows]] — Added "Multi-LLM Role Separation Pattern" section. Updated frontmatter (new tag: multi-llm, new source).
- [[SCHEMA.md]] — Added tags to taxonomy: multi-llm, workflow (Engineering category); blogger, developer-tooling (Meta category).
- [[index.md]] — Updated tim-sh entry with correct domain/description. Added tim-sherratt entry. Updated ai-coding-workflows description.

### Tagging changes:
- Added multi-llm, workflow, blogger, developer-tooling to SCHEMA.md taxonomy

## [2026-04-30] crawl | Daily Active Knowledge Crawl — Video Generation, AI Regulation, SLMs

**Active discovery crawl — identified and filled three major knowledge gaps not covered in hot-topics.yaml.**

### Files created:
- [[concepts/ai-video-generation-2026]] — Full concept page covering the 2026 landscape: Veo 3.1, Seedance 2.0, Kling 3.0, Runway Gen-4.5, Sora 2, Wan 2.6. Key trends: native audio generation, multi-shot storytelling, character consistency, 4K resolution, cost plunging to $0.022/sec. Open-source ecosystem (Wan series). Pricing comparison table.
- [[concepts/ai-regulation-2026]] — Full concept page covering 1,561 state AI bills in 2026, CA SB 53 (TFAIA) effective Jan 2026, NY RAISE Act amendments, EU AI Act timeline, UK non-legislative approach. Implications for developers: frontier AI frameworks, transparency requirements, incident reporting, model cards. Open questions on federal preemption.

### Files enriched:
- [[concepts/small-language-models]] — Upgraded from stub to full entry: key models (Phi-4, Llama 3, Qwen 2.5, TinyAgent, xLAM), SLM vs LLM comparison table, agentic SLMs (2026 trend with TinyLLM framework), hardware backends (CPU/GPU/NPU), use cases, limitations.

### Files updated:
- [[index.md]] — Added ai-video-generation-2026 and ai-regulation-2026 to Concepts section. Updated small-language-models description (removed TODO tag). Total pages: 710 | Full entries: 683 | Stubs: 619.

## [2026-04-30] searchcode.com — Code Intelligence for LLMs

- [[entities/searchcode-com]] — New entity page: code intelligence MCP server for LLMs. 6 MCP tools (code_analyze, code_search, code_get_file, code_get_files, code_file_tree, code_get_findings). Previously indexed 75B+ lines of code as a source code search engine (~2013–2025).
- [[entities/searchcode-com]] — Rebooted March 2026 as B2A (Business-to-Agent) service. World's first website with LLM testimonials. Claims 99% token reduction (267 MB raw code → 0.8 MB structured data).
- [[entities/searchcode-com]] — Powered by scc (Sloc Cloc and Code, 300+ languages) and cs (Code Spelunker). Free beta, REST API + MCP + Python SDK available. Enterprise: Docker + Helm for private repos.
- [[entities/ben-boyter]] — New entity page: Ben E. C. Boyter, Australian software engineer and creator of searchcode.com, scc, and cs. Author of the 'Marketing to the Machine' B2A thesis.
- [[entities/ben-boyter]] — 15+ years experience in testing, AWS, large-scale systems. Also created Bonzamate (Australian search engine), lc (License Checker), hashit. Blog at boyter.org.
- [[concepts/code-intelligence-for-llms]] — New concept page: providing LLMs with structured, pre-computed code analysis data via MCP/REST APIs. Replaces 'clone + cat' pattern. Canonical implementation: searchcode.com. Cuts token usage 99%.
- [[concepts/business-to-agent]] — New concept page: B2A paradigm where the primary user of a service is an AI agent/LLM. Coined by Ben Boyter. Services optimize for Context ROI (token efficiency). Contrasts with B2C model: MCP/API over UI, LLM testimonials over human testimonials.
- Raw article: raw/articles/2026-04-30-searchcode-com-code-intelligence-llms.md

---

## [2026-04-30] Dreaming Consolidation

- Updated [[entities/gpjt]] — Added Part 33 (Appendices reflection) with JAX follow-up milestone. Bumped updated date.
- Updated [[concepts/github-copilot-billing]] — Added Opus 4.7 multiplier promotional period note (ends April 30). Bumped updated date.
- Themes screened: 8 (3 scored ≥0.65, 3 scored 0.45-0.65, 2 skipped)
- 4 themes already well-covered by existing wiki pages; 2 minor updates applied

---

## [2026-04-30] RAG Is Not Dead — Added Part 6: Context Rot (Kelly Hong/Chroma)

- Created [[concepts/context-rot]] — The phenomenon where LLM performance degrades as input context length increases. Popularized by Kelly Hong (Chroma) in the "RAG Is Not Dead" series. Debunks NIAH benchmarks, documents distractor sensitivity (GPT hallucinates, Claude abstains), shuffled context paradox, and orchestrator pattern as mitigation.
- Updated [[concepts/rag-not-dead-series]] — Added Part 6 wikilink, detail section with Chroma experimental findings, graph query entry, and source. Fixed wrong wikilink to [[concepts/context-graph]] (enterprise decision traces) → [[concepts/context-rot]].
- Updated [[entities/hamel-husain]] — Added 2026 timeline entry for P6 publication, source reference.
- Saved raw article: `raw/articles/2026-04-30_hamel-husain-rag-p6-context-rot.md`
- Sources: https://hamel.dev/notes/llm/rag/p6-context_rot.html
- Updated index files: wiki/index.md, wiki/log.md.
## [2026-04-30] bookmark batch: Agent Engineering Guide 2026 + caching/memory/harness updates

- **New concept page**: [[concepts/agent-engineering-guide-2026]] — Comprehensive 30K-char guide: what to learn (context engineering, tool design, orchestrator-subagent, evals, harness, MCP, sandboxing), what to build with (LangGraph, MCP, Langfuse, E2B), what to skip (AutoGen, CrewAI, DSPy, autonomous agents, SWE-bench chasing, per-seat SaaS)
- **Updated**: [[concepts/prompt-caching]] — Claude Code production caching lessons: static-first layout, cache-safe plan mode, deferred tool loading, cache-safe compaction, monitor hit rate like uptime
- **Updated**: [[concepts/harness-engineering]] — Harness > Model principle, file-system-as-state pattern, production harness components stack (2026)
- **Updated**: [[concepts/ai-agent-memory]] — Mercury analysis: human vs. agent memory distinction, hybrid Markdown+structured architecture, five principles of serious agent memory
- **Updated**: [[entities/claude-code]] — Prompt caching architecture section, April 2026 regression postmortem reference
- **Saved**: 15 raw articles (8 X native articles + 1 Reddit + 6 tweet captures)
  - `raw/articles/2026-04-30_x--what-to-learn-build-skip-ai-agents.md` (30K chars)
  - `raw/articles/2026-04-30_x--lessons-claude-code-prompt-caching.md` (7.5K)
  - `raw/articles/2026-04-30_x--karpathy-second-brain-mercury.md` (6.3K)
  - `raw/articles/2026-04-30_x--your-agent-has-a-filesystem.md` (4.5K)
  - `raw/articles/2026-04-30_x--tuning-deep-agents-different-models.md` (4.0K)
  - `raw/articles/2026-04-30_x--prompt-auto-caching-claude.md` (3.5K)
  - `raw/articles/2026-04-30_x--naval-apple-dead-saas-next.md` (12.8K)
  - `raw/articles/2026-04-30_x--semantic-layer-2026.md` (6.5K)
  - `raw/articles/2026-04-30_reddit--pi-coding-agent-qwen-local.md` (3.5K)
  - + 6 tweet captures (HALO, SID-1, Dwarkesh lecture, local AI, shifting structures, Sequoia fireside chat)
- **Scored 16 bookmarks** against Karpathy's filter: 7 Tier 1 (3x compound topics), 5 Tier 2, 4 Tier 3
- **Karpathy filter alignment**: 5 bookmarks on context engineering (compound), 2 on tool design (compound), 1 on orchestrator-subagent (compound), 1 on eval discipline (compound)

---

## [2026-05-01] newsletter ingest | 2 newsletters: The Signal + Ben's Bites (triage recovery)

- Newsletter pipeline: newsletter-triage failed to produce valid JSON; wiki-ingest performed triage directly.
- Source 1: "How to run Claude Cowork from your phone" (The Signal, Alex Banks) — Paywalled; extracted Claude Dispatch concept (async agent orchestration from phone). Updated [[entities/alex-banks]].
- Source 2: "Building gets easier" (Ben's Bites, Ben Tossell) — Rich AI ecosystem roundup.

### New Pages Created
- [[concepts/agentic-commerce]] — ★★★★★ Stripe's Agentic Commerce Suite, ACP/SPT protocols, Link CLI agent wallet, Stripe Projects (Cloudflare co-design). Core concept for agent economy.
- [[entities/cloudflare]] — ★★★★☆ Agentic cloud infrastructure: Agents SDK, Project Think, autonomous account provisioning, Registrar API.
- [[entities/warp-terminal]] — ★★★☆☆ AI-native terminal open-sourced (AGPLv3), OpenAI founding sponsor, Oz orchestration platform.

### Updated Pages
- [[entities/alex-banks]] — Added Claude Cowork/Dispatch series timeline entry and agentic engineering relationship.
- [[entities/cursor-3]] — Added Ben's Bites source reference.
- [[entities/poolside]] — Added Ben's Bites source reference.

### Updated Index
- Total pages: 736 → 739
- Entities: 352 → 354 | Concepts: 391 → 392

