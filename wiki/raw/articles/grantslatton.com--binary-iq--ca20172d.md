---
title: "Binary IQ"
url: "https://grantslatton.com/binary-iq"
fetched_at: 2026-04-29T07:02:16.642253+00:00
source: "grantslatton.com"
tags: [blog, raw]
---

# Binary IQ

Source: https://grantslatton.com/binary-iq

Binary IQ
I'm defining a term I refer to as
Binary IQ
, or sometimes
Yes/No IQ
.
The basic idea is suppose you have a prompt where everything that could possibly be relevant is in the context window. Nothing irrelevant is in there. You ask a simple yes or no question. How well does the model do?
My hypothesis is that performance on this benchmark is
the
main bottleneck to getting LLM-based agents to work in the near term.
A related thought is that the best LLMs (Claude 3.5, GPT-4o, Llama 3 405B) only
seem
to be "high IQ" when operating in-distribution, when they can draw on vast, vast memorization.
Note
: I'm not at all saying that LLMs can't reason, that they aren't useful, that they are dead-end, or any of that. Just that they are not as smart as many people think in the more out-of-distribution, general cases one runs into when trying to implement an agent program.
Here's a motivating example. I once gave GPT4 a prompt that looked something like this:
Plan:
Step 1
Step 2
Step 3
Execution log:
Did step 1
Did step 2
Based on the plan and execution log, has the plan been finished? Yes/No
And GPT4 said "Yes" when the answer is obviously "No" to even a child. In the real case, the steps had instructions and the log had more information, but the basic structure was the same, and the extra information was not significant.
In the particular agent, it got this question right probably 95% of the time. But that's simply not good enough to build a reliable agent.
You can obviously improve upon this success rate with some kind of checker process, or additional chain of thought. But those processes will run into the same issue.
With every recursive checker or iterative chain of thought, as the end, you have to look at everything in the context window and ask "Is my conclusion correct? Or should I keep doing more checking/thinking?". This is another binary yes/no question.
My hypothesis is that GPT4-tier models have an in-distribution IQ that appears to be something like an IQ 125 adult, but out-of-distribution it's more like IQ 75. I could see this number changing with scale, synthetic training data, new training paradigms, etc — but for now, it's the bottleneck.
Collective IQ
A related and somewhat downstream topic is something I've been calling
Collective IQ
. The question goes something like this:
Suppose you take a group of 10 people with IQ 100 and have them collaborate on an IQ test. How high does the collective score? My hypothesis is that they will probably score slightly higher than 100, but not too much.
The bottleneck is the aforementioned
binary IQ
concept. The N people can collaborate however much they want, but at the end of the day, they must make a decision on what answer to choose, and that decision will be made by someone with an IQ of 100.
There's a somewhat more nuanced version of the question that goes like:
Suppose a person of IQ 150 gives some structure, organization, written instructions, etc to a group of 10 IQ 100 people. How high can they score?
That is, the IQ 150 person can say "Ok, you are the leader. You 3 are the doubters who do nothing but find logic flaws. You 2…". Or he can provide high-level meta-heuristics on general problem solving like "Try to break the problem into sub-problems" or "Try to invert the problem and find the opposite", etc.
This version of the question is somewhat similar to an intelligent programmer trying to write an agent program. Each "person" is analogous to each different prompt in your orchestration flow chart.
I bet the answer is the group will score a fair bit higher, but still not
much
higher.
In conclusion: like there is no known way for a group of IQ 100 people to score IQ 120 on a test, there is no known way for a group of GPT-N to perform like GPT-(N+1) in the
general
sense.
Evals
I'm thinking of the best way to formulate an eval that measures binary IQ. If you have any ideas, I'd love an email or DM.
My current thinking is to synthesize data by generating random boolean algebra expressions of increasing complexity, and then re-skinning them to plain English.
For example, take the boolean expressions:
A => B
~B
A?
You could re-skin this into:
If it's raining, Alice wears a raincoat.
Alice isn't wearing a raincoat.
Is it raining?
Modern GPT4-tier LLMs obviously get this one correct. But you can keep conjuring increasingly complex expressions and they will eventually break down.
I'm sure there are interesting and good evals other than this that get to the same core idea, so please contact me if you have ideas.
Conclusion
Techniques like chain-of-thought are obviously helpful at scaffolding across many problems, but do not fundamentally raise the intrinsic binary IQ of the network. LLM agents are fundamentally bottlenecked by the
deep, unrepresentable insight
contained within the activations of the network.
While it could change with another model generation, LLMs are simply not deeply smart enough yet.
