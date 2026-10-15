---
title: "Microsoft Patches More Than 1,400 Security Flaws"
url: "https://krebsonsecurity.com/2026/10/microsoft-patches-more-than-1400-security-flaws/"
fetched_at: 2026-10-14T10:01:15.259421+00:00
source: "krebsonsecurity.com"
tags: [blog, raw]
---

# Microsoft Patches More Than 1,400 Security Flaws

Source: https://krebsonsecurity.com/2026/10/microsoft-patches-more-than-1400-security-flaws/

Microsoft
today issued updates to fix more than 1,400 security vulnerabilities in its
Windows
operating systems and other software. Today’s epic patch batch dwarfs September’s record of nearly 1,000 fixes, which was already about ten times the normal monthly patch load from Redmond.
Just one of the weaknesses patched this week is considered a “zero day,” or already exploited in the wild.
CVE-2026-96951
is a security feature bypass in the
Windows Shell
that affects Windows 10 and 11 systems, as well as some Server versions.
Windows 10 users might be wondering if they can still expect security updates after this month. Microsoft had been slated to stop shipping updates for Windows 10 systems in October 2025, but ended up adding another year of free updates after considerable pushback. A few months ago, Microsoft
quietly extended that support
for another year (until October 2027).
At least 78 of the flaws fixed this month are rated “critical,” meaning they could be exploited with little or no action by the user, and most of those critical bugs allow an attacker to execute code of their choice on the vulnerable system.
While Microsoft said there are no signs anyone is exploiting it yet, a security feature bypass in the .NET Framework (
CVE-2026-108398
) was publicly disclosed prior to today, potentially giving attackers advance time to work out how to exploit the bug.
Satnam Narang
at
Tenable
said the number of flaws fixed this month far surpasses the previous record-setting year 2020, when Microsoft patched 1,261 CVEs.
“We’ve now crossed the 4,000 CVE mark with two months left to go,” he said.
Microsoft credits large language models for the high volume of bug discovery, and presumably AI gets credit for many of the patches used to fix these flaw. Meanwhile, security experts have been warning that these unusually large patch volleys from Microsoft are placing extra strain on corporate security teams, which often have to test individual updates before deploying them across a network to ensure the fixes don’t cause problems for other software.
Tyler Reguly
, associate director of security research and development at
Fortra
, notes that just 26 Microsoft vulnerabilities appeared in the “Known Exploited Vulnerabilities” (KEV) catalog maintained by the U.S. Cybersecurity & Infrastructure Security Agency (CISA) so far this year, and security teams would do well to prioritize patching those 26 vulnerabilities first.
“Security leaders should focus on exploitable risk, and ask whether their teams have the clarity, capacity and support to act,” Reguly said.
Which vulnerabilities deserve the most scrutiny in your organization? The folks at
Cisco Talos
have
a useful roundup
of the more noteworthy flaws that Microsoft fixed today, and of course the
SANS Internet Storm Center
has
a reliable roundup
that indexes vulnerabilities by severity, CVE number and affected software.
