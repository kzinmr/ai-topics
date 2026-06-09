---
title: "Reinforcing Recursive Language Models"
author:
  - Daniel Kim
  - Rehaan Ahmad
published: 2026-05-13
captured: 2026-06-09
source_url: "https://www.alphaxiv.org/blog/reinforcement-learning-for-rlms"
type: blog-post
tags:
  - reinforcement-learning
  - recursive-language-models
  - RLM
  - agents
  - GRPO
  - SFT
  - LLM
  - inference-scaling
  - evidence-selection
  - SkyRL
---

# Reinforcing Recursive Language Models

_We RL fine-tune small (4B) models to behave as native recursive language models (RLMs) by training parent and child RLMs under a single, shared policy. With RL, small models can learn task-specific, RLM behavior that cannot be elicited through prompting or even SFT. This blog assumes a basic level of familiarity with RLMs. A great resource for learning about them is the[original RLM blog post](https://alexzhang13.github.io/blog/2025/rlm/)._


We investigate RL fine-tuning 4B models to be used as RLMs in production settings. While RLMs are a powerful inference strategy, they can have unpredictable latency and can require extensive prompt tuning to elicit consistent behavior. RL fine-tuning allows us to train purpose-built RLMs that are cheap to deploy.

Rather than training separate policy models for parent and child RLMs, we train one model to play both roles of a parent decomposer and child sub-agent. We use a simple RL training setup where rollouts from children RLMs inherit the advantages of rollouts of the parent RLMs that spawned them, which allows us to train a single policy. This eliminates the need for additional reward signals for individual child RLM trajectories.

On an evidence selection task over several scientific documents, we show that an RL fine-tuned 4B model performs just as well as Claude Sonnet 4.6 with an identical RLM harness and REPL environment, all while being a fraction of the size and cost.

[Our code](https://github.com/NovaSky-AI/SkyRL/pull/1596), which includes training scripts, our implementation of the RLM scaffold, and our evidence selection environment, is available on [SkyRL](https://github.com/NovaSky-AI/SkyRL).

## What is a Recursive Language Model?

RLMs [1] spawn language models (LMs) inside a programmatic environment that stores long user prompts (context), which are traditionally fed directly into the context window of an LM. In this environment, the context is an external object that the LM can inspect through programmatic operations and decompose by recursively calling itself with the ultimate goal of answering some user query about the context.

Like the original RLM paper, we use a Python Read-Eval-Print-Loop (REPL) as our environment. Rather than treating code execution as just another tool, RLMs in a REPL make code the primary interface through which the model inspects and transforms data. Every turn, the model writes code it wants to execute, the REPL executes the code, and the RLM orchestrator returns the results of the executed code (primarily `print()` statements) as a user message back to the model for the next turn.

The REPL exposes a set of built-in functions to the model:

  * **`FINAL(answer)`** / **`FINAL_VAR(variable_name)`** — Marks the end of the rollout: `FINAL(...)` returns the literal string as the final answer, while `FINAL_VAR(...)` looks up an existing REPL variable by name and returns its value.
  * **`rlm_query(prompt, context=None)`** — Spawns a single child RLM rollout with the given prompt (and optional context override), running a fresh agent loop under the same policy, and returns the child's final answer string back into the parent's REPL.
  * **`rlm_query_batched(prompts, context_list=None)`** — Same as `rlm_query` but dispatches multiple children in parallel (one per prompt, paired with the corresponding context) and returns a list of their final answers in order.


The ability to interact with context programmatically and spawn sub-RLMs or sub-LMs makes RLMs a very powerful inference strategy for tackling long context problems.

## Evidence Selection

For this blog, we'll focus on the task of evidence selection from scientific documents. Given a question and a set of arXiv papers, the objective is to return snippets from the papers that answer the question. The context that is stored in the REPL for this task is the full text of all of the papers in the set for a given question.

In the single paper case, consider the following question about the original RLM paper: _What baselines are used for this paper?_ A simple strategy that the RLM can use is to call a keyword search function with the term "baseline" over the context, analyze the matches, and return the most relevant snippets.

When extending this to multiple papers, it's clear the task can be decomposed and parallelized with sub-RLMs. An obvious approach is to have the root RLM identify which papers are worth further exploring and spawn sub-RLMs to extract snippets from individual papers. One point worth highlighting here is that the benefits of RLMs extend beyond just long-context tasks. This particular task doesn't have an incredibly long context to begin with (experimenting with several hundred papers is something we want to try), but it is highly parallelizable. Not only does embracing the parallelizable nature of the task improve wall-clock time, but it actually also improves task performance. Several works show that sequential reasoning [2] throws LLMs into the "prefix" trap, which is where the model ends up exploring whatever it first explores.

An important distinction here from other tasks that RLMs have typically been evaluated on is that the root RLM spawns true sub-RLMs that have access to a REPL environment. For other datasets like OOLONG, RLMs have only been trained to make sub-LM calls to an external, frozen model.

To abstract away certain basic operations, we initialize REPL environments with four predefined functions:

  * `list_papers(ctx)` Iterates through every paper in the context dict and prints each paper's ID, title, and abstract. Returns the list of titles.
  * `search(text, keyword, window=300, bidirectional=True)` Case-insensitive keyword search that returns sentence-aligned snippets around each hit. If `text` is a dict it searches every paper and groups results by paper ID, otherwise it searches a single string.
  * `extract_section(snippet, start_phrase, end_phrase)` Pulls out the substring of `snippet` that begins at `start_phrase` and ends at `end_phrase` (inclusive, case-insensitive). If either phrase isn't found it falls back to the start of the snippet or runs to the end.
  * `get_paper_abstract(ctx, paper_id)` Looks up one paper in the context dict and returns a formatted "Paper ID / Title / Abstract" string, used to tag child prompts so the worker knows which paper it's processing.


These predefined functions are analogous to tool calls in traditional multi-turn, ReAct agent loops.

## Dataset

We generate scientific queries and supporting evidence synthetically. We start by selecting a random paper on alphaXiv and then retrieve up to 9 semantically similar papers to form a group, with preference given to high-upvoted papers. From there, an OCR model breaks each paper from the group into paragraphs and we have a frontier model generate questions and select the relevant paragraphs from a subset of papers for that question. Not every paper in the group has paragraphs relevant to the question. The OCR model is used only to build clean ground-truth evidence. At test time, the model sees noisy text from a PDF-parsing library, mimicking production settings where running OCR on every new document is unwieldy and expensive. In all, we synthetically generate 1000 queries over groups of up to 10 papers, with up to three queries per group.

Another point to make clear is that RAG is a poor fit for this task. The model needs to dynamically return verbatim spans of varying length and count, not a fixed-size top-k. RAG and RLMs aren't mutually exclusive though, indexed chunks could be exposed as just another REPL tool alongside search and extract_section.

## Training

The original RLM paper SFTs Qwen3-8B with RLM-like reasoning trajectories from Qwen3-Coder-480B-A35B-Instruct. The purpose of SFT is to teach the model how to navigate a REPL environment, including RLM-specific syntax for submitting an answer and making sub-LM calls. However, SFT was not used to train RLMs for a specific task or dataset.

For reasoning models and traditional agent harnesses, RL has proven to be a robust way to improve the capabilities of a model for a specific task without the catastrophic forgetting that accompanies pure SFT-based approaches. How can we extend this to RLMs?

### RLM (no sub-calls)

Before considering the recursive element of RLMs, we want to first confirm we can RL fine-tune Qwen3.5-4B on the single-paper variant of our evidence selection task, which doesn't involve spawning child RLMs. There are a couple of takeaways from these initial runs that are worth sharing.

**Task Strategy.** The specific task strategy has to be in the prompt. This includes descriptions of predefined functions to guide the RLM and expedite rollout generation. For the single-paper task, the strategy is searching the paper with multiple keyword variants using `search`, expanding the most promising snippets with refined `search` calls, and then submitting final answers with `extract_section`, all across 5-7 turns. Without an explicit strategy, even a frontier model like Sonnet 4.6 will take 90 seconds to generate a rollout compared to 30 seconds when given a strategy.

**Cold-start SFT.** While this may not be needed with larger models, the RLM harness is tricky enough that even with a good prompt and predefined tools, Qwen3.5-4B will have 0 pass@16 scores. RLM-based tasks are outside the edge of competence [3] for most small models.

When training without an SFT phase, we observed many of the same failure modes observed in the original RLM paper, which include using the wrong syntax to submit final answers and excessive reasoning and tool calls that would bloat the model's context window across turns.

For the SFT phase itself, we use the same methodology from [1]. We generated teacher RLM rollouts with Qwen3.5-397B-A17B on the same evidence selection task and filtered out rollouts that either contained REPL errors or scored zero F1 on character-span overlap between retrieved evidence snippets and gold evidence snippets. Our SFT dataset was a small, held-out portion of the RL dataset of a few dozen examples. In initial runs, we found that doing SFT on traces produced over the entire RL training dataset (even though it isn't a large dataset) led to entropy collapse and subsequent instability [4][5].

**Stepwise Training.** Another nuance of the RLM scaffold is that successive turns do not share prefixes. The user prompt is not part of the persistent chat history and is instead appended before each turn. The point of this is to ensure the original user query is not buried deep into the context window of the model and that the RLM is reminded of its task.

Because the per-turn user prompt is rewritten rather than accumulated, you cannot use a rollout as a single training example. Each turn has to be a separate training sample, so a rollout of N turns produces N samples. For advantage calculation, only rollouts corresponding to the last step of trajectories are included in the GRPO group, and the advantage is broadcast to rollouts from previous turns. See more about step-wise RL training [here](https://github.com/NovaSky-AI/SkyRL/issues/1278).

**LLM Judges.** We use rubric-based LLM judges for reward assignment. We initially tried verifiable rewards like F1 of selected snippets, but this proved to be very noisy. Questions like "Which method scores the best on X baseline?" could be answered with several selections of text, some of which weren't included in our labels. We experienced a similar issue in our [previous work on retrieval agents](https://www.alphaxiv.org/blog/training-retrieval-agents-for-arxiv-search). To circumvent this, we used rubric-based LLM judges that were provided with the original query, the ground truth text, and the predicted text. Rubric-based judges have been shown to be more robust to reward hacking [6][7]. A great overview of rubric-based rewards by Cameron Wolfe can be found [here](https://cameronrwolfe.substack.com/p/rubric-rl).

With these considerations, RL fine-tuning yields significant improvements on the single-paper task, with eval judge scores jumping from around 0.6 to 0.8 with Qwen3.5-4B.

Note that because we RL on top of an SFT model, training begins at 0.6 reward rather than zero, demonstrating the importance of a cold-start SFT phase.

### RLM (with sub-calls)

Now let's consider the multi-paper case, which requires a true RLM with recursive sub-calls. We want the root RLM to identify which papers are worth dispatching child RLMs to, and child RLMs should extract the relevant passages from their assigned paper.

It might be tempting to train separate policies for root and children RLMs. However, this would require two sets of reward signals and an unwieldy training pipeline to train two policies. Alternatively, we can use a frozen model for sub-calls and only train a model for the root RLM, which is the approach taken by the original RLM paper. However, given that an SFT 4B model is unable to perform the child task successfully, some form of on-policy training is necessary. We devise a training objective and an RL training setup that can generalize across different RLM tasks and enables a single policy to effectively learn both root and child RLM roles.

**Put simply.** Advantages are computed for root RLM rollouts using standard GRPO. Each child rollout inherits the advantage of its parent root, and child contributions to the loss are averaged (divided by kgk_gkg​, the number of children in that rollout) so no single root is overweighted for spawning more sub-calls.

**Or more formally.** For each query xxx in the batch, sample a group of GGG root rollouts:

{yg}(g=1)G∼πθold(⋅∣x)\lbrace y_g \rbrace_{(g = 1)}^G \sim \pi_{\theta_{\text{old}}}(\cdot \mid x){yg​}(g=1)G​∼πθold​​(⋅∣x)

Each root RLM rollout ygy_gyg​ deterministically induces a set of child prompts ϕ(yg)={xg,i}i=1kg\phi(y_g) = \lbrace x_{g,i} \rbrace_{i=1}^{k_g}ϕ(yg​)={xg,i​}i=1kg​​ via its `rlm_query` or `rlm_query_batched` calls, and children are sampled from the same policy:

yg,i∼πθold(⋅∣xg,i),i=1,…,kgy_{g,i} \sim \pi_{\theta_{\text{old}}}(\cdot \mid x_{g,i}), \quad i = 1, \dots, k_gyg,i​∼πθold​​(⋅∣xg,i​),i=1,…,kg​

**Advantage Calculation.** Only root RLM rollouts receive a verifiable reward rg=R(x,yg)r_g = R(x, y_g)rg​=R(x,yg​). Group-relative advantages are computed over the GGG root rollouts:

Ag=rg−mean ⁣({rg′}g′=1G)std ⁣({rg′}g′=1G)A_g = \dfrac{r_g - \text{mean}\\!\left(\lbrace r_{g'} \rbrace_{g'=1}^G\right)}{\text{std}\\!\left(\lbrace r_{g'} \rbrace_{g'=1}^G\right)}Ag​=std({rg′​}g′=1G​)rg​−mean({rg′​}g′=1G​)​

**Advantage Inheritance.** For simplicity, we have every child of ygy_gyg​ inherit ygy_gyg​'s advantage.

Ag,i:=Agfor all i=1,…,kgA_{g,i} := {A_g} \quad \text{for all } i = 1, \dots, k_gAg,i​:=Ag​for all i=1,…,kg​

**GRPO Objective.** Let

ρθ(y∣x)=πθ(y∣x)πθold(y∣x)\rho_\theta(y \mid x) = \dfrac{\pi_\theta(y \mid x)}{\pi_{\theta_{\text{old}}}(y \mid x)}ρθ​(y∣x)=πθold​​(y∣x)πθ​(y∣x)​

denote the per-token importance ratio (token index suppressed for clarity).

The GRPO objective extended over the RLM tree is:

J(θ)=Ex,{yg},{yg,i}[1G∑g=1G(Lgroot(θ)⏟root rollout+1kg∑i=1kgLg,ichild(θ)⏟child rollouts)]−β DKL[πθ∥πref]\mathcal{J}(\theta) = \mathbb{E}_{x, \lbrace y_g \rbrace, \lbrace y_{g,i} \rbrace} \Bigg[ \dfrac{1}{G} \sum\limits_{g=1}^{G} \Bigg( \underbrace{\mathcal{L}_g^{\text{root}}(\theta)}_{\text{root rollout}} + {\color{red}\dfrac{1}{k_g} \sum\limits_{i=1}^{k_g} \underbrace{\mathcal{L}_{g,i}^{\text{child}}(\theta)}_{\text{child rollouts}}} \Bigg) \Bigg] - \beta \, \mathbb{D}_{\text{KL}}[\pi_\theta \| \pi_{\text{ref}}]J(θ)=Ex,{yg​},{yg,i​}​[G1​g=1∑G​(root rolloutLgroot​(θ)​​+kg​1​i=1∑kg​​child rolloutsLg,ichild​(θ)​​)]−βDKL​[πθ​∥πref​]

where each per-rollout clipped surrogate is

Lgroot(θ)=1∣yg∣∑t=1∣yg∣min⁡(ρθ(yg(t))Ag, clip(ρθ(yg(t)),1−ϵ,1+ϵ)Ag)\mathcal{L}_g^{\text{root}}(\theta) = \dfrac{1}{|y_g|} \sum\limits_{t=1}^{|y_g|} \min\Big( \rho_\theta(y_g^{(t)}) A_g, \; \text{clip}(\rho_\theta(y_g^{(t)}), 1-\epsilon, 1+\epsilon) A_g \Big)Lgroot​(θ)=∣yg​∣1​t=1∑∣yg​∣​min(ρθ​(yg(t)​)Ag​,clip(ρθ​(yg(t)​),1−ϵ,1+ϵ)Ag​)

Lg,ichild(θ)=1∣yg,i∣∑t=1∣yg,i∣min⁡(ρθ(yg,i(t))Ag,i, clip(ρθ(yg,i(t)),1−ϵ,1+ϵ)Ag,i)\mathcal{L}_{g,i}^{\text{child}}(\theta) = \dfrac{1}{|y_{g,i}|} \sum\limits_{t=1}^{|y_{g,i}|} \min\Big( \rho_\theta(y_{g,i}^{(t)}) A_{g,i}, \; \text{clip}(\rho_\theta(y_{g,i}^{(t)}), 1-\epsilon, 1+\epsilon) A_{g,i} \Big)Lg,ichild​(θ)=∣yg,i​∣1​t=1∑∣yg,i​∣​min(ρθ​(yg,i(t)​)Ag,i​,clip(ρθ​(yg,i(t)​),1−ϵ,1+ϵ)Ag,i​)

Note that we add a normalization term 1kg\frac{1}{k_{g}}kg​1​ when summing the loss contributions of the child RLM rollouts. This is to ensure that the contribution across all depths of the RLM is balanced. Without normalization, child rollouts dominate the gradient update when kg≫1k_g \gg 1kg​≫1.

While the training objective above assumes a max RLM depth of 1, this objective can be expanded to any RLM depth with a nice recursive structure. For a given RLM trajectory yyy, the recursive subtree loss is:

Lsubtree(y,A)=Lnode(y,A)+1ky∑i=1kyLsubtree(yi,A)\mathcal{L}_{\text{subtree}}(y, A) = \mathcal{L}_{\text{node}}(y, A) + \frac{1}{k_y} \sum_{i=1}^{k_y} \mathcal{L}_{\text{subtree}}(y_i, A)Lsubtree​(y,A)=Lnode​(y,A)+ky​1​∑i=1ky​​Lsubtree​(yi​,A)

where {xi}i=1ky\lbrace x_i \rbrace_{i=1}^{k_y}{xi​}i=1ky​​ is the set of child RLM prompts dispatched by yyy, AAA is the advantage assigned to yyy, and each child RLM rollout is sampled by yi∼πθold(⋅∣xi)y_i \sim \pi_{\theta_{\text{old}}}(\cdot \mid x_i)yi​∼πθold​​(⋅∣xi​).

The rationale behind having children inherit their parent trajectory's final advantage is the same rationale behind assigning every token the same sequence-level advantage in GRPO, even though different tokens make different contributions to the sequence-level advantage. This is an unbiased estimator of the true gradient that, with sufficient training steps, yields stable results.

Alternatively, if the child RLM rollouts are highly repetitive, you can randomly sample one to contribute to the gradient instead of averaging across all kgk_gkg​. While this approach can speed up training, it can also be very noisy.

j∼Uniform(1,…,kg)j \sim \text{Uniform}(1, \dots, k_g)j∼Uniform(1,…,kg​)

J(θ)=Ex,{yg},{yg,i}[1G∑g=1G(Lgroot(θ)⏟root rollout+Lg,jchild(θ)⏟sampled child)]−β DKL[πθ∥πref]\mathcal{J}(\theta) = \mathbb{E}_{x, \lbrace y_g \rbrace, \lbrace y_{g,i} \rbrace} \Bigg[ \dfrac{1}{G} \sum\limits_{g=1}^{G} \Bigg( \underbrace{\mathcal{L}_g^{\text{root}}(\theta)}_{\text{root rollout}} + {\color{red}\underbrace{\mathcal{L}_{g,j}^{\text{child}}(\theta)}_{\text{sampled child}}} \Bigg) \Bigg] - \beta \, \mathbb{D}_{\text{KL}}[\pi_\theta \| \pi_{\text{ref}}]J(θ)=Ex,{yg​},{yg,i​}​[G1​g=1∑G​(root rolloutLgroot​(θ)​​+sampled childLg,jchild​(θ)​​)]−βDKL​[πθ​∥πref​]

## Results

For the final multi-paper RLM training runs, we train on an SFT Qwen3.5-4B model. Training is done on a single 8xH200 node with a batch size of 16 and 8 samples per prompt. With up to 4 child RLMs per parent, generation can hit 512 concurrent rollouts, which initially surfaced race conditions around REPL timeouts for child RLMs. After fixing these, we observe a consistent and stable reward curve.

Through RL post-training the 4B model, the average rubric score jumps from 0.3 to 0.6 on the training dataset. On the eval dataset, the fine-tuned RLM stacks up well against other frontier models using the same RLM scaffold.

While short of Sonnet's 0.607 average rubric score, the wall-clock time of an RLM query from our model is 7 seconds on a single node, whereas Sonnet-based RLMs take over 60 seconds.

As mentioned in the step-wise section above, during RL fine-tuning we maintain the same scaffold as the original RLM paper, where the user query is moved to the end of the conversation history across turns. This means different turns do not share the same prefix. Additionally, we maintain lengthy prompts that describe the strategy in detail. While this was necessary to get good results for models out-of-the-box that were not trained to behave as RLMs, it should ideally not be required if we are RL fine-tuning. As an ablation, we try training with a significantly reduced prompt (200 tokens instead of 1500 tokens), keeping the user query right after the system prompt.

Training with this setup converges slightly below the original run and is generally more unstable (this can likely be fixed with simple curriculum learning, though that is outside the scope of this blog). This experiment gives us a sense of why RLM training is useful beyond optimizing specific tasks. Today's models need elaborate strategy prompts because none of them natively understand the RLM role. The long-term goal is an RLM where the prompts can simply describe the sub-calls and high-level task.

## What's Next

**Task Exploration.** We've chosen this particular task selfishly for our own production needs. Beyond evidence selection, there's a whole world of tasks worth exploring with RLM training. If RLMs are indeed next in the line of popular inference scaling techniques that have previously included CoT and ReAct, the training story will matter. Taking CoT as an example, even though researchers found improvements when prompting to induce better CoT reasoning [8], it was RL fine-tuning that ultimately worked best [9]. We will be curious to see what the "A-ha!" moment will look like when RL fine-tuning RLMs at scale.

**Reward Assignment.** We have chosen to have children RLM rollouts inherit the advantage of their parents. While this is an effective estimator, more fine-grained credit assignment can lead to faster convergence. For our given evidence selection task, we could score root RLM rollouts by the F1 score of the papers they select to dispatch child RLMs to and score child RLMs with LM judges based on the snippets they select. While reward assignment depends heavily on the specific task, we would like to do more experiments with multi-tiered reward calculations across the RLM tree.

**Strategy Discovery & Scale.** One limitation that we've assumed about RLMs in this blog post is that they need an explicit task strategy detailed in the system prompt. For various datasets and tasks, RLMs are typically deployed with environment-specific tips that explain how the RLM should decompose its context and formulate its answer.[[10]](https://www.primeintellect.ai/blog/rlm)

However, explicitly providing a strategy may be a hindrance when training larger, more capable RLM-native models. Traditional reasoning models for math or coding are trained without supplementing them with tips and strategies, so why should we include them with RLMs? The big unlock with RLMs will be when they themselves discover new strategies that humans would have not come up with for decomposing and solving truly difficult, long-context problems. Scaling RLMs to model sizes where strategy discovery, not execution, is the main task of training will be the next big milestone for RLMs.

## Try it out

You can find the [training configs](https://github.com/NovaSky-AI/SkyRL/blob/main/examples/train/rlm/run_multi_paper_rlm.sh) we used in the official [SkyRL repo](https://github.com/NovaSky-AI/SkyRL). We've added an [RLM environment](https://github.com/NovaSky-AI/SkyRL/blob/main/skyrl-gym/skyrl_gym/envs/rlm/env.py) and encourage you to play around with it and try it on other tasks. Most training was done with an 8xH200 node.

## Acknowledgements

We'd like to thank [Sumanth Hegde](https://sumanthrh.com/) and [Charlie Ruan](https://www.charlieruan.com/) from the SkyRL team for their responsiveness in resolving issues and for providing an amazing RL library for the community. We'd also like to thank [Alex Zhang](https://alexzhang13.github.io/) for his work on the original RLM paper as well as for providing feedback throughout this project!

## References

  1. [1][Recursive Language Models](https://www.alphaxiv.org/abs/2512.24601) — Zhang et al.
  2. [2][Native Parallel Reasoner: Reasoning in Parallelism via Self-Distilled Reinforcement Learning](https://www.alphaxiv.org/abs/2512.07461) — Wu et al.
  3. [3][On the Interplay of Pre-Training, Mid-Training, and RL on Reasoning Language Models](https://www.alphaxiv.org/abs/2512.07783) — Zhang et al.
  4. [4][Scalpel vs. Hammer: GRPO Amplifies Existing Capabilities, SFT Replaces Them](https://www.alphaxiv.org/abs/2507.10616) — Rajani et al.
  5. [5][Learning While Staying Curious: Entropy-Preserving Supervised Fine-Tuning via Adaptive Self-Distillation for Large Reasoning Models](https://www.alphaxiv.org/abs/2602.02244) — Wang et al.
  6. [6][Curing Miracle Steps in LLM Mathematical Reasoning with Rubric Rewards](https://www.alphaxiv.org/abs/2510.07774) — Yuan et al.
  7. [7][Rubrics as Rewards: Reinforcement Learning Beyond Verifiable Domains](https://www.alphaxiv.org/abs/2507.17746) — Gunjal et al.
  8. [8][Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://www.alphaxiv.org/abs/2201.11903) — Wei et al.
  9. [9][DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://www.alphaxiv.org/abs/2501.12948) — DeepSeek-AI et al.
  10. [10][Recursive Language Models: the paradigm of 2026](https://www.primeintellect.ai/blog/rlm) — Prime Intellect
