## 2026-04-16 — AI Organization Concept Hierarchy Upgrade (Block, Reddit, McKinsey, Reworked, Agile Leadership Day)

### Concept Pages Upgraded (3 pages + front page)
- **[[concepts/ai-organization/ai-org-from-hierarchy-to-intelligence]]** → Full upgrade from Block article:
  - AI's true potential quote (coordination mechanism vs productivity tool)
  - Historical hierarchy analysis (Roman army → Prussian General Staff → US Railroads → Taylorism → Post-war → Tech era)
  - Company World Model + Customer World Model detailed breakdown
  - 4 Building Blocks (Capabilities, World Model, Intelligence Layer, Interfaces)
  - Failure-signal driven roadmap generation
  - 3 new roles (ICs, DRIs, Player-Coaches) with hierarchy inversion
  - Company identity revelation thesis
- **[[concepts/ai-organization/ai-org-solo-founder-and-super-ic]]** → Full upgrade from Reddit/FourWeekMBA:
  - Reddit r/ClaudeCode hot take analysis (1 person = 10-person team)
  - Domain knowledge prerequisite thesis
  - FrontPage era historical parallel (1990s web development democratization)
  - MVP commoditization thesis (execution speed → product vision/monetization)
  - FourWeekMBA Super IC framework (traditional IC vs Super IC comparison)
  - $10M→$100M Solo Founder path (phases, success factors, scaling limits)
  - GIGO principle and quality assurance challenges
- **[[concepts/ai-organization/ai-org-context-as-moat]]** → Full upgrade from McKinsey/Reworked/Agile Leadership Day:
  - McKinsey Agentic Organization 5 pillars (already present, confirmed)
  - Reworked Diamond Org Chart (inverted pyramid: AI+experts at center)
  - Agile Leadership Day practical implementation model
  - Agent Orchestration Layer concept
  - Human-in-the-loop control framework

### Front Page Upgraded
- **[[concepts/ai-organization/_index]]** → Added 3-model comparison table (Block vs McKinsey vs Solo Founder), cross-cutting themes matrix, updated source list with 7 entries

### Updated Files
- **wiki/index.md** — AI Organization section descriptions upgraded with key concepts
- **wiki/log.md** — This entry

### Key Insights
- **Hierarchy as information routing protocol**: Jack Dorsey's most powerful insight — layers existed to overcome human cognitive limits (span of 3-8). AI removes this bottleneck.
- **Failure-signal roadmap**: Block's innovation — roadmap emerges from capability gaps, not PM hypotheses. Reality-driven planning.
- **Diamond vs Pyramid organization**: Traditional pyramids invert when AI executes. Humans become supervisors at top/bottom, AI+experts form the thick middle.
- **MVP commoditization paradox**: AI makes building easy but building the RIGHT thing harder. Competitive advantage shifts to domain knowledge and monetization strategy.
- **FrontPage warning**: 1990s democratized web creation but created unmaintainable spaghetti code. Same risk with AI coding — need architecture guardrails early.

### Sources
- https://block.xyz/inside/from-hierarchy-to-intelligence
- https://www.reddit.com/r/ClaudeCode/comments/1ri5pnc/hot_take_solo_founders_with_ai_are_about_to_build/
- https://www.mckinsey.com/capabilities/people-and-organizational-performance/our-insights/the-agentic-organization-contours-of-the-next-paradigm-for-the-ai-era
- https://www.reworked.co/employee-experience/humans-and-ai-agents-planning-the-org-chart-of-tomorrow/
- https://agileleadershipdayindia.org/blogs/agentic-ai-leadership-management/agentic-ai-workforce-org-chart-structure.html
- https://fourweekmba.com/solopreneurs/

---

## 2026-04-16 — Vivek Trivedy (@vtrivedy10) entity page created

### New Entity Pages
- **[[entities/vtrivedy10]]** — Vivek Trivedy (LangChain Product Lead). Deep Agents CLI architect. Harness Engineering (Agent = Model + Harness). Terminal Bench 2.0 Top 30 → Top 5 improvement. HaaS thesis, reasoning sandwich, self-verification loops.

## 2026-04-16 — Sandbox Infrastructure横断分析、JS Runtime概念ページ追加、sandboxディレクトリ体系構築

### New Concept Pages
- **[[concepts/sandbox/_index]]** — Sandbox: AI Agent Code Execution Isolation (3-layer model)
- **[[concepts/sandbox/infrastructure]]** — Infrastructure Layer: Containers, Micro-VMs, WASM, gVisor, Firecracker, E2B, Modal, Daytona
- **[[concepts/sandbox/in-process]]** — In-Process Layer: Monty (Rust Python VM), Pyodide, capabilities-based security
- **[[concepts/sandbox/js-runtime]]** — JS Runtime Layer: Bun, Deno, Node.js, E2B SDK, WebContainer
- **[[comparisons/agent-sandboxing]]** — Agent Sandboxing: Containers vs gVisor vs MicroVMs vs WASM vs Zeroboot

### Updated Entity Pages
- **[[entities/samuel-colvin]]** — Monty sandbox, CodeMode relationship
- **[[entities/jarred-sumner]]** — Anthropic acquisition, Claude Code Bun runtime
- **[[entities/ryan-dahl]]** — Deno 2.0 sandbox security

### Wiki Structure
- sandbox/ ディレクトリ新設
- `wiki/index.md` にsandbox関連エントリ追加

     1|## 2026-04-15 — Personal Superintelligence concept page created, Meta entity updated
     2|
     3|### New Concept Pages
     4|

### Updated Entity Pages
- **[[entities/meta]]** — Added Personal Superintelligence vision section (Zuckerberg philosophy), Ray-Ban AI glasses collaboration details (700万+ sold 2025, 2000-3000万 target 2026), Agentic Commerce strategy, Superintelligence Labs (Alexandr Wang, $115B-$135B capex 2026), Muse Spark context, Key People section, cross-references to personal-ai ecosystem players.

### Cross-References
- Related to [[concepts/anthropic-openclaw-conflict]]: Platform control vs open access tension
- Related to [[concepts/death-of-browser]]: Wearable-first computing paradigm
- Related to [[concepts/open-claw-ecosystem]]: Community-led personal agent movement
- Connected to [[entities/peter-steinberger]]: OpenClaw "you own your agent" philosophy
- Connected to [[entities/shlok-khemani]]: Filesystem-first personal AI memory
- Connected to [[entities/sero]]: Freedom Tech / local AI infrastructure
- Connected to [[entities/mario-zechner]]: Minimal agent on consumer hardware
## 2026-04-16 — Samuel Colvin Entity Page Created (L3 depth)

### New Entity Pages
- **[[entities/samuel-colvin]]** — Samuel Colvin: Creator of Pydantic, Founder & CEO of Pydantic. PhD in Mathematics (Bristol), MSci from Imperial College London. Built Pydantic (27.3K stars, 46M+ monthly downloads), Pydantic AI (15.9K stars, type-safe agent framework), Monty (6.6K stars, minimal Rust Python sandbox for AI agents), and Logfire (4.1K stars, AI observability platform). Key philosophy: developer experience first, type safety for reliability, "start from nothing" security model.

### New Concept Pages
- **[[concepts/code-mode]]** — CodeMode: LLM writes Python code for parallel execution instead of sequential tool calls. Latency: 0.004ms (Monty) vs 195ms (Docker) vs 1000ms+ (sandbox services)
- **[[concepts/monty-sandbox]]** — Monty: minimal, secure Python interpreter written in Rust for AI agents. Capabilities-based security, from-scratch bytecode VM using Ruff's parser
- **[[concepts/pydantic-ai]]** — Pydantic AI: type-safe Python agent framework with 15+ model providers, structured outputs, MCP/A2A support, Logfire integration
- **[[concepts/capabilities-based-security]]** — Start from zero access, explicitly grant capabilities. Contrast with traditional sandbox (full VM → restrict down)

### Cross-References
- Related to [[concepts/harness-engineering]]: Monty as harness environment for AI agents
- Related to [[concepts/ai-agent-engineering/building-effective-agents]]: Type safety as agent reliability pattern
- Related to [[concepts/ai-agent-engineering/code-execution-with-mcp]]: CodeMode vs MCP tool execution
- Connected to [[entities/andrej-karpathy]]: Both advocate code-over-sequential-tool-calls paradigm
- Connected to [[entities/sebastián-ramírez]]: FastAPI-Pydantic symbiosis
## 2026-04-13 — Auto-triage ingest (RSS scan)

### Updated Entity Pages
- **[[entities/claude-mythos]]** — Added UK AI Security Institute (AISI) evaluation results: first model to complete cyber range end-to-end, assessment that Mythos could compromise weakly defended systems, Gary Marcus analysis. Updated `updated:` date to 2026-04-13.
- **[[entities/gemma-4]]** — Added MoE expert routing visualization section: Martin Alderson's interactive tool showing ~25% of experts never activate per prompt, varies by prompt. CPU MoE inference insights. Updated `updated:` date to 2026-04-13.

### Updated Concept Pages
- **[[concepts/cognitive-cost-of-agents]]** — Added Steve Yegge industry AI adoption data (20/20/60 split at Google and industry-wide), Bryan Cantrill's "LLMs lack laziness" thesis connecting to code bloat and abstraction quality.

### Sources
- https://garymarcus.substack.com/p/claude-mythos-evaluated (Gary Marcus evaluation)
- https://simonwillison.net/2026/Apr/13/steve-yegge/ (Yegge on Google AI adoption)
- https://simonwillison.net/2026/Apr/13/bryan-cantrill/ (Cantrill on laziness)
- https://martinalderson.com/posts/moe-expert-routing-visualization/ (MoE routing visualization)

---

## 2026-04-16 — gm8xx8 Paper Curation Analysis (29 papers, March–April 2026)

### Entity Page Updated
- **[[entities/gm8xx8]]** — gm8xx8 (@gm8xx8): AI paper curator & infrastructure researcher. Updated with comprehensive 29-paper curation analysis from March–April 2026 batch.
  - 9 interest clusters: Architecture/Training (24%), Theory/Math (17%), Efficiency (14%), Multimodal (14%), Agents/Verification (emerging), Robotics/VLA (7%), Hardware (7%), Embeddings (7%), Evaluation (3%)
  - Key signals: Model training science (DGPO, HyperP, daVinci-LLM), mathematical foundations (Tao, CDCL proofs), efficiency frontier (1-bit Bonsai, TARA), verification-centric agents (AgentFixer, Marco DeepResearch)
  - Cross-cutting pattern: Papers bridging "lab demo" → "production system" — efficiency, reliability, verification, real-time performance, mathematical rigor
  - Curation style: High-volume, no-commentary signal detection. Cross-platform (HF upvotes, X tweets, GitHub contributions). Early trend detection.
  - Status upgraded from skeleton to L3 depth (comprehensive interest taxonomy)

## 2026-04-15 — Dario Amodei, Mustafa Suleyman, Demis Hassabis Entity Pages Created (L3 depth)

### New Entity Pages
- **[[entities/dario-amodei]]** — Dario Amodei: Anthropic CEO & co-founder. Page covers:
  - Princeton PhD in physics (statistical mechanics of neural circuits)
  - OpenAI VP of Research (2016-2021): GPT-3, "Concrete Problems in AI Safety" (2016)
  - Anthropic founding (2021) with Daniela Amodei and others
  - Constitutional AI framework and Responsible Scaling Policy (RSP)
  - Mechanistic interpretability as "MRI for AI"
  - AI Safety Levels and board-level governance
  - $380B valuation, 30B Series G funding
  - Council on Foreign Relations keynote (March 2025)
  - India AI Impact Summit (February 2026)
  - Progressive taxation on AI-driven profits advocacy
  - L3 depth: Thought analysis, quote density >30%

- **[[entities/mustafa-suleyman]]** — Mustafa Suleyman: Microsoft AI CEO & 3x founder. Page covers:
  - Working-class North London upbringing, Syrian immigrant family
  - Oxford philosophy dropout, Muslim Youth Helpline co-founder
  - DeepMind co-founder & CPO (2010-2019) with Hassabis & Legg
  - Inflection AI co-founder (2022-2024) with Reid Hoffman
  - Microsoft AI CEO (2024-present), reports to Satya Nadella
  - "The Coming Wave" book (2023) - AI containment framework
  - Applied ethics philosophy vs. temporary AI pauses
  - AI consciousness warnings and "AI psychosis" concept
  - Management style controversies (2019 administrative leave)
  - CBE (2019), WTF Innovators Award (2023)
  - L3 depth: Philosophical analysis, direct quotes, controversy coverage

- **[[entities/demis-hassabis]]** — Sir Demis Hassabis: Google DeepMind CEO. Page covers:
  - Chess prodigy (master by 13, Elo 2300), second-highest U14 globally
  - Game development: Theme Park (Bullfrog, 1994), Black & White (Lionhead, 2001)
  - Elixir Studios founder (2000-2005)
  - Cambridge CS (Double First), UCL neuroscience PhD (hippocampus & episodic memory)
  - DeepMind co-founder (2010) with Suleyman & Legg
  - AlphaGo vs Lee Sedol (2016), AlphaGo Zero, AlphaZero
  - AlphaFold 1/2/3 - protein structure prediction breakthrough
  - Google acquisition (2014, ~£400M)
  - Google DeepMind merger (2023), Gemini development
  - AGI predictions (50% by 2030, "10x industrial revolution")
  - 2024 Nobel Prize in Chemistry (shared with Jumper & Baker)
  - Knighthood (2024), Companion of Honour (2023)
  - NHS data privacy controversies
  - L3 depth: Comprehensive career analysis, philosophical framework

### Updated
- **wiki/index.md** — Added three new entries to Frontier AI Leaders section, entity count to 70
- L3 depth achieved for all three pages

### Key Insights
- **Different approaches to AI safety**: Amodei (Constitutional AI, RSP), Suleyman (applied ethics, containment), Hassabis (internal governance, empirical milestones)
- **Gaming-to-AI pipeline**: Both Suleyman and Hassabis came through game development, reinforcing the connection between interactive systems and intelligence research
- **Physics/neuroscience roots**: Amodei's physics PhD and Hassabis's neuroscience PhD show how non-CS backgrounds contribute unique perspectives to AI
- **Three-way competition**: Amodei (Anthropic), Suleyman (Microsoft), and Hassabis (Google) represent three different paths to AGI development
- **Ethical frameworks**: All three advocate for some form of AI safety governance, but with different implementations

### Sources
- Grokipedia: Dario Amodei, Mustafa Suleyman, Demis Hassabis
- Anthropic publications and RSP documentation
- DeepMind/Google DeepMind research papers
- Nobel Prize in Chemistry 2024 announcement
- Council on Foreign Relations, India AI Impact Summit keynotes
- "The Coming Wave" (Suleyman & Bhaskar, 2023)
- "Concrete Problems in AI Safety" (Amodei et al., 2016)
- UCL Gatsby Unit publications (Hassabis PhD research)

---

## 2026-04-15 — Hugo Bowne-Anderson Entity Page Created (L3 depth)

### New Entity Pages
- **[[entities/hugo-bowne-anderson]]** — Hugo Bowne-Anderson (@hugobowne): Independent AI educator, podcaster, consultant. Vanishing Gradients host. Page covers:
  - Core Philosophy: "Evaluation is the engine, not the afterthought" — Eval-driven development for AI systems
  - "Beyond Prompt-and-Pray" (O'Reilly, Jan 2025): Structured automation over runtime agent improvisation
  - "Escaping POC Purgatory" (O'Reilly, Apr 2025): Eval-first methodology with synthetic data bootstrapping
  - Vanishing Gradients Podcast: 72+ episodes with guests including Wes McKinney, Fei-Fei Li, Hamel Husain, Shreya Shankar, Samuel Colvin
  - Career: Max Planck → Yale → DataCamp (30+ courses, 6M+ learners) → Coiled → Outerbounds (Metaflow) → Independent
  - GitHub: 56 repos, top projects include deep-learning-from-scratch-pytorch (121★), building-with-ai (91★), build-your-own-deep-research-agent (64★)
  - Maven course co-instructor with Stefan Krawczyk on "Building AI Applications"
  - Conceptual frameworks: Traditional SDLC vs AI SDLC, Prompt-and-Pray vs Structured Automation, Eval Harness as Operating System

### Updated
- **wiki/index.md** — Added Hugo Bowne-Anderson to "AI Education & Evaluation" section, entity count to 67

### Key Insights
- **"You're not launching a product: You're launching a hypothesis."** — AI development requires experimental mindset
- **Structured Automation over Prompt-and-Pray**: Business logic must be decoupled from conversational AI for production reliability
- **POC Purgatory**: Teams build flashy LLM demos that never reach production due to nondeterminism and lack of structured validation
- **Eval-First Methodology**: Start with ~50 manually written queries → bootstrap synthetic data → build automated eval harness → iterate via rejection analysis
- **The "Agent Paradox"** (Ep. 66): Most productive enterprise AI systems aren't full agents — they're structured workflows with narrow scopes
- **Connection to Harness Engineering**: Hugo's "Structured Automation" thesis directly aligns with Ryan Lopopolo's Harness Engineering — control and reliability trump autonomy

### Sources
- https://hugobowne.substack.com/ (Vanishing Gradients podcast/newsletter)
- https://www.oreilly.com/people/hugo-bowne-anderson/ (O'Reilly author page)
- https://github.com/hugobowne (GitHub)
- https://hugobowne.github.io/ (Personal blog)
- https://medium.com/@hugobowne (Medium)
- https://www.linkedin.com/in/hugo-bowne-anderson-045939a5 (LinkedIn)

---

## 2026-04-15 — Dax Raad Entity Page Created

### New Entity Pages
- **[[entities/dax-raad]]** — Dax Raad (@thdxr): Co-founder of Anomaly, creator of OpenCode and SST. Page covers:
  - OpenCode: 135k+ GitHub stars, 1.5M+ MAUs, open-source AI coding agent (MIT License)
  - SST (Serverless Stack): 25k+ stars, profitable by 2025
  - "The Honest Take" on AI productivity (Feb 2026 viral tweet, 793k+ views): "Your org rarely has good ideas. Ideas being expensive to implement was actually helping."
  - Core ideas: AI productivity skepticism, "slop" crisis warning, model agnosticism, local-first philosophy, DX over benchmarks
  - Business model: OpenCode Zen for API access, but "bring your own keys" remains the primary model
  - Other projects: Bumi (local-first sync), OpenAuth
  - Related entities: Jay V, Frank Wang, Adam Elmore, Paul Copplestone

### Updated
- **wiki/index.md** — Added Dax Raad to "Coding Agents & Terminal Tools" section, entity count to 65

### Key Insights
- **Coding was never the bottleneck**: Raad argues the real constraints are good ideas, motivation, bureaucracy, and the "realities of shipping something real"
- **"Slop" crisis**: AI-assisted PRs have 1.7x more bugs; high-performers get overwhelmed reviewing low-quality AI code and quit
- **Model agnosticism as moat**: OpenCode's "bring your own keys" approach differentiates it from locked-in competitors
- **Terminal-first development**: OpenTUI (Zig + SolidJS) reflects commitment to superior developer experience for power users
- **Open source pragmatism**: "Just because something's open source doesn't mean it's going to be any better" — open is a means to iterate fast, not just an ethical stance

### Sources
- https://blog.codacy.com/the-creator-of-opencode-thinks-youre-fooling-yourself-about-ai-productivity
- https://medium.com/@jpcaparas/how-opencode-went-from-zero-to-titan-in-eight-months-dcdcd8ff5572
- https://embed.businessinsider.com/dax-raad-post-ai-coding-workplace-bottleneck-productivity-2026-2
- https://reading.sh/dax-raad-just-dropped-the-most-honest-take-on-ai-productivity-fd8c552b4dd7
- https://news.qq.com/rain/a/20260220A03OXQ00
- https://github.com/anomalyco/opencode

---

## 2026-04-15 — Sero (0xSero) Entity Enriched to L3 Depth

### Updated Entity Pages
- **[[entities/sero]]** → **L3 depth** (was L2). Major expansion:
  - Homelab hardware build breakdown ($12,360 total: 8x RTX 3090, 192GB VRAM, 512GB RAM, EPYC 7443P)
  - Performance benchmarks: 3,000-9,000 TPS prefill, 30-50 TPS generation, 180k-500k+ context window
  - Cerebras REAP benchmark for GLM-4.5-Air-Reap-82b (8-bit)
  - Model preference rankings (S-Tier: GLM-4.5-Air, GLM-4.5V, MiniMax-M2.1; A-Tier: Hermes-70B, Qwen-72B, GPT-OSS-120B)
  - New projects: TurboQuant (976 stars, KV cache quantization), pi-brain (151 stars, privacy-first dataset extraction), factory-cursor-bridge (62 stars, BYOK proxy for Cursor), Thrive Protocol ($150M+ committed capital)
  - Updated Open Orchestra details (269 stars, hub-and-spoke orchestration, Neo4j memory, 6 worker profiles)
  - Updated project star counts (AI Data Extraction: 594, Parchi: 461, vLLM Studio: 366, Azul: 165, Mem-Layer: 78)
  - 12+ direct quotes covering Freedom Tech, anti-inference resale, digital wellness, model comparisons, and AI philosophy
  - AI/LLM stance section: Anthropic anthropomorphism criticism, Codex vs GPT-5.4 comparison, Pi caching praise
  - 200+ public repositories count updated
  - Private Home RAG details (1.2TB indexed, BGE-M3 embeddings, HNSW index)
  - Cost analysis: ~$10,000/mo value → ~$2,012 actual cost → ~$50/mo electricity with homelab

### Updated Files
- **wiki/index.md** — Added Sero to "AI Infrastructure & Open Source" section, entity count 65→66
- **wiki/log.md** — This entry

### Key Insights
- **"Freedom Tech" philosophy** — technology that empowers individuals rather than creating corporate lock-in
- **Anti-inference resale stance** — "selling inference is not the right choice for any wrapper, ADE, etc."
- **Digital wellness rules** — strict guidelines including no AI-written content, no LLM relationships, avoid short-form content
- **Homelab economics** — demonstrates that competitive AI inference is achievable on consumer hardware at ~2% the cost of cloud subscriptions
- **TurboQuant honesty** — publicly corrects his own "5.1x compression" claim to the honest ~4.6x figure, showing intellectual integrity
- **Trajectory pattern** — Content protection → Web3/DAOs → AI Infrastructure, driven by "becoming a father" turning point

### Sources
- https://github.com/0xSero (200+ repositories)
- https://x.com/0xsero (X/Twitter activity)
- https://www.sybilsolutions.ai/ (Sybil Solutions)
- https://blog.thriveprotocol.com/about (Thrive Protocol)

---

## 2026-04-15 — gm8xx8 Entity L3 enrichment, index.md updated

### New/Updated Entity Pages
- **[[entities/gm8xx8]]** → Upgraded from skeleton to L3 depth. Page covers:
  - Pseudonymous AI infrastructure researcher with 132K Farcaster followers, 7K X followers
  - cuLA (CUDA linear attention kernels) contributor — targeting Blackwell SM10X, Hopper SM90
  - MiroMindAI ecosystem contributor (trace-blame, MiroEval, MiroRL)
  - Active across 10+ OSS projects: capgym, GLM-skills, DIAL, MyPhoneBench, varex-bench
  - Core philosophy: efficiency-first architectures, attention alternatives (FFT, linear, M2RNN), KV cache optimization
  - HuggingFace activity: M2RNN/GDN model evaluation, 14 models liked in open-lm-engine collection
  - "Practitioner-researcher" pattern: surfacing papers → technical analysis → code contributions
  - Related entities: xjdr, Grad, karpathy, Chaofan Yu (cuLA lead), Max Fu (capgym)
- **wiki/index.md** — Added gm8xx8 to "AI Infrastructure & Open Source" section, updated entity count to 64

### Key Insights
- **Signal filter role** — gm8xx8 acts as a critical information filter for ML systems community
- **Attention alternatives focus** — Consistent engagement with non-quadratic attention (FFT, linear, delta networks)
- **Agent-native infrastructure** — trace-blame explicitly designed for Claude Code/agent consumption with install-skill
- **Pseudonymous impact** — No public real name or personal website, yet 132K Farcaster followers
- **Cross-stack contributor** — From CUDA kernels (lowest level) to robot manipulation benchmarks (highest level)

---

## 2026-04-15 — Benjamin Clavié Entity L3 confirmed, index.md updated

### Updated Entity Pages
- **[[entities/benjamin-clavi]]** → L3 depth already confirmed. Page covers:
  - RAGatouille (3.9k★) creator, ModernBERT co-lead (5.5k★), Mixedbread ML R&D, NII Tokyo PhD
  - Core philosophy: "ColBERT is a semantic keyword matcher", "Retrieval is the bottleneck of practical AI"
  - 8 detailed Core Ideas sections with direct quotes (>30% quote rate achieved)
  - JaColBERT, mxbai-edge-colbert-v0, Wholembed v3 (Recall@5 92.45, surpassing BM25)
  - Late Interaction Workshop @ ECIR 2026 organizer, Mixedbread Search agentic search
  - Complete career timeline (2017-2026), influence metrics, key quotes, related entities
  - Health/productivity philosophy ("Working While Sick")
- **wiki/index.md** — Added "Information Retrieval & RAG" section with Benjamin Clavié entry

### Key Insights
- **"Semantic keyword matcher"** — Clavié's most powerful framing: ColBERT isn't dense retrieval, it's TF-IDF with neural semantics
- **BM25 surpassing is possible** — Wholembed v3 achieves Recall@5 92.45 vs BM25's 85.7 on LIMIT benchmark
- **Agentic search** — Mixedbread Search optimizes for AI agent queries (sub-90ms latency), not human-written queries
- **Open IR community** — Clavié advocates for the same open growth NLP/LM experienced, applied to Information Retrieval
- **ML democratization** — "ML is infrastructure now" — bridging research-practice gap through open-source toolchains
- **Small model philosophy** — 17M params outperforming ColBERTv2, challenging "bigger is better" narrative

---

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
