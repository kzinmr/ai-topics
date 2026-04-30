# Lessons from Building AI Agents for Financial Services

**Source:** https://www.linkedin.com/pulse/lessons-from-building-ai-agents-financial-services-nicolas-bustamante-nhrnc/
**Author:** Nicolas Bustamante (Fintool)
**Date:** 2026-04-30 (ingested)

## Key Insight

In financial services, precision is the product. A single error in a $100M position destroys trust forever. The "moat" is not the LLM, but the infrastructure, data normalization, and domain-specific skills built around it.

---

## 1. Architectural Foundations

### The Sandbox Is Not Optional

Executing arbitrary code is essential for complex tasks (like DCF valuations), but dangerous.
* **The Risk:** LLMs may attempt destructive commands like `rm -rf /` while "cleaning up."
* **The Solution:** Every user gets an isolated environment.
* **Access Control:** Uses AWS ABAC with short-lived credentials. User A physically cannot access User B's data via IAM policies using `${aws:PrincipalTag/S3Prefix}`.
* **Performance:** Sandboxes are "pre-warmed" when a user starts typing to eliminate latency.

### S3-First Architecture

S3 is used as the primary source of truth for user data (watchlists, memories, skills) rather than a traditional database.
* **Workflow:** Writes go to S3 → Lambda triggers sync to PostgreSQL → Reads hit DB for listing, S3 for single-item freshness.
* **Benefits:** 11 9's of durability, free versioning/audit trails, and human-readable YAML/Markdown files for easy debugging.

### Temporal for Reliability

Long-running financial tasks (5+ minutes) are prone to server restarts or network blips.
* **Implementation:** Fintool uses **Temporal** to handle worker crashes and retries automatically.
* **Cancellation:** Uses heartbeats to stop activities across different servers when a user clicks "stop."

---

## 2. Data: Context is the Product

The core challenge is normalizing "adversarial" financial data (SEC filings, transcripts, research) into clean context.

### The Normalization Layer

Everything is converted into three formats:
1. **Markdown:** For narrative content (filings, transcripts).
2. **CSV/Tables:** For structured numerical data.
3. **JSON Metadata:** For searchability (tickers, dates, fiscal periods).

### The Parsing Problem

SEC filings are designed for legal compliance, not machine reading.
* **Challenges:** Tables spanning multiple pages, nested tables, and inconsistent XBRL tags.
* **Fiscal Period Normalization:** "Q1 2024" varies by company (e.g., Apple's Q1 is Oct-Dec). Fintool maintains a fiscal calendar for 10,000+ companies to map references to absolute date ranges.

> "Low-confidence extractions don't enter the agent's context—garbage in, garbage out."

---

## 3. Skills: The New Unit of Value

Fintool moved from elaborate RAG pipelines to **Agentic Search** and **Modular Skills**.

### Markdown-Based Skills

Skills are defined in `.md` files with YAML frontmatter. This allows non-engineers (analysts) to encode financial methodologies without writing code.
* **Shadowing Logic:** Priority follows `private > shared > public`. Users can override default skills by dropping a file in their `/private/` folder.
* **Discovery:** Uses SQL discovery for "lazy loading" to avoid burning tokens by injecting every skill into every prompt.

### Designing for Obsolescence

> "The Model Will Eat Your Scaffolding."

As models improve, complex prompt engineering becomes unnecessary. Fintool designs skills to be easily updated or deleted as the base model's "reasoning" capabilities improve.

---

## 4. Tools and User Experience

### File System & Bash Tools

Agents use `ReadFile`, `WriteFile`, and `Bash` to explore data.
* **Hybrid Approach:** SQL is used for structured queries, while Bash is used to `grep` through filings and verify patterns.
* **Artifacts:** Files created in `/private/artifacts/` become clickable, interactive links in the UI.

### Real-Time Streaming & Interaction

* **Delta Updates:** Instead of sending full states, the system sends operations like `APPEND` or `PATCH` via Redis Streams.
* **AskUserQuestion Tool:** Allows the agent to pause and ask for clarification (e.g., "Should I use consensus estimates or management guidance?") before proceeding with high-stakes calculations.

---

## 5. Evaluation & Monitoring

### Domain-Specific Evals

Generic NLP metrics (BLEU/ROUGE) are useless for finance. Fintool uses **Braintrust** to track ~2,000 test cases:
* **Ticker Disambiguation:** Distinguishing "Apple" (AAPL) from "Appel Petroleum" (APLE).
* **Numeric Precision:** Ensuring "4.2B" isn't just reported as "4.2."
* **Adversarial Grounding:** Injecting fake numbers into context to ensure the model ignores them in favor of official sources.

### Production Observability

* **Auto-filing:** Production errors automatically create GitHub issues with full conversation traces.
* **Model Routing:** Simple queries use cheaper models (Haiku), while complex valuations use top-tier models (Sonnet).

---

## Summary Quote

> "Your moat is not the model. Your moat is everything you build around it... financial data, domain-specific skills, reliable infrastructure, and trust."
