---
title: "Production-Ready Agent Engineering — Bonus Lesson: GRPO Details (Lecture Transcript)"
author: Will Brown
date: 2025-07-03
date_ingested: 2026-06-11
source: https://maven.com/will-brown-kyle-corbitt/agents-mcp-rl
notebook: https://raw.githubusercontent.com/willccbb/agent-engineering/refs/heads/main/lectures-1-through-4/lec5-grpo-details/grpo_details.ipynb
type: transcript
tags:
  - reinforcement-learning
  - grpo
  - ppo
  - agentic-rl
  - ai-agents
  - vllm
  - lora
  - fine-tuning
  - gpu
  - vram
  - ml-infrastructure
  - async-rl
  - off-policy
  - on-policy
  - education
  - transcript
related_article: articles/2025-07-03_willbrown_agents-mcp-rl-lesson5-5.md
participants:
  - Will Brown (instructor)
---

# Production-Ready Agent Engineering — Bonus Lesson: GRPO Details (Lecture Transcript)

**Instructor:** Will Brown (Research Lead, [[entities/prime-intellect]])
**Date:** July 3, 2025
**Companion course:** [[concepts/agents-mcp-rl-course|Production-Ready Agent Engineering: From MCP to RL]]
**Notebook:** [grpo_details.ipynb](https://raw.githubusercontent.com/willccbb/agent-engineering/refs/heads/main/lectures-1-through-4/lec5-grpo-details/grpo_details.ipynb)

---

## 1. RL Infrastructure Ecosystem Survey

**[00:01:13]** This will be less of walking through a specific code example and more of doing a survey of the techniques that people use that are important optimizations for doing GRPO, as well as the infrastructure ecosystem.

### Anyscale and Ray

**[00:02:23]** One blog post that just came out today — an overview of the RL ecosystem from Anyscale. Anyscale is a startup spun out of Berkeley that makes infrastructure for distributed training and machine learning distributed systems. They created Ray, which is an infrastructure layer that is very popular in reinforcement learning, even pre-LLM. People used it with tools like OpenAI Gym and Stable Baselines uses it. It's essentially for orchestrating resources across machines.

**[00:03:26]** As you scale up RL, it's not just one trainer anymore — you have tools, judges, your model doing training, a different version of models doing inference, all these moving parts.

### Verl (formerly OpenRLHF)

**[00:03:56]** Verl is one very popular library for doing scalable RL. Verl is the default choice people use when writing research papers and want to create a framework doing RL with some new algorithm. They start with Verl and fork it. It has all these pre-configurations for doing things at larger scale — if you want to run on 32 or 64 GPUs, Verl is built for that use case.

**[00:04:36]** In my opinion, it is very much overkill for small scales, and it's not very user friendly, but it has all these things that are important as you get up to larger scales.

### PPO vs GRPO: The Critic Model

**[00:06:13]** PPO is kind of the algorithm people were using for RL for a while. The difference between PPO and GRPO/GPO is that PPO has a **critic model**. In the case of GRPO, the critic is replaced by the group. The group is the idea that we are using sampling to do our advantage estimates. PPO has a whole other model that is being trained to be an advantage estimator.

**[00:06:40]** In PPO you have rollouts with final scores, then you have another copy of your initial model where it's trained to predict the value of each token based on being trained on the rollouts with outcome rewards. GRPO is in some sense a simplified approximation of PPO because you don't have to have this whole other model.

**[00:07:18]** Having a whole other model massively increases your memory requirements for inference. One thing that catches people off guard: the multiplier from model size to memory needed to train it is typically at least 10x.

---

## 2. VRAM Napkin Math

**[00:07:47]** Let's say we have a 7B model:

| Component | Calculation | Memory |
|-----------|-------------|--------|
| Model weights (bfloat16) | 7B × 2 bytes | 14 GB |
| AdamW optimizer (fp32) | 2 momentum vectors × 4 bytes each = 8 bytes/param | 56 GB |
| Gradients | Same size as model (fp32) | 28 GB |
| Activations (varies) | Depends on context length / batch size | ~14+ GB |
| **Total rule of thumb** | **~10× model size** | **~70+ GB** |

**[00:08:07]** bfloat16 is the type people typically use. There's fp32, fp8. The ecosystem for fp8 tooling right now is still early — I would not recommend people try to do fp8 unless you're using something pre-built off the shelf like Unsloth, which handles a lot of the hard parts of bit-level optimization. I would not expect it to just plug-and-play work if you're writing your own code.

### The AdamW Optimizer

**[00:09:37]** Adam maintains 2 running averages of gradients — one is momentum (first moment), one is second-order momentum (second moment). People use AdamW as the default optimizer. When people talk about "stochastic gradient descent," what they really mean usually is AdamW.

**[00:11:24]** The way I like to think about momentum: you don't want your gradient to just be the last sample. You want to still remember some things about the direction you're moving. The goal of optimization is not to memorize — it's to learn the underlying distribution. Every gradient for one sample is just "what direction makes me do better on this one sample." What we really care about is what directions are good for every sample, things that are general.

**[00:12:19]** These momentum vectors store the good parts of past data. We have 2 different vectors: one is normal momentum, one has nonlinearity for scaling properties — it should emphasize shared components more and be less sensitive to task-specific pieces.

**[00:13:19]** Models at inference time are fine with more quantization, but gradients get messy when you quantize them — training can blow up more easily. People do this in fp32 by default.

### LoRA: The Memory Workaround

**[00:15:10]** LoRA — the idea is you don't tune all parameters. Every weight matrix becomes a smaller dimension matrix, training in the smaller dimension, then projecting back up. Total parameters can be 100× lower or more.

**[00:16:16]** In Verifiers, I have a default LoRA config: r=16, alpha=32 (typically alpha should be 2-4× r). This is much more memory efficient. For getting started especially, it helps with stability.

**[00:16:33]** Rule of thumb: if you're doing fine-tuning for one task and the model is already okay at the task, definitely do your experimentation with LoRA. You can get rid of it when you want to scale up.

**[00:17:14]** For this tiny LoRA setup, the GPU setup will typically be 2× L4 or 2× A10. These are nice and cheap. One for inference, one for training is how Verifiers is set up. For ART (which Kyle has been working on), you can do it all in one GPU.

---

## 3. Inference + Training Architecture Patterns

**[00:18:00]** There are a couple of considerations for how you architect your RL system.

### Pattern A: GPU Swapping (ART-style)

**[00:18:22]** ART looks more like this — you swap whether you're in inference mode or training mode on the same GPUs. You do inference, then switch to training mode. You drop the inference model weights from your inference copy and move them into your training copy — same model, not duplicating weights in memory, just changing modes.

**[00:19:16]** The LLM is really optimized for inference but not set up for training. Under the hood it's a vLLM server, and we're adding endpoints to update parameters — a trainer can send a request to update a tensor, and the inference worker hot-swaps it.

### Pattern B: Overlapping Inference + Training (Verifiers-style)

**[00:19:44]** You have designated GPUs for inference and training. Initially just inference, then for subsequent steps: on some GPUs we're training on old batches from the last inference step, while in parallel doing more inference for the next step. This cascade keeps all GPUs working all the time with some bubbles.

### LoRA-Specific Optimization

**[00:23:34]** If you're only using LoRA, the update step is much easier — LoRAs are so small you can just write them to disk. vLLM has a first-class API for hot-swapping LoRA directly without needing to reach in and change anything.

**[00:24:02]** Designing systems depends on scale: do you need full parameter fine-tuning or is LoRA enough? Multi-node or single/few GPUs? Large models? Total efficiency vs user experience? Having a setup comfortable for trial and error is key.

**[00:25:06]** For the 2-GPU scale, debugging your code, doing test runs, watching curves, trying new environments, fiddling with reward functions — you're spending less than a dollar an hour. You can get a lot of GPU time out of $100 of credits.

**[00:25:41]** What I would caution against is jumping to the big machines until you feel like you know what you're doing. If you got something working really well on a 1B model and want to see how it does for a bigger model — that's a good time.

---

## 4. Async RL: Two Meanings

**[00:36:54]** "Async" is becoming an overloaded term in RL.

### Off-Policy (Stale Rollouts)

**[00:37:00]** Off-policy means the inference is coming from an older copy of the model. We're training on rollouts from step 1 to 8, but those rollouts came from one step earlier. This delay exists so we can overlap — inference generates more completions while training on old ones.

### Async Inference (Multi-Turn)

**[00:37:49]** For multi-turn agent inference, we want each rollout to be isolated. Each rollout is a while loop: get response from model, do tool calls if needed, get environment responses. Each request doesn't need to think about scheduling or batching or coordination with other rollouts because all of that is inside the LLM server.

**[00:39:47]** vLLM does micro token-level batching dynamically — it adjusts batch size as a function of how many active prompts there are whose generations are being processed. You just treat it like an OpenAI endpoint: send stuff, it sends it back when done, handles all batching for you.

---

## 5. GRPO Parameters and Gotchas

**[00:52:44]** If you're optimizing for memory efficiency and your model is already okay at a task, some simplifications:

### Beta = 0 with LoRA (No Reference Model)

**[00:52:47]** You can use LoRA and not use a reference model at all (beta = 0). There's been lots of papers saying you need it, lots saying you don't. If you want to pick a case where you can safely remove it: when you're also doing LoRA, because LoRA already acts as a constraint on how much your model can go off the rails.

**[00:54:05]** The reference model also has to be in memory — another source of memory usage. In the case of LoRA, the model without the LoRA is essentially the reference model — you kind of get it for free.

### On-Policy vs Off-Policy Spectrum

**[01:09:13]** Experiment with different degrees of delay: the longer delay you have, the more forgiving it is. At extreme delay, you collapse into fully offline RL (DPO), where your ability to do exploration and learn from it is diminished. There's probably a sweet spot that depends on the task.

**[01:11:22]** For this overlapping to work, you have to do at least one step off-async. I do it by default in Verifiers and it tends to be just fine. Whether you could do 10 steps async is an open question.

**[01:11:48]** No one knows for sure how they are training models like Deep Research. One thing that's a good exercise: look at products or behaviors from big lab models, try to think "what sort of training behavior would have made that possible?" For Deep Research — rollouts can take 20 minutes, and you need to do lots of steps. That run is going to take a while.

### Multi-Turn Think Token Removal

**[01:14:42]** One blog post explores multi-turn training where the model needs to do multiple steps, thinking in each step, but without thinking tokens blowing up context. They want the model to think and then throw away the thinking for the next step. You can't do this with normal GRPO without changing the algorithm — they modify it. Each next step becomes a new prompt because they rewrite history to throw away thinking tokens.

### VinePPO: Explicit Tree Search

**[01:06:24]** VinePPO explicitly does tree search: do a couple of rollouts, have some prefix of states, do more sampling from each, see which is better on average. You get intermediate estimates — you can pinpoint where the difference is coming from. This **credit assignment** problem — deciding which actions deserve credit for which parts of the rollout — is tricky. PPO's critic model does token-level estimation for this.

### REINFORCE and Batch-Based Approaches

**[01:16:14]** REINFORCE is a very simple policy gradient algorithm that people are revisiting. Rather than explicit grouping, you just throw all states/results/rewards into a big batch. If people can get this to work at scale, it simplifies the multi-turn process quite a bit.

---

## 6. RL Ecosystem: Services and Skepticism

**[00:50:57]** A lot of RL-as-a-service startups are a UI around TRL GRPO or something similar. Be skeptical of services that promise a lot without showing what they're doing.

**[00:56:10]** Companies I'd trust: OpenPipe (code is public, blog posts showing their whole experience), Bespoke Labs (partner directly, walk you through the process), OpenAI RFT, Databricks (strong RL people). If a company hasn't released any outputs of their systems and just joined YC — be skeptical.

**[00:59:58]** Some services charge $10/hour for a GPU — that's way too much. Market rates: H200 ~$3/hour, H100 $1-2/hour. H100 will trend toward $1/hour. Know what GPUs cost.

**[01:02:30]** OpenAI's RFT is probably the most user-friendly and has the best hyperparameters pre-configured. It still won't be perfect — still takes iteration, trial and error.

### GRPO Is Not the Endgame

**[01:02:47]** PPO is not dead. People moved away from it largely because DeepSeek used GRPO and was really impressive. GRPO allows experimentation at smaller scales and democratized it. But the goal of all these algorithms is **advantage estimation** — measuring the value of a stage. There's a large design space of different bells and whistles, different knobs.

---

## 7. RL for Non-Verifiable Domains

**[01:25:26]** The real question is: can you evaluate it? If you can do evaluation for non-verifiable tasks, you can do RL pretty reliably. But that requires creating a system that evaluates things consistently with human judgments.

**[01:26:06]** One approach: use LMs to judge, do tournament-style comparisons between outputs, use Elo scoring. This paper from the Qwen team applies this to creative writing with good results.

**[01:27:48]** I would imagine scaling RL for non-verifiable domains will look like figuring out how to create good evaluation systems using LMs as part of the evaluation loop, ideally also part of the task generation loop.

---

## 8. Test-Time Training

**[01:29:11]** A really cool direction: **test-time training** — the model generates something, then trains on it after generating. It's learning a representation of the thing at inference time.

**[01:31:44]** One way: synthetically generate questions about a document, train a LoRA using these Q&A pairs — all at inference time. Training a LoRA on a few hundred examples is really fast (few minutes). If people are willing to wait 10+ minutes for Deep Research results, test-time training might make sense.

**[01:33:33]** In-context learning is like skimming — you get a retrieval-surface-level understanding, not deep thinking about interplays between concepts. Training is one way of having richer, deeper representations folded back into the model.

---

## 9. Recommended Resources

**[01:21:11]** Best way to keep up: follow certain accounts on X, or read Nathan's blog (Interconnects) for weekly coverage.

| Resource | Description |
|----------|-------------|
| [Anyscale RL ecosystem blog](https://www.anyscale.com/blog/open-source-rl-libraries-for-llms) | Overview of RL infrastructure landscape |
| [Nathan Lambert — Interconnects](https://www.interconnects.ai/) | Weekly RL/AI news digest, RLHF book |
| [Dylan Patel — Semi Analysis](https://semianalysis.com/) | GPU supply chain + big lab RL strategies |
| [@gm8xx8](https://x.com/gm8xx8) | Paper curator — filters notable papers |
| ML Street Talk podcast | Deep technical interviews |
| Dorkish podcast | AI/ML commentary |

---

## Related

- [[concepts/agents-mcp-rl-course|Production-Ready Agent Engineering: From MCP to RL]]
- [[raw/articles/2025-07-03_willbrown_agents-mcp-rl-lesson5-5]]
- [[concepts/grpo-rl-training]]
- [[concepts/agentic-rl]]
- [[entities/will-brown]]
- [[entities/prime-intellect]]
