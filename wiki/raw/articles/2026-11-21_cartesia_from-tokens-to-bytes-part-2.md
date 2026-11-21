---
title: "From Tokens to Bytes II: Learning from Raw Data"
source: "Cartesia Blog"
url: "https://www.cartesia.ai/blog/from-tokens-to-bytes-part-2"
scraped: "2026-11-21T06:00:35.344430+00:00"
lastmod: "None"
type: "sitemap"
---

# From Tokens to Bytes II: Learning from Raw Data

**Source**: [https://www.cartesia.ai/blog/from-tokens-to-bytes-part-2](https://www.cartesia.ai/blog/from-tokens-to-bytes-part-2)

In the
first post
of this series, we saw remarkable efficiency improvements from hierarchical networks over standard tokenized language models. In this post, we’ll dissect some of these empirical phenomena more deeply through analyzing a wide range of methods. Our ultimate goal is to gain more clarity on the following question: if
our goal is to train the best language models we can, given no priors
, what are the tradeoffs of different approaches? And how much are those priors buying us right now?
Our primary tool will be carefully studying two types of laws:
Compute-to-loss: the standard scaling law, measuring how efficient a model is at pretraining.
Loss-to-loss: the relationship between a model’s pretraining strength (measured in loss or bits-per-byte) and its downstream performance.
Loss-to-loss laws capture some measure of a model’s generalization ability, and we use them as a proxy for how well a pretrained model actually understands its data. We’ll introduce a sequence of carefully controlled models to understand how architecture decisions (particularly those around how input data is processed) affect model performance:
Byte Transformer
BPE with no pretokenization
BPE with pretokenization
H-Net
BLT (Byte Latent Transformer)
A central tension that emerges is
Standard language models operating over compressed inputs have stronger compute efficiency;
Models with access to underlying finer-grained data (such as byte-level) have stronger generalization.
H-Nets turn out to have the best of both worlds, and we provide evidence that their end-to-end nature is essential. Strikingly, a pattern emerges where the quality of a model’s input processing (tokenization or chunking) seems strongly correlated with its ability to understand the data. We’ll find a number of other interesting phenomena along the way!
Pretokenization: the hidden prior
We’ll take a quick detour to discuss an oft-overlooked component of tokenization: the
pretokenization step
. This step involves pre-segmenting the corpus with a hand-crafted regex, which have been progressively engineered to be more and more complex. Here are a few examples.
1
Four regexes that decide
what can become a token
changed from the regex above
GPT-2
OpenAI, 2019
Also used in GPT-3, Falcon, StarCoder2, EXAONE
's
|
't
|
're
|
've
|
'm
|
'll
|
'd
|
␣
?\p{L}+
|
␣
?\p{N}+
|
␣
?[^\s\p{L}\p{N}]+
|
\s+(?!\S)
|
\s+
One of the earlier examples of pretokenization in LLMs, this handled contractions as an explicit list of seven English suffixes; also splits consecutive letters, numbers, and other symbols, which can take one leading space
cl100k
OpenAI, 2023 (GPT-3.5, GPT-4)
Also used in Llama-3, SmolLM3, Phi-4, OLMo 2. Qwen uses it with
\p{N}
.
(?i:
's
|
't
|
're
|
've
|
'm
|
'll
|
'd
)
|
[^\r\n\p{L}\p{N}]?
\p{L}+
|
\p{N}
{1,3}
|
␣
?[^\s\p{L}\p{N}]+
[\r\n]*
|
\s*[\r\n]+
|
\s+(?!\S)
|
\s+
Contractions become case-insensitive; numbers are split every three digits; a word can take one leading non-letter
o200k
OpenAI, 2024 (GPT-4o)
Also used in gpt-oss, MiniMax-M1. Kimi K2 and Nemotron-H use variants.
[^\r\n\p{L}\p{N}]?
[\p{Lu}\p{Lt}\p{Lm}\p{Lo}\p{M}]*[\p{Ll}\p{Lm}\p{Lo}\p{M}]+(?i:'s
|
't
|
're
|
've
|
'm
|
'll
|
'd)?
|
[^\r\n\p{L}\p{N}]?
[\p{Lu}\p{Lt}\p{Lm}\p{Lo}\p{M}]+[\p{Ll}\p{Lm}\p{Lo}\p{M}]*(?i:'s
|
't
|
're
|
've
|
'm
|
'll
|
'd)?
|
\p{N}{1,3}
|
␣
?[^\s\p{L}\p{N}]+[\r\n
/
]*
|
\s*[\r\n]+
|
\s+(?!\S)
|
\s+
Words are split on case, so
CamelCase
becomes
Camel
+
Case
; contractions attach to the word instead of being split off
DeepSeek-V3
DeepSeek, 2024
Also used in DeepSeek-R1, V3.1, V3.2
\p{N}{1,3}
then
[\u4E00-\u9FA5\u3040-\u309F\u30A0-\u30FF]+
then
[!"#$%&'()*+,\-./:;<=>?@\[\\\]^_`{
|
}~][A-Za-z]+
|
[^\r\n\p{L}
\p{P}\p{S}
]?[
\p{L}
\p{M}]+
|
␣
?[
\p{P}\p{S}
]+[\r\n]*
|
\s*[\r\n]+
|
\s+(?!\S)
|
\s+
Three regexes in a row: digits, then a hardcoded CJK range (ideographs and kana, no Korean), then a standard pretokenization regex with additional punctuation rules
The most obvious effect of pretokenization is to break English text into whitespace-separated words; without pretokenization, the vocabulary ends up with many gibberish-looking tokens.
Details: Examples of tokens without pretokenization
The most obvious examples of tokens that don’t carry semantics cross whitespace without spanning full words.
Common suffixes, prefixes, and words glued to each other:
ed the
s and
s of the
es in the
the s
a c
to re
ed and un
s are un
Middle substrings of multi-word proper nouns:
North Kore
New Yor
ong K
audi Arab
Tokens crossing sentence punctuation:
. The
, and
s, but
I don't
Said...\n\n
Tokens crossing newlines and indentation:
.\n\nThe
;\nimport
\n\n	def __init__(self,
(self):\n self.
Intuitively, the broader role of pretokenization is to try to align tokens with semantics in the data
(notably, whitespace-separated words tend to carry semantics in Latin-script languages).
Once again, pretokenizers are
not
learned from data at all, running counter to the bitter lesson, and indicating that learning basic concepts such as words from bytes is a nontrivial problem. In this post, we’ll try to quantify some of the effects of pretokenization.
Loss-to-loss scaling laws: how pretraining transfers downstream
In
Post I
, we saw that an H-Net’s relative compute advantage grows between the in-distribution pretraining loss and downstream distributions:
1.3x compute multiplier on a diverse data mixture, going up to 2x on downstream evaluations
2x compute multiplier on the code subsplit, going up to 5x on out-of-domain languages
Is this a fluke of the setup, or is there something deeper here?
Taking a step back, why does the community care so much about scaling laws, and in particular laws for
pretraining loss
?
It’s broadly believed that pretraining loss is the most important predictor of a model’s quality, and, for example, that downstream performance can be predicted fairly accurately from pretraining loss. A typical procedure first fits compute-to-loss laws, and then fits the loss against downstream evaluations.
The way to measure this is through
loss-to-loss laws
, which for a family of models plots
(loss in domain A, loss in domain B)
, measuring the correlation between losses on different distributions.
When A is the pretraining distribution and B is a downstream evaluation domain, it’s further believed that this loss-to-downstream conversion happens at an “intrinsic rate”, transferring across model families.
For example, many scaling laws (such as
Marin
) take pretrained models from entirely different families and fit a fairly accurate law across them!
Prior work has explicitly stated that the tokenizer, of relevance to us, does not have a major impact on loss-to-loss laws (
LLMs on the Line
, Figure 5).
We’ll provide empirical evidence that
this belief is a myth
, and in fact
Input encodings such as tokenization can produce very large compute efficiency effects (2-4x) on downstream evaluations
We will examine this through exploring a range of baselines including
Byte-level isotropic (non-hierarchical) models
BPE-tokenized Transformers,
with
and
without
pretokenization
Hierarchical networks: the standard end-to-end H-Nets, as well as variations with different chunking behaviors
We’ll start with a pure byte-level model (Byte Transformer) on its own, with no tokenizer or chunking at all. We trained new scaling ladders from scratch with their own hyperparameter tuning, following the
same methodology
as the BPE ladder.
For
every
run on its ladder,
including those not on the compute-optimal frontier
, we plot the validation bits-per-byte against the bpb of the OLMES evaluation suite. The two are strongly correlated: the runs fall on one smooth curve, which forms the ladder’s loss-to-loss law (we also call this the validation-to-OLMES law to be specific about which losses). Above it is compute-against-loss; switch it to C → OLMES for the other half of the picture, the compute-to-downstream law.
A loss-to-loss law
Validation bpb vs. compute
0.7
0.8
0.9
1.0
1.1
10
18
10
19
10
20
Compute (FLOPs)
Validation loss (BPB)
OLMES bpb vs. validation bpb
0.4
0.5
0.6
0.7
0.8
1
1.2
1.4
0.25
0.3
0.4
0.5
0.6
0.7
Validation loss (BPB, log)
OLMES loss (BPB, log)
BPE Transformer
Byte Transformer
BPE-NP Transformer
H-Net
BLT-like
Each point is one run of the Byte Transformer sweeps used to compute its laws (not just the compute-optimal frontier), plotting both validation and OLMES bpb; the curve is its loss-to-loss law.
BPE with No Pretokenization
The BPE algorithm by itself (and other tokenization algorithms like Unigram and so on) can be considered “learning from raw data”, in the sense of being a generic unsupervised learning procedure that depends on the data distribution and starts from bytes. But the existence of highly engineered pretokenization steps breaks this fantasy. So how important are they, really? We’ll examine the effect of pretokenization by using a tokenizer created using
BPE with no pretokenization
, which we call
BPE-NP.
2
We trained a new BPE-NP tokenizer in-corpus following the same methodology as usual, and re-trained a scaling ladder. Immediately, there’s a really interesting tradeoff between
compute-to-loss
and
loss-to-loss
.
Compute-to-loss
Compared to byte-level models,
BPE tokenization noticeably improves compute-to-loss
: it’s
nearly 5x
more compute efficient to reach the same validation loss.
Intuitively, merging low-level bytes into larger tokens downsamples the data significantly (in this case, by 6.03x), which allows compute to be used for high-level processing. To spend an equal number of FLOPs on the same data, the BPE Transformer can use 6x more parameters than the Byte Transformer!
3
Loss-to-loss: the prompt boundary problem
On the other hand, BPE-NP tokenization has very poor loss on OLMES out of the box (significantly worse than the Byte Transformer and any other model), measured by the standard autoregressive calculation: segment the data, compute next-token conditional negative log-likelihoods, average.
It turns out there’s one major source of error, which is subtle and is essentially what’s called the
prompt boundary problem
that’s been known to plague tokenized language models. Corrections are
known to exist
, which marginalize the model’s predictions correctly and fix the model’s probabilities across boundaries. These fixes are nontrivial to design and implement, and may affect a model’s inference efficiency.
Details: The prompt boundary or marginalization problem
The problem essentially boils down to the fact that token sequences don’t map 1-1 onto byte sequences. One way of viewing this is that for a given piece of text (e.g.
How are you doing?
) there are many ways to split it into tokens. The standard bpb calculation only looks at the probability of the
canonical BPE tokenization
(e.g.
How
are
you
doing
?
). But there are other segmentations of the same string (for example, the one that segments into individual bytes), which may still have a non-zero probability assigned by the model. In order to produce the true implied distribution over underlying data (bytes), the model needs to sum over all possible splittings of the string. We call this the “marginalization problem”.
When considering tasks that require prompts and answers, or when using an LLM as a generative model, this gives rise to the
prompt boundary problem
. This happens whenever a prompt ends in the middle of a natural token, so that the correct completion has a non-canonical tokenization. For example, it most commonly appears when language models are prompted with a space at the end, since spaces are usually merged at the beginning of the next word in tokenizers. Fixing this requires the marginalization, or at least considering the canonical tokenization of the full prompt + completion.
BPE-NP (boundary correction)
BPE-NP (no correction)
OLMES vs. compute
0.9
1
1.2
1.4
1.6
1.8
2
2.2
10¹⁸
10¹⁹
10²⁰
10²¹
Compute (FLOPs)
OLMES loss (BPB, log)
OLMES vs. validation
0.9
1
1.2
1.4
1.6
1.8
2
2.2
0.7
0.8
0.9
1
Validation loss (BPB, log)
OLMES loss (BPB, log)
Figure 16. BPE-NP with and without boundary correction.
This plot shows the loss-to-loss and compute-to-eval curves for BPE-NP with and without the prompt boundary fix. Without the marginalization correction, the results for OLMES aren’t even sensible at all.
All of this is generally another issue with tokenization!
Corrected loss-to-loss
The prompt boundary problem particularly affects BPE without pretokenization, because the strange non-semantic nature of the tokens makes it particularly easy to end prompts in the middle of tokens. After addressing this issue - which, again, is subtle and requires a nontrivial fix - we plot the loss-to-loss laws. For the remainder of this post, BPE-NP is the only algorithm that gets special treatment for the way it’s evaluated.
Even despite this fix, it still has much worse loss-to-loss scaling than the pure byte model! This means that
the tokenization of the data fundamentally affected how well pretraining transferred to evaluations
: at equal validation bpb, the byte model consistently has significantly better OLMES bpb!
The loss-to-loss compute multiplier
We can try to translate this difference by mapping it back onto a compute multiplier: if BPE-NP scaled on loss-to-loss just as Byte does, how much more efficient would it be in loss-to-downstream?
More formally:
take a
(validation bpb, OLMES bpb)
point
(x, y)
on the
BPE-NP
loss-to-loss frontier;
at the same validation
x
the byte model frontier will result in a pair
(x, y’)
with lower downstream loss
y’ < y
;
we calculate how much more compute
BPE-NP
would need to drive OLMES bpb from
y
down to this lower
y’
.
This ends up at over
1.9x
. This is quite large and we interpret it as revealing something about how tokenization affects a model’s ability to understand the data and transfer its knowledge to tasks.
Note, however, that this multiplier isn’t enough to offset the massive efficiency savings one gets by compressing the data (nearly 5x from the compute-to-loss law), ending up in an overall win for BPE-NP.
Loss-to-loss laws can differ significantly between architectures, and are a separate axis from compute-to-loss; byte is better than BPE-NP on loss-to-loss, but much worse on compute-to-loss
BPE with no pretokenization
Validation bpb vs. compute
0.7
0.8
0.9
1.0
1.1
10
18
10
19
10
20
Compute (FLOPs)
Validation loss (BPB)
4.86×
OLMES bpb vs. validation bpb
0.4
0.5
0.6
0.7
0.8
1
1.2
1.4
0.25
0.3
0.4
0.5
0.6
0.7
Validation loss (BPB, log)
OLMES loss (BPB, log)
1.93×
BPE Transformer
Byte Transformer
BPE-NP Transformer
H-Net
BLT-like
BPE significantly improves compute efficiency (almost 5x less compute to reach the same validation BPB as a byte-level model), but has worse transfer to downstreams. At a given validation bpb, the BPE-NP model has significantly worse OLMES bpb (representing almost 2x compute).
Adding Pretokenization
Next, we add back the original “BPE” baseline defined in
Post I
.
The addition of pretokenization
improves both compute-to-loss and loss-to-loss
over the BPE-NP models.
On compute-to-loss, BPE is
1.5x
more compute efficient than BPE-NP, which also brings its advantage over byte-level to almost 7.2x.
On loss-to-loss (validation bpb to OLMES bpb), it’s an additional 1.3x more efficient than BPE-NP.
Combining these two, the addition of pretokenization compounds to almost
1.9x
more efficiency when translating compute into the downstream evaluation!
One more interesting takeaway from this comparison is another point of verification that
The point of tokenization is not (just) about compression
This point has been made in prior work such as the aptly named
Tokenization is More Than Compression
, but our scaling law here makes it very acute: despite compressing noticeably more (6.03x vs. 4.57x, about 32%), BPE-NP is much worse than BPE!
4
Instead, we think that tokenization is about (some fuzzy notion of)
finding semantics in the data
, the recurring theme of this post and the spirit behind hierarchical networks.
Indeed, when looking at loss-to-loss laws, the BPE (with pretokenization) method still has a noticeably worse transfer compared to byte-level models, representing a 1.5x compute multiplier. Comparing all three methods so far, an interesting story starts to emerge for loss-to-loss laws.
The model working over raw data (Byte Transformer) has the best transfer from validation to downstream, somehow indicating it perhaps has the best understanding of the data.
Meaning-transforming input encodings such as BPE seem to hinder this understanding.
And the worse these encodings align with our intuitive understanding of the semantics of the data (e.g. removing pretokenization), the worse it gets.
Adding pretokenization
Validation bpb vs. compute
0.7
0.8
0.9
1.0
1.1
10
18
10
19
10
20
Compute (FLOPs)
Validation loss (BPB)
1.48×
7.18×
OLMES bpb vs. validation bpb
0.4
0.5
0.6
0.7
0.8
1
1.2
1.4
0.25
0.3
0.4
0.5
0.6
0.7
Validation loss (BPB, log)
OLMES loss (BPB, log)
1.26×
1.54×
BPE Transformer
Byte Transformer
BPE-NP Transformer
H-Net
BLT-like
BPE is better than BPE-NP in both compute-to-loss and loss-to-loss scaling laws, but still has worse loss-to-loss (1.54x) than the byte-level model.
Aside: The prompt boundary problem for BPE with pretokenization
Just as with BPE-NP, the prompt boundary problem is an issue for BPE and can also be fixed. We found that this provides a small improvement to loss-to-loss laws, but much smaller than for BPE-NP. We don’t report BPE curves with this fix for the rest of the post, because the difference is small, and this seems to be a non-standard technique that may also slow down the inference of models.
This is yet another hidden effect of pretokenization: because it bakes in heuristics to align tokens with common “semantic” boundaries, it reduces the likelihood of the prompt boundary problem appearing. The less meaningful tokens are, as with BPE-NP, the more likely it is that a semantically complete prompt ends in the middle of a token.
Enter Hierarchical Networks
Now we add back the H-Net ladder from
Post I
. Recall that this ladder has the same compression rate matched to that of the BPE Transformer, as well as matching inner and outer networks. Here we find the best of both worlds:
On compute-to-loss, the hierarchical network gets the same compute efficiency improvements from compression that BPE models get, making it way more efficient than the Byte Transformer and a bit more than the BPE.
On loss-to-loss, the hierarchical network has the same efficiency as the Byte Transformer, much better than BPE (1.61x)!
The two gains stack: fitting compute-to-OLMES directly gives about 2.06×.
Note that the 1.28x and 2.06x compute multipliers are the same as from
Post I
. But our loss-to-loss multiplier is saying more than just 2.06 / 1.28 = 1.61.
The compute-to-loss laws (both the 1.28x compute-to-validation and 2.06x compute-to-OLMES) are fit directly, representing the
compute-optimal frontier
, using the iso-FLOP methodology.
The loss-to-loss curves are not fitted directly on the scattered points; they are implied by the fitted compute-optimal frontiers for validation and evaluation, so by construction the loss-to-loss curves describe compute-optimal runs. However, even runs far from the frontier also fall on the curves (within about 1% RMSE). The conversion from validation to evaluation bpb is therefore not just a property of compute-optimal scaling; it seems to be an intrinsic property of the architecture.
Enter hierarchical networks
Validation bpb vs. compute
0.7
0.8
0.9
1.0
1.1
10
18
10
19
10
20
Compute (FLOPs)
Validation loss (BPB)
1.28×
OLMES bpb vs. validation bpb
0.4
0.5
0.6
0.7
0.8
1
1.2
1.4
0.25
0.3
0.4
0.5
0.6
0.7
Validation loss (BPB, log)
OLMES loss (BPB, log)
1.61×
BPE Transformer
Byte Transformer
BPE-NP Transformer
H-Net
BLT-like
H-Nets trained on bytes reach the same loss-to-loss transfer as isotropic byte models, while also leveraging hierarchy to improve compute efficiency beyond BPE models.
How much does end-to-end training help?
So far the evidence is consistent with this interpretation:
Models operating at a byte-level interface can “understand the data” better, achieving better loss-to-loss transfer.
Models compressing the data (either through pre-processed tokenization, or hierarchical models) are more compute efficient.
But H-Nets aren’t the only models with this property; one of their defining features is being learned end-to-end, but it’s possible to define simpler hierarchical models that still have the above two properties. Perhaps the most well-known one for byte-level modeling is the Byte Latent Transformer (BLT), which uses an entropy heuristic from a proxy model to define how to chunk data.
We define a
BLT-like
architecture that keeps the exact same hierarchical structure (architecture and compression rate) as our H-Net, but defines boundaries using a proxy model instead of learning them end-to-end. More specifically, it uses a smaller byte-level model trained separately, then decides to create chunks whenever this proxy model’s conditional predicted distribution of the next byte has an entropy exceeding a fixed threshold (the threshold is monotone to compression rate, so it’s tuned on the validation set to target the 4.57 BPE compression ratio).
5
We also considered: what if instead of training the boundaries end-to-end inside the H-Net, we treat the boundaries as fixed, but given by another H-Net? This disentangles whether boundaries are good because they’re trained end-to-end, or simply because they’re “high quality” (dynamically generated using a different end-to-end model).
We trained a few models at varying FLOP budgets, with the following methodology:
At each training FLOP budget, we trained a slightly smaller isotropic proxy model E and a smaller H-Net proxy model H (both target a FLOP budget 1e0.5 times less than the target).
At the target FLOP budget, we then compared three models:
A hierarchical network with boundaries determined by the entropy heuristic using E
A hierarchical network with boundaries given by the encoder of H
A hierarchical network fully trained end-to-end (the standard H-Net)
Model FLOPs
(proxy FLOPs)
Validation BPB
Entropy Proxy
H-Net Proxy
H-Net
10
19
(10
18.5
)
0.8160
0.8139
0.8001
10
19.5
(10
19
)
0.7623
0.7504
0.7488
10
20
(10
19.5
)
0.7138
0.7057
0.7027
Table 2.
Proxy FLOPs denote pretraining budgets of the proxy model. All models use the exact same architecture and compression rate; proxy training and inference FLOPs are ignored in favor of the baselines.
The results show a consistent pattern.
Comparing entropy proxy vs. H-Net proxy, we see that
boundary quality matters
: the ones given by the H-Net proxy are better than the entropy heuristic.
Comparing H-Net proxy vs. H-Net, we see that
end-to-end training matters
: learning the boundaries inside the model is better than using a pretrained H-Net’s frozen boundaries. Note that this comparison is even generous to the proxy version, because we’re not counting FLOPs used to train the proxy model
or
FLOPs at inference used for it to create boundaries!
The sidepanel plots show the full scaling ladders of H-Net vs. BLT-like, where H-Net shows advantages in both compute-to-loss and loss-to-loss. The loss-to-loss is interesting: when looking at Byte Transformer and H-Net we speculated that they had the best loss-to-loss transfer because they’re byte-level interfaces, but BLT-like indicates that this isn’t sufficient. Models should not just operate over low-level data, but need to learn and utilize the right patterns in the data. Heuristic chunks such as those given by the entropy threshold are better than BPE, but still suboptimal. Once again, the bitter lesson shows its face.
End-to-end training
Validation bpb vs. compute
0.7
0.8
0.9
1.0
1.1
10
18
10
19
10
20
Compute (FLOPs)
Validation loss (BPB)
1.40×
OLMES bpb vs. validation bpb
0.4
0.5
0.6
0.7
0.8
1
1.2
1.4
0.25
0.3
0.4
0.5
0.6
0.7
Validation loss (BPB, log)
OLMES loss (BPB, log)
1.32×
BPE Transformer
Byte Transformer
BPE-NP Transformer
H-Net
BLT-like
Training chunks end-to-end is truly beneficial! Other multi-stage pipelines that define chunks offline don’t match the performance of an H-Net.
Learning from raw data
Putting it all together, we compare a suite of methods that only uses the byte-level data generically.
Isotropic Byte Transformer
: A standard byte-level Transformer, where the rungs account for compute but the models have fewer parameters. Every other model in this suite has matched compute
and
parameters.
BPE-NP Transformer (no pretokenization)
: We interpret this as a two-stage pipeline of (1) tokenization using BPE (which technically doesn’t use priors and learns from data) and (2) language modeling over tokens. This can still be considered operating over the raw data.
BLT-like
: A hierarchical model with the same architecture layout and compression rate as our H-Net, only varying the way chunks are defined.
Following the BLT paper, the proxy model is a byte Transformer (our optimal rung at 1e19.5 FLOPs). To be favorable to this baseline, we don’t count its FLOPs at all, both training and inference.
H-Net
: The
ladder
we set up to match BPE models.
Finally, we include
BPE (with pretokenization)
as well, as the standard language model baseline. Note that because of hand-engineered pretokenization this doesn’t follow the spirit of learning from raw bytes, and is distinguished with a dashed line.
Learning from bytes, side by side
Pick the ladders to compare
Validation bpb vs. compute
Enlarge
0.7
0.8
0.9
1
10
18
10
19
10
20
Compute (FLOPs)
Validation loss (BPB, log)
OLMES bpb vs. validation bpb
Enlarge
0.4
0.5
0.6
0.7
0.8
1
1.2
1.4
0.25
0.3
0.4
0.5
0.6
0.7
Validation loss (BPB, log)
OLMES loss (BPB, log)
OLMES bpb vs. compute
Enlarge
0.8
0.9
1
1.2
1.4
1.6
10
18
10
19
10
20
Compute (FLOPs)
OLMES loss (BPB, log)
Compute multiplier · pick any two
BPE
H-Net
BPE-NP
Byte
BLT-like
BPE Transformer
H-Net
BPE-NP Transformer
Byte Transformer
BLT-like
Figure 17. Methods that learn from bytes, with BPE for reference: compute to validation loss (left), validation loss to OLMES (middle), and compute to OLMES (right). Click to enlarge any graph.
Quantifying the bitter lesson
Feel free to play around with the plot! We observe the following multipliers, reported as the multiplier that H-Nets have relative to other methods.
Method
Compute multiplier vs. H-Net
Compute → validation
Validation → OLMES
Compute → OLMES
H-Net
1×
1×
1×
BLT-like
1.40×
1.32×
1.84×
BPE
1.28×
1.61×
2.06×
BPE-NP
1.89×
2.02×
3.82×
Byte
9.19×
1.05×
9.60×
On compute-to-loss, H-Net is the only method without priors that scales better than BPE. The loss-to-loss additionally shows a striking pattern,
consistent with the following hypothesis.
Models that can manipulate the raw data (finer-grained representations, free from encoders that are potentially semantic-warping) represent the ceiling of “understanding the data”, and have the best transfer from pretraining to evaluation. Pure (isotropic) byte-level models represent this ideal.
The less “semantic” the encoding of information, the worse this transfer.
Pretokenization is a hard-coded hack to enforce such semantics, and in our experiments represents a 1.26x compute multiplier for loss-to-loss laws (BPE vs. BPE-NP).
Even with this hack, BPE models still have a 1.5x compute multiplier from the byte ceiling: pre-defined tokens can still be misaligned from the semantics of the data.
1-stage hierarchical networks can recover the ceiling, despite performing a version of compression similar to tokenization, by doing their chunking dynamically (depending on the context) and end-to-end.
Overall, we see a wide range of performance across different methods, indicating that architectures and tokenization can really affect the abilities of language models.
We can think of this as one way the bitter lesson shows itself – how exactly does preventing a model from learning what it wants to affect its ability to scale?
Conclusion
This post examined methods that learn language modeling from bytes, exploring their tradeoffs through compute-to-loss and loss-to-loss scaling laws. Here are a couple of takeaways that we found interesting.
Loss-to-loss scaling laws are very interesting to study, and contrary to common belief they can vary significantly by architecture and tokenizer. The difference between byte-level models and BPE with no pretokenization represents an up to 2x compute multiplier.
The prompt boundary problem is real for BPE models, which can show up in some types of evaluations. We’re not sure how prevalent it is and it can be influenced strongly by pretokenization.
Compression is not directly related to compute efficiency (evidenced by BPE vs. BPE-NP).
Pretokenization, an often overlooked part of tokenization that is incredibly hand-engineered, has a very large effect. It improves both compute-to-loss and loss-to-loss while reducing data consumed.
Overall, the way byte-level data is processed and encoded (e.g. variations of tokenization, or hierarchical models with different chunking rules) can compound into very large compute efficiency effects on downstream evaluations (2-4x).
H-Nets can recover or exceed the pretraining compute efficiency of standard language models (measured by validation loss scaling laws), while also matching the loss-to-loss transfer of byte-level models, achieving the best of both worlds.
Consistent with the bitter lesson, H-Net’s improved performance is directly attributable in part to its end-to-end learning.
Many questions remain. For example, this post only studied pretraining - but if end-to-end chunking shows improved transfer from pretraining loss to evaluations, how would it transfer to posttraining, where deep understanding of the data’s semantics might matter even more? We’ll leave such questions to future work.
We hope this journey through hierarchical networks was interesting and offered some surprising results or inspired new ideas!
Footnotes
These are published in
tiktoken
and each model’s
tokenizer.json
on HuggingFace.
↩
Technically speaking, it would be more accurate to relabel what we are calling “BPE” and “BPE-no-pretok” (BPE-NP) instead as “BPE-with-pretok” and “BPE” respectively. We’ll stick to this terminology since the conflation of BPE with the full tokenization pipeline has become the convention.
↩
Roughly speaking 6x; perhaps a little more due to the quadratic cost of attention, perhaps a little less due to the increased embedding parameters for the larger vocabulary.
↩
Although results along these lines seem to have been touched on in related papers, we haven’t seen scaling laws comparing pretokenization.
↩
We call this “BLT-like” instead of BLT because it uses the defining entropy heuristic of BLT, but BLT’s hierarchical architecture differs somewhat from the one we use here. We believe that architecture is largely orthogonal to the core problem of chunking, but it could matter especially when learning chunks end-to-end.
↩
