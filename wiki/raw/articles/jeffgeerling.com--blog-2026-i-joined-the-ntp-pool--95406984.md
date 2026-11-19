---
title: "I joined the NTP Pool, but not with my Stratum 1 Pi"
url: "https://www.jeffgeerling.com/blog/2026/i-joined-the-ntp-pool/"
fetched_at: 2026-11-19T10:01:32.789304+00:00
source: "jeffgeerling.com"
tags: [blog, raw]
---

# I joined the NTP Pool, but not with my Stratum 1 Pi

Source: https://www.jeffgeerling.com/blog/2026/i-joined-the-ntp-pool/

Before I get
too
deep into the
time-nuts
rabbit hole, I figured I should share a little bit of the good time I now have in my studio, with everyone
else
.
Thus, I've finally joined the
NTP Pool
, offering one public Stratum 2 NTP time server (
ntp-01.jeffgeerling.com
), which gets its time from my Stratum 1 time server (
time.jeffgeerling.com
) in the studio.
My
Time Pi
is connected to an outside GNSS antenna through a
TimeHAT v6
, which I paired with a high quality timing-grade GNSS module, the
u-blox ZED-F9T
.
I posted a video about the setup today on YouTube:
I'd encourage anyone else interested in network time to contribute to the NTP Pool. However, there are some things you should know before contributing your own time services:
Time Commitment
You don't need to go all out with a timing-grade GNSS module like I'm using. Heck, you don't even need GNSS-backed time at all!
The main requirements for hosting a node in the global NTP pool are:
Keeping the system online (servers are only made active in the pool if they're online and serving good time consistently for a long period)
Maintaining a good time—which can mean Stratum 1 GNSS service, but could also mean pulling time from a few other reliable time servers, and running as Stratum 2 or 3
A stable IP address (IPv4 and/or IPv6), and a long-term commitment
Just 'testing the waters' in the Pool wastes resources—when you bring a new server online, it will take at least a few hours just to spin up all the tests to verify the server's providing a good time.
If you just want to operate your own time server, that's fine; the NTP Pool is a shared global resource, so joining it is a
little
more of a commitment.
Two other important caveats:
Your NTP server's IP address will be public
NTP traffic will slowly decay, and some misconfigured systems could take months or even
years
before they'll stop sending NTP traffic at your IP
The first caveat matters a lot to me: back when I exposed my home IP address trying to self-host this website on a cluster of Raspberry Pis,
some doofus decided to DDoS my website
—and was persistently doing so for the better part of a month.
I had to
cycle my home IP
, then put my site behind Cloudflare, just to protect my poor Pis (and eventually the VPS I now host it on).
Secure and Measurable Time
For those reasons, I chose to have two layers to my public time services:
Stratum 1
: I have my Time Pi running in the studio, running a WireGuard tunnel to:
Stratum 2
: A VPS I host with a cloud provider in St. Louis, to keep the latency down (ideally with fewer hops across the Internet, which leads to better time sync via NTP)
I include the Stratum 2 time server in my Stratum 1 time server's
chrony
config as a
noselect
source, so I can easily compare the Internet delay between the two servers, outside the WireGuard tunnel:
server ntp-01.jeffgeerling.com noselect
This provides me with the following graph:
I've been tracking my time in comparison to an NTP time server hosted at WWV in Ft. Collins, CO (pictured below), one of NIST's NTP servers in Boulder, CO, and Cloudflare.
For typical NTP configurations, you shouldn't single out time servers like this; I'm only doing it for long-term measurement (and I only poll the servers every 1024 seconds). Most systems should use pool addresses,
as documented here
.
The line for Cloudflare steps up and down sometimes, most likely due to BGP routing: as routes and servers change, packets between St. Louis and
time.cloudflare.com
can take very different paths there and back.
Note: You might be looking for info on NTS, or
Network Time Security
—I haven't explored it much, so expect more on that at a later time. Currently the NTP Pool doesn't support NTS, though
some have experimented with it
. I'm okay with basic NTP and would recommend anyone with critical timing needs to use other time sources as well (don't
only
rely on NTP!).
Chrony and GPS time tweaks
My Time Pi is not only serving as a Stratum 1 timing reference for my public NTP server, it's also my primary reference for local time in the studio.
The TimeHAT on top does most of the heavy lifting, with its built-in Intel i226 NIC. The i226 includes hardware timestamping, essential for accurate PTP timing on the LAN. To deliver the most accurate time possible, I installed a timing-grade GNSS receiver (u-blox ZED-F9T, built to the
M.2 NGFF Sync Module
specification.
The entire configuration (for both servers) is managed by Ansible in my
time-pi
project.
Using the i226, I'm able to discipline the NIC's hardware clock (called the 'PHC', or 'PTP Hardware Clock')
in hardware
, directly from the GPS module's PPS (Pulse Per Second) pin. Using linuxptp's
ts2phc
tool, I can discipline the PHC to within tens-of-ns of UTC, and distribute that time to other PTP-aware computers on the LAN.
The time on the PHC is shared to my Pi's system clock using
refclock PHC
inside Chrony, instead of
phc2sys
, because I was experiencing a weird 200ms jump every so often. Chrony then disciplines the system clock, but this can only be accurate to about a microsecond, because the pulse goes through the PCIe bus, which adds latency I can't measure.
I'm actually trying to make this latency more measurable, since GPIO is routed through the RP1 chip deterministically. See
ahmadexp's rp1-ptp-pps utility PR
.
PTM
could reduce the error between the NIC's PHC and the system clock to a few ns, but the BCM2712 SoC on the Pi doesn't support it.
One other quirk I ran into was Debian's default
sourcedir /run/chrony-dhcp
directive, which was picking up another NTP server via DHCP, causing
chrony
to stampede my
extremely
accurate GNSS-derived time from
phc2sys
with a far-less-accurate time from a public NTP server! (This was another motivation behind moving clock steering to
chrony
instead of
phc2sys
.)
Time for an Outage
I'm hosting my public Stratum 2 server with
Oxtrys
, a VPS provider I'd never used before—and one thing I was nervous about was how they'd react to a VPS handling only UDP packets like this.
Some automated firewalls shut down public NTP servers because NTP traffic may
look
like abuse. I wondered if that was the case late on the night of November 16, because the server dropped offline
while I was writing this blog post
:
But looking at the logs further, it seems an unattended upgrade installed a new Debian kernel, then rebooted the server, and the new kernel caused problems. For now the server still runs automatic upgrades, but leaves reboots to me.
Oxtrys' live chat support has been responsive enough, though their account dashboard is broken until November 22, so it doesn't list my server's out-of-band management options.
As you can see in the graph above, the NTP Pool monitors have slowly brought the server's score back up past '10', at which point it can serve time in the pool again. It takes maybe 6–12 hours to recover if the server's been down long enough.
Conclusion
I've certainly learned a lot at every stage of this journey: NTP is loaded with utility, and is currently an essential piece of global timing infrastructure. I think I know about 1% (probably less) of what there is to know about hosting a public NTP server, and hopefully I can share more as I increase that to a few more percentage points!
I'm thankful to all the other NTP Pool operators, as well as all the timelords who built and manage massive NTP endpoints like
time.apple.com
,
time.cloudflare.com
, etc.
