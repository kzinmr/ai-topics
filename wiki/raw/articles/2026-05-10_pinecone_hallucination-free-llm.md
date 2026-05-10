---
title: "Introducing the First Hallucination-Free LLM"
source: "Pinecone Blog"
url: "https://www.pinecone.io/blog/hallucination-free-llm/"
scraped: "2026-05-10T01:27:32.836820+00:00"
lastmod: "2024-06-05T18:55:56Z"
type: "sitemap"
---

# Introducing the First Hallucination-Free LLM

**Source**: [https://www.pinecone.io/blog/hallucination-free-llm/](https://www.pinecone.io/blog/hallucination-free-llm/)

←
Blog
Introducing the First Hallucination-Free LLM
Edo Liberty
Apr 1, 2024
Company
Share:
Jump to section:
The motivation: LLMs hallucinate without access to company data
How it works: Information-free training
Performance: Zero hallucinations... at a cost
Future Research
Share:
Subscribe to Pinecone
Get the latest updates via email when they're published:
Get Updates
While Pinecone is most known for the
vector database
which helps reduce hallucinations through
Retrieval Augmented Generation
, we’re also investing in finding other ways to reduce
hallucinations
. Today, we’re excited to announce a breakthrough in our research: The first-ever LLM that never hallucinates — ever.
It’s called Luna, and we will open-source the model eventually, but for now, due to the far-reaching implications of an AI model that never hallucinates, we’re only sharing the model’s source and weights with vetted institutions.
The motivation: LLMs hallucinate without access to company data
Hallucinations are the predominant reason why most AI applications never reach production. While LLMs answer most questions about public information, they don’t have sufficient knowledge to answer questions that require access to private data. While this is already being addressed with RAG — using a vector database to retrieve and feed relevant context to the LLM — we wondered if there was an even easier way.
Our novel approach targets the root issue causing all other LLMs to hallucinate: They don’t know the limits of their knowledge, so they often fail to admit when they don’t know the answer. And so they make something up. And therein lies the key insight: A model will never hallucinate if it always admits what it does not know.
O Light Eternal, in Thyself contained!
Thou only know Thyself, and in Thyself
Both known and knowing, smile on Thyself!
How it works: Information-free training
The result of many months of research — conducted in a previously undisclosed satellite Pinecone office in Bowling Green, Kentucky — and many millions of dollars spent on GPUs is a 122B-parameter AI model designed to address hallucinations without access to domain-specific knowledge.
The model was developed with a novel technique we call
information-free training
. Just as Alpha-zero made history [1] by becoming the best chess engine in the world merely by playing itself and without knowledge of historical games, our model does the same for factual question-answering tasks. Rather than being trained on public, semi-public, accidentally public, and questionably public data, the model was trained by endlessly asking itself questions and measuring the resulting answer quality. The technique also draws on ideas from Ming-Wei et al.[3] and other work on zero-shot learning.
Our scientists noticed a strong correlation between trying to answer questions factually and hallucination. We define the
assumed knowledge factor
(AKF) as the confidence level set by the model when it forms factual content. High levels of AKF indicate high confidence that factual sentences contain correct information. Low AKF makes the model more unsure about its answers’ factual contents. Note that AKF correlates positively with hallucinations.
IMAGE 1: Rate of hallucinations when training Luna as a function of AKF.
The key insight with training Luna is to consider the other extreme value of AKF. That is, what happens when you set AKF to zero?
IMAGE 2: The low range of the AKF scale, rate of hallucinations when training Luna as a function of AKF.
Amazingly enough, slowly adjusting AKF all the way to zero while training Luna reduced hallucinations to precisely 0%. To our knowledge, this is the first LLM to achieve this feat.
Based on our experiments, the equation above gives the best-performing adjustment schedule for AKF (denoted by Zeta). Here,
t
gives the epoch training index and the values of X are only loosely defined to have some relation to the factualness and correctness of the output. Note that conditional probability over loosely defined variables makes training much more complicated and compute-intensive. We will elaborate on these technical difficulties and consequent solutions in a future technical report.
Performance: Zero hallucinations... at a cost
Luna is not (yet) the best model in the world on all fronts. Achieving zero hallucinations comes at a steep price of significantly diminished performance on other tasks. When reviewing results, we found Luna tends to answer pretty much all questions with some version of “I don’t know.” Therefore, the results are relatively poor on coding (0%) and task completion (0%), as well as usefulness (0%).
While this might diminish the magnitude of the achievements, one must remember that Luna achieved these results without access to any information.
It is not clear whether these results can be improved.
IMAGE 3: Results from HugginFace LLM-Perf Leaderboard [2]. The results clearly show how different models perform on Latency vs Memory.
IMAGE 4: Interacting with Luna, the hallucination-free AI model, in a chatbot.
Future Research
Pinecone is heavily invested in AI research as a whole and knowledgeable AI specifically. We’re deeply committed to advancing the state of the art in this field, and
we’re hiring
.
That said, we will probably halt further research on information-free training. If you want to reliably improve the quality, performance, and commercial viability of your AI applications, you can pair any other LLM of your choice with
the Pinecone vector database
.
References
[1]
Mastering Chess and Shogi by Self-Play with a General Reinforcement Learning Algorithm
[2]
LLM-Perf Leaderboard
[3] Ming-Wei Chang, Lev Ratinov, Dan Roth and Vivek Srikumar:
Importance of Semantic Representation: Dataless Classification
Share:
Was this article helpful?
Yes
No
Recommended for you
Further Reading
