# Evaluation vs Safety vs Benchmarks Separation

## The Three-Way Distinction

When classifying pages tagged with `evaluation`, `safety`, `security`, or `benchmark`, apply this taxonomy:

| Directory | Scope | Examples |
|---|---|---|
| `ai-benchmarks/` | Individual benchmark pages (one page per benchmark) | SWE-bench, GPQA, MMLU-Pro, HLE |
| `evaluation/` | Evaluation methodology, metrics, judge frameworks, eval tooling | llm-as-judge, pass-k-metric, ndcg, eval-loops, reward-hacking |
| `security-and-governance/` | Safety, alignment, containment, governance, model cards | ai-safety, agent-governance, model-cards-system-cards, open-model-safety |

## Decision Rules

1. **Is it a specific benchmark?** → `ai-benchmarks/` (even if it has `evaluation` tag)
2. **Is it a metric or evaluation method?** → `evaluation/` (pass-k, ndcg, llm-as-judge)
3. **Is it about safety/alignment/governance?** → `security-and-governance/` (ai-safety, model-cards)
4. **Is it a MOC bridging benchmarks and evaluation?** → `evaluation/` with strong cross-references to `ai-benchmarks/index`

## Metrics Move from ai-benchmarks/ to evaluation/

User explicitly requested: metrics (ndcg, pass-k-metric) belong in `evaluation/`, not `ai-benchmarks/`. The distinction: benchmarks are "things you test with", metrics are "how you measure".

## Safety Pages to security-and-governance/

Pages about AI safety, alignment, model cards, and system cards go to `security-and-governance/`, NOT `evaluation/`. The user explicitly separates safety/security/governance from evaluation methodology.

Pages moved: ai-safety, ai-safety-and-alignment, ai-safety-alignment-rlhf-scalable-oversight-interpretability, ai-safety-military-governance-claude, open-model-safety, model-cards-system-cards.

## ai-benchmarks-and-evals MOC Page

This MOC page lives in `evaluation/` (not in `ai-benchmarks/`). It bridges both directories:
- Part A-D: Links to individual benchmarks in `ai-benchmarks/`
- Part D+: Links to evaluation methodology in `evaluation/`
- Strong navigation pointers to `ai-benchmarks/index` at the top
