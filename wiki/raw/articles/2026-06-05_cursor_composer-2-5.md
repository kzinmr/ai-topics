---
title: "Introducing Composer 2.5 · Cursor"
source: "Cursor Blog"
url: "https://cursor.com/blog/composer-2-5"
scraped: "2026-06-05T06:00:41.761790+00:00"
lastmod: "2026-06-05T05:23:59.758Z"
type: "sitemap"
---

# Introducing Composer 2.5 · Cursor

**Source**: [https://cursor.com/blog/composer-2-5](https://cursor.com/blog/composer-2-5)

Blog
/
research
May 18, 2026
·
research
Introducing Composer 2.5
7 min read
Table of Contents
↑
Training Composer 2.5
Targeted RL with textual feedback
Synthetic data
Sharded Muon and dual mesh HSDP
Try Composer 2.5
Composer 2.5 is now available in Cursor.
It's a substantial improvement in intelligence and behavior over
Composer 2
. It is better at sustained work on long-running tasks, follows complex instructions more reliably, and is more pleasant to collaborate with.
We improved Composer by scaling training, generating more complex RL environments, and introducing new learning methods.
In addition to training Composer 2.5 on more difficult tasks, we improved behavioral aspects of the model like communication style and effort calibration. These dimensions are not well captured by existing benchmarks, but we find that they matter for real-world usefulness.
Composer 2.5 is built on the same open-source checkpoint as Composer 2,
Moonshot's Kimi K2.5
.
Together
with SpaceXAI
, we're training a significantly larger model from scratch, using 10x more total compute. With Colossus 2's million H100-equivalents and our combined data and training techniques, we expect this to be a major leap in model capability.
#
Training Composer 2.5
Composer 2.5 contains several new improvements to our training stack. These changes target both model intelligence and usability.
#
Targeted RL with textual feedback
Credit assignment during RL is becoming an increasingly difficult challenge as rollouts can span hundreds of thousands of tokens. When a reward is computed over an entire rollout, it may be hard for the model to tell which specific decision helped or hurt the outcome. This is especially limiting when we want to discourage a localized behavior, such as a bad tool call, a confusing explanation, or a style violation. The final reward can tell us that something went wrong, but it is a noisy signal for
where
it went wrong.
To address this, we trained Composer 2.5 with targeted textual feedback.
1
The idea is to provide feedback directly at the point in the trajectory where the model could have behaved better. For a target model message, we construct a short hint describing the desired improvement, insert that hint into the local context, and use the resulting model distribution as a teacher. We use the policy with the original context as the student and add an on-policy distillation KL loss that moves the student's token probabilities toward the teacher's. This gives us a localized training signal for the behavior we want to change, while still retaining the broader RL objective over the full trajectory.
As an illustration of the text feedback process, consider a long rollout that includes a tool call error where the model attempts to call a tool that is not available. During the rollout, the model will receive a “Tool not found” error and continue making additional valid tool calls. The fact that it hit one error in the process of hundreds of tool calls will have a minimal impact on its final reward.
With text feedback, we can target this specific mistake by inserting a hint in the context of the problematic turn, such as “Reminder: Available tools…” with a list of available tools. This hint changes the probabilities for the teacher, lowering those for the wrong tool and increasing those for a valid replacement. For that turn only, we then update the student weights towards to the new probabilities.
During the Composer 2.5 run, we applied this method to a variety of model behaviors, from coding style to model communication.
#
Synthetic data
During RL training, Composer's coding ability improves substantially to the point where it begins to get most training problems correct. To continue increasing intelligence, we both select for and create harder tasks dynamically throughout the run. Composer 2.5 is trained with 25x more synthetic tasks than Composer 2.
We use a range of approaches for creating synthetic tasks that are grounded in real codebases. For example, one synthetic approach is feature deletion. For these tasks the agent is given a codebase with a large set of tests, and asked to delete code and files in such a way that the codebase remains functional while specific testable features are removed. The synthetic task is to reimplement the feature, and the tests are used as a verifiable reward.
One downstream consequence of large scale synthetic task creation is that it can cause  unexpected reward hacking. As the model became more adept, Composer 2.5 was able to find increasingly sophisticated workarounds to solve the task at hand. In one example, the model found a leftover Python type-checking cache and reverse-engineered the format to find a deleted function signature. In another, it was able to find and decompile Java bytecode to reconstruct a third-party API. We were able to find and diagnose these problems using agentic monitoring tools, but they demonstrate the increasing care necessary for large scale RL.
#
Sharded Muon and dual mesh HSDP
For continued pretraining, we use Muon with distributed orthogonalization. After forming the momentum update, we run Newton-Schulz at the model's natural granularity: per attention head for attention projections, and per expert for stacked MoE weights.
The main cost is orthogonalizing expert weights. For sharded parameters, we batch same-shaped tensors, all-to-all shards into complete matrices, run Newton-Schulz, then all-to-all the result back to the original sharded layout. These transfers are asynchronous: while one task is waiting on communication, the optimizer runtime advances other Muon tasks, overlapping network and compute. This is equivalent to full-matrix Muon, but keeps the shard group busy; on the 1T model, optimizer step time is 0.2s.
This interacts closely with how we use HSDP for MoE models. HSDP forms multiple FSDP replicas and all-reduces gradients across corresponding shards. We use separate HSDP layouts for non-expert and expert weights: non-expert weights are comparatively small, so their FSDP groups can stay narrow, often within a node or rack, while expert weights hold most of the parameters and most of the Muon compute, so they use a wider expert sharding mesh.
Keeping these layouts separate also lets independent parallelism dimensions overlap: CP=2 and EP=8 can run on 8 GPUs instead of requiring 16 in a single shared mesh. This avoids wide communication for small non-expert state while spreading expert optimizer work over many GPUs.
#
Try Composer 2.5
Composer 2.5 is priced at $0.50/M input and $2.50/M output tokens.
There's also a
faster variant with the same intelligence
at $3.00/M input and $15.00/M output tokens, a lower cost than the fast tiers of other frontier models. Similar to Composer 2, fast is the default option. See our
model docs
for full details.
Composer 2.5 includes double usage for the first week.
For more background on this approach see
Self-Distillation Enables Continual Learning
,
Reinforcement Learning via Self-Distillation
, and
Self-Distilled Reasoner: On-Policy Self-Distillation for Large Language Models
.
↩
Filed under:
research
Author
:
Cursor Team
