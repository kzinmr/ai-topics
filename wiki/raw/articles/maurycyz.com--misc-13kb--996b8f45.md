---
title: "Loading... [13 kB]"
url: "https://maurycyz.com/misc/13kb/"
fetched_at: 2026-04-30T07:01:49.828821+00:00
source: "maurycyz.com"
tags: [blog, raw]
---

# Loading... [13 kB]

Source: https://maurycyz.com/misc/13kb/

Loading... [13 kB]
2026-04-03
—
2026-03-05
(
Programming
)
While testing my gopher client, I noticed something interesting:
All downloads froze at 13 kilobytes.
Sometimes, it was barely noticeable, other times it would stall for a good second or so.
Networks operate on small chunks of data called packets
.
This allows resources to be shared between computers:
Instead of waiting for someone else's download to finish before loading a website,
your web traffic can be sent in between the other user's packets.
There's still some waiting, but it's on the order of milliseconds instead of hours.
... but it does create a problem if you're the one doing that download.
Because each packet is routed independently, they frequently arrive out-of-order or get lost in transit:
Any large file would be hopelessly corrupted.
Transmission Control Protocol
:
The obvious way to solve the first problem is to number each packet.
That way, even if they arrive in the wrong order, the file can be reassembled correctly.
For example, the string "Hello, World!" could be sent like this:
#
1
: "
Hello
"
#
2
: "
, Wor
"
#
3
: "
ld!
"
... get shuffled around in transit ...
#
2
: "
, Wor
"
#
3
: "
ld!
"
#
1
: "
Hello
"
... and still be put back togther:
"
Hello
, Wor
ld!
"
To deal with packet loss,
the receiver responds to each data packet
with an acknowledgment containing the next sequence number it expects.
Since communication is bidirectional, I'll call the computer sending data the "server", and the computer receiving it the "client".
Let's send another "Hello, World!":
Server sends:
   #
1
: "
Hello
"
   #
2
: "
, Wor
"
   #
3
: "
ld!
"
... but packet #2 never arrives:
Client receives and responds:
   #
1
: "
Hello
"  -> ACK #
2
(next please.)
[ nothing ]
#
3
: "
ld!
"    -> ACK #
2
(got #
3
, but I still need #
2
!)

Got: "
Hello
.....
ld!
"
... soon:
Server receives:
   ACK #
2
ACK #
2
After waiting long enough to rule out packet reordering or jitter, the server assumes that packet #2 got lost and sends it again:
Server sends:
   #
2
: "
, Wor
"
Client receives:
   #
2
: "
, Wor
"    -> ACK #
4
(I already have #
3
)

Got: "
Hello
, Wor
ld!
"
Now, the client has all the data, and the server knows it can safely continue or close the connection.
Modern implementations also retransmit if they see enough duplicate acknowledgment packets, which can be faster then waiting for a timer.
* Technically, these examples are wrong: TCP numbers bytes, not packets.
On paper, this is a great system
, but in practice, it's very dangerous.
If the network gets overloaded, routers are forced to drop packets.
This causes systems to constantly retransmit data, creating more congestion, causing more packet loss...
To avoid breaking the internet (again, this happened in 1986)
, TCP adjusts its "congestion window":
The number of packets that will sent ahead of the last received acknowledgment.
This is a roundabout way to cap the transfer speed, because it limits how much data is sent in a singe round trip.
At the start of a connection, TCP's "slow start" sets the window to 10 packets.
Each (sequential) acknowledgment increases the window by one, causing it to double each round trip.
Once packet loss is observed, the window is halved,
 and TCP switches to incrementing the transmit window by one packet every round trip.
This "congestion avoidance" aims to track the maximum capacity of a network and evenly share bandwidth.
There's a bit of subtly here with how control is handed around
:
If a packet loss is detected by repeated acknowledgment numbers, congestion control proceeds as described.
If it's detected by timeout, the window is reset to 1 and "slow start" takes over until half the original window size.
The reasoning is that if the server gets a bunch of acknowledgments, this means that most of the packets have arrived
and are no longer taking up network resources.
If nothing is received, it's possible that those packets are still on the network and it should be careful —
both to avoid creating congestion and to avoid wasting bandwidth with unnecessary retransmissions.
Anyways, if the network isn't congested
, transfer speeds will ramp up exponentially, but that can take a while. 
With long ping times, the client might have to wait multiple seconds to get more than the 10 initial packets.
In my testing, most packets contained 1368 bytes of TCP payload, for a total of 13.2 kB...
but some variation exists because of differences hardware along the path:
different types of link can handle different amounts of data, and things like vlans can cut into the size limit.
Why should I
care
?
The practical takeaway is that size matters, even on gigabit connections.
During the first RTT, a client will receive somewhere on the order of 13 kB.
After two, it'll receive twice that, for a total of ~40 kB.
After three, it'll have ~92 kB of data.
If you are writing a website
, that first 13 kB should include everything needed to render the first screen's worth of content.
This includes inlining any critical CSS or/and JavaScript.
Although, these aren't hard numbers
, even though "Why your website should be under X kB" makes a good blog title.
Setting aside network variations, HTTP headers and encryption can take up quite a bit of data.
On the flip side, HTTP compression can save space.
... and those network variations are significant:
While the limit is usually quoted as 14.2 kB, but it's almost never actually 14.2 kB.
The only way to be sure is to open up Wireshark, but even then, you can't be sure that it will be the same for all your visitors.
Related:
