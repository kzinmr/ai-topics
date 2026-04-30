---
title: "See Jane 128 by Arktronics run (featuring Magic Desk, 3-Plus-1 and the Thomson MO5)"
url: "https://oldvcr.blogspot.com/2025/06/see-jane-128-by-arktronics-run.html"
fetched_at: 2026-04-30T07:01:19.424093+00:00
source: "oldvcr.blogspot.com"
tags: [blog, raw]
---

# See Jane 128 by Arktronics run (featuring Magic Desk, 3-Plus-1 and the Thomson MO5)

Source: https://oldvcr.blogspot.com/2025/06/see-jane-128-by-arktronics-run.html

"Look," says Jane. "I'm a computer program. Run, computer program, run."
I still maintain that the 1986
Commodore 128DCR
is the best 8-bit computer Commodore ever made: built-in 1571 disk drive, burst mode serial, detachable keyboard, 2MHz operation, separate 40 and 80 column video, CP/M option, a powerful native mode, full Commodore 64 compatibility and no external power brick. But when the O.G. "flat" 128 was coming to market in 1985 Commodore really wanted it to be the business computer the 64 wasn't (and prior efforts like Magic Desk and Plus/4 3+1 didn't help). Unfortunately for Commodore, it would still be at least a year before the sophisticated GUI of
Berkeley Softworks' GEOS
arrived on the 64 and another year after that for the native 128 version, so to jump-start the productivity side, the management in West Chester contracted with a small Michigan company to port their Apple II software suite to the new machine — which Commodore then sold under their own name. That company was Arktronics, led by Howard Marks and Bobby Kotick — the very same names later at Activision — and the software package was Jane.
I never used Jane myself back in the day, or for that matter any 128 native word processor, and even when we got a 128 I still wrote my term papers in Pocket Writer 64 or Timeworks Word Writer. However, that faulty but repairable Australian Commodore 128DCR
I got last Christmas
came with a big box of software and in there was a complete copy of Jane 128 along with the data disk the previous owners' family had used. They were delighted when I said I wanted to take a whack at converting their files as a thank you — and along the way we'll take a look at Jane's oddball history, the original Apple II version, the Commodore 128 version and its all-but-unknown port to the French Thomson MO5, plus those
other
attempts at productivity applications Commodore tried in the mid-1980s.
PETs, of course, had many productivity software options and even the VIC-20, if suitably upgraded, could manage basic tasks. Some small businesses reportedly even used them for simple finances. The 64 itself was hardly an ideal productivity machine when introduced in 1982, but it was certainly far more up to the task than the VIC-20 was and many such software packages were naturally available later on. Initially, however, dealers and customers openly groused about the absence of a spreadsheet or even a word processor, much to Commodore chief Jack Tramiel's profound displeasure. The task of rectifying this situation was handed to executive Sigmund Hartmann and his recently consolidated Commodore Software division, formed in April 1983 from the prior two separate software units handling system software (under Paul Goheen) and games (under Bill Wade).
At least one side project would become critical to the reworked division. Engineer John Feagans had been the initial developer of the PET Kernal, its internal ROM-based operating system, which pioneered the then-novel idea of separating I/O and other system routines from the built-in Microsoft BASIC. (Prior versions of BASIC on early microcomputers often simply drove devices directly.) Feagans' innovation facilitated the use of these routines by user-written machine language programs through a standardized jump table, which was reused and greatly expanded by Bob Russell for the VIC-20 and 64.
Feagans' side project was a PET demonstration of a small picture-based file manager, using an office filing cabinet as its central metaphor and drawn with PETSCII graphic characters. In 1982 the Commodore office in Moorpark, California where Feagans worked was closed and he was reassigned to their then-executive offices in Santa Clara. With little else to do at the time, Feagans rewrote his file cabinet demo for the new 64 to get familiar with the hardware, primarily in BASIC. As an exploration of the 64's joystick and moveable sprite capabilities, he additionally implemented an animated "hand" controlled by the joystick that served as a pointer. By this time Hartmann had just weeks until Summer CES in June 1983, the deadline he had promised Tramiel. While working on licensing deals with outside firms, Hartmann also ordered Andy Finkel, promoted from the VIC team to technical manager, to find anything the software division was already working on that could get finished fast. Finkel saw Feagans' new demo and convinced Hartmann that it was both feasible and viable as a product.
Magic Desk was completed by Feagans, Finkel and other Commodore developers at record speed, recruiting resources from Rich Wiggins' speech group in Dallas, Texas and marketing and documentation head Michael Tomczyk, who in turn brought in artist and programmer Jeff Bruette to develop the sprite-based icons and additional PETSCII backgrounds. With time being a severely limited resource, after completion of the typewriter and filing cabinet it was instead decided that this Magic Desk would be the first of a whole line of Magic Desk software between which data could be exchanged. This was Magic Desk I: Type & File, and it made it to CES along with almost 70 other programs for the 64 and VIC-20. "We want everyone to know that Commodore's in the software business," Hartmann declared to
COMPUTE!'s Gazette
.
Like many Commodore Software titles Magic Desk was released on cartridge, a wise decision as it started up within seconds, and its interface was colourful, audacious and unlike anything else at that year's CES. (At the time Feagans claimed never to have seen the Apple Lisa or Xerox PARC machines when he developed it, though his recollection later varied.) As a result it quickly overshadowed the software division's other C64 productivity titles licensed from outside companies, such as Easy Script from British developer Precision Software Ltd which débuted at the same show.
When it eventually emerged for sale in the fall, however, reviewers were somewhat less enamoured. Although the user-friendly appearance was praised,
RUN
found the hand pointer difficult to manipulate and complained "the Help screens [were] little or no help," and
Ahoy!
noted the file cabinet required a disk drive and the questionable use of RELative files for storage, slowing access and hampering interchange. Reviewers also were quick to notice the icons for later planned Magic Desk modules, nevertheless already on the desktop yet programmed to do absolutely nothing. But the most unanimous and direct criticism came for what few built-in applications there were, especially the centrepiece typewriter which was seen as limited and idiosyncratic — and moreso given Magic Desk initially sold for $71.95 (in 2025 dollars over $230) at a time when other, better and often cheaper options had since become available, including from Commodore themselves.
InfoWorld
was the harshest of its detractors, concluding, "We really question whether Commodore's approach with Magic Desk is the best way to develop 'people literacy.'"
Part of this cost was the expense of manufacture. Magic Desk initially came as 32K of ROM in four 8K chips, quite possibly the largest cartridge developed for the 64 at that time and requiring additional logic on the PCB for bank switching. (Its design is still used to this day for large multicarts, now supporting as much as a megabyte of ROM.) Internally, although some code had been converted to machine language using a custom compiler, there wasn't enough time to do it all and a fair portion of Magic Desk thus remained written in BASIC (moved up to start at $0a01 instead of $0801). As part of initialization this BASIC program is read out of the ROMs and copied to RAM for execution, which is the slight pause at the beginning before the title screen appears.
Despite the cool press reception, Magic Desk sold surprisingly well to new 64 users, and in numbers sufficient to solve its production problems such that its price dropped in half by late 1984. Sales were enough to propose an upgraded version called Magic Desk II for Commodore's new (and, ultimately to its detriment, incompatible) 264 series, capable of speech prompts when paired with the speech group's Magic Voice synthesizer hardware, and featuring a more sophisticated interface with "Lisa-like" pulldown menus and icons.
At the same time the software division finished the remaining pieces of the original 64 Magic Desk (now simply called "The Magic Desk"), also with speech capability; the screenshots here of the presumably completed budget and phone modules are from prototype ROMs in an auction lot of Feagans' old Commodore memorabilia, double the size of the original version.
Commodore intended the upper-tier 264s to be home and small business productivity systems, designing their hardware and TED video chip to match, with the 64 remaining as their general purpose gaming and home computer. Tramiel strongly believed, as Michael Tomczyk wrote in
The Home Computer Wars
, that "home computers would have the power of small business computers like IBM and Apple — but would be priced like home computers, perhaps as low as under $500." Smaller versions of the 264, with their much lower part counts, could even compete in the ultra-low market segment against systems like the ZX series in the UK.
As Hartmann, Tomczyk and others in the software group felt the 264 would be most meaningful with built-in software, Magic Desk II became one of several possible option ROMs representing potential machine configurations, along with others featuring different programming languages or applications like a spreadsheet or terminal program. Tramiel embraced the idea, seeing it as a car with different models "just like General Motors." At least three "flavours," aligning with the internal groups in the software division (business, home and education), were envisioned — though the concept also met swift resistance from dealers and even Commodore's own sales team who protested having to handle multiple different versions of one computer. (One possible unspoken reason is that it was already known not to be 64 compatible, and dealers were undoubtedly unhappy about taking stock space away from a financial anchor.)
With time yet again a factor, for the top-end "business flavour" the software division looked for a quick potential port and found it in Trilogy, a forthcoming 64 software package from Orange County, California-based Tri Micro demonstrated at Spring Comdex 1983. Trilogy was to be a combination of three existing Tri Micro programs, Your Home Office (word processor and spreadsheet) and The Write File (word processor and database) merged into a single application, and Plus Graph (charting) — what would have been called "integrated software" in those days. Commodore contracted with David Johnson, its developer and Tri Micro's VP of software engineering, to also port it to the 264.
In January 1984 Jack Tramiel was forced out of the company he founded by chairman Irving Gould and shortly thereafter the 264 line was slashed by new CEO Marshall Smith. Three models were chosen from the various prototypes and experiments, the 16K 16 (and in Europe the 116 as well) to serve as the low-end, and the 64K 264, now renamed the Plus/4, as the high-end. Both the completed Magic Desk and Magic Desk II were cut, as was the education flavour based on a built-in Logo implementation. Only the Plus/4 would offer Trilogy, renamed to 3-Plus-1, and its ROM size was cut to 32K to reduce production costs further which in turn forced Johnson to make serious reductions in functionality. As a result 3-Plus-1 became nearly as maligned as the Plus/4 itself (mocked in the press as the "Minus/60" for its idiosyncrasies, deliberately incompatible ports and lack of 64 software compatibility), though yours truly actually used the spreadsheet for a household budget when I was a starving student, and
it wasn't
that
bad
.
Nevertheless, as evidence of the hasty last-minute switch, the Plus/4 manual still makes vague reference to "built-in software packages," saying the computer will tell you "which packages are available and which function key to use to activate them." There was only ever one in the production model, and it was 3+1. As Tri-Micro had still maintained the rights, Trilogy was subsequently released in its original form for the 64 as Team-Mate to the rave reviews 3-Plus-1 never got (in July 1985
RUN
called it "a high-performance program that Commodore users will discover to be one of the best available"). Johnson later got his chance to show what 3+1 was really capable of with
Plus/Extra
, a full disk version sold by Tri Micro, but it lacked the close integration of both Team-Mate and 3+1 and ended up tainted in the market by its predecessor. Commodore never adopted it.
The failure of the Plus/4 to succeed the 64, much less overtake it, demonstrated clearly to Commodore management that 64 compatibility was essential in their next computer. Around this same time Sig Hartmann had noted the success of Atari's own first-party software unit Atarisoft on non-Atari platforms (though
AtariLab was developed externally
), even for the 64, and said there were similar plans to port Commodore first-party software and licenses to the Apple II, IBM PC and PCjr. (NARRATOR: This didn't happen.) However, by mid-1984 the software division had also developed a reputation for poor quality, with Scott Mace commenting in
InfoWorld
that — hits like International Soccer notwithstanding — "so far, the normal standard for Commodore software is mediocrity." In the meantime, Tramiel had bought the ailing Atari from Warner Communications and lured several Commodore managers, including Hartmann (who was already in conflict with Smith over cuts to the software division), to defect. Paul Goheen, the former systems software group head, became the new software chief.
As the Commodore 128 neared completion, management constructed a new sales strategy to put it head to head against the Apple IIc and PCjr in specialty stores as well as Tramiel's favoured mass market retailers. To more plausibly bill it as a productivity machine, once again the software division had to look outside the company.
Arktronics started in the dorms of the University of Michigan as a partnership between sophomore Robert "Bobby" Kotick and junior Howard Marks, who were then roommates. "We knew that unlike other industries," said Kotick in a 1984 interview, "there was a place for 19 and 20 year olds [in computers]." In July 1983 the company was formed to capitalize on Marks' ideas to envision a friendlier user interface for productivity applications. Marks, who was French, had previously worked for Apple and had access to its peripherals, including the then-novel use of a mouse as a pointer device. "This was way before there was ever a Lisa," Kotick added. "We realized that the biggest problem was that people like us couldn't use these things [computers] yet because they were too difficult and time-consuming to learn." They crafted a wish list and design document oriented to systems with 64K of RAM or less but featuring a picture (now we'd say icon-based) interface driven by a pointing device, such as a joystick or mouse, and an extensive on-line tutorial.
Marks and Kotick hired students and even lured away some professors to work on the application, christened Jane after the
Dick and Jane
introductory reading books, who accepted shares in the company in lieu of salary. To fund development by their team of about thirty, Kotick tagged along with a friend to the annual Cattle Baron's Ball in Dallas at which he met real estate and casino investor Steve Wynn. Kotick managed to hitch a ride back to the East Coast on Wynn's plane where he pitched him on their company and Wynn encouraged him to write up a business plan. Three months later Marks and Kotick were summoned to Wynn's offices in Manhattan and flown to Atlantic City, whereupon Wynn handed them a cheque for $300,000 (in 2025 approximately $970,000) in exchange for a third of the company, providing business advice as the product progressed.
Jane missed a first deadline for Comdex in December 1983 due to testing delays and finally launched at Softcon in February 1984 for the Apple II/II+ with 64K and the IIe at an MSRP of $295 [$920], later reduced to $179 [$560]. The program shipped on three colour-coded floppies, a grey bootable "systems disk" containing the word processor, database and spreadsheet applications (Janewrite, Janelist and Janecalc, respectively), a yellow "help disk" with the tutorial, and a black "data disk" for the user to save files. To ease the need for disk swapping, it would hunt for the right disk in either disk drive if you had two. Versions for the IBM PC and Atari 8-bits were said to be in progress.
The initial release was uniquely accompanied by
its own single-button mouse
(Instagram link), a lower-cost unit — Kotick admitted settling for "a lesser quality product" — manufactured under contract by joystick maker Wico and incompatible with Apple's own later mouse options. This mouse interfaced to the Apple with a custom card and an 8-pin connector.
Jane's appearance at the show attracted attention from another Steve, but at the Apple booth instead: Steve Jobs. Jobs visited the company in Ann Arbor and, suitably impressed, told Kotick and Marks they were wasting their time in college. Kotick duly dropped out to concentrate on the company, much to the consternation of his parents.
Because it was intended to run on any existing Apple II with sufficient RAM, pretty much nothing was assumed about the hardware. It displayed strictly in monochrome and used the Apple hi-res mode to display upper and lowercase since the II/II+'s text mode was purely uppercase. Additionally, as 80-column capability wasn't universal, it used a software text shaper to display 60-column text in the word processor and, here, in the file requester. Basic windows like these, with title and information in the actual window bars, served for dialogue boxes and file selection.
Although no emulator presently supports Jane's oddball original mouse, the PBS MacNeil/Lehrer NewsHour did
a piece on Arktronics
in 1984 (the photo above of Marks and an open Apple II case is from this clip) and, along with pictures of the Arktronics offices which I've scattered throughout this article, had some screenshots that illustrate its capabilities. Here a document is being edited in Janewrite. You can see close, scroll and size gadgets in the window frame, but interestingly the control to maximize the current window is in the lower right.
The top of the screen shows the editing tools (hand pointer, arrow, scissors [cut], camera [copy] and paste jar), icons for the three core apps, and then system-wide icons for on-line help, printing, the file manager, preferences and "STOP" to globally cancel an operation. Across the bottom, beside the window maximize gadget, are tools for adjusting line justification, font style (bold, underline, bold and underline, superscript, subscript), print settings and search. I'll have more to say about all of these when we get to Jane's Commodore port.
Document windows could also be moved and resized, and multiple windows from different Jane applications could be open simultaneously.
If you hit Control-Reset, a Easter egg briefly flashes on-screen with the names of the Apple II programmers: Mike Lagae, John R. Haggis, Brent Iverson, Jim Poje, Peter Lee, Uwe Pleban, Allen Leibowitz and Ken Roe. Because portability to other, sometimes wildly different, systems was always contemplated, application-level components were written in a high level language and compiled for the target (allegedly an early microcomputer dialect of C), with the graphics and I/O drivers written directly in assembly. With the release of the IIc Arktronics updated the program to support Apple's mouse as well.
Reviews of the Apple II version were decidedly mixed. In June 1984,
InfoWorld
called it "innovative" but also observed that "overbearing use of icons, some slow features, and some awkwardness mar the product, which could benefit from an emphasis on efficiency rather than gimmickry." Down under,
Your Computer
in November 1984 liked the simple interface and believed it would appeal to undemanding users but criticized the 236-page manual and found the mouse unreliable. "When the mouse works properly, it is good," wrote reviewer Evan McHugh, but "when it doesn't it's the pits." Likewise, although
A+
's 1985 review also liked the interface and the fact that multiple windows from each module could be open at once, the magazine also felt that "the individual modules in Jane are not up to professional productivity quality." Perhaps because of the software display, Janewrite "was too slow to respond to the keystrokes of a moderately proficient typist," and Janecalc, equally slow, was also panned as "crippled" because it only supported a 24x20 maximum spreadsheet. "Thank you, Jane," quipped reviewer Danny Goodman, "[l]eave your number at the door."
Jane was also billed as available for the Commodore 64, even in contemporary advertising, but
COMPUTE!'s Gazette
in January 1985 said it was "scheduled to be released for the Commodore 64 by the time you read this. The price is expected to be about $80 [$240]." Interviewed for the article, Marks said that Jane for the 64 was to come as a combination cartridge and disk package, where a "32K plug-in cartridge" would quickly and automatically bring up the system. The article claimed the cartridge would autoboot the applications from (now) just a single floppy plus the data disk, though I suspect the actual configuration was that the
cartridge
contained the applications and the disk contained the online tutorial, simultaneously furnishing a modicum of both instant access and copy protection. Notably, this version didn't come with its own mouse; Marks said they were working to support third-party mice as well as joystick and "touch pad" (presumably KoalaPad) options instead. Accounting for publishing delays, the
Gazette
piece would have been written several months prior in the fall of 1984 —
after
advertisements for the C64 version of Jane had been in multiple periodicals such as
Creative Computing
and
Family Computing
claiming you could purchase it already.
In fact, the 64 version of Jane would never be released — it was simply cancelled once Commodore paid Arktronics to port it to the 128 and badged it as a Commodore product. As the 128's graphic and sound capabilities are virtually identical to the 64's in 40-column mode, save for the extra colour RAM, the port was relatively straightforward. (At the same time Commodore also rebadged the CP/M-based Perfect Software series from Thorn EMI for the 128, but this was non-exclusive, and their rebranded versions were exactly the same as sold for other CP/M-compatible systems. Goheen promised "comprehensive and professional developer support" for the new computer.)
The new Jane could also be made cheaper: since the 128 is capable of autobooting a suitably coded floppy disk in drive 8, the cartridge could be dispensed with and the less expensive three-floppy scheme restored (though the grey disk was now called the "application disk"). A 128-mode 1541 fastloader is used if the new and much faster 1570 or 1571 disk drives aren't detected, though the 1571 still boots Jane noticeably faster than the fastloader.
(Parenthetically, a frequent misconception is that the Z80 in the 128 does the boot sector check to start CP/M. In fact, the 8502 does that after the Z80 has already checked the Commodore key isn't down and entered 128 mode. In CP/M's case, the code in the CP/M disk boot sector instructs the 8502 to give control back to the Z80 so it can finish the boot sequence — if this weren't the case, the BASIC
BOOT
command wouldn't be able to start CP/M. Interestingly, 1581s booting CP/M have a special startup file to keep their own CP/M boot sector
in a different location
.)
Otherwise, Jane 128 openly betrayed its origins on the 64: other than fastbooting with the 1571, which it mostly got for free, and support for the 128's new keys it took no advantage of any other 128 features, in particular no 2MHz support nor true VDC 80-column mode. Although the manual and box copy say using a mouse is supported, only the original 1350 mouse works, which strictly emulates a joystick. All three applications that were in the Apple II version are included. Under the hood the apps are implemented as overlays for a central kernel called
JANEGM
. Sadly, I didn't see any obvious credits while scanning through the disk files.
The manual, which appears to have been written by a third party, insists on camelcasing the apps as JaneWrite, JaneCalc and JaneList even though the rear box copy doesn't distinguish them that way and the Apple II version and Arktronics' own advertising called them Janewrite, Janecalc and Janelist. I'll use the latter here.
Commodore also included some official marketing material with the box, hawking their new 1902 monitor (with 80 column mode, which was useless for Jane), 1571 disk drive (which works well with Jane), 1670 Modem/1200 (which Jane doesn't use), 512K REU (which Jane doesn't use either) and the 1350 mouse — which in this photo is somewhat different-appearing than the released 1350/1351, and might have been a mockup. Actually, this system would have been a very nice 128 setup and very similar to the one we'll be using both for real and in VICE. Too bad Jane 128 could use relatively little of it.
Both Jane and the Perfect series were demonstrated with the 128 for Winter CES 1985, though Commodore didn't announce MSRPs then for any of them at the time. It eventually emerged later that year for $49.95 [$150]; by the next year some retailers were selling it for as low as $35 [$100], compared to each of the Perfect titles then going for $45 apiece [$130]. Plus, the Perfect titles, being CP/M-based, were bland and text-based and failed to show off the C128's graphics, so Commodore ended up emphasizing Jane more in its contemporary marketing.
Booting Jane 128 from the 128DCR's internal 1571 drive with my own 1902 monitor.
Although its interface is similar to the Apple II's in broad strokes, Jane 128's most obvious difference is colour. However, there are numerous more subtle UI changes in this version, sufficient for it to be called "Jane 2.0" internally before release. We'll step through them here and in the next set of screenshots because they're an interesting comparison point to modern human interface practice.
As with the Apple II, across the top of the screen are the various icons, or what the manual calls "pictures." These were slightly altered for the 128 from the Apple II originals. The blue icons again set the mode of the pointer ("tools") from the hand pointer, the insertion arrow, scissors (cut), camera (copy) and paste jar. The current tool is highlighted. You select a new tool by clicking on it, but you can also use the function keys (CLR/HOME, F1, F3, F5 and F7).
By modern conventions Jane's tools are used backwards: instead of selecting a text range and "choosing a tool" (e.g., Command-C for copy) to operate on it, you choose a tool first and with that tool select the text range it operates on. I'll demonstrate this specific functionality in a couple instances, but any verb-object operation in Jane will work this way. (Linguistically, this makes Jane a
head-initial language
, while most modern GUIs are head-final.)
Next to the tools are the main apps, Janewrite (now in purple), Janecalc (in green) and Janelist (in cyan), and next to them in grey are the same standard applets built into the kernel (online help, print dialogue, disk/file manager and setup). Finally, the STOP icon, now a solid red, stops the current app, and can be used to escape some screens, though not all. Unexpectedly it doesn't serve to quit Jane entirely: you just turn the computer off. Jane remembers what app is loaded and doesn't reload the overlay if you exit and re-enter it.
However,
unlike
Jane for the Apple II, Jane 128 does not allow you to have multiple documents open simultaneously, a limitation that challenges the definition of "integrated software." In fact, of the three official Commodore productivity packages we've looked at so far, only poor abused 3-Plus-1 could do so. If you're working in one app and select another, Jane 128 will prompt you to save your work as if you'd clicked STOP, and the window will close. Given that the Apple II version managed to implement multiple documents in 64K of RAM, the Commodore 64 version — let alone the 128 — would seem to have little excuse, though I can think of two potential explanations. One is to increase the amount of memory available for any one document, which the Apple II version was indeed criticized for. The second is particular to the 128: its default memory configuration doesn't have a lot of free RAM, and it may have been judged too complicated to span or swap working sets across banks. (Some fiddling in the monitor shows that the documents simply occupy RAM in bank 1 and don't span elsewhere.) On the other hand, other 128 applications certainly do manage it, and it's possible development deadlines were a contributing factor.
Let's start out with the online help, one of Marks and Kotick's fundamental design goals. Assuming you got the joystick (or 1350) plugged into the right port, there's a big honking question mark. What happens when you click on it?
You get right into the online help window. The pointer snaps to the options; you can also move the pointer from option or cell to another option or cell with the CRSR keys/128 arrow keys and select it with the Commodore key.
The window's yellow border is salient: any window that gives you choices to select from carries a yellow border. We'll see this again later. Incidentally, the manual is not in colour (just black, white and an accent magenta), and possibly as a result is all but totally ignorant of these UI choices or why they were made.
The Apple II version's windows have a corner close gadget in the typical open square style, but this would only have made visual sense to someone familiar with the Lisa or Mac — which most Commodore users in 1985 wouldn't be. Instead, here windows you can close have a big bright red EXIT button (the ESC key can also serve this role in most cases). All icons are simply drawn onto the VIC-II high-res screen; unlike Magic Desk where pretty much everything was a sprite, the only sprite here is the pointer. Windows cannot be moved or resized, but by limiting icon and window boundaries to VIC-II 8x8 cells, drawing is fairly fast.
Of course, most of the topics are on the yellow help disk (see? it matches). Jane 128, like the Apple II version, supports two disk drives, so you could have the help disk in device 9 and it would find it.
The online help is pretty good, considering. It shows the icons and images as they would appear on-screen, and while they aren't live, they are accurate. The only black eye it gets is the technically truthful but functionally insufficient prompt "Press a key to continue" — the joystick or 1350 mouse button also work, and so does the ESC key to exit early, even though the exit button isn't shown. Some help items are animated and show you a demonstration, and each app has its own bespoke help.
The system keeps track of what disks are where. If we start Janewrite by going to the typewriter, this blue dialogue box will appear — informational dialogue boxes always have a blue border — as it loads the overlay ...
... but then looks for a data disk, fails to find it, and asks for one. You need one even for a new document, and you can get stuck in a loop here if you don't provide one (pressing ESC just makes it try again, and clicking on the STOP icon doesn't do anything). You could put in the black data disk it comes with, but this one contains our generous donor's files, so we'll just give a blank disk image to VICE instead which Jane will offer to format. When creating a new data disk in VICE, if a 1571 is detected then Jane will want a real
.d71
with the full available space, not a
.d64
, as it will then expect it can format both sides of the virtual disk. However, all of the Jane original disks, including the black one, are formatted single-sided for the 1541 since many early 128 owners would still be using one.
The other way you can do this is from the disk icon. As these icons are in grey, so are their windows (except, curiously, help, but I can see how a yellow question mark would have looked bad against a white background), suggesting a global applet served by the central Jane kernel and thus matching the grey system disk.
The disk icon brings up a basic file manager allowing you to make duplicate backup files (but only to the same disk), rename or delete them, or create a new disk. The copy option is the default and is pre-selected when the window opens, which is irritating, because our modern reflexive habit of selecting the file first and
then
the action will cause an immediate copy to occur before you get the chance to click anything else. I don't think this was just me: there were several spurious duplicate files on the original black data disk I suspect for the same reason. If files are present on the disk, they will appear with their names and a filetype letter (W, C or L for Janewrite, Janecalc or Janelist respectively). Notice the slightly misshapen scrolling arrows, which were nice and clean on the Apple.
We'll provide the
.d71
to Jane here.
Windows warning you about data loss have a red border. Interestingly, it provides both a No button and the exit button, which both do the same thing: abort back to the file manager. Jane seems unable to distinguish between an unformatted disk and a completely absent one, and will (fruitlessly) attempt to format an empty drive.
Formatting in progress. The time estimates are surprisingly not far off.
With our disk formatted, let's return to Janewrite at the end, since this will be the majority of the documents we'll convert. Instead, we'll start with the spreadsheet, Janecalc.
Whenever any of the three built-in applications starts up, and once Jane has located the data disk, a file selector (in grey) appears. There are no spreadsheets ("worksheets") on our freshly formatted disk, so we click the NEW icon.
Entering the new filename (blue window). You may have noticed that the red and blue windows are all invariably the same size regardless of contents and any active controls they contain. This probably simplified rendering quite a bit.
Because Janecalc is green, its content window border is likewise green, and because Jane 128 doesn't multitask between the applications, it takes up the entirety of the screen.
Two templates are provided, along with a roll-your-own option. We'll go with the Home Budget for illustration.
The Home Budget template pulls up a simplified home budget by month which you can fill in. Jane supports 40, 64 and 80 column modes, all rendered in software on the VIC-IIe 320x200 display (not with the VDC's 640x200 display), but by default it uses 40. (I'll get to this in more detail in the word processor.)
Along the bottom are various operators and the extent of the formula functions available (hardly competition for the
Convergent WorkSlate
). They can be selected with the pointer in lieu of text entry, which makes them quite discoverable, but in practice it's simply faster to type them. No other functions are implemented. Since the content window cannot be resized, the maximize gadget from the Apple II version became obviously useless and was removed.
By using the joystick/mouse you can use the hand to point to a cell and then, with the hand pointing to it, just start typing text or a number. The cursor keys will move the pointer from cell to cell for you, though they will not exit the content area.
If you click or otherwise select the cell with the hand, however, Jane considers this an attempt to construct a formula, which again would be frustrating to modern audiences used to, say, Microsoft Excel. But to edit it again, you pick the insert tool instead of the hand, and this time you
must
select the cell to type in it.
Motion around the content area in all three applications is accomplished using multiple small icons in the bottom and right window borders. The "half full" icon pushes it all the way to the outer edge in that direction, while the double and single arrows move the viewport by large leaps and small leaps respectively. There are no thumbs to show relative location, but you can click anywhere along the scroll area for a proportionately "medium" jump if you like. You can also use CTRL-CRSR/CTRL-arrow keys.
Even in 40-column mode, and even given that the scroll doesn't animate and just snaps to the new position, scrolling is agonizingly slow and multiple clicks on the scroll controls invariably overshoot. Putting it in 80 column mode doesn't just give you more on the screen — it also means you don't need to endure as many pauses trying to move around. Again, I'll have more to say about font sizes when we get to Janewrite.
Unique to Janecalc, the scrolling actually wraps. Worksheets remain limited to 26 columns (A-Z), as in the Apple II version, but now up to 50 rows are allowed. Still, this wouldn't have been sufficient for anything larger than a modest small business, even in 1985.
Formulas are approximately VisiCalc-style using A1 absolute notation for cells, though there are no sigils for functions (not that there's very many) and ranges are delimited by colons. Most basic math operators and parentheses are available. Here, we'll get a sum of this row ...
... and then manually calculate an average by dividing the sum by the count of populated rows (we could also just use
avg
). The template includes this at the bottom, but this shows you how formula entry worked.
As we add data to dependent cells the sheets recalculate but circular references are not handled, though in fairness this capability was still not common in small spreadsheet applications.
We'll go to Janelist next. When we do so, a red window pops up to prompt us to save our work.
Switching to Janelist.
Creating our new list. All very consistent (the file manager and requester seem to be part of the Jane kernel).
Janelist, in fairness, never purported to be a database in any incarnation and acts more like a cardfile; even the manual merely refers to it as a "list keeper." Like Janecalc it comes with templates, though Janelist supports a substantial number more.
For variety I'll try to enter some of my very large CD collection, because I'm one of
those
people (vinyl is for art, CD is for listening).
The list comes up as fillable fields. There may be up to 15 field names up to 12 characters long. If you choose to create your own, then Jane will step you through entering the field names. That's about all the customization you can do.
The values for those fields can span multiple lines, which is what the viewport scrolling is for — you use the icons at the bottom to advance through individual cards. Incidentally,
Atom Heart Mother
is Pink Floyd's finest album and I will tolerate no disagreement.
The icon that looks like cards being pulled out suggests how to make a query (the magnifying glass icon, or possibly the funnel icon to denote a filter, wasn't universal at this point). Because it gives you choices, it's yellow, remember?
The two OK buttons do different things. The top one filters cards to the query requested, but the bottom one
undoes
any query. You can query on top of queries for a primitive sort of logical-AND. Partial word searches are supported.
For example, here is the second best Beatles album — the best is, of course,
Abbey Road
.
Since we searched for the Beatles, when we run out of Beatles CDs, nothing more turns up from my formidable library.
It is also possible to sort cards, in which case they appear in that order instead. You cannot sort on multiple fields, and you can't sort descending.
Finally, Janewrite, where we will spend the rest of our time — and where apparently most of Jane's users spent theirs, including our previous owners.
I've got a prefab file here I constructed while playing around to explore the file format, so this time we'll load a document instead of entering one, just to show you what that looks like from the file requester.
Janewrite is IMHO the most polished and competent of the three apps, and it feels like the most development time was spent on it, too. It also shows what the Jane font renderer is capable of: although non-proportional and only a single typeface, you can see bold, underline, bold
and
underlined, superscript, and subscript are all possible.
The bottom shows left, right, centre and full justification options, done per line, plus the font options, and then search (this time with a magnifying glass) and page layout. These icons are larger and more detailed than the Apple's. As with other parts of the UI, text attributes are set verb-initial, i.e., you would choose the desired style, then the insertion tool,
then
highlight the range of text and finally release the button (or, annoyingly, wait, which makes fine adjustments harder than they should be). Notice that there is an explicit bold-and-underline option, instead of using the separate bold and underline options in combination: that's because you can't make superscripted or subscripted text bold or underlined.
The top of the content area shows the ruler — in characters, not inches — and margin stops and the single paragraph indent stop, which you can drag to change them. Interestingly, the ruler seems to be new for Jane 128: no screenshot for the Apple II version demonstrates one.
Janewrite is also capable of a modicum of WYSIWYG if you select the 80 column option. This and other options come from the "computer" icon, which acts as a preference panel. Preferences are saved to the application disk and are global to all three applications. Despite this presenting a choice window (ordinarily yellow), Jane seems to treat it as a global window from the kernel, so it's grey.
The bottom set of options are specifically for configuring the printer. Print output is generated with control codes and text only; Jane does not generate graphic sequences, so what actually shows up on the page depends on what your printer actually supports. The default middle print size option corresponds to 80 columns (more accurately, the default or 12cpi font size), while the small font corresponds to the condensed 15cpi and/or 132 column option available on some printers, and the large font corresponds to the 60 or 64-column (e.g., 10cpi) option also only available on some printers — not the expanded double wide printing option more typical of Commodore-specific devices.
You could also select between regular fanfold tractor feed or plain paper, as well as the Near Letter Quality print option some printers supported, and finally the printer itself.  There was built-in support for the MPS-801 (i.e., 1525), MPS-802 (i.e., 1526), 1101, "Oki" (generic Okidata), and generic "Epson" printers, assuming they were connected somehow to the IEC serial such as through a third-party parallel printer interface. These printer drivers varied wildly in their capabilities: the 1525/MPS-801 "driver" supported almost nothing except basic text, while the generic Okidata and Epson drivers supported nearly everything that Jane could generate.
The "OTHER" driver is customizeable, a neat idea, if a little clumsy. A BASIC program called
BUILDPRT
on the grey disk allows you to populate it with your printer's control codes. Control sequences up to three characters long were supported. You would enter these from the manual, it would save them to disk, and then you could use the custom driver inside Jane.
The topmost options affect the appearance of Jane. You can choose from three font sizes, all non-proportional, corresponding to 40, 64 or 80 column text. Confusingly, the 80-column option is the last when it's the middle option for printing. (The Apple II version likely didn't support 80 column text due to its smaller hi-res horizontal width.) Pointer speed and the "beep" Jane makes when you select options are also configurable.
Here's how it looks in 80 columns, using the typical "soft 80" approach on the 64 which is more or less legible, at least on a composite display. As there are no colours in the content area, there is no risk of colour clash. This is probably the most useful view in Janewrite.
The 64-column view, by contrast, is probably the least useful. The 40-column view is the most legible and 2:1 the size of a typical 80-column line, so it's easy to mentally grok page layout that way, but the 64-column view is odd enough to end up being the worst of both worlds.
An interesting feature of Janewrite are the accented characters, which was not frequently seen on home computer-class word processors, as explained by the on-line help.
Janewrite treats them as diacritics, and they can even be applied to letters that wouldn't ordinarily use them (because who knows? some language might), such as the grave and acute accents on the n as well as the more typical tilde. In fact, you can apply them to
any
character, even punctuation. However, the use of the up arrow to indicate a circumflex means there's no way you can type a literal caret into your document, and while a macron would have been nice, omitting the umlaut seems a greater fault. The decorators are also rather hard to distinguish in 80 columns, so Spanish users of Juana 128 might want to go to cuarenta column mode to mirar mejor.
Janewrite also has basic find and/or find-and-replace, and a small pane appears below the content area when it's active.
There are also decent page layout options, including setting both a per-page title and its position, adding a page number and its position, and margins, number of copies and starting page, though the last two would seem more appropriate for a print dialogue than a page layout one. Note that Jane will always print a 10-space left margin, so an 80-column printed line can be no longer than 70 characters, and this is indeed the maximum width Janewrite will support.
However, paragraphs are apparently not stored as continuous sequences of text, demonstrated here with a contrived example. (In fact, we'll
prove
they aren't shortly.) While Janewrite will word-wrap at the right margin, inserting text after that will wrap onto a
new
line, not into the next line, even if the two lines were previously entered "together." There's a speed/flexibility tradeoff here in that Janewrite doesn't have to continuously reflow paragraphs, but it also means its concept of a paragraph is entirely based on how much you select. The text can be manually reflowed, joining lines if necessary, by picking one of the paragraph justification options and selecting the text with the hand, which will then be reflowed (and, if needed, spaces inserted) to match. In fact, this is also necessary if you change the margins because Jane doesn't automatically reformat your document then either.
I also promised you an example of cut and paste, so here's one using the scissors (cut). You simply pick it and, with the button down, drag it across the text you want and release the button. Note that there is no undo, though I suppose you could just immediately paste it back in.
Exiting Janewrite (though not saving, because we need the accented characters to stay in the file).
Now that we understand what Jane can do and how it works, let's move on to converting the files. We can extract our test files we made from our
.d71
with VICE's
c1541
utility and hexdump it. This got a little more difficult than it should have been:
% c1541 work.d71
c1541 (VICE 3.8)
Copyright 1995-2023 The VICE Development Team.
C1541 is free software, covered by the GNU General Public License, and you are
welcome to change it and/or distribute copies of it under certain conditions.
c1541 #8> dir
0 "data#000        " 01 2a
39   "c.TESTCALC"       prg 
3    "l.TESTLIST"       prg 
4    "w.nOTE.2"         prg 
4    "w.TESTCONV"       prg 
1278 blocks free.
c1541 #8> read "w.TESTCONV"
ERR = 62, FILE NOT FOUND, 00, 00
cannot read `w.TESTCONV' on unit 8
invalid filename
As you may have guessed, that's because the filenames, and it turns out the data in the files themselves, are stored as true ASCII, not PETSCII (indeed as they would have been on the Apple II, also), so
c1541
's filename conversion fails. Fortunately, the
extract
command will walk the entire directory and pull out all the files no matter what they're named.
The documents are all regular Commodore PRoGram files with a starting address and they appear to be loaded in-place at that address into bank 1. This introduces the possibility of some delightful save-file hacks but we're not here for that today.
That means we can also simply extract our previous owners' files en masse as well. I imaged their disk using my ZoomFloppy and external 1571, and since they are normal PRGs, a BAM copy of the allocated sectors is all we need to do, with one wrinkle:
% d64copy -B 9 r_jane_bam.d64
[Warning] growing image file to 683 blocks
14: --*****--*****--*****     8%    15/171[Warning] read error: 0e/00: 5
14: ?********************    12%    21/171[Warning] giving up...
14: ?********************                  
15: *********************                  
16: *********************                  
17: *********************                  
18: *******************                    
19: *******************                    
20: *******************                    
21: *******************                    
22: ****..***...***...*     100%   171/171
170 blocks copied.
% c1541 r_jane_bam.d64
c1541 (VICE 3.8)
Copyright 1995-2023 The VICE Development Team.
C1541 is free software, covered by the GNU General Public License, and you are
welcome to change it and/or distribute copies of it under certain conditions.
c1541 #8> extract
c1541 #8> quit
Fortunately it doesn't look like the bad sector was in any of the files they cared about.
Let's get an idea of the format from our test files. Janecalc files are "huge" because it looks like the entire 26x50 cell range is saved regardless of whether anything's in it or not. Looking at the directory of their data disk where they had saved a couple of sparse test spreadsheets of their own, they also were 39 blocks in length no matter how many cells were actually populated. The on-disk format is consequentially a bit wasteful:
000003a0  00 00 00 00 00 20 20 20  4a 61 6e 75 61 72 79 20  |.....   January |
000003b0  20 46 65 62 72 75 61 72  79 20 20 20 20 20 4d 61  | February     Ma|
000003c0  72 63 68 20 20 20 20 20  41 70 72 69 6c 20 20 20  |rch     April   |
000003d0  20 20 20 20 4d 61 79 20  20 20 20 20 20 4a 75 6e  |    May      Jun|
000003e0  65 20 20 20 20 20 20 4a  75 6c 79 20 20 20 20 41  |e      July    A|
000003f0  75 67 75 73 74 20 53 65  70 74 65 6d 62 65 72 20  |ugust September |
00000400  20 20 4f 63 74 6f 62 65  72 20 20 4e 6f 76 65 6d  |  October  Novem|
00000410  62 65 72 20 20 44 65 63  65 6d 62 65 72 00 00 01  |ber  December...|
00000420  04 00 00 00 00 00 00 20  20 54 6f 74 61 6c 20 20  |.......  Total  |
00000430  20 41 76 65 72 61 67 65  20 20 20 00 00 01 04 00  | Average   .....|
Cardfiles are stored much more efficiently. Here's the entirety of our two cards. The fields are in the header, padded out to the fixed 12 character length, but with technically unnecessary nulls between them. A spurious "Beatles" entry looks like a buffer that was captured as part of the save, and there is also a page-aligned (counting the starting address) pad of nulls. Otherwise, the value strings look null-delimited, in the order they appear in the field list (unpopulated fields are zero-length strings). When you run out of fields, you're on the next card.
% hexdump -C l.TESTLIST
00000000  00 7f 01 00 36 02 08 00  04 00 54 69 74 6c 65 20  |....6.....Title |
00000010  20 20 20 20 20 20 00 4c  65 61 64 20 41 72 74 69  |      .Lead Arti|
00000020  73 74 20 00 4f 74 68 65  72 20 41 72 74 69 73 74  |st .Other Artist|
00000030  00 43 6f 6d 70 6f 73 65  72 20 20 20 20 00 43 6f  |.Composer    .Co|
00000040  6e 64 75 63 74 6f 72 20  20 20 00 57 68 65 72 65  |nductor   .Where|
00000050  20 4b 65 70 74 20 20 00  42 6f 72 72 6f 77 65 64  | Kept  .Borrowed|
00000060  20 62 79 20 00 44 61 74  65 20 4c 65 6e 74 20 20  | by .Date Lent  |
00000070  20 00 00 00 ff ff 01 ff  ff ff ff ff ff ff ff ff  | ...............|
00000080  ff ff ff ff ff 00 01 02  03 04 05 06 07 00 01 02  |................|
00000090  03 04 05 06 07 ff ff ff  ff ff ff ff ff ff ff 00  |................|
000000a0  00 54 68 65 20 42 65 61  74 6c 65 73 00 00 00 00  |.The Beatles....|
000000b0  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
*
00000100  d7 09 80 60 60 ac 98 09  ae 04 cf a5 ea a9 d7 15  |...``...........|
00000110  80 ac 1d 21 d6 1c 80 60  60 ac 98 09 ae 04 cf 20  |...!...``...... |
00000120  75 0b 00 00 ac 0a 95 a5  f0 b0 a9 a6 b1 a9 a4 b1  |u...............|
00000130  a5 f1 b0 a9 a7 b1 a9 a5  b1 ac c0 08 cf 20 75 0b  |............. u.|
00000140  fe ff a5 37 ae 8c ff 00  c0 d8 4b 80 cf a5 f0 b0  |...7......K.....|
00000150  a7 a6 b1 c0 d8 60 80 a5  f1 b0 a7 a7 b1 c0 d8 60  |.....`.........`|
00000160  80 cf a5 f0 b0 a7 a6 b1  00 00 09 00 01 5d f6 00  |.............]..|
00000170  00 00 00 09 00 09 00 01  66 f6 00 00 00 00 54 00  |........f.....T.|
00000180  50 00 01 b1 f6 69 64 65  20 12 00 42 00 01 6f f6  |P....ide ..B..o.|
00000190  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
000001a0  00 00 00 00 00 00 00 52  65 76 6f 6c 76 65 72 00  |.......Revolver.|
000001b0  54 68 65 20 42 65 61 74  6c 65 73 00 00 4c 65 6e  |The Beatles..Len|
000001c0  6e 6f 6e 2d 4d 63 43 61  72 74 6e 65 79 2d 48 61  |non-McCartney-Ha|
000001d0  72 72 69 73 6f 6e 00 47  65 6f 72 67 65 20 4d 61  |rrison.George Ma|
000001e0  72 74 69 6e 00 00 00 00  00 41 74 6f 6d 20 48 65  |rtin.....Atom He|
000001f0  61 72 74 20 4d 6f 74 68  65 72 00 50 69 6e 6b 20  |art Mother.Pink |
00000200  46 6c 6f 79 64 00 00 57  61 74 65 72 73 2d 47 69  |Floyd..Waters-Gi|
00000210  6c 6d 6f 75 72 2d 4d 61  73 6f 6e 2d 57 72 69 67  |lmour-Mason-Wrig|
00000220  68 74 2d 47 65 65 73 6f  6e 00 50 69 6e 6b 20 46  |ht-Geeson.Pink F|
00000230  6c 6f 79 64 00 00 00 00                           |loyd....|
00000238
This would be very easy to convert, and I just manually did this by dumping everything with
strings
for their one cardlist with one single record. Other things I can pick out are the file length minus the starting address at byte offset 4 (as a little-endian unsigned 16-bit quantity), and the value at byte offset 6 might be the number of fields, though we don't need either of those to simply grab the data.
Now for the Janewrite files, starting with our test document which should contain every sort of text ornamentation that Janewrite can represent. The first section looks like this.
% hexdump -C w.TESTCONV
00000000  00 88 01 00 21 00 00 00  46 00 05 00 47 00 34 03  |....!...F...G.4.|
00000010  00 20 00 20 00 20 00 20  00 20 00 20 00 20 00 20  |. . . . . . . . |
*
00000030  00 20 00 20 00 20 00 20  05 00 04 02 0a 50 01 05  |. . . . .....P..|
00000040  3d 42 01 01 6e 81 61 6e  61 20 61 62 72 83 65 83  |=B..n.ana abr.e.|
00000050  20 61 6c 82 6f 82 20 61  6c 84 65 00 01 6e 00 61  | al.o. al.e..n.a|
00000060  00 6e 00 61 00 20 00 61  00 62 00 72 03 65 00 20  |.n.a. .a.b.r.e. |
00000070  00 61 00 6c 02 6f 00 20  00 61 00 6c 04 65 00 20  |.a.l.o. .a.l.e. |
00000080  00 20 00 20 00 20 00 20  00 20 00 20 00 20 00 20  |. . . . . . . . |
*
Skipping the start address (this is indeed its location in bank 1), we again see some pieces of what looks like a buffer, as well as the file length (again minus the starting address) at byte offset 14. The left margin is (probably) at byte offset 6 because the right margin is at byte offset 8 (also a 16-bit LE short), followed by the paragraph indent. After this header, we now get the text, shown here in its entirety.
000000a0  00 20 00 49 74 20 77 61  73 20 61 20 64 61 72 6b  |. .It was a dark|
000000b0  20 61 6e 64 20 73 74 6f  72 6d 79 20 6e 69 67 68  | and stormy nigh|
000000c0  74 2e 00 90 49 74 90 20  90 77 61 73 90 20 90 61  |t...It. .was. .a|
000000d0  90 20 90 64 61 72 6b 90  20 90 61 6e 64 90 20 90  |. .dark. .and. .|
000000e0  75 6e 64 65 72 6c 69 6e  65 64 90 20 90 73 74 6f  |underlined. .sto|
000000f0  72 6d 79 90 20 90 6e 69  67 68 74 2e 00 88 49 74  |rmy. .night...It|
00000100  88 20 88 77 61 73 88 20  88 61 88 20 88 64 61 72  |. .was. .a. .dar|
00000110  6b 88 20 88 61 6e 64 88  20 88 62 6f 6c 64 88 20  |k. .and. .bold. |
00000120  88 73 74 6f 72 6d 79 88  20 88 6e 69 67 68 74 2e  |.stormy. .night.|
00000130  00 98 49 74 98 20 98 77  61 73 98 20 98 61 98 20  |..It. .was. .a. |
00000140  98 64 61 72 6b 98 20 98  61 6e 64 98 20 98 62 6f  |.dark. .and. .bo|
00000150  6c 64 98 20 98 61 6e 64  98 20 98 75 6e 64 65 72  |ld. .and. .under|
00000160  6c 69 6e 65 64 98 20 98  73 74 6f 72 6d 79 98 20  |lined. .stormy. |
00000170  98 6e 69 67 68 74 2e 00  00 a0 49 74 a0 20 a0 77  |.night....It. .w|
00000180  61 73 a0 20 a0 61 6c 73  6f a0 20 a0 73 75 70 65  |as. .also. .supe|
00000190  72 73 63 72 69 70 74 65  64 a0 20 20 c0 61 6e 64  |rscripted.  .and|
000001a0  c0 20 c0 73 75 62 73 63  72 69 70 74 65 64 2e c0  |. .subscripted..|
000001b0  20 20 2e 2e 2e 20 62 75  74 20 6e 6f 74 20 62 6f  |  ... but not bo|
000001c0  74 68 2c 00 61 6e 64 20  6e 6f 74 20 63 6f 6d 62  |th,.and not comb|
000001d0  69 6e 65 64 20 77 69 74  68 20 75 6e 64 65 72 6c  |ined with underl|
000001e0  69 6e 69 6e 67 20 6f 72  20 62 6f 6c 64 2e 00 00  |ining or bold...|
000001f0  48 65 20 6c 65 66 74 20  6a 75 73 74 69 66 69 65  |He left justifie|
00000200  64 20 68 69 6d 73 65 6c  66 2e 00 ff 58 48 65 20  |d himself...XHe |
00000210  72 69 67 68 74 20 6a 75  73 74 69 66 69 65 64 20  |right justified |
00000220  68 69 6d 73 65 6c 66 2e  00 ff 24 48 65 20 70 75  |himself...$He pu|
00000230  74 20 68 69 6d 73 65 6c  66 20 72 69 67 68 74 20  |t himself right |
00000240  69 6e 20 74 68 65 20 63  65 6e 74 72 65 2e 00 ff  |in the centre...|
00000250  0a 48 65 20 6d 61 64 65  20 65 76 65 72 79 74 68  |.He made everyth|
00000260  69 6e 67 20 65 78 70 61  6e 64 20 6f 75 74 2c 20  |ing expand out, |
00000270  61 20 70 61 72 61 67 72  61 70 68 20 65 78 74 65  |a paragraph exte|
00000280  6e 64 69 6e 67 20 6f 76  65 72 20 6d 75 6c 74 69  |nding over multi|
00000290  70 6c 65 00 ff 0a 6c 69  6e 65 73 2c 20 61 20 66  |ple...lines, a f|
000002a0  72 61 67 6d 65 6e 74 20  74 68 61 74 20 62 65 63  |ragment that bec|
000002b0  61 6d 65 20 61 6e 20 69  63 6f 6e 20 75 6e 74 6f  |ame an icon unto|
000002c0  20 69 74 73 65 6c 66 2e  00 00 61 82 61 86 61 87  | itself...a.a.a.|
000002d0  61 82 61 81 20 61 6e 64  20 6e 65 78 74 20 41 82  |a.a. and next A.|
000002e0  41 86 41 87 41 82 41 81  20 6e 65 78 74 20 6e 82  |A.A.A.A. next n.|
000002f0  6e 86 6e 87 6e 82 6e 81  20 6e 65 78 74 20 4e 82  |n.n.n.n. next N.|
00000300  4e 86 4e 87 4e 82 4e 81  20 6d 61 81 6e 81 61 6e  |N.N.N.N. ma.n.an|
00000310  61 20 61 62 72 83 65 83  20 61 6c 82 6f 82 20 61  |a abr.e. al.o. a|
00000320  6c 84 65 00 00 00 00 00  00 00 00 00 00 00 00 00  |l.e.............|
00000330  00 00 00 00 00 00                                 |......|
Most of the document again can be trivially understood as null-delimited strings. Notice that no single line ever exceeds 80 columns in length: as we demonstrated above, there are no
Dana
paragraphs, only
Zuul
lines.
There are also various meta-sequences for the formatting. We can pick out the easy ones right away: $90 turns on and off underlining (interesting that Jane automatically skips spaces, much as would be the convention on a typewriter), $88 bold, $98 bold and underlined, $a0 superscript and $c0 subscript.
For justification, we can infer that a line starting with $ff indicates different formatting for that line. A superficial guess would suppose the next character sets the justification type, e.g. $58 right, $24 centre, and $0a full justification (left justification is the default and implied). However, looking at some of the family's files, there were other values here, many of which were close to those numbers but many that were also rather disparate, and none that exceeded $8c (140). Eventually it became clear that all it indicates is the number of leading spaces multiplied by two, or more generally stated, all levels of justification are simply baked into the document and pre-calculated with spaces. This is entirely consistent with the lack of automatic reflow we saw while in Janewrite.
Accents are also a little odd. If we take the last four words with single accents, then the ornamented letter would seem surrounded by the metacharacter: $81 $63 $81 for ñ (CTRL-@), $82 $6f $82 for ô (^), $83 $65 $83 for é (CTRL-;) and $84 $65 ($84) for è (CTRL-*), though since it occurs at the end of the line it would be cancelled anyway. An experiment I did showed that this is true for multiple characters as well, as long as they're all the same diacritic. So far so good, but the strange part is alternating between multiple accented characters back to back with different accents. Our letter sequences are unaccented, circumflex, grave, acute and tilde, yet the metacharacters seem to change between the $82s, after which we drop down to $81
following
the final character which sounds like the delimiter itself changed too. This is the same pattern for each of the other multibyte clusters in this example. I did a test document with "ãâáàa" (i.e., ascending metacharacters $81 $82 $83 $84) and got
$81
$61
$83
$61
$81
$61
$87
$61
$84
$61, while "àáâãa" (descending $84 $83 $82 $81) is rendered
$84
$61
$87
$61
$81
$61
$83
$61
$81
$61, "áàãâa" (i.e., $83 $84 $81 $82) is rendered
$83
$61
$87
$61
$85
$61
$83
$61
$82
$61, and "àâáãa" (i.e., $84 $82 $83 $81) comes out
$84
$61
$86
$61
$81
$61
$82
$61
$81
$61.
A couple of Pibb Xtras later, I finally realized what it was doing: it's exclusive-ORing the low nybble of adjacent metacharacters together so that it recognizes them as continuations (or, if the sequence is over, zero). Because of the specific values used, they won't generate any other valid metacharacter. To encode $81 $82 $83 $84, 1 is XORed with 2 and the high bit restored to yield $83, 2 is XORed with 3 to yield $81, 3 is XORed with 4 to yield $87 and then $84 is the expected terminal delimiter. To decode the resulting $81 $83 $81 $87 $84, $81 is used as the initial delimiter, then 1 is XORed with 3 to yield $82, then this is used as the next low nybble XORed with 1 to yield $83, then 3 is XORed with 7 to yield $84, and then 4 XOR 4 is 0, ending the sequence.
This is a little complex to model and I didn't need it to convert the family files, so I went with this small Perl script which converted them to RTF, preserving boldface, underline, superscripting and subscripting, and the leading indent. It was also an excuse to learn how to write RTF documents from scratch, though please don't consider its output to be particularly
good
RTF.
#!/usr/bin/perl

eval 'use bytes'; $crlf = "\015\012";

# magic read from either ARGV or STDIN, set ARGV filehandle
# splitting it up into bytes was to analyze the header
$/ = \163; @header = map { ord } split(//, <>); # get header
die("abnormally short\n") if (scalar(@header) != 163);
$/ = "\00"; # lines are null-separated

print STDOUT
"{\\rtf1\\ansi{\\fonttbl\\f0\\fmodern\\fprq1 Courier;}\\f0\\fs20\\pard${crlf}";
while(<ARGV>) { chop; # not chomp
	$bold = 0; $under = 0; $bunder = 0; $sup = 0; $sub = 0;

	# load indent
	if (s/^\xff([\x00-\xff])//) { $_ = " " x (ord($1)/2) . $_; }
	# force NBSP because Word thinks it's smarter than we are
	s/ /\\u160;/g;

	unless (/[\x80-\xff]/) { print STDOUT "$_\\par$crlf"; next; }
	foreach (map { ord } split(//, $_)) {
		unless ($_ & 128) { print STDOUT chr($_); next; }
		if ($_ == 136) { $bold ^= 1; print STDOUT "\\b$bold "; next; }
		if ($_ == 144) { $under ^= 1;
			print STDOUT "\\ul$under "; next; }
		if ($_ == 152) { $bunder ^= 1;
			print STDOUT "\\ul$bunder\\b$bunder "; next; }
		# XXX: sup/sub looks fine in Mac Text Edit, wrong in Word
		# because it shrinks the font as well
		if ($_ == 160) { $sup ^= 1;
			print STDOUT (($sup) ? '{\super ' : '}'); };
		if ($_ == 192) { $sub ^= 1;
			print STDOUT (($sub) ? '{\sub ' : '}'); };
		# XXX: accented characters not yet implemented
	}
	print STDOUT '\b0' if ($bold || $bunder);
	print STDOUT '\ul0' if ($under || $bunder);
	print STDOUT '}' if ($sub || $sup); # shouldn't be nested
	print STDOUT "\\par$crlf";
}
print STDOUT "}$crlf";
I relentlessly tested the output against TextEdit, NeoOffice, LibreOffice and Microsoft Word on the Mac, and Word on my office PC, and concluded there was no good way to make them
all
happy. Since Janewrite is strictly non-proportional and character-oriented, the resulting document has to be monospace and spaces must be fixed-width to preserve the original formatting. TextEdit was the most flexible about this, accepted nearly anything, and rendered it as expected. Word, however, thought it was smarter than my carefully crafted output and changed the width of spaces even with an explicitly monospace font such that things failed to line up. The solution was to make it use a non-blocking space, which TextEdit also serenely accepts (though it wanted an explicit delimiter, not just a space character), but which shows up as a block character in NeoOffice and LibreOffice. I gave up at that point and declared it good enough. Change the above if you disagree. Maybe I should have done this in HTML because everything renders HTML the same, right? (Right??)
A residual problem is that superscript and subscript in Word, NeoOffice and LibreOffice also reduce the font size, which is not consistent with Jane and also messes up alignment, and there didn't seem to be a way to manually specify the vertical baseline in RTF but keep the same font size to get around that. Once again, only TextEdit's output properly resembles Janewrite's. This is another exercise left for the reader since I didn't need that to convert their documents either.
With our task complete, let's finish the story of Jane. The Atari 8-bit and IBM PC ports likewise never materialized, but Jane was ultimately ported to one more — and, outside its home country of France, rather obscure — system: the 1985 Thomson MO5, manufactured by French electronics company Thomson SA (now Vantiva SA), which had recently been nationalized out of Thomson-Brandt and Thomson-CSF by French president François Mitterand in 1982.
The Thomson home computers were all based on a 1MHz Motorola 6809E CPU with various custom video chips and produced from 1982 to around 1989. They broadly divide into the more upmarket TO-class and the entry-level MO-class machines, ostensibly compatible within lines, though I'll demonstrate that this is not always the case. The MO5 was the second of these systems, an enhanced version of the original TO7 with 48K of RAM and an improved colour palette, developed as terminals ("nanomachines") for the French government's
Plan Informatique pour Tous
("Computing for All") to introduce computers to French pupils and support domestic industry. It was sold against, and intended to compete directly with, the ZX Spectrum — particularly as initially sold with a Chiclet-style keyboard — and the Commodore 64. These screenshots were taken with
the DCMOTO emulator
.
Not counting the unreleased Commodore 64 version, Jane for the MO5 is the only version of Jane that actually
does
come as
a cartridge-floppy combination
, and thus requires the optional CD 90-351 or CQ 90-028 floppy disk interface (only tape is supported by the base unit). Although the cartridge is a whopping 64K in size, MO5 Jane is still a three-disk system (i.e., apps, help and data). The cartridge appears to contain the MO5 Jane kernel and low-level drivers. Similar to Commodore and Jane 128, MO5 Jane was explicitly Thomson-badged and sold. When turned on with the cartridge installed, it immediately prompts (with a blue window) for the application floppy.
The main screen. Like the TO7 before it, the MO5 comes with a light pen which Jane uses as its primary pointing device, and this is the only Jane port that officially uses one. It's not clear who (Thomson or Arktronics or a third party) did this port and I don't have a copy of the manual. However, I also strongly believe Howard Marks was personally involved with its development given his country of origin.
Jane 128 and MO5 Jane are obviously related to each other, quite clearly more than either is related to the original Apple II version, and as such I'm not exactly sure which one came first — though my suspicion is still Jane 128, since it almost certainly built on already existing work for the 64, and would have been a higher corporate priority due to Commodore's larger install base. Indeed, MO5 Jane uses much the same colour scheme, icons and basic interface as Jane 128, though the STOP (not ARRÊT?) icon is oddly rendered in orange instead of red and there's no black anywhere despite the EFGJ03L video chip having both colours in its palette.
With a single drive there ends up being a lot of disk swapping. A
lot
of disk swapping.
The NEW icon and EXIT button are now NEUF and SORTIR, but the rest of the basic interface (modulo palette) is much the same, even the same lumpy file requester arrows.
The online help remains available in bright flaring yellow and as good as it ever was, but the constant floppy cha-cha will dampen your interest to use it. The MO5 does not have hardware sprites, so the pointer is drawn by software and demonstrates that familiar Speccy-style colour clash.
Probably because of the limited RAM, all three applications are simplified compared to the Apple and Commodore versions, in some cases drastically. Like Jane 128, there is no multitasking and windows are fixed, but there are other cuts. For example, here in Janewrite, there are no superscripts or subscripts, though accents are kept — it's French, after all — and it even supports umlauts and cedillas. This is done with the MO5's ACCENT key, which you press, release, and then press the desired key (such as ACCENT, E for ë, ACCENT, 6 for é and ACCENT, 9 for ç).
Janelist now only supports two templates (plus create your own). Fortunately I can still keep my record collection in it.
On the other hand, Janecalc is now just a basic spreadsheet — no templates at all — and the spreadsheet is even more limited to A-O (i.e., just 15 columns) and 25 rows.
But probably the biggest limitation in MO5 Jane is that everything is 40 columns, even though the graphics hardware and 320x200 display are absolutely capable of the same "soft 80" display Jane 128 generates. For crying out loud, even the Apple II version had a 64-column option. It really makes you wonder what on earth that 64K of ROM in the cartridge is actually doing.
I should mention as a postscript that MO5 Jane is quite finicky about the hardware configuration. Even with the lightly-modified MO5E export model some prompts get garbled, and on the network-enabled MO5 NR (or, presumably, an MO5 with the network upgrade installed) the cartridge is recognized but the machine immediately crashes when selected. It also won't run on the later MO6 and it was never ported to any other Thomson system. Run it only on the original.
Although it's arguable which of the two is more powerful — the Apple II version is more flexible and more integrated, but the Commodore 128 version has a stronger interface, larger workspace and 80-column output — Jane 128 got similar reviews to Jane on the Apple II and some of the same criticism as well.
RUN
in March 1987 again approved of the interface, but complained about the sluggish performance — both on-screen and on-paper — and that the 80-column software output was hard to read compared to the VDC's native 80-column output, which the reviewer called "[t]he program's greatest flaw." The review also noted that printing a spreadsheet had to be stopped manually or it would merrily waste paper on empty cells until the entire sheet had been iterated over. Still, reviewer John Premack said it was "a must for beginners of all ages" and gave it a "B" grade overall.
I don't think Commodore was expecting much from Jane, and it ably occupied the low-end niche that Goheen and Smith wanted it to, so perhaps that was enough. It certainly seems to have been for my Australian 128DCR's previous owners, because the entire family used it (even some brief school papers from their kid) and some documents are dated well into 1990, long after Jane — and for that matter the 128 itself — was off the market. That probably speaks well of its interface and its suitability to basic tasks.
Jane was never available on any other systems and Commodore never released any updates, but Arktronics did work on at least one other port for Commodore:
the original Textcraft
for the Amiga 1000 in 1985. This seems to have been the last product Arktronics was involved in, after which it went under in May as the new 16-bit systems made its flagship software package obsolete. That same year five employees, including at least two of the original Apple II programmers, sued Arktronics and Marks and Kotick personally (
Mantei v. Arktronics
) over their now worthless shares, saying they had been misled. In 1989, after protracted litigation, Kotick was ordered to honour the settlement of $17,000 [$44,500 in 2025 dollars] and again in 1998, by then increasing to $49,226 with interest [$96,500]. (In 2022, one of the plaintiffs, John Wiersba,
said he was still never paid
, an assertion which Kotick's spokesman disputed.)
But this was all likely a mere distraction to Marks and particularly Kotick, who in 1987 turned around to make an audacious if unsuccessful attempt to buy
Commodore
, believing the Amiga could lead a comeback in computer gaming after the 1983 video game crash. Commodore managed to rebuff him and in 1991 Kotick, Marks and their partners executed a hostile takeover of another target instead for just $440,000 [about $1.15 million], an ailing software company called Mediagenic. Mediagenic had a long prior history in video games, but believed the field was unlikely to rebound, and was in the midst of an unsuccessful effort to broaden into productivity software. Kotick, who had just
left
that market segment, disagreed and reconstituted the company back into its prior business and under its former name: Activision. In the process Kotick didn't forget his previous benefactor and Steve Wynn ended up with a million and a half shares in the new company, which became so successful in its revitalized form that in 2012 Wynn commented in amazement to
the New York Times
that "[t]he kid [Kotick] was telling me I had $31 million I didn't know about."
Despite Activision's stratospheric rebirth, Kotick's leadership became nearly as controversial as it was profitable. Although Marks entered as the new Activision's chairman, by the late 1990s his relationship with his college friend had frayed over what Marks called Kotick's willingness to battle over even trivial sums of money, and he left the company in 1997. After a new business software venture called eMinds failed, in 2004
Marks bought out the trademark
of the defunct Acclaim Entertainment to form a new Acclaim Games focusing on the MMO market, which he sold in 2010 and flamed out just months later. Marks subsequently co-founded equity crowdfunding platform StartEngine, where he
remains the CEO
. Meanwhile, Kotick steered Activision through its 2008 $18.9 billion merger with Vivendi Games and its Blizzard subsidiary, becoming Activision Blizzard and for a time the largest video games publisher in the world, its 2013 split back out from Vivendi, lawsuits over toxic workplace allegations, and Microsoft's 2022 buyout for $68.7 billion under which Kotick left the company at the end of 2023. It isn't clear who retains the rights and IP to Jane today, though at least for the Apple II version they likely remain split between Marks and Kotick personally and possibly Wynn, while Cloanto and Vantiva retain joint rights to the Commodore 128 and Thomson MO5 versions.
As for Sig Hartmann, arguably the father of Commodore's software division, he passed away
in 2014
.
