---
title: "Production-Ready Agent Engineering — Lesson 4: Introduction to Reinforcement Learning (Lecture Transcript)"
author: Will Brown
date: 2025-06-26
date_ingested: 2026-06-11
source: https://maven.com/will-brown-kyle-corbitt/agents-mcp-rl
notebook: https://raw.githubusercontent.com/willccbb/agent-engineering/refs/heads/main/lectures-1-through-4/lec4-rl/grpo_intro.ipynb
type: transcript
tags:
  - reinforcement-learning
  - grpo
  - agentic-rl
  - ai-agents
  - tool-calling
  - agent-evaluation
  - education
  - transcript
related_article: articles/2025-06-26_willbrown_agents-mcp-rl-lesson4.md
participants:
  - Will Brown (instructor)
  - Kyle Corbitt (co-instructor)
---

# Production-Ready Agent Engineering — Lesson 4: Introduction to Reinforcement Learning (Lecture Transcript)

**Instructor:** Will Brown (Research Lead, [[entities/prime-intellect]])
**Co-instructor:** Kyle Corbitt (CTO, OpenPipe)
**Date:** June 26, 2025
**Companion course:** [[concepts/agents-mcp-rl-course|Production-Ready Agent Engineering: From MCP to RL]]
**Notebook:** [grpo_intro.ipynb](https://raw.githubusercontent.com/willccbb/agent-engineering/refs/heads/main/lectures-1-through-4/lec4-rl/grpo_intro.ipynb)

---

## 1. RL Crash Course: From MDPs to Policy Optimization

**[00:07:11]** The goal today is to learn about reinforcement learning — what is RL, why do people do it, how do we think about it, and how do we go from the basics of old-school RL to large language models and agents. First, a brief crash course into RL from scratch: how do you build up towards it? Why is it a thing you would do in a toy setting that does not use language models?

**[00:07:31]** A term you hear thrown around a lot when people talk about RL is the idea of an **environment**. Formally, what an environment really is is what we call a **Markov Decision Process** (MDP). An MDP is this object, which is a collection of pieces: you have **states**, you have **actions**, you have **transition probabilities** (dynamics), and then **rewards** as well as a **horizon**.

**[00:07:49]** The horizon is some interval of time — maybe a fixed number of time steps, or an infinite amount of time where you care more about the future than the present, or more about the present than the future. The goal is to find a **policy** which maximizes your reward over your horizon. A policy is essentially a mapping from states to actions. This could be a randomized policy — the traditional original versions of policy optimization methods were deterministic (every state → one action), then people moved towards more exploration-based methods with online learning and trial-and-error sampling.

**[00:08:37]** Policy gradient algorithms, the most dominant family of online RL algorithms, generally leverage randomized policies. We'll see that this fits very naturally into the LM framing: **your LLM is your policy** — the mapping from states to actions.

**[00:08:48]** For a toy example of an MDP: states 1, 2, 3, 4, 5 with actions A, B, C. A reward is a function that returns a score for a given state and action. Transition probabilities: if we're at a state and take an action, what state do we go to next? Generally we want to think of this as a randomized process — the next state is not always the same. It's a world that can have randomness in it.

**[00:09:39]** A **rollout** is the idea that we start at some state (which could also be random), iteratively take actions, observe our next state, and accumulate rewards as we go. The reward function could depend on the time step; it could be that we don't see the reward till the end. What matters is that we have some ability to estimate the reward, either at the final state or at intermediary steps.

**[00:10:37]** The total reward is just accumulating the per-step reward each time. **Reinforcement learning** is the idea that we do this rollout thing a bunch and figure out which policy π is going to be best for maximizing total reward.

**[00:11:11]** You often start with essentially a randomized policy that's fully uniform — trying everything. This is the deep RL / Atari way: you don't start with a thing trained on anything. As you get more information, you optimize via converting this into a gradient, just like gradient descent for any other ML system, where your loss function is in terms of this reward.

**[00:11:37]** As you do this more and more, you start placing more weight on which actions in which states are resulting in high rewards downstream. You're figuring out how to estimate the **advantage** of taking one action over another, then learning to place more and more weight on those good actions based on this feedback.

### Mapping RL to LLMs

**[00:11:46]** In the context of LLMs:
- **State** = everything so far — the full sequence of tokens up till now
- **Action** = next token
- **Policy** = next-token distribution
- **Transition** = appending the token to what we have so far

Another way of thinking about it: in an agent setting, your **turns** are your actions. But for now, think of tokens as actions.

**[00:12:20]** The **reward** is like an eval — maybe a format eval, partially determined after some prefix of steps. You're building towards what is going to be the final evaluation. You could think of an estimated eval at any given point — if you were to roll back part of your tokens and resample, there's an estimate of how good your rollout so far is.

**[00:13:27]** This is what RL for LLMs is really all about: optimizing — given some intermediate state (some prefix of tokens), which tokens are going to be the next best token to take?

---

## 2. Multi-Armed Bandit Warm-Up

**[00:13:39]** As a warm-up, a single-turn game: the **multi-armed bandit**. Like a slot machine — you have a bunch of slot machines you can pull from. The joke: a one-armed bandit is a slot machine, a multi-armed bandit is many slot machines.

**[00:14:01]** Setup: hidden number is 42. The algorithm doesn't know it's 42 — it only knows there's some number between 0 and 99 (100 numbers to choose from). Those are our actions: every turn we pick a number and get some reward. We also have a number of steps we can take.

**Notebook code pattern:**
```python
Q = 42          # hidden target
N = 100         # action space size
A = list(range(N))
T = 10000       # total steps
bs = 1000       # batch size
lr = 0.0002     # learning rate

def R(a, Q=Q):
    Q_delta = abs(a - Q) / N
    noise = np.random.normal(0, 1)
    return 1 + noise - Q_delta

pi_t = np.ones(len(A)) / len(A)  # uniform policy
```

**[00:14:35]** We set a batch size — we'll do a bunch of steps, do some learning, play a bunch of games in parallel, update our strategy, and repeat. One batch = 1000 versions of the game. A learning rate (0.1 to start) tells us what to do given this round. RL will be: do a batch of rollouts → update strategy → do another batch → hope it improves.

**[00:15:15]** Reward: measuring how close we are. Guess exactly 42 → reward ≈ 1 + noise. As you go further from the target, reward degrades. We want to figure out where it is by sampling and trial and error.

### The Advantage Estimation Loop

**[00:16:01]** At each turn, we sample a batch (1000 games in parallel) using our current policy π_t. For each sample, we estimate the **advantage**: what's the baseline (average), which ones were better, which ones were worse?

**[00:16:39]** We normalize by standard deviation so we're agnostic to the range of rewards — we don't want learning to slow down dramatically because we've already gotten close. The normalization just says: we care about the variance within our samples.

**[00:17:28]** The learning step: take this advantage. If it's a good thing, go up a little bit; if bad, go down. This will break the fact that probabilities sum to one, so we re-normalize. Anything better than average goes up; anything below average goes down.

### Convergence and Stability

**[00:18:01]** First attempt: chaotic, unstable RL. We kind of learned it, then went away. Too much craziness, moving too fast.

**[00:18:52]** What's happening: there's randomness in the sampling. We have to sample to explore, but the sampling makes things chaotic. Sometimes we get unlucky — our best guess might be 39 instead of 42, and we over-index on 39. Then 40 looks better, so we decrease 39, but it oscillates.

**[00:19:22]** The fix: increase stability by **slowing down learning** — increase batch size, decrease learning rate.

**[00:20:40]** After tuning: a nice, clean, converged RL run. Learning really slow, taking its time. There's a lot of fiddling to get this sweet spot. The one that went really far down and got stuck on a bad thing (probably 41 or 43) — we don't necessarily always need the exact optimum.

**[00:21:15]** This is what people mean when they say RL is **finicky or subtle**: there's all these things that if you go too fast, sometimes it works, sometimes it doesn't because you explore too much in a thing that works for a little bit but is ultimately not what you really want.

---

## 3. GRPO for LLMs

**[00:21:34]** Now briefly introducing GRPO. We're not doing any training here — just talking about what a batch is in the context of samples. Then Kyle will do a deeper dive.

**[00:21:48]** For LLMs, there's not just one goal — we want any sort of prompt as input. These are different starting states. Starting states in the context of LLMs are your prompts.

**[00:22:00]** We take a set of prompts (math questions), duplicating them so we have 4 or 8 copies of each. A **batch** = a set of prompts. A **group** = multiple rollouts per prompt. **Group Relative Policy Optimization** — the G in GRPO — is about this group: for any prompt, for any initial starting state, you do multiple samples.

**[00:22:28]** The batch is all of the completions. In the context of gradient optimization, the batch is both prompts and completions: prompt set + group of responses per prompt = one batch. One prompt and its rollouts = mini-batch (though that term has other meanings).

**[00:23:37]** The 8 responses to one prompt = your **group**.

**Notebook code pattern:**
```python
B = 4           # number of unique prompts
G = 8           # group size (rollouts per prompt)
batch_prompts = prompts.repeat(G)  # 32 total completions

vf_env = vf.SingleTurnEnv(
    dataset=batch_prompts,
    system_prompt=system_prompt,
    parser=parser,
    rubric=vf.Rubric(funcs=[correct_answer_reward_func], weights=[1.0]),
)
batch_results = vf_env.evaluate(client, model)
```

**[00:23:44]** Going through prompts, logging results of 32 different completions, getting the average reward distribution, computing advantages.

**[00:24:15]** With a dumb model that makes silly mistakes — sometimes doesn't do formatting right, fails to parse answers. The ones that parsed correctly and got the right answer are correct; formatting failures count as wrong. Some answers are truly wrong. Some say 84 but the real answer is 98.

**[00:24:33]** The signal: the one correct answer vs. everything else wrong. Whatever the model did in the version where it got the right answer — that's good stuff. Everything else is probably bad stuff. Isolating this difference is where the learning comes from.

**[00:25:11]** This is the idea of GRPO: try a bunch of stuff, some work, some don't. You have answers you can evaluate. You get scores about relative performance of different rollouts for the same prompt within your group. **Group relative** policy optimization — this relative signal is what drives learning.

---

## 4. Q&A: Temperature, SFT vs GRPO, and RL Frameworks

**[00:26:12]** **Temperature for GRPO:** You typically want temperature ≥ 1. Temperature 0 = nearly deterministic output (same token always). Higher temperature = more randomness/creativity. This is really what the magic of RL comes from — lots of randomness and sampling and creativity to explore which options are better.

**[00:27:31]** **SFT vs GRPO:** SFT = you have some other system that creates good rollouts (big model, filtering system, prompting tricks) and you train on the good stuff. GRPO = the good stuff is in the model but it's not natural for the model — it's seen the good stuff but doesn't know when to use it or how to generalize. GRPO teaches the skills of when to use what. The sampling has the model try different strategies in different settings; GRPO says "this works here and not there, and vice versa."

**[00:29:19]** **Weight-level difference (SFT vs GRPO):** Both are ultimately getting a loss and backpropagating. However, in practice GRPO seems to update a **much smaller fraction of weights** than SFT — an interesting experimental result without a fully satisfying explanation yet.

---

## 5. Kyle Corbitt: Live-Coding an Agent for RL Training

**[00:28:19]** Kyle introduces the practical portion: live-coding a full agent that can be trained with GRPO. The agent is called **Art E** — an agentic RAG system for email search.

**[00:30:37]** The goal: connect to an email inbox, give tools to read and search, answer natural language questions. Best off-the-shelf model (o3) gets ~90% accuracy; with RL, they achieved **96% accuracy** (60% fewer errors).

### Agent Architecture

**[00:33:49]** Building `run_agent.py`: agent takes a question, returns an answer. Uses a while-loop (max 10 turns), message array with system prompt + user question, appending to message log as the agentic loop runs.

**[00:36:25]** Using **LiteLLM** as the model wrapper — calls many models (Gemini, Claude, open-source) in a consistent format. Built-in caching to disk and observability hooks.

**[00:40:35]** First issue: no tools defined. The agent hallucinates answers. Need to give it actual search/read tools.

### Tool Design

**[00:42:03]** Two tools needed:
1. **search_emails** — keyword search with filters (inbox, sent_before, max_results)
2. **read_email** — fetch full email by message ID

**[00:43:28]** Using SQLite + FTS5 (Full Text Search 5) for local email indexing. The Enron email dataset (~500K emails) from HuggingFace is loaded into a local SQLite database with full-text search indexing.

**[00:52:05]** Tools must be converted to OpenAI-compatible JSON schema format. Using `langchain` utility `convert_to_openai_tool()` — "the only piece of langchain infrastructure we use."

**[00:54:07]** Debugging tip: print the tool schema to verify the LLM understands what each tool does. Good descriptions and parameter descriptions matter for model performance.

### Tool Execution Loop

**[00:55:22]** After adding tools, the model returns tool calls instead of content. Need to:
1. Parse tool calls from response
2. Execute the corresponding function
3. Append tool results back to messages
4. Loop until model returns content (answer) or max turns reached

**[01:01:01]** Multiple tool calls per turn: some models (especially open models) are trained to do parallel tool calls — "run this search AND this search AND this search" in a single turn. The loop should handle multiple tool calls.

### Wrapper Pattern for Tool Abstraction

**[00:58:43]** Key pattern: **wrapper functions** that hide implementation details from the LLM. The search_emails function has parameters (inbox, keywords, sent_before, max_results) but the LLM only needs keywords. Create a `search_inbox` wrapper that pre-fills the inbox, simplifying the tool interface.

> This is a pattern I use a lot for these agents — there's information I have that the agent doesn't have or need to have to use these tools.

### Handling Tool Results

**[01:07:35]** Tool results must be JSON-serializable. Data classes need `.dict()` or manual conversion. The message history must maintain proper OpenAI format: `{role: "assistant", tool_calls: [...]}` for assistant messages with tool calls, and `{role: "tool", ...}` for tool results.

---

## 6. Benchmarking and Synthetic Data

**[01:23:21]** Before RL, optimize the agent as much as possible with prompt engineering and tool design. Reasons:
1. Validate tools are actually working
2. Having the strongest baseline prompt helps RL converge better
3. Need a fast feedback loop for testing and debugging

**[01:24:40]** **Synthetic data generation** (vibe-coded): iterates over email inboxes in batches of 20, asks GPT-4.1 to generate plausible questions and answers. Includes a "realism" score (0-1) — filtering for >0.9 produces much more natural questions.

```python
# Output schema
class SyntheticQuery:
    id: str           # dataset ID
    question: str     # natural language question
    answer: str       # ground truth answer
    source_emails: list[str]  # email IDs containing the answer
    realism: float    # 0-1, how realistic the question is
    inbox: str
    query: str
    split: str        # train/test
```

---

## 7. Agentic RAG vs Vector RAG

**[01:28:34]** Agentic keyword search works **phenomenally better** than embedding/vector RAG for this use case. The model can explore synonyms, doesn't require worrying about chunking (too big/too small). Keywords alone are usually good enough; sometimes adding semantic queries (vector search for snippets) helps as a supplementary tool.

---

## 8. RL Training Ecosystem

**[01:38:25]** Will on the RL framework landscape:
- **Art** (OpenPipe) — focused on fine-tuning agents on specific tasks, efficient and fast, uses same GPUs for training and inference
- **Verifiers** (Prime Intellect) — environment layer for large-scale training runs, separate inference/training GPUs, syncs weights between them
- **TRL** (Hugging Face) — both Kyle and Will have borrowed from HF toolkit; no first-class agent training support
- **Unsloth** — heavily optimized for efficient training on top of Hugging Face, single/multi-GPU
- **veRL** (ByteDance) — industrial scale, very popular, "very annoying to work with, bloated and hard to understand, not super intuitive for beginners"
- **Single-file GRPO implementations** — super readable, fewer features, less scalable

**Key infrastructure:** LLM (vLLM) for inference, PyTorch for training — the agreed-upon building blocks.

**[01:32:21]** **Non-verifiable tasks + LM judges:** In practice, mostly what people use. One interesting paper (RLPR): take the whole reasoning run, look at the likelihood that the model would generate the true answer given all that context, and optimize against that.

**[01:34:19]** **Custom vocab/abbreviations:** Start by putting a brief glossary in the instructions. Could the LLM learn through RL? Theoretically yes, but why force it if you already know?

---

## Companion Resources

- **Notebook:** [grpo_intro.ipynb](https://raw.githubusercontent.com/willccbb/agent-engineering/refs/heads/main/lectures-1-through-4/lec4-rl/grpo_intro.ipynb)
- **Course repo:** [agent-engineering](https://github.com/willccbb/agent-engineering)
- **Blog post:** [Art E — Agentic RAG Agent](https://openpipe.ai/blog/art-e) (Kyle's original write-up)
- **RLPR paper:** [RLPR: Reinforcement Learning from Principle-based Rewards](https://arxiv.org/abs/2504.13837)

## Related

- [[concepts/agents-mcp-rl-course|Production-Ready Agent Engineering: From MCP to RL]]
- [[concepts/grpo-rl-training]]
- [[concepts/agentic-rl]]
- [[concepts/rl-harness-lifecycle]]
- [[concepts/agentic-search]]
- [[entities/will-brown]]
- [[concepts/corbett-kyle-corbitt]]
- [[entities/openpipe]]
