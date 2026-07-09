---
title: "The Special Value Pi 4 was extremely short-lived"
url: "https://www.jeffgeerling.com/blog/2026/special-value-pi-4-extremely-short-lived/"
fetched_at: 2026-07-09T07:01:31.566159+00:00
source: "jeffgeerling.com"
tags: [blog, raw]
---

# The Special Value Pi 4 was extremely short-lived

Source: https://www.jeffgeerling.com/blog/2026/special-value-pi-4-extremely-short-lived/

The 'Special Value' Pi 4 pictured above is probably the rarest Raspberry Pi I own—even rarer than my
blue special edition Pi
.
A Raspberry Pi reseller
briefly listed a special 'value edition' Pi 4
. But the product page 404's now. While it was up, my curiosity got the better of me, and now I have two 'value' Pi 4s.
What makes them a 'value'? They're only certified to run at 1.25 GHz (retail Pi 4s run at 1.8 GHz, and can usually be overclocked).
The price for the 4GB edition was $89—before shipping and tariffs. All-in, I paid $160 to get it to my door. If I run over to Micro Center and grab a 4GB Pi 4 off the shelf, it's just
$94.99 plus tax
.
What a savings
...
Note
: The 1 GB Pi 4 is still $35, at least at Micro Center — however, higher-memory SKUs have gotten eye-wateringly expensive, with the 16GB Pi 5 hitting $299!
But what do you get, when you buy the world's slowest Pi 4?
This blog post is a lightly-edited transcript of the following video:
Inspecting with camera closeup
Comparing it closely with one of my retail Pi 4s, I couldn't find
any difference at all
. The main chip markings are the same, the board is marked the same, both are made in the UK...
The only discernible difference is the LPDDR4 DRAM package, which is different because Raspberry Pi's had to scramble (like everyone else in the hardware business) to find stock for new boards. (Even with older hardware, I've seen Pis use multiple RAM vendors, so this isn't a big deal.)
The 8GB model had an older
B0 stepping
, which is the same as my oldest retail Pi 4s, but there's still B0 stock here and there.
Externally, there's
nothing
different about these 'value' boards. That's probably why the listing was pulled.
Could you imagine, people buying up binned Pis,
some which could actually run at 1.8 GHz, but were never validated for that clock speed
, and then reselling them as normal Pis? Not great for the end user.
Benchmarking - Power and Performance
I didn't know what to expect booting one up, but I put Pi OS on a microSD card, and it booted right up, and ran at 1.8 GHz.
I don't know what I was expecting, but certainly not for it to run at 1.8 GHz. Maybe that's a lesson that even if something's binned, that doesn't mean it can't run
at all
at the higher clocks, just that it didn't pass whatever validation Raspberry Pi runs at the factory.
So I plugged in the 8 GB, and in this case, I got kernel panics and clock speed errors. I modified the Pi boot config to force the arm cores to 1.25 GHz, and it booted up fine.
Running at that speed, everything worked, just... slightly slower than a regular Pi 4.
Power consumption was different than expected, though. This Pi used
3W
at idle. Most Pi 4's I've tested idle at less than 2W.
To find out why, I asked a Pi engineer.
Binning for Industry
He said they
'bin' hardware
, something every manufacturer does. He said less than .01% of Pis they build don't test at normal voltages and frequencies, so they put them aside.
It sounds like they can separate those out and sell batches to specific industrial customers
who know what they're getting into
. That saves them from e-wasting small batches of failed Pis, and gives some partners a slight discount.
But for every Pi, there's dynamic adjustments to the chip voltage, that's part of DVFS, or
Dynamic Voltage and Frequency Scaling
. For lower-binned chips, the Pi might actually need to
raise
the voltage to hit acceptable performance, even at lower clock speeds (thus higher power draw at a given clock).
For better chips, they can run at default clocks using even a little less power. Using DVFS, the Pi's firmware can normalize the performance across all Pis. So even with retail Pis, one Pi might be
just slightly
more efficient than another.
That's why
some
of my Pi 5s
I can overclock to 3 or even 3.4 Gigahertz
. But other ones can't even get to 2.6. It's just the silicon lottery, and this strange Pi gave me a peek behind the scenes into one area of parts binning I never thought about.
I have
all my benchmarks up on GitHub
and I'll link to them below, but all that to say, I'm not a silicon engineer, so take everything I'm saying here with a grain of sodium chloride.
