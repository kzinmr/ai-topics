---
title: "Why hardware development is hard"
url: "https://danluu.com/hardware-unforgiving/"
fetched_at: 2026-05-05T07:01:35.607684+00:00
source: "Dan Luu"
tags: [blog, raw]
---

# Why hardware development is hard

Source: https://danluu.com/hardware-unforgiving/

In CPU design, most successful teams have a fairly long lineage and rely heavily on experienced engineers. When we look at CPU startups, teams that have a successful exist often have a core team that's been together for decades. For example, PA Semi's acquisition by Apple was a moderately successful exit, but where did that team come from? They were the SiByte team, which left after SiByte was acquired by Broadcom, and SiByte was composed of many people from DEC who had been working together for over a decade. My old company was similar: an IBM fellow collected
the best people he worked with at IBM
who was a very early Dell employee and then exec (back when Dell still did interesting design work), then split off to create a chip startup. There have been quite a few CPU startups that have raised tens to hundreds of millions and leaned heavily on inexperienced labor; fresh PhDs and hardware engineers with only a few years of experience. Every single such startup I know of failed.
This is in stark contrast to software startups, where it's common to see successful startups founded by people who are just out of school (or who dropped out of school). Why should microprocessors be any different? It's unheard of for a new, young, team to succeed at making a high-performance microprocessor, although this hasn't stopped people from funding these efforts.
In software, it's common to hear about disdain for experience, such as Zuckerberg's comment, "I want to stress the importance of being young and technical, Young people are just smarter.". Even when people don't explicitly devalue experience, they often don't value it either. As of this writing, Joel Spolsky's ”
Smart and gets things done
” is probably the most influential piece of writing on software hiring. Note that it doesn't say "smart, experienced, and gets things done.". Just "smart and gets things done" appears to be enough, no experience required. If you lean more towards the Paul Graham camp than the Joel Spolsky camp, there will be a lot of differences in how you hire, but Paul's advice is the same in that
experience doesn't rank as one of his most important criteria
,
except as a diss
.
Let's say you wanted to hire a plumber or a carptener, what would you choose? "Smart and gets things done" or "experienced and effective"? Ceteris paribus, I'll go for "experienced and effective", doubly so if it's an emergency.
Physical work isn't the kind of thing you can derive from first principles, no matter how smart you are. Consider South Korea after WWII.
Its GDP per capita was lower than Ghana, Kenya, and just barely above the Congo
. For various reasons, the new regime didn't have to deal with legacy institutions; and they wanted Korea to become a first-world nation.
The story
I've heard
is that the government started by subsidizing concrete. After many years making concrete, they wanted to move up the chain and start more complex manufacturing. They eventually got to building ships, because shipping was a critical part of the export economy they wanted to create.
They pulled some of their best business people who had learned skills like management and operations in other manufacturing. Those people knew they didn't have the expertise to build ships themselves, so they contracted it out. They made the choice to work with Scottish firms, because Scotland has a long history of shipbuilding. Makes sense, right?
It didn't work. For historical and geographic reasons, Scotland's shipyards weren't full-sized; they built their ships in two halves and then assembled them. Worked fine for them, because they'd be doing it at scale since the 1800s, and had
world renowned expertise
by the 1900s. But when the unpracticed Koreans tried to build ships using Scottish plans and detailed step-by-step directions, the result was two ship halves that didn't quite fit together and sunk when assembled.
The Koreans eventually managed to start a shipbuilding industry by hiring foreign companies to come and build ships locally, showing people how it's done. And it took decades to get what we would consider basic manufacturing working smoothly, even though one might think that all of the requisite knowledge existed in books, was taught in university courses, and could be had from experts for a small fee. Now, their manufacturing industries are world class, e.g., according to Consumer Reports, Hyundai and Kia produce reliable cars. Going from producing unreliable econoboxes to reliable cars you can buy took over a decade, like it did for Toyota when they did it decades earlier. If there's a shortcut to quality other than hiring a lot of people who've done it before, no one's discovered it yet.
Today, any programmer can take Geoffrey Hinton's
course on neural networks and deep learning
, and start applying state of the art machine learning techniques. In software land, you can fix minor bugs in real time. If it takes a whole day to run your regression test suite, you consider yourself lucky because it means you're in one of the few environments that takes testing seriously. If the architecture is fundamentally flawed, you pull out your copy of Feathers' “
Working Effectively with Legacy Code
” and repeatedly apply fixes.
This isn't to say that software isn't hard, but there are a lot of valueable problems that don't need a decade of hard-won experience to attack. But if you want to build a ship, and you "only" have a decade of experience with carpentry, milling, metalworking, etc., well, good luck. You're going to need it. With a large ship, “minor” fixes can take days or weeks, and a fundamental flaw means that your ship sinks and you've lost half a year of work and tens of millions of dollars. By the time you get to something with the complexity of a modern high-performance microprocessor, a minor bug discovered in production costs three months and millions of dollars. A fundamental flaw in the architecture will cost you five years and hundreds of millions of dollars.
Physical mistakes are costly. There's no undo and editing isn't simply a matter of pressing some keys; changes consume real, physical resources. You need enough wisdom and experience to avoid common mistakes entirely – especially the ones that can't be fixed.
Thanks to Sophia Wisdom for comments/corrections/discussion.
CPU internals series
In retrospect, I think that I was too optimistic about software in this post. If we're talking about product-market fit and success, I don't think the attitude in the post is wrong and people with little to no experience often do create hits. But now that I've been in the industry for a while and talked to numerous people about infra at various startups as well as large companies, I think creating high quality software infra requires no less experience than creating high quality physical items. Companies that decided this wasn't the case and hire a bunch of smart folks from top schools to build their infra have ended up with low quality, unreliable, expensive, and difficult to operate infrastructure. It just turns out that, if you have very good product-market fit, you don't need your infra to work. Your company can survive and even
thrive while having infra that has 2 9s of uptime and costs an order of magnitude more than your competitor's infra
or
if your product's architecture means that it can't possibly work correctly
. You'll make less money than you would've otherwise, but the high order bits are all on the product side. If you contrast that chip companies with inexperienced engineers that didn't produce a working product, well, you can't really sell a product that doesn't work even if you try. If you get very lucky, like if you happened to start deep learning chip company at the right time, you might get big company to acquire your non-working product. But, it's much harder to get an exit like that for a microprocessor.
