---
title: "Why is Gemini 4 Carbon taking so long?"
source: "https://kernel.dev/blog/why-is-gemini-4-carbon-taking-so-long/"
author: "Kernel (kernel.dev)"
published: 2026-11
fetched: 2026-11-18
type: article
sha256: d8e32a6374c3f5c59c3a28973cd308410d1b542b330b5ccdeb1bc0ee696f60b3
---

While benchmarking Gemini 4 Carbon on one of our private evals, we found something surprising: it spent close to an hour completing tasks that routinely took Opus and Astra only a few minutes:

 Time and cost per trial 
 Left is faster; lower is cheaper. 

 API list price 
 On a $200 plan, fully used 

 Carbon is priced at its post-introductory rate. Subscription subsidization rates used: Opus 40×, Astra 13×, Carbon 3×, Hydrogen 17×. 

 Turns out we weren't alone in noticing this. 

 Theo - t3.gg @theo I don't really know how to properly emphasize this. Gemini 4 Carbon is unacceptably slow in real world usage. Gemini 4 Carbon low: 22m21s Opus 5.5 high: 9m33s Nov 11, 2026 828 104 replies Elliot Arledge @elliotarledge i really love gemini 4 carbon but its too slow. im losing my mind waiting just to stay focused and learn simple things Nov 12, 2026 36 5 replies Shayan @ImSh4yy dude why is carbon so fucking slow Nov 13, 2026 8 4 replies Simon Mahns @ CoRL @nautsimon_ carbon is nearly unusable because of how slow it is, but people are majorly sleeping on it Nov 16, 2026 30 3 replies 

 To find out why, we traced every step of Carbon's runs and quantified what contributes to the slowness. 

 The Task 
 In each task, the agent gets a codebase from just before a bug was fixed, along with a report that describes the bug only by its symptoms. Its job is to diagnose the bug and fix it, without making any unrelated changes. 
 Much of the task's difficulty comes from engineering judgment rather than raw intelligence: tracing the user's symptoms to the right code path, ruling out rival explanations, putting the fix in the right place, and knowing when to stop. 
 Slow inference, or more work? 
 The first (and easiest) factor to separate out was inference speed: queueing at the provider, network latency, prompt processing and generation speed. Together, these set how long each step takes: 

 Seconds per step 

 Slower inference accounts for part of the gap: 16–30% of Carbon’s extra time compared with Astra, and 45–49% compared with Opus. The rest comes from longer trajectories. Carbon simply does more work per task, as the step counts, tool calls and tokens below show: 

 The workload 
 GPT-6 Astra against Gemini 4 Carbon, mean per bug. 

 GPT-6 Astra Gemini 4 Carbon lighter = lower effort 

 Carbon takes about seven times as many steps as Astra, and eleven times as many actions such as reading a file or running a command. It writes seven times as much and, because every step re-sends a longer and longer conversation, it processes more than sixteen times as much input. 
 Ruling out the obvious 
 Before looking inside the runs, we checked two simpler explanations. 

 The harness. We also ran Carbon inside two other coding agents, opencode and mini-SWE-agent, and saw no meaningful difference. 
 Mismatched reasoning levels. Effort settings aren't standardized across providers, so Carbon's "high" may sit closer to the other models' maximum settings, and the fairer comparison might have been Carbon on low. But on low, Carbon often failed to produce a fix at all: it went in circles, re-reading code it had already read instead of making the fix. 

 Reading the traces 
 We labelled every step of the Astra and Carbon runs by what it was for, and then counted how many steps went to each kind of work: 

 Semantic trace analysis 
 Each model’s steps, grouped by what they were for. 

 Leaves out the 20 steps Carbon spent re-reading code it had already read; the next section covers those. 

 Half of Carbon’s steps went into work the ticket never asked for: 

 Auditing code beyond the bug. Once it had found the cause, Carbon kept widening its search, checking every related path through the system and auditing code the fix never needed to touch. 
 Closing loopholes the ticket had already ruled out. Carbon defended against cases the ticket's facts had already excluded, hardening the code against problems nobody had reported. 

 Can Carbon identify its own overworking? 

 Sample trial: time to find the cause vs. time to first edit 
 Minutes from the start of each run. GPT-6 Astra at max effort, Gemini 4 Carbon at high. 

 In this sample trial, both models identified the cause early, Astra within a minute and Carbon within about six. Astra had its fix written three minutes later; Carbon didn't write any code for another 25 minutes. 
 Carbon might not have been sure it had the cause (a knowledge gap), or it might have known and kept going anyway (a general habit, learned from training that rewards right answers more than it penalises extra steps). To tell them apart, we re-ran one of the trials in a modified harness that automatically injects the same check-in every five turns: "do you already have enough to make the fix?" 

 Sample trial with check-ins: time to find the cause vs. time to first edit 
 The same bug and scale as above. Gemini 4 Carbon at high, with the check-in injected every five turns (circles). 

 With check-ins, Carbon finished in 28 minutes instead of 37, and the wait between naming the cause and editing shrank from 25 minutes to about 10. This implies that the slowness seems to come from how Carbon behaves, not what it knows. 

 Carbon's necessary work is also slower 
 Even within the steps the fix needed, we found some additional low-hanging fruit: Carbon got less done with each step, and it kept re-reading code it had already seen. 

 Astra made more than two tool calls per step, often reading several files at once — Carbon, on the other hand, made about one, usually reading a single file. Carbon also re-read far more: 39% of the lines it read were ones it had already seen, against 7% for Astra. We estimate that these two "mechanical" inefficiencies account for roughly 25% of Carbon's excess runtime. 

 Conclusion 
 On difficult bug-fixing tasks, Carbon took close to an hour where Opus and Astra took minutes. We traced that gap to three sources: 

 Slower inference. Each step takes longer, which explains 16–30% of the gap against Astra and about half against Opus. 
 Unnecessary work. About half of Carbon's steps went on work the tickets never asked for: auditing code the fix didn't need and closing loopholes the ticket had already ruled out. 
 Mechanical inefficiencies. Fewer tool calls per step and frequent re-reading slow Carbon down; we estimate that fixing them alone would cut its runtime by roughly a quarter. 

 Interested in model performance and want to collaborate? 
 Contact us at [email&#160;protected]


## HN discussion highlights (item 50541790, 126pts)

[user_7832] I am increasingly more convinced every day that every LLM company is just making their latest model to be the best at (coding) benchmarks, at the cost of pretty much everything else. I use LLMs for non code purposes (probably not very common on HN) and Sonnet 3.5&#x2F;3.6 still ranks as probably one of the best models I've used. Can today's models put out tech demos and call more tools that make it way more impressive? Sure. But it's really hard to see any actual significant gains over the last few months, they're so mild (again, no

[auyez] At this point it might make sense to put all their resources into improving coding and math skills, because it might lead them to a state where they keep accelerating their capabilities. Even in the worst scenario where LLM approach would hit some wall, they would have technology to quickly explore all other approaches.

[londons_explore] The Human mind so far has shown remarkably little ability to redesign other human minds to be smarter. The existence of AI able to design a smarter AI I would not say is a given.

[wellcolormesurp] They are cracking software and math, not finance, law or medicine or whatever it is you do. Those two domains have leverage, the others do not. It makes perfect sense. If you and I had the goals they have we would start with code and math as well. The other dominos will fall automatically once you got the engineering automated. It makes no sense to stop focusing on that until you either run out of money or achieve your goal.

[oblio] &gt; The other dominos will fall automatically once you got the engineering automated. Based on...? Wishful thinking?

[SyneRyder] Are you able to give hints to some of those use cases? Recent Opus and Fable seem to have made big leaps in art and music, and I don't think all of that is the longer context window since Sonnet 3.x. But those are both things that can be created with code and mathematical thinking as well. I definitely wouldn't want to use recent models for writing though (not that I ever wanted them to write for me anyway).

[knollimar] Opus 5.5 trashes everything not fable and astra for my knowledge work. It’s an insufferable pedant though. I haven’t used a lot of Carbon though.

[vintermann] I also use LLMs for a difficult non-coding task (historical HTR), and my experience is that Gemini Argon is much better than its competitors on that. Its main failure modes are silently stopping with the first column of a multi column layout, and ignoring explicit formatting instructions and polluting the transcription with letter variants and ligatures (such as long s, ū, double-dotted y and æ in Latin). It's a bad habit it's picked up from HTR datasets. Still, those are much better failure modes than hallucinating, which powerful

