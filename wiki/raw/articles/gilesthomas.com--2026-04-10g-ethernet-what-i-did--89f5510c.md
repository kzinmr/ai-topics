---
title: "10Gb/s Ethernet: what I actually did to get it working in my home"
url: "https://www.gilesthomas.com/2026/04/10g-ethernet-what-i-did"
fetched_at: 2026-05-01T07:13:06.205371+00:00
source: "gilesthomas.com"
tags: [blog, raw]
---

# 10Gb/s Ethernet: what I actually did to get it working in my home

Source: https://www.gilesthomas.com/2026/04/10g-ethernet-what-i-did

Archives
Categories
Blogroll
Having
learned enough
about 10Gb/s
Ethernet to be comfortable about setting it up in my
house, it was time to bite the bullet: order it from the ISP, buy some kit, and
get started.
I already had 2.5Gb/s working.  The apartment has structured cabling --
each room has one or more RJ45 sockets in the wall,
and there's a patch panel downstairs by our front door that has a matching patch socket
for each wall socket.  So when we moved in, I simply set things up so that there was a 2.5Gb/s switch
down by the patch panel, and wired everything together there.  Most of our stuff works
over WiFi, of course, but I needed a wired backbone to connect the excessive number
of computers in my study both to each other, and to the outside world.
What did I need to do?
Simplifying a bit, I had this 2.5Gb/s setup:
The ISP connection came into the apartment in the living room.
It went through a router/firewall machine I'd set up myself (more on that later),
then via a 2.5Gb/s switch to the main WiFi AP and also to a wall socket.
Down at the patch panel, I had a 2.5Gb/s switch, which was connected to the patch
socket corresponding to the router's wall socket.
Another connection from that switch went to the patch socket corresponding to the
wall socket in my study.
In the study, I had another 2.5Gb/s switch that handled internal networking.
There are a few other things dotted around, of course -- extra APs and what-have-you --
but that's the core, and I'll focus on that to keep things simple.
Would I be able to get it all upgraded to work with 10Gb/s?  The most important
question was the structured cabling in the walls; was it CAT-5E or CAT-6, or even CAT-6A?
Remember from the last post, 10GBASE-T might work over short runs of -5E (even though
officially it's not meant to be able to).  It probably would run over -6, because that's
generally OK up to 55 metres or so, and I don't think any of the runs in the house are longer than that.
And it would be fine over -6A, which is good for 100-metre runs.
I was unable to find out exactly which type I had (the
parts of the cables that are visible to me don't have any kind of marking to say),
so I decided to do a staged rollout.
The first step was to set up the wired network within my study as 10Gb/s.  There
were two important things to wire up; my primary desktop,
perry
, and a Proxmox
cluster I have running in an 11" rack.  The setup I had was just one 2.5Gb/s switch
sitting on top of the rack, linked to the wall, to the cluster machines, and to
perry
.
Now, getting the Proxmox cluster up to high-speed internal networking was a non-starter.
The machines there are all old ones -- it's essentially a retirement home for mini-PCs
I used to use for other things .  They're mostly gigabit ethernet, with one
2.5Gb/s one.
But getting
perry
up to 10Gb/s was an important goal, as that's where I do most
of my work.  I also wanted to have space for a second machine that I'm planning to
set up to do training/inference without tying up
perry
's GPU, and that would also
need fast networking.
I wanted to have things running reasonably cool (after all, the PC itself and its GPU pump out
quite enough heat already when doing a
training run
),
so DAC felt like the right way to go.
I bought a reasonably cheap managed 10Gb/s switch , a
MikroTik CRS305-1G-4S+IN
, with a single
10GBASE-T adapter to allow me to connect it to the wall socket.  I tend to name
anything on my network with its own IP, so this became
nigel
.
Next, a 10Gb/s SFP+ PCIe card -- an
Asus XG-C100F
-- for
perry
and a DAC cable to connect the two.
For the Proxmox cluster, I decided to stick with the old 2.5Gb/s unmanaged switch, a
TRENDnet TEG-S5061
.
I'd originally bought that one because it was the cheapest 2.5Gb/s on Amazon with
decent reviews, and had completely forgotten that it had one major feature --
an SFP+ 10Gb/s port for the uplink!  So another short DAC to connect that to the MikroTik,
and the study network "backbone" was 10Gb/s.
Of course, no two computers in there could actually
communicate at that speed, as only
perry
was 10Gb/s-capable -- but I could have all of the Proxmox machines talking to
perry
at the same time at full speed.  I did some tests with
iperf3
to make sure that it was
all working as expected; I couldn't test very thoroughly, but I was able to get about 4Gb/s total throughput,
which was reassuring: two machines at 1Gb/s plus one at 2.5Gb/s should
be a touch less than 4.5Gb/s.
The next step was to check the possibilities for the connection down to the patch panel.
I bought a
Ubiquiti 10G Ethernet dongle
,
and took my laptop,
laura
, down there.
The news was good!  Running an
iperf3
test between
perry
and
laura
down the
structured cabling, I was able to get just less than 10Gb/s from
laura
to
perry
,
and about 7Gb/s from
perry
to
laura
.  The slower receive speed at the
laura
end
worried me, but when I checked
ps
it became obvious what was going on.  I could see
the
ksoftirqd
kernel process running at 100%, so some single-core thing was maxing out.
The Ethernet dongle
was connected over USB, of course, and that meant it needed to do much more work on the CPU for each
incoming "data has arrived" interrupt than a PCIe card like the one on
perry
.
That meant that
laura
could only receive
data at a rate that one core could handle, which happened to be 7Gb/s.
laura
is a ThinkPad optimised for lightness and
long battery life, not CPU power, so single-core performance is not great, and it
hit a wall.
But the 10Gb/s speed in the other direction was enough to make me comfortable
that the structured cabling could
handle that speed, which was excellent news -- probably I had either short runs of CAT-6,
or CAT-6A in there, though conceivably I was just getting very lucky with CAT-5E.
The downside was the heat.  The USB dongle got too hot to comfortably hold while it was
running, and while I wasn't able to check the SFP+ module in the MikroTik during the test,
when I came back upstairs again I touched it and it was even hotter.
I decided that that was something to keep an eye on for later (and as you'll see, it
did become a recurring theme).
For now, it was time to do the rest of the upgrade.
Downstairs at the patch panel, it was a simple choice.  All of the connections were
RJ45, of course, and I only needed four.  So the
MikroTik CRS304-4XG-IN
was the obvious choice.
The final place where I needed to do some upgrades was at the ISP end.  The box that our provider
gave us had just one 10Gb/s port -- a 10GBASE-T RJ45 one.  Now, I don't generally
trust ISP routers that much, so I've always had my own router sitting between them
and the home network -- a dual-port mini-PC running a locked-down Arch installation .
My old one was dual-2.5Gb/s, so that needed an upgrade.
I settled on a
Protectli VP2440
, which has
two SFP+ 10Gb/s cages, plus two normal 2.5Gb/s RJ45s.  I didn't need the latter,
but it was the cheapest option with 10Gb/s in their range, and I've always been very
happy with their hardware and customer service.
However, I was a little concerned about thermals.  As I mentioned, the SFP+ module
in the MikroTik in the study got very hot when I did my test.  I'd need dual SFP+ modules
for the Protectli -- one for the WAN port connected to the ISP box, and the other for
the wall socket to go down to the patch panel.  Might it overheat?
The good thing about Protectli is that you can just ask them.  I dropped them a line, and
got a reply the next day from a customer support rep saying that he believed it would
be fine, but he just wanted to double-check with one of their techs.  The following day,
he followed up to say that the tech had confirmed that it would be OK.
Promising!  And because of that, plus their 30-day money-back guarantee, I decided to
go for it.
A few days later, the new router arrived.  I named it
reggie
, set it up with
my normal router Arch installation, plugged it into the ISP box and the wall...
and it worked just fine!
So the setup at this point was:
ISP box to WAN on
reggie
the router.
LAN on
reggie
to wall socket.
Patch panel socket corresponding to that wall socket to port 0 on the downstairs
RJ45-only switch,
nelly
.
nelly
port 1 to the patch panel corresponding to my study's wall socket.  (Other
ports to other things I'm disregarding for simplicity.)
Wall socket in the study to the RJ45 SFP+ module in port 0 on
nigel
.
nigel
port 1: DAC to an SFP+ network card on
perry
, my workstation.
nigel
port 2: DAC to the SFP+ 10Gb/s uplink on the old TRENDnet 2.5Gb/s switch to
handle the Proxmox cluster.
At the same time I decided to move the main WiFi AP (
winona
, a
Ubiquiti U6 Enterprise
) that
was previously next to the router over
to my study -- so that was hanging off
the TRENDnet switch.
After a bit of bedding in, I decided I wanted to move
winona
back to the same
place as the router -- it's more central so it provides better WiFi coverage from there.  So I
got another CRS304-4XG-IN -- the 10GBASE-T MikroTik
switch, like the one by the patch panel -- so that the first part of the above topology became:
ISP box to WAN on
reggie
the router.
LAN on
reggie
to the new switch (
norman
) port 0.
Port 1 on
norman
to the wall socket (thence down to the patch panel).
Port 2 on
norman
to the WiFi AP via a PoE injector.
All of this is sitting in a sideboard next to the dining table with no ventilation.
That's probably close to a pathological case for hot-running network infrastructure
like this, so... how about those thermals?
In which I consider replacing my airfryer with an SFP+ module
I like to keep track of what is going on with my zoo of computers, so I run
Telegraf
on all of them.  This
collects stats like the CPU temperature, system load, disk space, CPU and network use,
and so on.
They send this to an InfluxDB instance on a Proxmox VM (
varro
, if you're keeping track).
When I set all of this up, I also wanted to monitor the switches.  MikroTik switches
expose their stats over SNMP, so with a bit of help from various LLMs I was able to augment
the Telegraf config on
reggie
to also scrape that data and send it to
varro
.
I use Grafana to get all of this stuff into various dashboards, and one of them is
the temperatures of the networking hardware.  Firstly,
reggie
-- the Protectli
router with two SFP+ cages, each of which has a 10GBASE-T module.  I receive
separate temperatures for the CPU and for each SFP+ module:
That's not exactly running cool, but TBH it's not too bad!  I believe that the SFP+ cages
are thermally coupled to the case (which is essentially one giant heatsink).  So they're
running a bit hotter than the machine as a whole, but it's not baking.  Let's see how
that does as the weather warms -- you can see that it's been going up over the last week or
so as we had a bit of a heatwave here in Lisbon.
How about
norman
, the MikroTik CRS304-4XG-IN switch -- all native 10GBASE-T, in the
same sideboard as
reggie
?
A bit hotter than I'd like -- above the tested ambient temperature of up to 70C,
though of course this is internal rather than external;
reggie
, which is right
next to
norman
, having an internal temperature lower than
70C suggests that we're probably still OK, as its internal temperature can't be lower
than ambient.
I think that both of those could be improved, though.  The sideboard they're in is
unventilated, and it has
winona
the Ubiquiti U6 Enterprise WiFi AP in there too --
that runs pretty hot.
So a sensible first step is probably to move the AP elsewhere, and if that's not enough,
perhaps to add a USB fan to bring cooler air in through the back of the sideboard.
Now, how about
nelly
, the switch downstairs by the patch panel?  It's also in a
cupboard with no airflow, and while it's not sharing it with a router, there is a
PoE injector and another WiFi AP,
wilbur
, in there (albeit a cooler-running one, a
Ubiquiti U7 Lite
).
Not too bad at all!  Plenty of headroom there.
Finally, let's go back upstairs to my study.  If you remember, I have
nigel
there,
a MikroTik CRS305-1G-4S+IN -- a four-port SFP+ switch.  I get just data for the switch
itself and for the 10GBASE-T module -- the DACs don't report numbers.  Check
this out -- the right hand chart especially:
Yikes!  The switch itself is OK at a comfortable 48C, but that SFP+ module is hovering
around 93C.  That's internal rather than the "touch" temperature, but assuming they're close,
it's definitely getting towards blistering temperatures if you touch it.
I'm getting a stick-on mini-heatsink -- the type you can get for Raspberry Pis -- to see if
that might help.  It's also sitting on a 11" rack, so I might see if I can find a way to
thermally couple it to that.
But despite those somewhat concerning numbers, it's all working fine!
I have a periodic network test running on
perry
, checking end-to-end out to Google's
8.8.8.8 nameservers, and I haven't seen a glitch.
iperf3
tests from
perry
to
reggie
show negligible numbers of errors.
It's a working system, so naturally I want to change things.  What?
What next?
TBH, I think I'll be able to limit my desire to tinker in the short term to just
sorting those worrying thermal numbers.  For
reggie
and
norman
in the sideboard,
I think that moving
winona
the WiFi AP out again will help.  It's power-over-Ethernet,
so I can just run one wire up the wall and hide the AP itself behind some art.
For the almost-boiling-point SFP+ module on
nigel
, the study switch, a stick-on Raspberry
Pi heatsink is, as I said, probably a good starting point.  If that isn't enough,
perhaps one with a cooling fan.  The actual amount of power being used there isn't much,
just 3W or so -- it's only reaching such a high temperature because it's in such a small
space.
The more interesting question is, what will I do if and when it's time to take
the next step up, to 40Gb/s or higher?  As I said in
my last post
, 10GBASE-T is essentially
the end of the RJ45, twisted pair world we've been in for the last 20+ years.  CAT-8
cabling can, apparently, run up to 40Gb/s, but it comes with its own problems --
it's super-stiff, and hard to run around tight corners or to get into the limited
space in the boxes behind wall sockets.
I think that the right thing to do would probably be to switch to optical fibre.
I did some initial research around this while I was still unsure if the existing cabling
would work, and it seems like replacing each cable drop (that is, run from a wall
socket to the patch panel) with at least a dual-fibre cable, one to send and one to
receive, would work fine, potentially even up to 800Gb/s with the right setup.
The wall sockets could
be LC duplex, which are designed to be easy to connect (by fibre standards).
If I wanted to really future-proof things, it might even make sense to run four-fibre or
even eight-fibre cables, and leave all but two of each "dark".  That would potentially
leave even more space for improvement, and would actually cost very little extra --
the installation cost would be way higher than the cost of the cable.
Still, at hundreds of Euros per cable drop, plus project overheads, I'm glad I
don't have to do that now.  A good decision to be able to punt down the line; who
knows what will change between now and whenever my ISP starts offering even faster
speeds?
So let's wrap this up with the moment you've undoubtedly been waiting for...
The money shot
Not bad! Not quite the 10Gb/s advertised, but it's close -- and I've seen it get
up to 9Gb/s from time to time (but unfortunately not screenshotted it).  And to be clear, that was from
perry
-- so the
speed was through all three of the switches,
nigel
,
nelly
and
norman
, and
through
reggie
the router.  Direct tests from
reggie
from the CLI version of
the Ookla
speedtest
app  get similar results -- in fact, oddly, they tend to
be about 5% slower than the ones from
perry
.  Not sure what to make of that.
I'll have to investigate further, but if anyone has any ideas about what might cause
it, I'd love to hear them.
So now, when I'm uploading models to Hugging Face and downloading others,
syncing large
uv
environments, downloading the latest Arch ISO, and streaming music,
while at the same time Sara is watching Netflix
and my Dropbox is Dropboxing, everything can run smoothly.
Nice!  Mission accomplished.  I hope this was an interesting read, and perhaps
helpful for other people who are considering a similar upgrade.
Now, time for me to go back to your regularly-scheduled all-AI, all-the-time content ;-)
