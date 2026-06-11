---
title: "Production-Ready Agent Engineering — Lesson 5: Formulating Business Problems as RL Tasks (Lecture Transcript)"
author: Kyle Corbitt
date: 2025-07-02
date_ingested: 2026-06-11
source: https://maven.com/will-brown-kyle-corbitt/agents-mcp-rl
notebook: https://raw.githubusercontent.com/willccbb/agent-engineering/refs/heads/main/lectures-1-through-4/lec5-grpo-details/grpo_details.ipynb
type: transcript
tags:
  - reinforcement-learning
  - grpo
  - agentic-rl
  - ai-agents
  - tool-calling
  - agent-evaluation
  - reward-engineering
  - vllm
  - lora
  - fine-tuning
  - openpipe
  - education
  - transcript
related_article: articles/2025-07-02_kylecorbitt_agents-mcp-rl-lesson5.md
participants:
  - Kyle Corbitt (instructor)
  - Will Brown (co-instructor)
---

# Production-Ready Agent Engineering — Lesson 5: Formulating Business Problems as RL Tasks (Lecture Transcript)

**Instructor:** Kyle Corbitt (CTO, [[entities/openpipe]])
**Co-instructor:** Will Brown (Research Lead, [[entities/prime-intellect]])
**Date:** July 2, 2025
**Companion course:** [[concepts/agents-mcp-rl-course|Production-Ready Agent Engineering: From MCP to RL]]
**Notebook (Lecture 5.5 — Will Brown):** [grpo_details.ipynb](https://raw.githubusercontent.com/willccbb/agent-engineering/refs/heads/main/lectures-1-through-4/lec5-grpo-details/grpo_details.ipynb)

---

## 1. Recap: Email Agent and the Path to Training

**[00:06:57]** We are in lecture 5 of the building real-world agents course. We're going to take this — hopefully most people here today were there for lecture 4 as well. If you missed it, we are building an email agent with the ability to get a natural language query and then use tool calls to search an inbox and hopefully give an answer.

**[00:08:18]** Today, if all goes well, we will by the end of this lecture have a model training that should hopefully beat state of the art or match state of the art on that email agent task. We won't actually have a model that does it because once we start that training process, it's going to take at least several hours, but hopefully we'll have one kicked off and we'll be able to see dashboards of the training happening.

**[00:08:53]** This is going to be mostly live coding. I will be building it as we go.

### Refactored Agent: Scenario-based Architecture

**[00:09:19]** We have this `run_agent` file. I've refactored this slightly — previously we were just asking for a question string and getting back a string answer. I've refactored this because instead of taking a question, we now have a `scenario` object. This scenario comes from our synthetic question data — the `generate_synthetic_question_data` file which goes through existing sample inboxes and creates synthetic question-answer pairs.

**[00:10:48]** This is the dataset we produced from that script: ids, question-answer pairs, the email id that is the canonical source for the answer (used later to verify correctness), and a date to make sure we're not referencing emails after the question date.

### Return Final Answer Tool

**[00:14:01]** I've added a 3rd tool: `return_final_answer`. Previously the model could call search inbox and read email tools, and when it wanted to return a final answer, it would just return content without tool calling. I switched to an explicit tool for returning the final answer because I want structured output — the answer plus reference message IDs.

**[00:15:01]** This is the kind of thing if you're building a real production application that could be really useful — like OpenAI's research interface or web search interface, it'll often cite specific sources and footnotes. This gives us the ability to build functionality like that because we're getting the exact IDs of the messages containing our answers.

**[00:15:50]** Once it returns the final answer, we end our agentic loop — we check if the tool called was `return_final_answer`, then return the result instead of continuing.

---

## 2. Judge Correctness: LM-as-Judge for Reward Signal

**[00:20:56]** The main piece we need for RL is a way to test correctness. I've defined a `judge_correctness` function that takes a scenario and the LLM-generated answer. I've got a pretty simple system prompt.

**[00:21:28]** This system prompt — the real one I have in the repository is significantly longer. It has like a rubric. You would think that answering "are these 2 about the same" is easy for an LLM. Unfortunately, there's a lot of edge cases. For example, the reference answer included extra information that's not wrong but not necessary, and my judge model was marking AI-generated answers that didn't include the same amount of reference information as wrong. I had to do prompt engineering to fix that.

**[00:22:22]** Did I manually create the prompt or use DSPy? This is manually done. You could theoretically use DSPy to optimize it, but I found it significantly faster to do the prompt engineering myself. I find the edits DSPy makes are either too specific to a situation or not capturing the nuance. That's been my personal experience.

**[00:23:23]** We ask the judge model to reason a little bit — this is mostly helpful for debugging. This is a big part of how I was able to prompt engineer the judge model: I would look at the reasoning of what it was paying attention to, then update it until it was paying attention to the right things. Then just a Boolean: accept or reject.

### Run Agent and Score

**[00:24:11]** I'm creating a wrapper function `run_agent_and_score` that takes a scenario. It runs the agent, and if the answer is none (something went wrong), it gives a score of 0. If it's not none, it judges the correctness and returns 1 if accepted, 0 if not.

**[00:25:41]** This is about the simplest reward function you can write. I'm not giving partial credit, not giving extra penalties for formatting issues, not giving more credit for using fewer turns (which is something I do in the real project to incentivize efficiency). In the next lecture we'll probably expand on this reward function and do more interesting things with it.

---

## 3. Benchmarking: Parallelized Evaluation

**[00:30:30]** The next thing to do is benchmarking. I will spend a significant fraction — maybe 50% — of the time I spend on one of these projects is benchmarking and then debugging. There's a lot of rounds of back and forth and iterating and looking at actual outputs.

**[00:34:34]** The reason everything is done with Async is to make parallelization easier. Async lets Python do other things while network operations happen. Since 99.9% of the time is spent on LLM calls, we can do all of them at the same time without multiple processes. Using `asyncio.gather` + `tqdm.asyncio` to run all scenarios in parallel.

**[00:38:03]** We got 10 results complete in 25 seconds (vs 82 seconds sequential). Not getting very good scores but it is working.

### Debugging with Weave

**[00:43:51]** The best way to debug is to actually look at model outputs. I use Langfuse and more recently Weave from Weights and Biases. Weave does monkey patching of the OpenAI SDK and LiteLLM, collecting inputs and outputs of decorated functions.

**[00:50:46]** Looking at traces: the model is being too specific with search keywords — searching for "Steven TV spots Enron" when all emails are Enron. It should find things in 2-3 searches but it's taking many more. Eventually it gets more general and finds relevant emails.

**[00:54:08]** I would spend a lot of time iterating in exactly this process: what's going wrong, what's causing it to go wrong, do I need to add a new tool, do I need to update my prompt to explain better what I'm looking for. Iterating on that to get to a better spot.

---

## 4. Building the GRPO Training Loop

**[00:56:43]** Let's figure out how to train a model with GRPO. We've got our agent, we've hopefully gotten the best performance we can from the frontier model. Now we want to train a model.

### Environment Setup

**[00:57:35]** What I like to do is run as much as possible on my local machine (benchmarking, defining the agent) because it's fast, lowest latency. When it gets to training, I need a GPU, so I'll do that remotely. Using [SkyPilot](https://skypilot.co/) — write the script, then run it on a remote machine.

**[00:58:06]** Some people SSH into a GPU workstation and do everything there. I find that not ideal because you both under and over-provision. All the stuff we've been doing so far would just be burning dollars on a GPU machine. And once things are dialed in, I often want 4 different experiments simultaneously with different hyperparameters, which a single workstation can't do.

### ART: Agent Reinforcement Trainer

**[01:01:16]** We're going to be using ART — Agent Reinforcement Trainer — the library we're working on at OpenPipe.

```
import art
model = art.TrainableModel(
    base_model="Qwen/Qwen2.5-14B-Instruct",
    project="email-agent",
    name="email-agent-v1"
)
```

**[01:01:46]** Qwen 2.5 14B Instruct is a great model. Qwen 3 is great too, but if you don't need reasoning, I haven't found a huge benefit over 2.5. The chat templates are a little bit weird.

### Backend Registration

**[01:02:42]** One of the cool things about ART is you can run the whole training loop on your local computer and just have a GPU in the cloud — send over each agent rollout (which you can do on your own computer) to the GPU for training, then call that same GPU remotely for inference.

```
with LocalBackend() as backend:
    await backend.register(model)
```

**[01:04:18]** Under the hood this spins up a vLLM server for inference on the model as we're training, and the training code to update weights. `register` tells the backend to prepare a model with this configuration — loading Qwen 2.5 14B weights, initiating a LoRA. We also support full fine-tuning (experimental), default is LoRA.

### Data Loading

```
from local_email_db import generate_database
generate_database()  # Pull ~500K emails from S3 into local SQLite

training_data = load_scenarios(split="train", limit=1000)
validation_data = load_scenarios(split="test", limit=100)
```

### Training Iterator Configuration

**[01:08:09]** A step in training: run a bunch of rollouts in parallel, once we reach enough rollouts, grab a chunk and train on all of them at once.

```
groups_per_step = 12  # Scenarios per batch
num_epochs = 3        # RL doesn't overfit fast
rollouts_per_group = 4  # Kyle's finding: smaller than typical, works well
```

**[01:08:55]** Groups per step = how many different scenarios we run in parallel every step. I've played around with this and 12 worked well. RL doesn't overfit that fast so 3 epochs is fine.

### Trajectory Groups and Rollouts

**[01:12:28]** We have this concept of a **trajectory** — it tracks what happened in a specific agentic run. This is super important for training. We have to track exactly what the LLM was called with every time, because the way training works is it takes that message history, all the tokens the LLM produced, and the score, and uses that for training. The tokens produced need to be either up-weighted or down-weighted based on the score.

**[01:13:30]** We're going to create our own subclass of `Trajectory` to add our `final_answer` field.

```
@dataclass
class EmailAgentTrajectory(art.Trajectory):
    final_answer: str | None = None
```

**[01:16:59]** One of the things you need for reinforcement learning is the log probs — the probability of each token produced. To avoid recalculating log probs in the backend during training, we keep the entire choice object (not just the message, but the message plus additional information including per-token probabilities). This makes the training process faster.

### The Full Training Loop

```python
async def train():
    generate_database()
    training_data = load_scenarios(split="train", limit=1000)
    validation_data = load_scenarios(split="test", limit=100)

    model = art.TrainableModel(
        base_model="Qwen/Qwen2.5-14B-Instruct",
        project="email-agent",
        name="email-agent-v1"
    )

    with LocalBackend() as backend:
        await backend.register(model)

        training_iterator = iterate_dataset(
            training_data,
            groups_per_step=12,
            num_epochs=3
        )

        for batch in training_iterator:
            groups = []
            for scenario in batch:
                for _ in range(rollouts_per_group):
                    groups.append(
                        art.TrajectoryGroup(
                            trajectories=[run_agent_and_score(model, scenario)]
                        )
                    )

            finished_groups = await gather_trajectory_groups(groups)
            await model.train(finished_groups)
```

**[01:29:15]** What `train` does: it takes these groups, sends them to the GPU, does the training, and updates the model weights. As soon as this is done, we come back to the next iteration, and now the model we're using for inference is a slightly different version because we just trained it.

---

## 5. Running the Training Job Remotely

**[01:30:35]** Using SkyPilot to define the runtime environment — installing UV, running `uv run train.py`, pulling the local `.env` file, and defining task requirements (requesting an H100). SkyPilot finds a cloud with those requirements. Has auto-stop so the GPU doesn't consume resources forever when the task finishes.

---

## 6. Q&A and Discussion

### Temperature and Hyperparameters

**[01:32:41]** LiteLLM uses temperature 1 by default, which is what I recommend. If you don't use temperature 1, the math gets weird. I've used defaults for everything else and had pretty good luck.

### GRPO vs PPO

**[01:19:17]** (Will Brown) GRPO has become the default for our experimentation at small to medium scales. PPO requires a lot more memory and is probably what they're using to train ChatGPT or something like that. It's much harder to get it to work well at small scales than GRPO.

### Rollout vs Trajectory

**[01:18:30]** A trajectory is just the trace of a rollout. A rollout is the process of the model going through, and the trajectory is the final produced result — all the messages and the score associated with it.

### Caching Strategy

**[01:36:42]** Caching is fine for prompted models (takes into account all inputs). Caching is bad for models under training — if you use the same scenario on a new model, you don't want it cached. Multiple rollouts on the same model should be independent.

### What Goes in Trajectories?

**[01:37:43]** The main things: **history** (messages and choices — the agentic flow), **inputs**, **outputs** (assistant messages that the model produced), and **reward**. You can also set additional metrics (useful for seeing what's going well/poorly) and metadata for filtering in logs. In the next version, you'll be able to have sub-agents with multiple independent histories.

### What to Put in Prompt vs What to Learn

**[01:50:07]** I put as much in the prompt as I can — it's easy, it's cheap. If there's something the model needs to know, I'll throw it in the prompt. What I won't do is put in giant blocks of in-context examples (which people sometimes do with pure prompt engineering). That's the stuff it should be able to learn, and I want to save the tokens.

### Metrics to Monitor During Training

**[01:46:05]** The most important metric is whatever your downstream metric is — in this case `validation/answer_correct`. Then the reward as a proxy.

**[01:48:12]** **Reward standard deviation** and **entropy**: if these get too low (dropping to 0), the model is giving almost the same answer every time — it's too collapsed and won't learn anything new. There's no difference for the algorithm to operate on.

Task-specific metrics: did it ever read the right email? Did it ever call a search that gave the right email in results? Did it answer incorrectly with the correct source?

### Prompt Engineering vs Training

**[01:39:14]** The biggest reason to benchmark first is because oftentimes when your model's underperforming, it's because of some obvious missing thing — a missing tool, running out of context. It's much easier to debug with benchmarking. Also, prompt engineering can do as good or better job as model training, and it's way faster.

---

## Related

- [[concepts/agents-mcp-rl-course|Production-Ready Agent Engineering: From MCP to RL]]
- [[raw/articles/2025-07-02_kylecorbitt_agents-mcp-rl-lesson5]]
- [[concepts/grpo-rl-training]]
- [[concepts/agentic-rl]]
- [[concepts/corbett-kyle-corbitt]]
- [[entities/will-brown]]
- [[concepts/reward-hacking]]
- [[raw/articles/2025-04-14_corbt_art-trainer-new-rl-trainer]]
- [[raw/articles/2025-04-29_corbt_art-e-mail-agent]]
