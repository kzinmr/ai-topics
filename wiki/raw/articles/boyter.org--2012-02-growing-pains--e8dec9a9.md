---
title: "Ben E. C. Boyter"
url: "https://boyter.org/2012/02/growing-pains/"
fetched_at: 2026-05-05T07:02:05.742630+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Ben E. C. Boyter

Source: https://boyter.org/2012/02/growing-pains/

Growing Pains
2012/02/06
(315 words)
When I started searchco.de the amount of hardware required was fairly low. I did a lot of processing on other machines and pushed the results through allowing the machine that serves the site to just focus on the job of delivering results. The result was everything was running on a nice VPS provided by Atum.com 2.9 Ghz CPU 512 MB ram and about 30 GB of hard disk space. This was more then enough to support the index I had and do everything required. Then Google dropped Code Search and I decided I would try to fill in the gap.
My inital implementation which is live now has about 1.2 billion lines of code indexed. As you can imagine this pushed my little VPS to the limits. With some compression I got the indexed code itself reduced to about 12 GB on disk but the index itself was another story. The index of the code itself was well over 60 GB in size. I upped the size of the hard disk by 200 GB as a stopgap measure.
However the previous change was just a stopgap. As of last night I have greatly increased the size of the index by a factor of 2-3x (final counts to come). This naturally increases the size of things on disk and adds some additional strain to the CPU and ram. Because I need massive amounts of storage, cpu, ram and network traffic to continue to expand the index I have moved over to a dedicated server with 32x the amount of ram 8x the CPU and 15x the hard disk space. This will also allow me to start with realtime index updates in the coming weeks which should keep things running smoothly.
Anyway take it for a spin. The index is far larger now with more projects indexed and the speed should be much faster across the board.
