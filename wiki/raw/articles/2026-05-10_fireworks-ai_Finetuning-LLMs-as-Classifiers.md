---
title: "Fireworks AI"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/Finetuning-LLMs-as-Classifiers"
scraped: "2026-05-10T01:20:42.525031+00:00"
lastmod: "2026-01-16T21:11:43.000Z"
type: "sitemap"
---

# Fireworks AI

**Source**: [https://fireworks.ai/blog/Finetuning-LLMs-as-Classifiers](https://fireworks.ai/blog/Finetuning-LLMs-as-Classifiers)

DeepSeek V4 Pro is Live → Try it now.
Platform
Models
Developers
Pricing
Training
Partners
Resources
Company
Log In
Get Started
Blog
Finetuning Llms As Classifiers
Turn Your LLM into a Calibrated Classifier for $2
PUBLISHED
12/4/2025
Table of Contents
Why Use LLMs for Classification?
Adapting LLMs for Classification
Label Probabilities and Calibration
Experimental Validation
Code Example
No Fine-Tuning? Use the Embeddings API
Appendix: Why renormalization is not needed when fine tuning
Getting Started
Table of Contents
Table of Contents
Why Use LLMs for Classification?
Adapting LLMs for Classification
Label Probabilities and Calibration
Experimental Validation
Code Example
No Fine-Tuning? Use the Embeddings API
Appendix: Why renormalization is not needed when fine tuning
Getting Started
Table of Contents
Large language models aren’t just for free-form generation. A very common production use case is classification, where the model must choose among a small number of classes - and, crucially, return a probability (confidence) for each class.
In this post, we present a practical approach to tuning and serving LLMs for classification tasks. The method builds on existing model training and inference infrastructure and is grounded in a theoretical analysis of how class probabilities naturally emerge during training. These probabilities can then be leveraged for downstream applications - such as ranking and event prediction - or used directly as confidence estimates.
In many real-world setups, the training can be done with a surprisingly small budget - often as cheap as a couple of dollars in compute.
Why Use LLMs for Classification?
Large language models are trained to predict the next token - but many real-world applications don’t need free-form text at all. Instead, they boil down to making discrete decisions: picking one label, one intent, or one route among several options.
Think of:
•
Safety and moderation: allowed vs disallowed content.
•
Routing and triage: deciding whether to send a message to team A, B, or C.
•
Intent classification: identifying whether a user needs billing help or wants to cancel a subscription.
•
Domain-specific tagging: assigning medical codes, legal categories, or document types.
In each of these, the key output isn’t just a class - it’s the probability of each class. Those probabilities drive thresholding, ranking, and downstream decisions.
What makes this particularly interesting is that LLMs already model probabilities - over tokens. The challenge, then, is how to reinterpret or adapt those token probabilities into well-calibrated class probabilities, without giving up the general-purpose nature of the model.
Adapting LLMs for Classification
There are multiple ways to turn a generative model into a classifier. They differ in how much they modify the model, the training stack, or the inference interface.
Adding a Classification Head
A traditional approach is to replace the LM head with a small classifier - a linear or MLP layer trained on top of a pooled hidden representation. This yields a clean softmax over the label space and integrates naturally with classical deep learning setups. However, it changes the model architecture, which means retraining, new exports, and often incompatibility with standard inference stacks or hosted APIs.
Using Tokens as Classes
A more elegant path keeps the architecture completely intact. Each class is mapped to one or more tokens (e.g., "yes" / "no", "positive" / "negative", "0" / "1"). A short prompt is crafted to make the model respond with one of these tokens, and the next-token distribution becomes the class probability distribution.
This approach has several advantages:
•
No architectural changes
– works seamlessly with standard fine-tuning and inference APIs.
•
Cost-effective and robust
– especially for small or medium label sets.
•
Interpretable
– token choices often align with human semantics, making debugging easier.
Of course, tokenization details matter: leading spaces, casing, or multi-token classes can slightly distort the mapping. And when multiple tokens represent one class, their probabilities must be aggregated. But in practice, these issues are manageable – and the benefits far outweigh the complexity.
For most production setups, this method offers the cleanest path to deploy classification models built on top of existing LLM infrastructure: no new heads, no custom serving code, just careful prompt design and calibration. Furthermore, this approach remains fully compatible with standard fine-tuning methods such as supervised fine-tuning (SFT) and reinforcement learning (RL), allowing seamless use of existing post-training platforms.
Label Probabilities and Calibration
Let's focus on the approach that doesn’t modify the model architecture and instead leverages the vocabulary to represent classes. Once we map each class to a token, the model’s next-token probabilities effectively become class probabilities. But to make those probabilities useful – for ranking, thresholding, or downstream decision logic – they need to be calibrated, meaning they should reflect real-world likelihoods.
Calibration
Let's first formalize the meaning of calibration. For class
c
c
c
, define aggregate calibration as:
where
p
i
,
c
p_{i,c}
p
i
,
c
​
is the predicted probability for class
c
c
c
on example
i
i
i
,
y
i
,
c
∈
{
0
,
1
}
y_{i,c} \in \{0,1\}
y
i
,
c
​
∈
{
0
,
1
}
is the one-hot label, and
N
N
N
is the total number of examples in the evaluation dataset.
•
C
a
l
i
b
(
c
)
≈
1
\mathrm{Calib}(c) \approx 1
Calib
(
c
)
≈
1
: predicted probability mass matches the true frequency (good calibration).
•
C
a
l
i
b
(
c
)
>
1
\mathrm{Calib}(c) > 1
Calib
(
c
)
>
1
: model is over-confident for class
c
c
c
.
•
C
a
l
i
b
(
c
)
<
1
\mathrm{Calib}(c) < 1
Calib
(
c
)
<
1
: model is under-confident.
(You can also monitor standard metrics like ECE or Brier score, but this aggregate ratio is a simple, actionable signal during iteration.)
Getting class probabilities
Suppose each class
c
c
c
is represented by a single token
t
c
t_c
t
c
​
. When the model is prompted so that its next token should be the class token, it produces a log-probability
log
⁡
P
(
t
∣
context
)
\log P(t \mid \text{context})
lo
g
P
(
t
∣
context
)
for every token
t
t
t
in the vocabulary.
In principle, we care only about the probabilities of the class tokens - lets denote these tokes as
C
\mathcal{C}
C
. The challenge is that the softmax normalization spans the entire vocabulary – so probability mass assigned to unrelated tokens can distort the class probabilities. To generate calibrated class probabilities – lets denote them
p
^
c
\hat{p}_c
p
^
​
c
​
, we would need to renormalize them:
In practice, however, this renormalization turns out to be unnecessary once the model is fine-tuned for the classification task. As shown in the Appendix, the fine-tuning objective implicitly rebalances the token probabilities such that
p
^
c
≈
p
c
\hat{p}_c \approx p_c
p
^
​
c
​
≈
p
c
​
. That is, the raw next-token probabilities already behave as calibrated class probabilities, even when the number of classes is tiny relative to the vocabulary size.
Practical Tips
•
Prompting matters
: If the model is not fine-tuned, constrain it to single-token answers via careful prompting (e.g., “Answer with ‘yes’ or ‘no’ only”), and use logit bias or decoding constraints to suppress non-label tokens.
•
Fine-tuning helps
: Once fine-tuned, the model naturally focuses its probability mass on the label tokens – no special inference logic is required.
•
Mind tokenization
: Some tokenizers include a leading space (e.g., " yes" instead of "yes"). Always check which token IDs correspond to your labels before training or evaluation.
Experimental Validation
To verify these ideas empirically, we trained a classification model and tracked both its accuracy and calibration throughout training.
We used the
AG News
dataset, which consists of short news summaries labeled into one of four categories: World, Sports, Business, and Sci/Tech. For the base model, we fine-tuned Qwen3-4B using LoRA, enabling efficient supervised adaptation without modifying the model’s architecture or inference stack. The total cost of the training on this dataset on the Fireworks platform was around $2.
During training, each batch was evaluated on held-out examples: we computed both label accuracy and aggregate calibration before every weight update. This ensured that calibration was measured on unseen data rather than the current mini-batch.
The results confirm the earlier hypothesis: calibration naturally converges toward 1.0 even when we leave the model’s language-modeling head untouched – i.e., without renormalizing class token probabilities. In other words, a standard fine-tuning setup is sufficient to produce well-calibrated class probabilities directly from the model’s native token distribution.
Fig 1: Calibration and accuracy per training batch. The accuracy is defined as the fraction of samples in the current batch that were classified correctly.
Code Example
When categories are mapped to individual tokens, you can obtain their probabilities directly using a standard inference API – no architectural changes required.
While most closed-model providers do not expose token-level probabilities, open-source and developer-oriented platforms such as Fireworks AI make this fully accessible. This allows you to compute calibrated class probabilities exactly as discussed above.
Below is a minimal example showing how to query a model hosted on Fireworks AI and extract the probability assigned to each class token:
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
35
36
37
38
39
40
41
42
43
44
45
46
import
math
import
os
from
openai
import
OpenAI
client
=
OpenAI
(
api_key
=
os
.
getenv
(
"FIREWORKS_API_KEY"
)
,
base_url
=
"https://api.fireworks.ai/inference/v1"
,
)
model
=
"accounts/fireworks/models/deepseek-v3p1-terminus"
categories
=
[
"yes"
,
"no"
]
messages
=
[
{
"role"
:
"system"
,
"content"
:
"You are a helpful assistant."
}
,
{
"role"
:
"user"
,
"content"
:
"Is the sky high? Answer yes or no."
}
,
]
# Get response with logprobs
response
=
client
.
chat
.
completions
.
create
(
model
=
model
,
messages
=
messages
,
logprobs
=
True
)
# Extract matching tokens
matches
=
[
]
for
choice
in
response
.
choices
:
if
choice
.
logprobs
and
choice
.
logprobs
.
content
:
for
idx
,
token_info
in
enumerate
(
choice
.
logprobs
.
content
)
:
if
token_info
.
token
.
lower
(
)
in
categories
:
matches
.
append
(
{
"position"
:
idx
,
"token"
:
token_info
.
token
,
"logprob"
:
token_info
.
logprob
,
}
)
assert
len
(
matches
)
==
1
,
f"Expected 1 category, got
{
len
(
matches
)
}
"
# Print results
for
match
in
matches
:
prob
=
100
*
math
.
exp
(
match
[
"logprob"
]
)
print
(
f"Category '
{
match
[
'token'
]
}
' probability:
{
prob
:
.1f
}
%"
)
"""
Example output:
Category 'Yes' probability: 97.4%
"""
No Fine-Tuning? Use the Embeddings API
If you can’t (or don’t want to) fine-tune a model, you can still get normalized class probabilities from any base model using Fireworks’
/v1/embeddings
endpoint.
Instead of pulling full-vocab logprobs and renormalizing client-side, you:
•
Provide the input text and a small list of label token IDs.
•
Call the embeddings endpoint with return_logits=true and normalize=true.
The server computes logits only for those label tokens and applies a softmax over that subset, returning a probability distribution that sums to 1 over your classes. This lets you reuse the “tokens as labels” idea from this post, but without any fine-tuning or custom inference logic - just a single embeddings API call.
Appendix: Why renormalization is not needed when fine tuning
Let
V
V
V
be the vocabulary,
C
\mathcal{C}
C
be the class tokens. For a specific input
x
x
x
with target label token
c
∈
C
c \in \mathcal{C}
c
∈
C
, the model outputs
z
∈
R
∣
V
∣
z \in \mathbb{R}^{|V|}
z
∈
R
∣
V
∣
and probabilities
p
=
s
o
f
t
m
a
x
(
z
)
p = \mathrm{softmax}(z)
p
=
softmax
(
z
)
.
We analyze the dynamics of the logit gap between the target class
c
c
c
and any non-class token
j
∉
C
j \notin \mathcal{C}
j
∈
/
C
under gradient descent with learning rate
η
\eta
η
. The gradients for the cross-entropy loss imply the following updates:
z
c
t
+
1
=
z
c
t
+
η
(
1
−
p
c
t
)
,
z_c^{t+1} = z_c^{t} + \eta (1 - p_c^{t}),
z
c
t
+
1
​
=
z
c
t
​
+
η
(
1
−
p
c
t
​
)
,
z
j
t
+
1
=
z
j
t
−
η
p
j
t
.
z_j^{t+1} = z_j^{t} - \eta p_j^{t}.
z
j
t
+
1
​
=
z
j
t
​
−
η
p
j
t
​
.
We define the gap
Δ
j
t
=
z
j
t
−
z
c
t
\Delta_j^{t} = z_j^{t} - z_c^{t}
Δ
j
t
​
=
z
j
t
​
−
z
c
t
​
The update rule for this gap is:
Δ
j
t
+
1
=
Δ
j
t
−
η
(
1
+
p
j
t
−
p
c
t
)
.
\Delta_j^{t+1} = \Delta_j^{t} - \eta (1 + p_j^{t} - p_c^{t}).
Δ
j
t
+
1
​
=
Δ
j
t
​
−
η
(
1
+
p
j
t
​
−
p
c
t
​
)
.
Note that
1
−
p
c
t
=
∑
k
≠
c
p
k
t
1 - p_c^{t} = \sum_{k \neq c} p_k^{t}
1
−
p
c
t
​
=
∑
k

=
c
​
p
k
t
​
Since
j
j
j
is one of those non-target tokens, we know that
1
−
p
c
t
≥
p
j
t
1 - p_c^{t} \ge p_j^{t}
1
−
p
c
t
​
≥
p
j
t
​
.
Therefore:
1
+
p
j
t
−
p
c
t
≥
2
p
j
t
.
1 + p_j^{t} - p_c^{t} \ge 2 p_j^{t}.
1
+
p
j
t
​
−
p
c
t
​
≥
2
p
j
t
​
.
This implies that at every step where the model assigns non-zero probability to token
j
j
j
, the gap
Δ
j
t
\Delta_j^{t}
Δ
j
t
​
decreases (becomes more negative) by at least
2
η
p
j
t
.
2 \eta p_j^{t}.
2
η
p
j
t
​
.
p
j
t
=
e
z
j
t
∑
k
e
z
k
t
<
e
z
j
t
e
z
c
t
=
e
Δ
j
t
.
p_j^{t} = \frac{e^{z_j^{t}}}{\sum_{k} e^{z_k^{t}}} < \frac{e^{z_j^{t}}}{e^{z_c^{t}}} = e^{\Delta_j^{t}}.
p
j
t
​
=
∑
k
​
e
z
k
t
​
e
z
j
t
​
​
<
e
z
c
t
​
e
z
j
t
​
​
=
e
Δ
j
t
​
.
As
Δ
j
→
−
∞
\Delta_j \to -\infty
Δ
j
​
→
−
∞
, the probability
p
j
p_j
p
j
​
is forced to
0
0
0
. Consequently, the probability mass concentrates entirely on the class tokens
C
\mathcal{C}
C
, making
∑
c
∈
C
p
c
→
1
\sum_{c \in \mathcal{C}} p_c \to 1
∑
c
∈
C
​
p
c
​
→
1
. Thus, explicit renormalization becomes unnecessary after fine-tuning.
Getting Started
Ready to start training? Our
Supervised Fine-Tuning
and
Reinforcement Fine-Tuning
docs walk you through how to tune base LLMs on your own data, step by step. Prefer video? Check out our
quickstart walkthrough
to see the full training flow in action.
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
