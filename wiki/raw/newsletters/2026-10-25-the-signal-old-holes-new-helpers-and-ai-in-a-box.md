---
title: "The Signal: Old Holes, New Helpers, and AI in a Box"
date: 2026-10-25
source: "The Signal (Alex Banks), publication_id=293154 post_id=221818469"
author: "Alex Banks"
url: https://thesignal.substack.com/p/old-holes-new-helpers-and-ai-in-a
fetched_via: curl + <article> paragraph extraction (Substack HTML, isAccessibleForFree: true)
tags: [newsletter, raw]
---

# The Signal: Old Holes, New Helpers, and AI in a Box

- **Source:** The Signal (Alex Banks), publication_id=293154 post_id=221818469
- **Author:** Alex Banks
- **URL:** https://thesignal.substack.com/p/old-holes-new-helpers-and-ai-in-a
- **Date:** 2026-10-25

---

Alex Banks 
 Oct 25, 2026 

 9

 Share

 Article voiceover
 0:00

 -12:47

 Audio playback is not supported on your browser. Please upgrade. Hey friends 👋 Happy Sunday.

Here’s your weekly dose of AI and insight.

This week AI dug up two 14-year-old holes in the code that runs most of the web, and I spent Wednesday in Berlin with Nebius at NVIDIA’s GTC.

If you’re enjoying this kind of analysis and want to support my work, become a paid subscriber today . You’ll get access to the full archive of The Signal, access to our Slack community of professionals, and 6 months free of Wispr Flow, my most-used AI tool, so that you can dictate instead of type. If you’re a paid subscriber, reply to this email for access.

Today’s Signal is brought to you by Attio .

Your CRM wasn’t built for your agents. Attio was. 

 Your team of people and agents need the controls of business software at the scale of infrastructure. Attio gives them both:

Every agent bound by your team’s permissions

Explore the new architecture of software here .

Rasmus Lerdorf, creator of PHP / William Stadtwald Demchick via Wikimedia Commons (CC BY-SA 4.0) / The Signal Newsletter 
 PHP 1. PHP’s Fourteen-Year Itch

Researchers using AI found two critical holes in PHP, the language behind most websites , and the flaws had been there since 2012.

The bugs: The two flaws ( CVE-2026-109618 and CVE-2026-109619 ) let an attacker run their own code on a server running PHP. Both score 9.2 out of 10 for severity, and the root cause dates back to PHP 5.4.

Who found them: Calif ’s team spotted the flaw on 1 August with help from AI, and reported a working attack on 11 August. OpenAI and Wiz found the same flaws on their own. OpenAI says it led the group that prepared fixes before the news went public.

The race: The PHP Foundation shipped fixes on 21 October, a day early, after the bug IDs leaked. The NSA told anyone who couldn’t update to take systems offline, and Amazon reportedly saw attack attempts before the news broke.

Alex’s take: This bug sat inside PHP for 14 years. With help from AI, Calif’s team went from spotting it to a working attack in ten days. The fix then took another 71 days to ship, and the news still ended up leaking a day early.

AI has made finding holes fast and cheap, and the same models are equally available to attackers and defenders alike. Even so, about a third of PHP sites still run versions 5 or 7, which got no official fixed release, only source patches for some versions.

OpenAI calls this period the “ Defender’s Window ”. I’d call it a lucky head start that only counts if you use it. If you run a website, email whoever hosts it this week and ask whether PHP has been updated.

Anthropic launched a personal agent that speaks up before you ask, and published two pieces of research that show where its models can be trusted today.

Claude Duet: A research preview of an always-on agent that works in the background across your connected apps and comes to you with what needs doing. It’s on a waitlist for Pro and Max users in the US, at no extra cost.

Scorpion binders: Claude designed proteins to latch onto scorpion toxins, and 17 of the 211 tested in a lab stuck. Nobody has tested whether they neutralise the venom yet.

Formal verification: With the startup Theorem, Claude helped prove mathematically that 123 software libraries can’t crash, rather than just testing them and hoping. The work turned up hundreds of bugs.

Alex’s take: Most of us still talk to AI by typing into a box. Duet is Anthropic’s answer to Meta’s Muse and OpenAI’s Dots: an assistant that comes to you. However, for now Duet is US-only , so I can’t try it from the UK, and Meta’s Muse is still limited to the US and Canada too. It’s a familiar headache over here, because I often find the most interesting AI tools land in America first and the rest of us wait, reading other people’s reviews instead of forming our own view. Needless to say, I can’t wait to get my hands on it, as Hark has been my go-to agent/assistant of choice for admin work since its release.

At GTC Berlin, NVIDIA showed AI data centres that arrive in shipping containers, and Nebius opened up its GPU prices for anyone to see.

Factories in a box: NVIDIA’s DSX POD ships Vera Rubin AI factories pre-built and tested inside containers. NVIDIA says setting one up at a prepared site takes as little as 14 days instead of about six months. NVIDIA aims to start deliveries in early 2027.

Agents on a leash: OpenShell is NVIDIA’s blueprint for running AI agents safely at scale. NVIDIA says a separate chip can spot an agent breaking its rules and stop it within milliseconds. Anthropic and Nebius are among the companies working with it.

Prices in public: Nebius now publishes its live spot prices (the going rate for renting spare GPUs right now) and added $10M in compute grants for European builders. A day later it signed a $3.5B loan facility with Citi to build data centres and buy GPUs.

Alex’s take: I was in Berlin with Nebius on Wednesday, and the number I keep coming back to is 14. NVIDIA says a DSX POD can be running in as little as 14 days, against about six months today. The hard infrastructure work happens in a factory before the container even ships. The catch is that the clock only starts at a “prepared site” with the power and cooling already in place. That fixes one bottleneck, but in Europe the other is getting power to the site, and nobody can ship that in a box yet.

Nebius putting its prices in public also caught my eye. Renting top GPUs has usually worked like booking a hotel before comparison sites existed. You’d ask for a quote and hope it’s fair. A public price tells a five-person startup whether compute is scarce or plentiful this week.

Gavin Baker, managing partner and CIO of Atreides Management / The a16z Show via YouTube 
 The investor who couldn’t find a bear case

Gavin Baker, who runs the investment firm Atreides Management, spent the summer asking AI leaders one question: “Can you tell me one quantitative data point in your business that’s getting worse? Just one.” He told David George on The a16z Show that nobody had given him one.

The episode came out at the end of August, but a clip a16z posted this month sent me back to the full 75 minutes, and I think the best part is the supply-and-demand economics. On demand, George said AI-native companies in a16z’s portfolio now spend around 10% of their payroll on AI, while old-economy firms that are doing it well spend about 1%. He also reckons fewer than 10 million people are heavy AI users today, out of roughly 1.5 billion knowledge workers. As he put it, “we’re nowhere on the demand side.”

On supply, Baker is more worried about building too little than too much. He says it’s rare to find companies that can invest hundreds of billions and earn it back within a year, and most of today’s spending still comes from companies’ own cash rather than debt. His own firm’s AI use rose 100-fold between March and August. If supply can’t keep up, he expects AI to get more expensive and warns of “compute inequality”, where big companies and wealthy people can afford it and everyone else can’t.

What stuck with me is the gap between 10% and 1%. If spending a tenth of payroll on AI becomes normal, today’s data centres are nowhere near enough, and that’s before most knowledge workers have even started.

Right now, I find myself paying for a Claude Max subscription with 20x usage every single month. I do this because I want access to the best intelligence that is currently available to sit across the knowledge work tasks that I currently do. This makes sense to me, but it most definitely differs from someone in a different role who may only need access to smaller models with fewer add-ons. The useful exercise is to work out how much of your own work AI could take on, and match spend accordingly.

Chamath Palihapitiya, Social Capital founder and All-In co-host / Christopher Michel via Wikimedia Commons (CC BY-SA 4.0) 
 Chamath on the one number that could break the AI build-out

On All-In last week, Chamath Palihapitiya called debt the AI boom’s Achilles heel . If the 10-year US Treasury yield climbs to 5.5-6%, he said, any business that makes its money on a financing spread will get hurt, whatever it does. In his words, “You’re going to be roadkill.” The 10-year closed at 5.13% on Wednesday , so his scenario isn’t far off.

Dario Perkins, an economist at TS Lombard, expects the borrowing to grow fast. He estimates AI companies could sell about $700 billion of new bonds in 2027, according to CNBC . The debt is already spreading beyond America, too. In August, the European Central Bank noted that US tech giants now make up almost 10% of new euro bonds sold by non-financial companies. This means if those US companies struggle to repay, investors in Europe will feel it as well.

Floating-rate loans: The interest is a short-term benchmark rate plus a fixed margin, so the bill rises every time the US central bank raises rates.

New fixed-rate borrowing: Lenders price it off the 10-year Treasury yield, the rate the US government pays, so when the 10-year rises, every new loan costs more.

The credit spread: This is the extra interest lenders charge a riskier company on top of that. It widens when they get nervous about one company, even if Treasury yields don’t move, and the worst case is both rising at once.

CoreWeave, which rents out AI chips, shows how this can feed on itself. It sells computing power on long, fixed-price contracts, then borrows to buy the chips. As borrowing gets more expensive, its margin shrinks, so lenders charge it more again. The yield on one of its bonds hit a record 15.76% on Thursday, and the cost of insuring its debt against default has almost tripled this year.

Now I still think the demand is real, as we discussed above in Content I Enjoyed. The risk sits in how the build-out is paid for, and the giants that fund most of it from their own cash are far safer than smaller companies living on borrowed money. If you want two numbers to watch, they’re the 10-year Treasury yield and the spread lenders charge AI companies. Worry starts when both climb together.

On Monday, Aleksander Madry, the MIT professor who used to lead OpenAI’s Preparedness team, said he’s going back to OpenAI to work on safety with chief scientist Jakub Pachocki:

“But we’ve since entered a different regime of AI progress. One in which getting the safety and security challenges of increasingly capable AI right has to become a central priority.”

Aleksander Madry @ aleks_madry 
 
 Personal update: Turns out that what I thought was leaving OpenAI became more of a sabbatical.

When I left a few months ago, I felt that the most important thing to focus on was making AI more useful to people. But we’ve since entered a different regime of AI progress. One in…
 5:16 PM · Oct 19, 2026 · 1.44M Views 
 
 162 Replies · 123 Reposts · 3.56K Likes 

 Sam Altman replied that “the safety and security challenges in front of us as we confront superintelligence are immense”. The same week, The Information reported that Altman had laid out three possible “endgames” for AI to staff. He reportedly favoured an international body modelled on the nuclear watchdog, the IAEA.

Madry was moved off the Preparedness team in 2024, and he left OpenAI earlier this year. The timing isn’t a coincidence either as we explored above, with this week AI helped find critical holes in PHP, the code behind most websites, so safety is now a security problem companies face today. Hiring one respected researcher is cheap, though. The real test is whether OpenAI gives the work enough computing power and the authority to actually delay a launch.

“Should AI companies owe the public a share, the way Norway’s oil fund does?”

Last Sunday, Anthropic committed 5% of its shares to a new Public Benefit Fund, subject to shareholder approval. At its last funding round that 5% would be worth about $48 billion (my estimate). Anthropic says AI “could also cause instability for many workers”, and that “bolder approaches may be needed”. It hasn’t said who will run the fund.

Elon Musk posted the next morning : “Next year, I will give one of my SpaceX shares to every kid in America. This will be the first of many.” He had already told Anthropic to give the shares “directly to the public”.

The tension arises over who ends up holding the money. Norway’s oil fund is worth about NOK 22.7 trillion , roughly NOK 4 million per Norwegian, but nobody gets a cheque, because the state invests it on everyone’s behalf. Anthropic’s version keeps the shares in a fund it set up, though it says the fund could also pay people directly. Musk wants them in people’s hands, although he hasn’t said how that would work.

I lean towards putting shares in people’s hands, because ownership is what buys people into capitalism. I find the people most sceptical of it are often the ones who don’t own anything that compounds in value over time. A share changes that, since it’s a stake you can hold, sell or pass on as you choose. It’s all about having the freedom to own and the opportunity to participate in free markets.

Would you rather own a share yourself, or have a fund invest it on your behalf? And should AI companies decide who gets a slice, or should governments?

Loading...

 Already a subscriber? Get your whole team on board. Signal Pro group subscriptions give everyone access to weekly AI analysis. Share this with your manager today.

Loading...

 💡 If you enjoyed this issue, share it with a friend.

P.S. Someone raced Cognition CEO Scott Wu against five AI models at a maths card game.
