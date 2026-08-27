---
title: "Debugging Ubiquiti's 5G Backup on AT&T"
url: "https://www.jeffgeerling.com/blog/2026/unifi-u5g-backup-debugging/"
fetched_at: 2026-08-26T10:00:59.859588+00:00
source: "jeffgeerling.com"
tags: [blog, raw]
---

# Debugging Ubiquiti's 5G Backup on AT&T

Source: https://www.jeffgeerling.com/blog/2026/unifi-u5g-backup-debugging/

For a mobile 'mini homelab' project I'm working on, I wanted to use 5G Internet as a primary 'on-to-go' connection, but still have the ability to plug in another Internet connection when I put the mobile rack I'm building in a fixed location.
I'll have more on that project soon, but I figured this project was a good way to check out Ubiquiti's solutions, especially considering many of their smaller gear fits nicely within the dimensions of a
mini rack
(the 3U DeskPi RackMate TT is pictured above).
I decided to test the
UniFi 5G Backup
, which is a small PoE-powered 5G RedCap-enabled device good for up to 220 Mbps of downlink bandwidth. It takes a SIM card, and because other 5G products list AT&T and T-Mobile network support, I assumed this device would work with an AT&T Enterprise 'AIA' plan (which differs from the consumer 5G plans, and
supports 5G RedCap
).
Later on, I did notice this warning in their device FAQ:
Does the U5G support AT&T data plans?
AT&T consumer plans do not currently support 5G RedCap, which is required for U5G operation. Support may become available as carriers expand 5G RedCap offerings. For immediate connectivity, UniFi eSIM Data Packs are recommended.
I assumed the specific callout regarding
consumer
plans meant that
business/enterprise AIA plans
would still be supported. Especially since the Technical Specifications on the product page list
AT&T
alongside
T-Mobile
under 'Certifications'.
But I ran into a few issues:
The Cloud Gateway Fiber wouldn't connect to it; once I adopted it, it got stuck in an update loop. I had to put it in recovery mode then
use TFTP to upload newer firmware
—a process without a progress bar, you just have to cross your fingers and hope it works (it took about 5 minutes to transfer).
My AT&T Business 5G SIM would only work on 4G LTE, not 5G.
When I contacted my AT&T rep, he tried adding the U5G Backup's IMEI to my 5G SIM, but got the error message "The entered IMEI is not eligible for AT&T Internet Air for Business".
5G RedCap
(5G Reduced Capabilities), which is all the Quectel modem inside the U5G Backup supports, limits the maximum performance you get with a module like this, but it should be good enough for backup Internet—exactly what this device is intended for.
Except, according to
my experience
and
others
, AT&T so far doesn't support this device on their network. I guess, I'm surprised even 4G LTE works in that case, but it does.
But that limits the utility of this stick, as I'm only able to get a maximum of about 30 Mbps down and 12 Mbps up—assuming a strong signal (< 90 dBm). Otherwise the download tops out around 10-12 Mbps.
Debugging the Cellular Connection
I wanted to document how I was debugging the cellular connection on the U5G Backup for my own reference.
UI gear can be set to allow direct SSH connections. In addition, if you go into the device settings in the Network UI, there's a 'Debug' link that opens up a debug console, which drops you in as root on the device itself.
This can be dangerous, as you could potentially break things—so don't run commands willy-nilly in here.
But one of the most useful commands to see the current state of the U5G Backup is
mca-dump
. Here's some example output:
# mca-dump
{
"architecture"
:
"armv7l"
,
"gateway_ip"
:
"192.168.1.1"
,
"hostname"
:
"U5GBackup"
,
...
"mbb"
: {
"geo_info"
: {
...
"isp"
:
"AT&T Wireless"
,
"organization"
:
"AT&T Enterprises, LLC"
},
"imei"
:
"[redacted]"
,
"radio"
: {
"5g_sa_mode"
: false,
"band"
:
"eutran-30"
,
"ca_lte"
: [
{
"band"
:
30
,
"dl_bw_mhz"
:
10.0
,
"dl_earfcn"
:
9820
,
"primary"
: true,
"ul_bw_mhz"
:
10.0
}
],
...
"networkoperator"
:
"AT&T"
,
...
"rat"
:
"LTE"
,
"rat_5g_uw"
: false,
"rat_caps"
: [
"5gnr-sa"
,
"lte"
],
"rat_mode_active"
:
"LTE"
,
...
"rsrp"
:
-
95
,
"rsrq"
:
-
12
,
"rssi"
:
-
68
,
"signal"
:
3
,
"signal_percent"
:
100
,
"snr"
:
13.800000190734863
"model"
:
"U5G-US"
,
"model_display"
:
"U5G-US"
,
...
"uptime_str"
:
"28m23s"
,
"version"
:
"1.4.3.360"
}
The variable
rat_mode_active
shows
LTE
, which matches what I see in the UI. And
5g_sa_mode
being
false
might mean one of two things:
5G Standalone is not supported on the cell tower I'm connected to (i.e. it only supports 5G Non-Standalone/NSA).
My AT&T SIM is not authorized for 5G Standalone on the U5G Backup.
Since the
U5G Backup tech specs
explicitly list
FCC, IC, PTCRB, GCF, AT&T, T-Mobile
under 'Certifications', I
assumed
it was set to work on AT&T's 5G network. But that seems not to be the case.
Conclusion
The same 5G AT&T SIM in a U5G Max works fine on the AT&T 5G network, and gets speeds in excess of 500 Mbps down from the same location:
It seems the U5G Backup only fully supports 5G speeds on T-Mobile's network at this time.
I missed it at first glance, but digging through the product pages, under the "Carrier Setup Tutorials", Ubiquiti notes:
Please check with your carrier to ensure your rate plan supports 5G RedCap.
AT&T has supported 5G RedCap nationwide
for over a year, but apparently this particular device might still need approval to hop on the network.
I'm hopeful
my forum post asking about AT&T 5G support for the U5G Backup
will get some traction with the UI team. But until then, I guess I'll have to settle for 4G LTE speeds on my U5G Backup!
