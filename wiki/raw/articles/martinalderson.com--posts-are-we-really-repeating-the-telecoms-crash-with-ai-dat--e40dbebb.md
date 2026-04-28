---
title: "Are we really repeating the telecoms crash with AI datacenters?"
url: "https://martinalderson.com/posts/are-we-really-repeating-the-telecoms-crash-with-ai-datacenters/?utm_source=rss&utm_medium=rss&utm_campaign=feed"
fetched_at: 2026-04-28T07:02:44.435716+00:00
source: "martinalderson.com"
tags: [blog, raw]
---

# Are we really repeating the telecoms crash with AI datacenters?

Source: https://martinalderson.com/posts/are-we-really-repeating-the-telecoms-crash-with-ai-datacenters/?utm_source=rss&utm_medium=rss&utm_campaign=feed

I keep hearing the AI datacentre boom compared to the 2000s telecoms crash. The parallels seem obvious - billions in infrastructure spending, concerns about overbuilding, warnings of an imminent bubble. But when I actually ran the numbers, the fundamentals look completely different.
I'm not here to predict whether there will or won't be a crash or correction. I just want to look at whether the comparison to telecoms actually holds up when you examine the history in a bit more detail.
What Actually Happened in the Telecoms Crash
Let me start with what the 2000s telecoms crash actually looked like, because the details matter. Firstly, there was massive capex - between 1995 and 2000 somewhere like
$2 trillion was spent laying 80-90 million miles of fiber
. Inflation adjusted, this is over $4trillion, or close to
$1trillion/year
in 2025 dollars.
By 2002 only
2.7% of this fibre was used
.
How did this happen? A catastrophic supply and demand miscalculation past the pure securities fraud involved in many of the companies. Telecom CEOs
claimed
internet traffic was doubling every 3-4 months.
But in reality,
traffic was doubling roughly every 12 months
. That's a
4x overestimate
of demand growth, which compounds each year. This false assumption drove massive debt-financed overbuilding. If you overestimate 4x a year for 3 years, by the end of your scenario you are 256x out.
Even worse
for these companies, enormous strides were made on the optical transceivers, allowing the same fibre to carry 100,000x more traffic over the following decade. Just one example is WDM multiplexing, allowing multiple carriers to be multiplexed on the same physical fibre line. In 1995 state of the art was 4-8 carriers. By 2000, it was 128. This
alone
allowed a 64x increase in capacity with the same infrastructure. Combined with improvements in modulation techniques, error correction, and the bits per second each carrier could handle, the same physical fibre became exponentially more capable.
The key dynamic: supply improvements were exponential while demand was merely linear. While some physical infrastructure needed to be built, there was enormous overbuilding that could mostly be serviced by technology improvements on the same infrastructure.
AI Infrastructure: A Different Story
Unlike fibre optics in the 1990s, GPU performance per watt improvements are actually slowing down:
2015-2020 Period:
Performance per watt improved significantly with major architectural changes
Process nodes jumped from ~20nm to 7nm (major efficiency gains)
Introduction of Tensor Cores and specialized AI hardware
2020-2025 Period:
More tellingly,
GPU TDPs (power consumption) are rising dramatically
:
V100 (2017): 300W
A100 (2020): 400W
H100 (2022): 700W
B200 (2024): 1000-1200W
This is the opposite of what happened in telecoms. We're not seeing exponential efficiency gains that make existing infrastructure obsolete. Instead, we're seeing semiconductor physics hitting fundamental limits.
The B200 from NVidia also requires liquid cooling - which means most datacentres designed for air cooling need to be completely retrofitted.
Demand Growth Is Actually Accelerating
The telecoms crash happened partly because demand was overestimated by 4x. What does AI demand growth look like?
Traditional LLM Usage:
ChatGPT averages 20+ prompts per user per day
. Extended conversations can reach 3,000-4,000 tokens cumulative, though many users treat it like Google - short "searches" with no follow-up, consuming surprisingly few tokens.
Agent Usage (
Anthropic research
):
Basic agents:
4x more tokens
than chat
Multi-agent systems:
15x more tokens
than chat
Coding agents:
150,000+ tokens per session
(multiple sessions daily)
We're looking at a fundamentally different demand curve - if anything, people are underestimating how much agents will consume. The shift from chat to agents represents a 10x-100x increase in token consumption per user.
We're not even there yet, and infrastructure is already maxed out, with AI infrastructure running at very high utilization rates. Major providers still experience peak-time capacity issues. The problem isn't unused infrastructure sitting idle; it's infrastructure struggling to meet current demand. One major hyperscaler told me they
still
have capacity issues at peak times causing free tier users to have high error rates.
Datacenter CapEx: Evolution, Not Revolution
Another important piece of context that gets missed:
Pre-AI Growth (2018-2021):
Combined Amazon/Microsoft/Google capex:
$68B (2018)
→
$124B (2021)
81% growth over 3 years
Annual growth rate:
~22%
Driven by cloud migration, pandemic acceleration, streaming
AI Boom (2023-2025):
2023: $127B
2024:
$212B
(
67% growth
year-over-year)
2025 projected:
$255B+
(Amazon $100B, Microsoft $80B, Alphabet $75B)
While it's no doubt a huge amount of capex going into this rollout; it's not quite as dramatic as some news stories make out. I have no doubt that now any datacentre related capex is being rebranded as "AI", even if it's just 'boring' old compute, storage and network not being directly used for AI.
Why Forecasting Is Nearly Impossible
Here's where I think the comparison to telecoms becomes both interesting and concerning.
The Lead Time Problem:
Datacenters take 2-3 years to build
GPU orders have 6-12 month lead times
Can't adjust capacity in real-time to match demand
The Prisoner's Dilemma:
Underestimating demand = terrible user experience + losing to competitors
Overestimating demand = billions in wasted capex (that might just get used slower)
Given the choice, rational players overbuild - because wasting some capex is infinitely better than losing the "AI wars"
The Forecasting Challenge:
Imagine you're planning datacenter capacity right now for 2027. You need to make billion-dollar decisions today based on what you think AI usage will look like in three years.
Here's scenario one: agent adoption is gradual. Some developers use Claude Code daily. A few enterprises deploy internal agents. Customer service stays mostly human with AI assist. You need maybe 3-4x your current infrastructure.
Here's scenario two: agents go mainstream. Every developer has an always-on coding agent consuming millions of tokens per session. Enterprises deploy agents across operations, finance, legal, sales. Customer service becomes 80% agentic with humans handling escalations. You need 30-50x your current infrastructure.
Both scenarios are completely plausible. Nobody can tell you which one is right. But you have to commit billions in capex NOW - datacenters take 2-3 years to build, GPU orders have 6-12 month lead times.
But here's the really insidious part:
even if you're directionally right, small errors compound massively. Let's say you're confident agents are going mainstream and you need roughly 50x growth over 3 years.
If actual demand is 40x, you've overbuilt by 25% - billions in excess capacity.
If actual demand is 60x, you've underbuilt by 20% - your service degrades and you lose market share.
You're trying to hit a moving target in the dark, and the margin of error is measured in tens of billions of dollars and thousands of megawatts of power infrastructure.
If you build for scenario one and scenario two happens, your service degrades to unusable, users revolt, and you lose the AI wars to competitors who bet bigger. If you build for scenario two and scenario one happens, you've got billions in underutilized datacenters burning cash.
Which mistake would you rather make?
This is where the telecoms comparison makes sense: given those choices, rational players overbuild. The difference is what happens to that overcapacity.
The Key Differences
Let me put this in a table:
Factor
Telecoms (1990s-2000s)
AI Datacenters (2020s)
Supply improvements
Exponential (100,000x capacity increase)
Slowing (69%→44% annual perf/watt gains)
Demand growth
Overestimated 4x
Potentially underestimated (agent transition)
Utilization
95% dark fiber (genuine overcapacity)
Very high - many providers still experiencing peak time scale problems
Technology curve
Making infrastructure obsolete
Hitting semiconductor physics limits
Power consumption
Decreasing
Increasing (300W → 1200W)
Infrastructure lifespan
Decades (fiber doesn't degrade)
Years (refreshed as better hardware arrives)
The telecoms crash happened because exponential supply improvements met linearly growing (and overestimated) demand, with infrastructure that would last decades sitting unused.
AI datacenters are facing slowing supply improvements meeting potentially exponentially growing demand. And crucially, because GPU efficiency improvements are slowing down, today's hardware retains value for longer - not shorter - than previous generations.
What About a Short-Term Correction?
Could there still be a short-term crash? Absolutely.
Scenarios that could trigger a correction:
1. Agent adoption hits a wall
Enterprises might discover that production agent deployments are harder than demos suggest. Hallucinations in high-stakes workflows, regulatory concerns around autonomous AI systems, or implementation complexity could slow adoption dramatically. If the agent future takes 5-7 years instead of 2-3, there's a painful gap where billions in infrastructure sits waiting for demand to catch up.
However, given the explosion in usage for software engineering and other tasks, I suspect this is highly unlikely. You can already use Claude Code for
non engineering tasks
in professional services and get very impressive results without any industry specific modifications, so I have no doubt there is going to be very high adoption of agents in all kinds of areas.
2. Financial engineering unravels
These datacenter buildouts are heavily debt-financed. If credit markets seize up, interest rates spike further, or lenders lose confidence in AI growth projections, the financing model could collapse. This wouldn't be about technical fundamentals - it would be good old-fashioned financial panic, similar to what happened in telecoms when the debt markets froze, but with one key difference - a lot of the key players (Microsoft, Google, Meta, Oracle) are extremely cash flow positive, which definitely wasn't the case in the 2000s fibre boom. The pure datacentre players though are at risk - who don't have a money printing main business to backstop the finance -  no doubt about that.
3. Efficiency breakthroughs change the math
Model efficiency could improve faster than expected. Or we could see a hardware breakthrough: custom ASICs that are 10x more efficient than GB200s for inference workloads. Either scenario could make current buildouts look excessive. I actually think this is the biggest risk - and this is
exactly
what happened in the fibre boom. So far, I'm not seeing signs of this though. While specialist ASICs are becoming available, they hit their impressive speed by having huge wafers, which isn't a huge efficiency game (yet).
The Key Difference From Telecoms:
Even if there's a correction, the underlying dynamics are different. Telecoms built for demand that was 4x overestimated, then watched fiber optic technology improvements make their infrastructure obsolete before it could be utilized. The result: 95% of fiber remained permanently dark.
AI datacenters might face a different scenario. If we build for 50x growth and only get 30x over 3 years, that's not "dark infrastructure" - that's just infrastructure that gets utilized on a slower timeline than expected. Unlike fiber optic cable sitting in the ground unused, GPU clusters still serve production workloads, just at lower capacity than planned.
And unlike telecoms where exponential technology improvements made old infrastructure worthless, GPU efficiency improvements are slowing. A GB200 deployed today doesn't become obsolete when next year's chip arrives - because that chip is only incrementally better, not 100x better. With process node improvements slowing down, current generation hardware actually retains value for longer.
A correction might mean 2-3 years of financial pain, consolidation, and write-downs as demand catches up to capacity. But that's fundamentally different from building infrastructure for demand that never materializes while technology makes it obsolete.
The Real Risk: Timing, Not Direction
I think the real question isn't whether we need massive AI infrastructure - the agent transition alone suggests we do. The question is timing.
If enterprises take 5 years to adopt agents at scale instead of 2 years, and hyperscalers have built for the 2-year scenario, you could see a 2-3 year period of overcapacity and financial pain. That might be enough to trigger a correction, layoffs, and consolidation.
But unlike telecoms, that overcapacity would likely get absorbed.
The telecom fibre mostly stayed dark because technology outpaced it and demand never materialized. AI infrastructure might just be early, not wrong.
Conclusion
Are we repeating the telecoms crash with AI datacenters? The fundamentals suggest not, but that doesn't mean there won't be bumps.
The key insight people miss when making the telecoms comparison: telecoms had exponential supply improvements meeting linear demand, with 4x overestimated growth assumptions. AI has slowing supply improvements potentially meeting exponential demand growth from the agent transition.
The risks are different:
Telecoms:
Built too much infrastructure that became completely obsolete by supply-side technology improvements
AI:
Might build too much too fast for demand that arrives slower than expected
But the "too much" in AI's case is more like "3 years of runway instead of 1 year" rather than "95% will never be used."
I could be wrong. Maybe agent adoption stalls, maybe model efficiency makes current infrastructure obsolete, maybe there's a breakthrough in GPU architecture that changes everything. But when I look at the numbers, I don't see the same setup as the telecoms crash.
The fundamentals are different. That doesn't mean there won't be pain, consolidation, or failures. But comparing this to 2000s telecoms seems like the wrong mental model for what's actually happening.
