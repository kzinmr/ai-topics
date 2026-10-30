---
title: "HN discussion: StackOverflow now gets fewer than 1000 questions a month"
url: "https://data.stackexchange.com/stackoverflow/query/1926661#graph?t=1"
hn_item: "https://news.ycombinator.com/item?id=50282454"
published: 2026-10-28
fetched_at: "2026-10-30T11:20:00+00:00"
source: "hn-algolia"
extraction: partial_blocked
points: 789
comments: 718
tags: [hn-discussion, raw]
---

# StackOverflow now gets fewer than 1000 questions a month

Source URL (as submitted to HN): https://data.stackexchange.com/stackoverflow/query/1926661#graph?t=1
HN story: https://news.ycombinator.com/item?id=50282454 — 789 points, 718 comments, submitted 2026-10-28.

extraction: partial_blocked — data.stackexchange.com returns HTTP 403 to programmatic
fetches, so the underlying SEDE query/graph could not be scraped directly. This raw file
captures the HN submission metadata plus the top-level discussion, which is where the
substantive debate (cause attribution) lives.

## What the datapoint says (from the HN title + thread context)

- Monthly new questions on Stack Overflow (stackoverflow.com main site) fell below **1,000 per month** as of late October 2026.
- Sibling queries on the same SEDE instance: "Total monthly number of StackOverflow questions over time" (1926661, previously 1,550 HN points) and "What AI did to stackoverflow in a graph" (1953768, 483 points / 595 comments, ~3 months earlier).
- Repeated in-thread claim: the decline is visible across **all Stack Exchange sites**, not only Stack Overflow, "regardless of moderation policy".

## Top-level discussion (verbatim, truncated to 900 chars)

- **cebert**: I don’t think they’re gonna be long for the world
- **gnabgib**: Related discussion What AI did to stackoverflow in a graph (483 points, 3 months ago, 595 comments) https://news.ycombinator.com/item?id=48956949
- **armchairhacker**: SO has been useless for years now, but the other Stack Exchanges can be interesting, they deserve more spotlight.
- **werdnapk**: And how much was AI trained on their data? That's the sad part. Nobody asking new questions, so not much more for AI to train from.
- **paulddraper**: The highly technical sites -- StackOverflow, Unix & Linux, MathOverflow -- see little use. Others like SciFi & Fantasy and Worldbuilding have kept relevance. Unfortunately, these more niche sites relied on StackOverflow to drive referral traffic, so the whole platform is declining.
- **esafak**: It is sad because it was such a well designed community. But its lessons live on.
- **6510**: This question has already been asked? Pages bloated like myspace make me reluctant to click the search result and I wont browse around if a website doesn't load instantly. Search some exotic kind of bad. That they haven't implemented an LLM is quite untechnological. It should have an LLM assist with constructing the questions and it should have answers from all providers willing to donate tokens. Upvotes should generate wonderful data on how to construct an answer.
- **pseudosavant**: Wow, what a steep drop off. They've gotten fewer questions over the last year than they averaged per month in 2024.
- **999900000999**: Well, I always found SO to be an intensely hostile community. Chat GPT doesn't ban you for asking which IDE to use
- **mawadev**: I have some wishful thinking for everyone reading this: what if the people at StackOverflow built one of the best bot protections out there? I would honestly expect the graph to go up with all the LLMs and automated content spamming..
- **cowlevel**: You're underselling it. It's less than in their second month of existence - and that has been true every month for the past year. For the last few months it's also lower than their first month. Stack Overflow, effectively, no longer exists. And we know why. It's because of their hostile attitude towards their users. No doubt they'll continue operating until there's no more value in selling AI data licenses, then they'll unplug the servers and unregister the business.
- **kstrauser**: And here's why: https://honeypot.net/2026/10/09/what-really-killed-stack-ove... LLMs are most commonly blamed, but the drop started way before those became popular. I'm confident that its horrid moderation drove people away long before AI had a chance to. Nothing's quite as demoralizing as: Q: Why does adding two Python objects fails although their classes are compatible? A: [closed as a duplicate of "Why do people say JavaScript is weakly typed?"] I'm a reasonably bright person, with scads of StackOverflow fake-karma-Internet-points, but even I gave up trying to ask a question. There just aren't enough hours in the day to fight with hermits seeking the Ultimate Question and downvoting everything else.
- **EvanAnderson**: I miss Server Fault-- more the time in my life, I suppose, than the site itself. I enjoyed the hell out of answering questions on Server Fault for a few years. It came along around the time my teaching gig at the local community college transitioned to online-only classes (which, oddly enough, I couldn't find enthusiasm to teach). I feel like the Server Fault community tried to make it a more hospitable place than Stack Overflow, FWIW, back in the day. When Stack Exchange added the realtime chat system I got into interacting with members of the community more than could be done in questions or comments. There were even a couple people who ended up being IRL acquaintances. There were also wacky hijinks, too: https://meta.serverfault.com/a/1854 (I'm agog that those things happened 15 years ago, too... Yikes!) Then we had our daughter and my time to dedicate to the site became scarce. I kne
- **ChicagoDave**: If there is any proof that no one will be writing code, this is it. I encourage all young developers to focus on information architecture, application architecture, pure logic, domain-driven design, and harness engineering.
- **faangguyindia**: Reddit is going the same way. I know many people who have got banned and never managed to get back on Reddit because Reddit is using some very invasive and persistent banned user detection techniques. Thing is, they use AI to ban people; over time, many false positives accumulate and not everyone has the time and energy to appeal bans. Slowly, more and more user accounts get banned, and even technical people I know fail to make a new account which lasts more than 3-4 days. But the Reddit management is seeing this as a "win," not able to see the consequence of doing this.
- **Vaslo**: I answered a number of questions on there. Some non-native English speaker started going my answers and making language editing suggestions. The grammar was fine. I refused all the changes because they were at best basically the same or at worst incorrect. I refused maybe 4-5. The next day the guy got on and had done a bunch more then went to some of my answers and made hostile comments about my answers on simple things like Pandas for Python. That was that for that site.
- **mgdev**: They should reboot, focused on 1) humans (AI assisted or not) answering with real-money stakes, and 2) people betting on which humans are correct (borrow page from prediction markets) This does four things simultaneously: 1) It introduces consequences for being wrong, which in turn introduces real asymmetric incentives to be contrarian-but-correct - which are high-value answers you don't get out of a stock model 2) It creates real-world incentives for human guided votes to answers (because, again, there's a real-world stake) 3) Together, this gets humans back on the platform answering questions, which creates meaningful exhaust data that can be sold back to the AI companies. 4) It creates incentives to game the system, which creates yet-more exhaust data for training anti-fraud AI systems
- **tdb7893**: I'm curious if the quality of AI answers will get worse without public sources like Stack Overflow or if LLMs have gotten to a point where that doesn't matter as much.
- **h4kunamata**: Deserved. Could never reply posts to help other unless I had done: * 1 trip to mars * 10 trips to the Moon * Converted water to wine The worst system until you can finally help others. Also, the CICD guy from my previous job, could not answer a single question if he was unable to search there, full stop. It will be fun watching those who doesn't really know anything dragging the whole team down. A developer girl knew more than him, and fixed problems he was unable to fix.
- **nreece**: Still over $100M in revenue, now mainly from AI and Enterprise customers. https://archive.is/20261017123508/https://medium.com/inside-...
