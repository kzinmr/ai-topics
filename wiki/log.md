## 2026-04-14 — Ali Farhadi Entity Enriched to L3 Depth

### Updated Entity Pages
- **[[entities/ali-farhadi]]** → **L3 depth** (was skeleton/L1). Major expansion:
  - Complete career timeline: UIUC → CMU postdoc → UW professor → Ai2 → Xnor.ai → Apple → Ai2 CEO → Microsoft (2026)
  - "Language Model of a Crow" Grand Challenge philosophy — embodied understanding as AI's ultimate test
  - "Truly Open" AI philosophy — beyond open weights to full pipeline transparency (data + code + weights + recipes)
  - Data transparency as safety — OLMoTrace output attribution, radical openness as the path to safe AI
  - Nonprofit-to-corporate migration structural analysis — why frontier-scale open research requires corporate compute
  - Embodied AI research arc — AI2-THOR, RoboTHOR, ProcTHOR, MolmoAct, Visual Commonsense Reasoning
  - Research Philosophy Synthesis table (6 principles with quotes)
  - Convergence analysis with Karpathy, Willison, Sanfilippo, Suleyman
  - 15 major contributions catalogued with impact
  - Related entities cross-references (Suleyman, Hajishirzi, Krishna, Redmon, OLMo concept pages)

### Updated
- **wiki/index.md** — Updated Ali Farhadi entry with comprehensive summary

### Key Insights
- **"Truly Open" > "Open Weights"** — Farhadi's most distinctive contribution: Meta's LLaMA is NOT open source because you lack the training data and recipes
- **The Crow Challenge** — Set 10 years ago: can AI understand that a crow watching something buried will later return and act on it? This is embodied understanding, not pattern recognition
- **Safety through radical transparency** — OLMoTrace traces every model output to specific training documents in real time. This is fundamentally different from closed-door evaluation approaches
- **Nonprofit can't compete with corporate compute** — $1B+ cost barrier for frontier model training forces open advocates into corporate structures
- **Microsoft as the pragmatic choice** — Unlike OpenAI, Microsoft still has room for genuinely open model development alongside proprietary products
- **YOLO's elegance** — Single network, single pass. Same simplicity philosophy as Karpathy's autoresearch and antirez's Redis

### Sources
- https://homes.cs.washington.edu/~ali/
- https://www.fastcompany.com/91283517/ai2s-ali-farhadi-advocates-for-open-source-ai-models-heres-why
- https://www.fastcompany.com/91225845/ai2-ceo-ali-farhadi-believes-open-source-is-the-future
- https://www.geekwire.com/2026/allen-institute-for-ai-ceo-ali-farhadi-steps-down-as-nonprofit-navigates-shifting-ai-landscape/
- https://www.geekwire.com/2026/microsoft-hires-former-ai2-ceo-ali-farhadi-and-key-researchers-for-suleymans-ai-team/
- https://madrona.com/ia-summit-2023-keynote-open-source-models-ali-farhadi
- https://building.theatlantic.com/open-research-is-the-key-to-unlocking-safer-ai-15d1bac9085d
- https://thelettertwo.com/2025/04/09/ai2s-olmotrace-tool-reveals-the-origins-of-ai-model-training-data/
- https://raivn.cs.washington.edu/
- https://www.youtube.com/watch?v=pNgFnmQ1ULs (Columbia Engineering lecture, 2026-03-13)

---

## 2026-04-14 — Teknium Entity Page Enriched to L3 Depth

### Updated Entity Pages
- **[[entities/teknium]]** → **L3 depth** (was skeleton). Major expansion:
  - Hermes Agent architecture (self-improving loop, 4-layer memory, gateway design, 6 terminal backends, security model)
  - Post-training philosophy and data engineering methodology
  - Harness Engineering & agentic workflow connections
  - Direct quotes from Delphi AMA and Nous documentation
  - Hermes 3/4 model family details and technical contributions
  - Open-source contributions (datasets, tools, RL environments)
  - Timeline 2024-2026 including 68K+ GitHub stars milestone
  - Related entities cross-references

### Updated
- **wiki/index.md** — Added Teknium to "AI Agent Platforms & Developer Tools" section

### Key Insights
- Hermes Agent's self-improving loop: Periodic Nudges → Skill Creation → Skill Self-Improvement → FTS5 Session Search
- "Most agents recall what happened, but Hermes goes one step further: it extracts what worked, writes it as a reusable skill"
- Teknium approaches Harness Engineering from the **model training side** (vs Ryan Lopopolo's orchestration side)
- Platform Registry Refactor (Issue #3823) proposes eliminating 17+ file touchpoints per new platform adapter
- Zero telemetry is "built-in architectural property, not a toggle"
- Nous Research: $1B valuation (Series A 2025, Paradigm), decentralized training (DiStrO), Psyche Network (Solana)

### Sources
- https://nousresearch.com/hermes-agent
- https://mranand.substack.com/p/inside-hermes-agent-how-a-self-improving
- https://www.delphiintelligence.io/research/ama-1-transcript-with-nous-research-co-founder-and-post-training-lead-teknium1
- https://arxiv.org/abs/2508.18255 (Hermes 4 Technical Report)
- https://arxiv.org/abs/2408.11857 (Hermes 3 Technical Report)
- https://github.com/NousResearch/hermes-agent/issues/3823
- https://en.wikipedia.org/wiki/Nous_Research
- https://github.com/teknium1/teknium1

---

## 2026-04-14 — Karpathy Loop (Autoresearch) Concept Page

### New Concept Pages
- **[[concepts/karpathy-loop]]** — The Karpathy Loop: Autonomous Experiment Design via `program.md` + agent iteration on `train.py` (5-min fixed budget, val_bpb metric, keep/discard loop). Covers: core architecture, four design constraints, community response, No Priors podcast key themes, Cerebras cheating experiments, real-world applications beyond ML training, relationship to Agentic Engineering & Harness Engineering, criticisms and open problems.

### Key Insights
- **Four constraints make it work:** Single mutable file, fixed time budget, unambiguous metric (val_bpb), cheap rollback (git reset)
- **~12 experiments/hour, ~100 overnight** on a single GPU (H100 tested)
- **Human's role shifted** from writing Python to writing `program.md` — the research protocol in natural language
- **Agent drift is the main failure mode** — Cerebras found agents abandon tasks within hours if guardrails are loose
- **The pattern generalizes** but only to domains with fast, unambiguous metrics and cheap rollback
- **~71K GitHub stars in weeks** — one of the fastest-growing repos in GitHub history
- **Notable forks:** MLX (Apple Silicon), Windows/RTX, AMD GPU, distributed SETI@home-style coordination

### Sources
- https://github.com/karpathy/autoresearch
- https://www.youtube.com/watch?v=kwSVtQ7dziU (No Priors Ep. 154)
- https://softmaxdata.com/blog/autoresearch/
- https://www.cerebras.ai/blog/how-to-stop-your-autoresearch-loop-from-cheating
- https://rywalker.com/research/autoresearch
- https://mohammadkhan.dev/blog/karpathy-autoresearch-constraint-design
- https://starkslab.com/notes/autoresearch-review-what-it-actually-does

### Updated Files
- **wiki/concepts/karpathy-loop.md** — 13.0KB concept page
- **wiki/index.md** — Added Karpathy Loop to Harness Engineering & Meta section

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
