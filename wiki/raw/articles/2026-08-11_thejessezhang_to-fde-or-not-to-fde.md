---
title: "To FDE, or not to FDE?"
type: x_article
author: Jesse Zhang
handle: thejessezhang
date: 2026-08-11
date_ingested: 2026-08-12
url: https://x.com/thejessezhang/status/2087198484093149421
article_url: https://x.com/i/article/2086604287136980992
engagement:
  bookmarks: 1104
  likes: 496
  impressions: 259618
  retweets: 29
  quotes: 23
  replies: 18
mentions:
  - AshwinSreenivas
  - DecagonAI
tags:
  - forward-deployed-engineering
  - enterprise-ai
  - go-to-market
  - ai-agents
  - product-strategy
sources:
  - https://x.com/thejessezhang/status/2087198484093149421
---

# To FDE, or not to FDE?

Two-thirds of our deployment work is now done autonomously by our own product (via Duet).
This post is about why that is, our philosophy on building a product + deployment motion, and how that's evolved over time.

## Something we used to look down on is now the default answer

"Forward deployed engineer" has become the answer to almost every hard question in AI go-to-market. Deployments are painful? Hire FDEs. Customers can't self-serve? FDEs. Product isn't ready? FDEs. Anthropic and OpenAI have both stood up enterprise deployment arms explicitly modeled on Palantir, and every seed-stage company I talk to now has an FDE job posting. Job postings for the title are reportedly up several hundred percent in the last year.

What's strange is that this was, until very recently, a thing you got criticized for. Deploying engineers into customers was seen as a sign you didn't have a real product: your revenue was lower quality, and your margins were structurally capped. Nothing about the underlying economics has changed.

The key with FDEs is that they deliver outcomes. This is awesome in the age of AI, because enterprises may not be sure what the path to get to the outcome is, but it is clear that AI yields compelling outcomes.

At the same time, the role is becoming overused and should not be a crutch to hide a structural problem.

## "FDEs eat pain and excrete product"

Palantir (where my cofounder @AshwinSreenivas came from) popularized the role in the mid-2000s selling Gotham into the CIA, NSA, and Army intelligence units. And they took the criticism for a long time. Joe Lonsdale, one of the cofounders, has written that for most of two decades the mainstream view of Palantir was that it was a glorified consultancy rather than a real technology company, and that the view was based on a true observation, which is that a lot of their engineers spent a lot of time sitting with customers.

But Shyam Sankar, Palantir's CTO, had a line he repeated constantly: FDEs eat pain and excrete product.

Palantir's early Gotham deployments were deeply bespoke, built to answer one intelligence question for one unit. Palantir encoded the problems they saw as platform primitives: the ontology, object models, permissioning, workflow engines, provenance tracking. Those primitives became Foundry. Foundry became the thing you could sell commercially. Apollo and AIP followed the same path.

None of that would have existed without engineers eating pain in the field first. The pain was the input to the product, not a cost of sale.

As Foundry matured, standardized deployments dramatically reduced the need for custom work, gross margins climbed into the 80s, and Palantir shifted away from an FDE-led motion toward account-based selling. Many of those FDEs migrated into core engineering. They also famously turned down contracts where the customer just wanted Accenture with better software.

The FDE team wasn't the business model. It was the way to build the right product.

## Why some AI startups genuinely do need FDEs right now

If you were building a SaaS CRM in 2015, you did not need to discover the workflow. Twenty years of people had already thought through what a pipeline is, what a stage is, what a lead handoff looks like.

If you're building an AI agent for accounting in 2026, there is no established workflow, because literally nobody has ever used one of these. Nobody knows what the user journey looks like — not you, and importantly, not your customer either. They can't tell you what they want, because the thing they'd want doesn't have a shape yet.

That's the same situation Palantir started in. Lonsdale's framing was that they went forward-deployed out of necessity: they had strong technology and no idea how their early defense and intelligence customers actually worked.

So yes, send engineers. Sit in the room. Watch your thing break in ways your tests never imagined. In a genuinely new category, the last mile isn't a delivery problem, it's a discovery problem, and there is no substitute for being there.

## The trap is not starting. It's not stopping.

Once you know what the user journeys actually are, you should start taking the FDEs out.

You will not want to. Not because anyone makes a bad decision, but because keeping them is easier in every single sprint.

FDEs let you avoid every hard product tradeoff. You never have to decide what the product does, or which of two customer requests wins, or where the configuration surface ends. It feels free. Nobody has to say no to anyone. No painful architectural call gets made. The customer is delighted.

And now you've got every drawback of the model and none of the discovery benefit. Your cost to serve doesn't decline. Your margins stay capped. Your growth is bounded by hiring. Every bespoke fix in the field is a product decision you chose not to make. Each deployment should make the next one easier.

On top of that, very few startups can close the 8-figure deals Palantir was getting off the bat, which makes the economics even harder to sustain.

## One more thing not to confuse

FDE is also not the same as implementation. "Build this integration into their ticketing system" is real, necessary work, but it's execution against a known spec, not discovery of an unknown one. Bundling the two under one title is how companies convince themselves a growing services org is a product investment.

Models write code well enough now that a lot of what an implementation team did in 2023 is becoming something the product does itself. Eventually, you will be able to build an agent that can do all the last-mile work end-to-end. It can observe workflows and even interview customers.

## What we did instead

In our specific case with @DecagonAI, we fundamentally believe a product-driven approach is the answer, rather than a services-driven or FDE-driven one. Customer service is high-volume, repeatable, and decomposable, and when we talk to enterprises, two things are always consistent:

**Speed of iteration is key.** Shipping an AI agent isn't a one-time thing. It constantly needs to be tuned and updated over time. If each tweak requires engineering, it will be far too slow and expensive to scale.

**Vendor lock-in and sovereignty.** Given organizations' experiences with SaaS, no one wants to be locked into a vendor and dependent on their resources.

In the early days, Ashwin and I would personally just build whatever customers were asking for. As the product got off the ground, we made the explicit decision that our core value prop would be having the best product.

To be clear, we are still partnering with the customer to deliver the outcome end-to-end. However, even through that process, we are owning the build, while enabling their team on our product and giving them the keys. As the product has matured, the customer-specific work our engineering team has done has gone down dramatically.

That decision has had its tradeoffs. It meant not hacking something together in the field when that would have been faster. It meant taking escalations and turning them into requirements instead of patches, which takes time in the short term.

**The payoff:**

- Two-thirds of deployment work now happens autonomously through Duet: configuration, iteration, the long tail of tuning that used to require a human in the loop.
- It takes just a few days now on average to launch the first AOP, even for big banks, airlines, telcos, etc.
- Still a lot of work to do, but we are on the journey.

## So: to FDE, or not to FDE?

Go forward-deployed early. Get the signal. Put your engineers in front of customers forever.

Then ask the real questions. Is the bespokeness in your customer's environment, or in your own product gaps? Is the last mile irreducible, or just unbuilt? Are your FDEs discovering something, or absorbing something? And what got built into the product the last time one of them came back?

Use FDEs to figure out what needs to exist in the product. FDEs eat pain and excrete product. If yours are eating pain and excreting more pain, you don't have an FDE team. You have a services business.
