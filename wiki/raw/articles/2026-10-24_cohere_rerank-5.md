---
title: "Cohere Rerank 5 | More Relevant Context for RAG and Agents"
source: "Cohere Blog"
url: "https://cohere.com/blog/rerank-5"
scraped: "2026-10-24T06:00:59.844724+00:00"
lastmod: "2026-10-21"
type: "sitemap"
---

# Cohere Rerank 5 | More Relevant Context for RAG and Agents

**Source**: [https://cohere.com/blog/rerank-5](https://cohere.com/blog/rerank-5)

Key takeaways
State-of-the-art retrieval
: Rerank 5 Pro leads on major public benchmarks, while Rerank 5 Fast delivers near-leading performance at lower cost.
Strong across enterprise domains
: Rerank 5 establishes itself as a leader across finance, healthcare, scientific research, parsed documents and multilingual retrieval.
Context Focus
: new to Rerank 5 - a single Rerank call returns the most relevant passages within each document, cutting LLM token costs with minimal loss in answer quality.
Calibrated relevance scores
: consistent scores across queries and domains let teams set one threshold to decide what reaches the LLM.
Deploy anywhere
: available through the Cohere API, Model Vault, Microsoft Foundry, Amazon SageMaker, privately in your own VPC or on-premises, and to all North users. Get started with just a few lines of code.
Introduction
Today, we're releasing Rerank 5, our most advanced enterprise retrieval models yet, available in Pro and Fast tiers.
Rerank 5
helps teams find the right information, send the most relevant context to their LLMs, and give customers more tailored search experiences. With Rerank 5 Pro, we’ve set a new standard in reranking quality, especially on reasoning-intensive search, visually rich documents, and key enterprise domains. Rerank 5 Fast brings that quality to latency- and cost-sensitive workloads. Both models introduce Context Focus, which pinpoints the most relevant spans of text within documents, going beyond document- or chunk-level retrieval to surface precisely the information that matters.
Every token your LLM reads is a token you pay for, and retrieval decides which tokens those are. As agents run more searches over longer documents, retrieval has become a key lever enterprises have over their AI cost, latency, and answer quality.
Rerank 5 joins
Embed 5
and
Parse 5
as part of our latest generation of search models. It is generally available today on the
Cohere API
and
Model Vault
,
Microsoft Foundry
,
Amazon SageMaker
, and to all
North
users. API pricing is $0.05 per 1M tokens for Pro and $0.02 for Fast.
Performance
Rerank 5 Pro leads public benchmarks such as
ViDoRe V3
,
nanoMTEB
,
BRIGHT
, and
BEIR
- outperforming every competing model tested. Of the 46 composite datasets evaluated, Rerank 5 Pro ranked first on 39 and placed at least second in 43. Models are evaluated using
RCP-nDCG@10
, a Cohere-developed methodology designed to address limitations in traditional nDCG caused by incomplete relevance judgments (qrel coverage).
The advantage is particularly pronounced on BRIGHT, a benchmark testing reasoning-intensive retrieval, where identifying relevant documents requires deeper understanding beyond keyword or semantic similarity. Rerank 5 Pro scores 82.2, outperforming Voyage AI Rerank 3 by 5.8 points and Rerank 4 Pro by 12.4 points, its largest generational gain across the four headline benchmarks. Pro also leads the strongest external competitor by 1.6 points on ViDoRe V3, 1.8 on BEIR, and 3.4 on nanoMTEB. These gains are increasingly important for agentic workflows, where complex, multi-step queries demand the ability to reason about relevance and return evidence that may not closely resemble the original query.
Rerank 5 Fast delivers substantial quality gains in the speed-optimized tier. In all four benchmarks, it outperforms Voyage AI Rerank 3 Lite and Qwen3-Reranker-0.6B, as well as the much larger Qwen3-Reranker-8B and previous-generation Rerank 4 Pro.
Headline benchmarks. Reranking quality (RCP-nDCG@10) on four public benchmarks: ViDoRe V3 (8 datasets), BEIR (13), BRIGHT (12) and nanoMTEB (13). Scores are averaged across each benchmark's datasets.
Domain-specific performance
Across specialized enterprise domains, Rerank 5 demonstrates consistent leadership. In finance and economics, Rerank 5 Pro leads competition on visual retrieval from financial documents (ViDoRe Finance), numerical reasoning over financial reports (
FinQA
), and complex economics questions (BRIGHT Economics). This is where its lead is largest, outperforming Voyage AI Rerank 3 by 9.6 points.
Similar results extend across healthcare, scientific research, and energy-focused retrieval, where benchmarks test the ability to surface relevant information from specialized scientific literature, biomedical research, and climate-related content. See the full list of results
here
.
Reranking quality (RCP-nDCG@10) on finance and economics datasets.
Reranking quality (RCP-nDCG@10) on healthcare and life sciences datasets.
Reranking quality (RCP-nDCG@10) on scientific research datasets.
Reranking quality (RCP-nDCG@10) on energy and sustainability datasets.
Multilingual
Rerank 5 Pro improves on Rerank 4 Pro in every language we evaluated, with gains of at least two points in Spanish, French, German, Arabic and Korean. It ranks first on 14 of the 19 non-English languages in our internal evaluation suite, including all six of the priority business languages shown below.
Against the competition, Pro leads Voyage AI Rerank 3 in every one of these languages. Its widest margins are in Japanese (+2.7), French (+2.3) and Arabic (+2.3). Rerank 5 Fast outperforms Voyage AI Rerank 3 Lite across all six, by as much as 4.5 points in Arabic.
See the full results across all 19 languages here
.
Model
Spanish
French
German
Arabic
Japanese
Korean
Cohere Rerank 5 Pro
91.2
90.5
90.6
89.7
89.4
91.8
Cohere Rerank 5 Fast
88.6
88.6
88.6
86.5
86.8
89.9
Voyage AI Rerank 3
89.4
88.2
89.4
87.4
86.7
89.9
Cohere Rerank 4 Pro
88.6
88.1
88.6
87.5
89.3
89.8
Voyage AI Rerank 3 Lite
86.0
84.7
86.3
82.0
83.8
86.6
Qwen3-Reranker-8B
85.4
84.0
86.2
84.4
85.9
88.0
Qwen3-Reranker-0.6B
76.9
74.2
78.0
74.6
78.6
80.8
Multilingual
.
Reranking quality (RCP-nDCG@10) by language on our internal evaluation suite across six selected languages. The entire suite consists of 20 world languages and 74 datasets.
Parsed PDFs
On retrieval tasks involving content extracted from PDFs, an important capability for enterprise document search, Pro achieves the highest average score of 89.9 in the evaluated suite. This puts it ahead of Voyage AI Rerank 3 (88.4) and Rerank 4 Pro (88.3). Fast follows closely at 88.5, marginally outperforming both models.
Parsed PDFs. Reranking quality (RCP-nDCG@10), averaged across 47 datasets of text parsed from PDFs. Documents were parsed using Gemini 1.5 Flash.
Latency + Throughput
Rerank 5 Fast is built for volume. Under sustained load, Fast reranks about 187 standard-length documents (1,000 tokens) per second on an NVIDIA A100 GPU - delivering 2.9x the throughput of Pro.
Fast also delivers nearly 3x faster response times than Pro, making it ideal for latency-sensitive applications and agents that run many searches per task. Pro remains best suited for applications where ranking quality takes priority over speed.
Document throughput and median request latency for Rerank 5 Fast and Pro on a single NVIDIA A100 Tensor Core GPU via the Cohere API, with 96 documents per request at a concurrency of 8, over 1,000 requests per document length. Document lengths are approximate.
Context Focus: unlock smarter token economics
As documents grow longer and AI agents retrieve information from more sources, the amount of context passed to LLMs continues to increase. Yet, often only a few sentences within each document are relevant to the query. Processing unnecessary content drives up token costs, increases latency and can introduce noise that reduces answer quality.
Context Focus, a new optional capability launching with Rerank 5, goes beyond identifying relevant documents to pinpoint the specific passages that matter most. Configurable thresholds let developers balance context reduction with evidence retention, while a single Rerank API call returns both document-level relevance scores and scored text spans. Applications can then pass only the most relevant evidence to an LLM, without adding steps to the retrieval pipeline.
Decouple context from answer quality
We measured how answer quality varied as Context Focus removes more of the retrieved text across 30 question-answering datasets. Removing half the context sacrificed only 2 percentage points of answer quality (96% retained), and removing three-quarters lost just 7 (87% answer quality retained). Context Focus therefore works like a dial: moderate settings are close to free, and teams that need bigger savings can trade some quality for up to 10x less context.
Answer quality as retrieved text is removed. Each model picks its top 5 documents from the same pool of 50 candidates, then removes text at a range of thresholds (one dot per threshold): Rerank 5 with Context Focus, the baselines with their own compressors. Qwen3.5-9B answers from what remains, and Qwen3.5-35B grades the answer. x-axis: share of retrieved tokens removed; y-axis: average judge score; both averaged over 30 single-turn QA datasets from ViDoRe, UNICORN, BRIGHT-Pro and agentic QA (up to 500 queries each).
We then gave a search agent a retrieval stack built up one step at a time, starting from keyword search (BM25). Adding Rerank 5 Pro raised accuracy from 46% to 49%. Turning on Context Focus then cut tokens and raised accuracy further. At the default threshold (0.1), tokens per task fell by 19% and accuracy rose to 57%. At 0.4, tokens fell by 34%, lower on every dataset, and accuracy reached 58%. Altogether, the full stack with Context Focus at 0.4 used 35% fewer tokens than BM25 alone, at higher accuracy (58% vs 46%). On the six deep-search benchmarks, it used 41% fewer tokens, and accuracy rose from 39% to 52%, with every benchmark improving on both measures. ​
Search-agent results, averaged over 17 datasets including six deep-search benchmarks (BrowseComp-Plus, MedBrowseComp, WebWalkerQA, SealQA, HERB and DRBench), with 50 questions per dataset. We follow the evaluation setup of BrowseComp-Plus. The agent is glm-5-3-flash, with search as its only tool and 5 results per search. Retrieval starts with BM25, and Rerank 5 Pro reorders the top 100 with Context Focus switched off. Context Focus is then shown at the default threshold (0.1) and at 0.4, each applied on top of Rerank 5 Pro. Accuracy is the percentage of questions answered correctly. Tokens are the average total per task, summed over every LLM call in the run: input, output and reasoning tokens. The prompt for each call includes the full conversation so far, and cached tokens are included.
Calibrated relevance scores
With Rerank 5, a score of 0.7 now means a 70% chance the document is useful.
Every reranker returns a relevance score, but until now those scores were mostly good for sorting. What counted as a "good" score changed from model to model. Teams had to tune a cutoff for each model and re-tune it on every upgrade.
Rerank 5's scores are calibrated out of the box: the
relevance_score
returned with each result reads as the probability that the document is useful, with no change to your request or the response format. Pro and Fast also agree on where the line is: "more likely useful than not" is a score of 0.50 for Pro and 0.45 for Fast.
Rerank 5's raw scores read as probabilities. Documents are sorted into ten bins by score, and each line connects a model's bins: the bin's average score (across) against the share of its documents judged useful (up). On the dotted diagonal, a score is exactly a probability; lines below it overstate relevance, and lines above it understate it. Scores are used as returned, with no recalibration. Left: blind human graders, 2,262 documents; useful = a mean grade of "Useful" or higher on a five-point scale (Off-topic, Topical, Useful, Answers, Complete). Right: NIST TREC-DL assessors, 20,646 documents; useful = grade 2 ("highly relevant") or higher on NIST's 0–3 scale.
We checked this against two independent sets of human judgments that no model was trained on: a blind panel of graders and NIST's TREC Deep Learning assessors. On both, Rerank 5 follows the diagonal far more closely than any other reranker. Competing models sit below it, overstating relevance: documents Voyage AI Rerank 3 scored around 0.55 were only 24% useful to the human graders.
The table below sums this up as expected calibration error (ECE): the average gap between a model's scores and the real share of useful documents, where 0 is perfect. Rerank 5's is about 0.06 on both sets of judgments; every other reranker we tested has nearly four times that error or more. Calibration doesn't cost ranking quality, either: Rerank 5 Pro and Fast rank first and second in average precision on both.
Expected Calibration Error
Judge
Model
Humans
NIST
Cohere Rerank 5 Pro
0.058
0.057
Cohere Rerank 5 Fast
0.058
0.058
Cohere Rerank 4 Pro
0.384
0.309
Voyage AI Rerank 3
0.234
0.307
Voyage AI Rerank 3 Lite
0.226
0.325
Expected Calibration Error sums up each line in the charts above: the average distance of its dots from the diagonal, weighted by how many documents each dot represents. In other words, how far a model's scores are from the real share of useful documents. Lower is better; 0 is perfect.
Why it matters
Filter by relevance, not by count.
Instead of passing a fixed top-k to your LLM, keep every document above the threshold. Narrow queries pass a few documents, broad ones pass more, and the model sees less noise.
Know when nothing relevant came back.
If no document clears the threshold, an agent can rewrite the query or say it doesn't know, instead of answering from whatever ranked first.
One threshold across domains and model sizes.
Across BRIGHT, NanoBEIR, and ViDoRe V3, the default stays between 0.47 and 0.53 for Pro, and Pro and Fast are within 0.05 of each other.
Start reranking
Rerank 5 Pro and Rerank 5 Fast are generally available through the
Cohere API
,
Model Vault
, Microsoft Foundry (
Fast
,
Pro
), and Amazon SageMaker (
Fast
,
Pro
), and to all North users. For private deployments in your own VPC or on-premises,
speak to a member of our team
.
Rerank 5 sits on top of the retrieval stack you already have. It works with any keyword, vector or hybrid search, with no re-indexing, and is available through frameworks including LangChain, Haystack, Elasticsearch and Weaviate.
Read the documentation
.
Start by
creating an API key
, then use the code snippets below to quickly make your first query.
#rerank with Context Focus
import
os
import
requests
query =
"How much did card provisions rise in Q3?"
documents = [
"Market update. Commercial real estate prices fell 6% this year as office "
"vacancies climbed. Analysts expect refinancing pressure on landlords to "
"persist into next year."
,
"Q3 credit quality. Net charge-offs held steady at 0.42% of average loans. "
"Commercial real estate loans stood at $14.3 billion, or 9% of total loans. "
"Office properties accounted for $2.1 billion of that balance. Card "
"provisions rose $85 million on higher delinquencies."
,
"Q3 mortgage lending. Residential mortgage originations rose 11% as rates "
"eased. The average loan-to-value ratio on new lending was 68%."
,
]
response = requests.post(
"https://api.cohere.com/v2/rerank"
,
headers={
"Authorization"
:
f"Bearer
{os.environ[
'CO_API_KEY'
]}
"
},
json={
"model"
:
"rerank-v5.0-pro"
,
"query"
: query,
"documents"
: documents,
"top_n"
:
2
,
"relevant_spans"
: {
"mode"
:
"enabled"
,
"threshold"
:
0.4
,
"max_spans"
:
10
},
#toggle Context Focus
},
)
response.raise_for_status()
for
result
in
response.json()[
"results"
]:
document = documents[result[
"index"
]]
print
(
f"
{result[
'relevance_score'
]:
.2
f}
{document[:
60
]}
..."
)
for
span
in
result.get(
"relevant_spans"
)
or
[]:
print
(
f"
{span[
'score'
]:
.2
f}
{document[span[
'start'
]:span[
'end'
]]}
"
)
Last thoughts
Try Rerank 5 inside a full retrieval stack.
Compass Cloud
, our managed search and retrieval platform, brings parsing, embedding, hybrid search and Rerank together in one service, with Cohere managing the infrastructure. It's now in private beta for teams building retrieval-heavy and agentic applications.
Request access
.
Follow us on
X
and
LinkedIn
for the latest from Cohere, and email
search@cohere.com
with any other questions.
Key contributors
Clifton Poth, Fabian Schmidt, Samarth Bhargav, Alekhya Nandula, Yuheng Huang, Arthur Maciejewicz, Dennis Zhao, Timothy Ang, Carlos Lassance, Nils Reimers
Blog
Written By
Cohere Team
Tags
Product Launch
Company News
Enterprise AI
Share
AI isn’t a shortcut.
It’s how business gets ahead.
Contact sales
