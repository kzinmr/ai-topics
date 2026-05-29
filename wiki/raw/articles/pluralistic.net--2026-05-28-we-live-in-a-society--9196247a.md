---
title: "Pluralistic: Hold on for dear life (28 May 2026)"
url: "https://pluralistic.net/2026/05/28/we-live-in-a-society/"
fetched_at: 2026-05-29T07:01:25.180481+00:00
source: "pluralistic.net"
tags: [blog, raw]
---

# Pluralistic: Hold on for dear life (28 May 2026)

Source: https://pluralistic.net/2026/05/28/we-live-in-a-society/

Today's links
Hold on for dear life
: Not your keys, not your wallet, entirely your problem.
Hey look at this
: Delights to delectate.
Object permanence
: Who owns "Web 2.0"; EFF saves bloggers' sources; Non-porn porn; Redaction fails; Canadian Tories say markets, not government, will help flood victims; Forced gold-farming; Walkaway cover; Oracle eats shit in Java API case; Captain America was a Nazi spy; Who Broke the Internet? (Pt IV).
Upcoming appearances
: London, Kansas City, LA, Menlo Park, Toronto, NYC, Edinburgh.
Recent appearances
: Where I've been.
Latest books
: You keep readin' em, I'll keep writin' 'em.
Upcoming books
: Like I said, I'll keep writin' 'em.
Colophon
: All the rest.
Hold on for dear life (
permalink
)
From the earliest days of technopolitics, the role of technology in resisting authoritarianism was unclear. On the one hand, there's the indisputable fact that modern cryptography, properly implemented, can deliver a degree of privacy that is proof against all technological attacks.
That is to say, if you pull out your distraction rectangle, fire up the camera, and tap the shutter button, in the ensuing eyeblink instant the image you've captured will be scrambled so thoroughly that it could never be unscrambled without the secret key unlocked by your passphrase or biometrics. Even if every hydrogen atom in the universe were converted into a computer, and even if all those computers spent all the time between now and the end of the universe trying to guess what the key was, we would run out of universe and time long before we ran out of possible keys.
What's more, this extremely robust form of scrambling and descrambling can be combined with other techniques to block tampering with the encrypted data, and to allow parties to reliably identify who scrambled the data and also to restrict who may
unscramble
it. These remarkable technological facts have inspired many excited debates about what they mean for our politics, most notably among a group of people who called themselves "cypherpunks":
https://web.archive.org/web/20151102012232/https://www.wired.com/1993/02/crypto-rebels/
One cypherpunk faction believed that modern cryptography could enable a kind of technological secession: by allowing ordinary people to communicate, transact and collaborate without the possibility of state interception or control, crypto could make states themselves obsolete.
But another faction pointed out that no amount of mathematics could help you if an agent of the state – or a criminal the state failed to protect you from – tortured you until you revealed the secret passphrase needed to unlock your secrets. This was (ironically) called "rubber hose cryptanalysis" (as in "Tell me your passphrase or I'll hit you with this rubber hose again"). Later, this became known as a "wrench attack" after a famous XKCD comic about $1m worth of security technology being defeated by hitting someone with a $5 wrench until they divulged the password:
https://xkcd.com/538/
Once you stipulate to the problem of wrench attacks and rubber-hose cryptanalysis, it becomes apparent that your cryptography is only as good as your physical defenses. What's more, the most effective physical defenses we have come from a strong rule of law, because even the thickest safe door benefits from the threat of prison for anyone who breaks into the safe, and the most effective tool for preventing a cop from hitting you with a rubber hose is the existence of a judge who can send that cop to prison for abusing your civil rights.
But what do you do if you already live under tyranny? The rule of law is a great defense, but cryptography alone can't bring about the rule of law. What is the role of technology in this foundational struggle?
My technopolitics faction – the faction associated with the Electronic Frontier Foundation, where I've worked for a quarter-century – has an answer: the role of encryption is to provide a measure of privacy and security that is best used to organize
political
struggles to demand the rule of law and respect for human rights. Encryption isn't proof against rubber hoses, but it
is
effective against many other forms of state repression, and it can provide a
technical
edge for those engaged in a
political
struggle.
Another faction – the faction most associated with bitcoin and subsequent cryptocurrency projects – rejects the role of the state altogether, and seeks to replace states (and state-regulated institutions like courts and banks) with mathematics. Rather than asking courts to interpret contracts, we can put our trust in self-executing "smart contracts," and rather than asking banks to safeguard our financial integrity, we can use cryptographic software to ensure that money only moves when the person it belongs to tells it to.
This has many problems. Smart contracts are slow, expensive, and unreliable. The number of people who understand contracts is small, the number of people who understand the software that embodies smart contracts is likewise small, and the Venn intersection of the two is more of a sphincter. What's more, there is irreducible ambiguity in all but the simplest of contracts, which means that even a "self-executing" contract ends up relying on a human adjudicator (an "oracle") who can be bribed or intimidated into cheating:
https://pluralistic.net/2022/02/14/externalities/#dshr
And when it comes to transactions, crypto proves to be unwieldy, expensive and complex, so that nearly all crypto users end up directing an intermediary (like Coinbase) to hold and move their cryptographic assets for them. The upshot is that cryptocurrency mostly replaces banks – imperfect, but heavily regulated and insured – with unregulated tech platforms with murky ownership and often defective security procedures, who may or may not be insured (or even locatable) in the event of a collapse or a breach. Consequently, cryptocurrency has become a scam magnet of unprecedented and unstoppable power, and hardly a day goes by without people being ripped off in the most ghastly ways imaginable:
https://www.web3isgoinggreat.com/
For bitcoin maxis and other anti-state cypherpunks, this is just a skill issue. Anyone who doesn't understand how to manage their own keys and turns to a platform to hold and move their crypto is getting what they deserve. As the maxim goes, "Not your keys, not your wallet," which is cypherpunkspeak for "caveat emptor."
That's where the wrench attacks come in. Because if you are in possession of keys that can be used to irreversibly and instantaneously steal large sums of money and move it to jurisdictions where the perpetrators are beyond any legal or physical recourse (e.g. North Korea), then there is a massive incentive for your adversaries to kidnap you and hit you with a wrench or a rubber hose.
That's precisely what's going on. People with substantial cryptocurrency holdings face grave personal danger, and the physical attacks on their person grow bolder, more violent, and more sadistic by the day:
https://github.com/jlopp/physical-bitcoin-attacks/blob/master/README.md
As crypto critic David Rosenthal writes, this problem is even worse than it seems at first blush:
https://blog.dshr.org/2026/05/wrench-attacks.html
For one thing, cryptocurrencies depend on "public ledgers" that indelibly, publicly record every transaction in the network. Cryptocurrency is nothing without these ledgers, and they
have
to be immutable and public to work. This is very bad news for anyone who relies on anonymity as their defense against physical attacks.
That's because "reidentification attacks" (where an anonymous person in a dataset is positively identified) get easier to perform over time. You might be represented in a database of hospital prescribing activities by a random number, and that number might be hard to associate with your real identity…at first. But with every subsequent release of data – whether in the form of an anonymized data-set or a breach – it gets easier to cross-reference the facts associated with your record with other facts from other records, such that a detailed, identifying picture of you emerges one fact at a time.
For example, if the taxi company you use suffers a breach that reveals journeys associated with every doctor's appointment at the hospital, now an attacker can pick out the home or work address of the single person who visited the hospital just before you received your prescription. The longer an "anonymized" data-set sits around in public view, the easier it gets to de-anonymize it:
https://www.nature.com/articles/s41467-019-10933-3
Combine the fact that permanent ledgers make it progressively easier to identify people whom you can torture into revealing their crypto keys with the irreversible, instantaneous nature of crypto transfers and you get some very juicy targets indeed. "Not your keys, not your wallet" means it's "not anyone else's problem" when you get robbed. You can't ask the bank to interdict or reverse the transaction.
Rosenthal provides a litany of the escalating security measures crypto holders are turning to as this problem goes progressively more dangerous and terrifying. There's the guy who splits his keys up in four physical vaults at four separate locations, whose management is instructed to make him wait a minimum of seven days when he asks to retrieve them. Despite all this, he keeps his identity secret:
https://www.bloomberg.com/news/articles/2026-05-19/crypto-conferences-up-security-after-attacks-scams
Rosenthal quotes Nicholas Weaver, who asks what kind of "internet of money" bitcoin can be if it can't be safely stored on a computer connected to the actual internet:
https://doi.org/10.1145/3208095
But an equally valid question is, what kind of escape from tyranny is it that requires you to hide your identity at all times lest you be snatched off the street and brutally tortured? What kind of "liberty" requires you to spend $860,000 armoring your two top execs' personal vehicles to protect them from gunfire and light artillery?
https://www.ft.com/content/71d7486d-89b5-48ac-8f94-857578c0a03b
It costs $6.2m/year to protect Coinbase's CEO – "more than the combined amount that JPMorgan Chase & Co., Goldman Sachs Group Inc. and Nvidia Corp. spent on their respective CEOs":
https://www.bloomberg.com/news/articles/2025-05-18/crypto-high-rollers-go-big-on-bodyguards-to-deter-kidnappers
Crypto true believers exhort one another to "HODL" (hold on for dear life). Selling your crypto during downturns is considered a moral failing. But now, crypto holders – especially those who manage their own keys – are
literally
holding on for dear life, as they are hunted by crime syndicates and state actors alike.
It's a good reminder of how badly crypto has failed on its own terms, delivering its biggest users into an existence of fear and physical peril that rivals the plight of even the most hunted dissidents in the most repressive societies. Worse: as cryptocurrency lobbyists have fused crypto with the world's largest and most corrupt governments (especially the Trump regime), crypto now has all the exposure to state coercion that made banks so unsuitable, but without the (inconstant, insufficient) protections offered by traditional banking.
And that's before we talk about the energy consumption problems, the scams enabled by crypto, and the rampant human trafficking that those scams necessitate:
https://www.pbs.org/newshour/show/how-human-trafficking-victims-are-forced-to-run-pig-butchering-investment-scams
People in my technopolitical faction have a saying of our own: "'Crypto' means
cryptography
." Cryptography plays a hugely important role in protecting people from crime and state repression. It is no substitute for the rule of law and democracy, but it remains a key tool for securing and defending both:
https://pluralistic.net/2022/03/27/the-best-defense-against-rubber-hose-cryptanalysis/
Cryptocurrency, on the other hand? That's the worst of all worlds.
Hey look at this (
permalink
)
Object permanence (
permalink
)
#20yrsago Can anyone own “Web 2.0?”
https://memex.craphound.com/2006/05/26/can-anyone-own-web-2-0/
#20yrsago iRiver gives customers the choice of switching off DRM
https://web.archive.org/web/20060619150812/http://www.iriver.com/mtp/
#20yrsago EFF scores win against Apple: bloggers’ sources are protected
https://web.archive.org/web/20060602020337/http://blog.wired.com/27BStroke6/index.blog?entry_id=1489151
#15yrsago Anonymous pre-paid credit-cards and money-laundering
https://web.archive.org/web/20110529001021/https://www.forbes.com/feeds/ap/2011/05/23/technology-lt-fea-plastic-money-laundering_8481416.html
#15yrsago More incompetence revealed on the part of France’s “three-strikes” copyright enforcer
https://web.archive.org/web/20120520073256/https://arstechnica.com/tech-policy/2011/05/french-three-strikes-anti-piracy-software-riddled-with-flaws/
#15yrsago Montage: Non-pornographic scenes from pornographic movies
https://www.youtube.com/watch?v=DVBhVDXLpaI
#15yrsago Improper court record redaction: a study
https://blog.citp.princeton.edu/2011/05/25/studying-frequency-redaction-failures-pacer/
#15yrsago Texas anti-TSA-grope bill killed by threat to shut down all Texas airports
https://www.texastribune.org/2011/05/24/fed-threat-shuts-down-tsa-groping-bill-in-texas/?r
#15yrsago Canadian Tories refuse to send soldiers to help flood victims because they’d compete with the private sector
https://web.archive.org/web/20110527053822/https://www.theglobeandmail.com/news/national/quebec/ottawa-initially-refuses-request-for-more-troops-to-aid-quebec-flood-victims/article2033562/
#15yrsago Gold-farming in a Chinese forced-labor camp
https://www.theguardian.com/world/2011/may/25/china-prisoners-internet-gaming-scam
#10yrsago Edward Snowden performs radical surgery on a phone to make it “go black”
https://web.archive.org/web/20160527125043/https://www.wired.com/2016/05/snowden-vice-cell-phone-hack/
#10yrsago FBI is investigating copyright trolls Prenda Law for fraud
https://web.archive.org/web/20160526005012/https://popehat.com/2016/05/25/fbi-actively-investigating-prenda-law-team-for-fraud/
#10yrsago How a pharma company made billions off mass murder by faking the science on Oxycontin
https://web.archive.org/web/20160524112437/http://static.latimes.com/oxycontin-part1/
#10yrsago GOP officials won’t let the FEC stop bosses from forcing employees to give to PACs
https://web.archive.org/web/20160526114245/https://prospect.org/blog/checks/fec-deadlocks-over-employer-political-coercion
#10yrsago Undetectable proof-of-concept chip poisoning uses analog circuits to escalate privilege
https://www.ieee-security.org/TC/SP2016/papers/0824a018.pdf
#10yrsago “Pickup artist” douche uses copyright to sue Youtube critics, fans raise $100K defense fund
https://www.gofundme.com/f/h3h3defensefund
#10yrsago The best thing you will read about the revelation that Captain America was a Nazi spy
https://web.archive.org/web/20160623131614/https://storify.com/rahaeli/captain-america
#10yrsago Revealed: the amazing cover for Walkaway, my first adult novel since 2009
https://reactormag.com/cover-reveal-walkaway-cory-doctorow//
#10yrsago Tor Project is working on a web-wide random number generator
https://blog.torproject.org/mission-montreal-building-next-generation-onion-services/
#10yrsago Jury hands Oracle its ass, says Google doesn’t owe it a penny for Java
https://www.eff.org/deeplinks/2016/05/eff-applauds-jury-verdict-favor-fair-use-oracle-v-google
#10yrsago Arcade cabinet enthusiasts discover trove of 50+ games in ship, derelict for 30 years
https://arcadeblogger.com/2016/05/06/arcade-raid-the-duke-of-lancaster-ship/
#5yrsago Monopolists are winning the repair wars
https://pluralistic.net/2021/05/26/nixing-the-fix/#r2r
#1yrago Who Broke the Internet, Part IV
https://pluralistic.net/2025/05/26/babyish-radical-extremists/#cancon
Upcoming appearances (
permalink
)
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
"Unauthorized Bread": a middle-grades graphic novel adapted from my novella about refugees, toasters and DRM, FirstSecond, April 20, 2027
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
