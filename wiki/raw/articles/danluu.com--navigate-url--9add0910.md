---
title: "What happens when you load a URL?"
url: "https://danluu.com/navigate-url/"
fetched_at: 2026-05-05T07:01:33.668759+00:00
source: "Dan Luu"
tags: [blog, raw]
---

# What happens when you load a URL?

Source: https://danluu.com/navigate-url/

I've been hearing this question a lot lately, and when I do, it reminds me how much I don't know. Here are some questions this question brings to mind.
How does a keyboard work? Why can’t you press an arbitrary combination of three keys at once, except on fancy gaming keyboards? That implies something about how key presses are detected/encoded.
How are keys debounced? Is there some analog logic, or is there a microcontroller in the keyboard that does this, or what? How do membrane switches work?
How is the OS notified of the keypress? I could probably answer this for a 286, but nowadays it's somehow done through x2APIC, right? How does that work?
Also, USB, PS/2, and AT keyboards are different, somehow? How does USB work? And what about laptop keyboards? Is that just a USB connection?
How does a USB connector work? You have this connection that can handle 10Gb/s. That surely won't work if there's any gap at all between the physical doodads that are being connected. How do people design connectors that can withstand tens of thousands of insertions and still maintain their tolerances?
How does the OS tell the program something happened? How does it know which program to talk to?
How does the browser know to try to load a webpage? I guess it sees an "http://" or just assumes that anything with no prefix is a URL?
Assume we don't have the webpage cached, so we have to do DNS queries and stuff.
How does DNS work? How does DNS caching work? Let's assume it isn't cached at anywhere nearby and we have to go find some far away DNS server.
TCP? We establish a connection? Do we do that for DNS or does it have to be UDP?
How does the OS decide if an outgoing connection should be allowed? What if there's a software firewall? How does that work?
For TCP, without TLS/SSL, we can just do slow-start followed by some standard congestion protocol, right? Is there some deeper complexity there?
One level down, how does a network card work?
For what matter, how does the network card know what to do? Is there a memory region we write to that the network card can see or does it just monitor bus transactions directly?
Ok, say there's a memory region. How does that work? How do we write memory?
Some things happen in the CPU/SoC! This is one of the few areas where I know something, so, I'll skip over that. A signal eventually comes out on some pins. What's that signal? Nowadays, people use DDR3, but we didn't always use that protocol. Presumably DDR3 lets us go faster than DDR2, which was faster than DDR, and so on, but why?
And then the signal eventually goes into a DRAM module. As with the CPU, I'm going to mostly ignore what's going on inside, but I'm curious if DRAM modules still either trench capacitors or stacked capacitors, or has this technology moved on?
Going back to our network card, what happens when the signal goes out on the wire? Why do you need a cat5 and not a cat3 cable for 100Mb Ethernet? Is that purely a signal integrity thing or do the cables actually have different wiring?
One level below that the wires are surely long enough that they can act like transmission lines / waveguides. How is termination handled? Is twisted pair sufficient to prevent inductive coupling or is there more fancy stuff going on?
Say we have a local Ethernet connection to a cable modem. How do cable modems work? Isn't cable somehow multiplexed between different customers? How is it possible to get so much bandwidth through a single coax cable?
Going back up a level, the cable connection eventually gets to the ISP. How does the ISP know where to route things? How does internet routing work? Some bits in the header decide the route? How do routing tables get adjusted?
Also, the 8.8.8.8 DNS stuff is anycast, right? How is that different from routing "normal" traffic? Ditto for anything served from a Cloudflare CDN. What do they need to do to prevent route flapping and other badness?
What makes anycast hard enough to do that very few companies use it?
IIRC, the Stanford/Coursera algorithms course mentioned that it's basically a distributed Bellman-Ford calculation. But what prevents someone from putting bogus routes up?
If we can figure out where to go our packets go from our ISP through some edge router, some core routers, another edge router, and then go through their network to get into the “meat” of a datacenter.
What's the difference between core and edge routers?
At some point, our connection ends up going into fiber. How does that happen?
There must be some kind of laser. What kind? How is the signal modulated? Is it WDM or TDM? Is it single-mode or multi-mode fiber?
If it's WDM, how is it muxed/demuxed? It would be pretty weird to have a prism in free space, right? This is the kind of thing an AWG could do. Is that what's actually used?
There must be repeaters between links. How do repeaters work? Do they just boost the signal or do they decode it first to avoid propagating noise? If the latter, there must be DCF between repeaters.
Something that just boosts the signal is the simplest case. How does an EDFA work? Is it basically just running current through doped fiber, or is there something deeper going on there?
Below that level, there's the question of how standard single mode fiber and DCF work.
Why do we need DCF, anyway? I guess it's cheaper to have a combination of standard fiber and DCF than to have fiber with very low dispersion. Why is that?
How does fiber even work? I mean, ok, it's probably a waveguide that uses different dielectrics to keep the light contained, but what's the difference between good fiber and bad fiber?
For example, hasn't fiber changed over the past couple decades to severely reduce PMD? How is that possible? Is that just more precise manufacturing, or is there something else involved?
Before PMD became a problem and was solved, there was decades of work that went into increasing fiber bandwidth, vaugely analogous to the way there was decades of work that went into increasing processor performance but also completely different. What was that work and what were the blockers that work was clearing? You'd have to actually know a good deal about fiber engineering to answer this, and I don't.
Going back up a few levels, we go into a datacenter. What's up there? Our packets go through a switching network to TOR to machine? What's a likely switch topology?
Facebook's
isn't quite something straight out of
Dally and Towles
, but it's the kind of thing you could imagine building with that kind of knowledge. It hasn't been long enough since FB published their topology for people to copy them, but is the idea obvious enough that you'd expect it to be independently "copied"?
Wait, is that even right? Should we expect a DNS server to sit somewhere in some datacenter?
In any case, after all this our DNS resolves query to an IP. We establish a connection, and then what?
HTTP GET? How are HTTP 1.0 and 1.1 different? 2.0?
And then we get some files back and the browser has to render them somehow. There's a request for the HTML and also for the CSS and js, and separate requests for images? This must be complicated, since browsers are complicated. I don't have any idea of the complexity of this, so there must be a lot I'm missing.
After the browser renders something, how does it get to the GPU and what does the GPU do?
For 2d graphics, we probably just notify the OS of... something. How does that work?
And how does the OS talk to the GPU? Is there some memory mapped region where you can just paint pixels, or is it more complicated than that?
How does an LCD display work? How does the connection between the monitor and the GPU work?
VGA is probably the simplest possibility. How does that work?
If it's a static site, I guess we're done?
But if the site has ads, isn't that stuff pretty complicated? How do targeted ads and ad auctions work? A bunch of stuff somehow happens in maybe 200ms?
Where I can get answers to this stuff? That's not a rhetorical question!
I'm really interested in hearing about other resources
!
Alex Gaynor set up a GitHub repo that attempts to answer this entire question
. It answers some of the questions, and has answers to some questions it didn't even occur to me to ask, but it's missing answers to the vast majority of these questions.
For high-level answers, here's
Tali Garsiel and Paul Irish on how a browser works
and
Jessica McKellar how the Internet Works
. For how a simple OS does things,
Xv6
has good explanations. For how Linux works,
Gustavo Duarte has a series of explanations here
For TTYs, this article by Linus Akesson is a nice supplement
to Duarte's blog.
One level down from that,
James Marshall has a concise explanation of HTTP 1.0 and 1.1
, and
SANS has an old but readable guide on SSL and TLS
.
This isn't exactly smooth prose, but this spec for URLs explains in great detail what a URL is
.
Going down another level,
MS TechNet has an explanation of TCP
, which also includes a short explanation of UDP.
One more level down,
Kyle Cassidy has a quick primer on Ethernet
,
Iljitsch van Beijnum has a lengthier explanation with more history
, and
Matthew J Castelli has an explanation of LAN switches
. And then we have
DOCSIS and cable modems
.
This gives a quick sketch of how long haul fiber is set up
, but there must be a better explanation out there somewhere. And here's
a quick sketch of modern CPUs
.
For an answer to the keyboard specific questions, Simon Inns explains keypress decoding and why you can't press an arbitrary combination of keys on a keyboard
.
Down one more level,
this explains how wires work
,
Richard A. Steenbergen explains fiber
, and
Pierret
explains
transistors.
P.S. As an interview question, this is pretty much the antithesis of the
tptacek strategy
. From what I've seen, my guess is that tptacek-style interviews are much better filters than open ended questions like this.
Thanks to Marek Majkowski, Allison Kaptur, Mindy Preston, Julia Evans, Marie Clemessy, and Gordon P. Hemsley for providing answers and links to resources with answers! Also, thanks to Julia Evans and Sumana Harihareswara for convincing me to turn these questions into a blog post.
