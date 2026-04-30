---
title: "Pluralistic: The (other) problem with automatic conversion of free software to proprietary software (23 Apr 2026)"
url: "https://pluralistic.net/2026/04/23/poison-pill/"
fetched_at: 2026-04-30T07:01:02.288351+00:00
source: "pluralistic.net"
tags: [blog, raw]
---

# Pluralistic: The (other) problem with automatic conversion of free software to proprietary software (23 Apr 2026)

Source: https://pluralistic.net/2026/04/23/poison-pill/

Today's links
The (other) problem with automatic conversion of free software to proprietary software
: You can't add ANY license to a public domain work.
Hey look at this
: Delights to delectate.
Object permanence
: Pimp My Snack; Abandoned Soviet missile silo full of cash; MPAA v 'democratizing culture'; 3,000 page garbage Kindle books; London's lost postal tunnels; Internet voting is stupid; Congress lobotomized itself; GWB v 'truth in politics'; Trump's FTC x tariff profiteering.
Upcoming appearances
: San Francisco, London, Berlin, NYC, Barcelona, Hay-on-Wye, London, NYC.
Recent appearances
: Where I've been.
Latest books
: You keep readin' em, I'll keep writin' 'em.
Upcoming books
: Like I said, I'll keep writin' 'em.
Colophon
: All the rest.
The (other) problem with automatic conversion of free software to proprietary software (
permalink
)
Here's an interesting stunt: a project called Malus.sh will take your money, and in exchange, it will ingest any free/open source code you want, refactor that code using an LLM, and spit out a "clean room" version that is freed from all the obligations imposed by the original project's software license:
https://www.404media.co/this-ai-tool-rips-off-open-source-software-without-violating-copyright/?ref=daily-stories-newsletter
Malus was co-created by Mike Nolan, who "researches the political economy of open source software and currently works for the United Nations." Nolan told 404 Media's Emanuel Maiberg that he shipped Malus as a real, live-fire business that will exchange money for an AI service that destroys the commons as a way to alert the free software movement to a serious danger.
As Maiberg writes, Malus relies on a legal precedent set in 1982, in which IBM brought a copyright suit against a small upstart called Columbia Data Products for reverse-engineering an IBM software product. IBM's argument was that Columbia must have copied its
code
– the copyrightable part of a work of software – in order to reimplement the
functionality
of that code. Functions aren't copyrightable: copyright protects creative expressions, not the ideas that inspire those expressions. The
idea
of a computer program that performs a certain algorithm is
not
copyrightable, but the
code
that turns that idea into a computer program
is
copyrightable.
Columbia's successful defense against IBM involved using a "clean room" in which two isolated teams collaborated on the reimplementation. The first team examined the IBM program and wrote a specification for
another
program that would replicate its functionality. The second team received the specification and turned it into a computer program. The first team
did
handle IBM software, but they did not create a new work of software. The second team
did
create a new work of software, but they never handled any IBM code.
This is the model for Malus: it pairs two LLMs, the first of which analyzes a free software program and prepares a specification for a program that performs the identical function. The second program receives that specification and writes a new program.
The Malus FAQ performs a "be as evil as possible" explanation for the purpose of this exercise:
Our proprietary AI robots independently recreate any open source project from scratch. The result? Legally distinct code with corporate-friendly licensing. No attribution. No copyleft. No problems.
This business about "attribution" and "copyleft" is a reference to the terms imposed by some free software licenses. The purpose of free software is to create a commons of user-inspectable, user-modifiable software that anyone can use, improve, and distribute. To achieve this, many free software licenses impose obligations on the people who distribute their code: you are allowed to take the code, improve the code, give it away or sell it,
but
you have to let other people do the same.
Typically, you have to inform people when there's free software in a package you've distributed (attribution) and supply them with the "source code" (the part that humans read and write, which is then "compiled" into code that a computer can use) on demand, so they can make their own changes. This system of requiring other people to share the things they make out of the code you share with them is sometimes called "copyleft," because it uses copyright, which is normally a system for restricting re-use to require people
not
to restrict that use.
Companies
love
to
use
free software, but they don't like to
share
free software. Companies like Vizio raid the commons for software that is collectively created and maintained, then simply refuse to live up to their end of the bargain, violating the license terms and (incorrectly) assuming no one will sue them:
https://pluralistic.net/2021/10/20/vizio-vs-the-world/#dumbcast
Malus's promise, then, is that you can pay them to create fully functional reimplementations of any free/open source software package that your company can treat as proprietary, without any obligations to the commons. You won't even have to attribute the original software project that you knocked off!
This is the risk that Nolan and his partner are trying to awaken the free/open source community to: that our commons is about to be raided by selfish monsters who serve as gut-flora for the immortal colony organisms we call "limited liability corporations," who will steal everything we've built and destroy the social contract we live by.
This is a real problem, but not because of AI. We
already
have this situation, and it's
really bad
. Most of the foundational free software projects were created under older licenses that did not contemplate cloud computing and software as a service. The "copyleft" obligations of these licenses are triggered by the
distribution
of the software – that is, when I send you a copy of the code.
But cloud services don't have to send you the code: when you run Adobe Creative Cloud or Google Docs, the most important code is all resident on corporate servers, and never sent to you, which means that you are not entitled to a copy of the new software that has been built atop of our commons. In other words, big companies have "software freedom" (the freedom to use, modify and improve software) and we've got "open source" (the impoverished right to look at the versions of these packages that are sitting on services like Github – itself a division of Microsoft):
https://mako.cc/copyrighteous/libreplanet-2018-keynote
Then there's "tivoization," a tactic for stealing from the commons that wasn't
quite
invented by Tivo, though they were one of its most notorious abusers. Tivoization happens when you distribute free software as part of a hardware device, then use "digital locks" (sometimes called "technical protection measures") to prevent the owner of this device from running a modified version of the code. With tivoization, I can sell you a device running free software and I can comply with the license by giving you the code, but if you change the code and try to get the device to run it, it will refuse. What's more, "anti-circumention" laws like Section 1201 of the US Digital Millennium Copyright Act make it a
felony
to tamper with these digital locks, so it becomes a
crime
to use modified software on your own device:
https://pluralistic.net/2026/03/16/whittle-a-webserver/#mere-ornaments
There's no question that the tech industry would devour the free software commons if they were allowed to, and the AI threat that Nolan raises with Malus seems alarming, but while there's
something
to worry about there, I think the risk is being substantially overstated.
That's because copyleft licenses – and indeed, all software licenses – are
copyright
licenses, and
software written by AI is not eligible for a copyright
, because
nothing made by AI is eligible for copyright
:
https://pluralistic.net/2026/03/03/its-a-trap-2/#inheres-at-the-moment-of-fixation
Copyright is awarded
solely
to works of
human
authorship. This fact has been repeatedly affirmed by the US Copyright Office, which has fought appeals of this principle all the way to the Supreme Court, which declined to hear the case. That's because the principle that copyright is strictly reserved for human creativity isn't remotely controversial in legal circles. This is just how copyright works.
Which means that the "be evil" version of Malus's business model has a fatal flaw. While the code that Malus produces is indeed "legally distinct" with "no attribution" and "no copyleft," it's not true that there are "no problems." That's because Malus's code doesn't have "corporate-friendly licensing." Far from it: Malus's code has
no
licensing, because it is born in the public domain and
cannot be copyrighted.
In other words, if you're a corporation hoping to use Malus to knock off a free software project so that you can adapt it and distribute it without having to make your modifications available, Malus's code will not suit your needs. If you give me code that Malus produced,
you can't stop me from doing anything I want with it
. I can sell it. I can give it away. I can make a competing product that reproduces all of your code and sell it at a 99% discount. There's nothing you can do to stop me, any more than you could stop me from giving away the text of a Shakespeare play you sold me. You can't stick a license agreement or terms of service between me and the product that binds me to
pretend
that your public domain software is copyrighted – that's
also
not allowed under copyright.
Does that mean that Malus is a meaningless stunt? No, because this automated reimplementation
does
create
some
risks to our software commons. A troll who doesn't care about selling software could clone every popular free software project and make public domain versions that would be confusing and maybe demoralizing. Combining these clean-room reimplementations with cloud software or tivoization could create hybrid forms of commons-enclosure that are more virulent than the current strains.
But reimplementation itself is
not a risk to free software
. Reimplementation is the
bedrock
of free software. GNU/Linux itself is a reimplementation of AT&T Unix. Free software authors re-implement each other's code all the time, often because they think the license the original code was released under sucks. Literally the coolest free software thing I've seen in the past 12 months included a reimplementation of Raspberry Pi's PIO module to escape from its bullshit patent encumbrances:
https://youtu.be/BbWWGkyIBGM?si=vO5zLH3OG5JLW7OP&amp;t=2253
Reimplementation is
good, actually
. And honestly, if corporations are foolish enough to reimplement their code using an LLM, and in so doing, create a vast
new
commons of public domain software, well, that's not exactly the freesoftwarepocalypse, is it?
(
Image:
Muhammad Mahdi Karim
,
GNU FDL
; modified
)
Hey look at this (
permalink
)
Object permanence (
permalink
)
#25yrsago PimpMySnack: homemade, gigantic versions of snack food
https://web.archive.org/web/20060421034050/http://www.pimpmysnack.com/gallery.php
#20yrsago Thieves discover abandoned Soviet missile silo full of cash
https://web.archive.org/web/20060411021047/http://www.mosnews.com/news/2006/03/07/moneyfound.shtml
#15yrsago Victorian house’s facade converted to a folding garage-door
https://web.archive.org/web/20110423213819/https://www.blog.beausoleil-architects.com/2011/03/architectural-magic.html
#15yrsago Xerox’s first successful copier burst into flame so often it came with a fire-extinguisher
https://en.wikipedia.org/wiki/Xerox_914
#15yrsago MPAA: “democratizing culture is not in our interest”
https://torrentfreak.com/mpaa-democratizing-culture-is-not-in-our-interest-110420/
#15yrsago Mail Rail: London’s long-lost underground postal railroad
https://web.archive.org/web/20110805130854/http://www.silentuk.com/?p=2792
#10yrsago Kindle Unlimited is being flooded with 3,000-page garbage books that suck money out of the system
https://web.archive.org/web/20160421055052/https://consumerist.com/2016/04/20/amazon-unintentionally-paying-scammers-to-hand-you-1000-pages-of-crap-you-dont-read/
#10yrsago America’s wealth gap has created an ever-increasing longevity gap
https://www.counterpunch.org/2016/04/21/the-death-gap/
#10yrsago Why is Congress so clueless about tech? Because they fired all their experts 20 years ago
https://www.wired.com/2016/04/office-technology-assessment-congress-clueless-tech-killed-tutor/
#10yrsago Why Internet voting is a terrible idea, explained in small words anyone can understand
https://www.youtube.com/watch?v=abQCqIbBBeM
#10yrsago VW offers to buy back 500K demon-haunted diesels
https://www.reuters.com/article/us-volkswagen-emissions-usa-idUSKCN0XH2CX/?feedType=RSS&amp;feedName=topNews
#10yrsago Printer ink wars may make private property the exclusive domain of corporations
https://www.eff.org/deeplinks/2016/04/eff-asks-supreme-court-overturn-dangerous-ruling-allowing-patent-owners-undermine
#5yrsago Some thoughts on GWB's call for truth in politics
https://pluralistic.net/2021/04/21/re-identification/#seriously-fuck-that-guy
#5yrsago What's wrong with EU's trustbusters
https://pluralistic.net/2021/04/21/re-identification/#eu-antitrust
#5yrsago Hawley and Taylor Greene faked their donor-surge
https://pluralistic.net/2021/04/21/re-identification/#jan-6-fraud
#5yrsago The Observatory of Anonymity
https://pluralistic.net/2021/04/21/re-identification/#pseudonymity
#1yrago Trump's FTC opens the floodgates for tariff profiteering
https://pluralistic.net/2025/04/21/trumpflation/#andrew-ferguson
Upcoming appearances (
permalink
)
San Francisco: 2026 Berkeley Spring Forum on M&A and the Boardroom, Apr 23
https://www.theberkeleyforum.com/#agenda
London: Resisting Big Tech Empires (LSBU), Apr 25
https://www.tickettailor.com/events/globaljusticenow/2042691
NYC: Enshittification at Commonweal Ventures, Apr 29
https://luma.com/ssgfvqz8
NYC: Techidemic with Sarah Jeong, Tochi Onyibuchi and Alia Dastagir (PEN World Voices), Apr 30
https://worldvoices.pen.org/event/techidemic/
Barcelona: Internet no tiene que ser un vertedero (Global Digital Rights Forum), May 13
https://encuentroderechosdigitales.com/en/
Berlin: Re:publica, May 18-20
https://re-publica.com/de/news/rp26-sprecher-cory-doctorow
Berlin: Enshittification at Otherland Books, May 19
https://www.otherland-berlin.de/de/event-details/cory-doctorow.html
Hay-on-Wye: HowTheLightGetsIn, May 22-25
https://howthelightgetsin.org/festivals/hay/big-ideas-2
SXSW London, Jun 2
https://www.sxswlondon.com/session/how-big-tech-broke-the-internet-b3c4a901
NYC: The Reverse Centaur's Guide to Life After AI (The Strand), Jun 24
https://www.strandbooks.com/cory-doctorow-the-reverse-centaur-s-guide-to-life-after-ai.html
Recent appearances (
permalink
)
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
"The Reverse-Centaur's Guide to AI," a short book about being a better AI critic, Farrar, Straus and Giroux, June 2026 (
https://us.macmillan.com/books/9780374621568/thereversecentaursguidetolifeafterai/
)
"Enshittification, Why Everything Suddenly Got Worse and What to Do About It" (the graphic novel), Firstsecond, 2026
"The Post-American Internet," a geopolitical sequel of sorts to
Enshittification
, Farrar, Straus and Giroux, 2027
"Unauthorized Bread": a middle-grades graphic novel adapted from my novella about refugees, toasters and DRM, FirstSecond, 2027
"The Memex Method," Farrar, Straus, Giroux, 2027
Today's top sources:
Currently writing: "The Post-American Internet," a sequel to "Enshittification," about the better world the rest of us get to have now that Trump has torched America. Third draft completed. Submitted to editor.
"The Reverse Centaur's Guide to AI," a short book for Farrar, Straus and Giroux about being an effective AI critic. LEGAL REVIEW AND COPYEDIT COMPLETE.
"The Post-American Internet," a short book about internet policy in the age of Trumpism. PLANNING.
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
Like this:
Like
Loading...
