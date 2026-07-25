---
title: "The problem with hypergrowth AI startups"
source: "Warp Blog"
url: "https://www.warp.dev/blog/the-problem-with-hypergrowth-ai-startups"
scraped: "2026-07-25T06:00:41.914251+00:00"
lastmod: "2026-07-22T20:05:57.000Z"
type: "sitemap"
---

# The problem with hypergrowth AI startups

**Source**: [https://www.warp.dev/blog/the-problem-with-hypergrowth-ai-startups](https://www.warp.dev/blog/the-problem-with-hypergrowth-ai-startups)

Engineering
The problem with hypergrowth AI startups
Zach Lloyd
July 22, 2026
The coming revenue squeeze for hypergrowth AI startups
Startups that have had explosive AI-driven revenue growth might be in trouble. This is a consequence of the exact same
open-weight model
and
AI sovereignty dynamics
that are driving hype and discussion across twitter right now.
For context, the past couple of years have seen record rates of revenue growth for early stage AI startups. It has become a regular occurrence to hear of companies going 0 → $100M ARR in 12 months or less.
The reason this is happening  is because applying intelligence is very useful (duh). Whether in the coding domain, legal, copywriting, etc – it turns out that having intelligent tokens to bring to bear on a problem creates a ton of economic value. Thus you’ve seen companies like Cursor and Harvey and (remember?) Jasper explode in revenue. Almost every week you hear of a new “fastest ever to $100M ARR.”
But if you look under the hood at most of these companies, they are scaling their revenue by reselling inference at very low (and sometimes negative) margins. So, of the $100M revenue they have, they might be sending $90M to Anthropic, OpenAI, and perhaps some open weight model clouds, like Fireworks or Baseten. Hell, they might even be sending all of it.
Where the “fastest ever to $100M ARR” actually goes
Understandably, VCs seem excited about this growth. It’s hard to get folks to pay you,  so if you have a thing that they are paying you for, that’s concrete  proof of product-market fit. Or, is it? If your revenue has no margin or negative margin, then the value of the product or service you are providing isn’t adding anything on top of the intelligence you are re-selling. In the worst case, you could find yourself in the dubious business of selling $2 for $1 – that’s an easy business to grow, but not a good business to be in.
This is all fairly obvious: If you want a better measure of the value these companies are creating, you should be looking at their net revenue, not their top-line, which is driven by passing through token costs. VCs should get this, but I think a lot of them have lost the plot.
The story these companies tell to VCs is that if they grow the top line enough now, they can figure out the margins later. They claim that open weight will be good for them because it will drive down token costs while they maintain their prices.
I think the opposite is true. As tokens at any given level of intelligence become commoditized, it’s going to be harder and harder to charge a high price for them. Your AI services are at risk from a competitor offering similar services but taking less margin. So long as the value of what you provide is mostly in a thin offering around the tokens, you are at competitive risk. You can build some moat around brand, scale, etc., but depending on your domain, the switching costs might be low enough that your business isn’t safe.
In addition to the commodification of tokens, there’s another trend that also makes it harder for startups to make money from inference reselling. Most enterprises Warp works with want the ability to bring their own inference (BYO). They prefer this because (1) they often have their own commits to burn down with model providers; (2) they want control of who uses what model and where data is sent, and (3) they may actually have their own fine-tuned models. They want AI sovereignty, and rightfully so.
If you are a startup founder or VC, ask yourself this question - if tomorrow all of your customers demanded to bring their own inference, how much would your platform actually be worth? What would your customers pay for it?
Both of these trends will put downward pressure on revenue growth across AI startups. This wouldn’t be a big deal if we were looking at net revenue for these companies. But since VCs are largely anchored on top-line revenue, it puts any company that scaled revenue by reselling expensive tokens in a very tricky position. If you raised capital at a high valuation off of that rev growth, then you need to maintain it. If your revenue growth is coming from the unique differentiated value of your product or platform, you’re fine. But if it’s largely coming because intelligence itself is valuable, that’s a problem.
In a normal market, the sensible thing to do as COGS drop is to maintain your margin and pass the savings on to your customers; and maybe even take a bit more profit yourself. You as a business don’t lose much by doing that. But if the story you have been telling is all about top line revenue growth, this becomes harder to do. It’s a very bad look for top line revenue growth to decelerate or drop. So if you got that $100M very quickly, and growth starts stalling because token prices drive down prices across the board, that’s a bad spot to be in from a fundraising and momentum standpoint.
At Warp we are increasingly moving out of the token reselling business to align our incentives better with our customers’. As I wrote in my
guide to cloud software factories
, anyone deploying a cloud software factory to optimize ROI should be looking for a vendor that is not primarily a token reseller. This rules out the model labs, but it also rules out a whole cohort of startups that need token reselling to maintain their growth trajectory for their next round.
At the end of the day, we may end up back in a world where startup growth looks a lot more like it did before AI: high margins, slower top-line growth for companies that really have sticking power. And this might not be a bad thing.
Start your software factory
Book a demo and we’ll walk you through the workflows that map to your stack.
Get Started
Related articles
Jul 23, 2026  ·  5 min
The Cloud Software Factory Build Guide
A cloud software factory is an automation loop around the software development lifecycle: triage, spec, implement, review, verify, ship, monitor. This guide walks through building one from scratch on GitHub Actions runners, one skill at a time.
Jul 15, 2026  ·  7 min
How to build a cloud software factory - self-improving code review
I'll describe how to build a code review agent, and how to have the quality of reviews it produces automatically improve over time as part of a cloud software factory.
Jul 7, 2026  ·  17 min
A guide to cloud software factories for engineering leaders
Software development is shifting from interactive coding agents to cloud software factories — systems that automate major parts of the SDLC while improving security, compliance, and measurable ROI.
