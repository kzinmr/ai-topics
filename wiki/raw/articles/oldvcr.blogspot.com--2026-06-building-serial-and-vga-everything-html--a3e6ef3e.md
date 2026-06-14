---
title: "Building a serial and VGA \"everything console\""
url: "https://oldvcr.blogspot.com/2026/06/building-serial-and-vga-everything.html"
fetched_at: 2026-06-14T07:00:55.180074+00:00
source: "oldvcr.blogspot.com"
tags: [blog, raw]
---

# Building a serial and VGA "everything console"

Source: https://oldvcr.blogspot.com/2026/06/building-serial-and-vga-everything.html

Some of our recent (and some upcoming) projects are oriented to systems with serial consoles, but it's been getting pretty old dragging around old CRT terminals or tying up Mac laptops with a serial port. I'd like something that's self-contained, a little more portable and a bit less heavy. I'm sure there's any number of all-in-one setups you can buy to do this, but I'm cheap, so I'm going to DIY it.
We'll start with this used, slightly abused IBM 1U console that I got for $120 (shipped) from eBay, add a terminal emulator, and put all the fixin's on.
Nearly every server company produces one of these. They slide into a regular 19" rack and provide a flip-up LCD screen and keyboard in 1U. This was an IBM 7316-TF3 with a 17" screen and a combo keyboard-mouse slimline keyboard. IBM apparently manufactured these
from 2004 to 2014
, so it's almost on-topic for this blog, even. I chose it because it was a little banged up and the LCD had some areas of damage (probably improperly closed on something), and the seller had priced it accordingly, but the screen was still sufficiently legible and the keyboard looked fine. Naturally you can do mostly what we're doing here with any of the similar Dell or HP or etc. units that can also be easily found.
The keyboard is an IBM "USB Travel Keyboard with UltraNav" SK-8845RC, the variant with an extra-long cable. This is part of a family of such keyboards including a PS/2 variant (SK-8840), the short cable regular version (SK-8845), and the larger SK-8835 with a numeric keypad.
I actually rather like this keyboard. It's decently space-saving and has a not-horrid tactile feel given its thickness, and of course the lower tray is customized to fit it. Also, being
an UltraNav
, the fact it gives you a choice of pointing device is rather nice: if you like TrackPoints (I don't hate them), you can use that, or if you prefer trackpads (I don't hate them either but I'd rather use the TrackPoint), you can use that. The keyboard and UltraNav are implemented as HIDs on a single hub which also offers two more USB ports.
The keyboard's USB cable comes out on the other end carried by an extensible folding arm which is how everything stays connected when you pull the assembly forward from the rack. The other cable carried on this arm is the VGA connector.
The screen is "
fine
." Like I say, there was some damage, probably because it got closed improperly on something and messed up the display, but it's sufficient as a simple terminal or here connected to the M1 MacBook Air with a USB-C dongle.
The only drawback is that it gets a little daft with non-60Hz rates; it's rated to 75Hz, but 60Hz had fewer artifacts. The panel's maximum resolution of 1280x1024 is sufficient for my purpose.
Although the keyboard can be lifted up clear of the tray it sits in, it is only tethered by a single bolt and clip. This is fortunate because of ...
... what we chose for the terminal emulator. Assuming you don't want to build or program this yourself from scratch (and I didn't), there are a few homebrews here that will take a USB keyboard and a VGA screen and a serial port and do the needful, and what
you
need to do is pick what is the most convenient for you and has the right features. There are slightly more such devices which use a PS/2 port, but I decided to stick with USB since it would be more flexible and if I really needed something else, I could use an active converter like a
ps2x2pico
for PS/2 or a
Wombat
for Macs with ADB.
I eventually selected
this one from Tattler Solutions
(not affiliated) because it ships from the United States (damn you UPS,
you still owe me $600
on that tariff you stiffed me on), comes in a nice self-contained case and can be USB-powered, runs up to 115200bps, and has demonstrably good VT100 terminal support. All up it cost me $86 shipped. However, it also has a big drawback: its USB controller does
not
support combo devices like our IBM keyboard, which he does warn you about, and believe me, I tried really hard to get that to work because I really like the keyboard. Unfortunately, it truly is (and in fairness, as described) a fundamental hardware limitation that can't be programmed around, so that means we can't use our nice UltraNav.
I looked at slimline keyboards on Amazon and found two by Perixx (not associated, not affilated) that looked like they might fit ($20 and $25) and also had a PrtScr key to open the terminal's setup screen. The $25 keyboard would fit but did not sit in the little tray area, so we'll go with the $20 one and I'll find something else to use the $25 one for.
After a quick whirl through the keys to ensure that all the necessary function and control keys could be used and worked with the terminal emulator box, it's time to modify the lower tray.
My expert and exceptionally precise measurements showed that its thinness was just enough to fit in the cleft against the screen, so I got out the silane metal glue and some black-painted mending braces to serve as supports. However, we'll come back to this point.
Measure twice ...
and glue once (after scuffing the undersides with some steel wool and marking everything with silver Sharpie). Ignore what the tube says: this needs to cure for
days
. The first time I tried it, I tested it out after 24 hours as suggested and while the excess silane glue exposed
directly
to air had cured, the silane between the metal had only partially done so and the whole thing peeled right off. The second time I let it sit for a week. That seemed stable.
As insurance I also put some Flexseal tape over each support for extra rigidity and to hide the excess glue.
The appearance on the other side. One got a little crooked but it's fine.
To hold the keyboard in position, I then added some Velcro strips left over from another project, with the sticky side out.
The sticky side adhered to the keyboard, and then the Velcro kept it in place. This was nice for typing but also added a small amount of additional thickness I had not considered in my calculations. Again, more later.
Finally threading the cable out the previous hole. I made the cord long enough so the keyboard could be pulled out alongside as necessary. We'll more securely affix it momentarily.
Now for the rest of it. I went down to Target and bought some more Velcro tape and some Velcro cable guides ($21 for both), plus a little miniature power strip with two built-in USB 5V ports ($13), then from eBay bought a couple of "The Best" (that's how you know they're, like, the best) manual USB and VGA switchboxes ($20 for both shipped), and finally pulled out a whole bunch of matching USB and VGA cables from my stock closet. The idea is that this device will have two modes: in one, the keyboard USB and panel VGA will be connected to the VT100 terminal box, and in the other, they will be free connectors to plug into something else (as this unit did originally).
I started with installing the power strip. We'll remove the extension arm since we're not going to rackmount this; it comes off by unscrewing the nut with a pair of pliers and lifting it off the bolt it attaches to. The little plastic loop on this particular power strip nicely fits around the leftover bolt which is embedded in the metal.
The monitor has its own little brick power adapter, which is also (IBM and I think alike, which is moderately disturbing) attached by its own Velcro pad. We'll leave the power brick in place and merely move its power plug to the new power strip by taking off its clip and nut.
One of the Velcro cable strips neatly bundles up the slack in the power cable, and I reattached the nut and clip in a new location to hold the loops in place.
Next I laid out where I wanted the two switchboxes and the VT100 terminal box on the top. The idea is to have the switchboxes face to the side so that I can access the buttons. The "lower" buttons will be for raw USB and VGA, and the "upper" buttons will be for the terminal box.
The terminal box did require some thought. On one side is the USB power connector and the DE-9 ("DB-9") serial port, and the other the USB keyboard and VGA. I would have preferred the power cable to go there also, but since this is what we have, I decided to have the USB keyboard and VGA ports on the terminal box face down nearest the switchboxes. Using a yardstick I made sure everything was symmetric before marking their placements.
After that I attached all three boxes with Velcro tape, and connected the master USB from the keyboard and master VGA from the monitor panel to the switchboxes.
Simultaneously I made sure we had enough length on the keyboard cable, and with everything connected secured the cable in the proper position with its own nut and clip. A little plastic tubule wedges into the exit hole as well.
Now the power connector for the VT100 box. This will be powered directly from the USB on the power strip. I ran this cable from the power strip up along the monitor's power input, then under the box so it would keep it in position and looped it into its jack on top.
Following that we run the remaining USB and VGA cables. One set of USB and VGA cables goes to the VT100 box. The excess cable for this set is looped with a Velcro tie and then stuck onto a Velcro pad so it stays fixed, but can be removed if needed. The other set goes down the centreline with its own set of Velcro ties holding them together until they branch off.
A quick power test.
Finally, we'll put hooks on top of the switchboxes and Velcro cable ties on the ends of the external USB and VGA cables so they can be looped and affixed. A Velcro pad glued to the top of the power cable with its own attachment site completes the cable management.
It's a lot of cables, but they stay in one place, and everything has one.
Unfortunately, a second problem became apparent: the extra bit of height added by the Velcro meant the top of the keyboard was now contacting the screen when the unit closed.
I looked around for some Z-brackets of approximately the right height to match the keyboard and allow it to sink into the tray hole. This set of black steel ones ($9 on Amazon) were roughly correct.
The keyboard front portion is elevated from the rest of the unit, so it is possible to slip the Z-brackets in back to the stepoff where the two meet and secure them there. In this position, however, the side pieces will block the keyboard, so I peeled them off.
This does make the brackets extend lower than the usual bottom of the unit. To deal with that ...
... once the glue on the Z-brackets had hardened, I got a whole bunch of shims and bumpers out of the junk drawer, measured everything, and then installed several pieces to level off the bottom. I think I need a low-mounted crossbeam here to support the keyboard better but I'd have to fashion that out of Z-brackets of different height and smaller size. For the time being the Velcro keeps it in place well enough, it no longer hits the screen (and the unit can now close completely), and I generally use it on flat surfaces anyway. When I think I've got the underpieces all in permanent locations, I'll redo it all with JBWeld since the silane goo can still give way if you bang on it enough.
Proof of function: as a console for the POWER9
Raptor Blackbird
, using a VGA-to-HDMI dongle on the Blackbird side.
And as a serial console for an AT&T 3B2/310, which will hopefully be the subject of
a future entry
if I can get the kernel to come up.
Folded up more flat this time, ready for the next project. A latch and a handle would also help to make this more portable, though I suspect some drilling may be required for that. I'll look at some options. For now, this suffices.
