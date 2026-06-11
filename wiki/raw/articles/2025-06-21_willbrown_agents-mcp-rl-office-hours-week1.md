---
title: "Production-Ready Agent Engineering — Office Hours (Week 1)"
author: Will Brown
date: 2025-06-21
date_ingested: 2026-06-10
source: https://maven.com/will-brown-kyle-corbitt/agents-mcp-rl
type: transcript-raw
tags:
  - ai-agents
  - agent-framework
  - prompt-engineering
  - fine-tuning
  - browser-agents
  - education
  - transcript
participants:
  - Will Brown (instructor)
  - Eddy Atkins (student)
  - Phlo (student)
  - Michał Barrington (student)
  - Aditya Advani (student)
  - Jan-Hendrik Ruettinger (student, Dataleap)
---

# Production-Ready Agent Engineering — Office Hours (Week 1)

**Instructor:** Will Brown (Research Lead, [[entities/prime-intellect]])
**Date:** June 21, 2025
**Companion course:** [[concepts/agents-mcp-rl-course|Production-Ready Agent Engineering: From MCP to RL]]

---

## Agent Framework Selection (Eddy Atkins)

**[00:02:08]** Eddy: We've started deploying agentic behavior at work — web search, internal chatbot. We've used the OpenAI Agents SDK. How much should we invest in framework-specific features (guardrails, handoffs) vs keeping things flexible?

**[00:03:18]** Brown: The biggest drawback of the OpenAI Agents SDK is that it locks you into OpenAI. If you're already locked in for other reasons, it makes sense. But many people will find Gemini or Claude to be stronger model choices. If you're on a platform where you can access those and you're not using them because of Agent SDK, that's a pretty big restriction.

**[00:05:05]** If I was gonna pick a stack to bet on and invest in for the key pieces of my system, it'd be **MCP**. Keep the other stuff at a higher level where you maintain flexibility. A lot of agent frameworks are thin — the things they're doing are very easy to do yourself.

### LangChain Tech Debt Warning

**[00:08:15]** Brown: I experienced this a lot in a previous role — a lot of people were really eager to use LangChain and they would accumulate tech debt really quickly. Stuff baked into old patterns, assuming certain things about how systems should work, that became irrelevant very quickly. But it was so deeply embedded throughout the stack — people had bet on LangChain and it was hard to extract out of it.

**[00:08:51]** What I would always tell people: start with completions API, give people examples of how to do things with that. Go to something more robust when you need it.

### When Frameworks Make Sense

**[00:10:51]** The reason to adopt an agent framework is because you need one. Frameworks that solve a very specific problem are safer bets:
- **DSPy** — compositionality, automatic pipeline optimization, prompt tuning
- **Instructor / Outlines** — structured generation, surgical, doesn't swallow your system
- **MCP** — tool portability, standardized protocol
- **Devals** (or similar) — LLM-as-judge, plugs in as eval layer without committing to agent framework

**[00:13:03]** Be skeptical of any framework that wants to swallow your whole system — that's a lot of times the goal: vendor lock-in.

**[00:10:28]** Will the answer change in a year? It'll depend on whether any frameworks come out with really killer app features — something everyone loves that is really annoying to do yourself, done in a clean way.

### Self-Hosting Considerations

**[00:09:05]** Sometimes you really need to self-host logging because of enterprise security constraints. MLflow and Arize Phoenix are very easy to self-host. If you wanted to use Weave, you'd have to sign a contract and onboard them, which takes a long time. Something self-hostable is important — then figure out vendor engagements as needed.

---

## Agent Evaluation for Summarization (Phlo)

**[00:14:17]** Summaries are nice because there are tricks you can do. Using `difflib` for comparing overlap of sequences — a good summary should have high character/word-level overlap with the true sentence, but also not too long.

**[00:14:50]** Better approach: take the original, generate 10 questions from it, have your summary pipeline output a summary, then see if another model can answer these questions using only the summary. This evaluates whether the summary conveys the key facts. FAQs are a reasonable way of condensing "key facts."

**[00:16:09]** Evals and reward functions are kind of the same thing. We're not doing training here, but we want hand optimization: which model, what prompts, can we tell whether it's doing a good job?

### Chunked Summarization for Small Models

**[00:17:24]** Phlo: Running an 8B model at home on a 3090, transcript context exceeds 100K tokens. Want to summarize previous chunk, then go to next chunk and keep moving.

**[00:18:08]** Brown: DeepSeek V3 via API (100K context), or host via W&B (free credits), Together, etc. V3 is better than R1 for summarization — R1 sometimes thinks too much. Summarization isn't super reasoning-intensive.

**[00:18:39]** DeepSeek is cheap and you're allowed to train on the data from it. For products, most closed-source providers have clauses saying don't train on our outputs.

---

## Prompting as Documentation (Michał Barrington)

**[00:19:54]** Michał: Are we trying to craft perfect prompts and tools rather than the model itself?

**[00:20:13]** Brown: Tools should be thought of as software — you're building a function or library that does a set of things really well. The model fills in the gaps of pieces of software that are very hard to write deterministically.

**[00:21:13]** The way to think about prompting is really about **writing documentation**. Magic prompting tricks change model to model and aren't the same over time. But good documentation is always good documentation. Tools should be documented well — just as you would want a human to have a description of what they do and how to use them, with examples.

**[00:21:56]** A great system prompt looks kind of like a **README**, but for a different thing. You're talking to the model, telling it what its tools are, how they work, how they're supposed to be used, and giving it the ability to use those tools.

---

## O3 Model Architecture (Jan-Hendrik Ruettinger)

**[00:24:11]** Jan-Hendrik: Is the O3 model in ChatGPT (with search) just the normal O3 model plus smart prompts, or is it completely fine-tuned?

**[00:24:44]** Brown: The initial deep research was a fine-tuned version of the older O3 (announced December 2024). The O3 model we use via API now is likely also trained to do deep research as one of its skills. It's probably one fixed model used via API, ChatGPT, or deep research — but with very different (elaborate) system prompts.

**[00:25:36]** Evidence: they made a mini deep research with O4-mini pretty quickly — they just plugged in O4-mini instead of O3. Behind the scenes, one of the deep research updates was likely moving from the fine-tuned version to the general O3 model.

---

## AG2/AutoGen (Aditya Advani)

**[00:29:00]** Aditya: Using AG2 (open-source AutoGen fork, v0.2) for first production agent task. It's modeled as assistant + user proxy — like a ChatGPT session but with lots of knobs to control, including an **autonomy slider**. Has OpenTelemetry bindings.

**[00:30:03]** Brown: For very chat-focused agents, this could make a lot of sense — multi-model chats, users talking to multiple models, group chat with good handover and context management. The more a framework is opinionated about a certain way you should use it and is not trying to solve everything, the better.

**[00:29:58]** Naming confusion: there are two near-identical AutoGens (Microsoft's official v0.4 and the AG2 open-source fork).

---

## Personalized Tutoring Agent

**[00:31:22]** Getting information out of users is tricky — people are not great at saying what they want. Easiest approach: decide what you think they want, make something, then give them the ability to tell you "no, not that, wrong for X reason." People are much better at telling you what they want once you show them something close but wrong.

**[00:32:17]** Good pattern: **CLAUDE.md-style user state files** — lightweight state for agents. A text file that keeps track of rules, essentially becomes the system prompt. Tell the agent: "whenever I tell you 'note this,' edit the file to account for this." This gives you dynamic continual learning — in a new session, the agent has bullet points describing things it should be doing.

---

## Model Selection: Thinking vs Non-Thinking

**[00:34:07]** Brown: I almost always start with an unthinking model. I will prompt it to do chain of thought (a few sentences, not many paragraphs). Non-thinking models are faster, more flexible in prompt structure, and easier to move between models — especially if doing any kind of training. Thinking models have different thinking formats, so parsing code and evals can't always be the same.

**[00:35:14]** Use thinking models when you need really high quality answers with few steps and can tolerate async delay (e.g., GitHub PR agent — 5 minutes is fine). Don't lean on them for user-facing chat where you want answers now.

---

## Fine-Tuning Data Collection

**[00:53:44]** Brown's workflow:
1. Create environment, verify it works
2. Plug in GPT-4.1 as eyeball test — does it look right? Obviously wrong things in prompt?
3. Optimize prompts by hand (or DSPy)
4. Collect data: plug in DeepSeek V3 (trainable), run through setup, do a bunch of rollouts, save them
5. Evals rank which data points are better — take top half or everything above threshold
6. Filter also by tool call failure counts — models that make silly errors then eventually get it right can be filtered out
7. This filtered dataset is the starting point for training

**[00:56:10]** Brown's rule for DSPy: people who use it really love it, and they tend to use it for most things. Small agents is a fun educational tool. General rule of thumb: start with basically just an API, do your while loop yourself, use lightweight frameworks (MCP, instructor) for tools. If you find yourself really getting annoyed with prompt optimization or rewriting similar code — that's when you reach for a framework.

---

## Browser Agents

**[00:46:53]** Momo from Allen AI — training a point-and-click model. Key insight: you can cheaply create good synthetic data with multiple representations (HTML + image). You know programmatically where a button is, so you have ground truth for pixel-level click location.

**[00:48:33]** Off-the-shelf browser use is still not great. Benchmark scores for state-of-the-art are still pretty low. OpenAI Operator is probably still state-of-art for general purpose computer use, and it's not that great.

---

## PDF Processing

**[00:40:39]** For arXiv papers: raw LaTeX is available, download and parse directly. For standardized-structure PDFs: parse the structure.

**[00:41:19]** Multimodal approach: Gemini is really good at native images of PDF pages — convert whole PDF to image, have model read it directly. But image-based search over PDFs for keywords is tricky.

**[00:42:30]** Simon Willison's script using Mistral OCR — converts PDFs to markdown with extracted images. Brown has a version for arXiv papers that does parsing, makes nice markdown, extracts images separately.

---

## Agent Hosting

**[00:37:41]** Any CPU server works if not hosting models: Hetzner, AWS, Modal, Cloudflare. For local: entry-level Mac Mini is a fun agent box — MLX is quite good for batch-size-1 small model inference (run 8B-70B models fine). If using API models, any remote web server does the trick.

---

## RL vs Fine-Tuning vs Prompt Optimization

**[00:49:03]** Brown: Think of it holistically — task-specific optimization of agents. RL is one piece. Use RL when: locally hosted models, small efficient cheap-to-inference models, high-scale usage where cost is serious concern.

**[00:50:06]** The pipelines aren't necessarily just RL — they're the sorts of things you should be doing anyway: creating good benchmark datasets, good example tasks and evals, optimizing prompts. The way to think about what an agent should be doing and how to evaluate it — there's a lot of ideas from RL that are very generally applicable.

**[00:50:29]** Brown: I start with fine-tuning first pretty much all the time. Prompt optimization → fine-tuning → RL is the progression.

---

## Reasoning Models: Tokens = Time

**[00:51:23]** Think of it as having more time on a test. If you can't do work by hand and only have a few seconds to write your answer — reasoning models are like models allowed to spend time working on the problem with scratch paper and a calculator. Tokens for LLMs is like time for humans — more tokens = more time working before giving the answer.

**[00:52:15]** You can spend too much time — just like humans, reasoning models can go in circles doing useless work.

---

## Miscellaneous Q&A

**Reinforcement Pre-Training** (00:59:34): Paper about doing reasoning for next token prediction. Interesting but not worth spending too much time on yet.

**Text Reversal Training** (00:59:58): Brown trained a reasoning model to reverse text order. Tokenization challenge — trivial for humans but transformers aren't natively good at it because tokens are multiple letters. Training with reward incentivizing correct reversal teaches the mapping.

**Simon Willison** (00:52:56): Great writings. His World's Fair talk uses an eval about models writing SVG code for "a pelican riding a bicycle" as a through-line for discussing model improvements.

**Lovable's Go Backend** (00:27:37): They ported their whole backend to Go, agents built in Go. Makes sense for their use case — the apps they support are similar to how Lovable itself is written. TypeScript would also make sense (MCP initially supported only Python and TypeScript).

**Always-on Agent Prompts** (00:39:51): Absurdly long prompts are fine. Take advantage of prompt caching — most providers offer steep discount (~10% cost) for subsequent retrievals of the same input prefix.

**Best Homework Approach** (00:57:45): Pick a task you understand well yourself — easiest to build a good agent for tasks where you can distill your own knowledge into system prompts and evals. Games are fun. Creative applications using libraries you enjoy (e.g., Rich for terminal UIs).
