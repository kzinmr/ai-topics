---
title: "Back to the Southern Hemisphere Commodore 128DCR"
url: "https://oldvcr.blogspot.com/2025/10/back-to-southern-hemisphere-commodore.html"
fetched_at: 2026-04-29T07:01:24.562988+00:00
source: "oldvcr.blogspot.com"
tags: [blog, raw]
---

# Back to the Southern Hemisphere Commodore 128DCR

Source: https://oldvcr.blogspot.com/2025/10/back-to-southern-hemisphere-commodore.html

Pretty sure this will end up as one of my longest-term restoration projects, but I'm back in the Southern Hemisphere for a little while to visit my wife's side of the family and giving me another opportunity to see if we can make progress on our
defective PAL 128DCR
, my favourite Commodore 8-bit.
When we left it last Christmas, it had an obviously defective U19 colour RAM and the serial bus locked up on any access to the internal disk drive or the included printer. As few chips on the DCR are socketed and certainly none of the likely suspects, the relevant chip replacements on this unit would require desoldering and I wasn't sure whether the 128's CIAs or the internal 1571's VIA (or both? neither?) was to blame. Those are big chips to replace. For this trip (and so I wouldn't spend the whole time hunched over a soldering iron) I decided to attack the colour RAM first, since I knew for sure that was bad, and it's a smaller job.
The U19 colour RAM is a 2Kbyte SRAM (as 2048 x 8 bits), officially a 2016 or similar, though the two 2016-type SRAMs in this unit are M2128-15 (aka MSM2128) SRAMs made by Oki. For its replacement I managed to source exactly a new-old-stock M2128-15, though I forgot to pop it in the chip tester before I left (big heaping bowl of foreshadowing). I also packed my new-in-box clone 785260 diagnostic kit and a couple extra tools the closest full-service Jaycar didn't have in stock and flew to Sydney.
The first step is to run the diagnostic on the 128DCR as it is. This is actually derived from Commodore's own diagnostic cartridge and harness they used for test and analysis back in the day, currently widely cloned and presently available from many sellers. It is now typically shipped as a set of dongles plus the cartridge, with a little LED voltmeter attached to the +5V line. The dongles connect to all the ports except the video output from the VIC-IIe (and RF) and VDC.
Unfortunately, the cassette one doesn't clear the slot on the DCR (admittedly this is my first use of this test kit because I haven't had any cause to use it on my States-side computers).
Fortunately my father-in-law whipped out his angle grinder and clipped off the tabs, and now it fits.
Side ports connected (switch the keyboard switch to off until the test starts) ...
... and rear ports, with the attached LED voltmeter on the cartridge reading a steady 5.00 volts.
The test is now running.
After burning it in for seven tests, with the bad colour RAM fault obvious (the screen text colours should be primarily blue and red), the cassette, serial port and user port are "BAD" and it also claims both 6526 CIAs are suss as well. I can well believe this for the serial port (CIA #2) but the keyboard works fine and so do the joystick ports (CIA #1). However, no other faults are identified.
I left the machine partially disassembled from our last post, but at this point we'll need to take out both the power supply and the floppy drive mechanism to proceed further. We already saw the
steps needed to remove the power supply
in our States-side repair of my usual NTSC 128DCR and repeated them here (always note the polarity: the PSU connector is
not
keyed). We then remove the three floppy mechanism connectors next to it ...
... and one more on the other side.
The floppy drive eject lever is only held on with a friction fit and can be pried off the rod it sits on with a spudger.
Finally, the mechanism is attached to the frame by two screws on this side ...
... and one more on the other. With that it slides back and out.
Vegemite and cheese toastie break.
The logic board is screwed into metal standoffs on the bottom. These positions can easily be identified from the underside.
Besides the typical screws at the corner and somewhat midboard, a number of the ports are screwed down to these standoffs and also need to be unscrewed, such as these on the side of the keyboard connector ...
... and these on the rear. Some of these ports also showed signs of rust or oxidation.
The power supply is propped up over the logic board by a screw-in standoff. This needed a bit of leverage to loosen.
Finally, the disk drive activity LED must be removed. The leads for this LED is soldered directly to the logic board with a blob of glue for strain relief. While some people have installed pin headers for this LED so it can be more easily detached, we don't need to do that simply to remove it. Like
the power LED
, this is held on the front via a screw and a easily fractured clip. We remove the screw ...
... and lever the LED off with the spudger. The clip may crack from this but the screw will still hold it in place.
It can then be threaded back through the front case hole (its attachment is at the bottom under the epoxy). I don't know why Commodore did this when they have a detachable power LED cable for the power supply.
With that the board simply lifts up.
I did notice some discolouration on the front of the board near the floppy drive. I'm not sure if this was a manufacturing defect or a sign of corrosion.
For a little more diagnostic information I decided to disable the ATN line on the internal disk drive to get a better idea if it was the 128's CIA, the 1571's integrated drive electronics or both causing the hangs accessing the IEC serial bus. This can be done semi-permanently by snipping pin 1 of U113, an 74LS14. I clipped it long enough so that we can put a switch here later.
Interestingly this caused the CIAs to now test good. Note that the clipped chip caused the diagnostic cartridge to detect it as a flat 128, and display the flat 128's RAM loadout, though I don't know what to make of the "2164" at "U45" (actually part of the 41464 chip at U39) testing bad when the full RAM tests all tested good. Despite that, in 128 mode it still freezes on startup trying to access device 8, and in 64 mode when accessing any IEC serial device, so the clean CIA bill of health is probably a fluke too. (Note from the future: it is.)
Don't get confused: on this particular machine, Commodore used the exact same M2128-15 in two places even down to the date code, and that may be the same situation on yours. This one here is the RAM for the internal disk drive at U103. While we may end up replacing it as well, it's not the colour RAM.
The colour RAM is here at U19. It is of course not socketed, so we'll need to clip it off and install one.
The chip is out and I spent some time cleaning up the holes to install a socket. 

You don't actually need the colour RAM installed to run the system — arguably that was the case already with it failed — so it's a good way to test your work. We can put the power supply back in temporarily with just three screws: one on the frontmost side (hard to insert), one on the topmost rear, and the centre one on the screw-in standoff. Always check the polarity of the connector before powering it up!
When I powered the system up with the socket installed, I got this display. Pop quiz: what did I do wrong?
Pencils down. The RAM data lines are missing bit 5. We know this because the spaces on screen (PET screen code 32) got turned into 0, and numbers and punctuation also lost that bit, among others turning the number 7 into the letter V and the period into the letter N. I checked my work
against the schematic
and reflowed the solder on the data lines, and also found there was no connectivity to ground or one of the MMU lines. For those two no amount of reflow would fix them, so I ended up soldering a couple of short bodge wires on the back.
Okay, let's pop the chip in! Conveniently Commodore observed a standard convention for where pin 1 should be located.
That doesn't look right. Only half of the colours are correct and we also have a weird grey out of place which argues against a bad address or data line. There's no open bus flashing anymore either, so I really don't think my wiring is at fault.
I brought it up in 64 mode to do a little more testing. Here we can see the colour RAM is actually not correct at all; it was only coincidental that it partially matched the 128's default light green text.
Here is the relevant section of the schematic. It's possible the write enable line could be faulty but I have good connectivity on that line to the 74LS74 at U56 and there isn't any crosstalk (except for chip select and output enable which are wired together). The four low data lines also can be picked up on the 4066 at U20 (the others are wired high using a resistor pack) and the address lines go through to the 74F24S at U55, the PLA and the MMU.
If I set screen memory to all 160s (reverse space), we can see the pattern. This does not clearly correlate to any one bad line. It does change slightly between power-on cycles.
If I keep screen memory set to all 160s but also try to set the colour memory to zero (black), some of it sticks. Even where it isn't black and some of the other bits remain stuck on, those colours do at least change (such as the pink now becoming green).
Conversely, if I try to set the colour memory to 255 (light grey), it looks almost the same as our original screen, modulo some power cycles later. There are a lot of stuck bits here.
I went ahead and re-ran the diagnostic to see if I had broken anything else. Again, most of this screen should be blue with some red. Oddly, it has gone back to detecting it as a 128DCR, and the CIAs "have failed."
With the chip out, we get the same results. Again, I'm very suspicious that CIA #1 is actually bad, and likewise U39, but nevertheless we have not fixed our colour RAM problem.
I don't have any more spare parts to try and I should have tested it before I got on the plane, so I'm taking the chip back with me to the States. It
is
new old stock, so it's possible it was DOA. On the other hand, if it passes in the chip tester, then I'm going to suspect U20 or U55 next which are pretty standard parts. (I would prefer not to consider the possibility that the schematic is wrong, or I read it wrong.) Snipping U113 also didn't solve our serial bus lockups and I think I'm going to have to bite the bullet and clip out CIA #2. I'd like to get this machine to the point where it can at least load and run things from an external drive like an SD2IEC — but I guess that will have to wait until next visit.
