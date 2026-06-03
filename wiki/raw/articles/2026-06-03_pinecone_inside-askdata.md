---
title: "Inside AskData: How We Slashed Token Consumption by Over 90%"
source: "Pinecone Blog"
url: "https://www.pinecone.io/blog/inside-askdata/"
scraped: "2026-06-03T06:00:33.815341+00:00"
lastmod: "2026-06-02T14:24:21Z"
type: "sitemap"
---

# Inside AskData: How We Slashed Token Consumption by Over 90%

**Source**: [https://www.pinecone.io/blog/inside-askdata/](https://www.pinecone.io/blog/inside-askdata/)

←
Blog
Inside AskData: How We Slashed Token Consumption by Over 90%
Simon Lu
Jun 2, 2026
Engineering
Share:
Jump to section:
The Last Mile is a Knowledge Problem
V0 — Throw it into Claude/Cursor, See what happens
AskData V1: Building the Knowledge Layer
Where V1 hit its limits
What Nexus had to be
The migration
What the Numbers Actually Mean
Deletions are What Matter
Build your own
Share:
Subscribe to Pinecone
Get the latest updates via email when they're published:
Get Updates
Data underwrites how products evolve and how companies make decisions. But pulling answers out of a data warehouse, quickly, correctly, with the right business context baked in, is still harder than it should be.
As Pinecone grew into a multi-product, multi-channel business, static dashboards stopped being enough. The questions that actually drive decisions, about pipeline health, retention risk, product adoption, revenue mix, rarely fit neatly into a pre-built view. Analysts became the bottleneck. Ad-hoc questions went unasked. Decisions got made on stale numbers or gut feel.
To close that gap, we built AskData: an in-house AI data agent that explores and reasons over our warehouse, informed by the accumulated knowledge of how our business actually operates. That knowledge is scattered across Slack threads, call transcripts, CRM records, billing systems, and internal documents. Surfacing all of it alongside structured warehouse data is what makes the difference between a query runner and an agent people actually trust.
In May 2026, we rebuilt AskData on top of
Pinecone Nexus
. Token usage dropped by over 92%. Query turns dropped by 78%.
This is the story of how we got there.
The Last Mile is a Knowledge Problem
Pinecone's data stack is a pretty standard setup. Events land in BigQuery.
dbt
transforms them. Mart tables feed dashboards on top.
The pipelines work. The dashboards work. The gap is the last mile; translating questions phrased in business vocabulary into the right table, right column, the right filter and the right caveat. And do it at scale.
That is a knowledge problem, not a data problem.
The data lives in the warehouse. The meaning of data lives somewhere else. Which view is canonical for ARR? Which metric has how much lag? Which accounts to filter out? When the definition changed last quarter. None of that is discoverable from schema inspection.
For analysts working in the warehouse every day, this is another normal day. For everyone else, the cost of self-service is high enough that most ad-hoc questions never get asked at all. Decisions get made on stale dashboards or gut feel. Analysts become the bottleneck for every cross-functional question.
That's the gap AskData had to close.
V0 — Throw it into Claude/Cursor, See what happens
The obvious starting point was to wire a set of tools to BigQuery, dbt and a few internal docs and hand them directly to local coding agents like Claude or Cursor. Many internal users tried this in late 2025.
The agent loop itself was not the problem. Given enough business context fed by hand in each session, the coding agent could read SQL, reason about transformation, and replicate metric definitions well enough. The problem was everything else.
Same question, different answers.
Two people asking the same question would walk away with different SQL, different filters and different numbers. When an agent is reporting critical business metrics meant to drive decisions and align mental models is inconsistent, decisions stop. We needed one canonical answer to “what does ARR mean” and a way for a correction caught by one person to reach the next person immediately. We needed a centralized knowledge management and agent harness that can achieve consistency and reproducibility.
No shared learning.
The questions users ask range from "what's last month's revenue" to "explain why this account is at risk and what to do about it." Those questions require very different levels of reasoning and intelligence. Figuring out which model tier fits which kind of questions is challenging work you want to do once, for everyone.
No feedback loop.
Without centralized tooling, there was no eval to run regressions against, no production observability and no signal about which questions were tripping up the agent.
Orientation tax on every session
. Each fresh session starts cold. Schemas alone do not carry business meaning, so the agent has to blind-traverse the unstructured context (dbt code, Slack threads, analyst notes, query history) from scratch on every question, burning tokens orienting before it can answer.
AskData V1: Building the Knowledge Layer
The agent loop wasn't the hard part. The hard part was the layer above the SQL, the one that holds what the SQL formulas and numbers actually mean for the business.
A traditional 'semantic layer' holds schema and metric definitions, typically manually maintained descriptions of structured data which slowly drift out of sync with your business. What we needed was a knowledge layer that holds the unstructured context (Slack, Gong, dbt comments, docs) that explains why a metric is defined the way it is, and
when
that definition last changed.
That knowledge layer had to bridge the vocabulary gap between how people ask questions and how SQL expresses logic. Raw dbt SQL didn't work. SQL encodes transformations, not meaning. The question "how many monthly active orgs do we have" embeds as a vector that has almost nothing in common with a
count(distinct …)
expression over an
is_active
flag.
Across business questions like "
how is our ARR trending
" or "
did our service have any outages this month
," LLM-summarized markdown describing the relevant warehouse table scored at least 2X higher cosine similarity to the question than the raw SQL that defines or queries the same table. Same data, different vocabulary. Embedding models alone couldn't close the gap.
So we started writing the knowledge articles. A few high-quality hand-written markdown files at first, then scripts that used LLMs to generate more from dbt models and query logs, then a Curator agent whose only job was to investigate gaps and propose edits. By the time V1 stabilized, the KB was 234 markdown files (18,000 lines) served by
Pinecone Assistant
. Five additional retrieval surfaces (Slack threads, Gong calls, historical SQL, dbt source) ran on
Pinecone vector indexes with integrated inference
. Hosted embedding and reranking meant no embedding pipeline to manage, and the retrieval substrate was Pinecone end-to-end. The five ETL pipelines feeding it hadn't been tuned beyond "it runs daily."
V1 launched in #ask-data. Three months in:
Stat
Value
Questions answered
3,690
Slack channels with active threads
40
Follow-up runs (chained conversations)
~49%
Avg SQL queries per run
2.2
Questions per day (May 11)
191
The surprise wasn't volume. It was the
49% follow-up rate
. People were having conversations with the data: adjusting scope, drilling into a result, comparing cohorts. The bar for asking dropped, and the long tail of small questions started showing up. This is the gap BI tools have spent years trying to close with drill-downs and other ad-hoc explore primitives.
A 24/7 data analytics agent that gets the basics right reshapes how a company decides.
Where V1 hit its limits
The retrieval substrate was Pinecone end-to-end, but the agent's view of it was anything but unified.
By the time V1 stabilized, the system had grown to:
22 tools across two agents (DataAgent + Curator).
6 dedicated retrieval surfaces (Pinecone Assistant + three Pinecone indexes + dbt file reads + historical SQL search).
1,300 lines of Airflow code syncing Slack, Gong, and BigQuery logs into Pinecone every day.
2,200 lines of Curator code maintaining 18,000 lines of hand-curated markdown across 234 files.
A system prompt that grew with the agent, explaining when to use
search_kb
versus
search_slack
versus
search_query_logs
versus
grep_dbt
, how to dedupe across them, how to handle dbt's
ref()
macros that don't match a literal grep.
Each backend brought its own client, schema, embedding strategy, retry logic, and ETL pipeline. The Curator existed because the KB couldn't maintain itself. There was no layer underneath that compiled the parts into something coherent; cross-source synthesis happened at query time, by the agent, on every question.
That cost showed up in the token traces. A multi-part question ("what was the total pipeline amount, opportunity count, and weighted pipeline for opportunities qualified in January") took 9 steps and around 240,000 tokens. The agent fanned out across KB searches, dumped a 292-column schema JSON into context, re-searched twice to find the right date column, ran a
DISTINCT
query just to learn the vocabulary, and finally got SQL right on its 4th attempt. 7 of those 9 steps were spent orienting (which table, which column, which filter) before the actual analysis could begin.
A compiler doesn't re-parse its source on every run. Without a knowledge layer underneath, agent infrastructure was doing exactly that.
That's what Nexus had to fix.
What Nexus had to be
Pinecone Nexus was being designed in parallel with V1, and AskData was the workload it had to support first.. A few asks coming directly from V1's pain stuck:
One curation pipeline, many sources.
A single managed system that takes structured, semi-structured, and unstructured inputs from every source, and produces task-specific views and artifacts the agent can leverage in one call. For AskData that meant natural-language-to-SQL semantics: which table, which column, which pattern. Not five ETL pipelines, not five retrieval surfaces. One.
Adaptive knowledge representation.
The artifact's schema and representation shouldn't require human design upfront. It should evolve organically based on the task at hand, driven by the eval signal and source data, not by a fixed ontology or hand-authored template.
Human-in-the-loop knowledge updates.
The Curator agent's actual job (investigate a gap, propose an edit, get it reviewed) had to survive into Nexus, not as a separate agent but as a first-class feedback mechanism.
Nexus shipped against those requirements. The architecture and primitives (Context Compiler, KnowQL, and the rest) are their own story; for that, see the
Nexus deep dive
.
The migration
The migration started with defining the eval, since we needed clear retrieval outcomes for Nexus's build loop. V1 had no clean contract; the agent just drove the context expansion from six tools and stitched them together itself.
We built the eval from V1 production traces. Each question had a full call log: which tools the agent fired, what each tool returned, which chunks the agent ultimately used to write SQL. For each question, we extracted the minimum context payload that would have let the agent get the SQL right on the first attempt. Those payloads became the expected outputs in the eval. The eval set was the target Nexus's build loop optimized toward.
Sample Eval Question:
{
    "id": "difficulty_hard_minimum_fee_revenue",
    "input": "I need comprehensive context to write a correct BigQuery SQL query for: analyzing how much minimum fee revenue came from enterprise vs standard plan customers in a given month.\nReturn ALL relevant information as structured markdown:\n1. **Tables**: Which tables to use (full names like analytics.table_name)\n2. **Key Columns**: Every column needed with its role\n3. **Methodology**: Calculation logic with SQL snippets\n4. **Anti-patterns**: Common mistakes with wrong vs. right examples\n5. **Exclusions/Filters**: Required WHERE clauses\nBe exhaustive. Include SQL code blocks. This context directly determines SQL correctness.",
    "expected_output": "Must mention revenue columns that distinguish minimum fee or platform fee, plan or tier-based segmentation, and dim_orgs as source table to use. Must mention column platform_minimum_fee_1d. Must mention revenue data latency as a caveat. Must mention minimum fee is not final until month end.",
    "match_type": "llm_judge"
}
The plan was straightforward: stand up two Nexus Contexts serving different retrieval goals: one for the semantic layer (schemas + dbt source + SQL patterns), one for customer context (Slack threads + Gong call transcripts).
Replace the six retrieval tools with two:
search_semantic_layer
and
search_customer_context
. Delete the Curator agent and replace its KB-amendment function with a single
semantic_layer_feedback
tool that submits corrections back to Nexus for knowledge amendments. Re-point the ETL to feed sources into Nexus Contexts with minimal prep and transformation, instead of one dedicated custom pipeline per legacy Pinecone index.
Three weeks later, V2 hit full parity with V1 on our regression set:
68.3% on both
. The set is 101 questions across 14 business domains, weighted toward the hard, context-heavy cases we use to benchmark AskData internally. The point of the migration wasn't to lift accuracy. The goal was matching accuracy on a fraction of the budget, and validating Nexus as the substrate underneath: fewer tokens, less code, much shorter path to standing up a system like this in the first place.
We also measured a third baseline: a fresh Claude Code session pointed at the dbt repo and given the bq CLI. No KB, no Nexus, no AskData tooling.
On 20 questions stratified across our 14 domains, it matched V1/V2's accuracy (68.3%). It just paid for it: ~625K average input tokens per question (~16× V2), 21 turns (~4.6× V2), $0.35 per question (~5× V2 with caching normalized). The orientation tax is real. Even a capable coding agent can find the right answer; rebuilding context from raw SQL on every question is what costs.
Metric
V0 (Claude Code raw)
`
V1
V2
V0 → V2
Avg input tokens per question
~625,287
64,008
39,595
-93.7%
Avg turns per question
~21
4.5
4.6
-78%
Avg cost per question
$0.35
$0.20
$0.07
-80.2%
What the Numbers Actually Mean
The per-step view is where the change is structural, not incremental.
In V1, the first LLM call after retrieval averaged about 10,000 input tokens with a wide p25–p90 spread. Every question got a differently-sized pile of concatenated retrieval chunks. In V2, the same call averaged 6,000 tokens with a much tighter spread. Every question had the same focused context. By step 3, V1 was sitting at 21,000 tokens against V2's 10,500. That compounding is the 38% input-token drop.
Output tokens went up by 22%. The agent wrote more SQL per run (1.8 queries on average versus 1.3 in V1) because it had the context to write SQL immediately, instead of burning budget orienting.
Simple lookup
: a daily-revenue ranking question. V1 burned 74,000 tokens over 4 steps: three parallel retrievals injected 10,000 tokens of raw KB, a
get_schema
call returned a 478-column JSON, context climbed past 30,000 tokens before SQL ran. V2 burned 11,000 tokens over 3 steps:
search_semantic_layer
returned a 1,200-token brief naming the exact column, the date column, the filter to exclude internal orgs, an anti-pattern warning about the trailing-window variant, and an example query. No
get_schema
needed. Seven times less budget for the same answer.
Multi-step pipeline question
: the pipeline question from earlier. V1: 240,000 tokens, 9 steps, 4 SQL attempts spent discovering the data model. V2: 35,000 tokens, 5 steps, 2 SQL attempts. Nexus named the right mart table directly in step 0, gave the weighted-pipeline formula, and provided the correct stage filter. One SQL failed on a typo, the agent fixed it.
Unstructured context awareness
: One class of questions has no SQL-only answer: "why is this account's usage dropping?" While a schema-based semantic layer would get the query right, the real explanation lives in unstructured sources.
search_customer_context
surfaces a support thread and a Gong call showing the account is mid-migration from pods to serverless and the actual usage drop is healthy and expected.
The structured number alone says anomaly but the unstructured sources contextualize the meaning to the business.
Deletions are What Matter
The Curator agent (2,194 lines, 9 tools, its own system prompt) is gone. The 234 hand-curated KB files became Nexus curation artifacts. The KB-generation scripts were replaced by Nexus's build process. The Airflow ETL was repurposed to feed Nexus Contexts instead of legacy Pinecone indexes. Across three repos, 25,000 lines went away. The agent itself got smaller; tool count dropped from 22 to 10.
A few things we took away:
Compile once, read many.
Moving synthesis from query time to compile time produced the 38% input-token drop. Nexus spends ~8,000 tokens once to give the agent a brief that saves it ~24,000 downstream. Roughly three-to-one.
Fewer tools, better agents.
Every exposed tool is a branch in the agent's decision tree. Six tools collapsing to two cut the input-token spread by ~4×. Fewer choices, better choices, more SQL per run.
Curation has to be iterative, with the agent in the loop.
A single-pass build can't match months of human refinement. Incremental curation + agent-driven feedback give Nexus the same quality ratchet the KB had.
Structured data tells you what but unstructured data tells you
why
.
The warehouse gives you the number but the business rationale behind it (e.g. why a metric dropped, how ARR is actually defined) lives in unstructured sources. AskData's accuracy came from treating those unstructured sources as first-class inputs to create the knowledge layer for data.
V1 proved a competent internal data agent is feasible and changes how a company decides. V2 proved that with a managed knowledge layer underneath, building and maintaining that agent stops being a months-long bespoke project. Same accuracy, a third of the tokens, simplified code.
Build your own
We published a demo so you can try this yourself.
nexus-analyst-demo
is a stripped-down version of the agent, with two agents in one repo:
agent-nexus/
is the Nexus version. One retrieval tool (
nexus_query
). The agent asks a natural-language question against a Nexus Context and gets back a compiled brief.
agent-classic/
is the baseline. Three retrieval tools (
search_schema
,
search_docs
,
search_notebooks
) over a plain Pinecone vector index, with manual chunking and per-source filtering. Roughly the shape AskData had before the migration.
Otherwise the two agents are identical: same loop, same SQL executor, same chart and file tools, same Gemini inference. The only difference is the retrieval substrate.
The companion repo,
nexus-analyst-demo-ingest
, is the data side. Shows how we prepared Nexus for the knowledge layer. It builds the Nexus Context from a fictional SaaS company Acme: structured warehouse data alongside unstructured organizational knowledge (Slack threads, Gong-style transcripts, runbooks, postmortems). Two scripts sit side-by-side:
upload_to_nexus.py
builds the Nexus Context end-to-end (sources + an eval set + a
build.md
), and
index_pinecone.py
chunks the same sources into a plain Pinecone index for the classic agent. Both pipelines, one repo. The Nexus side is under 1,000 lines of glue. There's no per-source ETL to tune, no chunking strategy to optimize, no embedding model to pick. You hand Nexus the sources, an eval set, and a build spec; the Context Compiler does the rest.
An eval set of 30 hard multi-part questions (sentinel-value gotchas, schema drift, cross-source joins across Acme's warehouse) runs against both agents and surfaces the gap directly.
Live at
https://nexus-analyst-web.vercel.app/
if you want to try it before standing it up yourself. Pick a question, watch the baseline agent stitch together multiple searches and re-derive context on every call, while the Nexus agent does it in one.
If you want to build something like this for your own internal systems,
sign up for Pinecone Nexus early access
.
Share:
Was this article helpful?
Yes
No
Recommended for you
Further Reading
