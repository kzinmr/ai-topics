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
- **Models**: model, multimodal, text-generation, image-generation, video-generation, audio-generation, local-llm, sglang, reasoning, reasoning-model, code-model, reinforcement-learning, mixture-of-experts, moe, rlm, long-context, sparse-attention, neurosymbolic, interpretability, vlm, transformers, llm, transformer-architecture, rwkv, non-transformer, autoregressive, foundation-models, hybrid-reasoning, generative-ai, gpt, transformer, frontier-models, encoder-decoder, claude-fable-5
- **People/Orgs**: company, lab, open-source, legal-tech, anthropic, openai, google, deepmind, huggingface, nvidia, langchain, pytorch, microsoft, deepseek, mistral, llama, qwen, alibaba, ant-group, xai, databricks, earendil, ibm, eleutherai, nous-research, discord, meta, sourcegraph, xiaomi, zyphra, ai-research, ai-researcher, analyst, cloudflare, indie-maker, ycombinator, chroma, entrepreneur, founder, researcher, pseudonymous, prime-intellect, browserbase, prefect, linear, nist, sentry, vercel, shopify, modal, daytona, ceo, cohere, stability-ai, stanford, mit, palantir, tencent, sakana-ai, jetbrains, japan, tokyo, france, epoch-ai, skyscanner, dagster, curtis-yarvin, instructor, ilya-sutskever, arena-ai, ml-research, research-lab, spotify, apple, conviction, apache, dagworks
- **Products**: product, platform, tool, service, protocol, framework, environment, claude-code, codex, cursor, devin, github-copilot, mcp, dspy, browser-agent, managed-agents, ai-native, agent-native, agent-first, browser-automation, gemini, generative-ui, notion-cli, notion-mcp, warp, hermes-agent, datasette, hearth-ai, enterprise-saas, antigravity, service-as-software, agent-platform, pricing, business-model, promptfoo, slack, obsidian, openrouter, grok, optuna, kaggle, vllm, torchspec, mem0, bedrock, creao, figma, chatgpt
- **Models**: model, multimodal, text-generation, image-generation, video-generation, audio-generation, local-llm, sglang, inference, fine-tuning, training, quantization, alignment, deliberative-alignment, safe-completions, benchmark, eval-loops, evaluation, evaluations, evals, llm-as-judge, game-based, speculative-decoding, diffusion, prompting, metaprompting, rag, kv-cache, testing, property-based-testing, sandbox, red-teaming, hallucinations, disinformation, synthetic-data, datasets, distillation, post-training, distributed-training, grpo, ppo, rlhf, dpo, lora, peft, chain-of-thought, optimization, scaling, scaling-laws, embeddings, data-science, data-visualization, information-retrieval, neural-reranking, continual-learning, dense-retrieval, query-understanding, lexical-search, llm-query-understanding, agentic-search, agentic-retrieval, search-ranking, bm25, bm25f, multi-field-search, metadata-retrieval, explainable-ranking, tokenization, vector-search, hnsw, ann, retrieval, direct-corpus-interaction, voice-ai, evolutionary-algorithms, streaming, middleware, prompt-caching, token-economics, model-routing, rlvr, test-time-scaling, chat-template, nanogpt-speedrun, bayesian, gepa, realtime, translation, edge-ai, on-device, context-compression, hierarchical, recurrent, latent-space, training-efficiency, overfitting, adversarial, reward-hacking, reward-engineering, self-play, colbert, late-interaction, maxsim, multi-vector, simulation, drowning-in-documents, hill-climbing, benchmark-optimization, trace-analysis, bertopic, clustering, fused-kernels, memory-efficiency, simd, simd-optimization, score-matching, block-wise-training, residual-networks, model-merging, deep-learning, niah, needle-in-haystack, context-rot, context-degradation, query-expansion, position-interpolation, context-extension, rope, position-encoding, beir, mteb, model-training, tool-calling, programmatic-tool-calling, automl, feature-engineering, data-lakes, branching, versioning, mvcc, copy-on-write, activation-steering, silent-intervention, prompt-modification, async-rl, importance-sampling, policy-lag, off-policy, on-policy, self-distillation, generative-retrieval, semantic-ids, chunking, pretraining, open-weight, gemma
- **Engineering**: agentic-engineering, harness-engineering, backend-engineering, ai-software-engineering, ai-agent-engineering, context-engineering, context-management, text-optimization, multi-llm, workflow, software-engineering, software-development, programming-language, python, go, kotlin, java, formal-methods, developer-tooling, developer-tools, llm-engineering, cli, terminal, ide, api, git, filesystem, docker, pydantic, observability, monitoring, experiment-tracking, reliability, devops, mlops, ml-engineering, cloud, serverless, ai-infrastructure, agent-infrastructure, developer-experience, devrel, web-development, decision-centric, agent-ergonomics, ai-coding, vibe-coding, cost-optimization, cost, code-review, technical-debt, deterministic, probabilistic, feedback-loop, design-patterns, progressive-disclosure, ai-automation, performance, performance-engineering, typescript, dotnet, rust, plugins, extensibility, code-quality, production-ml, frontend, ci-cd
- **AI Agents**: ai-agents, multi-agent, orchestration, agent-orchestration, agent-coordination, agents, coding-agents, memory-systems, agent-memory, agent-safety, prompt-injection, openclaw, agent-harness, agent-framework, agent-sdk, agent-architecture, agent-runtime, agent-evaluation, agent-observability, agent-security, agent-communication, autonomous-agents, async-agents, cloud-agents, self-driving-codebases, self-healing, subagents, computer-use, human-in-the-loop, tool-use, cognition, durable-execution, self-improving, self-replicating, recursive-self-improvement, personal-ai, agent-media, skill-graph, content-engine, enterprise-ai, knowledge-graph, agent-loop, autoresearch, ralph-loop, deep-research, planning-agent, research-agent, ambient-agents, agent-training, agent-skills, verification, agents-md, swere-bench, deep-agents, code-intelligence, proactive, acp, agent-communication-protocol, agent-design-patterns, agent-tooling, enterprise-agents, agent-identity, agent-governance, agent-forking, lineage-tracking, agent-ontology, meta-harness, agent-employees, human-agent-collaboration, human-sandwich, notebook-agents, code-act, plan-then-execute, pointer, html, agentic-rl, multimodal-agents, embodied-ai, loops, self-correction, memory
- **Infrastructure**: platform, protocol, security, architecture, infrastructure, hardware, aws, ray, database, sqlite, postgres, isolation, nlp, networking, gpu, vram, apple-silicon, macos, webview, webrtc, moq, amd, email, virtualization, state-management, data-flow, event-sourcing, reactive-systems, langsmith, coinbase, mtp, hybrid-architecture, llm-proxy, self-hosted, object-storage, file-storage, cloud-infrastructure, ml-infrastructure, kubernetes, data-integration, open-data, control-plane, multi-tenancy, audit, communication, sql, data-platform, llm-inference
- **Meta**: comparison, timeline, controversy, prediction, review, survey, taxonomy, safety, ai, ai-safety, announcement, event, build-2026, vulnerability, supply-chain, blogger, content-creator, developer, developer-tooling, ecosystem, community, search, relevance, methodology, epistemology, probabilistic-systems, governance, reliability, automation, cron, hn-popular, x-account, education, educator, philosophy, philosophy-of-science, economics, platform-economics, vendor-lock-in, privacy, regulation, policy, ethics, ai-adoption, author, consultant, ai-assistance, ai-governance, geopolitics, agi, career, career-strategy, writing, blog, robotics, fintech, china, reverse-engineering, emerging, curriculum, product-management, ai-product, ai-native, active, industry, research, real-time, youtube, podcast, ai-society, content-quality, information-ecosystem, ai-detection, mental-health, quality-assurance, strategy, positioning, narrative, ai-commentary, valuation, consulting, power, structured-outputs, lean-startup, customer-development, innovation, bizops, strategy-execution, technical-literacy, leadership, law, startup, internship, robustness, vc, investor, ai-slop, automation-paradox, benchmark-framing, saas, fde, ai-consulting, transparency, religion, knowledge-management, europe, productivity, case-study, content-moderation, platform-policy, ai-content-detection, ai-transparency, ai-ethics, anti-pattern, personal-software, transcript, neurips-2024, search-teams, recsys-2025, trust, permission, tutorial, philanthropy, model-card, system-card, preparedness-framework, domain-specific, eu-ai-act, responsible-scaling-policy
- **Domain Concepts**: coordination, game-theory, existential-risk, memetics, transhumanism, rationality, techno-pessimism, techno-optimism, singularity, evolution, selection-theorem, information-theory, agent-foundations, world-models, spatial-intelligence, causal-reasoning, resource-allocation, mechanistic-interpretability, circuits, superposition, crypto, defi, distributed-systems, local-first, psychology, causal, zeno-paradox, business-process, workflow-mapping, nature-inspired, collective-intelligence, competitive-programming, conversational-ai, sports-analytics, biotech, formal-verification, mathematics, biology, physical-ai, cybersecurity, labor, domain-expertise, ai-moat, cognitive-science, technology-criticism, civilization-decline, thymos, e-acc, gtc, ai-skepticism, political-theory, geospatial, quantified-self, bitter-lesson, scaling-hypothesis, superintelligence, failure-modes, reward-function, system-prompt, chain-of-command, openpipe, ai-educator, private-data, ai-investment, absorption-frontier, legible-work

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

## Naming Policy (Page Filenames)
Wiki filenames (slugs) must be concise, English-only, and descriptive. Enforced by pre-commit hook and `wiki_health.py`.

- **English only**: No CJK characters in filenames (content can be any language)
- **No date-prefix slugs**: `2026-04-23-something` is a raw article title leak, not a concept name
- **Max 10 words** (ERROR at ≥11): If your slug has 11+ hyphen-separated words, it's a tag pile — pick a focused concept name
- **Warn at ≥8 words**: Consider shortening. Descriptive names like `a-philosophy-of-software-design-vs-clean-code` are acceptable; tag piles like `claude-code-prompt-engineering-context-management-caching-agent-architecture` are not
- **Good names**: `claude-code`, `agentic-engineering`, `back-of-house-multi-agent-patterns`, `mcp`
- **Bad names**: `background-agent-orchestration-linear-github-workflow-automation-graph-based` (tag pile), `ai-memory-systems-chatgpt-vs-coding-agent-design-philosophy-comparison` (was CJK, now anglicized)

Checked automatically:
- **Pre-commit hook**: Blocks NEW files with CJK, date-prefix, or ≥11 hyphens
- **wiki_health.py**: Reports all violations (ERROR/WARN) in weekly health digest

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
