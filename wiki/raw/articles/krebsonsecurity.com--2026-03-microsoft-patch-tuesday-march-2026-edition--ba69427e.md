---
title: "Microsoft Patch Tuesday, March 2026 Edition"
url: "https://krebsonsecurity.com/2026/03/microsoft-patch-tuesday-march-2026-edition/"
fetched_at: 2026-04-30T07:01:59.306851+00:00
source: "krebsonsecurity.com"
tags: [blog, raw]
---

# Microsoft Patch Tuesday, March 2026 Edition

Source: https://krebsonsecurity.com/2026/03/microsoft-patch-tuesday-march-2026-edition/

Microsoft Corp.
today pushed security updates to fix at least 77 vulnerabilities in its
Windows
operating systems and other software. There are no pressing “zero-day” flaws this month (compared to February’s five zero-day treat), but as usual some patches may deserve more rapid attention from organizations using Windows. Here are a few highlights from this month’s Patch Tuesday.
Image: Shutterstock, @nwz.
Two of the bugs Microsoft patched today were publicly disclosed previously.
CVE-2026-21262
is a weakness that allows an attacker to elevate their privileges on
SQL Server 2016
and later editions.
“This isn’t just any elevation of privilege vulnerability, either; the advisory notes that an authorized attacker can elevate privileges to sysadmin over a network,” Rapid7’s
Adam Barnett
said. “The CVSS v3 base score of 8.8 is just below the threshold for critical severity, since low-level privileges are required. It would be a courageous defender who shrugged and deferred the patches for this one.”
The other publicly disclosed flaw is
CVE-2026-26127
, a vulnerability in applications running on
.NET
. Barnett said the immediate impact of exploitation is likely limited to denial of service by triggering a crash, with the potential for other types of attacks during a service reboot.
It would hardly be a proper Patch Tuesday without at least one critical
Microsoft Office
exploit, and this month doesn’t disappoint.
CVE-2026-26113
and
CVE-2026-26110
are both remote code execution flaws that can be triggered just by viewing a booby-trapped message in the Preview Pane.
Satnam Narang
at
Tenable
notes that just over half (55%) of all Patch Tuesday CVEs this month are privilege escalation bugs, and of those, a half dozen were rated “exploitation more likely” — across Windows Graphics Component, Windows Accessibility Infrastructure, Windows Kernel, Windows SMB Server and Winlogon. These include:
–
CVE-2026-24291
: Incorrect permission assignments within the Windows Accessibility Infrastructure to reach SYSTEM (CVSS 7.8)
–
CVE-2026-24294
: Improper authentication in the core SMB component (CVSS 7.8)
–
CVE-2026-24289
: High-severity memory corruption and race condition flaw (CVSS 7.8)
–
CVE-2026-25187
: Winlogon process weakness discovered by Google Project Zero (CVSS 7.8).
Ben McCarthy
, lead cyber security engineer at
Immersive
, called attention to
CVE-2026-21536
, a critical remote code execution bug in a component called the Microsoft Devices Pricing Program. Microsoft has already resolved the issue on their end, and fixing it requires no action on the part of Windows users. But McCarthy says it’s notable as one of the first vulnerabilities identified by an AI agent and officially recognized with a CVE attributed to the Windows operating system. It was discovered by
XBOW
, a fully autonomous AI penetration testing agent.
XBOW has consistently ranked at or near the top of the Hacker One bug bounty leaderboard for the past year. McCarthy said CVE-2026-21536 demonstrates how AI agents can identify critical 9.8-rated vulnerabilities without access to source code.
“Although Microsoft has already patched and mitigated the vulnerability, it highlights a shift toward AI-driven discovery of complex vulnerabilities at increasing speed,” McCarthy said. “This development suggests AI-assisted vulnerability research will play a growing role in the security landscape.”
Microsoft earlier provided patches to address nine browser vulnerabilities, which are not included in the Patch Tuesday count above. In addition, Microsoft issued a crucial out-of-band (emergency)
update on March 2
for
Windows Server 2022
to address a certificate renewal issue with passwordless authentication technology Windows Hello for Business.
Separately,
Adobe
shipped updates to fix 80 vulnerabilities — some of them critical in severity — in
a variety of products
, including
Acrobat
and
Adobe Commerce
.
Mozilla Firefox
v. 148.0.2 resolves three high severity CVEs.
For a complete breakdown of all the patches Microsoft released today, check out the SANS Internet Storm Center’s
Patch Tuesday post
. Windows enterprise admins who wish to stay abreast of any news about problematic updates,
AskWoody.com
is always worth a visit. Please feel free to drop a comment below if you experience any issues apply this month’s patches.
