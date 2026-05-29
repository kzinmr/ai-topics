---
title: "Tuning in FM Radio on a 3D Printer Heatbed"
url: "https://www.jeffgeerling.com/blog/2026/tuning-in-fm-radio-on-a-3d-printer-heatbed/"
fetched_at: 2026-05-29T07:01:24.593165+00:00
source: "jeffgeerling.com"
tags: [blog, raw]
---

# Tuning in FM Radio on a 3D Printer Heatbed

Source: https://www.jeffgeerling.com/blog/2026/tuning-in-fm-radio-on-a-3d-printer-heatbed/

Pooch
from Repkord dropped by my studio while he was in St. Louis, and asked a simple question:
Can a 3D printer's heatbed act as an antenna?
A fair question, as many an antenna is embedded in a PCB these days... and the traces on a
PCB heatbed
like the one used in Prusa's Core One look kinda like an antenna, if you squint the right way.
Really, anything (or anyone) can be an antenna, given enough power.
But to stick to the scientific method, I had my Dad come over and show me the ropes with a
NanoVNA
—a useful tool radio engineers and amateur radio operators use to measure the performance of antenna systems (among other things).
There's a video detailing the whole journey over on Geerling Engineering, and I've embedded it below:
Too long, didn't watch
If you'd rather get to the punchline, here it is:
When plugged into the NanoVNA, there were many notches on the SWR chart, like around 1 GHz, 130 MHz, and 43 MHz. They weren't well-defined, but there were definitely frequecies that seemed to be okay candidates for radio reception!
A 3D printer heatbed is designed for low resistance DC power for heating, so the traces and design are not at all optimized for RF use (either transmit or receive)
However
... if you're within a mile of a high-power FM transmitting tower (like KYKY-FM in St. Louis, which broadcasts at 30+ kW), you can pick up the signal; clear enough for stereo reception!
Now I'm wondering whether Prusa should include a headphone jack in their next printer design...
