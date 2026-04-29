---
title: "10Gb Ethernet: what I had to (re)learn"
url: "https://www.gilesthomas.com/2026/04/10g-ethernet-what-i-relearned"
fetched_at: 2026-04-29T07:00:51.669235+00:00
source: "gilesthomas.com"
tags: [blog, raw]
---

# 10Gb Ethernet: what I had to (re)learn

Source: https://www.gilesthomas.com/2026/04/10g-ethernet-what-i-relearned

Archives
Categories
Blogroll
My ISP recently started offering a 10Gb option, and my "shiny new thing!" Pavlovian
response immediately kicked in.  So of course, I
had to upgrade the wired networking in my home -- which meant I had to learn a few things to get
it all working, and relearn a bunch of stuff I'd forgotten over the years.
Wired networking for home and small offices hasn't really moved forward that much in the last 20-odd years.
Back in 2006, gigabit Ethernet was standard for businesses, and most home users moved
to it not long after.  Perhaps due to the rise of WiFi for most "last few metres" connections,
it's pretty much stagnated there, perhaps with a bit of a push towards 2.5Gb/s more
recently.
But with faster ISP connections arriving, I think things are starting to become
a bit more interesting.  Even the fastest WiFi 7 connections are only able to get up
to around 6Gb/s to a single device -- and that's in an ideal "super-fast machine sitting right next
to the AP in a shielded lab" setup.
Here's what I had to drag up from my memory, and the new stuff I had to learn, in
order to get this all working.  I'll write about the background in this post, and
then tomorrow I'll post about what I actually put in place.
A bit of history
Let's start with a bit of the backstory.  Bear with me, it's not just self-indulgent
reminiscing!
When I first started using networked computers, back in the early 90s, the most popular
standard was
10BASE2
.  We had this in the first
office that I worked in, and in the university computer labs.  In the back of your
computer, you'd have a T-shaped connector like this:
© Raimond Spekking /
CC BY-SA 4.0
(via
Wikimedia Commons
)
The end facing the camera in that photo was the bit that went into your computer.
Computers were daisy-chained together; you might have a server connected to workstation
one, workstation one to workstation two, and so on, until you reached the last workstation.
You'd have to cap the unused end of the T connectors at each end of the chain with a special terminator.
Essentially it was a single coaxial cable, so every computer saw every
bit that was sent along the bus.  In turn, that meant that everyone was sharing the same bandwidth, a meagre
10Mb/s.  The cool thing about Ethernet (compared to older networking technologies) was
that the computers shared it without any need for coordination -- if two of them started
"speaking" at the same time, they'd notice, and stop.  They would then start again after
a random back-off, so one of them would randomly wait for less time than the other and
start first.  The other would notice that "the line was busy" and would wait again for another
chance.
Of course, this limited the number of computers you could have on one network, as past
around 20 or so, they'd spend all of their time interrupting each other and never actually
be able to send anything -- and anyway, sharing 10Mb/s across a large number of computers
would be an issue.  On top of that, there was a hard cap of 30 machines per network.
You'd use more specialised networking equipment to link
different networks together -- bridges, switches and routers.  More about switches later.
By the time we started setting up networking in a house that I shared with friends,
in around 1996 or so , the most popular option had changed: now people were using
10BASE-T.  Still 10Mb/s, but using the RJ45 connectors and twisted-pair cables that we've come to know and love.
All of the computers would have a single cable going to a hub, in a star topology.
You might link multiple hubs together to build larger networks.
However, these
hubs were still little more than a convenient form factor to electrically link all
of the wires together into a single bus.  You still had the problem that every computer could see
every bit on the bus, and the same bandwidth-sharing and limits with the number of computers that you
could handle as a result.
Over the years after that, things moved on.  Switches had been relatively expensive
things; they would be used to interlink hubs, or 10BASE2 networks.  They would learn (from seeing the
source MAC address on incoming packets) which machines were sending to each of their ports,
and use that to know where to send packets that came in on other ports.  If, say, a switch
learned that addresses A, B, and C were on port 1, then if a packet for one of those machines
came in on port 2, it would know it could just send it out on port 1 and not on the others.
That helped to address the bandwidth-sharing and the problems with collisions.
Prices for switches got lower and lower, and eventually -- I think sometime between 2005 and
2010 -- they became so cheap that
there was little point in bothering with hubs -- you'd just connect every computer
directly to a switch.  That meant that any two computers on the same switch
could talk to each other at the full network speed, as packets would just be
switched from port to port .  The connections between switches were still a bottleneck, of course,
but that was much less of a problem.
At the same time, speeds increased, from 10Mb/s
to 100Mb and then finally to 1Gb/s, which was standard for business machines by 2005 or so --
I remember that when we bought our first computers for Resolver Systems back then, that's what they
came with by default.
Home computers weren't far behind -- and that's where we've been ever since.
ISPs and larger networks: the move to SFP
Back to that bottleneck between the switches.  Even back in the days of 10Mb/s
networks, if you were managing a larger network, you would want a faster network to interlink them -- so, for example, if
two computers on the same switch both wanted to access some external resource, they
wouldn't be competing for the same 10Mb/s uplink.  Once you went past small office-sized
networks, that kind of thing started becoming important.  ISPs and datacenters, of course,
had the same problem in spades.
What you would need was an uplink on the switch that could run at a faster data rate.
So even when 1Gb/s Ethernet was too expensive for the connections to the computers themselves,
you might have a switch with a 1Gb/s uplink to connect it to the larger network,
and a bunch of 100Mb/s ports for the local stuff.
Additionally, for larger networks you would have another problem -- physical
distance.  All of these RJ45-based networking technologies had a maximum cable length
of 100m.  You could extend that by putting a repeater (or even just a switch) every 100m or so as a "signal booster" --
but if, for example, you wanted to link two buildings, that could be tricky.  You'd
need to run both the data cable and power, and you'd need to have some way of getting
access to the repeaters if they went wrong.
Ethernet over fibre optic connections had been a standard thing for years, though, and
it had much better range -- for single-mode, many kilometers.  So while it was too fiddly for LANs,
it made great sense as a backbone technology.
What that meant, though, was that in order to set up some particular network topology,
you might wind up having to get a whole bunch of different switches.  For short connections
between two of them, you might use an RJ45 uplink connection, while for longer ones you
might want fibre.  More complex topologies might need some entirely different mix of
ports.
To make this worse, there were a bunch of different fibre optic standards -- multi-mode
and single mode fibres, different connectors, and so on.
Rather than manufacturing a large range of different kinds of switches with all of the
combinations that people needed, manufacturers
separated out the physical layer of the transport from the switching hardware.  A switch,
instead of having specific RJ45 or fibre connectors for its ports, would have Small
Form-factor Pluggable (SFP) "cages", essentially a new kind of socket.  These allow people to mix and match different kinds of
transceiver modules, which would slot into the cage to provide an actual usable interface  -- one for RJ45 for gigabit Ethernet, or one for the particular
kind of fibre connection they were using -- whatever configuration worked best for them.
A typical switch for a larger network might have one or two of those for backbone
connections, and then RJ45s for local connections.  Over time, gigabit backbones
were no longer enough, and SFP was followed by SFP+, which could handle 10Gb/s.
Since then, there have been extensions for even faster speeds, way up to hundreds of
Gb/s.
Back in the day, this stuff was only important to network admins for medium-sized networks and larger,
of course.  But now, 10Gb Ethernet means that we've now hit the point where it matters
even for home users, and that's because of thermals.
10GBASE-T is so hot (right now)
Here's the problem.  Somewhat loosely speaking, the faster a network connection on a particular
kind of wiring, the hotter it runs.  Over an RJ45/twisted pair connection, 10Mb/s Ethernet basically shed no heat, 100Mb/s
a little more, even gigabit Ethernet just left your switches somewhat warm.
The jump up to 10Gb over RJ45, called 10GBASE-T, makes things decidedly toasty --
you'll see just how toasty in tomorrow's post.
There's also the issue of cabling.  Because network speeds have been stable
for some time -- Gigabit Ethernet being the standard for ~20 years --
most buildings with structured cabling (the kind of thing where there are RJ45 sockets
in the walls wired together) will have the standard for that -- CAT-5E.  Unfortunately 10Gb/s Ethernet
won't officially work over it -- you might be lucky, especially with short cables,
but in general it won't work, or if it does it won't be reliable.
CAT-6 cabling helps -- it can handle 10Gb/s over runs up to about 55 metres.  And
the ideal is CAT-6A, which can handle 10Gb/s over the same 100 metre cable lengths
that you'd expect for the older, slower setups.
What this meant was that an interim standard was created.  10GBASE-T is hot and needs
cables that people don't necessarily have, especially when you're talking about what's
installed in the walls of their building.  But if you run it a bit slower, you can
do so over older cables and without melting them.
That's why I didn't mention 2.5Gb/s Ethernet earlier (or indeed the rarer 5Gb/s).
They were introduced as slowed-down versions of 10Gb/s to get it to work on existing
infrastructure without major upgrades.  And that's great, right up until the point
your ISP emails you to say that they're offering 10Gb/s to your home now...
So, what can you do to run 10Gb/s without melting things?
SFP+, DAC, fibre
Let's think about what an SFP or SFP+ module actually is.  It slots into a cage on a
switch.  On one side, there's an electrical connection to the switch hardware, which
is carrying the signal -- incoming and outgoing -- using a particular protocol .
The module does its magic, and on the other side we have -- say -- 10GBASE-T to an RJ45
socket, or a blinking laser with an appropriate interface for optical fibre.
What would happen if you just had a dumb electrical cable to connect an SFP+ cage on
one switch to another on another switch?  That actually works pretty well!  It's called a
passive Direct Attach Copper (DAC) cable.  The interfacing is a little more complicated
than just a completely dumb wire -- the switch
will want to query the module in the cage to find out some details about it, so you need
a tiny bit of electronics -- but it's still really simple.
On top of that, if you add a bit of amplification to the DAC, then you get an active
DAC, which can double that kind of length (though these are relatively rare).
The neat thing about DACs is that they run
much
cooler than 10GBASE-T, using about
a third of the power.  Of course,
they lose out in terms of range.  But for simple stuff within one room, and especially
between switches in a rack, they work really well.
The next step on top of DACs is that you can convert the underlying SFP(+) protocol
directly to light, and send it down an optical fibre -- normally called an Active Optical
Cable, or an AOC for short
(though I've seen the rather confusing terminology "optical DAC" in various places).
With that, you can normally get up to 100m.  These are cheap and easy to use (because
they're all-in-one units, so you don't have any fiddly alignment of the fibre to do),
so they're the best option once you pass passive-DAC distances.
After that, though, you really need to switch to the official standards, and go to
more traditional fibre-optic setups.  I've done much less research into those, so
won't try to explain them.  Either way, for the home, anything above this level is
probably overkill right now...
Wrapping up
So: moving from the 2.5Gb/s networks that work smoothly with the same infrastructure
we've been using for the last 20 years or so to 10Gb/s is a tricky step change.  Suddenly,
things that didn't matter -- thermal management, cable lengths, and so on -- become
important.  And there are solutions, but you need to start actually understanding things
again rather than just plugging stuff in and assuming it will work.
Fun!  Time to put it into practice :-)  In my
next post, I'll show exactly the changes I had to make to get my existing 2.5Gb/s
network ported over to 10Gb/s -- the hardware I wound up buying, how well it works,
and (importantly) how hot it all runs.
