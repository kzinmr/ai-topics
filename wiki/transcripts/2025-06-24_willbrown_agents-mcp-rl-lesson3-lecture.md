---
title: "Production-Ready Agent Engineering — Lesson 3: Agent Evals and Optimization (Lecture Transcript)"
author: Will Brown
date: 2025-06-24
date_ingested: 2026-06-10
source: https://maven.com/will-brown-kyle-corbitt/agents-mcp-rl
notebook: https://raw.githubusercontent.com/willccbb/agent-engineering/refs/heads/main/lectures-1-through-4/lec3-evals-optimization/evals_optimization.ipynb
type: transcript
tags:
  - ai-agents
  - evaluation
  - llm-as-judge
  - reinforcement-learning
  - grpo
  - fine-tuning
  - reward-hacking
  - agent-evaluation
  - education
  - transcript
related_article: articles/2025-06-24_willbrown_agents-mcp-rl-lesson3.md
participants:
  - Will Brown (instructor)
  - Kyle Corbitt (co-instructor)
---

# Production-Ready Agent Engineering — Lesson 3: Agent Evals and Optimization (Lecture Transcript)

**Instructor:** Will Brown (Research Lead, [[entities/prime-intellect]])
**Co-instructor:** Kyle Corbitt (CTO, OpenPipe)
**Date:** June 24, 2025
**Companion course:** [[concepts/agents-mcp-rl-course|Production-Ready Agent Engineering: From MCP to RL]]
**Notebook:** [evals_optimization.ipynb](https://raw.githubusercontent.com/willccbb/agent-engineering/refs/heads/main/lectures-1-through-4/lec3-evals-optimization/evals_optimization.ipynb)

---

## Lesson Focus: Evals, Optimization, and the Road to RL

**[00:02:49]** Today we'll be focused on evals and optimizations, kind of building towards RL and laying the groundwork for doing some things that are kind of RL. We won't be necessarily going into specific RL algorithms too much, although towards the end we'll get into it a little bit.

**[00:03:04]** The main things I want to focus on are eval best practices — doing a quick survey of what real-world evals look like. What goes into these benchmark scores? What goes into measuring model performance? What models are good at what things?

**[00:03:25]** Then also going through some exercises of designing a few different evals and reward functions with different goals in mind, to get a more holistic view of how we evaluate tasks. This is going to be the foundation of reinforcement learning and optimization of our agents, because we need to be able to tell what they're doing and how well they're working in order to improve them.

**[00:04:09]** I also want to spend a good amount of time talking about supervised fine-tuning today, because especially if you've done all you can with an API model but it's too slow or too expensive, or you want to run it locally — fine tuning is a good entry point into custom model optimization. If you're not familiar with doing fine tuning, then RL is going to feel very difficult getting started.

**[00:05:13]** We'll also touch on DSPy at the end, depending on how much time we have. DSPy is another way of framing the goal of optimizing your LLM systems in terms of evals and metrics, with prompt optimization as the main entry point.

---

## 1. Model Benchmarks and Evaluation Sites

**[00:06:33]** For evals, one site to be aware of is Artificial Analysis — one of the main provider sites that does a lot of their own reporting of different benchmarks.

**[00:06:42]** The benchmarks they use are fairly simple ones:
- **GPQA** — multiple choice science questions
- **Humanity's Last Exam** — short answer, LM-judged
- **LiveCodeBench** — live-updating coding problems from LeetCode and Codeforces
- **AIME and MATH 500** — math questions where answers can be judged by an explicit function fairly easily

**[00:07:08]** If you want a rough sense of how models stack up, this is a useful starting point. It roughly matches most people's intuitions about model quality by aggregating these evals. Model quality is fuzzy, but there is a ranking somewhat.

**[00:07:47]** Together AI has a site where you can talk about different criteria for your model, and it shows results — they're a hoster of many open-source models, so especially if you're thinking about models that might be a good starting point for fine tuning, this might be useful.

**[00:08:42]** One recommendation: if you wanted to build the closest thing to a Claude for agent performance — not in terms of absolute performance, but for agent performance — the latest, largest Qwen 3 model is quite good. It's a reasoning model, but it's also been trained to do tool calling and MCP.

---

## 2. Model Spec as Eval Foundation

**[00:09:06]** I think one way of thinking about eval design is doing even higher-level specification of what the goal of your system is. Being familiar with the idea of a **model spec** is really useful.

**[00:09:17]** This is OpenAI's model spec — talking about things that sometimes might feel really obvious, but this is really how you start shaping your evals. You define the things you want your system to do. Defining what you want your system to do is important before you measure how it's doing.

**[00:09:36]** Especially if you're designing agents that are meant to interact with people, simulating this and evaluating this is not easy.

### User Simulation

**[00:10:24]** The way you might want to do it is having a piece of your environment simulating the user. Maybe you have a long user bio system prompt describing how the user could interact. You have the agent do its thing, then at some point the agent hands off to the user. Now the user is being simulated by another LLM. This will require some tuning to get right.

**[00:10:41]** You would want to clarify what your user behavior is in terms of personality, profile, maybe examples of past user chats for prompting the model to follow a certain style. If you hand-curate a short transcript of past examples showing how the user behaves, and your user simulator has these few-shot examples, this gives you something to simulate a user.

**[00:11:11]** This could be a way you poke at different edges of model behavior. For example, maybe you have a user who's trying to elicit certain negative behaviors — let's say you have a flight booking agent, and you want to ensure that your flight booking agent will not do an action it's not permitted to.

### Guardrails and FAQ Evals

**[00:11:32]** Generally you should handle this at a system level, not at a model prompting level. But you do want some initial guardrails around the model. Any model that's going to be user-facing, I think you need to think about these questions — what are the sorts of backdoors the user might try to exploit?

**[00:12:15]** As a rule of thumb, there's no way to permanently block these. Any sufficiently motivated user will be able to get around the behavior you try to nudge into the model. But this is generally your first layer of defense for lazy users or insufficiently motivated bad actors.

**[00:12:24]** If your website has a chatbot as an agent that can do some actions around your site, the chatbot maybe can search for FAQs. And this should definitely be one of your evals — is the agent for this site good at answering the FAQs of the site?

**[00:13:57]** This is a quick win and a good sanity check: can your agent reliably answer user questions about your system? You can quite likely easily write 20 or 30 FAQs, the same way you'd see on lots of websites.

### Writing a Model Spec

**[00:14:21]** More holistically, the idea of a model spec is really just an exercise that you should do before any sufficiently important agent system. You are thinking about the use cases, thinking about edge case behaviors, defining what the intended behavior should be in these scenarios. This is a really good starting point for crafting more granular evals.

**[00:14:53]** For example, with a finance agent — if you want it to go look at reports, and it has a tool to look at reports, it should mention that to the user in context.

---

## 3. Popular Agent Benchmarks

**[00:15:46]** A useful thread from a friend on Twitter curating an overview of popular evals:

- **GPQA** — science multiple choice questions
- **LiveCodeBench** — live-updating questions from LeetCode and Codeforces
- **Polyglot** — popular coding benchmark with lots of different languages
- **MMLU-Pro** — updated version of the classic MMLU multiple choice benchmark
- **Long context benchmarks** — adding strings to specific locations in long documents

**[00:17:08]** These use LM-as-judge to ground the answer. There's some text-based ground truth answer, and the eval uses a standard LLM and prompt setup to judge the submission against this ground truth.

**[00:17:30]** The general pattern of having an LM judge be a fuzzy matcher who can see the ground truth, can see the context, can see whatever criteria you want to give it, and uses that to determine whether or not the task has been completed successfully — that is a very common building block.

### BFCL v3 (Berkeley Function Calling Leaderboard)

**[00:18:08]** BFCL v3 is a multi-turn tool call benchmark where there are different kinds of tools being given to a model and it has to successfully do multiple turns of interaction. It has a user simulator.

**[00:18:34]** This is a good example of user simulation — the user has to ask "book the 10 AM flight" which only makes sense if the first call succeeded. The decision tree of how the user simulator responds based on earlier turns is something you'd specify at some level of granularity.

**[00:18:53]** BFCL v3 is one of the truly good multi-turn tool-call agent benchmarks that really feels like in the spirit of what we mean when we talk about building useful agents.

### TAO Bench

**[00:19:27]** TAO Bench is in a similar theme — user simulator, tool calls, multiple rounds of interaction. It's grounded in domains like airlines and reservations.

**[00:20:21]** Other fun one: **Minecraft Bench** — agents use tools to create Minecraft objects, and you vote on which one's better. More of a creative/visual agent eval, but it requires really good tool use.

---

## 4. Deterministic Evals

**[00:20:54]** Now let's go through some different ways we can do evals. First, very basic parsing for format.

### Format Verification with Box Notation

**[00:21:41]** The answer is just an integer. We're setting this up to parse the answer from the text — the format uses a boxed notation (common in LaTeX). If you want to do deterministic verification, this is the sort of thing where you could use Pydantic.

**[00:22:08]** But some models will want to respond in a very specific way. For example, many reasoning models (DeepSeek R1, Qwen) will always respond in terms of think tokens. This does not necessarily play nicely with parsing via Pydantic/instructor, because those things want the whole model response to be in JSON, which is going to hurt the performance of a lot of these models.

**[00:22:41]** Models oftentimes will perform much better in certain formats than others. The easiest way to do the right format is just do the one that the model is trained on. If a model is trained to use think tokens, you should allow it to use these think tokens.

**[00:23:37]** In math, people often use this box notation — `\boxed{4}` in LaTeX. They train on this; they already have the sense that putting a box around a thing means it's an answer. It's kind of intuitive for them to give an answer inside of this sort of expression.

### Reward Functions: Correctness + Format

**[00:24:31]** One of the reward functions here is the correct answer (1 if correct), and there's also a format reward function. For the think parser, it's checking that the format starts with a think token, there's something inside, there's another think token, and then there's more content after. Just a few if-statements.

**[00:25:24]** We set the weights of these: correctness is the main one, format is the other one. For evaluating your system, it's kind of fine to have many individual benchmarks that you just look at and decide for yourself what to do with them.

### Tool Calling Evals

**[00:26:23]** Especially when you're building agents, I would go ahead and take all of the actions you might want your model to do and treat these essentially as evals. You would want a dashboard where, in the same way we looked at the Logfire logging before, these are the metrics you'll care about:

- Fraction of times a model calls a tool
- Amount of times the tool call does not return an error
- Amount of turns where there's certain tools versus any tool

**[00:27:26]** You should plan on architecting your system in a way where these can all essentially be evals. You can have lots of evals. You probably should have lots of evals.

### Instruction Following Eval (IFEval)

**[00:28:22]** This is a dataset from Google that has tasks where the prompt is like "no commas in the response" or "do not use any comments" or "highlight at least 3 sections with this format."

**[00:28:56]** These kinds of properties are often the sorts of things you might write down in your model spec — "if XYZ is true, model should behave like this." You can write an if-statement for these. Often they will not need an LM judge — they can just be Python functions.

**[00:29:47]** Checking if the letter T appears at most once — we can just write a function. Models are really bad at doing things involving letter counts.

**[00:30:31]** No commas — same idea. Make sure the word "war" is used at least 8 times and "peace" at least 10. These are a little simplistic and silly, but they're good examples of how you can get creative with evals that are deterministic.

### Generating Large Eval Sets

**[00:31:38]** For things that are very precise, these are good — like an extension of format rewards. This one is writing short stories about animals playing sports which use a given letter at least N times.

**[00:31:55]** If you want a large eval set to get a high confidence score about model A being better than B, taking the set product of variables gives you a really long list of prompts. We got 1,800 prompts from this set.

---

## 5. Non-Verifiable Tasks: LM Judges and Golden Answers

**[00:34:40]** For non-verifiable tasks, there are a few different patterns:

### LM Judges
Using LM judges as your first approach towards evaluating whether certain properties hold about your tasks.

### Golden Answers
The gold standard for golden answers is something where you have human data. If your goal with your agent is to automate some human process, you don't necessarily need to have a human trajectory of the whole process. But you might want the final object.

**[00:35:19]** A lot of agents can be thought of similarly to reasoning models — the tool calls are kind of treated as part of the reasoning process. The framing of the eval is still question-and-answer or input-output, but the output is not necessarily the whole trace. It's the thing at the end — the objective of the agent is to use tools and reasoning to create this object at the end.

### Best-of-N Sampling

**[00:36:12]** A lot of times your agent systems will be the sorts of things where you have ways to spend more to get better outputs. The ways you can get more quality in exchange for spending more time or compute are:
- Using bigger models
- Using more trials
- Using more thinking tokens

**[00:40:18]** This is one way of kind of bootstrapping a better response — spending more compute on inferencing more samples, then trying to pick the best one. For your evals this might be worth doing upfront, because the number of things you want as your golden answers are pretty small.

**[00:40:55]** Using bigger models, using more reasoning — this can be what you compare your other systems to that have to be faster for deployment, have to be more efficient, etc.

---

## 6. Text-Based Metrics

**[00:42:38]** For things that are very text-based, the **longest common subsequence (LCS)** algorithm is useful. Think of it as the way that GitHub will do diffs — finding the best one-to-one matching in a sequence, and whatever is different is the diff.

**[00:44:09]** We can also use **embedding similarity** as another way — more conceptual and less literal. ROUGE is a benchmark, BLEU is a benchmark — there are a few different algorithms.

### Calibrating LM Judges

**[00:44:32]** Having judges that can be reasoning models is a relatively new thing. One trick to measure how large is too large of a judge: start seeing how often your judges agree with themselves versus agree with other models.

**[00:45:07]** Does GPT-4.1 Nano agree with GPT-4.1? Does that agree with Opus from Anthropic? You really can't do much better than the biggest model. But if a small model is very consistent with the choices of a big model, then you can pretty safely fall back on the smaller model.

**[00:45:37]** Doing this comparison of running with multiple judges and seeing if the judges agree with each other on the same set of outputs will give you a good sense of how much they vary. Also running a judge multiple times — there's the temperature thing. Temperature controls randomness; many models default to 0.7 as the sweet spot.

**[00:46:19]** Measuring correlation between judges gives you a measure of how much randomness there is. If correlation between multiple judges is very close to one, there is very little randomness being introduced by rerunning or by using a different judge.

---

## 7. LM Judge: Pairwise Comparison

**[00:51:41]** If you're doing pairwise comparisons with an LM judge, a lot of times judges have a bias towards a certain position where they might always prefer the first one or the second one. It's good practice to **randomize the order**.

**[00:52:32]** GPT-4.1 versus GPT-4.1 should converge to 50%. We basically do see that — exactly half the time the judge picked the first one, half the time picked the second one. These are the same model, just reruns.

**[00:54:03]** Generally good to run evals multiple times to get a sense of how much variance there is. Ideally you want confidence intervals — if model A is better than model B by the margin of error from your confidence intervals, this tells you you've actually made an improvement and not just getting lucky.

---

## 8. Agent Tool-Use Evals

**[00:55:02]** Final answer evals plus patterns of tool call use are really the things you want to be thinking about. This is a tool call environment for math questions — a math coding agent that can use a code REPL.

**[00:58:57]** Good question about rewards for tool use — it can be a slippery slope for reward hacking.

**[00:59:08]** I generally prefer to reward models for using tools a non-zero amount of times. We can measure:
- Were tools used at least once?
- What are the fraction of tool calls that succeeded?
- Encouraging not using too many tool calls (Kyle Corbitt's addition)

### Kyle on Tool Call Efficiency

**[00:59:52]** Kyle Corbitt: "In the reinforcement learning side, we oftentimes want to incentivize it to do fewer rounds as long as it gets the correct answer. And you can just add that to your reward function."

---

## 9. Self-Play and Judge Training

**[01:00:22]** Absolute Zero is really cool research. I expect a lot of cool things to come from it. I don't think it's the sort of thing that is battle-tested. Doesn't seem to be the case that anyone is really using self-play in a serious way to make really truly self-improving agents.

**[01:00:47]** We're kind of doing the judge iteration side manually — tuning reward functions by hand, thinking hard about scenarios, setting reward functions that make sense to us. Automating that whole piece is tricky.

**[01:01:23]** There has been a lot of work training judge models specifically. People have trained very small judge models that do quite good at reasoning before giving their judgment, and they use RL to train the judge. The idea of "figure out what you want your judge model to do, train a really good judge model, and then do RL with that judge" is totally fine. But the full interactive both-learning-at-the-same-time is where it gets really tricky.

---

## 10. Supervised Fine-Tuning (SFT)

**[01:02:24]** Once we have these results, we can turn them into datasets. This will be the starting point for doing supervised fine-tuning.

**[01:04:30]** Supervised fine-tuning (SFT) is a scenario where you have a prompt and a completion. Just like traditional machine learning with X's and Y's — training a model to guess Y given X. The objective function of SFT is all about encouraging this response to become more likely.

### Libraries and Tools

**[01:05:18]** The one I typically reach for is **HuggingFace TRL SFT Trainer** — good balance of flexibility with easy user interface.

**[01:05:58]** Important things to think about:
- **Context length** — your max sequence length
- **Batch size** — at least 16 samples; can go down to 8, wouldn't go lower
- **Total steps** — at least 100 steps
- **Dataset size** — 1,000 examples is usually where I'll start; 10,000 is great; 100,000 is often overkill
- The **1,000 to 10,000 range** is often a good starting point

### Creating Training Data

**[01:06:51]** Taking datasets created by running rollouts and saving them. I had a score and a reward for finishing Wordle in fewer turns. Then filtering based on the top half of scores — that's kind of a rule-of-thumb heuristic.

**[01:08:30]** Throwing away the bad ones — your evals now are a filter you can apply to the output of this agent setup. Now you have a dataset of examples of an agent in a setup that we care about, doing multiple turns of interaction to do well for the task.

### GPU Recommendations

**[01:09:08]** The site you'll be getting credits for GPUs is Prime Intellect.

**[01:09:37]** For getting started, pick something small. For a small model (1B parameters), there's napkin math about how much memory you need.

**[01:10:04]** I often work with the RTX 6000s or the 48 GB ones — I will often use 2 of them. That's $1.50/hour. This is where I usually test my setups and do experiments with 1B parameter models. Training experiments typically run pretty quick — a few minutes up to 10 minutes.

**[01:11:53]** For a 7B model, it takes ~14 GB of memory. Full fine-tuning adds a factor of 5 → ~70 GB. You can get this much smaller by doing **LoRA** (Low-Rank Adapters) — only tuning a smaller low-rank space, much more memory efficient.

**[01:12:23]** If you really want to maximize your fine-tuning juice, **Unsloth** is probably your best bet — designed for single GPU usage.

**[01:13:15]** **Axolotl** is also popular. Both Unsloth and Axolotl are built by taking TRL and changing it a bunch.

**[01:13:31]** For something fully self-contained with very few dependencies and really hackable — **Torchtune**, the official PyTorch one.

### LoRA vs Full Fine-Tuning

**[01:14:02]** For a LoRA fine-tune, this should be doable on one GPU with decent batch size and context length for a 7B model.

**[01:14:10]** H100 is the industry standard. H200s have been taking over lately (more memory). A100s are the older generation — cheaper now, good for getting things working.

**[01:14:55]** LoRA is totally works. I default to not doing it, partly because of my research goals (multitask learning, scaling up to larger training runs). If you are doing a model that's already pretty good and really fine-tune for your thing, LoRA does make a lot of sense.

Kyle Corbitt: "The larger your training run, the longer your training run, the more tasks you're trying to do, the further you expect your training run to get away from the base model capabilities — then the less sense it makes to use LoRA."

### Curriculum Learning

**[01:18:16]** Sorting your dataset is the easiest way to do curriculum learning. You could have your model answer every question 3 or 5 times, look at the number of times it got it right — this is now a score. Sort the dataset by this column: easy ones first, hard ones later.

**[01:21:37]** Often you will want to throw away anything that the model always got right. You might also want to start by throwing away everything that the model always got wrong.

**[01:22:00]** The way RL will work best is if you have problems that are kind of in the right sweet spot — the model gets it right sometimes and wrong sometimes. GRPO works by having multiple outputs where some are good, some are bad, and it looks at the difference between them.

---

## 11. GRPO Deep Dive

**[01:24:20]** In GRPO, the algorithm is about having a bunch of prompts. In each step, we take a set of randomly chosen prompts. A batch will have many prompts as well as many rollouts per prompt. These are both different knobs we can tune.

**[01:24:54]** Typically you could do 64 rollouts per prompt. The original DeepSeek paper had 64 rollouts per prompt. More is better.

### Key Knobs

**[01:25:20]** GRPO is the sort of thing that was not widely used up until early 2025. We have about 5 months of people really going into the weeds since R1 was when everyone realized.

### Reference Model and KL Penalty

**[01:25:46]** One of the big questions is whether or not you use a **reference model** (the frozen version of the original model) and applying a **KL divergence penalty**.

**[01:26:01]** KL divergence is about difference in **token space** (as opposed to weight decay or grad norm penalties which are about difference in weight space). At a given step, what's the probability distribution that would naturally come out of the model versus what the gradient update would nudge the model towards?

**[01:26:31]** Some papers have beta value being really high like 0.4. Anything above 0.1 is a high beta value. You can go down to 0.

**[01:27:58]** I tend to find that training failures happen when the model has learned quite a bit, maybe learning rate is too high, but you don't have good variance in your rewards. Maybe you hit a batch where all the answers are 0 or all are 1, and the KL penalty takes over and is really large.

### Online Reference Model Updates

**[01:28:27]** One trick: having the model be updating online. You can have your reference model updating every 100 steps — a half-update where it's a merge. Your reference model is an anchor that's lagging behind but always following it. You're always in this vicinity where it's not too jumpy.

### On-Policy vs Off-Policy

**[01:33:57]** Off-policy: think of it as static distributional. SFT is off-policy. DPO is off-policy — the set of things you're training on comes from a fixed distribution.

**[01:34:13]** Online learning: the sample you're training on is changing as a function of the iteration. In GRPO, you are always generating new samples from your model for the prompts.

**[01:35:25]** The simplest version of GRPO is fully synchronous — you do inference, get this batch, train on this batch, update your model, then use this model to do more inference. This is 0-step off-policy, the same as on-policy.

**[01:36:03]** Going more off-policy means allowing for more lag where your rollouts are more stale. As you go to the extreme, this collapses into offline/batch-based off-policy RL.

**[01:37:04]** For GRPO, it tends to be safe to go at least one step off-policy without worrying too much. The benefit is that now you can fully overlap training and inference without having to swap versions of the model.

### Kyle on LoRA for RL

**[01:41:51]** Kyle Corbitt: "For everything we've looked at in the course, LoRA would work completely just fine. For the examples we'll be talking about with RL — my plan is to talk mostly about LoRAs, because I suspect that most of you are interested in making agents that are very reliable for your own specific tasks, as opposed to competing directly with Prime Intellect and making these big general-purpose agents."

### DSPy and GRPO

**[01:42:18]** DSPy has a GRPO implementation. It is very cool to look at. For DSPy programming with it, it is probably not going to be the most effective optimizer — they tend to find that their prompt optimizers work really well.

**[01:43:06]** A lot of the GRPO value is in having fine-grained control over it and being able to do this experimentation. I'm not sure that DSPy is the interface that makes the most sense for it. DSPy wants you to not have to worry about the optimizer — you plug in and try, and pick your favorite. For RL, having the ability to specify all these things and being forced to think about what they mean is really useful for tuning your experiments.

---

## Companion Resources

- **Notebook:** [evals_optimization.ipynb](https://raw.githubusercontent.com/willccbb/agent-engineering/refs/heads/main/lectures-1-through-4/lec3-evals-optimization/evals_optimization.ipynb)
- **Course portal:** [[concepts/agents-mcp-rl-course|Production-Ready Agent Engineering: From MCP to RL]]
- **Article summary:** [[raw/articles/2025-06-24_willbrown_agents-mcp-rl-lesson3|Lesson 3: Agent Evals and Optimization]]
