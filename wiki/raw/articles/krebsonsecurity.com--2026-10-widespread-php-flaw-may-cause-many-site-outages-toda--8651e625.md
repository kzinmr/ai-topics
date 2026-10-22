---
title: "Widespread PHP Flaw May Cause Many Site Outages Today"
url: "https://krebsonsecurity.com/2026/10/widespread-php-flaw-may-cause-many-site-outages-today/"
fetched_at: 2026-10-22T10:01:04.117640+00:00
source: "krebsonsecurity.com"
tags: [blog, raw]
---

# Widespread PHP Flaw May Cause Many Site Outages Today

Source: https://krebsonsecurity.com/2026/10/widespread-php-flaw-may-cause-many-site-outages-today/

Expect to see quite a few websites serving error pages today: Nearly 70 percent of websites need to update their core software to fix a pair of vulnerabilities that allow an attacker to seize full control over affected servers. Experts say there are working exploits for the flaws, and that these critical bugs are already being exploited in the wild.
Image: Shutterstock.com, Sashkin.
The flaws at issue are present in
PHP
, the programming language that powers sites running on a large number of web publishing systems, including
Drupal
,
Magento
,
Joomla
and
WordPress
. Earlier today, PHP released
an emergency security update
to fix two critical bugs that can allow an attacker to execute code of their choosing on a vulnerable server.
Reuters
reports
that government websites in Europe and elsewhere went offline today after the PHP vulnerabilities were disclosed. Cloudflare
said
it has already detected some exploitation of the flaw, and that at 3:02 am (UTC) it implemented web application firewall rules to protect websites from attack traffic seeking to exploit the bugs, which could cause a denial of service condition, remote code execution, and data exposure.
OpenAI
, which was involved in the vulnerability research and outreach,
said
“given the severity of these flaws and PHP’s widespread use, we consider this one of the most impactful security issues in recent memory.”
Censys
, a company that tracks the technology used by Internet hosts,
said
a recent scan identified approximately 2.58 million Internet facing hosts and 54.9 million web properties running PHP.
Security experts at
Wiz
said every PHP version released in the last decade is affected by at least one of these vulnerabilities [full disclosure: Wiz is an advertiser on this blog].
“These findings rank among the most severe vulnerabilities discovered in PHP, and arguably in software history,” reads
a blog post
published today by a team of researchers at Wiz, which was one of several organizations credited with discovering the vulnerabilities. “The underlying flaws had been present for decades, but demonstrating their exploitability required an exceptionally complex chain of steps, at the edge of what human researchers could practically achieve. Frontier AI models substantially reduced that barrier, turning a longstanding flaw into an exploit.”
The Wiz researchers say it is likely the PHP vulnerabilities will be mass-exploited to install web-based backdoors or “web shells,” which give attackers a web-based panel that allows them to remotely control infected sites. Wiz said that prior to the PHP bugs being publicly disclosed, the company worked with the PHP team, Calif and OpenAI to measure the size of the problem and coordinate patch verification and disclosure.
The PHP zero-day vulnerabilities are being tracked by their CVE numbers,
CVE-2026-109618
and
CVE-2026-109619
, and they affect all web servers running PHP 5.4 or later. The bugs are fixed in PHP
8.5.12
,
8.4.27
,
8.3.36
, and
8.2.35
.
According to Wiz, PHP is so deeply embedded in many web applications that we are likely to see organizations struggling to patch these vulnerabilities for some time to come, comparing this PHP vulnerability pair with
the Log4Shell weakness
that emerged in 2021 — a widespread, severe-as-it-gets security flaw in Log4j, a popular Java logging framework.
“A vulnerability in core PHP reaches far beyond a single application,” the Wiz researchers wrote. “PHP runs across clouds, hosting providers, content-delivery networks and millions of independently managed servers. Reducing exposure before the technical details became public required coordinated work across that entire ecosystem.”
The
SANS Internet Storm Center
is
keeping an eye on
major software platforms that are shipping updates to deal with these PHP flaws. For example, Ubuntu just released updated PHP packages. For a technical deep-dive on these vulnerabilities that tells the timeline of the discovery of these bugs in a comic book style, check out
this post
from
Calif
, another technology company credited with finding the PHP flaws.
This is a fast-moving story. Updates will be noted here with timestamps.
Update, 2:30 pm ET:
Add figures from Censys and a link to Calif’s writeup.
