---
title: "A Tough Combination"
url: "https://feed.tedium.co/link/15204/17319282/linux-external-fingerprint-reader-challenges"
fetched_at: 2026-05-01T07:01:03.563477+00:00
source: "tedium.co"
tags: [blog, raw]
---

# A Tough Combination

Source: https://feed.tedium.co/link/15204/17319282/linux-external-fingerprint-reader-challenges

As you may or may not know,
I’m somewhat obsessed with tech on the edges, gadgets that do a thing comparable to a more expensive thing, and making the most of the things I have. (See my
Colmi R02
smart ring, which I’m wearing now.) And I kind of hate typing in my password a thousand times a day.
So I bought a fingerprint reader on Temu. And it works pretty well, all things considered.
In the world of Windows and MacOS, the options have been pretty solid. All modern Mac laptops, besides the base model MacBook Neo, have fingerprint readers. (For desktops, the situation is more complicated. Apple doesn’t make a standalone fingerprint reader, only putting one in its Magic Keyboard, but should.)
Microsoft has
Windows Hello biometrics
, a laptop-level approach to Face ID, but it works barely at best. My laptop, which has it, has only sporadically been able to get it to work with Windows. (Ironically, it works a little better on Linux.) But that has problems, too. If you’re in a dark room, for instance, it either doesn’t work at all or floods your face with a flash of light. Not exactly a fun 2 a.m. experience.
The solution here is to get a fingerprint reader that can help secure logins and offer an alternative to typing your sudo password 100 times per day. But there’s a challenge for Linux users: There are lots of modern fingerprint readers out there, but almost none of them support Linux via its standard security tool
fprint
. The ones that do are large and clunky, built not as laptop appendages but as large accessories that make more sense in complex desktop settings.
ThinkPads famously have pretty good fingerprint support on Linux compared to other platforms. (photos via
DepositPhotos.com
)
So what are laptop users to do? Beyond getting a ThinkPad, the options aren’t easy. When I started thinking about getting a fingerprint reader for my laptop, recently, I felt like I was tilting at windmills. I wasn’t sure what made the most sense, but I wanted something that could live off a USB-A port. What I found was a messy climate of cheap fingerprint readers that only barely do the thing that‘s listed on the tin. Finding a Linux-supporting fingerprint reader is a total crapshoot, and the best you can do is hope that someone else got there first.
(Not helping: The
list of supported devices
on fprint is thick as mud, presuming that you know the code name for the chip in your fingerprint reader. Plus, the list of
unsupported devices
is just as long, thanks to unfinished drivers.)
But there is a narrow path out of this annoying situation, and we have gamers to thank for all this. See, a few years ago the enthusiast company
GamePad Digital
(GPD) made a series of laptops called the GPD Win Max, which are essentially decked-out, handheld netbooks for gamers. In the days before the Steam Deck, it was the best PC gamers could do for portable gaming. The Win Max is still made today, and it has a fingerprint reader. Users wanted to use the fingerprint reader in Linux, and that led to a community developing a solution. This chip, the Chipsailing CS9711, is used in a number of USB fingerprint readers. If you know where to find them and are willing to
install a fork of libfprint
, you can use this device as a fingerprint reader on your laptop.
Not exactly painless—you have to know a few commands—but it’s absolutely doable, if you can find one. I found one, but it wasn’t easy, and I ultimately had to buy the thing via, of all things, Temu.
If you get a fingerprint reader like this, odds are you’re going to struggle to determine if it’s Linux-compatible. There’s nothing on the device that suggests it might be.
So, Is This Safe?
I think the key thing you might be asking yourself is, is buying a random fingerprint reader introducing a security risk to your device?
The short answer: Well, it’s an attack surface, and attack surfaces are made to be exploited. Even without the influence of Linux, Windows Hello devices have been getting exploited for years. At last year’s Black Hat security conference, a team of researchers figured out how to
shove someone else’s face into the camera stream
the feature relies on. Before that, Microsoft itself
found issues
with common fingerprint readers.
There are some benefits to an external fingerprint reader that an internal one does not have. If you’re concerned someone might try to log into your machine at the coffee shop while you’re hitting the restroom, take the fingerprint reader with you. (As I was writing, I actually tried this. It worked.) This has limits; the reader is generic, so you can’t do something like pair the specific device to your machine, so if anyone else has a fingerprint reader with the same chip, they can use it on your machine.
The more expensive
YubiKey
, which comes in models with or without fingerprint readers, could be a good alternative to folks who want to skip the Temu lottery.
This is not exactly hardened like a
YubiKey
or Titan device might be, but if your goal is to offer a modest amount of convenience, it could be just enough to make your life slightly easier. (Odds are, a snooper isn’t going to have a fingerprint reader of their own that matches yours—much like most people aren’t going to go to the trouble of hacking a device
via its Thunderbolt connection
.)
So, what’s the solution here? I think the best thing would be if manufacturers intentionally took steps to support fingerprint readers on Linux, but that doesn’t seem to be happening any time soon. So the alternative: Chinese manufacturers should probably explain what chip they used in the description of the device they’re selling. Currently, they don’t, and that presumably leads a lot of nerds to buy these devices, learn the devices don’t work on Linux, and immediately return them. That has to be costing them money.
There’s another solution that might be staring you in the face as you’re reading this: A lot of Android phones have fingerprint scanners already. Why not use one of those as your authentication tool, rather than doing Temu dumpster diving? I didn’t see any projects that formalized this, though I have seen some hacky solutions on GitHub.
KDE Connect
, the widely used phone connection tool, could be a great choice for a user-friendly version of this.
All I know is that it’ll be nice to cut down on the number of times each day that I have to type in my password.
Fingerprint-Free Links
Publishers are getting wary
of AI scraping, and they’re taking it out on the Internet Archive again.
Fight for the Future recently organized
an open letter of journalists who want to defend this important resource, and I was happy to be a
signatory
. We should not take it for granted.
I didn’t realize the aesthetic of Panera had a name,
but apparently it does: “
Global Village Coffeehouse
.” Jonathan Carson
breaks down
the design style, which you’ve seen for years but didn’t quite know how to refer to it.
G. Love, a popular ’90s musician from Philly,
recently lost his life savings in a
crypto scam
that also nailed
lots of other people
. Probably a good time listen to some G. Love & Special Sauce on a streaming service to help him out. Start with “
Rodeo Clowns
,” so Jack Johnson gets some royalties, too.
--
Find this one an interesting read?
Share it with a pal
! Are you sick of your password? Share it with us, and you’ll never be able to use it again. (Kidding!)
And thanks again to
la machine
for sponsoring. It doesn’t have or need a fingerprint sensor.
