---
title: "Pluralistic: Adversarial interoperability is a team sport (21 Oct 2026)"
url: "https://pluralistic.net/2026/10/21/brittle-individualism/"
fetched_at: 2026-10-22T10:01:03.653432+00:00
source: "pluralistic.net"
tags: [blog, raw]
---

# Pluralistic: Adversarial interoperability is a team sport (21 Oct 2026)

Source: https://pluralistic.net/2026/10/21/brittle-individualism/

Today's links
Adversarial interoperability is a team sport
: Vibe-coded jailbreaks are fun, but don't solve the problem.
Hey look at this
: Delights to delectate.
Object permanence
: Labour Whip's pro-Iraq war threats; LoC's emulators; Kevin Mitnick plays CIA stooge; ICE: "The warrant is coming out of my balls"; WIPO's secret trademark meeting; Linking isn't libel (in Canada); Make: singing busts; Tory minister kills Turing's Law; Trump hotels rebrand as "Scion".
Upcoming appearances
: Vancouver, Ottawa, Vienna, Kilkenny, Courtenay, Vancouver, Oxford, Sheffield, Virtual, Oxford, Montreal.
Recent appearances
: Where I've been.
Latest books
: You keep readin' em, I'll keep writin' 'em.
Upcoming books
: Like I said, I'll keep writin' 'em.
Colophon
: All the rest.
Adversarial interoperability is a team sport (
permalink
)
Enshittification is particularly galling because (in theory, at least), digital technology should be
really
hard to enshittify.
That's because the only digital computer we know how to build is the "Turing-complete, universal von Neumann machine," which is to say, a calculating engine capable of computing every valid program. In some deep, important, foundational sense, every computer is the same as every other computer. Sure, they vary in terms of speed, storage and RAM, but given enough time and electricity, every computer can run every program.
This has profound implications for enshittification. Say a tech boss takes away a feature you value (as when Sonos pushed an update that removed nearly all the functionality from its "smart" speakers), or adds a feature you hate (like when Chamberlain blocked third-party apps from controlling its garage doors so it could force its customers to view
seven ads
before they could open or close their garages). At that point, a programmer can write an "interoperable" program that restores the good feature or blocks the bad one.
This program can be costlessly and instantaneously distributed to every affected technology user, and those users will likely pay something for it. After all, enshittification is a way to shift value away from technology users to tech companies, which makes the case for you paying for disenshittification technology that wrestles that value back.
All of that means that, in a state of nature, companies that are contemplating enshittification need to worry that their greed will tempt new companies to enter the market and poach their customers and suppliers. This alone might be enough to frighten companies off from enshittificatory gambits, and if companies press ahead regardless, then they open market opportunities for better companies that can costlessly, instantaneously usurp the original manufacturer's relationship with their entire affected customer base.
That's how it
should
work. But in 1998, Bill Clinton signed the Digital Millennium Copyright Act, and Section 1201 of the DMCA establishes a felony (punishable by a five-year prison sentence and a $500,000 fine) for reverse-engineering and modifying technology without the manufacturer's permission. Then, the US Trade Rep spent the next 25 years making sure that every US trading partner had an identical (or even worse!) "anticircumvention" law:
https://pluralistic.net/2025/05/26/babyish-radical-extremists/#cancon
The result is a grotesquely asymmetrical digital world, in which companies are free to use the flexibility of digital computers to downgrade or brick your digital devices, but where you commit a crime if you avail yourself of a countermeasure to get more out of something you own. This is the core technological factor at play in enshittification.
Enter AI. Thanks to vibe-coding, everyday people are rolling their own software for their devices
and
building the tools to shatter the digital locks that manufacturers use to block disenshittification. An excellent article by 404 Media's Jason Koebler runs down some of these hacks, including drop-in replacements for smart TV software that blocks the endless ads and surveillance that have made TVs all but unusable:
https://www.404media.co/reverse-engineer-anything-is-the-new-wild-west-of-ai/
These AI tools mix several techniques to disenshittify users' devices. One major component is automating the installation of existing alternative firmware for these devices that have been (possibly illegally) created by hobbyists and uploaded to various code repositories. Installing these alternative OSes is typically a gnarly task, requiring the user to do a lot of complex, fiddly, highly technical work to bypass their devices' digital locks.
In a world without anticircumvention law, a company that sold alternative OSes could hire a ton of programmers and UX developers to smooth over this process, but this is beyond the reach of a typical hobbyist or even a community of hobbyists, especially if they must operate in the shadows, under the threat of civil and criminal liability.
There's a useful analogy here to the trajectory of desktop versions of GNU/Linux. The first time I tried to install Linux (on an original iMac, in the late 1990s), the installation process included a multi-week post-installation wrangle that saw me (often unsuccessfully) compiling key modules from source code and then painstakingly configuring them to get the computer's graphics and I/O working reliably.
Fast forward 30+ years and installing Linux is trivial, thanks to highly capitalized companies like Canonical (makers of Ubuntu, the flavor of Linux I've used for nearly 20 years now). Installing Ubuntu today merely requires that you download the OS to a thumbdrive, reboot your computer using the drive as a startup disk, and click "install." Canonical's installer automatically hunts down the correct software for your hardware and configures it. Canonical writes and contributes to a lot of parts of the Linux OS, but the most important work it does is the fiddly, painstaking, labor- and capital-intensive work of perfecting that installer so it Just Works.
Much of what a vibe-coded jailbreaking tool does is stand in for Canonical, but for hobbyist OSes for smart TVs and speakers and many other devices. These LLMs patiently research every weird error and peccadillo and parse through message boards and logfiles detailing other hobbyists' struggles to get the code working and methodically apply and adapt those solutions until your device Just Works.
Some of these vibe-coded interop tools go farther than that. According to Koebler's coverage, some device owners had their coding assistants scratch-build entirely new, heavily customized OSes for their devices, complete with bypasses that allow this new code to be installed despite the manufacturer's countermeasures which are designed to prevent this. Delightfully, many of these users have created software that revives their bricked, discontinued devices. This poses the possibility of a world in which manufacturers no longer have the last word in your use of your own property: the mere fact that the manufacturer lost interest in a device and killswitched it does not mean that you must consign that valuable device to a landfill to become immortal, toxic e-waste.
All of this is good news. Some of the most sophisticated jailbreaking tools (such as those on the super viral "Reverse Engineer Anything" Github page) run locally, on your own computer, without invoking the "frontier models" that the big, awful AI companies have created:
https://github.com/morluto/rea
This is good even if you're just modifying your own devices to get them to more closely conform to your own use-case. LLMs are genuinely good at coming up with the abstruse and obscure configuration lines and other incantations to get your technology working. Recently, I used a local model to fine-tune the power-management on my new laptop in ways that go beyond the options that are exposed through user-friendly graphic interfaces. The LLM spat out a grub "GRUB_CMDLINE_LINUX_DEFAULT" line that (again) Just Worked.
The last time I had to do this, I spent days painstakingly trouble-shooting options by trial-and-error. Using a chatbot to fill in the gaps left by decisions about which configuration options to place within reach of regular users and which to reserve for power-users has made my computer much more useful to me for the things I want to do, like writing and making collages.
The reality is that it's just not practical for technology developers to turn every conceivable function of your computer into a simple-to-use, accessible tool. A large part of technology design is about leaving things out (or, as my favorite Eno Oblique Strategy goes, "Be the first person to not do something that no one else has ever thought of not doing before"). No matter how thoughtful and diligent a technology designer is, they will never fully anticipate the needs and exigencies of their users. That's why the motto of the disability rights movement is "Nothing about us without us."
The users of technology know more about their use-cases than can ever be captured through a requirements gathering exercise and user testing. One of the best and proudest legacies of technology is the lineage of "user-friendly" programming tools that let nontechnical people design their own applications that exactly met their needs, from Hypercard to Visual Basic to Scratch, a lineage that vibe-coding tools are arguably part of:
https://pluralistic.net/2026/09/25/other-people/#right-there
But these tools are not perfect (nothing is). For all that Hypercard lets you do
many
things that would otherwise require a skilled programmer, it was also always limited relative to, say, writing MacOS code in Objective C. Your Hypercard program might do
exactly
what you needed it to, but slowly, and sometimes unreliably, and with serious limitations, such as a relatively low ceiling for the number of records you could add to a database.
Vibe-coded personal apps aren't necessarily subject to these limitations, but they come with some significant risks. Vibe-code can have serious security vulnerabilities that expose the user to things like identity theft or sextortion. It's conceivable that a vibe-coded garage-door opener app might make it possible for attackers to open your garage door when you're not home (or worse, when you are!). Depending on your risk-tolerance and expertise, these might be acceptable prices, or they might be too high.
But it's important to clearly identify the problem here: if the alternative OS you install on your smart TV exposes you to privacy-invading hack attacks, the problem is the
defect
in that software. The problem
isn't
that you had the temerity to rip out the manufacturer's own software and replace it with code of your choosing. You bought that TV, it's yours, and you don't owe the manufacturer an obligation to expose yourself to its own, built-in, intentional surveillance and invasive ads.
Here's a parallel: you have the right to put any shoelaces in your running shoes. Sure, Nike might prefer you to lace up your Jordans with its expensive OEM laces, but that's Nike's problem, not yours. Now, Nike might argue that by using no-name laces, you run the risk of having a lace break while you're running, which could also break your ankle. That's certainly a possibility: shoelaces do break, and Nike might be justifiably proud of the quality of its laces. But if your generic laces snap (and so does your ankle), the problem is that the shoelaces you chose were defective. The problem is
not
that you chose someone else's laces.
Your stuff is yours. You can put anyone's milk on your cereal, not just the milk that Kellogg's endorses. If the milk you choose is sour and you have to pour your cereal down the toilet, that's too bad, but it doesn't mean that Kellogg's should have the right to shame you for having the temerity to choose the milk you preferred, and it
certainly
doesn't militate for DMCA-style enforcement to coerce you into using Kellogg's official milk in the name of protecting you from food wastage.
I raise this because there's a live debate over this subject, which is well represented in the latest 404 Media podcast:
https://www.youtube.com/watch?v=UbG1qwxMtU0
In the podcast, Koebler and his 404 co-founder Joseph Cox express misgivings about various possible uses of "slop interop." Koebler discusses the fact that John Deere sells the same physical tractor at many different price-points, depending on which software a farmer chooses, and raises the possibility that a farmer might vibe-code software that replicates the high-end functionality without paying for it. Koebler discusses two possible downsides to this: first, that the vibe-coded software might be defective and expose the farmer to risk; and second, a question about whether it's fair or just for a farmer to get those additional functions of their tractor without paying for them.
I think the first objection is entirely legitimate. The software you run on your expensive tractor should be secure, both for your own benefit and for the security of our food supply. That's actually a pretty good reason to ditch John Deere's own software, which is
very
insecure:
https://pluralistic.net/2022/05/08/about-those-kill-switched-ukrainian-tractors/
But I think the second question – whether it's legit to get this functionality without paying John Deere for it – is spurious. Sure, if John Deere provides you with that functionality, then they can send you the bill for it. But if you provide
yourself
with that functionality, using software
you
procured independently of John Deere, then John Deere has no right to get paid for it, and they certainly shouldn't have the right to stop you.
That tractor is
yours
. The fact that John Deere manufactured it is irrelevant. If you pay a contractor to build a house for you and later on pay a different contractor to add another bathroom to it, you don't owe the first contractor anything. It's your house (and if that bathroom has a leaky toilet, that's a matter between you and the second contractor, and not a reason to force you to only use your original contractor).
The law defines a narrow slice of functions that manufacturers get to control: those ideas that a patent examiner deems "novel, useful and nonobvious." It's legit (and good) for commercial operators to copy and improve the ideas of their rivals and competitors. It's why skilled tradespeople cluster together in the same geographic area.
Take Clerkenwell, the neighborhood in London where precision machining was invented by the jewelers and machinists who clustered there during the Longitude rewards. The reason all those competitors sought such close promixity to one another was because they wanted to copy the new techniques their rivals were developing (even if that meant that their rivals would be able to copy them):
https://en.wikipedia.org/wiki/Longitude_rewards
If you're old enough to remember the advent of spreadsheets and the rollout of Visicalc, Lotus 1-2-3 and Excel, you'll know that every time a software vendor invented a new spreadsheet feature, all the other ones immediately copied it. This wasn't bad for spreadsheets: it was
good
for spreadsheets, just as copying your competitors was good for precision machining in Clerkenwell.
Everything from GNU/Linux (a feature-for-feature clone of AT&T Unix) to SAMBA (a plug-compatible clone of Microsoft's SMB) to iWork (file-compatible, feature compatible clones of MS Office's apps) came about through this "adversarial interoperability." What's more, the heyday of this kind of adversarial interop was also the heyday of disenshittification, the era in which any anti-feature installed by your existing vendor could be countered by a disenshittifying patch from a new one:
https://www.eff.org/deeplinks/2019/06/adversarial-interoperability-reviving-elegant-weapon-more-civilized-age-slay
The question of whether vibe-coded software is any good is separate from the question of whether it's good to replace the software in your devices, even if you replace it with software that has features that the manufacturer would normally charge a premium for. You are under no obligation to arrange your commercial affairs to the financial benefit of manufacturers, and anyone who claims to be surprised that someone they sold a device to used it to benefit themselves at the manufacturer's expenses is either disingenuous…or unserious. You bought it, it's yours.
But just as this vibe-coded adversarial interop has drawn both valid and spurious criticism, it's also drawn excitement that is partially justified and partially overblown.
When it comes to reviving bricked devices or rooting out the surveillance and ads from your smart TV, vibe-coded interop tools are genuinely exciting. These are the kinds of enshittification that can truly be remediated with individual jailbreaks.
But the real, meaty examples of enshittification can't be addressed on an individual level – they require systemic fixes. If you jailbreak your iPhone so that it can use alternative app stores, that fact is not sufficient to cause those alternative app stores to come into existence. If we want to stop Apple from levying a $100b "app tax" on the digital economy, it's not enough for individuals to vibe-code their own iPhone patches. We need to repeal the law that bans jailbreaking iPhones, so that a would-be alternative app store can raise capital and pay programmers and tech support staff and salespeople to assemble rival catalogs of software and help customers figure out how to get up their phones to use it.
The same goes for jailbreaking your printer so it accepts generic ink. Sure, this may work for you if you're up for refilling your own cartridges, and I'm sure that you can find someone on Alibaba who will sell you ink by the gallon. But the mere fact that a few users have secretly and privately jailbroken their inkjets won't conjure up a generic inkjet cartridge manufacturing sector. For that to happen, we need to make jailbreaking printers
legal
, not just
possible
.
Indeed, if we want to improve the quality of all that jailbreaking code the chatbots are writing and circulating, we need to be able to put those jailbreaks in public repositories for public inspection and public critique. It's possible for some of the code produced by an LLM to be slop, and for other code to be fine, and for yet a third tranche of code to be
remediable
slop that can be made robust and reliable through auditing and refactoring. You can't figure out which is which if you have to keep that vibe code a secret on pain of a long prison-sentence.
I think there's good cause to be excited at the prospect of getting your devices working better, or just working at all. I think that even if the code stops working after a while, that's still fine – either you got more use out of your device than you would have without the new code, or maybe you just make
more
code that runs for a while for you, and then you do it again.
These individual improvements to your devices and technology are worth celebrating. But they are no substitute for systemic intervention. If we're going to have a new, good internet, a post-American internet that truly disenshittifies America's defective tech exports and replaces them with robust, transparent digital public goods, we need to make reverse-engineering legal again. Once we fix our
policy
,
then
we can fix our
code
:
https://pluralistic.net/2026/01/01/39c3/#the-new-coalition
Hey look at this (
permalink
)
Object permanence (
permalink
)
#25yrsago Secret recording of Labour Whip demanding support for Iraq invasion
https://www.theguardian.com/politics/2001/oct/22/uk.september11
#25yrsago LoC launches emulator-based digital file preservation
https://web.archive.org/web/20011217002337/http://www.techreview.com/magazine/oct01/innovation5.asp
#25yrsago Kevin Mitnick to play CIA lackey
https://web.archive.org/web/20011111105016/http://www.theregister.co.uk/content/55/22395.html
#15yrsago ACLU Tennessee brings suit against ICE officers who broke into house and said, “We don’t need a warrant, we’re ICE, the warrant is coming out of my balls.”
https://web.archive.org/web/20111025092605/http://www.aclu.org/blog/immigrants-rights/we-dont-need-warrant-were-ice/
#15yrsago WIPO’s secret, corporate-run trademark enforcement meeting
https://web.archive.org/web/20220121054715/https://craphound.com/PROGRAMManilaEdited10212011-FINAL.pdf
#15yrsago Canada’s Supreme Court: Linking isn’t libel
https://web.archive.org/web/20111026134334/http://www.bbc.co.uk/news/world-us-canada-15374238
#15yrsago HOWTO recreate the Haunted Mansion’s singing busts
https://www.youtube.com/watch?v=zRtiiMW47i4
#10yrsago Facebook’s crackdown on publishers feeds has sites paying celebs to repost
https://digiday.com/media/facebook-thirsty-publishers-turn-celebrities-worm-news-feed/
#10yrsago Internet-destroying outages were caused by “amateurish” IoT malware
https://krebsonsecurity.com/2016/10/hacked-cameras-dvrs-powered-todays-massive-internet-outage/
#10yrsago Tory minister’s filibuster kills Turing’s law and pardons for 65,000 persecuted gay men
https://www.theguardian.com/law/2016/oct/21/chris-bryant-commons-plea-gay-pardon-law
#10yrsago Trump hotels, faced with massive declines in bookings, rebrand as “Scion Hotels”
https://web.archive.org/web/20161023182616/http://www.travelandleisure.com/hotels-resorts/trump-scion-hotels
Upcoming appearances (
permalink
)
Vancouver: Life After AI (Vancouver Writers Festival), Oct 22
https://writersfest.bc.ca/festival-event-2026/46
Ottawa: Life After AI (Ottawa Writers Festival), Oct 24
https://writersfestival.org/event/life-after-ai
Vienna: TED AI, Oct 28-30
https://tedai-vienna.ted.com/
Kilkenny (Kilkenomics), Nov 6-8
https://kilkenomics.com/
Courtenay: Enshittification (Sid Williams Theatre Society), Nov 10
https://www.sidwilliamstheatre.com/events/cory-doctorow-talks-enshittification/
Vancouver: BC Policy Solutions Gala, Nov 12
https://bcpolicy.ca/gala/
Oxford: Ministry of the Future, Nov 23
https://ministryforthefuture.co.uk/events.html
Sheffield: Reverse Centaur at Juno Books, Nov 25
https://www.outsavvy.com/event/40274/cory-doctorow-in-conversation
Virtual: Enshittification, AI, and the Future of Technology (UBC Master of Educational Technology), Nov 28
https://met.ubc.ca/2026/09/met-speaker-series-cory-doctorow-enshittification-ai-and-the-future-of-technology/
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
“Once Is Enemy Action,” a science fiction novel about the origins of modern technofascism. Today's words: 533 (27469 total).
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
