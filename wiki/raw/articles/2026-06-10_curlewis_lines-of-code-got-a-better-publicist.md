---
type: article
title: "Lines of Code Got a Better Publicist"
source: curlewis.co.nz
date: 2026-06-10
url: https://curlewis.co.nz/posts/lines-of-code-got-a-better-publicist/
author: David Curlewis
x_referrer: @badlogicgames
---

Lines of Code Got a Better Publicist

10 June 2026

·

8 min read

·

#ai

,

#leadership

,

#productivity

It’s fifteen years ago (bear with me, I’ve been in this industry since the late 90s, most of my good stories start this way), and you’ve got two senior developers at a SaaS company. One of them writes 40% more lines of code than the other. Is that developer better? More impactful for the business? Should the other one be polishing their CV?

Of course not. You’d want to know what actuallyshipped. What it did for customers, for revenue, for reliability. Lines of code, PR counts… we spent a couple of decades learning these are stereotypically bad ways to measure a developer, to the point where suggesting them today is laughable.

Of course not. You’d want to know what actually

shipped

. What it did for customers, for revenue, for reliability. Lines of code, PR counts… we spent a couple of decades learning these are stereotypically bad ways to measure a developer, to the point where suggesting them today is laughable.

Sooooo… Here’s what the industry put on the billboard this year:

Google:75% of new code is AI-generated.

Google:

75% of new code is AI-generated

.

Anthropic:~80% of merged production code is written by Claude, and engineers ship “8x more code per quarter”.

Anthropic:

~80% of merged production code is written by Claude

, and engineers ship “8x more code per quarter”.

OpenAI:also ~80%, apparently.

OpenAI:

also ~80%

, apparently.

Cursor:“100M+ lines of enterprise code written per day”.

Cursor:

“100M+ lines of enterprise code written per day”

.

Every single one is a volume claim. “Percent of code written by AI” is just lines of code with a better publicist. (The sceptic in me editing this draft would like to point out that it’s no coincidence that all of these are AI vendors of some kind, so pumping adoption isprettyimportant to them.)

Every single one is a volume claim. “Percent of code written by AI” is just lines of code with a better publicist. (The sceptic in me editing this draft would like to point out that it’s no coincidence that all of these are AI vendors of some kind, so pumping adoption is

pretty

important to them.)

We used to claim outcomes

Rewind a few years and the headline number was different in kind, not just size. GitHub’s flagship claim was that developers completed tasks55% fasterwith Copilot. Say what you like about that study (plenty did), but it was anoutcomeclaim. Bold, falsifiable, about value. If it was wrong, you could show it was wrong.

Rewind a few years and the headline number was different in kind, not just size. GitHub’s flagship claim was that developers completed tasks

55% faster

with Copilot. Say what you like about that study (plenty did), but it was an

outcome

claim. Bold, falsifiable, about value. If it was wrong, you could show it was wrong.

The 2026 claims can’t fail. That’s the genius of them; “75% of our code is AI-written” could be true, and will keep going up, regardless of whether anything got better (faster delivery, fewer incidents, happier customers, etc). A volume number can only ever disappoint you if adoption stalls, and adoption is the one thing most of us agree is real. 📈

So the claims got bigger and started saying less. What happened in between?

The bit nobody puts on a billboard

The outcome evidence got complicated, that’s what happened.

The strongest pro-adoption result is stillCui et al.; nearly 5,000 developers, +26% completed tasks, with the biggest gains for junior devs. Not really in dispute. But thenGitClearshowed code churn rising and refactoring collapsing as Copilot adoption deepened. ThenMETRran the study many have quoted: experienced open-source devs were 19%slowerwith AI in their own codebases, while believing they were 20% faster.

The strongest pro-adoption result is still

Cui et al.

; nearly 5,000 developers, +26% completed tasks, with the biggest gains for junior devs. Not really in dispute. But then

GitClear

showed code churn rising and refactoring collapsing as Copilot adoption deepened. Then

METR

ran the study many have quoted: experienced open-source devs were 19%

slower

with AI in their own codebases, while believing they were 20% faster.

But! Hold my beer… inFebruary 2026 METR effectively walked it back: their follow-up estimates flipped to aspeedup(with error bars wide enough to ride a Moto Guzzi, with panniers, through!), and they abandoned the study design entirely - because developers now refuse to workwithoutAI, and can’t reliably self-report time on agentic work. Their latest position: AI probably speeds developers up in 2026, and we can no longer cleanly measure by how much.

But! Hold my beer… in

February 2026 METR effectively walked it back

: their follow-up estimates flipped to a

speedup

(with error bars wide enough to ride a Moto Guzzi, with panniers, through!), and they abandoned the study design entirely - because developers now refuse to work

without

AI, and can’t reliably self-report time on agentic work. Their latest position: AI probably speeds developers up in 2026, and we can no longer cleanly measure by how much.

Meanwhile at the company level, anNBER survey of ~6,000 executivesfound 69% of firms actively using AI and roughly nine in ten reporting no measurable productivity impact. The cross-study consensus sits somewhere around 10% organisational gains. Not nothing! Still bloody useful! Buuuut, also not “you don’t need developers anymore” territory.

Meanwhile at the company level, an

NBER survey of ~6,000 executives

found 69% of firms actively using AI and roughly nine in ten reporting no measurable productivity impact. The cross-study consensus sits somewhere around 10% organisational gains. Not nothing! Still bloody useful! Buuuut, also not “you don’t need developers anymore” territory.

And if you’re a sceptic still quoting “19% slower”, you’re cherry-picking too. The research keeps updating; the industry just changed what it counts.

Vanity metrics, now in AI flavour

It’s not just AI vendor claims, to be fair. Carnegie Mellon’s SEI and Accenture launched anAI Adoption Maturity Modeljust a few days ago: five levels, eight dimensions, marketed off a stat about 95% of organisations seeing no returns. Steve Yegge’s“8 levels of AI-assisted development”ranks you by which tools you run and how much supervision you give them. And every tools vendor now ships a maturity ladder whose top rung is, usually, “use more of our product”. These ladders measure adoption intensity and call it maturity. Same substitution, nicer packaging.

It’s not just AI vendor claims, to be fair. Carnegie Mellon’s SEI and Accenture launched an

AI Adoption Maturity Model

just a few days ago: five levels, eight dimensions, marketed off a stat about 95% of organisations seeing no returns. Steve Yegge’s

“8 levels of AI-assisted development”

ranks you by which tools you run and how much supervision you give them. And every tools vendor now ships a maturity ladder whose top rung is, usually, “use more of our product”. These ladders measure adoption intensity and call it maturity. Same substitution, nicer packaging.

My favourite data point in this whole genre: Augment surveyed 219 engineering leaders and asked them todefine “AI-native engineering”. They got 219 different answers. 🫠

My favourite data point in this whole genre: Augment surveyed 219 engineering leaders and asked them to

define “AI-native engineering”

. They got 219 different answers. 🫠

And the prize for holding both ends of the rope goes to Anthropic, who gave us the “8x more code shipped” claimandone of the more rigorous studies of the year:an RCT finding that AI-assisted developers scored 17% lower on comprehensionof the code they’d just shipped, with no statistically significant productivity gain. I use Claude every single day (it recommended half the links I read for this post, so the irony is not lost on me), the products are genuinely excellent, and their research arm updates while their marketing arm counts volume. Both things are true at once, which is kinda the point.

And the prize for holding both ends of the rope goes to Anthropic, who gave us the “8x more code shipped” claim

and

one of the more rigorous studies of the year:

an RCT finding that AI-assisted developers scored 17% lower on comprehension

of the code they’d just shipped, with no statistically significant productivity gain. I use Claude every single day (it recommended half the links I read for this post, so the irony is not lost on me), the products are genuinely excellent, and their research arm updates while their marketing arm counts volume. Both things are true at once, which is kinda the point.

Why I actually care

Because these numbers aren’t decorative. They move budgets, performance expectations, and headcount plans. In February, Jack Dorsey cutover 40% of Block’s workforce(4,000+ people) with AI as the explicit core thesis: “A significantly smaller team, using the tools we’re building, can do more and do it better.” A couple weeks later, Atlassiancut 10% (~1,600 people), while conceding it would be “disingenuous to pretend AI doesn’t change the mix of skills we need or the number of roles required”. And there’s a key detail that gets me: Dorsey said, in the same announcement, that the business was strong and gross profit was growing.

Because these numbers aren’t decorative. They move budgets, performance expectations, and headcount plans. In February, Jack Dorsey cut

over 40% of Block’s workforce

(4,000+ people) with AI as the explicit core thesis: “A significantly smaller team, using the tools we’re building, can do more and do it better.” A couple weeks later, Atlassian

cut 10% (~1,600 people)

, while conceding it would be “disingenuous to pretend AI doesn’t change the mix of skills we need or the number of roles required”. And there’s a key detail that gets me: Dorsey said, in the same announcement, that the business was strong and gross profit was growing.

When a company says “AI made everyone more productive, so we need fewer people”, I want to see the evidence - and I don’t believe it exists today. Show me that x% of your workforce is genuinely idle (or even just underutilised) because the work can now be done by fewer people. Even then: I’ve never seen a product/SaaS company that didn’t have an endless roadmap. If you got a free headcount increase essentially overnight, why wouldn’t you use it to deliver more value to your customers, faster? That should show up as MAU, conversion, revenue. Choosing the layoff instead tells me the productivity claim is doing PR work for a decision that was already made for other reasons (over-hiring, investor pressure, take your pick).

Look, every business carries some fat, and I can accept efficiency-driven trimming as a thing that sometimes legitimately happens - it has at every step change in this industry. But when it happens, try to do so using the individual performance systems you already run, the ones that surface who’s cruising and who’s disengaged. Not token counts. Not “% of code AI-written” or somebody’s level on a maturity ladder. If your selection evidence is a vanity metric, your selection is a lottery wearing lipstick.

Where I land

As I’ve said inprevious posts, don’t read any of this as anti-AI. I think every engineershouldbe using AI daily. Call it AI-first, AI-proficient, whatever you like. Be curious, try the new tools, test the latest models. To not do so is silly. I’ve watched this industry absorb higher-level languages, IDEs, autocomplete, agile and devops, and there were always crusty hold-outs reminiscing about the good old days before X came along and ruined everything. The hold-outs eventually got on board (usually). The difference this time is pace: you could delay adopting “the cloud” for a couple of years and survive. With AI you might get a few months. The way we work has already changed, and it’s not changing back as far as I can tell.

As I’ve said in

previous posts

, don’t read any of this as anti-AI. I think every engineer

should

be using AI daily. Call it AI-first, AI-proficient, whatever you like. Be curious, try the new tools, test the latest models. To not do so is silly. I’ve watched this industry absorb higher-level languages, IDEs, autocomplete, agile and devops, and there were always crusty hold-outs reminiscing about the good old days before X came along and ruined everything. The hold-outs eventually got on board (usually). The difference this time is pace: you could delay adopting “the cloud” for a couple of years and survive. With AI you might get a few months. The way we work has already changed, and it’s not changing back as far as I can tell.

But adoption is thestarting line, not the scoreboard. We already know how to measure whether engineering is delivering: DORA metrics, reliability, rate of meaningful change, and ultimately revenue and customer value. Battle-tested, crusty stuff. Why are we throwing all of that out for bullshit AI vanity scores? (I could be wrong about plenty in this post, but I don’t think I’m wrong about that one.)

But adoption is the

starting line

, not the scoreboard. We already know how to measure whether engineering is delivering: DORA metrics, reliability, rate of meaningful change, and ultimately revenue and customer value. Battle-tested, crusty stuff. Why are we throwing all of that out for bullshit AI vanity scores? (I could be wrong about plenty in this post, but I don’t think I’m wrong about that one.)

So here’s the question to smuggle into your next vendor pitch, exec review, or LinkedIn doom-scroll:is that an outcome, or a volume?It’s amazing how quickly a position or statement deflates when you ask that.

So here’s the question to smuggle into your next vendor pitch, exec review, or LinkedIn doom-scroll:

is that an outcome, or a volume?

It’s amazing how quickly a position or statement deflates when you ask that.

The change is here to stay and the tools are good. The hopeful part is that we already know how to measure what matters (and none of it is counted in tokens).

Be AI-first in how you work, but battle-tested in how you measure it.

Cheers,Dave

Cheers,

Dave

← Older

Is coordinating a fleet of AI agents the same as managing a team of people? Yes, but mostly no.

Related Posts

Calibrating on Capability, Not Activity— 7 May 2026

Calibrating on Capability, Not Activity

— 7 May 2026

My AI Context System: The Sequel— 13 March 2026

My AI Context System: The Sequel

— 13 March 2026

Here's My AI Context System— 16 February 2026

Here's My AI Context System

— 16 February 2026