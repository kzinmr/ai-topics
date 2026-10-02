---
title: "The AI margin collapse is gathering pace"
url: "https://martinalderson.com/posts/ai-margin-collapse-gathering-pace/?utm_source=rss&utm_medium=rss&utm_campaign=feed"
fetched_at: 2026-09-30T10:01:23.706843+00:00
source: "martinalderson.com"
tags: [blog, raw]
---

# The AI margin collapse is gathering pace

Source: https://martinalderson.com/posts/ai-margin-collapse-gathering-pace/?utm_source=rss&utm_medium=rss&utm_campaign=feed

I've written a lot about the
economics
of
inference
-  especially with the advent of "good enough" open weights models. We're starting to see real price competition from
all
the frontier labs, even Anthropic who have been reticent to reduce prices. Let's dive into the market dynamics.
OpenAI fired the starting pistol
The original
80% price cut
at the very end of July on GPT-5.6 Luna certainly shook the market up, and indeed for the first time in recent memory ended up with a non open weights model briefly taking the top spot on
OpenRouter
.
This was quickly followed by a
further
50% price cut on GPT-6 Luna
and
GPT-6 Sol. In around 2 months, we've seen a 90% price cut in Luna and a 60% price cut in Sol.
This is an unusually aggressive trajectory for a frontier lab. Clearly OpenAI is wanting to gain market share, and I think it's proving highly successful.
DeepSeek
While this article would get too long to go into detail of all the open weights models, I think DeepSeek is the one to watch. They've really impressed the market with their inference efficiency - no doubt the frontier labs are doing similar behind the scenes - but the huge amount of papers they are publishing in the open really have grabbed my attention.
Let's take a quick look at their inference prices on their official API (
▲
/
▼
vs the previous price for the same window):
Effective (2026)
Model
Window
Input
Cached input
Output
Apr 24
V4-Flash
Flat
$0.14
$0.028
$0.28
Apr 26
V4-Flash
Flat
$0.14
$0.0028
▼
$0.28
Aug 16
V4-Flash
Off-peak
$0.22
▲
$0.007
▲
$0.66
▲
Aug 16
V4-Flash
Peak
$0.44
▲
$0.014
▲
$1.32
▲
Sep 10
V4.1-Flash
Off-peak
$0.15
▼
$0.003
▼
$0.60
▼
Sep 10
V4.1-Flash
Peak
$0.30
▼
$0.006
▼
$1.20
▼
Interestingly, these prices have gone
up
from the April baseline - input is roughly flat off-peak, but output is ~2x off-peak and ~4x at peak. Though it's important to note that DeepSeek's "peak" hours are actually
Chinese
peak hours, so for Western timezones they are actually well suited to the working day for the most part.
To underline just how aggressive OpenAI are being, they are now
cheaper
on input and output tokens than DeepSeek. But there's a significant gotcha with this - DeepSeek is still
vastly
cheaper for
cached
input, which as I
wrote about recently
actually drives most of the cost for agentic use cases, so I think for many use cases DeepSeek will be (often significantly) cheaper, but it is a really interesting market dynamic that I don't think many have really caught onto.
Anthropic's response
The biggest news I think though has to be Opus 5.5's significant price cut. I've always got the sense that until now Anthropic doesn't really believe they need to compete on price.
I think the
underwhelming response to Fable
has probably changed their mind. Between the aggressive guardrails making it hard to use for a lot of demanding engineering work, and the extremely high pricing, I think many have stuck with Opus.
With Opus 5.5 though they do seem to be responding to the market, reducing pricing by 20% on input and output tokens. While this is still significantly more than Sol, the more interesting price reduction is in the
cache read
rate, which drops 60% (!). As this is the main driver of costs on longer agentic sessions, this is actually a much larger price drop than the 20% looks, potentially reducing the blended rate of some sessions by 50%.
It also looks like there is a new Haiku 5.5 model coming out in the next few weeks - which will be a direct competitor to Luna. I'll be
very
curious to see if they start competing on price with OpenAI on that.
Side by side
Here's how the current prices stack up (per million tokens), along with the cost of two example agentic sessions. Session A is 10M cache reads, 0.5M input and 0.2M output. Session B is more cache-heavy: 20M cache reads, 0.2M input and 0.1M output. I've ignored cache writes for simplicity.
Model
Input
Cache read
Output
Session A
Session B
GPT-6 Luna
$0.10
$0.01
$0.50
$0.25
$0.27
DeepSeek V4.1-Flash (off-peak)
$0.15
$0.003
$0.60
$0.23
$0.15
DeepSeek V4.1-Flash (peak)
$0.30
$0.006
$1.20
$0.45
$0.30
GPT-6 Sol
$2.00
$0.20
$10.00
$5.00
$5.40
Opus 5
$5.00
$0.50
$25.00
$12.50
$13.50
Opus 5.5
$4.00
$0.20
$20.00
$8.00
$6.80
The more cache-heavy the session, the more DeepSeek pulls ahead of Luna - and the closer Opus 5.5 gets to that 50% reduction.
How big is the frontier, actually?
This poses a very interesting question though. Luna, DeepSeek and others are perfectly usable models day to day, and they are faster to use. As these models get better and better there's less and less need to use the large, expensive frontier-class models.
So I believe these models and price cuts are cannibalising a
lot
of revenue. This is no doubt offset by
far more
consumption, but at a (much) lower gross margin.
To be fair, a price cut isn't the same as a margin cut. If serving costs are falling just as fast, margins could hold up fine - and as I've
written before
, I think the labs have a lot of headroom on inference. But a 90% cut in two months is hard to explain with efficiency gains alone.
It's increasingly becoming apparent to me that we may be ending up in a situation where the Astra, Fable and Opus-class models become a very specialised niche for specific tasks. The average "office" worker is more than well served by the smaller models, and increasingly most software engineering tasks are too.
I'm not convinced the market for inference is
that
large for the flagship models in the medium term.
This poses a very interesting problem for the frontier labs. These models are almost certainly orders of magnitude more expensive to train, and are potentially seeing their relative demand dropping, which means the cost of training them is spread across fewer customers. Strictly speaking training is R&D rather than cost of sales, so it won't show up in gross margin - but it does mean each training run takes far longer to pay back, if it ever does.
This results in two obvious outcomes, assuming this holds.
The first is frontier labs pivot away from training these huge models and instead focus far more on inference efficiency and the quality of the smaller models. How feasible this is I'm not entirely sure, the Chinese labs are extremely well suited to this and have a much lower cost basis for the most part. It's hard not to notice that the calls for regulation to pace the frontier would be rather convenient for the labs in this scenario. If nobody is allowed to race ahead, you can sweat each expensive training run for a lot longer.
The other outcome is that the frontier labs move up the stack away from providing inference for these larger models, and instead keep these to themselves and work on "vertically integrated" offerings, for example cutting-edge science research in pharma. We've seen Anthropic
quietly set up a biology lab
, which would track with this.
But as always it's hard to predict the dynamics of this market. Either way, we're seeing an explosion of affordable intelligence, which
itself
was not looking hugely likely a year or two ago.
I'd recommend keeping a very close eye on these pricing updates. My gut feel now is that the market is going to increasingly switch to rewarding those that can make breakthroughs in inference efficiency over raw intelligence.
