---
title: "OpenAI may be in cost control mode"
source: "https://micjm.com/blog/openai-is-in-cost-control-mode/"
hn: "https://news.ycombinator.com/item?id=50652527"
collected: 2026-11-27
type: article
sha256: pending
---

# OpenAI may be in cost control mode

Source: https://micjm.com/blog/openai-is-in-cost-control-mode/
HN: https://news.ycombinator.com/item?id=50652527 (335 points)

## Article text (extracted)

OpenAI may be in cost control mode | micjm micjm blog about subscribe OpenAI may be in cost control mode 2026-11-26 OpenAI’s recent release of Astra 6.2 and Sol 6.2 was widely panned. What happened? Based on our data, it looks like they’ve been tuned for cost savings. Specifically output tokens per task and reasoning tokens per task have dropped. Here is a chart of high-level cost change from the GPT-6 to GPT 6.2: The X axis in the above chart is the ratio of spending of the GPT model compared to opponents in our battle system for real work . The Y axis on the above chart is Elo from our leaderboard . The moves in the chart are significant, here’s the same chart with confidence intervals: What changed Compared to opponents, Astra and Sol seem to be reasoning a lot less. Here is a chart of how much models reason compared to opponents in the same battle. Above the line means more reasoning and below means less. You can see that both Astra 6 and Sol 6.1 were pretty normal models, but Astra 6.2 and Sol 6.2 become outliers. We can see the same effect with output tokens: Are these changes significant? The p-value on output dropping is 0.0055 for Sol and 0.022 for Astra. The p-value on reasoning dropping is 0.00013 for Sol and 0.0064 for Astra. In conclusion, Astra and Sol appear to be cost tuned compared to their predecessors, and to a degree that makes them underthinking outliers. What I'm working on Agent Duel - a battle system on top of OpenCode

## HN discussion highlights (item 50652527, 335pts)

# OpenAI may be in cost control mode | 335pts | seizethecheese

[seizethecheese] "It's over". But really, OpenAI's business is heavily skewed towards consumer, meanwhile enterprise has better margins and they're losing to Anthropic.

[baq] More like people just ran out of stuff to do with smarter, more expensive models. Please note this is very much not good for everyone if true.

[Havoc] It definitely isn't. Hosting a non-terrible model locally can be done with capital outline that is high for a hobby/toy but not unreasonable. So AI coding is absolutely within financial reach of many. It's when people insist on using SOTA beasts of models to design their blog where things get sketchy on economics. AI is here to stay...routine use of SOTA as default...not so sure about that

[kobalsky] there are third parties, who don't have the luxury of burning money, selling access to open weights models at affordable prices they may not be as good as frontier models but not that bad either, and harnesses will only continue improving.

[howard941] The bubble deflation will be like Hemingway described bankruptcy. Gradually, then suddenly.

[voxgen] They're also dispensing resets dramatically less frequently[1]. One of this week's resets was even limited to just Business plans. Perhaps this is a test of the mobility of their customer base? They knew they were going to have a bad month after the GPT-6.2 models were panned on launch, but aren't visibly trying to keep customers. [1] https://codex-resets.com/

[minimaxir] Tibo claimed in a podcast months ago once that there isn't a rhyme or reason to the resets, which is crazy for several reasons. I suspect with IPO pressure that will no longer be the case.

[jhloa2] I wonder if it's because everyone with a paid plan seems to be putting it towards gta 6 right now.

[operatingthetan] The IPO is dead in the water for the foreseeable future. I'm sure Sam is elated that Dario went first.

[jrflo] This is a common pattern over the last few years. Same thing happened with Opus, 4.5 was amazing, and gradually got worse until we hit 5.5. Seems like the labs follow the formula: 1) release amazing model 2) distill it and optimize for inference costs while trying to maintain perf 3) repeat

[seizethecheese] It certainly seems like this, since Sol 6.2 outperforms Sol 6.1 at lower cost on benchmarks, but not in real world battles from real people (the data is from here https://github.com/bottomless/agent-duel ).

[SOLAR_FIELDS] >Same thing happened with Opus, 4.5 was amazing, and gradually got worse until we hit 5.5 Would love to see an eval benchmark that shows the same task degrading over time to demonstrate this. Else it's just feels.

[srcreigh] I guess they are usually spending (say) 50% of their GPUs on training and 50% on inference, after launching a model they do more 80% inference for a few days then back to normal

[yababa_y] Models build niches of slop and having slop in their context degrades their performance. The "amazingness" exuberance is what itself produces the gradual decline in performance.

## HN discussion highlights (item 50651117, GPT-6.2 usage cuts, 491pts)
# OpenAI cuts GPT-6.2 usage: Astra hits limits 40% faster, Sol 25% faster | 491pts | Herrera

[rspeele] These models were already like "meh, ok I guess, not really 1:1 with Fable and Opus but at least they're cheap" and now it turns out they were not even supposed to be cheap. Is OpenAI ok?

[stoorafa] One of their biggest appeals to me was I could keep going without as much worry I’d hit my limit I guess not anymore :/

[Aurornis] They actually sent a weird, short email about it earlier that didn’t have enough context to understand what was happening. They had to send a follow up email today with enough details to clarify. It feels like the communication I’d get from a tiny startup doing the move fast and break things routine, not a company on the verge of a trillion dollar IPO.

[_s_a_m_] "billing mistake" my ass. the last thing they'd do is how much money they charge, the scamming beginns.. Luckily there's black friday offer by Google for the Pro account and Gemini Neon is almost exactly as good as Astra.

[_puk] There was a billing error. Anecdotally I was using Astra 6.2 recently for hours and was still sat at 100%. To the point I went clicking around the settings to see if the usage widget was broken. But.. This feels like they are using fixing an issue to do a much wider rug pull in the hope people like me will say "but it was broken" and deflect from the wider point. So don't let my anecdote deflect your ire!

[andriy_koval] more likely they are not competitive on coding models market, losing money, and want to shift funds somewhere else (e.g. chatgpt consumers with shopping and ads) where they hope to actually make profit.

[preommr] Oh to be a fly on the wall at openai right now. I am not buying the bravado that they're not concerned, or the excuses that they've actually got really powerful models like Bel that they're using for other secret projects.

[sgnelson] Wow. I feel like this is their backdoor way to make the changes they were going to make to the plans (that they announced at the end of September, and then they supposedly quietly dropped?) I felt like I was going through my plan extraordinarily quickly before this. Now, I don't know if I'm going to keep the subscription. It definitely doesn't seem to be a good value proposition, whereas with Anthropic I feel like I'm getting a good deal.

[demosthanos] Whether Anthropic or OpenAI is a better deal has been alternating back and forth the entire time this product category has existed. You can bet that it'll happen again before too long in the other direction.

[lukeify] Behind in productivity integrations that Anthropic provides, models that aren't quite as good as Anthropic, with a harness that isn't quite as polished as Claude Code, with mindshare and usage still showing Claude Code is the more popular tool. But yeah sure OpenAI, go right ahead and make your developer experience even worse.

[demosthanos] In OpenAI's favor is that they're still the one of the two that allows me to use my subscription with Pi, which is enough to keep me coming back. Claude Code's bloat and incessant churn have started to actually hurt productivity more than they help unless you have unlimited tokens to spend on the latest "fan out" or "workflow" stuff.

[drnick1] Codex still accepts most RE tasks without too much trouble, whereas Opus 5.5 immediately refuses to look at binaries.

[from_memory] I have noticed this in my day to day. Nice change, takes the pressure off of prioritizing jobs versus being able to try some more creative things. Not totally, not yet, but they are getting there I think. edit: wow, reading through the comments, I am in the minority. I'm still grateful for whatever that is worth.

[demosthanos] I feel like maybe you're thinking of a totally different change? This is about them decreasing how many tokens you're allowed to use on the latest models with their subscriptions.
