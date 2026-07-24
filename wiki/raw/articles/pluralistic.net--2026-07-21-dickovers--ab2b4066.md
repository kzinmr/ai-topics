---
title: "Pluralistic: Dealing with dickovers (21 Jul 2026) dickovers"
url: "https://pluralistic.net/2026/07/21/dickovers/"
fetched_at: 2026-07-24T10:13:57.492445+00:00
source: "pluralistic.net"
tags: [blog, raw]
---

# Pluralistic: Dealing with dickovers (21 Jul 2026) dickovers

Source: https://pluralistic.net/2026/07/21/dickovers/

Today's links
Dealing with dickovers (
permalink
)
One of 2026's better tech-related coinages is "dickover," John Gruber's term for
a modal panel, popover, or curtain presented by a website or app, deliberately obscuring its own content to frustrate the user with an unwanted, unnecessary, mandatory interaction; e.g. asking the user to accept “cookies”, subscribe to a newsletter, install the website’s mobile app, agree to terms of service, or anything else that the user couldn’t give two shits about.
https://daringfireball.net/2026/05/what_is_a_dickover
These are bad everywhere, but they are especially terrible in the UK and EU, where websites practice a form of malicious compliance to the GDPR, Europe's landmark privacy law. Under the GDPR, websites are required to secure your affirmative consent to process your data. The obvious way that websites should respond to this is by not collecting your data unless there's a damned good reason for it, but the
actual
response is to repeatedly shove cookie-consent dialogs in your face before letting you use the site.
These are absolutely unnecessary. Your browser can be configured to transmit a "global privacy control signal" by default that tells websites you don't consent to be spied on while you look at their pages:
https://support.mozilla.org/en-US/kb/global-privacy-control
But many websites punish you by throwing up a "Global Privacy Control detected" dickover that forces you to click through to affirm their confirmation of your confirmation that you don't want to be spied on.
If you don't have the GPC set, websites will demand that you tell them whether you want to be spied on – and they'll do it again, every time you visit them. The website operators falsely claim that they have to do this under the terms of the GDPR (or other laws, like California's CCPA). This is a lie. Every privacy law contains an exception that allows websites to store data about you for a "legitimate interest," and that obviously includes setting a cookie that says, "don't ever spy on this user."
What's a legit interest? Well, I can tell you what it
isn't
. Facebook claimed that they
had
to spy on you, even if you opted out by laboriously clicking through one of their dickovers or by transmitting a GPC signal to their servers, because you had
also
clicked through their terms of service, which say, "Facebook is going to spy on you with every hour that god sends, from asshole to appetite, abandon hope all ye who enter here" (a direct quote). Facebook claims that this is a
contract
with you, whereby the company has
promised
to spy on you, and if they stop, they would be
violating the contract
, which might make you mad, so they are
legally required
to eavesdrop on every conversation you have and follow you everywhere you go:
https://www.cliffordchance.com/content/dam/cliffordchance/briefings/2023/07/european-court-of-justice-in-facebook-ruling-clarifies-interplay-between-eu-competition-law-and-data-protections-enforcement.pdf
This is bullshit, and the European Court of Justice affirmed it. But despite the fact that surveillance advertising companies are happy to stretch the definition of "legitimate interest" to cover "spying on you because our ToS say we will," these same companies insist that "legitimate purpose" can't
possibly
include "remembering the fact that you told us not to spy on you the last time you were here," and so every time you click through to one of many popular websites, you get a dickover, and the only way to make it stop is to "consent" to being spied upon.
But it doesn't have to be this way. While the right answer to this kind of rampant lawlessness is stonking fines and even the corporate death penalty for repeat offenders, internet users have a myriad of options available to them for banishing dickovers to the scrapheap of history. These measures aren't difficult to avail yourself of, and using them will make your life infinitely better, so I'm going to tell you about some of them.
Before I start, one note: these measures only work on browsers, not apps. An app is a webpage wrapped in the right kind of IP law to make it a felony to change how it works, which is why companies are infinitely horny to get you to use their apps, not their websites:
https://pluralistic.net/2024/05/07/treacherous-computing/#rewilding-the-internet
What's more, these measures really only work on
desktop
browsers, because mobile browsers are apps, and are severely limited by law and mobile operating systems, making it hard-to-impossible to customize them so that they'll respect your rights. This is true of all mobile browsers, but it goes triple for iOS (iPhones and iPads):
https://pluralistic.net/2022/12/13/kitbashed/#app-store-tax
Finally, this mostly only works on
Firefox
, and it works
worst
on Chrome, Google's monopolistic browser. When it comes to customizing your browsing experience to get rid of annoyances like dickovers and ads, Chrome is hands-down the worst choice, and Google is about to make it much, much worse, forcing a change that will kill the most popular blockers. Stop using Chrome, switch to Firefox:
https://protonprivacy.substack.com/p/google-is-finally-killing-ublock
So, once you're on your actual computer, using Firefox, how can you disenshittify your internet experience? The first thing to familiarize yourself with is Reader Mode, a built-in Firefox feature that switches any webpage to a black type/white background column of text. Just click the little "page view" icon next to the Firefox location bar or use the key combo "ctrl-alt-r."
Some power tips for Reader Mode: Firefox tries to guess whether a given page should have a Reader Mode option based on its layout. This sometimes blocks Reader Mode on pages that badly need it. You can force Firefox to
always
allow you to try Reader Mode by going to "about:config" in your location bar, then searching for "reader.parse-on-load.force-enabled" and toggling it to "true". If you switch to Reader Mode and the page breaks, you can switch back by hitting ctrl-alt-r again.
Many websites' "soft paywalls" (which allow you to read an article or two before getting a demand to register and/or pay) can be defeated with Reader Mode. Just hit ctrl-alt-r and see if the whole article appears. If it doesn't, try one or both of: a) reloading the page while still in Reader Mode, and/or; b) Clearing cookies for the page (click the shield next to the site's URL in Firefox's location bar, then click "Clear cookies and site data"), and then reload.
That's Reader Mode, and it comes built into Firefox, and can be installed via various extensions on other browsers. Now let's move on to more advanced techniques, starting with "Kill Sticky," a bookmarklet that deletes any "static" elements in a web-page you've loaded (broadly, this is anything that won't change position when you scroll your browser).
Just click the "Kill Sticky" bookmarklet and all the static elements in the current tab go away. This includes things like navigation bars, which are often (but not always) useless annoyances. The original Kill Sticky, created by Alisdair McDiarmid, is 13 years old, and it still works great, but eight years ago, gala8y created a new version that caught some outliers that the original Kill Sticky missed. I've been running gala8y's version for a year now with no problems, and I recommend it as your second line of dickover defense (after Reader Mode):
https://github.com/gala8y/kill-sticky–forked
Kill Sticky is great for getting rid of the dickovers on a website you're not planning to visit more than once. But if you visit a dickover website regularly, you can
permanently
block its dickovers by using the Adblock Plus (ABP) browser extension:
https://adblockplus.org/
Once you have Adblock Plus installed, you can instruct your browser
never
to render a given website's dickover. Just load the website, hover your pointer over the dickover, and click your right mouse-button (Mac users need to ctrl-click). This will pop up a Firefox context menu, and at the bottom of that menu is "Block Element…".
Select "Block Element," then move your mouse around the screen. Different regions of the screen will glow pink, showing you which element (part of the page) ABP can access there. Once you've highlighted the dickover, click the "Preview" button on the ABP dialog in the bottom right corner. This will show you how the page looks after you've banished that element.
If it's an element you want to delete forever, click "Create" and ABP will create a new rule for that page that blocks that element. Note that many dickovers consist of
several
elements, each atop the other, and after you block one element, you might have to repeat the process to delete the element "behind" it, digging your way down to the actual webpage. Each element you block is listed in the top pane of the ABP dialog box. For example, here's Wired.com's UK dickover:
||media.wired.com/photos/6a565246c8e0799a2981818e/1:1/w_*c_limit/WEB_2026-06-21_EA-WIRED-NBNO-FullQual_0011.jpg
If you block an element by accident and want to restore it, just delete its corresponding line in the Block Element dialog. When websites change their layouts and their dickovers come back, just add the new one to the Block Element for that page. No need to delete the old entries.
Finally, if all else fails, there's Remove Paywall, a website that tries several different ways to load a page without its interrupters, nag screens, regwalls and paywalls:
https://www.removepaywall.com/
It's also available as a browser plugin, so you can just right-click on any page and select "Remove Paywall" from the pop-up menu. Remove Paywall often loads a page with all of its dickovers, and you can use all the techniques enumerated above – Reader Mode, Kill Sticky and Block Element – with Remove Paywall versions of pages.
Back in 2024, Ed Zitron tried an experiment: he bought Amazon's bestselling laptop and tried to use it, discovering it to be a horror-show of shovelware, including processor-devouring preinstalled spyware that rendered it all but unusable:
https://www.wheresyoured.at/never-forgive-them/
Zitron's (excellent) point is that technically proficient people have better computers than most users, and these computers are configured in better ways, and as a result, we participate in a fundamentally different internet to the one that normies are forced to use.
It's an excellent observation, and Zitron's point – that these laptops were actively enshittified by hardware makers and OS vendors – is an important one (the essay is called "Never Forgive Them").
But to this point, I would like to add another: we have a duty and obligation to the people we love to show them how to seize the means of computation. The normies in your life need the tips and tricks I lay out in this article more than anyone. Sure, it takes some doing to install Firefox, Kill Sticky, Adblock Plus and Bypass Paywalls; it takes a minute to figure out Reader Mode.
But if you install these tools for the people you love and show them how to use them (or just reconfigure the sites they visit most frequently to block dickovers and other annoyances), you will
permanently
improve their internet experience, clawing back
hours
of annoyances every week, while also protecting their privacy.
Anyone who is confused by switching to Firefox is
also
going to be confused by the deceptive language and practices that go along with dickovers. By leaving your unsophisticated loved ones exposed to dickovers, you're not decreasing the amount of technological confusion they're likely to experience in a day – you're
vastly increasing
the amount of danger they face as a result of that confusion.
There's never been a better time to disenshittify your cherished normies' computers. The AI companies' illegal monopolization of the memory market has sent the price of new computers, RAM and storage skyrocketing:
https://www.youtube.com/watch?v=BORRBce5TGw
All of us – but especially normies – are having to do more with less. The best way to squeeze extra performance out of any computer (but especially an aged and underpowered computer) is by switching to a free/open operating system like GNU/Linux and replacing your proprietary, resource-gobbling apps with free/open alternatives:
https://www.fosslinux.com/158206/linux-on-older-hardware-revival-guide.htm
Seizing the means of computation isn't theft, it's
bargaining
. Commercial surveillance companies will tell you that by spying on you, they are simply engaged in a marketplace exchange in which you swap your privacy for access to online services. But they are running a very curious sort of market: it's a "market" where as soon as you stop to browse someone's wares, the stallholder gets to reach into your pocket and clean out your wallet. In "markets," prices are announced and bargained over, not set unilaterally and extracted from anyone unwise enough to cross the threshold.
Adblocking, dickover blocking and other customizations are a way for you to bargain back, to answer the opening bid of "How about you give me all of your data forever and let me do anything I want with it?" with "How about 'nah?'"
https://www.eff.org/deeplinks/2019/07/adblocking-how-about-nah
Dickovers are companies' illegal response to privacy laws. Privacy laws are the public response to companies' out-of-control data theft and weaponization. They call us thieves, but they're the ones who embarked upon a generation-long campaign of unrestricted data plunder. What they call "theft" is just self-defense.
A generation ago, publishers and advertisers fell in love with pop-up ads. Early pop-ups were virulent in ways that are hardly imaginable today: visiting a website summoned
dozens
of pop-ups, some of them employing dirty tricks like spawning as an invisible 1×1 pixel, or running away from your cursor when you tried to close them. They auto-played sound and music. They were
Satanic
.
We got rid of pop-ups by installing pop-up blockers. Browser vendors (starting with Opera, then Mozilla) blocked pop-ups by default. Soon, pop-ups simply
ceased to exist
for the majority of internet users, and at that point, the same companies who'd insisted that they would go out of business unless they could fill your screen with pop-ups quietly gave up on them and found another way to advertise.
No one should ever have to look at another dickover. If dickovers become invisible for everyone on the web, there won't be any dickovers. Companies claim they
need
dickovers to survive. It's bullshit. They
want
dickovers, but if dickovers cease to be rendered on their target audience's screens, they'll switch to less invasive tactics, just like they've always done.
(
Image:
Kanerva T
,
CC BY 4.0
, modified
)
Hey look at this (
permalink
)
WRITERS GUILD OF AMERICA, WEST, INC., and WRITERS GUILD OF AMERICA EAST, INC., Plaintiffs, vs. PARAMOUNT SKYDANCE CORPORATION, and WARNER BROS. DISCOVERY, INC
https://www.wga.org/uploadedfiles/news_and_events/public_policy/wga-v-paramount-warner-bros-complaint.pdf
Deliria 2, Cyberpunks Mutants & Mondoids
https://grayarea.org/event/deliria-2-cyberpunks-mutants-mondoids/
Can machines replace human workers? Notes on agency, automation, and AI
https://publications.jrc.ec.europa.eu/repository/handle/JRC147594
Scorpions bite again
https://jasminatesanovic.wordpress.com/2026/07/14/scorpions-bite-again/
Mandatory Update: A Short Story
https://micahflee.com/mandatory-update-a-short-story/
Object permanence (
permalink
)
#20yrsago Worst week in the history of broadcast TV
https://web.archive.org/web/20060717100605/http://asia.news.yahoo.com/060711/ap/d8iq1l8g0.html
#20yrsago Pen with built-in WiFinder
https://web.archive.org/web/20060808191736/https://informatica.shopwprintit.com/index.cfm?action=ViewDetails&amp;ItemID=135&amp;Category=95
#15yrsago Russian Pirate Party must change name, contemplates “Pira7e Party”
https://torrentfreak.com/judge-pirate-party-name-ban-decision-stands-110722/
#15yrsago Public special ed employee has $0 paycheck after health insurance deductions
https://web.archive.org/web/20110726080414/http://www.educationvotes.nea.org/2011/07/20/a-special-education-worker-talks-candidly-about-empty-paychecks-organizing/
#15yrsago Act now! Congress wants to kill WiFi-like spectrum, sell it off to highest bidder instead
https://web.archive.org/web/20110722113231/https://publicknowledge.org/dont-let-cos-buy-way-out-regulation
#15yrsago New Yorkers freestyle rap in Union Square
https://www.youtube.com/watch?v=N3fd9mzfRoQ
#10yrsago Advances in transparent, brain-revealing skull-windows
https://web.archive.org/web/20160722140424/https://www.medgadget.com/2016/07/transparent-skull-implant-repeat-brain-laser-therapy.html
#10yrsago EFF is suing the US government to invalidate the DMCA’s DRM provisions
https://www.theguardian.com/technology/2016/jul/21/digital-millennium-copyright-act-eff-supreme-court
#10yrsago Ed Snowden and Andrew “bunnie” Huang announce a malware-detecting smartphone case
https://www.tjoe.org/pub/direct-radio-introspection/release/
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
