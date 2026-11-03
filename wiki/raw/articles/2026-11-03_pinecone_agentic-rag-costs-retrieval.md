---
title: "Agentic RAG Costs: Retrieval Beats Every Other Fix Combined"
source: "Pinecone Blog"
url: "https://www.pinecone.io/blog/agentic-rag-costs-retrieval/"
scraped: "2026-11-03T06:00:51.545614+00:00"
lastmod: "2026-11-02T15:25:24Z"
type: "sitemap"
---

# Agentic RAG Costs: Retrieval Beats Every Other Fix Combined

**Source**: [https://www.pinecone.io/blog/agentic-rag-costs-retrieval/](https://www.pinecone.io/blog/agentic-rag-costs-retrieval/)

←
Blog
Agentic RAG Costs: Retrieval Beats Every Other Fix Combined
Team Pinecone
Feb 19, 2026
Engineering
Events
Share:
Jump to section:
Where the Baseline's Tokens Go
Stage 1: Retrieval
Stage 2: Prompt Caching, Tighter Context, Shorter Answers
Stage 3: Semantic Caching
What the Ladder Leaves Out
Where to Start
Share:
Subscribe to Pinecone
Get the latest updates via email when they're published:
Get Updates
An internal IT support agent answers 20,000 questions a day. Each call sends the model 6,050 tokens and gets 500 back. At $5 per million input tokens and $15 per million output tokens, that's $22,650 a month, and nothing has been optimized yet.
Vamshi Enabothala, Principal AI Architect at Pinecone, priced this agent one fix at a time in a spreadsheet. With the fixes applied in his order, cutting the retrieved context saves $12,600 a month on the token bill, more than every fix after it combined.
Each saving on his ladder is measured on the bill the stage before it left, so later levers work on a smaller bill. His spreadsheet doesn't price the fixes themselves. At the end we price the one with a published rate, reranking, and name the rest.
This post was adapted from Vamshi Enabothala's webinar
From Tokens to Vectors
. Here's the full replay:
Watch "
Youtube Video Player
" on YouTube
Watch
Where the Baseline's Tokens Go
Every call carries four things: a system prompt that tells the model how to behave, context that gives it the facts, the user's question, which is short, and the model's answer, which is billed at three times the input rate.
Component
Tokens per call
Billed as
Monthly cost
System prompt
1,000
input
$3,000
Context
5,000
input
$15,000
Question
50
input
$150
Response
500
output
$4,500
Total
6,550
$22,650
600,000 calls a month at the illustrative rates Vamshi used: $5 per million input tokens, $15 per million output tokens.
The 6,550 total includes the 500-token response, so input per call is 6,050.
Context is 5,000 of those input tokens, about 83%. An agent sends that much when it can't tell which part of a document answers the question, so it sends the whole thing. Vamshi's own example of a complete document ran to 10,000 tokens, so for an agent sending whole documents, this baseline is if anything low.
Agentic loops multiply all of this. One question can take three, five, sometimes ten model calls as the agent retrieves again, calls tools, or checks another knowledge base. Each of those calls is billed for its own input and output. The ladder below prices one call per question.
Stage 1: Retrieval
The first fix sends the model the passages that answer the question instead of the whole document. Documents are split into chunks ahead of time and each chunk is embedded as a vector. At query time the question is embedded too, and its
nearest neighbors
become the context.
In Vamshi's spreadsheet that cuts context from 5,000 tokens to 800. Input per call falls to 1,850, and on the 6,050-token baseline above the monthly bill falls from $22,650 to $10,050. That's a 55.6% cut, worth $12,600.
"The smarter approach is not more context. It's only the right set of context."
A model given a whole document has to process all of it, which slows the response and leaves more room to hallucinate. His observation is that in some cases accuracy is even higher after the cut, because the model sees only the context that answers the question.
Narrow retrieval works better when the index knows what each chunk is. His example is financial filings. A 10-K is filed once a year and a 10-Q each quarter, so an index without the year in its metadata can answer a question about 2024 revenue with chunks from the 2023 or 2025 filing. Those tokens are paid for and wrong.
With the company, the form type, and the year stored as metadata, a
metadata filter
limits the search to records that match.
Hybrid search
adds a keyword signal to the semantic one, so exact strings like product codes still match. Which fields to store comes from trial and adjustment. In Vamshi's words, "It's always an iterational trial."
Stage 2: Prompt Caching, Tighter Context, Shorter Answers
With retrieval narrow, Vamshi's second stage makes three changes to the rest of the stack at once.
Prompt caching.
The system prompt is mostly the same from call to call, and most providers offer caching for it. His spreadsheet treats caching as halving the prompt, 1,000 tokens to 500, and his estimate for prompt-caching savings is 30 to 50%.
Halving is an approximation, because providers bill cached tokens at a discount.
Anthropic's prompt caching docs
, for one, bill cache reads at 0.1 times the base input price and five-minute cache writes at 1.25 times.
Tighter context.
His slides frame this as retrieving the top three chunks instead of the top ten, using hybrid search followed by
reranking
. A small, cheap model deployed locally then summarizes them. (His suggestion is to fine-tune an open model on the domain for that one job.) Context drops from 800 tokens to 300.
Pinecone's
context engineering guide
treats reranking and summarization the same way, as tools for pruning context to cut cost and latency.
Shorter answers.
The prompt asks for a fixed structure and no reasoning in the response, and sets a budget for the output. As Vamshi put it, "LLM always works on the token budget." Responses drop from 500 tokens to 300.
Together these take input per call to 850 and output to 300. The bill drops from $10,050 to $5,250, a saving of $4,800, well under half of what retrieval saved.
Monthly LLM token cost at 600,000 queries a month and $5/$15 per million input/output tokens, baseline input corrected to 6,050 tokens a query.
At baseline, output is 20% of the bill. After retrieval it's 45%. After the stack fixes, output is $2,700 of $5,250.
The first two stages cut input far harder than output: input fell from $18,150 to $2,550, output from $4,500 to $2,700. So the model's own writing now costs as much as everything it reads, at three times the per-token price. That's our reading of his numbers, not a point he made.
Stage 3: Semantic Caching
The last stage stops some questions from reaching the model at all. A semantic cache embeds each incoming question and looks for a stored question close enough in meaning. If it finds one, it returns the stored answer. If not, the model answers and the pair goes into the cache. It's a pattern a team builds and tunes for its own traffic.
The appeal is paraphrase. A user who wants to reset a password and another who forgot their credentials need the same answer, and a traditional cache keyed on exact text treats them as different questions.
Vamshi put the reduction in model usage at around 20 to 60% in production systems when the cache is built well, and assumed the midpoint: 40% of questions served from cache. That leaves 360,000 calls a month reaching the model. The bill drops from $5,250 to $3,150, a saving of $2,100, leaving the bill 86.1% below the baseline.
He called semantic caching one of his favorite techniques, and he was also more cautious about it than about any other lever. Similarity thresholds are hard to choose. In his words, "False positives are biggest nightmare here." A false positive hands a user the stored answer to a different question. A cached answer also goes stale when the document behind it changes, so the cache has to be repopulated.
Unlike the first two stages, a semantic cache skips the model call entirely, on the strength of a similarity score. Its saving is the smallest on the ladder, partly because it works on the smallest bill.
What the Ladder Leaves Out
Vamshi's spreadsheet prices tokens only. The costs in this section are Pinecone's addition to his numbers, not something he said.
Reranking is billed per request. Pinecone's
pricing page
, as of October 2026, lists hosted rerank models such as
bge-reranker-v2-m3
at $2 per 1,000 requests on the Standard and Enterprise plans.
At one rerank request per query, that's about $1,200 a month at 600,000 queries, or about $720 once the cache absorbs 40% of them. That cost sits outside the ladder's token totals; Pinecone
bills reranking
separately.
Reranking alone costs a quarter of the stack fixes' $4,800. Rerankers also
add latency
, which belongs in the same decision.
Stage
Model calls / month
Token cost / month
Saved vs. prior stage
Reranking / month
Baseline
600,000
$22,650
–
–
1. Retrieval
600,000
$10,050
$12,600
–
2. Prompt caching, tighter context, shorter answers
600,000
$5,250
$4,800
about $1,200
3. Semantic caching
360,000
$3,150
$2,100
about $720
Token cost at $5 per million input and $15 per million output tokens. Reranking at $2 per 1,000 requests (Pinecone pricing as of October 2026), billed separately from tokens.
Other costs aren't in the table at all. The summarizer model has to be hosted and called. The semantic cache embeds every question and runs a lookup before anything else happens. Neither has a figure for this workload, so we leave both unpriced.
We haven't priced the index, so retrieval's lead here is a lead in token spend: $12,600 against the $6,900 the later stages save together. The reranker, the summarizer and the cache all sit on the later rungs. Their costs come out of the later stages' savings, which only widens retrieval's lead. The costs that can narrow it sit on the first rung: the index and the query embeddings retrieval runs on.
Where to Start
If you run a support or internal-knowledge agent, start with what goes into the context window: how many chunks reach the model, and which metadata filters keep the wrong ones out. Then price your index and query embeddings against what retrieval saves on your own token bill before you treat it as settled.
Measure your own split between input and output dollars before picking the next lever. Once context is tight, the model's output may be half the bill.
When you turn on prompt caching, keep the system prompt static and check the cached-token count in the model's response. If it stays at zero after the first call, caching isn't firing, and the savings in your spreadsheet aren't real.
Leave the semantic cache for last, and turn it on only with similarity thresholds you've tested on your own traffic.
Share:
Was this article helpful?
Yes
No
Recommended for you
Further Reading
