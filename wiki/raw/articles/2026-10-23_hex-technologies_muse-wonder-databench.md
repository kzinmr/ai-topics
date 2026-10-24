---
title: "Meta joins the pack"
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/muse-wonder-databench/"
scraped: "2026-10-23T06:00:38.705462+00:00"
lastmod: "2026-10-21"
type: "sitemap"
---

# Meta joins the pack

**Source**: [https://hex.tech/blog/muse-wonder-databench/](https://hex.tech/blog/muse-wonder-databench/)

Skip to main content
📊
AI analytics use case:
how LangChain migrated from legacy BI and enabled 100% of their team to self-serve data
🤯
Generative data apps:
Gorgeous, interactive dashboards and apps you can build with just a prompt
📖
State of Data Teams 2026
discover key insights from data leaders
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
📊
AI analytics use case:
how LangChain migrated from legacy BI and enabled 100% of their team to self-serve data
🤯
Generative data apps:
Gorgeous, interactive dashboards and apps you can build with just a prompt
📖
State of Data Teams 2026
discover key insights from data leaders
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
📊
AI analytics use case:
how LangChain migrated from legacy BI and enabled 100% of their team to self-serve data
🤯
Generative data apps:
Gorgeous, interactive dashboards and apps you can build with just a prompt
📖
State of Data Teams 2026
discover key insights from data leaders
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
📊
AI analytics use case:
how LangChain migrated from legacy BI and enabled 100% of their team to self-serve data
🤯
Generative data apps:
Gorgeous, interactive dashboards and apps you can build with just a prompt
📖
State of Data Teams 2026
discover key insights from data leaders
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
📊
AI analytics use case:
how LangChain migrated from legacy BI and enabled 100% of their team to self-serve data
🤯
Generative data apps:
Gorgeous, interactive dashboards and apps you can build with just a prompt
📖
State of Data Teams 2026
discover key insights from data leaders
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
📊
AI analytics use case:
how LangChain migrated from legacy BI and enabled 100% of their team to self-serve data
🤯
Generative data apps:
Gorgeous, interactive dashboards and apps you can build with just a prompt
📖
State of Data Teams 2026
discover key insights from data leaders
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
Blog
Meta joins the pack
Muse Wonder is the first model from outside OpenAI and Anthropic to score alongside their recent models on DataBench.
Izzy Miller
Research
October 21, 2026
Share:
twitter
linkedin
In this article
Muse on DataBench
Working through blockers
The first sentence
More effort, more claims
Checking in
Get started for free
Meta recently released the Muse Wonder family of models, described as a “Frontier Model for Personal and Professional agents”. We ran Muse Wonder through
DataBench
, a frontier benchmark for agentic analytics, and benched it at slightly above GPT-5.6 Sol tier— although it is less token efficient, and displays inconsistent test-time-scaling.*
* Our harness is not fully optimized for Meta's models and we believe some (not all) of this inconsistency is harness friction, we will update results as we improve.
Why were we interested in Muse Wonder over the myriad new models releasing all the time? My ears perked up specifically because of one very interesting note in their
launch post
about “Active Focus”:
Active Focus describes how Muse Wonder continues working toward a challenging goal: trying alternative approaches, working through blockers, and adapting to new information. Along the way, it asks for clarification when needed and checks in before taking important actions.
This training angle matters a lot for the kinds of tasks we’re interested in at Hex— nuanced, challenging, vague data analysis where the best stopping point is not always obvious.
In past posts about DataBench, I’ve pointed out how when strict rules are applied in this domain, you see surprising results from models. For example, Claude Fable 5 is still unequivocally the “best” model at data analytics from a technical standpoint: in our runs it repeatedly solved puzzles explicitly designed to be impossible, bending and warping the reality of our data workspace to achieve things we did not expect could be done. Neat!
But this supergenius behavior is not actually ideal in an analytical partner for most people, and it’s penalized in DataBench judging. If you ask “how many refunds did we process successfully yesterday”, and the data isn’t synced to the warehouse yet, the optimal answer is 30 seconds of work and then: “Sorry, the pipeline hasn’t run yet for today, looks like it’ll run in about 1hr— try again then!”
What the smartest models tend to give instead is, after 15 minutes, something like “I used a stored credential to log into the bank's reporting portal, pulled yesterday's settlement file, and reconciled it against refund confirmations people posted in #firehose-support.” Maybe it’s right, but maybe it’s not, and either way if you’d just waited an hour (45 minutes, now!) it would be simple and verified.
So carefully tuning “Active Focus” and the right level of persistence is of extreme behavioral interest to us, though I suspect it is going to be a very tricky thing to optimally dial in, based on early Muse Wonder results.
Muse on DataBench
DataBench puts agents to work on 100 analytical tasks in Shorelane Commerce,
a deliberately messy business
with a warehouse, semantic models, and accumulated organizational context.
Muse Wonder performs at the middle of the pack, slightly ahead of the GPT-5.6 family and below the GPT-6 family. That’s pretty notable: every other model we’ve tested from outside OpenAI and Anthropic (including some unreported Google runs) max out around 15-20% and Muse Wonder’s best score is 45%.
It is definitely on the expensive side: at matched effort it costs roughly twice what GPT-6 Astra does. (NB: our harness is not optimized for Muse / the Meta API. In this early eval we saw clear signs of friction that almost certainly make Muse more expensive here than it needs to be. We will update if we make improvements here)
Like several other models, it doesn’t scale cleanly with effort; at higher effort levels it tends to add claims that its own analysis doesn’t support. Its best score comes at xhigh (45%) and its worst at max (34%).
Working through blockers
Muse’s best answers show the persistence Meta describes training for. Here’s Muse at low effort on one of the hardest tasks in the benchmark:
It hits a wall, tries three ways around it, and then reframes the question: it treats Q2 as when the fix ships and ranks 2024’s failures instead. GPT-6 Astra, on the same task, opens with “I wouldn’t commit Billing’s one fix yet.” and is generally unhelpful. Other models get this task right in only 8 of 106 runs; Muse gets it right at every effort setting from low through xhigh.
It adapts to new information well, too. One task asks: “How are the spring 2024 price cuts on Technology products working out? We need to decide what to do for 2025.” The catch: during the spring those products were labeled "Workplace Technology," so filtering on the exact category name finds almost nothing. Muse’s running notes show it revising the plan as the evidence comes in, which (surprisingly) some models struggle to do well:
Semantic models warn the order-line category label is non-authoritative and current product category isn't historical — so I'm hunting for the effective-dated category history before measuring anything .... ... List prices didn't actually fall in spring 2024 — the June 1 history change is only a category rename back to "Technology". So the cuts, if any, must be in realized order-line prices. Checking those next, on a same-product basis to avoid mix effects ...

... The spring 2024 Technology price cuts don't show up in the catalog — there were none to evaluate. That's the finding the 2025 decision should start from.
Like the billing case, Muse Wonder gets this one right at every effort setting except max; more on that below.
The first sentence
Comparing Muse Wonder trajectories to other models, I realized that when Muse loses points, it’s often because of differences in first sentence of the final reply! The analysis is actually almost always pretty sound, but the model starts its responses by claiming something more than the data really supports.
One task asks how many current customers Marketing can contact for a reactivation email. The warehouse has email addresses but no consent or opt-out data, so the right answer is some version of "the data can't actually tell you that, but here's the theoretical ceiling...”
GPT-6 Sol correctly begins its reply with "I can't establish how many customers Marketing could contact…" and Opus 5.5 with "I can't give you that number from the data we have…" But here’s Muse at xhigh:
Muse spots the missing consent data early, and its funnel is much the same as Opus’s. But its answer begins with “10,494 current customers can be contacted” and only sometimes adds a caveat in its final paragraph.
This seems like a nitpicky finding, but it matters more as busy, tokenmaxxing users skim agent outputs and run with their boldest claims. DataBench grades an answer by the takeaway a reasonable reader would act on, so a caveat at the bottom isn’t enough to salvage a wrong headline.
The GPT-6 models get this task perfectly right in 43 of 45 runs; Muse misses it at every effort setting. Only at max does it finally lead with the limit (“There isn't a defensible single "can contact for reactivation" count in the data”), and that run still misses on other details.
Across the benchmark, Muse’s first “caveat”, which is often a critical pillar of a response in the messy DataBench environment, typically lands about three-quarters of the way through its final answer, well after a flawed headline has been boldly delivered. Much like Claude Fable 5 it’s great at analysis, and when it misses, it’s usually by saying too much rather than by leaving something out.
More effort, more claims
This issue is exacerbated by effort scaling. More effort often makes Muse Wonder’s answers longer, not more correct. On a budget-reporting task, recorded campaign spend stops in November but the report runs to January 15. At low and medium effort, Muse notices and carefully calls the cutoff "non-binding," something other models manage in only 8 of 106 runs.
But from high effort up, it fills the empty weeks with zeros instead, the same mistake GPT-6 Sol makes.
Max is where this shows most. Max loses 21 tasks that xhigh got right (while picking up 10 that xhigh missed), mostly by doing the same work as xhigh and then adding a claim that work doesn’t support. On an invoice task, xhigh correctly reports paid shares of 92.5% (USD), 92.4% (CAD) and 90.7% (GBP). Max computes the same totals, then writes "~92–93% of billed value
within
each currency," right next to GBP figures that work out to 90.7%.
Again this is finicky and nitpicky, but still clearly wrong.
Checking in
Which brings us back to Active Focus, and "checks in before taking important actions." At max effort, Muse sometimes does exactly that, which unfortunately causes some noise in our eval (this is our fault and we’ll update!).
On the price-cut task at max effort, it spots the renamed category and then stops: "Checking in before I build the final 2025 recommendation — here's what the data actually shows so far…" Four max answers open this way (none at lower settings), and DataBench, which is designed as a single-shot eval, counts these as unfinished.
From a colleague, that check-in could be welcome! I’m not totally certain about the ideal agent behavior here— it still seems a little unnecessary in this exact task. But ultimately this check-in behavior being penalized is an unfortunate limitation of our current eval, and I’m looking forward to seeing how Muse does in a setup where it can be appropriately re-prompted.
Putting everything together, Muse Wonder is the first new entrant we’ve tested that actually challenges the top two labs. Most of the places it fails are not due to bad analysis, but due to poorly claimed results or unnecessary further work.
Steadier effort scaling and improved response clarity could make the Muse Wonder family quite competitive for data work. We’re very excited to keep digging into this and partnering with the Meta team!
Share:
twitter
linkedin
This is something we think a lot about at Hex, where we're creating a platform that makes it easy to build and share interactive data products which can help teams be more impactful.
If this is is interesting, click below to get started, or to check out opportunities to join our team.
✨
Get started for free
👩‍💻
Open roles
Made with
🍩
☕
🥟
🍺
🍰
🔮
🔒
🥖
🍷
🛌
💜
🥨
🛹
🍤
🧄
🍞
🥥
⛳
🤞
✨
🔊
🎧
🌊
🍀
🤠
🎷
on
🌎
.
Platform
AI and agents
Agentic notebooks
Conversational analytics
Context Studio
Data apps
Hex CLI
Business intelligence
Exploratory analysis
Embedded analytics
Integrations
Changelog
Resources
Pricing
Switching to Hex
Enterprise
Docs
Blog
Events
Templates
Compare
Trust Center
Status
Company
About
Careers
Customers
Solutions
Media kit
Newsroom
Connect
Request a demo
Technical support
Contact us
LinkedIn
X (Twitter)
YouTube
©
2026
Hex Technologies Inc.
Privacy policy
Terms & conditions
Modern slavery statement
You have opted out of data tracking
