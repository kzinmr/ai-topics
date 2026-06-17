---
title: "10Gb/s Ethernet: switching to a Broadcom SFP+ module"
url: "https://www.gilesthomas.com/2026/06/10g-ethernet-switching-to-broadcom-sfp-plus"
fetched_at: 2026-06-17T07:01:20.273230+00:00
source: "gilesthomas.com"
tags: [blog, raw]
---

# 10Gb/s Ethernet: switching to a Broadcom SFP+ module

Source: https://www.gilesthomas.com/2026/06/10g-ethernet-switching-to-broadcom-sfp-plus

Archives
Categories
Blogroll
Posted on 16
June 2026
in
TIL
,
Gadgets
Back in April
, I upgraded my home LAN to 10Gb/s.
The in-wall cabling is CAT-6 or similar, so I had to use 10GBASE-T.  Now, the router
I'm using, and the switch in my study, provide 10Gb/s through SFP+ cages; that meant
that they needed 10GBASE-T SFP+ modules in order to connect.
That kind of module is known to run hot -- sometimes too hot to actually work.  The
modules in
reggie
, the router, appeared to be running OK (see the linked post above
for charts), but the one in
nigel
, the study switch, was a worrying 93C.  I tried
sticking some mini-heatsinks on it
, which
seemed to help a bit.  But the weather got warmer, and eventually the module overheated.
I lost access to the Internet from the study, and checking the metrics showed me this:
You can see that it's "flapping": the temperature gets up to a level where the module
shuts itself down for its own protection -- about 95C, I think -- and then when it
has recovered, it switches on again, the temperature rises, and the process repeats.
I was able to work around the problem by switching on the air conditioning in the study.
But normally I only have it on when I'm in there, and keeping aircon on 24/7 just to keep
the network working felt like the wrong solution.
It was time to switch to a more power-efficient SFP+ module.
My original 10Gb/s post had quite a lot of discussion
on Hacker News
,
and
xxpor
mentioned that there are two generations of 10GBASE-T SFP+ modules:
old ones using a Marvell chip, and newer ones using
one from Broadcom.
blunden
on the ServeTheHome forums
made the same point.  The Marvell-based ones were known to run hot, and they both recommended
finding Broadcom-based ones.
I'd confirmed that the
MikroTik S+RJ10
that
I had in
nigel
was indeed a Marvell one, so the solution was pretty simple: get a better one.
So I went on Amazon and picked up
a 10Gtek ASF-10G-T80-INT
.
Checking
10Gtek's own page on that module
confirmed that it used the right kind of chip (although it was a little bit garbled):
10Gtek's ASF-10G-T80 is a newest version copper transceiver, its biggest feature
  are ultra lowpower consumption and longer transmission distance
  (1.6W C10Gbps 30m，2.0W 110Gbps 80m). ASF-10G-T80 is a 10GBase mult-rate Copper
  RJ45 SFP+ transceiver, designed in with BROADCOM BCM84891 PHY chip following
  IEEE 802.3an/az and SFP+ MSA, supporting up to 80-meter transmission over CAT.6a or CAT.7.
A day or two later, it arrived.  It came in a rather pretty little metal case:
Installing it took a little while, because I found removing the existing MikroTik
module tricky;
Willie Howe's video on YouTube
helped quite a lot in showing how to disengage the latch, but I still needed to fiddle around with it quite a bit to get it out.
However, that was eventually done, and the new module went in.
I plugged all of the network cables back in, switched on the switch, and (after
a slightly nerve-wracking wait for it to boot up) the network was back up and running!
So, were the temperatures any better?  I checked my monitoring, and:
Huh, nothing was being reported.
That made sense, though.  The way I was charting those numbers was that the switch
exposed them over SNMP, and then the
Telegraf
daemon on my router,
reggie
, read the numbers and sent them to
InfluxDB
;
finally,
Grafana
did the charting.
I'd been reading the module temperatures in using the SNMP OID that I'd identified
that the switch was providing them on (
.1.3.6.1.4.1.14988.1.1.19.1.1.6.3
if you're interested),
but perhaps the new module was published on a different OID.  It was time to log
in to the switch and take a look.
[admin@Nigel] > /interface ethernet monitor sfp-sfpplus1 once
name: sfp-sfpplus1
status: link-ok
auto-negotiation: done
rate: 10Gbps
full-duplex: yes
tx-flow-control: yes
rx-flow-control: yes
supported: 10M-baseT-half
10M-baseT-full
100M-baseT-half
100M-baseT-full
1G-baseT-half
1G-baseT-full
1G-baseX
2.5G-baseT
2.5G-baseX
5G-baseT
10G-baseT
10G-baseSR-LR
10G-baseCR
sfp-supported: 1G-baseX
10G-baseSR-LR
advertising: 1G-baseX
10G-baseSR-LR
link-partner-advertising:
sfp-module-present: yes
sfp-rx-loss: no
sfp-tx-fault: no
sfp-type: SFP/SFP+/SFP28/SFP56
sfp-connector-type: LC
sfp-encoding: 64B/66B
sfp-link-length-om1: 30m
sfp-link-length-om2: 80m
sfp-link-length-om3: 300m
sfp-vendor-name: Intel Corp
sfp-vendor-part-number: FTLX8571D3BCV-IT
sfp-vendor-revision: A
sfp-vendor-serial: IN101Q14436
sfp-manufacturing-date: 26-01-31
sfp-wavelength: 850nm
eeprom-checksum: good
eeprom: 0000: 03 04 07 10 00 00 00 00  00 00 00 06 67 00 00 00  ........ ....g...
0010: 08 03 00 1e 49 6e 74 65  6c 20 43 6f 72 70 20 20  ....Inte l Corp
0020: 20 20 20 20 00 00 1b 21  46 54 4c 58 38 35 37 31      ...! FTLX8571
0030: 44 33 42 43 56 2d 49 54  41 20 20 20 03 52 00 85  D3BCV-IT A   .R..
0040: 00 1a 00 00 49 4e 31 30  31 51 31 34 34 33 36 20  ....IN10 1Q14436
0050: 20 20 20 20 32 36 30 31  33 31 20 20 00 f0 03 96      2601 31  ....
0060: 00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  ........ ........
It's saying that it's an Intel module; that in itself is
not all that odd -- there are frequently compatibility issues between switches and SFP+
modules, so sometimes modules are configured to "lie" about which manufacturer made
them -- and I'd specifically bought the "Intel-compatible" one on Amazon, the
ASF-10G-T80-INT
,
because I couldn't find one that pretended to be MikroTik.  Research had suggested that
it would work OK, and it did.
But the really odd bits were these:
sfp-connector-type: LC
sfp-wavelength: 850nm
sfp-link-length-om1: 30m
sfp-link-length-om2: 80m
sfp-link-length-om3: 300m
sfp-vendor-part-number: FTLX8571D3BCV-IT
Not only was it impersonating an Intel module -- it was saying that it was a
fibre-optic one
!
Perhaps if I had found the "MikroTik-compatible" option it would have been better --
though, equally, it might have just impersonated a MikroTik fibre module anyway.
Anyway, it was working -- so that was OK.  But there was some bad news.  If the switch
was able to read a temperature from the new module, then you'd expect it to appear in that
output, as
sfp-temperature
.  So, sadly, I don't think I'll be able to monitor the temperature
of the new module.
How could I tell whether it had helped, then?  Well, one thing would be to simply
see if there are any further instances of network flapping.  I actually did the
replacement just over two weeks ago, and everything has been fine as far as I can tell
from using it and from the other monitoring (despite another hot week last week).
But another interesting metric is the CPU temperature for
nigel
over the two
weeks before and after the module change:
You can see that there was a real drop-off late on 1 June, when I switched the modules, and it has been running about 5C
cooler since.  Of course, there's a lot that's different about the new module -- as
well as having a different chipset and a mendacious EEPROM, it's likely to have different
thermal coupling characteristics -- it might be shedding more or less of its heat to the
SFP+ cage and thence to the switch's CPU.  So it's not proof of anything, but in
combination with the improved link stability, I'll take it as a win.
So, an interesting little excursion into the world of SFP+ modules -- in particular,
slightly dodgy ones :-)   Let's see if this one holds up better as we go through the
toasty Lisbon summer.
