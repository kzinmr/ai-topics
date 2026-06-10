---
title: "A Record-Breaking Patch Tuesday for June 2026"
url: "https://krebsonsecurity.com/2026/06/a-record-breaking-patch-tuesday-for-june-2026/"
fetched_at: 2026-06-10T07:01:29.098837+00:00
source: "krebsonsecurity.com"
tags: [blog, raw]
---

# A Record-Breaking Patch Tuesday for June 2026

Source: https://krebsonsecurity.com/2026/06/a-record-breaking-patch-tuesday-for-june-2026/

Microsoft
today released software updates to plug nearly 200 security holes across its
Windows
operating systems and supported software, a record number of fixes for the company’s monthly Patch Tuesday cycle. Nearly three dozen of those bugs earned Microsoft’s most dire “critical” rating, and exploit code for at least three of the weaknesses is now publicly available.
The software giant said in
a blog post
last month that both its engineers and the security community are increasing using artificial intelligence tools to find bugs, meaning this month’s heavy Patch Tuesday may start to become the norm, said
Satnam Narang
, senior staff research engineer at
Tenable
.
“Some surveys put AI usage among security professionals generally at 90%, so it’s unsurprising that this volume of patches may be the norm,” Narang said. “Pandora’s proverbial box has been opened, and as more advanced AI models become available, we expect the norm to continue upward across the board, not just for Patch Tuesday.”
June’s zero-day bugs include
CVE-2026-49160
, a denial of service vulnerability affecting a range of web servers, including Microsoft
Internet Information Services
(IIS). Microsoft says the flaw was reported by OpenAI’s Codex.
Two of the zero-days addressed this month appear to stem from recent vulnerability disclosures by
Nightmare Eclipse
, the nickname chosen by a security researcher who has been dropping exploits for various Windows flaws. One of those, dubbed “GreenPlasma,” leverages an elevation of privilege weakness in the Windows Collaborative Translation Framework, the same framework patched today in
CVE-2026-45586
.
Nightmare Eclipse also last month released “YellowKey,” an exploit for a Windows BitLocker vulnerability that allows an attacker with physical access to view encrypted data, and
CVE-2026-50507
is a patch for an elevation of privilege bug in BitLocker.
Microsoft received heavily blowback on social media last month after it said in
a blog post
that it was considering taking legal action against the security researcher. The company later clarified on Twitter/X that while it has no intention of pursuing legal actions against researchers, it would report them to authorities if they break the law. The advisories for CVE-2026-49160 and CVE-2026-50507 do not credit any researchers in the acknowledgement section, saying only that “Microsoft recognizes the efforts of those in the security community who help us protect customers through coordinated vulnerability disclosure.”
Nightmare Eclipse
claims to be
a former employee
of Microsoft, although Microsoft has not responded to questions about this claim.
Rapid7
notes that a recent blog post by Nightmare Eclipse included an image of Albert Vesker, a character from the Resident Evil video game series who formerly worked as a researcher for a technology company before going rogue.
Nightmare Eclipse has pledged to release even more zero-day exploits for Windows in what they called a “bone shattering” drop planned for July 14 (the same day as next month’s Patch Tuesday). Immediately following the release of Microsoft patches today, the researcher
published an exploit
for what they claimed was a zero-day bug in Windows Defender.
While 200 vulnerabilities may be a record for Patch Tuesday, the actual number of security flaws Microsoft addressed this month is far higher, said Rapid7’s
Adam Barnett
.
“So far this month, Microsoft has provided patches to address 360 browser vulnerabilities, which is an order of magnitude more than has been typical in any given month over the past few years,” Barnett wrote. “As usual, browser [flaws] are not included in the Patch Tuesday count above. Indeed, the vast, and presumably sustained, uptick in the number of browser vulnerabilities has led to Microsoft no longer enumerating Chromium CVEs in the Security Update Guide.”
Microsoft also patched a zero-day vulnerability in
Visual Studio Code
that allows attackers to steal GitHub tokens with a single click. The company was forced to push a stopgap fix for the flaw on June 3, after a researcher
published instructions
showing how to exploit it. The researcher said they opted not to work with Microsoft because of a recent experience wherein Redmond silently patched a flaw they reported without offering credit or recognition.
Microsoft battled its own internal zero-day emergencies last week, after at least 72 of the company’s public code repositories were infected with
a variant of the Shai-Hulud worm
. Researchers found that all of the affected packages were connected to Microsoft official Azure Durable Task SDK, which got
hit by the same Shai-Hulud worm
in May.
Other major software makers are also shipping outsized update bundles this month.
Adobe
has released updates to fix a massive number of critical vulnerabilities
across a range of products
, including
Adobe Experience Manager
,
Acrobat Reader
and
Cold Fusion
. On June 3,
Google
resolved
a whopping 429 vulnerabilities
in its latest
Chrome
browser update (Chrome automatically downloads updates but installing them usually requires a complete restart of the browser).
As ever, please consider backing up your data before applying operating system updates, and drop a note in the comments if you run into any problems with this month’s patches.
Further reading:
Microsoft’s Security Update Guide
Action1’s Patch Tuesday breakdown
SANS Internet Storm Center notes on Patch Tuesday
