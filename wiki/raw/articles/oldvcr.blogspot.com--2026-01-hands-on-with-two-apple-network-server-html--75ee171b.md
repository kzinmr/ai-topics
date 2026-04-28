---
title: "Hands-on with two Apple Network Server prototype ROMs"
url: "https://oldvcr.blogspot.com/2026/01/hands-on-with-two-apple-network-server.html"
fetched_at: 2026-04-28T07:02:04.219052+00:00
source: "oldvcr.blogspot.com"
tags: [blog, raw]
---

# Hands-on with two Apple Network Server prototype ROMs

Source: https://oldvcr.blogspot.com/2026/01/hands-on-with-two-apple-network-server.html

Grateful acknowledgement made to the several former Apple employees who materially contributed to this entry. This article wouldn't have been possible without you!
Here's why I need to do inventory more often.
This is an Apple prototype ROM I am ashamed to admit I found in my own box of junk from various Apple Network Server parts someone at Apple Austin sent me in 2003. The 1996 Apple Network Server is one of Apple's more noteworthy white elephants and, to date, the last non-Macintosh computer (iOS devices notwithstanding) to come from Cupertino. Best known for being about the size of a generous dorm fridge and officially only running AIX 4.1, IBM's proprietary Unix for Power ISA,
its complicated history
is a microcosm of some of Apple's strangest days during the mid-1990s. At $10,000+ a pop (in 2026 dollars over $20,700), not counting the AIX license, they sold poorly and were among the first products on the chopping block when Steve Jobs returned in 1997.
stockholm
, my own Apple Network Server 500, was a castoff I got in 1998 — practically new — when the University bookstore's vendor wouldn't support the hardware and it got surplused. It was the first Unix server I ever owned personally, over the years I ended up installing nearly every available upgrade, and it ran Floodgap.com just about nonstop until I replaced it with a POWER6 in 2012 (for which it still functions as an emergency reserve). Plus, as the University was still running RS/6000 systems back then, I had ready access to tons of AIX software which the ANS ran flawlessly. It remains one of the jewels of my collection.
So when
the mythical ANS MacOS ROM finally surfaced
, I was
very
interested. There had always been interest in getting the ANS to run MacOS back in the day (I remember wasting an afternoon trying with a Mac OS 8 CD) and it was a poorly-kept secret that at various points in its development it could, given its hardware basis as a heavily modified Power Macintosh 9500. Apple itself perceived this interest, even demonstrating it with Mac OS prior to its release, and leading then-CTO Ellen Hancock to later announce that the ANS would get ROM upgrades to allow it to run both regular Mac OS and, in a shock to the industry, Windows NT. This would have made the ANS the first and only Apple machine ever sold to support it.
Well, guess what. This is
that
pre-production ROM Apple originally used to demonstrate Mac OS, and another individual has stepped up with the NT ROMs which are also now in my possession. However, at that time it wasn't clear what the prototype ROM stick was — just a whole bunch of flash chips on a Power Mac ROM DIMM which my Apple contacts tell me was used to develop many other machines at the time — and there was no way I was sticking it into my beloved production 500. But we have a solution for that. Network Servers came in three sizes: the rackmount ANS 300 ("Deep Dish") which was never released except for a small number of prototypes, the baseline ANS 500 ("Shiner LE"), and the highest tier ANS 700 ("Shiner HE") which added more drive bays and redundant, hot-swappable power supplies.
Which brings us to
this
machine.
Meet
holmstock
, my Network Server 700, and the second ANS in my collection (the third is my non-functional
Shiner ESB prototype
). This was a ship of Theseus that my friend CB and I assembled out of two partially working but rather thrashed 700s we got for "come and get them" in August 2003. It served as
stockholm
's body double for a number of years until
stockholm
was retired and
holmstock
went into cold storage as a holding bay for spare parts. This makes it the perfect system to try a dodgy ROM in.
I'll give you a spoiler now: it turns out the NT ROM isn't enough to install Windows NT by itself, even though it has some interesting attributes. Sadly this was not unexpected. But the pre-production ROM does work to boot Mac OS, albeit with apparent bugs and an injection of extra hardware. Let's get the 700 running again (call it a Refurb Weekend) and show the process.
The 700 weighs around 85 pounds unloaded and is exactly like trying to cram a refrigerator into the backseat of your car (in this case my Honda Civic Si). While it does have wheels on the bottom, even the good ones don't have a great turning radius (and these aren't good), and getting it in and out of the car unavoidably means having to pick it up. Lift with your knees, not with your back.
Preparing the 700 for testing
This section is basically a cloaked Refurb Weekend, but even if you're familiar with ANS guts, I'm going to point out a few specific things relevant to ROM support as we go along. We want this machine as ship-shape as we can get it so that accurate observations can be made for posterity!
I would also like to thank my wife who chose to politely ignore the new noisy beast hulking in the living room for a few days.
Continuing in the fridge motif, the 500 and 700 have a front keylock controlling a sliding door, along with a unique 4-line LCD which displays boot information and can be used as an output device in AIX and other operating systems. Unlike my very minimally yellowed 500 which has spent most of its life in quiet smoke-free server rooms, this one seemed to have gotten a bit more sun. Fortunately most of the chassis is painted metal which is also where most of the weight comes from. The keylock position on power-up is noted by the firmware; the leftmost is the service setting, the middle is a normal boot, and the rightmost (locked) position puts the machine into a power failsafe mode.
The sliding door covers seven front drive bays, normally one with a CD-ROM, one with some sort of tape drive (typically a DAT/DDS drive, but a few have 8mm tape instead, both the same drives as sold for the Workgroup Server 95 and 9150), and the rest various hard drives which can be either independent or connected into an optional RAID. The 700 can take two more drives in a rear bracket. Although I have the RAID card, I never ended up installing it since a single drive was more than sufficient for what I was using it for. As most of the drive trays and both drive brackets had been removed from the two donor 700s used to assemble
holmstock
, I ended up just keeping a CD-ROM and two trays, and used the other open space for storage.
At the top are the NMI, reset and power buttons, plus a standard Mac floppy drive.
It is worth noting here that the internal bays are all serviced by two Symbios Logic 53C825A controllers, providing two Fast Wide SCSI busses running at 20MB/s. Unlike the typical Power Mac MESH (10MB/s) controller, the ANS internal SCSI controllers are unique to the ANS and appear in no other Apple product. Remember this for later. A second external SCSI bus is available on the rear, using the same (slower 5MB/s) CURIO SCSI/Ethernet/serial combo chip as other contemporary Power Macs and implementing an NCR 53C94.
The rear (with the monitor power cable photobombing the shot) is much less yellowed. Ports are here for audio in and out (standard
AWACS
), ADB, two beige Mac MiniDIN-8 serial ports, VGA (oddly but happily a conventional HDI-15, not Apple's traditional DA-15), AAUI 10Mbit Ethernet (any AAUI Mac dongle will work), and the external SCSI bus DB-25. Six PCI slots are available. A second keylock secures the logic board which is on a slide-out drawer accessed with the two handles. Both rear panels have their own fans which are hot-swappable as well. Apple included a monitor dongle in the box.
It is also worth noting here that the onboard video is a Cirrus Logic 54M30, also unique to the ANS, and likewise also used in no other Apple product. We'll be coming back to this point too.
Parenthetically, here are the keylocks (new replacements in my part box). They are wafer-lock keys of the same type used in the Quadra 950, Apple Workgroup Server 95 and Workgroup Server 9150. As sold Network Servers came with three keys, one front, one back and one spare, but they are all interchangeable. These keys have a small three-digit code engraved into the metal identifying the lock they are designed to fit.
I also got out a lot of parts from storage just in case they were needed, some of which were in the 700 and some of which were separate. Besides my two boxes of tricks, I also pulled out a spare logic board, five boxes of RAM upgrade kits (these are only 16MB each, though, so this isn't as much memory as you'd think), a 200MHz CPU upgrade kit, several more loose CPUs I also have, and a RAID card just for fun.
I dimly recalled the machine may not have been working right when I committed it to storage, but we'll proceed as if it had been, starting with a visual inspection of the electronics.
The keylock on the logic board drawer (shown here with the rear panel off so you can see how it operates) has just two positions. In the horizontal locked position, the board is connected to power and a metal tab prevents the drawer from coming out. In the vertical unlocked position, the board is disconnected and the tab is moved away from the chassis so the drawer can be pulled free. We turn the rear key, grab the handles and pull the board drawer out.
This is the logic board (the spare in the bag). It has a broadly similar layout to other six-slot Power Macs and has many of the same chips, including a Grand Central (labeled I/O CNTRL, near the Cirrus Logic video ASIC), CURIO (labeled SCSI/ENET) and two Bandits (labeled as PCI BRIDGEs). However, it only has eight RAM DIMM slots instead of the 9500's twelve, and most of the system connections are consolidated into a single card edge at the top and a large power connector at the bottom. There are separate slots for the ROM DIMM, the CPU daughtercard and the L2 cache. Headers handle both internal SCSI busses, the mainboard fan and the rear keylock. A small red CUDA reset button is at the top left.
Installed, the board sits in front of the mainboard fan which is primarily used to cool the CPU daughtercard. This daughtercard rides in plastic rails that serve as alignment guides and structural support. Tabs and a couple mounting screws hold the logic board in place in the drawer. The tabs, card rails and much of the drawer itself are unfortunately made from Amelioplastic, but this drawer is thick and not normally exposed to the exterior, and it mercifully remains in good physical condition. Note that when the drawer is open, the board is completely ungrounded, so only handle it with antistatic precautions.
I never store machines with their PRAM batteries installed (especially since my Shiner ESB prototype had been ruined by the previous owner doing so, during which time it leaked and corroded the logic board), but in this particular case since we will be messing with the system it is easier to reset the logic board if we never install the battery at all. With the machine unplugged, the battery out and the rear key unlocked (horizontal), the board will be completely depowered and will reset in about three minutes or so.
The CPU card is much larger than the ones used in most other PCI Power Macs and was intended to accommodate a dual-processor SMP option which was never sold, though again some prototypes have escaped (I would love to get one). Unfortunately this means that Power Mac CPU cards can't upgrade an ANS and the highest-speed option is the 200MHz 604e card shown here, but any ANS CPU card will work in any ANS, so
stockholm
also has a 200MHz card. Bus speed and CPU speed are related: the 132MHz (base 500) and 176MHz 604 cards run the bus at 44MHz, but the 150MHz 604 (base 700) and 200MHz 604e cards run the bus at 50MHz.
At the top is the 700's standard 1MB L2 cache (the 500 came with 512K). These are allegedly regular Power Mac caches, and a Network Server 1MB cache should work in other Power Macs, but the 500 kernel-panicked with a Sonnet L2 cache upgrade and I eventually had to chase down a 1MB card pulled from another 700.
Behind that is the ROM stick and the centrepiece of this article. They are not always labeled — one of my spares isn't — but when they are, the standard production ROM is part 341-0833. It is a regular 4MB ROM like other Old World Macs. We're going to test this machine with that before we go installing the others.
To get a test report will require a minimum amount of RAM. The ANS uses the same 168-pin DIMMs as other Power Macs and can accept up to 512MB (anything greater is not supported by the memory controller), but uniquely needs 60ns
parity
RAM for highest performance. If
any
DIMM is not parity, then the system ROM disables parity for
all
DIMMs
and
sets the timing to 70ns, even if the RAM is faster. This is a non-trivial hit, especially at the fastest 50MHz bus speed, so you really want parity if you can get it. Here I'm using parity FPM, which was sold standard in the units (all units came with at least 32MB in two 16MB DIMMs) and in upgrade kits (16MB in two 8MB DIMMs), all manufactured by IBM as OEM under contract and sold at typically exorbitant Apple prices.
Later on 64MB and 128MB parity DIMMs became available and
stockholm
has a full 512MB from eight 64MB parity sticks. RAM need not be installed in pairs, though this is preferred as the ANS supports interleaving. While EDO RAM should "just work" (treated as FPM), I've never tried parity EDO in an ANS. We'll put in two IBM 16MB parity FPM DIMMs to equal the base 32MB.
With the drawer closed and the rear key locked, we plug in the server (no drives attached yet), turn the front key to service, and then press the front power button to get ... a mostly blank front LCD instead of startup messages.
Having worked with these beasts for decades, this appearance — a backlit LCD with a mostly blank or dark block display — almost certainly indicates a problem with the processor card, because enough of the logic board is working to power on the front panel but the CPU isn't running. Typically this is because the processor wormed itself out of the board and needs to be reseated, but you can also get something like this if the card went bad, and less commonly if the ROM stick isn't installed correctly.
However (moving the monitor cord out of the way), we have a problem: we can't get the drawer to open wide enough to pull out and reseat the CPU card. We'll have to take the drawer off.
As usual, removing the drawer is relatively easy (it's getting it back on that's the trick). Two plastic latches on the underside of the drawer, fortunately still also in good nick, slip into two gaps in the metal slide rails. Supporting the drawer with your other hand so it doesn't fall off, push each latch in and push back the rail to disengage it.
The drawer then lifts off and can be put aside, preferably onto an antistatic mat.
Here's the inside, where the logic board connects. The powerplane connector is at the bottom. The board at the top is the right half of the mezzanine (codenamed "HENDY"), with the slot for the logic board's card edge and a connector for the front panel.
The mezz is a "horseshoe" that straddles both sides, better shown here with the top off. The other side has connectors for the NMI and reset buttons, floppy drive and SCSI busses.
Those bus connectors come from the SCSI backplane on the other side, here with that panel off (which can now be removed because the drawer is out). Both the front (and in the 700, the rear) drive connectors hook up here. I'd forgotten I'd disconnected bus 1 when I stored it, so I later reconnected the cable to J11 before closing this back up. If you don't do this, besides drives not working, you may get spurious errors warning that the drive fan failed or is not present (see later on).
The problem with the sliding rails turned out to be two-fold, first some stuck broken pieces of plastic which I removed, and second whatever lubricant Apple had used which over the decades had desiccated into gluey, copper-coloured gunk. I cleaned off most of the ick and then used WD-40 white lithium (not regular WD-40) on the rails and worked it back and forth into the bearings. If it's good enough for your garage door opener, it's good enough for your unusual Apple server.
After about ten minutes of spraying and sliding, both rails now move smoothly and reach their maximum extents. I was very careful to wipe off any excess so there wouldn't be a mess later.
Now to remount the drawer. This is not well-explained in the official Apple service manual, so I'll be more explicit here. On each slide are two small metal hooks. If you don't see the hooks, pull the slides forward until you do.
On each slide, one of the hooks goes into a metal notch on the two metal rails mounted on the back of the drawer. On the top slide, the bottom hook engages; on the bottom slide, the top one does.
Once you've done that, then while using one hand to support the drawer, pull each slide forward until it engages with each of the black latches (it will click into position).
Now we can pull the drawer all the way out, pull out the 200MHz card and try to reseat it using the card guides. You shouldn't need to force it in, though it does need a bit of grunt to ensure both rows of contacts get into the slot.
Closing the drawer likewise doesn't require force
per se
, but the rear keylock will not turn unless you have the board fully engaged with the mezz and powerplane. There are thumbscrews but they don't really make much difference for this. Sometimes you have to slam it in a couple times, making sure the thumbscrews are completely loosened and out so that they don't get in the way. When the logic board is properly engaged and the drawer is fully closed, it should be easy to turn the rear key.
Unfortunately reseating the processor card didn't fix it, so the next step is to try a different one.
I'm saving the other 200MHz card as a spare for
stockholm
, but we have several 150MHz cards, so I selected one of those.
And it starts up! We have messages on the LCD showing the 150MHz 604 (with 50MHz bus), 32MB of parity RAM and 1MB of L2 cache were all properly detected. The reported ROM version of 1.1.22 is consistent with production ROMs as shipped. If you connect to Port 2 on the rear at 9600bps during POST, you may see additional messages.
Since the front key is in the service position, it goes into a service boot, first trying the CD (looking for a bootloader) and then looking for the file
diags
on a floppy disk. We have provided the machine with neither, and nothing else is available, so the server drops to an Open Firmware prompt.
Open Firmware is the boot environment for all Power Macs starting with the first beige PCI systems. Originating at Sun as OpenBoot, Open Firmware provides an interactive Forth interpreter, which is used for interpreting cross-platform FCode (bytecode) in device ROMs but can also be used for development, and makes available a built-in means of managing and storing settings for installed hardware. In Macs of this generation it was generally invisible to the user except if specifically enabled or requested — remember this for later as well — and the Apple Network Server was the earliest Power Mac (well, derived, anyway) system where Open Firmware was explicitly user-facing. Open Firmware survives today largely in the form of
OpenBIOS
.
The
diags
file in question could be theoretically any XCOFF binary, but it's specifically looking for this, the Network Server Diagnostic Utility. This came on a floppy disk in the ANS accessory pack. We'll use the NSDU to check the rest of our configuration.
We could reboot the server, but we can just start it from the Open Firmware prompt directly with
boot fd:diags
. You can also see some of the system's current Open Firmware environment variables; we'll have much more to say about those when we finally get to experimenting with the ROMs. Sorry about the screen photographs but the default refresh rate does not agree with my VGA capture box.
The NSDU is also a single XCOFF binary. When it starts up it prints a summary of installed hardware and the results from initial POST. It has detected all RAM is parity, detected the CPU speed and internal L1, detected the external L2, detected both power supplies, and correctly shows installed RAM, no PCI cards, and most of the sensors. The only one that's wrong is the Drive Fan reads "Off" but that's because I hadn't remembered to reconnect the disconnected SCSI bus cable to the backplane. We'll now run the complete system test (option 3).
The tests scroll up on the screen, here showing the two internal SCSI controllers and the LCD. The video chip also gets exercised for conformance with various test displays.
In the end, we have a clean bill of health, both on the screen ...
... and on the LCD. There's one more thing left to do to certify operation: a test boot of AIX from the CD.
ANS AIX, codenamed Harpoon, is specific to the Apple Network Server — you can't use a regular AIX CD, and installing Base Operating System packages from such a CD is likely to corrupt your install (don't ask me how I know this). Most systems shipped with this CD in the accessory pack, version 4.1.4.1. 4.1.2 was used on preproduction servers but I've never seen it myself. Apple later issued version 4.1.5, which fixed many bugs and is strongly recommended.
Booting from the CD.
The LCD is live during an AIX boot, showing the march of AIX bootloader codes. They are the same codes as most IBM servers of this era.
Finally, the AIX kernel comes up, asking to define the system console. This proves our hardware (and CD-ROM) both work and that its native AIX can start, which means any weird behaviour after this point is more likely than not due to what we're testing.
We're finally ready to begin. Let's enumerate the currently known Network Server ROMs. In these pre-Open Firmware 3 ROMs, the ROM version and the Open Firmware version are the same. For comparison purposes, PCI Power Macs of this era were typically 1.0.5.
Pre-production ROMs. Currently one version is known, 1.1.20.1. These were used to boot Mac OS and AIX (and possibly another operating system I'll mention), but the internal video and SCSI controllers are not supported in Mac OS. This was the version that turned out to be on my flash DIMM.
Production ROMs. Currently one version is known, 1.1.22. These only boot AIX, though systems with these ROMs can also boot NetBSD and certain Linux distributions. I won't talk further about that in this article, but if I were to use a non-AIX operating system on a production ANS, it would almost certainly be NetBSD even though it doesn't currently support internal video or the on-board Ethernet.
Prototype Mac OS ROMs. Currently one version is known, 2.0. These contain ROM drivers for the internal video and SCSI controllers, and are the only known ROMs to fully support all internal devices in Mac OS. This is not currently in my possession — though I'd love to get one! — but at least one person has created replica ROMs from a dump graciously made available by their owner, and then used them to successfully boot their own machine.
Prototype Windows NT ROMs. These ROMs also appear to have multiprocessor support. Currently three versions are known, 2.26b6, 2.26b8 (not dumped, referred to on the LinuxPPC-ANS list) and 2.26NT, with relatively small changes between them.
These ROMs differ primarily in what operating systems they will boot (and, underlyingly, features they add or remove) and devices they contain internal support for. Those differences can be glimpsed by looking at the Forth words the ROM defines and the packages (implemented as pseudo-devices) they carry. For example, here are the packages and devices in this 700 with the production 1.1.22 ROM. The exact addresses are irrelevant for our purposes here except for the addresses of the Bandit PCI bridges, the Hammerhead memory controller and the Toolbox ROM, which are fixed.
disk2:aix  
Device isn't there! can't OPEN: /bandit/53c825@11/sd@2,0:aixOpenFirmware1.1.22
To continue booting from the default boot device type:
BOOT<return>
 ok
0 > dev /  ok
0 > ls 
004308E0: /PowerPC,604@0
00430B90:   /l2-cache@0,0
004313F0: /chosen@0
00431520: /memory@0
00431668: /openprom@0
00431728: /AAPL,ROM@FFC00000
00431968: /options@0
00431E40: /aliases@0
00432080: /packages@0
00432108:   /deblocker@0,0
004329A8:   /disk-label@0,0
00432F18:   /obp-tftp@0,0
00435B28:   /mac-files@0,0
00436410:   /mac-parts@0,0
00436D30:   /aix-boot@0,0
00437488:   /fat-files@0,0
00438DF0:   /iso-9660-files@0,0
004398E0:   /xcoff-loader@0,0
0043A410:   /terminal-emulator@0,0
0043A4A8: /bandit@F2000000
0043B500:   /53c825@11
0043DDE0:     /sd@0,0
0043EA48:     /st@0,0
0043F8A8:   /53c825@12
00442188:     /sd@0,0
00442DF0:     /st@0,0
00444288:   /gc@10
004446C0:     /53c94@10000
00446460:       /sd@0,0
00447248:       /st@0,0
004480C8:     /mace@11000
00449248:     /escc@13000
004493A0:       /ch-a@13020
00449AD8:       /ch-b@13000
0044A210:     /awacs@14000
0044A2F8:     /swim3@15000
0044BB88:     /via-cuda@16000
0044D088:       /adb@0,0
0044D178:         /keyboard@0,0
0044D950:         /mouse@1,0
0044DA00:       /pram@0,0
0044DAB0:       /rtc@0,0
0044DFE0:       /power-mgt@0,0
0044E1B8:     /nvram@1D000
00462BC8:     /lcd@1C000
00450780:   /pci106b,1@B
00450958:   /54m30@F
0044E7D0: /bandit@F4000000
00462350:   /pci106b,1@B
0044FF28: /hammerhead@F8000000
 ok
0 >
We'll do the first and last of these in the remainder of this article. Since the Bible says the first shall be last and the last first, let's begin with the
final
known ANS ROM, 2.26NT.
2.26NT Windows NT ROMs
Hancock's late 1996 announcement that the Apple Network Server would optionally run Windows NT caught many industry observers by surprise. Although NT 3.x and 4.x were designed to be architecture-independent and ran on processors as diverse as MIPS and DEC Alpha as well as 32-bit x86, the PowerPC build had been limited to low-volume IBM hardware and never officially ran on Power Macs. Still, it was clear to Apple that NT would be very important in the industry and felt supporting it would broaden the appeal of the server line — or at least soften the impact of its sticker price. Importantly, NT support would not have to wait for Apple's then-expected CHRP Power Macs: reworked ROM support could enable the ANS to boot it "now." (In the end, Jobs eventually scuttled the CHRP initiative to starve the Mac clones; the upcoming New World Macs were ultimately an incompatible blend of CHRP and the earlier PReP standard instead.)
When Jobs talked Gil Amelio into canning the ANS as well, the ROM initiative naturally went out the window with it. However, while the existing 2.0 Mac OS ROMs are only known on an unmarked development flash stick similar to mine, these final 2.26NT ROMs appear almost production-ready with fully printed labels, suggesting they had reached a very late stage of development. (The "ESB" tag indicates a prototype designation — consistent with Shiner, the ANS'
beer-themed codename during development
, ESB stands for "Extra Special Bitter.")
These ROMs were kindly sent to me by a former Apple employee at the Elk Grove, CA campus. Sadly this person no longer has the 700 they were running in, but attests to the fact NT did run and apparently even ran well, adding, "I’m pretty certain that the NT ROM was the Apple business systems team trying to find a way to keep their product from being canceled completely. Motorola had just shipped their PowerStack NT machines a few months previously and they were garbage compared to the ANS when it came to field service and expandability." (So true!)
The NT ROM DIMM simply replaces the production ROM DIMM in the slot. We'll power it up with the front key set to service just in case.
On the LCD, not only is the version displayed, but as mentioned this is also one of the ROMs that checks for a second CPU (if we had one of the prototype dual-CPU cards, that is — contact me, I'm interested if you've got one to get rid of!).
Our first order of business is to immediately dump these ROMs for posterity (they are posted on
the group thread at Tinker Different
). This can be done without a chip reader by having Open Firmware itself dump the contents in hex over one of the serial ports, and then post-processing the resulting output.
We start by switching the console to a serial port using
setenv input-device ttya:57600
and
setenv output-device ttya:57600
(
ttya
is port 2 on the back) followed by
reset-all
to commit the settings. Then, on a connected terminal program at 57600bps capturing the output (I did something like
picocom -b57600 /dev/cu.usbserial-10 | tee out
), you can either enter
h# ffc00000 h# 00400000 dump
which dumps the contents with the addresses, or if you don't need those, you can try something faster but a little more complicated like (suggested by @joevt)
0 ffc00000 do i 3f and 0= if cr then i l@ 8 u.r 4 +loop cr
which emits 64 bytes per line. The ANS ROM is already visible in the default memory map, so it can be dumped immediately.
This process is not very quick, but when it finishes you would take the transcript and turn the hex strings back into binary (Perl's
pack
function is perfect for this), which if properly captured would yield a file exactly 4,194,304 bytes long. Something like this should work on the 64-bytes-per-line output:
#!/usr/bin/perl

select(STDOUT); $|++; while(<>) {
    chomp; chomp; next unless (length == 128);
    print STDOUT pack("H*", $_);
}
which the Perl golfers will probably have turned into a handful of indecipherable bytes in the comments shortly. After the process is complete,
setenv input-device kbd
,
setenv output-device screen
and
reset-all
will move the console back to the ADB keyboard and VGA port.
There are a number of interesting things about this ROM, though most of it (about the first 3MB) is still identical to the 9500's.
The default boot device remains
disk2:aix
, but there are apparently NT-specific words in this version of Open Firmware like
nt-gen-configs
,
nt-gen-config-vars
,
init-nt-vars
,
maybe-create-nt-part
, etc. Their Forth code looks like this:
ok
0 > see nt-gen-configs defer nt-gen-configs
: (nt-gen-configs 
  maybe-read-nt-part get-first-str 
  begin 
    while/if 
      _cfgval _cfgvallen encode-string _cfgname count set-option get-next-str 
    repeat 
  ; ok
0 > see nt-gen-config-vars defer nt-gen-config-vars 
: (nt-gen-config-vars 
  maybe-read-nt-part get-first-str 
  begin 
    while/if 
      _cfgname count _configname pack drop ['] string-var gen-config-var 
      get-next-str 
    repeat 
  ; ok
0 > see maybe-read-nt-part 
: maybe-read-nt-part 
  init-nt-vars osnv-good? if 
    read-part 
    else 
    nvram-buffer nv-buffer-size erase 
    then 
  ; ok
0 > see init-nt-vars 
: init-nt-vars 
  nvram-buffer 0= if 
    /osnv dup to nv-buffer-size alloc-mem to nvram-buffer nvram-buffer nv-buffer-size 
    erase nvram-size alloc-mem to _cfgval nvram-size to _cfgval-size _cfgval 
    _cfgval-size erase 
    then 
  ;
From this you can get the general notion that these allocate a block of NVRAM for NT-specific configuration variables. There are also words for direct mouse support.
If we list out packages, we see other interesting things.
ok
0 > dev /  ok
0 > ls 
FF8362C0: /PowerPC,604@0
FF836570:   /l2-cache@0,0
FF836DA8: /chosen@0
FF836ED8: /memory@0
FF837020: /openprom@0
FF8370E0: /AAPL,ROM@FFC00000
FF8373A0: /options@0
FF837878: /aliases@0
FF837AF0: /packages@0
FF837B78:   /deblocker@0,0
FF8383E0:   /disk-label@0,0
FF838988:   /obp-tftp@0,0
FF83BFA0:   /mac-files@0,0
FF83C7A0:   /mac-parts@0,0
FF83D078:   /aix-boot@0,0
FF83D808:   /fat-files@0,0
FF83F608:   /iso-9660-files@0,0
FF840390:   /xcoff-loader@0,0
FF840DB8:   /pe-loader@0,0
FF8416A0:   /terminal-emulator@0,0
FF841738: /bandit@F2000000
[...]
Yes, there is a
pe-loader
package — as in Portable Executable, the format first introduced in Windows NT 3.1 to replace the old 16-bit New Executable
.exe
, and today the standard executable format for all modern versions of Windows. Here are some pieces of that:
ok
0 > see boot 
: boot 
  "boot " boot|load init-program go ; ok
0 > see boot|load 
: boot|load 
  _reboot-command pack drop set-diag-mode ['] (init-program) to ^-7DA998  
  carret word count (load) ; ok
0 > see init-program defer init-program 
: (init-program) 
  0 to ^-7DB118  loadaddr "\ " comp 0= if 
    "evaluating Forth source" type loadaddr loadsize evaluate loadaddr loadmapsize 
    do-unmap true to ^-7DB118  
    else 
    loadaddr 2c@-be F108 = if 
      "evaluating FCode" type loadaddr 1 byte-load loadaddr loadmapsize do-unmap 
      true to ^-7DB118  
      else 
      loadaddr 2c@-be 1DF = if 
        "loading XCOFF" type 0 0 "xcoff-loader" $open-package "init-program" 
        2 pick $call-method close-package 
        else 
        loadaddr 2c@-be F001 = if 
          "Loading PE/COFF" type cr 0 0 "pe-loader" $open-package "init-program" 
          2 pick $call-method close-package 
          else 
          "unrecognized Client Program format" type 
          then 
        then 
      then 
    then 
  ; ok
0 > dev /packages/pe-loader  ok
0 > words 
init-program    close           open            map-space       header-size     new-load-adr    
stack-size      scthdr.size     >pes.rawptr     >pes.size_raw   >pes.rva        >pes.virt_size  
>pes.name       opthdr.size     >peo.no_dir     >peo.loader_flags               >peo.heap_com_size              
>peo.heap_res_size              >peo.stack_com_size             >peo.stack_res_size             
>peo.head_size  >peo.image_size >peo.file_algn  >peo.scns_algn  >peo.image_base >peo.sndata     
>peo.sntext     >peo.entry      >peo.bsize      >peo.dsize      >peo.tsize      >peo.magic      
filehdr.size    >pe.nscns       >pe.machine     
 ok
0 > see init-program 
: init-program 
  real? little? 0= or real_base 700000 u< or "load-base" eval 700000 u< or 
  if 
    "false" "real-mode?" $setenv "true" "little-endian?" $setenv @startvec 
    >ramsize @ h#100000 - dup (u.) "real-base" $setenv h#100000 - (u.) "load-base" 
    $setenv cr "RESETing to change Configuration!" type cr force-reboot 
    then 
  loadaddr filehdr.size + >peo.image_base @ dup to new-load-adr "image_base  " 
  type u. cr loadaddr filehdr.size + >peo.head_size @ to header-size new-load-adr 
  stack-size - loadsize h#fff + h#-1000 and stack-size + map-space new-load-adr 
  stack-size - stack-size 0 fill loadaddr header-size + new-load-adr loadsize 
  header-size - move new-load-adr loadsize header-size - bounds do 
    i ^dcbf i ^icbi 14 
    +loop 
  loadaddr loadsize do-unmap 0 4000 map-space install-interrupt-vectors ci-regs 
  h#100 h#deadbeef filll new-load-adr stack-size - FF00 + spsv reg! new-load-adr 
  sasv reg! new-load-adr srr0sv reg! ['] cientry argsv reg! 0 crsv reg! msr@ 
  17FFF and srr1sv reg! state-valid on ?state-valid ; ok
0 >
Your eyes deceive you not: when configured to boot NT, this ROM runs the machine
little-endian
— which at the time would have been a first for a Power Mac as well, though this is the only way that Windows NT on PowerPC
ever ran
. 32-bit PowerPC has little-endian support through a little-endian bit in the machine state register or by setting a flag on memory pages in the MMU (which is how Virtual PC ran) or at the instruction level with byteswapping, but to this point all official Power Mac payloads had run big.
That means this ROM may be able to run PowerPC Portable Executables directly, so I got out my OEM Windows NT 4.0 kit to see.
I ran those words just in case they made a difference and then tried to do a naïve boot directly from the Windows NT 4 CD. This looks something like
boot disk0:,\ppc\setupldr
(don't forget the colon and the comma).
And, well, it can indeed load it and has a sensible image base address — but immediately crashes with a
CLAIM failed
, suggesting it couldn't map memory for the executable image, even though 32MB of RAM should have been more than enough to start Windows NT Setup. You can see from
init_program
above that it provides computed  values for Open Firmware
load-base
and
real-base
, so I imagine they were tailored specifically to boot NT (and NT Setup), but nevertheless I couldn't get past this point.
[In the comments, Andrei Warkentin asked if it could boot the veneer from the CD. It parses ...
... but it does not run either.]
To be sure, we almost certainly don't have all the pieces together for a successful NT boot
yet
. One thing I could find no trace of in the ROM was ARC. We talked about the rise and fall of ARC in
our SGI Indigo
2
refurb weekend
, but even though IBM, Sun, HP, Intel and Apple were never members of the Advanced Computing Environment consortium, Microsoft was. As a consequence virtually any machine capable of booting Windows NT would have some means of system specification through ARC (this particular historical vestige persisted until Windows Vista). On DEC Alphas, this was implemented in firmware, which is why you need the right firmware to boot it; for the IBM Power Series workstations and laptops, the ARC console was on floppy disk. It is highly likely the ANS also had an ARC console of its own, and since it doesn't appear to be in the ROM, there must have been a floppy or CD that provided it which we don't have.
Additionally, Windows NT relies on a hardware abstraction layer (HAL) which operates between the physical hardware and the rest of the operating system. The HAL is even more lower-level than device drivers, implementing functions like allowing device drivers to access ports in a more standardized fashion, abstracting away interrupt management, and unifying firmware interfaces and DMA. There are HAL DLLs on the 4.0 CD for various IBM (Types 6015, 6020, 6030, and 6070), FirePower (Powerized MX and ES) and Motorola (PowerStack 2 and Big Bend) PowerPC systems, but none for any Power Mac. The HAL necessarily gets loaded early in the setup process, often from another floppy, and you won't be able to successfully bring up Windows NT without it. Although there are apocryphal references to "halbandit" out there and this name is likely a reference to the ANS HAL, we don't have it either. (While it should be possible to get
the Windows NT for Power Mac port
running on the ANS, per the maintainer its current HAL relies on Mac OS support, so it wouldn't actually be using this ROM.)
Do you have any of these pieces? Post in the comments, or if you'd prefer to be anonymous, drop me an E-mail at ckaiser at floodgap dawt com.
Even without Jobs' looming axe, NT on the ANS was probably ill-starred anyway no matter how well it ran. The unique persistence of Windows NT on the DEC Alpha was a side-effect of primary architect Dave Cutler strongly basing NT on DEC VMS, an aspect hardly lost on DEC's legal team, to the point where various filenames and directory structures in the NT codebase even directly matched those in VMS. To avoid a lawsuit Microsoft paid off DEC, helped promote VMS, and committed to continued support for NT on Alpha, which remained until the beta phase of Windows 2000. This situation was absolutely not the case with PowerPC: IBM was so irked with Microsoft over OS/2 and NT's adoption of an expanded Windows API instead that its support for RISC NT was never more than half-hearted. Likewise, the only MIPS hardware that ran NT were DECstations — quickly cancelled by DEC in favour of Alpha — and directly from MIPS, the Magnum R4000 — also cancelled to avoid competition with Silicon Graphics' IRIX hardware when SGI bought them out. At that point, and already not favourably predisposed to Microsoft's initiative, IBM didn't see any value in continuing to support Windows NT on PowerPC and Amelio's Apple definitely didn't have the resources to do so themselves.
1.1.20.1 preproduction ROMs
Let's rewind a bit here and talk about booting Mac OS on the ANS, given that's how all this got started in the first place. The stock 1.1.22 ROM blocks booting it at the Open Firmware level:
ok
0 > dev /AAPL,ROM  ok
0 > words 
load            open            
 ok
0 > see open 
: open 
  "MacOS is not supported. " type false 
  ; ok
0 > see load 
: load 
  real_base 400000 <> virt_base -800000 <> or real? or little? or if 
    10 base ! "FFFFFFFF" "real-base" $setenv "FFFFFFFF" "virt-base" $setenv 
    "false" "real-mode?" $setenv "false" "little-endian?" $setenv "boot /AAPL,ROM" 
    !set-restart cr "RESETing to change Configuration!" type cr reset-all 
    then 
  ; ok
0 >
If you try anyway with
boot /AAPL,ROM
, it won't work.
You can force it by patching out those Forth words, but even though it will try to start, it will immediately crash and return you to the Open Firmware prompt.
Still, repeated reports back in the day swore they could do it. A couple people
tried using 9500 ROMs
, noting they would get a picture on an IMS Twin Turbo video card, though there was disagreement on whether it could actually boot anything and the different Bandit mapping almost certainly assured this wouldn't get off the ground. A few other people had intermittently acquired remaindered ANS systems from Apple that did indeed boot MacOS (retrospectively they very likely had 2.0 ROMs in them). More interesting, however, were reports that the Network Servers had
previously
booted Mac OS during development.
One of these early ROMs ended up sitting in a box in my closet for about 20 years. Apple Austin (the address on the box is no longer an Apple building) was the last stand of the Network Server, where a number of systems remained serving content as late as 2005. Per an Apple employee on the LinuxPPC-ANS list in March 2003, "Our team here at Apple decommissioned over 40 Shiners early last year. They used to be the backbone of the Apple Support site [that is, the former
www.info.apple.com
] serving all the software downloads, all the images for the support site and performing much of the heavy lifting behind the scenes that made our website the highest rated support site in the industry." About twenty of them were sold to list members — I was a starving medical student at the time and couldn't afford either the cash or the space — but I did make a deal to pick up some of the spare parts. I got two 10Mbit Ethernet cards and some 68-pin SCSI interconnects, and also some RAM. I didn't look too closely at what was in the box otherwise. I am told the servers that did not sell were crushed. :(
It wasn't until I was looking through my box for a spare ROM to see if I could get it converted to 2.0 that I found this ROM stick in the bottom of the box. It was not labeled and if I hadn't seen a picture of the 2.0 ROM, I probably wouldn't have recognized it for what it was.
This was how the 2.0 ROM looked in the Apple employee's Deep Dish that booted OS 9. Apple used flashable DIMMs exactly like this for Power Mac development generally; the form factor will fit in any beige Power Mac. (We don't know how to flash these yet but I know people are working on it.)
Still, the fact it came from the Network Server afterlife meant it probably wasn't any ordinary DIMM, so now let's give it a spin.
It comes right up ... and it's a pre-production ROM! This is currently the earliest known ROM available for the Network Server. I have no idea how it got in that box; I didn't request a spare ROM DIMM from them, but it was down at the bottom with the network cards and the other pieces that I did order.
I immediately dumped this one also to compare. Our Apple employee with the 2.0 ROMs also had a 1.1.20.1 set, and the hashes match his dump, so this is the same.
disk2:aix  
Device isn't there! can't OPEN: /bandit/53c825@11/sd@2,0:aixOpenFirmware1.1.20
To continue booting the MacOS type:
BYE<return>
To continue booting from the default boot device type:
BOOT<return>
 ok
0 > dev /  ok
0 > ls 
FF830648: /PowerPC,604@0
FF8308F8:   /l2-cache@0,0
FF831158: /chosen@0
FF831288: /memory@0
FF8313D0: /openprom@0
FF831490: /AAPL,ROM@FFC00000
FF8316F0: /options@0
FF831BD0: /aliases@0
FF831E10: /packages@0
FF831E98:   /deblocker@0,0
FF832738:   /disk-label@0,0
FF832CA8:   /obp-tftp@0,0
FF8358B8:   /mac-files@0,0
FF8361A0:   /mac-parts@0,0
FF836AC0:   /aix-boot@0,0
FF837218:   /fat-files@0,0
FF838B80:   /iso-9660-files@0,0
FF839670:   /xcoff-loader@0,0
FF83A1A0:   /terminal-emulator@0,0
FF83A238: /bandit@F2000000
FF83B290:   /53c825@11
FF83DB70:     /sd@0,0
FF83E7D8:     /st@0,0
FF83F638:   /53c825@12
FF841F18:     /sd@0,0
FF842B80:     /st@0,0
FF844018:   /gc@10
FF844450:     /53c94@10000
FF8461F0:       /sd@0,0
FF846FD8:       /st@0,0
FF847E58:     /mace@11000
FF848FD8:     /escc@13000
FF849130:       /ch-a@13020
FF849868:       /ch-b@13000
FF849FA0:     /awacs@14000
FF84A088:     /swim3@15000
FF84B918:     /via-cuda@16000
FF84CE18:       /adb@0,0
FF84CF08:         /keyboard@0,0
FF84D6E0:         /mouse@1,0
FF84D790:       /pram@0,0
FF84D840:       /rtc@0,0
FF84DD70:       /power-mgt@0,0
FF84DF48:     /nvram@1D000
FF8628D8:     /lcd@1C000
FF850490:   /pci106b,1@B
FF850668:   /54m30@F
FF84E560: /bandit@F4000000
FF862060:   /pci106b,1@B
FF84FCA8: /hammerhead@F8000000
 ok
This ROM specifically advertises it can boot Mac OS, and there is no block in Open Firmware.
0 > dev /AAPL,ROM  ok
0 > words 
load            open            
 ok
0 > see open 
: open 
  true 
  ; ok
0 > see load 
: load 
  real_base 400000 <> virt_base -800000 <> or real? or little? or if 
    10 base ! "FFFFFFFF" "real-base" $setenv "FFFFFFFF" "virt-base" $setenv 
    "false" "real-mode?" $setenv "false" "little-endian?" $setenv "boot /AAPL,ROM" 
    !set-restart cr "RESETing to change Configuration!" type cr reset-all 
    then 
  ?cr "MacOS is currently unsupported, use at your own risk." type <bye> 
  ; ok
0 >
However, if you enter
bye
as directed with a CD in the internal CD-ROM, the screen will go blank and nothing will happen.
The clue comes from those who claimed they got the system partially running with 9500 ROMs: the 9500 has no on-board video and always came from Apple with a video card, so they added a video card. With that, they got a picture
on the video card
. No Mac OS support for the internal Fast Wide SCSI nor the Cirrus Logic video is implemented in this ROM, and as we mentioned earlier, having never been used in any prior Apple product, the operating system proper doesn't know what they are either. In fact, the Cirrus Logic video is gimped even in AIX — the ANS Hardware Developer Notes say that the video controller provides "only a little-endian window into the packed-pixel frame buffer, hence Big Endian [sic] operating systems are limited to 8 bits per pixel unless low-level transformation routines are written."
For a server that's probably good enough. For a really powerful under-the-desk workstation, that stinks. Let's add a video card.
I chose an IMS Twin Turbo 128MA, nearly the pinnacle of 2D classic Mac performance, and one of the BTO options Apple offered for the 9500.
I also put as much high-capacity parity RAM in it as I could get my hands on. The biggest parity FPM DIMMs I have in stock were 64MB. You may need to examine your RAM sticks carefully to make sure you aren't actually putting in
non
-parity (the stick in the bottom picture is
not
parity). These two got me 128MB to start.
Initially I could only scrape together 192MB of parity RAM from what I had left and the 16MB upgrade kits, so I started with that.
For a test boot, I decided to try the external DB-25 BlueSCSI dongle I had left over from when we experimented with
Novell NetWare on the Power Macintosh 6100
, for two reasons: it already had a bootable image of 7.6 on it I was using for another project, and it also has an image of Cyberpunk, Apple's codename for the very alpha port of NetWare to the Power Mac originally intended for Shiner systems. Recall that this Forth word exists in every known ANS ROM, even the late 2.26 NT ROM, with the notable exception of the 2.0 MacOS ROMs:
0 > see setenv-netware 
: setenv-netware 
  "false" "real-mode?" $setenv "ttya:19200" "input-device" $setenv "ttya:19200" 
  "output-device" $setenv ?esb if 
    "scsi-int/sd@2:0" 
    else 
    "scsi-int/sd@3:0" 
    then 
  "boot-device" $setenv 
  ; ok
I wasn't sure if this version of Cyberpunk, intended for Piltdown Man machines (i.e., the 6100 and allies), would start on it but if any ROM could, I felt sure these beta ROMs had a decent chance. I set the Open Firmware
input-device
back to the default
kbd
and the
output-device
back to the default
screen
and brought it back up again.
Notice that it will still try to boot AIX as default — you would need to change the boot device to
/AAPL,ROM
to autoboot Mac OS, and this will be lost if the board NVRAM gets reset.
At this point, we plug the monitor into the Twin Turbo card and blindly type
bye
. Yes, you can set the Open Firmware
output-device
directly to the video card — something like
/bandit@F2000000/IMS,tt128mbA@D
would work for slot 1 — but this isn't necessary to boot ...
... because the Toolbox ROM will automatically use the card anyway and we get our long awaited Happy Mac. This is analogous to the situation on a real 9500 where Open Firmware 1.0.5 isn't on the console; by default it's on the serial ports. Another big heaping bowl of foreshadowing for you to keep in mind.
I left the Cyberpunk image on SCSI ID 0 to see what it would do, though I was pretty sure it would fail, and it did. This image has System 7.1.2 on it and no PCI Power Mac officially supported anything earlier than 7.5.2.
But, rearranging the IDs so that the 7.6 image was on ID 0 and the Cyberpunk image was in ID 1, 7.6 will boot! Let's switch to proper screenshots.
Unsurprisingly, 7.6's relatively underpowered System Profiler identifies the system as Gestalt ID 67, which matches the 9500, 9515, 9600 and the WGS 9650, but gives us little more detail than that. For a deeper dive we'll fire up TattleTech which was already on this disk image.
TattleTech reports the same Gestalt ID.
Cursorily scanning the Gestalt ID list, they all look pretty similar to a Mac of that generation booting 7.6. There is little hint here that this computer is anything other than a 9500.
On the other hand, the PCI slot layout is a little different. Like the 9500 and 9600, the ANS has two Bandits (there is even space in the memory map for a third, which remains unimplemented) and thus two PCI busses, but the 9500/9600 assign
three slots each to each Bandit
(Grand Central handling non-PCI devices is on the first). In the ANS, the first Bandit also carries the internal SCSI and internal video as well as Grand Central, so it only handles two slots, with slot 3 going to the second Bandit. This rearrangement manifests here in TattleTech showing just two slots on the first bus.
The ROM checksum also doesn't match. 9500 ROMs contain an Apple checksum of either $96CD923D or $9630C68B (the 9600 might also have $960E4BE9 or $960FC647), but this ROM checksums as $962F6C13. The same checksum appears in the 1.1.22 production ROM, which still contains a substantial portion of the 9500 v2 ROM even though it definitely won't boot Mac OS. This likely represents held-over code that simply no one bothered to remove.
We can also see that the two internal SCSI busses are detected, even if they aren't bootable with this ROM, and they are properly probed as a 53C825. The 53C94 used for the external SCSI which we are running from likewise appears.
Finally, the built-in AAUI Ethernet is detected as well (MACE, via Grand Central). I point this out specifically because ...
... it doesn't seem to work. While both AAUI dongles I tried showed working LEDs and activity on the network, 7.6 refused to enable the port. This did work in AIX at one point when I used it to sub for
stockholm
while investigating a hardware fault, but now it won't netboot either from Open Firmware. I'm concluding the MACE embedded in CURIO works but the PHY it connects to must have crapped out in storage.
Since we have the Cyberpunk image up, I tried running the PDMLoader just to see. Recall from our
NetWare on Power Macintosh
article that the PDMLoader is, at least on NuBus Power Macs, what starts the NWstart kernel and enters NetWare. Among other things it provides a fake Open Firmware environment to allow those Macs to resemble a Shiner ESB unit for demonstration purposes, which was the intended target hardware. Early Shiners reportedly could boot it directly. Unsurprisingly, the PDMLoader checks that it was started on a supported Mac and (based on the Gestalt ID) finds our franken-ANS wanting.
If we look back at our definition for
setenv-netware
, however, we can see NetWare was expected to run from a so-called "partition zero" loader. This is like it sounds: a runnable binary occupies partition zero of a bootable disk, usually XCOFF, and is loaded as blocks into memory by Open Firmware and executed. Unfortunately, the Installer we used for Cyberpunk didn't support creating this, and it wouldn't have been necessary for a NuBus Power Mac anyway which doesn't boot like that. As it's a regular XCOFF binary otherwise, I tried putting
NWstart
onto a plain physical ISO 9660 CD and fed that to 1.1.20.1, but ...
disk2:aix  
Device isn't there! can't OPEN: /bandit/53c825@11/sd@2,0:aixOpenFirmware1.1.20
To continue booting the MacOS type:
BYE<return>
To continue booting from the default boot device type:
BOOT<return>
 ok
0 > boot disk0:,\NWSTART. 
disk0:,\NWSTART.  loading XCOFF
tsize=2A14A1 dsize=90028 bsize=10E17C entry=843EC 
SECTIONS:
.pad     00000000 00000000 00000E14 000001EC
.text    00000000 00000000 002A14A1 00001000
.pad     00000000 00000000 00000B5F 002A24A1
.data    00000000 00000000 00090028 002A3000
.bss     00090028 00090028 0010E17C 00000000
.pad     00000000 00000000 00000FD8 00333028
.loader  00000000 00000000 0003BC04 00334000
loading .text, done..
loading .dataCLAIM failed
 ok
... while the ROM can read the file from disc and it will load, it halts with the same memory claim error I got trying it on the 500 with production ROMs, even after fiddling with the load and real base values to accommodate a large kernel. It's possible this kernel won't run outside of the PDMLoader environment and the Shiners used a different one, but that's not on the CD I have. Oh well.
Since the on-board Ethernet was shot, I decided to see if I could get it working with one of the Ethernet cards I ordered from Apple Austin way back when. This is a 10Mbit "Apple Ethernet PCI" card but not the same as the more typical one found in regular Power Macs — this particular card (820-0765-A, 630-1798, MM4709Z/A) is specific to the Apple Network Server. It has 10baseT, 10base2 and AAUI ports and is based on the DEC 21041 "Tulip" NIC, and is also distinct from the ANS 10/100 card (M3906Z/A). I installed the card in slot 6 so it would be on the other Bandit.
Rummaging through the box with the Ethernet cards in it, I also found some more 16MB sticks and bumped the parity RAM to 224MB at the same time.
Unfortunately Mac OS 7.6 doesn't see the card; it isn't even offered as a choice. This seemed like a good time to try installing Mac OS 9, first because it might have updated drivers, and second because I wanted to see if 9.1 would work in any event. I ended up copying the 7.6 screenshots to the main server with LocalTalk PhoneNET and a really long telephone cable, which my wife graciously chose to ignore temporarily as well.
Incidentally, a shout-out to my trusty Power Macintosh 7300 that batch-converts these and other PICT screenshots to PNG using Graphic Converter.
To start clean, I powered off the box, pulled the plug and turned the rear key for a full reset. While I waited for that to finish, I set up a new microSD card with an empty hard disk image and copied in an ISO of Mac OS 9.1. With power restored and the BlueSCSI reconnected, the CD image booted up — a gratifying sign that Mac OS 9 was going to work just fine — and I formatted the virtual hard disk in Drive Setup.
Even though it was over the slow 5MB/sec external SCSI, the installation went surprisingly quickly, likely because the emulated "CD" it was installing from was so fast. When it finished, I restarted the ANS ... and got a black screen on both the video card and the onboard VGA, even though I could see activity on the BlueSCSI and heard alert sounds. The ANS also properly responded to me pressing RESET and RETURN to cleanly shut it down, just like a Mac should. I reset the board again and it rebooted normally with
bye
from the blind console. We're going to come back to this really soon, because now I was starting to doubt the logic board despite all our testing earlier.
9.1 System Profiler again identifies it with Gestalt ID 67. Everything shows up here that we expect to, including the CPU, clock speed, RAM size and L2 cache.
We also see our Twin Turbo and Apple Ethernet PCI cards.
And, to my profound pleasure, it shows up (as "Ethernet slot SLOT.>4" [sic], even though I put it in slot 6, because it's slot 4 to the second Bandit) and can be selected.
We are now able to mount our usual assisting Netatalk server over the Ethernet, which replaces one long cable with another long cable, but it's all in the name of science! I did try the MACE Ethernet one more time here, and 9.1 doesn't throw an error, but it still doesn't work.
As a transfer test I pulled Gauge Pro off the server. It transferred completely and quickly, so I ran it to see what it thought about the hardware, and it didn't seem to find anything unusual.
So, about those reboots. At this point I shut down the machine and found the same thing happened when I tried to start it up again: a black screen, rectified by another complete board reset, but the Mac OS still seemed to boot headless and regardless. After the third such attempt, and out of ideas, I decided to foul the boot completely and see what was going on over the serial port. This can be done by letting it boot in regular mode, then for the next boot ensure the floppy drive is empty and turn the key to service, which will forget the boot setting from beforehand and try to start diagnostics. Lo and behold ...
fd:diags  NO DISK  can't OPEN: /bandit/gc/swim3:diagsOpenFirmware1.1.20
To continue booting the MacOS type:
BYE<return>
To continue booting from the default boot device type:
BOOT<return>
 ok
0 > printenv 
security-#badlogins 1 
security-password   
security-mode       none

little-endian?      false               false
real-mode?          false               false
auto-boot?          true                true
diag-switch?        false               false
fcode-debug?        false               false
oem-banner?         false               false
oem-logo?           false               false
use-nvramrc?        true                false
f-segment?          false               true
real-base           -1                  -1 
real-size           100000              100000 
virt-base           -1                  -1 
virt-size           100000              100000 
load-base           4000                4000 
pci-probe-list      -1                  -1 
screen-#columns     64                  64 
screen-#rows        28                  28 
selftest-#megs      0                   0 
boot-device         /AAPL,ROM           disk2:aix
boot-file                               
diag-device         fd:diags            cd fd:diags /AAPL,ROM
diag-file                               
input-device        ttya                kbd
output-device       ttya                screen
oem-banner                              
oem-logo                                
  z 2C + 8CC '& 8 + BRpatchyn then ;;l-method else $call-parent then ;
boot-command        boot                boot
 ok
0 >
... the serial port was active. Instead of
kbd
and
screen
(or the TT video card directly), I could see the input and output devices had been set to
ttya
. I didn't do that — Mac OS did that. Its fingerprints can be found in the apparently nonsense line of text between
oem-logo
and
boot-command
, which is in fact an NVRAMRC expected to run at startup to wallpaper firmware bugs.
Now it made sense what was going on. Mac OS thought this was a
real
9500, and patched its Open Firmware variables accordingly. The default settings for the Open Firmware 1.0.5 console point to the serial port, but on a real 9500 where Open Firmware wasn't intended as a user-facing interface, the ROM would simply ignore them and continue the boot with the video card and ADB HIDs. Not so on the ANS, where Open Firmware is meant to be interacted with directly: it actually
obeys
these settings! While Mac OS still brought ADB up regardless, neither the video card nor the onboard video would be enabled, and so the screen would stay black. (
NetBSD/macppc explains a related phenomenon.
)
However, even after I reset the
input-device
and
output-device
to
kbd
and
screen
, I still got no display. But from a cold board reset we wouldn't have an NVRAMRC either, so I also added
setenv use-nvramrc? false
, and
now
we reboot successfully! The PRAM settings persisted as well.
This means our logic board is likely not at fault, but I do consider this
some
sort of bug, especially because I don't want to have to constantly rescue it from a serial port just to restart the operating system. Fortunately there's a tool out there we can repurpose to get around the problem.
Paul Mackerras, now working
at IBM down under
and well-known to us in the OpenPOWER community, years earlier had written a control panel utility called Boot Variables. This CDEV very simply gives you a graphical Mac OS interface to what's stored in Open Firmware. To get this back up I would have had to fix the Mac OS patches, so you can see that the new (tainted) settings are written on startup, not shutdown. This is good news because if we undo the damage beforehand, we'll shutdown and/or reboot normally.
Boot Variables lets you save the current contents or load them from a file. If we save the current contents, we can see the NVRAMRC is rather lengthy (extracting the text from the binary dump Boot Variables generates):
boot: '& get-token drop ;
: >& dup @ 6 << 6 >>a -4 and + ;
: & na+ >& ;
6ED '& execute

0 value mi

: mmr " map-range" mi if my-self $call-method else $call-parent then ;
89B '& ' mmr BRpatch

: mcm -1 to mi $call-method 0 to mi ;
8CB '& 1E na+ ' mcm BLpatch

: maa -1 to mi 1D swap ;
8C9 '& 5 na+ ' maa BLpatch
8C9 '& 134 + ' 1 BLpatch

8CD '& 184 + dup 14 + >& BRpatch

8C6 '& 7C + ' u< BLpatch

0 value yn
: y yn 0= if dup @ to yn then ;
8CB '& ' y BRpatch
' y 28 + 8CB '& 8 + BRpatch
: z yn ?dup if over ! 0 to yn then ;
8CC '& ' z BRpatch
' z 2C + 8CC '& 8 + BRpatch
This does a lot of low-level patching, and while it's not exactly clear what part the ANS doesn't like, the script is also rather unnecessary since it boots fine without it.
Boot Variables can also write and restart the machine in one step with your new settings. In fact, if you open a Boot Variables dump with the Option key down, it will load those settings and reboot immediately with them, so we can just reboot that way — not exactly an ideal solution, but it works. Since the source code is available for Boot Variables, I'm tempted to write a Shutdown Items version that will do these steps automagically without prompting. In the meantime you can download it
from the NetBSD archives
, since it has obvious utility for NetBSD/macppc.
Because these steps are a bit of a pain, I suspected (and still do) that the version of Mac OS Apple exhibited during the ANS beta test was likely patched to work around the problem. That's yet to show up, though, if it even exists.
The former Apple employee who got me the 2.26NT ROM also mentioned he'd gotten Rhapsody running on one of their orphaned 700s. This would have had obvious political overtones within Apple at the time, and his boss told him not to tell anybody. Interestingly, the 2.26 ROMs do have strings in them claiming they can boot MacOS:
% strings rom1122.bin | grep -i macos
[...]
driver,AAPL,MacOS,PowerPC
MacOS is not supported. 
% strings rom226b6.bin | grep -i macos
driver,AAPL,MacOS,PowerPC
[...]
MacOS is not supported. 
+MacOS is unsupported, use at your own risk.
:MacOS requires PCI video card and external SCSI boot disk.
% strings rom226nt.bin | grep -i macos
driver,AAPL,MacOS,PowerPC
[...]
MacOS is not supported. 
+MacOS is unsupported, use at your own risk.
:MacOS requires PCI video card and external SCSI boot disk.
Despite running the system little when (trying to) boot NT, the 2.26NT ROM is of course perfectly capable of running big, and indeed must in order to boot AIX. Those strings appear to be false flags, though, because like the production 1.1.22 ROMs it too is blocked from booting Mac OS at the Open Firmware level:
disk2:aix   can't OPEN: /bandit/53c825@11/sd@2,0:aixOpenFirmware2.26
To continue booting from the default boot device type:
BOOT<return>
 ok
0 > dev /AAPL,ROM  ok
0 > words 
load            open            
 ok
0 > see open 
: open 
  "MacOS is not supported. " type false ; ok
0 > see load 
: load 
  real_base 400000 <> virt_base -800000 <> or real? or little? or if 
    10 base ! "FFFFFFFF" "real-base" $setenv "FFFFFFFF" "virt-base" $setenv 
    "false" "real-mode?" $setenv "false" "little-endian?" $setenv "boot /AAPL,ROM" 
    !set-restart cr "RESETing to change Configuration!" type cr reset-all 
    then 
  ?cr "MacOS is unsupported, use at your own risk." type ?cr "MacOS requires PCI video card and external SCSI boot disk." 
  type <bye> ; ok
0 > boot /AAPL,ROM 
/AAPL,ROM  MacOS is not supported.  can't OPEN: /AAPL,ROM
 ok
0 >
... and it will also hang if you patch out the words anyway.
No matter whatever hacking I tried, it would not go past this point either. It
is
noteworthy, however, that it claims it would boot with a PCI video card and external disk — it does
not
— which is exactly our successful configuration for 1.1.20.1. Given these limitations, it seems most likely that our Apple employee did this on a 2.0 ROM system (i.e., the "real" ANS Mac OS ROM), but let's see if the pre-production ROMs can pull off the same trick.
Currently I run Mac OS X Server v1.2 (i.e., Rhapsody 5.5) on a WallStreet PowerBook G3, probably the best laptop for doing so, but all versions have been reported to run on beige PCI Power Macs including the 9500. However, my previous experience with Rhapsody was that it rebooted multiple times during the install, and I was concerned this would be a problem with our rickety restart situation. So ... let's have the Wally install it to the BlueSCSI for the 700, and then see if the 700 will boot it.
The Wally is also technically unsupported, but you can get around that in the Installer, and the installation created is universal.
The installation process ran a lot more slowly than Mac OS 9's, even with the Mac OS X Server v1.2 CD images on the BlueSCSI.
When it completed, I took the finished hard disk and the installer CD disk image back to the 700. The 700 booted the CD just fine — it's just Mac OS 9, after all — but its Startup Disk control panel didn't see the Rhapsody disk.
I rebooted from the Mac OS 9.1 hard disk image but with the Rhapsody install also present on SCSI ID 1. While both Drive Setup and SCSIProbe saw it, neither mounted it (not even forcibly with SCSIProbe), and Startup Disk still failed to see it.
Apple made a tool to deal with this and other related startup situations called System Disk. Distinct from the built-in Startup Disk CDEV, this is a utility application that lets you pick your boot volume and as a nice side effect can be used to edit Open Firmware variables too. It comes as a self-mounting disk image.
System Disk
is not supported on some systems
and we should not be surprised it is not supported on this one either.
That said, it alone is able to see the Rhapsody volume and can tell us what we need to know. It has the boot and output devices completely wrong —
scsi-int
would be the internal SCSI, not the external, and
/chaos/control
references built-in graphics in models like the Power Mac 7300 and 8600 — and this version of Open Firmware lacks the words
O
or
bootr
, but we can see where it expects to load the Mach kernel from (partition 8) using its own "partition zero" bootloader.
This information is enough to come up with a command line to try booting it manually, but after all that I couldn't get it to start; it gives the same
CLAIM
failure message that's doomed our other attempts. Since I wasn't able to get it any further, it doesn't seem like trying real OS X out would go anywhere either. They may simply not work with this ROM.
Overall, however, the machine boots OS 9.1 well enough as long as you deal with the reboot-and-shutdown situation. It's a bit overkill to do this entirely over the external SCSI but at least doing it with flash media is far faster than a regular hard disk or CD-ROM, and as far as size goes I suppose it's no worse than
using an SGI Crimson to browse your filesystem
. If this is all you have to boot Mac OS on the ANS, and you really
want
to boot Mac OS on the ANS instead of indulging in the jackbooted bliss of AIX, it's perfectly cromulent.
The current situation
The pre-production ROMs work. Still, I'm hoping to get a 2.0 ROM in the near future and working with someone on doing just that. Even so, if you're an Apple employee with one of these ANS ROMs you need to get rid of, let's talk! The 2.0 ROM should solve our remaining issues with Mac OS 9, probably enable us to boot Rhapsody, and possibly even get early versions of Mac OS X working on the Apple Network Server too.
Similarly, if you know anything about "halbandit" or can provide the HAL or ARC console for the ANS' spin of Windows NT, that would be great! And anyone with knowledge of how Cyberpunk/NetWare was supposed to boot on Shiner ...
If you'd prefer not to post in the comments or wish to remain publicly anonymous, you can contact me at ckaiser at floodgap dawt com.
More to come
.
