---
title: "Moat: Your OpenRouter Replacement (Command Code)"
source: https://commandcode.ai/moat
type: article
fetched: 2026-11-26
sha256: 8de6d31bc3ff53e76efbc20d69ea2d843e2f9af7958828b5357d120f35d3c7e5
---

# Moat: Your OpenRouter Replacement

Product page fetched 2026-11-26. Positioning as reported in the HN thread (item 50652184, 99 pts / 71
comments, posted 2026-11-26): a discounted-token gateway from Command Code. Users pay a membership fee
and then a reduced per-token price (~70% off DeepSeek, smaller discounts on other models) - i.e. a
"Costco for tokens" rather than genuinely unlimited usage.

## HN discussion highlights (item 50652184)

[fedupnow] It's not no limits, they're giving you a discount. Like a "Costco" card. You're still paying per
token. It's really not that great of a deal either, and there's thousands of these discounted offerings
now. Their prices are competitive to OpenRouter I guess but there's lots of discounted token shops
selling unused token allocations for 80% off.

[mythosofs] it literally is like costco, you pay the fee to be in the membership and then pay a reduced
price for the tokens :) (-70% on deepseek, less reduction on other models)

[Oras] I went through that website and docs trying to find the catch, but it's all fluff.

[edoceo] What about that TrustedRouter project I've seen mentioned on here? Do I even need a router? I
just got pi.dev to work.

[Oxodao] For Pi / Opencode, if you have a subscription to one AI service and you're happy with it, you
don't need a router. Routers are great to try out a lot of different models from different providers
without creating accounts everywhere. For API usage ... since you have to tweak your prompts depending
on the model anyway I'm not sure it's that good an idea to rely on a router.

[jochem9] I tried Commandcode Go (intent of upgrading to Goat - $10/m). Was comparing it to Opencode Go.
Both are not getting DeepSeek API TPS. Commandcode sometimes goes fast, but regularly drops in
performance. I ended back at DeepSeek API pricing - a bit more expensive (about 50% more) but consistent
performance is worth something.

[neya] You should really not be using OpenCode at all after their recent security clusterfuck and the way
they handled it (rather poorly). Particularly their online offerings.

[resonious] The trust element for LLM inference is huge. For serious usage I'm sending all kinds of data
... all my source code ends up on there. And with tool calling, it's basically full access to my
machine. Will we see attacks where an infected/evil router injects malicious tool calls? I don't want to
find out for myself. So personally I would take these cheap routers as too good to be true. It's not
really hard to make these yourself either.

[petesergeant] I had to write an embarrassing security disclosure report yesterday, because while
evaluating models for code security scanning I'd forgotten to set OpenRouter to be ZDR (for the first
couple of hours only), and then later got a notice to tell me that one of the end providers it'd be
routed to had been hacked.

[cyanydeez] i've got my gitlab setup on expiring tokens and moving to a One Time Password for securing my
interfaces. That's the closest one can get when all this data is potentially logged somewhere in "the
machine".

[trollbridge] Combination of DeepSeek, Xiaomi MiMo, and local models. I generally run everything through a
quick judgment in a local model basically saying "is this likely to violate a provider's TOS/guardrails?"
