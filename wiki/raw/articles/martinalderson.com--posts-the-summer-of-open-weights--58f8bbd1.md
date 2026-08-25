---
title: "The summer of open weights"
url: "https://martinalderson.com/posts/the-summer-of-open-weights/?utm_source=rss&utm_medium=rss&utm_campaign=feed"
fetched_at: 2026-08-24T10:32:19.822579+00:00
source: "martinalderson.com"
tags: [blog, raw]
---

# The summer of open weights

Source: https://martinalderson.com/posts/the-summer-of-open-weights/?utm_source=rss&utm_medium=rss&utm_campaign=feed

Over the winter of 2025, after the release of Opus 4.5, coding agents grew tremendously and usage exploded. I think this summer is proving itself to be a similar tipping point for open weight models.
The compute crunch and pricing
As I argued in my
margin collapse blogs
(
part 2 here
), we're starting to see some very aggressive moves on pricing. We've seen OpenAI cut the cost of
5.6 Luna
- its fast, cheapest tier - by 80%, and now
Sol
- its flagship - by 20%.
Meta is also offering its open model Muse Spark 1.2 for an almost-free price of $0.10/$0.20 per MTok on its contributor tier (where Meta may train on your data - standard pricing is $1.25/$4.25), with currently the cheapest API price for
cache reads
of $0.002 per MTok on that tier (!).
Anthropic hasn't matched this pricing yet, but the FT is leading with a
story
about the poor uptake of Fable 5 - Anthropic's $10/$50 frontier model, its most expensive tier - (tl;dr: it's too expensive) - headline: "Anthropic's best AI model struggles to attract users as cheaper tools thrive". And their Claude Developer social media account is suggesting they are still (extremely?) compute starved, wanting to make their weekly limit increases permanent but struggling for capacity:
By no means am I suggesting that Anthropic is in real trouble here - they have very impressive market share, but if the market starts to move towards much cheaper models, (currently) I believe they're the lab with the least ability to respond price wise because of their lack of available compute.
A plethora of alternative models are here
We've now got at least five AI labs outside of OpenAI, Anthropic and Google offering very good models - Z.AI, DeepSeek and Kimi - plus Meta and Grok. It's been strongly suggested that Meta is going to release their frontier models as open weights, which leaves us with four open weight models of good enough quality to drive agentic sessions.
No doubt there will be more - the Ox Alpha stealth model has been getting a lot of hype - but it really indicates to me that there is a
huge
amount of competition for this inference.
In my eyes there are two possible scenarios that play out here:
The first one is that the gap between frontier and challenger/open weights models continues to decrease substantially - to the point where it becomes almost a commodity between these models. This is
extremely
bad news for labs built around proprietary models. Right now, this seems to very much be the path ahead.
However, the other scenario I wouldn't discount is a
huge
leap from the frontier labs, which would then expand the gap. While historically this has been what happens - open weights close the gap, then just when it looks like they are about to catch up, OpenAI/Anthropic puts a new release out which expands the gap again. This time I do feel it's different - the gap has never been this small, and I'm struggling where to see this huge jump would come from. But regardless, it's definitely possible - and with many trillions of dollars of IPO market cap riding on this - I wouldn't rule out any surprises like this.
It's important to note as well that this leap could come through token efficiency too, not just pure "intelligence". The flagship models from Anthropic and OpenAI are ~5-10x more expensive than the best open weight models per token. But, it's fair to say the open weight models tend to use quite a
lot
more tokens per task. So if a hypothetical future Fable 6 could achieve similar intelligence to Fable 5, but use 10x less tokens to achieve the same end goal, it'd still be a very competitive model.
The lack of compute is a wildcard, though
I recently saw this very interesting
interview
with Gavin Baker, who makes the salient point that the industry has a
lot
of compute that was reserved for say $2/GPU-hour in 2-3 year commitments going to roll "off contract" and therefore going to be repriced.
Given current rates for Blackwell GPUs are significantly above that, he makes the point that these people are
hoping
to pay $4/GPU-hour - the win would be a doubling of underlying costs.
I think this really makes the token efficiency angle even stronger. There is
enormous
competitive advantage - more so than pure intelligence I think right now - in being able to serve these models more efficiently.
So what happens next?
Winter 2025 was about agents needing frontier intelligence at any price. This summer is about
good enough
intelligence at a tenth of the price - and whether the frontier labs can keep charging a premium for being slightly better.
Right now the pricing power isn't with the smartest model, it's with whoever has the megawatts to spare. OpenAI can afford to cut Luna 80% and put Sol on a three-month 20% promo because it has the capacity and the efficiency gains to back it up. Anthropic - renting 300MW from SpaceX at $1.25bn a month precisely because it
doesn't
- has to extend limits with a caveat that "capacity may be tight".
That flips the usual tech story. For decades software captured the margin and hardware was the commodity. Here the hardware
is
the margin, as I argued in
xAI's new rental business
. The handful of open-weight hosts - Fireworks, Together, Cloudflare and a dozen others - all have the same incentive: squeeze more tokens per GPU, because whoever does wins the price war regardless of who trained the model.
If that efficiency race keeps going, then cheap inference keeps pulling demand forward. The frontier labs' two escape routes are the ones I laid out in the
margin collapse series
: stay meaningfully ahead on intelligence, or make the model so much more token-efficient that the sticker price stops mattering. Fable 5 being called "too expensive" at $10/$50 tells you neither is guaranteed.
I wouldn't bet against a surprise leap - we've seen the gap close and re-widen before, and trillions in IPO market cap is a strong motivator. But this is the first summer where the open weights are close enough that most agentic work just doesn't need the frontier. That's a genuine tipping point, just like agents were last winter.
