---
title: "Introducing FrontierHarness Eval v1.1 — What is the best harness for each model?"
source: "https://runta.com/blog/introducing-frontierharness-eval-v1-1/"
author: "Shilin Zhu / Guanlan (Runta), with Baseten"
published: 2026-11-17
fetched: 2026-11-18
type: article
sha256: 6ac74140816d6dff3c1e7ba036dde2425e0ad140aad058e555f63d61b4f54a32
---

We partnered with Baseten to build the largest-scale harness leaderboard using 83B tokens across 27,280 agent runs. We wanted to answer two questions: when you switch your model, should you consider switching the harness too? What is the best harness for each model? 
 Previously, our v1.0 FrontierHarness leaderboard ranked harnesses on a single model, Kimi K3. 
 V1.1 expands the benchmark to 22 harnesses × 5 models × 62 tasks × 4 attempts, 76× the size of v1.0. 
 Through our experiments, we found that you should consider switching harnesses when switching models to maximize your experience. 
 Each model had a different best-value (pass rate vs. cost) harness: Codex CLI with GLM-5.3, Pi with GLM-5.3 Flash, ZCode with DeepSeek V4.1 Flash 1017, Oh My Pi with Muse and Alma with Kimi-K3. Cost ranks moved far between models. 
 By cost per task, the median harness moved 11 of 22 places, and Codex CLI went from 1st with GLM-5.3 to 16th with Kimi-K3. 

 Result 
 Figure 1. Cost per task and pass rate of each harness 
 Each point is one harness: further left is a lower average cost per task, and higher is a higher pass rate. The orange line joins the harnesses that no other harness beats in both cost and pass rate. Select a model to filter all figures of this post. 

 This figure is interactive and needs JavaScript. 

 Over all models, four harnesses are on the line: OpenCode v2 (lowest cost per task, $0.561), Pi, Codex CLI and ZCode (highest pass rate, 61.9%). The others cost up to 1.6 times as much and passed 50.6% to 60.2%. 
 Each card names the best-value harness for one model: the lowest cost per pass, unless another harness costs at most 30% more per pass and passes at least 5 points more often. This rule picked ZCode over OpenCode v1 with DeepSeek (25% more cost, 7.7 more points) and Alma over Oh My Pi with Kimi-K3 (9% more cost, 6.5 more points). 

 Why We Built FrontierHarness Eval v1.1 
 V1.0 ran nine harnesses with one model. Their pass rates were within 17 points of each other, but the median cost per pass differed by 17 times. We thought that this came mostly from the pair of harness and model: a harness that is cheap with one model can be expensive with another. 
 V1.1 runs each harness with five models. 

 What We Tested 
 Harnesses. 18 harnesses. The four DeepSeek Harness profiles have different tool sets, and OpenCode ran at two versions. Each counts separately: 22 configurations. Table 2 in the appendix gives their versions. 
 Models. Baseten served all five: GLM-5.3 ( zai-org/GLM-5.3 ), GLM Flash ( zai-org/GLM-5.3-Flash ), DeepSeek ( deepseek-ai/DeepSeek-V4.1-Flash-1017 ), Muse ( meta-models/muse-spark-open ) and Kimi-K3 ( moonshotai/Kimi-K3 ). 
 Tasks. 62 terminal tasks. The time limits are those of the tasks, from 15 minutes to 8 hours. 

 Setup and Scoring 
 Configuration and Runtime 
 We ran the Harbor evaluation with each harness’s default settings, because we think this is closest to how people use a harness every day. Each harness used the same version and settings with all models, at the maximum reasoning effort. 
 Figure 2. How Harbor and Runta divide the work in each trial 

 Each trial gets a new Runta runtime, which is deleted at the end. Thus no trial can see the files of an earlier trial. 
 Scoring Method 
 Table 1. Methodology 

 This figure is interactive and needs JavaScript. 

 A cell is one harness and model pair. We use the two cost metrics of our dashboard : 

 Average cost per task: the mean cost of the priced trials of each task, then the mean over the tasks. Figure 1 and the cost ranks use it (Figures 4 and 5). 
 Cost per pass: the average cost per task divided by the pass rate. The best-value harness uses it (Figures 3, 6 and 7). 

 We pick the best value by cost per pass because we want harnesses at the top left of a chart of pass rate against cost per task: a high pass rate at a low cost. Draw a line from the origin to the point of a harness. Its slope, pass rate ÷ cost, is the passes per dollar. Cost per pass is the inverse of this slope, so the lowest cost per pass has the steepest line. 
 Audits of the trial logs flagged 216 trials for reward hacking, and 163 of them were online lookups. These trials score 0. Table 3 in the appendix gives the count for each harness and model. 

 Results by Model 
 Figure 3. Cost and pass rate of each harness with each model 

 This figure is interactive and needs JavaScript. 

 A deeper cell costs less than the others in its column. Codex CLI was the cheapest per pass with GLM-5.3, $0.803, but 12th with Muse and 10th with Kimi-K3. Over all models, it cost the least per pass, $0.937, and Antigravity CLI the most, $1.63. 
 How Sure Are These Results? 
 We drew the 62 tasks again 4,000 times and chose the best-value harness each time. Codex CLI stayed first with GLM-5.3 in 99.6% of the draws. The other four winners are the most likely of several close harnesses: Oh My Pi with Muse (53%), ZCode with DeepSeek (47%), Pi with GLM Flash (42%) and Alma with Kimi-K3 (25%). 

 The Harness Changes the Cost 
 The model sets the general level of the cost, because the list prices of the models differ by 20 times or more (Figure 9). We took the average cost per task of the 110 cells on a log scale, so that a doubling counts the same with each model. A two-way analysis of variance divides the spread of these costs into three parts: 

 Model, 92.8%: the differences between the five models. 
 Harness, 2.3%: the part of the effect of a harness that is the same with every model. 
 Pair, 4.9%: the rest. It also contains noise, because each cell has one value. 

 So with the model fixed, 68% of the variation between harnesses (4.9 of 7.2 points) depends on the pair, or is noise. 
 With the Model Fixed, the Harness Changes the Cost by 1.8 to 5.0 Times 
 Figure 4. Lowest-cost and highest-cost harness for each model 
 Each row is a model, on a log scale of average cost per task. The ratio divides the highest cost by the lowest. 

 This figure is interactive and needs JavaScript. 

 To test for chance, we shuffled the trials between the harnesses of each model 300 times and calculated the ratio again. “Chance” is the median of these ratios, 1.2 to 1.8 times. All five real ratios are larger than every shuffle (p = 0.003), so the spread comes from the harnesses, not from the noise of reruns. The largest is with DeepSeek: Cline CLI cost 5.0 times as much as OpenCode v1, for 2.0 more points. With the other models, the cheapest harness per task was at most 0.4 points behind the most expensive one. 
 The Cheapest Harness per Task Changes With the Model 
 Figure 5. Cost rank of each harness with each model (1 = lowest cost per task) 
 Each line is a harness, with the cheapest at the top. The five highlighted lines are the cheapest harnesses per task with GLM-5.3, GLM Flash, DeepSeek, Muse and Kimi-K3. 

 This figure is interactive and needs JavaScript. 

 Codex CLI was 1st with GLM-5.3 and 16th with Kimi-K3. DeepSeek Harness: Creator moved the most, from 1st with Muse to 21st with GLM Flash. OpenCode v1 was 1st with DeepSeek and 13th with Muse. 
 Reruns do not explain these moves. We divided the attempts into two halves and ranked the harnesses by cost in each half. With the same model, the two rankings had a mean rank correlation of 0.71. With two different models, it was 0.26. 
 A Higher Cost Does Not Give a Higher Score 
 Figure 6. Lowest and highest cost per pass for each model 
 This is Figure 4 for cost per pass. After each ratio is the rank correlation of the cost per task and the pass rate of the harnesses, from −0.39 to +0.22. A positive value means that the more expensive harnesses passed more often. 

 This figure is interactive and needs JavaScript. 

 The harness with the highest pass rate was 5th to 20th of 22 in cost per task. With four of the five models, the most expensive harness per pass passed less often than the cheapest one. 

 Does a Simpler Harness Cost Less? 
 No. We compared four factors with the cost per pass. Prompt size, tool count and cache hit rate are not the main cost factors. Steps are. 

 Start tokens: the input tokens of the first agent-loop request: the system prompt, the tool definitions and the task. 
 Tools: the tools that the first request offers. 
 Cache hit rate and steps: the mean over the passed trials. A step is one entry of the agent trajectory. 

 Figure 7. Four factors of each harness and the cost per pass 

 This figure is interactive and needs JavaScript. 

 Over the 22 harnesses, the rank correlation of the steps per pass and the cost per pass was +0.51 (p = 0.015). For the other three factors, it was −0.03 to +0.02 (p ≥ 0.88). Within each model, tool calls tracked cost as well as steps. Table 4 below and Table 5 in the appendix give the values. 
 Each step sends the context again, so a trial used 2.0 to 4.8 million input tokens on average, by harness, and the largest first request, 21,365 tokens, is less than 1% of that. mini-SWE-agent has the smallest first request, 882 tokens, but took 38 steps per pass and was 17th of 22 in cost per pass. 
 Table 4. Start tokens, tools, cache hit rate, steps and cost per pass of each harness 

 This figure is interactive and needs JavaScript. 

 Where the Cost Comes From 
 Figure 8. Inference cost of each harness, by token type or by trial outcome 

 This figure is interactive and needs JavaScript. 

 All costs are inference estimates at list prices. The pass rate of the harness on the model card has an outline. 
 Over all trials, input from the cache was 42% of the cost, output 33% and other input 25%. 
 Tokens and the Cache 
 The cache makes repeated input much cheaper. Cached input costs 2% (DeepSeek) to 20% (GLM Flash) of the price of other input (Figure 9). 
 Figure 9. List prices of each model (USD for one million tokens) 

 This figure is interactive and needs JavaScript. 

 One pair shows the effect of the cache. Cline CLI with DeepSeek (highest cost per task) read 86% of its input from the cache, and OpenCode v1 read 97%. It also sent twice as much input. Input that did not come from the cache was 57% of its cost. 
 Most of the Cost Goes to Trials That Do Not Pass 
 64.5% of the list-price cost of the scored runs went to trials that did not pass : 52.7% to failures and 11.8% to timeouts. 

 What the Best-Value Harnesses Share 
 The traces of the five best-value harnesses show three common design choices. These are observations, not tests. 
 One shell tool does most of the work. By harness, it got 61% to 93% of the tool calls. Pi’s default prompt has four tools and sends file searches to bash : 
 selectedTools: [...(input.selectedTools ?? ["read", "bash", "edit", "write"])],
addRule("Use bash for file operations like ls, rg, find");

 Each request only adds to the one before it. The start of the context does not change, so the provider reads it from the cache: 91.1% to 94.0% of input in passed trials (Table 4). But 18 of the 22 harnesses read 91% or more, so this does not separate the five. Each step pays the full input price for only about 500 new tokens: 
 # Pi, GLM-5.3, merge-diff-arc-agi-task (trial cd2f6dfd)
request prompt tokens cached tokens
 8 15,954 15,616
 9 16,351 15,936
 10 16,999 16,320

 No subagents and almost no summaries. Each of the five used a subagent in at most 6 trials, too few to tell if subagents help. Of the five, only Codex CLI summarized, in 8 trials (the 11 Alma trials in Table 6 only drop old images and reminders). Codex CLI summarizes at 90% of the window (Table 6): 
 .map(|context_window| (context_window * 9) / 10);

 The five also share a weakness. Failed runs end with a confident answer. About three in four failed trials ended with a final answer, not at the time limit: from 68% with Pi to 82% with Codex CLI. Few said that the work was incomplete: 
 # Codex CLI, GLM-5.3, cancel-async-tasks (trial 37182b0e)
Agent: - Validated with system Python, including concurrency and
 cancellation-cleanup tests.
Verifier: FAILED test_tasks_cancel_above_max_concurrent
 assert stdout.count("Cleaned up.") == 2
 AssertionError: assert 0 == 2

 Trials that did not pass took 60% (Codex CLI) to 69% (Alma) of the cost of each harness. A check before the harness stops could save part of it, but we did not test this. 

 Limitations and Future Work 

 Open models, one provider. Closed models can give different results. The cache and the prices are those of Baseten, and another provider can change the cost ranks. 

 We plan two next steps: 

 Closed models. We will add closed models, such as Claude Opus 5.5, GPT-6 Astra and Gemini 4 Carbon. 
 Long-horizon work. We will study how a harness that runs continuously in the cloud improves itself during long work. 

 Conclusion 

 When you change the model, think about changing the harness too. Test the candidate harnesses with your model on a private dataset of your own tasks, large enough to see past the noise. 
 The model sets most of the cost, and the harness is second. The model explains 92.8% of the variance of cost per task. With the model fixed, the most expensive harness cost 1.9 to 4.9 times as much per pass as the cheapest (1.8 to 5.0 times per task), so compare the cost when you pick a harness. 
 A higher cost does not buy a higher pass rate. For each model, the rank correlation of cost per task and pass rate was −0.39 to +0.22. 
 Size does not predict cost. mini-SWE-agent, the smallest harness, was 19th of 22 by cost per task over all models. 
 Most of the cost, 64.5%, went to runs that did not pass. With the five best-value harnesses, 68% to 82% of the failed runs ended with a confident final answer, not at the time limit. 
 With a cheap model that has a wide range of pass rates, pick a harness with a high pass rate. Pass rates varied by harness, from 54.0% to 69.0% with DeepSeek. But each pass rate has a 95% interval of about ±10 points, so a gap of a few points is a tie. 
 For harness developers: cut steps, not just prompt tokens. Prompt size, tool count and cache hit rate did not predict cost per pass. Steps did, because every step sends the whole context again. 

 Appendix: Reference Tables 
 Table 2. Harness configurations 

 This figure is interactive and needs JavaScript. 

 Table 3. Reward-hacked trials of each harness 

 This figure is interactive and needs JavaScript. 

 Table 5. Prompt and tools of each harness 

 This figure is interactive and needs JavaScript. 

 References 

 FrontierHarness dashboard 
 Harbor and Harbor Hub , where the ten jobs are stored 
 Introducing FrontierHarness Eval , our v1.0 results 
 Baseten , Model APIs , the inference provider for performant open models 
 Runta Harbor guide and Runta pricing 
 Runta Agent execution layer for token efficiency, secret protection, and governed access. SOC 2 Type II & ISO 27001 — in progress. View Trust Center SOC 2 · ISO 27001 © 2026 Runta Resources Docs Blog About Company Careers Trust Center Privacy policy Terms of service Social Discord GitHub X LinkedIn Contact us


## HN discussion highlights (item 50532191, 385pts)

[guanlan] Hi HN, I’m Guanlan, founder of Runta. The eval runs on our runtime, so weigh this accordingly. The short version: when you change the model, think about changing the harness too. On any one model, cost per pass varies by up to 4.4x What we ran: 22 harness configurations × 5 open-weight models × 62 terminal tasks × 4 attempts. 27,280 runs, 83B tokens. Each harness ran with default settings at maximum reasoning effort, each trial in a fresh sandbox. Costs are Baseten list prices times reported tokens. What we found: The lowest-cost harn

[radlad] Hi Guanlan, I vouched for your comment since you involved in this post, but you should be aware that all of your posts have been flagged, likely for AI patterns in your writing. &gt; Don't post generated text or AI-edited text. HN is for conversation between humans. https:&#x2F;&#x2F;news.ycombinator.com&#x2F;newsguidelines.html

[latentsea] This is why for open-weights models at least harness aware post-training is becoming a thing. Also closed source harnesses that aren't fully editable are basically an anti-pattern. The labs should just hurry up and productionize self-evolving harnesses, and have the models internalize harness engineering, so they can optimise the harness for the given task. These are solvable problems.

[Alwayshasbeeb] This. I have coworkers who are really smug about claude code being "the best" experience for AI assisted development and who refuse to try anything else. They also constantly submit pull requests littered with trash "trace of thinking" slop comments and when I point it out they say "yeah I usually try to make it not do that but this one got through". Meanwhile in pi this was trivial to fix and I'm often mining session history to refine the efficiency.

[Majromax] Saying that 'steps per pass' explains cost seems nearly tautological. Run costs are proportional to the number of tokens produced, and the number of tokens is strongly correlated to the number of steps. The 'steps per pass' criterion is also not something under the harness's direct control in the way that its tool collection and system prompt (&#x2F;start tokens) are. Even the cache hit rate is hard to control beyond a limit, since modern harnesses rarely rewrite history. I'm also suspicious about the run-to-run variance between mode

[Zigurd] I find myself pulled in two directions by the performance of coding agents: First, keeping them on a short leash seems sensible. I don't get failed results very often. When I first started using coding agents, this seemed not just sensible but required in order to not deal with a lot of hallucinated weirdness. Secondly though, it's pretty cool to vaguely wave your hands in a certain direction and get both user interface and business logic that's objectively nicer than I would've gotten from the effort I would've put into manually codin

[embedding-shape] Not every problem should (or even could sometimes) be solved the same way. Are you planning to maintain the produced code for more than a year? No, then wave away. But if you're expecting others to depend on it, and you want to be able to continue evolving what it is, then a tight leash and full understanding of how it actually works, is very much needed, even if you don't actually type characters into an editor anymore. Otherwise you still end up with balls of spaghetti where each change takes longer and longer to work into t

[smallnamespace] The cost of AI is rapidly falling while its engineering capabilities keep rising. This implies that code is becoming more fungible, and you should expect any code you write today to mostly be replaced in the near future. The requirements will be more stable than the code. Focus on them instead.

