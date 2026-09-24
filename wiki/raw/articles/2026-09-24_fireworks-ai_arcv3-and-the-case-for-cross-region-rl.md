---
title: "Every byte counts: ARCv3 and the case for cross-region RL"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/arcv3-and-the-case-for-cross-region-rl"
scraped: "2026-09-24T06:00:18.575546+00:00"
lastmod: "2026-09-23T17:37:20.000Z"
type: "sitemap"
---

# Every byte counts: ARCv3 and the case for cross-region RL

**Source**: [https://fireworks.ai/blog/arcv3-and-the-case-for-cross-region-rl](https://fireworks.ai/blog/arcv3-and-the-case-for-cross-region-rl)

Join us for our inaugural conference, Forge 2026
Product
Solutions
Models
Pricing
Resources
Log In
Get Started
Blog
Arcv3 And The Case For Cross Region Rl
Every byte counts: ARCv3 and the case for cross-region RL
PUBLISHED
9/23/2026
Table of Contents
TL;DR
Inside ARCv3: Not all updates are created equal
How ARCv3 compares to the field
Using ARCv3
Making distributed compute work for RL
Table of Contents
Table of Contents
TL;DR
Inside ARCv3: Not all updates are created equal
How ARCv3 compares to the field
Using ARCv3
Making distributed compute work for RL
Table of Contents
TL;DR
•
Fireworks' new ARCv3 compressor reduces the size of BF16 weight updates sent from the trainer to the machines generating reinforcement learning (RL) rollouts.
•
Across 1,000 production RL weight-update deltas, ARCv3 produced payloads nearly 50% smaller than ARCv2, with lossless reconstruction of the trainer's exact BF16 weights.
•
Smaller transfers help rollout fleets stay closer to the current policy, making it more practical to use compute across regions without one giant co-located cluster.
•
ARCv3 is available in the
Fireworks Training API
through
fireworks-delta-compression
for teams using their own trainer with Fireworks rollouts.
As more teams push into reinforcement learning to train their own frontier-scale models, two things matter more than ever: getting access to training compute, and optimizing the pipes that move data between the machines doing that training. RL is uniquely demanding on those pipes. A frontier model can have trillions of parameters, and the trainer needs to keep pushing updated versions of it out to a fleet of machines generating rollouts, continuously, as training progresses.
When those pipes can't keep up, teams get pushed toward a single option: one massive co-located cluster with everything wired together on the same physical floor. That's expensive, hard to get, and locks smaller players out. At Fireworks, we take every available path to keep that from being the only option. Otherwise, we end up with a training market only a handful of companies can enter.
In a previous post,
Frontier RL is cheaper than you think
, we walked through how we make cross-region RL work in practice. The core observation is that, in the RL workloads we examined, only about 2% of the model's BF16 weights changed between consecutive checkpoints. So instead of shipping the full 1 TB checkpoint to every rollout machine every time the trainer takes a step, we ship a compact delta, a compressed description of what changed, and reconstruct the updated model on the other end. That's what keeps a training run in sync across three or four regions without a dedicated high-bandwidth network between the clusters.
The size of that delta helps determine how well this works in practice. Smaller deltas help the rollout fleet update faster, stay closer to the current policy, and pull from available compute across regions. Bigger deltas can mean the trainer starts to outrun the rollouts, the fleet drifts out of date, and the multi-region setup starts to lose its edge over a single mega-cluster.
How ARCv3 deltas move from trainer to rollouts.
Each trainer shard uploads its slice of the compressed weight delta to shared object storage (S3) in parallel. Then, the Fireworks API signals every region that a new update is available, and each rollout region pulls the pieces it needs and reconstructs the updated model locally. The trainer never talks directly to the rollout fleet, which is what lets a globally distributed inference cluster stay in sync over ordinary network links.
We’re releasing ARCv3, the newest version of the compressor we use to build those deltas. These improvements apply to BF16 weights, where ARCv3 produces nearly half the payload size of the previous version, an average delta payload of around 0.19% of the original BF16 weight size, down from 0.36% (lower is better). The compression is lossless: the reconstructed model on the rollout side is bit-for-bit identical to what the trainer produced. ARCv3 is available in the Fireworks Training API through
fireworks-delta-compression
for teams using their own trainer with Fireworks rollouts.
Inside ARCv3: Not all updates are created equal
The improvement comes from a specific property of how BF16 weights change between training steps.
When we ran production RL training sessions and looked at what actually happens between checkpoints, we observed a strong asymmetry. Of the roughly 2% of BF16 weights that changed on a given step, the overwhelming majority saw only a mantissa shift, while the exponent and sign stayed put. Updates that touch the exponent are rare, and updates that flip the sign are rarer still. In other words, most weight updates are nudges, not jumps.
ARCv3 encodes that asymmetry directly. Unchanged weight values are omitted from the payload. Mantissa-only changes contribute just their mantissa bits. The rarer updates, where the exponent shifts or the sign flips, get packed separately, with each update's changed fields encoded together as a single block. On the rollout side, both streams are applied to the previous checkpoint, and the result is checksummed against the trainer's original to verify that the reconstruction matches.
How ARCv3 encodes a block of weights.
Each prev/next pair is XORed and classified by which fields actually changed. Unchanged weight values (zero XOR) are omitted from the output. Mantissa-only changes, the common case, contribute just their mantissa bits (highlighted). Rarer updates, where the exponent shifts or the sign flips, are packed together with the changed fields encoded as one block. The output stream is shaped by what changed, not by the fixed width of the input format.
For each tensor in the model, ARCv3 also runs several general-purpose compression algorithms in parallel and keeps whichever produces the smallest output. This costs more CPU than picking a single algorithm up front, but trainer machines usually have spare CPU cycles while the GPUs are doing the actual training, so it's worth spending them.
How ARCv3 compares to the field
We benchmarked ARCv3 against three alternatives on 1,000 real weight-update deltas drawn from production RL workloads. All updates were in BF16, and all four compressors ran losslessly, so what we compared was pure payload size: how many bytes each compressor needed to describe the exact same weight update.
The alternatives to ARCv3 were:
•
ARCv2
, the previous version of our own compressor.
•
PULSESync
, the weight-synchronization algorithm from
Understanding and Exploiting Weight Update Sparsity for Communication-Efficient Distributed RL
(Miahi & Belilovsky, 2026). PULSESync also exploits sparsity in BF16 weight updates using a sparse-patch design.
•
The
delta-compression implementation in Hugging Face TRL
.
Compressor
Compressed / original BF16 weight ratio
Compressor
Compressed / original BF16 weight ratio
ARCv3
0.19%
PULSESync
0.35%
ARCv2
0.36%
HF TRL (draft)
0.67%
Lower is better here, and ARCv3 produces the smallest payloads in this benchmark. On the BF16 weight tensors tested, ARCv3 shrinks the compressed delta to roughly half the size of the next-best approach. Every rollout region pulls the delta pieces it needs and reconstructs the trainer's exact BF16 weights. That helps keep a globally distributed rollout fleet closer to the current policy, which is what makes cross-region RL work at scale.
Using ARCv3
If you use the Fireworks Trainer SDK for rollouts, there's nothing to do, because ARCv3 is already the default. Your rollout fleets are getting smaller transfers with no code changes on your end.
If you're bringing your own trainer and using Fireworks for rollouts, you can integrate ARCv3 directly through the
fireworks-delta-compression
package. See the
Fireworks rollouts documentation
for the full integration flow.
bash
Copy
1
pip install fireworks-delta-compression
python
Copy
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
import
torch
from
fireworks_delta_compression
import
delta_compress
,
delta_decompress
src
=
torch
.
randn
(
1024
,
1024
,
dtype
=
torch
.
bfloat16
)
dst
=
src
+
1e-3
*
torch
.
randn_like
(
src
)
compressed_diff
,
checksum
=
delta_compress
(
src
=
src
,
dst
=
dst
,
compression_format
=
"arc_v3"
,
)
restored
=
delta_decompress
(
src
=
src
,
compressed_diff
=
compressed_diff
,
checksum
=
checksum
,
compression_format
=
"arc_v3"
,
)
# bit-for-bit identical to the original
assert
torch
.
equal
(
restored
.
view
(
torch
.
uint8
)
,
dst
.
view
(
torch
.
uint8
)
)
Making distributed compute work for RL
RL weight updates have structure, and the compressor can take advantage of it. Separating rare exponent changes from common mantissa updates, and racing a handful of general-purpose codecs on top, buys us nearly twice the compression of our own previous version for the relatively low cost of extra CPU on machines that already have some to spare.
We push on this because every byte we shave off the delta is a byte that doesn't have to travel between continents on a training step. That brings us closer to making training across three or four regional clusters feel like training in a single building. It helps more teams compete on ideas rather than on how much co-located compute they were able to buy.
For teams building specialized models, the payoff is more flexibility in how they scale RL. Fireworks handles weight distribution and synchronization across rollout regions.
ARCv3 is where we are right now. We’ll keep pushing.
Bring your trainer to Fireworks.
Related Posts
Company News
9/22/2026
Introducing The Specialized Intelligence Index
Company News
8/31/2026
Train past the frontier: Training API now generally available
Company News
7/15/2026
Announcing our Series D and $1B ARR
Next
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
