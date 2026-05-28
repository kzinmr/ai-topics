---
type: x_article
x_article_title: "Avoiding Death on the Yellow Brick Road"
x_article_author: "a16z (J Schmidt)"
x_article_url: "https://x.com/i/article/2059491657683443712"
getxapi: false
date: 2026-05-27
tags: [a16z, vertical-ai, ai-startups, ai-application-layer, strategy, agentic-workflows, governance]
---

# Avoiding Death on the Yellow Brick Road

## Why The App Layer Isn't Dead 

The question I keep getting from founders and prospective employees: is there any AI application layer left to build, or are OpenAI and Anthropic going to kill everything?

There's a particular flavor of AI psychosis behind the question. Some people have concluded the only durable places to avoid the permanent underclass are inside a big lab or out on the frontier building in robotics, hardtech, or similar – theoretically anything "the labs can't touch." If every piece of software is about to be eaten, either by Codex or Claude absorbing the work directly, or by a future model that will make whatever you've built unnecessary, then run!

Listen I'm as much of an AI maximalist as almost anyone, and I think they're half right. The labs really are coming for a huge swath of the application surface. But "the application layer" isn't just one homogenous opportunity. The right framing is whether you're on the Yellow Brick Road or somewhere else in Oz.

The Yellow Brick Road is our shorthand for the path the labs are walking, where they're committing extraordinary resources. The reason the labs are best-suited for problems like code generation, writing, or image-creation is because these problems improve with raw model capability: every dollar spent on pre-training and post-training improves product quality. Meanwhile, the rest of Oz is inhabited by more complex, often vertical problems, that aren't as simple as giving a business user a horizontal tool with access to standard tools and computer use. The value comes less from the underlying model's raw capability (though that's still important!) than from the scaffolding around it that makes the output trustworthy, compliant, and operational inside a specific industry.

We're seeing this play out in real time as OpenAI and Anthropic are effectively telling the market they can't solve every problem with a generic AI coworker. They've announced massive forward-deployed joint ventures to build whole companies around configuring and customizing their models for the enterprise. You don't pour billions into those programs if you think the next model release is going to take care of it.

So if you want to get rich building AI apps – avoid the yellow brick road and build somewhere else in Oz. Here's what we've learned, and what some of our portfolio founders have learned, about what works.

## The Yellow Brick Road

If you're starting a company, The Yellow Brick Road is the most obvious path to go down, but it's the most dangerous. Take a high performing model, plug in some off-the-shelf connectors (like G Drive, Slack, Salesforce, Notion, GitHub), and ship some sort of agentic orchestration layer on top of that. Magic!

The problem with this is that this is what the labs are doing with Cowork and Codex. Obviously, they own the model, which gives them better margins, control, and the ability to exert pricing power on anyone who's downstream from them. But maybe most importantly also own the architectural choices that define what their products are built to solve well. They've been deliberate so far about the model plus tool calls pattern, and this is exactly what horizontal low-step-count work on the road requires. Even if a startup could somehow outperform Codex or Claude Code, the labs have massive distribution arms and the biggest brand halo in AI.

If you're an AI app company running that playbook with the same connectors, no sub-agents or configuration below it, and no distribution, you're likely walking down the road to nowhere.

## The Rest of Oz

It's not all doom and gloom for startups. There's an enormous opportunity outside the Yellow Brick Road, where startups have a clear path to own their customer and solve complex problems.

These businesses are building agentic experiences where the model is woven through a complex web of tools, automations, and integrations (read: software), leading most of these startups to be vertical by default. They can focus on multi-step and multi-player work, with sub-agents for role- and vertical-specific tasks, that Anthropic and OpenAI can't reach with horizontal platforms: gathering context across systems, then routing through multiple humans who have to approve at different stages. It often involves one or more legacy systems, tends toward needing deterministic outcomes where ambiguity isn't acceptable, and is at times tied to some valuable business outcome. The labs understand how valuable these problems are: that's why they're building their own outsourced configuration shops, and why an entire upmarket class of reinforcement learning businesses exist.

## Why the rest of Oz won't be owned by the Wizard

The response to the above would be that to date, it's been a pretty bad trade to bet against the models/labs improving. They'll likely just keep getting better and eventually eat into the market served by these application layer businesses.

The labs will certainly improve, but I'd argue there are a few ways the rest of Oz can defend themselves over time:

### Data and learning flywheels

A lot of what you internalize isn't in any training set — unwritten industry norms, undocumented standards, the tribal knowledge that lives in practitioners' heads. None of it is on the public web. No amount of training compute substitutes for being inside the workflows where this knowledge actually lives. There are two flywheels stacked on top of each other here: an across-customer one — patterns that compound as you see more variants of the same problem — and a within-customer one — the why behind specific decisions, the unsaid exceptions, the firm's own rules of thumb that only surface through real interaction with the system.

Even if customer data can't be used across customers, application companies will be able to leverage pattern recognition across customer problem types, and use that to inform the right architecture for future problems. A company that has run its agents through a hundred legal redlines, a thousand insurance underwriting cycles, or ten thousand SDR campaigns has internalized the shape of the problem in a way the next entrant cannot replicate by spinning up a fresh agent for the first time.

A horizontal agent could in principle build the same learning infrastructure. The reason it doesn't, beyond pure focus, is UX: capturing this kind of knowledge depends entirely on the workflow surfaces you give the user, and vertical players can shape those surfaces around exactly what their workflow needs to surface. Horizontal tools can't. Eval sets, labeled outputs, and edge-case taxonomies can compound into a vertical-specific data flywheel which can fuel fine-tuning the next entrant can't generate without comparable production exposure.

### Managing model variability and complexity

The labs are already routing internally — different model classes for different requests, ensembles under the hood. What they can't do is route across vendors, or evaluate a competitor's model for a specific sub-task, or use an open-source fine-tune for the narrow piece where it's actually best. The Rest of Oz company picks the right model for each sub-task across the entire model market, not just what its parent lab ships. It also does the work nobody wants to do — re-running evals on upgrades, recalibrating prompts for the customer's edge cases, rolling out without breaking production — every time a new model lands. The labs aren't doing this on the customer's behalf; they sell you their next model and tell you to migrate. The Rest of Oz company absorbs the migration. What the customer gets is the best intelligence available across the whole market, plus continuity through every upgrade.

### Cost optimization

Running every query through Opus 4.7 is the fastest path to negative gross margins. The best Rest of Oz companies route across tiers of models — frontier models for the hardest tasks, mid-tier for the bulk, smaller custom or fine-tuned models where they've earned the right to use them. Some are now post-training their own models on top of that, optimizing them for the narrow slice of work their customer cares about and serving them at a fraction of the cost of a frontier API call. The labs price the floor: the least intelligence available at $X. The Rest of Oz company sells the inverse — the lowest dollar cost for the specific level of intelligence the workflow actually requires.

### Governance

There is considerable value in becoming the control plane for how their customers run AI in that vertical – the place where permissions, auditing, what-the-agent-is-allowed-to-do, and what-the-agent-actually-did all converge. That control plane is built out of use case specific guardrails that look completely different across industries and job types. Because they own the tools, the workflows, and the data the agent touches end-to-end, they can provide deterministic outcomes in ways horizontal tools will struggle to. They are also the entity that absorbs the regulatory complexity for the end buyer — FRCP and bar rules in legal, HIPAA in healthcare, SEC and FINRA in finance, state insurance regulations, and so on. A horizontal player can't credibly do that without becoming a hundred different verticals at once. CIOs want to have a partner that contractually states they are handling compliance for the agents they are providing.

All of these come back to the same thing: **focus**. That could be a vertical (insurance, legal, accounting) or a function done deeply (sales, customer support, finance). Either way, the work needs a team that's heads-down on one customer set — its workflows, its edge cases, its regulations. The labs aren't built for that. They have to be everywhere, for everyone, which is how they built the Yellow Brick Road in the first place. The same trade-off keeps them out of the rest of Oz — you can be everywhere at once, or you can be great at one thing. Not both.

## Sales as an example – practical tips from 11x's technical CEO

How should you think about this in practice? Here's some practical tips from Prabhav Jain, the CEO of 11x.

**Focus on outcomes.** A tactical path to building a company that is resilient to the labs is to just start from a specific outcome that your customers really care about. For us that was helping companies generate more pipeline. From there the questions get tactical. Which activities do we want to own end-to-end that actually drive pipeline? Decompose each activity into tasks. Which tasks are agentic and which aren't. Which require intricate domain insight and which don't. The labs will ship workflows too, but when the workflow has many steps, messy inputs, hard-to-interpret state, or real-world constraints, a better model alone won't get you there. The work falls to good old-fashioned software engineering, and the labs hold no edge over a focused application company on that surface. For example, here are some of the tasks that we handle, some agentic, and some not: lead prospecting based on custom signals, lead enrichment, deep account research, context fetcher from CRM, channel-specific message writer, lead qualification agent, and email deliverability system. These aren't tasks you can just one-shot and require deep engineering.

The critical insight in the Oz analogy is that roughly half of any real workflow that is non-agentic carries no lab advantage. They are no better than you are at writing the deterministic software underneath the model layer. And the half that is agentic still requires you to tune, train, and constrain the models against the result you actually want. Domain knowledge often doesn't sit in general training data. Those skills get built from the ground up for the vertical or function, and fed into the model at the right moment in the workflow.

More importantly, those skills become outdated all the time because businesses evolve, so your ability to evolve those workflows and context becomes a competitive advantage. As an example, when we started our scaled email outreach product, "AI" written emails were just starting to come into play. Fast forward to today, folks have a tuned sense of emails that are AI written vs human and crucially, this changes every few months. Our agents have to constantly adapt given the market dynamic, but this is where the moat is built. In fact, despite this dynamic, our positive reply rates have gone up 4x in the last few months and we've generated hundreds of millions in pipeline for our customers.

**Work on problems where complexity is high.** Complex problems are where real business value gets unlocked. Otherwise you'll find yourself building a thin wrapper.

Decompose any sufficiently complex business problem and messiness shows up quickly. Here's an example from the GTM world that sounds trivial: you shouldn't reach out to a contact at a company if that company is already a customer. It's anything but. Maybe you have the domain associated with the company in your CRM. What about companies with dozens of subsidiaries? What if the CRM record has the parent's domain? What if a stale matching field in Salesforce sends a cold pitch to a current customer's CRO? Real-world data is messy. Humans struggle with it. Models don't magically clear that bar. Driving order out of that mess requires purpose-built agents engineered for the specific shape of the problem, not a general-purpose copilot pointed at a CRM.

**Guardrails aren't just to prevent bad stuff from happening. That's what your customers are paying you for.** Guardrails are severely underestimated. Even inside the same product, every use case needs its own. For us, a regulated financial services prospect demands different guarantees than a mid-market SaaS customer, and those guarantees roll down into how the agent is allowed to write, who it can contact, what data it can touch, what it can say on a call and how every decision gets logged.

A one-size-fits-all system collapses under that variance. Guardrails have to be built per use case, configured per customer, and audited continuously, and that work sits squarely with the application company. This is why we have FDEs and technical deployment strategists that need to tune for each customer's requirement. As an example, we worked with a F1000 institution to do consented outbound via voice to their large SMB customer base. The initial few iterations had low pickup rates - we had to quickly iterate and learn how to get this specific type of audience to engage in the first 10s of the call. SMB business owners behave very differently from larger B2B buyers or consumers. We now generate more sales opportunities for them in a day than their entire sales team for that segment in a month.

## Insurance as an example – practical tips from FurtherAI's CEO

Sales is one example. Insurance is another, and it makes the same point from a different angle. Here's how Aman Gour, CEO of FurtherAI, thinks about building off the road:

When we started deploying AI inside real insurance operations, we kept hearing a particular assumption: the model is the intelligence, and the workflow is just scaffolding around it.

The more carriers we worked with, the more convinced we became that this is backwards.

In insurance, a lot of the intelligence lives inside the workflow itself. Two carriers can run a submission through what looks like the same path: submission, review, quote, bind. But the path is the easy part. What separates the two carriers is everything inside it: which risks get escalated, which loss signals matter, which appetite rule wins when two of them conflict, when a human has to sign off, which external data gets pulled in, and how the final decision gets documented.

That logic does not live in one clean rules engine. It is spread across SOPs, manager reviews, underwriting philosophy, carrier-specific appetite, and years of operational experience. A lot of it is not written down in a form a model can simply read.

This is why we do not believe in a pure agent that reasons from scratch every time, and we do not believe in a rigid workflow that breaks the moment reality gets messy. And instead been building agentic workflows. The workflow gives you repeatability, auditability, and cost control. The agent handles variability and recovers when the happy path breaks. The human stays in the loop for the judgment calls where accountability matters.

On day one, this automates manual work. But over time, every escalation becomes a signal, every exception is a feedback and every human correction shows where the runbook was incomplete. Over time, the workflow stops being a script and starts becoming the carrier's operating memory. This is the part the labs will find hard to reach. They will keep shipping better models and better general agents, and they should. But they do not sit inside a carrier's production workflows long enough to learn why one account was escalated, why one risk was declined, or why an underwriter overrode the appetite guide and was right to do so.

That understanding only comes from running the workflow, in production, many thousands of times. The workflow you ship on day one is not the moat. The loop that production usage creates over time is.

For us, that is what it means to build off the road.

## How do you decide if you are in the rest of Oz or not?

**The tools-and-steps test**: How many steps does the work take, and how complex are the tools you have to build to support it? Compare a horizontal AI search across Google Drive — one step against one tool with a forgiving outcome, the user reads the summary and re-asks if it's wrong — to a multi-step legal redline against three years of firm precedent: dozens of steps across many tools, output that has to clear partner review and may need to be argued in court. Both look like "an agent doing work," but only one of them requires the kind of deep software a focused team takes years to build.

**The system test**: Are you building a system the customer runs their work through, or a tool that sits on top of a system they already have? Systems own the workflow end-to-end — the data capture, the governance, the records of what got done — and they're what the customer points to when describing how the actual work happens. Tools on the other hand just add intelligence to a workflow the customer already runs. The tool case generates real revenue and the labs can take it because the customer isn't depending on you as the orchestration layer. High ACV is usually a signal of a system, since systems replace real headcount and get paid accordingly, but it isn't a guarantee. Ask yourself if the customer would still need your tool if a lab shipped something that supposedly directly competes with you. If yes, you're building a system. If no, you're a tool — even if your ACV is high.

**The hedge fund / P&L test**: While lab performance is judged against benchmarks, rest of Oz performance is judged against your customer's P&L. Your customer doesn't care that your model scored well on SWE-Bench or MMLU — they care whether your agent closed the deal, redlined the contract correctly, or bound the right policy. If they're fixated on their workflow-specific outcome, not on a generic capability score, you're in the rest of Oz. If they're paying for generic capability, you're selling them something they can get with a Claude or Codex seat. The best agent businesses are going to need to execute like hedge funds — winning on alpha measured in customer P&L, not in benchmark scores.

## Both can (and will) win

We're going to see massive winners on and off the Yellow Brick Road. The models will continue to win because they own the model and they own the distribution for the horizontal tools they have designed.

The rest of Oz can win if they own the system of work — the surface where the work of the company actually executes and the data that flows from it gets captured. These companies own the data capture, the workflow system of action, and the governance. As more complex workflows mature in a vertical, they compound into one core experience the customer comes to depend on. As new model generations ship from incumbents and new entrants, the company becomes the layer that integrates and delivers them to the customer. The model is fungible underneath; the system of work is not.

The next generation of enterprise software is going to be built off the road.

If you're building it, reach out: jschmidt@a16z.com.
