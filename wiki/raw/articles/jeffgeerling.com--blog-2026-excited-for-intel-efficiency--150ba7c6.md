---
title: "I'm excited for Intel after testing the XPS 13"
url: "https://www.jeffgeerling.com/blog/2026/excited-for-intel-efficiency/"
fetched_at: 2026-08-08T10:13:47.214186+00:00
source: "jeffgeerling.com"
tags: [blog, raw]
---

# I'm excited for Intel after testing the XPS 13

Source: https://www.jeffgeerling.com/blog/2026/excited-for-intel-efficiency/

Shortly after Apple launched the budget
MacBook Neo
, Dell announced their response, a new low-end
XPS 13
.
Matching the Neo's
current
pricing, it starts at $699, or $599 with an educational discount. That discount is currently set to expire on November 2, and with the current component pricing insanity, I'd be surprised if we don't see a price increase on both laptops by next year.
I ran the XPS 13 through my
gauntlet of benchmarks
, and published a review on my YouTube channel:
Some headline improvements over the Neo:
Higher-resolution touchscreen display, with a more matte finish
Backlit keyboard (includes a CoPilot button, ick)
Both USB-C ports are 10 Gbps with DisplayPort and PD
Base storage is 512GB, the included SSD is faster than the Neo's built-in storage,
and it's upgradeable
(2230-sized NVMe).
Linux support is specifically not advertised, but I was able to get all hardware functionality working in Fedora 44, including WiFi 7 (I had to plug in a USB Ethernet adapter temporarily to run
dnf upgrade
)
A few things are worse, of course:
The top-hinge trackpad makes it hard to click anywhere besides the bottom (tap to click is fine anywhere)
The built-in webcam and microphone are a bit lower quality
Sound from the built-in speakers is noticeably worse
There's no headphone jack
It only
officially
supports Windows 11 (and comes with Home)
Watch the video for opinions on the laptop itself.
In this blog post, I thought I'd dive deeper into the most interesting part
for me
: the Intel Core 5 320.
Intel Core 5 320
Intel's had a string of decent low-end SoCs, incorporating a CPU, GPU, and more recently, NPU. At the lowest end, the N150 and N350 match or surpass midrange Arm SoCs, while keeping the wide x86 compatibility Intel's known for.
These chips are the reason many Mini PCs became viable sub-$200 options for homelabs and low power utility computers (at least until DRAM prices torched everything).
But the
Core 5 320
inside—one of Intel's new low-end Wildcat Lake chips—is the first x86 chip that's scored in the top 10 of my
HPL FP64 efficiency benchmark
.
In fact, it's number two, second only to the M4 Mac mini!
This surprised me, because I'd never seen an x86 system (laptop, desktop, or server) approach even 4 Gflops/W of efficiency in this specific benchmark. The next-best x86 system
I've
tested, one with Intel's slightly-older 265K chip, came in at 2.71 Gflops/W.
And idle power consumption is wildly improved, too—the XPS 13 would only use 0.5-0.8W at idle with the display turned off, matching the MacBook Neo. That bumps up to 3-4W with the display on at 50% brightness, and add 1-3W for WiFi activity and video playback.
Conclusion
Obviously, all this efficiency is on the low end—the laptop only achives a little over 120 Gflops, while Apple's faster M3 and M4 Macs are pushing through up to 1.2
Teraflops
.
But these new cores paired with Intel's power management tweaks, are exciting. I can only hope they'll push through the same efficiency to dense-core-count server chips, and low-end IoT chips in < 10W TDPs.
That is, if the product managers can get it through that efficiency matters more than pushing clocks to their extreme.
Better efficiency targets lead to:
Lower cooling requirements (for slower fans, or none at all, as in the MacBook Neo's case)
Lower power consumption (better battery life or more compute density with lower power requirements per rack)
Chips that don't
burn themselves out
Intel's built-in graphics don't hold up nearly as well as the CPU side of these low-end SoCs, though—at least compared to Apple.
But I'm glad competition has spurred the market to better solutions, especially in an affordable laptop.
