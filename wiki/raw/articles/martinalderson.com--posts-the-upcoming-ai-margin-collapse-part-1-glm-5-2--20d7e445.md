---
title: "GLM 5.2 and the coming AI margin collapse (part 1)"
url: "https://martinalderson.com/posts/the-upcoming-ai-margin-collapse-part-1-glm-5-2/?utm_source=rss&utm_medium=rss&utm_campaign=feed"
fetched_at: 2026-07-07T07:01:41.315719+00:00
source: "martinalderson.com"
tags: [blog, raw]
---

# GLM 5.2 and the coming AI margin collapse (part 1)

Source: https://martinalderson.com/posts/the-upcoming-ai-margin-collapse-part-1-glm-5-2/?utm_source=rss&utm_medium=rss&utm_campaign=feed

This is a two part series focusing on what I believe is perhaps the least understood upcoming shift in AI economics. If you've enjoyed this and want to be notified about the second post, please feel free to sign up for my
newsletter
.
The real DeepSeek moment is upon us
What feels like decades ago, markets recoiled at DeepSeek's R1 model. The theory being that given the underlying V3 model reportedly cost under $6m to train, the market therefore thought the huge investment in capex for model training was over, and thus
the stock price of Nvidia et al collapsed overnight
.
Of course, this was a hugely poor read of where the costs
actually
lie in AI. Training - while no doubt capex intensive - is a fixed, up-front cost. You spend hundreds of millions to train a model, then you are "done".
Inference, on the other hand, scales with your demand. It has
genuine
marginal costs. I've
written
about
this at length over the past year or so. Again, the mainstream understanding of this - that the API costs the providers
charge
are their
real costs
is mistaken.
Indeed, when Anthropic/OpenAI charge $25/MTok for inference, my napkin maths suggests that this is
probably
something like 90% gross margin on the cost of compute vs the rack rate. It may be a bit higher, or a bit lower (OpenAI's leaked financials suggest a ~60% gross margin on revenue, but this no doubt includes a lot of other costs like support, payment processing and other services they offer), but the whole business model of frontier AI labs is in short to spend a large amount of money on salaries on compute to
train
a model, then amortise that cost over
a lot
of
very
profitable inference. If you can amortise that cost over enough inference you turn from profitable on a COGS basis to... actually profitable.
GLM 5.2
I have been playing around with GLM5.2 from Z.ai for the last couple of weeks. I believe GLM5.2 is the first model that reaches the "bar" of a
genuine
open weights competitor to Opus and GPT (at the time of writing, the latest version of GPT was 5.5 - future models no doubt will exceed this).
It's genuinely very good and hard for me to tell the difference between Opus - my daily driver and it.
I've found that it is
slow
because of the amount of thinking it tends to do. For non interactive agentic tasks (like reviewing PRs in the background) which aren't time critical this is a non issue, but for interactive use it is definitely a tad
too
slow to keep my attention. This also somewhat reduces the cost effectiveness of it (more thinking means more tokens, which increases costs).
It also doesn't have vision support. It's funny how quickly I've gone from basically never wanting to use vision (because it was so inaccurate, I'd often pause sessions when I caught it using vision), to using it all the time - since Opus 4.7 introduced far higher resolution vision capabilities. It's genuinely frustrating it not being able to read image-based PDFs, screenshots and design files. I'm sure they have a more multimodal model in the works, but this is a significant weakness against the frontier labs.
Secondly, and something I
really
didn't expect to be a blocker, is the lack of/poor web search capabilities. It turns out that nearly every agentic session does a
lot
of web searching for looking up items. Z.ai provides a replacement MCP for web search, but it's pretty awful and slow. Fireworks doesn't provide any, though they gave me a very vague answer saying they are always looking to improve products. I would take that as no plans personally, but let's see.
I've managed to somewhat work around this by telling the agent to use a CLI based web search like
ddgr
, but this is a real weakness right now. I am very bullish on the potential of 3rd party web search APIs. This is actually a huge gap in what open weights model providers can offer, and it turns out
great
web search capabilities are
essential
for many agentic tasks.  Regardless, this no doubt will be solved with time - there are many people building web search indexes and it just requires the right partnerships and plumbing in place.
Drop in replacement
Where it gets really scary for the frontier labs is how
easy
it is to migrate to open weights models. Both Z.ai and Fireworks offer both an OpenAI compatible and Anthropic compatible endpoint. This makes it absolutely trivial to use with Claude Code and Codex. You just set the base URL to point to your inference provider, give it the API key and tell it to use GLM5.2.
Given Anthropic recently
announced
(then backtracked) on charging API rates for
claude -p
non interactive agentic use, you will find for many/most of those use cases you can just drop in GLM instead. And for interactive use, apart from the lack of vision and slow(er) speed, it was genuinely almost impossible for me to realise I wasn't using Opus in Claude Code.
This is
not
Microsoft or Salesforce like lock in, where you need to spend
years
planning a migration. The switching costs are incredibly low, and I would argue that are actually far less than trying to keep up on all the policy and term changes that the frontier lab models tend to scramble around with. It's possible that Claude Code will make it harder to use 3rd party providers, but there are many good open source options (like Codex itself and OpenCode, amongst dozens).
One concern I do hear from enterprise is data privacy and security. There is no doubt that using Z.ai's official API and subscription is almost certainly a non-starter, with their terms being at best weak and the deep connection to Mainland China. But of course, with open weights being
open
there are many other providers in the market, many with proper contractual provisions. And, if
that
isn't enough, you can of course host in on premises yourself, which actually opens up
even more
sensitive data - that couldn't be sent to any third party - to Opus-quality agentic workflows.
Cost savings
The going rate for GLM5.2 seems to be around the $4.40/MTok mark. This is less than 20% of the retail price of Opus and ~15% the cost of GPT5.5. Now, given it
does
use more tokens for a given task, this isn't a totally apples to apples comparison. But I'd be very surprised if it wasn't more than 50% cheaper for nearly all workflows, for a very similar level of quality.
In terms of subscriptions, Z.ai offers a "coding plan" subscription which mirrors the plans you'd see from Anthropic and OpenAI, but with a higher claimed usage limit. I expect for most professional use the very lax terms around training and data retention will make this a difficult sell, but if the frontier labs were to try and increase pricing substantially I can see it being a credible option for those that are budget-conscious.
I expect these costs for GLM5.2 to come down significantly over the coming months as well, as more optimisation is done to the serving stack(s). Wafer
wrote
an interesting write up of their efforts to run it on AMD hardware. They suggest that it is 2.75x cheaper per token to run inference on AMD vs Nvidia Blackwell.
Part two is where this gets interesting - what a collapse in inference margins actually does to the industry, and who is likely to win and lose. I'd keep Bezos's famous "your margin is my opportunity" line in mind. If you'd like me to drop it in your inbox the moment it's out,
sign up to the newsletter
- or grab the
RSS feed
if that's more your thing.
Disclosure - Fireworks kindly gave me some free credit to experiment with GLM to help write this article.
