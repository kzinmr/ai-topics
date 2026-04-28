---
title: "Build your own Dial-up ISP with a Raspberry Pi"
url: "https://www.jeffgeerling.com/blog/2026/build-your-own-dial-up-isp-with-a-raspberry-pi/"
fetched_at: 2026-04-28T07:02:52.832483+00:00
source: "jeffgeerling.com"
tags: [blog, raw]
---

# Build your own Dial-up ISP with a Raspberry Pi

Source: https://www.jeffgeerling.com/blog/2026/build-your-own-dial-up-isp-with-a-raspberry-pi/

Last year my aunt let me add her
original Tangerine iBook G3 clamshell
to my collection of old Macs
.
It came with an AirPort card—a $99 add-on Apple made that ushered in the Wi-Fi era. The iBook G3 was the first consumer laptop with built-in Wi-Fi antennas, and by
far
the cheapest way
to get a computer onto an 802.11 wireless network.
I go into more of the history of Apple's AirPort and iBook G3 in today's video (embedded below), but something I've always wanted to do is emulate a dial-up ISP locally.
What better way to do it than through Wi-Fi? Wait,
what?
Wi-Fi as we know it today typically routes fiber or cable Internet connections, with bandwidth measured in megabits or even
gigabits
.
But WiFi in 1999 (when the AirPort was released) maxed out at 11 Mbps. And half that, in real world conditions.
It's hard to find an AirPort Base Station with an intact Apple leaf.
The AirPort Base Station included a 10base-T Ethernet jack (for the rare few who had access to broadband), alongside a 56K dial-up modem. Most people going wireless in 1999 were still using AOL or some other dial-up ISP.
I had purchased a used first-generation AirPort Base Station
years
ago for an unrelated project that never got anywhere, so I figured I'd challenge myself this
#MARCHintosh
to see if I could run my own local dial-up ISP, using a Raspberry Pi—and then unite dial-up speed with 802.11b Wi-Fi!
Hardware
POTS, or the Plain Old Telephone System, is tricky to emulate. You can't just plug one modem into another. So in addition to a modem for my 'Pi ISP', I need a telephone line simulator.
Aside: I could also build my own little
PBX
with some VoIP hardware, but I'm saving that for a future project... I have plans :)
I chose the following hardware to build out my ISP:
You may also need a few phone cords to plug everything together. You plug the USB modem into the SBC, then plug a phone cord between the modem and the phone line simulator.
Then plug another computer (in my case, the iBook G3) into the other phone jack on the phone line simulator.
I switched dip switch #3 to the 'UP' position to decrease the audio volume, since the modems can achieve slightly better speeds that way.
With this setup, assuming you haven't changed any other defaults on the DLE-200B, either modem picking up will ring the other line a number of times (until the remote end either picks up, or ignores the call).
If you want to get fancy like I did, you can add in a
bell-style telephone
in the mix (pictured above). Plug the 'Line' jack into the phone line simulator, and the 'Data' jack into the Pi's modem.
With this setup, whenever the computer calls into the ISP, any rings will result in a nice, loud
physical
ring on the phone before the ISP modem picks up (useful for debugging!).
Software
On the Pi, we'll utilize two Linux tools,
mgetty
and PPP:
mgetty
("modem get tty") will handle calls through the modem, and negotiate with remote modems. Once a connection is established, it will hand off the connection to PPP.
PPP (Point-to-Point Protocol) will authenticate the remote computer, then configure a network bridge between the two computers, allowing the remote computer to behave as if it were on the local network.
I won't get into all the detail here, instead I'll point you to my
Pi ISP project
, where I have an Ansible playbook that configures everything for you.
In that repository, I also recommend two other resources, where I learned a lot about the dialup process in Linux:
If you clone my
pi-isp
project, then run the Ansible playbook on your Raspberry Pi (or any other computer running Debian), it should automatically start listening for a ring on the line—assuming you have a modem connected.
If you dial in from another modem (no phone number necessary, if you use the DTE-200B like I did—just wait a ring), you can monitor the PPP daemon's connection negotiation with
sudo journalctl -fu mgetty
:
Mar 26 15:32:35 dialpi pppd[15926]: PAM Account OK for dial
Mar 26 15:32:35 dialpi pppd[15926]: pam_unix(ppp:session): session opened for user dial(uid=1001) by (uid=0)
Mar 26 15:32:35 dialpi pppd[15926]: PAM Session opened for user dial
Mar 26 15:32:35 dialpi pppd[15926]: user dial logged in on tty ttyACM0 intf ppp0
Mar 26 15:32:35 dialpi pppd[15926]: PAP peer authentication succeeded for dial
Mar 26 15:32:35 dialpi pppd[15926]: Peer dial authenticated with PAP
You could even stop
mgetty
and run
minicom -D /dev/ttyACM0
to interact with the modem manually, using
AT commands
, like
ATA
to Answer a call.
The Internet at 33.6 kbps
But I was able to establish a connection at 33.6K
most
of the time; sometimes it would just not sync up correctly, and this was fixed by adjusting the maximum allowed speed with the
AT+MS
command inside
init-chat
(there's a convenient setting for this in my Ansible playbook's configuration).
That speed is the maximum you'll be able to get with POTS—you have to go digital to reach 56K, and even there...
The Serial Port has been building out a digital ISP
using top-of-the-line vintage phone system equipment, and they had trouble getting beyond 44K!
It's likely you'll have a more stable connection at 28.8K or lower.
But 33.6K should be good enough to relive late-90s dial-up:
And, yikes, 2.8 KB/sec... I'm now remembering those times when I'd wait until bed time, dial up from my computer, then trigger some shareware download to run overnight. It was too risky during the day
, when someone (usually my sister) would pick up the phone to call a friend. Most downloads would not gracefully resume after a disruption!
Picking up the phone while a modem is connected to the Internet is a risky move.
On an old computer, almost every modern website (including the one you're reading right now) will not load. Old browsers like Internet Explorer or Netscape Communicator don't have up-to-date TLS certificates—much less the cryptographic support required to use them.
But my Pi ISP has an ace up its sleeve:
Macproxy Classic
. This is a local 'proxy' server that sits between an old computer and the modern Internet, translating websites into a more barebones structure retro computers can handle.
The proxy strips away modern CSS, Javascript, and HTML tags, and outputs something old browsers and slower computers can render.
I just turned on proxy support in Internet Explorer 5:
And now I can browse my own website, on an iBook from 1999, running Internet Explorer 5:
But we're just browsing the Internet via a direct dial-up connection, with the iBook tethered to the phone line simulator. That's fun, but what's
more
fun, is going
fully wireless
.
Dial-up over WiFi
I think part of my justification for this whole adventure was spending over $200 refurbishing the battery on this iBook, to get it back to its original 6+ hours of battery life:
Unlike modern laptops, many of these turn-of-the-century bricks used full-size 18650 battery cells, which makes them surprisingly easy to rejuvenate—assuming you can cut open the plastic shell, and that you have a battery tab welder!
I didn't want to do it myself, not least because I don't like dealing with lithium-ion's fire potential. So I
shipped my battery off to have it refurbished
.
This wasn't cheap, but it was worth it to me, to see what it was like using the first WiFi laptop in 1999—without being tethered to the iBook's
yo-yo power adapter
.
I was able to test the iBook for hours, which was useful, because the old AirPort base station I was testing seemed to have stability issues—especially if I had it plugged in for more than an hour at a time. Maybe another casualty of Steve Jobs' obsession with form over heat-dissipation
.
I go into more detail in the video embedded earlier in this post, but Apple actually nailed the AirPort Admin Utility pretty early on—in fact, throughout their AirPort product line, they maintained what I think is the best Access Point management UI, probably to this day.
For some reason, every ASUS, Netgear, etc. wireless box I plug in has 50 different menus, and it's complete chaos trying to figure out how to change certain DNS settings. Apple did a great job of organizing the important settings in an intuitive way, that might only be matched by Ubiquiti gear (which I don't have much experience with).
One last thing I tinkered with was Macproxy Classic's
WayBack Machine Extension
: you can go to web.archive.org (while the proxy is active), and enable a kind of 'time machine' for your browser. Choose a date, then browse to any URL, and the extension will retrieve that URL
at that date in history
, as long as it exists in the WayBack Machine.
For example, Apple in late July 1999:
As a final test of my new wireless dial-up setup, I plugged an old Lucent WaveLAN PC Card (the same one that powers the original AirPort Base Station) into a PowerBook G3 I inherited from another one of my aunts (they all seemed to like Macs):
It worked a treat, and it felt nice having the extra screen real estate the 'Pro' level Apple laptop at the time afforded.
Conclusion
People sometimes ask why I do 'pointless' projects like these. Some of it is nostalgia, of course. And maybe to justify accepting all this old equipment...
But a big reason why is it keeps me learning. I'd never dealt with either mgetty or PPP in Linux, and seeing how the modem handshake works on the software level, or how the
ppp0
network connection is set up, helped me understand more about even modern connections like with VPNs.
Further, I got to learn how modems used
QAM
—and this in turn increased my understanding of how Quadrature Amplitude Modulation works with modern WiFi to give us
gigabits
of bandwidth, expanding on tricks developed years ago.
