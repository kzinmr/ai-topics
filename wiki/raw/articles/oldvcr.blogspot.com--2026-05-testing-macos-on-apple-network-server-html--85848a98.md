---
title: "Testing MacOS on the Apple Network Server 2.0 ROMs"
url: "https://oldvcr.blogspot.com/2026/05/testing-macos-on-apple-network-server.html"
fetched_at: 2026-05-03T07:01:03.076878+00:00
source: "oldvcr.blogspot.com"
tags: [blog, raw]
---

# Testing MacOS on the Apple Network Server 2.0 ROMs

Source: https://oldvcr.blogspot.com/2026/05/testing-macos-on-apple-network-server.html

It's time for another save point in the continuing saga of the various ROMs for the
Apple Network Server
, Apple's first through-and-through Unix server (
previously
,
previously
). The Apple Network Server was only ever officially able to boot AIX, IBM's proprietary Power ISA-specific Unix, though it was originally intended to run
Novell NetWare
and was demonstrated booting Mac OS with early pre-production ROMs. However, much to industry surprise, late in its life cycle then-CTO Ellen Hancock announced that the ANS would be able to boot Mac OS and even Windows NT as well using ROM upgrades. Neither ROM was officially released before Steve Jobs convinced Gil Amelio to cancel the line, and for many years they were believed to be vapourware.
But they've started to surface, first with an ex-Apple employee who had both the preproduction ROM and the Mac OS ROM on a flash ROM SIMM, and later another employee turned up with the NT ROM, though sadly more is needed to make it actually run NT. It turned out that I also had the preproduction ROM in a box gathering dust, and a couple months ago
we put both the preproduction ROMs and NT ROMs through their paces
.
Well, thanks to Jeff Walther who generously built a few replica ROM SIMMs for me to test, we can now try the "2.0" MacOS ROMs on
holmstock
, our hard-working Apple Network Server 700 test rig (
stockholm
, my original ANS 500, is still officially a production unit). And there are some interesting things to report, especially when we pit the preproduction ROMs and this set head-to-head in MacBench, and even try booting Rhapsody on it.
When
we last left the 700
, it still had the preproduction 1.1.20.1 ROM installed, which can be used to boot either MacOS or AIX and makes it look to MacOS like a Power Macintosh 9500, the ANS's closest relative. However, the ANS has unique hardware: two Symbios Logic 53C825A SCSI-2 Fast and Wide controllers (20MB/s) for the internal SCSI bays and on-board Cirrus Logic 54M30 graphics used in no other Apple product. MacOS never supported these and the preproduction ROM does not contain support for them, so to boot Mac OS you have to use the external 5MB/s CURIO SCSI (the ANS doesn't have the typical Power Macintosh MESH controller) and a Mac-compatible PCI video card. I selected a IMS TwinTurbo, the same card shipped with the Power Macintosh 9500, and booted it off an external BlueSCSI, both of which work well for this purpose. Once you get everything set up, versions up to at least Mac OS 9.1 are compatible, though with various annoying glitches you have to work around because it's not
really
a 9500.
The value proposition of the 2.0 ROM is that support for Cirrus video and 53C825A SCSI comes standard — the drivers are built-in to the firmware. You can then boot Mac OS from the internal CD and install it to an internal SCSI disk at full speed, and connect your monitor directly to the ANS's VGA port (one of the only Apple systems of this era to have a standard HDI-15 video connector instead of the usual Mac DA-15). To test this, we'll unplug the BlueSCSI, remove the TwinTurbo and also take out the ANS-specific 10Mbit Ethernet card I installed because the onboard MACE Ethernet wasn't working, just in case it makes a difference. (More on that in a bit.)
The ANS also has a front-mounted LCD which can be used for displaying system status or other notifications. AIX and NetBSD both directly support it. Ordinarily this would be full of diagnostics and POST messages while the system boots, but the LCD is completely blank with the 2.0 ROMs installed and never shows any activity. In fact, it's the same kind of blank you'd get if the processor board went wacky, which is a little unnerving to an old ANS hand like me.
For some reason, and it could be my system because I usually have the PRAM battery out to let the logic board more quickly reset between experiments, I always had to three-finger reset it with Control-Command-Reset to get it to bong. The bong this ROM makes also seems a little truncated, and compared to regular ROMs with the extensive Long RAM test, these ROMs come up
very
quickly to the patterned Toolbox background. We have nothing installed it can boot from, so it almost immediately displays a gimme-disk animation, just like a regular Mac. But unlike most other Old World Macs (and the preproduction ROMs), the icon is in colour, because this is Open Firmware 2.0.
I reset it again and held down Command-Option-O-F to force Open Firmware to start. This also comes up immediately, and on the main screen as it would on a regular ANS.
This ROM is notable in that, besides the usual
bye
and
boot
words, there is an
io
word to redirect output for you. If you type
ttya io
at the console, it immediately switches to serial on rear port 2 at 38400bps by default. We want to see if it does anything interesting when we start it, so we'll
setenv input-device ttya:57600
,
setenv output-device ttya:57600
and
reset-all
to default it to serial startup, but we still have to hold down Cmd-Opt-O-F or it snaps back into the Toolbox ROM. Let's dump the device tree.
Open Firmware, 2.0
To continue booting the MacOS type:
BYE<return>
To continue booting from the default boot device type:
BOOT<return>
For Open Firmware serial I/O type:
TTYA IO<return>
 ok
0 > printenv 

VARIABLE            CURRENT             DEFAULT
little-endian?      false               false
real-mode?          false               false
auto-boot?          true                true
diag-switch?        false               false
fcode-debug?        false               false
oem-banner?         false               false
oem-logo?           false               false
use-nvramrc?        false               false
real-base           -1                  -1 
real-size           100000              100000 
virt-base           -1                  -1 
virt-size           100000              100000 
load-base           4000                4000 
pci-probe-list      -1                  -1 
screen-#columns     64                  64 
screen-#rows        28                  28 
selftest-#megs      0                   0 
boot-device         /AAPL,ROM           /AAPL,ROM
boot-file                               
diag-device         fd:\diags           fd:\diags
diag-file                               
input-device        ttya:57600          kbd
output-device       ttya:57600          screen
oem-banner                              
oem-logo                                
nvramrc                                 
boot-command        boot                boot
 ok
0 > dev /  ok
0 > ls 

Children of the node:
FF82A4C8: /                             [AAPL,9500 MacRISC]

Node Adr    Node Name                     Compatible

FF82B8B8: /cpus@0
FF82B9D0:   /PowerPC,604@0
FF82BDE8:     /l2-cache@0,0
FF82C528: /chosen@0
FF82C658: /memory@0
FF82C7A0: /openprom@0
FF82C860: /AAPL,ROM@FFC00000
FF82CA78: /options@0
FF82CF28: /aliases@0
FF82D168: /packages@0
FF82D1F0:   /deblocker@0,0
FF82D9C8:   /disk-label@0,0
FF82E4B8:   /obp-tftp@0,0
FF830710:   /mac-files@0,0
FF832508:   /mac-parts@0,0
FF8336F0:   /aix-boot@0,0
FF833B40:   /fat-files@0,0
FF835158:   /iso-9660-files@0,0
FF835AC0:   /xcoff-loader@0,0
FF836388:   /terminal-emulator@0,0
FF836420: /bandit@F2000000
FF837848:   /gc@10
FF837C80:     /53c94@10000
FF839490:       /sd@0,0                [sd]
FF83A1E0:       /st@0,0                [st]
FF83AE80:     /mace@11000
FF83BD10:     /escc@13000
FF83BE68:       /ch-a@13020
FF83C4C0:       /ch-b@13000
FF83CB18:     /awacs@14000
FF83CC00:     /swim3@15000
FF83E050:     /via-cuda@16000
FF83EF00:       /adb@0,0
FF83EFF0:         /keyboard@0,0
FF83F910:         /mouse@1,0
FF83F9C0:       /pram@0,0
FF83FA70:       /rtc@0,0
FF83FF10:       /power-mgt@0,0
FF83FFD0:     /lcd@1C000
FF840908:     /nvram@1D000
FF8426D0:   /pci106b,1@B
FF8428A8:   /54m30@F                   [pci1013,a0]
FF8445F8:   /apple53C8xx@11            [53c825]
FF8471E0:     /sd@0,0
FF8480D8:   /apple53C8xx@12            [53c825]
FF84ACC0:     /sd@0,0
FF840AA0: /bandit@F4000000
FF84BD60:   /pci106b,1@B
FF841F30: /hammerhead@F8000000
This is a little different from the device trees on our other ROMs, and not everything seems to work or was updated, suggesting this was unfinished at the time the product was cancelled. For example, if we look at the list of device aliases ...
ok
0 > devalias 
vci0                /chaos@F0000000
pci1                /bandit@F2000000
pci2                /bandit@F4000000
fd                  /bandit/gc/swim3
kbd                 /bandit/gc/via-cuda/adb/keyboard
ttya                /bandit/gc/escc/ch-a
ttyb                /bandit/gc/escc/ch-b
enet                /bandit/gc/mace
scsi                /bandit/gc/53c94
scsi-int            /bandit/gc/mesh
screen              /bandit@F2000000/54m30@F
... the definition for the internal SCSI doesn't actually exist. You'd think that
scsi-int
would point to the internal SCSI, and a path like
/bandit/gc/mesh
(GC in this case is Grand Central)
would
do so on a regular Power Mac, but the ANS doesn't have a MESH. That means trying to list the contents of a CD-ROM in the internal optical drive, ordinarily SCSI 0 on an ANS ...
ok
0 > dir scsi-int/sd@0,0:,\  unable to open the DIR device
... doesn't work. You have to do it in long-hand:
ok
0 > dir /bandit/apple53C8xx@11/sd@0,0:,\ 
.                   00000010 000023 000002048 000 000
..                  00000010 000023 000002048 000 000
DIAGS.              00000000 000024 000189345 000 000
NWSTART.            00000000 000117 003603460 000 000
OFWBOOT.            00000000 001877 000349998 000 000
TRANS.TBL           00000000 002048 000000655 000 000
Also, even though there is an AIX loader package in the 2.0 ROMs, it doesn't work either (using a bootable 4.1.5 CD):
ok
0 > boot /bandit/apple53C8xx@11/sd@0,0:aix loader: unrecognized client program format
state not valid
In fact, if you have a bootable AIX drive plugged in, the system will crash. I found that out when the ANS was freezing up shortly after POST and I eventually tracked down the culprit.
By comparison, the 1.1.20 preproduction ROMs show a much more sensible list of device aliases.
disk2:aix  
Device isn't there! can't OPEN: /bandit/53c825@11/sd@2,0:aixOpenFirmware1.1.20
To continue booting the MacOS type:
BYE<return>
To continue booting from the default boot device type:
BOOT<return>
 ok
0 > devalias 
vci0                /chaos@F0000000
pci1                /bandit@F2000000
pci2                /bandit@F4000000
fd                  /bandit/gc/swim3
kbd                 /bandit/gc/via-cuda/adb/keyboard
ttya                /bandit/gc/escc/ch-a
ttyb                /bandit/gc/escc/ch-b
enet                /bandit/gc/mace
scsi                /bandit/gc/53c94
scsi-int            /bandit/53c825@11
lcd                 /bandit/gc/lcd
screen              /bandit/54m30@F
scsi-int2           /bandit/53c825@12
disk0               /bandit/53c825@11/sd@0,0
disk1               /bandit/53c825@11/sd@1,0
disk2               /bandit/53c825@11/sd@2,0
disk3               /bandit/53c825@11/sd@3,0
disk4               /bandit/53c825@12/sd@4,0
disk5               /bandit/53c825@12/sd@5,0
disk6               /bandit/53c825@12/sd@6,0
 ok
0 >
Accordingly, a command like
boot disk0:aix
or
boot /bandit/53c825@11/sd@0,0:aix
will boot AIX from the internal CD-ROM.
The Network Server Diagnostic Utility (NSDU) shows other strange stuff. Because it never runs a Long RAM test, the RAM is never marked parity (even though it is; we labouriously dug out every parity FPM DIMM we had in stock to put in this thing). On ANS production ROMs (and the preproduction ROMs), the ROM will set the RAM timing to 70ns instead of 60ns if any stick of RAM is not parity, a rare case of where having parity memory
improves
performance. It's not clear what this ROM does in that instance, and in any case there are bigger problems such as the absolutely preposterous processor speed (this is a 150MHz PowerPC 604e). The L2 cache, at least, is correctly detected as the standard 700 1MB. We'll come back to this too.
For comparison, here's what a proper diagnostics readout would look like with the preproduction ROMs (slots 1 and 6 contain our video and Ethernet cards).
Well, let's try to start it up. I got out a retail Mac OS 9.1 CD and put it into the internal CD-ROM, with no other drives installed.
The system immediately booted. Again, the Happy Mac is colour, because this is a later Open Firmware.
Starting up. There is nothing connected to the external SCSI port — it's booting entirely on the fast internal SCSI — and the video is coming from the logic board. It all "just worked."
And it gets to the desktop just fine. Still, it seemed a little poky and I didn't remember it being quite that bad with the preproduction firmware. It wasn't clear to me if this was the video hardware or something more intrinsic to the system, so we should really set up an OS install and do a proper benchmark.
To put the internal SCSI through its paces requires hardware capable of keeping up with it, so I got out a newer ZuluSCSI Wide, installed it in a drive tray with a 68-pin SCSI mezz interposer, created a 4GB blank disk image and ran a clean Mac OS 9.1 installation. To my surprise, on rebooting I was able to plug in an AAUI dongle to the internal MACE Ethernet and it worked just fine when it wasn't working before, so I then added TattleTech, Gauge PRO and MacBench 5.0 from the home AppleShare server. Since I figured I'd want to compare this to the preproduction ROMs, rather than find an external CD-ROM I also used Disk Copy 6.5b11 to make an image of the MacBench CD for the graphics tests. We'll then use the same disk image in the external BlueSCSI for consistency.
As before, the Gestalt ID (as reported in both Apple System Profiler and TattleTech) is the same as the Power Macintosh 9500 and Workgroup Server 9650. However, the ROM checksum is $772.7DD0. To the best of my knowledge, this is unique to this ROM.
Apple System Profiler was taking an inordinately long amount of time to update the screen and I
knew
it hadn't been that bad. It also reported a bogus amount of L2 cache (2MB) despite the figure in the NSDU. But both Gauge PRO and TattleTech said there was
no
cache.
Also as the NSDU had reported, the RAM was not seen as parity and parity checking was disabled.
The Shiner-specific hardware is all correctly enumerated by Apple System Profiler. Both SCSI controllers appear and would have their own bus. In this case we're only using one bus, but there could potentially be three if you had a whole lot of drives installed and were using the external SCSI as well. They appear as PCI devices hanging off the on-board Bandit PCI controllers.
The Cirrus Logic 54M30 also appears, but its maximum colour depth is still limited to 8-bit (256 colours) like it is in AIX, even though there is more than enough VRAM to support a higher colour depth. The reason is, according to the Network Server Hardware Developer's Notes, "This controller implements only a little-endian window into the packed-pixel frame buffer, hence Big Endian operating systems are limited to 8 bits per pixel unless low-level transformation routines are written." [sic] It looks like that wasn't done here either.
The Ethernet is shown coming from "Built-In," off the on-board MACE, and our AppleShare server is connected from it. Nice to see that the logic board wasn't at fault after all.
Our ZuluSCSI Wide that we booted from is also rated for the full 20MB/s. It should run like a bat out of hell.
And the problem is ... this system doesn't. Even considering the reference comparison for this version of MacBench 5.0 is a 300MHz Power Macintosh G3, the 2.0 ROM's performance in Mac OS is absolutely dismal. Graphics, CPU and FPU testing are all between three and five times slower than the G3 reference. Although the disk performance seems superficially decent at sixty percent of the G3's, with the fast SD card in the ZuluSCSI and the full 20MB/s available we should have done a lot better.
I tried to make it a fair fight by putting in the TwinTurbo video card again, since we'll need it to run the tests on the preproduction ROMs. I used 24-bit colour depth since that would be the major advantage of using it. (Interestingly, when you start the system this way, there is a pause at the beginning where you see what looks like an Open Firmware cursor, then some garbage, then the Toolbox pattern.)
Even with its hands tied behind its back, as it were, the TwinTurbo still managed 20 percent of the G3 reference despite pushing three times the pixel data as the on-board Cirrus. That doesn't speak well of the Cirrus video's performance, or at least of the ROM driver for it.
At this point I had to know if I was imagining things, so I yanked the 2.0 ROMs, put back in my 1.1.20 ROMs, copied the disk image to the BlueSCSI and booted from the external SCSI port. The Ethernet immediately stopped working, using the same AAUI dongle, same Ethernet cable and same port, so it looks like these ROMs don't support the on-board Ethernet after all and I had to put the ANS 10Mbit Tulip Ethernet card back in. But hey, it's not the board!
The $77D.28F2 checksum for this ROM as reported by Apple System Profiler is the same as the 9500 and related systems. Although TattleTech still doesn't see the L2 cache, Gauge PRO does, and both Apple System Profiler and Gauge PRO agree on the correct size (1MB).
On the other hand, TattleTech does not report the RAM as being parity, despite a successful Long RAM test. We'll go with the NSDU's assessment here. I'm also not sure what to make of the lower "moving memory" rating, so let's run everything through MacBench again.
It's not even close, folks. CPU was 35% of the reference G3 (a whopping 75% faster), FPU 47% (47% faster), and graphics 33% at millions of colours (65% faster). But the real shame is the disk score: despite being on an interface up to four times slower, the preproduction ROMs get
eighty-nine percent
of the reference G3 — 48% faster!
My suspicion is this can be chalked up largely to the complete fail on the L2 cache and possibly also to the RAM speed, but either way, it was shocking how badly the 2.0 ROMs performed.
Still, if the 2.0 ROM can boot other operating systems, that might redeem it for certain purposes. We already had a fully installed Rhapsody 5.6 (essentially pre-Mac OS X NeXTSTEP ported to PowerPC and sold as Mac OS X Server v1.2) image on a BlueSCSI we tried to boot without success on the preproduction ROMs, so let's try that here — if Rhapsody works, we might get Mac OS X working next.
The magic boot string from the BlueSCSI on the external port, for a disk image set to device 2, turned out to be
boot scsi/sd@2,0:0 scsi/sd@2,0:8,mach_kernel
(using a "partition zero" loader to chain into the actual Rhapsody kernel). On the preproduction ROMs, we got a
CLAIM failed
from Open Firmware no matter what settings I tried.
On the 2.0 ROMs, it started immediately, though on the internal video it just made some colourful displays. On the TwinTurbo I actually got a proper startup screen, and I thought we were getting somewhere until I abruptly got this kernel panic. (What a pretty icon for a kernel panic window!) The problem seems to be that
waitForInterrupt
bombed out, possibly because of the different interrupt setup on the ANS compared to the 9500.
I tried a verbose boot (hold down V as you're entering that boot command) to see if I could get more information. It seemed to be loading drivers just fine from the Rhapsody partition ...
... but it still crashed in the same way, though we can see from the bigger window this time that much of the system
is
correctly detected.
Just for yuks I tried Rhapsody Developer Release 2 instead. The Mac OS-side installer will run, but I couldn't get it into the second installer stage despite poking around on partition 10 where it claimed to want to boot from. I also tried booting from the Mac OS X 10.0.3 and 10.2 CDs, but while I got a Happy Mac, the system simply locked up after.
So after all that, if you want to run Mac OS with top performance on the Apple Network Server, you need to be running the preproduction ROMs — not the 2.0 ROMs. I don't think the 2.0 ROMs were ever actually finished, or at least not
these
2.0 ROMs, or more elemental issues like the L2 cache support would have gotten fixed. It certainly does smooth out certain rough spots, it supports all the ANS hardware as advertised, and it was more reliable with reboots, but the speed penalty you'll take running it just doesn't seem worth it. I could only see myself running this version if I had to have the biggest, baddest, meanest AppleShare server with tons of SCSI drives in Mac OS. Is there a later version out there yet to be found that
does
deal with those problems?
Meanwhile, I'm going to work on a patched version of Mac OS for this machine to fix
the reboot problems in 1.1.20
, which I believe should be solveable with some resource hacking. That said, I'm not done with these ROMs just yet: I think Rhapsody, at least,
can
be made to work but it clearly needs a kernel patch, and I suspect the former Apple employee who got it working on the 2.0 ROMs did just that. Performance might still be hideously bad, but it's nevertheless another solid Un*xy option for Apple's best beige Unix box, and it even has historical value. To be continued if I can get my hands on some Rhapsody source code. Anybody feel leaky?
