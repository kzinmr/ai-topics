---
title: "Pluralistic: New York vs auto-enshittification (25 Nov 2026)"
url: "https://pluralistic.net/2026/11/25/empire-state-strikes-back/"
fetched_at: 2026-11-26T10:00:52.299837+00:00
source: "pluralistic.net"
tags: [blog, raw]
---

# Pluralistic: New York vs auto-enshittification (25 Nov 2026)

Source: https://pluralistic.net/2026/11/25/empire-state-strikes-back/

Today's links
New York vs auto-enshittification (
permalink
)
As of February 27, 2027, it will be illegal for companies in New York to charge car-owners a subscription fee or an upcharge for any software feature that runs on hardware already installed in their car. It's a bold – if imperfect – disenshittification gambit aimed at the
extremely
(and increasingly) enshittified automotive industry:
https://wgna.com/car-bill-extra-fees/
In a state of nature, there'd be no reason to pass a law like this. Say BMW decided to sell you a car that charged you a monthly subscription for the "feature" that auto-dipped your high-beams when there was an oncoming car (a thing BMW actually does):
https://www.autoevolution.com/news/netizens-up-in-arms-over-bmw-adaptive-headlight-subscription-237335.html
In a state of nature, BMW's sleazy scam would conjure forth competitors who would offer mechanics and drivers a one-click way to unlock the feature forever. Drivers would curse BMW and pay a one-time fee to get permanent access to the feature, and that would be the end of the matter. Indeed, the fact that this third-party fix
could
exist at all might well convince BMW not to bother with the high-beam scam in the first place (and if it didn't, well, then tinkerers, hackers, and entrepreneurs would swiftly obviate it).
But we don't live in a state of nature. We live in a world with a federal "anticircumvention" law: Section 1201 of the Digital Millennium Copyright Act (DMCA 1201), which imposes a 5-year sentence and a $500k fine for this kind of reverse engineering, even if it does not result in a copyright infringement.
There's no copyright law that says you can't change the software in your car to activate your high-beams' automatic controller, but that doesn't matter, because activating the controller without BMW's permission requires a reverse-engineering step and
that's
a felony.
Jay Freeman rightly calls this "felony contempt of business-model" because it lets companies send you to literal
prison
for doing otherwise legal things, just because it makes them unhappy.
What's more, copyright is a firmly federal matter: copyright law "pre-empts" the states, meaning that states can't pass laws that modify federal copyright policy. That means that states can't override DMCA 1201 by legalizing reverse-engineering for otherwise lawful purposes (such as independent repair, performing software upgrades, or allowing generic consumables and parts).
Anticircumvention is an attractive nuisance: it invites manufacturers to dream up as many scams as they can think of and then bury them in their products, secure in the knowledge that it is a literal felony to thwart their commercial plans. It's especially bad for cars, where anticircumvention is used:
to block third-party parts and independent repair;
to prevent drivers from preventing manufacturers, lenders and dealerships from spying on their driving habits, car informatics, and locations;
to enable lenders (and hackers who break into dealerships' computers) to immobilize your car without any notice, appeal or due process:
https://pluralistic.net/2023/07/24/rent-to-pwn/#kitt-is-a-demon
The New York State bill (S.9348A/A.10411A)
partially
addresses
some
of these unfair and deceptive practices:
https://www.nysenate.gov/legislation/bills/2025/S9348/amendment/A
Before I get into
what
this law does (and doesn't) do, I want to get into
how
it does anything at
all
. Remember: anticircumvention was shoehorned into copyright law, and copyright is a federal matter. Copyright enjoys pre-emption, a ban on states' modifying it.
At first blush, it
seems
like the states shouldn't be able to do anything about the enshittification that anticircumvention law enables. But the Right to Repair movement came up with a clever hack around pre-emption. States can't override federal copyright law, but state legislatures
can
regulate goods and services that are sold within their states. That means that states can simply
ban
the sale of goods that use anticircumvention to rip off or spy on the people who live within state limits.
This is the basis for several successful Right to Repair laws, starting in 2022 with Colorado's powered wheelchair repair law (HB22-1031, cosponsored by the very excellent Brianna Titone):
https://pluralistic.net/2022/06/08/chair-ish/#r2r
This law does not purport to limit which copyrights the private-equity-backed powered wheelchair duopoly can exercise. It just orders anyone selling powered wheelchairs in Colorado to take steps to enable independent repair such that these copyright issues (including anticircumvention) never arise.
This became the template for a slew of state repair bills, including Oregon's electronics repair law, which was later copy/pasted into Washington state law:
https://pirg.org/oregon/updates/governor-kotek-signs-the-right-to-repair-act-into-law/
A very similar law was passed in New York state, only to be gutted by Governor Kathy Hochul:
https://www.techdirt.com/2024/02/07/nys-right-to-repair-law-was-neutered-by-lobbyists-and-governor-hochul-after-passage-now-some-lawmakers-are-trying-to-fix-it/
Hochul will shortly get a chance to redeem herself, when A8405, a law that re-inserts all the provisions she stripped out of the original repair law, comes to her desk:
https://www.nysenate.gov/legislation/bills/2025/A8405
Perhaps Hochul
will
sign that law. After all, her press release about the new automotive bill sure makes it sound like she's anti-enshittification:
My message to car companies is clear: this kind of deceptive business model isn’t going to fly in New York State. Keep your hands out of New Yorkers’ wallets.
https://www.governor.ny.gov/news/money-your-pockets-governor-hochul-signs-bill-restricting-exploitative-vehicle-subscription
But the specifics of this new NY automotive bill matter, and they're a decidedly mixed bag. Let's start with the penalty for noncompliance: a dealer, automotive manufacturer or lender who violates the new law faces a whopping
$250
fine per violation. That means that if your dealer charges you $1,000 for a software upgrade and you later realize you've been ripped off, they'll only pay a penalty of $250.
In this case, a dealer who manages to fleece one driver for every three who know their rights and can figure out how to enforce them will still come out ahead – and
that's
only if you can get the dealer to refund your $1000, which might involve going to small claims court.
Then there's the carve-outs: this law does not cover subscription fees and software upsells for "navigation system updates, infotainment features, satellite radio, in-vehicle wi-fi, telematics services, roadside assistance, software-dependent driver assistance or driver automation features, or vehicle-connected services that rely on cellular or other data networks for continued operation."
This is a
huge
loophole. Take that last clause, "services that rely on cellular or other data networks for continued operation." This clause allows manufacturers to bypass the
entire
statute, merely by redesigning their subscription and software upsells to "rely on cellular or other data networks for continued operation." For example, the BMW feature that automatically dips your high-beams could "require" a daily check for new versions and then the company can claim that the feature relies "on cellular or other data networks for continued operation."
Sure, a judge might eventually find that "continued operation" doesn't mean a daily check for software updates, but only after the state AG or a class action lawyer forces the question, which could take years. Also: don't hold your breath waiting for the class action lawyer, because the car manufacturers can also make you click through a binding arbitration waiver when you first turn on your car and thus take away your right to join a class action:
https://pluralistic.net/2025/10/27/shit-shack/#binding-arbitration
Beyond this, there's the breadth of vague phrases like "driver automation features" (is automatically dipping your high-beams a "driver automation feature?" I could sure see a lawyer making that argument). Likewise "telematics" (a buzzword that might mean anything, nothing or everything).
On the other hand, there are some interesting ambiguities in this bill that I quite like. For example: if you live in New Jersey, but you happen to be in New York on the day Tesla bills you for subscribing to your whole battery (some Tesla models only let you use half your battery's charge unless you pay a monthly fee). Does that mean Tesla violated the law by charging a fee for a subscription feature for a car that is in the state of New York? That would be a fun one to see!
Like I said, this is only a partial fix for auto-enshittification. It won't stop your car from spying on you and ratting you out to your insurer:
https://pluralistic.net/2024/03/12/market-failure/#car-wars
It won't help you if the manufacturer goes bust and bricks your car:
https://pluralistic.net/2024/10/10/software-based-car/#based
It won't help you if Tesla hacks your odometer to sell a lie about the range you can expect from your charge:
https://pluralistic.net/2023/07/28/edison-not-tesla/#demon-haunted-world
This law would have had much more effect if it was better-drafted; on the other hand, maybe if it was drafted to capture a more meaningful slice of enshittificatory gambits, Hochul would have gutted it the way she did with the state's 2022 electronics repair bill.
Above all, though, we must remember: the only reason this bill exists
at all
is that Congress created DMCA 1201, the "felony contempt of business-model" law that lets companies conjure new crimes out of thin air and send you to prison for making their shareholders sad.
It's fantastic that the Repair Coalition came up with a loophole that lets states protect the American public from some of the worst effects of anticircumvention law, and it's cool that this tactic is being used to fight other kinds of enshittification.
But none of this should be necessary
at all
, and the real fix is for Congress to repeal Section 1201 of the Digital Millennium Copyright Act.
Hey look at this (
permalink
)
Object permanence (
permalink
)
#20yrsago Copyright Office creates 6 DMCA exemptions
https://web.archive.org/web/20061125140940/http://www.eff.org/deeplinks/archives/005021.php
#20yrsago PSP homebrewers develop DRM
https://web.archive.org/web/20061211005619/https://pspupdates.qj.net/Protect-your-homebrew-applications-with-DAS/pg/49/aid/73867
#15yrsago Why you shouldn’t parse HTML with regexp stackoverflow.com/questions/1732348/regex-match-open-tags-except-xhtml-self-contained-tags/1732454#1732454
#15yrsago European Court of Justice: spying with national copyright censorwalls is illegal
https://torrentfreak.com/european-court-isps-cant-spy-on-pirating-customers-111124/
#15yrsago Canadian indigenous band declares state of emergency due to horrific conditions, government takes no notice
https://www.huffpost.com/archive/ca/entry/what-if-they-declared-an-emergency-and-no-one-came_b_1104370#undefined
#10yrsago Russian social media erupts as Putin apparat tries to suppress video of booing crowd
https://www.bbc.co.uk/news/world-europe-15869047
#10yrsago Conservative Alberta politician changes sides over Trumpism, gets gendered death threats and slurs from the Tory base
https://calgaryherald.com/news/politics/braid-jansen-stuns-legislature-by-reading-out-explicit-anti-female-slurs
#5yrsago The Tesla-financial complex
https://pluralistic.net/2021/11/24/no-puedo-pagar-no-pagara/#Rat
#5yrsago Spaniards fight Wall Street landlords
https://pluralistic.net/2021/11/24/no-puedo-pagar-no-pagara/#fuckin-aardvarks
#1yrago Cooking in Maximum Security
https://pluralistic.net/2025/11/24/moca-moka/#culinary-apollo-13
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
Currently writing:
“Once Is Enemy Action,” a science fiction novel about the origins of modern technofascism. Today's words: 502 (39670 total).
"The Post-American Internet," a sequel to "Enshittification," about the better world the rest of us get to have now that Trump has torched America. Fourth draft completed. Submitted to editor.
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
