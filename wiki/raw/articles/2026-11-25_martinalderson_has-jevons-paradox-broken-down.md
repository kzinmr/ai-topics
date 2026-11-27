---
title: "Has Jevons paradox broken down?"
source: https://martinalderson.com/posts/has-jevons-paradox-broken-down/
author: Martin Alderson
published: 2026-11-25
type: raw-article
content: full
fetched: 2026-11-27
---

On a recent YC podcast , Ramp's CEO Eric Glyman claimed that "over the last two months, Jevons paradox broke". Ramp is a corporate card and spend management company, so they see what tens of thousands of businesses actually spend on tokens - and growth in that spend went from 42% in July to 1.5% across August and September combined . Jevons paradox is the idea that making something cheaper makes people use so much more of it that total spend goes up . 
 Ramp's data certainly isn't the full story. It's inherently noisy, skews towards venture-backed tech companies, and won't capture spend that never touches Ramp - e.g. big contracts paid directly by bank transfer, or tokens bought through a cloud provider. 
 I've been thinking a lot about this recently, noticing that my token consumption has at best plateaued recently. I think there's a few core drivers for that, plus some organisational issues I'm noticing. 
 Why my own usage has stalled 
 Perhaps I'm in the minority, but I'm finding myself running out of stuff to actually build, at least on a personal level. I've built prototypes of a decade of random ideas I've had, most of them not quite as good in the flesh as I thought they'd be. 
 On a more professional level, there's plenty to build... but I'm very cognisant of "featureitis" [1] . I (still) believe saying no to features is a really key competitive advantage. 
 The final point I'd make is that I'm pretty exhausted from the increased pace of development. I used to have weeks to mull product and technical strategy while implementation was underway. In many cases this is now down to hours. 
 One strategy I've found that works quite well is capping myself at one hour a day of kicking off "new" stuff, and spending the rest of the day reviewing what comes back. That hour generates more than enough to fill the day - which means it's my attention, not the models, limiting how many tokens I get through. 
 Simon Willison spoke about this when coding agents started getting good, and I feel like the adrenaline of the excitement is wearing off. I've seen a lot of people I know get pretty ill from working themselves too hard, and I think we really need to focus on burnout prevention for people managing product and engineering decisions. 
 Everything feels disposable 
 In parallel to this, given the models have got so good recently, I find myself treating all software as pretty disposable mentally. It turns out the grind of getting something working and the related dopamine hit had a lot to do with staying motivated on ideas. 
 When you see models do weeks or months of hard software engineering work in minutes or hours, it's absolutely magical the first few times. But increasingly I've thrown models at previously impossibly ambitious projects [2] and it all seems so easy I find myself thinking everything is disposable in my head, which is a shame because there is still an awful lot to be said for the refinement and iteration phase after the initial prototyping. 
 But at least for personal itches I want to scratch, without that initial grind it's hard for me to stay focused on "finishing" a project. I'm sure those who have a similar inherent urge to build stuff can look at a graveyard of projects in their GitHub account. 
 The four steps of AI adoption 
 Tinkerers like me are in the vast minority of the overall population. But according to Ramp, the top 1% of spenders are 80% of all token spend - so if the heavy users are hitting limits, that shows up in the numbers. So it is interesting to hypothesise about how far people can go with this kind of stuff, because I think it sets some overall limits on token consumption per person. 
 To step back, I think there are 4 clear steps of AI adoption. 

 1. LLM chat. Occasional chatting with LLMs. Most , but certainly not all (yes, some organisations still do not have even basic LLM chat rolled out!) businesses are at around this stage. This is usually very token light - a few thousand tokens, with a few turns per conversation. Call it 50K tokens a day per person. 
 2. Ad hoc agents. A sizeable minority - but not a majority in my estimation - of organisations are moving towards agentic workflows (e.g. Claude Cowork). Software engineering tends to be far ahead of this, with most organisations adopting Claude Code et al, but outside of SWE adoption is still really lagging, often roadblocked on access control. An agent re-reads its whole context on every tool call, so even one session a day is around 3M tokens - my median Claude Code session is 2.6M. 
 3. Engineered agents. Defined autonomous agents executing long running, repeatable business processes, triggered manually. In software engineering this is becoming increasingly common, with many developers building systems that allow them to take a task and execute it with little to no handholding. Outside of SWE, this is vanishingly rare. I've only really seen startups do it. You can quickly get to 100s of millions of tokens a day. 
 4. Autonomous agents. The "end state" of sorts, which is agentic processes running autonomously in the business, spawning themselves and spawning other workflows (often recursively). You could think of this as a "software factory". What I'm more interested in though is this applied to non-SWE tasks, with entire business departments being able to be operated with a fleet of agents. This isn't really per person any more, but could easily be billions of tokens a day. 
 Therefore, I still think we have at least 4 orders of magnitude of token consumption to grow into. 
 So I don't think Jevons paradox has broken. Cheaper tokens get you more usage within a step, but moving up a step is an organisational problem, not a pricing one. 
 The intersection is what matters 
 But, given token prices are falling rapidly, and even faster per unit of intelligence, the real question seems to be does organisational change - and thus agentic system adoption and token consumption - outpace the decline in token costs? Glyman himself reckons the majority of spend on frontier models could be done by a simpler one. 

 It's still hard to say, but seeing how slowly, and let's be honest; badly, most organisations have adopted AI, it does make me question things. On the other side I do think there is enormous value to be created for agentic first startups to start tackling boring business processes, which may actually lead to this explosion of token consumption. 
 Also, there may be a limit to how efficient models can get, and therefore how far prices can fall. It's hard to say, but there's no doubt that video compression had staggering efficiency improvements in the late 90s, but quickly hit diminishing returns. I suspect that is the case with LLMs, but I've no idea if we are at the MPEG1 stage or H.264 stage. 
 I'd love to hear from you if you are having roadblocks (or not) implementing agentic workflows outside of SWE. I'm working on a piece on best practices for navigating this, and I'll treat all submissions strictly on background and confidential. 

 A highly technical term for post AI products which have built thousands of features, turning the product into an absolute mess ↩︎ 

 For example, rewriting the entire ClickHouse query analyser and dispatch process to work on Vulkan - I don't know any shader code whatsoever - delivering orders of magnitude improvements in query speeds, or reverse engineering the Excel COM interface to work on Linux natively - when I haven't touched the Win32 API in decades, never mind reimplementing parts of it on Linux. ↩︎ 

 If you found this useful, I send a newsletter every month with all my posts. No spam and no ads. 

 Subscribe 

 Get the newsletter 
 Monthly updates, no spam 

 Related 

 The Coming AI Compute Crunch 

 How the AI boom might really end: 5 scenarios 

 How I think about reducing AI costs
