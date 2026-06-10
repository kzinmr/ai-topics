# Wiki Log Archive


## 2026-05-13 11:30 UTC — X Bookmarks Ingest

**Source**: X bookmarks pipeline (2 bookmarks, x-bookmarks-ingest cron)

### Pages Created
- 🆕 `entities/kyle-jeong.md` — Kyle Jeong entity page (Growth Engineer at Browserbase, writes about AI infra: Firecracker, agent sandboxing, Kubernetes)
- 🆕 `entities/david-fowler.md` — David Fowler entity page (Distinguished Engineer at Microsoft, Aspire, NuGet, SignalR)

### Pages Enriched
- ✏️ `concepts/firecracker.md` — Upgraded from stub (24 lines) to full page (~100 lines). Added architecture details, isolation problem analysis, agent infra company usage, Firecracker vs gVisor comparison table, history. Source: Kyle Jeong's X Article.

### Raw Articles Saved
- `raw/articles/2026-05-11_kylejeong_firecracker-agent-infra.md` — metadata-only (X Article behind auth wall, blog mirror not found)
- `raw/articles/2026-05-12_davidfowl_ai-made-us-faster.md` — metadata-only (X Article behind auth wall, no mirror found)

### Index Updates
- index.md: +3 indexed entries (firecracker concept, kyle-jeong entity, david-fowler entity)
- concepts: firecracker added
- Entities: kyle-jeong, david-fowler added

### Notes
- Both bookmarks were X native articles (x.com/i/article/...) with no external URLs. Blog mirror for Kyle's article could not be resolved (403/404). David Fowler's article has no mirror.
- Firecracker stub was already present (created 2026-04-25) — enriched rather than duplicated.

## 2026-05-13 10:00 UTC — INTELLECT-2 paper ingestion + model entity page

- **📄 Paper saved**: `wiki/raw/papers/2025-05-12_2505.07291_intellect-2-decentralized-rl.md` — arXiv:2505.07291 (May 12, 2025), 26 pages
- **📄 New model entity created**: `[[entities/intellect-2]]` — 32B reasoning model, first globally distributed RL training run. GRPO with two-sided clipping. Infrastructure: PRIME-RL + SHARDCAST + TOPLOC. 285K verifiable tasks (NuminaMath-1.5, Deepscaler, SYNTHETIC-1). Outperforms QwQ-32B. Apache 2.0. 14 co-authors including Fares Obeid (Grad).
- **📋 Prime Intellect page updated**: Upgraded Models section to INTELLECT-2/3 paper-compliant details. Added intellect-2 to ## Related Pages.
- **📋 Index updated**: Added intellect-2 entity (+1 page, +580 entities).

## 2026-05-13 09:45 UTC — Grad page consolidation: merge duplicate into entities/grad

- **🔄 Consolidation**: `@Grad62304977` 's duplicate page organized. 
 - **Deleted**: `entities/grad62304977.md` (33-line degraded copy) → consolidated into `entities/grad.md` (200-line canonical version)
 - **Deleted**: `concepts/fares-obeid-grad62304977.md` (24-line stub) → real name info already merged into entities/grad.md
 - ** updated **: `entities/grad.md` — `updated`date, `researcher`/`pseudonymous`/`reinforcement-learning` tags added, Prime Intellectcolleagues cross-link added 
 - ** fixed **: `entities/prime-intellect.md` — grad reference `[[entities/grad|Fares Obeid (Grad)]]` fixed 
- **📋 Index**: Removed grad62304977 entry, adjusted counts (-2 pages, -1 entry)
- **Lesson learned**: Must check for duplicates with `search_files` before creating wiki pages. entities/grad.md already existed under the filename `grad`.

## 2026-05-13 09:30 UTC — FIX: Restore overwritten Prime Intellect people pages

- **🔄 Overwrite restoration**: Restored 3 existing entity pages from git history with Prime Intellect cross-links only.
 - `[[entities/will-brown]]` — 203→206lines restored. vincent-weisser, florian-brand, elie-bakouch to cross-link added. 
 - `[[entities/florian-brand]]` — 183lines restored. ## Related People slots vincent-weisser, will-brown, elie-bakouch with filled. 
 - `[[entities/elie-bakouch]]` — 140→144lines restored. move to Prime Intellect reflected (formerly HuggingFace). ## Related Wikilinks for Prime Intellect colleagues added. 
- **⚠️ Lesson learned**: Always check for existing pages with `search_files` before creating pages. Check not just filenames but also index.md entries.
- **📋 SCHEMA updated**: `researcher`, `pseudonymous` tags added (continued from previous commit). 

## 2026-05-13 09:15 UTC — Prime Intellect people entity pages + cross-links

- **📄 New entity page created**: Created 5 entity pages for Prime Intellect team members, cross-linked to [[entities/prime-intellect]].
 - `[[entities/vincent-weisser]]` — Co-founder & CEO (@vincentweisser, 29K followers)
 - `[[entities/will-brown]]` — Research, "reward hacking" (@willccbb, 43.5K followers). PhD Columbia. prime-rl/verifiers creator.
 - `[[entities/florian-brand]]` — Research Engineer, evals (@xeophon, 13.2K followers). Interconnects editor.
 - `[[entities/elie-bakouch]]` — Training LLMs (@eliebakouch, 15K followers). Previously HuggingFace (SmolLM, FineWeb).
 - `[[entities/grad62304977]]` — Pseudonymous RL researcher (@Grad62304977, 9K followers). GRPO, reward engineering.
- **📋 Prime Intellect page updated**: Upgraded Key People section to full cross-links. Added all 5 members to ## Related Pages.
- **📋 Index updated**: Added 5 entities to index.md.

## 2026-05-13 11:00 UTC — Active Crawl | GNAP + AEM + InclusionAI Ring-2.6-1T (4 wiki pages + 3 raw articles)

- **📄 New concept pages created**: `[[concepts/gnap-git-native-agent-protocol]]` — Git-Native Agent Protocol: farol-team lightweight open-source protocol. Coordinates AI agent teams via 4 JSON files shared in a git repo. Zero server, zero database. Complementary with MCP/A2A.
- **📄 New concept pages created**: `[[concepts/aem-adaptive-entropy-modulation]]` — Baidu/Tsinghua 2026: Unsupervised credit assignment for multi-turn agent RL. Adaptively controls exploration/exploitation tradeoff via response-level entropy modulation. +1.4% on SWE-bench-Verified.
- **📄 New entity page created**: `[[entities/inclusionai]]` — AI company. Develops agent-optimized LLMs. Offers Ring model series for free on OpenRouter.
- **📄 New entity page created**: `[[entities/ring-2-6-1t]]` — 1T MoE reasoning model (63B active). For coding agents, tool use, long-duration tasks. Released May 8, 2026. Free on OpenRouter.
- **📄 Raw article saved**: `raw/articles/2026-05-13_gnap-git-native-agent-protocol.md`, `raw/articles/2026-05-13_aem-adaptive-entropy-modulation.md`, `raw/articles/2026-05-13_inclusionai-ring-2-6-1t.md`
- **📋 Index updated**: Added 4 pages to index.md. Updated section counts (Entities: 580, concepts: 1252).
- **🔍 Sources**: arXiv:2605.00425, github.com/farol-team/gnap, openrouter.ai/inclusionai/ring-2.6-1t:free

## 2026-05-13 09:00 UTC — Prime Intellect entity + renderers concept pages

- **📄 New entity page created**: `[[entities/prime-intellect]]` — Comprehensive entity page for Prime Intellect. Founded 2023, $20.5M raised (Founders Fund, Andrej Karpathy, Clem Delangue, Tri Dao). Lab (RL post-training platform), Environment Hub (2,500+ RL environments), Compute (distributed GPU marketplace). Open source: renderers, verifiers, prime-rl. INTELLECT-1/2/3 model series.
- **📄 New concept pages created**: `[[concepts/renderers-token-level-templating]]` — Detailed concept page for Prime Intellect's open-sourced token-level templating library. 3-stage evolution (MITO → Generic TITO → renderers), bridge_to_next_turn, 3x training efficiency, Token-In/Token-Out paradigm, harness boundary interactions.
- **📄 Raw article saved**: `wiki/raw/articles/2026-05-12_primeintellect_renderers-token-level-templating.md` — Full Prime Intellect blog post (22KB).
- **📋 SCHEMA updated**: `chat-template` tag Techniques category added. 
- **📋 Index updated**: Added entities and concepts to index.md.

## 2026-05-13 08:15 UTC — RLM v3 paper update and wiki refresh

- **Updated:** `wiki/raw/papers/2025-12-31_2512.24601_recursive-language-models.md` — Replaced v2 with v3 (May 11, 2026). Added: depth>1 experiments (depth=0-3), OpenCode & Claude Code baseline comparisons, MRCRv2 length generalization results, OOLONG prompting case study, expanded error analysis (§5 — syntax errors, decomposition mistakes, first-decomposition importance), 6-appendix summary, and full results tables for GPT-5 and Qwen3-Coder-480B-A35B.
- **Updated:** `wiki/concepts/rlm-recursive-language-models.md` — Version bumped to v3. Added: V3 New Findings section (Recursion Depth Scaling, OpenCode & Claude Code Comparisons, MRCRv2 Length Generalization, Error Analysis & Prompting Case Study), updated Benchmark Performance with full v3 tables (depth=0-3, OpenCode, Claude Code), updated RLM-Qwen3-8B training details, expanded Limitations (7 items with v3 context).
- **Key v3 findings:** Depth=3 achieves 76.0% on OOLONG-Pairs (31% improvement over depth=1); RLM training generalizes from 64K→1M context on MRCRv2; coding agents (OpenCode/Claude Code) lag far behind RLMs on information-dense tasks despite context offloading.
- **Sources:** arXiv:2512.24601v3

## 2026-05-12 07:50 UTC — Blog Wiki Ingest | 4 reference updates from blog triage

- Updated `concepts/harness-engineering/agentic-engineering.md`: Added "Emerging Practices (May 2026)" section with 3 subsections — James Shore maintenance cost economics (velocity gains must match inverse maintenance cost reductions), Shopify River Lehrwerkstatt case study (public-by-default agent interactions in Slack), LLM shebang pattern (plain-text as executable agent scripts). Added 3 raw article sources.
- Updated `entities/openai.md`: Added "ChatGPT Adoption Metrics (Q1 2026)" section — gender parity reached, 35+ age group gaining share, geographic spread into LatAm/APAC/Africa, health documentation as fastest-growing workplace task. Scope note: excludes Codex and enterprise. Added 1 raw article source.

- **2026-05-13**: Cross-synthesis enrichment — integrated Armin Ronacher's "Agents Built for Agents Building Agents" Pi philosophy (lucumr.pocoo.org, Jan 2026) with the Hugo+Ivan workshop pages. **Enriched concepts/agents-that-build-themselves.md**: added "Armin Ronacher's Perspective" section — session trees, extension state in sessions, no-MCP philosophy, write→reload→test→loop pipeline, Software Building Software lived experience. **Enriched entities/pi.md**: added "Agents Built for Agents Building Agents" section with session trees, extension state persistence, no-MCP philosophy, Armin quotes. **Enriched entities/armin-ronacher.md**: added "Pi Experience" section bridging Pi philosophy to Hugo+Ivan's Pure Python workshop. Source: raw article `lucumr.pocoo.org--2026-1-31-pi--0eb410a7.md` (already ingested).
## 2026-05-13 07:45 UTC — Lance Martin 'Learning the Bitter Lesson' ingested

## 2026-05-13 - Blog Ingest

### Updated Entity Pages
- **[ed-zitron](entities/ed-zitron.md)**: Added "Data Center Construction Investigation (May 2026)" section covering Zitron's investigative analysis of hyperscaler data center claims, finding significant discrepancies between announced and operational capacity. Microsoft's 4GW claim traced to only ~342MW verified. Stargate Abilene far below 1.2GW promised. CoreWeave contracted vs. operational power obfuscation pattern identified.
- **[jeff-geerling](entities/jeff-geerling.md)**: Added "Bambu Lab and Open Source Social Contract (May 2026)" section documenting Geerling's critique of Bambu Lab threatening an OrcaSlicer fork developer with legal action over AGPLv3-compliant code use. Louis Rossmann pledged $10K to defend the developer.
- **[simon-willison](entities/simon-willison.md)**: Expanded May 2026 Updates with Mitchell Hashimoto's TDM motivations analysis ("90% motivated by NOT GETTING FIRED") and Mo Bitar's "Ralph Loop" satire on enterprise AI adoption patterns.

- **Raw article saved**: `wiki/raw/articles/2025-07-30_rlancemartin_bitter-lesson-ai-engineering.md` — Lance Martin's blog post. Applies Rich Sutton's Bitter Lesson to AI engineering. open-deep-research case study (add structure → bottleneck → remove cycle). Hyung Won Chung's 'add structure then remove it later' framework.
- **📄 concept page enriched**: `[[concepts/rich-suttons-bitter-lesson]]` — stub → complete. Rich Sutton original (2019), historical case study table per domain, Hyung Won Chung framework, Lance Martin AI engineering application (open-deep-research case study), 3 practical lessons, agent harness implications.
- **📋 Entity updated**: `[[entities/lance-martin]]` — Added new raw article to sources.
- **📋 Index updated**: `wiki/index.md` `rich-suttons-bitter-lesson` added. 

## 2026-05-13 08:15 UTC — RLVR concept page + o1/o3 → GPT-5 consolidated timeline + MCP practical origins (3 new pages created)

- **📄 New concept pages created**: `[[concepts/rlvr]]` — Comprehensive RLVR concept page. Standard pairing with GRPO, test-time-scaling connection, verifier design space (3 types), ART·E $80 case study, o1→o3 10x RL compute scaling, comparison with RLHF/DPO. 27KB research base.
- **📄 New concept pages created**: `[[concepts/gpt/gpt-o-series-gpt5-unification]]` — Complete timeline: o1 (Sep 2024) → o3 (Dec 2024) → o3 cancelled on Altman roadmap shift (Feb 2025) → GPT-5 unification (Aug 2025). GPT-5 3-component architecture, strategic rationale (model picker complexity + DeepSeek R1 competition).
- **📄 New concept pages created**: `[[concepts/mcp]]` — Comprehensive MCP concept page. Two-layer origin story: David Soria Parra's personal frustration (copy-paste hell) and John Welsh's organizational chaos (integration chaos). M×N problem, 3 primitives, industry timeline.
- **🏷️ SCHEMA updated**: `rlvr`, `test-time-scaling` tag categories added to Techniques. 
- **📋 Index updated**: 3 entries added,, stale `mcp-protocol` + `model-context-protocol-mcp` consolidated replacement. 

## 2026-05-13 08:00 UTC — Lance Martin's AIE 2025 summary ingested + ambient-agentsconceptpage created 

- **Raw article saved**: `[[raw/articles/2025-06-10_rlancemartin_state-of-ai-agents-aie-2025]]` — AI Engineer World's Fair 2025 on-site report covering 5 major themes: mes: Ambient Agents, Agent UX/Bitter Lesson debate, Agent Training (RLVR, Art-E $80), Agent Tools (MCP origins), Agent Evaluation.
- **📄 New concept pages created**: `[[concepts/ambient-agents]]` — Asynchronous autonomous AI agent paradigm without chat UI. Devin, Codex, Windsurf, Claude Code examples, Solomon Hykes 4 requirements, AIE 2025 major theme.
- **✏️ Entity page enriched**: `[[entities/ai-engineer-youtube]]` — New Flagship Events section (World's Fair 2025 5-theme table + 2026 preview), sources/tags updated.
- **✏️ Entity page updated**: `[[entities/lance-martin]]` — Added AIE 2025 article to Blog/Recent Posts, updated tags/sources.
- **🏷️ SCHEMA updated**: `ambient-agents`, `agent-training` tag categories added to AI Agents. 

## 2026-05-13 07:40 UTC — AI Engineer YouTube channel added to monitoring targets 

- **🔧 Monitoring setup**: `config/feeds/blogs.opml` YouTube Channels section created and, AI Engineer (@aiDotEngineer) 's RSS feed added. `blogwatcher-cli add` with DB registration, first 15 items marked as read. 
- **📄 New entity page created**: `[[entities/ai-engineer-youtube]]` — 466K subscribers, 700+ talks. Official YouTube channel for AI Engineer conference series (World's Fair, Summit, Code).key talks, content themes, wiki relevance documented. 
- **📋 Index updated**: `wiki/index.md` entity added. 

## 2026-05-13 05:15 UTC — Claude Code Agent SDK session management + Context Engineering implementation analysis

- **Raw article saved**: `wiki/raw/articles/2026-05-13_anthropic_claude-code-agent-sdk-sessions.md` — Anthropic official documentation 'Work with sessions'. Persistence, restoration, and branching of conversation history via 3 operations: continue/resume/fork.`~/.claude/projects/<encoded-cwd>/*.jsonl` 's auto-persistence to, `ClaudeSDKClient` (Python), `continue: true` (TypeScript), cross-host session restoration. 
- **✏️ concept page enriched**: `[[concepts/harness-engineering/context-engineering]]` — Added new section "Claude Code Agent SDK: SDK ## Implementation of Context Engineering".Continue/Resume/Fork Martin 's Write/Select/Compress/Isolate framework mapped to. conversation status and file status's concern separation (Offload), Bitter Lesson's antithesis and action's foundation primitives' SDK absorption analysis. 
- **🔧 Entity page updated**: `[[entities/claude-code]]` — Added new Session Management section (Continue/Resume/Fork operation details, architecture mapping with Context Engineering framework, cross-host operation, design implications).sources and updated updated. 

## [2026-05-13] refactor | Harness Engineering blog unified boundary framing
- id: blog-harness-engineering-boundary-refactor-2026-05-13
- summary: Refactored the Harness Engineering survey around a unified boundary-interface framing, integrating Context Engineering, Action-oriented harness design, Agent Trace/Open Eval, open harness ownership, RLM-based learned context management, and anti-harness counterarguments into one coherent arc.
- touched:
 - [[blog/2026-05-12_hermes_harness-engineering-from-coding-agents-to-general-agents]]
 - [[concepts/harness-engineering]]
 - [[concepts/harness-engineering/context-engineering]]
 - [[concepts/rlm-recursive-language-models]]
 - [[concepts/unharnessed-agents]]

- **2026-05-13**: Discord user request → ingested Claude Code `/goal` documentation page. **New page**: `concepts/claude-code-goal.md` — Goal-driven autonomous workflow via prompt-based Stop hook + evaluator model (Haiku). Architecture comparison with Codex /goal, /loop, Stop hooks. Condition writing best practices. Lifecycle diagram. Non-interactive mode support. **Enriched**: `concepts/agentic-loop.md` — added Claude Code /goal as named variant in comparison table + ## Related concepts link. **Raw articles**: `2026-05-13_anthropic_claude-code-goal.md` (6.2KB). Index: +1 entry. Tags: claude-code, coding-agents, agent-loop, autonomous-agents, anthropic, prompt-caching, tool-use.

- **2026-05-13**: Discord user request → ingested "Build Your Own Deep Research Agent" workshop (Ivan Leo, Google DeepMind + Hugo Bowne-Anderson, Mar 2026). **New page**: `concepts/deep-research-agent-from-scratch.md` — 10-step build pipeline from raw Gemini API to full research agent with phase swapping (plan/execute modes), deterministic guardrails, dynamic subagent spawning (Exa parallel search), OpenTelemetry tracing. **Enriched**: `entities/ivan-leo.md` (added Deep Research Agent Workshop section with 10-step breakdown), `entities/hugo-bowne-anderson.md` (enhanced collaboration description). **Raw articles**: 2026-03-28_youtube_deep-research-agent-workshop.md (27.6KB), 2026-03-28_github_deep-research-agent-readme.md (2.3KB). Index: +1 page (1782→1783), +1 entry (836→837).
## 2026-05-13 04:50 UTC — Lance Martin Context Engineering for Agents raw article saved + concept page enriched + blog monitoring added + cross-links

- **Raw article saved**: `wiki/raw/articles/2025-06-23_rlancemartin_context-engineering-for-agents.md` — Lance Martin's milestone article on Context Engineering. Proposes 4-bucket classification (Write/Select/Compress/Isolate).Anthropic/Claude Code/Manus/Cognition/Windsurf/ChatGPT etc.'s real examples incorporating comprehensive framework. 
- **✏️ concept page enriched**: `[[concepts/harness-engineering/context-engineering]]` — Added new section for Lance Martin's Write/Select/Compress/Isolate 4-bucket classification.each bucket's details (Write: scratchpad+long-term memory, Select: tool selection RAG+memory search+knowledge selection, Compress: summarization+trimming, Isolate: multi-agent+sandbox+State separation) and Anthropic 3 strategies and correspondence table including. Further Reduce/Offload/Isolate to evolution mapping added. source: `raw/articles/2025-06-23_rlancemartin_context-engineering-for-agents.md`
- **🔗 Cross-links**: `[[concepts/reduce-offload-isolate]]` ↔ `[[concepts/harness-engineering/context-engineering]]` — 4 buckets→3 principles's evolution mapping bidirectional added 
- **🔧 Entity page updated**: `[[entities/lance-martin]]` — Added raw article to sources, bumped updated to 2026-05-13
- **📡 Blog monitoring added**: Lance Martin (`rlancemartin.github.io`) OPML + blogwatcher DB added. RSS feed: `http://rlancemartin.github.io/feed.xml`. Initial scan: 10 articles (marked as already read) 
- **Raw article saved**: `wiki/raw/articles/2026-01-09_rlancemartin_agent-design-patterns.md` — Lance Martin by Agent Design Patterns. Context Engineering 's as an extension of 7's design patterns (Give Agents A Computer, Multi-Layer Action Space, Progressive Disclosure, Offload Context, Cache Context, Isolate Context, Evolve Context) systematized. Manus's cache hit rateprimary metric, Ralph Wiggum loop, RLM by context management absorption prediction etc. including. source added : `[[concepts/harness-engineering/context-engineering]]`, `[[concepts/reduce-offload-isolate]]`, `[[entities/lance-martin]]`

## 2026-05-13 04:55 UTC — Jeff Huber / Harness Engineering interview ingested + Inner/Outer Loop Extension

- **Raw article saved**: `wiki/raw/articles/2026-03-04_hugobowne_harness-engineering-agent-context.md` — Hugo Bowne-Anderson's Vanishing Gradients article. Jeff Huber (Chroma CEO) on context engineering > prompt engineering, large context windows's limits, agent harness = tools+sub-agents+workflows, code writing emergent reasoning unlocks, Inner Loop / Outer Loop framework. 
- **🆕 Entity page created**: `[[entities/jeff-huber]]` (L2) — Comprehensive page for Chroma CEO & Co-founder.Standard Cyborg (YC W15) → Chroma ($18M seed) 's background, Context Engineering > Prompt Engineering 's redefinition, Inner/Outer Loop framework, code writing by emergent reasoning thesis, practical builder advice (Hybrid Search / Golden Dataset / Cluster Analysis / Tool Engineering). 
- **✏️ concept page strengthened**: `[[concepts/reduce-offload-isolate]]` — Added new section for Jeff Huber's **Inner Loop vs Outer Loop** extension.Inner Loop = Reduce/Offload/Isolate per-task basis with applied to, Outer Loop = context filling over time improves system ("machine that builds the machines"). evaluation's open questions also noted. 
- **✏️ Cross-links**: `[[entities/hugo-bowne-anderson]]` — Wikilinked Jeff Huber in Key Collaborations table to [[entities/jeff-huber]].
- **Index updated**: jeff-huber entities section added (jeff-geerling and jensen-huang 's between). Total pages: 1783→1784, Indexed entries: 837→838, Entities: 558→559. 
## [2026-05-13] enrich | Agentic Search: Berryman 5-Level Model + Revealed Preferences + Ep.68
- id: concept-agentic-search-berryman-ep68-2026-05-13
- summary: Saved 3 raw articles (Berryman's 5-level maturity model blog, Turnbull's LLM-judges critique, Ep.68 show notes). Added two major sections to [[concepts/agentic-search]]: "Berryman's 5-Level Agentic Search Maturity Model" (Level 0-4: Trad Search → Beginner AI → Intermediate AI → Conversational Assistant → Async Research Agent) with comparison table vs 3-level framework, and "Revealed Preferences: The Fundamental Limit of LLM-as-Judge" (engagement blindness, hard negative blindness, sneaky overfitting, LLMs-as-analysts-not-judges). Added Jan 2026 blog post entry to [[entities/john-berryman]]. Cross-linked with [[concepts/llm-as-judge]].
- touched:
 - [[concepts/agentic-search]]
 - [[entities/john-berryman]]
 - raw/articles/2026-01-18_arcturus-labs_incremental-ai-adoption-ecommerce-5level.md
 - raw/articles/2026-01-23_vanishing-gradients_ep68-builders-guide-agentic-search.md
 - raw/articles/2025-11-02_softwaredoug_llm-judges-arent-the-shortcut.md
## 2026-05-13 04:30 UTC — Lance Martin Reduce/Offload/Isolate frameworkingested

- **Raw article saved**: `wiki/raw/articles/2025-12-12_hugobowne_agent-harness-context-engineering.md` — Hugo Bowne-Anderson + Duncan Gilchrist's Vanishing Gradients article.Lance Martin (Anthropic, at LangChain during recording) on 3 principles of context engineering from High Signal podcast, Bitter Lesson's harness design applied to, Manus 5 redesigns / Anthropic's Claude Code harness reduction's testimony. 
- **🆕 concept page created**: `[[concepts/reduce-offload-isolate]]` (L2) — Detailed framework for Reduce (context compression) / Offload (move outside prompt) / Isolate (sub-agent delegation).Bitter Lesson and connection, Write-Select-Compress-Isolate from evolution, Manus/Claude Code/Open Deep Research's real examples, harness design to implications including. 
- **✏️ Entity strengthened**: `[[entities/lance-martin]]` — Added High Signal podcast appearance to Podcast Appearances. Created dedicated Reduce/Offload/Isolate framework section.updated: 2026-05-13. 
- **✏️ Cross-links**: `[[entities/hugo-bowne-anderson]]` — Wikilinked "Reduce, Offload, Isolate" in Harness Engineering Philosophy section to [[concepts/reduce-offload-isolate]].
- **Index updated**: concepts/reduce-offload-isolate added. Total pages: 1782→1783, Indexed entries: 836→837, concepts: 1249→1250. 
- **2026-05-13**: Discord user request → ingested 'Agents That Build Themselves' content from 3 sources: Substack article (Hugo Bowne-Anderson, Feb 2026), YouTube workshop (96min live build with Ivan Leo), GitHub repo (build-your-own-ai-assistant). **New pages**: `concepts/agents-that-build-themselves.md` (Level 5: Self-Modification pattern — factory + hot reload + hooks + markdown memory), `entities/ivan-leo.md` (Ivan Leo — Google DeepMind, ex-Manus). **Enriched**: `concepts/self-evolving-agents.md` (added Level 5: Self-Modification with code example), `entities/openclaw.md` (added Core Architecture Patterns: hooks, memory compaction, tool factory + self-extension), `entities/hugo-bowne-anderson.md` (added build-your-own-ai-assistant repo). **Raw articles**: 2026-02-28_substack_agents-that-build-themselves.md (18KB), 2026-02-28_youtube_openclaw-from-scratch-workshop.md (33KB). Index: +2 pages (1780→1782), +2 entries (834→836).
## [2026-05-13] enrich | Agentic Search: Long-Running Agents & RLM practitioner perspective
- id: concept-agentic-search-rlm-practitioner-2026-05-13
- summary: Added "Long-Running Agents and Recursive Language Models" section to [[concepts/agentic-search]] from Doug Turnbull's Feb 2026 Vanishing Gradients interview. Documents the practitioner's RLM vision: context-as-variable, context-as-search-index, 4-stage evolution (linear history → compaction → context-as-variable → context-as-world). Includes comparison table (Academic RLM vs Turnbull's Practitioner Framing), OpenClaw self-extending loop example, and cross-links to [[concepts/rlm-recursive-language-models]], [[concepts/code-mode]], [[concepts/context-fragments]].
- touched:
 - [[concepts/agentic-search]]
## [2026-05-13] enrich | Agentic Search: In-Prompt RL section + Hugo Bowne-Anderson annotated talk
- id: concept-agentic-search-in-prompt-rl-2026-05-13
- summary: Saved Hugo Bowne-Anderson's annotated Substack transcript of Doug Turnbull's "How To Build Your First Agentic Search Application" talk as raw article `2026-02-21_hugobowne_how-to-build-first-agentic-search.md`. Added new "In-Prompt Reinforcement Learning" section to [[concepts/agentic-search]] covering the validator-as-dissatisfied-user pattern, RLHF vs in-prompt RL comparison table, validator taxonomy (LLM-as-Judge, reranker, rule-based, domain model), and connection to the broader harness architecture. Updated concept page sources and date.
- touched:
 - [[concepts/agentic-search]]
 - raw/articles/2026-02-21_hugobowne_how-to-build-first-agentic-search.md
## [2026-05-13] update | John Berryman entity + Unharnessed Agents concept + Arcturus Labs blog tracking
- id: entity-john-berryman-unharnessed-agents-2026-05-13
- summary: Created [[entities/john-berryman]] entity page (L2, Arcturus Labs founder, ex-GitHub Copilot engineer, author). Created [[concepts/unharnessed-agents]] concept page documenting Berryman's anti-harness thesis ("agent harness" is wrong frame, agents should leave the IDE, skills are new programs). Updated [[concepts/harness-commoditization]] with comparative analysis table (Amp vs Berryman). Saved raw article `2026-04-24_arcturus-labs_unharnessed-agents.md`. Added Arcturus Labs to blogwatcher DB + OPML with RSS feed. Moved from concepts/john-berryman.md stub. Fixed Doug Turnbull entity wikilink.
- touched:
 - [[entities/john-berryman]]
 - [[concepts/unharnessed-agents]]
 - [[concepts/harness-commoditization]]
 - [[entities/doug-turnbull]]
 - [[config/feeds/blogs.opml]]

## [2026-05-13] update | Hugo Bowne-Anderson entity enrichment + duplicate merge + x-accounts
- id: entity-hugo-bowne-anderson-enrichment-2026-05-13
- summary: Enriched [[entities/hugo-bowne-anderson]] (L3) with Privacy Engineering section (from "15 Privacy Questions" with Katharine Jarmul) and Agent Harness Engineering section (Harness Reading List, Lance Martin's Reduce/Offload/Isolate, Jeff Huber context engineering, Ivan Leo self-extending agents, Doug Turnbull agentic search). Added 5 new ## Related People. Merged and deleted duplicate [[entities/hugo-bowne]] stub. Added @hugobowne to x-accounts.yaml. Fixed wikilink in concepts/ai-safety.md.
- touched:
 - [[entities/hugo-bowne-anderson]]
 - [[entities/hugo-bowne]] (deleted)
 - [[concepts/ai-safety]]
 - [[config/feeds/x-accounts.yaml]]

## [2026-05-13] update | Max Rumpf entity page + SID-1 concept page created
- id: entity-max-rumpf-sid-1-2026-05-13
- summary: Created [[entities/max-rumpf]] (L2, CEO/Co-founder SID.ai, SID-1 developer) and [[concepts/sid-1]] (L2, first RL-trained agentic retrieval model). Added @maxrumpf to x-accounts.yaml. Web-sourced from maxrumpf.com, sid.ai, X, LinkedIn, YC, podcasts.
- touched:
 - [[entities/max-rumpf]]
 - [[concepts/sid-1]]
 - [[config/feeds/x-accounts.yaml]]

## [2026-05-13] update | Harness Engineering blog context/action synthesis
- id: blog-harness-engineering-context-action-synthesis-2026-05-13
- summary: Strengthened the Harness Engineering survey with a Context-axis/Action-axis synthesis, Lance Martin's Reduce/Offload/Isolate framing, RLM-based learned context management, and anti-harness/commoditization counterarguments.
- touched:
 - [[blog/2026-05-12_hermes_harness-engineering-from-coding-agents-to-general-agents]]
 - [[concepts/harness-engineering/context-engineering]]
 - [[concepts/reduce-offload-isolate]]
 - [[concepts/rlm-recursive-language-models]]
 - [[concepts/unharnessed-agents]]
 - [[concepts/harness-commoditization]]
