---
title: "Webinar Recap: From Data to Vectors to Context"
source: "Pinecone Blog"
url: "https://www.pinecone.io/blog/webinar-recap-data-to-vectors-to-context/"
scraped: "2026-11-10T06:00:25.016554+00:00"
lastmod: "2026-11-06T03:38:30Z"
type: "sitemap"
---

# Webinar Recap: From Data to Vectors to Context

**Source**: [https://www.pinecone.io/blog/webinar-recap-data-to-vectors-to-context/](https://www.pinecone.io/blog/webinar-recap-data-to-vectors-to-context/)

←
Blog
Webinar Recap: From Data to Vectors to Context
What AI Agents Need Beyond RAG
Team Pinecone
Nov 6, 2026
Product
Share:
Jump to section:
What Similarity Can't Tell You
Why Good Recall Still Gives Wrong Answers
Why It Matters More When an Agent Reads the Answer
Where the Deciding Happens
Share:
Subscribe to Pinecone
Get the latest updates via email when they're published:
Get Updates
Ask an agent for projected Q4 mobile growth. It generates SQL, runs it and comes back with +16%. But September 8 was a one-day partner promotion, and the agent counted the spike as demand. Exclude the promotion from the forecast, keep it in reported totals, and the same trend gives +6%. Those are illustrative values. The data was all there and the SQL was valid.
In a webinar on November 4, Jörg Schad, Pinecone's VP of Engineering, traced retrieval from keyword search to RAG, covered what changes once agents consume it, and took questions, including how to make semantic search more accurate. That question usually has its answer outside the search.
This post was adapted from Jörg Schad's webinar
From Data to Vectors to Context
. Here's the full replay:
Watch "
Youtube Video Player
" on YouTube
Watch
What Similarity Can't Tell You
Imagine the two nearest neighbors for a question about a feature are its design doc from three years ago and a scan of the codebase from this morning. Both are similar to the query. Only one describes the code that runs today, and a similarity score can't tell you which.
Each era of retrieval fixed the limit of the one before it. Keyword search runs on an inverted index and ranks with relevance metrics (IDF dates to 1972, BM25 to 1994), which gives exact match at scale. But "cancel" never matches "terminated subscription."
Semantic search closed that gap. With word2vec (2013), HNSW for approximate nearest-neighbor search (2016) and BERT (2018), retrieval finds related meaning across vocabulary. Its limit is the design-doc problem. Similar isn't authoritative.
RAG, from Lewis et al. in 2020, gave models a way to ground answers in a knowledge base at query time, and it has been in nearly every chat demo since. The grounding is unchecked, though. The model gets whatever comes back, with no step that checks whether it is the right result or whether the model used it.
Why Good Recall Still Gives Wrong Answers
Retrieval quality is usually measured as recall at K. Recall@10 is the share of relevant documents that land in the top 10 results. It's a good measure of whether the information is there at all.
Now take a policy that a newer one has superseded. Retrieval returns both versions, and recall counts both as relevant. A plausible answer grounded in the old version scores zero, and Recall@K can look fine anyway. The same goes for a document the caller isn't allowed to see: relevant to the query, and out of bounds for the answer.
So how do you make semantic search more accurate? Often the search is already doing its job. After a merger, one company's fiscal year runs January to December and the other's runs February to January, so the same quarter covers different months on each side. For any question that spans both, semantic search finds every relevant document. It can't say how to combine them.
Tuning the retriever won't help there. No similarity score carries a rule for lining up two fiscal calendars.
Retrieval is scored on Recall@K: did the right documents come back? Context is scored on the decision made with them. Every example so far splits the same way:
Query
What retrieval returns
What decides it
Projected Q4 mobile growth
Complete data, including a September 8 spike
That September 8 was a one-day partner promotion, excluded from the forecast
How does this feature work?
A three-year-old design doc and this morning's code scan
Which source describes the code that runs today
Any figure spanning both companies after a merger
Every relevant document from both
How a January-December fiscal year lines up with a February-January one
What does the policy allow?
The current policy and the version it superseded
Which version is in force
Why It Matters More When an Agent Reads the Answer
A person who sees a forecast far too high, or dropping when it shouldn't, raises an eyebrow and double-checks. An autonomous agent might ship it without that check, and agents call retrieval at volumes no human search ever generated.
A high-volume agent may not notice that results don't make sense or are out of date, and it may not ground the answer on its own. It's missing the context that would tell it.
So why not give the model everything and let it work out what's relevant? Because more input tends to make answers worse.
Chroma's context rot report
evaluated 18 LLMs and found that performance grows less reliable as input length grows, even on deliberately simple tasks. On LongMemEval, focused prompts averaging about 300 tokens beat full prompts averaging around 113,000 tokens. The same holds for agents: load one with information that isn't specific to its task and the outcomes get worse.
The question changes. Whether the right documents came back still matters, but an agent also needs to know what is valid, trusted, permitted and appropriate to use for this task.
Where the Deciding Happens
Search stays. Different tasks need different retrieval tools, and plenty need
more than one
. We put dense vectors, sparse vectors and
full-text search
with BM25 ranking in one index. Keyword search still earns its place wherever exact match matters, and all three are built into the database rather than beside it.
The deciding layer sits on top of search. Each task gets a task context: summaries, entities, policies and rules, plus knowledge artifacts curated in the background before any query arrives. The context resolves which artifacts are relevant to the task, then issues lexical, vector or hybrid queries against the index as it needs them.
Take the merger. Search already found every document. The missing piece is semantic information: how one fiscal calendar maps onto the other, held in the task context next to the policies and rules. The superseded policy works the same way, and so does the databot's one-day promotion. The index supplies the data, and a rule in the context decides how to treat it.
We built
Pinecone Nexus
, our
knowledge engine for agents
, to be that layer. Nexus
curation
keeps a ledger of processed sources, tracked by content hash, so a run only touches what changed. Answers carry
citations
to the file, page and verbatim span behind each claim.
Precedence gets written down, too. A context's
default instructions
act as a system prompt for every query against the context, and they can tell the model how to handle conflicting sources, such as which policy version wins.
We don't think Nexus is the answer for every workload. If your retrieval patterns are simple, you're fairly sure the top 10 results hold the answer, no complex rules or policies decide which source wins, and you're fine owning the grounding, RAG is enough.
Operational data that changes every second, like each purchase on a large online store, probably wants a live, dynamic view. Real-time feeds and records edited in place all day aren't a good fit for Nexus today. It works best where data changes on a slower schedule, such as contracts and research.
Before you spend a sprint on embeddings or reranking, check whether retrieval already found the documents. If it did, the fix belongs to the layer that decides. The
full replay
is on YouTube. To build that layer, start with the
Nexus docs
or
request a trial
.
Share:
Was this article helpful?
Yes
No
Recommended for you
Further Reading
