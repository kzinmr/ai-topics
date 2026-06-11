---
title: "Production-Ready Agent Engineering — Office Hours (Week 3) (Lecture Transcript)"
author: Will Brown
date: 2025-07-03
date_ingested: 2026-06-11
source: https://maven.com/will-brown-kyle-corbitt/agents-mcp-rl
type: transcript
tags:
  - ai-agents
  - dspy
  - reinforcement-learning
  - grpo
  - agent-framework
  - multimodal
  - fine-tuning
  - structured-outputs
  - education
  - transcript
related_article: articles/2025-07-03_willbrown_agents-mcp-rl-office-hours-week3.md
participants:
  - Will Brown (instructor)
  - Nick Gideo (student)
  - Raymond Weitekamp (student)
  - Phlo (student)
  - Michael McCall (student)
---

# Production-Ready Agent Engineering — Office Hours (Week 3) (Lecture Transcript)

**Instructor:** Will Brown (Research Lead, [[entities/prime-intellect]])
**Date:** July 3, 2025
**Companion course:** [[concepts/agents-mcp-rl-course|Production-Ready Agent Engineering: From MCP to RL]]

---

## 1. DSPy Deep Dive

**[00:06:02]** Back in Lecture 1, we were going over all the different ways you can implement standard agent frameworks. DSPy has a native agent tool-use setup — their version of an agent is called ReAct.

### Modules as Building Blocks

**[00:08:09]** In DSPy, all components are called **modules**. Modules are composable pieces of programs — you can think of them as having some input spec and some output spec, some plumbing. Predict is a simple classification output, Chain of Thought does different things in different cases to get the model to reason. It does a lot of optimization for you — for example, for a given model, what is the right type of chain of thought?

**[00:10:02]** If you're familiar with PyTorch or neural net libraries, DSPy modules are structured similarly to the idea of a directed acyclic graph. This is a pipeline of modules where things go in, they have different dependencies, and data flows from one direction to the next as long as the outputs of one match the inputs of the next.

### Signatures

**[00:11:35]** The thing you need to do to declare any module initially is give it a **signature**, which is this arrow notation: `question, answer -> output`. This is interpreted by DSPy as the spec of the program. You could have a predict program that's just this, you could have a react program that's just this. The magic is that this thing will have an answer type — when you call it with a question input, the production output is going to have an answer field.

**[00:14:17]** This is just a way of structuring your program where the way we're thinking about it is not in terms of prompts — we're thinking about it in terms of **data flow**.

### DSPy vs LangGraph

**[00:14:35]** If you really like this modular compositional way of writing LM programs, LangGraph might be an alternative. It's not focused on optimization but much more focused on enterprise readiness, deployment, and logging. DSPy is less targeted at connecting to your auth and all your other systems, whereas LangGraph is LangChain's protocol for building scalable, reliable systems.

**[00:16:01]** There's a lot of little modules inside LangChain and LangGraph that are convenient — for example, converting a function to a tool without having to write the OpenAI tool call spec from scratch. If you want one set of tools that's got all the building blocks in one place and you don't want to shop around for database connectors, LangChain is probably the most deployment-ready version of that.

### Optimizers: The Magic of DSPy

**[00:17:16]** Once you have a program written as a DAG, you can **optimize** the whole thing. The primitive of DSPy is that once you have a module and an optimizer, the module works for the optimizer — it's very modular and mix-and-match compatible.

**[00:17:55]** Some optimizers work with few-shot examples and a metric (which is essentially a reward function / eval). If you have 30 labeled examples and want to do few-shot prompting but want to know which examples are most instructive for the LLM, DSPy can do this automatically. You can also generate examples on the fly — synthetically generate input examples pre-formatted to your schema, filter out bad ones.

**[00:19:06]** The fanciest optimizer people use the most: **jointly optimizing few-shot examples and your prompt**. This is what people mean when they say "DSPy is for automatic prompt optimization." You give the schema of your problem to an LLM, have it generate candidate instructions based on some meta-prompt, evaluate them, and keep turning the crank.

**[00:20:06]** You can think of this whole process as **compilation** — just like a compiler in PyTorch tries to find a version of a program that is both correct and efficient, DSPy finds the prompts and examples that produce the best output.

### DSPy + GRPO

**[00:21:14]** DSPy does have GRPO integrated — it's still early but it works. It's pretty similar to Verifiers' optimizer as well as TRL, just translated to the DSPy framework. Now instead of optimizing the prompt, you're optimizing the whole program — typically a multi-hop tool use react pattern.

**[00:22:21]** If you wanted to quickly switch between GRPO and prompt tuning without rewriting your code, this would be a way of doing it. Verifiers does not natively support prompt optimization, but I'm planning on introducing some things along those lines.

---

## 2. Multimodal RL and Fine-Tuning

**[00:23:44]** Raymond asks about multimodal — images in the task, SimBA doesn't work with images right now.

**[00:24:55]** Potentially the answer would be different for multimodal, but the easiest workaround is **thinking of multimodality as tool use**. If you need to deal with lots of images, have a frozen multimodal model (Moondream, GPT-4o Mini) whose only job is image→text conversion according to some prompt. The agent doesn't need to see every image — it gets what it needs in text.

**[00:26:08]** The short-term workaround while people catch up is offloading image processing to tools.

### Visual Reasoning and Fine-Tuning

**[00:26:34]** Raymond's real interest: 3D CAD modeling with AI — visual reasoning capabilities are horrible. VLMs are blind — they can't tell if 2 lines intersect. The image has to be in the context for fine-tuning; there's no way to offload it.

**[00:27:38]** Normal fine-tuning is definitely easier to get started with for multimodal. For RL, it's not user friendly yet — you'll have to fork the repo and change a couple of things. People have done it: someone forked Verifiers and made a multimodal version (PR under review). Zihan Wang from Northwestern has done VLM agent work built on top of Verl.

**[00:29:37]** Multimodal support is coming soon to Verifiers — there's a PR open with initial support. Hopefully within the next couple of weeks it'll be much more easy to use.

### Audio Modality

**[00:30:45]** A good friend spent quite a while trying to get RL for audio working and found it very painful. The ecosystem for the Qwen 7B audio model is very underdeveloped, lagging even further behind images. For pure image/audio models, I don't know of anything really good and usable for RL.

**[00:31:44]** For integration to a larger system: speech-to-text and text-to-speech should be reasonably solvable problems. Once they are, you don't have to have your reasoning be in the same model. Having the intelligence exist in language, then thinking of speech/text as UI rather than the logic itself — that's how I tend to think about it.

---

## 3. SkyPilot for GPU Workflows

**[00:35:41]** SkyPilot is an all-in-one platform — you can think of it like Slurm but it uses whatever cloud resources you have. You give it your cloud API credentials so it can provision on your behalf. It's a nice CLI for running training jobs, creating and destroying clusters with auto-stop.

**[00:37:29]** Prime Intellect acts as an aggregator for lots of clouds — Lambda, RunPod, HyperStack, etc. — through one platform with credits in one account. SkyPilot lets you use your credits on GPUs from any of these places.

**[00:38:54]** My typical workflow: a small always-on machine with 2 smaller GPUs for debugging, then spin up larger nodes for big runs once the code is tested. Setup script gets environment files right, run the thing, kill it when done.

---

## 4. Think Tags and Structured Output

**[00:40:22]** For think tags: checking for think/end_think tokens, parsing the answer as everything after the last end_think. This is the Verifiers version. I tend to think it's easier to do at this level versus relying on flags in your vLLM instance.

**[00:41:45]** For XML tags inside tool calls: I typically assume tool calls are everything inside a top-level XML object. This parser doesn't solve every version of nested complex XML — you could use Beautiful Soup for production-grade hierarchical parsing.

**[00:42:32]** For regex-based structured generation: if you freeze the exact format you want and write it as a regular expression, you can use regex in structured generation to enforce output follows a certain schema. Going from one schema to a few options, regex is pretty good. Going the other direction (arbitrary schemas → avoiding edge cases) gets complex.

---

## 5. Reward Curve Oscillation

**[00:44:49]** If the reward curve is going up and down, this usually means you're learning too fast or your batch size isn't big enough. The cheapest way to increase batch size is **gradient accumulation** — doing a bunch of batches in a row and aggregating them. No extra memory needed, just slower.

### Reward Diversity

**[00:45:36]** What you really want in a batch: both within each prompt and across prompts, good **diversity of difficulty**. If a model always gets the max reward for a question, that's tricky. Increasing generations per prompt increases odds of good diversity.

**[00:46:09]** With 4 generations per prompt and yes/no rewards, you have to hope the model gets it right 1, 2, or 3 times (not 0 or 4). Smaller batch size → narrower range of difficulty that can be accommodated.

**[00:47:22]** Initial filtering step: run an eval where you sample the model on prompts and throw away tasks where it gets it right all the time or none of the time. Now you know this set of tasks is essentially the right level of difficulty.

### Prompt Reuse in GRPO

**[00:48:00]** For GRPO, it's totally fine to do many steps reusing prompts — one blog post used only 100-200 total prompts repeated many times across 100 epochs and still learned. You don't need tons of unique prompts; what matters is a good diverse set at the right difficulty level.

### Dynamic Resampling

**[00:50:11]** Something people will be doing more: keep sampling until you have a guarantee that some completions are better than others. This is where the signal in RL comes from — there is some response better than another, and the model learns from the differences.

---

## 6. Experimentation Scale

**[00:52:14]** RL is not yet at the point where there's a unified recipe that always works. Defaults in Verifiers are stable for 7-14B models, <10 turns, <8K total rollout size.

**[00:53:02]** For 1B models: SFT warmup becomes much more important, as well as picking easier tasks. Nothing wrong with picking tasks that are contrived or trivial for a big model but hard for a small model.

**[00:53:34]** Big AI labs don't run experiments on the whole cluster — lots of experimentation at smaller scales, then see scaling laws as you go bigger.

---

## 7. Environment Ideas for RL

**[00:54:07]** Text Arena: great library, just released a first-class RL framework for multi-agent settings. Games like number guessing, rock-paper-scissors, logic puzzles.

**[00:55:01]** Good proof of concept: have a bigger frozen model (API) playing a game against a small model you're training. Can you train the small model to beat the bigger model?

**[00:56:12]** Search tasks and tool use: any set of documents can be turned into an environment. Generate synthetic questions by giving a random document to an LM and asking it to generate questions. Build search tools for exploring documents, train the agent to get questions right.

**[00:58:17]** Interactive code execution: giving a model the ability to write code as a calculator to solve math questions (from MATH benchmark). The model goes in a loop — look at question, think, write code, see output, use that to inform calculations.

### Data Generation Costs

**[00:59:13]** The bottleneck is almost always RL compute, not data generation. With DeepSeek, generating thousands of completions costs a couple of dollars. Rule of thumb: DeepSeek price per 1M tokens is less than a dollar, so thousands of examples for a few dollars.

**[01:00:33]** For question generation, it's safer to use a proprietary model since you're not training on the model's outputs — the model is part of scaffolding. GPT-4.1 is pretty cheap. I would not use o3 for data generation unless I really knew I needed it.

**[01:00:58]** The most important thing: get a pipeline, do a small sample, look at it. Generate 50 and look — sometimes only 1 actually looks good, or they're not diverse enough. Iterating at the scale of dozens is a really good way to get a feel for the data set.

---

## Related

- [[concepts/agents-mcp-rl-course|Production-Ready Agent Engineering: From MCP to RL]]
- [[raw/articles/2025-07-03_willbrown_agents-mcp-rl-office-hours-week3]]
- [[concepts/grpo-rl-training]]
- [[entities/will-brown]]
- [[entities/prime-intellect]]
