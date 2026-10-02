---
title: "RCP-nDCG@10: A New Approach to Enterprise Retrieval Quality"
source: "Cohere Blog"
url: "https://cohere.com/blog/rcp-ndcg"
scraped: "2026-10-02T06:00:13.285811+00:00"
lastmod: "2026-09-30"
type: "sitemap"
---

# RCP-nDCG@10: A New Approach to Enterprise Retrieval Quality

**Source**: [https://cohere.com/blog/rcp-ndcg](https://cohere.com/blog/rcp-ndcg)

How well does nDCG capture the quality of modern retrieval systems?
nDCG is the established yardstick for measuring how well search systems rank results, and is widely used across benchmarks such as
MTEB
and
BEIR
. It is preferred because it reflects both relevance and position, giving more weight to useful results that appear near the top. However, it relies on pre-existing relevance labels, which, if incomplete, mean other relevant results can be missed or scored incorrectly.
To address this, we are introducing Rubric-Calibrated Preferences nDCG@10 (RCP-nDCG@10), an evaluation methodology that grades each retrieved document against the same explicit relevance criteria for every query, using a calibrated AI judge. Designed to better reflect real-world enterprise retrieval quality, RCP-nDCG@10 is the metric against which we have optimized our next generation search models. Here, we explain how it works, what's different from the status quo, and how we validated it against human judgment.
nDCG is only as good as its labels
In enterprise search, model performance is typically compared using a portfolio of established offline retrieval metrics. The most common are Recall@k, Mean Reciprocal Rank (MRR), and Normalized Discounted Cumulative Gain (nDCG@k). Each captures a different aspect of retrieval quality.
Recall@10 measures
how much
relevant material appears within the top ten results. It is useful when missing information is costly, but it pays no attention to ordering: a relevant result at position one is the same as one at position ten. MRR, by contrast, measures how high the
first relevant result
appears, but ignores everything that follows. It is therefore most useful when a single correct result is enough, such as FAQ search or simple question answering.
nDCG became widely adopted because it improved on simpler metrics by accounting for both degree of relevance and ranking position. More relevant documents contribute more to the score, and those near the top are weighted more heavily. Over time, this made nDCG a standard across search benchmarks and leaderboards.
Because each metric rewards something different, the three can reach different verdicts on the same results (Figure 1).
Figure 1.
But nDCG does not judge relevance itself. It compares a model’s results against an existing set of relevance judgments, or
qrels
, typically created by human assessors reviewing a subset of documents surfaced by earlier retrieval systems. Exhaustively judging a much broader candidate set of query-document pairs would be prohibitively expensive, so this pooling approach is a reasonable practical compromise — and one that is widely called upon by the industry today.
Figure 2 shows this on a real query from
ViDoRe v3
, asking for the color code used to mark nitrogen tanks. The answer key grades only two documents, and only one of them appears in the system's top five. The document at rank 3 quotes the answer directly, but because it was never judged, it is not considered relevant. The resulting nDCG@5 of 0.760 reflects just one of the five results.
Figure 2.
The trade-off is a growing coverage gap: a newer model may retrieve a genuinely relevant document that was never included in the original judgment pool, yet conventional nDCG will not recognize it. As retrieval systems become more capable and explore parts of a corpus that earlier systems did not, benchmarks can increasingly reflect just what previous generations of systems were able to find.
In our own 46-person human annotation study, these results were borne out:
Qrels are only modestly better than chance at predicting blind human relevance judgments
. As a predictor of a human-assigned grade, the qrel achieves an AUC — a measure of how well a score separates two classes, e.g., relevant vs irrelevant — of just 0.65. As we explore below, this shoots to 0.91 using the LLM's calibrated relevance score.
Missed relevance is the largest source of error
. Among documents labeled irrelevant by the benchmark, 28% are judged useful by humans. The reverse error is much less common: only 15% of documents labeled relevant fail even the basic test of topicality.
Sparse labeling is the driver
. The benchmark labels only 29% of these documents as relevant, whereas human evaluators suggest 60%.
Relevance judgments are subjective
. Pairs of reviewers independently grading the same document reached exact agreement on a 0-4 scale just 42% of the time. Other studies that re-annotated a standard benchmark have reported inter-annotator agreement as low as 17% [1]. The practical consequence is a ceiling: once models reach the limits of what the labels can express, the benchmark appears to stop being able to tell them apart.
The TL;DR: nDCG remains useful, but the reliability of qrels as a ground truth signal is limited because they substantially understate the amount of genuinely relevant material.
Introducing RCP-nDCG@10
RCP-nDCG@10 addresses this coverage gap while preserving the ordering objective of traditional nDCG.
Rather than relying only on a fixed human-labeled answer key, it uses a calibrated AI judge to assess every retrieved document against a
relevance rubric
. This means relevant documents can receive credit even if they were not included in the original benchmark judgments. In simple terms, traditional nDCG scores results against what was previously labeled; RCP-nDCG@10 scores each retrieved result on its
actual
relevance.
Figure 3.
This goes beyond asking an LLM to grade each document. RCP-nDCG@10 builds each score from two signals. The judge answers five yes/no questions about every document, ranging in difficulty and identical for every query. It also compares the documents against each other in groups, estimating how likely each one is to beat the others. Calibration then combines the two: the comparisons set the order, and the rubric places it on a scale shared by every query.
The result is a relevance score that means the same thing for every query — something that can’t be achieved from a single grade issued by an LLM judge.
Figure 4.
Validated against human judgment
To test whether RCP-nDCG reflects real-world relevance, we ran a blind human study. 46 contracted annotators, each with at least a BSc in the relevant field, graded the top-five results of competing systems on queries from
NanoBEIR
,
BRIGHT
and ViDoRe v3, without seeing system names, rankings, or the answer key. Three annotators reviewed every head-to-head contest, with the majority deciding the winner; 289 contests across 273 queries reached a verdict.
Where RCP-nDCG and traditional nDCG named different winners, reviewers sided with RCP-nDCG 70% of the time. Its confidence is meaningful, too: the bigger the margin RCP-nDCG reports between two systems, the more often reviewers agree, reaching 97% for the widest margins. Above a margin of about 0.02, reviewers agree with it 82% of the time; below that, agreement is no better than a coin toss. A bigger margin under conventional nDCG does not help: at the widest margins, reviewers agree with it only 53% of the time (Figure 5).
Figure 5.
Across all contests, RCP-nDCG picked the system reviewers preferred 77% of the time, against 52% for conventional nDCG. Both figures come from a pool that deliberately over-samples contests where the two metrics disagree; where they agree, both match reviewers 87% of the time. RCP-nDCG's key advantage comes from giving credit to relevant documents the answer key missed, which added 19 percentage points. Grading how relevant each document is added a further 6. Importantly, the two effects interact: grading alone added only 3.3 points, as it could only re-weight documents the key already lists.
This advantage holds however complete the key is: where the metrics disagree, reviewers back RCP-nDCG in 64% to 78% of contests at every level of coverage (Figure 6). Together, these results give us confidence that RCP-nDCG is a stronger measure of retrieval quality.
Figure 6.
Backed by the experts
“As embedding models get stronger, traditional retrieval benchmarks are becoming less able to separate the best systems. A big reason is that many potentially relevant documents were never judged in the first place.
RCP-nDCG is an interesting approach to that problem. By using rubric-anchored LLM judgments to fill those gaps, while validating closely against human annotators, it gives benchmarks more resolution and lets us differentiate between models that previous metrics couldn't.
We’re excited to bring RCP-nDCG into MTEB. It has the potential to improve the evaluation signal in existing datasets, while reducing runtime cost, and broaden the scope of languages that can maintain high-quality retrieval benchmarks.”
– Kenneth Enevoldsen, Assistant Professor at Aarhus University and primary maintainer of the Massive Text Embedding Benchmark (MTEB)
Optimizing our next-generation search and retrieval models
Steered by results like these, we chose to optimize against RCP-nDCG@10 rather than traditional nDCG during development of our upcoming fifth generation of
Embed
and Rerank.
One important outcome: these models may not always look strongest when judged only by legacy nDCG scores. Our objective, however, is not to optimize for any given metric for its own sake. It is to align model development more closely with the quality users actually experience in search: finding the most relevant information, including relevant information that older evaluation sets may have missed.
Our objective is not to optimize for any given metric for its own sake. It is to align model development more closely with the quality users actually experience in search.
See for yourself
Paper:
Rubric-Calibrated Preferences: Cross-Query Calibration of LLM Judgments via Item Response Theory
Code and data:
https://github.com/cohere-ai/rcp-ndcg
Want to learn more?
RCP-nDCG@10 reflects a broader shift in how search quality needs to be evaluated as retrieval systems become more capable.
Join us on X on October 8, 2026 with Cohere’s search modeling team for a deeper look at this new methodology, how it is shaping our upcoming releases, and our view of where enterprise search and retrieval evaluation are heading next.
We’re also recruiting private beta partners for
Compass Cloud
, our managed search and retrieval platform.
Request access
to try it on your own retrieval and agentic workloads.
Key contributors
Fabian David Schmidt, Donato Crisostomi, Carlos Lassance, Nils Reimers
Footnotes
1
Parry et al.,
https://arxiv.org/abs/2502.20937
Blog
Written By
Cohere Team
Tags
Technology
AI for Developers
Research
Share
AI isn’t a shortcut.
It’s how business gets ahead.
Contact sales
