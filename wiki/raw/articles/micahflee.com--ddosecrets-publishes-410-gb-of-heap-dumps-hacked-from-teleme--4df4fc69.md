---
title: "DDoSecrets publishes 410 GB of heap dumps, hacked from TeleMessage's archive server"
url: "https://micahflee.com/ddosecrets-publishes-410-gb-of-heap-dumps-hacked-from-telemessages-archive-server/"
fetched_at: 2026-04-30T07:01:56.992586+00:00
source: "micahflee.com"
tags: [blog, raw]
---

# DDoSecrets publishes 410 GB of heap dumps, hacked from TeleMessage's archive server

Source: https://micahflee.com/ddosecrets-publishes-410-gb-of-heap-dumps-hacked-from-telemessages-archive-server/

This morning, Distributed Denial of Secrets
published
410 GB of data hacked from TeleMessage, the Israeli firm that makes modified versions of Signal, WhatsApp, Telegram, and WeChat that centrally archive messages. Because the data is sensitive and full of PII, DDoSecrets is only sharing it with journalists and researchers.
There's a lot of background, so here's a quick timeline of events with relevant links:
March: Then-national security advisor Mike Waltz
invited
a journalist into a Signal group where they planned
war crimes
. This led to Congressional
hearings
about Trump officials using Signal groups to discuss classified information.
May 1: Waltz (the day he was demoted from position of national security advisor) was photographed using TM SGNL, a modified version of Signal made by TeleMessage. He had texts up with Tusli Gabbard, JD Vance, and Marco Rubio.
May 3: I
published
the source code of the TM SGNL to GitHub.
May 4: TeleMessage got hacked, which I
reported
in 404 Media with Joseph Cox.
May 5: TeleMessage got hacked again by someone else, as NBC News
reported
.
May 6: I
published analysis
of the TM SGNL source code, along with some of the hacked data, that prove the TeleMessage lied about its products supporting end-to-end encryption.
May 18: I
published details
about the TeleMessage server's vulnerability in WIRED.
TLDR: if anyone on the internet loaded the URL
archive.telemessage.com/management/heapdump
, they would download a Java heap dump from TeleMessage's archive server, containing plaintext chat logs, among other things.
Now, DDoSecrets has published 410 GB of these TeleMessage heap dumps. Here's the DDoSecrets description of
the release
:
Thousands of heap dumps taken May 4, 2025 from TeleMessage, which produces software used to archive encrypted messaging apps such as Signal and WhatsApp. The service came to public notice in 2025 when it was reported that former national security adviser Mike Waltz used TeleMessage while communicating with members of the Trump administration, including Vice President JD Vance and Director of National Intelligence Tulsi Gabbard. TeleMessage has been used by the federal government since at least February 2023.
Some of the archived data includes plaintext messages while other portions only include metadata, including sender and recipient information, timestamps, and group names. To facilitate research, Distributed Denial of Secrets has extracted the text from the original heap dumps.
It seems that the SignalGate saga of staggering incompetence is not yet complete. I'm digging into this data right now. It's bonkers.
Note: I'm a member of the DDoSecrets collective. If you can,
donate
! DDoSecrets operates on a shoestring budget and does incredibly impactful work.
Sign up for micahflee
Hi, I'm Micah. I'm a coder, a journalist, and I help people stay private and secure.
No spam. Unsubscribe anytime.
