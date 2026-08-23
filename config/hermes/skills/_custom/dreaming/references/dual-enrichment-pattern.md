# Dual-Enrichment Pattern — Cross-Page Content Spanning

## Problem

A single raw article may contain content that belongs on **two different wiki pages** — an entity page AND a concept page. The triage `candidate_wiki_path` only points to the primary canonical path, so the secondary enrichment target goes unaddressed.

## Concrete Example (July 2026)

**Article**: "Make Kimi K3 Yours: LoRA Training on Fireworks" (fireworks.ai blog)

| Aspect | Natural home | Why |
|--------|-------------|-----|
| Pricing, serving modes, infrastructure | `entities/fireworks-ai.md` | Fireworks' K3 LoRA service offering |
| K3 post-training methods, reward design, concrete tasks | `concepts/kimi-k3.md` | K3's available customization methods |

Triage marked `candidate_wiki_path: entities/fireworks-ai.md` — correct for Fireworks' capabilities, but `concepts/kimi-k3.md` also lacked the LoRA training content.

## Detection Heuristics

During Deep Sleep verification, check for dual-enrichment opportunities:

1. **Article source**: Is the article from a COMPANY blog (Fireworks, Cohere, Harvey) about a MODEL or PLATFORM? → Check the model's concept page.
2. **Article source**: Is the article from a company about a PRODUCT or FEATURE that affects an EXTERNAL ECOSYSTEM? → Check the ecosystem's concept page.
3. **Article author**: Is the article about PERSON X but discusses TECHNOLOGY Y? → Check both `entities/person.md` and `concepts/technology.md`.

**Quick check**: For any take whose article mentions model names (K3, GLM-5.2, Opus), product categories (agent orchestration, document processing), or frameworks (LoRA, MCP):
```bash
# Check if a concept page exists for the mentioned model/topic
find /opt/data/ai-topics/wiki/concepts -name "*k3*" -type f 2>/dev/null
find /opt/data/ai-topics/wiki/concepts -name "*lora*" -type f 2>/dev/null
```

## Execution

When dual-enriching, structure the enrichment between entity and concept page along these boundaries:

| Content type | Entity page | Concept page |
|-------------|-------------|--------------|
| Company/service capability | ✅ Company's product offering | ❌ Too broad |
| Model/tool post-training methods | ❌ Too narrow | ✅ Model's customization docs |
| Concrete benchmarks and metrics | ✅ Case study results | ✅ If benchmark-specific section exists |
| Broader ecosystem implications | ❌ Context/links to concept | ✅ Why it matters |
| Pricing and deployment specifics | ✅ Fireworks pricing tiers | ❌ Transient |

## Delegation Strategy

Dual-enrichment adds a second `delegate_task` task. Structure the tasks array:

```python
tasks = [
    {"goal": "Enrich entities/fireworks-ai.md with ...", "context": "..."},
    {"goal": "Enrich concepts/kimi-k3.md with ...", "context": "..."},
]
```

Both can run in parallel (they modify different files) — include in the same block up to the concurrent-children limit.
