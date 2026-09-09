---
title: "Microsoft Plugs Nearly 1,000 Security Holes"
url: "https://krebsonsecurity.com/2026/09/microsoft-plugs-nearly-1000-security-holes/"
fetched_at: 2026-09-09T10:00:59.779108+00:00
source: "krebsonsecurity.com"
tags: [blog, raw]
---

# Microsoft Plugs Nearly 1,000 Security Holes

Source: https://krebsonsecurity.com/2026/09/microsoft-plugs-nearly-1000-security-holes/

Microsoft Corp.
today issued updates to plug at least 974 security holes in its
Windows
operating systems and other software, by far its biggest single patch batch ever. Microsoft says artificial intelligence is helping to speed the discovery of vulnerabilities, but security experts warn that many organizations already are struggling to prioritize the more human-intensive endeavor of testing and deploying so many fixes each month.
Image: Shutterstock.com, Kirill Makarov.
This month’s patch bundle obliterates the software giant’s
previous record set in July
, when it released updates for at least 570 security vulnerabilities. September’s Patch Tuesday brings this year’s total to more than 2,600, more than twice Microsoft’s previous record-setting patch year in 2020 (1,245) and with three more months to go.
There are two “zero-day” flaws fixed this month that are being actively exploited: both
CVE-2026-81963
and
CVE-2026-85880
allow an attacker to elevate their privileges on Windows system.
Fully 113 of the bugs addressed today earned Microsoft’s “critical” rating, meaning they could be abused by malware or miscreants to seize control over a vulnerable Windows machine with little or no help from the user.
Among the more serious critical flaws this month is
CVE-2026-69730
, a DNS weakness present in Windows Server 2012 onward and on Windows 10. Microsoft warns that an unauthenticated attacker could leverage this weakness simply by sending a specially crafted packet to an affected system, and that it is likely to be exploited.
Also scary is
CVE-2026-69829
, a critical, remote code execution flaw in the Windows Shell. This vulnerability has a CVSS base score of 9.8 (10 is the most severe), and can be exploited with low attack complexity, no privileges, and no user interaction.
Microsoft’s summary of the security updates released today. Image: msrc.microsoft.com.
Microsoft is hardly alone in shipping monster patch bundles lately. Many other large software companies, including Adobe, Cisco, Google, Mozilla and Oracle, all have recently credited AI-assisted research with increasing their patch cadence and volume (Google said today it is now going to ship security updates every two weeks).
Tyler Reguly
, associate director of security research and development at
Fortra
, said one core challenge with deploying Windows updates is that they need to be tested before being installed across an organization because not all third-party software works seamlessly in the face of changes to the underlying operating system.
“It’s time to put our CISOs and CSOs on notice,” Reguly said. “How are you helping your teams through these difficult times? Do you have your teams deploy after hours and on weekends to avoid disruption to the business environment? Do you reward them for that effort? Time to dig into your budget and buy dinner for your teams that are working on Saturday to get patches rolled out before users return to work on Monday.”
Satnam Narang
is senior staff research engineer at
Tenable
. Narang said it’s important to recognize that while the number of vulnerabilities being patched by Microsoft is rising, the number of flaws that can and will affect most organizations remains quite low.
“AI-assisted vulnerability discovery in 2026 is creating larger haystacks, but it isn’t finding more needles,” he said. “It’s critical that organizations understand which vulnerabilities actually apply to them, whether they pose a threat by being reachable and exploitable, and prioritize remediation based on this risk context.”
Of course, regular Windows users don’t need to test patches before deploying them, but they still need to open Windows Update periodically or else assent to the program’s nag notices about pending updates. And at the rate these Windows patch releases are ballooning in size, it’s probably best not to let them pile up month after month.
Enterprise Windows admins will want to keep an eye on
askwoody.com
for news of any updates that appear to be causing problems. As always, the
SANS Internet Storm Center
has
a per-patch breakdown
ordered by severity and urgency.
