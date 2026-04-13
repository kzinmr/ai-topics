## 2026-04-13 (4/4)
- **Created [[concepts/decoder-only-gpt.md]]** (10.5KB): Complete intuitive explanation of decoder-only GPT architecture based on Karpathy's microgpt (200 lines pure Python). Covers: token embedding + positional encoding, RMSNorm vs LayerNorm, self-attention as "token communication", MLP as "where thinking happens", residual connections, autograd from scratch, Adam optimizer, cross-entropy loss, autoregressive sampling, temperature control, KV cache, scaling from microgpt (4K params) to production LLMs (1.8T params). Key thesis: "Everything else is just efficiency." Source: karpathy.github.io/2026/02/12/microgpt/
- **Enriched [[andrej-karpathy]]** microgpt section (+1KB): Added detailed technical breakdown with 7 key insights, architecture details, training data specifics. Added decoder-only-gpt to Related.

## 2026-04-13 — Local-First Software Concept + Martin Kleppmann Entity

### New Concept Pages
- **[[concepts/local-first-software]]** — Local-First Software (Kleppmann, Ink & Switch, CRDTs, AT Protocol, 7 Ideals, ecosystem mapping, 5 concrete bridges to AI Agent development + honest gap analysis)

### New Entity Pages
- **[[entities/martin-kleppmann]]** — Martin Kleppmann (Cambridge professor, DDIA author, Automerge, Bluesky AT Protocol, Local-First Software movement)

### Key Insights
- **7 Ideals**: No Spinners, Multi-Device, Network Optional, Seamless Collaboration, The Long Now, Security & Privacy, Ultimate Ownership
- **CRDTs as foundation**: Mathematical guarantee for conflict-free merging — still unsolved for AI agent "decision conflicts"
- **Generic Sync Server** (2024): Kleppmann's proposal to abstract sync away from application logic — parallels MCP's standardization of tool connections
- **5 concrete bridges to AI Agent**: Event sourcing → agent audit logs, Local authority → local agent execution, Generic sync → MCP, Edge inference → Network optional, CRDTs → CRDT for AI (research stage)
- **Honest gaps**: Agent decision conflicts have no mathematical guarantee, context compaction is immature (parallel to CRDT history bloat), A2A protocols are as nascent as P2P NAT traversal was

### Sources
- https://martin.kleppmann.com/papers/local-first.pdf (Ink & Switch, 2019)
- https://martin.kleppmann.com/2024/05/30/local-first-conference.html (Local-First Conference 2024)
- https://arxiv.org/abs/2402.03239 (Bluesky AT Protocol paper)
- https://localfirst.fm (Podcast series)
- https://electric-sql.com/blog/2024/07/17/electric-next (ElectricSQL generic sync)

### Updated Files
- **wiki/concepts/local-first-software.md** — 13.4KB concept page
- **wiki/entities/martin-kleppmann.md** — 7.3KB entity page
- **wiki/index.md** — Added Local-First Software concept + Martin Kleppmann entity, new "Distributed Systems & Local-First" section
- **wiki/log.md** — This entry

## 2026-04-13 — Boris Cherny Entity Enrichment (Claude Code Workflow)

## 2026-04-13 (3/3)
- **Enriched [[andrej-karpathy]] older blogs section** (28KB → 35KB): Added comprehensive analysis of 20+ blog posts from karpathy.github.io spanning 2012-2021. Key posts: "Software 2.0" (seminal paradigm shift essay), "A Recipe for Training Neural Networks" (essential ML practitioner guide), "The Unreasonable Effectiveness of Recurrent Neural Networks" (2015 viral post), "Short Story on AI: Forward Pass" (creative AI philosophy fiction), "Quantifying Hacker News with 50 days of data" (early data journalism), ConvNetJS interview, and 14 others. Each post analyzed for technical content, philosophical insights, and influence on the field. Source: karpathy.bearblog.dev/blog/ and karpathy.github.io/


## 2026-04-13 (2/2)
- **Enriched [[andrej-karpathy]] writings section** (22.6KB → 28KB): Added detailed blog analysis from karpathy.bearblog.dev. "I love calculator" (Sep 2024 - technology philosophy essay), "Chemical hygiene" (water/air/food/fabrics/cleaning systems), "Digital hygiene" (authentication/browsing/financial/device security), "Finding the Best Sleep Tracker" (Oura vs Whoop vs 8Sleep vs AutoSleep comparative analysis with correlation data), "The append-and-review note" (single-note knowledge management system). All bearblog posts now have detailed summaries with key excerpts, data points, and philosophical frameworks. Source: karpathy.bearblog.dev/blog/


## 2026-04-13
- **Enriched [[andrej-karpathy]]** (16.7KB → 22.6KB): Added birthplace/education timeline, research contributions (Deep Visual-Semantic Alignments, Sports-1M, character-level RNNs), OpenAI Universe/World of Bits details, Tesla Vision rollout dates and data engine, llm.c and nanochat projects, Dobby the Elf Claw, AGI timeline philosophy ("march of nines"), RL critique, data-centric AI, vibe coding concrete examples (MenuGen with Cursor/Claude/Superwhisper), Eureka Labs founding date. Source: grokipedia.com/page/Andrej_Karpathy


### Updated Files
- **wiki/entities/boris-cherny.md** — Major enrichment from 3 source articles: added Opus 4.5 + thinking rationale, Plan Mode → auto-accept workflow, CLAUDE.md as team infrastructure, PostToolUse hooks, self-verification patterns, subagents usage, MCP integration (BigQuery/Slack/Sentry), terminal optimizations, ChernyCode repo reference
- **wiki/index.md** — Updated Boris Cherny entry with key workflow patterns
- **wiki/log.md** — This entry
- **wiki/raw/articles/** — 3 source articles saved (Boris's original thread, Claude Code Camp team tips, ChernyCode repo docs)

### Key Additions
- **Opus 4.5 + thinking**: "Slower than Sonnet but smarter, requires less steering, ends up faster"
- **Plan Mode → Auto-Accept**: Shift+Tab twice → review plan → auto-accept → one-shot execution
- **CLAUDE.md as Team Memory**: Single shared file, whole team contributes, @claude on PRs to update guidelines
- **Self-Verification**: "The most underrated step. Give Claude a way to verify its work." Chrome extension, test suites
- **MCP Integration**: BigQuery, Slack, Sentry — Claude as full-stack dev hub
- **ChernyCode**: Reference implementation repo with actual config files

### Sources
- https://readwise.io/reader/shared/01kgcamtex6zews0fvz94a8qg4/ (Boris's original thread, Jan 2026)
- https://www.claudecodecamp.com/p/how-the-claude-code-team-really-works (Feb 2026)
- https://github.com/meleantonio/ChernyCode (curated config files)
- https://paddo.dev/blog/how-boris-uses-claude-code/ (detailed analysis)

## 2026-04-13 — AI Organization Concept Hierarchy

### New Concept Pages (4件)
- **ai-organization/_index.md** — AI時代の組織論フロントページ。階層からインテリジェンスへ、Solo Founder、Context as Moatの横断的テーマを整理
- **ai-organization/ai-org-from-hierarchy-to-intelligence.md** — Block (Jack Dorsey) のAgentic Design Principles。Hierarchy to Intelligenceモデル、Decision Rights Matrix、Open-Book Telemetry、透明性ベースの監視
- **ai-organization/ai-org-solo-founder-and-super-ic.md** — Solo FounderとSuper ICの台頭。Reddit/ClaudeCodeとFourWeekMBA。1人=従来10人の生産性、管理階層のバイパス、$10M→$100Mパス
- **ai-organization/ai-org-context-as-moat.md** — McKinsey Agentic Organization。Proprietary Context Layer（最後のモート）、M-shaped Supervisor

### Updated Files
- **wiki/index.md** — AI Organizationセクション追加（3+1件）、last updated更新
- **wiki/log.md** — This entry

### Key Insights
- **Hierarchy → Intelligence**: Jack DorseyがBlockで実践。報告ライン削除、意思決定権限分散、透明性最大化
- **Context as Moat**: 企業固有の判断基準・文化・市場知見を構造化しエージェントに供給。これが最後の防衛可能資産
- **Super IC**: AIによる管理層のバイパス。技術的実行力を最大化する新しいキャリアパス
- **Agentic Governance**: エージェント実行に対するリアルタイム監視、ガードレール、エスカレーション

### Sources
- https://block.xyz/inside/from-hierarchy-to-intelligence
- https://www.reddit.com/r/ClaudeCode/comments/1ri5pnc/hot_take_solo_founders_with_ai_are_about_to_build/
- https://www.mckinsey.com/capabilities/people-and-organizational-performance/our-insights/the-agentic-organization-contours-of-the-next-paradigm-for-the-ai-era
- https://organizationalphysics.com/2026/02/15/your-ai-strategy-isnt-failing-your-org-design-is/
- https://fourweekmba.com/solopreneurs/
