---
title: "Pluralistic: CARDiac, syntax coloring, view source and vibe code (03 Jul 2026)"
url: "https://pluralistic.net/2026/07/03/rod-logic/"
fetched_at: 2026-07-04T07:01:40.344010+00:00
source: "pluralistic.net"
tags: [blog, raw]
---

# Pluralistic: CARDiac, syntax coloring, view source and vibe code (03 Jul 2026)

Source: https://pluralistic.net/2026/07/03/rod-logic/

Today's links
CARDiac, syntax coloring, view source and vibe code
: With great abstraction comes great power comes great responsibility comes great loss of fidelity.
Hey look at this
: Delights to delectate.
Object permanence
: Real elections v reality TV; Copyright troll loses license; Who gets fed housing subsidies? Trump x forced labor.
Upcoming appearances
: London, Edinburgh, Sydney, Melbourne, Brighton, London, South Bend.
Recent appearances
: Where I've been.
Latest books
: You keep readin' em, I'll keep writin' 'em.
Upcoming books
: Like I said, I'll keep writin' 'em.
Colophon
: All the rest.
CARDiac, syntax coloring, view source and vibe code (
permalink
)
In the mid-1970s, my dad – then a budding computer scientist, subsequently a math teacher – brought home my first computer: the CARDiac, a Turing-complete, all-cardboard
papercraft
computer that you could write and execute programs on:
https://en.wikipedia.org/wiki/CARDboard_Illustrative_Aid_to_Computation
CARDiac stands for "CARDboard Illustrative Aid to Computation," and it was created in 1968 at Bell Labs as a way to teach high schoolers how computers worked. I wasn't anywhere near high school age (I think I was in third grade?) but the CARDiac was revelatory. The year before, I'd had access to a teletype terminal and acoustic coupler that let me operate a PDP machine at the University of Toronto, and I'd been endlessly fascinated with the possibilities. I wrote simple BASIC programs, chatted with ELIZA, and messaged other system users, one keystroke at a time, all on paper (the terminal didn't have a screen, just a printer, and we fed it 1,000' rolls of paper towels my mom brought home from her kindergarten classroom, which I then rolled back up so she could put them back in the bathroom for the kids to dry their hands on).
Interacting with a computer in real-time was captivating, but it wasn't until I assembled and used the CARDiac that it all snapped into place. With the CARDiac, you composed simple programs with pencil and paper, then followed instructions that directed you to move paper tokens in and out of various slots representing memory cells and an accumulator. All an electronic computer does is repeat these crude mechanical operations, millions of times per second, using microscopic transistors. None of that action can be observed with the naked eye, of course. If you had a very sensitive multimeter and a very good microscope, it's conceivable that you could indirectly watch this intricate dance, but only on very early processors, and only if you drastically slowed down their operations.
Much later, I learned a word for what I got from the CARDiac:
legibility
. Together, the CARDiac and I made a working digital computer, with me standing in for the physics that propels electrons down the endless labyrinth of a microchip, like a pinball triggering various blooping, beeping bumpers. Though the computing we performed was sub-trivial (adding one and one was a major undertaking!), the physical performance of that computing imbued me with
Fingerspitzengefühl
("fingertip feeling"):
https://en.wikipedia.org/wiki/Fingerspitzengef%C3%BChl
This stood me in great stead in the years to come. To this day, when I think about my computer, I sometimes imagine those little cardboard tokens, shuffling in and out of the slits in my paper CARDiac. There's something very reassuring about this imagery. No matter how many levels of abstraction sit between me and the nanoscale transistors ranked in their billions beneath my fingertips, they are all undertaking those familiar operations I painstakingly performed on my child's desk all those years ago.
(This is one of the things that makes
Science Comics Computers: How Digital Hardware Works
such an amazing kids' book! By illustrating how a computer's operations are built up from simple boolean logic that can be represented as physical switches, the comic performs that same legibilizing magic that I got from the CARDiac:)
https://pluralistic.net/2025/11/05/xor-xand-xnor-nand-nor/#brawniac
Not long after my CARDiac experience, my dad brought home an Apple ][+, which came with a schematic that revealed the inner workings of the machine in ways that I found visually striking, if significantly less accessible than the CARDiac:
https://downloads.reactivemicro.com/Apple%20II%20Items/Hardware/II_&_II+/Schematic/Apple%20II%20Schematics.pdf
(For me, at least. For the legendary hardware hacker Andrew "bunnie" Huang, it was the start of a journey that turned him into one of the world's virtuoso reverse-engineers and science communicators):
https://pluralistic.net/2026/01/09/quantity-break/#so-many-chips
The Apple ][+ did very little when you took it out of the box. It came with a few floppies' worth of demo programs, and we bought a few more down at the local computer store, but most of the programs I ended up using with that machine were ones I typed in myself, from magazines I bought at the corner store (I spent half my magazine budget on
Cracked
,
Mad
and
Crazy
, the other half on computer magazines full of BASIC program listings).
Typing in a program, keystroke by keystroke, was another Fingerspitzengefühl-generating exercise. I wasn't much of a typist, so it was slow going, and of course I made a lot of typos. What's more, BASIC had already fragmented into several dialects by this point, so even a correctly typed program could fail to run until it had been adapted for the BASIC that shipped with the computer. Getting a program to run on my computer required me to hone my typing skills, but even more so, my
problem solving
skills.
After months of this, I (re-)invented the debugger, from first principles, coming up with lots of little tricks and gimmicks (many of them horribly inefficient) for identifying and solving my programs' errors. In later years, I had lots of opportunity to work with
real
debuggers, created and maintained by trained programmers who'd forgotten more than I would ever know about writing code, and my own cack-handed efforts to build my own version of their tools conferred a confidence and intuitive understanding that I could not have achieved otherwise. Figuring out the need for a debugger and then rolling my own (crude, inefficient) one made
all
debuggers more legible to me.
I think that "legibility" is an underrated trait. If a system is legible to you, then you have a superior basis for understanding it, improving it, and making it work again when it breaks down.
There's an old joke that goes, "physics is applied math; chemistry is applied physics, and biology is applied chemistry" (I've also heard versions that start with "math is applied philosophy" and carry on to "sociology is applied biology," etc). While this isn't
entirely
true, there's something profound in it: we understand and manipulate our complex reality by wrapping it in abstractions that package up a writhing, shuffling, vibrating machine inside a smooth, serene membrane with a sturdy and easily grasped handle. You
could
do chemistry using the tools of physics, but it would take hours to perform the kind of calculations a chemist does in seconds (just as it takes an eternity to add one and one with a CARDiac).
Nevertheless, there are times when it is useful for a biologist to think about chemical processes, and for a chemist to think about interactions at the level of physics, and for a physicist to do math. The membrane and the handle are essential, but sometimes you have to decap the sealed package and inspect and manipulate its internals directly. Problem solving, improvement and maintenance all require the ability to move up and down the stack of abstractions to figure out where to stick your probes and stage your interventions.
This is where legibility comes in. Interacting with physical processes improves your mental model. In
Broad Band
(a magisterial history of women in computing), Claire Evans talks about how the first programmers were women who did the "unskilled" labor of physically cabling components together, developing powerful Fingerspitzengefühl, with such high-fidelity, trans-abstraction mental models of the machines' operations that they became the world's best programmers and debuggers:
https://pluralistic.net/2021/02/13/data-protection-without-monopoly/#broad-band
My early adventures in programming were so powerful and instructive because nearly all the programs I interacted with on my Apple ][+ were written in BASIC (not just the ones I keyed in, but also the demo software and much of the packaged software we bought). That meant that I could get a listing of any program I was using, peeling open the membrane to look at the machinery underneath. I could even laboriously trace the operations of that program using my toy debugger. This, too, was legibility: the ability to flip between the effects of the running code, and the instructions themselves (and then to mentally map those instructions onto the movement of cardboard tokens in my CARDiac).
This affordance was repeated later on the early web, thanks to the "View Source" function that came built into every browser, acting as a velcro tab for the membrane that separated rendered web pages from their underlying instructions. In my early years as a web developer, I copied, pasted, adapted, probed and traced HTML in ways that would have been instantly recognizable to the younger me, keying in those BASIC programs and ripping apart the commercial software on my computer.
I read somewhere that the Bell Labs scientists who created the CARDiac were worried that, thanks to transistorization, the next generation of programmers wouldn't understand the physical, material processes that unfolded when their programs ran, and that this would mean a loss of legibility and intuition and Fingerspitzengefühl. I can't track down the reference now, but it stuck with me, because the CARDiac is
such
a perfect way of preserving those virtues.
Modern computer science curriculum includes some chip design for just this reason (just as chemists study physics and biologists study chemistry). But there are plenty of programmers – better programmers than I ever was or will be – who taught themselves and never had a CARDiac or gave much thought to chip design. They work at different layers of abstraction and in different ways to solve different problems. Maybe they could improve their art by tinkering with FPGAs, but there's always something even the most skilled artisan can do to round out and incrementally improve their craft.
In the same way, there are plenty of programmers – better ones than I ever was or will be – whose journey started at higher abstraction layers than a teletype terminal or a CARDiac. Maybe they started with a browser's View Source, teasing apart other people's Javascript to create weird Myspace customizations. Maybe they tweaked a programmable block in Minecraft. Maybe they modded a Scratch game. Or maybe they recorded macros using Applescript or Hypercard or Visual Basic to automate a routine task, only to later open up the source code generated by the macro recorder to make fine adjustments.
Whether you're pasting source from Stack Overflow or recording a macro in Excel, you are just one operation away from unwrapping the membrane and exposing the code beneath it. And with the modern internet, with Wikipedia, with endless tutorial videos, you are one further operation from penetrating the high level code to get at the code beneath it, and the code beneath that, and the code beneath
that
, all the way down to the bare metal.
Which brings me to vibe coding. As I've written, there's a world of difference between writing code for production and writing "personal software" that solves a problem
you
have. Whatever deficits that code has (due to the fact that you're not a skilled programmer) are offset by the fact that
you're
the one making the tool (which means your needs aren't lossily filtered through a programmer's understanding of those needs):
https://pluralistic.net/2026/06/15/vernacular/#hypercardian
There's nothing wrong with code that solves your problem, even if you don't know how that code works, even if it breaks in a couple of years, even if no one else could maintain, extend or debug that code. Personal software is fundamentally different from software made to be used and maintained by others:
https://pluralistic.net/2026/07/02/canonization/#operate-iterate-improve
Higher-level abstractions are
necessary
. Moving tokens between the slits in a CARDiac is a powerful exercise, but eventually you want to do something more substantial than adding one and one, and so you need to package up the mechanics of computing inside a membrane with an easily grasped handle (knowing that you can always open the membrane if need be).
The more automated code you generate – macros, pasted Javascript, Minecraft blocks – the greater the likelihood that you will be failed by a readymade, prefab component. At that point, you have means, motive and opportunity to open the membrane and start tinkering with the internals, and every time you do, you have a better chance of making a realization that improves your grasp on the whole system.
Automated code – whether from an LLM, View Source, Stack Overflow, or a macro recorder – is the top of a funnel. Many – most – of the people who enter the funnel won't slip further down the abstraction chute. They'll solve their problem (a virtue unto itself!) and move on. But the more people we put at the top of the funnel, the more chances our civilization gets to produce another skilled artisan who understands and can improve, iterate and repair the code the rest of us use.
Hey look at this (
permalink
)
Object permanence (
permalink
)
#20yrsago What real elections can learn from reality TV voting
https://henryjenkins.org/2006/07/democracy_big_brother_style_1.html
#20yrsago Veteran print journo on neglected demographics
http://citmedia.org/blog/2006/07/03/guest-posting-is-media-performance-democracys-critical-issue/
#10yrsago One of the copyright’s scummiest trolls loses his law license
https://fightcopyrighttrolls.com/2016/07/03/prendas-hansmeier-stipulates-to-suspension-of-his-law-license/
#10yrsago Macedonia’s Colorful Revolutionaries defy the state by splashing paint on government buildings and monuments
https://globalvoices.org/2016/07/03/defying-police-harassment-the-macedonian-colorful-revolutionaries-continue-to-chant-freedom/
#10yrsago Trump and Brexit are like lotto tickets: the more unrealistic, the better
https://www.irishtimes.com/news/world/europe/fintan-o-toole-brexit-and-the-politics-of-the-fake-orgasm-1.2707398
#10yrsago Low income US households get $0.08/month in Fed housing subsidy; 0.1%ers get $1,236
https://web.archive.org/web/20160702151008/https://www.thenation.com/article/who-benefits-most-from-housing-subsidies-the-wealthy/
#5yrsago The future is symmetrical
https://pluralistic.net/2021/07/03/beautiful-symmetry/#fibrous-growth
#1yrago Trump's not gonna protect workers from forced labor
https://pluralistic.net/2025/07/03/states-rights-trumps-wrongs/#mamdani
Upcoming appearances (
permalink
)
Recent appearances (
permalink
)
"The Reverse-Centaur's Guide to AI," a short book about being a better AI critic, Farrar, Straus and Giroux, June 2026
https://us.macmillan.com/books/9780374621568/thereversecentaursguidetolifeafterai/
"Canny Valley": A limited edition collection of the collages I create for Pluralistic, self-published, September 2025
https://pluralistic.net/2025/09/04/illustrious/#chairman-bruce
"Enshittification: Why Everything Suddenly Got Worse and What to Do About It," Farrar, Straus, Giroux, October 7 2025
https://us.macmillan.com/books/9780374619329/enshittification/
"Picks and Shovels": a sequel to "Red Team Blues," about the heroic era of the PC, Tor Books (US), Head of Zeus (UK), February 2025 (
https://us.macmillan.com/books/9781250865908/picksandshovels
).
"The Bezzle": a sequel to "Red Team Blues," about prison-tech and other grifts, Tor Books (US), Head of Zeus (UK), February 2024 (
thebezzle.org
).
"The Lost Cause:" a solarpunk novel of hope in the climate emergency, Tor Books (US), Head of Zeus (UK), November 2023 (
http://lost-cause.org
).
"The Internet Con": A nonfiction book about interoperability and Big Tech (Verso) September 2023 (
http://seizethemeansofcomputation.org
). Signed copies at Book Soup (
https://www.booksoup.com/book/9781804291245
).
"Red Team Blues": "A grabby, compulsive thriller that will leave you knowing more about how the world works than you did before." Tor Books
http://redteamblues.com
.
"Chokepoint Capitalism: How to Beat Big Tech, Tame Big Content, and Get Artists Paid, with Rebecca Giblin", on how to unrig the markets for creative labor, Beacon Press/Scribe 2022
https://chokepointcapitalism.com
"The Post-American Internet," a geopolitical sequel of sorts to
Enshittification
, Farrar, Straus and Giroux, 2027
"Unauthorized Bread": a middle-grades graphic novel adapted from my novella about refugees, toasters and DRM, FirstSecond, April 20, 2027
"Enshittification, Why Everything Suddenly Got Worse and What to Do About It" (the graphic novel), Firstsecond, 2027
"The Memex Method," Farrar, Straus, Giroux, 2027
Today's top sources:
Currently writing: "The Post-American Internet," a sequel to "Enshittification," about the better world the rest of us get to have now that Trump has torched America. Fourth draft completed. Submitted to editor.
A Little Brother short story about DIY insulin PLANNING
This work – excluding any serialized fiction – is licensed under a Creative Commons Attribution 4.0 license. That means you can use it any way you like, including commercially, provided that you attribute it to me, Cory Doctorow, and include a link to pluralistic.net.
https://creativecommons.org/licenses/by/4.0/
Quotations and images are not included in this license; they are included either under a limitation or exception to copyright, or on the basis of a separate license. Please exercise caution.
How to get Pluralistic:
Blog (no ads, tracking, or data-collection):
Pluralistic.net
Newsletter (no ads, tracking, or data-collection):
https://pluralistic.net/plura-list
Mastodon (no ads, tracking, or data-collection):
https://mamot.fr/@pluralistic
Bluesky (no ads, possible tracking and data-collection):
https://bsky.app/profile/doctorow.pluralistic.net
Medium (no ads, paywalled):
https://doctorow.medium.com/
Tumblr (mass-scale, unrestricted, third-party surveillance and advertising):
https://mostlysignssomeportents.tumblr.com/tagged/pluralistic
"
When life gives you SARS, you make sarsaparilla
" -Joey "Accordion Guy" DeVilla
READ CAREFULLY: By reading this, you agree, on behalf of your employer, to release me from all obligations and waivers arising from any and all NON-NEGOTIATED agreements, licenses, terms-of-service, shrinkwrap, clickwrap, browsewrap, confidentiality, non-disclosure, non-compete and acceptable use policies ("BOGUS AGREEMENTS") that I have entered into with your employer, its partners, licensors, agents and assigns, in perpetuity, without prejudice to my ongoing rights and privileges. You further represent that you have the authority to release me from any BOGUS AGREEMENTS on behalf of your employer.
ISSN: 3066-764X
