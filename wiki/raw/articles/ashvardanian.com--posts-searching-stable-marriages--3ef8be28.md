---
title: "Combinatorial Stable Marriages for DBMS Semantic Joins 💍"
url: "https://ashvardanian.com/posts/searching-stable-marriages/"
fetched_at: 2026-05-05T07:01:51.279158+00:00
source: "Ash Vardanyan"
tags: [blog, raw]
---

# Combinatorial Stable Marriages for DBMS Semantic Joins 💍

Source: https://ashvardanian.com/posts/searching-stable-marriages/

How can the 2012 Nobel Prize in Economics, Vector Search, and the world of dating come together?
What are the implications for the future of databases?
And why do Multi-Modal AI model evaluation datasets often fall short?
Synopsis:
Stable Marriages are generally computed from preference lists.
Those consume too much memory.
Instead, one can dynamically recalculate candidate lists using a scalable Vector Search engine.
However, achieving this depends on having high-quality representations in a shared Vector Space.
While this already works well for text-based features using modern BERT-like architectures, the quality decreases significantly for Multi-Modal data.
This shortcoming, reflected in OpenAI’s CLIP and our own
Unum’s UForm
, signifies the need for improving modern space-alignment techniques.
Their advancement could not only catalyze the integration of AI into databases but also enhance the performance of upcoming Generative Vision-Language models.
Sounds interesting?
How it all Started?
#
A few years back, after swapping my Physics textbooks for a keyboard and a startup called
Unum
, my first venture into applying our novel algorithms was…
a dating app
.
A predictable first step for a 20-something-year-old single guy, nerding out on Computer Science.
I named the app Amare, a nod to the Latin word for love.
It was the first product I showcased to an investor.
In 2015, explaining the tech behind it - AI, Vector Search, and speculating about Retrieval-based Neural Networks with External Memory - was more challenging than demoing the app itself.
Eventually, I decided to abandon all applications and focus on the underlying framework - Unum.
Much code has been written and many algorithms replaced since then.
But I’ve found that older, often overlooked algorithms still have untapped potential.
The Cost of Stable Marriages
#
The field of Combinatorics introduces a fascinating concept - the Stable Marriage.
Imagine you have two sets - “men” and “women”.
Your task is to pair them, considering their preferences, ensuring that no couples want to swap partners.
Suppose we have
n
men and
n
women, with each person having ranked all members of the opposite sex according to their preferences.
We have to arrange marriages between men and women such that no man and woman would rather be with each other than their current partners.
If no such pairs exist, the set of marriages is deemed stable.
The algorithm is trivial, to a point where a child could invent it.
But its applications are so profound that its creators bagged the Nobel Prize in Economics in 2012.
But here’s the kicker: when things get too big, they tend to break.
The algorithm assumes complete preference lists for every man and woman.
If we have a 1 Billion men and 1 Billion women on the lookout for a partner, each would need to rank 1 Billion candidates.
You can, of course, keep just a small set of candidates for every person.
But what if half of the population picks celebrities exclusively in their top list?
One can always engineer heuristics, but shortcuts have shortcomings.
With 1 Billion candidates for every person, you’d need 8 Million Terabytes of RAM to start with the classic algorithm.
Multiply that by $10'000 per Terabyte of RAM, and you get a jaw-dropping $80 Billion.
Practically infeasible and exorbitantly expensive.
To give you a frame of reference, the world’s most powerful supercomputer, the $600 Million Frontier, boasts less than 10 Petabytes of memory.
That’s a thousand times smaller than what we need for our matchmaking job.
Don’t lose heart though.
You don’t need a supercomputer to find a satisfying solution.
In fact, it can be achieved even on a single workstation.
Back in 2015, my proof-of-concept ran smoothly on 2x Intel Xeon e5 2698v3 CPUs.
Today, we can do it with even less.
The Art of Balancing Compute
#
In Computer Science, we often compare algorithm asymptotics, focusing mainly on time complexity and neglecting space complexity.
We tend to forget that you can actually compensate for one with the other.
Instead of storing preferences, we can recalculate them as needed.
A practical approach could look like this:
Encode all profiles using a single neural network.
Build two
kANN
indexes: one for men and another for women.
Generalize Stable Marriages over these indexes.
Sounds simple, right? But there’s a catch.
Existing public Vector Search engines lack the capability for “joins”.
So, we had to implement one in USearch.
Incorporating Joins into
USearch
#
The original
Gale–Shapley algorithm
, conceived in 1962, was designed to handle sets of identical sizes.
However, in 1970,
McVitie and Wilson
demonstrated that achieving stability in mismatched sets required only a slight modification to the termination conditions of the iterative process.
While this tweak greatly simplifies the work of coders like myself, it is insufficient when grappling with probabilistic data structures.
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
algorithm stable_matching is
Initialize m ∈ M and w ∈ W to free
while ∃ free man m who has a woman w to propose to do
w := first woman on m's list to whom m has not yet proposed
if ∃ some pair (m', w) then
if w prefers m to m' then
m' becomes free
(m, w) become engaged
end if
else
(m, w) become engaged
end if
repeat
The only thing USearch was lacking for this was a trivial fixed-capacity
“ring” class
to house the list of available men.
To ensure compatibility with many-core architectures, I’d advise limiting the number of proposals per man to
log(len(men)) + multiprocessing.cpu_count()
, and employing this as the termination criteria.
1
2
3
4
5
from
usearch.index
import
Index
men
=
Index
(
...
)
women
=
Index
(
...
)
couples
:
dict
=
men
.
join
(
women
,
max_proposals
=
0
,
exact
=
False
)
If you pass
max_proposals=0
, then USearch will automatically estimate the stopping criterea.
As we will be evaluating datasets of different size, I am going to hard-code the value to
max_proposals=100
to reduce variance.
Please note, the
full implementation
is more uglier, incorporating multiple concurrent bitsets for synchronization.
Performance
#
USearch implements the HNSW structure for Approximate Nearest Neighbors Search.
The performance of the vanilla HNSW highly hinges on the size of the index.
With small vectors and collections of less than 1 Million vectors that fit into CPU caches, USearch exceeds 500'000 queries per second.
However, when dealing with Billions of entries, the performance plummets down to a mere 1'000 queries per second.
After that, it begs the question:
How many proposals (queries) will every man make until we reach a convergence in mapping?
That is a tricky one.
If we always match with the right person, the procedure would take 1 Million seconds, or about 12 days, on a single CPU, or around $1'000 in AWS charges.
It sounds like a good baseline, but you can optimize further.
A possible next step would be to make embeddings smaller and JIT the distance function.
Starting with
v0.19 USearch supports every conceivable JIT approach, including Numba, Cppyy + Cling, as well as SimSIMD and direct assembly injections with PeachPy
.
The reality is harder.
Exploring Uni-Modal Representations
#
As mentioned, our work is far from dating these days.
Today, we’re more involved in matching different forms of content, predominantly visual and textual.
For simplicity’s sake, let’s narrow it down even further and consider the task of matching texts with other texts.
Along with my team, we took advantage of the
Arxiv dataset
, a rich trove of academic paper titles (
T
) and abstracts (
A
).
Here’s the game plan:
Encode the strings using
e5-base-v2
, a model that almost claims the crown in the
Retrieval and STS rankings of MTEB
- the
Massive Text Embedding Benchmark
, while remaining highly cost-efficient.
Construct two distinct search indexes for
T
and for
A
.
Execute a “dataset diagnostic”, examining:
Pair Quality, defined by the similarity between
A[i]
and
T[i]
.
Self-Recall @ 10: searching
T
within
T
and
A
within
A
.
Cross-Recall @ 10: searching
T
within
A
and
A
within
T
.
Merge the two collections, observing two key metrics:
The proportion of strings that are joined (paired).
The proportion of strings that are correctly joined (paired). The most important final metric!
The whole dataset clocks in at approximately 2 Million entries.
We’ll look at three log-step subsets - the initial 10 K, 100 K, and 1 M entries respectively.
Metric
10 K
100 K
1 M
Pair Quality
0.8754
0.8754
0.8768
Self-Recall
A
@ 10
99.98%
99.96%
99.85%
Self-Recall
T
@ 10
100.00%
99.99%
99.89%
Cross-Recall
A
in
T
@ 10
94.78%
86.49%
76.98%
Cross-Recall
T
in
A
@ 10
95.09%
86.85%
77.41%
Joined
98.12%
96.29%
94.34%
Joined Correctly
87.85%
70.47%
57.67%
As evident, the
percentage of correctly joined entries is typically marginally lower than the product of cross-recalls
.
The utilized embeddings from
e5-base-v2
are 768-dimensional.
Retaining them in their original
f32
format can be rather expensive, hence I decided to rerun the experiments downcasting to
i8
eight-bit integers.
The loss in accuracy is barely noticeable, yet the construction, and search/join speed increases threefold.
Metric
10 K
100 K
1 M
Pair Quality
0.8754
0.8754
0.8768
Self-Recall
A
@ 10
100.00%
99.97%
99.85%
Self-Recall
T
@ 10
100.00%
99.99%
99.89%
Cross-Recall
A
in
T
@ 10
94.59%
86.43%
76.91%
Cross-Recall
T
in
A
@ 10
95.15%
86.90%
77.39%
Joined
98.05%
96.30%
94.33%
Joined Correctly
87.60%
70.48%
57.59%
Pitfalls of Multi-Modal Representations
#
The more modalities you incorporate, the more challenging it becomes to weave them seamlessly into a single, especially compact, model.
Let’s examine “Open CLIP”, the most common adaptation OpenAI’s “Contrastive Language-Image Pre-training” (CLIP) paper.
This model is not only instrumental in search tasks but also lays the foundation for numerous Generative AI models like Dall-E 2.
We’ll evaluate the search and join quality on the Creative Captions dataset, comprising 3 Million pairs of images (
I
) and text (
T
).
Let’s start by focusing on the first 10'000 pairs, applying brute-force exact search:
Cross-Recall
T
in
I
@ 10: 72%
Cross-Recall
I
in
T
@ 10: 74%
Interestingly, almost 30% of the time, even with a modest dataset size of 10 K entries and full-precision calculations, we end up with embeddings so speckled with noise that the accurate linkage between an image and its corresponding text does not even make it to the top-10 rank.
This situation is somewhat analogous to your sought-after result failing to make it onto the first page of a Google search.
Now, to scale this further, one would typically shift from a brute-force approach to Approximate Nearest Neighbors Search.
Metric
10 K
100 K
1 M
Pair Quality
0.2565
0.2565
0.2566
Self-Recall
I
@ 10
99.99%
99.90%
99.66%
Self-Recall
T
@ 10
99.81%
98.39%
94.22%
Cross-Recall
I
in
T
@ 10
71.31%
47.31%
24.56%
Cross-Recall
T
in
I
@ 10
71.00%
46.15%
24.14%
Joined
95.54%
91.60%
84.43%
Joined Correctly
43.50%
22.91%
9.02%
The share of correct joins plummeted from the 58% for Uni-Modal representations in the previous section to 9% on Multi-Modal
.
These figures are indicative of the low performance of Open CLIP with the
ViT-B-16
visual tower.
However, this is not an issue exclusive to CLIP.
Our UForm neural networks exhibit the same symptoms, occasionally more severely, given their training on 1'000 times fewer samples.
Upon using a larger CLIP
ViT-G/14
checkpoint with 2 Billion neurons, the results get better:
Metric
10 K
100 K
1 M
Pair Quality
0.3759
0.3760
0.3759
Self-Recall
I
@ 10
99.99%
99.95%
99.77%
Self-Recall
T
@ 10
99.87%
98.64%
94.89%
Cross-Recall
I
in
T
@ 10
77.94%
54.64%
31.27%
Cross-Recall
T
in
I
@ 10
75.98%
54.26%
32.02%
Joined
95.97%
91.47%
83.81%
Joined Correctly
53.69%
30.80%
13.46%
Despite being the leading public model for zero-shot classification, when we plug its weights into USearch and request joins, the outcome is less than ideal with only 13% of entries being correctly joined.
This points to the glaring fact that our current Multi-Modal alignment techniques are far from satisfactory.
This remains true whether we employ traditional approaches like the OpenAI’s Contrastive Loss, or newer methodologies like the
Mid-Fusion used in UForm
.
The Road Ahead
#
Though merging AI and DBMS may seem a distant goal, let’s view this differently.
Almost a decade ago, I had some of the best dates of my life, all thanks to natural curiosity in Combinatorics and AI…
along with lenient data-regulation policies and experience writing enterprise-grade crawlers, of course 😅
USearch and any other decent implementation of NSW-like algorithms would work for anything with a defined similarity measure
.
From developing your dating app to applying “Semantic Joins” to job matching, targeted advertising, and beyond—the only limit is your imagination.
The future is yours to shape!
