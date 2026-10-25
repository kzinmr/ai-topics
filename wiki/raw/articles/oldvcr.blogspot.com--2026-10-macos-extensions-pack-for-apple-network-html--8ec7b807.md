---
title: "MacOS Extensions pack for the Apple Network Server v1.0"
url: "https://oldvcr.blogspot.com/2026/10/macos-extensions-pack-for-apple-network.html"
fetched_at: 2026-10-25T10:01:22.690188+00:00
source: "oldvcr.blogspot.com"
tags: [blog, raw]
---

# MacOS Extensions pack for the Apple Network Server v1.0

Source: https://oldvcr.blogspot.com/2026/10/macos-extensions-pack-for-apple-network.html

By now regular readers of this blog are quite familiar with my affection for the 1996
Apple Network Server
, Apple's Unix-through-and-through $10,000+ server that only shipped with, and only officially ran, Harpoon, its unique superset of IBM AIX. An ANS 500, the lower tier of this dorm fridge-sized computer, was the first server I ever personally owned, a nearly-new hand-me-down after Steve Jobs convinced Gil Amelio to cancel the machine and the bookstore's vendor at the University I worked for wouldn't support it anymore. There are
several fascinating features
present in Harpoon that were never implemented in any other Apple product. Currently I have three, that original ANS 500, this ANS 700 here which I use for testing, and a battery-bombed EVT prototype (a so-called "Shiner ESB" that
used to be at Netscape
).
The ANS was strongly based on the Power Macintosh 9500 and Apple was known to have demonstrated the ANS with Mac OS during development, but this confused potential buyers, causing the ability to boot Mac OS to be stripped from production systems. While then-CTO Ellen Hancock claimed in 1997 a ROM swap would enable the ANS to boot Mac OS again
and
Windows NT, these ROMs were believed to be vapourware until a former Apple employee presented a working dump of
both the preproduction ROM and the later ANS Mac OS ROM
.
A prototype Windows NT ROM also emerged
from another former employee, though there are pieces missing and booting Windows NT natively on the ANS is still a work in progress (hopefully to be the subject of
a future article
).
It turned out
I had one of the preproduction ROMs myself
and didn't realize what it was. Because the later Mac OS ROM was apparently unfinished,
it doesn't properly support the L2 cache
and consequently runs substantially slower, and it can't boot AIX. The preproduction ROM does boot both operating systems and does support the cache. On the other hand, it doesn't support the on-board video or the front Fast Wide SCSI-2 controller, the on-board MACE Ethernet doesn't work, and after MacOS first boots, the next restart without zapping the PRAM will come up with a black screen.
The good news is, many of the issues with the preproduction ROM in Mac OS can be fixed or worked around in software. So I've fixed or worked around many of them in software: the MACE Ethernet is fixed, the on-board video is now supported, and the ANS can restart properly back into Mac OS. Plus, because it's the preproduction ROM, you can still boot AIX, thus preserving the entire historical reason for Shiner's existence. Here's the first cut of that software and how it was developed.
Naturally, the first order of business is to get an Apple Network Server and the 1.1.20.1 preproduction ROM (the production ROM is version 1.1.22). I can't help you with the first part, but replica ROMs now exist to cover the second part, and as of this writing
Joe's Computer Museum
has a few in stock (not affiliated, just a satisfied occasional customer). I
tested the original design
of these ROM DIMMs, kindly provided by Jeff Walther. Jeff assembled and donated this particular batch to Joe Strosnider, who is selling them and donating the proceeds in turn to the maintenance of the Tinker Different forum, where
this whole thing started
.
Now that you have the basic hardware, you'll then need to install Mac OS to an external bootable SCSI volume. For this project I use a 25-pin BlueSCSI which connects directly to the ANS' rear SCSI port and runs on termination power. Set up a blank disk image of the desired size to the device's (micro)SD card and rename it to the desired SCSI ID, which for the ANS is typically SCSI ID 2.
If you have another Mac with a SCSI port handy, it's easiest to do the MacOS installation to the external volume with that system. Make sure it installs Mac OS for any supported Mac, especially if you are using a model-specific installer CD; up to Mac OS 9.1 inclusive will boot directly on the ANS, and 9.1 is what I'm using here. 7.6 will work and late versions of System 7.5
might
work, but I recommend at least 8.1 or later. If you only have the ANS and/or have no other suitable vintage Mac that can perform the installation, you can do it on the ANS itself with a bit more difficulty. For that you'll need to not only create the blank disk image but additionally include an ISO of a bootable MacOS CD (use ID 0), plus install a Power Mac-compatible PCI video card — I use a Twin Turbo 128MA but any ATI Mac-specific card of the era should also work, such as the Rage Orion.
Finally, unplug the server, unlock and pull open the mainboard drawer, remove the PRAM battery, install the preproduction ROM DIMM, and leave the drawer open and the system completely depowered for at least several minutes while you enjoy the droll prose of this blog post.
Here's the back of my testing ANS 700. The monitor is connected to the 700's video port, the BlueSCSI is plugged into the SCSI connector, and a Farallon standard AAUI-to-twisted pair dongle is attached to the on-board MACE Ethernet AAUI port (Apple's perverse little rework of AUI to avoid confusion with the Mac DA-15 video port).
Technically that should be all you need to run Mac OS or AIX. However, I also have the Twin Turbo video card in slot 1 (where it would usually be in a 9500, the closest hardware relative to the ANS), and as an alternative for the MACE Ethernet I have one of the unobtainium 10Mbit ANS Ethernet PCI cards in slot 6 that I ordered from Apple Austin when they were blowing out leftover Shiner hardware. This card works in AIX and later versions of Mac OS (not 7.6, possibly 8, definitely 9); my only 100Mbit ANS Ethernet card is in the 500. A regular Power Mac-compatible Ethernet PCI card will suffice if all you want to do is run Mac OS.
Let's talk about drivers and PCI devices on Power Macs.
Denizens of the classic Mac OS are painfully familiar with
INIT
s and
CDEV
s, which is to say, the extensions and control panels which extend the operating system (and in many cases constitute substantial parts of it). Adding device support to the operating system required a
DRVR
resource, which could be stored in the declaration ROM of a NuBus card and available at power-on, or in an
INIT
or
CDEV
and made available during the boot process, or in a regular application and loaded on demand. (Parenthetically, desk accessories were also implemented as
DRVRs
.) Even after the 1994 transition to PowerPC, some, if not all, of such code still had to be 68K for backwards compatibility, and thus required emulation on a Power Macintosh.
Since this requirement was an obvious performance bottleneck, Apple attempted to address it in Copland, Apple's fallback attempt to modernise the Mac OS stepwise amid the slow-motion death marches of Taligent and PowerOpen-A/UX 4. Copland's tale of woe is a much longer story, to be the topic of
a future article
, but the part relevant to this piece was the new driver architecture it introduced. This aspect was part of how Copland's design partitioned its components ih memory to avoid the attendant pitfalls inherent in the classic Mac OS. In order to wall the old Mac OS world off but retain compatibility, everything that was 68K code lived in the so-called "cooperative" address space and was treated as data to be interpreted by the Power Mac 68K emulator, including 68K portions of the Toolbox. Even PowerPC-native System 7 applications ran here, since significant portions of the Toolbox were still 68K. This cooperative address space would theoretically allow most applications to run as they did before, but intentionally without privileges to the rest of the system nor access to Copland's hardware abstraction layer (HAL).
As such, Copland drivers necessarily were fully native code, in this case implemented as regular PowerPC code fragments. These drivers hooked into the HAL and the Name Registry, an object database that tracked devices on the system and mediated loading and unloading device drivers as needed, and were collapsed into a separate global region at a lower execution level where only limited operating system functionality was available. Although such limitations restricted their ability to integrate with the operating system, it also enabled those drivers to run early in the boot process and remain protected from user code. This new class of driver was called a
native driver
.
Although Copland suffered from terminal second-system effect just as badly as its contemporaries, it was modular enough for parts of it to be used as transitional enhancements — such as its visual language, which later became the basis of Mac OS 8's Platinum theme, and other pieces that shipped more quietly. Germane to our discussion here was Apple's transition from NuBus to PCI, one not uniformly well-received by users, though in fairness it was effectively forced on Apple when IBM wouldn't support NuBus in the PowerOpen-based AIX 4. For these first PCI Power Macs, starting with the 9500 in 1995, Apple added a port of the Copland Name Registry to their ROMs as well as Eric Traut's faster dynamic recompiling 68K emulator, also intended for Copland.
In this scheme the system ROM initializes the hardware and hands control to its onboard copy of Open Firmware, which creates the device tree for all devices on the system, necessarily including PCI cards but also processor and logic board resources. The Code Fragment Manager, also in the Power Mac ROM, then runs code from any PCI card expansion ROMs and drivers in the Mac ROM itself. This code typically contains a low-level "expert" that creates a node in the Name Registry with sufficient information to identify the device and enable a driver to match against it.
Once the Name Registry is built out, the Mac ROM starts the Display Manager, SCSI Manager and/or ATA Manager, as needed, as part of booting the Mac OS kernel. These Managers in PCI Power Macs implement a different type of "expert" called a
family expert
. When the MacOS File Manager and Resource Manager are up, the Extensions folder is scanned for native drivers (stored as code fragments with a Type of
ndrv
, but otherwise the same general structure as their Copland antecessors) and handed to the expert of each particular service category for device classes the family expert supervises. Eligible and matching
ndrv
s, be they in ROM or on disk, are loaded before any other extension is ever invoked, and the family expert activates and wires them into the operating system.
Apple produced a driver development kit for PCI card vendors that included various debugging tools. This is the Display Name Registry browser from the PCI DDK 3.0, which I got off one of my Apple Developer CDs (there are other tools that do this
like @joevt's
, whose assistance with certain parts of this project is gratefully acknowledged), showing defined nodes on the ANS 700 booted into Mac OS 9.1 using the 1.1.20.1 pre-production ROM.
The most important thing to notice here is that even though the Name Registry was first added to PCI Power Macs, there are many more nodes here than merely PCI cards, as there would have been in Copland. Both our PCI cards indeed do appear, connected to one of the Bandit PCI controllers (the ANS has two but mapped differently than the 9500, and there is reserved address space for up to four). However, so do things like the CPU, L2 cache, Mac ROM, and devices attached to Grand Central, which acts as a bridge between PCI and traditional Mac devices like the AWACS sound chip (Crystal CS4217 codec), Grand Central's internal SWIM III floppy controller, and the AMD AM79C950KC "Super Combo" CURIO, containing the equivalent of an NCR 53C96 SCSI controller (for the external port), an AMD 85C30 serial chip and an AMD 79C940 Media Access Controller (MACE) for the on-board Ethernet. There are also various nodes that don't correspond to
any
physical device, such as the ROM software components making up the AIX booter and XCOFF executable loader.
The Display Name Registry browser is interactive and you can drill down into the tree to show a node's properties. I've chosen these two on purpose because they're unique to the Apple Network Server: one of the two NCR 53C825 Fast'n'Wide SCSI-2 controllers, and the Cirrus Logic 54M30 video chip, better known to PC users as the STB Horizon+. These devices are both internally connected via PCI to the first Bandit. Drivers can match on their mandatory
name
property, which is its primary identifier (
53c825
and
54m30
respectively), or the optional
compatible
property generated from the vendor and device IDs.
This first version has three components: two for the Extensions folder, the ANS MACE Fixer, an
INIT
which patches the Ethernet configuration, and the ANS Video Enabler, an
ndrv
which allows the 54M30 internal video to be used in 8-bit mode; and for the Startup Items folder, the ANS Startup Fixer, a regular application which rewrites NVRAM to remove inappropriate settings placed there on every boot by the operating system.
The initial piece I put together was the video driver, which is in fact ripped directly out of the 2.0 ANS Mac OS ROM.
Hex Fiend
has a rich and extensible Tcl-based template system, including the ability to parse
many classic Apple binary formats
like resource forks and PEF. Eric Harmon's
ROM Fiend
extension builds on this by allowing you to parse components of classic Mac ROMs, here a dumped ANS Mac OS ROM provided by our former Apple employee. ROM Fiend splits the ROM into the declaration component and the system ROM ...
... and then allows you to walk the resources within it. This is the video driver embedded in that ROM. Notice the name of the resource is
53m30
, which was almost certainly an error.
The actual driver itself is the data portion. The magic sequence
Joy!peffpwpc
heralds a Preferred Executable Format binary (specifically these three FourCCs indicate an Apple-specific container, that the container is a PEF, and that the architecture is PowerPC) with code fragments. We clip out starting from there ...
... to the end of the data portion and the beginning of the next resource, and emit that section to disk as a separate binary.
All such drivers have a description block, usually heralded by the FourCC
mtej
(this code seems like it was based on someone's name — spill the beans in the comments if you know). The exact binary format is obscured a bit here by PEF's trivial packing method, used to reduce its footprint in ROM, but note the node name stored as a Pascal string (i.e., length byte first), and then the driver name, also stored as a Pascal string and invariably starting with a dot.
Immediately before the driver name length byte is an $06. The two bits set in this byte indicate that the driver is opened as soon as it is loaded (
kDriverIsOpenedUponLoad
, $02), and that the family expert is responsible for doing so (
kDriverIsUnderExpertControl
, $04). The PCI DDK documentation states that all video drivers should set these two bits, and only these two. The family expert handling graphics drivers is hinted by the FourCCs in the next line,
ndrv
for a general native driver service category, and
vido
for the type, in this case a graphics card.
You might well ask how the production ANS works at all without such an
ndrv
, and the answer is that Open Firmware doesn't need this driver to display anything on the screen — that's all specifically handled by the code in the ANS ROM, and Harpoon AIX has its own drivers. The ANS was never officially supported with Mac OS, so a proper Mac OS driver was never needed.
To make this extension eligible for loading, we need to fix the file's type code, which must be
ndrv
(
not
INIT
), and add a skeletal
cfrg
resource to tag the single code fragment. The other resources are not strictly speaking essential, but are desirable to give it an icon suite, a version string, and for
CCI™
, a plain-text description in the Extensions Manager. I created the icons from the ANS template in Hubert Chan's
M.A.C. icon pack
, which are far better artistic depictions than anything I could ever draw myself in ResEdit.
Although you'll never see a Happy Mac on the internal video when loading this driver from disk, you
will
see the screen turn on before the usual march of
INIT
s, because
ndrv
s load early. (They are also unaffected by holding down SHIFT to load with extensions off, since disabling them could cause the machine to be unusable. Remember that for one of my failures later.) Since we now have two valid displays in this ANS, here is an entire screen grab of both sides simultaneously (the grey boxes is where the identify digits were). Unfortunately the 2.0 ROM driver has the same issue as the AIX driver insofar as none of the chip's 2-D acceleration features are implemented, and the driver only supports 8-bit colour depth even though the chip is capable of much more. This is because the 54M30 provides only a little-endian view into the framebuffer — Apple never wrote anything to byteswap. A project for another day.
Still, the driver otherwise works fine, and we can see that it loaded as a native video driver in TattleTech.
The next thing I started working on was fixing reboots in Mac OS, since every time I shut down the machine I had to reset PRAM or make other changes. This wasn't too hard because I never keep the PRAM battery in it anyway (it's a test machine), but it did mean I had to frequently redo various settings between test runs.
In
our previous article in January
, we learned this was because Mac OS monkeys with the ANS' NVRAM settings as if it were a real Power Mac 9500, installing an inappropriate
nvramrc
OpenFirmware startup script that interferes with normal operation, and then sets the input and output devices to serial port
ttya
, which on the back is serial port 2 (yes, two). On Open Firmware 1.0.5 systems like most beige PCI Power Macs, this does nothing more than keep Open Firmware itself on the serial port; the video and ADB keyboard remain the console. On the ANS' 1.1.x firmware, however, it actually obeys these settings so that you can install and run Harpoon AIX over a serial port, and this was also apparently
how Shiner NetWare ran
. In this configuration the machine comes up with no video at all, though interestingly ADB devices are still useable in Mac OS, including the keyboard.
The Startup Disk control panel is at least
part
of this problem. In the
CDEV
are three resources,
OFpt
,
OFtb
and
OFtc
. The latter two define mappings between the Open Firmware platform identifier and the respective NVRAM settings in
OFpt
, which is stored as a single long null-terminated string with embedded Mac $0d carriage returns. (The unreleased
PowerExpress
turns up in this table as the Power Macintosh 9700.) When loaded, the
CDEV
overwrites the NVRAM settings with the one selected by platform.
Theoretically it should be possible to binary-patch in another mapping and then add a specific script for the ANS, which with this ROM would have a platform string of
AAPL,ShinerESB
. I determined this approach was unacceptable for two reasons: first, it required modifying standard OS components instead of adding to them, and second, it doesn't solve the
ttya
problem even if we alter the mapping so that
no
machines match. In fact, the very
string
ttya
appears
nowhere
in Startup Disk, suggesting the input and output device settings are being munged someplace else.
In the prior article we solved this issue using
Boot Variables
, a utility originally written by Paul Mackerras (
now at IBM
) which allows you to directly manipulate Open Firmware variables and save them. Because the changes to NVRAM occur before the boot process reaches the Finder, once we get to the Finder we can then fix everything and remain confident it will stay unmolested until the next boot. This process works but obviously requires manual intervention, so since Boot Variables is open source under the GNU Public License, I decided I'd just hack in a hard-coded version which automatically undoes the munge when run.
I converted it to build under CodeWarrior Pro 7 which is my preferred environment for classic Mac work, and rigged it so that it would display a quick window to show you it was working, do its work, and then terminate back to the Finder. When placed in the Startup Items folder, it will do this job every boot automatically, or can be run on demand. If the input device and output device are both
ttya
, it resets them back to the default
kbd
(ADB keyboard) and
screen
(onboard 54M30 video), and installs an
nvramrc
of its own. The critical code looks like this, using a library function I transplated to do the NVRAM patching in place:
patchstr(21, "kbd");
patchstr(22, "screen");
nvvals[7].word_val = 1; // belt and suspenders approach
patchstr(25,
    "0 to my-self\015"
    "dev /bandit/gc/mace\015"
    "1 encode-int \" PLSCCPort\" property\015"
    "device-end\015"
    "?cr \" Pre-production patches on.\" type\015"
);
The numbers are fixed indexes into NVRAM since this is just a hack, but in order are
input-device
,
output-device
,
use-nvramrc?
and
nvramrc
itself. This simple nvramrc patches up the Ethernet to work correctly with the Mac OS
Apple Enet
INIT
. Prior Macintoshes with Ethernet, including first generation NuBus Power Macs like the
Workgroup Server 9150
, had a single Ethernet AAUI port, but AAUI was expensive and unpopular and as the industry moved to twisted-pair Apple offered both an 8P8C ("RJ-45") and AAUI port starting with the 9500 — but still using just the single MACE, so only one port was active at a time. For as yet unexplained reasons, the ANS went back to a single AAUI port with no 8P8C/"RJ-45" despite being an evolution of the same platform base.
This means the MACE is connected directly to the (A)AUI port in the ANS, whereas in machines like the 7300, 7500, 8600, 9500, etc., it switches between the AAUI (equivalent to AUI) or an internal MAU to provide the link over twisted-pair. The MACE embedded in CURIO has a register called PLSCC, or the Physical Layer Signaling Configuration Control, which determines which network port is active. In dual-ported machines, the PLSCC value should be 7 (which includes the $01 enable bit), which corresponds to the "General Purpose Serial Interface" to the circuitry where the signal is routed. In the ANS, however, this value should 1, which specifies a direct AUI connection.
The ANS Mac OS ROM internally and explicitly specifies a property
PLSCCPort
on
/bandit/gc/mace
with that value of
1
. @joevt gets credit here (a) for  discovering that the Apple Enet
INIT
looks for and if specified uses this property as an override, relying on a platform default if not, and (b) for the magic incantation required to make this property stick when placed in the
nvramrc
. Since the ANS looks like a Power Mac 9500 to Mac OS, this value must be provided before Apple Enet runs, so since it's not in the 1.1.20.1 ROM we'll provide it ourselves in Open Firmware before the operating system even starts.
This scheme works and solves both the reboot-shutdown and Ethernet problems simultaneously. But what about bringing the system up from a cold start, where this property won't yet have been set? Well, we have a solution for that too!
The Mac OS
NameRegistryLib
allows us to directly manipulate the Name Registry (which will necessarily have a copy of our Open Firmware properties), so we can also get this property installed during boot as long as we do so before the Apple Enet
INIT
opens. We could do this with an
ndrv
, but we have a simpler and more conventional way which I talked about in this blog before with ways to
expand virtual Mac device support in QEMU
.
kanjitalk755
's tablet
INIT
installs a handler for USB HID devices during startup which allows QEMU absolute pointer positioning to work with its synthesized virtual USB tablet.
In this
INIT
, a block of 68K code (remember, the normal state of the Power Macintosh nanokernel is to run 68K code in the emulator) invoked at load time displays the icon and uses the Code Fragment Manager to pull a single non-static PowerPC function from the "
PPC
" resource (yes, P P C and a trailing space), set up a Universal Procedure Pointer to it as PowerPC native code, and run it. This code fragment is what installs the HID report handler.
Because this extension is so modular in design, we can just gut it and replace the
PPC
resource with our own code (yes, PowerPC code can run from resources, not just from the data fork), though I also manually patched the 68K section with a couple
NOP
instructions to not bother displaying the icon since we don't really need to. This is the entirety of the PowerPC code:
#include <MacErrors.h>
#include <NameRegistry.h>

// MACE Fixer for Shiner ROM 1.1.20.1
// (C)2026 Cameron Kaiser, all rights reserved
// MIT license
// oldvcr.blogspot.com

#define AIX "Devices:device-tree:packages:aix-boot"
#define MACE "Devices:device-tree:bandit:gc:mace"
#define PLSCCPORT "PLSCCPort"

// Any other function must be declared static!
void main(void) {
	OSErr err;
	RegEntryID regEntryID;

	// Ensure this is an ANS ROM that can boot AIX (2.0 doesn't, but doesn't need this)
	err = RegistryCStrEntryLookup(NULL, AIX, &regEntryID);
	if (err != noErr) {
		return;
	}

	// Find MACE and set the PLSCCPort property on it if not already done.
	err = RegistryCStrEntryLookup(NULL, MACE, &regEntryID);
	if (err == noErr) {
		RegPropertyValueSize s; 
		err = RegistryPropertyGetSize(&regEntryID, PLSCCPORT, &s);
		if (err == nrNotFoundErr) { /* may not be found if nvram patches not on */
			UInt32 port = 1;
			err = RegistryPropertyCreate(&regEntryID, PLSCCPORT, &port, sizeof(UInt32));
		}
	}
}
Notice the device tree paths for the two devices we're interested in,
Devices:device-tree:packages:aix-boot
(or, as an Open Firmware path,
/packages/aix-boot
) and
Devices:device-tree:bandit:gc:mace
(
/bandit/gc/mace
). We don't need to know anything else about what these nodes are or how they're connected to query and modify them. The first step this function takes is to see if this is an AIX-capable ROM by checking for the AIX booter package as a Name Registry node, and if this package isn't present, such as a regular Power Mac or the ANS Mac OS ROM, then we exit. The second step is to see if the
PLSCCPort
property already exists; if it does, such as being set from our
nvramrc
, we exit also, or otherwise set the proper value of 1.
Since the whole scheme can only work if our extension runs first, we give it the special file type of
scri
instead of
INIT
, which is notionally a WorldScript extension but can be used to load any sort of extension, because WorldScript extensions load before all other
INIT
s (
Apple Enet
is an
INIT
). Failing that, the name of the extension (
ANS MACE Fixer
) is intentionally chosen to lexically sort above
Apple Enet
so that it will also run first. The upshot is that the property will be set one way or another before the Ethernet
INIT
runs, and with this extension installed, now the only circumstance where our Ethernet
won't
work would be on the very first boot after a PRAM zap
with extensions off
— which would obviously be an uncommon situation.
It is also important to ensure that
main()
is the
only
non-static function in the code fragment because of the way the 68K code finds, declares and calls it (see
the prior article
for why). CodeWarrior's project settings can be set to build this file as a resource and after doing so we manually merge everything together in ResEdit for the final extension.
As our last stop before the installation instructions, let me also talk a little bit about something
not
in this version of the extensions pack.
The NCR 53C825 Fast'n'Wide SCSI-2 controller also has its own
ndrv
in the ANS Mac OS ROM. Indeed, it must, or else the internal SCSI wouldn't be bootable with that ROM (the production and pre-production ROMs have their own support and hand everything over to AIX after boot). It is possible to extract this
ndrv
and wrap it as an extension in the same way. It won't be bootable, of course, but in theory this should allow devices on the internal SCSI to be used once Mac OS has booted from the external SCSI. Go ahead and try it. It doesn't work. The machine will boot, but no devices are visible from the internal SCSI drive bays.
Apple PCI DDK 3.0 also includes a utility (
Load Driver Test
) where you can test the structure of an
ndrv
to see if it's valid (useful for hardware builders before they spend a lot of money burning defective ROMs). This utility basically checks if the
ndrv
can be loaded as a code fragment, and if it can, that it has a sensible driver description block, and shows the device node it's looking for and the driver name it installs.
We can immediately see from this that the node name is wrong. In the ANS Mac OS 2.0 ROM, the 53C825 nodes in the Name Registry are named
apple53C8xx
, not
53c825
as they are in the pre-production ROM. Triumphantly I changed the string and length byte to make the matched name
53c825
. It still didn't work.
The PCI DDK has an additional tool (
PCIPeek
) which allows you to mess around with PCI-based devices. When we ask it for the PCI configuration space for one of the 53C825s using the node name
53c825
, we can pull it up and see all 64 bytes are valid. Though the
compatible
name doesn't
fetch
, this does at least prove that the issue isn't the logic board and the node name is correct.
The next step was to look at the driver description in the hex editor. This is again another trivially compressed PEF. Like any well-behaved SCSI driver, it implements a fully-specified SIM (SCSI Interface Module), which, according to the SCSI Common Access Method (CAM), is the link between the 53C825 host bus adapter (HBA) and the transport (XPT) layer that in turn hooks into the SCSI drivers used by the operating system. You should be able to see the device node name and the Macintosh driver name, but the byte before the Pascal string for the Mac driver name here is $04. Unlike video
ndrv
s, the documentation states SCSI
ndrv
s should only have a single bit set in that byte, in this case specifying that the family expert handles loading the driver (
kDriverIsUnderExpertControl
, $04).
Since that didn't load nor open the driver, I tried setting various bit combinations of forcing it to load upon discovery and/or open upon load, all of which ended up hanging the ANS doing boot. Remember how I said that SHIFT doesn't stop
ndrv
s from loading? Each of these permutations thus ended up making the external SCSI volume unbootable until the poison
ndrv
was removed. I had to connect it to the WallStreet PowerBook G3 (it was handy) to get it out, though as a check I had the Wally boot from the same volume just to see what it would do — and it booted fine. The driver doesn't load on the Wally almost certainly because the device name doesn't match anything, which also implies the hang is specific to trying to bring up the device on the ANS or we'd hang on the Wally too.
This leaves us at the mercy of the family expert, so the next thing I tried was various combinations of service category and type. By default this is
ndrvgenr
, so I tried
ndrvscsi
,
ndrvblok
,
blokgenr
,
blokscsi
,
scsigenr
,
scsiblok
,
scsiscsi
,
blokblok
and finally an intemperate combination inappropriate for a family blog, and while none of these locked up the 700, none of them made any difference either.
After all that I'm not sure this approach would have worked for getting the internal SCSI bus working anyway, at least not without additional code. Apple's PCI documentation says, "The SCSI expert is simpler than some other experts" and while it mentions the situation of a "PCI card that wants to register a SIM with the SCSI Manager" which necessarily covers the situation of one in ROM, it says nothing about disk-based drivers. It's possible the SCSI expert just doesn't handle this situation because a non-bootable SCSI bus is certainly less useful, and while we could write up an
INIT
to try loading the SIM manually, I'm still pondering how this would work and I have yet to find a working disk-based driver for a 53C825-based card that I could hack as an alternative (suggestions solicited in the comments). The PCI DDK 3.0 notably includes a "driver" for this chipset, but only to let you mess around with the hardware — it's intentionally not structured as a SIM, so it wouldn't be an effective foundation.
But you can still try the other pieces, so let's pick up with the install instructions now that you have the prerequisites.
If you were working with a pre-built Mac OS disk image, using the system you used to build it put the ANS MACE Fixer and ANS Video Enabler into the Extensions folder, and the ANS Startup Fixer into the Startup Items folder. If you are doing the install on the ANS itself, simply have the CD disk image ready to go on your external device (or connect a real physical external SCSI CD-ROM).
Assuming you didn't tl;dr this article, your depowered logic board should now be fully reset. Close the drawer and lock the rear key and plug the server back in, then plug in ADB and your SCSI device. Remove all hard drives from the front; you can't boot MacOS from them anyway, and it will simply confuse Open Firmware. The CD-ROM and any tape drives may remain, though do note they currently won't work either. Connect your display to the
on-board
VGA port, not to any PCI video card, and finally power on the system. If you are using one of Jeff's current replica ROMs, you may need to hit Control-Command-Reset after powering up to get the bong (this is an electrical issue we're sorting out). From a cold start with no bootable AIX volume, the 1.1.20.1 ROM will automatically bomb into Open Firmware, showing you the prompt here. If you don't see this screen, make sure your monitor is connected to the onboard port.
If you've already prepared your external Mac OS volume and the extensions are in their proper places, just type
bye
at the Open Firmware
ok
prompt. You will see the message
/AAPL,ROM
MacOS is currently unsupported, use at your own risk.
while the ROM component looks for your startup disk. Once it finds it, there will be a pause, then the screen will flash and drop into the Mac OS mid-boot. Remember, the Startup Fixer must run
once every time Mac OS starts up
, or your system will come up with a black screen on the next boot. You can manually fix this by entering Open Firmware with a serial connection to Port 2 (38400bps, 8-N-1) and enter
setenv input-device kbd
,
setenv output-device screen
,
setenv use-nvramrc? false
and
reset all
, or you can just reset the logic board.
If you are doing an install from an external Mac OS CD-ROM or CD image,
move your display to the PCI video card
and then
blindly
type
bye
. You will get the Mac 50% dithered grey, then a Happy Mac, then the CD should start. Install Mac OS as usual to your previously prepared blank disk image. After the installation completes, if you can, install the extensions (e.g., from a floppy disk or via AppleShare over LocalTalk) and startup item as described above
before you shut down
. Either way, shut down, power off and reset your logic board again, disable or remove the CD-ROM/image, move the display back to the onboard video port, and power back on to the Open Firmware prompt. If the extensions were installed, just type
bye
— you're good to go. If you couldn't, move the display to the PCI card again, blindly type
bye
, bring up Mac OS from your external volume, install the extensions, shut down, power off and reset your logic board one last time, then move the display back to the onboard video port.
Now
you can boot by just typing
bye
also.
Things still to do:
Get the internal SCSI bays working, which may require us to create a modified ROM and put the
ndrv
there with the proper node name. However, one other possibility is by installing a MacOS-bootable SCSI PCI card. The Shiner logic board has 68-pin connectors on the logic board that directly feed into the two front SCSI busses (bus 0 controls the top four trays and bus 1 controls the bottom three and the 700's rear two). These connectors were intended for the ANS PCI RAID card, but I don't see why we couldn't just connect a regular controller there as long as we change its SCSI ID to not conflict with the 53C825, which should be possible on Adaptec cards with the PowerDomain Control
CDEV
. I intend to do some experimentation with that, including finding an optimum card which is Mac-bootable (or flashable to same) and supports full Fast'n'Wide SCSI-2, yet is
not
supported by AIX so that the regular 53C825 will "just work."
On a reboot, the ANS may go into its Long RAM Test. This is not only
not
fatal but is arguably intended behaviour and it will start normally afterwards, though the delay is annoying. On the other hand, even though the ANS Mac OS ROM doesn't do this, it also doesn't properly register the sticks as parity RAM even if they are. I don't know if I can fix this by tweaking Open Firmware or this requires a ROM patch, though I suspect it's the latter. In the meantime, you can manually cut it short by hitting Control-Command-Reset.
Hopefully you'll see solutions to one or both of these in
a future article
. For now, you can get everything on
the Github repo
, including source code for CodeWarrior Pro 7. Note that this compiler cannot build the 68K portion of the ANS MACE Fixer, but I've included the source for that too, and you don't need to build the 68K segment anyway merely to modify the PowerPC portion. Each portion is under its own license and you should read the brief notes. No AI was used.
