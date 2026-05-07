---
title: "Open weights are quietly closing up - and that's a problem"
url: "https://martinalderson.com/posts/open-weights-are-quietly-closing-up/?utm_source=rss&utm_medium=rss&utm_campaign=feed"
fetched_at: 2026-05-07T07:01:37.225133+00:00
source: "martinalderson.com"
tags: [blog, raw]
---

# Open weights are quietly closing up - and that's a problem

Source: https://martinalderson.com/posts/open-weights-are-quietly-closing-up/?utm_source=rss&utm_medium=rss&utm_campaign=feed

It's been a bit of a given in the LLM world that there will be somewhat competitive open weights models. I'm not sure that's a good assumption anymore.
A short history of LLMs
In the relatively brief history of LLMs, there's been two types of LLMs - closed and "open weights". Closed models include nearly everything from OpenAI (despite the name!) with open weights models being released from other labs. Famously the Llama series of models were open weights, but more recently the Chinese labs such as MiniMax, Z.ai, DeepSeek and Qwen (Alibaba) have been the leading open weights models, with Google's Gemma series and OpenAI's
gpt-oss
models generally coming somewhere behind the Chinese ones.
Open weights models allow anyone to
run
the model on their own hardware. Typically models that were worth running required very beefy hardware - but this is rapidly changing, with smaller models becoming far more useful.
Being able to run these models locally - as opposed to via an API to an OpenAI/Anthropic/Google - has three main advantages.
Firstly, privacy and compliance. If you have (very) sensitive data, it's difficult/impossible to send it over an API to a frontier labs data centre. Being able to run the model 'on prem' means it never needs to leave your network.
Secondly, it allows more flexibility. You can use these models as a basis for fine tuning, or quantise (roughly speaking, compress) the models to your exact hardware standards.
Finally, and what I'll concentrate this article on is cost. They can be
vastly
more affordable than frontier models. Obviously if you're running them on your own hardware, you just have the capex cost of the hardware and cost of electricity and operations to worry about. But
more
importantly there are dozens of companies that will run them on a hosted basis for you, generally at less than 10% the cost of the frontier models per token.
Why open weight models are so important
Borrowing loosely from contestable markets theory in economics: even in monopolistic (or oligopolistic) markets, incumbents tend to behave competitively when there's a cheap and credible alternative. It's not a perfect fit - the theory strictly assumes near-zero sunk costs, which is obviously the opposite of frontier training - but the underlying mechanic holds. The threat is
latent
; the option for consumers to switch is what disciplines pricing.
In essence, I believe open weights models provide significant downwards price pressure on the frontier labs. This isn't absolute - clearly people will pay (much) more for higher quality models
and
the benefits of an inference contract with a ~trillion dollar company vs a cheap inference provider via OpenRouter. OpenAI et al offer SLAs and legally binding commitments on things like confidentiality.
But, it does provide enough downwards pressure in my eyes that it would be (very) difficult for the otherwise oligopolistic market behaviour to rear its head. If the frontier labs decided (coincidentally, of course) to raise prices by 5x overnight a huge amount of people
would
switch to open weights models, especially for less demanding use cases.
I think of open weights models a bit like generic pharmaceuticals from a price behaviour standpoint. If they're available, the big pharma companies cut prices to be
far
closer to the generic price, and they focus their efforts on new treatments that are a step "ahead" of the generic treatments to maintain prices.
Without open weights, the frontier labs would have far more pricing power than they currently do.
Licenses are a changin'
Open weights models availability isn't a given though. They're expensive to train, and the companies behind them are commercial companies - perhaps (heavily?) subsidised by the Chinese state - but they are not charities.
Indeed we have seen a significant tightening in the license conditions for these models. Meta has (so far) totally dropped the open weights for their newest "Muse Spark" models and doesn't release them at all.
Alibaba have increasingly released models first (or in some variants, only) on their API. Kimi's K2.6 license adds an attribution clause - if you have more than 100M monthly active users or $20m/month in revenue, you have to prominently display "Kimi K2.6" in your product's UI. France's Mistral also imposed varying license conditions on commercial use.
There are exceptions - DeepSeek actually became
more
permissive, but I think it's fair to say the general trend is to less permissive licenses (and both Meta and Alibaba stopping releasing some/all of their models at all).
What happens next?
In a (currently hypothetical) years time we may end up in a situation where most or
all
of the best previously open weights models are no longer released. While there will certainly be price comparison between them, if the increasing cost and complexity of training these models continues, it is fair to assume that we may end up with a handful of players - the big three Western frontier labs and a handful of Chinese ones - or perhaps a state-mandated 'merger' of them into one or two Chinese 'superlab(s)'. There is plenty of precedent for this kind of consolidation in strategic industries - China has done exactly this with rail (CRRC), nuclear, airlines, and telecoms, and the West isn't immune either - look at the defence primes after the post-Cold War consolidation.
The implications of this are frankly concerning. AI produces a vast amount of consumer surplus - I get far more than the cost of my tokens back in value, and I'd pay 10x today's prices without thinking twice. For high-value professional or agentic work, the gap between what I'd pay and what I do pay is much wider still. That gap is the prize an oligopoly without an open-weights floor would be in a position to capture.
In this world economic theory would point towards a historic concentration of power and economic wealth to a handful of companies - the labs start extracting that consumer surplus straight to their margin. And with an oligopoly of a handful of firms and huge barriers to entry (capex on new models), there is likely to be limited price competition.
Equally, this dystopian vision may be unwarranted. It may be that with faster and faster hardware, training a "good enough" model actually becomes
easier
over time. And despite there being only a handful of hardware manufacturers we see intense competition for AI hardware. Distillation - training smaller models on the outputs of frontier ones - is sometimes raised as a release valve, but it still depends on having access to a strong base model in the first place, which is exactly the thing at risk here.
A competitive open weights ecosystem has been a quiet load-bearing assumption underneath the whole AI economy. It's worth paying attention to the fact that it's eroding - and the implications for the wider economy are enormous.
