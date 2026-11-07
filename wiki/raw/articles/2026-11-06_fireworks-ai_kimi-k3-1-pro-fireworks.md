---
title: "Kimi K3.1 Pro on Fireworks: More Intelligence per Dollar, Delivered Fast"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/kimi-k3-1-pro-fireworks"
scraped: "2026-11-06T06:00:21.851878+00:00"
lastmod: "2026-11-05T01:41:34.000Z"
type: "sitemap"
---

# Kimi K3.1 Pro on Fireworks: More Intelligence per Dollar, Delivered Fast

**Source**: [https://fireworks.ai/blog/kimi-k3-1-pro-fireworks](https://fireworks.ai/blog/kimi-k3-1-pro-fireworks)

Kimi K3.1 Pro
from Moonshot AI is available on Fireworks at launch. You can use it on serverless with pay-per-token pricing, or run it on a dedicated deployment for reserved capacity.
What’s new in K3.1 Pro
In our
Specialized Intelligence Index
evaluations, K3.1 Pro was the fastest model on Legacy Bench and CorporateBench, and second-fastest on ORCA. Moonshot post-trained K3.1 Pro from K3 and swapped K3’s full-attention layers for sparse attention, which makes long contexts more efficient to serve. Key specifications:
Spec
Kimi K3.1 Pro
Modalities
Text and vision
Total parameters
2.78T
Active parameters
104B
Input context length
1040k tokens
Experts
896 (16 active per token)
Attention
Kimi Delta Attention + Gated DeepSeek Sparse Attention
How it performs on the Specialized Intelligence Index
We evaluated K3.1 Pro on the Fireworks
Specialized Intelligence Index
(SII): benchmarks built by companies like Sierra, Harvey and Rogo to choose the models they run in production.
K3.1 Pro sits on the quality-for-cost frontier on five of these benchmarks: no model scores higher without costing more.
Figure 1: Kimi K3.1 Pro on Sierra’s τ³-Banking, score vs. cost per trial, from Fireworks’ Specialized Intelligence Index.
Customer support (
Sierra’s τ³-Banking
):
agents resolve banking requests using database tools while following bank policy. K3.1 Pro ranks first of 19 at 64.7%, 8.7 percentage points ahead of Claude Opus 5.5.
Legacy code (
Factory’s Legacy Bench
):
maintaining COBOL, Fortran and Java 7 codebases. K3.1 Pro scores 61.0%, third of 14 and the highest-scoring open model.
Legal (
Harvey’s LAB
):
work typically handled by a first-year associate. K3.1 Pro ranks second of 13 at 15.4%, behind Grok 4.6.
Finance (
Rogo’s Big Finance Benchmark
):
928 questions drawn from financial research workflows. K3.1 Pro ties Claude Opus 5.5 at 48.2%.
Incident response (
Traversal’s ORCA
):
finding the root cause of production incidents from traces, logs and metrics. K3.1 Pro scores 32.9%, third of 13 and the top open model, at less than one-fifth the cost per task of either model ahead of it.
Corporate legal (
Epiq’s CorporateBench
):
K3.1 Pro scores 76.9, fourth of 12 and the top open model.
Here’s how K3.1 Pro compares with Kimi K3 on five benchmarks:
Benchmark
Domain
Kimi K3
Kimi K3.1 Pro
Change
τ³-Banking (Sierra)
Customer support
51.5%
64.7%
+13.2 pp
Legacy Bench (Factory)
Legacy code
52.7%
61.0%
+8.3 pp
Big Finance Benchmark (Rogo)
Finance
41.3%
48.2%
+6.9 pp
CorporateBench (Epiq)
Corporate legal
72.4
76.9
+4.5 pts
ORCA (Traversal)
Incident response
31.2%
32.9%
+1.7 pp
Changes are in percentage points (pp), except CorporateBench, which uses score points.
How Kimi K3.1 Pro scores on Moonshot’s evaluations
Moonshot reports the following results at maximum reasoning effort:
Long-horizon coding:
51.7 on SWE Marathon v1.1, ahead of Claude Opus 5.5 (46.3), Claude Fable 5.1 (45.6) and GPT-6 Astra (42.5).
Agentic research:
70.0 on Humanity’s Last Exam with tools and 92.1 on BrowseComp, the top scores in Moonshot’s comparison on both.
Office work:
64.4 on OfficeQA Pro v2 and 73.3 on Artificial Analysis’ Automation Bench, ahead of Claude Opus 5.5 on both (62.2 and 69.5).
Moonshot evaluated K3.1 Pro using harnesses including Claude Code for coding, and sourced most competitor scores from published reports and leaderboards.
Pricing
Standard serverless pricing per million tokens: $2.00 uncached input, $0.20 cached input and $10.00 output.
Get started
Try Kimi K3.1 Pro in the
Fireworks playground
, or call it with model ID accounts/fireworks/models/kimi-k3p1-pro.
Model release
