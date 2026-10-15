---
title: "Pluralistic: Bundestrojaner (13 Oct 2026)"
url: "https://pluralistic.net/2026/10/13/petards-r-us/"
fetched_at: 2026-10-14T10:01:15.827504+00:00
source: "pluralistic.net"
tags: [blog, raw]
---

# Pluralistic: Bundestrojaner (13 Oct 2026)

Source: https://pluralistic.net/2026/10/13/petards-r-us/

Today's links
Bundestrojaner
: You can't make people more secure by making them less secure.
Hey look at this
: Delights to delectate.
Object permanence
: 9/11 sitcom; Jon Norman v Philcon; Bruce Sterling's post-9/11 geopolitics; Polaroid bankrupt; David Mamet x Shel Silverstein; "Great Big Beautiful Tomorrow"; Canadian government calls abortion doctors "terrorists"; Shanghai Ikea kicks out lonely, loitering seniors; Black Panther self-care.
Upcoming appearances
: Paris, Vancouver, Victoria, Ottawa, Vienna, Kilkenny, Oxford, Sheffield, Oxford, Montreal.
Recent appearances
: Where I've been.
Latest books
: You keep readin' em, I'll keep writin' 'em.
Upcoming books
: Like I said, I'll keep writin' 'em.
Colophon
: All the rest.
Every morning, I revisit my blog headlines from this date, going back 25 years, 20 years, 15 years, 10 years, 5 years, and one year. I publish the most interesting ones in a section of my newsletter that I call "object permanence," and I think it's the most useful part of my day.
"Object permanence," of course, is a reference to the stage in an infant's development when they acquire the ability to connect events in the past to events in the present, which is why it's the point at which babies cease to be amazed by peek-a-boo. I've been blogging for more than a quarter century, and these daily trawls through the things I considered important enough to share are an unexpectedly powerful way to connect the events of the past to the events of the present.
Take cybersecurity, subject that is filling today's headlines, primarily due to a spate of poorly understood (and criminally poorly explained) incidents in which AI companies' hacking tools broke into various servers on the internet, sometimes trashing them:
https://pluralistic.net/2026/09/12/god-in-the-box/#llms-are-fake
In my discussions of this subject, I've been at pains to tease apart two different aspects of these incidents: first, that it's wrong to speak of bots "going rogue" here (they're doing what they're designed to do); but second, that the alarming thing about these incidents is that they illustrate how deeply unserious our approach to information security has been, and remains.
This is important context, and context is what gives us the object permanence we need to both understand and address real problems, like the two related facts that a) our IT systems are poorly constructed and indifferently maintained; and b) the people who are supposed to be fixing this keep making it worse.
The worst culprits here are governments, though the private sector is also terrible (in truth, our cybersecurity nightmare is something of a private-public partnership from hell). Governments are deeply compromised when it comes to digital security because they have an irreconcilable conflict of interest: on the one hand, they want to defend their countries' administrative systems, firms and households from digital attacks. But on the other hand, they
really
want to be able to
launch
attacks on their adversaries, both foreign and domestic.
Worse: because governments don't know who those adversaries might be (or might become at some later date), the state security apparatuses of the world's governments keep insisting that
all
working computer security must be dismantled, so they can spy on all of us in order to figure out whom among us is a Bad Guy, and then "travel back in time" through each newly discovered "bad guy's" communications to identify their confederates and detail their nefarious plots.
This is an old, old,
old
fight. It was arguably the first policy fight of the digital era: the fight over whether we could have working encryption
at all
. Old hands call this era "the crypto wars" (from when "crypto" meant "cryptography"), when the NSA classed working encryption code as a "munition" and criminalized civilian access to it. That was a very hard-fought fight, and it was won decisively by the Electronic Frontier Foundation and our just-retired executive director Cindy Cohn, who, as a young lawyer, litigated the "Bernstein case" that established that code was a form of expressive speech protected by the First Amendment. If you're interested in learning more about this, you should read Cindy's newly published memoir,
Privacy's Defender
(all profits go to EFF):
https://mitpress.mit.edu/9780262051248/privacys-defender/
Before Cindy came on the scene, the crypto wars were being fought primarily by the "cypherpunks," a motley gang of computer security enthusiasts of many political stripes who were unified by their conviction that the most important aspect of security was
defensive
. The fact that the NSA wanted to be able to read the private messages and files of their adversaries (the "Four Horsemen of the Infocalypse": terrorists, drug traffickers, child pornographers and organized crime) must not be allowed to trump the fact that any encryption that the NSA could pierce could also be pierced by bad guys: corporate spies, state-sponsored spies, griefers, petty criminals, stalkers, identity thieves and other creeps.
This argument was so indisputable, it's a
tautology
: "You cannot make a computer user more secure by making their computers less secure." We don't know how to make a computer that only "good guys" can break into, but which "bad guys" bounce off of. Either we make computers more secure, or we don't.
We didn't.
In the decades since the crypto wars, governments have embarked upon an uninterrupted program to weaken the security of our computers, with catastrophic effect. The most spectacular example is unquestionably the spy agencies' doctrine called "NOBUS," which stands for "no one but us"; as in "No one but us is smart enough to find this bug, which means that we can withhold its discovery from the manufacturer, which will allow us to weaponize this bug and use it to attack our enemies. Because no one but us is smart enough to find this bug, none of those enemies will ever discover it, weaponize it, and use it to attack the people who pay our salaries, who expect us to keep them safe."
This turns out to be both catastrophically wrong and catastrophically dangerous. A series of leaks of computer vulnerabilities hoarded by both the NSA and CIA under NOBUS confirmed that these bugs were independently rediscovered by criminals and state actors at the rate of about 20% per year. Worse, though, is that these bugs don't need to be independently rediscovered, because the NSA and CIA both
leaked
them.
The highest-profile leak was an NSA-hoarded vulnerability in Windows they codenamed "Eternal Blue." Eternal Blue leaked in 2017, whereupon cybercriminals hybridized it with some otherwise undistinguished ransomware to create Wannacry, a devastating piece of malware that took down hospitals, banks and oil pipelines, as well as the entire city government of Baltimore
and
the British Library:
https://cdn.sanity.io/files/v5dwkion/production/99206a2d1e9f07b35712b78f7d75fbb09560c08d.pdf
But NOBUS isn't the only example of spy agencies making our computers less secure in the name of making us more secure. Perhaps the most egregious example of that are the Bundestrojaners, malicious software purchased by the German government, whose customs agents secretly installed it on the computers of unsuspecting people during border inspections. This "lawful interception" software was hugely invasive: it could grab your screen, plunder your hard drive, and install and execute software on your computer, all with the utmost stealth, intended to keep you from knowing it was installed and operating on your computer. But it wasn't merely invasive – it was insecure, so anyone (rival spies, criminals, stalkers) could scan the internet for infected computers and take them over:
https://www.ccc.de/en/updates/2011/staatstrojaner
You really couldn't ask for a more perfect example of the maxim that you can't make computer users more secure by making their computers
less
secure. Despite this, governments continue to demand the introduction of grave, universal secure vulnerabilities into our digital lives. Take "chat control," a proposal to force every device manufacturer to install software that continuously scans your devices for child sex abuse material (AKA "child porn"):
https://www.eff.org/deeplinks/2026/04/eu-parliament-blocks-mass-scanning-our-chats-whats-next
There are plenty of things wrong with this, starting with the fact that it requires your device to secretly grab and transmit sensitive images from your phone, which might include sensitive images of your kids that were requested by their doctors. This isn't a hypothetical: it's something that happened to a dad who subsequently lost his email, his login to every other account, his phone number, all of his files (including his tax records and his business data), and every photo he had ever taken of his family, without appeal, after Google automatically detected a photo he took of his son to send to the family pediatrician. Google also falsely accused this man of sexually abusing his child and sicced the SFPD on him:
https://pluralistic.net/2022/08/22/allopathic-risk/#snitches-get-stitches
But even if you're not worried about this, you should still have the object permanence to recall the lessons of NOBUS and the Bundestrojaner. We can't make computer users more secure by making their computers less secure, and it's hard to imagine something more insecure than a computer that you entrust with every sensitive detail of your life that is
designed
to run computer code in secret that you can neither inspect nor terminate (let alone delete).
Hardly a day goes by without some country demanding that your computer's security be weakened in the name of protecting you. For
years
, both Conservative and Labour UK governments have been steaming towards a total ban on working encryption in the name of catching bad guys:
https://pluralistic.net/2023/03/05/theyre-still-trying-to-ban-cryptography/
It's happening in Canada, too, where somehow "digital sovereignty" means "making every device used in Canada vulnerable to foreign spies so that our own spies can access our private communications":
https://www.eff.org/deeplinks/2026/05/canadas-bill-c-22-repackaged-version-last-years-surveillance-nightmare
Then there's the "age verification" laws proliferating all around the world. Remember, there's no such thing as "age verification," there's only "spying on everyone, all the time, to figure out who the kids are":
https://pluralistic.net/2026/06/23/destroy-the-village/#to-save-it
Age verification requires multiple entities to assemble vast corpuses of the kinds of sensitive identification papers that would allow identity thieves to destroy the finances and lives of everyone in the country, and (as foretold) every time it's tried, these files leak. Someday, this will lead to doxing whole
countries
:
https://arstechnica.com/tech-policy/2026/02/discord-faces-backlash-over-age-checks-after-data-breach-exposed-70000-ids/
Age verification is the latest and worst stage in governments' fraught relationship with private sector data-collection. The USA is the worst offender here: it is the largest, richest country in the world that has essentially
no
privacy protections. The last time the US updated its federal privacy law was in
1988
, when the Video Privacy Protection Act banned the disclosure of your VHS rentals. Tech companies spy on you for the same reason your dog licks its balls – because they can, and no one stops them:
https://pluralistic.net/2026/03/10/ice-tech/#foreseeable-outcomes
Which raises an obvious question:
why
hasn't Congress updated privacy law? And why hasn't the EU figured out how to force the US companies that pretend to be Irish to obey European privacy law? The answer is that governments
love
private sector data-collection, because it gives them a cheap, off-the-books source of warrantless access to information they aren't legally allowed to acquire:
https://pluralistic.net/2021/04/13/public-interest-pharma/#axciom
From Flock cameras to ICE's use of Google data in its ethnic cleansing campaign, the US government and the commercial surveillance industry have created a public-private partnership from hell, where governments refuse to block commercial spying and companies hand their commercial surveillance data over to governments in return.
From there, it was a short leap to governments
insisting
that the private sector gather our data. That's the right way to think about age verification, chat control, and other mandates for corporations to spy on us using our devices and our accounts: a government requirement for private-sector mass surveillance.
I have plenty of hostility to corporate overreach, but to have any hope of fighting that overreach, we need governments to be on
our
side. But for our governments, it comes to cybersecurity, we are the enemy, and spying corporations are our governments' allies.
Sometimes, that's utterly, literally true. Governments around the world are addicted to buying spyware from cyber-arms dealers, mostly headquartered in Israel and the UAE (with the odd Italian and British company for variety). These arms-dealers practice NOBUS-by-proxy, wherein they discover or pay bounties for bugs in widely used hardware, operating systems and applications and – rather than reporting them to the manufacturer – hoard them and weaponize them, and then sell the weapons to criminals, corporations, and our governments, who give them billions of our money to ensure that our computers have huge, glaring defects in them that leave us terribly vulnerable:
https://citizenlab.ca/focus-area/targeted-surveillance/
In a world where our governments' national security apparatuses were genuinely committed to our safety and security, they would criminally prosecute these companies, not make their owners into billionaires.
This is the context we should all be thinking about when it comes to these "rogue AI hacking agents." The IT systems that these irresponsibly deployed software products have trashed were
already
terrifyingly vulnerable…
by design
. Rather than fix these systems, our governmental "security" agencies have spent the past 40 years making them
less secure
, in order to make it easier for them to catch "bad guys," who now find it trivial to attack us through systems we are all totally reliant upon.
In every way, in every area of law, governments fail to take our security seriously. That even includes
copyright
law. All over the world, the US Trade Representative has ensured that every country has an "anti-circumvention" law that makes it a crime to reverse-engineer and modify software without permission:
https://pluralistic.net/2026/01/01/39c3/#the-new-coalition
From the very start, these have been a security nightmare. Remember the "Sony Rootkit?" Between 2005-2007, Sony-BMG Music distributed over 6m CDs that were deliberately infected with a piece of malicious software called a "rootkit" that was used to disable your computer's ability to rip (copy) music CDs.
The way this rootkit did so was depraved in its indifference to the security of Sony-BMG's customers: at the same time as Sony-BMG's malware installed its secret anti-ripping program, it also altered their computers' operating systems to make them incapable of detecting any program or file whose name started with $SYS$. Immediately, malicious software authors started adding $SYS$ to the start of all their filenames, and that malicious software was therefore undetectable to millions of users' computers. It was even invisible to anti-virus software. Worse: Sony-BMG's rootkit infected 200,000-300,000 US government and military networks:
https://www.schneier.com/blog/archives/2005/11/sonys_drm_rootk.html
Even worse: after the scandal broke, security researchers all over the world came forward to say that they'd discovered the Sony Rootkit months before it became common knowledge, but their lawyers had told them they weren't allowed to disclose its existence because doing so would fall afoul of anti-circumvention law. For months, this official, deliberate malware epidemic spread in secret because of anti-circumvention law.
It's been more than 20 years since the Sony Rootkit, and anti-circumvention law is now
worse
than it was in the oughts: now it applies to far more devices from far more vendors. Today, it's common for corporations to threaten their own customers with civil and criminal liability if they have the temerity to hire outside auditors to evaluate the software they entrust their businesses to for security defects. And oh God, it's even worse, because the worst offender is Oracle, who are now the de facto IT czars of America:
https://arstechnica.com/information-technology/2015/08/oracle-security-chief-to-customers-stop-checking-our-code-for-vulnerabilities/
I'm not saying that these are the only problems with our IT security. What I
am
saying is that the hacking bots everyone's freaking out about didn't appear out of nowhere. If you have just a little object permanence, you can see that they are the terminal stage of a pathology that governments have only ever worsened: by hoarding and weaponizing vulnerabilities; by paying others to hoard and weaponize vulnerabilities; by criminalizing security audits; by insisting that every computer we rely on be equipped with
deliberate
vulnerabilities in software we can't inspect, terminate or delete.
Yeah, there should be criminal and civil liability for OpenAI, Amazon, Anthropic and every other company whose bots "went rogue" and attacked servers. But that will do nothing to fix our IT.
The table-stakes for a secure digital world are: public agencies that try to make our computers as secure as possible, including by administering the corporate death-penalty to any company that hoards and weaponizes information about bugs in our computer. We should protect and reward individuals and firms who come forward with true disclosures about bugs in systems we rely upon. We should not give companies the right to silence and punish those critics who want to warn us about their defective products. And we should not
require
that companies make us less secure in the name of making it easier for spies and cops to catch the bad guys.
(
Image:
Pmk58
,
CC BY-SA 4.0
;
Wikipedian Prolific
,
CC BY-SA 3.0
; modified
)
Hey look at this (
permalink
)
Object permanence (
permalink
)
#25yrsago CBS sitcom about couple who meet in the WTC rubble
https://web.archive.org/web/20011014082646/http://dailynews.yahoo.com/h/eo/20011012/en/cbs_considers_wtc_comedy_1.html
#25yrsago Jon Norman not invited to Philcon
https://www.locusmag.com/2001/Departments/Letters10Norman.html
#25yrsago Bruce Sterling's post-9/11 geopolitics predictions
https://web.archive.org/web/20011102212150/https://www.edge.org/documents/whatnow/whatnow_sterling.html
#25yrsago Polaroid files Chapter 11
https://web.archive.org/web/20011107181428/http://www.polaroid.com/polinfo/press_releases/october01/101201a.html
#25yrsago David Mamet's tribute to Shel Silverstein
https://www.nytimes.com/2001/10/14/theater/theater-a-beloved-friend-who-lived-life-the-chicago-way.html
#15yrago Great Big Beautiful Tomorrow: a chapbook in PM Press’s Outspoken Authors series
https://craphound.com/category/gbbt/
#15yrsago Canadian government advice defines abortionists as terrorists
https://www.jezebel.com/canadian-government-lists-abortionists-as-terrorists-u-5849963
#10yrsago Ikea Shanghai to elderly, lonely Chinese people: buy something or get out
https://qz.com/806990/lonely-shanghai-seniors-now-have-to-buy-something-if-they-want-to-cruise-all-day-in-ikeas-cafeteria
#5yrsago Facebook shows mall ninja gear ads on insurrection articles
https://pluralistic.net/2021/01/14/10-point-program/#monetizing
#5yrsago The Black Panther self-care method
https://pluralistic.net/2021/01/14/10-point-program/#panthers
Upcoming appearances (
permalink
)
Paris: Slow Tech Summit, Oct 15
https://slowtechsummit.com/
Vancouver: Read, Resist, Repair, Rejoice (Vancouver Writers Festival), Oct 19
https://writersfest.bc.ca/festival-event-2026/01
Victoria: Munro's Books, Oct 20
https://www.munrobooks.com/events/6113620261020
Vancouver: Life After AI (Vancouver Writers Festival), Oct 22
https://writersfest.bc.ca/festival-event-2026/46
Ottawa: Life After AI (Ottawa Writers Festival), Oct 24
https://writersfestival.org/event/life-after-ai
Vienna: TED AI, Oct 28-30
https://tedai-vienna.ted.com/
Kilkenny (Kilkenomics), Nov 6-8
https://kilkenomics.com/
Vancouver: Enshittification (Sid Williams Theatre Society), Nov 10
https://www.sidwilliamstheatre.com/events/cory-doctorow-talks-enshittification/
Vancouver: BC Policy Solutions Gala, Nov 12
https://bcpolicy.ca/gala/
Oxford: Ministry of the Future, Nov 23
https://ministryforthefuture.co.uk/events.html
Sheffield: Reverse Centaur at Juno Books, Nov 25
https://www.outsavvy.com/event/40274/cory-doctorow-in-conversation
Oxford: Bennett Oxford Symposium on Open Code in Science, Dec 9
https://www.bennett.ox.ac.uk/events/2026-bennett-institute-symposium/
Montreal: World Science Fiction Convention, Sep 2-6
https://montreal2027.ca/en
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
“Once Is Enemy Action,” a science fiction novel about the origins of modern technofascism. Today's words: 574 (7730 total).
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
