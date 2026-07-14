---
title: "Code Red worm, July 13, 2001"
url: "https://dfarq.homeip.net/code-red-worm-july-13-2001/?utm_source=rss&utm_medium=rss&utm_campaign=code-red-worm-july-13-2001"
fetched_at: 2026-07-14T07:01:13.745983+00:00
source: "dfarq.homeip.net"
tags: [blog, raw]
---

# Code Red worm, July 13, 2001

Source: https://dfarq.homeip.net/code-red-worm-july-13-2001/?utm_source=rss&utm_medium=rss&utm_campaign=code-red-worm-july-13-2001

Code Red was a computer worm that exploited one of the earliest notorious Microsoft vulnerabilities, a buffer overflow in Microsoft IIS. It is credited as the first large scale mixed threat attack against enterprise networks. Code Red was released July 13, 2001, although its first observation happened two days later, on July 15, 2001. Infections peaked July 19, 2001, infecting 359,000 servers worldwide.
The Code Red worm’s discovery
The Code Red worm defaced websites, replacing sites written in English with this page.
The Code Red worm was first discovered and researched by eEye Digital Security employees Marc Maiffret and Ryan Permeh. They named it “Code Red” because they were drinking Mountain Dew Code Red, a cherry-flavored caffeinated soda, at the time they discovered it.
Code Red exploited CVE-2001-0500, a vulnerability in the Index Server ISAPI Extension in Microsoft IIS discovered by Riley Hassell. Microsoft Security Bulletin MS01-033, released a month earlier, fixed the vulnerability. In 2001, being a month behind in Microsoft patching was not at all unusual. Tools needed to distribute patches at enterprise scale were much less common in 2001 than they are today.
Code Red contributed to the now-common practice of patching Internet-facing devices very quickly after Patch Tuesday. My then-employer used IIS extensively, and I remember reading about Code Red, not reacting to it as I had
Love Letter
. We used Code Red to justify the practice. Code Red was also a factor in Bill Gates’ now-famous security memo that created Microsoft’s Trustworthy Computing initiative and Patch Tuesday.
How Code Red worked
Code Red spread itself using a common type of vulnerability known as a
buffer overflow
. It did this by using a long string of the repeated letter ‘N’ to overflow a buffer in the IIS Index Server ISAPI Extension, allowing the worm to execute arbitrary code and infect the target with the worm. From there it spread to additional web servers. Even if the systems it attacked weren’t vulnerable, the volume of traffic from multiple infected hosts trying to spread the worm could potentially cause a denial of service.
Looking in the logs of a different web server, such as Apache, makes it easier to see how the attack worked.
Worms were possible with Apache as well
, but were less common. An Apache server attacked by Code Red would show a remote computer made the following HTTP request:
GET /default.ida?NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN%u9090%u6858%ucbd3%u7801%u9090%u6858%ucbd3%u7801%u9090%u6858%ucbd3%u7801%u9090%u9090%u8190%u00c3%u0003%u8b00%u531b%u53ff%u0078%u0000%u00=a HTTP/1.0
The worm’s payload is the string following the last ‘N’. Due to a buffer overflow, a vulnerable host interpreted this string as computer instructions, propagating the worm.
Absence of a
NOP sled
is interesting. In this case, since the size of the buffer was arbitrary and well known, a long NOP sled was unnecessary.
Who wrote the Code Red worm?
Unlike some other early viruses and worms like
Melissa
, the exact author of Code Red was never discovered in spite of an international manhunt. eEye believed the worm originated in the Philippines like the
Love Letter virus
. The claim the worm planted of sites being hacked by the Chinese was almost certainly a false flag. Some early reports attributed it to a hacking group in the Netherlands called 29a, but 29a had written a virus called Red Code, a much earlier virus that ran under MS-DOS. Although the name was similar, the two viruses were completely different in what they did and what environments they ran in.
It’s kind of like the
Max Headroom incident.
But since Code Red’s spread happened less than a year after the Internet
reached 50% of the population of the United States
, it had less fanfare and less mystique.
David Farquhar is a computer security professional, entrepreneur, and author. He has written professionally about computers since 1991, so he was writing about retro computers when they were still new. He has been working in IT professionally since 1994 and has specialized in vulnerability management since 2013. He holds Security+ and CISSP certifications. Today he blogs five times a week, mostly about retro computers and retro gaming covering the time period from 1975 to 2000.
Related stories by Dave Farquhar
