---
title: "The agent tax has arrived: Google Workspace's MCP pricing"
url: "https://martinalderson.com/posts/the-agent-tax-has-arrived/?utm_source=rss&utm_medium=rss&utm_campaign=feed"
fetched_at: 2026-11-28T10:00:44.419061+00:00
source: "martinalderson.com"
tags: [blog, raw]
---

# The agent tax has arrived: Google Workspace's MCP pricing

Source: https://martinalderson.com/posts/the-agent-tax-has-arrived/?utm_source=rss&utm_medium=rss&utm_campaign=feed

Google has
announced some major changes
to their Google Workspace (Gmail, Google Docs and all related apps) pricing, as part of their new MCP rollout.
I think this is the first major product that's attempting to tax agentic use cases. I'm not sure it will work.
What Google actually announced
Effectively two things. Firstly, all agents need to use MCP, not API to interact with Google. Quite how they plan on enforcing this I'm not sure, as the best I suspect they can do is behavioural profiling of what APIs get called, which seems to be quite difficult. I strongly believe this is mostly targeted at large AI companies and not smaller developers or solo users; but it is likely to have serious impact on any company that is (or will) start integrating agentic workflows into their products.
Secondly, a new pricing tier for said MCPs. In true Google style it's complicated, but in essence it's
a charge per 1000 requests
, with different types of requests using different pricing tiers. Roughly speaking, you can read 1000 emails via MCP for $0.20.
There is a free tier of 5,000 calls a day, but this is grouped across all access for a specific Google Cloud project. Probably fine for solo use or a smaller business's internal agentic tooling, but past that it is going to be a major issue.
The asymmetry: apps get a massive free allowance, agents don't
There is an enormous difference in the allowances for "legacy" applications using the REST API vs the new tiers for MCP.
On the REST API, each
user
of the API gets its own allowance. On the free tier for REST, each user can do
6,000 quota units per minute
of requests. This roughly equates to reading 100 emails a minute,
per user
. There is another project level cap of 20,000 emails a minute.
Previously going above this required a quota request but wasn't charged for. Now you have to move to the paid tier to go higher, but even there a REST app gets a huge free daily allowance - 10 million email reads a day - before it pays anything. MCP on the paid tier gets none.
So the real way to look at this is that if you are building a REST API you can read 20,000 emails a minute for free, but if you are building some agentic tooling you can read 5,000 emails a
day
for free, and if you need more than that you get charged around $0.20 per thousand for every email you read, including the first 5,000.
It's an enormous difference, and puts the
Google Maps pricing changes
of yore to shame in scale.
Why is Google doing this?
I strongly suspect there are two key drivers.
Firstly, given Google has fumbled agentic workflows
so badly
(until very recently, asking Gemini in Google Slides to bold some text would give you a "Sorry, can't do that" response), I'm sure that MCP access via OpenAI and Claude (and others) has absolutely exploded. The usage graph of these products with Google Workspace via MCP connectors must be going hyperbolic and no doubt has seriously ruffled the feathers of the product leadership at Google.
Given this, I suspect this is one way to throw some banana skins in the way of Anthropic and OpenAI. If you have business users paying $20/month for ChatGPT or Claude and many of these users read and search their Gmail from it, it starts becoming a
serious
clip of their margins. If a user searches and reads emails adding up to 10,000 requests via the MCP, that is going to cost the frontier labs $2/month,
per user
. Given they do have significant compute costs against these subscription based users, it's likely to badly impact the unit economics of many of these accounts.
So I'm guessing the thoughts are at Google HQ they can stem the tide of users using MCP in
external
products by making it expensive for those external AI products to use their Google Workspace data.
It also puts the frontier labs in a difficult position. They can either eat the cost of these MCP calls, which hurts margins at the worst possible time with investors combing through their financials as they become public companies. Or they can cap usage (and potentially pass the cost on), but this leads to a poor user experience, and perhaps shifts some people back to using Gemini for agentic tasks - as Gemini won't have these caps.
Secondly, I have had a feeling for a while that Google's search business is more fragile than it looks. Search revenue still grew 12%
last quarter
, but that missed analyst estimates by over $1.5bn, and I think agents doing the searching instead of humans is only going to make that worse.
The revenue from this is small fry next to search. But it gives Google a story to tell investors: if agents are going to replace humans clicking around their products, they have a way to charge the agents instead.
Who follows?
If this works out then I suspect we will see a rush of other companies trying the same strategy.
Any system of record - Salesforce, Atlassian, Intuit to name some at random - will be (very) tempted to try this strategy.
The difficulty is that you need to be
very
sure that you really
are
a system of record. Agents are eating a
lot
of SaaS workflows. There is the risk this backfires entirely, and someone just downloads their data via CSV or some other old school mechanism and just has their agent query that.
Obviously at enterprise this is different. I still don't recommend anyone vibecode a Salesforce replacement, despite how many times I hear people thinking about it. But I think for B2C and smaller-tier B2B introducing these restrictions is a good way to get your churn rate to skyrocket,
especially
given a lot of legacy SaaS products have already very poor MCP usage and are at risk of being completely forgotten about.
Finally, keep in mind that agents have also
massively
reduced switching costs. You can just point an agent at SaaS product A with a browser tab connected and ask it to migrate data to product B (which could be a self hosted open source solution). It's scarily good at doing this - often enumerating internal APIs to bulk download data and transform it to the new system.
I saw the Cloudflare CEO
tweet
that he's tempted to set up a Gmail competitor on the back of this. This may open the floodgates of users switching from legacy SaaS. It certainly doesn't
feel
right to me that we pay a (rapidly increasing) amount for Google Workspace, and now they want to charge us
again
to read our own data in a different AI system.
Conclusion
This is no doubt going to be a fast moving topic. But this is the first mainstream attempt at an agent tax and a 'post agents' SaaS billing structure.
The agent tax is simple enough to describe. The same data, from the same account, costs effectively nothing when an app reads it and $0.20 per thousand when an agent does. You're not paying for a new feature or more compute. You're paying because of
what
is doing the asking.
That's a big shift. For twenty years the deal with SaaS was that you pay per seat and the API comes along for free, because the API made the product stickier. Agents break that deal. A seat that used to make a few hundred requests a day by clicking around can now make tens of thousands, and half of them come from a competitor's product. Google's answer is to stop pricing the human and start pricing the agent.
I can see the logic. But it only works if your customers can't leave, and agents are exactly the thing making it easier to leave. Charging people a second time to read their own email is a good way to make them wonder why they're paying the first time.
Honestly I don't know if this sticks. If it does, expect every system of record to have its own agent tax within a year. If it doesn't, I wouldn't be surprised if the pricing looks very different by the time billing starts in April.
