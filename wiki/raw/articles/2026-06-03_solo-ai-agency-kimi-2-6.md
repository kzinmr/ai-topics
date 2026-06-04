# How I Run an AI Agency Solo (No Employees, $40k MRR)

**Source:** X Article (id: 2059627968872280065), bookmarked 2026-06-03
**Author:** Anonymous solo AI agency operator (X handle unknown)
**Original URL:** https://x.com/i/article/2059627968872280065
**Content extracted from:** X Article plain_text (full content via xurl bookmark fetch)

---

I run an agency that does $40k MRR. No employees. No contractors. No standups. No payroll. No "let me check with my team and get back to you." Just me, a laptop, and a delivery system that does the work 5 people used to do. Total cost to run the whole thing: under $300/month.

That's not a typo. The agency clears more than $39k of that $40k every single month, and I take home a margin that no staffed agency on earth can touch.

For a long time I believed the same thing you probably believe right now: that scaling an agency means hiring. More clients, more people. More people, more management. More management, less actual work and thinner and thinner margins until you've built yourself a job you hate. I don't believe that anymore. The math changed and almost nobody noticed.

This article is the full breakdown. The offer, the delivery engine, the exact model stack, the unit economics, the acquisition system, and a 90-day plan to your first $10k MRR.

Quick context: I run an AI automation agency. I build automations and AI systems for small businesses and lean teams. Lead routing, customer support agents, content pipelines, internal ops tooling, data workflows. Boring, high-value stuff that businesses gladly pay monthly to never think about again.

My $40k MRR is 14 clients:
- 4 anchor clients on $5,000/mo retainers = $20,000
- 6 core clients on $2,500/mo retainers = $15,000
- 4 lite clients on $1,250/mo maintenance = $5,000

## 1. Why the Solo Agency Is Suddenly Possible (The Headcount Trap)

The bottleneck was never clients. It was delivery. In the old model, doing the work meant people. Sign 3 clients, hire a junior. Sign 5 more, hire two mid-levels and someone to manage them. Each hire is salary, onboarding, mistakes, sick days, churn, and the slow drift where you stop building and start managing humans who build worse than you do.

And here's the trap inside the trap: every person you hire eats your margin. A staffed agency at $40k MRR is keeping maybe $10-12k after payroll, software, and overhead. The other $28k walks out the door in salaries.

The reason the solo agency works in 2026 is simple: the production layer, the actual labor of delivering client work, can now be done by one model instead of a team. For me, that model is Kimi 2.6. Not the strategy. Not the client relationship. Not the judgment. Those stay with you. But the execution — the part that used to require a team of people grinding through tickets — that's the part that got automated.

## 2. The Offer: What a Solo Agency Should Actually Sell

The work has to be deliverable by a system, not by heroics. That means productized, repeatable, and scoped tight. Pick work that is high-value to the client but mechanical to produce.

Scope it so the deliverable is defined, not open-ended. "We'll build and maintain an AI support agent that resolves your top 20 ticket types, with a monthly retainer for tuning and new flows" is a product. The retainer is the key.

Charge for outcome, deliver with system. Clients pay $2,500-$5,000/month because of what the automation saves them: a support hire they didn't make, hours their team got back, leads they stopped dropping.

## 3. The Delivery Engine: How You Deliver Without a Team

Every piece of client work flows through a four-stage pipeline, and I'm only personally touching two of the four stages:

**Stage 1: Intake (me, 10 minutes)** — I take the request (a new flow, a bug, a feature, a content batch) and translate it into a clear spec. This is judgment work.

**Stage 2: Production (the model, not me)** — The spec goes to my delivery stack. Writing the automation logic, generating the code, building the content, wiring the integrations, drafting the configs. This runs on AI, and the bulk of it runs on Kimi 2.6.

**Stage 3: QA (me, 15-20 minutes)** — The model produces, I review. Reviewing finished work is 10x faster than producing it.

**Stage 4: Handoff (mostly automated)** — Deploy, document, notify the client. Templated, scripted.

### Why Kimi 2.6 is the engine

Kimi 2.6 does the bulk of delivery work — the code, the automation logic, the content generation, the integration wiring — at roughly $0.50 per million input tokens and $2 per million output. For the kind of production work an agency runs all day, that's about 6x cheaper than defaulting to a Sonnet-class model and 20-30x cheaper than running everything on a frontier model like Opus or GPT-5.

And here's the part most people still haven't updated their mental model on: the shipped quality on this kind of work is indistinguishable. The automations Kimi 2.6 produces pass the same tests, ship to the same clients, and hold up in production exactly like output from a model costing 6x more.

But cost is only half of why it's the engine. The other half is throughput. I run delivery for 14 clients. On a heavy day that's dozens of production jobs firing in parallel. If I were running that volume on a frontier model, I'd hit rate limits by mid-morning. Moonshot's rate limits are dramatically more generous, which means I can run my entire client load concurrently without getting throttled into a queue.

Think about what that replaces. The production work Kimi 2.6 does for me is the work I would otherwise be paying 3-5 junior and mid-level people to do. That's $25-30k/month in salary, plus the management overhead, plus the mistakes, plus the churn. I replaced all of it with a model that costs me a couple hundred dollars a month and never has a bad week.

## 4. The Model Stack & Routing (Your "Team Roster")

I don't actually run everything on one model. The right way to think about your stack is as a team roster:

- **The senior workhorse: Kimi 2.6 (90% of delivery)** — Every routine production task defaults here: building flows, generating code, writing client content, wiring integrations, debugging, refactoring. ~$0.50/$2 per million.

- **The specialist: premium tier, Opus 4.6 or GPT-5 (the 10% that compounds)** — Some decisions are too expensive to get wrong. Architecting a complex multi-system integration for an anchor client. A security-sensitive review before something touches a client's production data. A genuinely novel problem I haven't solved before. For that 10%, I route to a premium model and happily pay 20-30x more per token, because the cost of a wrong answer here is a blown client relationship, not a $0.04 retry.

- **The intern: cheap/local tier (cleanup)** — Formatting, simple renames, boilerplate, first-draft scaffolding, trivial single-step tasks. Runs on a cheap utility model or a local model on my own machine for $0.

### Routing Logic (Org Chart)

```
# default everything to Kimi 2.6, escalate only when it actually matters
default: kimi-2.6

routes:
  production:     # coding, content, automations, debugging
    model: kimi-2.6
  high_stakes:    # architecture, security, genuinely novel problems
    model: claude-opus-4-6
  cleanup:        # lint, format, boilerplate
    model: local-qwen
```

### Cost per real client task

| Task Type | Kimi 2.6 | Premium Model (e.g., Opus) | Savings |
|-----------|----------|---------------------------|---------|
| Build a support agent automation | ~$0.40 | ~$2.40 | 6× |
| Generate a month of content (30 posts) | ~$1.50 | ~$9.00 | 6× |
| Debug and fix a production issue | ~$0.60 | ~$3.60 | 6× |
| Full agentic workflow (100+ steps) | ~$3-5 | ~$20-150 | 20-30× |

## 5. The Unit Economics (Why You Keep 90% of Every Check)

Revenue: $40,000
Costs:
- Kimi 2.6 inference (the bulk of all delivery): ~$240
- Premium model for the 10% of high-stakes work: ~$110
- Cleanup/local tier: ~$0
- Infrastructure (hosting, automation platform, vector DB, servers): ~$180
- Tools/SaaS (CRM, scheduling, comms, misc): ~$220
Total monthly opex: roughly $750

I deliver $40,000 of client value on about $750 of cost. My delivery inference, the thing that replaced a 5-person team, is under $300 of that. That's a margin north of 90%.

If I ran that exact same delivery load on a frontier model instead of Kimi 2.6, the production work that costs me ~$240/month on Kimi 2.6 would run roughly 6x higher on a Sonnet-class default, and 20-30x higher on Opus or GPT-5 for the heavy agentic loops. Call it $1,500-$5,000+/month depending on the mix.

## 6. Client Acquisition Without a Sales Team

- **Inbound from content** (biggest channel) — Post about the work. Case studies, before/afters, automation breakdowns. When you show real outcomes publicly, the right clients self-select.
- **A niche offer that sells itself** — "I build AI support agents for X type of business, here's exactly what it does, here's what it costs, here's the result."
- **Referral loops baked into delivery** — Every happy client knows other business owners with the same problem.
- **Lightweight outbound** — A targeted list, a sharp personalized message, a specific offer. Keep this small and surgical.

## 7. Staying Solo at Scale (Systems, Not People)

**Graduated skills: solve once, reuse forever** — Every workflow I solve, I save. The first time I build a client support agent, it's real work: spec it, build it, QA it, deploy it. But I capture that entire process as a reusable skill. My 5th support-agent build costs me a fraction of the time and tokens of my 1st.

**Background agents running delivery 24/7** — Monitoring, content generation, data processing, routine maintenance flows run as background agents on Kimi 2.6, continuously, while I sleep. Running persistent 24/7 agents is only economically sane because the per-token cost is so low.

**Agent Swarm (Moonshot): when one agent isn't enough** — Kimi 2.6 ships with Moonshot's Agent Swarm. Instead of one agent grinding through every step of a job in sequence, the main agent splits the work into smaller pieces and runs up to 300 sub-agents in parallel, coordinated across 4,000 steps. The main agent picks its own workers on the fly — Moonshot calls it an AI-designed org chart instead of a human-designed one.

What that looks like in practice:
- A monthly content batch stops being "wait while Kimi writes 30 posts one by one." The main agent fans out, 15-20 sub-agents draft in parallel, another batch QAs them against the brand voice, a final one packages the output.
- A complex integration build splits into "spec the auth layer," "wire the webhook," "write the tests," "draft the docs," all running at once.
- For monitoring work, sub-agents can sit on different parts of a client's system at the same time.

Moonshot has shown internal Swarm runs going for hours, and in one case 5 straight days, handling incident response autonomously. And the cost story still holds: a 300-agent Swarm sounds expensive until you remember each sub-agent is running on Kimi 2.6 economics. A run that would cost triple-digit dollars orchestrated on a frontier model often comes in under $5.

## 8. When to Actually Spend More (The Honest Limits)

- **Some work needs the premium tier** — For the 10% of work that's high-stakes. Rule: if the cost of a wrong answer is more than 100x the model cost difference, use the expensive model.
- **Some work needs a human** — Deep client strategy, delicate relationship moments, creative direction calls, true one-offs that don't fit any system.
- **There's a real ceiling on QA capacity** — Right now 14 clients is comfortable. Somewhere north of that, I'd either raise prices and cap client count, or bring in one trusted person purely for QA.

## 9. The 90-Day Plan to Your First $10k MRR

**Phase 1 (Days 1-30): Nail the offer and land client #1** — Pick ONE productized service in a niche you understand. Build the offer's core delivery once. Get your first client (discount if needed for case study + testimonial).

**Phase 2 (Days 31-60): Build the delivery engine** — Set up model stack with Kimi 2.6 as default workhorse. Route high-stakes to premium, trivial to cheap/local. Capture first workflow as reusable skill. Add 2-3 more clients using case study from phase 1.

**Phase 3 (Days 61-90): Systemize and compound** — Every new client, capture the work as a skill. Move ongoing work to background agents running on Kimi 2.6. Start content/referral flywheel for inbound. Tighten QA into fast, repeatable checklist.

## Minimal Routing Setup (to Start)

```yaml
# default everything to Kimi 2.6, escalate only when it actually matters
default: kimi-2.6

routes:
  production:     # coding, content, automations, debugging
    model: kimi-2.6
  high_stakes:    # architecture, security, genuinely novel problems
    model: claude-opus-4-6
  cleanup:        # lint, format, boilerplate
    model: local-qwen
```

The bigger picture: When the production layer of your business can run on Kimi 2.6 for a couple hundred dollars a month instead of a team that costs thirty thousand, headcount stops being leverage and becomes a liability.
