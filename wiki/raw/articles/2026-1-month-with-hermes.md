---
title: "1 Month with Hermes"
created: 
author_id: ""
tweet_id: "2048678335950311860"
source: x_article
---

# 1 Month with Hermes

For the past month, I have spent so much time talking to AI — to the point where my fiance threatened to leave me (jk but she got very very mad).
Most of the time was spent debugging, fixing errors, adjusting the right configs, and making sure Hermes do things properly without making the same mistakes twice.
Disclaimer: Again, I’m using both Hermes & Claude as learning augments — they help me shorten the time for me to consume information & make decision (for investment, for trading/predicting, and for everything else in life). Execution is done purely by me (because I don’t trust AI enough yet even with the guardrails)
 
Here’s how my 1 month with Hermes went by
Week 1: learning how to configure basic model/inference provider set up. Tried many openrouter model setup/anthropic API and learned that opencode-go is the best subscription to get started
Week 2-3: learning how to properly delegate work, identifying clear tasks with clear end results. Learned that I have to be very specific in pointing out “remember”, “make sure to adjust [x] cron job” otherwise Hermes could forget or miss out on something. I also learned to implement health check to make sure to detect bugs ahead of cron jobs
Week 4: my world shattered on week 4 because I realized I’ve been using Hermes wrong all along. Hermes is not a builder, he’s an operator
Hear me out on this
What makes Hermes great is its persistent memory + self-learning loop — it remembers things across session, automatically setup skills if it thinks it’s necessary & can reduce time for the task next time (you can’t find this in Codex or Claude Code).
These characteristics make Hermes a perfect fit for recurring automated jobs like delivering reports/alerts that are tailored for your preference (i.e. a second brain that look out for you).
 
What it’s not good at is being a Builder
At least if you’re a non-technical like me, it’s so much easier to use Claude to create artifacts, websites, dashboards, slides, excel, anything that you wanna build with an ok design. It might just be because of the frontier models but also spending $100/month for Claude subs get you more inference than paying $100/month for Opus 4.7 on Openrouter.
Because of this learning, I now nominate Claude to be “the Builder” and Hermes to be “the Operator”
The Builder: builds dashboard/websites with passable aesthetics, configure UI/UX change or any other change (i.e. the developer/engineer).
Great for one-time building task.
The Operator: delivers report, analyze data, gleans & pulls data from the dashboard and learn from it (i.e. the analyst/assistant).
Great for on-going tasks tailored to your preference.
Hermes could build stuff — but based on my experience, it takes a lot of time for Hermes to build and the result is not on par with Claude (unless you use frontier models ofc). Plus, both Claude and Codex have built-in features/products that make it easy for non-technical people to navigate the UI and build, Hermes has none of that.
Here’s a concrete example on a product I’ve built with Claude + Hermes and how their roles are structured
 
PolyBond
 
PolyBond is my personal prediction market dashboard that surfaces opportunities from multiple sources. It’s designed to
Pick up aggregated sharp/whale signals
Potential insiders betting big into a specific market
Tracking LLM forecasters from predictionarena
Tracking opportunities from other sources (SN6 Numinous, Manifold)
The ultimate goal for this is to be a one-stop shop to finding great near-certainty PM opportunities that could replace DeFi yields.
Initially I used Hermes to build this out and quickly realized how bad that decision was — slow, clunky build, sad aesthetics.
And then I switched to Claude, Claude built this 10x faster saving me a lot of time in debugging and giving extra commands to get to the end result that I want.
For PolyBond, Hermes takes on the role of prediction market analyst. Every morning and every couple of hours, Hermes look at the dashboard/data sources powering the dashboard — the agent then delivers a brief report on what to focus on.
 
If I don’t have time to go through the dashboard myself, I can ask Hermes to expand and it’ll expand & summarize the insights for me.
 
What I’ve learnt so far
The flow of Claude as the Builder and Hermes as the Operator can be applied to any type of workflows.
For some, it might be easier to just have only Hermes deliver daily report/briefing instead of having a full blown dashboard (e.g. daily macro/tech/investment insights)
For others, it might be easier to just have a human-readable dashboard without the need of Hermes at all.
I’ve built several dashboards that I find useful — the best one that I like and constantly use a lot is “Bangkok This Weekend“.
 
It’s a dashboard that tracks fun activities to do during the weekend. It updates itself every Friday based on latest events/exhibitions happening around the city.
I used Claude to create this dashboard because I found myself wondering what to do during the weekend. The dashboard now covers 4 of my fav capital cities (Bangkok, Singapore, Tokyo, Hong Kong)
 
(There are usually a lot more events & more pictures during Fri - Sun)
Besides this one, I’ve also built a bunch of different things — personal x402 + 8004 dashboard, Bittensor dashboard that tracks subnet owner selling/buying back, travel dashboard. Most things are very easy to build BUT things with “premium” or useful data tend to cost $$$.
In the end, if you have a clear useful idea, it’s very easy to build things that bring value to yourself and to others (regardless of whether it’s a wrapper or a slop). So, I hope this article gives you an idea or an inspiration to get started!
Remember, you have to steer the AI. Not let it steer you.
Use the AI to augment learning. Not the other way around.
Thanks for reading and see you in the next one!
Personal Note: If you like something like this, let me know. Thinking of starting a sub-page on my Substack to share AI building resources + cool stuff I’ve built.
AND if you're looking for high signal/low noise prediction market opportunities/strategies that are replicable, I've gone over them in last week's the After Hour EP.52 — Gold in the Goose.
For any interesting questions you have dropped, I'll pick a few and answer them in-depth in Hermes article next week.   
