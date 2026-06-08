---
title: "Tool Use Examples — Semantic Conventions Beyond Schema"
type: concept
created: 2026-06-02
updated: 2026-06-02
tags:
  - tool
  - mcp
  - context-engineering
  - prompting
  - harness-engineering
aliases: [input-examples, tool-semantic-layer, usage-pattern-specification, schema-plus-examples]
related: [concepts/advanced-tool-use, concepts/tool-search-tool, concepts/programmatic-tool-calling, concepts/rlm-recursive-language-models, concepts/code-execution-with-mcp, concepts/dspy-rlm]
sources:
  - raw/articles/2025-11-24_anthropic_advanced-tool-use.md
  - https://www.anthropic.com/engineering/advanced-tool-use
---

# Tool Use Examples — Semantic Conventions Beyond Schema

## Definition

**Tool Use Examples** are concrete usage demonstrations attached to tool definitions that convey **semantic conventions** — format preferences, optional parameter correlations, domain idioms, and usage patterns — that JSON Schema alone cannot express. They represent a generalization of the principle that **structural validity ≠ semantic correctness**.

**Coined by:** Anthropic (Nov 2025) as `input_examples` field in tool definitions.
**Generalized here as:** a pattern applicable to any system where agents must bridge the gap between schema and semantics.

## The Gap: Schema vs. Semantics

JSON Schema defines what's **structurally valid** but not what's **semantically correct**:

| Schema Tells You | Schema Cannot Tell You |
|------------------|------------------------|
| `due_date` is a string | Format: "2024-11-06" vs "Nov 6, 2024" vs ISO 8601? |
| `reporter.id` is a string | Convention: UUID vs "USR-12345" vs "12345"? |
| `escalation.level` is an integer | Correlation: How does it relate to `priority`? |
| `labels` is an array of strings | Convention: kebab-case? When to include? |
| `reporter.contact` is an object | When to populate: critical bugs only? |

This gap is **universal** — it appears wherever a formal interface meets a real-world domain.

## Anthropic's Implementation: `input_examples`

```json
{
  "name": "create_ticket",
  "input_schema": { "properties": { "title": {...}, "priority": {...}, "labels": {...}, ... } },
  "input_examples": [
    {
      "title": "Login page returns 500 error",
      "priority": "critical",
      "labels": ["bug", "authentication", "production"],
      "reporter": {"id": "USR-12345", "name": "Jane Smith", "contact": {"email": "jane@acme.com"}},
      "escalation": {"level": 2, "notify_manager": true, "sla_hours": 4}
    },
    {
      "title": "Add dark mode support",
      "labels": ["feature-request", "ui"],
      "reporter": {"id": "USR-67890", "name": "Alex Chen"}
    },
    {"title": "Update API documentation"}
  ]
}
```

From 3 examples, the model learns:
- **Format conventions**: dates = YYYY-MM-DD, IDs = USR-XXXXX, labels = kebab-case
- **Nested structure patterns**: contact populated only for critical bugs
- **Parameter correlations**: critical → full escalation; feature → no escalation; internal → title only

**Result**: Complex parameter handling accuracy improved from 72% → 90%.

## Generalization: The Semantic Layer Pattern

Tool Use Examples instantiate a broader pattern — **Semantic Layer for Agents** — where usage examples bridge the gap between formal interfaces and domain knowledge. This pattern appears across multiple domains:

### 1. Few-Shot Prompting (General)
The most basic form: providing examples in the system prompt to teach the model how to format outputs, follow conventions, or handle edge cases. Tool Use Examples are few-shot at the **tool level** rather than the **prompt level**.

### 2. Data Analysis Agents (Semantic Layer)
In data analysis, a **semantic layer** maps technical schemas to business concepts:
- Column `revenue_usd` → "Revenue in USD, exclude refunds, include tax"
- Table `orders` → "Customer orders, excludes cancelled, includes pending"
- Metric `churn_rate` → "Monthly churn = (lost customers / start-of-month total) × 100"

Tool Use Examples serve the same function for API tools: they encode **domain knowledge** that the schema cannot.

### 3. RLM Data Sampling (Recursive Language Models)
In [[concepts/rlm-recursive-language-models|RLM]], the first iteration often **samples the data** to understand its structure before building a decomposition plan:

```
Iteration 1: Read first 50 rows → understand schema, formats, distributions
Iteration 2: Build decomposition plan based on observed structure
Iteration 3+: Execute sub-queries with correct conventions
```

This is the same principle applied at runtime: **observe examples before acting**. The model builds an internal "semantic layer" from the data itself.

### 4. DSPy's Signature + Examples
[[concepts/dspy-rlm|DSPy]] uses `Signature` (schema) + `Example` (semantics):
- Signature defines input/output types
- Examples show the model how to fill those types correctly
- Optimization finds the best examples automatically (few-shot optimization)

### 5. Skills/Query Plans in Agentic Search
[[concepts/agentic-search|Agentic Search]] uses "Skills" — vector DB lookups of "how to search for X" — that inject domain-specific search strategies into the prompt. This is semantic layer at the **search orchestration** level.

## The General Pattern: Schema → Examples → Behavior

```
┌─────────────────────────────────────────────────────────┐
│  Formal Interface (Schema)                              │
│  ─ What's structurally valid                            │
│  ─ Types, required fields, enums                        │
├─────────────────────────────────────────────────────────┤
│  Semantic Layer (Examples)                              │
│  ─ What's semantically correct                          │
│  ─ Format conventions, correlations, domain idioms      │
├─────────────────────────────────────────────────────────┤
│  Runtime Behavior (Model Actions)                       │
│  ─ What the model actually does                         │
│  ─ Informed by both schema and semantics                │
└─────────────────────────────────────────────────────────┘
```

| Layer | Source | Provides |
|-------|--------|----------|
| Schema | JSON Schema, TypeScript types | Structural validity |
| Examples | `input_examples`, few-shot, data samples | Semantic conventions |
| Behavior | Model's learned priors + context | Actual execution |

## Best Practices

1. **Focus on ambiguity**: Only add examples where correct usage isn't obvious from schema
2. **Use realistic data**: Real city names, plausible prices, not "string" or "value"
3. **Show variety**: Minimal, partial, and full specification patterns (1-5 examples per tool)
4. **Document correlations**: Show how optional parameters relate to each other
5. **Update with schema**: Examples must evolve as APIs change

## When to Use

| ✅ Use Tool Use Examples | ❌ Skip |
|-------------------------|---------|
| Complex nested structures | Simple single-parameter tools |
| Many optional parameters with patterns | Standard formats (URLs, emails) |
| Domain-specific conventions not in schema | Validation better handled by JSON Schema |
| Similar tools where examples clarify selection | |

## Design Principles

1. **Examples are executable documentation**: They show, not tell, how to use a tool correctly
2. **Semantic layer scales with tool count**: As agents handle more tools, examples become more critical for disambiguation
3. **Progressive enrichment**: Schema → examples → runtime samples → learned conventions
4. **Examples are bidirectional**: They teach the model AND document the API for humans

## Related Concepts

- [[concepts/advanced-tool-use]] — Anthropic's framework (Search + PTC + Examples)
- [[concepts/tool-search-tool]] — Progressive disclosure layer for tool discovery
- [[concepts/programmatic-tool-calling]] — Code-based tool execution
- [[concepts/rlm-recursive-language-models]] — RLM's data sampling in first iteration is the runtime analogue
- [[concepts/dspy-rlm]] — DSPy's Signature + Example pattern
- [[concepts/agentic-search]] — Skills/Query Plans as search-level semantic layer
- [[concepts/code-execution-with-mcp]] — Filesystem-based progressive disclosure
