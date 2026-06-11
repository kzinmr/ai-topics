---
title: Doug Turnbull - Speaking & Community
type: entity-sub
parent: doug-turnbull
created: 2026-04-10
updated: 2026-06-05
tags:
  - person
  - writing
  - community
  - methodology
sources:
  - https://www.youtube.com/watch?v=OGnW2Pu2uVE
  - https://www.youtube.com/watch?v=UXQ916WRK0A
  - https://www.youtube.com/watch?v=h370222tnAQ
  - https://www.youtube.com/watch?v=Jd2_7sVXUxA
  - https://www.youtube.com/watch?v=AJPH9kpN3Sc
---

# Doug Turnbull: Speaking & Community

## Conference Talks

Turnbull is a regular speaker at search industry conferences:

- **\\\\\\\"Lexical Search & BM25\\\\\\\" — Cheat at Search Essentials** (May 2026, Maven course): Live training course on the fundamentals of lexical search. Covers tokenization (whitespace → intelligent tokenizers with stemming/synonyms/entities), query processing (AND/OR matching, Elasticsearch DSLs), scoring evolution (TF → TF\\*IDF → BM25), multi-field search (naive sum vs. DisMax), BM25 parameters (k1 saturation, b length bias), and BM25F for combining fields. Key insight: \\\"BM25 ≈ Relevance Given Match\\\" — and agents handle the semantics when matching fails. Course discount code: `bm25rocks`. Uses [[entities/jxmo|searcharray]] educational library. [[raw/articles/2026-05-13_softwaredoug_lexical-search-bm25]]

- **\\\\\\\"Vector Search & Embedding Retrieval\\\\\\\" — Cheat at Search Essentials** (May 2026, Maven course): Day 3 of the Maven course. Covers embeddings primer (triples training, dot product/cosine similarity, sigmoid + contrastive loss, backpropagation), Two-Tower architecture for cold-start (user/movie encoders → dot product), transformer sentence embeddings (BERT CLS token, Q&A retrieval), vector search algorithms (k-means clustering, HNSW hierarchical graphs, ScANN/DiskANN clusters+graphs), filtered similarity (pre-/post-/native filtering, ACORN1), embedding pitfalls (hubness/collapse, compression loss, Similarity ≠ Relevance), and hybrid search strategy (multiple retrieval arms, LLM as orchestrator). Key insight: \"Split by strategy, not by index type — BM25 + vector as tools for agents.\" Discount code: `vectorsrock`. [[raw/articles/2026-05-13_softwaredoug_vector-search-embeddings]]

- **\\\\\\\\\\\\\\\"How To Build Your First Agentic Search Application\\\\\\\\\\\\\\\"** (Feb 2026, Vanishing Gradients podcast): 35-minute interview covering the practical implementation side of agentic search. [[raw/articles/2026-02-20_doug-turnbull-build-first-agentic-search-app]] [[transcripts/2026-02-20_doug-turnbull-build-first-agentic-search-app]]
  - **Passive vs. Active search spectrum**: Passive = user types query, gets results, no iteration. Proactive = user manually vets results (e.g., spreadsheet of 100 job postings). Active (agentic) = agent automates the proactive loop — iterating, evaluating relevance, reformulating queries until done
  - **Three essential agent components**: (1) Tools — simple, transparent APIs (BM25, grep) the agent can reason about, (2) Reasoning — LLM reflects on results and decides next action, (3) Reformulation — agent rewrites queries based on what it learned from previous results
  - **Two-loop harness architecture**: Inner loop = agent iterates through tool calls. Outer harness loop = validates agent output against quality criteria. LLM-as-a-Judge scores each result; if below threshold, passes feedback back to agent ("Result X has low Y, keep trying")
  - **Simple tools win**: BM25's transparency lets agents understand *why* results are returned. Complex search APIs with hidden synonym expansion, query rewriting, reranking confuse agents. Grep is a "happy path" agents learned during training — they naturally navigate file systems
  - **Build-vs-buy advice**: Pydantic AI good for structured outputs and tool definitions. Hand-rolling recommended for teams that know their domain intimately. Decision factor: team comfort and domain complexity, not theoretical purity
  - **Future directions**: Long-running agents (persist across hours/days), memory/compaction (compression of reasoning history to fit context windows), Recursive LMs (agent calling itself recursively for deeper search tasks)

- **\"Rag is the What. Agentic search is the How.\"** (April 2026): 54-minute talk tracking the paradigm shift from classical RAG to agentic search — arguing that complexity moves from retrieval to the agent+harness, and that \"dumb retrievers\" (BM25, grep) work best with agent reasoning. [[raw/articles/2026-04-22_doug-turnbull-rag-is-the-what-agentic-search-is-the-how]] [[transcripts/2026-04-22_doug-turnbull-rag-is-the-what-agentic-search-is-the-how]]
  - **RAG unwound**: RAG evolved into a \"thicc daddy\" search system — query understanding on ingress, different retrieval strategies, combine + rerank, aggregate stats, append to LLM context. Exactly what we've built for decades. Now agents replace the entire search stack using simple tools
  - **Four-stage evolution**: (1) Structured Attributes — LLMs do query understanding via schema, (2) Tool Calling — agents intentionally search rather than being force-fed context, (3) Agent Reasoning — agents reflect on results and course-correct, (4) Dumb Retrievers — complexity moves to the harness, agents get by with BM25/grep
  - **Why dumb retrievers work**: When agents can reason about search results, they understand exactly how results are produced, iteratively refine queries across multiple rounds, reflect on relevance and retry with different strategies. The LLM itself handles semantic understanding — no need for sophisticated embedding-based reranking
  - **Design principle**: Don't start RAG today assuming you need the classic embedding+chunking paradigm. Focus on tools that deliver needed context. \"The dumbest thing that can work, with simplest.\"
  - Explicitly connects to [[concepts/agentic-search]] three levels (IR, Harness, Externalized Processing), [[concepts/sid-1|SID-1]], semantic grep, and scaffold+tool design
  > \"Don't waste too much time on the original RAG paradigm. AI has moved on.\"
  > \"A big thicc daddy search system. We're unwinding that now.\"
  > \"Why chunk and embed when an LLM knows all about the 'semantics' of your query?\"
  > \"I wouldn't start RAG today assuming you need the classic RAG embedding+chunking paradigm.\"

- **\"Why 2026 is The Year of Agentic Search\"** (May 2026, YouTube): 65-minute fireside chat with Jo Kristian Bergum (Vespa.ai / Hornet) on the four pillars of agentic search. [[raw/articles/2026-05-01_doug-turnbull-2026-is-the-year-of-agentic-search]] [[transcripts/2026-05-01_doug-turnbull-2026-is-the-year-of-agentic-search]]
  - **Agent as the new user**: Bergum's definition — agentic search is when the agent decides the query formulation. "It's not me typing the query, it's the agent that is typing the query into the search box." The agent is the new user, and search engines need to be designed with agents in mind
  - **Agents search differently**: BrowserComp+ analysis reveals agents issue ~25 search calls per session (vs. 1.5–2.5 for humans), queries average 23 terms (vs. 2 in AOL logs), agents discover phrase queries and `site:` syntax unprompted, and they exhibit patience to exhaustively explore cause-and-effect relationships humans lack
  - **Token efficiency spectrum**: Grep-like tools give agents poor token efficiency (dumps irrelevant context) but strong cause-and-effect reasoning. Dense retrievers give 5 results but agents can't reason about why those results came back. The sweet spot is a middle path — harness around search that gives feedback without polluting context
  - **LLM Query Understanding at scale**: LLMs classify intent as structured attributes (color, material, category, price range), not semantic vectors. 80% of search relevance work could be automated; the remaining 20% (domain-specific, high-performance) requires human expertise
  - **Cascade effect in agentic search**: One bad search result can cascade — the agent goes down a wrong reasoning path. But agents also have self-correction capability: "Well, that didn't work. Let me try a different approach." The impact of bad search is amplified, but so is the recovery
  > "The search problems of 2026 are agentic search problems."
  > "80% of what people are doing with search relevance today could almost be done automatically." — Jo Kristian Bergum
  > "The whole search industry veterans are so biased about having to make it super fast and only doing single queries, but there are so many use cases where you can just let the agent rip through." — Jo Kristian Bergum

- **"AutoReSEARCH — Ranking Coded by Agents"** (May 2026, HaystackConf): 47-minute conference talk on using coding agents to iteratively optimize search ranking code. [[raw/articles/2026-05-14_softwaredoug_autoresearch-ranking-coded-by-agents-haystackconf]] [[transcripts/2026-05-14_softwaredoug_autoresearch-ranking-coded-by-agents-haystackconf]]
  - **Dependency injection pattern**: Instead of agent-in-the-loop at query time, inject BM25/vector/categorization primitives as LEGO pieces. The agent assembles ranking functions offline, then deployed code runs in production without any agent. Advantage over traditional LTR: no new inference service needed
  - **Three guardrails against overfitting**: (1) LLM-based overfit detection — ask a mini model "Does this code look overfit? Does it contain query-specific product terms?", (2) Patch size limits — 10 lines, 120 chars wide, forces tactical thinking and prevents query-specific memorization, (3) Train/validation/holdout splits — training gets full per-query NDCG feedback, validation only sees aggregate improvement ≥0.003, holdout is completely hidden
  - **AutoReSEARCH IS machine learning**: Feature engineering → choosing primitives; Data splits → train/validation/holdout; Regularization → patch size limits; Model training → code generation loop; Overfitting → query-specific memorization. The agent's code edits are functionally gradient updates
  - **Focused composition**: Don't give the agent all tools at once. First round: optimize retrieval (BM25 + embeddings) → produces optimized reciprocal rank fusion code. Second round: hide first round behind a single `search` tool, add query rewriting. Each round focuses on one dimension
  - **MS Marco BM25 experiment**: Agent discovered bigram-based BM25 — adding stop words back and weighting by bigram term frequency. Novel approach, but didn't generalize from mini-Marco to full dataset. LLMs default to well-known patterns (RRF) from training data
  > "Deep learning is a universal function approximator — it's really just linear algebra being optimized. AutoReSEARCH is just a different sort of putty being optimized, but in the same sort of harness."
  > "When we're doing this AI coding, the way to think about it is this AI auto-research really is machine learning. We still need to take our eval data, have good splits, and control the visibility of that data to the model."
  > "If we made a tactical couple of lines changed and saw which queries improved or got worse, it's easier to reason about why that might have happened."


- **\\\"LLM Query Understanding — Cheat at Search\\\"** (May 2026, guest lecture): Practical code-level guide to using LLMs for query understanding in e-commerce search. Covers embedding collapse (hubness), why structured QU beats pure embeddings for narrow domains, synonym extraction with Pydantic+BM25 boosting, deep multi-label category classification (10K+ labels) with dynamic Pydantic enums for cost optimization, and caching strategies. Demonstrates 12% NDCG improvement (0.541 → 0.608) on Wayfair queries with gpt-4.1-nano. Key insight: \"BM25 narrows the label space, enabling cheap LLM classification, which then boosts BM25 scores\" — a virtuous cycle. Complemented by [[concepts/query-understanding]] concept page enrichment. [[raw/articles/2026-05-20_softwaredoug_llm-query-understanding-cheat-at-search]]

- **\"Long Running Search Agents — Cheat at Search\"** (June 2026, guest lecture): Progressive strategies for search agents that run unattended for hours/days/weeks. Covers 7 strategies: single context, cron job (fresh restarts), context compaction, local index/memory, frontier prompt (guided exploration), non-agentic query model, and agent self-querying. Key empirical finding: local index yields 3.7x improvement over naive restart patterns (2.68 vs 0.72 yield/call). Introduces two-loop design separating exploration planning from execution. Colab notebook available. [[concepts/long-running-search-agents]] [[raw/articles/2026-06-02_softwaredoug_long-running-search-agents]]

- **\"Agents That Code Their Own Search — RLMs & Ranker Coding\" — Search with Agents Lesson 6** (June 2026, guest lecture): Two-part lecture. Part 1 applies [[concepts/rlm-recursive-language-models|RLM (Recursive Language Models)]] to search — using a Python REPL as the agent's sole tool, with stateful variables (`historical_results`), external search functions (`patent_search`), and recursive `llm_query()` calls. Demonstrates expert-finding from patent literature where the agent batches queries, rates inventors programmatically, and delegates judgment to sub-LLMs. Part 2 introduces [[concepts/agent-driven-ranker-optimization|Agent-Driven Ranker Optimization]] — a coding agent iteratively patches a `rerank_wands()` function using structured `Edit` objects, evaluates against NDCG on train/test splits, and is constrained by guardrails (overfitting detection, length limits, post-change holdout validation). Key insight: "AI coding IS model development" — the agent's code edits are functionally gradient updates requiring the same train/test discipline. Without guardrails, the agent overfits immediately (holdout NDCG plateaus); with guardrails, it improves from 0.5605 to 0.5753 over 10 iterations. Ends with the question: "Could we RLM this? Let the search code call a language model!?" [[raw/articles/2026-06-04_softwaredoug_search-with-agents-lesson6-rlms]]

- **\\"Steering Lost Agents — Cheat at Search\\"** (May 2026, guest lecture): Part 3 of the Cheat at Search series — 65-slide deep dive into agentic design patterns for search. Covers the two-loop architecture (agentic loop + harness control plane), carrot-and-stick steering model, seven steering patterns (Ralph loop, rule-based validation, LLM-as-Judge, reranker-in-response, few-shot priming, tool guards, subagent delegation), filesystem-like search tools (`ls_wands`/`grep_wands`/`cat_wands`), and BEAM search for systematic exhaustive exploration. Empirical results on WANDS dataset: BM25 0.5408 → FS Tools 0.5565 → +Few-Shot 0.5652 → +Delegation 0.5661. Key insight: \"The agent picks the tools, you control how the tools respond — tool responses ARE prompt engineering.\" Complemented by new [[concepts/harness-engineering/agent-steering]] concept page and [[concepts/agentic-search]] enrichment. Colab notebook available. [[raw/articles/2026-05-27_softwaredoug_cheat-at-search-steering-lost-agents]]

- **\"Will Agents Replace Search Teams? (a discussion)\"** (Jan 2026, YouTube): 55-minute discussion with Daniel Tunkelang (Endeca co-founder) exploring the boundary between what agents can and cannot replace in search teams. [[raw/articles/2026-01-29_doug-turnbull_will-agents-replace-search-teams]] [[transcripts/2026-01-29_doug-turnbull_will-agents-replace-search-teams]]
  - **Latency-feedback tradeoff**: Tunkelang's core concern — search's killer feature is speed of feedback. Traditional search gives instant results → user refines → iterate. Agentic search introduces 15-minute delays; if the agent misunderstood, that's 15 wasted minutes
  - **Domain-specific LLM assumptions**: Auto parts case study — LLM assumed searching for a part number means wanting that part, but salespeople were checking commissions. 20% gap in domain assumptions requires query performance prediction and domain-specific evaluation datasets
  - **Economic disruption**: If agents (not humans) consume search results, the ad-based model breaks. EXA charges for agent-accessible web indexes; Reddit monetizes content access; Stack Overflow traffic declines as LLMs return answers directly
  - **Stakes-based error models**: Low stakes (playing a song) → just do it; Medium (researching) → show evidence; High (sending email to wrong person) → confirm before acting
  - **When agents excel vs. don't**: Good for complex research (real estate, expert sourcing), federated search, background candidate collection. Bad for impulse buying, commodity search, exploratory browsing where the user doesn't know what they want until they see it
  > "The best case for agentic search is very much what would happen if I were to outsource my search needs to a human agent." — Daniel Tunkelang
  > "The LLM will make assumptions about the user domain. 80% of the time it's aligned, but 20% of the time it reveals your assumptions about the domain that you didn't even know you had." — Doug Turnbull
  > "I haven't seen any of them replaced by agents. Right?" — Daniel Tunkelang

- **Berlin Buzzwords / Haystack EU** (2024): "Learning to Rank for Reddit Search: A Project Retro" with Charles Njoroge

- **Elastic{ON}16** (2016): "The Ghost in the Search Machine"
- **MICES 2024** (Mix Camp E-Commerce): "Planning of E-Commerce Relevance Work"
- **Relevance Cornucopia** workshops: Intensive small-group training on "Think Like a Relevance Engineer" and "Hello LTR"

He maintains an active blog at softwaredoug.com with regular "daily search tips" — concise, practical observations about search engineering — and a newsletter with thousands of subscribers.

## Key Quotes

> "Agents put the Resilient in RAG."

> "Grug-brained evals: Big brain spend months building perfect quality metrics. Grug brain no trust, and just want dumb labels from coworkers 👍/👎."

> "The tests are the code now."

"> "Content understanding IS query understanding."

> "Embedding collapse is real. In your tiny domain, everything looks similar. Structured query understanding fixes this."

> "All search is structured now — there's no excuse for unstructured search queries in the age of LLMs."

> "If you have discipline to throw away your first idea, draft, throwaway code — you can move faster than any design doc."

> "Start with Who, not Why. Work with amazing people you love collaborating with, the rest falls out."

> "RAG isn't a vector search problem. Through market forces, embeddings became the singular framework we understood RAG. It's the wrong lens."

> "Agents turn simple keyword search into compelling search experiences. Thick APIs hide the reasoning from the agent."

> "Semantic search needs three pillars: representation, similarity, AND match criteria. Embeddings fail at the third."

> "The agent picks the tools, you control how the tools respond. Tool responses ARE prompt engineering."

> "Don't waste too much time on the original RAG paradigm. AI has moved on."

> "The LLM will make assumptions about the user domain. 80% of the time it's aligned, but 20% of the time it reveals your assumptions about the domain that you didn't even know you had."

> "80% of what people are doing with search relevance today could almost be done automatically." — Jo Kristian Bergum

> "The biggest danger I see in the technology of search getting too easy is that we're masking the importance of critical thinking." — Daniel Tunkelang

## Related

- [[entities/doug-turnbull]] — Main entity page
