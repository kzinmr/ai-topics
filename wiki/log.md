## [2026-05-14] create | Concept: Prime-RL Post-Training for Subagents (Ramp Labs Fast Ask)

### Pages Created
- `concepts/prime-rl-post-training.md` — Ramp Labs Fast Ask case study: RL post-training (GRPO) for specialized retrieval subagents using Qwen3.5-35B-A3B + Prime Intellect platform. Beats Claude Opus 4.6 by 4pp at Haiku 4.5 latency. Covers adversarial workbook design, reward function design, async off-policy RL.

### Pages Updated
- `wiki/index.md` — Added prime-rl-post-training to Concepts section.

### Raw Source
- `raw/articles/2026-05-07_RampLabs_building-fast-accurate-agents-with-prime-rl-post-t.md`

## [2026-05-14] create | Concept: The 2026 AI Engineer Roadmap

### Pages Created
- `concepts/ai-engineer-roadmap-2026.md` — The 2026 AI Engineer Roadmap by Rohit (@rohit4verse): 5 production-grade projects to bridge the $150K gap between prompt engineers and systems architects.

### Pages Updated
- `wiki/index.md` — Added ai-engineer-roadmap-2026 to Concepts section.

### Raw Source
- `raw/articles/2026-01-09_rohit4verse_the-2026-ai-engineer-roadmap.md`

## [2026-05-14] ingest | X Bookmarks: ntn (Notion CLI) + Codex Memory Pipeline

### Pages Created
- `concepts/notion-cli.md` — Notion CLI (ntn): official CLI for Notion API, Workers, file uploads. Announced May 2026 by @NotionDevs. Designed for devs and AI coding agents.

### Pages Updated
- `concepts/agent-memory-engineering.md` — Added Codex Memory Pipeline deep dive (Mem0, May 2026): two-phase async pipeline, markdown storage format, grep-based recall, caps & sweeps, geographic constraints, "where it stops" analysis.

### Raw Articles Saved
- `raw/articles/2026-05-13_notion-cli-ntn-developer-docs.md` — developers.notion.com overview
- `raw/articles/2026-05-08_mem0-how-memory-works-in-codex-cli.md` — mem0.ai blog by Himanshu Sangshetti

### SCHEMA.md
- Added canonical tags: `notion-cli`, `notion-mcp`

# Wiki Log

> Chronological record of all wiki actions. Append-only.
> Format: `## [YYYY-MM-DD] action | subject`
> Actions: ingest, update, query, lint, create, archive, delete
> When this file exceeds 500 entries, rotate: rename to log-YYYY.md, start fresh.

## [2026-05-14] active-crawl | LangChain Harness Profiles, Delta Channels, ServiceNow Build Agent, Coder Agents Update, Snyk-Claude Security

### Pages Created
- `concepts/harness-profiles.md` — Model-specific agent tuning (prompts, tools, middleware) per LLM family. LangChain Deep Agents feature, 10-20pt tau2-bench gains.
- `concepts/delta-channels.md` — LangGraph DeltaChannel (beta v1.2) — incremental checkpoint storage for long-running agents. Bounds resume costs for production agents.
- `entities/servicenow.md` — ServiceNow enterprise platform. Build Agent (May 2026): natural language app creation with Anthropic models, multi-IDE support, governed by default.
- `entities/snyk.md` — Snyk developer security platform. Claude integration (May 2026) for AI-powered vulnerability discovery and automated remediation.

### Pages Updated
- `entities/langchain.md` — Added Harness Profiles and Delta Channels sections to history and architecture. Updated tags (deep-agents, state-management). Added tau2-bench benchmark data.
- `entities/coder.md` — Updated Coder Agents section with market stats (61% adoption, 70% infra mismatch) and beta pricing details.

### Raw Articles Saved
- `raw/articles/2026-04-29_langchain-harness-profiles.md` — LangChain blog: Tuning Deep Agents for Different Models
- `raw/articles/2026-05-12_langchain-delta-channels.md` — LangChain blog: Delta Channels for Long-Running Agents
- `raw/articles/2026-05-06_servicenow-build-agent.md` — BusinessWire: ServiceNow Build Agent launch
- `raw/articles/2026-05-06_coder-agents-beta-enterprise.md` — CityBiz: Coder self-hosted AI coding agents
- `raw/articles/2026-05-08_snyk-claude-security-partnership.md` — Booboone: Snyk-Claude Security integration

### Sources
- https://blog.langchain.dev/tuning-deep-agents-different-models/
- https://www.langchain.com/blog/delta-channels-evolving-agent-runtime
- https://www.businesswire.com/news/home/20260506008934/en/
- https://www.citybiz.co/article/842905/coder-launches-self-hosted-ai-coding-agents-for-enterprise-development-teams
- https://booboone.com/may-8-2026-ai-updates-from-the-past-week-coder-agents-launch-snyk-claude-partnership-opsera-cursor-partnership-and-more/

---

## [2026-05-14] create | Concept: Cognitive Surrender

### Pages Created
- `concepts/cognitive-surrender.md` — 認知的サレンダー概念ページ。Addy Osmani (May 2026) + Shaw & Nave (Wharton 2026) の実証研究に基づく。AIの出力を無検証で自分の出力として受け入れる心理的メカニズム。[[concepts/simulacrum-of-knowledge-work]]（組織レベルのシミュラークル化）と[[concepts/cognitive-debt]]（個人レベルの認知負債蓄積）の両方に深く接続。

### Pages Updated
- `entities/addy-osmani.md` — Cognitive Surrenderコンセプトへのリンク説明を詳細化。シミュラークルと認知負債の話と接続。
- `concepts/simulacrum-of-knowledge-work.md` — Related Conceptsにcognitive-surrenderを追加。「シミュラークルは組織現象、cognitive surrenderはそれを生む個人の心理的失敗モード」という接続。
- `concepts/cognitive-debt.md` — Related Conceptsにcognitive-surrenderを追加。cognitive surrender が cognitive debt の蓄積メカニズムであることを明示。
- `raw/articles/2026-05-05_addyosmani_cognitive-surrender.md` — サマリーから完全版に置換（41行→フル記事）。

### Sources
- https://addyosmani.com/blog/cognitive-surrender/
- https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6097646 (Shaw & Nave, Wharton 2026)

---

## [2026-05-14] enrich | Blog Wiki Ingest: Sierra τ-knowledge benchmark

### Pages Updated
- `entities/sierra.md` — Added "Research & Benchmarks" section covering τ-Knowledge / τ-Banking benchmark. Key data: GPT-5.5 xhigh leads at 37.4% pass^1 (up 11.9pt from GPT-5.2), ~63pt headroom remains, behavioral insights on smarter search patterns (9.1 vs 19.4 queries/task). Added sources, benchmark/evaluation/research tags, and cross-references to concepts/tau-knowledge and concepts/tau-bench.

---

## [2026-05-14] ingest | Newsletter Wiki Ingest: AINews "Codex Rises, Claude Meters Programmatic Usage"

### Pages Created
- `concepts/mandate-equinox.md` — Mandate Equinox: OpenAI-Anthropic 6ヶ月交代サイクル概念。DanB (@irl_danB) 提唱。

### Pages Updated
- `entities/claude-code.md` — Added "Programmatic Usage Metering (May 2026)" section. Anthropicが$200サブスクリプションに$200 APIクレジットを付与。Claude Agent SDK/claude -p/サードパーティハーネス利用が正式メータリング対象に。
- `entities/openai-codex.md` — Added "Growth Metrics" section. Codex 300万WAU (April 8)、400万WAU (April 22) の成長データ。

### Sources
- AINews "Codex Rises, Claude Meters Programmatic Usage" (May 14, 2026)
- @ClaudeDevs pricing announcement (May 13, 2026)
- Sam Altman Codex 3M WAU announcement (April 8, 2026)
- WSJ Codex 4M WAU report (April 22, 2026)

## [2026-05-14] ingest | Blog scan: 36 articles (20 saved, 16 skipped)

### Major AI articles processed:

1. **Sierra τ-knowledge leaderboard update (May 2026)** — Updated concepts/tau-knowledge.md with GPT-5.5 pass^1/pass^4 results (37.4%/20.6%), behavioral analysis of search patterns, and pass^1 metric clarification. GPT-5.5 achieved 2x improvement in pass^4 over GPT-5.2 but still ~63pt from saturation. Key insight: stronger agents search smarter (fewer, more surgical queries) not more.

2. **OpenAI Codex Windows Sandbox** — Updated entities/codex.md with Windows sandbox architecture details. Two-prototype evolution from unelevated to elevated sandbox using dedicated local users, Windows Firewall for network isolation, 3-binary architecture (codex.exe → setup.exe → command-runner.exe) to cross UAC boundary.

3. **OpenAI TanStack Supply Chain Attack (Mini Shai-Hulud, May 2026)** — Created concepts/openai-tanstack-supply-chain-2026.md. Two infected corporate devices, code-signing cert compromise, 108 internal source repos accessed, limited credential exfiltration, full certificate rotation. Updated entities/openai.md.

4. **Sierra τ-knowledge blog** — Referenced as primary source for tau-knowledge.md updates. Key finding: strongest model (GPT-5.5 xhigh reasoning) gets 37.4% pass^1 on realistic customer service tasks with full documentation access — agent capabilities still far from production-ready for knowledge work.

### Other articles saved (not AI-relevant):
- pluralistic.net: "vibe governance" — Cory Doctorow on AI solipsism and fascist paradigm (noted, pluralistic-net.md entity updated)
- danieldelaney.net: "Ideal failures" — UI design philosophy (Daniel De Laney entity exists)
- nesbitt.io: "Showing Our Work" — Open source dependency validation research
- susam.net: commenting guidelines
- shkspr.mobi: SVG sparklines
- troyhunt.com: Have I Been Pwned Bahamian Government
- rachelbythebay.com: HTML generation
- devblogs.microsoft.com/oldnewthing: Windows keyboard layout hang
- dfarq.homeip.net: Kevin O'Leary Shark Tank
- buttondown.com/hillelwayne: measurement units
- tedium.co: BuzzFeed Byron Allen analysis
- seangoedecke.com: space AI datacenters cooling
- dynomight.net: slide decks
- idiallo.com: "Software Engineers are Obsolete"
- simonwillison.net: Datasette blog launch + Boris Mann quote
- evanhahn.com: Firefox extension (not saved — not AI-relevant)

- Updated: tau-knowledge.md, codex.md, openai.md, pluralistic-net.md
- Created: openai-tanstack-supply-chain-2026.md
- Updated: index.md (+1 concept, +2 entity references)
- Updated: log.md

## [2026-05-14] ingest | Show Us Your Agent Skills Ep.1 + Agentic Engineering article
- Ingested Hugo Bowne-Anderson's Substack article "Agentic Engineering and the Lost Art of Verification" (2026-05-12)
- Ingested YouTube transcript for "Show Us Your (Agent) Skills Episode 1" with Wes McKinney, Jeremiah Lowin, Randy Olson (2026-05-08)
- Created entity pages: hugo-bowne-anderson.md, thomas-wiecki.md (completed; wes-mckinney, jeremiah-lowin, randy-olson created by subagents)
- Created concept page: concepts/agentic-engineering.md — from vibe coding to verified agent workflows, generator-evaluator patterns
- Updated index.md with new entries

## [2026-05-14] create | comparisons/open-harness-vs-agent-framework + enrich concepts/agent-harness
- Saved raw analysis: `raw/articles/2026-05-14_kzinmr_open-harness-vs-agent-framework.md` — kzinmr による Open Harness 対 Agent Framework/SDK の包括比較レポート
- Created comparison page: `comparisons/open-harness-vs-agent-framework.md` (16 pages) — Open Harness（OpenClaw, Hermes Agent, OpenCode, Pi）と Agent Framework/Runtime（Claude Agent SDK, OpenAI Agents SDK, Google ADK, Strands Agents, LangGraph, Pydantic AI）の本質的差異を投資対象として整理。Operator Workbench Readiness vs Untrusted Product Runtime Readiness の2軸評価、4種類のロックイン分析、推奨分離アーキテクチャ、実務選定指針を含む
- Enriched `concepts/agent-harness.md` — 「Agent Harness と Agent Framework/SDK の本質的差異」セクション追加（2つの投資対象、Operator Workbench vs Product Runtimeの2軸評価、4種類のロックイン、推奨分離アーキテクチャ、選定指針）
- Updated index.md: Comparisons 15→16, added new entry

## [2026-05-14] query | queries/data-analysis-open-harness
- Created query page: `queries/data-analysis-open-harness.md` — kzinmr の質問「データ分析に適したOpen Harnessはあるか？」に対する回答をWiki化
- 回答要旨: データ分析専用の真のOpen Harnessはまだ発展途上。現状は汎用coding harness（OpenCode/Pi）にDB MCP connectorを付けて使うのが最もOpenな選択肢。Cognition DANAは強力だがClosed Harness
- 選択肢マトリクス: 汎用coding harness転用（OpenCode/Pi/Claude Code/Codex/Aider）、データ分析特化製品（Cognition DANA/OpenAI社内Data Agent/Hex）、Frameworkからの進化（OpenAI Agents SDK）
- Karpathyの「良い回答はWikiにファイリングすべき」パターンに従い、チャット履歴に埋もれさせずqueryページとして資産化
- Updated index.md: Queries 0→1

## [2026-05-13] rotate | Log rotated (638 lines → log-2026.md)
- Previous log archived to `log-2026.md` for historical reference

## [2026-05-14] create | entities/randy-olson.md
- Created comprehensive person entity page for Randy Olson (Randal S. Olson)
- Co-Founder & CTO of Goodeye Labs, data visualization legend, r/DataIsBeautiful moderator
- Documented Tufte Test, Truesight MCP agent skills, generator-evaluator workflow, reflect-and-improve pattern, digital twin concept
- Added tags: agent-skills, data-visualization, verification to SCHEMA.md taxonomy
- Updated index.md with new entry

## [2026-05-13] index | Added 6 orphan pages to index.md (entities: dex-horthy, merge-dev; concepts: agentic-rag, agentic-retrieval, claude-opus-4-7, death-of-browser). Fixed merge-dev alphabetical position. Updated section counts.

## [2026-05-13] lint | Frontmatter validation fixes
- Fixed 6 wiki pages with YAML frontmatter syntax errors:
  - `entities/ramp-labs.md` — related block invalid YAML (flow/block mix)
  - `entities/intuit-machine.md` — related block invalid YAML (flow/block mix)
  - `entities/anthropic.md` — related block invalid YAML (flow/block mix)
  - `concepts/agent-harness.md` — bulleted list inside [...] flow context
  - `concepts/societal-shadow.md` — missing closing --- frontmatter separator
  - `concepts/ai-coding-workflows.md` — corrupted frontmatter line (truncated source entry)

---

## [2026-05-13] index | Added 20 orphan concept pages to index.md

- Added 20 high-quality concept pages (not previously listed) to the Concepts section:
  - ai-infrastructure-engineering/distributed-training, ai-infrastructure-engineering/hardware-lottery, ai-infrastructure-engineering/pytorch-gpu-memory-profiling
  - ai-organization/ai-org-context-as-moat, ai-organization/ai-org-from-hierarchy-to-intelligence, ai-organization/ai-org-solo-founder-and-super-ic
  - ai-regulation-2026, ai-safety, ai-video-generation-2026, anthropic-managed-agents
  - bitsandbytes, chatgpt-images-2.0, chief-of-staff-agent-patterns, claude-mythos-preview, cmu-llms-methods-applications
- Updated header counts: Concepts 1253→1273, Total 1834→1854, Indexed 900→920
- No index corruption found (pipe_prefix: 0, line_number_prefix: 0, triple_brackets: 0, space_prefix: 0)
- Wiki-health: 980 orphans remain (not auto-applied — max 20 per run), 125 stale pages (31-34d), 5,405 unprocessed raw articles


## [2026-05-13] lint | Index audit — orphan entries identified
- 21 orphan index entries found (pointing to non-existent files):
  - `entities/_index` — index files don't need separate entries, remove from index
  - 10x `entities/omar-khattab/*` — these are subdirectory pages, not in main entities/ namespace
  - `concepts/agent-engineering-guide-2026|...` — link text syntax, should be cleaned
  - `concepts/ai-patterns-for-glam|...` — link text syntax, should be cleaned
  - `concepts/ambient-agency|...` — link text syntax, should be cleaned
  - `concepts/genai-handbook` — file doesn't exist
  - `concepts/glut-of-circuits` — file doesn't exist
  - `concepts/harness-commoditization` — file doesn't exist
  - `concepts/tau-bench` — file doesn't exist (concept page exists but may have been renamed)
  - `entities/theodoros-galanos|...` — link text syntax
  - `entities/vibevoice|→詳細` — link text syntax
  - `concepts/agent-team-swarm/managed-devins` — wrong namespace format
## [2026-05-13] lint | Wiki watchdog auto-fix

### ✅ Fixed: 11 duplicate index entries removed
- 4 entity skeletons removed (addy-osmani, elie-bakouch, florian-brand, gary-marcus)
- 4 more entity skeletons removed (jaya-gupta, tobi-lutke, parallel-web-systems, claris-filemaker)
- 1 will-brown double-entry block removed (2 adjacent lines), kept L589 entry
- 1 concepts/mcp and 1 comparisons/agent-harnesses stripped of skeleton entries
- Index header updated: Total pages: 1797 → 1834, Indexed entries: 853 → 894

### 🔍 Verified: All 21 "ghost entries" are false positives
- All 10 `entities/omar-khattab/*.md` files exist in subdirectory
- `entities/_index.md` exists and is properly indexed
- 3 pipe-syntax entries (`agent-engineering-guide-2026|...`, `ai-patterns-for-glam|...`, `ambient-agency|...`) use valid Obsidian display-text wikilinks pointing to existing files
- 4 `<missing>.md` entries (genai-handbook, glut-of-circuits, harness-commoditization, tau-bench) all exist in `concepts/`
- `agent-team-swarm/managed-devins.md` exists in subdirectory
- Root cause: health scanner used non-recursive directory listing

### ⚠️ Needs human review
- **933 pages not in index.md** — too large to batch-auto-apply (max 20 per policy)
- **810 pages missing frontmatter fields** (770+ missing `sources`) — needs batch fix strategy
- **Pipeline watchdog**: x-accounts-scan (26h stale) — normal for `*/2` schedule, next run 22:30 UTC today

### 📊 Post-fix index health
- Index entries: 894 (was 853 before dedup)
- Total pages: 1834 (577 entities, 1238 concepts, 16 comparisons, 1 queries, 2 events)
- Duplicates: 0 (was 11)
- Pipe corruption: 0 ✅ | Triple bracket: 0 ✅ | Line-number corruption: 0 ✅

## [2026-05-13] dreaming-wiki-ingest | entities/andrew-nesbitt.md enriched
### Context
- Dreaming pre-run failed (JSON parse error) — cross-pipeline check performed
- newsletter-ingest: 0 candidates | sitemap-monitor: 0 saved | blog-ingest: 1 take consumed
- All other recent raw articles (GNAP, InclusionAI Ring-2.6-1T, AEM, Firecracker, David Fowler, Prime Intellect renderers) already processed by other pipelines

### Changes
- `entities/andrew-nesbitt.md`:
  - ✅ Removed triplicated "The Mismeasure of Open Source" sections (removed 2 duplicate copies)
  - ✅ Added "Not a Security Issue: AI Scanner Policy Engineering" section documenting AI scanner self-triage via policy files
  - ✅ Updated `updated` date to 2026-05-13
  - ✅ Added source entry and raw article reference (nesbitt.io--2026-05-12-not-a-security-issue-html--c464f9c9)

### Files affected
- `~/wiki/entities/andrew-nesbitt.md` — updated (265 lines, up from 274 with duplicates)
- `~/wiki/log.md` — updated
- `~/wiki/index.md` — no change (entry already exists)

## [2026-05-14] ingest | NVIDIA Vera Rubin platform technical blog
- Saved raw article: `raw/articles/2026-01-05_nvidia_vera-rubin-platform.md` (92,829 chars, 1,319 lines)
- Source: https://developer.nvidia.com/blog/inside-the-nvidia-rubin-platform-six-new-chips-one-ai-supercomputer/
- Author: Kyle Aubrey, published 2026-01-05, updated 2026-03-16

## [2026-05-14] create | concepts/nvidia-vera-rubin
- Created comprehensive concept page: `concepts/nvidia-vera-rubin.md` (12,989 chars)
- Covers: 6-chip architecture (Vera CPU, Rubin GPU, NVLink 6, ConnectX-9, BlueField-4 DPU, Spectrum-6), extreme co-design philosophy, bottleneck shift from FLOPS → bandwidth/interconnect/integration, ICMS KV-cache tier, NVL72 rack → DGX SuperPOD scaling, software stack, RAS, security, energy efficiency, performance (10T MoE training, reasoning inference)

## [2026-05-14] update | entities/nvidia
- Updated `entities/nvidia.md`: Added Vera Rubin Platform section, added source reference, added wikilink to [[concepts/nvidia-vera-rubin]], bumped `updated` date

### Files affected
- `~/wiki/raw/articles/2026-01-05_nvidia_vera-rubin-platform.md` — new (1328 lines)
- `~/wiki/concepts/nvidia-vera-rubin.md` — new
- `~/wiki/entities/nvidia.md` — updated
- `~/wiki/index.md` — updated (added nvidia-vera-rubin entry)
- `~/wiki/log.md` — updated

## [2026-05-14] ingest | NVIDIA Rubin comprehensive research report
- Saved raw article: `raw/articles/2026-05-14_kzinmr_nvidia-rubin-comprehensive-report.md` (108 lines)

## [2026-05-14] enrich | concepts/nvidia-vera-rubin
- Major enrichment from comprehensive research report (340 lines, ~24 KB):
- Added: Scaling law shift analysis (Pre-Training → Post-Training → Test-Time), MFU 35-50% utilization, compute 4.4×/yr vs bandwidth 2×/2-3yr growth gap
- Added: HBM4 supply chain dynamics (NVIDIA 11-13 Gbps pin speed requirements, SK Hynix shifting to TSMC 3nm, Samsung 4nm + 3D hybrid bonding, CoWoS-L packaging, Intel ZAM competition)
- Added: DGX Rubin NVL8 enterprise air-cooled variant (8 GPU, Intel Xeon 6776P, ~24 kW, 400 PFLOPS NVFP4)
- Added: Groq 3 LPX detailed architecture (500MB SRAM/chip, 80 TB/s/chip, 256-chip LPX rack, 40 PB/s SRAM fabric, joint decode computation)
- Added: Co-Packaged Optics (CPO) physics deep dive (<5 pJ/bit vs 20-30 pJ/bit, 6× optical density gap)
- Added: Physical infrastructure impact (190-230 kW/rack, 45°C DLC forcing chiller elimination, HVAC market impact)
- Added: NVL72 detailed performance specs table (all precision modes: NVFP4 through FP64)
- Added: Market deployment timeline (Q1 2026 mass production, H2 2026 shipments)
- Added: Blackwell → Rubin generation comparison table

### Files affected
- `~/wiki/raw/articles/2026-05-14_kzinmr_nvidia-rubin-comprehensive-report.md` — new
- `~/wiki/concepts/nvidia-vera-rubin.md` — enriched (196 → 340 lines)
- `~/wiki/log.md` — updated

## [2026-05-14] create | concepts/test-time-scaling
- Created comprehensive concept page (14 KB, 250+ lines) from scratch
- Covers: Three axes of AI scaling (pre-training → post-training → test-time), Snell et al. compute-optimal allocation, 7 core techniques (CoT, Self-Consistency, Best-of-N with ORM/PRM, Beam Search, Tree/Forest-of-Thought, Sequential Refinement, RL-trained reasoning o1/o3/R1), compute-optimal strategy, thinking-optimal scaling caveat, comparison with model scaling/speculative decoding/post-training, practical implications, open questions
- Cross-references: scaling-hypothesis, chain-of-thought, rlvr, grpo, post-training, reasoning, rlm, speculative-decoding, nvidia-vera-rubin

## [2026-05-14] enrich | concepts/chain-of-thought
- Replaced stub (24 lines, 288 bytes) with comprehensive page (5.5 KB, 130+ lines)
- Covers: Emergent behavior property, domain effectiveness, variants (Few-Shot/Zero-Shot/Auto-CoT/Long CoT/RL-trained CoT), comparison table with other reasoning methods, faithfulness/error propagation limitations, relationship to test-time scaling

## [2026-05-14] redirect | concepts/inference-time-scaling → test-time-scaling
- Replaced stub with redirect page pointing to [[test-time-scaling]] as canonical

## [2026-05-14] update | concepts/scaling-hypothesis
- Updated related links and internal references from inference-time-scaling → test-time-scaling

### Files affected
- `~/wiki/concepts/test-time-scaling.md` — new (14 KB)
- `~/wiki/concepts/chain-of-thought.md` — enriched (288 bytes → 5.5 KB)
- `~/wiki/concepts/inference-time-scaling.md` — rewrote as redirect (312 bytes → 503 bytes)
- `~/wiki/concepts/scaling-hypothesis.md` — updated references
- `~/wiki/index.md` — updated (added test-time-scaling, enriched chain-of-thought)
- `~/wiki/log.md` — updated

## [2026-05-14] update | entities/wes-mckinney.md — major expansion

### Changes
- Expanded from skeleton (92 lines, 5 KB) to comprehensive entity page (~210 lines, 15 KB)
- Added: Quick Facts table, full Bio with all career milestones
- Added: Agentic Engineering philosophy section with key quotes ("I almost don't read code now"), adversarial agent review approach, Agent Ergonomics thesis, Four-Layer Stack model, "The Mythical Agent Month" framework, vibe coding vs agentic engineering distinction
- Added: Current Projects section covering RoboRev (Go, 55+ releases, post-commit hook), Agents View (session DB), Middleman (GitHub dashboard), Kata, msgvault (DuckDB-powered), spicytakes.org (1M+ lines, 93 posts, 679 quotes over 16 years)
- Added: Skills Framework section documenting Superpowers (Jesse Vincent) usage
- Added: Professional Timeline table, Key Projects table with languages, Key Quotes section (7 quotes)
- Updated: tags to [person, ai-agents, agent-skills, code-review, developer-tooling, harness-engineering, open-source]
- Updated: sources linking to raw articles 2026-05-12 and 2026-05-08
- Updated: frontmatter dates to 2026-05-14

### Sources consulted
- Web research: Wes McKinney pandas creator, agentic engineering, RoboRev, spicytakes.org, POSIT
- Raw articles: vanishing-gradients show-us-your-agent-skills ep1, hugobowne agentic-engineering-verification
- External: wesmckinney.com, Wikipedia, Posit blog (Rich Iannone), spicytakes.org, X/Twitter, Joe Reis Podcast transcript, Rill Data Podcast transcript, Data Renegades transcript

### Files affected
- `~/wiki/entities/wes-mckinney.md` — major expansion (92 → ~210 lines, 5 KB → 15 KB)
- `~/wiki/index.md` — updated summary line
- `~/wiki/log.md` — updated

## [2026-05-14] create | entities/jeremiah-lowin.md — new entity page

### Created
- Jeremiah Lowin entity page: Founder & CEO of Prefect, creator of FastMCP, Prefab, Cardboard
- Documented: career (Prefect, Apache Airflow PMC, Marvin, ControlFlow), agent philosophy ("second brain" with voice memo pipeline, explain skill), key projects (FastMCP ~25K stars, Prefab generative UI DSL), strategic advisory roles (Spotify, Positive Sum, OSV), Compass Coffee Global Ambassador
- Tags: [person, ai-agents, agent-skills, context-engineering, developer-tooling, open-source, entrepreneur, mcp, generative-ui, prefect]
- Added `prefect` tag to SCHEMA.md taxonomy (People/Orgs section)

### Sources consulted
- Web research: jlowin.dev/about, GitHub, FastMCP v2.6/v3.0/GA launch posts, Prefab announcement, Compass Coffee 10-year post, Prefect origin story, Vanishing Gradients podcast (Show Us Your Agent Skills Ep. 1), Hacker News Prefab Show HN, YouTube (First Commit with Nina)
- External: LinkedIn, Crunchbase, X/Twitter (@jlowin)

### Files affected
- `~/wiki/entities/jeremiah-lowin.md` — new (~210 lines)
- `~/wiki/index.md` — added entry between jeff-huber and jensen-huang; fixed merged-line bug
- `~/wiki/SCHEMA.md` — added `prefect` to tag taxonomy
- `~/wiki/log.md` — updated

## [2026-05-14] ingest | NVIDIA RTX AI Garage: Hermes Agent on DGX Spark

### Ingested
- Raw article: `wiki/raw/articles/2026-05-13_nvidia_rtx-ai-garage-hermes-agent-dgx-spark.md`
- NVIDIA blog post (May 13, 2026) by Abhishek Gore: Hermes Agent endorsed as RTX AI Garage's centerpiece agent framework
- Key data points: 140K+ GitHub stars, #1 on OpenRouter, Qwen 3.6 model recommendation, "Same model, better results" harness engineering claim

### Entities enriched
- `entities/hermes-agent.md` — Added "Milestones (May 2026)" section (140K stars, OpenRouter #1, NVIDIA endorsement), "Harness Engineering: Same Model Better Results" subsection, "NVIDIA DGX Spark 統合" section, updated sources and related links
- `entities/nvidia-dgx-spark.md` — Added "Hermes Agent Integration" section (5 synergy points: always-on, large model compatibility, Qwen 3.6 optimization, official playbook, harness engineering), updated timeline with May 2026 milestone, added related links

### Concepts created
- `concepts/nvidia-rtx-ai-garage.md` — New concept page (~125 lines): NVIDIA's program for curating/optimizing AI tools on RTX hardware. Covers positioning (curation, playbooks, optimization verification, hands-on sessions), recommended agents (Hermes, NemoClaw, OpenClaw), supported models/optimizations, added value over DIY setup (model selection, NVFP4 optimization, hardware-software integration verification), information channels

### Files affected
- `wiki/raw/articles/2026-05-13_nvidia_rtx-ai-garage-hermes-agent-dgx-spark.md` — new
- `wiki/entities/hermes-agent.md` — enriched (added Milestones, Harness Engineering, DGX Spark sections)
- `wiki/entities/nvidia-dgx-spark.md` — enriched (added Hermes Agent Integration section, timeline entry)
- `wiki/concepts/nvidia-rtx-ai-garage.md` — new
- `wiki/index.md` — updated (added nvidia-rtx-ai-garage concept entry)
- `wiki/log.md` — updated
