---
title: "Taking down my site on purpose:"
url: "https://maurycyz.com/misc/v6day/"
fetched_at: 2026-04-29T07:01:55.849741+00:00
source: "maurycyz.com"
tags: [blog, raw]
---

# Taking down my site on purpose:

Source: https://maurycyz.com/misc/v6day/

Taking down my site on purpose:
2026-04-17
—
2026-04-18
(
Programming
) (
Web sites
)
Skip the history
If you have multiple computers, you'll quickly run into the problem of having data on one but needing it on the other.
Because of this, people have been connecting them together since the beginning.
However, this created a classic problem:
Each network used it's own addressing scheme, wire protocol, headers, etc, etc...
If you wanted to get a file between two networks, you had to find a machine that was connected to both and manually forward it.
To automatically route data between networks
, we had to agree on a universal numbering scheme for computers.
During the 1980, people settled on the 32-bit "IPv4" address.
Here's my server's address (split into bytes):
65.109.172.162
Back then, computers were massive and extremely expensive
, so 32-bits was plenty:
After all, there's no way there would ever be billions of computers in the world...
There was enough headroom to assign addresses roughly geographically and in power-of-2 sized blocks.
This made the internet scalable because each router doesn't have to know the exact details of every computer:
When your ISPs network sees my address, it doesn't have to know that exactly what computer
65.109.172.162
is,
just that everything starting with
65.109
should be sent to Finland.
... but it does mean that the maximum computers is a lot smaller than the full 32-bit address space.
We ran out around 2011
.
To keep the internet working, people started hiding multiple computers behind a single address.
Odds are, every single machine on your home network has to share a single IPv4 address through a rather complex "NAT" setup.
... but this was not enough
.
Recently, ISPs have started putting multiple customers behind a single address.
This obviously creates problems if you want to host services from home
(a website, multiplayer games, etc), but is also a problem for normie activities:
It's common to get punished by a website for something you didn't do.
If you've ever seen a "You've been blocked" message, gotten a Captcha every time, or simply had it mysteriously refuse to load...
there's a good chance this is what happened:
Someone who had the address before you was either doing something bad or
— more likely —
got hacked and was used as an unwitting proxy for a criminal's traffic.
Remember that the IP address is the one signal websites have to know who's sending something.
Unless they want to require everyone to make an account, IP blocking is the only option.
The solution is quite simple
:
Since we've run out of addresses that fit in 32-bits... just use longer ones.
This was first standardized all the way back in 1995 with 128-bit IPv6 addresses:
four times as long as IPv4.
Here's how many unique addresses that allows:
340,282,366,920,938,463,463,374,607,431,768,211,456
Needless to say, that's quite a few. Here's mine:
2a01:04f9:c011:841a:0000:0000:0000:0001
These larger addresses also have a lot of other benefits:
There's less need for virtual hosting,
the address hierarchy can be cleaner,
and it's possible put MAC addresses in a /64 block for stateless (and predictable) IP assignment.
Problem solved, right?
No.
Despite being around for 30 years (almost as old as gopher!), most people still do not have access to an IPv6 capable network:
10
Users don't have IPv6 support
20
... so websites are forced to support IPv4.
30
... so users don't notice they are missing anything.
40
... and don't complain to their ISP
50
GOTO
10
Because of this, even though the solution has existed ~forever,
bad decisions from 1980 continue to make your internet connection worse and more expensive.
To help break out of this cycle
, I've decided to remove IPv4 support on my site.
Cutting off most of my readers is a bit hash, so it'll only be disabled for one day each month:
The 6th will now be IPv6 day.
Any attempts to access my site over IPv4 will yield a message telling you that your network still doesn't support a 30 year old standard.
If you really want to access my site during the sixth, use your phone:
All major cell carriers have long since caught up with the times
because giving each device it's own address improves performance and simplifies administration.
(Quite a few actually run IPv6 only networks, and use a NAT64 proxy for accessing IPv4 only servers.)
Obviously, one website going down is just a site going down
.
For this to work, a lot of people have to do it.
If you have a website where 97% uptime is tolerable, consider doing something like this.
If downtime is too much, how about a banner that warns about IPv4?
Related
:
