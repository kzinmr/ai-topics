---
title: "How the AI boom might really end: 5 scenarios"
url: "https://martinalderson.com/posts/how-the-ai-boom-might-really-end/?utm_source=rss&utm_medium=rss&utm_campaign=feed"
fetched_at: 2026-10-18T10:01:01.144070+00:00
source: "martinalderson.com"
tags: [blog, raw]
ingested: 2026-10-18
sha256: PLACEHOLDER
---

# How the AI boom might really end: 5 scenarios

Source: https://martinalderson.com/posts/how-the-ai-boom-might-really-end/?utm_source=rss&utm_medium=rss&utm_campaign=feed

With the Anthropic IPO gathering pace - and chip stocks just posting their
longest losing streak since 2008
amid
worries about AI debt
, I thought it'd be worth writing up some of my thoughts I've put together while thinking through what may happen. By no means is this meant to be exhaustive - just a list of what
I
think is the most interesting to think through.
Before I dive into the scenarios, while I'm sure there are going to be failures and mispricing of asset classes - like any huge investment wave - I think it's worth saying that unlike many bubbles there is an
enormous
amount of value being created.
In essence, I think this is the first time capital can be turned into intelligence. You buy (or borrow money for) GPUs, you get tokens out which represent a growing share of professional service work. I'm certainly biased as a software engineer by trade - the models just get better and better at coding and it's humbling to see it do my previous tasks
so
quickly and increasingly
better
than I can do them.
And unlike (say) the dotcom boom, which was arguably
directionally
correct, but far too early, we're seeing mass adoption and
huge
revenues being generated, far quicker than in the late 90s.
So thinking through this, I'd group the scenarios into two categories. Firstly, AI
itself
doesn't deliver the value promised
or
gets stopped by external factors. I think these are worth thinking through.
The other category - and potentially more likely - is that AI works well, but the value doesn't flow to the people that are putting the money in. I think this is where the unwinding could happen, and arguably is already showing up.
Group 1: AI disappoints or gets stopped
Models stop getting any better
While it's hard to argue that the models as is aren't "good" at specific tasks now, it may well be that we hit a scaling wall. Increasing amounts of capex is pumped into model training, but the results are incrementally better. This leads to a "hard" wall on progress until another architecture or approach potentially comes along.
This one I'd discount for now. We're seeing no signs of progress slowing, and we're seeing very fast advancement in capabilities. And
even
if this did happen, most organisations and people aren't using anywhere near their full power.
The one watch out though which is a bit more insidious is that the models continue getting better at specific tasks, but start regressing badly in others. I feel Opus 5 was a good example of this - better at coding, but produced infuriatingly hard-to-read prose. Perhaps we'll see models more focused at specific tasks if this gets harder to mitigate (much like the Codex series of GPT models, which then got unified back into the main GPT models).
Alignment risks
The other
major
risk with AI is that it ends up doing something
bad
in the real world. We've already seen the
Hugging Face incident
as a 'warning shot'. But there are far more catastrophic risks at play - for example, shutting down national infrastructure, or hacking a major financial institution that results in systemic risk across markets. Or, it goes full Skynet.
There is no doubt this would cause enormous political upheaval that would lead to very rapid and severe backlash. Where the industry goes after that is hard to see - potentially progress gets frozen, resulting in far fewer orders for GPUs. On the other hand, it's hard for me to see a globally coordinated moratorium on AI given the breakneck competition between (primarily) the US and China. If it happened in China, is the US likely to follow suit? Or would it, instead, be blamed on "defective Chinese" models, and the US continues as is? Equally, if it happens in the US, does China pause or see this as a once in a generation opportunity to leap ahead?
I think we are getting dangerously close to an incident that may cause some sort of significant pullback in AI spending. It's certainly hard to predict, and the severity matters a lot - along with human impact.
Datacentre ban
Slightly less science fiction-y would be widespread local or political opposition to datacentre rollouts causing a very widespread pause on new capacity coming on stream.
While this is certainly happening - I have a suspicion this could be one of the key battlelines for the 2028 US election cycle - it again would have to be a global ban to have any significant effect. If the US does a ban, projects and investments would quickly shift to other jurisdictions.
And I'm almost certain that China would not even entertain any sort of ban like this, which again adds a geopolitical angle to it. Would the US really want to go ahead with a national ban when China
already
has a commanding lead in electricity capacity (if not semiconductors).
As such, I can't see this having a great effect on the deployment as a whole. The
real
weakness lies in financing these deals. Much like Ørsted needed a
$9.4bn rights issue
after US stop-work orders on its offshore wind projects spooked its financing, we could quickly see a domino effect of financing failures caused by it.
Group 2: AI works, but the capex holders don't capture the value
Open weights get so good they collapse margins
I think this is the standout from where I see the risk and something I've been writing about for a while now. We're in the middle of a
brutal
inference price war - if you want to read more read my
other recent article
.
This is largely caused by open weights models crossing the threshold of being "good enough" for many tasks.
Anthropic releasing Haiku 5.5 at a huge discount - 90% cheaper on short context windows - means that for shorter, bulk tasks, Anthropic & OpenAI are actually as cheap as, or
cheaper
than, comparable open weights models. This doesn't apply for longer agentic tasks with Haiku - the price jumps 5x once you go over 100K tokens of context. Interestingly, OpenAI is far more aggressive here: GPT-6 Luna only goes up 1.5-2x, and only past 272K tokens. But I was surprised recently to find that no reputable inference provider offers comparable open weights models (e.g. DeepSeek) at any significant discount to Haiku and Luna, which is an enormous change from where we were at the start of the year, where the frontier labs were charging 10-20x more than open weight models.
How much this cannibalises their more expensive models is up for debate. They've done the pricing in such a way that for longer agentic tasks, open weight models are still very attractive.
But the perpetual price drops must be having some impact on margins, even if it does lead to them (re)taking market share from open weights competitors.
So the
hope
is that they continue cutting prices, but revenue/token growth outstrips that. It is certainly possible - but it shows how fast this market switches that we've now got frontier labs offering this inference
at all
.
The wildcard I would keep though is that while the open weights labs have kept pace, we can't rule out the frontier labs' ability to throw a
lot
of compute and brainpower at new models. Opus 5.5, for example, is an excellent model for more demanding tasks. And the Chinese labs are clearly short of hardware
and
facing
new export restrictions
from the Chinese government.
Huge efficiency breakthroughs
Note that the previous scenario, while catastrophic for the frontier labs if this compression continues, arguably
increases
demand for semiconductors, memory and the related supply chain.
But another risk is that if there are huge efficiency breakthroughs, either through hardware
or
software/model improvements. This is what killed the
telecoms boom in the early 2000s
- it wasn't so much that bandwidth growth stopped, but the efficiency of fibre optics far outpaced the demands.
So far we've seen
a lot
of innovation on the model side, but hardware has struggled to keep pace. Discounting all the hype stats that Nvidia etc put out for each new generation, underlying tokens/watt - the best figure to watch - is improving far slower than the headlines suggest.
The model efficiency improvements have been pretty amazing to watch. But so far, this has all been put into longer context windows (enabling longer running agentic tasks) and have enabled some of the price decreases we've seen.
But, there is a world where a new hardware or software approach does lead, much like DWDM fibre back in the 2000s, to efficiency running far, far ahead of token growth, even taking Jevons paradox into account.
My gut says that token demand is growing so fast, and will
continue
to grow so fast that it will consume all efficiency gains in the near future. The key way to track this I think is
not
looking at some of the "token cost indexes" that get posted about - this doesn't adjust for the exponential growth in demand - but instead look at the cost of GPUs on the spot market. If we start seeing
big
,
broad
drops across all compute types, then that's a clear sign that supply and demand is starting to reach equilibrium and this scenario is starting to play out.
Conclusion
There are no doubt many risks to the AI "economy", and it's always easy to point to whatever one is making the most news.
But to me the
real
question is whether AI progress is turning into tangible value. Right now - for me, and many others, the answer is a resounding yes. Token consumption is going through the roof, because as models get better more and more tasks can be executed with AI. And I still think early adopters that are pushing agentic workflows comprise a small single-digit percentage of the professional services market as a whole.
But this doesn't mean that the labs making and serving those models take the benefit. History is littered with huge technological advancements which went to
consumer surplus
, not whoever bet the most capital.
And my view is that's what we are seeing right now. The frontier labs are in serious peril of losing margin, and therefore market valuation, to open weights competitors.
The important point though is that the frontier labs do not make up the whole market. Tokens need compute, memory and power whether it's a frontier lab or open weights.
I see endless analysis of OpenAI vs Anthropic revenue figures. What's far
more
important to the AI ecosystem is
overall
revenues. And as the market continues to fragment, it's harder and harder to join that together. Unless AI does hit a wall, open weights may mean the end of the boom in frontier labs valuations. But the underlying supply chains may be doing
better
than ever.
Which is why I think the market has this week backwards. Chip stocks are being punished just as TSMC reports record revenue and says
AI demand still exceeds supply
.
The one caveat is leverage. So much of this buildout is debt-funded that even small changes can unwind far faster, and far more completely, than they should. CoreWeave's
credit default swaps hit distressed levels
this week on a hot inflation print and a
viral chart
- not because anyone stopped wanting GPUs.
If the AI boom ends, I don't think it ends with fewer tokens. It ends with the same tokens - or far more - flowing to far more people at far lower margins.
