---
title: "A Dick Smith VZ200 without the Dick Smith (but with a serial port)"
url: "https://oldvcr.blogspot.com/2026/09/a-dick-smith-vz200-without-dick-smith.html"
fetched_at: 2026-09-13T10:01:14.324263+00:00
source: "oldvcr.blogspot.com"
tags: [blog, raw]
---

# A Dick Smith VZ200 without the Dick Smith (but with a serial port)

Source: https://oldvcr.blogspot.com/2026/09/a-dick-smith-vz200-without-dick-smith.html

Australians!
They walk among us
! Do not be deceived by those charming faces!
They might be your parent! They might sleep in the same bed as you at night! A half-breed might write the very blog you read!
For the preservation of our
precious bodily fluids
, we must remove the scurrilous larrikin influence of Australia upon our American home computers, and I know exactly where to start! Why allow Dick Smith's name (even though he'd already sold Dick Smith Electronics' controlling interest to Woolies by then but stop ruining my intro) to corrupt this, um, rubber-keyed diminutive beige home computer when we can return it to its prior, pristine, plasticky state as it once rolled out from a
glorious Asian factory
?
Let us restore it to its purest virginal roots! Let this American, possibly sold in Canada, original of a Hong Kong-manufactured super-cheap home computer that was also sold in Europe but never mind that flourish once more!
... after, of course, we compare this seppo VTech VZ200 with the Dick Smith units and the bumper crop of crap American home computers in 1983, and fix the keyboard and video.
Then
, to avoid wrecking it with a botched logic board repair, we'll bolt on a USB serial port using the very latest peripherals from down under, write cycle-counted Z80 assembly language to blast data to it at 57.6kbps, and hack a few games. Because only
this
will make the VZ200 great again!
Let us also acknowledge that the cultural context of 1980's home computers was naturally somewhat different between the United States and Australia, and I think that's primarily why the NTSC VZ200's fate was rather unlike the DSE rebadge's. There's not a lot of early history on these particular machines, but we'll try to construct a coherent one; similarly, as there are many down-under perspectives on this machine, I'll give an alternative view from the North American side as a kid growing up during that era.
The introduction of the Intel 4004 in 1971, one of the earliest microprocessors (though see also "
TI vs. Everybody
"), was a seismic event in computing. Hong Kong entrepreneurs Allan Wong and Stephen Leung were two of many to realize that the microchip would trigger a revolution in consumer electronics, and over several years accumulated sufficient funding to establish Video Technology Ltd in 1976. Their first factory operated from the Freder Centre in Ma Tau Kok, a semi-industrial area on the west side of Kowloon Bay.
Initially VTech, as it became known, concentrated on video games, primarily as an OEM for the more profitable North American and European markets. Their first products were Pong clones, released in the United Kingdom as the Grandstand Adman T.V. Game 2000 (black and white) and Adman T.V. Game 3000 (colour) in 1977, both based on the Texas Instruments TMS1965N, TI's clone of the well-known General Instrument
AY-3-8500 Pong-on-a-chip
(compare with the rather more complex
MOS 7601
). Grandstand was a brand name of Adam Imports, then a substantial toy and games importer to the UK and for a period of time New Zealand, and had other Asian contacts, notably
Tomy
. If the picture on
VTech's history page
is to be believed, and I point out there are some verifiable inaccuracies on that page, VTech continued to produce other consoles for Grandstand/Adam like the (deep breath) Grandstand Adman Colour TV Game 3600 Mk III, which used a regular AY-3-8500 and was produced until 1979. For the portable market, VTech produced a number of handheld LED, VFD, LCD games, sold under various brands and through retailers such as Radio Shack.
VTech was hardly the only such Hong Kong tech company, of course; across the Bay in Kwun Tong was EACA, established in 1975 by Guangzhou escapee Eric Chung. EACA also produced consumer products such as radios and its own video games, notably the 1978 Colour TV Game, also based on the TMS1965N and variously sold under other brands such as the Sonesta Hide-Away TV Game.
Meanwhile, in August 1977 Tandy Corporation's Radio Shack subsidiary introduced the TRS-80 (retroactively named the TRS-80 Model I) computer. It was based around the Zilog Z80 microprocessor, no doubt due to the influence of the MITS Altair's Intel 8080, provided a 64x16 display with 128x48 semigraphics, and came with BASIC, cassette support and built-in keyboard for $399 [$2200 in 2026 dollars]; the higher-end model added an integrated monitor and tape recorder for $599 [$3300]. Tandy made many compromises to get it to that base price, such as its relatively slow 1.774MHz CPU clock (derived from an oddball 10.6445MHz crystal), complete lack of lowercase, stuttery keyboard, low base RAM (4K), weak BASIC and temperamental video circuitry, but it was cheap, it was credible and above all else, it was available. As a result, it outsold the competing Apple II by a significant margin and was in Radio Shack stores well before Commodore could clear its notorious backlog on the PET.
EACA, among others, noticed all three systems used largely off-the-shelf hardware and discrete TTL logic, and quickly planned for a clone computer to expand their product line. With respect to the TRS-80, the only custom part other than the system ROMs was a Motorola MCM6670 "character generator," effectively another ROM with character bitmap data used by the video circuit. Since it was the market leader, third-party support for the platform was growing and Tandy had little presence outside the United States, Chung decided to start there first.
In summer 1979 EACA introduced the Video Genie, ostensibly the first original design from a Hong Kong technology company (as reported in
Creative Computing
in August), but in fact ripped off from and largely compatible with the TRS-80, and advertised as such (well, the compatible part, anyway). While there were some internal differences and significant changes to the keyboard layout, EACA mostly copied the TRS-80 system ROMs for production with only minor changes, shipping it with a licensed version of Microsoft Level II BASIC. At Summer CES in Chicago it directly competed with the APF Imagination Machine and the Texas Instruments 99/4 (the original), and indirectly with the Atari 8-bits which earlier debuted at the Winter show. While it lacked the $599 model's monitor (a TV set or Tandy monitor was required), it had a better keyboard mechanism and a built-in cassette recorder, and was variously announced between $500 and $600 with 16K of RAM [$2200-$2760].
Down under, Dick Smith Electronics had grown far beyond its car park roots in 1968 Sydney and was already by this point making early steps into the computer business. For readers unfamiliar with the chain, DSE shops in Australia and New Zealand occupied the same market niche back in the day that Radio Shack and Heathkit outlets did in North America, catering primarily to the home enthusiast with hobby parts, kits and rebadged consumer electronics. (There were also a small handful of stores in California but they were never successful.) In 1977 the company started selling a kit computer detailed in
Electronics Australia
, John Kennewell's National Semiconductor SC/MP-based
MINI-SCAMP
, running the CPU at roughly 500kHz (based on a typical 2μs cycle time) and 256 bytes of RAM expandable to 1K (64K addressable). DSE advertised the machine as "33% of the cost of the
EDUC-8
," an earlier
Electronics Australia
bit-serial TTL hobbyist system inspired by the
DEC PDP-8
and designed by Jamieson Rowe — remember that name — who became an enthusiastic proponent of the new machine. Over in Silicon Valley, Palo Alto arcade game builder Exidy had developed their own Z80-based computer in 1978, the Exidy Sorcerer, a premium system featuring programmable character graphics, a faster 2.1MHz CPU and a built-in internal S-100 bus. Exidy saw the export market as a growth opportunity and aggressively inked deals with multiple foreign distributors, including DSE, who were taking ready advantage of the Whitlam government's 1973 import tariff reduction to bring more finished goods to DSE stores.
The Sorcerer arguably found greater success in Europe than it ever did in the United States, particularly in the Netherlands where the licensed Compudata Sorcerer became the default government-supported educational system, and certainly in Australia due to Dick Smith's dogged promotion. Still, even in the US it was considered relatively expensive at $895 [$4580], and with tariff and import costs tacked on it didn't price itself well to the Aussie
working class nerd
. Conversely, the EACA Video Genie had meanwhile achieved some popularity of its own within Europe, notably West Germany, in no small part due to its lower cost. That alone made it a logical system to transition to, and better still, EACA had absolutely no objection to DSE outright rebadging it as a Dick Smith unit.
New for a new decade, the EACA Video Genie became the Dick Smith System 80 in (wait for it) 1980 and started at A$595 for a 4K version, approximately US$510 at prevailing spot rates and around US$2060 in 2026 dollars (the 16K version was A$695). Peter Hartley in
Micro-80
disliked the altered keyboard (no CLEAR and TAB, no left and right arrows, up and down replaced by ESCAPE and CONTROL), complained about its changes to the character set and video circuitry, found the built-in cassette deck hideous, and noted the lack of board sockets and the missing-at-launch S-100 expansion box, but approved of the "brilliant" and "attractive" appearance, its overall functionality, and most of all its purchase price. "Even if you buy a decent tape deck from your local Big W and put it in the System 80," Hartley concluded, "you end up at least $150.00 [US$130 spot, US$520 in 2026 dollars] ahead — and that pays for your next 16K of RAM chips ... the machine has an identical computing capacity to the TRS-80, for a lot less dollars."
At this point it was inevitable someone would poke the Tandy bear, and that someone was Recortec (they're
still around
), established in Sunnyvale, California in 1969 to specialize in magnetic tape recording technology. In 1980 Recortec, also attempting to expand their product base, opened Personal Micro Computers, Inc. (PMC) as a new venture in Mountain View, initially entering negotiations with Exidy to buy out the Sorcerer — until, through EACA's American subsidiary, they became aware of the Video Genie. To PMC/Recortec, the Genie was a remarkable opportunity, a less expensive TRS-80 compatible system already selling in Europe and entering the Australian market, and PMC now had the chance to corner it for American distribution. The company immediately backed out of the deal with Exidy, bought up Genie distribution rights in August for the entire Western Hemisphere, rebranded it as the PMC-80 and launched it in 1981 with 16K of RAM for $675 [$2330].
InfoWorld
was more complimentary than
Micro-80
had been, noting PMC's planned Fastload high-speed cassette scheme, a 50-40 adapter to connect Model I peripherals  directly and a true lowercase conversion kit. "Tandy," said columnist Tracy Deliman, "is apparently curious now" — and in particular their attorneys, who promptly filed suit in federal court against both PMC and EACA of America, claiming, among other allegations, that the name PMC-80 infringed their trademark and that EACA and by extension PMC had committed copyright infringement as well by substantially copying the system ROMs. (Tandy didn't dispute the BASIC ROM, as that was licensed from Microsoft, but EACA and PMC dragged Microsoft into court with them anyway as a third-party defendant. Microsoft was a lot smaller then.)
In their motion to dismiss, PMC and EACA did not deny that the code had been copied and that then-current copyright law covered computer programs, but argued that section 117 of the in-force 1976 Copyright Act required the infringement claim to be interpreted according to the law prior to January 1, 1978 ("this title
does not afford to the owner of copyright in a work any greater or lesser rights
with respect to the use of the work in conjunction with automatic systems
capable of storing, processing, retrieving, or transferring information, ... than those afforded to
works under the law, whether Title 17 or the common law or statutes of a State,
in effect on December 31, 1977"). Robert Peckham, chief judge for the Northern District of California, disagreed in August 1981 and denied the motion, writing "that section 117, as it existed in the 1976 act,
was aimed at the problem of copyrighted material inputted [sic] into a computer, such as books,
magazines, and even computer programs. It was not intended to provide a loophole by
which someone could duplicate a computer program fixed on a silicon chip." Moreover, even if it did, "[t]he plaintiff
has suggested that the evidence may well show that the chip was duplicated by first taking a
visual display or printout of the program in question ... If this method of unauthorized duplication in fact is proved, there can be no doubt that the
unauthorized duplication of a visually displayed copy of the program would fall within the
reach of the federal copyright laws."
The case was quietly settled out of court, and although it obviously didn't enjoin EACA outside of the United States, domestically PMC replaced the line with the CP/M-based MicroMate in 1983. By then, and unknown to his backers, Eric Chung's failed investments in the Hong Kong real estate market had put him millions of dollars in debt. In October 1983 he abruptly fled to Taiwan reportedly with $10 million stuffed in a suitcase, leaving EACA to quickly fold. Simultaneously, Dick Smith sold a 60% stake in Dick Smith Electronics to Woolworths (the Australian version) later in 1980 and then the rest in 1982, leaving only his name and his bespectacled grin to remain at the company he founded. Although DSE sold the Video Genie's modestly upgraded direct successors also as System 80 variations, the System 80 family never included the Colour Genie, EACA's last system before its ignominious demise. PMC's former headquarters in Mountain View are now collectively Google Building E475.
Back in Hong Kong, VTech had come to a similar conclusion about the TRS-80's cloneability but approached it from the opposite end of the market, more congruent with their low-end toy and electronics emphasis. This strategy was bolstered by the successful 1980 UK introduction of the Sinclair ZX80, the first computer under £100, about US$225 spot and US$910 in 2026 dollars (cheaper still if you built it yourself). By any objective criterion, even contemporary ones, the ZX80 was an exercise in deprivation: a membrane keyboard, a software-generated black-and-white text-and-semigraphics screen that required its unlicensed (!) NEC Z80 clone CPU to devote much time to drawing it (or not), 1K of RAM (shared with the 32x24 screen), no audio, and simple cassette output. Reviewers found them unreliable and they overheated easily. They also sold like hotcakes — by the end of 1980 over 9,000 were being produced a month — and so did the modestly upgraded 1981 ZX81, which enhanced the BASIC and reduced the hardware to just a handful of chips, making it even cheaper to produce. Regardless, or perhaps because, of its faults, the machines endeared themselves to thousands of Britons who might not have been able to afford a computer otherwise, becoming their
first step to computer literacy
.
The success of the ZX80 suggested other dirt-cheap home computers might also flourish. VTech accordingly began developing a low cost computer of their own in 1981 that could work
like
the TRS-80, planning to adopt its BASIC (and thus its Z80 CPU) much as crosstown rival EACA did and speed time to market, but by explicitly abandoning compatibility they were free to slash its production cost as much as practical. A substantial reduction in part count became possible immediately by using the inexpensive Motorola 6847 Video Display Generator, introduced in 1978, which replaced nearly the entire video system: with minimal support circuitry, the VDG chip could generate a 32x16 text display, comparable to the TRS-80 and Video Genie's 32-column mode for colour TV sets, 64x32 colour semigraphics reminscent of the same, and a variable high-resolution bitmap display depending on available memory. On top of that, the entire system could run from the VDG's standard 315/88 (3.58MHz) crystal, including the Z80, and part count could be reduced even more for a black-and-white low binned model by omitting the colour encoder completely. Everything else (cassette output, keyboard lines) could be supported with discrete components and a handful of TTL logic, price could be adjusted further on the basis of included RAM, edge connectors wired to the processor bus would suffice for peripherals and expansion, and
any
sort of keyboard would be a step up from a flat membrane.
While the low-end computer was in development, VTech also hedged its bets with a higher-spec video game system, which typical for the era (see, for example, the Intellivision Keyboard Component) was convertible into a home computer of its own. This console was likewise built from off-the-shelf components, using a 2MHz Rockwell 6502 CPU and the Texas Instruments TMS9918A for graphics, 17K of RAM (1K for the 6502's zero page, stack and low memory, and the other 16K for the VDP), and controllers that doubled as a membrane keyboard when used with the optional BASIC cartridge. It shared no parts or significant engineering with the computer prototype and proceeded along a largely separate development track, released to select European test markets first as the VTech CreatiVision in 1982.
Meanwhile, Sinclair Research and manufacturing partner Timex Corporation subsequently joined forces to launch the Timex Sinclair 1000 in the United States, a slightly reconfigured ZX81 with NTSC-compatible video output and 2K of RAM, but otherwise identical. It hit stores in the summer of 1982 at the same psychologically desirable price point, now US$100 [$345], though Timex Sinclair didn't get the bargain American home computer market to itself like the ZX80 mostly did in the UK: it now had to contend with Commodore, selling the VIC-20 as their well-supported low-end system, plus the ailing Atari and their Atari 400, Tandy's own TRS-80 Color Computer, and even Texas Instruments, then only months away from igniting a price war
using the TI-99/4A
. Nevertheless, industry observers generally believed the T/S 1000 would be a strong competitor, and its debut led to an accelerated scramble from VTech and others hoping to duplicate the ZX80/1's success. VTech identified two overall product positions, a super-low-cost black-and-white variation with Microsoft Level I BASIC for selected markets, and a colour model with full Microsoft Level II BASIC, each of which VTech intended to sell both under its own name and as an OEM. To prepare for the American launch of the nearly complete low-end computer and the CreatiVision, VTech opened a U.S. subsidiary that year in Elk Grove Village, Illinois outside Chicago (the picture above is from VTech's history page).
1983 in the United States was the year the low-end home computer market exploded, and a cavalcade of hopeful new market entrants crowded that year's shows. At the January Winter Consumer Electronics Show in Las Vegas (above from
Computer Gaming World
issue 3.2), it took the Las Vegas Convention Center, the Hilton Convention Center, the Riviera Convention Center, the rest of the Riviera and the old Rotunda to contain it all. Mattel introduced the Aquarius for $199 [$670] licensed from Radofin, also in Kwun Tong (with a 3.58MHz Z80A and 4K of RAM, cassette storage, no bitmap graphics option and a rubber chiclet keyboard), Texas Instruments hawked the TI-99/2 for $99 [$330] (with a 2.7MHz TMS9995, 4K of RAM, cassette storage, no bitmap graphics option and no colour, and a plastic chiclet keyboard), Sanyo proffered the PHC-20 also for $99 as the midrange of the pocket computer PHC-10 and higher-end PHC-25 (with a 3.58MHz Z80 clone and 4K of RAM, cassette storage, no bitmap graphics option and no colour, and a rubber chiclet keyboard), and at the higher end came the Panasonic JR-200U for $349 [$1170] (with a 0.89MHz 6800 clone and 36K of RAM, cassette storage, no bitmap graphics option, and a rubber chiclet keyboard), the NEC PC-6001 also for $349 (with a 4MHz Z80 clone and 16K of RAM, cassette storage, but bitmap graphics and a rubber chiclet keyboard that was quickly replaced with a typewriter-style one), and the Spectravideo SV-318 for $299 [$1000] (with a 3.58MHz Z80 and 16K of RAM, also bitmap graphics, and a rubber chiclet keyboard). There were multiple conversion kits to turn the Atari 2600 VCS into a low-end computer of its own, several with rubber chiclet keyboards, and even a completely unlicensed ripoff of the T/S 1000, the Unisonic Futura 8300 (with a rubber chiclet keyboard) for $99. Not to be outdone, Timex Sinclair themselves announced the T/S 2000, a modified US version of the ZX Spectrum, with 16K or 48K of RAM, a 3.5MHz Z80, colour bitmap graphics and a rubber chiclet keyboard; the 16K version started at just $150 [$500].
The latecomers arrived at the Summer CES in Chicago, though by that point the rot was already setting in. Against the background of Commodore slashing prices even lower on the VIC-20 and C64 to Texas Instruments' profound discomfort, Mattel suddenly decided the Aquarius needed a sequel (i.e., the
other
system Radofin was developing; price point to be determined but without a rubber chiclet keyboard); Timex Sinclair replaced the T/S 2000 with the enhanced T/S 2024 and T/S 2048 with higher resolution graphics, more RAM and a plastic chiclet keyboard, plus an upgraded T/S 1500 which was a T/S 1000 with 16K of RAM and a rubber chiclet keyboard; Rabbit Computer (who? also from Hong Kong) introduced its own Z80-based Rabbit RX83 with 2K of RAM, BASIC, three-channel sound, cassette storage, bitmap graphics and a plastic chiclet keyboard for $99; and Tomy unveiled the Tomy Tutor for "under $150" [$500] with a 2.7MHz TMS9995 (from a 10.7MHz crystal), 16K of RAM, cassette storage, bitmap graphics and a rubber chiclet keyboard. In the fall Tandy, never one to be left out of a race to the bottom, delivered the MC-10 Micro Color Computer for $120 [$400] with an 0.89MHz 6803 and 4K of RAM, cassette storage and bitmap graphics, and a rubber chiclet keyboard. Even Commodore, failing to learn its lesson from the critically maligned
Max Machine
, was working on their own ultra-low-end family of computers to follow on to the C64 —
one of which
(the 116) would have a rubber chiclet keyboard.
And, oh yeah, one other system made its debut at the Winter show.
COMPUTE!
in their March 1983 reporting called it "the first under-$100 [$330] color computer." Anticipated to hit American store shelves in April, the new VTech VZ200 featured 4K of RAM (expandable to 16K for $45 [$150] and 64K eventually), 12K of ROM (remember these numbers) with BASIC, and a simple push-pull piezo for sound. Two kilobytes of the 4K was allocated to the 6847, which used it to generate its default 32x16 text display, 64x32 semigraphics or 128x64 bitmap graphics. It had built-in jacks for cassette, TV and composite video, and shared its booth with the CreatiVision which VTech planned to sell States-side for $189 [$630], with the BASIC cartridge for $10 [$33] and an inevitable rubber chiclet keyboard for $30 [$100]. It isn't clear where the
name
VZ200 came from, possibly a riff on "ZX," but the computer's low cost even amongst a sea of low-cost computers still attracted positive attention.
Creative Computing
got a 4K VZ200 in
for review in their May issue
(accounting for publishing delays this would have to have arrived in February or early March), though they noted that they had no chance to try the peripherals or software. The article has some glaring technical errors — among others, they said the CPU was a
6502
— but reviewer David Ahl called the machine "a compact microcomputer with a great deal of capability and many unexpected features at a very attractive price." Although the review found the 4K of RAM "sparse" and was openly critical of the keyboard, particularly the absent space bar, single SHIFT key, nonstandard layout and the keys' inconvenient tendency to stutter, Ahl was nevertheless impressed by the full-screen editor ("a pleasure") and the 12K ROM implementation of BASIC (unbeknownst to him, secretly derived from the TRS-80 with added support for the on-board hardware), concluding the VZ200 to be "a great value for the suggested retail price of under $100."
There are certain attributes of the machine shown in both the
COMPUTE!
and
Creative Computing
photos that don't match released units, but we'll address this later on.
Collectively American industry rags used various euphemisms like "low cost home computers" and "computers under $300," like this
Creative Computing
Winter CES cover showing the VZ200, the Timex Sinclair 2000 (in its original form), the Texas Instruments 99/2, the Mattel Aquarius and the Spectravideo SV-318. Personally, however, I lump these computers together as the "crap home computers." I use this term with only love, and this uniquely terrible subtype of the home computer was indeed
greatly
loved, because as the ZX80 had demonstrated, ordinary people could now finally afford them. Heck,
my
first computer — the Tomy Tutor, introduced
at Summer CES
— was one of these 1983 crap home computers because it's what
we
could afford. We couldn't afford a Commodore 64 right then, but we could afford
that
. Not for nothing did Jack Tramiel thunder, "computers for the masses, not the classes!"
What these systems all had in common, other than crummy keyboards, a striking preference for the Z80 and an unabashedly low starting price, was aspirational and arguably fraudulent marketing, plus inadequate specifications requiring upgrades at additional cost to be practical — if there were any to begin with — alongside substandard quality control, a poor selection of software, and weak to non-existent customer support. Made cheap to sell cheap, most of these computers failed outright (e.g., the Mattel Aquarius) or were never even released (e.g., the TI 99/2).
The glut that hit the U.S. market that year not only soured many American consumers on home computers generally, but their game-heavy libraries were also likely a contributing factor to the 1983 video game crash. Although managing to move over half a million units, Timex Sinclair was not immune to this effect, and the company became unprofitable as the sales crossfire between Commodore and Texas Instruments forced the T/S 1000's street price below $50 in mid-1983. The situation was compounded by Timex's ill-considered decision to make the more expensive T/S 2068 (the eventual sole member of the 2000 family) largely incompatible with the ZX Spectrum, robbing it of the extensive British Spectrum software library, and the joint enterprise that was once expected to dominate the American home computer market collapsed in early 1984. Even large players like Texas Instruments and Warner Communications-era Atari took hundreds of millions of dollars in losses, with only Tandy (due to their strong retail presence) and Commodore (due to the C64's prodigious installed base and their vertically integrated manufacturing) able to weather the maelstrom effectively.
VTech suffered nearly as badly in the United States as the others, severely harming the VZ200's North American launch and forcing the States-side CreatiVision release in its console form to be cancelled completely. Fallout from the Tandy EACA-PMC lawsuit further unsettled VTech management, causing them to remove more obvious signs of their unlicensed Microsoft BASICs' original TRS-80 provenance and disable certain keywords (more on that later). For Summer CES 1983 VTech attempted to recover by reworking their then-disorganized and otherwise unrelated computer offerings into a unified "Laser" brand. The VZ200 and the CreatiVision's computer morph accordingly became the Laser 200 (still $99) and Laser 2001 (now $299 [$1000]) respectively, and VTech added their own 64K Apple II clone, the Laser 3000, for $699 [$2300].
But by then it was too late. Although VTech never attempted to introduce the black-and-white model in America — and the T/S 1000's plummeting price would have made it impossible to make money on anyhow — the colour VZ200 fared little better, virtually disappearing from North American store shelves by the end of 1983 with no evidence any Laser 200 units were ever sold there under that name. In
Family Computing
's inaugural September 1983 issue the columnists mention the SV-318 and even the stillborne T/S 1500, but nothing on the Lasers, and
Creative Computing
around that time was only running ads for the 3000. A few VZ200s were rebadged by Texas door-to-door nuisance business Dynasty Computer Corporation as the Smart Alec Jr., though like their multi-level marketing attempt at rebadging the spent Exidy Sorcerer, they sold barely at all (the company folded in November). On the other hand, the (now) Laser 200 got off the ground in Europe under its own name and others, most notably through Sanyo, but also through Salora, Seltron and Texet. It launched there alongside the black-and-white model as an ultra-low-end system, originally dubbed the Laser 100, but after the ROM change becoming the Laser 110 with the same Level II BASIC of the colour version.
However, there was one market where the VZ200 had particularly strong success, and that was of course Australia, though not exactly in its original form. History does not preserve the thought process of Dick Smith Electronics management, but DSE's probable aim was to nose past the Commodore VIC-20 on price and capability (DSE themselves even sold them for a time), which was colour and shipped with 5K RAM. That immediately excluded the black-and-white variation, since the ZX81 had since landed in Australia and the potential profit margin wasn't enough to bother, and it is instead more likely that during negotiations DSE prevailed upon VTech to strengthen the colour system and keep the price low. VTech's solution was a small 6K daughterboard retrofit that could replace the 2K system RAM chip, internally expanding the unit to a more appealing 8K (the other 2K video RAM chip was left unmolested) while still being able to use previously manufactured components. This modified VZ200, badged as a Dick Smith computer and subsequently sold elsewhere by VTech as the Laser 210, appeared in the 1983-84 catalogue as "new for 1983" at just A$199 [approximately US$220 spot and US$720 in 2026 dollars].
Although Tim Hartnell in his
Australian Personal Computer
April 1983 preview speciously characterised it as "to Dick Smith's specifications" (likely only the RAM complement was), he got quickly used to the keyboard, approved of the BASIC implementation (faster than the ZX Spectrum's) and full screen editor, noted the characters to be "rather like those produced by the TRS-80 Color Computer" (true!), and compared the memory loadout favourably to the VIC-20's. He was similarly pleased with the cassette tape performance and the included documentation, with about his only complaint being the weak sound. His editor Sean Howard was equally impressed, famously remarking that "I'm certainly going to buy one," which DSE promptly and repeatedly used in their advertising.
The computer became an immediate hit via DSE store shelves and mail order starting in May, sold with DSE's own tape software and rebranded VTech peripherals such as the essential 16K memory expansion pack. It launched simultaneously with Dick Smith's rebadge of the hapless CreatiVision, sold as the Wizzard [sic] for A$295, both the first of
many VTech rebadges
DSE would eventually sell. Although nothing was going to catch the Commodore 64 by then, which had the same stratospheric sales there as it did most other places, the DSE VZ-200 had the added good fortune of ZX Spectrum manufacturing issues that eroded its availability, giving the DSE VZ-200 almost unrestrained run of the Aussie low-end market from which the VIC-20 was already fading and the ZX81 all but gone. In 1984 it remained a strong seller at its new lower price of A$169, dropping to A$99 by the end of the year.
I think that suffices for a more detailed backstory; we'll talk a little more about its later history in Australia and VTech's overall as a postscript at the end. For now, we'll turn our attention to this orphaned American unit.
A convention I'll establish from now on in this and future articles:
although Dick Smith was not consistent on the hyphenation, variously rendering it VZ-200 and VZ200, in the few places it appears the American version was invariably written without one, so I'll write "VZ200" for the North American computer and "VZ-200" for the Australian computer.
This VZ200 set was from an eBay auction a few years ago that I dug out from the storage unit to test since I hadn't really worked with it much. By this point I'd acquired a Aussie VZ-200 and VZ-300, which we'll get to in a moment, so it was nice to pull this American unit back out as comparison. It came with the 16K RAM expander and a set of joysticks.
The box advertises 9 colo(u)rs, 16K "bytes" of ROM — more than the 12K of the CES units — Microsoft* BASIC, though the asterisk only indicates it's a trademark, "full on-screen editing" and "advanced graphic & sound features." A red flourish at the bottom prominently touts its "4K BYTES" of RAM.
The side of the box has some alleged screenshots. My personal favourite is the police officer game in which you apparently either have severe haematuria or recently took rifampin and pee red onto passing cars, or at least that's what I think is going on. I enjoyed Potty Pigeon on the C64, so this would seem like my kind of game. Unlike the front and a couple of the side panels which are English-only, this side is labeled in English, German, French and Spanish, where you can easily find the
biblioteca
. You can also see more clearly that the red blurb on top advertising "WITH 4K BYTES RAM" and "NTSC 4K" is in fact a sticker, so this box was almost certainly not exclusive to North America and may not have been exclusive even to 4K systems.
The back of the box is also labeled in all four languages and purports to show the VZ200 as part of this complete breakfast with a light pen, "television or monitor," joystick, cassette, "16K/64K RAM memory expansion module," and printer interface. The light pen, interestingly, was unavailable on either side of the Pacific, though it was sold for the Laser series in Europe and would work unmodified with the VZ-200. On the other hand, I can't find any evidence that anything other than the joysticks and 16K expander were sold in North America, and I have never seen a 64K expander (though I am told it exists).
Two of the boxes have price tags, the computer and the RAM expander, but unusually the computer started at $129.95 and then got
increased
to $149.95. Neither price matches its well-documented MSRP of $100. Unfortunately I can't make out the actual retailer, even with an extreme enlargement.
On the RAM expander box, however ($69.95), the store's name is legible: Heathkit. Zenith Radio Company (now Zenith Electronics, a subsidiary of LG), which had acquired the hobby electronics retailer in 1980, poured substantial money into expanding the firm as a Radio Shack competitor. This extended to opening a number of Heathkit Electronic Centers across the United States and also in Canada, where there were outlets in (at least) Mississauga, Calgary, Edmonton, Montreal, Ottawa, Vancouver and Winnipeg.
Although the eBay seller was also American, I've concluded that these were likely products produced for the United States but ultimately sold in Canada, possibly as remaindered stock. For readers outside of North America, Canada used the same NTSC video standard and 110 VAC outlets, so it would have "just worked." Also, the 1983 Canadian dollar exchange rate was roughly about C$1.23 per US$1, explaining at least the initial price, and while the lack of
markedly predominant
French labeling might have prevented its sale in the Montréal outlet, that wouldn't have enjoined it elsewhere. As far as its provenance, however, the fact it wasn't labeled that way suggests Canadian sale was not initially contemplated, and it also has U.S. Federal Communications Commission clearance (I'll show you in a bit).
The computer sits inside a Styrofoam sandwich as most systems were shipped at the time. There's a small amount of scuffing which I'm not pleased about but also means this machine at least did get used.
Compare the label and the keyboard to the previous
COMPUTE!
and
Creative Computing
pictures. Those earliest systems are labeled as a "VZ200 Personal Computer," not a "VZ200 Color Computer," and the colour labels over the number keys were absent. In fact, this same keyboard is used for the B&W Laser 110, though those early VZ200 systems must have been colour given that their colour capabilities were widely reported at the time. On the other hand, the VZ-200 that appeared in very early Dick Smith marketing like the flyer above was labeled a "VZ200 Color Computer" exactly like this one, including the American spelling.
The keyboard consists of 45 keys, with a bottom right SPACE key in the corner, only one SHIFT on the bottom left, and no ESCape key. Necessarily, many have multiple functions accessible with the CTRL key or CTRL-ENTER key combo. Most of these alternative functions are one-touch BASIC keywords like the Sinclair machines, though unlike those computers, you are not obligated to use them and can spell keywords out if you want. Semigraphics characters are also selected by key combination, as well as moving the cursor, inserting and deleting characters, and interrupting a BASIC program.
Inside the box is a demonstration tape, a heavy unregulated wallwart that would likely dent your skull if lobbed incautiously (outputs a nominal 8V DC 1.5A centre positive), an RCA cable for connection to a TV set (but no switchbox) or monitor, the user manual, a BASIC "application programs" book with simple sample BASIC programs for type-in, and a larger spiral-bound BASIC reference manual. Under the manuals is a 1/8" audio cable for the cassette port terminating in input (black) and output (red) leads.
I was immediately suspicious of the wallwart and bought a regulated 9VDC 2A switched wallwart to replace it (the machine will run fine at this voltage). The user manual proper is very sparse, mostly just how to hook the computer up. The BASIC "reference manual" picks up from there, less an encyclopaedic reference text than an in-depth tutorial.
The rear ports consist of, from left/west to right/east in this view, power jack, cassette jack, RCA jack for composite video, the expansion port, the peripheral port, and finally RF output for a TV set. There are no slots on the sides, only a single rocker power switch. The main difference between the expansion and peripheral ports is that the expansion port gets the full 16-bit address bus and certain other processor lines, while the peripheral port (also referred to as the I/O port) only sees the lowest eight bits of the address bus — all that would be required for using the Z80's 256 I/O ports — and a smaller set of control lines.
Notice the peripheral slot still has its cover on it, secured by two small screws, which ordinarily would have been removed before use. This is where the joysticks and printer interface (again, I have found no evidence it was ever sold States-side) would have connected, and we'll see why it was never used shortly. There should be a cover for the expansion slot also, but it
was
removed, because the 16K RAM expander connects there. The cover is not in the box and I'll presume it was lost or destroyed by the previous owner. That's annoying from a preservation perspective, but no great loss functionally, because we'll have something plugged in there pretty much all the time later on.
The underside of the unit is also noteworthy (serial# V078451). For this discussion I invite comparison with Bill Loguidice's computer (serial# V024662), which he has since sold but pictures are still
on the Wayback Machine
, and is the only other NTSC VZ200 unit I have seen myself. Both his and mine have a "VZ200 Color Computer" bottom plate with a copyright date of 1982, and both have US FCC clearance tags and an RF switch to pick the channel (2 or 3). There are passive cooling vents on both sides, though given the fairly small amount of clearance its rubber feetsies afford from one's desk I hesitate to say they'd be effective. (At least they let you hear the piezo speaker.) There is also a small red sticker on the bottom which on mine is partially missing, but Bill's has a complete one, which reads "U NTSC 4K." I put a small piece of transparent tape over the sticker on mine to prevent further damage. Bill's unit also has both port covers.
Although the serial number indicates his is a rather older unit, which we'll in fact confirm later, the label and keyboard are the same as mine and not those earliest CES models. Both units have FCC Part 15 clearance, specifically as a Class B computing device for home use; at the time Class B regulations were very strict and we'll see a consequence of that inside. The FCC ID is
BNX84H80-0323
, with an equipment authorization (EA) applied for February 10, 1983 and granted May 9, 1983. Accounting for publishing delays, this means
Creative Computing
must have had a pre-authorization prototype for their review. VTech later applied for a revised equipment authorization on July 11, 1983 and was granted
BNX84H80-0323-1
on October 11, 1983; this change may have been for redesignation as the Laser 200. The listed address for VTech in Hong Kong appears on all entries for FCC grantee BNX and doesn't seem to have been their corporate address at the time, but the tester in both EAs is one Thomas Cokenias from
Electro Service Corp., at
1116 Ninth Avenue in San Mateo, California, and Cokenias and Electro Service are seen in other EAs around that time for other Hong Kong manufacturers. However, the given address appears presently unoccupied, and the California Secretary of State indicates Electro Service is no longer in business.
The other two boxes contain the RAM expander and the JS-20 joysticks/JI-20 joystick interface. Now we see why the peripheral port cover was still on: these joysticks are unused, still in their original bag and packaging. (Note from the future: as we'll see, many games play just fine on the keyboard, so the prior owner may never have needed them.) Though the joystick interface comes with a small instruction pamphlet, the RAM expander does not. Bill did not have either of these devices and that's likely why neither port on his machine was ever used.
Let's get out the rest of the family. VTech continued the evolution of the Laser 200 series with the Laser 310, a cost-reduced upwardly compatible version that used several gate array chips instead of discrete logic, but added more RAM (16K plus the 2K video RAM) and, for the first time, a proper keyboard with real keycaps and even a space bar. This time there would be no NTSC version; the 310 was never even announced in North America, instead launching in April 1984 at CeBIT in West Germany. It was sold in at least that country as well as France and mainland China, and Dick Smith picked it up for 1985 as the A$199 VZ-300. VTech had also developed a disk drive upgrade for the series, which DSE eagerly sold, and virtually all of the VZ-300 peripherals
except
its 16K RAM expansion (due to differing address mapping) would work on the older machine because many of them were effectively unchanged except for the labeling. (The address mapping difference is also why the VZ-200 16K RAM expander
will
work on the VZ-300, but only giving you an additional 8K.) Although there have been
various other members
spotted in the Laser 300 series, apparently differing only in RAM size or case type, none were reportedly sold widely if at all.
The VZ-300/Laser 310 is otherwise nearly totally compatible with the VZ-200/Laser 210 except for its clock speed. As NTSC compatibility was no longer required, VTech switched to a single 17.734475MHz master crystal divided by four for the 4.43361875MHz PAL colourburst and five for the 3.546895MHz CPU clock. (The Motorola 6847 VDG in the VZ-300 and PAL systems generally is clocked with an altered signal which I'll talk about when we open the machines up.) Although that makes the VZ-300 slightly slower at 99.09% the speed of the VZ-200's 3.5795454MHz (315/88) oscillator, in practical terms the difference was imperceptible with most existing software — but of course it's going to be a problem for
us
later. VTech did no other upgrades, not even offering an alternate 6847 font ROM with lowercase, though we'll talk more about that when we get to the innards as well.
The DSE VZ-300 and VZ-200 have prominent Dick Smith branding and are both labeled as "Personal Colour Computers." The keyboard layout of the VZ-300 is almost identical to the VZ-200 except for a second SHIFT key where the SPACE key used to be and then an actual SPACE bar below that. The keys are wired the same for compatibility, however, so the two VZ-300 SHIFT keys look like the VZ-200's single SHIFT key, and the left/right/up/down cursor block on M, comma, period and SPACE is necessarily broken up on the VZ-300 because of the SPACE key moving below to the larger SPACE bar. Early VZ-300s had brown keycaps with varying labeling, but later units like this one from about 1987 on have platinum-coloured keycaps that match the case. The effect is (probably intentionally) reminiscent of the Commodore 64C, just shorter.
I don't have all the accessories with my VZ-200 that I do with my VZ200, nor do I have its original Dick Smith retail box, but for the ones I do have I've compared them together in this photograph: the two main computers, their demonstration cassette tapes, and various documentation. The VZ200 BASIC Reference Manual and the Dick Smith Basic [sic] Reference Manual both appear to be identical down to the use of American spelling, even in the Aussie version, which calls into question the claim in Hartnell's review that it was written by VTech "under strict instructions by Jime Rowe [Jamieson Rowe] of Dick Smith Electronics" even though it is also not unreasonable to believe that DSE had some role in shaping it.
On the other hand, one manual unique to the VZ-200 was the Technical Reference Manual (TRM), which Rowe, by then highly placed in the Dick Smith organisation, wrote himself from VTech internal documents. This slim A4 book was never sold in America, and was
a Christmas gift from my wife
(I married well). The DSE pricetag on the back gives its price as A$9.50 but I don't know where or when it was originally purchased. While the TRM does not approach the sheer detail of, say, the Commodore 64 Programmer's Reference Guide, which even has an exhaustive memory map covering its 64K of RAM and 20K of ROM, it does include documentation on most of its important RAM locations and a full set of schematics, some of which we'll be using in this very article. A similar manual exists for the VZ-300 with its own set of schematics, which also discusses the VZ-200 and has some details not in the earlier text.
My VZ-300 system has more of the peripherals but little documentation. Displayed here clockwise from the lower left/southwest corner is a VZ-ASTEROIDS tape sold by DSE that would work on a VZ-200 with RAM expansion also, the VZ-300 Centronics printer interface (also works on a VZ-200), VZ-300 16K RAM expansion module, its own set of JS-20 joysticks and JI-20 interface (identical, differing only in badging), and its demonstration cassette.
On the underside my Aussie VZ-200 (serial# V027967) has a custom Dick Smith plate copyright 1983 and some quality control stickers, but no FCC badge. Although the aperture for the channel switch is still present, it has no actual switch. On the other hand, for the VZ-300 (serial# V224844) the switch was repurposed for black-and-white or colour output, which disables or enables the colour encoder circuit as appropriate. Interestingly the VZ-300's plate does not mention Dick Smith at all, nor have a Dick Smith part number or even a copyright.
A single teal sticker on the VZ-300 says "PAL-V 18K." This likely means VHF because the DSE VZ-300 sends its TV signal on Australian channel 1 (57.25MHz), and the VZ-300 schematics show separate circuits for PAL-V and PAL-U, which accordingly would be UHF.
Although the ports are the same too, when I got my VZ-300 it had already lost both its port covers.
The demo tape appears to be exactly the same between all three systems. While my DSE VZ-200 tape is missing its label insert, here is the one for my American VZ200 ...
... and on the right, for the VZ-300. You'll note they are almost exactly identical, including the idiosyncratic "Have Fun [sic] with your demonstration programs!!!" step 11, and also use American spelling; the only differences are the part number in the lower left, and the absence of a copyright message on the VZ-300 insert (replaced with "MADE IN HONG KONG"). On the left is the insert for the Asteroids tape, though it seems to only have generic loading instructions.
At the time DSE Pty Ltd was on the corner of Lane Cove Road and Waterloo Road in North Ryde, New South Wales (today postcode 2113 is Macquarie Park). This location housed a retail store and their main warehouse, which remained in operation until around 2001 when the warehouse was moved to Chullora (for Los Angeles residents, read "Vernon"). The North Ryde building was subsequently occupied by German truck and bus manufacturer MAN, whose old stripped logo can still be seen on the facade, and is now split between multiple tenants.
This is how my PAL VZ-200 comes out on my trusty NTSC Commodore 1702 monitor, the best JVC CRT screen Commodore ever rebadged. The picture rolls a bit and there is of course no colour (because it's being encoded for PAL) but it's enough to show you the ROM version, which is 2.0. These were the last ROMs used in the Laser family and are the same ROMs in the VZ-300 as well. This setup also serves as a weak mockup of what an American black-and-white VZ system might have looked like — everything could otherwise be the same modulo the absence of a colour signal. The character glyphs come from the default Motorola 6847 font ROM built in to the video chip.
Early Laser 100 computers came with 8K of ROM containing TRS-80 Level I BASIC, while the prototype VZ200 units shown at CES had an larger 12K ROM set apparently using upgraded TRS-80 Level II BASIC. Subsequent Laser 200/300-derived systems and the Laser 110 have 16K of ROM and TRS-80 Level II BASIC as well, which was deliberately obscured in later revisions of the ROM.
Level I BASIC
is quite, uh, basic, evolved by TRS-80 designer Steve Leininger from Li-Chen Wang's "copyleft" Palo Alto Tiny BASIC which Leininger substantially altered, reworking its structure and adding floating point math (because it couldn't accept Charles Tandy's salary when he typed it in), two string variables and a single array, and support for the TRS-80 hardware. VTech's version is similarly modified to support its own architecture but is otherwise the same. Level II BASIC is Microsoft BASIC, derived from Microsoft's own Extended BASIC on the Altair, and again VTech initially imported it nearly unchanged except for adding support for their hardware and graphics, which replaced some of the keywords (like TROFF with COLOR). Proof can be seen by comparing the order of keywords in their token tables, which would have no reason to match as precisely as they do unless they came from the same origin. Another persistent relic in the VZ BASIC ROM is the old Microsoft two-character error message table (e.g., ?SN ERROR instead of ?SYNTAX ERROR) even though the existing code never references it.
Tandy's apparently successful legal action against EACA and PMC spooked VTech that they could be sued in the same way — but by Tandy
and
Microsoft. The company's solution was to dump Level I BASIC entirely, eliminating any objection from Tandy, and for Level II BASIC to secretly null out a large number of entries in the ROM BASIC keyword table potentially unusual enough to be used as evidence of copying. The
tokens
for those keywords still remained valid, however, and the ROM code for them also largely persisted. Disk-specific keywords were likewise omitted in the same fashion, at least until the VZ-300 disk drive debuted, but unlike the other gutted keywords were instead vectored through RAM for later expansion. These keywords (in token order) are CMD, RANDOM, DEFINT, DEFSNG, DEFDBL, RESUME, ON, OPEN, FIELD, GET, PUT, CLOSE, LOAD, NAME, KILL, LSET, RSET, SAVE, SYSTEM, DEF, DELETE, AUTO, FN, VARPTR, ERL, ERR, STRING$, INSTR, TIME$, MEM, FRE, POS, CVI, CVS, CVD, EOF, LOC, LOF, MKI$, MKS$, MKD$, CINT, CSNG, CDBL and FIX. Because their implementations often remained present, it was possible to resurrect many of them by hooking into the RAM vector for tokenizing "new" BASIC keywords, and some BASIC extensions did just that.
The earliest versions of the Laser/VZ ROM use light green text on a dark green background. Without a colour encoder this would produce light text on a dark screen, which is indeed what you see on a black-and-white
Laser 110
. Bill's earlier NTSC VZ200
is the same way
, using the same ROM 1.2. By ROM 2.0, as in this VZ-200, the display became dark green text on a light green background, like the Tandy Color Computer which uses the same MC6847 video chip.
My unit here is also ROM 2.0 and comes up the same way, now with proper NTSC colours. This is notable because that means the American VZ200 must have remained in production long enough to actually get these final ROMs. Since we know that it's at least able to power up, we'll switch over to the composite capture rig for the remainder of our screenshots.
The presence of the 2.0 ROMs raises the question of whether we really have a 4K or 8K system here, despite what the sticker on the bottom says, so we should check that first. The VZ200 memory map is detailed in the Technical Reference Manual, but in broad strokes places ROM from $0000 to $3fff, option/cartridge ROM (or nothing) from $4000 to $67ff, memory-mapped I/O from $6800 to $6fff, video memory from $7000 to $77ff, and then the rest of RAM from $7800 to whatever the "top of memory" (TOM) is, either $ffff or the end of physical RAM, whichever is less. (This layout is not exactly as described if the disk system is present, but we're going to ignore that for our current purpose.)
On startup the ROM tests available memory and stores that final valid RAM address to the systemwide TOM pointer at 30897-8. On a 4K system we would only have 2K of general RAM available, so the TOM pointer should be at $7800 + $07ff, yielding $7fff or 32767. That is indeed the value of the TOM pointer, so we
do
have a 4K system, just a very late one.
You may have noticed the oddly convoluted BASIC statement I entered to get that figure. That's because I had to avoid typing the number 5: the key didn't work. Normally the VZ200 will beep as you press keys, but there was no beep and no response when I did. In fact, an entire run of keys (5, T, G, B and N) was not working, and I was only able to enter the PRINT keyword by pressing SHIFT-P. We'll need to fix the keyboard now to do anything substantial with this machine.
In the TRM's schematics we find the keyboard matrix, which is divided into an 6x8 grid with rows selected by the lowest eight bits of the address bus. (The TRM explains in section 3 that the matrix is scanned through simple memory-mapped I/O, another common attribute of crap home computers, even ones with CPUs like the Z80 and TMS9995 that have perfectly cromulent and proper I/O space.) The six columns are normally pulled high to +5V by a block of six pull-up resistors. As each address line row is cycled low during keyscan, if a key is pressed in that row, it will register a corresponding low level in its column to the chip at U12 which emits the six-bit result for the effective address onto the data bus.
My initial theory was that the column connected to R8 and U12 pin 8 was bad, which involves our 5, T, G, B and N keys as predicted. However, this column also involves the 6, Y and H keys, which
did
appear to work. Still, it seemed like the most reasonable place to start, so let's crack the computer open.
Internally the VZ200 is very simple and very cheaply made. There are three main divisions, the logic board itself, a smaller board to the left/west soldered to the main board with connecting jumper wires, and the keyboard, which is attached by a stiff wired plastic ribbon. There are no internal connectors, because that would have added cost and complexity, and for further cost reduction the circuit boards are all low-grade phenolic resin PCBs. Other low points include cardboard washers to prevent the mounting screws from shorting anything (we also saw this on
another VTech unit
, the unrelated Laser 50) and a plastic cover sheet with slits for the top ports' card edges to reduce dirt getting inside. Also visible on the top right/northeast side is a sprawling heat sink screwed to the fin of a 7805 voltage regulator peeping out from the lower right/southeast corner. This heatsink sits under the ventilation slits in the top case.
Much of the logic board is covered by a large sheet metal Faraday cage serving as an RF shield, festooned with soldered metal braids connecting everything to the ground plane, and then the whole assembly placed on an irregularly shaped metal plate on the bottom with the piezo. As mentioned, in those days the FCC was very strict about radio interference from computers and video games, particularly home units where a Class B device (as this is) had a 10dB lower maximum than a commercial Class A one. Some systems like the Atari 400 solved this problem by effectively encasing the entire system in a molded metal endoskeleton and placing as few holes in the case as possible from which radio signals could emanate. That made for a very sturdy computer but one more expensive to manufacture, so VTech went for this cheaper, hackier approach which was no doubt iterated upon until it just cleared the bar.
One major component is
not
under the cage, however, and that is the Motorola 6847 VDG video chip, in a plastic carrier (MC6847P) with a date code of 24th week 1983. It's not precisely clear why that is, but it can be seen that the left board is connected to some of its lines.
The chip on the left board is a Fairchild TBA520 manufactured by Telefunken (the date code is probably 25th week 1983). The TBA520 is a
PAL
synchronous
de
modulator, a surprising choice, since the MC6847 is usually paired with the MC1372 NTSC colour
mod
ulator. The 6847 emits YPbPr (as Y, B-Y and R-Y) video, which in the black and white Lasers only the Y (luma) signal is used. In other systems like the Tandy CoCo the MC1372 takes the YPbPr lines, encodes the colour, and emits a signal suitable for a television set and/or composite video depending on the specific components.
The TBA520 can be made to do the same task, even generating NTSC colour with the right crystal, albeit with more supporting electronics. (I presume it was less expensive than an MC1372, plus there would be the advantage of not having a different chip for Euro and Aussie systems, since the TBA520 can obviously do PAL video too.) Reference B-Y and R-Y signals are generated to the TBA520 using the 3.58MHz (315/88) NTSC colourburst oscillator on the left board, while the B-Y and R-Y signals from the MC6847 are passed on different lines, with the MC6847 running on the same 3.58MHz clock. We then pulse the TBA520's line inputs at the necessary horizontal rate, approximately 15.7343kHz, causing the TBA520 to emit a single NTSC chroma signal (on its G-Y pin) from the 6847's PbPr signals. (This theoretically makes it possible to get proper S-video out of the VZ200, though we're not going to try that this time.) Discrete components then combine the luma and chroma into composite video for both the monitor connector and for feeding into the separate RF modulator.
For comparison, here is the inside of the Aussie VZ-200. The heatsink-7805 assembly can be seen here as well, but the big difference is that the logic board is longer and the left board, which we now know to be the colour encoder, is sitting on top of it and the 6847. The additional circuitry under the colour encoder is what coerces the 6847, which requires a 3.58MHz NTSC colourburst frequency signal and expects to generate a 60Hz 262-line interlaced NTSC display, to generate a credible 50Hz 312-line interlaced PAL one instead. The 6847 is an autonomous device and draws the screen independently of the CPU. When the 6847 is done, it emits a signal, typically used as an interrupt to the CPU, but here also used along with the horizontal sync line to drive a series of discrete logic counters. These counters intermittently redirect the VDG's clock signal, halting it for a certain number of screen lines each time to pad out the frame by another 50 lines. These added lines also necessarily reduce how often the VDG is free to scan video RAM and draw the next frame (i.e., (262/312)*60 is ~50.385), thus achieving the reduced refresh rate.
The colour encoder board here has a 4.43361875MHz PAL colourburst crystal, but uses the same TBA520 part to generate the chroma signal. Because of the added circuitry required (including a long power wire) and the fact the colour encoder board now needs to be stacked on top because of the limited space available, this is good evidence that the VZ200 was designed first and foremost for the United States: the case fits the NTSC colour encoder board and its shorter main board more elegantly, and fewer components were needed overall (cheap!). Adding PAL components for the Euro and Aussie versions made the system more complicated and slightly more expensive to manufacture, which wouldn't seem like a desirable initial design result, and the American market was of course much larger — assuming you could actually sell any.
The redesign of the VZ-300 gives up even fewer of its secrets. The RF modulator and heatsink-7805 assembly persist, but everything else is sheathed inside the soldered-down Faraday cage, even the VDG and colour encoder board. Small apertures allow trim adjustments for the video, but that's about it.
Still, through the holes we can see the MC6847 ...
... and a real Zilog Z80, with a date code of 18th week 1986.
Back to the Yank VZ. To be able to check continuity we're going to need to get the keyboard out, so we'll start by removing the small screws affixing it to the top case.
The keyboard appears to have been installed at the factory by slipping it behind this plastic strut, screwing it down, and then soldering on the ribbon and epoxying it for strain relief. Unfortunately the strut is preventing the keyboard's removal and we can't cleanly reverse those steps, so I decided to just break the strut to get it out. The screws will still hold the keyboard in place when we put it back.
We can now separate the PCB from the rubber key sheet (no individual keys fortunately) and slide it out, still attached to the motherboard.
Turning it over, the keyboard PCB has multiple contact pads that are connected when the conductive nubs on the bottom of the key sheet press against them. The traces carry the lines from the keyboard matrix and intersect at those contact points. To avoid having to make a multi-layered board, traces crossing traces without connecting them are separated from each other with a strip of insulating material, and the crossing trace then bridged using what looks like conductive paint (cheap!). With this in mind, if we map out the traces starting from the top (north) row at the 5th position from the left (west), which is the 5 key, we have our line of bad keys. It starts at 5, then goes southeast to T, G, and B, and then east (right) to the N.
That seemed suspiciously like a continuity break to me, so I verified continuity between the 5 key (the closest to the ribbon cable) and the ribbon cable, and got what appeared to be a good connection.
Next I looked at where the ribbon cable attaches to the logic board. This is also soldered on. Checking the same contacts, there appeared to be continuity from the 5 key to the logic board as well, which would rule out the connector and the ribbon as causes. Now we need to open the Faraday cage to see if there's a break inside on the main PCB.
The Faraday cage is held on by metal tabs passing through the motherboard and soldered beneath it. Eventually I'm going to completely remove the Faraday cage because I don't care about RF leakage and it's just in the way (and I may need to do some work on the board later, though we'll talk about that after we fix
this
problem), so I decided to just clip the tabs with angle cutters. One of those tabs is here over by the 7805 ...
... and the other by the MC6847. The other two tabs are in the back corners and were pulled down flush with the board which might have made it hard to cut them without scuffing traces, so I just bent the RF shield back at this point.
Now we can see the main components. This is a single-sided board (cheap!), so there are no hidden pieces on the underside except for the piezo at the bottom, and you are therefore looking at just about the entireity of what's there. A few months ago we did an exhaustive teardown of a 1985 Canadian video titler, the
Scriptovision Super Micro Script
, which has a 6802 CPU (a microcontroller version of the 6800) and a 6847 VDG, RAM, ROM and a simple keypad for entry. In
that article
I mentioned that those were enough to make it
almost
a home computer (replacing the ROM on the Super Micro Script to make it one) because home computers like the VZ-200 have a similar architecture. Now we'll prove the comparison is valid.
In this view, the MC6847 is the large DIP on the far left/west side. The chips in the back, going from left to right, are a Hitachi HM6116P-2 2K static RAM used for video memory, the CPU, a clone SGS Z80 (the former state-owned SGS Microelettronica "Società Generale Semiconduttori" of Italy prior to merger into STMicroelectronics in 1987) with a date code of 19th week 1983, a Hitachi 74LS139 and 74LS32 used as part of the address decoding for the memory mapped I/O range, and lurking in the back right (east) corner a 74LS174 6-bit flip-flop serving as a latch register. In the front, also left to right, are a Hitachi 74LS245 octal bus transceiver which bridges the shared 2K video RAM between the CPU and VDG, a Hitachi 74LS04 hex inverter used for various tasks such as the CPU reset circuit, a Hitachi 74LS244 octal driver, another Hitachi 6116 2K SRAM (the system RAM this time), and the two 2364 8K system and BASIC ROMs with date codes of 27th week and 32nd week 1983 respectively. On the Dick Smith schematic using the same order, these chips are numbered U15 (the 6847), then U7, U4, U3, U2 and U1 (74LS174), then U14 (74LS245), U13, U12 (assumed), no designation for the single 2K SRAM, and U10 and U9 for the ROMs. The ROMs are unsurprisingly the newest chips in the system and mean the computer could not have been assembled earlier than then, likely making it part of the last production runs before VTech abandoned the line in North America.
Obnoxiously, everything is soldered down; there are no sockets (cheap!). However, there
are
a number of unpopulated pads. Some extra pads near the ROMs were clearly intended to accommodate larger-capacity chips, and later machines indeed use a single 16K ROM with a change in board jumpers nearby. (Braver folks than I have extracted VZ-200 boards with 2364s and found bodge wires underneath. Apparently underpaid labour and smaller ROMs were less expensive at the time. Cheap!) There is also another set of pads near the VRAM chip between it and a big block of through-hole resistors. It's not clear what these pads were meant for, though the VZ-200 schematics show another resistor bank there serving as pull-ups. This bank is drawn on the schematic with dotted lines unlike the other set, so perhaps they were eliminated for cost reasons (cheap!).
Now let's talk about what we
don't
see. One thing we don't see here is a 3.58MHz master crystal. That's because ... we already saw it. The entire system runs from the 3.58MHz crystal on the
colour encoder
, so everything is precisely synchronized to the same clock source, including the TBA520, the MC6847 and the Z80. It is therefore impossible to merely switch the colour encoder boards and turn an NTSC VZ200 into a PAL VZ-200 or vice versa because of the added line padding circuit in the PAL unit and the absence of a second system crystal in the NTSC unit (cheap!). What about the VZ-300, where there's no 3.58MHz crystal either? In that system, the VDG is entirely clocked by one of the gate array chips, providing the same line padding logic, but also using the same 3.54MHz clock as the CPU which is apparently "close enough."
Another thing we don't see is something like a Motorola 6883 synchronous address multiplexer. Recall that the 6847 VDG has no externally exposed registers of its own (compare to, say, the VIC-II in a Commodore 64). Things like video modes and character attributes are twiddled by chip lines; for character attributes these lines are often wired to certain data bits from the video RAM, but to dynamically set a video mode under software control requires external hardware. Also, the VDG makes little attempt to cooperate with the CPU as to when it accesses video memory, other than indicating when it finishes a frame which is likewise asserted on one of its pins. In the Tandy Color Computers (prior to the CoCo 3, which uses a GIME), the MC6883 SAM sits between the 6809 CPU and the 6847 VDG and arbitrates all of this, managing the display mode and system timing, and servicing the VDG while the CPU is on the bus. On the other hand, this approach was judged too expensive for the cut-down Tandy MC-10, which instead uses a series of flip-flops to interleave bus access between its 6803 CPU and the 6847. A single 74LS245 bus transceiver allows the CPU unrestricted access to the video RAM when the processor is accessing memory.
Neither approach is suitable in this case, however. An MC6883 would be too expensive for the VZ200 also (cheap!), and the Z80 sits on the bus longer during a CPU cycle than a 6502 or 6800-family chip would, so the MC-10's interleaved approach won't work either. As it happens, the VZ200 does nearly exactly what the Scriptovision Super Micro Script does: during CPU video RAM access, the VDG's memory fetch is immediately suppressed using its MS pin and the 74LS245 bus transceiver temporarily kicks it off the bus. The contention problem is solved in both cases
with software
(cheap!) by simply not doing anything with VRAM until the VDG indicates it's between frames and not reading screen memory. The only difference is how they find that out; the SMS busy-waits on the VDG's FS signal before doing a screen update, while the VZ200 just wires FS to its IRQ line — screen updates using ROM routines are batched and when the interrupt is triggered, the ROM then blits the deferred changes to the screen all at once. Of course, if you write directly to the video RAM when the VDG is accessing it you'll get intermittent artifacts, and I'll show you what that looks like, but you can just watch for the IRQ yourself if you really care about it (many programs didn't). Otherwise, the VDG's mode pins for bitmapped graphics and alternate colour selection are handled through bits in the 74LS174 latch within the memory-mapped range, which also handles the piezo and cassette output. Overall this is a good demonstration of how the SMS was
almost a home computer
, because here's a home computer whose video architecture was almost the same.
A missed opportunity with the more upmarket VZ-300 was the potential for lowercase or at least an alternative character set, especially because it even got a word processing cartridge released for it later (we'll play with it, it works with the VZ-200 also). An external font ROM can be lashed to the 6847 with a bit of additional circuitry and the Super Micro Script has one to generate higher-quality character glyphs. It seems like VTech could have done something like that controllable by another latch bit, and with a six-bit latch there are a couple more data bits there that could be used, but I guess that was either judged too risky or not even thought about. On both systems the 6847 INT/EXT pin that would have controlled this is merely hardwired to ground.
One note about the metal RF shield: if the cage is not pulled back down into position, it may distort and contact some of the pins on the 74LS174. This will cause weird graphical artifacts and knock out the piezo (no keybeep). It doesn't appear to harm the computer, but I was very careful to ensure it was bent back to as similar a position as before after this happened a couple times. Obviously this is no problem if you just completely take it off.
The situation is slightly more complicated on the VZ-200 with the 6K RAM daughterboard. Here you can see it sitting on standoffs with the lines from the three 2K SRAMs wired into where the single 2K SRAM would go, next to its NEC D780C CPU, another Z80 clone, with a date code of 21st week 1983.
The 74LS244 in the front is not identified on the Dick Smith schematic, but the presence of six 4.7KΩ resistors near it rats it out as the U12 chip in our keyboard matrix. These resistors have continuity with the +5V plane, so they are the column pull-ups. Yes, the solder is supposed to be bridged between some of the resistors and the 74LS244 like that; some checks with the continuity probe indicate it is wired exactly as indicated.
The eight diodes for the rows are located near the cable. Probing these I got continuity between them and the 5 key as well.
I was now starting to wonder about the 74LS244, because it had some weird bronzing like it had gotten burned or something. We know that the key is sensed if it goes logic low during scanning, so I ran a jumper between the metal braid (grounded) and pin 8 on the 74LS244 where that column should be connected, and turned the computer on. On my portable composite display you can see it acted like the G key was stuck down, which seemed plausible depending on the order the rows get scanned, so I concluded that chip line was probably fine.
I went back to the keyboard PCB and started testing the other keys that weren't working. The T key and G key pads appeared to have good continuity also.
Testing the bottom row, however, I abruptly lost continuity. Probing the individual connections between traces revealed a break in the conductive paint above the N key. This line gets propagated to all the other keys above it, and those keys' apparent connectivity was thus actually only on one side (and I was testing
that
), which is why they could never complete a junction and be sensed. On the other hand, the 6, Y and H keys on that column are wired separately into the ribbon cable, so they were unaffected.
I'm not sure how such a fault would have happened. The keys move, but they don't sweep or scour, and ordinarily they shouldn't be contacting the painted portions anyway. It also doesn't seem likely to have been a factory defect because that would have made the computer very difficult to use, and this computer was clearly used.
I pondered the best way to fix it, since any repair would have to be flat or it would distort the key sheet on top (e.g., no solder blobs, no top bodge wires). I have a circuit pen I could use to draw a new trace, but it's temperamental, and I didn't want to do something I couldn't undo later in case it wasn't actually the problem.
Eventually I hit on a cheap solution of my own: a small single-layer sliver of alumin(i)um foil. I put the foil strip between the two points of the break and secured it with Kapton tape, and the whole thing laid nice and flat. If my theory turned out to be wrong, I could just remove them and try something else.
But the keys now
do
work!
Using the angle cutters I nibbled off any portion of the Kapton tape that might cover up nearby pads and exhaustively checked all the keys. They all worked. The keyboard is fixed.
We then slip the keyboard PCB back behind the strut, making sure that the LED comes out through its little hole in the top case ...
... and replace the screws.
Do not overtighten them
or you will interfere with the conductive nubs being able to make contact. I had a couple dud keys initially after this which were returned to life by slightly loosening the screw nearest to them (to my great relief).
While we were in there, I decided to make sure the display quality was as good as possible by tweaking the colour encoder's trim adjustments, since its components had likely drifted with age. On this board the two trimpots control the colour phase, while the trimcaps appear to adjust image stability. I wrote a quick BASIC program to display the 6847's full palette, which is only possible using semigraphic characters, and tweaked it by eye for good colour on both my handheld composite display, the Commodore 1702 and my composite capture box. Here is how it came out with alternate text colours (i.e., with the 6847 CSS pin set with
COLOR ,1
):
and the default:
That brings me to a brief digression on the VDG and colour. Many people, especially those who have only used VDG-powered machines in emulation, think they emit beautiful fully saturated RGB, that the green is a gorgeous
#00ff00
and red is
#ff0000
and so forth. That is definitely
not
the case; in fact, the default VDG palette is rather a bit muddy, with relatively poor saturation. For example, black (what the border is supposed to be) is often more like a very dark brown, buff is a dirty off-white, magenta becomes a flaccid purple where the red is a little too low, and what the documentation calls cyan comes out closer to seafoam green. Unfortunately, many simpler or older emulators provide an excessively rosy (no pun intended) simulation of what these typical home computer implementations usually generated. MAME uses the correct palette and the VDG's Wikipedia entry has
a credible synthetic screenshot
based on the YPbPr values in the datasheet, which you can compare with the real composite grabs above.
That does not mean that the MC6847 VDG is incapable of good quality colour. It is
absolutely
capable of good output, but to do so it needs a quality encoder, and the VZ's ain't it. The best colour I have ever seen from a VDG is actually the
Super Micro Script
's, using a very high quality output stage as shown in the actual grab above, and comes out vibrant, beautifully saturated, and fabulous on a CRT. You would expect that, however — it's a $500 prosumer video titler from 1985, not a $99 crap home computer from 1983.
The next order of business is software. I'd rather not use tape or audio files, and I don't have the disk drive. Fortunately, because the VZ series is so beloved in Australia, those wacky Aussies occasionally create their own modern peripherals in between prawns on the barbie. If you have a VZ-series computer, then you need the
BennVenn VZ300 SD Loader
. It is fairly inexpensive and provides you a way to load software into your VZ-series computer via SD card, along with topping off the RAM, even more memory with bank switching, and optional solder-yourself connectors for gamepads and I/O expansion.
I figured it might be fun to build some hardware for it (and we're going to create a very simple expansion ourselves for the VZ200 in this article), so I ordered the full kit. It works well for my purposes and my wife has ordered another for the VZ-300 now at my in-laws' house in regional NSW. However, I am neither affiliated nor associated with Ben, merely an overall satisfied customer, so this is the part where I will also make three gentle constructive complaints about it.
First, things like new firmware are largely delivered through a private Facebook group. This group appears to be very welcoming to new members, but it requires you to be on Facebook, and I don't want to be on Facebook. I managed to get the current firmware another way, and I will be putting it in
the Github repo
for this project so you don't need to join Facebook either. (If you do want to join, however, I'm sure the
"VZ200 VZ300 Laser210 Laser310 fans"
group would love to have you.) On the other hand, Ben was reasonably accommodating of my questions over E-mail which I did appreciate.
The second complaint has to do with assembly. If you don't want to hook up joypads (it's reportedly compatible with SNES ones) or create your own expansion device with its GPIO pins, and you're only using the RAM expansion and SD card interface, then you can just put it in the included 3D printed case, insert a card, plug it in your computer and use it immediately. I think most people are doing exactly that. However, I wanted both those things, so I started on the GPIO connector first. The expansion GPIO pins need their own headers and Ben provides a set of right-angle through-hole headers that you solder on. Once attached, the 3D case has a thinned-out rear strip you can snap off to expose the pins.
Unfortunately, the GPIO pins are not strictly wired in order, so finding a bad solder joint may require checking continuity in unexpected places. The proto board here that Ben used to sell has a set of surface mount LEDs that makes finding a bad line easier, and all of the LEDs should be lit when enabled, so I was immediately able to detect a couple of dud joints on my first pass. (It doesn't look like these boards were very popular and he doesn't appear to sell them right now; check his site for the latest.) However, I then proceeded to waste an entire hour reflowing one particular joint repeatedly that
looked
like the right one until I got out the continuity tester and realized the actual fault was elsewhere. I'm not sure why some of them were routed around instead of in a straight line.
The third complaint also has to do with assembly, but the joypad connectors this time. VZ joysticks have various, uh, deficiencies in their design that I'll get to soon, but they also have two buttons, which means you can't directly substitute something more familiar like an Atari stick. (The Tomy Tutor has a two-button joystick, however, and being a Tutor dweeb I have a number in stock, so I might think about how I could use one of those.) Ben's solution was to implement support for Super Nintendo game pads, where they can emulate a VZ stick, and software aware of the extra buttons can read those too. There are no ports on the cartridge, though: you get to solder those lines on yourself as well, passing the cable through preweakened holes in the case that you ream out.
I doubted myself several times on the orientation because of how the cartridge has to get mounted in the case. On the case side where the wires come in, the board is actually mounted upside down, and the joypads on each side are wired in mirror images of each other. I first wired the left pad completely wrong, then got it right but wired it to the wrong side of the board, then didn't notice the mirror image orientation and wired the second pad wrong. Police may have been called for a welfare check by this point.
In the end I never got the joypads working. I realize I have less manual dexterity than an inebriated wombat, and it is possible that the Shenzhen knock-off SNES pads I used were defective, but I had continuity from the inside of the joypad all the way through to the SD loader board and it still wouldn't work. Plus, because SNES pads generate a clocked data stream, not individual switches like Atari (or Tutor) sticks, if you mess up even one line you'll probably get nothing. That's indeed precisely what I got, so I just cut off the ends of the cables and gave up. I may try putting a port on in the future and messing with it some more but I don't think I'm going to be up to that for awhile. I'm glad this unit exists; it just shouldn't have been quite that tricky to get the most out of it.
Still, our prize for all that is ... the BennVenn board "just works" with this seppo VZ200, though I suspect this is the first time his board has ever been used with an American unit, and the TOM pointer is filled out all the way to 65535 as expected. It appears the cartridge thinks this machine is a
Salora Fellow
, a Finnish rebadge of the 4K PAL Laser 200 (by contrast, the Salora Manager is a Finnish rebadge of the CreatiVision-derived Laser 2001). This is determined by a simple memory map check in a snippet of its VHDL that Ben shared with me:
RAMarea300   <= '0' when (Address > x"B7FF" ) else '1'; --B800 or higher
RAMarea200   <= '0' when (Address > x"8FFF" ) else '1'; --9000 or higher
RAMareaSelora   <= '0' when (Address > x"7FFF" ) else '1'; --8000 or higher
This section checks the detected top of memory and sets certain flags to be able to fill the rest of the address space with RAM. The VZ-300 has the most onboard RAM ending at $b7ff, so the cartridge only adds on an extra 18K. On the other hand, the Fellow's memory space ends at $7fff, just like ours, so it gets an entire 32K to fill the remainder. The cartridge detects our memory map is the same as a Salora Fellow, so we also get the extra 32K, which is exactly what we want.
I also plugged it into the DSE VZ-200, and it worked perfectly there too.
Since we're not going to use the joypads, that means we'll be using the joysticks. (Note from the future again: many VZ games play just fine with the keyboard and I didn't use the joysticks much after all, so I'll probably just not bother with joypads when I build the unit for the VZ-300.) The BennVenn cartridge emulates VZ sticks by default, even if the joypads aren't connected, but you can easily turn this off and use the regular joysticks.
The joysticks are technically three separate peripherals, namely two JS-20 joysticks and one JI-20 interface, though they're in practice one unit since they can't be easily separated; the joysticks themselves are soldered directly to the interface board (cheap!). Both the VZ-200 and VZ-300 joystick sets are internally the same. This is the interior of the interface, with only three chips: a 74LS09 quad-AND, a 74LS138 for address decoding and a 74LS367 hex bus driver. The computer itself has no specific support for reading the joysticks (cheap!), moving all the "smarts," as it were, to the interface and querying their state through ports in the Z80's canonical I/O space instead of memory-mapped I/O. When the IORQ line is asserted by the CPU, the 74LS138 is used to check the address on the low eight bits of the address bus, which are the only address lines carried on the peripheral port connector, and correspondingly enable (or not) the switch status for the appropriate joystick to be put on the data bus. Separate ports (39, 45) are used for the buttons as well as the directions (43, 46).
Although we have a brand spanking new set for the VZ200, when I tested the VZ-300's some of the directions didn't seem to work at all, so let's see if we can fix them.
I'll set some expectations here beforehand: even at their best these were pretty horrid joysticks. We know this because we can use the brand-new VZ200 sticks as a benchmark; they have little throw and you have to hit directions dead on or sometimes they won't register. This is because the stick pushes a plastic ring with four pins into one or more metal leaf-spring switches (again mounted on a crummy phenolic resin PCB) to indicate direction. Unfortunately these plastic pins are neither particularly durable nor especially hard, and unless you hit it squarely and precisely, the pin may not be able to engage the corresponding switch.
The leaf-spring switches themselves can also go bad, either because the leaf is fatigued and stretched from too many presses, or because the metal button it contacts is oxidized or otherwise unable to make an electrical connection.
To rehabilitate each directional switch in each joystick, I started by scraping the top of the metal button to ensure that there was exposed conductive metal, then crimping the leafspring against the button until that bit in the port went low (engaged).
I then pried the leafspring up little by little just until the bit went high (unengaged) and checked the switch's responsiveness with my finger, repeating as necessary. This at least got the VZ-300 sticks to respond as "good" as the VZ200's, which is to say somewhere between annoying and obnoxious, and that's all I have to say about that. If the sticks fail again and end up being unserviceable, I think I'll look into a way of connecting a Tutor or modified Atari stick here instead.
When reassembling the sticks, be sure that the square pin on the bottom of the plastic ring goes through the hole for it in the switch board, and that the central screw is tight (the whole thing is spring-loaded).
For completeness, here's the inside of the RAM expansion. Even though I don't think this was subject to FCC clearance, and certainly has no tag for it, the box is sheathed in a sheet metal cage as well. The case has ventilation holes top and bottom, covered with a bit of screening to filter junk, but I can't imagine they would have helped much if that cage ended up trapping heat.
On the PCB side, however, you can see what we need to see: eight footprints for, in this 16K expander, what must be 2K RAM chips. The TRM shows them as 4116 DRAMs. The rest of it, according to the schematics in the TRM, is two 74LS157 4-bit multiplexers for managing the address bus, a 74LS74 dual flip-flop, a 74LS123 monostable multivibrator, a 74LS32 quad-OR, a 74LS00 quad-NAND and a 74LS266 quad-exclusive NOR.
As we finish getting our system in order, there was one more modification I ended up doing out of concern for the workout I was giving its rocker power switch, especially when all I really wanted to do is merely reset the computer. (The BennVenn reader does not handle card re-insertion, even the same card, without a reset.) Like most CPUs of the time, the Z80 does not reset itself automatically when power is applied, so a small circuit in the VZ200 briefly pulls its reset line to ground when the power switch is first turned on. The length of time the reset line is grounded is determined by a single capacitor also connected on one side to ground. Once this capacitor fully charges, the reset line is pulled up to +5V and the chip continues operation.
Earlier VZ reset switches simply shorted this capacitor to discharge it, thus forcing the reset line to be grounded anew until the capacitor charged back up, and this particular modification was well-documented in Australian hobbyist magazines of the time. Unfortunately, although the TRM schematics label resistors and capacitors, the VZ200 board itself does not (or anything else), and the capacitor in question appears to have moved with the redesign of the board for PAL. I also couldn't think of a place to
put
the reset button, nor was I particularly enthusiastic about drilling a hole in the case to make one, first due to the questionable quality of the plastic itself and second for purposes of historical preservation of an unusual machine.
Happily we have another option, and it doesn't require altering the VZ200 at all: the expansion port itself has both reset and ground lines that go directly to the CPU. Recall from our wire-up of
a Gremlin Blasto arcade board
(where we had no reset circuit of any kind) that its 8080A CPU could be crudely reset by simply putting a pushbutton switch between its reset pin and ground. As the Z80 can serve as a drop-in upgrade for an 8080, it can be reset in the same way.
That means all we have to do is solder a pushbutton switch between the corresponding pins (i.e., pins 1 and 2) in the SD loader cartridge, in this orientation the farthest two from the SD card slot. One caution: don't get this backwards because even though pin 22 appears as N/C in the TRM, it's actually ground — and pin 21 is +5V.
However, not only do we have to modify the cartridge's case to make the switch accessible, but we also need to figure out some way of detaching the switch if we want to even open the case. For that, the wires I actually soldered to the pins go to two Dupont female jumpers. I then soldered the pushbutton to two Dupont male jumpers (polarity doesn't matter).
After that I drilled a second hole in the side of the cartridge case ...
... and threaded the female jumpers out through it.
Last but not least, we connect the male jumpers to them. If we need to get back into the case, we just pull off the button switch and reattach it after.
Our complete upgraded system, with cartridge, joysticks and reset button, is ready to go. (Perhaps a reset button feature could be considered for a future revision of the SD loader.) That makes it time for a little tour of the system — which is where another, less tractable problem with this particular unit will emerge shortly.
Meanwhile, let's put some files on the SD card and try them out. The firmware expects them to be in the more or less standard
.VZ
format, which has a trivial 24-byte header indicating filename, starting address and type (BASIC or binary). The
LOAD
command will conveniently auto-execute binary files when the load completes. You can find many programs on
Dave "Bushy" Maunder's exceptionally comprehensive site
containing software, photographs, articles and documentation, and most software he offers can be copied directly to the card and used immediately.
I started off with a converted copy of the demonstration cassette, which was written by VTech themselves and serves as a rather slight introduction to the system.
Although the individual files can be loaded from the SD card reader, it is not implemented as a cassette deck, so since each subsection of the demo is kept small to fit into a 4K VZ200, they will all soon try to load the next part and then just end up sitting there. At that point you must stop it with BREAK and manually load the next part, stored in numerical order.
Still, it's very friendly and welcoming to new computer users, including a nice little semigraphics picture as part of the sequence. Remember that VDG semigraphics, at least as configured on the Laser series, are at most one colour plus black in the same 2x2 cell, appearing when the high bit in text screen memory is set. Despite that limitation, with a little thought you can use it to make very striking displays as it is the only mode where every single colour can appear onscreen simultaneously (or black can appear at all).
Alternatively, another part of the demo is this slow but pretty bitmapped kaleidoscope. Besides text/semigraphics mode, the VZ200 has a simple 128x64 bitmapped display which consumes the entirety of the 2K VRAM. In this mode you get your choice of only two fixed four-colour palettes also selected by the 6847 CSS pin, neither of which is ideal, but at least every pixel can have its own colour. This particular display is drawn with the "pastels" (cyan, magenta and orange on a buff background) as opposed to a more garish one (red, blue and yellow on a green background). Notice that neither bitmap palette has black nor either of the alternate shades of green and orange.
A better measure of the hardware might be Five Finger Punch's
2018AD
. There's not much of a VZ200 demoscene, but there are a few out there, and this exceptional demo is unquestionably one of the best. It will not run correctly on this particular computer because the video timing is different — not because the clock speed is faster, like you'd see between an NTSC Commodore 64 which is faster than a PAL Commodore 64, but because the NTSC VDG draws the screen faster and thus fires the end-of-frame interrupt more often, messing up synchronization. For that, you'll just have to watch this YouTube recording on actual PAL hardware.
It's set up like a trackmo, streaming cassette program data from one channel of a specially recorded CD audio track and using the other channel for music (admittedly a bit of a cheat but the music is excellent). If you didn't think rotozooms, raster splits and even
FLD-type effects
were possible on the 6847 VDG, then you're in for a treat. Another neat trick is the doubled vertical resolution while drawing the Kefrens bars. The source code is even
available for your education
.
The VZ200 also had its various arcade ports. Some were higher quality than others. This is a commendable, but slow, ripoff of Moon Patrol ("Mars Patrol," by Grant Rowe) entirely done with semigraphics. It restores the old light-on-dark screen colours used in earlier ROMs with
POKE 30744,1
(this works with twiddling the CSS pin with
COLOR,1
also).
On the other hand, Hoppy is an above-average Frogger clone, and did the original one better by spreading the frog's journey over two screens. Hoppy came from the well-known duo of
Dubois and McNamara
(i.e., Greg Dubois and Tricia McNamara, though Greg did all the programming), who created various titles for a number of DSE systems that were sold in stores. I should note that for many games, including this one, the more-or-less standard control keys are Q and A for up and down, M and comma for left and right, and where a fire button is used, typically SHIFT (SPACE for secondary).
Note the "snow" in this shot — that's because the program was animating screen memory at the same time the VDG was trying to read it, so the VDG's memory access got briefly suppressed during that period. Because the display scan can't wait for the VDG to be enabled again, the result is a brief splat of garbage on that line until the VDG is allowed to proceed. Dubois could have simply waited for the VDG's next interframe interrupt, but there's also only so much time between frames before the VDG will start drawing again. As a result, for many programs where significant CPU time was required to do screen updates, outright ignoring the video artifacts turned out to be the least bad approach.
Here's a short video I recorded of another high quality arcade clone, Galaxon (gee, I wonder what
that was
) by Stephen Clarke. It shows loading from the SD card, the title and options screen (even the VZ200 had software pirates), and then playing the game, which worked fine on the keyboard. This and the other recordings I did for this entry were generated from the composite capture rig for video, but for audio using a microphone near the VZ200's piezo speaker to capture sound (since there's no audio out). You'll notice I'm pounding on the keys a bit, which the microphone faithfully picks up, though you do have to hit the keys with a bit of, shall we say, deliberateness to get them to register.
One of the more interesting games I ran across was Learjet, an IFR-style flight simulator drawn on the text screen. Here we are allegedly flying from Sydney to Melbourne, possibly because we don't know any better. When I get some time I want to figure this sim out a bit more because it seems quite sophisticated by 8-bit standards.
Of course, it wouldn't be a home computer without at least a token attempt at education. Here is a very Australian variation of
Lemonade Stand
: Meatpies, where you sell pies. Yes, the meaty kind, America.
Appropriately for a Four'n Twenty take on sugar-sweetened citrus beverages, you decide how many
glasses
pies you want to make, how many advertising signs you want to buy, and the price per item you want to request. Other than the pie business, Larry Taylor's port of the game seems to be heavily influenced by the well-known Apple II version and includes the same sort of simple graphics for weather reports and the like.
An exceptional entry in the VZ's edutainment canon is Factory by VSoftwareZ. It oozes professional quality with a slick title screen and menu, and is an extremely fun puzzler to boot. The aim is to create a factory from various primitive machines (paint, rotate, hole punch) that will generate a specific product. It is so well animated and so thoroughly polished that it deserves this short video to fully appreciate it.
Dubois and McNamara didn't just do games; one of their more ambitious projects was Wordpro for the VZ-300. You should refer to the
copious documentation
for all its features, as it was a surprisingly credible word processor on par with at least, say,
Color Scripsit
on the Tandy Color Computer, though Color Scripsit is some years older. Although Wordpro came as a cartridge intended for the VZ-300, it would work on a VZ-200 with correspondingly less document memory available, since it occupied the slot where the RAM expander would go. On the other hand, the program seems to be calibrated for a VZ-300 keyboard since on this VZ200 the keys seem to frequently stutter. (I'll talk about how I got it to work on this 4K system later, though it would not have been possible without the BennVenn RAM expansion.)
The visual resemblance between Wordpro and Color Scripsit —
see this emulation
— is also notable because the CoCo 1/2 and the VZ-200/300 all lack lowercase, so both programs solve it in the same way by displaying "capital letters" in reverse video. Wordpro's user interface is more sophisticated than Color Scripsit's, but it's also newer. The lack of a lowercase option on the VZ-300 was again a real missed opportunity, and with the number of machines DSE was buying you'd think they could have talked VTech into engineering a solution. Although Wordpro supports both disk and tape, the BennVenn cartridge currently doesn't emulate them sufficiently for Wordpro to use it. Perhaps this is a hack we can do some other time.
And of course a couple more games. Here is a simple Formula 1 racer (also by Stephen Clarke) a la
Night Driver
where you are apparently an alien with wings and feet ...
... alongside a rather good 3-D maze game by Laserlink. It's only rendered at 90 degree angles, but it's fast and well-written, and deserved another video.
Now, I mentioned there was another problem with the system.
Some
games, though many were fine, would show a weird line pattern over certain sections of the screen like this port of
Exidy Circus
/Midway Clowns. The pattern was annoying, but in the first few games I played where it manifested, it appeared to be cosmetic (it does not restrain the jumping figures here) and I initially chalked it up to some other undiscovered difference in this NTSC unit.
However, when I tried (Space) Invaders, it became clear it was not merely a video artifact but actual garbage in VRAM. Indeed, Invaders would detect collisions with it and accordingly send the alien force on a hyperdrive descent, making the game practically unplayable.
As it happens, the very problem was there all along in some of the previous screenshots and videos. Can you see it? Here, let me clear the hi-res screen for you:
One ... lousy ... stuck ... bit!
First let's understand why this was a problem for some games and not others. I am a 6502 dweeb of long standing and — hi Martin! — it is therefore excruciatingly painful for me to say anything at all nice about the Z80 (even though there's one in my beloved Commodore 128DCR), but one unquestionable strength is its block transfer instructions. As any schoolchild will tell you, six of the Z80's registers, B, C, D, E, H and L, can be turned into 16-bit counters BC, DE and HL which likewise can indicate addresses. The Z80 has an instruction
LDI
that copies the contents of the address referenced by HL to the contents of the address referenced by DE; the instructions
LDIR
and
LDDR
expand upon it, running
LDI
repeatedly and decrementing the count in BC each time until it reaches zero, respectively incrementing or decrementing HL/DE on every step.
The most obvious application for these instructions is copying a block of memory elsewhere, but a less obvious application is using them to
fill
memory. Consider this segment of actual code from Invaders (dumped with
z80dismblr
):
; Subroutine: Size=36, CC=1.
; Called by: LBL1[8254h], LBL4[8F3Bh].
; Calls: -
8C9E SUB40:
8C9E              ld   hl,7000h         ; 28672
8CA1              ld   (DATA47),hl      ; 8DCEh
8CA4              ld   de,7001h         ; 28673
8CA7              ld   bc,081Fh         ; 2079
8CAA              ld   (hl),00h         ; 0
8CAC              ldir
Ignoring the instruction at $8ca1, you can see that this is setting the source to $7000 — i.e., the start of VRAM — and the destination to $7001 (?!), for a total of $0820 bytes (the zero test is post-decrement). Now, what would
that
accomplish? Just before the
LDIR
, we set the contents of $7000 (in HL) to zero. Let's step through the process
LDIR
takes manually. $7000 is first copied to $7001, which is now zero as well. HL is incremented to $7001, DE to $7002, BC decremented to $081e. Next, $7001 is copied to $7002, but $7001 had zero in it because it was copied from $7000, so all three locations are now zero. HL is incremented to $7002, DE to $7003, BC decremented to $081d. Then, $7002 is copied to $7003, so now all four locations are zero, and so on, filling all intervening locations with the immediate value before. At the end, when BC finally gets to zero, all locations from $7000 to $781f inclusive (i.e., the entirety of video memory and a little past it in system RAM) will have been zeroed out.
This is how Invaders clears the hi-res screen and it is indeed faster than a naïve loop, especially for large tracts of memory. But our obnoxious little plastic beast here throws in a wrench by having a location where the RAM isn't working properly. When the "copy" gets to that point, because the copy is only between adjacent memory locations, for every subsequent location the stuck bit will be propagated forward and faithfully copied to each and every byte afterwards. That's also why the pattern doesn't cover the whole screen, because the problem doesn't actually manifest until the "copy" operation arrives there. In fact, in the process Invaders was unwittingly corrupting some of its own game variables with the same stuck bit when they should have been zero, possibly another reason why it wouldn't run correctly.
The direct and most definitive solution would be to "simply" replace the VRAM chip, and I even have 6116 SRAMs in stock, but I warned you this is a very cheaply made PCB. Far better repairpersons than I
have tried
and
failed
to replace chips on these computers without requiring a lot of rework and bodges, and the prior portions of this article should have already convinced you it's only by the grace of God I haven't soldered my own fool face to the workbench yet. I did
not
want to try replacing that SRAM chip solely because of one stinking bad bit; I was only likely to make a bigger mess or render the computer completely inoperable.
But again: we have an alternative. This fill trick was not universally used or even known by all programmers at the time. The games that do work clear the screen with a simple loop that doesn't propagate the bad bit forward, which works because the store doesn't depend on what memory contents are already "there." Likewise, VTech doesn't seem to use it in the ROMs, which is why the problem didn't manifest during the demonstration tape or with BASIC programs drawing to the screen with BASIC keywords. Most VZ programs are small enough and this code idiom distinctive enough (and usually only present once) that such code can be found and patched to use a slightly slower but functional loop. As such a loop would generally require more bytes, the patch could either direct execution to a tacked-on routine to do the clear, or we could patch it to point to a standard routine in memory.
And how are we going to get a standard, always-present, stock routine into memory to do that? Easy: we're going to soft-alter the BennVenn SD loader's firmware. No, stop laughing, because we have a simple means to accomplish it. At the same time we'll combine that with a serial port loader so that we can test these programs live without having to constantly swap the SD card to and from the Talos II, so we'll also build it a bitbanged serial port (I said stop laughing). There were homebrew serial devices back in the day for these computers, so consider this one merely another entry from a venerable tradition.
The programs that we'll write, including our replacement firmware, need to be in
.VZ
format. Here's a simple, complete example of "Hello World" showing how to construct that header and which can run directly from the card, demonstrated in the screenshot. This is one of several files you will find in
this article's Github repo
. As with all our assembler projects except for the 6502 and PowerPC, we crossbuild using
the Macroassembler AS
.
org 07fe8h              ; $8000 - $18
        ; emit .vz header (24 bytes)

        db 056h,05ah,046h,031h  ; "VZF1"
        db "HELLO\0\0\0\0\0\0\0\0\0\0\0\0" ; filename null terminated
        db 0f1h
        dw entry

entry   ; now at 8000h

        ld hl,msg
        call 028a7h
        ret

msg     db "HELLO WORLD", 13, 0
The 24-byte header marks this as a machine language program that starts at $8000, the beginning of the extra memory furnished by the BennVenn device. Although the magic number
VZF0
(for BASIC programs, which always start at $7ae9) or
VZF1
would appear to be critical, the firmware doesn't seem to check it on loading or even generate it on saving, only that the byte just before the starting address word (everything is Z80 little-endian) is either $f0 or $f1. Upon execution our program then calls a "display null-terminated string" routine in the VZ ROM, the update for which is pushed to the screen during the next VDG interframe period, and returns to BASIC. The binary is assembled with AS like so, using a simple
Makefile
:
% make hello.vz
asl -cpu z80 -t 2 -L hello.a80
Assembling hello.a80
PASS 1
hello.a80(17)
PASS 2
hello.a80(17)

0.00 seconds assembly time

     17 lines source file
      2 passes
      0 errors
      0 warnings
p2bin hello.p hello.vz
Deduced address range: 0x00007FE8-0x00008013
hello.p==>>hello.vz  (44 Bytes)
% xd hello.vz
00000000  56 5a 46 31 48 45 4c 4c  4f 00 00 00 00 00 00 00  |VZF1HELLO.......|
00000010  00 00 00 00 00 f1 00 80  21 07 80 cd a7 28 c9 48  |........!....(.H|
00000020  45 4c 4c 4f 20 57 4f 52  4c 44 0d 00              |ELLO WORLD..|
0000002c
We then copy it to the card, where
LOAD"HELLO"
will load and immediately execute it from the given entry address (which is both the load and execute address), as shown in the screenshot above.
Now we'll proceed with the hardware part, and we won't even need to solder anything from here on out, because we'll just use DuPont female jumpers to connect to the BennVenn GPIO pins we've already attached — everything else will be done in software. The SD card board uses 3.3V logic and has 24 GPIO pins that can be individually configured as inputs or outputs. These are all accessible through the Z80's I/O space, with locations 68-70 setting the data direction (1=input), and locations 71-73 setting the value of outputs. All pins can be read, not only pins configured as inputs, but also the current state of any output pins. The SD card board's GPIO pins provide +5V and +9V lines as well, but we won't be needing them for this project.
As an example, in
the Github repo
I have a small program to cycle the LEDs on his proto board, which you can see in this brief video. It sets all GPIO pins to output and lights all 24 green LEDs connected to them (the red ones are check LEDs for 3.3V, 5V and 9V), then cycles a dark one through them from left to right until a key is pressed. This is done by hooking into the interrupt routine called when the VDG completes a frame, the only regular timesource on an unaltered VZ200, and used back in the day as a simple clock by various programs. Every third tick of the interrupt routine, this code runs:
push ix
        and a           ; clear carry flag
        ld ix,scrby
        rl (ix)
        rl (ix+1)
        rl (ix+2)
        pop ix
        ld a,(scrby)
        ; put top bit back into low bit, if set
        jr nc, ledsout
        or 1
        ld (scrby),a
ledsout out (71),a
        ld a,(scrby+1)
        out (72),a
        ld a,(scrby+2)
        out (73),a
It rotates an in-memory image of the GPIO pin values, then emits that to the I/O locations. Because the rotation is to the left, we can see that the GPIO lines must also be oriented little-endian, i.e., the least significant bit of each GPIO output register is on the left.
This then informs how we'll set up our bitbanger. A half-duplex system will suffice for downloading, since the sender will wait for us to indicate receipt between packets, and that will let us concentrate entirely on receiving until a full packet is obtained. The absolutely fastest speed we can receive at is generally limited by how quickly we can clock data bits into an accumulator from the receive line. If we connect the receive line to the least-significant input of one of the GPIO registers (we'll use the leftmost for convenience), we can do it in 23 cycles:
getabit MACRO
        in b,(71)       ; 11 cycles
        rr b            ; 8 cycles (rotate b bit 1 into carry)
        rra             ; 4 cycles (rotate carry into a little-endian)
                        ; = 23 cycles
        endm
The Z80's clock speed (in any of these systems) does not neatly divide into any standard bitrate, but theoretically 23 cycles per bit gives us a maximum possible transfer speed of ((315 000 000/88)/23) =~ 155632.4 bits per second. That suggests you might be able to get 115200bps with an unrolled loop, but at speeds this fast time required for other tasks starts to be a concern, such as storing to memory, checking how many bytes have been received, and branching back to get another, all of which together will certainly be more than 23 cycles.
The other problem is the time required to sense the start bit, because this can occur at any moment, and hardware UARTs generally end up repeatedly snooping the line at some multiple of the bitrate to ensure they won't miss one. We, on the other hand, can't even check for a start bit at just
twice
115200bps. In fact, the fastest we can check for a start bit (a zero) is
startbt in a,(71)       ; 11 cycles
        rra             ; 4 cycles
        jp c,startbt    ; 10 cycles taken or not
                        ; = 25 cycles
which because of the unavoidable branch is actually longer than the time to clock in a data bit!
However, these numbers
do
suggest that
half
that speed, i.e., 57600bps, is plausible. Flipping the equation around, that gives us a relatively generous ((315 000 000/88)/57600) =~ 62.1 cycles per bit, long enough to do our housekeeping tasks on each byte, and our tight startbit loop can poll the line at ((315 000 000/88)/25) =~ 143181.8 bits per second (a familiar number to some of you), which is at least twice the data rate and should be sufficient for the sort of continuous data transfer we'd experience receiving a data packet. We will target this speed. (Note from the future: an early draft used
in a,(c)
in the startbit loop, which is a 12-cycle instruction. This single extra cycle reduced the startbit poll rate to 137674.8bps, and at that speed multiple bytes got missed and/or corrupted. We are probably only
just
fast enough to make this work.)
Parenthetically, VZ-300 owners in the audience will now have asked if this will work for them. If we substitute its lower clock speed at 57600bps, we get ((17734475/5)/57600) =~ 61.5 cycles per data bit and a maximum startbit poll rate of ((17734475/5)/25) == 141875.8 bits per second exactly. Because you can sample a little bit faster but never slower, we would need a separate version for the VZ-300; the same code will not work reliably on both. Sorry! That will be the subject of
a future article
.
Note that by making receive fast, we made transmit slower: unless we occupy the least-significant bit of another GPIO register, which seems rather wasteful, the next fastest position is the second-to-least significant bit. This snippet needs no less than 31 cycles to send the next bit of a character stored in a register other than the accumulator (here we'll use B):
putbit  MACRO
        xor a           ; clear accumulator and flags (4 cycles)
        rr b            ; rotate low bit into carry (8)
        rla             ; rotate carry into low bit (4)
        rla             ; rotate up one more bit (carry must be zero) (4)
        out (71),a      ; 11 cycles
                        ; = 31 cycles
        endm
If we had to completely guard that GPIO register from interfering with any other GPIO pins on the same register, it would be even longer because we would need to read the current state and then do the bitmasks. Mercifully we'll just refuse to support that, and as 31 cycles is still well within our 62 cycle maximum per bit, she'll be right.
Now that we've gamed out how we'll connect our serial wires, we next need to figure out which pin on the BennVenn expansion header goes with which GPIO line. As I mentioned earlier, a minor gripe is that the lines are not necessarily wired in order, so it's a good idea to verify what pin is where. This is again most easily done with one of Ben's proto boards because you can continuity-test the back of the pin connector and any of the pin rows to see how they are connected (or, if you want, just wire directly to the marked lines on the proto board itself, but the angle makes it a bit less elegant). Find ground, then find pins one and two. I marked my findings with a
Texta
Sharpie.
If you don't have his board, you can still figure it out a little less conveniently with a voltmeter. Ensure all pins are set to output and turned off (something like
FORI=68TO73:OUTI,0:NEXT
will do from BASIC). The only live lines at that point should be ground, 3.3V, 5V and 9V. Find ground first, which you might do by checking for continuity with the ground test point Ben provides on the board, then use that as your common to find the voltage pins. Mark those; the rest are GPIO. Turn on pins one and two individually (
OUT 71,1
or
OUT 71,2
) and look for voltage.
Having done so, our serial port will be the very cheap, easily available and extremely flexible HW-597 USB-to-TTL converter, based on the CH340. There are buckets of these things on eBay from many manufacturers and they quietly reproduce in my desk drawer like hamsters. Which I don't mind, because it works at 3.3V or 5V, it connects to your host directly with USB, and pretty much every modern operating system has built-in drivers for it (at least both my M1 MacBook Air and my Raptor Talos II running Fedora do). Jumper it for 3.3V operation as shown here, then connect the ground to the ground pin, transmit — relative to the host, not the VZ200 — to pin 1, and receive to pin 2. This is how the wiring looks on mine.
Since we will be drawing power from the connected host and not the BennVenn,
don't
connect the 3.3V line. Instead, for the programs below, ensure the HW-597 is already plugged into your host (such as with a USB extension cable) and showing bright status LEDs before powering on the VZ-200, or it may try to unsuccessfully power itself from the other lines and get a little daft.
To test your connection, a simple program in the Github repo (
BITS
) toggles the screen colour as it sees activity on the receive line. This is easiest to watch at a slow bit speed of around 150 baud or so. Here, I hooked it up to the Talos II, ran
picocom -b150 /dev/ttyUSB0
(adjust for the path to your device), and just banged on the T2's keyboard. If you get alternating flashes of green and orange on the VZ while you do so, then your receive line at least has basic connectivity.
A more thorough test is now to accept entire bytes. This program displays any byte it gets from the receive line (
ASCII
), effectively one half of a very slow terminal program. We'll use the internal ROM routine to display a character, which will get us scrolling for free, and then force the update instead of waiting for the next IRQ — which is disabled anyway to make sure our timing remains precise. (Typing only upper case characters works; lower case shows as symbols.)
This program runs at a sedate 300bps, and the reason is because the VZ ROMs are written for space efficiency, not time efficiency, at least to any extent they're efficient at all. 300 baud gives us an apparent surfeit of cycles using our formula — 11931 cycles per bit — but we may well need all of them since we've really got no idea how long it can take the ROM routines to do any arbitrary screen update. We won't be using the ROM much for our data blaster program, but a general purpose terminal emulator would have to consider a proper solution to achieve faster speeds. This is something else we might revisit in
a future article
.
The other purpose of this ASCII test program is to mock up how we'll write the fast serial loader. Despite the fact we have over 10,000 cycles between bits at 300bps and could easily have written each bit we read as a subroutine call to save memory, I still inlined each clocked-in bit using a macro because we necessarily need to at 57.6kbps — among other things, each
CALL
is 17 cycles and the
RET
to return from it is 10, which would consume almost half our CPU budget by themselves. I'd also like to observe, again with my usual biases showing, that cycle counting isn't nearly as much fun on the Z80 as it is on the 6502. Most opcode tables will fortunately collapse the whole Z80 T-state and M-state business into a single unified cycle count, but unlike the 6502 where there are instructions with execution times of 2, 3, 4, 5, 6 or 7 cycles (so you can easily make a busywait from any combination), the Z80's cycle time options start at 4 and go as high as 23, skipping many numbers, and many of the smaller cycle times require specific conditions like not taking a branch. Having considered our little half-terminal program, here's what I settled on for 57.6kbps, written as AS macros:
getabit MACRO
        in b,(c)        ; 12 cycles
        rr b            ; 8 cycles (rotate b bit 1 into carry)
        rra             ; 4 cycles (rotate carry into a little-endian)
                        ; = 24 cycles
        endm

topwait MACRO
        ld (ix+0),b     ; 19 cycles
        endm

botwait MACRO
        topwait
        endm

getbit  MACRO
        topwait
        getabit
        botwait
        ; 19 + 24 + 19 = 62
        endm
From our previous maximal case I turned the
in b,NN
instruction into a slightly slower
in b,(c)
, which burns an additional cycle, but means we have 38 cycles left over of our 62 which we can split exactly between two
ld (ix+N),b
instructions of 19 cycles each. (This also lets us possibly alternate between multiple connected serial devices by changing C, but one catastrophe at a time, I always say.) The separate top and bottom waits are for situations where we have an odd number of cycles left over and need to have different wait times; consider this future expansion for the VZ-300.
When the stop bit arrives, we need to dump the byte into a buffer and get ready for the next one in the same 62 cycles, since we expect the other end will be ready to fire the next start bit at us immediately. To make an interesting and vaguely useful display (as well as not requiring additional memory), the screen itself would seem like a good place, but this also imposes some constraints: we only have 512 bytes there (i.e., 32x16), some of which we also need for indicating status, meaning our received packets should really be no larger than 256 or 384 bytes to allow for a transmission log and other useful info. The protocol we select should have packets no larger than that, be easy to implement (because I'm lazy), and be something that pretty much everything can speak. While we've seen Xmodem-1K or Xmodem-CRC implemented other places (like
The Newsroom's Wire Service
variant), I just decided to go with good old O.G. Xmodem. That contains 132-byte packets and is easy to write and checksum, and any errors over USB between your host computer and the VZ200 would undoubtedly be from bad bit framing rather than line noise which the default checksum algorithm should detect. While it overruns memory a bit at the end, this is largely irrelevant for just loading something we intend to immediately execute.
All that preamble yields us a stop bit stanza like this:
; stow character in screen buffer during stop bit time
        ; unfortunately we don't have enough cycle headroom to do
        ; a running checksum, so we have to do it after the fact
        ld (ix+0),a     ; 19 cycles
        ld (ix+0),a     ; 19 cycles
        inc ix          ; 10 cycles
        dec l           ; 4 cycles
        jp nz,datapak   ; 10 cycles
        ; 19 + 19 + 10 + 4 + 10 = 62
Here we use the IX index register as a pointer into screen memory and the L register as the packet length countdown. A double-store of the same location onscreen once again soaks up 38 cycles, then the increment and decrement, then the branch. A nice thing about the
JP
instruction, which is absolute instead of relative, is that the conditional branch form requires 10 cycles regardless of whether it's taken or not, so this entire stanza always consumes precisely 62 cycles as well. We use that instruction a lot in the cycle-exact portions so that we always have predictable CPU time.
Once we get a full packet, we know the sender won't do anything until we reply, so we can relax our timing and validate the packet at leisure, copy it into the correct place in memory and send the ACK for the next one. We send bytes using the same send-bit route I showed you before or a trivial variation, padded to 62 cycles per bit and also inlined. We accept
.VZ
-format files in this loader, so we have special handling for the first packet to make sure it has a generally correct format and note the type and memory address, which is where the rest of this packet and subsequent packets will be copied to. If it doesn't, then we send CAN and force the sender to abort.
By contrast, the start bit is handled with the same 25-cycle code I showed you before, because this is the fastest way we can be sure we won't miss one. But this also means we have no way of checking the keyboard nor implementing a timeout: there is no spare time to count cycles or scan for keys, and the only free-running timer is the VDG end-of-frame IRQ which will totally mess up our timing if that runs, so during the entire transaction IRQs are disabled as well. The program therefore assumes your sender is up and ready to go the moment it starts executing. On startup it fires off the initial NAK and waits, possibly forever if the other end never gets the signal until you reset the VZ200. (We display a message to alert you that no transmission has yet been received, which is immediately overwritten on-screen by the
.VZ
metadata.)
Let's see our loader in action. On the host side, to send the program to the VZ200 you can use any terminal program that speaks Xmodem (and just about everything does), just as long as it automatically starts the transfer as soon as the initial NAK arrives. With both my MacBook Air laptop and my Raptor Talos II workstation, I use
lsx
with the
usb2ppp
tool from
BURLAP
, which we earlier used to tunnel PPP over a serial line for
the Brother GeoBook
, but can be used to run pretty much
any
program over a serial port. Here's an example, substituting the path to the HW-597 that your machine uses (e.g., Fedora Linux on my Raptor Talos II uses
/dev/ttyUSB0
):
% usb2ppp /dev/cu.usbserial-110 57600 lsx -b ascii.vz
opening /dev/cu.usbserial-110
setting up for serial access
setting flags on serial port fd=3
starting process lsx
subprocess pid= 64301
Sending ascii.vz, 2 blocks: Give your local XMODEM receive command now.
We start the loader, which you can run as a separate program on its own and it will load anything that does not encroach on its default location at $e000. (We'll find an even better spot for it in just a minute.) Since our ASCII half-terminal program loads and executes from $8000, this is no problem; it takes up three blocks (there's apparently an off-by-one bug in
lsx
), so it's a good quick test of the machinery. The loader immediately sends NAK and we're off to the races.
Since we're assaulting screen memory every 62 cycles without regard for the VDG, there are accordingly "snow" artifacts everywhere, but we don't (and indeed can't) care. We have read our metadata, which we display on the top line (file type and starting address). Below that onscreen is an image of the current packet followed by a connection log of dots for successfully validated packets or an X for one that failed. This is a grab from a much longer transfer but it gives you the general idea. At the end of transmission, we automatically execute the file if it's a binary, or print a
RUN
you can just hit RETURN on to run a BASIC program.
Bytes Sent:    384   BPS:20                              

Transfer complete
subprocess terminated
restoring terminal settings
Ta-daaaaa!
In memory of Dick Smith's food company I've christened it the BFL, short for Bush Food Loader, a joke I otherwise refuse to explain (image from
The Australian
, paywalled link).
Now we want to make it part of the system. To convert it to "firmware" takes advantage of a specific feature Ben built into the SD card reader for easier updates: the ability to load and run a new system "ROM" directly from the card.
The default memory map for the VZ200 puts the system ROMs between $0000 and $3fff, reserving the space from $4000 to $67ff for ROM cartridges, though a cartridge could technically take over any address range above the TOM (that's how the RAM expanders worked, after all), and we'll come back to that point later. For the system to recognize code at $4000 or $6000 as part of a cartridge, a sequence $aa $55 $e7 $18 is required in that order, and execution then starts at $4004 or $6004. As shipped to you Ben's device not only fills in RAM above the TOM, it also fills RAM in from $4000 to $67ff and puts its own code there with that sequence, effectively "slushware" (a la
the DECmate II
, and we'll use the same term here since it's not really ROM). This code is run by the system ROM on startup like a "cartridge," because that's what it looks like to the system ROM, and this code is what does the RAM test and initializes SD card access. Once the system is up, it then does this:
The file
VZDOS.VZ
it's loading from the card is "magic." If present, it will be used to temporarily replace the slushware at runtime; for a couple extra seconds spent loading it you don't have to mess around with burning it to the cartridge. But this binary is not signed or checksummed, nor does the load check if it's even a new copy of the slushware — any program will serve as long as the
.VZ
header loads it to $8000 but the code is written to execute from $4004 (as the onboard image would). The slushware then places a little trampoline copy routine at $a000 and runs that to copy the 8K from $8000 to $9fff to $4000, overwriting the old slushware, and jump into the new one.
To make our replacement code useful, we should provide some quality-of-life features. We'll make it autostart into a transfer so that all you have to do is load up the program into your Xmodem sender and reset the VZ200, and after a polite delay it will pull down and run the program automatically. We'll also let you load multiple times if you want instead of immediately trying to execute the current file being transferred. We'll also finally put that routine in memory for the slower but more forgiving memory fill operation, and enable the VZ sticks by default in case we find something that really needs them. But more important than those, we should also let you drop back into BASIC and use the SD card loader normally without having to pop the card out. That requires us to include a copy of the
actual
VZDOS.VZ
which we will embed in our replacement code.
This adds an additional complication, because the 2.32 slushware (the most current as of this writing) is already 8068 bytes long minus the
.VZ
header, leaving us only a little over 2K for our own code. Moreover, if we're over 8192 bytes (and it's inevitable we will be), the loading process will overwrite at least 100 bytes of our code with the trampoline and fail to copy the rest. We'll solve this by immediately copying the remainder as the first step in our binary, and then post-processing the object to yield a new
VZDOS.VZ
with a 128 byte hole between the first 8K and the last 2K (remember it gets loaded to $8000, so we have plenty of space
there
). Part of this code will be used to make a jump table entry for our slower fill so the call will stay constant with future updates, if any. That looks like this:
di
        jp uentry
        ; any jump table entries we want should go here, and then be
        ; pulled out from VZDOS's offset below
        jp sloclr       ; slow hires clear for bad video RAM

        ; include original VZDOS but jump to our code
        ; start at a different offset, skipping the first three
        ; instructions which are never called again, so we can do them
        ; elsewhere
        binclude "vzdos.vz_232", 35

uentry  ;;; this code must all be under the 8K mark ;;;

        ; copy remaining 2K from its "safe" location + 128
        ld hl,0a080h
        ld de,06000h
        ld bc,00800h
        ldir

uentryb ;;; end code that must be under the 8K mark ;;;
        ; ensure ROM reloads
        ld a,0
        ld (08000h),a
        ; patch our VZDOS to not try to reload itself
        ld a,201        ; "ret"
        ld (04046h),a   ; only valid for 2.32
Since we are embedding VZDOS but we need to keep all its relative offsets intact, we skip the first 7 bytes and the
.VZ
header, and run those instructions later just before we jump back into it (if we do). We also do a couple patches so that VZDOS will reload (us) on a reset, but not when we execute the embedded copy, and still use an unmodified 2.32 so that you can see there's nothing up my sleeve.
Time for our fill routine.
; acts like ldir but does it manually (assume hl, de, bc set, and
        ; byte is in a). save the byte somewhere! don't save it in VRAM!
sloclr  ld (slobyte),a
sloclrl ld (hl),a
        inc de          ; make it real
        inc hl
        ld (hl),a       ; double store to emulate 7000->7001, etc.
        dec bc
        ld a,c
        or b
        ld a,(slobyte)  ; flags kept 
        jr nz,sloclrl
        ret
This is pretty simple-minded, but it works. We stash the fill byte somewhere
not
in VRAM, then do everything
LDIR
would and leave the routine with A, HL, DE and BC set as they would be at the end. (We do set the Z flag on exit, but most routines won't care about this.) Then our Invaders example, which was
; Subroutine: Size=36, CC=1.
; Called by: LBL1[8254h], LBL4[8F3Bh].
; Calls: -
8C9E SUB40:
8C9E              ld   hl,7000h         ; 28672
8CA1              ld   (DATA47),hl      ; 8DCEh
8CA4              ld   de,7001h         ; 28673
8CA7              ld   bc,081Fh         ; 2079
8CAA              ld   (hl),00h         ; 0
8CAC              ldir        
8CAE              xor  a
can be patched by overwriting the two instructions at $8caa with
ld a,0:call 04008h
.
Ta-daaaaa! (In fact, since A is preserved, we don't even need the
xor a
and could just
nop
it.)
Now, I'll note that this isn't foolproof. One interesting case is Super Snake, written for DSE by "S. Bjelic" (I couldn't cursorily find out more about this person), who also did Invaders and a number of other software releases for DSE under contract.
The game mostly plays properly
except
scrolling the attract-mode screen, because unavoidably we'll scroll up the stuck bit. I don't think there's a good general way around that. Fortunately it's purely cosmetic, and most games I converted in this fashion seemed to work fine without any glitches.
For its last bit of polish, let's give it a nice menu screen when it autostarts. You get around three seconds before it goes into the automatic load sequence (slightly less on an NTSC VZ200 because we use the end-of-frame IRQ to count, and the program can't tell the difference), but any key will interrupt it. You can also immediately (L)oad, return to (B)ASIC by jumping into VZDOS, or toggle VZ (J)oysticks or whether the program auto-e(X)ecutes.
We'll now create that loadable version of Wordpro as a useful hack and stress test, which by being over 96 blocks should unmask any insidious framing errors in BFL caused by long transfer drift. (The resulting
WORDPRO.VZ
can also be placed on the card and run from there as we did previously, though doing so doesn't enable file operations either.) You'll need copies of the actual ROMs, which do circulate. The entirety of the code — really a disguised linker script — looks like this:
org 07fe8h
        ; emit .vz header (24 bytes)

        db 056h,05ah,046h,031h  ; "VZF1"
        db "WORDPRO\0\0\0\0\0\0\0\0\0\0" ; filename null terminated
        db 0f1h
        dw entry

entry   ; copy code to 6000h and d000h
        ld hl,rom1
        ld de,06000h
        ld bc,0800h
        ldir

        ld hl,rom1
        ld de,0d000h
        ld bc,03000h
        ldir

        jp 06004h

rom1    binclude "vtech_wordpro/wordpro.u3"
rom2    binclude "vtech_wordpro/wordpro.u4"
rom3    binclude "vtech_wordpro/wordpro.u5"
Remember that Wordpro was first and foremost written for the VZ-300, which has 16K of RAM, so its TOM is much higher ($b7ff). The cartridge, because it has full control of the bus, thus maps its much larger ROM in at $d000-$ffff, with 2K of $d000 also mapped to $6000 with the cartridge header sequence. This echo of the main cartridge ROM is what actually autostarts everything since the system ROM doesn't know to check anywhere else but $4000 and $6000. The same scheme works for the VZ-200, except there is no RAM between $9000 and $bfff.
But with the BennVenn cartridge, we have RAM
everywhere
, so we load to $8000 and copy the Wordpro ROM dumps upon execution to their proper location(s), duplicating $d000-$d7ff to $6000-$67ff like a real one, and jump into the "cartridge" at $6004. This copy operation will destroy BFL-the-slushware, but we can just reset to reload it. Wordpro will get all the RAM it would expect to get on a VZ-300, even on this 4K VZ200.
To verify operation, I also tested it on my Dick Smith VZ-200 as shown here, alternating between the VZ200 and VZ-200 using both macOS and Linux as the host, and using different HW-597-type dongles in my parts drawer. It all seemed to work and I think it will work for you. Downloads at the end.
Now that we can iterate quickly on them, let's patch and play a few more games before we close.
Another outstanding edutainment title is Maths Armada (not Math Armada, which my wife would insists is patentlys incorrects), where you have to load your cannon with the right sum, quotient, etc., aim, and fire. In the video we autoload the new binary with the BFL and the game starts immediately. This one I had to tack on a custom routine; the programmer had been a little
too
efficient and constructed a general fill subroutine which lots of things called, the screen clear portion being only one of many. (Darn those efficient little assembly language programmers.)
Here's a Pac-Man clone this time, another Dubois and McNamara release slightly improbably called Ghost Hunter.
Continuing in that vein is a clone of Burger Time ("
we are closed now!
"), one of my favourite Intellivision titles, given a solid conversion as Hamburger Sam also by D&M.
More recently, Juergen Buchmueller's Defense Command is sort of like a vertical Defender (complete with descending aliens trying to harvest your brood), though it has a curious game deficiency in that the side-to-side entering attackers need never be shot, so you can enter an eternal stalemate by merely sitting there. Still, the action is fast and the animations, albeit small, are decent. This game was written in C using an earlier version of the
Z88 Development Kit
.
Another Z88DK game is
Arkaball by Jason Oakley
, an obvious Arkanoid clone, but competently crafted and worth a video.
Finally, a much more modern game is (the vibecoded)
VZ-DOOM
, a Claude-written raycast Wolfenstein 3D-style game. It fortunately didn't need patching and "just worked." Your mileage may vary as to whether you think the AI usage is cheating, and this blog has a strict no-AI-article-text policy, but it performs as advertised on this NTSC machine and likewise merits a video. VZ-DOOM uses WASD for motion, comma and period to strafe, E to open and SPACE to shoot.
I think that's quite enough for our first foray into the ZWonderful ZWorld of the VZ, so let's finish the history as we customarily do. While
VTech items continued to show up
in Dick Smith stores, and VTech did make other Laser computers, these "later Lasers" were not closely related nor compatible with the VZ line, or each other, and most of them were much less successful — with the exception of their Apple II clones. The Laser 3000, fresh from its Summer CES 1983 debut, also made it down under to Dick Smith stores as the
Dick Smith Cat
. It required real Apple II ROMs in an external cartridge for compatibility, which also made it a target for Apple, fresh off
their successful victory against Franklin Computer
for using substantial portions of the Apple II ROM in the Franklin Ace 1000. Although VTech was still able to sell it elsewhere and the Apple II ROMs were never integrated into the base machine, Apple instead argued that the mere
use
of the ROMs was an infringement upon its intellectual property regardless, and successfully blocked further imports to the United States.
VTech learned from this just like they learned from EACA, and developed new ROMs that were carefully clean-room reverse-engineered, additionally incorporating a licensed copy of Microsoft BASIC retrofitted to act like Applesoft BASIC. This process provided the legal assurance that not a nybble of Apple's code was even consulted, and VTech used these unencumbered ROMs to create what was introduced at Summer CES 1985 as a redesigned "90% compatible" (per
Creative Computing
) Laser 3000. In turn, that reworked Laser 3000 was transformed into the 1986 Laser 128, a semi-portable riff on the Apple IIe with an expansion slot and built-in 5.25" floppy (later 3.5"). VTech's work paid off handsomely: reviewers were impressed by its value for money, most software never noticed the difference, and Apple's repeated attempts to prevent its importation and sale all ended in failure. The Laser 128 family's low price and exceptional built-in functionality made them the most widely sold Apple II clones in the United States, finishing on the market as late as 1989 in an upgraded 3.6MHz version with a 3.5" disk drive and over 1MB of RAM.
By then, however, the world had moved on from the 8-bits as general purpose computers, and so had VTech, parlaying its experience with the Z80 once again into inexpensive toys and games like the Socrates while turning their explicit computer brand toward the clone Laser PC. Likewise, although Tandy Radio Shack still sold the CoCo 3 and the final incarnations of the original TRS-80, it too was quickly transitioning to more lucrative PC clones like its Tandy 1000 family which it advertised prominently. DSE did much the same, still offering the VZ-300 to budget users, but otherwise more aggressively positioning other PC clones as an OEM reseller. Unlike Tandy, at least initially DSE did not further develop nor rebadge them as a house line and they were typically sold under the manufacturer, the most prominent being Taiwanese system builder Multitech. The machines shown here in my 1987-88 catalogue were among the last to bear that name before the company reformulated under a new brand still used today: Acer.
At DSE Jim Rowe left the company and after a brief stint at Microbee eventually
returned to journalism
in 1987. Meanwhile, DSE was still selling enough VZ-300s to keep them in this 1987-88 catalogue, and according to Greg Dubois' contacts at Dick Smith even at that late date they continued moving over 100,000 units a year, but in the end it was actually VTech that wanted out: VTech wanted to redirect factory capacity to the Laser PC and wasn't willing to keep producing the older system, and even DSE's offer to double the order couldn't convince them otherwise. Although some software and accessories still appeared in the 1989-90 catalogue, the computer itself did not, and the line disappeared completely by 1991. For a time afterwards DSE sold IBM consumer PCs and even Commodore PC clones in the process of adopting its own DSX PC brand.
In the 2000s the company failed to make a successful transition from its mail order origins to the new world of online sales, and despite several attempts to rework its retail presence Woolworths unloaded Dick Smith to Anchorage Capital Partners in 2012 in a controversial deal where much of the sale price was allegedly financed by Anchorage liquidating DSE's own assets. Anchorage took the company public in 2013, netting tens of millions, but the company did not recover and all 363 remaining stores were closed by May 2016. Today the Dick Smith brand lives on
solely as a mark
of online retailer Kogan, primarily selling consumer electronics.
The DSE VZ-200 may have been a crap home computer too, but it was
Australia's
crap home computer, by golly. Much as Sinclair did in the UK and Commodore in the United States, the Aussie VZ-200 and its successor VZ-300 remain as beloved as they are because they introduced a entire generation of Australians to computers who could never buy one before. While a few importers tried to bring the also-rans to the South Pacific (DSE even had Radofin's undead zombie Aquarius in their 1985 catalogue!), the VZ was there first and in large numbers, over 20,000 VZ-200s alone, becoming the down-under standard against which all subsequent cheapo systems were measured. Indeed, when the desperately dire Tandy MC-10 got in front of
Australian Personal Computer
in December 1983, reviewer Surya commented that when considering it versus the VZ-200 "the MC-10 does not stand up well to this comparison." Legions of user groups and newsletters sprung up to support it, tinkerers designed all manner of expansions for it, and users wrote and sold their own software for it, ironically spawning exactly the sort of hobbyist-driven computer ecosystem post-Dick Smith that Dick Smith-era Dick Smith had previously tried to foster. Ultimately the little Hong Kong desk wedge became more of an Australian computer icon than even some truly homegrown ones.
As for this NTSC VZ200, it should be very possible to clone it because the ROMs are the same as the better-known DSE flavour and it's otherwise all off-the-shelf hardware; moreover, it would be infinitely easier to maintain and repair than the ghastly PCB it's got now. The schematics for the PAL Dick Smiths are widely available and there are even fewer components needed to build an NTSC one. At least one person has already made
an NTSC-compatible RC2014 workalike
, though that project uses a GAL, and it seems like we could make a more straightforward knockoff just using what the original did — with the exception of the colour encoder, which would be improved and somewhat simplified by using a proper MC1372 instead of the TBA520. I know "Leaded Solder" Mike has
his clone CreatiVision
, so I look forward to him picking this up as a new challenge. ;)
We'll be doing more with this system and particularly the VZ-300, now safely awaiting my next Southern Hemisphere trip, in
future articles
— along with a recently-acquired PAL CreatiVision of our own, the basis for the Dick Smith Wizzard, which we need to see if we can get up and running (I do like me a 6502 and a 9918). Meanwhile,
David "Bushy" Maunder's VZ website
can give you all the articles, technical information and software that you can
stick on an SD card
.
Just remember: you can never trust anyone mixing tea and solder.
The programs we wrote for this article and their assembler source code
are all on Github
, including
pre-built binaries
and ready-to-go Bush Food Loader "slushware" you can use with your own SD card loader, all of which are under the BSD 2-clause license.
