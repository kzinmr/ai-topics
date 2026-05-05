---
title: "Sloc Cloc and Code - LOCOMO (LLM Output COst MOdel)"
url: "https://boyter.org/posts/sloc-cloc-code-locomo-llm-output-cost-model/"
fetched_at: 2026-05-05T07:01:53.445579+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Sloc Cloc and Code - LOCOMO (LLM Output COst MOdel)

Source: https://boyter.org/posts/sloc-cloc-code-locomo-llm-output-cost-model/

One of the things I added to my
code counter scc
back when developing it was the COCOMO calculation. It’s not a reference to a
song by the beach boys
but instead the
Constructive Cost Model
, which is a model for estimating the cost of software developed by Barry Boehm in the late 70’s.
All models are wrong, but some are useful - George Box
Regardless if you find it useful or not, it was something that existed in
David Wheelers SLOCcount
which was never added into any other code counter. Hence its inclusion into
scc
, because I personally wanted it there.
However it is now 2026 and in the age of LLMs we need something new. COCOMO is a fairly simple model, that estimates effort and schedule, including the design time, code and test implementation as well as documentation time for users and developers. It is however not suited for what a LLM can do.
LOCOMO (LLM Output COst MOdel)
So I introduce the
LOCOMO (LLM Output COst MOdel)
. This is a new measure designed to estimate the cost and time to produce code using any number of differently sized LLMs. I have also built and shipped it into
scc
allowing others to look through it, validate it and comment before I ship it. I should mention up front this is an opt in model, and not likely to be the default
scc
output for a very long time.
Run with a freshly compiled version of
scc
you get the following output, run against its own source code limited to Go and removing the size to lower visual noise. Note that the model assumes a medium sized model such as Sonnet by default.
$ scc --locomo -i go --no-size
───────────────────────────────────────────────────────────────────────────────
Language            Files       Lines    Blanks  Comments       Code Complexity
───────────────────────────────────────────────────────────────────────────────
Go
32
26,200     1,679
584
23,937      1,856
───────────────────────────────────────────────────────────────────────────────
Total
32
26,200     1,679
584
23,937      1,856
───────────────────────────────────────────────────────────────────────────────
Estimated Cost to Develop
(
organic
)
$757,911
Estimated Schedule Effort
(
organic
)
12.38 months
Estimated People Required
(
organic
)
5.44
───────────────────────────────────────────────────────────────────────────────
LOCOMO LLM Cost Estimate
(
medium
)
Tokens Required
(
in/out
)
2.4M / 0.5M
Cost to Generate $14
Estimated Cycles 2.1
Generation Time
(
serial
)
2.7 hours
Human Review Time 4.0 hours
Disclaimer: rough ballpark
for
regenerating code using a LLM.
Does not account
for
context reuse, test generation, or heavy debugging.
───────────────────────────────────────────────────────────────────────────────
FFS $14?!!?! Oh man… If anyone needs me, I’ll be crying on the floor for a while.
The first thing to note here is that this number, and indeed all of the LOCOMO values are based on the question “For this exact codebase, how much would it cost to produce it?”. This mirrors COCOMO, since both are by default blind to the iteration cycles and effort that went into knowing what to do. So by default we are just talking cost to produce exactly what we already have using presumably a well written specification.
Tokens required is literally just tokens in and out, with the cost estimated on the number of tokens and the size of the model. Estimated Cycles is based on the complexity estimate (I will get into more details about this soon). Generation time is based on how many tokens per second (tps) any given model can currently produce. Human review time is assuming a human is reading every line of code.
As mentioned, this is a rough estimate just to regenerate everything, and is not accounting for a host of factors.
As you would expect with
scc
everything can be configured, in the same way COCOMO could be modified. So if you want to adjust for a large model
--locomo-preset large
is there for you. Local models?
--locomo-preset local
which reduces your costs to $0 at the expense of time (or trading a kidney or child for some very expensive video cards or an exo cluster of very expensive Mac Studios).
Enough chat, is the estimation even close?
Estimation Validation
Recently Anthropic used
Opus 4.6 to build a C compiler
, and they told us exactly what went into it and published the
compiler code
produced, which is kinda perfect timing for me on this. From the post,
I tasked 16 agents … Over nearly 2,000 Claude Code sessions and $20,000 in API costs, the agent team produced a 100,000-line compiler
While they say 100,000 line compiler, that’s probably ignoring tests and all the other content the LLM produced, which explains the discrepancy you see in the below figures.
With a quick clone we can start some analysis, we also set the locomo model size to large, as we are assuming a larger model like Opus was used, which is what was reported.
$ scc --locomo --locomo-preset large --no-size
───────────────────────────────────────────────────────────────────────────────
Language            Files       Lines    Blanks  Comments       Code Complexity
───────────────────────────────────────────────────────────────────────────────
Rust
351
186,696    13,235    29,804    143,657     34,213
Plain Text
35
1,501
196
0
1,305
0
Markdown
33
18,233     3,744
0
14,489
0
C Header
17
10,445     1,308     1,001      8,136
648
Shell
6
42
0
24
18
0
License
1
121
12
0
109
0
TOML
1
35
0
0
35
0
───────────────────────────────────────────────────────────────────────────────
Total
444
217,073    18,495    30,829    167,749     34,861
───────────────────────────────────────────────────────────────────────────────
Estimated Cost to Develop
(
organic
)
$5,854,479
Estimated Schedule Effort
(
organic
)
26.92 months
Estimated People Required
(
organic
)
19.32
───────────────────────────────────────────────────────────────────────────────
LOCOMO LLM Cost Estimate
(
large
)
Tokens Required
(
in/out
)
26.5M / 4.0M
Cost to Generate $387
Estimated Cycles 2.4
Generation Time
(
serial
)
1.6 days
Human Review Time 28.0 hours
Disclaimer: rough ballpark
for
regenerating code using a LLM.
Does not account
for
context reuse, test generation, or heavy debugging.
───────────────────────────────────────────────────────────────────────────────
$387… we aren’t even in the ballpark out of the box. However we have additional information we can use. Nicholas Carlini the author told us that he tasked 16 agents to write this, and it took over 2000 sessions. Let’s factor that in,
Since we know 16 agents, we can assume 125 cycles per agent, since 16*125=2000. If we plug those into our model,
$ scc --locomo --locomo-preset large --no-size --locomo-cycles
125
───────────────────────────────────────────────────────────────────────────────
Language            Files       Lines    Blanks  Comments       Code Complexity
───────────────────────────────────────────────────────────────────────────────
Rust
351
186,696    13,235    29,804    143,657     34,213
Plain Text
35
1,501
196
0
1,305
0
Markdown
33
18,233     3,744
0
14,489
0
C Header
17
10,445     1,308     1,001      8,136
648
Shell
6
42
0
24
18
0
License
1
121
12
0
109
0
TOML
1
35
0
0
35
0
───────────────────────────────────────────────────────────────────────────────
Total
444
217,073    18,495    30,829    167,749     34,861
───────────────────────────────────────────────────────────────────────────────
Estimated Cost to Develop
(
organic
)
$5,854,479
Estimated Schedule Effort
(
organic
)
26.92 months
Estimated People Required
(
organic
)
19.32
───────────────────────────────────────────────────────────────────────────────
LOCOMO LLM Cost Estimate
(
large
)
Tokens Required
(
in/out
)
1,375.3M / 209.7M
Cost to Generate $20,043
Estimated Cycles 125.0
Generation Time
(
serial
)
80.9 days
Human Review Time 28.0 hours
Disclaimer: rough ballpark
for
regenerating code using a LLM.
Does not account
for
context reuse, test generation, or heavy debugging.
───────────────────────────────────────────────────────────────────────────────
Please note the VERY cool result of, $20,043. This is almost exactly what was reported by Anthropic. Neat. You will also notice the tokens in and out have increased. To 1,375.3M / 209.7M. Looking at what was reported,
Over nearly 2,000 Claude Code sessions across two weeks, Opus 4.6 consumed 2 billion input tokens and generated 140 million output tokens, a total cost just under $20,000.
Not quite as spot-on with the tokens as with the cost, but still same order of magnitude. The higher input tokens in reality probably stems from agent overhead, heavy reasoning traces, retries, tool calls, context sharing across the 16 agents, etc… Something worth factoring into a future version, maybe with agent parallelism presets?
Conclusion
I am going to leave it at that. If you want to mess around with this you will need to build
scc
from source. Thankfully that’s a simple
go build
. You can find source at
github
with full documentation of the model and how it works on the
README.md
.
If you do end up reviewing this, remember it’s not designed to be 100% accurate. This is not created by someone in a lab performing studies. I am just some guy from Sydney Australia trying to answer a need because COCOMO inaccurate as it was is totally inadequate for what LLMs can do. If you have ideas on how to fix it feel free to email me or hit me up with some github discussion. I’d love to add presets for agent parallelism in there that are sensible defaults.
Or don’t contact me, I’m not your supervisor.
Hopefully however someone can use this as an idea to design a real cost model we can use.
