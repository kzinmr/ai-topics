---
title: "Fine-Tune Your Own Embedding Model from an LLM — for the Price of a Coffee"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/fine-tuning-your-own-embeddings-model"
scraped: "2026-07-31T06:00:03.091961+00:00"
lastmod: "2026-07-30T23:16:36.000Z"
type: "sitemap"
---

# Fine-Tune Your Own Embedding Model from an LLM — for the Price of a Coffee

**Source**: [https://fireworks.ai/blog/fine-tuning-your-own-embeddings-model](https://fireworks.ai/blog/fine-tuning-your-own-embeddings-model)

Kimi K3 on Fireworks: Frontier Intelligence You Can Own
Product
Solutions
Models
Pricing
Resources
Log In
Get Started
Blog
Fine Tuning Your Own Embeddings Model
Fine-Tune Your Own Embedding Model for the Price of a Coffee
PUBLISHED
7/29/2026
Table of Contents
Why Fine-Tune an LLM into an Embedding Model?
How Embedding Fine-Tuning Works: In-Batch Negatives and InfoNCE
Experimental Results
Experiment 1: Legal Citation Retrieval (LegalBench)
Experiment 2: Clinical Trial Matching (TREC Clinical Trials)
Experiment 3: EU Case-Law Citation Retrieval (LegalPincite)
Code Example: Train on Your Private Data
What Else We Found
When Fine-tuning Didn't Move The Needle
Getting Started
Three Fireworks Training Modes: Flexibility vs. Efficiency
Interested in Fireworks Training?
Table of Contents
Explore us in AI tools
ChatGPT
Claude
Grok
Perplexity
CoPilot
Gemini
Table of Contents
Why Fine-Tune an LLM into an Embedding Model?
How Embedding Fine-Tuning Works: In-Batch Negatives and InfoNCE
Experimental Results
Experiment 1: Legal Citation Retrieval (LegalBench)
Experiment 2: Clinical Trial Matching (TREC Clinical Trials)
Experiment 3: EU Case-Law Citation Retrieval (LegalPincite)
Code Example: Train on Your Private Data
What Else We Found
When Fine-tuning Didn't Move The Needle
Getting Started
Three Fireworks Training Modes: Flexibility vs. Efficiency
Interested in Fireworks Training?
Table of Contents
TL;DR
Retrieval-augmented generation (RAG), semantic search, reranking, recommendation, intention classification, deduplication, clustering — an enormous share of production AI boils down to one primitive: turning text into a vector so that related things land close together and unrelated things land far apart.
The quality of that vector space is the ceiling on every system built on top of it. A great reranker cannot rescue a retriever that never surfaced the right document; a RAG pipeline cannot cite a case it failed to retrieve. So the question becomes:
how do you get the best possible embeddings for your domain?
In this post we show a practical, low cost recipe (<$10) for adapting a general-purpose embedding LLM (Qwen3-Embedding-8B) to a specific domain using contrastive fine-tuning on the Fireworks platform — and we measure the result on two hard, real-world retrieval tasks. The short version: a short fine-tune lifts retrieval quality dramatically over the base model (e.g.
+36% nDCG@10
on legal citation retrieval) while keeping the model's general-purpose strengths intact.
Why Fine-Tune an LLM into an Embedding Model?
Text embeddings have been studied for over a decade, going back to
word2vec
and its successors, which first showed that the meaning of text could be captured in a dense vector. Today there are three broad ways to obtain embeddings for a domain — and only one of them is both high-quality and cheap:
Use a base LLM embedding model off the shelf.
Train an embedding model from scratch.
Fine-tune an LLM-based embedding model (this post).
Let's weigh the trade-offs of each.
Option 1 — Use a base embedding model off the shelf.
Modern embedding models derived from LLMs (Qwen3-Embedding, E5-Mistral, NV-Embed, …) are excellent generalists: trained on a vast slice of the internet, they produce strong vectors for everyday text. But "generalist" is exactly the limitation on a specialized corpus. A base model doesn't know that, in U.S. case law, 36 So. 3d 84 and Reed v. State refer to the same authority, or which eligibility criteria make a patient a match for a given clinical trial. It captures general-purpose text well and domain-specific semantics poorly. As we'll show, on a legal citation-retrieval task the base model reaches only
0.43 nDCG@10
— usable, but far below what the corpus allows.
Option 2 — Train an embedding model from scratch.
For much of the past decade, embedding systems for search, recommendation, and advertising were trained from scratch (
DSSM
,
embedding-based retrieval in Facebook search
) — typically a dedicated BERT-style encoder fit to in-domain data, which can work reasonably well. But for most teams this is a trap: with the modest amount of labeled data available, a from-scratch model overfits the training distribution and
loses the broad linguistic competence
that makes embeddings robust. It memorizes your training pairs and then stumbles on the paraphrases, typos, and novel phrasings it meets in production — you discard billions of tokens of pretraining to chase a few thousand labeled pairs. Also, training an embedding model from scratch is generally reserved for AI labs and organizations with the research expertise, large-scale datasets, and compute infrastructure needed to train foundation models. It is typically only justified when existing embedding models cannot adequately represent a highly specialized domain or when there is a need for complete control over the model’s architecture and optimization objectives. For most companies, using or fine-tuning a state-of-the-art embedding model provides comparable performance at a fraction of the cost and complexity. That is precisely the idea behind Option 3.
Option 3 — Fine-tune an LLM-based embedding model (this post).
Start from a strong pretrained embedding LLM (
BERT
,
Don't Stop Pretraining
) and gently adapt it with a contrastive objective on your domain pairs. This is the best of both worlds:
•
You keep the generalization.
The base model already understands language, syntax, entities, and world knowledge. Fine-tuning nudges the geometry of the vector space toward your domain instead of rebuilding it — a few hundred steps specialize the model without catastrophic forgetting.
•
You gain the domain.
The model learns your notion of relevance: that a masked legal paragraph should retrieve the precedent it cites, or that a patient summary should retrieve the trials they qualify for.
•
It's cost effective..
Because you're adapting rather than pretraining, a useful run is ~150 optimizer steps — minutes of trainer time on Fireworks, with either full-parameter updates or a tiny LoRA adapter.
This mirrors the lesson from
turning LLMs into classifiers
: the winning move is to
adapt the model you already have
, reusing the same training and inference infrastructure, rather than bolting on a new architecture or starting from zero.
How Embedding Fine-Tuning Works: In-Batch Negatives and InfoNCE
An embedding model maps a piece of text to a single vector. For an LLM-based encoder like Qwen3-Embedding, we run the text through the transformer and take the
last token's
final hidden state as the embedding (the causal attention mask means the last position has "seen" the entire sequence), then L2-normalize it. Similarity between two texts is just the dot product (cosine similarity) of their vectors.
To teach the model a domain's notion of relevance, we need training data shaped as
(query, positive) pairs
— a query and a document that should be retrieved for it. For our legal task, the query is a court paragraph with its citation masked out, and the positive is the case it cites. For clinical trials, the query is a patient summary and the positive is a trial they're eligible for.
The objective is
contrastive
: pull each query close to its positive, and push it away from everything else. The elegant trick that makes this efficient is
in-batch negatives
. Within a training batch of B (query, positive) pairs, each query already has exactly one correct document — and the other B−1 documents in the same batch serve as free negatives. (It is worth noting that more advanced hard negative mining and cross-batch negatives could further boost the performance; we will leave it for the next post). So far, let's focus on a basic setup using only in-batch negatives.
Concretely, for a batch we compute the full
B × B
similarity matrix
S,
where
S[i][j]
is the cosine similarity between query
i
and document
j
. The diagonal entries are the true positives; every off-diagonal entry is a negative. We then apply the
InfoNCE
loss — a softmax cross-entropy that asks each query to assign the highest similarity to its own positive among all B candidates:
The B×B in-batch-negative similarity matrix: the diagonal holds the true (query, positive) pairs, every other cell is a negative drawn for free from the rest of the batch.
1
2
3
L_q2d = cross_entropy(S / τ, targets = diag)   # each query picks its positive
L_d2q = cross_entropy(Sᵀ / τ, targets = diag)  # each doc picks its query
L     = ½ (L_q2d + L_d2q)                       # bidirectional / symmetric
Two details matter:
•
Temperature τ
(we use 0.02) sharpens the softmax so the model is pushed to make positives clearly win, not just barely win.
•
Bidirectional loss
— we apply InfoNCE in both directions (query→doc and doc→query) and average. This symmetric form trains both sides of the retrieval relationship and is more stable than a one-directional loss.
Experimental Results
We evaluated on two hard, domain-specific retrieval benchmarks, comparing the
base
Qwen3-Embedding-8B against a
fine-tuned
version of the same model. In both cases we trained full-parameter for 150 steps with batch size 64 (batch 8 for the long-context case→case run below, where only 8 16k-token sequences fit), learning rate 1e-5, temperature 0.02 — a recipe that takes only minutes of trainer time. Evaluation is on
held-out queries
the model never saw during training, and all metrics use the standard pytrec_eval library (the same one MTEB uses). To keep the tables readable we report
nDCG@100
(ranking quality) and
Recall@100
(coverage); the other standard metrics — nDCG@10, Recall@10, MRR, MAP@100 — all improved significantly as well.
Experiment 1: Legal Citation Retrieval (LegalBench)
The task: given a legal question, retrieve the court opinions that should be cited in the answer. We built this by joining the legal-bench citation-retrieval questions with the full text of the cited cases from the Caselaw Access Project — 4,899 questions over a 6,061-document corpus of real U.S. court opinions, ~19 relevant cases per query. We split by source case so that evaluation queries come from cases never seen in training. The questions are from
phalanetwork/legal-bench_cat1_cite_retrieval
, and we pair each with the full opinion text of its cited cases from the
Caselaw Access Project
. A (query, positive) pair looks like:
Query:
"In Florida, I'm advising a county clerk's office on managing pro se prisoner petitions after the Pray v. Forman decision. … What specific administrative protocols should we implement to comply with recent court standards?"
Positive (cited opinion):
Pettway v. State, Supreme Court of Florida — "John Everett Pettway, Petitioner, v. State of Florida, Respondent … "
Metric
Base
Fine-tuned
Relative gain
nDCG@100
0.462
0.644
+39%
Recall@100
0.540
0.758
+40%
Fine-tuning lifts retrieval quality substantially —
+39% nDCG@100 and +40% Recall@100
(every other metric improved too: +36% nDCG@10, +43% Recall@10, +17% MRR, +61% MAP@100) — because the base model, strong as it is on general text, had real headroom on the specialized task of matching legal questions to the precedents they rely on. A few minutes of contrastive fine-tuning closed most of that gap.
Experiment 2: Clinical Trial Matching (TREC Clinical Trials)
The task: given a patient case description, retrieve the clinical trials the patient may be potentially eligible for (TREC Clinical Trials, ~63k trial corpus). This is a different domain with a very different structure — long, structured eligibility documents and many relevant trials per patient — which makes it a good test of whether the recipe generalizes beyond legal text. With only ~130 training queries, this is also a deliberately data-scarce setting. Queries are the patient "topics" from the
TREC Clinical Trials track
(2021–2023); the corpus is trial records from
ClinicalTrials.gov
. A (query, positive) pair looks like:
Query (patient):
"Patient is a 45-year-old man with a history of anaplastic astrocytoma of the spine, complicated by severe lower-extremity weakness and urinary retention … on high-dose steroids …"
Positive (eligible trial):
Radiation Therapy With or Without Chemotherapy in Treating Patients With Anaplastic Oligodendroglioma (NCT00002569) — inclusion: histologically proven supratentorial anaplastic oligodendroglioma; age ≥ 18 …
Metric
Base
Fine-tuned
Relative gain
nDCG@100
0.495
0.556
+12%
Recall@100
0.303
0.352
+16%
Even with a tiny training set, a short fine-tune improves every metric, which is exactly what matters for a clinical-trials matching workflow where a clinician wants all plausibly-eligible trials surfaced, not just the single best one.
Experiment 3: EU Case-Law Citation Retrieval (LegalPincite)
A second legal-citation task, this time on European Court of Justice judgments from
theresiavr/legalpincite
. Here the query is a passage of a judgment with one of its citations
masked out
, and the model must retrieve what was cited. The dataset comes in two granularities that tell different stories.
Paragraph → paragraph
— retrieve the cited paragraph from a ~594k-paragraph corpus. Queries and documents are short, so this is evaluated at the standard 512-token context. A (query, positive) pair looks like (the masked-out citation is shown as ___):
Query (citation masked):
"68 In addition, as the General Court noted in ___ of the order under appeal, that reasoning applies with the same force in a situation in which lawyers are employed by an entity connected to the party they represent (judgment of ___ Prezes ___)."
Positive (the cited paragraph):
"25. That reasoning applies with the same force in a situation such as that of the legal advisers in issue in the present dispute, in which the lawyers are employed by an entity connected to the party they represent. …"
Metric
Base
Fine-tuned
Relative gain
nDCG@100
0.548
0.584
+7%
Recall@100
0.833
0.866
+4%
The gain is real but modest: the base model is already strong here (0.55 nDCG@100), because matching a short legal paragraph to the short paragraph it cites is close to general semantic similarity — little headroom. (Other metrics moved similarly: nDCG@10 0.501→0.540, MRR 0.501→0.536, MAP@100 0.446→0.481.)
Case → case
— retrieve the cited case, i.e. a full judgment. A (query, positive) pair — both are entire judgments, shown heavily truncated here:
Query (citation masked, ~37k chars):
"1 By their appeals, PJ and PC seek to set aside the order of the General Court of the European Union of 30 May 2018, ___ (PJ v EUIPO — Erdmann & Rossi), 'the order under appeal', by which the General Court … "
Positive (the cited case, ~23k chars):
"1 By application lodged at the Court Registry on 4 October 1979, Australian Mining & Smelting Europe Limited ('AM & S Europe'), which is based in the United Kingdom, instituted proceedings … " — the landmark AM & S Europe judgment on legal professional privilege.
These documents are long (queries ~8.7k tokens at the median), so the comparison must be done at long context. Evaluating
fairly at a matched 16k-token window
— and training the fine-tune at a 16k window too:
Metric
Base
Fine-tuned
Relative gain
nDCG@100
0.484
0.778
+61%
Recall@100
0.653
0.881
+35%
Here fine-tuning
roughly doubles
ranking quality (nDCG@10 0.40→0.72, MRR 0.62→0.89). The lesson we learned the hard way: a fine-tune trained at a short 512-token window barely beat the base under long-context evaluation — the model has to be trained at the context length it will serve at. Match both windows to your document length and the payoff is large.
Reproducibility.
The numbers above come from the Fireworks production trainer. We also provide a standalone single-GPU reproduction kit (open
sentence-transformers
, full-parameter, same recipe) that lands within ~0.03 nDCG@100 of these results: LegalBench (0.639 vs 0.644 fine-tuned nDCG@100) and LegalPincite paragraph→paragraph (0.601 vs 0.584) exhibit high reproducibility; LegalPincite case→case reaches 0.747 vs 0.778 (the small residual is the standalone trainer vs. the production trainer). Clinical Trials shows a consistent ~0.05 nDCG@100 offset on both base and fine-tuned (0.449→0.510 reproduced vs 0.495→0.556 here) from eval-harness differences, but the same ~+0.06 absolute lift. In short, the fine-tuning gains reproduce on every task with open tooling.
Code Example: Train on Your Private Data
Fine-tuning on your own data takes a JSONL file of (query, positive) pairs and a few lines of SDK code. First, your data:
1
2
{"query": "How do I reverse a list in Python?", "positive": "In Python you can reverse a list in place with list.reverse(), or create a reversed copy with slicing my_list[::-1] or the reversed() built-in."}
{"query": "What is the capital of France?", "positive": "Paris is the capital and most populous city of France, located on the river Seine in the north of the country."}
Each line is one positive pair. For a domain like ours you'd write, e.g.,
{"query": "<legal question>", "positive": "<text of the case to cite>"}
. You don't need to supply negatives — in-batch negatives are generated automatically.
Then run the contrastive fine-tune through the Fireworks Training SDK. The trainer is provisioned for you; the loop streams batches, computes the bidirectional InfoNCE loss, and promotes the final checkpoint to a model you can deploy:
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
import
os
import
training
.
recipes
.
embedding_loop
as
embedding_loop
from
training
.
utils
import
TrainerConfig
config
=
embedding_loop
.
Config
(
log_path
=
"./embedding_logs"
,
# Start from a strong pretrained embedding LLM — do NOT train from scratch.
base_model
=
"accounts/fireworks/models/qwen3-embedding-8b-ft-base"
,
tokenizer_model
=
"Qwen/Qwen3-Embedding-8B"
,
# Your private (query, positive) pairs.
dataset
=
"my_domain_pairs.jsonl"
,
# Contrastive objective: bidirectional InfoNCE over in-batch negatives.
output_mode
=
"embedding"
,
# "contrastive_loss" runs it server-side in one round trip
temperature
=
0.02
,
# sharpen the softmax
batch_size
=
64
,
# 64 -> 63 in-batch negatives per query
learning_rate
=
1e-5
,
epochs
=
3
,
# ~150 steps is plenty for most datasets
# A query-side instruction tailored to YOUR task (Qwen3 convention).
query_instruction
=
"Given a legal question, retrieve court opinions that should be cited in the answer"
,
# lora_rank=32 for a cheap, swappable adapter; 0 = full-parameter.
lora_rank
=
0
,
# Promote the trained checkpoint to a deployable model.
output_model_id
=
"qwen3-embedding-8b-my-domain"
,
trainer
=
TrainerConfig
(
)
,
# infra (GPU/region) resolved by the platform
)
metrics
=
embedding_loop
.
main
(
config
)
print
(
"Final metrics:"
,
metrics
)
Once training finishes, your model serves through the standard embeddings endpoint — same API as the base model, now specialized to your domain:
1
2
3
4
5
6
7
8
9
from
fireworks
.
client
import
Fireworks
client
=
Fireworks
(
api_key
=
os
.
environ
[
"FIREWORKS_API_KEY"
]
)
resp
=
client
.
embeddings
.
create
(
model
=
"accounts/<your-account>/models/qwen3-embedding-8b-my-domain"
,
input
=
[
"In Florida, what authority governs frivolous pro se prisoner petitions?"
]
,
)
query_vec
=
resp
.
data
[
0
]
.
embedding
# L2-normalized; dot product = cosine similarity
Or call the
/v1/embeddings
endpoint directly (the response is OpenAI-compatible):
1
2
3
4
5
6
7
curl -s https://api.fireworks.ai/inference/v1/embeddings \
-H "Authorization: Bearer $FIREWORKS_API_KEY" \
-H "Content-Type: application/json" \
-d '{
"model": "accounts/<your-account>/models/qwen3-embedding-8b-my-domain",
"input": ["In Florida, what authority governs frivolous pro se prisoner petitions?"]
}'
Index your corpus once with the same model, and retrieval is a nearest-neighbor lookup over these vectors.
What Else We Found
Beyond the two headline results, we ran a series of sweeps. The details are out of scope for this post, but the takeaways are worth stating:
•
Fine-tuning's gain tracks the base model's headroom.
Where the base is already strong, gains are small; where it struggles, they are large. We saw the same pattern on three more domains — code search (
CoSQA
), developer Q&A (
StackOverflow-QA
), and e-commerce product search (
Amazon ESCI
): a clear lift on ESCI, a small one on the already-near-ceiling StackOverflow-QA, and essentially flat on CoSQA.
•
~150 steps is the sweet spot.
Training to 300 steps gave no improvement and sometimes slightly regressed top-rank metrics — a short adaptation specializes the geometry without overfitting.
•
LoRA nearly matches full fine-tuning.
A rank-32 LoRA adapter landed within ~1 point of full-parameter fine-tuning on every metric, at a fraction of the cost — a great default for a cheap, swappable domain adapter.
•
Bigger batches didn't help here.
Pushing in-batch negatives from 63 (B=64) to 255 (B=256) gave no gain on these tasks and ran far slower — 64 was already plenty.
•
Context length can matter more than fine-tuning.
On a full-judgment (case-level) variant, a model fine-tuned at a 512-token window barely beat the base under long-context evaluation; training at an 8k–16k window instead
nearly doubled
nDCG and MRR. When documents exceed the encoder's window, truncation — not model quality — is the bottleneck, so train and evaluate at a length that fits your data.
When Fine-tuning Didn't Move The Needle
Not every dataset improved. The clearest non-results came from tasks where the base model was already strong, or where "relevance" is close to plain semantic/lexical similarity:
Dataset
What it asks
Base nDCG@10
Fine-tuned nDCG@10
CoSQA
natural-language query → code snippet
0.439
0.433 (flat)
StackOverflow-QA
question → answer post
0.944
0.967 (already near-ceiling)
FiQA2018
financial question → answer
0.645
0.638 (no gain)
NFCorpus
health question → PubMed doc
0.414
0.419 (negligible)
These non-results fall into two scenarios:
The task isn't actually domain-specialized.
When "relevance" reduces to general semantic or lexical similarity, the base model already handles it and there is no specialized signal to add. CoSQA — matching a natural-language query to the code snippet that answers it — is close to generic semantic search; StackOverflow-QA answer posts are lexically almost identical to their questions (base nDCG@10 0.94, near ceiling). Fine-tuning has nothing to learn.
The benchmark is popular and already saturated by foundation models.
FiQA (finance) and NFCorpus (medical) look domain-specific, but they are widely-used public IR benchmarks whose documents and relevance patterns were almost certainly in the base model's pretraining data. The model has effectively already seen the task, so fine-tuning on a small slice of it adds nothing (FiQA even dipped slightly).
Together these refine the hypothesis:
fine-tuning delivers large gains only when the task carries a specialized relevance signal the base model has not already internalized
— not merely domain-specific vocabulary, and not on public benchmarks that foundation models have already absorbed. The big wins — LegalBench citation retrieval (+36% nDCG@10) and full-judgment case matching (~2×) — came precisely where "relevant" means something the domain defines (which precedent governs the question, which trial a patient qualifies for) and that general pretraining never taught.
Getting Started
If your product relies on search, RAG, reranking, or recommendation over a specialized corpus, the base embedding model is leaving quality on the table — and training from scratch would cost you generalization. Contrastive fine-tuning of an embedding LLM is the cheap middle path that captures your domain's relevance while keeping the model's broad competence.
•
Collect a few thousand
(query, positive)
pairs from your domain.
•
Fine-tune Qwen3-Embedding-8B with the recipe above (~150 steps, minutes of trainer time).
•
Evaluate on held-out queries with nDCG / Recall / MRR before and after.
•
Deploy through the same embeddings API and re-index your corpus.
Three Fireworks Training Modes: Flexibility vs. Efficiency
Now available in preview, Fireworks exposes this contrastive fine-tuning loop in three modes that trade off
flexibility
(how freely you can define the loss) against
training efficiency
(how much data has to move between the client driving the loop and the trainer holding the model). They optimize the same family of objective; they differ in where the loss is computed and what crosses the client↔trainer boundary.
embedding
— most flexible, least efficient. The trainer runs the forward pass and returns the raw embedding vectors, and you compute the loss yourself, client-side, with whatever function you like — InfoNCE, triplet, custom margins, multi-positive schemes, anything. This is the most general option: you are not limited to any built-in objective. The cost is bandwidth. The full embedding matrix (batch × hidden dim — e.g. 4096-d) is sent from the trainer to the client on the forward pass, and the corresponding gradients are sent back on the backward pass. For large batches and the wide hidden states of an 8B model, moving those tensors back and forth dominates step time.
cos_similarity_matrix
— a middle ground. The trainer computes the pairwise cosine-similarity matrix and returns its rows; you still define the loss client-side, but over the much smaller N×N similarity matrix instead of the N×D embeddings. When the batch size N is below the embedding dimension D (the usual case), this transfers far less data than embedding while still letting you customize any loss expressible over similarities — InfoNCE variants, temperature schedules, custom masking. The trade-off: the full matrix has to be assembled on one device, so this mode requires a single-data-parallel (DP=1) trainer.
contrastive_loss
— least flexible, most efficient. The bidirectional InfoNCE loss is computed entirely on the trainer in a single round trip: no embeddings or gradients cross the boundary — the batch goes in, a scalar loss comes back. This is the fastest option and the right default when InfoNCE is what you want, which for retrieval it almost always is. You give up the ability to plug in an arbitrary loss in exchange for minimal communication overhead.
Mode
Loss computed
Crosses the client↔trainer boundary
Flexibility
Efficiency
Constraint
embedding
client
embeddings + gradients (N×D)
any custom loss
lowest
—
cos_similarity_matrix
client
similarity matrix (N×N)
any similarity-based loss
medium
DP=1 (single GPU)
contrastive_loss
trainer
data in, scalar loss out
built-in InfoNCE only
highest
—
Rule of thumb: start with
contrastive_loss
for standard retrieval fine-tuning; reach for
cos_similarity_matrix
when you want a custom similarity-based loss without paying the full embedding-transfer cost; use
embedding
when you need complete freedom over the objective. (The experiments above use the embedding mode.)
Interested in Fireworks Training?
Tell us about your training needs so our forward deployed team can best help you on your journey to specialized intelligence.
Get in touch
Explore us in AI tools
ChatGPT
Claude
Grok
Perplexity
CoPilot
Gemini
Platform
AI Native
Enterprise
Customers
Use Cases
Code Assistance
Conversational AI
Agentic Systems
Search
Multimodal
Enterprise RAG
Developers
Model Library
Docs
CLI
API
Changelog
Pricing
Serverless
On-Demand
Fine Tuning
Enterprise
Partners
Cloud and Infrastructure
Consulting and Services
Technology
Fireworks for Startups
Resources
Blog
Demos
Cookbooks
Company
Leadership
Investors
Careers
Trust Center
© 2026 Fireworks AI, Inc. All rights reserved.
