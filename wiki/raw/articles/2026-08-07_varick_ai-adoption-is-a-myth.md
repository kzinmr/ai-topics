---
type: x_article
x_article_title: "AI Adoption is a Myth"
x_article_author: "@vasuman (CEO, Varick Agents)"
source_url: https://x.com/i/article/2085540776512192512
parent_tweet_id: "2085806422072418632"
date: 2026-08-07
getxapi: false
tags:
  - ai-adoption
  - enterprise-ai
  - enterprise-agents
  - applied-ai
  - career-strategy
---

# AI Adoption is a Myth

You're already in the top 1% of AI users. Yes, there's a gap between you and the folks on the frontier. The crazy kids running 20 terminals simultaneously with a knowledge base that rewrites itself after every run.

The bad news is you're never catching up to those people. The good news is that you don't need to. That gap, the gap in front of you, is far smaller than the gap behind you.

## The Barbell Distribution

It might not feel like you're in the top 1% because you see nerds on X spinning up agent fleets on a whim, but trust me, you're in the top 1%. You're likely using a model every day, you have opinions about how best to use it, and you maybe even tinker with agents or have set up Hermes on your own machine.

On the other hand, between you and the median employee at a big enterprise company is a chasm. They have maybe opened ChatGPT 4 times in 2 years. They used 3.5-turbo and decided AI was stupid, not realizing that GPT-5.6 Sol Ultra just produced a proof of a graph theory conjecture that had been open for 50 years. Every AI strategy article or post assumes that this person, this median employee, is going to eventually catch up.

I'm telling you, they won't.

For context, I'm the CEO of @varickagents. We work with the largest companies on the planet to implement AI agents and strategy across their organizations, so we know a thing or two about the reality of AI at enterprise.

## Claude Cowork Rollout: Real-World Data

I recently spoke to a leader of a non-technical enterprise's operations org (thousands of people). Without AI, he said, his team was moving at a decent rate. No major complaints there.

Then they rolled out Claude Cowork, and what do you know? The team kept moving at the same rate. He asked me why.

I've seen the same split across every organization. Doesn't even matter if it's 50 people or 5000, it's the same split every time: **a barbell**.

- **5-10%** were power users. They were using Cowork every day, leveraging skill files, connectors to Outlook, and more. These were the evangelists, the ones who pushed for Claude Cowork in the first place because they tinker with AI outside the job and see first-hand how impactful it can be.
- **~20%** would use it a couple of times a day, pretty poorly. They get some value out of it, but a fraction of what the frontier folk get.
- **~70%** didn't use it at all.

The dashboards in his org would indicate that the rollout counts as adoption. But to him, nothing got faster. **Both of these were true simultaneously.**

## Using It vs. Using It Well

Even among those who do use AI, the skill gap is enormous. Users of AI who have no idea what they're doing are far worse off after AI than they were before.

It is trivial to install Claude, point it at a repository, send a four-word prompt, and watch something happen (could be right, could be wrong).

Using it well is a different skill:
- Knowing when to clear context
- Knowing that the thing you just did twice should become a skill file the model reads every time, instead of a prompt you retype
- Knowing which 15% of the automation project requires a model for judgment vs which 85% just requires deterministic code
- And most importantly: **reading a diff properly before you accept it**

If you give the same ticket to two engineers, this divergence becomes apparent in the first 5 minutes:
- **Engineer A**: pastes Jira text into Claude, hits submit. Fix touches six files. Skims through, sees tests pass, merges. Three weeks later, config value changed for no reason.
- **Engineer B**: pastes Jira text, flags where code lives in the repo, specifies folders to touch vs leave alone, has skill files ensuring minimalist PRs, reads the diff, catches stray change, fixes with quick prompt, merges a PR half the size.

At least half of any organization is never going to get to that second version. Using AI well is a craft. It takes enormous iteration to get really good at using AI, and the inertia of someone who isn't on AI is insurmountable for many. Turning a slop-cannon into a refined power user is just as hard.

## A Perfect Rollout Still Produces a Barbell

The obvious objection is that "well these are just companies that are doing it poorly. I would do it much better." No. Even if you roll it out perfectly, you'll get a barbell no matter what.

Another executive we spoke with had just finished putting enterprise licenses in front of their organization. An eight-figure commitment for the year. **Roughly 10% of people burn 90% of the tokens.**

To put that into perspective: if the other 90% used AI the way the top decile does, spend goes up roughly 10x. $10M of commitment becomes $100M, and your best-case scenario is now your worst.

## Adoption Is Binary, Skill Is a Spectrum

McKinsey's 2025 survey says 88% of organizations use AI in at least one business function. Only 6% see more than 5% of their EBIT come from it. Another stat from MIT NANDA's GenAI Divide report: **5% of integrated pilots extract millions in value and the other 95% show no measurable P&L impact.**

If you track adoption as a metric, you're very likely asking (at most) an abstraction of a yes-or-no question:
- "Did this person log in this month?"
- "Did this person log in this year?"
- "Did this person send at least 5 prompts per day?"

If you want to differentiate between "has never opened it" and "pastes emails in for reformatting" and "has three agents in production touching the general ledger," you need a better system of measurement. This is not the case for 99.9% of enterprise AI adoption trackers.

But the number is technically real, and people are not lying about adoption. This is far easier to measure than the real thing you care about: **how skillful is each person at using AI, and what is their ROI per token used?**

That's why AI adoption is a myth. If you actually tracked this metric, you would realize there is no hope for the vast majority of people to become AI-native in the enterprise. Does that mean they have no value? Of course not. It just means that your implementation and rollout plan needs to be adjusted accordingly.

## Every Incentive Keeps the Chasm Open

Every AI vendor's roadmap pitches increased capability for agents but says nothing about the teams' ability to use it effectively. So the only people who use it effectively are frontier users, who are the loudest, so they get their say. They're also the most flattering to build for, so it's a clear win-win. **Every feature release raises the skill floor to use the product well, and this only widens the chasm** between the frontier and the majority in an organization.

I keep seeing enterprises seduced by the idea of "train your employees how to prompt!" This is 10% of the game. The other 90% is "train your employees to understand which workflows should never touch a model vs which workflows should be entirely automated." The reason you can't sell this as easily as the prompt-training is because the answer is different at every single company, and it takes a few weeks on-site to work out.

And the AI ninjas inside your company have no incentive to fix it either. Their leverage IS the chasm. They're doing their work 70% faster, then get to coast. Or they do the work of 3 people. But the moment everyone's on that wave, they lose their edge. Why would they fix it without additional incentive?

## The Solution Framework

### 1. Train Anyway (Diagnostic, Not Remedial)
You have to train anyway. You won't know who's in the top slice vs who's not until you do. Training is **diagnostic, not remedial**. There are definitely some people at your company who are interested in AI but lack the time and leverage to go deep. You should train to expose everyone's ability and comfort level.

### 2. Publish the Power Users' Skills
For your top slice, your power users, give them somewhere to publish, like a shared database, so that every skill they make gets posted, ranked, and installed by others. This is the only mechanism I've seen that turns one person's breakthrough into something sharable. Ranking is the incentive: power users will trade their edge for status in an org. The gap remains though: you can blast this to everyone and still 50% of people will never use a skill.

### 3. Background AI for Everyone Else
For everybody else, the work has to get done without them changing how they work, which means **the AI goes into the background**.

Why do you need AI to be prompted by a human anyway? Just figure out what the most repetitive processes are, build agents in your existing systems of record that employees are used to (Salesforce, NetSuite, Dynamics, etc.), and only pull in humans where you need a second glance.

For example: you have dozens of AP analysts who move invoices all day. 90% of this is automatable. You can't expect them to spin up agents or prompt their way through it reliably without breaking in production. So build the agents that run every single day, and now these analysts are just approving, rejecting, or editing the work the agents do.

**People are not in the market for a tool that helps them get the work done. They just want the work done.**

### 4. Change the Reporting Metric
Stop reporting "adoption" to your board. Report what share of the work today is manual vs hybrid vs fully automated. This is the only reporting and conversation that matters.

## About Varick

How do you build those background agents and stand them up? That's a separate article entirely. But for more color, this is exactly what we do at Varick, and it's the only thing that's worked for the clients we've rolled out AI for. These are incredibly large companies with thousands of people, and the playbook is the same:

We audit where the work actually happens inside an organization, then build agents into your existing systems of record, so the work gets done without asking five thousand people to become good at a craft they did not sign up for.

We work with companies doing over $500M in revenue, across finance, sales, procurement, operations, HR, and more. Check us out at varickagents.com. And if you want more content like this, subscribe to our newsletter at varickagents.com/newsletter.

## TLDR

- You're likely in the top 1%, and while there's still a gap in front of you, there's a chasm behind you. The median employee at your company is miles behind you, and the gap actually increases with every release.
- The average Claude Cowork or similar rollout goes like this: 5-10% become power users, 20% use it poorly, 70% hardly use it, and nothing gets faster, but you definitely burn millions of dollars.
- Using a tool and using it well are separate skills, and at least half of any organization never uses it well.
- A great rollout does not fix this. You can put AI in front of thousands, but 10% of your org will still burn 90% of your tokens.
- Adoption metrics collapse an entire spectrum into a binary yes and no, which is how you get 88% adoption while only 6% see real EBIT impact.
- You need to train the top slice and publish what they build. For everyone else, put the AI in the background of the systems they already work in.
