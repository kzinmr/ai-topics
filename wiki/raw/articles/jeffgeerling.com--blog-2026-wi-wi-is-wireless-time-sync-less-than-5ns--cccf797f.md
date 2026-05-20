---
title: "Wi-Wi Is Wireless Time Sync at 1 nanosecond"
url: "https://www.jeffgeerling.com/blog/2026/wi-wi-is-wireless-time-sync-less-than-5ns/"
fetched_at: 2026-05-20T07:00:49.849622+00:00
source: "jeffgeerling.com"
tags: [blog, raw]
---

# Wi-Wi Is Wireless Time Sync at 1 nanosecond

Source: https://www.jeffgeerling.com/blog/2026/wi-wi-is-wireless-time-sync-less-than-5ns/

At NAB, I found a demo of
Wi-Wi STAMP
, a wireless time synchronization protocol that
came out of Japan's NICT
.
Wi-Wi stands for Wireless 2Way interferometry, and it uses the 900 MHz band for picosecond-level time sync, and mm-level distance accuracy, in a tiny box, currently the size of a smartphone.
The system is still in development, but existing prototypes have 20ps of phase synchronization jitter, and time synchronization down to 30ns. The next generation will have time down to 5ns in real-world use.
I recorded a video on the tech with Nobu (one of Wi-Wi STAMP's co-founders) at Meinberg's booth:
I witnessed two practical applications:
Meinberg used the devices for wireless
black burst
time synchronization for two remote video cameras
.
Nobu and Ahmad demonstrated the mm-level position accuracy with a set of three Wi-Wi units, and a transmitter in a cup, playing the
shell game
(pictured below).
The graph on the laptop (to the left in the picture above) showed the X-Y position of the cup with the Wi-Wi transmitter, updating 20 times per second. The wireless range of the current system seems to be between 0.2-5 km, depending on the RF power.
Using the 900 MHz band (920 MHz in North America), signal penetration can be much better than GNSS indoors, or in spaces where running wires may be prohibitively expensive. For some other practical applications,
check out this 2024 presentation
.
There was a
lot
to see at NAB this year, and my Dad and I covered it on the Geerling Engineering channel:
The broadcast industry is changing in 2026
.
But me being the time-nut I am, I was scanning the floor for timing-related tech, and now it's ubiquitous with the adoption of SMPTE 2110 and protocols like Ravenna, Livewire, and AES67 everywhere in broadcast tech.
It's even ubiquitous enough Ubiquiti themselves are getting into the game; they had a full booth, though I didn't get hands-on with their new PTP-aware
Enterprise AV switches
.
But if you're interested in nanosecond-level wireless time sync, or want to learn why commodity WiFi setups can't support it
, watch the video above!
Note: My trip to NAB 2026 was entirely self-funded. I can work on these posts thanks to the support of
readers like you
!
