---
title: "Our support agent now solves most tickets without a human"
source: "Pinecone Blog"
url: "https://www.pinecone.io/blog/support-agent-nexus/"
scraped: "2026-09-02T06:00:17.551288+00:00"
lastmod: "2026-09-01T12:00:01Z"
type: "sitemap"
---

# Our support agent now solves most tickets without a human

**Source**: [https://www.pinecone.io/blog/support-agent-nexus/](https://www.pinecone.io/blog/support-agent-nexus/)

←
Blog
Our support agent now solves most tickets without a human
Jackson Gold
Sep 1, 2026
Engineering
Share:
Jump to section:
Before Nexus
After Nexus
Quantified improvements with Nexus
How far the agent gets before a human is needed
Why Nexus
Share:
Subscribe to Pinecone
Get the latest updates via email when they're published:
Get Updates
Every support ticket used to start from nothing. A customer would write in, the default agent provided by our support platform would search our docs, and it would send back the closest general answer it could find. That answer was usually wrong, because the real one depended on which project the customer was on and what had happened to their account that week. In Q2'26, it resolved 24.6% of the tickets it was assigned. The rest went to a person.
Most of what that person needed was already in our own tables. The plan tier, the recent errors, what changed on the account yesterday. Someone had to open the ticket, look up account details, and write back. The customer waited through all of it. The agent had no way of knowing which table to check or how to ask. In mid-July, we used
Pinecone Nexus
to compile that knowledge once into artifacts the agent could query, and they've been on every ticket since.
Our early results show the agent now resolves 55.1% of the tickets it's assigned, with no human involved at any point, and a resolution often takes more than one exchange: the agent asks, the customer answers, and the ticket closes without anyone on our side touching it. Counting the ones it escalated after fully investigating the ticket, 77.6%. The agent escalates in two cases: when a customer requests a person, and when a human has to make a decision, such as a refund, a limit override, or anything the agent isn't authorized to grant. We watch the 77.6% more closely than the 55.1%, because it tracks the intake work our customer success team stopped having to do.
Before Nexus
One question was rarely enough: what the error actually said, what the customer was doing when it broke, whether anything on their end had changed. Each one went out, and then we waited, and the ticket stayed open through all of it. That work landed on our customer success team, and it scaled with ticket volume. They spent their days rebuilding context one question at a time, hours they'd rather have spent on proactive work.
The previous agent could answer questions, but it couldn't put them in context.
It had our docs, knowledge base, and runbooks. The account was the part it couldn't get to, and the account was where the answer usually was. That gap isn't really about access, either. Knowing that a billing question depends on the plan tier, that plan tier lives in one table and usage in another, that the two join on org ID, and that the usage figure lags a day. None of that is in the docs, and none of it is something a model works out from a ticket alone. It's the kind of thing a support engineer picks up over time doing the job.
After Nexus
A Nexus artifact holds what a support engineer knows and rarely writes down: the join keys, the freshness caveats, the canonical recipes that turn a support question into the right query, and the anti-patterns that produce a confidently wrong answer. It sits there, precompiled, on every ticket, instead of being rebuilt a call at a time.
Same list, now reachable. The agent can pull the plan, the usage, the recent errors, and what changed on the account yesterday, and it does that before it's needed rather than after a person asks.
Reaching the data is the easier half. The harder half is knowing what the data means once you have it. For example, a customer asks why one of their indexes is getting throttled. The index belongs to an org, the org has a plan, and the plan has a rate limit, so the answer looks like a single join away. But limits are enforced at the project level, and a project can carry its own, tighter than anything the plan implies. Skipping that hop produces an answer that tells a customer they're nowhere near their limit while their requests keep coming back rate-limited. The join was valid. It just answered a different question. Nothing in the schema marks the shortcut as wrong, and nothing in the ticket does either. A Nexus artifact can carry that distinction the way a support engineer would, on every ticket.
A ticket's wording is usually just the route the customer picked to describe their problem, and with the account in view the agent can read past it to the outcome they're actually after. Knowing what a complete answer needs is also how it spots what's missing, and the account closes most of those gaps by itself. One question usually remains, and only the customer can answer it.
The previous agent asked the same set of surface-level questions regardless of the ticket, typically about information already in our own tables. The new agent asks only what the customer alone can tell it, and answers from there.
Quantified improvements with Nexus
Metric
Previous Agent
Nexus Agent
Assign rate
76.5%
94.2% [+17.7 pts]
Assist rate
60.5%
87.8% [+27.3 pts]
Resolution rate
24.6%
55.1% [+30.5 pts]
Resolution + fully investigated rate
N/A
77.6%
The first three metrics are defined the same way for both columns. The fourth has no equivalent for the previous agent, which reported nothing about the work it did before handing off. The previous agent column covers 527 eligible tickets across Q2'26, 403 of which were assigned to it. The Nexus column covers 52 eligible tickets from July 17th to August 7th, 49 of them assigned.
Assign rate matters less as a percentage than as a signal we can act on. With our previous agent it was a black box. When a ticket didn't reach the previous agent we had no way of finding out why, so 76.5% was a number we couldn't act on. Our new agent reports every skip. Of the 52 eligible tickets it took 49, and the three it passed on were errors on our own side that we could see and correct. We expect to get that to 100%.
Assist rate had an even larger improvement with Nexus. Under the previous agent, 159 of 403 first responses did nothing for the customer, and those tickets sat until someone picked them up. Now 43 of 49 either resolved the ticket or moved it forward.
Resolution rate is the one that changed most: 27 of the 49 assigned tickets closed without a person touching them. The rest still go to a human, either because the customer asked for one or because the decision wasn't the agent's to make, and those arrive with the intake already done.
How we measured
A ticket counts as eligible if it arrived over email or from the console. Slack, Teams, and Discord are out, along with anything tagged junk, which covers spam, misdirected mail, and auto-responder loops.
Assign rate is the share of eligible tickets routed to the agent at all. Assist rate is the share where the first response either fixed the problem or moved the ticket forward. Resolution rate is the share of assigned tickets closed without a person.
These are early numbers on a small window. The difference in the day to day has been obvious since we put the agent live.
Resolution rate only credits a ticket the agent closes start to finish, so it misses something that matters just as much: how far the agent gets on the tickets it still has to hand off. That's what the resolution + fully investigated rate, 77.6%, is built to capture, and it's worth walking through what it actually counts.
How far the agent gets before a human is needed
Escalation is a last resort. The agent works the ticket as far as it can first, ruling out what the account can rule out, gathering what the conversation already contains, and asking the customer for the one piece only they have. It hands off when there's nothing answerable left, with a written brief of what it found.
A customer wrote in unable to log back in after signing up. The agent checked the account for blocks and suspensions and ruled both out, which put the failure at login rather than on the account. That left the network side, which only the customer could tell it, so it asked them to capture a failed attempt with their browser's network tab open. Then it handed the ticket over with the account issues already eliminated and a recording attached.
A compiled Nexus artifact is what let the agent run those checks itself. A support engineer would have run the same checks and landed on the same question, but only once the ticket reached them.
Resolution rate counts a ticket only if the agent closed it end to end, so that login ticket scores as a failure. Include the escalations that arrive finished like that one, and the figure goes from 55.1% to 77.6%. The 11 tickets in between are the ones nobody had to start from scratch, which is why we track the second number.
Why Nexus
The knowledge behind all of this already existed: that rate limits sit at the project level, that yesterday's usage row isn't final yet. It just lived in a few people's heads instead of somewhere the agent could reach it.
Every support team has a version of that: two or three people who know which fields lie, which numbers need a caveat, and which question to ask first. Their tickets close faster than everyone else's, and none of it is anywhere an agent can use.
That knowledge is also what makes an answer trustworthy. Raw table access is enough to produce a confident wrong answer: the customer told they're well under their limit while their index keeps returning 429s. An artifact carries the caveat and the join that's actually correct, so the agent says what a support engineer would have said, and hands off to a person as soon as the decision is no longer the agent's to make.
That's what Nexus is for. Someone who knows the systems defines what a complete answer needs, Nexus curates against that structure once, and the agent queries it on every ticket after that. The Nexus artifact that answers a billing question today handles the next one, and the one after, without being rebuilt. It's a knowledge layer that sits over your data and your systems, not a prompt that has to be reassembled a call at a time.
If you're running a support agent that starts every ticket cold, that's the part to fix.
Learn more at
pinecone.io/nexus
, or
Start Your Trial
today.
Share:
Was this article helpful?
Yes
No
Recommended for you
Further Reading
