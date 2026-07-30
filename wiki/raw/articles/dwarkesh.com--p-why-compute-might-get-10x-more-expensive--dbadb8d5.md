---
title: "Why compute might get 10x more expensive in coming years"
url: "https://www.dwarkesh.com/p/why-compute-might-get-10x-more-expensive"
fetched_at: 2026-07-30T10:06:47.582302+00:00
source: "dwarkesh.com"
tags: [blog, raw]
---

# Why compute might get 10x more expensive in coming years

Source: https://www.dwarkesh.com/p/why-compute-might-get-10x-more-expensive

I want to experiment with very quick blog post where I time-box writing for 2 hours. I won’t be able to nail down a lot of important sub-questions, but the alternative is just not making any progress on a lot of different topics I’m curious about.
Today I want to talk about the compute situation of the labs over the coming years.
Anthropic revenue has 10xed year over year. Anthropic likely ends the year with ~$100–150B of revenue. For this trend to continue, Anthropic would have to make $1T in revenue by the end of next year. There’s no deep reason why the trend needs to continue, and it very well might not - it’s ultimately a question about AI capabilities. But suppose it does. What would have to be true about that world?
Lab compute
3x-es
year over year. For a lab to 10x revenue while continuing to only 3x compute, some combination of the following 3 things has to happen: 1. Lab margins have to increase, 2. The price of compute has to increase, 3. Labs have to spend a greater fraction of their compute on inference.
My understanding is that basically all 3 of these things have been happening: 1. Anthropic went from 40% margins in 2025 to probably >80% this year for Fable inference
(though perhaps not on the marginal compute - see more below). 2. Spot prices for compute are up 40%+ from the February trough, and that likely understates how much more the labs have to pay (again, more below). 3. Roughly a quarter of OpenAI’s 2024 compute spend went to inference
according to Epoch
, and it’s certainly closer to 50% if not higher now.
Labs would prefer
not
to do 3 (spend greater and greater shares of compute on inference). As has been said jokingly, the point of inference revenue is to convince investors to give you more money to buy more compute to train bigger models. If you’re spending most of your compute on inference, you’re kind of declaring that AI progress has stalled, because it’s not worth investing more in training, and your business is basically that of a cloud provider. The labs do not think this is true - they think they are serving models that will look extremely shitty within a year in order to build up the business case to continue training smarter models.
So that leaves 1. lab margins will increase, or 2. compute gets more expensive. It will be more of the former if the leading 1 to 2 labs are significantly ahead of the competition. In a market, your margins are set by how much better you are than the next best alternative. For effect 1 to dominate, margins would have to be in the mid-90s percent by the end of next year. That sounds quite crazy to me. But it does sound plausible to me that AI lab revenues will keep growing astonishingly fast.
So that leaves one more effect to explain how this world of crazy $1T revenue by end of next year might come to be: compute gets a lot more expensive. As I mentioned, this is already starting to happen. The price increase is even stronger when we look at the tranche of compute that the labs need - they obviously can’t rely on spot instances - they need security for their weights and customer info, and enough scale to get good utilization and flexibility. To look at how crazy the compute market is in that tranche, consider the price at which Google and Anthropic are renting compute from SpaceX. Google is reportedly paying
$900 million a month for 110K GPUs
that are a blend of GB200s and GB300s. That’s roughly 2x the spot price per hour for those GPUs. And the current spot price is itself 40% higher than it was in February.
I want to emphasize the key conclusion here: as AI models become smarter, they’ll better monetize the same amount of compute.
If a true human-level software engineer that could run on an H100 equivalent, at current market rates for software engineers, that H100 should rent for over $250k a year.
That’s 15x today’s spot prices.
Of course you might expect that if we have 10 million extra software engineers, the marginal value of a software engineer would decrease and so that H100 wouldn’t necessarily be able to produce 15x more revenue than it currently does. But I actually don’t know if that’s true. If we applied this argument to people instead of AI, then this would be the classic
lump of labor fallacy
. Economists generally believe that high-skilled immigration does not decrease wages in the long run because of how specialization and innovation increase the value of labor. Maybe this labor supply shock is so big and so fast that this general heuristic no longer applies. But if we believe what standard economics says about labor, then the marginal value of compute (and thus the marginal price of compute) should become astonishingly high.
What would happen in such a world?
As the top models get better and better at monetizing compute, it becomes harder and harder to catch up. If by 2028 we’ve automated software engineering and the price of compute is 15x higher than it is right now, then it’s going to be much more difficult for you, with no revenue, to compete for compute against the frontier labs.
If you can train the best, most efficient model, then you’ll be able to charge MUCH higher margins than you can today.
This is the
Alchian–Allen effect
: when a fixed cost gets added to two goods of different quality, the premium good becomes relatively cheaper, so demand shifts toward it.
At $20 per H100-hour, it’s going to be extremely costly and stupid to use a weaker, less efficient model, because it’s going to burn more tokens running your expensive compute to get the same result
. So labs will be able to charge a very large premium if they can train a model that better economizes this scarce resource.
If you’re gonna have to pay so much for the underlying compute in the first place (directly or indirectly), you might as well pay extra to use the very best, most efficient model that runs on that same amount of compute.
A lot of current popular applications of AI get priced out. The reason AI is relatively cheap right now, at least in comparison to human labor, is partly that it can’t do a lot of things that top humans can do. At some point that will no longer be the case. And so using GPUs to make short-form video slop will just get priced out.
At the same time, this kind of prediction does pattern match onto the ways people have been wrong about scarcity in the past. I’m thinking of the Simon–Ehrlich wager, where Paul Ehrlich bet that the cost of a basket of commodities would increase rather than decrease in the decade leading up to 1990. This wager is famous in popular economics discussion, because it’s supposed to illustrate how Ehrlich’s Malthusian worldview was falsified — he underestimated the way in which market signals and human ingenuity would find ways to better economize scarce inputs. (Though other
analysis
shows that if this bet had been made in a different decade, Ehrlich would have won).
I’m guessing the Simon-Ehrlich basket of commodities is not the correct reference class for compute, because compute supply is much less elastic, and much less capable of absorbing large demand shocks, than the extraction of different metals is.
That 3x in compute capacity per year comes from multiplying the following numbers together
;
: 1.4x from Moore’s Law, 1.2x from new fab construction (
bottlenecked through at least 2030 by EUV tool supply
), 1.8x from AI taking leading edge wafer allocation from other devices (which will start to hit a wall by end of 2027, when AI will go from 60% of N3 to 86%). Seems hard to shift any 3 of those inputs into compute scaling much more, and the final one will actually hit a will within a year or two as wafer allocation gets saturated.
I want to clarify that at some point in the future compute becomes cheap again. At some point robots will be able to turn shores of silica sand and mines of copper into computers. At which point the price of compute should fall closer to the cost of raw inputs and tools. I’m just talking about this current regime where AI compute merely 3x-es year over year, which is not fast enough to offset the price effect of how much more useful AI is becoming year over year.
By the way, the fact that Ant revenue has been 10x-ing year over year, while compute has only been 3x-ing, suggests that there are very strong economies of scale in the model business.
Logically this makes sense - when you train a model, you pay this one time cost of learning all these different skills that you can then amortize across all your users. (Unlike with human labor, where each instance has to be retrained from scratch).
I wish we didn’t live in a world with such strong economies of scale of intelligence (because I’m worried about power concentration). But it seems we do.
