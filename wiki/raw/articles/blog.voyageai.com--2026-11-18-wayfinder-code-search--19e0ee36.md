---
title: "Wayfinder: Frontier-level Code Search at a Fraction of the Cost"
url: "https://blog.voyageai.com/2026/11/18/wayfinder-code-search/"
fetched_at: 2026-11-19T10:01:33.116234+00:00
source: "Voyage AI Blog"
tags: [blog, raw]
---

# Wayfinder: Frontier-level Code Search at a Fraction of the Cost

Source: https://blog.voyageai.com/2026/11/18/wayfinder-code-search/

Author
:
Henry Weller
Before a coding agent can fix a bug, it has to find the code that matters. The coding agent industry has generally embraced grep as the way agents search code, but repeated searches with grep can become slow and expensive as codebases grow. For customers building coding agents, we wanted to explore a practical question: can indexing codebases for search ahead of time significantly reduce retrieval cost while still helping agents complete the task? Given that AI coding tool budgets are not infinite at most enterprises, we saw this as a useful research question to provide effective and efficient coding tools to the broadest set of users.
To test that idea, we built Wayfinder, an open-source research project combining a small model fine-tuned for tool use and search tasks with a hybrid search (semantic and BM25) index synced to a codebase. Wayfinder is not a MongoDB product. We’re sharing the model, code, and findings so developers can evaluate the approach in their own agents.
TL;DR
Indexed search helps smaller models approach frontier quality at lower cost:
Adding a hybrid search index raised the share of relevant files found using a 35B open model from 65%–69% to 74%, for roughly $0.01 per search. Frontier Sonnet-class models found 76%–78% at $0.07–$0.12 per search.
Promising results for end-to-end coding tasks:
We observed that open models retrieving files for a parent coding agent achieved a similar task completion rate to frontier searchers.
When grep alone stops working
Frontier models are quite good at code search, and they have been trained to use the same tools engineers use, namely filesystem tools such as grep and cat. For a single repository, this is often all you need. However, the cost increases significantly as codebases grow and agents run more searches.
We ran a short experiment with an off-the-shelf agentic search model,
Agents-A1 35B
, to see how search performance changes as the codebase grows. We created 421 search tasks from real Git commits; each question described the purpose of a change without naming the affected files, and the files modified by the commit are treated as the golden set of files to be searched for.
We tested the model with and without a hybrid search index, expanding the search space from one repository to multiple repositories totaling 205 million lines of code. We measured rollout precision: the share of retrieved files that belonged to the correct answer set known ahead of time.
Figure 1: Search time and rollout precision against codebase size for Agents-A1 35B
As the codebase grew (Figure 1), grep got slower and less accurate, with search time rising from 0.3 seconds per task at 240k lines of code (LOC) to 51 seconds per task at 205M (LOC), and recall falling from 0.39 to 0.14. An index cut total wall time at 205 million LOC from 110 to 67 seconds at only slightly improved recall, indicating that many grep loops ultimately were able to catch up to the performance of the index.
This haystack experiment was the first hint that there was an opportunity to improve efficiency. It shows that grep gets worse as code grows, but not how large the recall gain from retrieval is in general when using an index, or whether the efficiency gains are significant broadly. Measuring that requires assessing more coding tasks across more models, codebase types, and generally considering a broader set of ablations.
Training a small model for better code search
We built a training pipeline that yielded a fine-tuned model,
wayfinder-qwen-35B-a3b
(or wayfinder-qwen for short), which outperforms Agents-A1 35B and frontier search models in terms of effectiveness and efficiency.
This pipeline has three attractive features:
Scalable:
We were able to produce a large set of labeled code search tasks using the same method mentioned in the haystack test. These labeled code search tasks are also useful in producing agentic code search traces using more capable models
Adaptable:
We can fine-tune new open models in the 35B param range in under $300 using the 1300+ agentic search traces we collected for frontier search quality
Steerable:
We can use a markdown retrieval spec to yield even more retrieval gains when using this model as a plugin within popular code harnesses.
Figure 2:
From code commits to a fine-tuned code-search model
We call the combined model and harness “Wayfinder,” and using it we can understand not only the gains in the model layer, but in the harness itself.
The retrieval spec essentially defines the following cascading retrieval pattern:
Initial search (run in parallel)
Broad grep: A ~30B agentic search model performs an initial grep and reports a ranked list of files
Hybrid search: The harness runs vector search against chunked and embedded code files using
treesitter
and
voyage-code-4
and hybridized with a BM25 index. The hybrid search is weighted 80% towards semantic search and 20% towards BM25 search.
Merge + rerank:
Results from 1a and 1b are merged and reranked using
rerank-3
Follow-up greps:
The model finally performs subsequent grep based on results from 2, following the conventional agentic search loop
Similar to a method for secure codebase indexing from
Cursor
, the hybrid index stores hashes and embeddings on an object-storage based vector database, never raw code. Files are split on function and class boundaries on the developer’s machine using treesitter and embedded, and the original text is never indexed to the server.
A new pareto frontier for code search
Using 200 held-out coding tasks, we were able to assess search performance under a number of conditions.
We test search with two kinds of queries:
Commit-subject queries:
A commit-subject query is the one-line subject of the original fix, about 50 characters, such as “fix timeout when retrying uploads” (see the left side of Figure 3). It is short, easy to reproduce, and cheap to run, so it is our main benchmark.
Long brief queries:
Coding harnesses rarely send a search subagent a query resembling 1. The parent model usually writes a few sentences describing the problem and what it needs found. To approximate this, we also ran every task with a long brief: a 120 to 165 word description of the problem (see the right side of Figure 3) and the types of things that need to be searched for based on the commit message.
Figure 3: Example commit-brief and long brief queries
We found that for both commit-subject queries and long brief queries, the recall@12 for our model and Agents-A1 35B using the cascading retriever approached frontier-level search and end-to-end coding performance for a significant fraction of the cost (Figure 4). We also found that long brief queries lead to finding the right file much more often, which is another hint at the importance of the right prompting within the harness itself.
Figure 4: Recall and cost per search for commit-subject and long-brief queries
We tested three approaches to better understand where the gains come from:
Sonnet and GPT search with grep, providing a baseline for a frontier model using standard filesystem tools.
We tested two open models, off-the-shelf Agents-A1 35B and our fine-tuned Wayfinder, with and without the cascading retriever, separating the benefit of model training from the benefit of indexed results. We also estimated the benefit of pooling two Wayfinder searches: merging their file lists, giving extra weight to files found by both, and selecting the top 12. This can surface files either run missed, but uses twice the tokens.
For completeness, we tested indexed search without an agentic model, combining semantic matching, keyword search and reranking to see how much retrieval can achieve on its own in the traditional “RAG” setting.
Figure 5: Share of the right files found against cost per search. Higher and to the left is better.
Our experiments show that the index makes agentic search both more effective and more affordable. On their own, Agents-A1-35B and wayfinder-qwen find 65% and 69% of the right files using grep and file reads. Index-based search alone finds 61% for a tenth of a cent, but combining the two approaches brings both models to about 74% for roughly a cent per search. That puts them within two percentage points of Sonnet 5.5 high effort (76%, $0.12) and four of GPT-6.1 Sol medium effort (78%, $0.07).
Interestingly, we observe that the index and grep are complementary: the model with grep finds files the hybrid search index misses, adding 12 to 13 points, while the index adds five to nine points over the model alone. Pooling two wayfinder-qwen runs closes the remaining gap with GPT-6.1 Sol, reaching 78% for about $0.02 per search.
To test whether those search results support working code, we held the coder and task setup fixed and changed only the search method. Across 42 tasks, adding search raises the pass rate from 14% to between 51% and 61%.
Figure 6: Connecting search performance with end to end coding performance
Correlating end-to-end coding task completion with search performance is a secondary goal of evaluating which search method is most effective, but can directionally tell us whether the model is reward hacking when searching for certain file types that are not useful to the end result.
Figure 7: End-to-end pass rate by searcher using Opus 5.5 as the parent coding agent providing the search subagent with long-brief queries
As shown in Figure 7, we find that the overall performance is essentially indistinguishable amongst the most competitive methods, with index-based methods having a slight edge. wayfinder-qwen achieves 55%, alongside Sonnet 5.5 high effort and GPT-6.1 Sol medium effort at 57%; pooling reaches 61%, though this sample is too small to establish a clear lead.
The practical result is that an open model paired with an index approaches frontier search quality at a fraction of the search cost, while supporting a similar rate of completed coding tasks in this test.
Conclusion
Grep remains a useful tool, but our results show the value of pairing it with indexed search. Adding semantic and keyword retrieval helped both open models find more of the right files, approaching frontier search quality for roughly a cent per search. In a smaller coding evaluation, those results also supported task completion rates similar to frontier searchers, though the sample was too small to establish a clear winner.
For customers building coding agents, this suggests a practical way to reduce search costs: combine a smaller model with an index that helps it find relevant code. The savings matter most when agents search frequently, spreading the cost of building and maintaining the index across many tasks. Search is only part of the total coding bill, but it is a part developers can make more efficient.
Again, Wayfinder is an open-source research project, not a MongoDB product. We’re sharing the
model weights
,
training data
and
harness
so developers can test this approach on their own codebases. If you’re building a coding agent, explore the project and evaluate what indexed retrieval adds to your search workflow.
Appendix
Dataset detail
The methodology for producing the code search dataset was generally defined in the blog post, and some more details on their shape are described below.
Figure A1: Share of each set’s tasks by language, in percent.
Training data
Value
Examples
1,383 (1,350 teacher, 33 Agents-A1-35B)
Tasks and repositories
344 tasks in 153 repositories
Size
41.6M tokens, of which 7.0M are the assistant’s own
Examples that use the index tool
77%
Training run
LoRA fine-tune of Qwen3.6-35B-A3B, 2 epochs, 4 H200 GPUs, 88 minutes, about $28
The full trajectories are available here:
https://huggingface.co/datasets/hweller1/wayfinder-training-data
Off-policy distillation
Wayfinder’s search behavior comes from a large teacher model. We ran the teacher, Muse Spark Open (816B parameters), through the same search loop on training tasks, 5,683 rollouts in all, and kept the ones that worked. A rollout survived only if it found every right file, read the evidence for each, stayed within the 75th-percentile number of turns, and fit in 49k tokens. That left 1,350 examples, and we added 33 all-right-file rollouts from Agents-A1 35B, for 1,383 examples across 344 tasks in 153 repositories (Figure A2). The fine-tune is a LoRA run of 88 minutes on four H200 GPUs, costing about $28.
Figure A2: Teacher rollouts kept at each filter, from 5,683 to 1,383 training examples.
Inference cost is not total cost
A search that costs $0.017 does not include building the index. Embedding the median repository (53 MB, about 8,800 chunks, 2.6M tokens) costs about $0.31 once, and keeping it in sync and stored costs about $0.16 a month on the prototype’s vector database, most of it re-embedding and sync writes. Across a large haystack, embedding costs about $1.70 to $1.90 per million lines of code. A default Sonnet search costs about $0.11 and a Wayfinder search about $0.017, so an index pays for itself in cost after about two searches per repository per month. That arithmetic favors repositories that agents search often and punishes those that are indexed and never searched.
