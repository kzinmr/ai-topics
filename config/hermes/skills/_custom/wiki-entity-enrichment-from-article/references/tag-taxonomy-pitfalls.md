# Tag Taxonomy Pitfalls — Pre-Commit Hook Reference

When editing any wiki page (entity, concept, comparison, event, query), the `pre-commit` hook in `ai-topics/.githooks/pre-commit-tag-validator.py` blocks commits that contain tags not registered in `wiki/SCHEMA.md`'s canonical taxonomy.

## The Hook

Hook path: `ai-topics/.githooks/pre-commit`
Validator: `ai-topics/.githooks/pre-commit-tag-validator.py`
Taxonomy source: `wiki/SCHEMA.md`

On commit, the hook:
1. Scans all staged `.md` files in `wiki/` for YAML frontmatter `tags:`
2. Validates each tag against the canonical list in SCHEMA.md
3. Prints a detailed error listing: file path, invalid tag name
4. Blocks the commit (exit code 1) if any violation found

## Prevention Checklist

**Before every `git commit` that modifies wiki pages:**

1. **Identify all new tags** you added to page frontmatter
2. **Search SCHEMA.md** for each tag: `search_files(pattern="tagname", path="wiki/SCHEMA.md")`
3. **If tag is missing**, add it to the appropriate category:

| Category | Examples | Common new additions |
|---|---|---|
| Products | tool, platform, service, framework, product | `openrouter`, new IDE/tool names |
| People/Orgs | company, lab, anthropic, openai | `siliconflow`, new company names |
| Models | model, llm, moe, text-generation | New model family names |
| Techniques | prompting, rag, kv-cache, fine-tuning | New technique names |
| AI Agents | ai-agents, coding-agents, agent-safety | New agent-related concepts |
| Infrastructure | cloud, gpu, security, architecture | New infra technologies |

4. **Add missing tags** to SCHEMA.md, preserving the comma-separated format
5. **Verify placement**: SCHEMA.md categories are long comma-separated lines — `patch` fuzzy matching has been known to insert tags into the WRONG category. Re-read the line after editing.
6. **Stage both files**: `git add wiki/SCHEMA.md` alongside your page changes

## When the Hook Blocks Your Commit

The error output is precise. Example:

```
🚨 TAG TAXONOMY VIOLATIONS — COMMIT BLOCKED
⚠️  TAGS NOT IN SCHEMA.md TAXONOMY (1):
   wiki/entities/tencent-hy3.md:  openrouter

   Fix options:
   1. Add 'openrouter' to SCHEMA.md taxonomy
   2. Map it to an existing canonical tag
   3. Use an existing SCHEMA tag instead
```

**Response**: Add `openrouter` to the Products category in SCHEMA.md, `git add`, retry commit.

## Common Non-Canonical → Canonical Mappings

| Non-Canonical | Canonical | Notes |
|---|---|---|
| `rl` | `reinforcement-learning` | Shorthand never works |
| `llm-training` | `training` | Drop the `llm-` prefix |
| `llm-infrastructure` | `ai-infrastructure` | Use `ai-` not `llm-` |
| `exploration` | (no canonical) | Use `inference`, `reasoning`, or `scaling` |
| `interview` | (no canonical) | Use `career` |
| `dllm` | (no canonical) | Use `reinforcement-learning` or `diffusion` |
| `ai-alignment` | `alignment` | Drop the `ai-` prefix |
| `benchmarking` | `benchmark` | Noun form, not gerund |
| `cuda` | `gpu` | Use the broader `gpu` tag; CUDA-specific context goes in page body |
| `decentralized-ai` | `sovereign-ai` | Use `sovereign-ai` for decentralized/distributed AI philosophy |
| `agentic-model` | `ai-agents` + `model` | Use both existing tags; compound model-type tags are rarely canonical |
| `legal` | `law` | Use `law` for legal disputes, lawsuits, regulatory actions |
| `learning` | `education` | Use `education` for learning tools, pedagogy, educational content |
| `ui` | `frontend` | Use `frontend` OR `gui` for user interface topics |
| `infinite-canvas` | (no canonical) | Drop it — the concept doesn't fit a single canonical tag; describe in page body |

See also: `references/tag-taxonomy-quick-reference.md` for the full mapping table.
See also: `references/tag-taxonomy-openai-concept-mappings.md` for OpenAI/company concept page tag mappings and Japanese content policy.

## Historical Incidents

- **2026-05-27**: Agent added `openrouter` tag to `entities/tencent-hy3.md` without registering it in SCHEMA.md. Pre-commit hook blocked commit. Fixed by adding `openrouter` to Products category.
- **2026-05-13 (batch-person-entity)**: Tags `researcher` and `pseudonymous` added to person pages without SCHEMA.md registration. Hook blocked commit. Also: `llm-proxy` was inserted into Engineering AND Infrastructure categories due to `patch` fuzzy matching on long lines.
- **2026-06-12 (RL interview pages)**: Multiple non-canonical tags in batch-created pages: `rl` (→ `reinforcement-learning`), `interview` (no canonical), `llm-training` (→ `training`), `llm-infrastructure` (→ `ai-infrastructure`), `dllm` (no canonical), `exploration` (no canonical). Required two fix rounds. Lesson: when creating pages from a non-English source (Chinese Zhihu interview list), the translated topic names rarely match canonical tags — always validate against SCHEMA.md before the first commit attempt.
- **2026-06-15 (PerfCodeBench arxiv ingestion)**: Tag `cuda` used in `kernelbench.md` frontmatter — not in SCHEMA.md taxonomy. Pre-commit hook blocked commit. Fixed by replacing `cuda` with canonical `gpu`. Lesson: even obvious technology names (CUDA, cuDNN, Triton) must be checked against SCHEMA.md — prefer broader existing tags (`gpu`, `hardware`) and put specificity in the page body.
- **2026-07-11 (blog-triage)**: Tags `decentralized-ai` and `legal` used in new entity/event pages without SCHEMA.md registration. Pre-commit hook blocked commit. Fixed by mapping `decentralized-ai` → `sovereign-ai` and `legal` → `law`. Lesson: descriptive compound tags (`decentralized-ai`, `legal-tech`-adjacent) often aren't canonical — prefer existing single-word or established tags.
- **2026-07-29 (blog-wiki-ingest, cryptanalysisbench)**: Tags `ai-benchmarks`, `llm-security`, `model-evaluation`, `cryptography` used in new `concepts/ai-benchmarks/cryptanalysisbench.md` — none in SCHEMA.md taxonomy. Fixed by mapping `ai-benchmarks` → `benchmark`, `llm-security` → `security`, `model-evaluation` → `evaluation`, `cryptography` → `crypto`. Lesson: the `concepts/ai-benchmarks/` directory name is a strong attractor for the compound tag `ai-benchmarks`, but the canonical tag is just `benchmark` (Techniques section). Always destructure compound names into existing single-word tags.
- **2026-08-02 (newsletter-wiki-ingest, kim-isenberg enrichment)**: Raw article `raw/articles/2026-08-01-the-duel-that-never-happened.md` carried frontmatter tags `[ai-benchmarks, ai-evaluation, ai-industry, paywalled]` — NONE canonical. Layer-1 raw files are NOT hook-validated, so they can carry non-canonical tags; do NOT copy raw frontmatter tags verbatim into Layer-2 entity/concept pages. Mapped to `benchmark`, `benchmark-framing` (+ existing `ai-governance`, `ai-adoption`) and the commit passed validation first try. Lesson: when enriching from a raw article, treat its frontmatter tags as a *suggestion*, always re-validate against SCHEMA.md (raw tags `ai-evaluation` → use `evaluation` or `benchmark-framing` contextually).
- **2026-08-10 (manual article ingestion, Meta Muse Glimmer)**: Tag `agentic-model` used in `entities/muse-glimmer.md` frontmatter — not in SCHEMA.md taxonomy. Pre-commit hook blocked commit. Fixed by removing `agentic-model` and adding `ai-agents` (existing canonical tag for agent-related models). Lesson: compound descriptive tags like `agentic-model`, `coding-model`, `reasoning-model` are rarely canonical — prefer the existing `model` tag plus a domain tag (`ai-agents`, `code-model`, `reasoning`) from the taxonomy.
- **2026-08-05 (manual article ingestion, Yegge "Shape of Things to Come")**: Tags `emacs` and `bespoke` used in `concepts/wheelhouse.md` frontmatter — neither in SCHEMA.md taxonomy. Pre-commit hook blocked commit. Fixed by replacing both with `customization` (existing canonical tag). Lesson: tool/IDE names (`emacs`, `vim`, `ghostty`) and descriptive adjectives (`bespoke`, `custom`, `tailored`) are almost never canonical tags — map to broader categories like `customization`, `ide`, or `terminal`.
