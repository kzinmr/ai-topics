# Wiki Schema

## Domain
AI/ML research and engineering — tracking models, platforms, tools, frameworks, and engineering practices in the AI ecosystem.

## Conventions
- File names: lowercase, hyphens, no spaces (e.g., `transformer-architecture.md`)
- Every wiki page starts with YAML frontmatter (see below)
- Use `[[wikilinks]]` to link between pages (minimum 2 outbound links per page)
- When updating a page, always bump the `updated` date
- Every new page must be added to `index.md` under the correct section
- Every action must be appended to `log.md`

## Frontmatter
```yaml
---
title: Page Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query | summary
tags: [from, taxonomy, below]
sources: [raw/articles/source-name.md]
---
```

## Tag Taxonomy (Canonical)

### Core Types (auto-set by type field)
- `concept`, `entity`, `comparison`, `query`, `summary`, `coding-agent`, `memory-system`, `person`

### Primary Categories
- **Models**: model, multimodal, text-generation, image-generation, video-generation, audio-generation, local-llm, sglang, reasoning, reinforcement-learning, mixture-of-experts, moe, rlm, long-context, neurosymbolic, interpretability, vlm, transformers, llm, transformer-architecture, rwkv, non-transformer, autoregressive, foundation-models, hybrid-reasoning
- **People/Orgs**: company, lab, open-source, anthropic, openai, google, deepmind, huggingface, nvidia, langchain, pytorch, microsoft, deepseek, mistral, qwen, alibaba, ant-group, xai, databricks, earendil, ibm, eleutherai, nous-research, discord, meta, sourcegraph, xiaomi, zyphra, ai-research, ai-researcher, cloudflare, indie-maker, ycombinator, chroma, entrepreneur, founder, researcher, pseudonymous, prime-intellect, browserbase, prefect, linear, nist, sentry, vercel, shopify, modal, daytona, ceo, cohere, stability-ai, stanford, mit, palantir, tencent, sakana-ai, jetbrains, japan, tokyo, france
- **Products**: product, platform, tool, service, protocol, framework, claude-code, codex, cursor, github-copilot, mcp, dspy, browser-agent, managed-agents, ai-native, agent-native, browser-automation, gemini, generative-ui, notion-cli, notion-mcp, warp, hermes-agent, datasette, enterprise-saas, antigravity, service-as-software, agent-platform, pricing, business-model, promptfoo, slack, obsidian, openrouter, grok, optuna, kaggle, vllm, torchspec, mem0, bedrock
- **Techniques**: inference, fine-tuning, training, optimization, quantization, alignment, benchmark, evaluation, speculative-decoding, diffusion, prompting, metaprompting, rag, kv-cache, testing, property-based-testing, sandbox, synthetic-data, datasets, distillation, post-training, distributed-training, grpo, rlhf, dpo, lora, peft, chain-of-thought, scaling, embeddings, data-science, data-visualization, information-retrieval, query-understanding, lexical-search, agentic-search, agentic-retrieval, bm25, bm25f, multi-field-search, metadata-retrieval, explainable-ranking, tokenization, vector-search, hnsw, ann, retrieval, direct-corpus-interaction, voice-ai, evolutionary-algorithms, streaming, middleware, prompt-caching, token-economics, model-routing, rlvr, test-time-scaling, chat-template, nanogpt-speedrun, bayesian, gepa, realtime, translation, edge-ai, hierarchical, recurrent, latent-space, training-efficiency, overfitting, adversarial, reward-hacking, self-play, colbert, late-interaction, maxsim, multi-vector, simulation, drowning-in-documents, hill-climbing, benchmark-optimization, trace-analysis, bertopic, clustering, fused-kernels, memory-efficiency, simd, simd-optimization, score-matching, block-wise-training, residual-networks, model-merging, deep-learning, niah, needle-in-haystack, context-rot, context-degradation, query-expansion, position-interpolation, context-extension, rope, position-encoding, beir, mteb, model-training, programmatic-tool-calling
- **Engineering**: agentic-engineering, harness-engineering, backend-engineering, ai-agent-engineering, context-engineering, context-management, multi-llm, workflow, software-engineering, programming-language, python, go, kotlin, java, formal-methods, developer-tooling, cli, terminal, ide, api, git, filesystem, docker, pydantic, observability, monitoring, reliability, devops, mlops, ml-engineering, cloud, serverless, ai-infrastructure, agent-infrastructure, developer-experience, web-development, decision-centric, agent-ergonomics, ai-coding, vibe-coding, cost-optimization, cost, code-review, technical-debt, deterministic, probabilistic, feedback-loop, design-patterns, progressive-disclosure, ai-automation, performance, performance-engineering, typescript, dotnet, rust, plugins, extensibility, code-quality, production-ml
- **AI Agents**: ai-agents, multi-agent, orchestration, agent-orchestration, agent-coordination, agents, coding-agents, memory-systems, agent-memory, agent-safety, prompt-injection, openclaw, agent-harness, agent-framework, agent-sdk, agent-architecture, agent-runtime, agent-evaluation, agent-security, agent-communication, autonomous-agents, subagents, computer-use, human-in-the-loop, tool-use, cognition, durable-execution, self-improving, self-replicating, recursive-self-improvement, personal-ai, agent-media, skill-graph, content-engine, enterprise-ai, knowledge-graph, agent-loop, autoresearch, ralph-loop, deep-research, planning-agent, research-agent, ambient-agents, agent-training, agent-skills, verification, deep-agents, code-intelligence, proactive, acp, agent-communication-protocol, agent-design-patterns, agent-tooling, enterprise-agents, agent-identity, agent-governance, agent-forking, lineage-tracking, agent-ontology, meta-harness, agent-employees, human-agent-collaboration, human-sandwich, notebook-agents, code-act, plan-then-execute
- **Infrastructure**: platform, protocol, security, architecture, infrastructure, hardware, aws, ray, database, sqlite, isolation, nlp, networking, gpu, vram, apple-silicon, macos, webview, webrtc, moq, amd, email, virtualization, state-management, data-flow, event-sourcing, reactive-systems, langsmith, coinbase, mtp, hybrid-architecture, llm-proxy, self-hosted, object-storage, file-storage, cloud-infrastructure, ml-infrastructure, kubernetes, data-integration, control-plane, multi-tenancy, audit, communication
- **Meta**: comparison, timeline, controversy, prediction, review, survey, taxonomy, safety, ai, ai-safety, announcement, event, vulnerability, supply-chain, blogger, content-creator, developer-tooling, ecosystem, community, search, methodology, epistemology, probabilistic-systems, governance, reliability, automation, cron, hn-popular, x-account, education, educator, philosophy, philosophy-of-science, economics, platform-economics, vendor-lock-in, privacy, regulation, policy, ethics, ai-adoption, ai-assistance, ai-governance, geopolitics, agi, career, career-strategy, writing, blog, robotics, fintech, china, reverse-engineering, emerging, curriculum, product-management, ai-product, ai-native, active, industry, research, real-time, youtube, podcast, ai-society, content-quality, information-ecosystem, ai-detection, mental-health, quality-assurance, strategy, positioning, narrative, ai-commentary, valuation, consulting, power, structured-outputs, lean-startup, customer-development, innovation, bizops, strategy-execution, technical-literacy, leadership, law, startup, internship, robustness, vc, investor, ai-slop, automation-paradox, benchmark-framing, saas, fde, ai-consulting, transparency, religion, knowledge-management
- **Domain Concepts**: coordination, game-theory, existential-risk, memetics, transhumanism, rationality, techno-pessimism, techno-optimism, singularity, evolution, selection-theorem, information-theory, agent-foundations, world-models, causal-reasoning, resource-allocation, mechanistic-interpretability, circuits, superposition, crypto, defi, distributed-systems, local-first, psychology, causal, zeno-paradox, business-process, workflow-mapping, nature-inspired, collective-intelligence, competitive-programming, conversational-ai, sports-analytics, biotech

### Guidelines
- Every tag must be a useful category — avoid one-off tags that just restate the page title
- Prefer plural forms: `memory-systems` not `memory-system`, `coding-agents` not `coding-agent`
- Tags are lowercase kebab-case only — no wikilinks, no leading dashes, no spaces
- Add commonly used new tags here first, then use them across pages

Rule: every tag on a page must appear in this taxonomy. If a new tag is needed,
add it here first, then use it. This prevents tag sprawl.

## Page Thresholds
- **Create a page** when an entity/concept appears in 2+ sources OR is central to one source
- **Add to existing page** when a source mentions something already covered
- **DON'T create a page** for passing mentions, minor details, or things outside the domain
- **Split a page** when it exceeds ~200 lines — break into sub-topics with cross-links
- **Archive a page** when its content is fully superseded — move to `_archive/`, remove from index

## Entity Pages
One page per notable entity. Include:
- Overview / what it is
- Key facts and dates
- Relationships to other entities ([[wikilinks]])
- Source references

## Concept Pages
One page per concept or topic. Include:
- Definition / explanation
- Current state of knowledge
- Open questions or debates
- Related concepts ([[wikilinks]])

## Comparison Pages
Side-by-side analyses. Include:
- What is being compared and why
- Dimensions of comparison (table format preferred)
- Verdict or synthesis
- Sources

## Update Policy
When new information conflicts with existing content:
1. Check the dates — newer sources generally supersede older ones
2. If genuinely contradictory, note both positions with dates and sources
3. Mark the contradiction in frontmatter: `contradictions: [page-name]`
4. Flag for user review in the lint report
