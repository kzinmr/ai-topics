# Poor Man's Continuous Learning

> **Knowledge-based continuous improvement for LLM agents, without model fine-tuning.**

Poor Man's Continuous Learning (PMCL) is a design pattern where an AI agent improves over time by capturing successful outputs, user corrections, and domain knowledge into an external, queryable knowledge base — rather than updating model weights. Every good query becomes future context; every mistake becomes a rule; every clarification becomes shared knowledge.

The term was coined by **Ashpreet Bedi** ([source article](https://www.ashpreetbedi.com/sql-agent)) in the context of Text-to-SQL agents, but the pattern has independently emerged across multiple systems and frameworks in the data-AI ecosystem.

## Motivation

LLM-based agents lack the "tribal knowledge" that human domain experts accumulate over years. Common failure modes include:

- Guessing column/field names based on surface-level semantics
- Missing domain-specific definitions (ARR, churn, LTV, etc.)
- Ignoring business rules encoded in table relationships
- Re-inventing queries that already exist in the organization
- Generating syntactically correct but semantically wrong SQL

Parametric knowledge in LLMs is insufficient for domain-specific query generation. The solution is to externalize organizational knowledge so it can be retrieved at inference time — effectively giving the agent "long-term memory" of how work is done.

## Core Architecture

PMCL splits the system into two paths:

### Online Path (Inference)
The agent retrieves relevant context at query time via hybrid search (semantic + keyword):
- Table schemas and metadata
- Common join keys and relationships
- Metric definitions and business rules
- Past successful queries matching the user's intent
- "Gotchas" and anti-patterns for the domain

### Offline Path (Learning)
When a successful result is produced:
1. User approves the query for memorization (human-in-the-loop)
2. The system extracts the structured knowledge (schema, query, business context)
3. The knowledge base is updated with new entries
4. Optionally, a regression harness validates that new entries don't break existing functionality

## Knowledge Base Design

A well-structured PMCL KB follows three categories:

| Category | Purpose | Examples |
|----------|---------|---------|
| **Table Information** | Ground the agent in the data model | Schemas, column types, column rules (`status` is in `orders.state`), partition keys |
| **Sample Queries** | Prevent re-inventing known patterns | KPI definitions, common aggregations, join patterns |
| **Business Semantics** | Map organizational language to the database | "ARR" → `SUM(revenue) WHERE subscription_type = 'annual'`, "churn" → `COUNT(DISTINCT user_id) WHERE last_active < DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)` |

## Implementations & Related Concepts

### 1. Ashpreet Bedi's SQL Agent (Canonical PMCL)
- **Tech Stack:** FastAPI + PostgreSQL + OpenAI/Anthropic + Docker/Railway
- Structured KB stored as JSON files (table info, sample queries, common queries)
- Hybrid search (question text + entities) for context retrieval
- Human-in-the-loop approval for KB updates
- Source: [Self-Improving Text2Sql Agent](https://www.ashpreetbedi.com/sql-agent)

### 2. BigQuery Conversational Analytics — Golden Queries
Google Cloud BQ's "Golden Queries" feature ([docs](https://docs.cloud.google.com/bigquery/docs/conversational-analytics?hl=ja)) allows data agents to learn organizational business logic from curated, known-good queries:

> "Golden queries teach the data agent business logic for the organization."

A **Data Agent** in BQ Conversational Analytics is configured with:
- Table metadata describing data for specific use cases
- Processing instructions (field name synonyms, important fields, default filters/grouping)
- **Golden queries** that the agent uses as exemplars for generating correct SQL

**Key similarity:** Both treat successful queries as a source of truth for future queries. Golden queries are the BQ-native equivalent of PMCL's "every good query becomes future context."

### 3. Google's Native Semantic Layer (Graph Approach — CIDR '26)
The research paper ["Semantic Data Modeling, Graph Query, and SQL, Together at Last?"](https://medium.com/google-cloud/bigquerys-native-semantic-layer-the-graph-approach-4ba8aa3aa965) proposes a **Semantic Graph Object** with:

- Tables as **nodes**, foreign keys as **edges**
- `ANNOTATION` metadata containing **Golden Query patterns** alongside synonyms, owners, and descriptions
- Agents restricted to traversing explicitly defined edges — preventing "topological hallucinations"
- Standalone, versioned semantic graphs (different departments get different graphs over the same physical data)

> *"The ANNOTATION metadata provides the necessary semantic definitions, telling the agent exactly what the data means before it ever attempts to write a query."*

This is PMCL at the **schema level**: instead of a separate KB, the business knowledge is baked into the database engine's semantic layer.

### 4. dbt Semantic Layer (Ontology-Driven)
The dbt Semantic Layer ([docs](https://docs.getdbt.com/docs/use-dbt-semantic-layer/dbt-sl)) takes a different but complementary approach: instead of teaching the LLM via examples, it pre-defines a **structured ontology** of metrics, dimensions, and entities using MetricFlow:

- The LLM's job is reduced to decomposing a natural language question into the correct combination of metrics and dimensions
- MetricFlow generates the actual SQL **deterministically** — no incorrect joins or bad aggregations
- Trade-off: only answers questions within the scope of what's been modeled

> *"Text-to-SQL is flexible but fragile. The Semantic Layer is constrained but correct."* — [dbt Labs, 2026 Benchmark](https://docs.getdbt.com/blog/semantic-layer-vs-text-to-sql-2026)

The dbt Semantic Layer represents the **most structured form** of the PMCL philosophy — knowledge is so thoroughly codified that the LLM's role is minimized to intent classification.

### 5. LPE-SQL (Continual Learning via Mistake Notebooks, ICLR 2025)
LPE-SQL ([paper](https://arxiv.org/html/2411.13244v1)) formalizes the same intuition as PMCL but with a specific focus on **mistake capture**:

- **Correct Notebook:** Stores successful (question, SQL) pairs
- **Mistake Notebook:** Stores failed attempts with reflection-generated tips
- Both are retrieved at inference time as in-context demonstrations
- Smaller Llama-3.1-70B with LPE-SQL **outperforms** Llama-3.1-405B with standard SoTA methods

This validates the PMCL thesis empirically: a knowledge-augmented smaller model beats a larger one without such augmentation.

## Comparison: PMCL Approaches Spectrum

| Approach | Knowledge Capture Mechanism | LLM Role | Coverage | Correctness Guarantee |
|----------|---------------------------|----------|----------|----------------------|
| **Raw Text-to-SQL** (no KB) | None | Full SQL generation | Unlimited | Low |
| **PMCL SQL Agent** (Bedi) | User-approved successful queries as KB entries | SQL generation + retrieval-augmented | High (grows with use) | Medium (human approval gate) |
| **BQ Golden Queries** | Curated exemplar queries | SQL generation + golden query patterns | scoped to golden queries | Medium-High |
| **LPE-SQL** | Correct + Mistake notebooks | SQL generation + cross-consistency | High (auto-captures) | Medium (reflection-based) |
| **BQ Semantic Graph** | Schema-level annotation + golden queries | Traversal of predefined edges only | Limited to modeled graph | High (topologically constrained) |
| **dbt Semantic Layer** | MetricFlow YAML ontology | Intent decomposition only | Limited to modeled metrics | Very High (deterministic SQL) |

## When to Use PMCL

PMCL is most effective when:

1. **Domain shifts slowly** — Business logic changes infrequently enough that a curated KB stays relevant
2. **Query patterns repeat** — Analysts ask the same KPI questions with different parameters
3. **Correctness matters more than creativity** — You need reliable, auditable SQL, not novel queries
4. **Fine-tuning is impractical** — You're using closed-source models or lack ML infrastructure
5. **Human-in-the-loop is acceptable** — Knowledge capture requires human approval

## When PMCL Is Insufficient

- **Highly dynamic schemas** — Rapidly changing tables make KB maintenance expensive
- **Ad-hoc exploratory queries** — One-off questions unlikely to benefit from historical patterns
- **Complex multi-step reasoning** — KB helps with schema grounding but not with multi-hop logic

## Related Wiki Pages

- [[concepts/semantic-layer]] — The broader category of ontology-driven data access (TODO: create)
- [[concepts/rag-for-sql]] — RAG-based SQL generation patterns
- [[concepts/agent-memory]] — Agent memory architectures (episodic vs semantic vs procedural)
- [[entities/ashpreet-bedi]] — Author of the canonical PMCL article
- [[concepts/grpo]] — GRPO: the "rich man's" continuous learning (model fine-tuning via RL)
