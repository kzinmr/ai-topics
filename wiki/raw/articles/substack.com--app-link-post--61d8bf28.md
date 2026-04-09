---
title: "Marc Andreessen introspects on The Death of the Browser, Pi + OpenClaw, and Why "This Time Is Different""
url: "https://substack.com/app-link/post?publication_id=1084089&post_id=193082940&utm_source=podcast-email&play_audio=true&r=2flx6&utm_campaign=email-play-on-substack&token=eyJ1c2VyX2lkIjo0MDg3NDgyLCJwb3N0X2lkIjoxOTMwODI5NDAsImlhdCI6MTc3NTIzNTQ4NSwiZXhwIjoxNzc3ODI3NDg1LCJpc3MiOiJwdWItMTA4NDA4OSIsInN1YiI6InBvc3QtcmVhY3Rpb24ifQ.9TxIIy0b-XlVZDxDSRYTgQHDvKWB0dfyRYqNIIUwAjw&utm_source=substack&utm_medium=email&utm_content=play_card#play"
fetched_at: 2026-04-09T16:27:19.487780+00:00
source_date: 2026-04-10
tags: [newsletter, auto-ingested]
---

# Marc Andreessen introspects on The Death of the Browser, Pi + OpenClaw, and Why "This Time Is Different"

Source: https://substack.com/app-link/post?publication_id=1084089&post_id=193082940&utm_source=podcast-email&play_audio=true&r=2flx6&utm_campaign=email-play-on-substack&token=eyJ1c2VyX2lkIjo0MDg3NDgyLCJwb3N0X2lkIjoxOTMwODI5NDAsImlhdCI6MTc3NTIzNTQ4NSwiZXhwIjoxNzc3ODI3NDg1LCJpc3MiOiJwdWItMTA4NDA4OSIsInN1YiI6InBvc3QtcmVhY3Rpb24ifQ.9TxIIy0b-XlVZDxDSRYTgQHDvKWB0dfyRYqNIIUwAjw&utm_source=substack&utm_medium=email&utm_content=play_card#play

Fresh off
raising a monster $15B
,
Marc Andreessen
has lived through multiple computing platform shifts firsthand, from Mosaic and Netscape to cofounding A16z.
In this episode, Marc joins swyx and Alessio in a16z’s legendary Sand Hill Road office to argue that AI is not just another hype cycle, but the payoff of an “80-year overnight success”: from neural nets and expert systems to transformers, reasoning models, coding, agents, and recursive self-improvement. He lays out why he thinks this moment is different, why AI is finally escaping the old boom-bust pattern, and why the real bottleneck may be less about models than about the messy institutions, incentives, and social systems that struggle to absorb technological change.
This episode was a dream come true for us, and many thanks to
Erik Torenberg
for the assist in setting this up. Full
episode on YouTube
!
We discuss:
Marc’s long view on AI
: from the 1980s AI boom and expert systems to AlexNet, transformers, and why he sees today’s moment as the culmination of decades of compounding technical progress
Why “this time is different”
: the jump from LLMs to reasoning, coding, agents, and recursive self-improvement, and why Marc thinks these breakthroughs make AI real in a way prior cycles were not
AI winters vs. “80-year overnight success”
: why the field repeatedly swings between utopianism and doom, and why Marc thinks the underlying researchers were mostly right even when the timelines were wrong
Scaling laws, Moore’s Law, and what to build
: why he believes AI scaling laws will continue, why the outside world is messier than lab purists assume, and how startups can still create durable value on top of rapidly improving models
The dot-com crash and AI infrastructure risk
: Marc’s comparison between today’s AI capex boom and the fiber/data-center overbuild of 2000, plus why he thinks this cycle is different because the buyers are huge cash-rich incumbents and demand is already here
Why
old
NVIDIA chips may be getting more valuable
: the pace of software progress, chronic capacity shortages, and the idea that even current models are “sandbagged” by supply constraints
Open source, edge inference, and the chip bottleneck
: why Marc thinks local models, Apple Silicon, privacy, trust, and economics all point toward a major role for edge AI
American vs. Chinese open source AI
: DeepSeek as a “gift to the world,” why open models matter not just because they’re free but because they teach the world how things work, and how open source strategies may shift as the market consolidates
Why Pi and OpenClaw matter so much
: Marc’s claim that the combination of LLM + shell + filesystem + markdown + cron loop is one of the biggest software architecture breakthroughs in decades
Agents as the new “Unix”
: how agent state living in files allows portability across models and runtimes, and why self-modifying agents that can extend themselves may redefine what software even is
The future of coding and programming languages: why Marc thinks software becomes abundant, why bots may translate freely across languages, and why “programming language” itself may stop being a salient concept
Browsers, protocols, and human readability: lessons from Mosaic and the web, why text protocols and “view source” mattered, and how similar principles may shape AI-native systems
Real-world OpenClaw use
: health dashboards, sleep monitoring, smart homes, rewriting firmware on robot dogs, and why the most aggressive users are discovering both the power and danger of agents first
Proof of human vs. proof of bot
: why Marc thinks the internet’s bot problem is now unsolvable via detection alone, and why biometric + cryptographic proof of human becomes necessary
00:00 Marc on AI’s “80-Year Overnight Success”
00:01 A Quick Message From swyx
01:44 Inside a16z With Marc Andreessen
02:13 The Truth About a16z’s AI Pivot
03:29 Why This AI Boom Is Not Like 2016
06:33 Marc on AI Winters, Hype Cycles, and What’s Different Now
10:09 Reasoning, Coding, Agents, and the New AI Breakthroughs
12:13 What Founders Should Build as Models Keep Improving
16:33 AI Capex, GPU Shortages, and the Dot-Com Crash Analogy
24:54 Open Source AI, Edge Inference, and Why It Matters
33:03 Why OpenClaw and PI Could Change Software Forever
41:37 Agents, the End of Interfaces, and Software for Bots
46:47 Do Programming Languages Even Have a Future?
54:19 AI Agents Need Money: Payments, Crypto, and Stablecoins
56:59 Proof of Human, Internet Bots, and the Drone Problem
01:06:12 AI, Management, and the Return of Founder-Led Companies
01:12:23 Why the Real Economy May Resist AI Longer Than Expected
01:15:53 Closing Thoughts
Marc
: Something about AI that causes the people in the field, I would say, to become both excessively utopian and excessively apocalyptic. Having said that, I think what’s actually happened is an enormous amount of technical progress that built up over time. And like for, for example, we now know that neural network is the correct architecture.
And I, I will tell you like there was a 60 year run where that was like a, you know, or even 70 years where that was controversial. And so, so the way I think about what’s happening is basically, I think, I think about basically the, the, the period we’re in right now is it’s, I call it 80 year overnight success, right?
Which is like, it’s an overnight success ‘cause it’s like bam, you know, chat GPT hits and then, and then oh one hits, and then, you know, open claw hits and like, you know, these are open, these are, these are like overnight, like radical, overnight transformative successes, but they’re drawing on an 80 year sort of wellspring backlog, you know, of, of, of, of ideas and thinking it’s not just that it’s all brand new, it’s that it’s an unlock of all of these decades of like very serious, hardcore research.
If I were 18, like this is a hundred, this is what I would be spending all of my time on. This is like such an incredible conceptual breakthrough.
swyx
: Before we get into today’s episode, I just have a small message for listeners. Thank you. We will not be able to bring you the ai, engineering, science, and entertainment contents that you so clearly want if you didn’t choose to also click in and tune into our content.
We’ve been approached by sponsors on an almost daily basis, but fortunately enough of you actually subscribed to us to keep all this sustainable without ads, and we wanna keep it that way. But I just have one favor to ask all of you. The single, most powerful, completely free thing you can do is to click that subscribe button.
It’s the only thing I’ll ever ask of you, and it means absolutely everything to me and my team that works so hard to bring the in space to you each and every week. If you do it, I promise you will never stop working to make the show even better. Now, let’s get into it.
Alessio
: Hey everyone, welcome to the Lidian Space Pockets. This is CIO, founder Kernel Labs, and I’m joined by s Swix, editor of Lidian Space.
swyx
: Hello. And we’re in a 16 Z with a, uh, mark G and welcome.
Marc
: Yes, yes. A and what, half of 16? Something like that. A one. Exactly,
swyx
: exactly. Uh, apparently this is the, the final few days in your, your current office.
You’re moving across the road.
Marc
: Uh, we’re, yeah. We have a, we have some, we have some projects underway, but yeah, this is actually, oh, this is the original. We’re in actually the original office. We’re in the, we’re in the, we’re, we’re in the whole thing.
swyx
: It’s beautiful. Yeah. Great.
Marc
: Thank you.
swyx
: So I have to come out, uh, this is a, you know, I wanted to pick a spicy start in October, 2022.
I just made friends with Roone and, uh, I wanted to give him something to sort of be spicy about. And I said, uh. Uh, it’ll never not be funny. The A 16 Z was constantly going. The future is where the smart people choose to spend their time and then going deep into crypto and not in ai. And that was in October 22nd, 2022.
And Ruen says there was an internal meeting in a 16 Z to reorient around Gen ai. Obviously you have, but was there a meeting? What, what was that?
Marc
: I mean, I don’t, look, I’ve been doing AI since the late eighties.
swyx
: Yeah.
Marc
: So I, I don’t know, like all that, as far as I’m concerned, this stuff is all Johnny cum lately.
Yeah. You, I mean, look, we’ve been doing ar entire existence. I mean, we’ve been doing AI machine learning deep, you know, deeply. We’ve been doing this stuff way from the beginning. Obviously a AI is just core to computer science. I, I, I actually view them as like quite, uh, quite continuous. Um, you know, Ben and I both have computer science degrees.
Um, you know, we, we both, Ben, Ben and I actually both are world enough to remember the actual AI boom in the 1980s. Yeah. There was like a, there was a big AI boom at the time. Um, and there was a, was names like expert systems. Um, and they of like lisp and lisp machines. Uh, I, I coded in lisp. I was coding a lisp in 1989.
When that was the, the language of the AI future. Um, yeah. So this is something that we’re like completely, you completely comfortable with. I’ve been doing the whole time and are very enthusiastic about
swyx
: is there a strong, like this time is different because, uh, my closest analog was 20 16 17. It was an AI boom.
Mm-hmm. And it petered out very, very quickly. Um, we, it just, it just in terms of investing
Marc
: sort of, sort of,
swyx
: yeah. Investment, investment excitement.
Marc
: Although that’s really when the, the, the Nvidia phenomenon really, it was, I would say it was in that period when it was very clear that at, at the time it, the vocabulary was more machine learning, but it, it was very clear at that time that machine learning was hitting some sort of takeoff point.
Alessio
: Yeah.
Marc
: Well, and as you guys, you guys have talked about this at length on, on your thing, but, you know, if you really track what happened, I think the real story is, it was, it was the Alex net, uh, basically breakthrough in like 2013. That was the, that was the real knee in the curve. Um, and then it was obviously the transformer breakthrough in 17.
Alessio
: Yeah.
Marc
: Um, and then everything that followed. But, but, you know, look, machine learning, you know, there were, you know, look, uh, I mean look, I’ve been working, you know, I’ve been working with, uh, one of my, you know, kind of projects working with Facebook since 2004. Um, and on the board since 2007, and of course, you know, they, they started using machine learning very early, um, and, you know, have used it basically, you know, for like 20 years for, you know, content, you know, feed optimization and advertising optimization.
And obviously many, you know, financial services. You know, many, many, many companies, many different sectors have been doing this. And so it’s like one of these things, it’s like, it’s not a, it’s not a single thing. Like it’s, it’s like, it’s like layers, right? Yeah. Um, and, and the layers arrive at different paces and, but they kind of build up.
swyx
: Yeah.
Marc
: Uh, they kind of build up over time and then, and then, yeah. And then look, in retrospect, it was 2017 was kind of the, you know, the key, the key point with the trans transformer and then. And then as you guys know, there was this really weird like four year period where it’s like the, the transformer existed and then it was just like,
swyx
: let’s go.
Yeah.
Marc
: Well, but, but it was just, but, but between 2020, but between 2017 and 2021, I mean, that was the era of which like companies like Google had internal chat Botts, but they weren’t letting anybody use them.
swyx
: Yeah.
Marc
: Right. And then, you know, and then OpenAI developed Chat GT or GPT two, and then they told everybody, this is way too dangerous to deploy.
Right. Yeah. You know, we can’t possibly let normal people, normal people use this thing. And then you, you guys, I’m sure remember AI Dungeon, um mm-hmm. So the o for, there was like a year where like the only way for a normal person to use GP T three was in, in AI dungeon.
Alessio
: Yeah.
Marc
: And so you, you, we would do this, you’d go in there and you’d pretend to play Dungeons and Dragons.
In reality, you’re just trying to talk to talk to GPT. And so there was this, you know, there was this long, you know, and I, you know, the big, big companies, you know, big companies are cautious and, you know, the big companies were cautious. It, it, by the way, it took open ai. You know, they, they, they talk about this, it took open AI time to actually adjust, you know, kind of re redirect their research
swyx
: path.
I, I think, uh, let say Rosewood, right? Uh, the, the dinner that founded OpenAI was right there.
Marc
: Right, right. But that, that dinner would’ve taken place in 20
swyx
: 18
Marc
: 19. The formation of OpenAI Uhhuh as late as 2018.
swyx
: Uh, uh, sorry. Uh, no, I’m, I’m, I’m, I’m wrong. Probably It should be 20. Yeah. They just celebrated a 10 year anniversary, so it it is 2025.
Yeah, so, so 2015?
Marc
: Yeah. 2015. Yeah. 2015. But then, uh, um, Alec Radford did G PT one in what, probably
swyx
: mm-hmm. 17, 18,
Marc
: yeah. 17, 18. So it, yeah. For, and then, and then they didn’t really, and then GPT three was what? 2020? 2020.
swyx
: 2020.
Marc
: Because that became copilot immediately. Even open ai, which has been, you know, the leader of, of this thing in the last decade, you know, e even they had to adapt and, and, and lean into the new thing.
And so. Um, yeah, I, I think it’s just this process of basically sort of wave after wave layer after layer, you know, building on itself. And then you kind of get these catalytic moments where, where the whole thing pops and, and obviously that’s what’s happening now.
swyx
: Is it useful to think about will there be any ai, winter?
‘cause there’s always these patterns. Like, is this, in the summer is something I constantly think about because do I get, do I just like. Just get endlessly hyped and just trust that I will only be early and never wrong or right. Well, are we, will there be a winter?
Marc
: So there’s something about, say the following.
There’s something about AI that has led to this repeated pattern. Um, and, and, and you guys know this,
swyx
: it’s summer, winter, summer,
Marc
: winter, summer, winter, summer, winter. And it goes back 80 years. Yeah. 80 years. Uh, so the original neural network paper was 1943. Right. Which is, which is amazing. Uh, that it was, it was far back that long.
And then there was you, if you guys have ever talked about this on your show, but there was this, uh, there was a big, uh, there was an a GI conference at Dartmouth University in 1950. 55. 55, yeah. And they got a NSF grant to, uh, for the, all the AI experts at the time to spend the summer together. And they figured if they had 10 weeks together, they could get a GI, uh, at the other end.
And they got their, by the way, they got the grant, they got the 10 weeks and then, you know, 1955, you know. No, no. A GI. And like I said, I, I lived through the eighties version of this where there was a big, a big boom and a crash. And so, so there is this thing, and there, there is something about AI that causes the people in the field, I would say, to become both excessively utopian and excessively apocalyptic.
Um, and, and it’s probably on both sides of like the, the, the boom bus cycle. You, you kind of see that play out. Having said that, I think what’s actually happened is like just, and you know, and we now know in retrospect like an enormous amount of technical progress that built up over time. And like for, for example, we now know that neural network is the correct architecture.
And I, I will tell you like there was a 60 year run where that was like a, you know, or even 70 years or that was controversial. And, and we now know that that’s the case. And so we, we now, you know, everything we’re building on today just sort of derives from the original idea in 1943. And so, so in retrospect, we, we now know that like, these, these guys are right.
They, they, you know, they would get the timing wrong and they thought, you know, capabilities would arrive faster, or they were, it could be turned into businesses sooner or whatever, but like, they were fundamentally, the, the scientists who worked on this over the course of decades were fundamentally correct about what they were doing.
And, and the, and the payoff from, from, from all their work is happening now. And so, so the way I think about what’s happening is basically, I think, I think about basically the, the, the period we’re in right now is it’s, I call it 80 year overnight success, right? Which is like, it’s an overnight success.
‘cause it’s like bam, you know, chat, GPT hits and then, and then oh one hits, and then, you know, open claw hits and like, you know, these are open, these are, these are like overnight, like radical, overnight transformative successes, but they’re drawing on an 80 year sort of wellspring backlog, you know, of, of, of, of ideas and thinking it’s not just that it’s all brand new, it’s that it’s an unlock of all of these decades of like very serious, hardcore research.
Um, and thinking, and look, there were AI researchers who spent their entire lives. They got their PhD. They, they worked for, they’ve researched for 40 years. They retired in a lot of cases, they passed away and they never actually saw it work.
swyx
: Yeah. It’s all sad.
Marc
: It is. It is sad. It’s sad. Knew
swyx
: Jeff Hinton was like the last guy.
Marc
: Yeah. Yeah. Well, there were the guys, uh, was a guy, Alan Newell. I mean, there’s tons of John McCarthy. You know, John McCarthy was like one of the inventors in the field. He’s one of the guys who organized the Dartmouth Conference and you know, he taught at Stanford for 40 years. Wow. And passed, you know, passed away, I don’t know, whatever, 10, 10 years ago or something.
Never, never actually go. Got to see it happen. But like, it is amazing in retrospect, like, these guys were incredibly smart and they worked really hard and they were correct. So anyway, so then it’s like, okay, you know, say history doesn’t repeat, but it rhymes. It’s like, okay, does that mean that there’s gonna be another, like, you know, basically boom buzz cycle.
And I, I will tell you, like, let, like in a sense, like yes, everything goes through cycles and, you know, people get overly enthusiastic and overly depressed and there’s, there’s a time, there’s a timelessness to that. Having said that, there’s just no question. Um, so the form, the foremost dangerous words in investing this time are, this time is different.
Do you know the 12 most dangerous words investing? No. The four most d foremost dangerous words in investing are this time is different. Yeah. Um, the 12 most dangerous words. And so like, I’ll tell you what’s different. Like now it’s working like, like there’s just no, I mean, look, there’s just no question.
And by the way, I, I’ll just give you guys my take. Like L LLMs, like from, from basically the Chad G PT moment through to spring of 25. I think you could still, I think well intention, well, and of. Form skeptics could still say, oh, this is just pattern completion. And oh, these things don’t really understand what they’re doing.
And you know, the hall hallucination rates are way too high. And, you know, this is gonna be great for creative writing and creating, you know, Shakespeare and so sonnets and, you know, as, as rap lyrics or whatever, like, it’s gonna be great and all that stuff, but we’re not gonna be able to harness this to make this relevant in, you know, coding or in medicine or in law or in, you know, you know, kind of feels that, you know, kind of really, really matter.
And I think basically it was the reasoning breakthrough. It, it was oh one and then R one that basically answered that question basically said, oh no, we’re gonna be able to actually turn this into something that’s gonna work in the real world. And, and then obviously the coding breakthrough over the, over basically the coding breakthrough that kind of catalyzed over the holiday break was kind of the third step in that.
Mm-hmm. Where you’re just like, alright, if, if, you know, if Linus Tova is saying that the AI coding is no better than he is like. Like, that’s, that’s never happened before. That’s the
swyx
: benchmark.
Marc
: Yeah. That’s never happened before. And so now we know that it’s, it’s gonna sweep through coding and, and then, and then we, we know, you know, we know that if it’s gonna work in coding, it’s gonna work in everything else.
Right. It’s just then, because that’s, that’s like, that’s like, that’s like the hardest in many ways. That’s the hardest example. And how everything else is gonna be a, a derivative of that. And then on top of that, we just got the agent breakthrough, you know, with Open Claw, which is fantastic. Which is amazing and incredibly powerful.
And then we just got the, the, um, the auto research, uh, you know, the, the self-improvement. You know, we’re now into the self-improvement breakthrough. And so the, so the way I think about it is we’ve had four fundamental breakthroughs in functionality, l OMS reasoning, uh, agents, um, and then, uh, and, and then now RSI, um, and, and they’re all actually working.
Um, and so I’m, I’m just, as you like, you can tell I’m jumping outta my shoes. Like, like this is, like this is it like this, this is the culmination of 80 years worth of worth of work, and this is the time it’s becoming real.
Alessio
: Yeah.
Marc
: I, I’m completely convinced.
Alessio
: I think the anxiety that people feel is like during the transistor era, yet Mors law, and it’s like, all right, we understand why these things are getting better.
We understand the physics of it. Yeah. With ai, it’s. It’s so jagged in like the jumps where like, like you said, it’s like in three months you have like this huge jump like, and people are like, well this can keep happening. Right? But then it keeps happening,
Marc
: it’ll keep happening.
Alessio
: And so like how do you think about also timelines of like what’s we’re building?
I think we always have this question with guests, which is like, you know, should you spend time building harness for a model versus like the next model just gonna do it one shot in the lead space. Right. And how does that inform, like how you think about the shape of the technology? You know, you talk about how it’s a new computing platform.
If you have a computing platform, then like every six months it like drastically changes in what it looks like. It’s hard to build companies on top of it.
Marc
: Yeah. So, so a couple things. So one is like, look, the, the Moore’s law was what we now call a scaling law. Like Moore’s Law was a scaling law and for your younger viewers, more Moore’s Law was every chip chip chips either get twice as powerful or twice as cheap every, every 18 months.
And that, and that and that, you know, that it’s gotten more complicated in the last few years. But like that, that was like the 50 year trajectory of, of, of the computer industry. And then, and then by the way, and that’s what took the mainframe computer from a $25 million current dollar thing into, you know, the phone in your pocket being, you know, a million times more powerful than that.
Like that, you know, for, for 500 bucks. And so that, that was a scaling law. And then, and then, and then key to any scaling law, including Moore’s Law and the AI scaling laws is, you know, they’re not really laws, right? They’re, they’re, they’re, they’re predictions, but when they work, they become self-fulfilling predictions because they, they, they, they, they set a benchmark and, and then the entire industry, right?
All the smart people in the industry kind of work to make sure that, that, that actually happens. And so they, they kind of motivate the breakthroughs that are required to, to keep that going. And, and in and in chips, that was a 50 year, that was a 50 year run. Right. And it, it was amazing. And it’s still happening in, in some areas of, of chips.
I think the same thing is happening with the, the core scaling laws. The core scaling laws. In, in, in ai, you know, they’re, they’re not really laws, but like they, they are basically. There are predictions and then they’re motivating catalysts for the research work that is required to be. And, and, and, and by the way, also the investment, uh, dollars, um, uh, you know, required to basically keep, you know, keep the curves going and, and look, it, it is, it’s gonna be complicated and it’s gonna be variable and they’re, you know, there’re gonna be walls that are gonna look like they’re fast approaching, and then they’re gonna be, you know, engineers are gonna get to work and they’re gonna figure out a way to punch through the walls.
And obviously that’s, you know, that’s been happening a lot, you know, and then look, there’s gonna be times when it looks like the walls have, you know, the, the, the laws have petered out and then they’re gonna, they’re gonna pick up again and surge and then, and then, and then it, it appears what’s happening to the eyes is there’s not multiple, you know, multiple scaling laws.
Um, there’s multiple areas of improvement. And, and I think, you know, I don’t know how many more there are already yet to be discovered, but there are probably some more that we don’t know about yet. You know, they, like, for example, there’s probably some scaling law around, um, world models and robotics that we don’t fully understand, you know, kind of acquisition of data at scale in the real world that we don’t fully understand yet.
So that, that, that one will probably kick in at some point here. There’s a bunch of really smart people working on that. Um, and so, yeah, I, I think the expectation is that, that, you know, the, the scaling laws generally are gonna continue. Yeah. The, the pace of improvement will continue to move really fast.
Um. To your question on like what to build. So, uh, I’m a complete believer the scaling laws are gonna continue. I’m a complete believer the capabilities are gonna keep getting amazing, um, you know, leaps and bounds. Uh, the part where I kind of part ways a little bit with how, what I would describe as the AI purists, um, you know, which is, which I would characterize as like the people who are.
In many ways, the smartest people in the field, but also the people who spend their entire life, like at a lab, um, and have, have, I would say, have very little experience in the outside world. Um, the, the, the nuance I would offer is the outside world of 8 billion people and institutions and governments and companies and economic systems and social systems is really complicated.
Um, and, um, and doesn’t, you know, it it 8 billion people making collective decisions on planet Earth is not a simple process of like, just like you see this happening now. It’s like a bunch of AI CEOs have this thing, which is just like, well, there’s just this, they just all have this kind of thing when they talk in public where they’re just like, well, there’s these, these obvious set of things that so society to do.
Alessio
: Mm-hmm.
Marc
: And then they’re like, society’s not doing any of those things. Right. And it’s like, how can society not, you know, what, whatever their theory is, how can society not see x, y, Z? Mm-hmm. And the answer is, well, society is number one. There’s no single society, it’s like 8 billion people. And they like all have a voice, and they all have a vote, like at the end of the day of how they, they react to change.
And then, you know, it just like, it’s just human reality is just really complicated and messy. Um, and, and, and so the specific answer to your question is like, as usual, it depends. Um, you know, it, it depends. Look, pe there’s no question people are gonna, like, there’s no question they’re gonna be companies.
It’s already happening. There are companies that think that they’re building value on top of the models and then they’re just gonna get blissed by the, by the next model. There’s no question that’s happening. But I think there’s no question also that just the process of adaptation of any technology into the real and into the real messy world of humanity is, is just going to be messy and complicated.
It’s, it’s not going to be simple and straightforward. It’s gonna be messy and complicated. And there are gonna be a lot of companies and a lot of products, um, uh, and in, in fact entire industries that are gonna get built to, to, to basically actually help all of this technology actually reach real people.
Alessio
: The amount of capital going into these companies, I mean, Dario talked about it on the Door Cash podcast and Door Cash was like, why don’t you just buy 10 x more GPUs? And he is like, because I’m gonna go bankrupt if the model doesn’t exactly hit the, the performance level. How do you think about that?
Also as a risk on, you know, you guys are investors, open AI and thinking machines and world apps. It seems like we’re leveraging the scaling loss at a pretty high rate, right? Like how comfortable, I guess, do you feel with the downside scenario, like, and say like things Peter out, you think you can kind of like restructure uh, these build outs and uh, you know, capital investments.
Marc
: Yeah. So should start by saying, so I live through the.com crash, um, and I can tell you stories for hours about the.com crash and it was horrible. No, it was awful. It was, it was, it was apocalyptic by the way. The, a lot of the.com crash was actually at the time, it was actually a telecom crash. It was a bandwidth crash.
Like the, the thing that actually crashed, that wiped out all the money with the tele, the telecom companies.
swyx
: Global
Marc
: crossing. Global, global, yeah.
swyx
: I’m from Singapore and they, they laid so much cable o over over our oceans.
Marc
: Actually there was a scaling law in the.com. Era. And it was literally the, the US Commerce Department put out a report in 1996 and they said internet traffic was doubling every quarter.
Um, and, and actually in 1995 and 1996, internet traffic actually did double every quarter. And so that became the scaling law. And so what all these telecom entrepreneurs did was they went out and they raised money to build fiber, anticipating that the demand for bandwidth is gonna keep doubling every quarter.
Doubling every quarter though is like, you know, grains of chess and the chessboard, like at some point the numbers become extremely large. Right. And, and, and it really, and really what happened was the internet. The internet by the way, continuously kept growing basically since inception. And it’s, you know, it’s, it’s continuously grown.
It’s never shrunk. And it’s grown really fast compared to anything else. Mm-hmm. You know, in, in, in human history. But it wasn’t doubling every quarter as of 19 98, 19 99. And so there was this gap in the expectation of what they thought was a scaling law versus reality. And that’s actually what caused the.com crash, which was the, it they, they way over companies like global crossing way overbuilt fiber, which is sort of the, and by the way, fiber, telecom equipment, you know, so all the, all the networking gear, you know, and then, and then by the way, the actual physical data centers, like that was the beginning of the, of the, of the data center build and then, and the data center overbuild.
And so you had that, but it was, it was literally, I think it was like $2 trillion got wiped out, right? It was like Jesus, it was like a big, it was. And by the way, the other, the other subtlety in it was the internet companies themselves never really had any debt. ‘cause tech, tech companies generally don’t run on debt, but the telecom companies run on debt.
Physical infrastructure companies run on debt. And so the companies like Global Crossing not just raise a lot of equity, they also raise a lot of debt. So they’re highly levered. And so then you just do the thing. It’s just like, okay, you have a highly levered thing where you’re, you’re just over, you’re overbuilding capacity.
Demand is growing, but not as fast as you hoped. And then boom, bankrupt. Right. And, and then it, and then it’s like they say about the hotel industry, which is, it’s always the third owner of a hotel that makes money. It has to go bankrupt twice, right? You have to wash out all of the over optimistic exuberance before it gets to actually a stable state.
And then it makes money. So by the way, all of those data centers and all of those, all the fiber that they’re in use, it’s all in use today. Yeah. But 25 years later. But it, it, it took, and actually the elapsed time was, it took 15 years. It took 15 years from 2000 to 2015 to actually fill, fill up all that capacity.
The cautionary warning is the, the overbuild can happen. Um, and, and, and, and, you know, you, you get into this thing where basically everybody, everybody who basically has any sort of institutional capital, it’s like, wow. It’s just, I, I don’t know how to invest in these crazy software things. For sure I can put build data centers and for sure I can buy GPUs that I can deploy, you know, compute grids and, and all these things.
Um, and so, you know, if you’re a pessimist, you could look at this and you could say, wow, this is like really set up to be able to basically replicate, you know, what we went through, what we went through in 2000. Obviously that would be bad. The counter argument, which is the one I I agree with, which is the counter on, on the other side is a couple things.
One is the companies that are investing all the, the companies that are investing the money are like the bluest chip of companies. And so back, back, back in the, in the do, like Global Crossing was like a, it was like an entrepreneur. It was like a, a new venture, but like the money that’s being deployed now at scale is Microsoft, and, you know, and Amazon and Google, Facebook and Facebook and Nvidia and, you know, these, these, these, and, and now you know, by the way, open ai philanthropic, which are now at like, you know, really serious size, um, you know, as companies with, you know, very serious revenue.
These are very large scale companies with like, lots, lots of cash, lots of debt capacity that they’ve, they’ve never used. And so th this is institutional in a way that, that really wasn’t at the time. And then the other is, at least for now, every dollar that’s being put into anything that results in a running GPU is being turned into revenue right away.
Like so, and you guys know this, like everybody’s starved for capacity, everybody’s starved for compute capacity and then, you know, all the associated things, memory and, and, and interconnected and everything else. Um, data center space. And so e every dollar right now that’s being put into the ground is turning into revenue.
And, and it, and in fact, I actually think there’s an interesting thing happening, which is because everybody starve for capacity, the models that we actually have that we can use today are inferior versions of what we would have if not for the supply constraints. That’s true. Um, if Right pose a hypothetical universe in which GPUs were 10 times cheaper and 10 times more plentiful mm-hmm.
The models would be much better. ‘cause you would just allocate a lot more money to training and you’d just build better models and they would be better. Um, and so we’re, we’re actually getting the sandbag version of the technology.
swyx
: Yeah. No. Everything we use is quantized because the, the labs have to keep the, the full versions,
Marc
: right?
swyx
: Like
Marc
: we’re not even getting the good stuff.
swyx
: Yeah.
Marc
: But, but getting the good stuff, it’s, it’s just, even if technical progress stops. Once there’s like a much bigger build of like GPU manufacturing capacity and memory, you know, all, all the things that have to happen in the course of the next five or 10 years.
Once it happens, even the current technology is gonna get, gonna get much better. And then as you know, like there’s just like a million ways to use this stuff. Like there’s just like a million use cases for this. Mm-hmm. Like, it, it, you know, this isn’t just sending packets across a, a thing, whatever, and hoping that people find something to do with it.
This is just like, oh, we apply intelligence into every domain of human activity. And then it works like incredibly well. Yeah. Um. Here’s what I know, here’s what I know. Um, in the next three or four year, it’s like somewhere between three or four years out, basically everything is selling out. So like the, the entire supply chain is, is, is, is sold out or, or, or selling out.
And so there, there’s no, like, we’re just gonna have like chronic supply shortage for, you know, for years to come. Um, there’s going to be a response from the market that’s gonna result in an enormous, you know, it’s happening now. An enormous flood of investment in a new fab capacity and ev you know, every, everything else to be able to do that, at some point the supply chain constraints will unlock, you know, at least to some degree that will be another accelerant to industry growth when that happens.
‘cause the products will get better and everything will get cheaper. Um, and so, so I know that’s gonna happen. I know that, you know, the deployments, you know, the, the actual use cases are like really compelling. And then, like I said, you know, with reasoning and agents and so forth, like, I know they’re just gonna get like much, much better from here.
And so I, I, I know the capabilities are like really real and serious. I also know that the technical progress is not going to stop. It. It, it is excel. It is, is accelerating. Like the, the breakthroughs are are tremendous. I mean, even just month over month, the breakthroughs are really dramatic. And so, you know, I think if you were a cynic and there, there are cynics, you can look at 2000, you can find echoes.
But I can’t even imagine betting it that this is gonna like somehow disappoint and, you know, at least for years to come, I think it would be essentially suicidal to make that bet. Yeah. Um, it was that Michael Burry, uh, uh, that’s
swyx
: an
Marc
: interesting guy, huh? We’ll pick on a guy. We’ll pick, let’s pick on one guy.
We’ll pick. Well ‘cause he did, he he came out with, it was, it was the, he
swyx
: doesn’t mind.
Marc
: It was the Nvidia short. Right. He came with the Nvidia short. And then if you guys probably talked about this, which is the, the analysis now that like the current models are getting better faster at such a rate that if you are running an Nvidia, if you’re running an Nvidia inference chip today, that’s three years old, you’re making more money on it today than you did three years ago because the pace of improvement of the software is, is faster than the, the, the depreciation cycle, the chip.
And then my understanding is Google is running. I don’t if they’ve, I don’t know exactly what, uh, these are rumors that I’ve heard or maybe it’s public, but, um, I think Google’s running very old TPUs, very profitably. Ference. Yeah. And very profit and very profitably. Yeah. Um, and so, so it actually turns out, as far as I can tell, it’s actually the opposite of the Beery thesis is actually.
He was actually 180 degrees wrong. It’s actually the, the, the, the old Nvidia chips are getting more valuable, which is something that’s like literally never happened before. Like it’s never been the case that you have an older model chip that becomes more valuable, not less valuable. And that, and again, that’s an expression of the just ferocious pace of software progress.
Ferocious pace of capability payoff. Yeah. Uh, that you’re getting on the other side of this. And so I just, the idea of betting against that, like.
swyx
: Yeah. Yeah. Well, one of
Marc
: my, it seems like an invitation to get your face ripped up.
swyx
: One of my early hits was like modeling the lifespan of the H 100 and h two hundreds and, and going like, you know, usually they advise like four to seven years and it was, you know, maybe you sort of realistically haircut cut it down to two to three.
Yeah. But actually it’s going up and not down. Yeah. And, and uh, that’s, I mean that’s, I think that’s the dream. Uh, we are finding utilization and I think utilization solves all problems. Like, you can, you can find use, use cases for even like the poor, like even memory, we’re having a shortage. Right. And, and even like the, the shittier versions of, of memory that we do have, we are finding use cases for it.
So like That’s great.
Marc
: Yeah.
Alessio
: How, how important is open source AI and kinda like edge inference in a world in which you have three years of supply crunch. Like, do you think in the, like, you know, if you fast forward like five years, like how do you think about inference, uh, in the data center versus at the edge?
Marc
: Well, so just to start, yeah. So I think, I think open source is very important for a bunch of reasons. I think edge, edge inference is very important for a bunch of reasons. I, I think just practically speaking, if we’re just gonna have fundamental construc, supply crunches for the next, I mean, you, you guys know if you just project forward demand over the next three years, right?
Yeah. Relative to supply, one of the, its main predictions you can do is what’s gonna, what, what’s gonna happen to the cost of, of inference in the core, uh, over the next three years? And like, it may rise dramatically, right? Like, so, so what is, and then is, is, you know, like the, the, the big model competition are subsidizing heavily right now.
Right? Right. And so, so what’s the, what will be the average person’s, you know, per day, per month token cost, you know, three years from now to do all the things that they want to do. And I, I don’t know, it’s gonna. I mean, I have, you guys probably have friends, I have friends today who are paying a thousand dollars a day for open claw, for claw tokens to run open claw.
Right? And so, okay. $30,000 a month. Right? And, and by the way, those, those friends have like a thousand more ideas of the things that they want their claw to do, right? Yeah. And so you, you could imagine there, there’s like latent demand of up to, I don’t know, five or $10,000 a day of, of, of tokens for a fully deployed, you know, per personal agent.
Uh, and obviously consumers can’t pay that, right? And so, so, but it gives you a sense of the fu of the fu of the future scope of demand, right? And so, so even, even if there’s a 10 x improvement in price performance, that still, you know, goes to a hundred dollars a day, which is still way beyond what people can pay.
Mm-hmm. So there’s just gonna be like. Ferocious to me, by the way. The agent thing, the other interesting thing is I think the agent thing, so up until now, a lot of the constraints of GGPU constraints, I think the agent thing now also translates into CPU constraints. Mm-hmm. Right?
swyx
: CPU memory.
Marc
: Yes. CPU memory, right?
And so, like the entire chip ecosystem is just gonna get wait,
swyx
: wait for network constraints, that that will be the killer.
Marc
: It’s all bottleneck potentially for years. And so, so I, I think that Brad, and, and I think it’s actually possible, I mean, generally inference costs are gonna keep coming down, but I think the, let’s put it this way, the rate of decline, I think may level out here for a bit because of these supply constraints.
And then at some point, maybe the lab stops subsidizing so much and that, that, that again, will be, be an issue. And so there’s just gonna be so much more demand for inference than, than can be satisfied. Um, you know, kind of with the centralized model. And then, and then, you know, you guys know this, but like all the, just the dramatic, I mean just the dramatic innovations that have happened in the Apple silicon to be able to do, uh, inferences, it’s quite amazing the level of effort being put.
Like the open source guys are putting incredible effort into getting, you know, this recurring pattern where the big model will never run on a pc, and then six months later mm-hmm. Oh, it runs in a pc, right? It’s like amazing. And there’s very smart people working on that. So there’s all that. And then look, there’s also, you know.
There’s also like other, there’s other motivators. There’s other motivators which is just like, okay, how much trust are the big centralized model providers? You know, how much trust are they building in the market versus, you know, how much are, you know, at least for, in certain cases with some people, for certain use cases, people being like, well, I’m not willing to just like, turn everything over.
So there, there, there’s all the trust issues. Um, by the way, there’s also just like straight up price optimization. There’s many uses of AI where you don’t need Einstein in the cloud. You just need like a, a a, a smart local model. There’s also performance issues where you want, you know, you want, you know, you’re gonna want your doorknob to have an AI model in it.
Right. You know, to be able to, you know, do, um, you know, to be able to do access control. Um, obviously like everything with a chip is gonna have an AI model in it. Mm-hmm. And it, a lot of those are gonna be local. Um, and so, yeah. No, like I think, I think you’re gonna have ti and then you’re gonna, by the way, also wearable devices, you know, you don’t wanna do a complete round trip.
You want, you know, you, whatever your smart devices are, you want it to be like super low latency. Yeah.
swyx
: The question, do we care who makes it? Yeah. One of the biggest news this week was the collapse of AI two, the Allen Institute. Mm-hmm. One of the actual American open source model labs. Yeah. Um, and, uh, I’m not that optimistic on, on American open source.
Yeah. Like you, you guys invested in MIS trial and MIS trial’s doing extremely well outside of China. That’s about it.
Marc
: Yeah. We’ll see. We’ll see. I look, I, number one, I do think we care. Uh, I do think we, I do think we care who makes it. Um, I would say this, the, the, the, the previous presidential administration wanted to kill it in the us Oh yeah.
They wanted to drown in the bathtub. Um, and so they wanted to kill it. So at least we have a government now that actually like, actually wants it wants it to happen. And you
swyx
: earned to council
Marc
: and Yeah. And the new and the P pcast. Yeah. So the, the, you know, this admin for whatever other political issues people have, which are many, you know, this administration has, I think a very enlightened view and in particular an enlightened view on AI and in particular on open source ai.
Uh, and so they’re very supportive. Um, my read is the Chi. The Chinese have a very, the various Chinese companies have a very specific reason to do open source, which is, they, they, they don’t fundamentally, they don’t think they can sell commercial, uh, AI outside of China right now. And or at least specifically not, not in the US for a combination of reasons.
And so they, they kind of view, I think, open source AI as a bit of a loss leader against basically domestic, uh, you know, paid, paid services. And then kind of an, you know, kind of an ancillary products. You know, they’re, they’re very excited about it, by the way. I think it’s great. I think it’s great that they’re doing it.
Um, you know, I think Deeps seek was like a gift to the world. Um, I think. The great thing about open source, open source, the, the, the impact of open source is felt two ways. One is you, you get the software for free, but the other is you get to learn how it works, right? And so like the paper, the paper, the paper and, and the code, right?
And the code. And so, like, for example, I thought this was amazing. So open comes out with L one and it’s an amazing technical breakthrough, and it’s just like, absolutely fantastic. But of course they don’t explain how it works in detail. And then of course they hide the, they hide the reasoning traces, right?
And, and then, and then, and then everybody’s like, okay, this is great, but like, who’s gonna be able to replicate this? Are other people gonna be able to do this? You know, is their secret sauce in there? And then our one comes out and it’s just like, there’s the code and there’s the paper, and now the whole world knows how to do it.
And then, you know, three months later, every other AI model is, is adding reasoning. And so, so you get this kind of double, like even if the Chinese models themselves are not the models that get used, the education that’s taken place to the rest of the world, the information diffusion, you know, is incredibly powerful.
So that happens and then, I don’t know. We’ll, we’ll see. You know, there are a bunch of American, you know, open source, you know, ai, uh, model companies. I mean, look, there’s gonna be tremendous, you know, there already is. There’s, you know, there’s gonna be tre there’s tremendous competition, uh, among the primary model companies.
You know, there’s, depending on how you count, there’s like four or five, you know, big co model companies now that are, you know, kind of neck and neck, uh, in different ways. Um, uh, you know, and, and, and, um, you know, and then obviously Bo Bo both X and then MetAware involved are, you know, both have huge, you know, huge attempts to, you know, kind of, to kind of leapfrog underway.
And then you’ve got, you know, a whole fleet of startups, new companies, including a whole bunch that we’re backing, that are, you know, trying to come out with different approaches. And then you’ve got whatever it is. I don’t know how, how many, how many, like main line foundation model companies are there in China at this point?
It’s probably six. It’s
swyx
: five Tigers is what they call it. Yeah. Uh, Quinn is in questionable because there’s change in leadership,
Marc
: right?
swyx
: Yeah.
Marc
: But that, does that include, that includes like Moonshot,
swyx
: yes. Can deep seek, uh, uh, ZI, um, Quinn oh one is in there.
Marc
: Right. And then, um, and by dance and, and then you see,
swyx
: ance would be like the next tier ance.
They weren’t as prominent. They weren’t, didn’t have
Marc
: a leading. Yeah. But they, you at least, you know, ance is very inspiring and presumably they have more stuff coming and Tencent probably has more stuff coming and, and so forth. And so, so, so like, look, here, here would be a thing you can anticipate, which is there are not these markets, there are not going to be between the US and China right now, there’s like a dozen primary foundation model companies that are like at scale, at, at some level of a critical mass.
It’s not gonna be a dozen in three years, right? Like, it just because these industries don’t bear a dozen, it’s, it’s gonna be three or you know, there’s gonna be three or four big winners or maybe one or two big winners. And so there’s gonna be like a whole bunch of those guys that are gonna have to figure out alternate strategies.
Um, and I think like open source is one of those strategies. And so I, I think you could see like a whole, i, I, I think the questions like, who’s gonna do open source? I think that could change really fast. I, I think that, that, that’s a very dynamic thing. I think it’s very hard to predict what happens. And, and I think it’s very important.
swyx
: NVIDIA’s doing a lot.
Marc
: Well, I was gonna say. Well, exactly. And then you’re got Nvidia and then, and then, you know, just to, again, indu, there’s an old thing in business strategy, which is called, uh, commoditize Compliments. Commoditize the compliment. That’s right. And so if your Jensen is just kind of obvious, of course, you wanna commoditize the software.
Yeah. And he’s, and to his enormous credit, he’s putting enormous resources behind that. And so maybe it, maybe it’s literally Nvidia and I think that would be great.
Alessio
: Yeah. Uh, narrative violation to European projects, uh, in the, uh, damn.
swyx
: I’m hosting my, uh, Europe, uh, conference soon. And I got both of them.
Alessio
: They got us.
They got us. Mark
Marc
: finished. They got us, us. Well, wait a minute. Where was Peter? So where was Steinberger when he did? In Austria
Alessio
: was, yeah, yeah, yeah.
Marc
: He was in what? He was in Vienna. Oh, he was in Vienna. And then where is he now?
swyx
: Uh, he’s moving to sf.
Marc
: Okay. Okay. Alright. Okay, there we go. And then, yeah, the PI guy, right?
The PI guys are European.
swyx
: Yeah, they’re also, they’re buddies in
Alessio
: Australia. Mario’s also there. Yeah.
Marc
: Right. And are they, yeah, they haven’t announced yet. Any sort of change changed or have they
Alessio
: No, they’re, they have a company there.
Marc
: Okay. Got, okay. Good.
Alessio
: Good, good,
good.
Alessio
: Um,
Marc
: yeah, good.
swyx
: Anyways, I think pie and open cloud very important software things and, and I just wanted you to just go off on what you think.
Marc
: Yeah. So I think in co the, the combination of the two of them I think is one of the 10 most important softwares. Open
swyx
: Claw got all the attention, but Right. Talk about pie,
Marc
: pi pie’s, kind of the Yeah. PI’s, PI’s kind of the architectural breakthrough for those of us who are older. There was this whole thing that was very important in the world of software basically from like 1970 to, I don’t know, it still is very important, but like 19, from 1973 to like basically the creation of Linux, which is basically this, this thing used to call like the Unix mindset.
Like so, so, ‘cause there were all these different, you know, theories. There are all these different operating systems and mainframes and, and then you know, all these windows and Mac and all these things. And then there was this, but kind of behind it all was this idea of kind of the Unix mindset. And the Unix mindset was this thing where basically you don’t have these, like, like in the old days, like, like the operating system that like made the computer industry really work, like in the 1960s mm-hmm.
Was this thing called o os 360, which was this big operating system that IBM developed that was supposed to basically run everything. And it was this like giant monolithic architecture in the sky. It was like a, you know, it was like a giant castle. Um, of software. And, and by the way, it worked really well and they were very successful with it.
But like, it was this huge castle in the sky, but it was this thing, it was almost unapproachable, which is like, you had to be kind of inside IBM or very close to IBM. And you had to really understand every aspect, how the system worked. And then the, the Unix sky is originally out of at and t and then out out of Berkeley, um, you know, came out and they said, no, let’s have a completely different architecture.
And the way architecture’s gonna work is we’re gonna have, we’re gonna have a, a prompt and, and a, and a shell. And then, and then we’re gonna, all, all the functionality is gonna be in the form of these discreet modules, and then you’re gonna be able to chain the modules together. Mm-hmm. Yeah. And so like the, the, the op, it’s almost like the operating, operating system itself is gonna be a programming language.
Um, and then that led led to the, the, the sort of centrality of the shell. Um, and then that led to sort of, uh, you know, basically chaining together Unix tools. And then that led to the emergence of these, these scripting languages like Pearl, where you, you could basically kind of very easily do this, and then the shells got more sophisticated and then, and then, and then look like, you know, that, that, that number one, that worked and that, that was the world I grew up in.
Like I was, I was a Unix guy. You know, sort of from, call it 1988 to, you know, kind of all, all the way through my work and it worked really well. It, it’s in the background, um, you know, nor normal people don’t need to, didn’t need to necessarily know about it, but like, if you were doing like system architecture, application development, you, you, you knew all about it.
Um, and then, you know, it’s been in the background ever since. And, you know, look, your Mac still has a Unix shell, you know, kind of in there, and your iPhone still has a Unix shell kind of buried in there somewhere. So they’re kind of in there. And then, you know, the Windows shell is kind of a, you know, sort of a weird derivative of that.
But, um, you know, but look, the inter, the internet runs on Unix, um, and that smartphones, actually, both iOS and Android are Unix derivatives. And so, you know, kind of Unix did end up winning. But, but anyway, and then we just started taking that for granted. And then, and then so, so basically the, the way I think about what happened with Pie and then with Open Claw is basically what those guys figured out is, I always say the, the great breakthroughs are obvious in retrospect, right?
Which is the best kind, the best kind. They weren’t obvious at the time or somebody else would’ve done them already. Um, and so there is a, like a real conceptual leap, but then you look at it sort of the backwards looking and you’re just like, oh, of course. Mm-hmm. Like the, the, to me those are always the best breakthroughs.
Well, actually language models themselves are like that. It’s just like, oh, next token completion. Oh, of course.
swyx
: Yeah. What other objective mattered?
Marc
: Yeah, exactly. But, but like it, right. But she’s even saying it wasn’t obvious until somebody actually did it. Right. And so the conceptual breakthrough is real and deep and powerful and, and very important.
And so the way I think about pie and olaw is it’s basically marrying the, the language model mindset to the un to the Unix, basically shell prompt mindset. And so it’s, it’s basically this idea that what, what, so what is an agent, right? And as, as, and as you know, like many smart people who have been trying to figure out what an agent is for, for, for decades, and they’ve had many architectures to build agents and the whole thing.
And it turns out what is an agent. So it turns out what we now know is an agent is the following. It’s, so it’s a language model. And then above that, it’s a ba, it’s a bash shell. Um, so it’s a, it’s a Unix shell, and then it’s, and then the agent has access, uh, has access to, to the shell. And, you know, hopeful, hopefully in a sandbox, maybe in, maybe in a sandbox.
So it’s, it’s the model. Um, it’s the shell. Um, and then it’s a fi, it’s a file system. Um, and then the state is stored in files. And then, you know, there’s the markdown format for the, you know, for, for the files themselves. And then, and then there’s basically what in Unix is called Aron job. There’s a loop and then there’s a heartbeat for the, there’s heartbeat and, and the thing basically Wake Wakes up.
Wakes up. So it’s basically LLM plus shell, plus file system, plus markdown, plus kron. And it turns out that’s an agent. And, and, and every part of that, other than the model is something that we already completely know and understand. And in fact, it turns out that like the latent power of the Unix shell is like extraordinary because basically like all, like, there’s just like an, there’s just enormous latent power in the shell.
There’s enormous numbers of Unix commands, there’s enormous number of command line interfaces into all kinds of things already in the, you know, your entire, I mean your entire, just to start with, your computer runs on a shell. If you’re running a Mac or a, or, or a phone, your computer, your computer’s running on a shell, uh, already.
And so like the full power of your computer is available at the command line level. Um, and then it turns out it’s really easy to expose other functions as a command line interface. And so like this whole idea where we need like MCP and these like product mm-hmm. Fancy protocols, whatever, it’s like, no, we don’t, we just need like a command, command line thing.
So that’s the architecture. And then it turns out what is your agent? Your agent has a bunch of files starting a file system. And then there’s the thing that just like completely blew my mind when I write my head around it as a result of this, which is like, okay. This means your agent is now actually independent of the model that it’s running on.
Because you can actually swap out a different LLM underneath your agent and your, your agent will change personality somewhat. ‘cause the model is different, but all of the state stored in the files will be retained.
swyx
: Yeah. Different instruction set, but you just compiled
it.
Marc
: Right, exactly. And it’s all right.
It’s like right. Swapping out a ship and recompiling, but it’s, it’s still, it’s still your agent with all of its memories. Um, and with all of its capabilities. And then by the way, you can also swap out the shell, uh, so you can move it to a different execution environment that is also, is also a b shell, by the way, you can also switch out the file system, right.
Uh, and you can, and you can, and you can swap out the, the, the heartbeat for the, the crown framework, the, the loop that the agent framework itself. And so your agent basically is ba basically at the end of the day, it’s just. It’s just, its files. Um, and then, and then there’s of course it a open
swyx
: call.
Marc
: Yeah, it’s, it’s basically, it’s, it’s just the files.
Um, and then by the way, as a consequence of that, the agent and then the agent itself, it turns out a couple important things. So one is it, it’s, it, it can migrate itself, right? And so you’re, you can instruct your agent, migrate yourself to a different, uh, runtime environment, migrate yourself to a different file system, migrate yourself to a different, you know, swap out the language model.
Your agent will do all that stuff for you. And then there’s the final thing, which is just amazing, which is the agent is the agent actually has full introspection. It actually, it actually knows about its own files and it could rewrite its own files. Right. Which by the way, is basically no widely deployed software system in history where the, the, the thing that you’re using actually has full introspective knowledge of how it itself works and is able to modify itself.
Like that, that, I mean, there have been toy systems that have had that, but there, there’s never been a widely deployed system that has that capability and then that leads you to the capability. That just like completely blew my mind when I wrap my head around it, which is you can tell the agent to add new functions and features to itself and it can do that.
Extend yourself. Yeah. Right? Extend, extend yourself. Like extend yourself. Give yourself a new capability. Right? And so, and so literally it’s just like you run into somebody at a party and they’re like, oh, I have my open claw, do whatever, connect to my eat, sleep bed, and it gives me better advice and sleep.
And you go home at night and you tell your claw, or if they’re at the party, by the way, you tell your claw, oh, add this capability to yourself. And your claw will say, oh, okay, no problem. And it’ll go out on the internet and it’ll figure out whatever it needs and then it’ll go out to claw code or whatever.
It’ll write whatever it needs. And then the next thing you know, it has this new capability. And so you don’t even have to, like, you can have it upgrade itself without even having to, without having to do anything other than tell it that you want it to do that. And so anyway, so the, the combination of all this is just, I mean, this is just like a massive, incredible, I mean, it’s just incredible.
Like if I, if I were, if I were 18, like this is a hundred, this is what I would be spending all of my time on. This is like such an incredible conceptual breakthrough. Yeah. And again, pe people are gonna look at it and they already get this response. People are gonna look at it and they’re gonna say, oh, well, where’s the breakthrough?
‘cause these, the, all of these components were already known before. Mm-hmm. But, but this is the key, the key to the breakthrough was by using all these components that were known before, you get all of the underlying capability of that’s buried in there. And so all, and so for example, computer use all of a sudden just kind of falls, trivi, trivial.
Of course it’s gonna be able to use your computer. It has full access to the shell. Right. And then, and then you just, you, you give it access to a browser, and then you’ve got the computer and the browser and, and often away it goes. And, and then you’ve got all the abilities of the browser also. Um, yeah.
And so, and so the capability unlock here is profound. My friends who are, you know, deepest into this, are having their claw do like a, like, literally like a thousand things in their lives. They have new ideas every day. They’re just like constantly throwing new challenges at the thing. And by the way, it’s early and, you know, these are, you know, these are prototypes and there are, you know, as you guys know, there’s security issues.
Yeah. And, and so, you know, there’s a bunch of stuff to be ironed out, but the, the unlock of capability is just incredible.
swyx
: Yeah.
Marc
: And I, I have absolutely no doubt that everybody in the world is gonna, is gonna have at least, you know, an agent like this, if not an entire family of agents. And we’re gonna be living in a world where I think it’s almost inevitable now that this is the way people are gonna use computers.
swyx
: I was gonna say for someone who is deeply familiar with social networks, the next step is your claw talking to my Claw. Mm-hmm.
Marc
: Posting
swyx
: on Claw Facebook, uh, posting their jobs on cloud LinkedIn and close posting their tweets on claw XAI or what, whatever, you know. Um, I do think that that is how, uh, you know, we, we get into some danger there in, in terms of like alignment and whether or not we want these things to, to, to run.
Marc
: You guys know where Rent a, rent a human.com.
swyx
: Yeah. Rent a,
Marc
: yeah. Yeah.
swyx
: I mean, it’s Fiverr, it’s TaskRabbit.
Marc
: Sure, of course.
swyx
: Mechanical
Alessio
: Turk.
Marc
: Yeah. But flipped, right. The agent hiring the people.
Alessio
: Yeah.
Marc
: Which of course is gonna happen, right? It’s obviously gonna happen.
Alessio
: I’m curious if you have any thoughts on the engineering side.
So when you build the browser, the internet, you know, just a bunch of mostly plain text file plus some images, and today the, every website and app is like, so complex. Somehow, you know, the browser kept evolving to fit that in. Mm-hmm. Are there any design choices that were made like early in the browser and kinda like the internet and the protocols that you’re seeing agents similar to this?
Like, Hey, this thing is just not gonna work for like this type of new compute and we should just. Rip it out right now.
Marc
: There were a whole bunch, but I’ll give you a couple. So one is, um, and we didn’t, you know, to be clear like this, this was not, you know, this is totally different. We didn’t have the capabilities we have today, but because Wet have, we didn’t have the language models underneath this, but, um, we did have this idea that human readability actually mattered a great deal.
Um, and, and, and so, and specifically in those days, it was, it was not so much English language, but it was there, there was a design decision to be made between binary protocols and text protocols. And basically every, every, every basically old school systems architect that had grown up between like the 1960s and the 1990s basically said, you know, the internet, it’s, what do you know about the internet?
It’s star for bandwidth. You, you just, you have these very narrow straws. Uh, you know, look, people, when we did the work on Mosaic, like pe, people who had the internet at home had a 14 kilobit modem, right? So you’re, you’re trying to like hyper optimize every bit of data mm-hmm. That, that travels over the network.
And so obviously if you’re gonna design a protocol like HGTP, you’re gonna want it to be binary, you know, highly compressed, binary protocol for maximum efficiency. And you’re gonna wanna have it be like a single connection that persists. And you’re, you’re, the last thing you’re gonna wanna do is like, bring up and tear down new connections.
And you definitely, you’re not gonna, not gonna want a text protocol. And so of course we said no. We actually want to go completely the other direction. It’s obviously, we only want text protocols. Uh, by the way, same thing in H TM L itself. We want html to be relatively verbose. You know, we want the tags to actually be like human readable.
Um, we wanna use
swyx
: the most inefficient things possible.
Marc
: Yeah, we wanna do the, we wanna do the in, we wanna do the inefficient things.
swyx
: You’re the original token Mixer.
Marc
: Yeah, exactly. Yeah, yeah, yeah. Basically it’s just like better lesson
Alessio
: filled.
Marc
: Well, yeah. Well actually this was, this was actually the, the conscious thing, which basically says just like assume, assume a future of infinite, infinite bandwidth built for that, right?
And then basically what it was, is it was a bet that it, it was a bet that if the system, if the, if the latent capabilities of the system were powerful enough, and that was obvious enough to people that would create the demand for the bandwidth that would cause the supply of bandwidth to get built that would actually make the whole thing work.
And then specifically what we wanted was we wanted everything to be human readable because we, at the engineering level, we wanted people to be able to read the protocol coming over the wire and be able to understand it with their, with their bare eyes without having to like disassemble it or whatever.
Right. Have it converted outta binary. Right. And so the, the, the, all the pro, you know, HTTP and everything else were, were, it was always, uh, text protocols. Uh, and the same thing with HTML and in, in many ways, some people say that the key breakthrough in the browser was the view source option, um, which is every webpage you go to, you could view source, which means you could see how it worked, which means you could teach yourself how to build right new, uh, to, to build new webpages.
There was that. So human readability. Um, and, and again, human readability in those days still meant technical, you know, specs. You know, now it means English language, but there’s an incredible latent power in giving everybody who uses the system the option to be able to drop down and actually understand and see how it’s working.
And that worked really well for the web and I think it’s working really well for ai. That was one. Um, what was the other, um. A big part of the idea of web servers was to actually surface the underlying latent capability of the operating system and to be able to surface the, uh, also the underlying latent capability of the database because basically what was a web server?
What, what, what, what is a web server? Fundamentally? Architecturally, it’s, it’s, it’s the operating system. So it’s, it’s the operating system’s ability to, you know, it’s running on top of an os. So it’s the OSS ability to manage. The file system and do everything else that you wanna do, process everything. Um, and then of course, a lot of early, you know, a lot, a lot of websites are, are front ends to databases.
Um, and so you wanted to, you wanted to unleash the underlying latent power of whether it was an Oracle database or some other, you know, some other Postgres or whatever, whatever it was. Um, and so a lot of the function of the web server was to just bridge from that internet connection coming in to be able to unlock the underlying power of the OS and the database.
Uh, and again, people looked at it at the time and they were like, well, is this really, does this really matter? Like, is this important Because we’ve had databases forever and we’ve always had, you know, user interfaces for databases and this is just another user interface for a database. And it’s like, okay, yeah, fair enough.
But on the other side of that is just like, this is now a much better interface to databases and one that 8 billion people are going to use and is going to be like, far easier to use and far more flexible. And, and, and, and you’re not just gonna have old databases. Now you have a system where people can actually understand why they want to build, you know, a million times more database apps than they have in the past.
And then the number of databases in the world exploded. And so again, this goes to this thing of like building, building in layers. Some of the smartest people in the industry look at any new challenge and they’re like, okay, I’m, I’m, I need to build a new kind of application. So the first thing I need to do is build a new programming language, right?
And then the next thing I need to do is build a new operating system, right? And then the next thing I need to do is I need to build a new chip. Right? And they, they kind of wanna reinvent everything. And I’ve, I’ve always had, maybe it’s just, I don’t know, pg pragmatic mentality or something, or maybe an engineering over science mentality, but it’s more like, no, you have just like all of this latent power, uh, in the existing systems and you, you don’t want to be held back by their constraints, but what you wanna do is you wanna kinda liberate that power and open it up.
Yeah. And so I, I think, I think, and I think the web did that for those reasons. And I think it’s the same thing now that’s happening. It’s a great
swyx
: perspective on the web.
Alessio
: Programming language just is not a good thing. We have Brett Taylor on the podcasts and we were talking about rust. And you know, rust is memory safe by the phone.
So why are we teaching the model to not write memory, unsafe code, just use rust, and then you get it for free. How much do you think there’s like. Time to be spent like recreating some of these things instead of taking them for granted. I’ll be like, oh, okay. Python is kind of slow Python
swyx
: type scripts,
Alessio
: you know?
It’s like, yeah.
swyx
: As, as imperfect as they are, they are the lingua franca.
Marc
: I mean, I think this is gonna change a lot. ‘cause I don’t think the models care what language they program in. Mm-hmm. And I think they’re gonna be good at programming in every language, and I think they’re gonna be good at translating from any language to any other language.
Like, okay, so this gets into the coding side of things. I, I think we’re going through a really fundamental change. And then, look, I, I grew up hand, you know, I grew up hand code, you know? Yeah, yeah, yeah. I grew up hand coding. Everything I did was actually everything I did actually was written in CI wasn’t even
Alessio
: back in the days,
Marc
: I wasn’t even using c plus plus, so I, or like Java or any of this stuff.
Right. Uh, and so, um, I, everything, everything I ever did, I was like managing my own memory at, at, at the level of c and then I, you know, I, I’m still from the generation that, you know, I, I knew assembly language and, you know, I, I, you know, um, so I, I could drop down and do things, uh, right on the ship. And so we, we’ve just, we’ve all, all of us, we’ve always lived in a world in which software is like this precious thing that like, you have to think about very carefully.
And it’s like really hard to generate good software. And there’s only a small number of people who can do it. And like, you have to be very, like, jealous in terms of thinking about like, how do you allocate, like what are your engineers working on and how many good engineers do you actually have? And how much software can they write?
And how can, how much software can human beings, you know, kind of maintain? And I think like all those assumptions are being shot right out the window right now. Like, I think they’re, I, I think those days are just over. And I think the new world is like, actually high quality software is just like infinitely available.
Mm-hmm.
Marc
: And if you need new software to do X, Y, Z, like, you’re just gonna wave your hand and you’re gonna get it. And then if it’s, if you don’t like the languages written in, you just tell the thing, all right, I want the, now I want the rush version. Um, or, you know, se secure, you know, secure. We’re about to, by the way, we’re about to go through computer security is about to go through the most dramatic change ever, which is number one, like every single latent security bug is about to be exposed,
swyx
: right?
Marc
: So we’re gonna have like, the in, we’re, we’re, we’re set up here for like the computer security apocalypse for a while. But, but, but on the other side of it, now we have a coding agents that can go in and actually fix all the security bugs. And so how, how are you gonna secure a software in the future?
You’re gonna tell the, tell the bot to secure it, and it’s gonna go through and, and fix it all. And so, so this thing that was this incredibly scarce resource of high quality software is just going to become a completely fungible thing that you’re just gonna have as much as you want, right? Uh, and, and that has like, you know, that has like tons and tons of consequences in some sense.
The answer to the question that you posed, I, I think it’s just somewhat, I don’t know, simple or something, or straightforward, which is just, if you want all your software and rust, you just, all the bot, you want all your software and rust, like, things that used to be like hard or even like, seem like an insurmountable mountain to get to get through all of a sudden, I think, become very easy.
swyx
: I, I think Brett had a theory that there would be a more optimal language for lms. And so the contention is, uh, there isn’t like, just don’t bother, just whatever humans already use LMS are perfectly capable, porting.
Marc
: I think we’re pretty close to being, I don’t know if this would work today. I think we’re pretty close to being able to ask the AI what would its opt optimal language be and let Right, and let it design it.
True. Okay, here’s a question. Are you gonna even gonna have programming languages in the future? Um, or the ai, are the AI just gonna be emitting binaries? Let’s assume for a moment that humans aren’t coding anymore. Let’s assume it’s all bots. The bot. What levels of intermediate abstraction do the bots even need?
swyx
: Yeah.
Marc
: Or are they just coding binary directly? Did you see there’s actually an experi, somebody just did this thing where they have a, they have a, a language model now that actually emits model weights for a new language model. Right. And so will the bots be just
Alessio
: predict the weights
Marc
: Will, yeah. Will the bots literally be emitting not just coding binaries, but will they, will, will they actually be admitting weights for, for new models?
Yeah. Direct directly and. Conceptually, there’s no reason why they can’t do both of those things. Uh, like architecturally. Both of those things seem completely possible. It’s
swyx
: very inefficient. You’re basically very
Marc
: inefficient.
swyx
: A simulation of a simulation in a simulation inside of the weights. Correct?
Marc
: Yeah, yeah. Very inefficient. But like, look, LMS are already like incredibly inefficient. Ask an uh, in favor thing, ask Claude, add two plus two equals four. Right? It’s just like, you know, it’s like, you know, it’s, it’s, it’s like whatever, billions and billions of times more inefficient than using your pocket calculator.
swyx
: Yeah.
Marc
: But, but, but yet the, the, the payoff is so great of the general capability. And so anyway, like I, I kind of think in 10 years, like, I’m not sure. Yeah. Like, I’m not sure there will even be a salient concept of a programming language, um, in the way that we understand it today. And in fact, what we may be doing more and more is a form of interpretability, which is we’re trying to understand why the bots have decided to, uh, structure, uh, code in the way that they have.
swyx
: I mean, if you play it through, you don’t need browsers, then like, that’s the depth of the browser.
Marc
: Well, so I, I would take it a step further, which is you may not need to use your interfaces. So who is gonna use software in the future?
swyx
: Other bots.
Marc
: Other bots. Yeah. Yeah. And
swyx
: so you still need to, I don’t know, pipe information in,
Marc
: do we?
swyx
: And out
Marc
: really
swyx
: well, what are you gonna do then?
Marc
: Are you sure
swyx
: you’re just gonna log off and touch grass?
Marc
: Whatever you want. Exactly. Isn’t that better?
swyx
: I want software to do stuff for me.
Marc
: Isn’t that? But isn’t that better? I mean, look, I, you know, I don’t know. Look like, you know, you know, you, all the arguments here, you know, it was not that long ago that 99% of humanity was behind a plow.
swyx
: Right.
Marc
: Right. And what are people gonna do if they’re not plowing fields all day to, to, to grow food? Right. And it just turns out there’s like much better ways for people to spend time than plowing fields. Yeah.
swyx
: Dooms growing.
Marc
: Uh, yeah, exactly. Exactly. Or, you know, talking to their friends and look, and I’m not an absolutist and I’m not a utopian.
And I, and to be clear, like I’ve, I have an 11-year-old and he’s learning how to code and like I’m, you know, I, I think it’s still a really good idea to learn how to code and so forth, but I just, if you project forward, you just have to think forward to a world in which it’s just like, okay, I’m just gonna tell the thing what I need and it’s gonna do it, and then, and then it’s gonna do it in whatever way is most optimal for it to do it.
Mm-hmm. Yeah. Unless I tell it to do it non optimally. Like if I tell it to do it in Java or in Rust or whatever, it’ll do it, I’m sure. But like, if I’m just gonna tell it to do, it’s, gonna do it in whatever way is like the optimal way to do it. Yeah. And then I, and then if I need to understand how it works, I’m gonna ask it to explain to me how it works.
Right. And so it’s gonna be doing its own, interpret it, it’s gonna be the engine of interpretability to explain itself. And I, I just am not convinced that, that I’m not, I’m not convinced that in that world you have these historical, the goals of the abstractions will be whatever, the Boston network with the human Right.
Alessio
: Yeah. Yeah. That, well, I, I’m curious like. If that’s true, then shouldn’t the models providers be building some internal language representation that they can do extreme, kinda like rl uh, and reward modeling around, because it’s like, today they’re kind of like tied to like type script and Python because the users need to write in that language versus they can have their own thing internally and like they don’t need to teach it to anybody.
They just need to teach their model. And I think that’s how you get maybe the version between the models, like going back to like the pie open claw thing. It’s like, oh, I built all the software using the open AI model and now switch to the RO model. But the TRO model doesn’t understand the thing. So I I, it feels like there still needs to be some obstruction.
But maybe not. Maybe that’s the lockin that the model providers want to have. I don’t,
Marc
: I’m not even sure that’s lockin though. ‘cause why can’t the second model just learn what the first model has done? Like,
swyx
: exactly.
Marc
: Okay. So okay. Give you an example. So as you know, models can now reverse engineer software by, right?
Isn’t it the whole thing now where people are reverse engineering, like Nten, Nintendo, gay binaries. Yeah. So you, you have like there’s, I’ve seen a bunch of reports like this where somebody has like a favorite game from the 1980s and the source code is like long dead, but they have like a binary brand to do a chip or something, another reverse engineer to get a version that runs in their Mac.
Right. And so if you reverse it, if, this is why I kinda say if you’re reversing like X 86 binaries, then why can’t you reverse engineer
Alessio
: whatever the degree. Yeah. And because we’re all on a Unix based system, it has to be reversible because it needs to run on the target.
Marc
: Yeah, yeah, yeah, yeah, yeah. Basically.
And so I just, I just think it’s this thing where it’s just like, and by the way, and everything we’re describing is something that human beings in theory could have done before, but just with like, right. Yeah, yeah. But with enormous where, but it was just always like cost and labor prohibitive. Reverse engineer.
I learned how to reverse engineer. Human beings can reverse engineer binaries. Yeah. It’s just for any complex binary, you need like a thousand years mm-hmm. To do it. But now with a model, you don’t. And so all of a sudden you get, you get these things. Or, or another way to think about it is so much of human built systems are to compensate for the human limitations.
swyx
: Mm-hmm.
Marc
: Yep. Right? Um, and if you don’t have the human limitations anymore, then all of a sudden you have, and, and it’s not that you, you won’t have abstractions, but you’ll have a different kind of abstraction. Yep. Yep.
swyx
: I have two topics to bring us to a close. And, uh, you could pick whichever ones. Uh, just talking about protocols, was it you or someone else?
Uh, I forget my internet history. Who said that? Like the biggest mistake that we didn’t figure out in the early days was payments. Yes. Was that you?
Marc
: Yes. It
swyx
: was a 4
Marc
: 0 2
swyx
: 0 2 4
Marc
: 0 2 payment required.
swyx
: We have a chance now. Nope. I don’t think we’re gonna figure it out. I don’t know. Like, what’s your take?
Marc
: Oh, I think, we’ll, yeah, no, now I think it’s gonna happen for sure.
swyx
: Yeah.
Marc
: Yeah. And there’s two reasons to example for sure. One is we actually have internet native money now in the form of crypto. Stable coins. Stable coins and crypto. And this is, I, I think this is the grand unification basically of ai, crypto, uh, is what’s about to happen now. Um, I think AI is the crypto killer app, I think is where, where this is really gonna come out.
Um, and then the other is it’s just, it, I mean it’s just, I think it’s now obvious. It’s like obviously AI agents are gonna need money and it’s already happening, right? If you’ve got a c if you’ve got a claw and you wanted to buy things for you, you have to give it money in some form.
swyx
: I would say the adoption’s probably like 0.1% if, if that, but Yeah.
Marc
: Oh, today? Yeah. Yeah, yeah. But think, think forward, like where is it going
swyx
: forward thinking
Marc
: The ultimate principle of everything and, and everything that I think I, we, we do is, it’s the William Gibson quote, which is, the future is already here. It just isn’t distributed. Mm-hmm. It isn’t, isn’t distributed yet.
My friends who are the most aggressive use users of, of, of, of open claw, just like have given their clause bank accounts and credit cards. Um, and, and, and, and, and not only have they done it. Obvious that they needed to do it because it’s obvious that they needed to be able to spend money on their behalf.
swyx
: Yeah. Yeah.
Marc
: It’s just completely obvious. And so, and again, like, so the number of people who have done that today to your point is like, I don’t know, probably 5,000 or something. Yeah. But
swyx
: it’ll grow.
Marc
: That’s how these things start
swyx
: actually, I mean, since, uh, you keep mentioning,
Marc
: and by the way, open cloud, by the way, if you don’t give it a bank account, it’s just gonna break into your, your, it’s gonna break high agency, it’s gonna break into your bank account anyway, and, and take your money.
So you, you might, as you might as well do it, you might as well do it,
swyx
: uh,
Marc
: by the way. I really love, I gotta tell you, I really love the phenomenon. I love the Yolo. Um, I’m not doing it myself to be clear, but, but I love the people that are just like, yeah, what, what is it? Skip, skip, vision,
swyx
: danger, skip.
Marc
: Dangerous.
swyx
: Which by the way, is a Facebook thing.
Marc
: Okay?
swyx
: Right. Because, uh, because we, uh, in Facebook, they, they have this culture to name the thing dangerous, so that you are aware when you enable the flag that you are opting into a dangerous thing.
Marc
: Okay, good.
swyx
: And they brought it into open ai and of course that
Marc
: makes it enticing.
swyx
: Sam runs Codex, uh, with skip permissions on, on his laptop.
Marc
: Yes, a hundred percent. And so I, I th I think the way to actually see the future is to find the people who are doing that. There’s a man, you know, and they, you knows,
swyx
: log everything, you know, just watch it, watch the logs,
Marc
: but. Let’s actually find out what the thing can do.
Yeah. And the way to find out what the thing can do is just like, try everything. Yeah. Let it try everything. Let it unlock everything. By the way, that’s how you’re gonna find all the good stuff it can do. By the way. That’s also how you’re gonna find all the flaws. Yeah. I think the people who turn that on for bots are like, they’re, they’re like martyrs to the progress of human civilization.
Like, I feel very bad for their descendants that their bank accounts are gonna get looted by their bots in the first like 20 minutes. But I think the contribution that they’re making to the future of our species is amazing.
swyx
: It’s like gentleman science, you know?
Marc
: Yes. It’s, yes, yes. Experi yourself. It’s, uh, Ben Franklin out with the, trying to try, trying to get lightning to strike his, his, uh, his balloon and see, seeing if he gets electrocuted.
swyx
: Yeah.
Marc
: It’s, uh, Jonas sk with the polio vaccine, right. Injecting it. Yes. So, yes. I, I, I, I think we should have, like agl, we should have like flags and like we should have like monuments to the people that just let open club run their lives.
swyx
: More anecdotes of like, what, what are the craziest or interesting things that people listening to this should go, go home and do.
Marc
: I mean, this is, this is the, this is the, the extreme thing is just like the straight Yolo, like just Yeah. Turn, turn your life
swyx
: on. I mean, that’s a general capability. Yeah. Yeah. Is there like a specific story that was like, wow. And, and everyone in a group chat just lit up.
Marc
: I mean, like, you know, so there’s tons of, there’s already tons of health, you know, there’s the health dashboard stuff is just, is just absolute personal health.
Absolutely amazing. Yeah. The number of stories on, um, I just don’t wanna violate people’s, you know, obviously personal. Yeah. Anonymized. But, um, you know, one of the things open clouds are really good at is hacking into all this stuff in your land. Uh, it’s really good. So, you know, internet of things. AKA internet of shit.
swyx
: Yeah.
Marc
: Like
swyx
: super insecure, but great. It’s discoverable.
Marc
: Yeah, it’s discoverable. O open claw is happy to scan your network, identify all the things. And then my, my, my friends who are most aggressive at this are having open claw take over everything in their house.
swyx
: Yeah.
Marc
: Take it takes over their security cameras.
It takes over their, their, you know, their whatever their, their access control systems. It takes over their webcams. I have a friend whose claw watches him sleep. Put a webcam in your bedroom. Put the, put the claw, put the claw on a loop. Uh, I have it. Wake up frequently and have it watch, just tell it, watch me sleep.
And, and I’ve, I’ve seen the transcripts and it’s literally like Joseph asleep. This is good. This is good that Joe’s asleep. ‘cause you know, I have, I have his health day and I know that he hasn’t been getting enough sleep and so it’s really good that he’s getting sleep. I really hope he gets his full, whatever, you know, five hours of REM sleep.
Uh, Joe’s moving. Joe’s moving. Um, uh, Joe might be wake waking up. This is a real pro. If Joe wakes up now, he is gonna ruin his sleep cycle. Oh, okay. It’s okay. Joe just rolled over. Okay. He’s gone back to bed. Okay, good. Alright. Okay. I can relax. This is fine. He’s
swyx
: monitoring the situation
Marc
: monitoring, monitoring the situation, and, and being a bot, like, you know, is just like very focused, right?
It’s just like, uh, this is like, its reason for existence is to watch Joe sleep. And then, and then I was talking to my friend who did this is like, you know, on the one hand it’s like, all right, this is weird and creepy. Um, and I need to, I need to, maybe this has taken over my life. And then the other thing is like, you know what if I had a heart attack in the middle of the night, this thing literally would like freak out and call 9 1 1.
Like, there’s no question. This thing would figure out how to like, alert medical authorities and like, prob probably some in SWAT teams and like, do whatever would be required to save my life. Right? And so it’s like, you know, like, yeah. Like that’s happening. What else? Um, I’ll give, I, um, uh, it’s a company unitary, uh mm-hmm.
That makes the robot dogs. Um, and I, I actually have one at home, which is, it’s actually really fun. The Chinese companies, the Chinese companies are so aggressive at adopting, uh, new technology, but they don’t always like, listen, take the time to really.
swyx
: Package it,
Marc
: package it, and maybe think it all the way through.
And so, so the, at least the industry dog I have, so it, it has a old non LLM just control system, which by the way is not very good in, in markets. Well, but it, in practices, it’s not that good. It has trouble with stairs and so forth. And so it’s not quite what it should be. But then the language model thing comes out in the voice.
So they, they add, so they add LLM capability and then they, they add a voice mode to it. Um, but, but that LLM capability is not at all connected to the control system. So, so you’ve got this schizophrenic dog that like, is a complete idiot when it comes to climbing the stairs, but it will happily teach you quantum mechanics.
Right. In like a lum English accent. Right. Like, it, it, it is just like absolutely amazing. Jagged intelligence. Yeah. Yeah. Talk about jagged and then, now obviously what’s gonna happen in the future is, is they’re gonna connect together, but they’ll do it. But right now it’s, it’s, and so right now it’s not that useful.
And so I, I have a friend who has one of these who had his claw basically hack in and rewrite the code Rew write new firmware. Yeah. Write new firmware for the, for the unit robot. Ooh. And now it’s, now it’s an actual pet dog for his kids.
swyx
: You could do that before or after like. The motion.
Marc
: Yeah. It’s, he said it’s completely different.
He said it’s a complete transformation. Yeah. And whenever there’s an issue in the thing, now the claw just like reiterates the code. You know, you know, you goes in, it does, does the code and so is it kind of goes to your thing here. So, so like all of a sudden, uh, this is why the way we wanna think about AI code AI coding is not just like writing new apps.
It’s also going in and rewriting all the old stuff that should have worked that never worked. And so, like, I, I think, I think basically, I think the internet, the internet of shit is basically over. Like, I, I think everything, there’s a potential here where like all these devices in your house that have been like basically marginal or you know, basically dumb, you know, like all of a sudden they might all get really smart.
Now you have smart
swyx
: home.
Marc
: You have to decide if, yes, there are horror movies in which this is just, of which this is the premise. And so you have to decide if you want this. Yeah. But, but, but this is the first time I can say with confidence, I now know how you could actually have a smart home. Yeah. Yeah.
With 30 different kinds of things with chips and internet access, where it actually all makes sense and all works together and it’s all coherent in the, in the whole thing. And to have that unlock without a human being having to go do any of that work, like, you know.
swyx
: You know, I, I’m, I’m waiting for a, sorry, mark.
Uh, I can’t let you open that fridge door, you know, like
Marc
: Exactly, exactly. Yes, yes.
swyx
: Because Oh, yeah, yeah. You’re not supposed to eat right
Marc
: now. I have all of, yes, I have every shred of health information, you know, and I know you think you’re doing, you know, da da da. I didn’t think you do this, but you know, this is a real, are you really, you know, are you really sure?
And you know, you told, you know, you told me last night, you really don’t want me to let you do this, so, you know, I’m sorry, but the fridge door is locked. Um, yes. Open
swyx
: the fridge doors.
Marc
: Exactly. And by the way, I know you’re supposed to be studying for a test, so why don’t we, why don’t you go when you can pass the test, um, I will open the fridge door for you.
Yeah.
swyx
: Final protocol and then, and then we can wrap up, uh, proof of human
Marc
: Yes.
swyx
: Uh, right.
Marc
: Yeah.
swyx
: That’s the last piece that we gotta figure out.
Marc
: Yeah. So I would say there’s, there’s two massive, I would say, um, uh, sort of asymmetries in the world right now where we’ve known these asymmetries exist and we, we societally have an unwilling to grapple with them.
And I think they’re both tipping right now. And, and they’re, they’re, they’re, they’re the same thing. It’s virtual world version. It’s a physical world version. So the virtual world version is, is the bot problem. We’re just like, you know, the internet, internet is just like a wash and bots, internet’s a wash and fake people.
It has been forever. Um, by the way, a lot of that has to do with lack of money, you know? And so this, you know, this is the Yeah, this is this.
swyx
: My spicy take was these two are the same thing. And corporations of people too, you know? So interesting.
Marc
: Yeah, yeah, yeah.
swyx
: Okay. So a bank account is proof of human.
Marc
: Yeah.
Okay. Yeah. Until you, until you give the bots bank accounts. Yeah, exactly. So, okay. Yeah. So there’s that. But yeah, look, look, the bot, I mean, every social media user knows this. The bot, the bot problem is a big problem. You know, the bot, the bot problem has been a big problem forever. It’s, it’s a huge problem.
And it’s never really been confronted directly, like at any point, by the way. The physical world version of this is the drone, the drone problem. Um, right. And so we, we’ve known for, you know, we’ve known for 20 years now that the asymmetric threat both in Milit military and actual military conflict, but also in just like security, like, like, you know, security on the home front.
The big threat is, is the cheap attack drone. Right? The, the, the cheap, the cheap suicide, you know, drone with the bomb. And we’ve known that forever. And by the way, like, you know, it’s very disconcerting how like every, you know, every office complex in the, in the co you know, in the world is like unprotected from drone attacks.
Um, every, every stadium, every school, every prison. Like, like, sure e okay, we’ve known that, we’ve never done anything about what you gonna do
swyx
: about it. Yeah.
Marc
: One possibility is just leave, leave them unprotected forever and live in a world of like, asymmetric terrorism forever. Or the other is take the problem seriously and figure out the set of techniques and technologies required to, to be able to deal with that.
Whether those are lasers or jammers or early warning systems, or, you know, all
swyx
: personal force fields,
Marc
: kinetic, personal for dune, uh, personal, personal force fields. Exactly. And in both cases, the, these are, these are economic asymmetries. These are economic asymmetries, right? ‘cause it’s really cheap to field a bot, but it’s very hard to tell something, a bot.
It’s very cheap to field a drone. It’s very hard. It’s very expensive to defend against a drone. But you see what I’m saying is it’s, it’s, it’s the, it’s the virtual version of the problem, and it’s the physical version of the problem. Uh, the virtual version of the problem. What we, what we need quite literally is proof of human.
The reason is because you’re, you’re, you’re not gonna have proof of bot. The, the, the, especially now the, the bots are too good. The, the, the bots can pass the Turing test. And if the bots can pass the Turing test, then you can’t, you can’t screen for bot. You can’t have proof of not a bot. But what you can have is you can have proof of human, you can have, you know, cryptographically validated, this is definitely a person, and this is, and then you can have cryptographically validated.
This is definitely like something that a person said, yeah, this video is real. Right. Um,
swyx
: just to double click on, on, uh, do you think Alex Lanya with world? Yeah. Do you think he’s got it or is there an alternative?
Marc
: Oh, so I mean, there’s gonna be, I think there’ll be, I think many people will try, we’re one of the key, you know, participants in, in, in the World, in the World Project.
I dunno that, yeah. So we’re, we’re partisans, but yeah, I, I think so we think world is exactly correct. Okay. And, and the reason is it, it has, it has to be, it, it has to be proof of human. It it has, because you can’t do proof of not bought. You have to do proof of human to do proof of human. You, you need, you need biological validation.
You, you needed to start with this was actually a person, right? Because otherwise your bot signing up as fake people. Right? So you, you have to have like something, you have to have a bi. Biometric. And then you have to have cryptographic validation. And then the ability to do, to do, to do the lookup. And then, by the way, the other thing you need, which that you, you also need selective disclosure.
Um, so you need to be able to do proof of human without reviewing privacy, all the underlying information. Privacy. Yeah. By the way, another thing you’re need, you’re gonna need proof of age, right? ‘cause there’s all these laws in all these different countries now around you need to be 13 or 16 or 18 or whatever to do different things.
And so you’re gonna, you’re gonna need a, you know, sort of validated proof of age, um, you know, to be able to legally operate, right? And so that, that’s coming. And then you’re gonna want like, proof of credit score and, you know, proof of like, you know, a hundred other things.
swyx
: That’s a tricky one.
Marc
: It is a tricky one, but you’re gonna, you’re gonna, there, there’s no reason, like if somebody’s checking on your credit, somebody shouldn’t, I’ll give you an example.
Somebody shouldn’t need to know your name in order to be able to find out whether you’re credit worthy.
swyx
: Right? I see. Independently verifiable pieces of information.
Marc
: Pieces of information, yeah. It’s like selectively disclosed. And this is the answer to the privacy problem wr large, which is, I, I only need to prove, I need to prove at that moment.
So like, you’re gonna need that. And I, I think their, their, their architecture makes sense. So that needs to get solved. I think language models have tipped, the bots are now too good. Uh, and, and, and so they’re undetectable. And so as a consequence, you, we now need to go confront that problem directly. And then, and like I said, and then the other problem is we, we need to go actually confront the drone problems.
The Ukraine conflict has really unlocked a lot of thinking on that. And now the, um, and now the, the, the, the, the Iran situation is also unlocking that. And so I think there’s gonna be just like this incredible explosion of, of both drone and counter drones.
swyx
: Our drones are better than their drones to keep it that way.
Marc
: Yeah. Yeah. And counter drones,
Alessio
: I think we can sneak in one more question. Go for it. Um, I’m trying to tie together a lot of things that you said over the years. So at the Milken Institute debate with Teal, which is amazing. Um, you talked about the lag between a new technology and kinda like the GDP, um, impact of it.
Marc
: Yep.
Alessio
: The other idea you talked about is bourgeois capitalism and how, you know, this kind of managerial class was needed because of this complexity. And I think if you bring AI into the fold, you have like much higher leverage of people. So like if you have, you know, the Musk industries, um, and you give Elon a gi, you can run a lot more things That’s right.
At once.
Marc
: That’s right.
Alessio
: And then you have the social contract. And I know you reviewed a clip of Sam ing, um, we’re rethinking the whole thing, and you’re like, absolutely not. Yes.
Marc
: Under,
Alessio
: and I wa I was in an event with Sam last night, uh, and he actually said in the last couple weeks it felt like now people are taking that seriously.
Yeah. So I’m just curious like how you’re seeing the structure of organization changing, especially when you invest in early stage companies and, um, yeah, just like how the impact of. Work structure and, uh, all of that is playing out. Yeah.
Marc
: So there’s a whole bunch of, there’s a whole bunch of topics. I know, yeah.
We, we could spend, and by the way, we’d be happy to spend more time, but we could, we could spend more time on all that. So just for people who haven’t followed this, so the, this, this, this term managerial comes from this thinker in the 20th century, James Burnham, who, um, just one of the great kind of 20th century political thinkers, um, societal thinkers.
And he sort of said a as, and he was writing in like the 1940s, 1950s. Um, and he said kind of the, the whole history, capitalism until that point had been in two phases. Number one had been what he called bourgeois capitalism, which was think about as like name on the door, like Ford Motor Company. ‘cause Henry Ford runs the company.
Um, and Henry, it’s like a DIC dictatorial model. And Henry Ford just like tells everybody what to do. And he said the problem with bourgeois capitalism is it doesn’t scale. ‘cause Henry Ford can only tell so many people to do so many things. And then he runs at a time in the day. And so, um, he said the second phase of capitalism was what he called managerial capitalism, which was the creation of a professional class of managers, um, that are trained not to be like.
Car experts or to be whatever experts in any particular field, but are trained to be experts in management. And then that led to, you know, the importance of like Harvard business, you know, business schools and management consulting firms and all these things. And then you look at every big company today, and like most of the executives at most of the Fortune 500 companies are not domain experts in whatever the company does.
And they’re certainly not the founders of those, but they’re professional managers. And in fact, in the course of their careers, they’ll probably manage many different kinds of businesses. They’ll rotate around and they might work in healthcare for a while and then work in financial services and then go work in something else, you know, come work in tech.
And what Burnham said is he said that transition is absolutely required because the, the, the, the problem with bourgeois capitalism is, is it doesn’t scale. Henry Ford doesn’t scale. And so if you’re gonna run capitalist enterprises that are gonna have millions to billions of customers, um, you’re gonna need to, you’re, they’re gonna be operating a level of scale and complexity that’s gonna require this professional management class.
And he said, look, the, the professional management class has its downsides. Like they’re not necessarily experts at doing the thing. They’re not as inventive, you know, they’re not gonna create the next breakthrough thing. But he is like, whether you think that’s good or bad or whatever is what’s gonna be required.
And basically that’s what happened. Right. And so he wrote that book originally in like 1940, you know, over the course of the next 50 years, basically. Managerialism. Well, I mean, today, up till today, managerial managerialism basically took over everything. Mm-hmm. And you know, what I’m describing is basically how all big companies run and how all governments run and how are large scale nonprofits run and kind of everything, you know, everything runs basically what, what, what Venture Capital does is we basically are a rump, uh, sort of protest movement to that.
To try to find the next Henry Ford or, or just to say El Elon Musk or, or the next, or the next Elon Musk or the next Steve Jobs, or the next Bill Gays. The next Mark Zuckerberg. And so we, we, we, we start these companies in, in the old model, right? We, we, we start them out as, as, as, as in the Henry Ford model.
And so we start them out with a founder or a, or a, or a founder with, with colleagues. But you know, there’s the a founder, CEO, um, and then we basically bet that we basically bet that the startup is going to be able to do things, specifically innovate in ways that the big incumbents in that industry are not gonna be able to do.
And so it’s a bet that by, basically by relighting this sort of name on the door, you know, kind of thing. Mm-hmm. This new innovative thing with like a king monarchical, uh, uh, political structure, um, that they’re gonna be able to innovate in a way that the incumbent is not going to be able to because the incumbent is, is being run by managers.
Right. And, and, and, and by the way, and of course venture being what it is, sometimes that works, sometimes it doesn’t. But we’re, we’re constantly doing that, but I’ve always viewed it my entire life as like, we’re like raging against the dying of the light. Mm-hmm. Like we’re, we’re, we’re, we’re sort of constantly trying to fight off managerialism, just basically swamping everything and everything.
Getting basically boring and gray and dumb and old. Right. And we’re trying to keep some level of energy vitality in the system. AI is the thing that would lead you to think, wow, maybe there’s a third model.
Alessio
: Mm-hmm.
Marc
: Right? And, and maybe may and way to think about it would be, maybe it’s a combination of the two, maybe the new Henry Ford or the new Elon or the new Steve Jobs plus ai, right.
Is the best of both. Right. Because it’s, it’s, it’s sort of the spark of genius of the name on the door model, the Henry Ford model. But then it’s give that person AI superpowers to do all the managerial stuff and let the boss draw the managerial stuff. That may be the actual secret formula. And we’ve never even known that we wanted this because we never even thought it was a possibility.
But I mean, you know, this, what is the thing that these bots are really good, they’re really good at doing paperwork. Like they’re really good at filling out forms, right? Like they’re really good at writing reports, they’re really good at reading, they’re really good at doing all the managerial work. Like they’re amazing at it.
And so, yeah, so I, I think, I think the, I a hundred percent, I think the answer, the answer very well might be to get the best, best of both worlds by doing this. And then the challenge is gonna be twofold. The challenge is gonna be for the innovators to really figure out how to leverage AI actually do this.
Right? Um, and, and then, and then the, the other challenge is gonna be for the, for the incumbents that are managerial, to figure out like, okay, what does that mean? ‘cause now they’re gonna, they’re, they’re gonna be facing a different kind of insurgent competitor that has a different set of capabilities than they’re used to.
And so th the, this really I think is gonna force a lot of big companies to kind of figure out innovation. EE either I say figure out innovation or die trying.
Alessio
: Do you feel like that structure accelerates the impact on the actual GDPN economy? If you look at Space Act? Yes. The growth is like so fast. Yeah.
And like, instead of having these companies kind of like Peter out in growth and impact, they can kind of like keep going if not accelerating.
Marc
: Yeah, that’s for sure. The hope, um, the, the, the challenge and, and you know, and, and look, the AI utopian view is of course, of course. And, and, and that’s gonna be the future of the economy.
And it’s gonna grow 10 x and a hundred x and a thousand x. And we’re entering this regime of like much higher economic growth forever and consumer cornucopia of everything. And it’s, it’s gonna be great. And I, and, and I hope that’s true. I hope that’s, that’s like the u you know, that’s the current kind of utopian vision.
I hope that’s true. The problem is, it goes back again. The real world is really messy. Um, and I’ll give you an example of how the real world is really messy. It requires 900 hours of professional certification training to become a hairdresser in the state of California. Um, so it’s like 35% of the economy, something like that.
You have to get some sort of professional certification to do the job, which is to say that the, the professions are all cartels, right? Yeah. And so you have to get licensed as a doctor. You have to get licensed as a lawyer, you have to get licensed as a. You have to get into a union. Mm-hmm. Um, by the way, to, to work for the government, you need to be, you, you have both civil service protections and you have public sector unions.
You have two layers of insulation, uh, against ever getting fired for anything or anything. Anything ever changing. I’ll give you another example. The the dock work. The dock workers one on strike a couple years ago. Mm-hmm. ‘cause they, you know, robotics, you know, if, if you go look at a modern dock, like in Asia, it’s all robots.
If you go to American dock, it’s like all still guys, dragon, dragon stuff, by by hand, the dock works. Goes on a strike. It turns out there are 25,000 dock workers working on, on, on, on Docs in America. It turns out they have incredible political power. Mm-hmm. Because it’s a, it’s, it’s one of these un unified blocks of things.
They won their strike and so they got commitments from the dock owners to not implement more automation. We learned a couple things in that. So number one, we learned that even a union as small as 25,000 people still has like tremendous political stroke. We also learned that they, it actually turns out the Dock Workers Union has 50,000 people in it.
‘cause there’s 20, they have 25,000 people working in the docks. They have 25,000 people during full paycheck sitting at home from prior union agreements. Oh my
swyx
: God.
Marc
: From prior union agreements. I’ll give you another great example. There are government agencies, there are federal government agencies where the employees right of have civil service protections and there are in public sector unions.
There are entire federal government agencies that struck new collective bargaining agreements during COVID, where not only are they have their jobs guaranteed in perpetuity, but they only have to report to work in an office one day per month. And so there are entire office buildings in Washington DC that are empty 29 outta 30 days of the year that are still operating and are still, we’re all still paying for it.
20 and say, and then what they do, it turns out what the employees do is they’re very, they’re very smart in, in, in this way. And so they figure out, they come in on the last day of a month and the first day of the next month. And so and so, they’re, so, they’re in there, they’re in the office two days per 60 days, which means these buildings are empty for 58 days at a time.
And you see what I’m, you see where I’m heading with this? Like this is like locked in, right? This is like locked in in a way that has nothing to do with like, and people say capitalist, it’s like anticapitalistic. It’s like, it’s, it’s basically it’s restrictions on trade, it’s restrictions on the ability to like change the workforce.
And so, so much of our economy is, is, you know, the, the, I I’m, I’m describing the entire healthcare system. I’m describing the entire legal profession. I’m describing the entire housing industry. I’m describing the entire education system, right? K through 12 schools in the United States. They’re a literal government monopoly.
How are we gonna apply AI and education? The answer is we’re not, because it’s a literal government monopoly, it is never going to change the end. And there is nothing to do, by the way, you can create an entirely new school system. Like that’s the one thing you can do, is you can do what Alpha School’s doing.
You can create an entirely new school system. Other than that, you’re not gonna go in and change what’s happening in the American classroom, like K through 12. There’s no chance the teachers are 100% opposed to it. It’s a hundred percent not gonna happen. So, so you see what I’m saying is like there’s this like massive slippage that’s gonna take place.
Both the AI utopians and the AI dors are far too optimistic.
swyx
: Right.
Marc
: You see what I’m saying? Be because they believe that because the technology makes something possible that 8 billion people all of a sudden are gonna change how they behave. And it’s just like, nope. So much of how the existing economy works.
Mm-hmm. It’s just, it. It’s just like wired in. And so we’re gonna be lucky as a society, we’re gonna be lucky if AI adoption happens quickly. Right. Because if it doesn’t, what we’re just gonna have is stagnation.
Alessio
: Awesome. Mark. I know you gotta run.
swyx
: Yeah. We all know or still welcome. But, uh, it was such a pleasure talking to you.
Uh, we’re truly living in the age of science fiction coming to real life.
Marc
: Yes. Yes. Could not be more exciting. Yeah. Really. Thank you, mark. You guys awesome.
swyx
: Thank That’s it.
Marc
: Good. Thank you. That’s it.
