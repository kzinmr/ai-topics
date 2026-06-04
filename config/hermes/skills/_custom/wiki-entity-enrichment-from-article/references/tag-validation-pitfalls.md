# Tag Validation Pitfalls — blog-ingest session 2026-05-30

## The Problem

The pre-commit hook (`pre-commit-tag-validator.py`) in the ai-topics repo validates ALL `tags:` in YAML frontmatter against the canonical taxonomy defined in `wiki/SCHEMA.md`. If any tag is not in SCHEMA.md, the commit is BLOCKED with an error listing the violations.

## What Happened

During a blog-ingest session, three new wiki pages were created with intuitive but non-canonical tags. The commit was rejected with 9 tag violations:

```
❌ TAGS NOT IN SCHEMA.md TAXONOMY:
   ai-evaluation      → should be: evaluation
   developer-tools    → should be: developer-tooling
   benchmarking       → should be: benchmark
   biosecurity        → use: ai-safety, policy
   trusted-access     → use: ai-safety, policy
   government         → use: policy, announcement
   preparedness-framework → use: ai-safety, evaluation
   frontier-models    → use: evaluation, ai-safety
   ai-eval            → use: evaluation
   safety             → should be: ai-safety
```

## Canonical Tag Categories (from SCHEMA.md)

| Category | Key Tags |
|----------|----------|
| **Models** | model, multimodal, llm, reasoning, transformers, moe, peft, lora, grpo, rlhf, dpo, quantization, inference |
| **People/Orgs** | company, lab, open-source, anthropic, openai, google, deepmind, nvidia, blogger, researcher, founder, entrepreneur |
| **Products** | product, platform, tool, service, framework, claude-code, codex, cursor, mcp, notion, vllm, bedrock |
| **Techniques** | inference, fine-tuning, training, optimization, benchmark, evaluation, rag, distillation, post-training, chain-of-thought, scaling, synthetic-data, datasets, testing, sandbox |
| **Engineering** | agentic-engineering, harness-engineering, developer-tooling, observability, monitoring, reliability, devops, mlops, ai-infrastructure |
| **AI Agents** | ai-agents, multi-agent, orchestration, coding-agents, agent-evaluation, agent-safety, agent-harness, tool-use, memory-systems, computer-use |
| **Infrastructure** | gpu, vram, cloud, serverless, database, networking, kubernetes, ml-infrastructure |
| **Meta** | comparison, timeline, controversy, prediction, review, survey, safety, ai-safety, announcement, vulnerability, governance, policy, ethics, economics, regulation |
| **Domain Concepts** | game-theory, existential-risk, singularity, crypto, distributed-systems, psychology, philosophy |

## The Fix Pattern

When creating a new wiki page:

1. **Decide tags first** — before writing frontmatter
2. **Search SCHEMA.md** — `search_files` for candidate tag strings to verify they exist
3. **Map intuitive → canonical**:
   - "ai-evaluation", "ai-eval" → `evaluation`
   - "developer-tools" → `developer-tooling`
   - "benchmarking" → `benchmark`
   - "safety" → `ai-safety`
   - Anything about government/policy/regulation → `policy`, `governance`, `regulation`
   - "frontier-models" → `model`, `llm`
   - Domain-specific concepts → check if `ai-safety`, `evaluation`, `announcement` cover it

## Prevention

Add this checklist item to any wiki page creation task:
> ☐ Tags validated against SCHEMA.md taxonomy
