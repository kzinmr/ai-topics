---
source_url: https://www.pinecone.io/blog/vq-bench/
ingested: 2026-09-19
sha256: 328e9c2aaef7c766bcbad69c19ee0548ed37fdceaea5ab0d1f629880cef3ca2d
title: "VQ-bench: A Composable Vector Quantization Framework"
---

# VQ-bench: A Composable Vector Quantization Framework

**Source**: https://www.pinecone.io/blog/vq-bench/

Full-Text Search is Now Generally Available In Pinecone Database

-

Read the announcement

Dismiss

Products

Enterprise

Customers

Resources

Pricing

Contact

Log in

Start for free

←

Blog

VQ-bench: a Composable Vector Quantization Framework

Ashwin Padaki
, 

Amir Ingber
, 

Edo Liberty

Sep 17, 2026

Engineering

Research

Share:

Jump to section:

Quantizers

Primitives

Pipelines

Experimental Results

Contribute

Share:

Subscribe to Pinecone

Get the latest updates via email when they're published:

Get Updates

Before a vector database can search vectors, it has to store them. But storing high-dimensional vectors at full precision is quite expensive. 
Vector quantization
 (VQ) reduces the number of bits needed to store a vector, making it a critical part of maintaining a vector database.

Because VQ is so important (to both vector databases and LLMs), many research papers are published on the topic every year. Pinecone has been using quantization since its first prototypes. But we can always do better, so we set out to survey and benchmark newer results. We were pretty overwhelmed by just how many quantizers are out there. To make matters worse, every paper seemed to evaluate performance differently, measuring different metrics on different datasets and optimizing for different hardware. We were unable to find any systematic attempt to evaluate the leading methods against one another.

Of course, faithfully implementing dozens of quantizers from scratch comes with its own challenges. Luckily, as we dug deeper into the literature, we began to notice a pattern. Many published quantizers are actually just slight variations of existing ones. In fact, most of them are built from a relatively small set of primitive operations. That gave us an idea: what if we published an open-source library of these core primitives, where building a quantizer was as easy as writing a recipe of which primitives to use and in what order? Then, we would be able to evaluate all of these quantizers in a fair and reproducible way. It would also make it easier to experiment with new variations of existing quantizers or invent new ones altogether.

This was the start of the VQ-bench project. With this post, we're excited to share VQ-bench with the public, including:

A public 
website
 with a running benchmark of popular quantizers

A 
GitHub repo
 where you can contribute your own quantizers and primitives

A 
paper
 on VQ-bench (presented at 
VecDB@VLDB 2026
), along with the 
talk slides
.

Note that this is just the first iteration of VQ-bench; we encourage feedback, corrections, and contributions, and we will add more quantizers over time.

Quantizers

A 
quantizer
 is anything that can take a set of vectors, compress them, and recover desired information later on. In VQ-bench, a quantizer must implement four methods:

 Method 

 Function 

fit

 given a sample of vectors (and optionally queries), learn a 
model

encode

 given the model and a set of vectors, return per-vector 
codes

reconstruct

 given the model and the code for vector 
x
, 
reconstruct
 it 

score

 given the model, a query vector 
q
, and the code for 
x
, estimate the dot-product 
score
 ⟨q, x⟩ 

Primitives

Quantizers are rarely built from scratch. In the literature, they are assembled from a small set of basic operations, which VQ-bench formalizes as 
primitives
. A primitive implements the same four methods as any other quantizer, plus two more that specify exactly how it hands data to the next stage:

 Method 

 Function 

apply

 given the model, transform the vectors into what the next stage should see 

apply_queries

 given the model, transform the queries into what the next stage should see 

A primitive's 
reconstruct
 and 
score
 methods also take as input the next stage's reconstruction and score estimate, respectively.

That makes six methods in total. The extra two are the chaining contract: they are what let primitives be composed, which is the subject of the next section.

VQ-bench implements three groups of primitives.

Conditioners
 transform the data and pass it downstream (
Center
, 
Normalize
, 
PCA
, 
RandomRotate
, ...).

Rounders
 cast each vector to a finite codebook, passing the 
residual
 downstream (
CastUint
, 
CastAngular
, 
CastNormal
, 
KMeans
, ...).

Splitters
 split the vectors and quantize each part with its own chain of primitives (
Segment
).

Pipelines

A 
pipeline
 is a special type of quantizer given by composing two or more primitives in a chain. Compressing a vector walks it forward through the chain, and recovering a vector (or its score) walks it backward.

The forward pass: 
fit
 and 
encode
 follow the same path. At each stage, they perform that stage's job (learning the model / computing the codes). Then, they call 
apply
 to transform the vectors to the next stage and recurse. At the end, 
fit
 concatenates each stage's model and 
encode
 concatenates each stage's codes.

The backward pass: 
reconstruct
 starts at the last stage. Each stage above it folds its own contribution back in (e.g., adding back the mean, undoing a rotation, etc.) until the first stage has an approximation of the original vector.

score
 works the same way, except every stage needs the query as 
it
 saw the data. So, it begins by walking just the query forward with 
apply_queries
. Then, it performs the backward pass on the score.

A quantizer does not have to be a pipeline. Anything that implements the four methods qualifies, and the interface leaves room for methods that are built some other way. But most published quantizers can be expressed as pipelines of primitives, which is what makes the decomposition worth building on.

For example, E-RaBitQ is a popular quantizer (which we found to be quite performant in our experiments). The E-RaBitQ pipeline consists of four primitives:

Center:
 subtract the average dataset vector from each vector

Normalize:
 scale each vector to unit norm

Random Rotation:
 apply a random orthogonal (or random Hadamard) rotation to each vector

Angular Cast:
 snap each vector to a 

-bit integer grid by rounding to the nearest grid point in angle.

A diagram of this pipeline and table for the primitive functions are given below.

The E-RaBitQ pipeline.

 Center 

 Normalize 

 Random Rotation 

 Angular Cast 

fit

 mean dataset vector μ 

 none 

 rotation seed 

 none 

encode

 none 

 the norm ‖x‖ 

 none 

 grid(x) and cos(x, grid(x)) — b bits per dimension and one scalar 

apply

 x → x − μ 

 x → x / ‖x‖ 

 x → Rx 

 x → x − ĝ, where ĝ = grid(x) / ‖grid(x)‖ 

apply_queries

 identity 

 identity 

 q → Rq 

 identity 

reconstruct

 y → y + μ 

 y → ‖x‖ · y 

 y → Rᵀy 

 y → y + ĝ 

score

 s → s + ⟨q, μ⟩ 

 s → ‖x‖ · s 

 s → s, since the query was rotated too 

 s → s + ⟨q, ĝ⟩ / cos(x, grid(x)) 

Experimental Results

We evaluated a suite of 14 quantizers on 5 datasets from 
VIBE
. Each dataset consists of vectors to encode and queries to score. Below, we present some results for two of the datasets: 
ArXiv
 (1,344,643 vectors in 768 dimensions) and 
Yahoo
 (677,305 vectors in 384 dimensions). You can view the full results on the 
website
.

Reconstruction error

Reconstruction MSE
 is the traditional metric for VQ, and it's important for applications like LLM weight compression. To measure it, we sample 1000 random dataset vectors 

. A quantizer reconstructs 

 and we measure the average value of 

.

ArXiv

Yahoo

Recall

For vector databases, a more relevant metric is 
recall
, specifically for reranking. To measure it, we take each query and compute the 1000 dataset vectors of maximum dot-product. A quantizer estimates these 1000 scores, and we measure what fraction of the estimated top-10 were contained in the true top-10 (averaging this fraction over all queries).

ArXiv

Yahoo

Encode time

We also measure how long it takes to encode the entire dataset. Note that encoding is done in chunks and accelerated via multithreading. These results were obtained on an Apple M2 Pro with 16GB RAM using 6 threads.

ArXiv

Yahoo

Discussion

Overall, we can see some clear trends. PQ and OPQ consistently have the lowest reconstruction MSE. EDEN and E-RaBitQ are comparable in terms of recall, especially at higher bit budgets. EDEN is also much faster to encode than PQ, OPQ, and E-RaBitQ, making it a good candidate for most quantization applications.

Contribute

We built VQ-bench to be extended, and the 
repo
 takes two kinds of contributions.

Got a new quantizer?
 Usually just a few lines of code. The E-RaBitQ pipeline above is 
four primitives in a list
, and many published quantizers are a similar reordering of primitives the library already ships.

Got a new primitive?
 Implement the six methods above and it composes with every other primitive in the catalog. Every pipeline can use it, including the ones nobody has written yet.

Either way, you get the evaluation harness. A short config runs your method over the whole suite, measured exactly the way every other method is measured: recall@k, reconstruction and score error, bias, softmax KL and total variation, size in bits per dimension, and encode, score, and reconstruction cost. Both lists keep growing as we add datasets and metrics. We refresh the published benchmark on a regular cadence, and new methods are folded in then.

We also want corrections. If we implemented your quantizer wrong, or we missed a method worth including, open an issue and tell us.

Share:

Was this article helpful?

Yes

No

Recommended for you

Further Reading

Start building knowledgeable AI today

Create your first index for free, then pay as you go when you're ready to scale.

Start Building

Get a Demo

Products

Vector Database

Dedicated Read Nodes

Assistant

Documentation

Pricing

Security

Integrations

Resources

Community Forum

Learning Center

Blog

Customer Case Studies

Status

What is a Vector DB?

What is RAG?

Company

About

Partners

Careers

Newsroom

Contact

Legal

Customer Terms

Website Terms

Privacy

Cookies

Cookie Preferences

© Pinecone Systems, Inc. | San Francisco, CA

Pinecone is a registered trademark of Pinecone Systems, Inc.
