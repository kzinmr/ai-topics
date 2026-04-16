---
title: "Soap Bubbles and Attention Sinks: The Theory and History of the HALO-Loss"
url: "https://substack.com/redirect/325f35e4-a4da-4e07-980c-1b5b6b7ad66b?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E"
fetched_at: 2026-04-16T19:09:13.896315+00:00
source_date: 2026-04-16
tags: [newsletter, auto-ingested]
---

# Soap Bubbles and Attention Sinks: The Theory and History of the HALO-Loss

Source: https://substack.com/redirect/325f35e4-a4da-4e07-980c-1b5b6b7ad66b?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E

The standard Cross-Entropy loss has a well-known flaw: it forces neural networks to push their features toward infinity just to reach full confidence. The result is a messy latent space and models that confidently hallucinate when fed absolute garbage data.
This post breaks down my attempt to fix this with the HALO-Loss. It covers the weird geometry of high-dimensional "soap bubbles", how wiring a parameter-free "I don't know"-button directly into the classification head can significantly reduce out-of-distribution false positives, and a fast math trick to keep GPUs happy while doing so. HALO probably won't magically boost your raw accuracy benchmarks too much, but it can improve calibration and safety, mostly just by giving the network a mathematically sound place to throw its trash.
A few months ago, in my post on
Teacher-Free Self-Distillation (TFSD)
, I discussed how standard Categorical Cross-Entropy (CCE) computes its logits using unconstrained dot products. Recall the geometric definition of a dot product between two vectors:
$$ Q \cdot K = ||Q|| \cdot ||K|| \cdot \cos(\theta) $$
Due to the softmax, to become 100% confident and push the loss to zero, the network is forced to push its features infinitely far away from the origin. This "radial explosion" stretches the latent space and produces models that sometimes confidently hallucinate, even when fed pure noise.
My proposed fix was the TFSD loss, which essentially switched the network over to a metric regime. Instead of a linear layer outputting logits directly and computing the softmax over them, the model outputs an embedding. We then compare this embedding to a set of learned class centroids using the negative squared L2-distance, which is basically an RBF-kernel (Radial Basis Function). This means closer distance equals higher probability. Because distance is physically bounded by zero, the infinite gap disappears. Maximum confidence suddenly maps to a finite location rather than an unbounded asymptotic limit.
It worked beautifully on paper, but explicitly computing pairwise Euclidean distances for thousands of classes is clunky and memory-hungry. GPUs generally hate doing it when they could just be running matmuls instead.
The RBF Detour and the Attention Sink
So, like any responsible researcher, I ignored the inefficiencies and went to work on Transformers instead. ;)
In my most recent work on
Scaled RBF Attention
, I used the same distance-based math for the core of a seemingly more numerically stable attention mechanism. In the process, I found out about a wonderfully simple algebraic workaround. Because we eventually pass these distances through a Softmax function, and Softmax is mathematically
shift-invariant
(adding or subtracting a constant to every logit changes absolutely nothing about the final probabilities), we can actually factor out the query's magnitude entirely:
$$ -||x - c||^2 = -||x||^2 + 2(x \cdot c) - ||c||^2 $$
Since the $-||x||^2$ term is a constant for the whole row being fed into the softmax, we can just drop it, leaving us with a shifted logit:
$$ \text{shifted\_logit} = 2(x \cdot c) - ||c||^2 $$
Suddenly, our annoying distance calculation is just a dot product, penalized by the L2 norm of the key.
In the case of RBF-Attention this created a new headache I had to find a fix for. Standard Transformers use "magnitude bullying" to create attention sinks. They dump unnecessary attention into dummy tokens simply by making their keys massive. Our new distance math strictly penalized massive vectors, so the model couldn't waste unnecessary attention anymore. The fix to these missing attention sinks was to explicitly introduce "Register Tokens" to act as safe, dedicated dumpsters for excess attention.
The "Eureka!" Moment
Some time later, at 2 AM on a Sunday, I was staring at the wiggling lines of a training run, and the wires finally crossed.
If a Transformer needs an attention sink to politely say
"I don't know where to look"
,
wouldn't a classifier massively benefit from a sink to say
"I don't know what this is"
?
An attention sink is really just an
Abstain Class
. It gives the model the explicit structural choice to gracefully nope out of a decision.
What if we applied our highly efficient, shift-invariant RBF math back to the classification head? We create a virtual $K+1$ class with its centroid permanently bolted to the geometric origin ($c = \vec{0}$). What is the shifted logit for this Abstain class? The true distance to the origin is just $-||x||^2$. But remember, our mathematical trick shifted all logits by
adding
$+||x||^2$. So the Abstain logit perfectly cancels itself out:
$$ -||x||^2 + ||x||^2 = 0 $$
(In practice, we compute a mathematically ideal
abstain_bias
based on extreme value theory, instead of strictly 0 to set an adjustable energy threshold. More on that later.)
This method requires zero extra parameters and zero extra compute. If you feed the network a picture of a galaxy, it won't align well with the "Cat" or "Dog" centroids. The standard logits will drop, the L2 centroid penalties will suppress them further, and the constant Abstain bias will naturally win the Softmax. We just built a mathematically rigorous "I have no clue!" button for free.
The Soap Bubble Problem
I happily wired it all up, hit train, and... the embeddings looked terrible and the network capacity completely tanked...
*Sound of dreams going POP*
Did anyone ever warn you about
the curse of dimensionality
? I heard it *a thousand times* and I
still
managed to forget about it.
In 2D or 3D space, if you sample normally distributed points around a center, most points safely clump near the middle like a solid bowling ball. But high-dimensional space is pretty weird. In 128 dimensions, volume expands so aggressively as you move away from the center that almost
all
the probability mass of a Gaussian sits on a microscopically thin outer spherical shell. High-dimensional Gaussians don't look like solid spheres; they behave exactly like
hollow soap bubbles
.
By blindly forcing the model to push positive embeddings to a distance of exactly $0.0$ (the dead center of the class centroid), I was demanding it to compress a natural 128-dimensional soap bubble into an infinitely dense singularity. It had to fight the fundamental physics of high-dimensional space, wasting massive amounts of representational capacity just trying to overcome the expanding volume.
To fix this, I introduced a
geometric regularizer
. Instead of a brute-force squared distance penalty, we evaluate the negative log-likelihood of the true radial distribution (
radial_nll
):
volume_coeff
=
0.5
-
1.0
/
self
.
D
radial_nll
=
-
(
volume_coeff
*
torch
.
log
(
r_sq_true
)
-
0.5
*
r_sq_true
)
It's a balancing act. The $-0.5 r^2$ term (the Gaussian prior) acts as gravity, pulling the feature inward. But the $\log(r^2)$ term acts as a repulsive force modeling the expanding volume of the hypersphere. It actively pushes the embeddings slightly away from the dead-center, allowing them to rest comfortably on their natural $D$-dimensional shell without collapsing.
When you combine the fast RBF-shift, the zero-parameter Abstain Class, the TFSD soft-targets, and the soap-bubble regularizer, you get
HALO (Hyperspherical Alignment & Latent Optimization)
.
The Empirical Reality Check
I can sit and think about fancy math all day, but eventually, a loss function has to survive the benchmark. To see how HALO actually behaves, I ran it head-to-head against standard Categorical Cross-Entropy (CCE) on a ResNet-18 using CIFAR-10 and CIFAR-100.
(I know, ResNet-18 is a few steps away from being a massive frontier model, but I don't have the resources to scale much further than that right now. If your team is working on representation learning and has the infrastructure to properly scale these architectures, I am looking for ML research roles and would love to connect. :) )
To make sure this was a fair, apples-to-apples comparison, I went out of my way to handicap HALO slightly. Standard classifiers project their features into a dimension exactly equal to the number of classes (e.g., 10 dimensions for CIFAR-10). HALO doesn't actually need this restriction. It can happily cluster 10 classes in a roomy 128-dimensional space. But to prove the geometry is doing the heavy lifting, and not just an inflated latent space, I strictly capped HALO's embedding dimensions to match the dataset class count. No extra capacity, no hidden tricks.
Pinky promise!
Usually, in AI safety and calibration research, there is a painful tradeoff: if you want better Out-of-Distribution (OOD) detection, you have to pay a tax by sacrificing some of your base In-Distribution (ID) accuracy. With HALO, that penalty pretty much vanishes. On CIFAR-10, HALO actually edges out CCE slightly in raw accuracy. On the much harder CIFAR-100 dataset, it practically ties, dropping a teeny tiny 0.14%. Maintaining almost exact parity on base accuracy while fundamentally overhauling the latent geometry was a huge relief to me!
Here is how the numbers compare:
Note:
"Near OOD" means feeding CIFAR-100 test images to the CIFAR-10 model, and vice versa.
"Far OOD" means feeding it the Street View House Numbers (SVHN) dataset, a domain it has never even remotely seen.
CIFAR-10 Benchmark (ResNet-18)
Metric
Standard CCE
HALO
ID Accuracy $(\uparrow)$
96.30%
96.53%
Calibration (ECE) $(\downarrow)$
0.0798
0.0151
Far OOD (SVHN) AUROC $(\uparrow)$
92.51%
98.08%
Far OOD (SVHN) FPR@95 $(\downarrow)$
22.08%
10.27%
Near OOD (CIFAR-100) AUROC $(\uparrow)$
82.83%
91.72%
Near OOD (CIFAR-100) FPR@95 $(\downarrow)$
48.94%
37.63%
CIFAR-100 Benchmark (ResNet-18)
Metric
Standard CCE
HALO
ID Accuracy $(\uparrow)$
80.94%
80.80%
Calibration (ECE) $(\downarrow)$
0.1102
0.0283
Far OOD (SVHN) AUROC $(\uparrow)$
81.01%
86.91%
Far OOD (SVHN) FPR@95 $(\downarrow)$
81.00%
63.70%
Near OOD (CIFAR-10) AUROC $(\uparrow)$
79.75%
81.00%
Near OOD (CIFAR-10) FPR@95 $(\downarrow)$
76.77%
75.38%
I'll try to be cautious about throwing around "
SOTA
" on my fun little blog, but if you look at the
OpenOOD
benchmark leaderboards, getting this kind of robust outlier detection natively during training is exceptionally rare. Finding an architectural drop-in that preserves ID accuracy while natively slashing the False Positive Rate (FPR@95) by more than half on some datasets, without relying on heavy ensembles, post-hoc scoring tweaks, or exposing the model to outlier datasets during training, is definitely something I'm proud of.
Hyperspherical Alignment
So now let's take a look at the PCA visualizations of the final 10-D latent spaces for the CIFAR-10 models.
Caution:
Highly subjective visual analysis ahead. Apply boulders of salt...
Despite beeing trained with label-smoothing enabled, standard CCE tends to produce "starburst" streaks. The dot-product mostly cares about angles, so when the optimzer wants to inflate a logit to push the loss closer to zero, it often ends up shoving the embedding further out into the void.
HALO, on the other hand, seems to pull classes into bounded spherical clusters that neatly orbit the origin. Because the logits are explicitly capped by physical distance, the network literally cannot inflate its confidence by throwing vectors to infinity. There's zero gradient incentive for a radial explosion.
Calibration and OOD Detection
Because without labels smoothing CCE constantly pushes features toward infinity, its logits tend to grow larger. This forces the Softmax function to squash everything to 99.9% confidence, even when the model is staring at pure noise and basically flipping a coin.
HALO physically bounds the maximum similarity at an L2-distance of $0$, forcing the network to output more realistic, grounded probabilities. As a result the Expected Calibration Error (ECE) tends to be much lower. On CIFAR-10, it drops from roughly 8% down to a pretty crisp 1.5%.
But the real test is feeding the model data it shouldn't know. Standard CCE struggles immensely, often confidently classifying house numbers (SVHN) as dogs or airplanes. HALO's origin sink catches this data more easily, absorbing significantly more of the out-of-distribution inputs, even when it was never explicitly trained for this task.
Implementation Details: Scaling and Distillation
Taking fancy concepts from a whiteboard and making them actually converge, usually means fighting off a lot of real world issues. To make HALO train smoothly without requiring agonizing hyperparameter sweeps, there are three practical engineering details under the hood:
Dimensional Scaling ($\gamma$):
In high-dimensional spaces, the rising variance is a massive problem. If you simply sum squared distances across 128 dimensions, the raw numbers get huge. Pass that into a Softmax, and it instantly saturates into one-hot vectors, killing your gradients before the model has a chance to learn anything. To fix this, we explicitly average the dot product by dividing by the number of embedding dimensions. We also dynamically initialize a learnable temperature $\gamma$ so the expected initial distance of random vectors perfectly matches a mathematically safe target scale.
The
Ideal
Abstain Bias:
Finding the right energy threshold for an Abstain Class usually turns into a brittle hyperparameter grid-search nightmare. Too high, and the model acts like a nervous student, constantly abstaining; too low, and the sink is practically useless. But because of our shift-invariant math trick, things simplify beautifully. If you expand the algebraic equation for the unnormalized true shifted logit, you'll notice something neat: the centroid norm ($y^2$) completely cancels out! This means the network can freely inflate the magnitude of its centroids to ruthlessly squash out-of-distribution noise without accidentally shrinking its own ID margins.
Because standard unnormalized networks naturally anchor their spatial variance (our $x^2$) roughly around $1.0$ via initialization and weight decay, we know exactly where the 'true' logit is going to naturally settle at equilibrium. We just calculate that mathematical anchor ($t_{ideal}$) and drop the
abstain_bias
exactly one cross-entropy margin below it. The math essentially builds an optimally calibrated rejection threshold.
Teacher-Free Self-Distillation:
Training on a classification task, forcing a probability of exactly 1.0 (using hard one-hot targets) demands unnatural, infinite separation between classes. This would destroy the nice spherical structure we just built. Carried over from my previous work, HALO constructs a soft target distribution using
its own
distances to negative classes, zeroing out only the true class logit. It learns to correct its true class prediction without torching the semantic "dark knowledge" and relative spatial relationships of the rest of the latent space (e.g. keeping cats closer to dogs than to airplanes).
The Big Picture
As far as I can tell, this kind of loss function is novel. We've taken shift-invariant RBF math, a parameter-free origin sink, an exact algebraic equilibrium threshold, and a geometric "soap bubble" regularizer, jammed them into a drop-in replacement for Cross-Entropy. The result scratches an architectural itch I've had for
a long time
.
And the empirical data seems to back up the theory. Getting this level of outlier detection natively during training, without giving up raw accuracy, is a big deal. It drastically reduces overconfident hallucinations by changing the training geometry.
But I think the real potential goes way beyond squeezing better calibration out of standard classifiers. By forcing models to respect euclidean geometry, HALO provides a unified approach to embedding spaces across the broader deep learning ecosystem:
Safer Classification & Uncertainty:
In high-stakes environments like medical diagnostics or autonomous driving, a model's ability to confidently say "I don't know" is at least as critical as its accuracy. A mathematically grounded origin sink natively bakes high-quality outlier detection directly into the forward pass for free.
Multi-Modal Architectures (CLIP):
Vision-language models map text and images into a shared space using unconstrained contrastive dot products. This means they suffer from the exact same magnitude bullying and overconfidence issues as classification heads. Imagine training a CLIP-like model with HALO: matching modalities are strictly bounded by physical distance, and out-of-context inputs naturally collapse into the shared origin sink. You get a geometrically sound rejection threshold for unaligned image-text pairs, while structuring the embedding space without the massive compute overhead of traditional contrastive pairwise mining.
Self-Supervised Learning:
Pretty much all SSL architectures constantly fight "representation collapse", the tendency to map every input to a single point to trivially minimize the loss. Some workarounds require asymmetric momentum encoders or heavy variance-covariance matrices. HALO's geometric "soap-bubble" regularizer acts as a simple repulsive force. It explicitly models the expanding volume of hyperspheres, preventing collapse by ensuring embeddings spread out and rest comfortably on their natural $D$-dimensional shells.
The Code
I’ve put together a clean PyTorch implementation of the HALO-Loss designed to be a relatively simple replacement for standard CCE. All the code, full evaluation reports, and the scripts used to generate the reports plots and animetions are open-sourced and available on GitHub.
If you're dealing with noisy data, building embedding models, or just want to see how clean these latent spaces look, I'd love for you to check out the repository. Give it a spin on your own data, break it, and let me know what you find!
And if it saves you a few hallucination-induced headaches or you just find the math interesting, dropping a star on the repo is much appreciated.
Or you can drop the halo.py file below into your own code and use it like this:
# your imports...
# ...
from
halo
import
HALOModel
,
HALOLoss
# ...
# build and wrap the base embedding-model
base_embedding_model
=
build_embedding_model
(
...
)
model
=
HALOModel
(
model
=
base_feature_extractor
,
n_classes
=
num_classes
,
embedding_dim
=
embedding_dim
)
# init the loss
criterion
=
HALOLoss
(
emb_dims
=
embedding_dim
,
num_classes
=
num_classes
)
# prepare centroid target ids
centroid_targets
=
torch
.
arange
(
num_classes
,
device
=
preds
.
device
)
# your training loop:
for
inputs
,
target
in
dataloader
:
# ...
# compute embeddings and centroids
embeddings
,
centroids
=
model
(
inputs
)
# compute loss
loss
=
criterion
(
embeddings
,
target
,
centroids
,
centroid_targets
)
# ...
# halo.py
import
math
import
torch
import
torch.nn
as
nn
import
torch.nn.functional
as
F
class
HALOModel
(
nn
.
Module
):
"""A wrapper class for extracting sample embeddings and managing class-centroids."""
def
__init__
(
self
,
model
,
n_classes
,
embedding_dim
):
super
(
HALOModel
,
self
)
.
__init__
()
self
.
model
=
model
self
.
n_classes
=
n_classes
self
.
emb_dims
=
embedding_dim
self
.
centroids
=
nn
.
Parameter
(
torch
.
randn
(
n_classes
,
embedding_dim
,
dtype
=
torch
.
float32
)
)
def
forward
(
self
,
x
):
embeddings
=
self
.
model
(
x
)
centroids
=
self
.
centroids
centroids
=
centroids
-
centroids
.
mean
(
dim
=
0
,
keepdim
=
True
)
return
embeddings
,
centroids
class
HALOLoss
(
torch
.
nn
.
Module
):
def
__init__
(
self
,
emb_dims
,
num_classes
,
learn_gamma
=
True
,
distill
=
True
,
label_smoothing
=
0.1
,
reduction
=
"mean"
,
):
super
()
.
__init__
()
assert
emb_dims
>
1
,
"Embedding dimensions must be > 1"
self
.
D
=
float
(
emb_dims
)
self
.
K
=
float
(
num_classes
)
self
.
learn_gamma
=
learn_gamma
self
.
distill
=
distill
self
.
label_smoothing
=
label_smoothing
self
.
reduction
=
reduction
r_sq_target
=
1.0
-
(
2.0
/
self
.
D
)
r_sq_init
=
2.0
init_gamma
=
20.0
/
(
r_sq_init
-
r_sq_target
)
# unnormalized abstain bias
if
label_smoothing
>
0
:
# Exact expected target probabilities strictly over K classes
max_prob
=
1.0
-
label_smoothing
+
(
label_smoothing
/
self
.
K
)
min_prob
=
label_smoothing
/
self
.
K
else
:
max_prob
=
0.99
min_prob
=
0.01
/
self
.
K
margin_ce
=
math
.
log
(
max_prob
/
min_prob
)
t_ideal
=
init_gamma
*
(
1.0
-
r_sq_target
)
self
.
abstain_bias
=
t_ideal
-
margin_ce
# inverse softplus
if
init_gamma
>
20.0
:
gamma_start
=
init_gamma
else
:
gamma_start
=
math
.
log
(
math
.
expm1
(
init_gamma
))
self
.
gamma
=
nn
.
Parameter
(
torch
.
tensor
([
gamma_start
],
dtype
=
torch
.
float32
),
requires_grad
=
learn_gamma
,
)
def
forward
(
self
,
pos
,
target
,
centroids
,
centroid_targets
):
pos
=
pos
.
to
(
torch
.
float32
)
cen
=
centroids
.
to
(
torch
.
float32
)
x_sq
=
pos
.
pow
(
2
)
.
mean
(
dim
=-
1
,
keepdim
=
True
)
y_sq
=
cen
.
pow
(
2
)
.
mean
(
dim
=-
1
,
keepdim
=
True
)
dot_product
=
(
pos
@
cen
.
T
)
/
self
.
D
gamma
=
F
.
softplus
(
self
.
gamma
)
# Softmax is shift-invariant, so we factor out -(x_sq * gamma).
# This leaves standard dot-product similarity with an L2 penalty on keys!
logits_k_shifted
=
gamma
*
(
2.0
*
dot_product
-
y_sq
.
T
)
# The Abstain class acts as an origin sink using the theoretically ideal equilibrium.
logit_abstain_shifted
=
torch
.
full
(
(
pos
.
size
(
0
),
1
),
self
.
abstain_bias
,
dtype
=
pos
.
dtype
,
device
=
pos
.
device
)
# Shape: N x K+1
logits_k_plus_1
=
torch
.
cat
([
logits_k_shifted
,
logit_abstain_shifted
],
dim
=-
1
)
# Reconstruct true absolute distances strictly for Distillation & Return Values
# (Clamping against float errors)
logits_k_true
=
torch
.
clamp
(
logits_k_shifted
-
(
gamma
*
x_sq
),
max
=
0.0
)
# cross_entropy on k+1 calsses
if
self
.
distill
:
mask
=
target
.
unsqueeze
(
1
)
==
centroid_targets
.
unsqueeze
(
0
)
with
torch
.
no_grad
():
# Margin calculation uses the absolute clamped distances
margin
=
logits_k_true
/
self
.
label_smoothing
target_logits
=
torch
.
where
(
mask
,
0.0
,
margin
)
target_probs_k
=
F
.
softmax
(
target_logits
,
dim
=-
1
)
zeros
=
torch
.
zeros
(
(
pos
.
size
(
0
),
1
),
device
=
pos
.
device
,
dtype
=
pos
.
dtype
)
target_probs
=
torch
.
cat
([
target_probs_k
,
zeros
],
dim
=-
1
)
loss_ce
=
F
.
cross_entropy
(
logits_k_plus_1
,
# Uses the shifted, un-clamped logits for smooth gradients!
target_probs
,
reduction
=
self
.
reduction
,
)
else
:
# Labels smoothing with explicit abstain class handling
with
torch
.
no_grad
():
K
=
logits_k_shifted
.
size
(
1
)
target_probs
=
torch
.
full_like
(
logits_k_plus_1
,
self
.
label_smoothing
/
K
,
dtype
=
pos
.
dtype
,
device
=
pos
.
device
,
)
target_probs
.
scatter_
(
1
,
target
.
unsqueeze
(
1
),
1.0
-
self
.
label_smoothing
+
(
self
.
label_smoothing
/
K
),
)
# set the abstain class probability to strict 0.0
target_probs
[:,
-
1
]
=
0.0
loss_ce
=
F
.
cross_entropy
(
logits_k_plus_1
,
target_probs
,
reduction
=
self
.
reduction
,
)
# Geometric Regularizer
diff_true
=
pos
-
cen
[
target
]
r_sq_true
=
diff_true
.
pow
(
2
)
.
mean
(
dim
=-
1
)
.
to
(
pos
.
dtype
)
volume_coeff
=
0.5
-
1.0
/
self
.
D
volume_term
=
volume_coeff
*
torch
.
log
(
r_sq_true
)
gaussian_term
=
-
0.5
*
r_sq_true
radial_nll
=
-
(
volume_term
+
gaussian_term
)
if
self
.
reduction
==
"mean"
:
radial_nll
=
radial_nll
.
mean
()
elif
self
.
reduction
==
"none"
:
pass
else
:
raise
NotImplementedError
total_loss
=
loss_ce
+
radial_nll
return
total_loss
,
logits_k_true
