---
title: "The Apple Network Server MacOS ROMs have resurfaced"
url: "https://oldvcr.blogspot.com/2025/10/the-apple-network-server-macos-roms.html"
fetched_at: 2026-04-28T07:02:04.354861+00:00
source: "oldvcr.blogspot.com"
tags: [blog, raw]
---

# The Apple Network Server MacOS ROMs have resurfaced

Source: https://oldvcr.blogspot.com/2025/10/the-apple-network-server-macos-roms.html

The 1996 Apple Network Server was Apple's first true Unix-through-and-through server (the Apple Workgroup Server 95, actually a Quadra 950 with a special PDS card limited to A/UX, doesn't really count) and
through a complex history
came to run
IBM's AIX
as its native operating system. I actually had an ANS 500 when it was almost new, in 1998, and it ran Floodgap until 2012. It is still in my collection and still runs, along with an ANS 700 I later acquired and a (sadly battery bombed)
"Shiner ESB" prototype that used to be at Netscape
. AIX was your only choice — no other operating system was supported.
Still, it was a relatively open secret that the ANS was heavily derived from existing Power Macintosh hardware, most closely the Power Macintosh 9500, and early "Shiner" prototype systems were even demonstrated with MacOS. This was apparently the underpinning of
Apple's brief flirtation with NetWare as a server OS
, variously codenamed Wormhole, Deep Space Nine and most famously Cyberpunk. Then-CEO Michael Spindler made public statements supporting NetWare on Apple hardware; Wormhole was reportedly demonstrated on an early prototype likely of
the Workgroup Server 9150
and Cyberpunk was explicitly meant for Shiner. Cyberpunk will no longer run on an ANS with production ROMs, but reportedly did run on ANSes with pre-production ROMs that could still boot MacOS, and
does
run on early NuBus Power Macs like the Power Macintosh 6100, which is
how we demonstrated it
. However, potential customers strongly preferred a Unix option and Apple had an arrangement with IBM around AIX, and so as the last operating system still standing that's what
the ANS ended up running
. Production ANSes as sold with the standard Open Firmware 1.1.22 ROMs lock MacOS out entirely and you get a message like this:
Although an old nerds' tale circulated at the time saying you could pull 9500 ROMs, put in a video card and boot from an external hard disk (because the video chip and internal SCSI controller are unique to the ANS and weren't supported by the 9500 or MacOS), this couldn't possibly have worked because among other things the Bandits in the ANS are mapped differently. Lots of people, including yours truly, had certainly tried. Still, I was used to AIX as an AIX administrator since the 3.2.5 days on real RS/6000 hardware and the ANS ran it splendidly, so today mine still runs it (4.1.5 is the last AIX release supported).
But to me the best thing about the ANS was that I got a big beefy RISC server for a summer's work, so I didn't have to plump down a credit card. For everyone else, the ANS was expensive (starting at $10,000+ in 1996, a cool $20 grand in 2025 dollars) and Apple wasn't moving many. CEO Gil Amelio had lured Ellen Hancock away from National Semiconductor as Apple's new CTO and tasked her with finding a new path for the MacOS, though in the meantime Apple had this big hulking midrange server that wasn't selling. So, as an attempt to juice sales, Hancock announced at Comdex 1996 that the ANS would be able to run other operating system choices, not just AIX. MacOS was an obvious one because it already had before, but Hancock also proposed Windows NT to the great surprise of attendees. While Windows NT was built to be system-agnostic and versions already ran on PowerPC hardware, and people have since
hacked it to run on Power Macs
, this would have been the first time it could officially ever run on an Apple machine.
Hancock's assertion was a simple ROM change would do it, and as it happens the ROMs on the ANS are conveniently on a small daughtercard that can be replaced. However, it seems that the market was sceptical this could work — heck,
I
was sceptical while doing the story research, since I knew no such ROMs were ever publicly sold — and the recently-returned Steve Jobs talked Amelio into cancelling the ANS line
and OpenDoc
both on the same day in 1997. Nothing more ever turned up about either option.
Recently a former employee who was on the business development team for Apple's server products
posted on the Tinker Different boards
: not only did he have the mythical MacOS ROM, he had it installed in a Deep Dish booting the MacOS. Deep Dish was the code name for the planned but unreleased ANS 300, a small rackmountable version (as opposed to the rackmount plates Apple sold for the 500 and 700 which take up a whopping 19U), so here was a prototype machine running development ROMs booting an operating system it was never actually sold with. More to the point, he confirmed the Windows NT ROMs actually did exist and worked as well.
Though he didn't have the NT ROMs, he did dump the two development ROMs he had (a third is in progress) which included the MacOS ROM — and now we have them for analysis. What's interesting is that both the explicit MacOS ROM and the Open Firmware 2.26b6 ROM he dumped seem capable of booting MacOS, though the 2.2 ROM has strings saying
MacOS is unsupported, use at your own risk.
and
MacOS requires PCI video card and external SCSI boot disk.
(which may lend credence to that old nerds' tale, assuming you had the right ROMs, not the 9500's). However, the full MacOS ROM reportedly "just works," all the way to Mac OS 9; one wonders if with XPostFacto you could drag it into OS X that way, giving it another Unix option besides AIX, Linux and NetBSD, the driver issue notwithstanding. Though the MacOS ROM does not use the ANS's front-mounted LCD, which is one of its best features, it wouldn't seem difficult to come up with an INIT extension for it. A particularly tantalizing thought is this might also get Cyberpunk running on a Shiner for the first time since 1996, the very machine it was intended for.
To make all that happen, of course, we next need to get the MacOS ROM on an actual ROM card. The ROMs this individual had were flashable and I need to do some looking at mine, and the connectors aren't common. Nevertheless, the first step is to actually
have
the ROM and now we do. I'm hopeful that this breakthrough might encourage further exploration of my favourite Apple server and that someone out there has the NT ROMs and steps forward. The Apple Network Server was always a cult favourite as one of Apple's more notorious white elephants and now almost 30 years after its introduction there may be even more fun things to do on it. If you know where to find them, post in the comments or drop me a line at ckaiser at floodgap dawt com (happy to keep you anonymous if you prefer which I have done for other former Apple engineers in the past).
