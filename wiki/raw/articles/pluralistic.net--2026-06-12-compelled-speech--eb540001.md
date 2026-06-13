---
title: "Pluralistic: Google’s new remote attestation scheme is every bit as terrible as its old remote attestation scheme (12 Jun 2026)"
url: "https://pluralistic.net/2026/06/12/compelled-speech/"
fetched_at: 2026-06-13T07:00:50.882028+00:00
source: "pluralistic.net"
tags: [blog, raw]
---

# Pluralistic: Google’s new remote attestation scheme is every bit as terrible as its old remote attestation scheme (12 Jun 2026)

Source: https://pluralistic.net/2026/06/12/compelled-speech/

Today's links
Google's new remote attestation scheme is every bit as terrible as its old remote attestation scheme (
permalink
)
Long before "agentic AI," we had the idea that software would act as your agent on the internet. That's why the old-fashioned technical term for a browser is a "user agent." Your browser acts on your behalf to retrieve information and then show it to you, in the format you choose. It's your agent:
https://pluralistic.net/2024/05/07/treacherous-computing/#rewilding-the-internet
This is a powerful and profound idea. It is because browsers are our "agents" that we expect them to accept our directives, say, by blocking pop-ups, or by turning off autoplay sound, or by blocking commercial surveillance trackers:
https://privacybadger.org/
Your browser does all that because your browser works for
you
. The reason your browser
can
work for you is that the web is an open, standardized technology. In theory, anyone who follows the standards published by the World Wide Web Consortium (W3C) can make a browser, and that web browser can connect to
any
web server. Browsers and servers are
interoperable
. It's the same force that means you can put anyone's gas in your gas-tank, or anyone's shoelaces in your shoes, or anyone's milk on your cereal.
But what if manufacturers could dictate those choices to you? What if your light socket refused to use a lightbulb unless it was officially blessed by the socket's manufacturer? What if your dishwasher refused to wash your dishes unless you bought them from one of the manufacturer's "dish partners"? What if your toaster refused to toast "unauthorized bread"?
https://arstechnica.com/gaming/2020/01/unauthorized-bread-a-near-future-tale-of-refugees-and-sinister-iot-appliances/
It's hard to see how a company could win its market with this strategy. After all, if the dishes are really better than the competition's, you'd buy them voluntarily, without any need for law or technology to force the matter. The only reason to make a dishwasher that refuses a rival's dishes is if the manufacturer's own dishes are ugly, expensive, and/or badly made.
But once a company owns the market – once they've achieved dominance by buying out their rivals; by bribing potential competitors to stay out of their lane; and by engaging in deceptive conduct to trap key suppliers and customers – they could cement their dominance by blocking interoperability, keeping out rival dishes, milk, gas, lightbulbs, shoelaces and bread, capturing their whole market and
squeezing
it.
That's what Google has done, and that's what Google wants to do more of. Google's commercial behavior has been so unethical, deceptive and abusive that the company just lost
three
federal antitrust cases:
https://www.bigtechontrial.com/p/google-loses-the-adtech-monopolization
This thrice-convicted monopolist bribed Apple – more than $20b/year – to stay out of the search market:
https://www.eff.org/deeplinks/2025/02/how-do-you-solve-problem-google-search-courts-must-enable-competition-while
They cheated app vendors, ripping them off with sky-high junk fees and onerous conditions that raised prices while lowering the share of your spending that went to the companies whose products you were paying for:
https://www.thebignewsletter.com/p/boom-google-loses-antitrust-case
They cheated advertisers, rigging the ad market to gouge businesses on ad prices and underinvesting to fight rampant ad-fraud, sucking hundreds of billions out of the productive economy for overpriced ads that no one saw:
https://www.justice.gov/opa/pr/department-justice-prevails-landmark-antitrust-case-against-google
Google wasn't always this way. The "don't be evil" company owes its very existence to the open web ecosystem. When the company started to index the web in 1998, it was playing on an open field, where any web server could talk to any "user agent," even one whose user was a startup like Google, that was making a copy of every page on the server.
For years, Google thrived on the open web, and built open technologies. Android – the mobile operating system that Google bought in 2005 – was presented as an "open" alternative to existing mobile offerings, and as the mobile market collapsed into two companies – Google and Apple – Google always presented Android as the open alternative to Apple's "walled garden."
There were always ways in which Google's "open" Android wasn't
exactly
open. The company engaged in illegal "tying" arrangements that forced hardware vendors and carriers to lock out versions of Android that were created by Google's competitors:
https://ec.europa.eu/commission/presscorner/detail/en/ip_18_4581
In other words, even though Google offered a mobile platform that was (mostly)
technically
open, they used
commercial
and
legal
strategies to choke off the market oxygen for alternative Android versions that tried to capitalize on that technical openness.
But life finds a way. The existence of an open, modifiable, tinkerer-friendly mobile operating system meant Android hackers could create alternatives to Google's (de facto) walled garden, which thrived in the cracks in that garden wall. Operating systems like CalyxOS, PureOS and Graphene offered a more private, more secure Android experience, one that was largely "de-Googled," blocking Google's relentless acquisition of your private data:
https://grapheneos.org/
And Google's data-hunger is
relentless
. Android exfiltrates a chunk of your personal and behavioral data
every five minutes
. The "resting heartbeat" of Android surveillance pulses and pulses, irrespective of whether you're using your device, and the instant you unlock your screen, that heartbeat quickens, sending even more data to the company:
https://digitalcontentnext.org/blog/2018/08/21/google-data-collection-research/
All that data has proved irresistible to authoritarian governments. Donald Trump's enforcers have seized on Google data as a vital source of information about the identity of protesters and the location of migrants hunted by ICE:
https://www.eff.org/deeplinks/2026/04/google-broke-its-promise-me-now-ice-has-my-data
So there are plenty of reasons why users would seek out these de-Googled alternatives to Android, finding them in spite of Google's illegal commercial tactics to block access to competing technologies. The worse it got, the better those alternatives looked.
Perhaps this explains Google's years-long effort to increase the
technical
barriers to using modified versions of Android, beefing these up to match the commercial restrictions that stand in the way of a de-Googled existence.
Back in 2023, Google floated the idea of "Web Environment Integrity" (WEI), a set of modifications to web standards that would force your computer to disclose its operating environment to the web servers it connected to,
even if you objected to this disclosure
:
https://pluralistic.net/2023/08/02/self-incrimination/#wei-bai-bai
WEI was a form of "remote attestation." That's when your device uses a sub-processor (sometimes called a "Technical Protection Module" or "TPM") or a walled off part of its main processor (sometimes called a "secure enclave") to produce a cryptographically signed description of your device and its configuration: which hardware, software, plug-ins and settings you're running.
When you connect to a server, it demands that your device send this "attestation" before it handles your request. If your device won't provide this data, or if the server doesn't like (or recognize) your device and its details, it can refuse to deal with you. And because the attestation is prepared by a TPM or a secure enclave that you can't modify or override, you don't get to decide which facts about your device it's allowed to see.
Practically speaking, this means that remote attestation lets a server refuse to deal with you until you turn off your ad-blocker and your tracker-blocker. It means that the server can discriminate against users who block auto-play sound and video, who block pop-ups, who put the tab in the background when it's playing a mandatory pre-roll ad.
WEI was especially disturbing in light of Google's efforts to kill ad-blockers and privacy blockers through updates to Chrome, an effort that continues to this day:
https://protonprivacy.substack.com/p/google-is-finally-killing-ublock
These blockers are an important part of the dynamic between web publishers and their users. In the real world, when you get an offer, you can make a
counter-offer
. That's all an ad-blocker is: a way for users to respond to a server whose opening bid is, "How about you give me all your data and let me take over your computer in exchange for showing you this page?" with "How about 'Nah?'"
https://www.eff.org/deeplinks/2019/07/adblocking-how-about-nah
We didn't get rid of pop-up ads by making them illegal, or by boycotting advertisers who used them. We got rid of pop-up ads when web users installed pop-up blockers, which made pop-up ads pointless. Take away our ability to block obnoxious digital content and you
guarantee
that we will be flooded with it.
These kinds of modifications aren't just used to block ads – they're also key to accessibility. People who have photosensitive epilepsy or who (like me) suffer from low-contrast vision problems use add-ons to reformat pages so that we can safely and legibly access them.
WEI's creators said they were only trying to put the web on a level playing field with apps, which routinely rat you out to the companies you connect to. Apps are a source of bottomless enshittification, not least because (unlike the web), they enjoy special, dangerous legal protections that make it
very
legally risky to modify them:
https://pluralistic.net/2025/07/31/unsatisfying-answers/#systemic-problems
WEI wasn't an effort to level the playing field between apps and the web – it was
a race to the bottom
, an attempt to make the web as enshittogenic as the app hellscape.
Public outrage to WEI killed the project, but Google's commitment to augmenting its illegal commercial lockdown efforts with
technical
lockdowns never ended. Now, Google has rolled out an experimental "reCAPTCHA Mobile Verification" that uses an app, your camera, and your device's TPM or secure enclave to produce an attestation about your Android device:
https://support.google.com/recaptcha/answer/16609652
This will make it much easier for the apps and other services you interact with to block your device if you run an Android alternative, or if you install a mod that overrides the actions of Google's stock Android:
https://www.reddit.com/r/PrivacySecurityOSINT/comments/1tbdjbj/privacy_concerns_around_googles_recaptcha_mobile/
This is a terrible idea – it's every bit as bad as WEI was. In an age in which Big Tech is ever-more tied to authoritarian governments, redesigning our devices to tell strangers things we don't want them to know isn't just shortsighted, it's inexcusable.
Hey look at this (
permalink
)
Object permanence (
permalink
)
#20yrsago Images from anti-DRM protest at the San Fran Apple Store
https://www.flickr.com/photos/quinn/tags/drmprotest/
#15yrsago Reasons people were arrested at the Toronto G20
https://memex.craphound.com/2011/06/11/reasons-people-were-arrested-at-the-toronto-g20/
#15yrsago Paul Krugman: Rule by rentiers favors billionaires, Chinese bond-holders over jobs and homeowners
https://www.nytimes.com/2011/06/10/opinion/10krugman.html?_r=1
#15yrsago Ontario publicly funded Catholic school bans rainbows, appropriates student donations for LGBT cause and gives them to Catholic charity
https://web.archive.org/web/20110610125236/https://www.xtra.ca/public/Toronto/Rainbows_banned_at_Mississauga_Catholic_school-10262.aspx
#10yrsago How to be less wrong about the First Amendment
https://web.archive.org/web/20160611221927/https://popehat.com/2016/06/11/hello-youve-been-referred-here-because-youre-wrong-about-the-first-amendment/
#10yrsago Mounties used Stingrays to secretly surveil millions of Canadians for years
https://web.archive.org/web/20160610182607/https://motherboard.vice.com/read/the-rcmp-surveilled-thousands-of-innocent-canadians-for-a-decade
#5yrsago Privacy Without Monopoly, EU edition
https://pluralistic.net/2021/06/11/technological-self-determination/#dma
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
