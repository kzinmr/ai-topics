---
title: "Reverse-engineering Roadsearch Plus, or, roadgeeking with an 8-bit CPU"
url: "https://oldvcr.blogspot.com/2025/08/make-your-apple-ii-or-commodore-64.html"
fetched_at: 2026-04-30T07:01:18.723941+00:00
source: "oldvcr.blogspot.com"
tags: [blog, raw]
---

# Reverse-engineering Roadsearch Plus, or, roadgeeking with an 8-bit CPU

Source: https://oldvcr.blogspot.com/2025/08/make-your-apple-ii-or-commodore-64.html

Sorry, Doc Brown: we still needed roads in 1985. That meant paper atlases and misfolded roadmaps and a lot of stereotypical male anxiety asking for directions. Fortunately, in 1985, this problem also had a solution.
Yes, if your car inverter could handle a 45-ish watt load — and your wife doesn't want her seat back right away — you could navigate major routes across America on your home computer like this portable Commodore SX-64. I particularly enjoyed writing this article because my
other
irredeemably nerdy habit is roadgeeking, exploring and mapping highways both old and new, and it turns out that 8-bit roadgeeking on ordinary home computers was absolutely possible.
For computers of this class, devising an optimal highway route becomes an exercise not only in how to encode sufficient map data to a floppy disk, but also performing efficient graph traversal with limited hardware. Today we'll explore Roadsearch-Plus, one of the (if not the) earliest such software — primarily on the Commodore 64, but originating on the Apple II — and at the end "drive" all the way from southern California to British Columbia along US Highway 395, my first long haul expedition, but as it was in 1985. Buckle up while we crack the program's runtime library, extract its database, and (working code included) dive deeply into the quickest ways to go from A to B using a contemporary home computer.
Although this article assumes a little bit of familiarity with the United States highway system, I'll provide a 30-second version. The top-tier national highway network is the 1956
Eisenhower Interstate System
(abbreviated I-, such as I-95), named for president Dwight D. Eisenhower who promulgated it, signed with red, white and blue shields. Nearly all of its alignments, which is to say the physical roads composing it, are grade-separated full freeway. It has come to eclipse the 1926
United States Numbered Highway System
(abbreviated US, such as US 395), a nationally-numbered grid system of highways maintained by the states, albeit frequently with federal funding. Signed using a horned white shield, these roads vary from two-lane highway all the way to full freeway and may be multiplexed (i.e., multiply signed) with other US highways or Interstates in many areas. While they are no longer the highest class of U.S. national road, they nevertheless remain very important for regional links especially in those areas that Interstates don't service. States and counties maintain their own locally allocated highway systems in parallel.
Here is a glossary
of these and other roadgeek terms.
Geographic information systems (GIS) started appearing in the 1960s, after Waldo Tobler's 1959 "Automation and Cartography" paper about his experience with the military Semi-Autographic Ground Environment system. SAGE OA-1008 displays relied on map transparencies developed manually but printed with computers like the IBM 704. Initially such systems contained only geographic features like terrain and coastlines and specific points of interest, but support for highways as a layer or integral component was rapidly implemented for land use applications, and such support became part of most, if not all, mainframe and minicomputer GIS systems by the late 1970s. However, these systems generally only handled highways as one of many resource or entity types; rarely were there specific means of using them for navigational purposes.
Quite possibly the first consumer-level computer for highway navigation was the 1981
Honda Electro-Gyrocator
. Because Global Positioning System (GPS) satellite data was not then available for civilian applications and other radio navigational systems like LoRAN were hard to reliably receive in canyons or tunnels, it relied on its own internal gas gyroscope to detect rotation and movement aided by a servo in the car's transmission. The Electro-Gyrocator used a Texas Instruments TMS9980 (a derivative of the 16-bit TMS9900 in the TI-99/4A but with an 8-bit data bus) as its CPU and a sidecar TMS9901 for I/O. It had 10K of ROM, 1K of SRAM and 16K of DRAM, hopeless for storing map data of any consequence, so the actual maps were transparencies too; the 9980 integrated sensor data provided by the 9901 from the gyroscope and servo to plot the car's course on a small 6" CRT behind the map overlay. The user was expected to set the starting location on the map before driving and there was likewise no provision for routing. It was only made available that year for ¥300,000 (about US$2900 in 2025 dollars at current exchange rates) on the JDM Honda Accord and Honda Vigor, and discontinued by 1982.
There were also a few early roadgeek-oriented computer and console games, which I distinguish from more typical circuit or cross-country racers by an attempt to base them on real (not fictional) roads with actual geography. One I remember vividly was Imagic's
Truckin'
, a Mattel Intellivision-exclusive game from 1983 which we played on
our Tandyvision One
.
To the best I can determine, Truckin' is the first fully-fledged truck simulator game, using real-life highways and locations that are in general more accurate than not. It predates CRL's
Juggernaut
for the ZX Spectrum by at least two years, and Juggernaut uses a completely fictitious game world instead.
Gameplay has you driving across much of North America while managing your load, fuel and speed. It features changing weather and highway conditions, intermittent brushes with the fuzz, and a bit of white knuckles dodging other truckers who inevitably swerve all over the road. The game displays your position as a combination of highway number and a two-letter city code with a list of specific routes. While these routes were fixed, the game does no navigation either — because
you're
expected to do that!
Truckin's map database is rather noteworthy even considering the deliberate geographic liberties taken to fit it and the rest of the game into 16K of ROM. In the Truckin' universe, Interstates are the only highways except for US 101 on the extreme Pacific coast (appearing as "Interstate 01"), a single "Highway 1" in Canada as a composite of the southern Trans-Canada Highway (and continuous with US 1 in Maine), and an undocumented California State Route 9 as part of
an easter egg
. Besides very terse prompts and a heavily compressed internal routing table, the game makes all highway numbers unique and has no multiplexes or three-digit auxiliary Interstates, and while you can drive into Canada you can't drive into Mexico (admittedly it was pre-NAFTA). Additionally, for gameplay reasons every highway junction is a named "city," introducing irregularities like Interstate 70 ending in Provo, UT when it really ends about 130 miles south, or Interstate 15 ending in El Cajon, CA, and many cities and various two-digit primary Interstates are simply not included (e.g., I-12, I-19, I-30, I-85, I-93, etc.). As a result of these constraints, among other inaccuracies Interstate 90 terminates in Madison, WI at I-94 (not Boston), I-94 terminates in Milwaukee at I-55 (not Port Huron, MI), and I-40 is extended west from its true terminus in Barstow, CA along real-world California State Highway 58 to intersect I-5 "in Bakersfield" (real Interstate 5 is around twenty miles away). Still, it contains an extensive network of real highways with their lengths and control cities, managing it all on an early console platform with limited memory, while simultaneously supporting full 1983-level gameplay.
The 8-bit home computer was ascendant during the same time and at least one company perceived a market for computer-computed routes with vacations and business trips. I can't find any references to an earlier software package of this kind for this class of computer, at least in the United States, so we'll call it the first.
Columbia Software, based out of Columbia, Maryland, seems to have sold exactly one title, namely this one: Roadsearch. It ran out of a private residence which I've chosen to censor from this actual ad (the house still exists), and while no credits appear in either the Apple II or Commodore 64 version, the name was probably a d/b/a for John Pandelides who was the likely author and is listed as Columbia Software's contact in
The Software Writer's Marketplace
from 1984. If this is the same person, he later appears in a 2001 document as the Ground and Mission Systems Manager at the NASA Goddard Space Flight Center in Greenbelt, Maryland, about a half hour's drive away. Columbia Software does not appear in any magazines prior to 1982 nor does it appear after 1985, though no business record under that name is known to either the state of Maryland or the state of Delaware.
The Apple II version boasted 406 cities and road junctions and roughly 70,000 road miles, shown on a static high-resolution map as the program loaded. The connecting roads were primarily Interstates but also included many major US highways and some state routes, although not all routes appeared in their entirety. There were also a smattering of Canadian cities and routes yet no Alaskan ones despite the fact you can absolutely drive to Alaska through Canada (see, for example, the Alaska Highway). On the other hand, it makes sense there weren't any Hawai'ian or Puerto Rican ones.
The version we have here is the "basic" version of Roadsearch that simply used that database for $34.95 [about $118 in 2025 dollars], but there was also an enhanced version called Roadsearch-Plus that could add an additional fifty user-defined junction points and roads between them for $74.95 [$250]. Although we're going to spend most of our time with the 1985 Commodore 64 version because it has both a larger and more current map along with the Plus database editor, the 1982 Apple II version's design informs the C64 port, so we'll take the earlier iteration apart a bit first for analysis.
The basic functionality between both ports was roughly equivalent: given a starting point among its database of cities and junctions, you could either manually walk the available roads from point to point until you reached your destination, or let the computer figure it out. Should there be specific roads you wished to avoid (e.g., tolled, known to be closed, bad weather conditions, etc.), you could provide a list to the program and it would duly ignore them while constructing the itinerary. If you provided a target speed and/or fuel economy level, it would additionally estimate the elapsed time and fuel usage based on miles driven. Even in the lower-tiered version it was possible to modify the on-disk map by altering the distances between junction points, presumably to account for highway rerouting, though you couldn't add any new roads or waypoints except in the "plus" version.
If you chose to have the computer do the walking, there would be a minute or two or twenty of computation and then the automatically determined route was presented to you in summary format. Cities and waypoints could be searched for, or, if you knew the number, you could just enter the number directly. You could also naturally print it out for the car, though there was no option to save a generated routing for later. The program would remember the target speed and fuel economy and save them for future runs.
The disk catalogue suggests that we're dealing with a compiled Applesoft BASIC program based on the suspiciously-named files
T%()
,
N%()
and
B%()
which sound like Applesoft BASIC integer arrays. (The file
MPH
just contains the MPG and MPH targets in text.) In fact, there are actually two compiled programs present,
ROADSEARCH
(the main executable) and
DBA
(the distance editor), and using these "variable" files allows both programs to keep the memory image of the arrays, no doubt the representation of its map database, consistent between them. You can start either compiled program by
BRUN
ning them, as
HELLO
does.
Exactly
which
compiler we can also make a fairly educated guess about: there were only a few practical choices in 1981-82 when it was probably written, and most of them we can immediately eliminate due to what they (don't) support or what they (don't) generate. For example, being almost certainly Applesoft BASIC would obviously eliminate any Integer BASIC compiler. It also can't be On-Line Systems' Expediter II because that generates "Applesoft BASIC" programs with a single
CALL
statement instead of binaries that are
BRUN
, and it probably isn't Southwestern Data Systems' Speed Star because of the apparent length of the program and that particular compiler's limited capacity.
That leaves the two major compilers of this era, Microsoft's TASC ("The Applesoft Compiler"), which was famously
compiled with itself
, and Hayden Book Company's Applesoft Compiler. TASC uses a separate runtime that must be
BLOAD
ed before
BRUN
ning the main executable, which
HELLO
doesn't do. Hayden's compiler is thus the most likely tool, and this theory is buoyed by the fact that this compiler does support variable sharing between modules.
If we run
strings
on the DOS 3.3
.dsk
image, we see things like
S(Y/N)?ENTER PRINTER SLOT NUMBER PLEASE TURN PRINTER ONPR#ROUTE (40 COL
UMN)!  ELAPSEDTIME ! MI.  TIME---- !---- -----MI)TO-*******************
********!***********HIT ANY KEY TO CONTINUEHIT ANY KEY FOR OUTPUT MENUD
ETAILED ROUTE BY COLUMBIA SOFTWARE*********OPEN ROADS,L12READ ROADS,RCL
OSE ROADS HAS BEEN DELETEDCOMPUTINGMILES TRAVELED 0000PLEASE BE PATIENT
OUTPUT MENU<1> PRINT/LIST ROUTE SUMMARY<2> PRINT/LIST ROUTE(40 COLUMN)<
3> PRINT DETAILED ROUTE(80 COLUMN)<4> CHANGE <5> START OVERDO YOU WISH 
TO PRINT RESULT
[...]
 HRS:MINAVERAGE SPEED--VEHICLE MPG----TOTAL GALLONS-- GAL.------------!
 -------------------!-------------!----------------!---------------!NOT
 ENTERED PROPERLY. PLEASE TRY AGAIN
----------------------------------------------------OPEN ROADMAP CITIES
,L19READ ROADMAP CITIES,RCLOSE ROADMAP CITIESFORMATS:CITY NO. <RETURN>C
ITY NAME STATE <RETURN><RETURN> (TO CONTINUE)OK(Y/N)? FROM-----------TO
-------------TOTAL DISTANCE-TOTAL TIME-----**************************! 
ELAPSED     !   REMAINING   !     ROAD    !    TO (CITY)      !MI  TIME
GAL ! MI   TIME  GAL !MI    TIME  GAL!ELAPSED MILES--CURRENT CITY---ENT
ER CONNECTING CITY: TAKE ROAD   MI.     CONNECTING CITY----------   ---
----------
[...]
O CONTINUE)IS AN ILLEGAL NUMBER. PLEASE CHECK THE  FORMATHAS NOT BEEN M
ATCHED.CHECK THE FORMAT AND OR THE LISTOK(Y/N)? 
 )B 
B%(),A30733,L5448 TAKE ROAD   MI.     CONNECTING CITY----------   --- -
-------------------------------------------------------------OPEN ROADM
AP CITIES,L19READ ROADMAP CITIES,RCLOSE ROADMAP CITIESFORMATS:CITY NO. 
<RETURN>CITY NAME STATE <RETURN><RETURN> (TOVERYOUR CHOICE:NOT ENTERED 
PROPERLY. TRY AGAINRUN HELLO====================ENTER CITY #1FROM -ENTE
R CONNECTING CITYNOT CONNECTED BY ROAD. TRY AGAINOPEN ROADS,L12READ ROA
DS,RCLOSE ROADSROAD---------FROM---------TO-----------DISTANCE-----NEW 
DISTANCE=BSAVE 
L#5BLOAD B%(),A30733OPEN T%()READ T%()CLOSE T%()CHANGE DATABASE========
=======THIS SUBROUTINE ALTERS THE CONTENTS OF  YOUR ROADSEARCH DISK. PL
EASE PROCEED    CAUTIOUSLY.THESE ARE YOUR OPTIONS<1> CHANGE ROAD DISTAN
CE<2> SAVE CHANGES TO DISK<3> START 
[...]
Accounting for the fact that the disk interleave will not necessarily put lines in sequential order, you can pick out the strings of the program as well as a number of DOS 3.3 file manager commands, sometimes in pieces, such as
B%(),A30733,L5448
which is probably part of a
BSAVE
command, or
BLOAD B%(),A30733
. The disk also has examples of both kinds of DOS 3.3 text files, both sequentially accessed (such as
OPEN T%()
,
READ T%()
and
CLOSE T%()
) but also the less commonly encountered random access (with explicitly specified record numbers and lengths such as
OPEN ROADS,L12
and
OPEN ROADMAP CITIES,L19
, then
READ ROADS,R
and
READ ROADMAP CITIES,R
which would be followed by the record number).
For these random access files, given a record length and record number, the DOS track-and-sector list is walked to where that record would be and only the necessary sector(s) are read to construct and return the record. We can see the contents with a quick Perl one-liner to strip off the high bit and feeding that to
strings
:
% perl -e 'eval "use bytes";$/=\1;while(<>){print pack("C",unpack("C",$_)&127);}' roadsearch.dsk | strings
[...]
PHOENIX AZ
PIERRE SD
PITTSBURGH PA
PLATTSBURG NY
POCATELLO ID
PORT HURON MI
PORTLAND ME
PORTLAND OR
PORTSMOUTH NH
PRATT KS
PROVIDENCE RI
PUEBLO CO
QUEBEC PQ
[...]
JCT US89/UT14 UT
JCT US93/I15ST NJ
JCT I25/US20 WY
JCT I26/I95 SC
JCT I35/US20 IA
JCT I40/I81 TN
JCT I5/CA152 CA
JCT I5/CA99 CA
JCT I5/I580 CA
JCT I57/I24 IL
[...]
Again note that the order is affected by the disk interleave, but the file is stored alphabetically (we'll extract this file properly in a moment). Another interesting string I found this way was "
TIABSRAB WS AIBMULOC
" which is
COLUMBIA SW BARSBAIT
backwards. Perhaps someone can explain this reference.
In a hex editor the city database looks like this, where you can see the regularly repeating 19-byte record format for the names. Remember that the characters are stored with the high bit set.
000044a0  ce a0 ce d9 8d 00 00 00  00 00 cd c9 cc c5 d3 a0  |................|
000044b0  c3 c9 d4 d9 a0 cd d4 8d  00 00 00 00 00 cd c9 cc  |................|
000044c0  d4 cf ce a0 d0 c1 8d 00  00 00 00 00 00 00 00 00  |................|
000044d0  cd c9 cc d7 c1 d5 cb c5  c5 a0 d7 c9 8d 00 00 00  |................|
000044e0  00 00 00 cd c9 ce ce c5  c1 d0 cf cc c9 d3 a0 cd  |................|
000044f0  ce 8d 00 00 00 00 cd c9  ce cf d4 a0 ce c4 8d 00  |................|
00004500  00 00 00 00 00 00 00 00  cc c9 d4 d4 cc c5 a0 d2  |................|
00004510  cf c3 cb a0 c1 d2 8d 00  00 00 00 cc c9 d4 d4 cc  |................|
00004520  c5 d4 cf ce a0 ce c8 8d  00 00 00 00 00 00 cc cf  |................|
00004530  ce c4 cf ce a0 cf ce 8d  00 00 00 00 00 00 00 00  |................|
00004540  00 cc cf d2 c4 d3 c2 d5  d2 c7 a0 ce cd 8d 00 00  |................|
00004550  00 00 00 00 cc cf d3 a0  c1 ce c7 c5 cc c5 d3 a0  |................|
00004560  c3 c1 8d 00 00 00 00 cc  cf d3 d4 a0 c8 c9 cc cc  |................|
00004570  d3 a0 c3 c1 8d 00 00 00  00 00 cc cf d5 c9 d3 d6  |................|
00004580  c9 cc cc c5 a0 cb d9 8d  00 00 00 00 00 cc d5 c2  |................|
This is not a very efficient means of storage especially considering DOS 3.3 only had 124K free per disk side (after DOS itself and filesystem overhead), but it would be a lot easier for an Applesoft BASIC program to handle since the record lookup work could be shunted off to DOS 3.3 and performed quickly. Also, while you can list the cities and junctions from the menu, they are not indexed by state, only by first letter:
We extract the list of cities in Virtual ][ by dumping
ROADMAP CITIES
to the emulator's virtual printer. We know its record length because it was stored as a string in the compiled BASIC text we scanned previously. That, in turn, gives us a text file we can read on the Mac side. It is, as expected, 406 lines long. The same process gets us the
ROADS
list, which is 171 lines long. Keep in mind that's just a list of the
names
of the roads; it does not contain information on the actual highway segments between points.
However, the city list doesn't actually contain the index for the first letter. Instead, the index is in the only array that is stored as a text file (i.e.,
T%()
), where for each letter index 1-26, the value is the first record number for all cities starting with that letter. As we saw previously, the cities are already sorted on disk to facilitate. There are no cities starting with Z, so that letter just goes to the end of the file (non-existent record 407) and terminates.
This design choice makes it a bit more difficult to browse locations geographically, although at least entering J gets you all the junctions. I don't know, and no article says, how the database was constructed. However, the most likely explanation is that they sat down with a road atlas and labouriously typed it all in, as there wouldn't have been much alternative. Unfortunately the code strings in the compiled BASIC program don't give us enough obvious information to derive the dimensions or purpose of
B%()
and
N%()
, but we'll solve that problem a little later on.
In the interim the Commodore 64 came out and rapidly became the most popular home computer in North America (and a lot of other places). As Commodore BASIC 2.0 and Applesoft BASIC are both derived from Microsoft BASIC, the main program and the map editor could be ported with few changes; the only major change appears to have been to the data file format. The initial 1984 release used the same 1982 database from the Apple II with the same 406 cities and junctions, after which a second version came out in 1985 with an expanded 487-point database and updated routing information. However, this release appears to be specific to the Commodore port — if there were a 1985 map update for the Apple II, it has yet to surface — and I can find no subsequent release of Roadsearch after 1985 on any platform.
Both C64 versions came in the same Roadsearch and Roadsearch-Plus variants for the same prices, so the iteration we'll explore here is Roadsearch-Plus with the presumed final 1985 database. For purposes of emulation we'll use VICE's SuperCPU spin with the 65816 enabled as some number crunching is involved, but I also tested it on my real Commodore SX-64 and 128DCR for veracity. (Running
xscpu64
in warp mode will absolutely tear through any routing task, but I strongly recommend setting location 650 to 64 in the VICE monitor to disable key repeat.) It's worth noting that the various circulating 1541 disk images of the 1984 and 1985 editions were modified to add entries by their previous owners, though we'll point out how these can be detected and reversed. For much of this article I'll be running a 1985 disk that I manually cleared in a hex editor to what I believe was its original contents.
Although it's not copy-protected, or even write-protected, the disk comes with a(n easily forged) serial number and there are some irregularities which might be there as obfuscation. The Commodore version introduced a new simpler menu where cities could now be displayed by state (though this wasn't indexed, requiring a walk through the entire city file each time) and the connection listing option was removed, since you'd get that anyway by trying to manually construct a route. This is the "plus" release, so the option for making changes to map distances moved to the editor, where you could also show cities, roads and connections directly. We'll get to the editor later on.
Otherwise this version works much the same and generates the same routes as the Apple II version did, so they are undoubtedly using the same pathfinding algorithm. The speeds are also roughly comparable, which probably says more about the compilers than the computers (an NTSC 64 would be around the same speed as an Apple II, about ~1.02MHz). We'll get to what I think it's doing when we start dissecting the main program.
At least three versions of the Commodore 64 version presently circulate: two from 1984 and one from 1985. This is the directory listing for the later 1984 version, showing the main program (
ROADSEARCH+
), the editor (
IDBA
) and two RELative files for the
CITIES
and
ROADS
. RELative files are functionally equivalent to DOS 3.3 random access files, being a record-based file format with a fixed size and an index (made up of "side sectors"). They are an uncommon sight on commercial software due to their idiosyncracies and
a few outright bugs
, and they don't work well for binary data or support variable record sizes which is why Berkeley Softworks came up with VLIR for GEOS instead. On the other hand, they do just fine for text strings and the lookup can be very fast. The cities file looks like this when dumping the raw sectors from the
.d64
disk image:
000103e0  00 00 84 13 00 43 49 54  49 45 53 a0 a0 a0 a0 a0  |.....CITIES.....|
000103f0  a0 a0 a0 a0 a0 13 0a 1f  00 00 00 00 00 00 5e 00  |..............^.|

00017800  13 0b ff 00 00 00 00 00  00 00 00 00 00 00 41 42  |..............AB|
00017810  49 4c 49 4e 45 20 54 58  0d 00 00 00 00 00 00 00  |ILINE TX........|
00017820  00 ff 00 00 00 00 00 00  00 00 00 00 00 41 4b 52  |.............AKR|
00017830  4f 4e 20 4f 48 0d 00 00  00 00 00 00 00 00 00 00  |ON OH...........|
00017840  ff 00 00 00 00 00 00 00  00 00 00 00 41 4c 42 41  |............ALBA|
00017850  4e 59 20 4e 59 0d 00 00  00 00 00 00 00 00 00 ff  |NY NY...........|
00017860  00 00 00 00 00 00 00 00  00 00 00 41 4c 42 45 52  |...........ALBER|
00017870  54 20 4c 45 41 20 4d 4e  0d 00 00 00 00 00 ff 00  |T LEA MN........|
00017880  00 00 00 00 00 00 00 00  00 00 41 4c 42 55 51 55  |..........ALBUQU|
00017890  45 52 51 55 45 20 4e 4d  0d 00 00 00 00 ff 00 00  |ERQUE NM........|
The directory entry indicates a file with 31-byte records, the first side sector at track 19 sector 10 and the first data sector (shown in part below) at track 19 sector 0. Other than the obvious typo in Abilene, TX, it is the same basic format as the Apple version and also sorted, ending each string with a carriage return. As a method of what I assume prevents trivially dumping its contents, a naive read of each record won't yield anything useful because every record starts with an $ff and a whole bunch of nulls, which Commodore DOS interprets as the end. The actual string doesn't start until offset 12. The same basic idea holds for the roads file:
00016900  00 ff 84 17 09 52 4f 41  44 53 a0 a0 a0 a0 a0 a0  |.....ROADS......|
00016910  a0 a0 a0 a0 a0 18 00 18  00 00 00 00 00 00 1f 00  |................|

0001cd00  18 01 ff 00 00 00 00 00  00 00 00 00 00 00 41 42  |..............AB|
0001cd10  20 33 0d 00 00 00 00 00  00 00 ff 00 00 00 00 00  | 3..............|
0001cd20  00 00 00 00 00 00 41 42  20 34 0d 00 00 00 00 00  |......AB 4......|
0001cd30  00 00 ff 00 00 00 00 00  00 00 00 00 00 00 41 42  |..............AB|
0001cd40  33 2f 41 42 32 0d 00 00  00 00 ff 00 00 00 00 00  |3/AB2...........|
0001cd50  00 00 00 00 00 00 41 4c  20 31 38 36 0d 00 00 00  |......AL 186....|
0001cd60  00 00 ff 00 00 00 00 00  00 00 00 00 00 00 41 54  |..............AT|
0001cd70  4c 20 43 54 59 20 45 58  50 0d ff 00 00 00 00 00  |L CTY EXP.......|
0001cd80  00 00 00 00 00 00 42 41  49 4c 45 59 20 54 50 4b  |......BAILEY TPK|
The same offset trick is used, but here the records are 24-byte since route names are shorter. Again, this isn't a particularly efficient storage mechanism, but we have over 165K available on a formatted disk, and RELative file access to any arbitrary record is quite quick.
Despite the presence of side sectors, the actual
records
of a RELative file are still sequentially stored on disk with the usual forward track and sector pointers. As such, we don't need to grab the side sectors to simply extract its contents. For some period of time the
c1541
tool from the VICE suite would not copy REL files and this was only recently fixed, so here is a Perl script I threw together to iterate over a D64 disk image and transfer a file to standard output, either by name or if you specify a starting track and sector.
#!/usr/bin/perl

eval "use bytes"; die("usage: $0 d64 [file|-ts t s]\n") if (!length($ARGV[0]));
open(W, $ARGV[0]) || die("open: $!\n");
undef $/; @buf = unpack("C*", <W>); close(W);
die("abnormally small d64\n") if (scalar(@buf) < 174848);

if ($ARGV[1] eq '-ts' && $ARGV[2] > 0 && length($ARGV[3])) {
	$ft = 0+$ARGV[2]; $fs = 0+$ARGV[3]; $head = &tsoff($ft,fs);
} elsif ($ARGV[1] eq '-off' && length($ARGV[2])) {
	$head = ($ARGV[2] =~ /^0x/) ? hex($ARGV[2]) : 0+$ARGV[2];
	die("invalid sector offset\n") if ($head & 255);
} else {
@fts = qw(DEL SEQ PRG USR REL ??? ??? ???); # 18,0 = offset 91392 0x16500
$head = &tsoff(18, 1); FOUND: for(;;) { $nt = $buf[$head]; $ns = $buf[$head+1];
	for($i=0;$i<8;$i++,$head+=32) { # each sector has 8 entries
		next unless ($buf[$head+2] || $buf[$head+3] || $buf[$head+4]);
		$type = $buf[$head+2] & 7;
		$ft = $buf[$head+3]; $fs = $buf[$head+4];
		$sst = $buf[$head+21]; $sss = $buf[$head+22];
		$rs = $buf[$head+23];
		$fn = ''; for($j=5;$j<21;$j++) {
			$fn .= chr($buf[$head+$j]) unless
				($buf[$head+$j] == 160);
		}
		warn "$fts[$type] $fn\n";
		last FOUND if (length($ARGV[1]) && $fn eq $ARGV[1]);
	}
	$type = -1; last unless ($nt); $head = &tsoff($nt, $ns);
}
exit(0) unless (length($ARGV[1]));
die("file not found\n") unless ($type > -1);
warn "recordsize $rs, side sector block at $sst/$sss\n" if ($type == 4);
warn "data at $ft/$fs\n";
$head = &tsoff($ft, $fs);
}
for(;;) { $nt = $buf[$head]; $ns = $buf[$head+1];
	if ($nt) {
	for($i=2;$i<256;$i++) { print STDOUT pack("C", $buf[$head+$i]); }
	} else {
	for($i=2;$i<$ns;$i++) { print STDOUT pack("C", $buf[$head+$i]); }
	}
	last unless ($nt); warn "data at $nt/$ns\n"; $head = &tsoff($nt, $ns);
}

# 1-17 21 sectors, 18-24 19 sectors, 25-30 18 sectors, 31-35 17 sectors
sub tsoff {
	my ($t, $s) = (@_); my $ts; my $off=0; for($ts=1;$ts<$t;$ts++) {
		$off += ($ts < 18) ? (21 * 256) : ($ts < 25) ? (19 * 256) :
			($ts < 31) ? (18 * 256) : (17 * 256);
	} return ($off + ($s * 256));
}
Because this yanks the files "raw," we will then need to strip them down. Feed the extracted REL records to this and you'll get a text file:
#!/usr/bin/perl

eval "use bytes";
$/ = "\015"; while(<>) {
	chomp;
	s/^[\0\377]+//;
	print"$_ \n";
}
You'll notice that both the cities and roads lists are, or at least start out, sorted. All C64 Roadsearch images I've seen circulating so far have been altered by their previous owners to add their own local roads and cities, and their changes can be easily distinguished at the point where the lists abruptly go out of alphabetical order.
There is also a pair of SEQuential files, one named
MPH
and serving the same function to store the preferred speed and fuel economy, and a second one simply named
M
. This file contains four ASCII numbers, one obviously recognizeable as our serial number, though this is only one of the two places the program checks. The others are the number of cities (406, or 487 in the 1985 version), number of roads (215 in 1985), and a third we don't yet know the purpose of. You can confirm the first two by checking it against the number of lines in the files you extracted.
What we
don't
see are files for the arrays we spotted on the Apple disk. The only file left big enough to account for those is
MATS
. To figure out how that works, we should start digging into the program.
We had to make an educated (though I assert likely correct) guess about the compiler used with the Apple II version, but the source of the Commodore 64 version is immediately given away by the presence of
RTL-64
, a runtime library and the telltale sign of a program compiled with DTL BASIC. DTL BASIC, formally DTL-BASIC 64 Jetpack, became extremely popular with developers not just due to its good performance and compatibility but also requiring no royalties to sell programs compiled with it as long as credit was given. An optional "protector" version can obfuscate the program and/or require a hardware dongle, though this version is rarer due to its expense (and fortunately was not used here). The runtime library slots into the RAM under the BASIC ROM, so there is no obvious loss of free memory. DTL stood for "Drive Technology Ltd." and was written by David Hughes in the UK, first for the PET; the compiler is notable for being compiled with itself, like Microsoft TASC, and using the same "RTL" runtime library and protection system (and, obnoxiously, a dongle) as the object code it generates. The 64 tape version is substantially less capable than the disk one.
DTL BASIC compiles to its own bespoke P-code which is executed by the RTL. It achieves its speed through a greater degree of precalculation and preparsing (e.g., pre-resolving values and line numbers, removal of comments, etc.), a custom garbage collection routine, and also, where possible, the use of true signed 16-bit integer math. This is a substantial speed-up over most Microsoft-derived BASICs, in which Microsoft Binary Format floating point is the native system for all calculations to the point where integer variables must first be
converted
to floating point, the computation performed, and then converted
back
. Ordinarily this would only make them useful for smaller arrays in memory because the double conversion will make them slower than regular floating point variables. However, DTL BASIC
does
perform true integer math without conversion, first for all variables explicitly declared as integer, and even autoconverting other variables at compile time with a directive (pragma).
Although some private work on a decompiler
reportedly exists
, to the best of my knowledge that decompiler remains unfinished and unavailable. Interestingly, what I presume is the earlier 1984 disk image has some ghost directory entries, two each for the source BASIC programs and their "symbol tables" used by
ERROR LOCATE
for runtime errors:
00016980  00 00 00 08 00 49 44 42  41 2d 53 52 43 a0 a0 a0  |.....IDBA-SRC...|
00016990  a0 a0 a0 a0 a0 00 00 00  00 00 00 00 00 00 31 00  |..............1.|
000169a0  00 00 00 1c 04 4c 4e 2d  52 4f 41 44 53 45 41 52  |.....LN-ROADSEAR|
000169b0  43 48 2b a0 a0 00 00 00  00 00 00 00 00 00 08 00  |CH+.............|
000169c0  00 00 00 06 02 52 4f 41  44 53 45 41 52 43 48 2b  |.....ROADSEARCH+|
000169d0  2d 53 52 43 a0 00 00 00  00 00 00 00 00 00 30 00  |-SRC..........0.|
000169e0  00 00 00 1c 05 4c 4e 2d  49 44 42 41 a0 a0 a0 a0  |.....LN-IDBA....|
000169f0  a0 a0 a0 a0 a0 00 00 00  00 00 00 00 00 00 09 00  |................|
Sadly these source files were overwritten and cannot be resurrected, and even the ghost entries were purged on the second 1984 image. However, two aspects of the compiler make it possible to recover at least a portion of the original program text by hand. The first is that not all statements of the original program are fully converted to P-code: in particular,
READ
/
DATA
,
OPEN
,
INPUT
/
INPUT#
,
DIM
,
PRINT
/
PRINT#
and possibly others will be preserved nearly in their original BASIC form, including literal strings and most usefully
variable names
. For example, if we pull the compiled
ROADSEARCH+
off the disk image and run it through
strings
, we see text not unlike a BASIC program:
% strings roadsearch+
2073
hhLH
RTL-64 R
h` _
 234,234,234,234,234,173,237,192,174,238,192, 172,239,192,32,186,255,173,224,192, 162,225,160,192,32,189,255,96,234,234, 234,234,169,0,32,144,255,96,234,234, 234,234,234,234,234,234,234,234, 32,0,192,169,0,166,251,164,252,32,213, 255,32,32,192,96
VL-ROADSEARCH+W^
1,8,15,"I":
N%(756,4):A
B%(1080,3):A
T%(26):A
8)"***********************"
8)"**                   **"
8)"**  ROADSEARCH-PLUS  **"
8)"**    USA-CANADA     **"
8)"**                   **"
8)"**  COPYRIGHT 1985   **"
8)"**        BY         **"
8)"** COLUMBIA SOFTWARE **"
8)"**                   **"
8)"**ALL RIGHTS RESERVED**"
8)"***********************":
S5%:
6,8,3,"0:MPH,S,R"
6,MG
6,MH
5,8,4,"0:M,S,R"
5,CN%
5,CB%
5,CR%
5,SN%
23)"SN#";SN%
"SELECT ONE:"
[...]
DTL-compiled programs always start with an
SYS 2073
to jump into a small machine-code subroutine linked into the object. This section of code loads the RTL (the filename follows) and has other minor housekeeping functions, including one we'll explain shortly when we break into the program while it's running. It resides here so that it can bank BASIC ROM in or out as necessary without crashing the computer.
Following that is an incomplete machine language subroutine in a consolidated
DATA
statement. Disassembly of the fragment shows it's clearly intended to run from $c000, but at least part of it is missing. Of the portion we can see here, however, there are calls for what appears to be a Kernal load, so if we drop a breakpoint on $ffba in VICE (e.g., the Kernal SETLFS routine) we can run the 6502's call stack back to see the full routine and the filename (at $c0e1) it's trying to access:
MATS
. It loads it straight into memory in the middle of the available BASIC range.
After that, now we see the arrays we saw in the Apple II version, but more importantly they're clearly part of
DIM
statements, so we can also see their dimensions. We already knew
T%()
was likely to be only 26 (27 counting the zero index) integers long from dumping the Apple version's contents, but the
N%()
array has up to 757 entries of five fields each, and
B%()
is even bigger, with 1081 records of four fields each. This is obviously where our map data is stored, and
MATS
is the file it seems to be loading to populate them.
This brings us to the second aspect of DTL Jetpack that helps to partially decipher the program: to facilitate some reuse of the BASIC ROM, the generated code will still create and maintain BASIC-compatible variables which we can locate in RAM. So that we know what we're dealing with, we need to figure out some way to stop the program while it's running to examine its state. Naturally the compiler offers a means to defeat this.
With the program running we can see in the VICE monitor that the Kernal STOP routine has been revectored to $084f, within the utility section at the beginning of the program. Here's the complete disassembly starting at $080d/2061 with my annotations. Some of this code doesn't appear to be called under normal circumstances.
; warm start (2061)
.C:080d  20 52 08    JSR $0852
.C:0810  4C 2B A9    JMP $A92B

; not called?
.C:0813  20 52 08    JSR $0852
.C:0816  4C 11 A9    JMP $A911

; cold start (2073)
; load the RTL if flag not set, then start P-code execution
.C:0819  20 52 08    JSR $0852
.C:081c  AD FF 02    LDA $02FF
.C:081f  C9 64       CMP #$64
.C:0821  F0 17       BEQ $083A
.C:0823  A9 3F       LDA #$3F
.C:0825  85 BB       STA $BB
.C:0827  A9 08       LDA #$08
.C:0829  85 BC       STA $BC
.C:082b  A9 06       LDA #$06
.C:082d  85 B7       STA $B7
.C:082f  A9 00       LDA #$00
.C:0831  85 B9       STA $B9
.C:0833  A2 00       LDX #$00
.C:0835  A0 A0       LDY #$A0
.C:0837  20 D5 FF    JSR $FFD5
.C:083a  68          PLA
.C:083b  68          PLA
.C:083c  4C 48 A0    JMP $A048
.C:083f              .asc "RTL-64"

; seems to get called on a crash or error
.C:0845  20 52 08    JSR $0852
.C:0848  20 2F A0    JSR $A02F ; jumps to $a948
.C:084b  20 5F 08    JSR $085F
.C:084e  60          RTS

; dummy STOP routine
.C:084f  A2 01       LDX #$01
.C:0851  60          RTS

; bank out BASIC ROM
.C:0852  A9 03       LDA #$03
.C:0854  05 00       ORA $00
.C:0856  85 00       STA $00
.C:0858  A9 FE       LDA #$FE
.C:085a  25 01       AND $01
.C:085c  85 01       STA $01
.C:085e  60          RTS

; bank in BASIC ROM
.C:085f  48          PHA
.C:0860  A9 03       LDA #$03
.C:0862  05 00       ORA $00
.C:0864  85 00       STA $00
.C:0866  A5 01       LDA $01
.C:0868  09 01       ORA #$01
.C:086a  85 01       STA $01
.C:086c  68          PLA
.C:086d  60          RTS

; execute next statement (using BASIC ROM)
.C:086e  20 5F 08    JSR $085F
.C:0871  20 ED A7    JSR $A7ED
.C:0874  20 52 08    JSR $0852
.C:0877  60          RTS
With the dummy routine at $084f in place, RUN/STOP and RUN/STOP-RESTORE have no observable effect. This feature is controlled by DTL Jetpack's
DS
and
ES
compiler directives which disable and enable RUN/STOP respectively. If we scan the RTL for code that modifies $0328 and $0329 where the STOP routine is vectored, we find this segment:
.C:b7c9  20 DA B7    JSR $B7DA
.C:b7cc  20 D9 A6    JSR $A6D9
.C:b7cf  A9 EA       LDA #$EA
.C:b7d1  8D 22 A8    STA $A822
.C:b7d4  20 DA B7    JSR $B7DA
.C:b7d7  4C 58 A8    JMP $A858
.C:b7da  A9 ED       LDA #$ED
.C:b7dc  A2 F6       LDX #$F6
.C:b7de  8D 28 03    STA $0328
.C:b7e1  8E 29 03    STX $0329
.C:b7e4  60          RTS
.C:b7e5  A9 60       LDA #$60
.C:b7e7  8D 22 A8    STA $A822
.C:b7ea  20 F0 B7    JSR $B7F0
.C:b7ed  4C 58 A8    JMP $A858
.C:b7f0  A9 4F       LDA #$4F
.C:b7f2  A2 08       LDX #$08
.C:b7f4  4C DE B7    JMP $B7DE
$f6ed is the normal value for the STOP vector, so we can assume that the routine at $b7c9 (which calls the routine at $b7da to set it) enables RUN/STOP, and thus the routine at $b7e5 disables it. Both routines twiddle a byte at $a822, part of this section:
.C:a822  EA          NOP
.C:a823  A5 91       LDA $91
.C:a825  C9 7F       CMP #$7F
.C:a827  D0 1C       BNE $A845
.C:a829  20 D9 A6    JSR $A6D9
.C:a82c  20 DA B7    JSR $B7DA
.C:a82f  20 E5 A6    JSR $A6E5
.C:a832  A5 39       LDA $39
.C:a834  85 7A       STA $7A
.C:a836  A5 3A       LDA $3A
.C:a838  85 7B       STA $7B
.C:a83a  A9 02       LDA #$02
.C:a83c  20 7B A0    JSR $A07B
.C:a83f  A9 00       LDA #$00
.C:a841  38          SEC
.C:a842  4C 6E 08    JMP $086E
.C:a845  60          RTS
By default the byte at $a822 is $ea, a 6502
NOP
. This falls through to checking $91 for the state of the STOP key at the last time the keyboard matrix was scanned and branching accordingly. When the STOP routine is revectored, at the same time the byte at $a822 is changed to $60
RTS
so that the STOP key check is never performed. (The RTL further achieves additional speed here by only doing this check on
NEXT
and
IF
statements even if the check is enabled.)
The simplest way to deal with this is to alter
RTL-64
with a hex editor and turn everything from $b7e5 to $b7ec inclusive into
NOP
s. This turns the
DS
directive into a no-op as well, and now we can break out of the program by mashing RUN/STOP, though we'll do this after
MATS
is loaded. Parenthetically, instead of using
CONT
, the compiled program can be continued with
SYS 2061
instead of
SYS 2073
.
As a test we dump
T%()
, since we've assumed it has the same purpose in the Commodore port, and it does (once again there are no cities starting with Z, so the final letter points to non-existent record 488 beyond Yuma, AZ as record 487). We then use the BASIC routine at $b08b (
SYS 45195
) to look up the address of the first variable in the array — note no comma between the
SYS
and the variable reference — which is deposited as a 16-bit address in location $47 (71). In this case the pointer is to $6b8a (27530), the actual zeroth data element, so if we rewind a few bytes we'll also get the array descriptor as well as its entire contents:
>C:6b83  d4 80 3d 00  01 00 1b 00  01 00 01 00  0f 00 2d 00
>C:6b93  52 00 60 00  69 00 7c 00  8b 00 97 00  ed 00 f6 00
>C:6ba3  fe 01 16 01  36 01 43 01  4e 01 62 01  63 01 70 01
>C:6bb3  a3 01 b6 01  c8 01 cf 01  e4 01 e4 01  e8
Some explanation is in order: after the end of BASIC program text is non-array variables, and then any array variables (I'm ignoring strings for purposes of this discussion). The first two bytes are the variable name, with a null if the variable name is only one byte long. Type is determined by the combination of high bits (neither set is floating point, first byte set is a string, both bytes set is an integer variable as it is here). The second pair of bytes is the little-endian 16-bit length of the entire array including the name bytes (here 61 bytes total), followed by a byte for the number of dimensions in the variable (here one). Interestingly, the values that come after it are all
big
-endian: the dimensions themselves (a single big-endian short specified as 27, i.e. 26 plus the zeroth element), and then each value. In multidimensional arrays, each dimension is run out fully before moving to the next.
We can easily pick out the values we saw for
T%()
in the above dump, but more importantly we now have a long unambiguous 61-byte key we can search for. The entire sequence shows up in
MATS
, demonstrating that the file is in fact nothing more than an in-place memory dump of the program arrays' contents. Rather than manually dump the other two arrays from BASIC, we can simply walk
MATS
and pull the array values directly.
#!/usr/bin/perl

eval "use bytes"; undef %a;
# slurp file and drop starting address
$/ = undef; @arr = unpack("C*", <>); splice(@arr, 0, 2);
for(;;) {
	$v1 = shift @arr; $v2 = shift @arr; last if (!$v1);
	$j1 = $v1 & 128; $j2 = $v2 & 128;
	$v1 = chr($v1 & 127);
	$v2 = ($v2 == 0 || $v2 == 128) ? '' : chr($v2 & 127);
	$vn = "$v1$v2" . (
		($j1 & $j2) ? '%' :
		($j1) ? '$' :
		'');
	$vs = shift @arr;
	$vt = shift @arr;
	$vd = shift @arr;
	print STDOUT "$vn ($vd dimensions) \n";
	if ($vd == 2) {
		$d2 = 256*(shift @arr);
		$d2 += shift @arr;
		$d1 = 256*(shift @arr);
		$d1 += shift @arr;
		for($j=0;$j<$d2;$j++) {
			for($i=0;$i<$d1;$i++) {
				$v = 256*shift(@arr);
				$v += shift(@arr);
				$a{$vn}->[$i]->[$j] = $v;
			}
		}
	} else {
		print STDOUT " unsupported\n";
		splice(@arr, 0, (($vt << 8)+$vs-5));
	}
}
foreach (keys %a) {
	unless (open(K, ">out-$_\n")) {
		warn "out-$_ open: $!\n";
		next;
	}
	foreach (@{ $a{$_} }) {
		print K join("\t", @{ $_ }), "\n";
	}
	close(K);
}
This Perl script walks a memory dump of arrays (currently only two-dimensional integer arrays are implemented because that's all we need for this project). It skips the starting address and then writes out tab-separated values into files named by the arrays it finds. Unlike their storage in memory, where values go (0,0), (1,0), (2,0) ... (0,1), (1,1) and so on, this pivots the arrays horizontally so you get (0,0), (0,1), (0,2), etc., grouped into lines as "rows."
B%()
is the easiest to grok. Ignoring index 0, here is an extract from the file:
28      335     375     48
28      375     274     64
59      85      332     54
59      332     420     84
46      420     412     23
38      112     70      80
38      70      11      72
38      11      10      146
B%()
is referenced directly in one
PRINT
statement when displaying outgoing roads from a particular city:
% strings roadsearch+
[...]
" TAKE ROAD   MI.     CONNECTING CITY"
"----------   --- -----------------------":
"--------------------------------------":L
12)B%(I,3);
17)C$
")":LJ
1,8,15
3,8,3,"ROADS":
1,"P"
(LB%)
(HB%)
3,R$
1,8,15
3,8,3,"CITIES":
1,"P"
(LB%)
(HB%)
3,C$
Let's take city record number 1, which is the misspelled (but only in the 1985 version)
ABILINE TX
(that is, Abilene, Texas). The develop-a-route feature will list all connected cities. For Abilene, there are five in the database.
Now that we know what should appear in the list, we'll run it again but hold down RUN/STOP (in our hacked version) so that we immediately drop to BASIC before the first entry is
PRINT
ed.
We can see from the
PRINT
s above that
B%(I,3)
represents the mile length of the current connecting segment indexed by
I
(here 39), which would make
B%()
the array containing the connecting roads between cities and junctions. We also know it gets
R$
and
C$
from the RELative files
ROADS
and
CITIES
on each row. Helpfully, it tells us that
FORT WORTH TX
is city number 115 (it is), which we can see is
B%(I,1)
.
B%(I,2)
is 1, which must be us, leaving
B%(I,0)
as the route number which must be the record number for Interstate 20 in
ROADS
.
If we grab line 39 from
out-B%
(the value of index
I
), we do indeed see these same values. However, we can now do the search ourselves by just hunting for any record containing city 1 in columns 1 or 2 of our dumped array file (
^I
is a TAB character):
% grep '^I1^I' out-B%
38	115	1	153
38	1	26	111
162	1	473	143
193	389	1	207
193	1	245	147
Or, to show the correspondence more plainly:
I think their correlation is obvious, so that's it for
B%()
.
N%()
, on the other hand, is a little harder to crack. Other than its apparent
DIM
statement at the beginning (as shown above), it is never displayed directly to the user and never appears again in plaintext in the compiled object. Here are the first few entries of the array:
% head out-N%
9999	0	0	0	0
5664	17406	32766	0	0
7170	14226	32766	0	0
7444	12871	32766	0	0
7617	16294	32766	0	0
6123	18613	32766	0	0
7085	13158	32766	0	0
6145	17773	32766	0	0
5873	14978	32766	0	0
6213	14408	32766	0	0
The first record (index 0) is the second place where the serial number is stored, though only the map editor references it. Not counting index 0 the file has exactly one record for every city or junction, so it must correspond to them somehow. Otherwise, column 3 (except for index 0) is always an unusual value 32,766, near the positive maximum for a 16-bit integer variable, and columns 4 and 5 are always zero (note from the future: this is not always true for routes which are added in the editor). Additionally, columns 1 and 2 have an odd statistical distribution where the first is always between 4499 and 8915 and the second between 11839 and 21522. There are no negative values anywhere in the file, and the first three columns are
never
zero (other than index 0). Whatever they are, they are certainly not random.
The meaning of the values in this array managed to successfully evade my understanding for awhile, so in the meantime I turned to figuring out how Roadsearch does its routing.
The theorists reading this have already internalized this part as an exercise in
graph traversal
, specifically finding the shortest path. Abstractly the cities and junctions can be considered as the
nodes
or
vertices
of a
graph
. These nodes are enumerated by name in
CITIES
with additional, currently opaque, metadata in
N%()
. The nodes are then connected with
edges
, which are
weighted
by their mile length. These edges are the highway alignments listed with termini and length in
B%()
and their names in
ROADS
. The program appears to universally treat all edges as
bi-directional
, going both to and from a destination, which also makes the graph generally
undirected
. Because of the way the database (and indeed the nature of the American highway network) is constructed, all nodes are eventually reachable from any other node.
For a first analysis I presented Roadsearch with a drive I know well, having done it as part of longer trips many times in both directions: Bishop, California (city number 31) to Pendleton, Oregon (city number 338). This run can be traveled on a single highway number, namely US Highway 395, and it is also the shortest route. I have not indicated any roads that should be removed, so it will use everything in its database.
On the real machine (an NTSC 128DCR in 64 mode at 1.02272MHz, but also checked on the SX-64 for comparison) the routing process takes about two minutes and eight seconds per my stopwatch. There is no disk access during the routing process, so this is all CPU time.
On a fully-clocked 20MHz W65C816S SuperCPU, emulated here in VICE, it takes
five seconds
. No, warp mode was
not
on.
Take note of the progress display showing miles traveled. This is the first milepoint that appears. If we compare the edges (highway alignments) directly leaving from Bishop and Pendleton, an edge with a weight (length) of 198 miles only shows up leaving
Pendleton
, suggesting the program works the routing
backwards
:
% grep '^I31^I' out-B%
168	50	31	172
168	31	442	184
% grep '^I338^I' out-B%
90	349	338	208
90	338	207	171
168	338	43	198 <<<
131	338	464	42
The computed distance is 773 miles, which for 1985 would be approximately correct (depending on the exact endpoints which the program doesn't specify). The modern alignment is shorter by a few miles after the completion of Interstate 580 between Carson City and Reno, Nevada, which replaced several former alignments most of which are now signed as Business US 395 and Alternate US 395.
And here is the detailed leg-by-leg routing, very similar to the Apple II version (since they undoubtedly use the same or similar programming). Thirteen hours' drive wouldn't be far off as an estimate. Let's see if we can duplicate this process with our own code.
Arguably the "gold standard" for shortest path traversal is
Edsger Dijkstra's algorithm
, conceived in 1956 and published in 1959, an independent reimplementation of Vojtěch Jarník's 1930 minimum spanning tree algorithm that was also separately rediscovered and published by Robert C. Prim in 1957. In broad strokes, the algorithm works by building a tree out of the available nodes, putting them all into a queue. It keeps an array of costs for each node, initially set to an "infinite" value for all nodes except for the first node to be examined, traditionally the start point. It then repeatedly iterates over the queue: of all current nodes in the queue the lowest cost node is pulled out (so, first out, this will be the start point) and its edges are examined, selecting and marking any edges where the sum of the current node's cost and the cost of the edge (the mile length) are less than the current cost of the node it connects to (which, first out, will be "infinite"). The nodes connected by these marked edges take the current node as their parent, constructing the tree, and store the new lower cost value. Once the queue is empty, the algorithm halts and the tree is walked backwards from the target back to the start point, accumulating the optimal route using the parent pointers.
This Perl script accepts two city numbers and will generate the optimal route between them using the Roadsearch database with Dijkstra's algorithm. It expects
cities
,
roads
(both converted to text, not the raw RELative files) and
out-B%
to be in the same directory.
#!/usr/bin/perl

die("usage: $0 point_no_1 point_no_2\n") if (scalar(@ARGV) != 2);
$p1 = $ARGV[0]; $p2 = $ARGV[1];
die("wherever you go there you are\n") if ($p1 == $p2);

open(K, "cities") || open(K, "cities.txt") || die("cities: $!\n");
@cities = ( undef ); while(<K>) {
	$ln++;
	if ($ln==$p1) { $v1=$p1; print; }
	if ($ln==$p2) { $v2=$p2; print; }
	chomp; push(@cities, $_);

	# build Dijkstra distance and prev maps
	$dist[$ln] = 99999;
	$prev[$ln] = undef;
	push(@q, $ln);
}
die("both cities must be valid\n") if (!$v1 || !$v2);
close(K);
open(R, "roads") || open(R, "roads.txt") || die("roads: $!\n");
open(B, "out-B%") || die("out-B%: $!\n");
@roads = ( undef ); while(<R>) { chomp; push(@roads, $_); }
close(R);
$ee = 0; while(<B>) {
	chomp;
	($rn, $c1, $c2, $d) = split(/\t/, $_);
	$rn += 0; $c1 += 0; $c2 += 0; $d += 0;
	next if (!$d || !$c1 || !$c2 || !$rn);

	push(@edges, [ $rn, $c1, $c2, $d ]);
	push(@{ $a[$c1] }, [ $rn, $c2, $d, $ee ]);
	push(@{ $a[$c2] }, [ $rn, $c1, $d, $ee++ ]);
}
close(B);

$dist[$v1] = 0; while(scalar(@q)) {
	# find minimum distance in Q
	@q = sort { $dist[$a] <=> $dist[$b] } @q;
	$u = shift(@q);
	# find all arcs from $u
	foreach $arc (@{ $a[$u] }) {
		$v = $arc->[1];
		$alt = $dist[$u] + $arc->[2];
		if ($alt < $dist[$v]) {
			$dist[$v] = $alt;
			$prev[$v] = $u;
			$prou[$v] = $arc->[3];
		}
	}
}

$u = $v2; @s = ();
while($u != $v1 && defined($prev[$u])) {
	unshift(@s, $prou[$u]);
	$u = $prev[$u];
	last unless (defined($u));
}	
print join(' - ', @s), "\n";
$miles = 0; foreach(@s) {
	print $roads[$edges[$_]->[0]], " - ",
		$cities[$edges[$_]->[2]], " - ",
		$cities[$edges[$_]->[1]], " ",
		$edges[$_]->[3], " miles\n";
	$miles += $edges[$_]->[3];
}
print "total $miles miles\n";
We build arrays of
@cities
and
@roads
, and turn
B%()
into
@edges
and
@a
(for
arcs
) for expedience. We then walk down the nodes and build the tree in
@s
, noting which arc/edge was used in
@prou
so that we can look it up later, and then at the end walk the parent pointers back and do all the dereferencing to generate a human-readable route. As a check we also dump
@s
, which indexes
@edges
. Here's what it computes for Bishop to Pendleton, forward and reverse:
% route-dij 31 338
BISHOP CA 
PENDLETON OR 
399 - 398 - 397 - 396 - 395
US 395  - BISHOP CA  - CARSON CITY NV  172 miles
US 395  - CARSON CITY NV  - RENO NV  30 miles
US 395  - RENO NV  - LAKEVIEW OR  234 miles
US 395  - LAKEVIEW OR  - BURNS OR  139 miles
US 395  - BURNS OR  - PENDLETON OR  198 miles
total 773 miles
% route-dij 338 31
BISHOP CA 
PENDLETON OR 
395 - 396 - 397 - 398 - 399
US 395  - BURNS OR  - PENDLETON OR  198 miles
US 395  - LAKEVIEW OR  - BURNS OR  139 miles
US 395  - RENO NV  - LAKEVIEW OR  234 miles
US 395  - CARSON CITY NV  - RENO NV  30 miles
US 395  - BISHOP CA  - CARSON CITY NV  172 miles
total 773 miles
This is the same answer, and Dijkstra's algorithm further gives us a clue about one of the columns in
N%()
— the one which is invariably 32766. We already know from the plaintext portion of the compiled program that there are no other arrays, so the routing must be built in-place in the arrays that are present. We need an starting "infinite" value for each node within the range of a 16-bit signed integer, and no optimal path in continental North America would ever exceed that mileage, so this is the "infinite" value used to build the route into
N%()
. (It gets reset by reloading
MATS
if you select the option to start over after route generation.)
That said, it's almost certain that the program is
not
using an implementation of Dijkstra's algorithm. The queue starts out with all (in this case 487) nodes in it, making finding the lowest cost node in the queue on each iteration quite expensive on a little ~1.02MHz 6502. The usual solution in later implementations is a min-priority queue to speed up the search, but we already know there are no other arrays in memory to construct a faster heap or tree, so any efficiency gained would likely be unimpressive. Furthermore, it's not clear the author would have known about this approach (the earliest work on it dates to the late 1970s, such as Johnson [1977]), and even if he did, it still doesn't explain the meaning of the first two columns in
N%()
which aren't even used by this algorithm. After all, they're not there for nothing.
An alternative approach did exist at the time, however, published by Peter Hart, Nils Nilsson and Bertram Raphael in 1968. This algorithm came out of the Stanford Research Institute's Shakey project, the first general purpose robot intended to reason about its own actions (the photograph here is Shakey at SRI in 1972). The robot's height and proportions made it notoriously jittery in operation and led to its nickname.
To enable Shakey's autonomous motion about the lab required that it be able to solve its own path-finding requirements. Initially this was proposed using Graph Traverser, an ALGOL-60 program written at the University of Edinburgh, presumably by porting it to Lisp in which Shakey was programmed. Graph Traverser used a single evaluation function
E(x)
specific to the problem being examined to walk from a source to a target node, terminating when the target was reached. In the process it created a set of partial trees from the source to the target from which the lowest cumulative value of
E(x)
would ultimately be selected, starting with individual nodes where
E(x)
to some next immediate destination was locally smaller. Additionally, since it was now no longer required to construct a complete tree touching every possible node, the initial set of nodes considered could simply be the starting point. How the evaluation function was to be implemented was not specified, but a simple straight-line distance to the goal node would have been one logical means.
Raphael instead suggested that the function to be minimized be the
sum
of the distance to the goal node
and
the evaluation function, which was reworked as a
heuristic
. The heuristic thus provided a hint to the algorithm, ideally attracting it to the solution sooner by considering a smaller set of nodes. If the heuristic function was properly
admissible
— what Hart defined as never overstating the actual cost to get to the target — then this new algorithm could be proven to always find the lowest-cost path and greatly reduce comparisons if the solution converged quickly. Considering Graph Traverser as algorithm "A," this more informed
goal-directed
algorithm was dubbed "A*" (say it A-star).
If Roadsearch really is using A-star, at this point we don't know what the heuristic function is. (Note from the future: stay tuned.) Fortunately, a heuristic function that returns zero for all values is absolutely admissible because it will
never
overstate the actual cost. Although as a degenerate case doing so effectively becomes Dijkstra's algorithm, we'll still observe the runtime benefit of not having an initial queue potentially containing all possible nodes
and
being able to terminate early if the target is reached (which is always possible with Roadsearch's database).
To make the number of nodes more manageable for study, since we will also want to observe how the program behaves for comparison, we'll now consider a smaller routing problem that will be easier to reason about.
This is not an accurate map, and wasn't even accurate in 1985 because it doesn't contain Interstate 15E (today's Interstate 215), but this is largely how Roadsearch conceived of Southern California and the Mojave Desert. The routing we'll solve for is San Bernardino, California (375) to Needles, California (311), both within the largest county in the contiguous 48 United States (San Bernardino County, California). The optimal path is shown on the map as the blue path along "Interstate 15" and Interstate 40 and consists of five nodes (375 - 443 - 18 - 169 - 311), counting the start and goal. The white nodes are the blue nodes' immediate neighbours that are not part of the optimal route; all nodes contain their numbers so you can keep track. The highway edges between the numbers are also marked.
#!/usr/bin/perl

die("usage: $0 point_no_1 point_no_2\n") if (scalar(@ARGV) != 2);
$p1 = $ARGV[0]; $p2 = $ARGV[1];
die("wherever you go there you are\n") if ($p1 == $p2);

open(K, "cities") || open(K, "cities.txt") || die("cities: $!\n");
@cities = ( undef ); while(<K>) {
	$ln++;
	if ($ln==$p1) { $v1=$p1; print; }
	if ($ln==$p2) { $v2=$p2; print; }
	chomp; push(@cities, $_);

	# default gscore and fscore
	$gscore[$ln] = 99999;
	$fscore[$ln] = 99999;
}
die("both cities must be valid\n") if (!$v1 || !$v2);
close(K);
open(R, "roads") || open(R, "roads.txt") || die("roads: $!\n");
open(B, "out-B%") || die("out-B%: $!\n");
@roads = ( undef ); while(<R>) { chomp; push(@roads, $_); }
close(R);
$ee = 0; while(<B>) {
	chomp;
	($rn, $c1, $c2, $d) = split(/\t/, $_);
	$rn += 0; $c1 += 0; $c2 += 0; $d += 0;
	next if (!$d || !$c1 || !$c2 || !$rn);

	push(@edges, [ $rn, $c1, $c2, $d ]);
	push(@{ $a[$c1] }, [ $rn, $c2, $d, $ee ]);
	push(@{ $a[$c2] }, [ $rn, $c1, $d, $ee++ ]);
}
close(B);

@camefrom = (); @openset = ( $v1 );
$gscore[$v1] = 0;
$fscore[$v1] = 0; # heuristic of distance is 0 for the start
while(scalar(@openset)) {
	@openset = sort { $fscore[$a] <=> $fscore[$b] } @openset;
    print join(", ", @openset), "\n";
	$current = shift(@openset);
	last if ($current == $v2);

	foreach $n (@{ $a[$current] }) {
		$ni = $n->[1];
		$tgscore = $gscore[$current] + $n->[2];
		if ($tgscore < $gscore[$ni]) {
			$camefrom[$ni] = $current;
			$routefrom[$ni] = $n->[3];
			$gscore[$ni] = $tgscore;
			$fscore[$ni] = $tgscore + 0; # "heuristic"
			unless (scalar(grep { $_ == $ni } @openset)) {
				push(@openset, $ni);
			}
		}
	}
}

@s = ( ); while(defined($camefrom[$current])) {
	$route = $routefrom[$current];
	$current = $camefrom[$current];
	unshift(@s, $route);
}
print join(' - ', @s), "\n";
$miles = 0; foreach(@s) {
        print $roads[$edges[$_]->[0]], "($edges[$_]->[0]) - ",
                $cities[$edges[$_]->[2]], "($edges[$_]->[2]) - ",
                $cities[$edges[$_]->[1]], "($edges[$_]->[1]) ",
                $edges[$_]->[3], " miles\n";
        $miles += $edges[$_]->[3];
}
print "total $miles miles\n";
This is our A-star implementation using zero as the heuristic. You'll notice that much of the code is the same as the Dijkstra implementation. The key difference is that A-star tracks two functions,
f(x)
(realized here as
@fscore
) and
g(x)
(
@gscore
). The G-score for a given node is the currently known cost of the cheapest path from the start to that node, which we build from the mile length of each edge. The node's F-score is its G-score plus the value of the heuristic function for that node, representing our best guess as to how cheap the overall path could be if the path from start to finish goes through it. In this case, the F-score and G-score will be identical because the heuristic function in this implementation always equals zero. Also, because we're interested in knowing how many fewer nodes we've considered, we dump the open set on every iteration.
% route-dij 375 311
NEEDLES CA 
SAN BERNARDINO CA 
237 - 236 - 63 - 719
I 15  - SAN BERNARDINO CA  - US395/I15 CA  27 miles
I 15  - US395/I15 CA  - BARSTOW CA  44 miles
I 40  - BARSTOW CA  - I40/US95 CA  134 miles
I 40  - I40/US95 CA  - NEEDLES CA  12 miles
total 217 miles
% route-astar 375 311
NEEDLES CA 
SAN BERNARDINO CA 
375
443, 335, 274, 376
335, 274, 442, 18, 376
274, 442, 18, 376, 34
442, 18, 376, 171, 380, 34
18, 376, 171, 380, 15, 34, 31
376, 171, 380, 15, 34, 169, 262, 31
424, 171, 380, 15, 34, 169, 262, 31, 487
171, 380, 15, 34, 169, 262, 31, 487
380, 15, 34, 169, 275, 262, 31, 487
15, 34, 169, 275, 262, 31, 379, 487
34, 45, 169, 275, 262, 31, 379, 487
45, 169, 275, 262, 31, 379, 311, 487, 342
169, 275, 262, 31, 379, 311, 119, 487, 342
275, 311, 262, 31, 379, 119, 487, 342
311, 262, 31, 379, 336, 119, 487, 170, 342
237 - 236 - 63 - 719
I 15 (31) - SAN BERNARDINO CA (375) - US395/I15 CA (443) 27 miles
I 15 (31) - US395/I15 CA (443) - BARSTOW CA (18) 44 miles
I 40 (60) - BARSTOW CA (18) - I40/US95 CA (169) 134 miles
I 40 (60) - I40/US95 CA (169) - NEEDLES CA (311) 12 miles
total 217 miles
% route-astar 311 375
NEEDLES CA 
SAN BERNARDINO CA 
311
169, 251, 34
251, 34, 262, 18
168, 34, 262, 18
34, 262, 18, 475, 110
262, 18, 475, 110, 335, 342
454, 18, 475, 110, 335, 342, 427
18, 475, 110, 335, 342, 53, 427, 446
442, 443, 475, 110, 335, 342, 53, 427, 446
443, 475, 110, 335, 342, 15, 53, 427, 31, 446
475, 110, 375, 335, 342, 15, 53, 427, 31, 446
110, 375, 335, 342, 15, 53, 427, 31, 446
375, 335, 342, 15, 53, 427, 31, 446, 124, 247
719 - 63 - 236 - 237
I 40 (60) - I40/US95 CA (169) - NEEDLES CA (311) 12 miles
I 40 (60) - BARSTOW CA (18) - I40/US95 CA (169) 134 miles
I 15 (31) - US395/I15 CA (443) - BARSTOW CA (18) 44 miles
I 15 (31) - SAN BERNARDINO CA (375) - US395/I15 CA (443) 27 miles
total 217 miles
Although our queue dump shows we do wander a bit afield (a number of these nodes are more than one junction away, like 487 corresponding to Yuma, Arizona, or 380 being Santa Barbara, California), this is a much smaller set of nodes to consider than Djikstra and we still get the same answer, which Roadsearch also gets. Because we've observed Roadsearch seems to run the route backwards, I've provided the A-star dumps for both directions and you can see this simulation expands the set beyond the nearest neighbour in both cases.
Since we know the path must be constructed within the existing arrays and we have good evidence based on the "infinite" 32766 values that this storage array must be
N%()
, we'll instruct VICE to trap each integer array write to the range covered by
MATS
. (Trapping reads would also be handy but we'd go mad with the amount of data this generates.) We can get the value being written from $64/$65 (using the BASIC #1 floating point accumulator as temporary space) based on this code in the RTL:
.C:b094  A5 64       LDA $64
.C:b096  91 49       STA ($49),Y
.C:b098  C8          INY
.C:b099  A5 65       LDA $65
.C:b09b  91 49       STA ($49),Y
.C:b09d  4C 90 A0    JMP $A090
On each store we'll duly log the value in $64/$65 (remember it's big-endian) and the address it's being stored to. I wrote a one-off script to turn this string of writes into array offsets so we can understand how they relate to
N%()
, and then look them up in the tables so that we know which node and edge is under consideration. Remember, Roadsearch works this problem
backwards
starting with Needles.
# San Bernardino 375 to Needles 311

2e8e: 00 a8	N%(311,0)=168	NEEDLES CA 
2e8e: 00 a8	N%(311,0)=168	NEEDLES CA 
3478: 00 00	N%(311,1)=0	NEEDLES CA 
4636: 00 00	N%(311,4)=0	NEEDLES CA 	<destination>
3a62: 00 a8	N%(311,2)=168	NEEDLES CA 
404c: 00 01	N%(311,3)=1	NEEDLES CA 

2e16: 00 cf	N%(251,0)=207	KINGMAN AZ 
2e16: 00 cf	N%(251,0)=207	KINGMAN AZ 
3400: 7f fe	N%(251,1)=32766	KINGMAN AZ 
3400: 00 3c	N%(251,1)=60	KINGMAN AZ 
39ea: 01 0b	N%(251,2)=267	KINGMAN AZ 
45be: 00 3f	N%(251,4)=63	KINGMAN AZ  to NEEDLES CA  (60 miles) via I 40 
2c64: 00 a5	N%(34,0)=165	BLYTHE CA 
2c64: 00 a5	N%(34,0)=165	BLYTHE CA 
324e: 7f fe	N%(34,1)=32766	BLYTHE CA 
324e: 00 63	N%(34,1)=99	BLYTHE CA 
3838: 01 08	N%(34,2)=264	BLYTHE CA 
440c: 02 3c	N%(34,4)=572	NEEDLES CA  to BLYTHE CA  (99 miles) via US 95 
2d72: 00 9d	N%(169,0)=157	I40/US95 CA 
2d72: 00 9d	N%(169,0)=157	I40/US95 CA 
335c: 7f fe	N%(169,1)=32766	I40/US95 CA 
335c: 00 0c	N%(169,1)=12	I40/US95 CA 
3946: 00 a9	N%(169,2)=169	I40/US95 CA 
451a: 02 d0	N%(169,4)=720	NEEDLES CA  to I40/US95 CA  (12 miles) via I 40 
3f30: 00 02	N%(169,3)=2	I40/US95 CA 

2c44: 00 3b	N%(18,0)=59	BARSTOW CA 
2c44: 00 3b	N%(18,0)=59	BARSTOW CA 
322e: 7f fe	N%(18,1)=32766	BARSTOW CA 
322e: 00 92	N%(18,1)=146	BARSTOW CA 
3818: 00 cd	N%(18,2)=205	BARSTOW CA 
43ec: 00 40	N%(18,4)=64	I40/US95 CA  to BARSTOW CA  (134 miles) via I 40 
2e2c: 00 c3	N%(262,0)=195	LAS VEGAS NV 
2e2c: 00 c3	N%(262,0)=195	LAS VEGAS NV 
3416: 7f fe	N%(262,1)=32766	LAS VEGAS NV 
3416: 00 6d	N%(262,1)=109	LAS VEGAS NV 
3a00: 01 30	N%(262,2)=304	LAS VEGAS NV 
45d4: 02 3b	N%(262,4)=571	LAS VEGAS NV  to I40/US95 CA  (97 miles) via US 95 
3e02: 00 03	N%(18,3)=3	BARSTOW CA 

2f96: 00 16	N%(443,0)=22	US395/I15 CA 
2f96: 00 16	N%(443,0)=22	US395/I15 CA 
3580: 7f fe	N%(443,1)=32766	US395/I15 CA 
3580: 00 be	N%(443,1)=190	US395/I15 CA 
3b6a: 00 d4	N%(443,2)=212	US395/I15 CA 
473e: 00 ed	N%(443,4)=237	BARSTOW CA  to US395/I15 CA  (44 miles) via I 15 
2f94: 00 42	N%(442,0)=66	US395/CA58 CA 
2f94: 00 42	N%(442,0)=66	US395/CA58 CA 
357e: 7f fe	N%(442,1)=32766	US395/CA58 CA 
357e: 00 b2	N%(442,1)=178	US395/CA58 CA 
3b68: 00 f4	N%(442,2)=244	US395/CA58 CA 
473c: 02 0d	N%(442,4)=525	US395/CA58 CA  to BARSTOW CA  (32 miles) via CA 58 
4154: 00 04	N%(443,3)=4	US395/I15 CA 

2f0e: 00 00	N%(375,0)=0	SAN BERNARDINO CA 
2f0e: 00 00	N%(375,0)=0	SAN BERNARDINO CA 
34f8: 7f fe	N%(375,1)=32766	SAN BERNARDINO CA 
34f8: 00 d9	N%(375,1)=217	SAN BERNARDINO CA 
3ae2: 00 d9	N%(375,2)=217	SAN BERNARDINO CA 
46b6: 00 ee	N%(375,4)=238	US395/I15 CA  to SAN BERNARDINO CA  (27 miles) via I 15
From the above you can see where the program marks the order of each node and the accumulated mileage. Our running totals, most likely the F-score and G-score, for a given node
x
are in
N%(x,1)
and
N%(x,2)
, the length of the candidate edge is in
N%(x,1)
, the optimal edge for the node is in
N%(x,4)
, and the iteration it was marked in is recorded in
N%(x,3)
. (We count an iteration as any loop in which a candidate node is marked, which in this simple example will occur on every run through the open set.)
N%(x,0)
also looks like a distance, but it doesn't correlate to a highway distance. To construct the itinerary at the end, it starts with San Bernardino and then repeatedly walks the selected edge to the next node until it reaches Needles.
It's painfully obvious that compared to our models Roadsearch is considering a much smaller number of nodes (18, 34, 169, 251, 262, 311, 375, 442 and 443), counting the five in the optimal solution, and it duly converges on the optimal routing in just four iterations compared to
twelve
in our
best
case. I did look at its read pattern and found that
N%(x,0)
and
N%(x,1)
lit up a
lot
before they are later overwritten. These values are clearly important to computing whatever heuristic it's using, so I pulled out a few from across North America.
San Diego, CA       5710  20447
Bangor, ME          7820  12003
San Bernardino, CA  5952  20472
Bellingham, WA      8510  21375
Miami, FL           4499  13996
Medicine Hat, AB    8740  19313
Salina, KS          6779  17036
I stared at it for awhile until it dawned on me what the numbers are. Do you see what I saw? Here, let me plot these locations on a Mercator projection for you (using the United States' territorial boundaries):
The values are
coordinates
. The first column increases going north, and the second column increases going west. Indeed, in the very paper written by Hart et al., they suggest that the straight-line distance from the current node to the goal would make a dandy heuristic and now we can compute it!
The thing we have to watch for here is that the scales of the mileage and the coordinates are not identical, and if we use a simple distance calculation we'll end up clobbering the cumulative mileage with it — which would not only make it non-admissible as a heuristic, but also give us the wrong answer. To avoid that, we'll compute a fudge factor to yield miles from "map units" and keep the heuristic function at the same scale. Let's take San Diego, California to Bangor, Maine as a reference standard, for which
computing the geodesic distance
using
WGS 84
yields 2,696.83 miles from city centre to city centre as the crow flies. If we compute the straight-line distance between them using the coordinates above, we get 8703.63 "map units," which is a ratio of 3.23:1. To wit:
#!/usr/bin/perl

# divisor for distance
# if this is too low, it will overwhelm the mile distance to the goal
# computed from real-world straight-line distances
$fudge = 3.23;

# compute distance from target
sub h { my $xx = shift; my $yy = shift; $xx -= $vx; $yy -= $vy;
	return sqrt(($xx*$xx)+($yy*$yy)); }

die("usage: $0 point_no_1 point_no_2\n") if (scalar(@ARGV) != 2);
$p1 = $ARGV[0]; $p2 = $ARGV[1];
die("wherever you go there you are\n") if ($p1 == $p2);

open(K, "cities") || open(K, "cities.txt") || die("cities: $!\n");
$ln = 0; @cities = ( undef ); while(<K>) {
	$ln++;
	if ($ln==$p1) { $v1=$p1; print; }
	if ($ln==$p2) { $v2=$p2; print; }
	chomp; push(@cities, $_);
	# gscore and fscore set up from out-N%
}
die("both cities must be valid\n") if (!$v1 || !$v2);
close(K);
open(R, "roads") || open(R, "roads.txt") || die("roads: $!\n");
open(B, "out-B%") || die("out-B%: $!\n");
@roads = ( undef ); while(<R>) { chomp; push(@roads, $_); }
close(R);
$ee = 0; while(<B>) {
	chomp;
	($rn, $c1, $c2, $d) = split(/\t/, $_);
	$rn += 0; $c1 += 0; $c2 += 0; $d += 0;
	next if (!$d || !$c1 || !$c2 || !$rn);

	push(@edges, [ $rn, $c1, $c2, $d ]);
	push(@{ $a[$c1] }, [ $rn, $c2, $d, $ee ]);
	push(@{ $a[$c2] }, [ $rn, $c1, $d, $ee++ ]);
}
close(B);
open(N, "out-N%") || die("out-N%: $!\n");
$ln = 0; while(<N>) {
	chomp;
	# order and edge not used
	($x[$ln], $y[$ln], $fscore[$ln], $order, $edge) = split(/\t/, $_);
	# default gscore and fscore
	$gscore[$ln] = $fscore[$ln];
	$ln++;
}
close(N); $vx = $x[$v2]; $vy = $y[$v2];

@camefrom = (); @openset = ( $v1 );
$gscore[$v1] = 0;
$fscore[$v1] = 0; # heuristic of distance is 0 for the start

while(scalar(@openset)) {
	@openset = sort { $fscore[$a] <=> $fscore[$b] } @openset;
	print join(", ", @openset), "\n";
	$current = shift(@openset);
	last if ($current == $v2);

	foreach $n (@{ $a[$current] }) {
		$ni = $n->[1];
		$tgscore = $gscore[$current] + $n->[2];
		if ($tgscore < $gscore[$ni]) {
			$camefrom[$ni] = $current;
			$routefrom[$ni] = $n->[3];
			$gscore[$ni] = $tgscore;
			$h = &h($x[$ni], $y[$ni]) / $fudge;
			$fscore[$ni] = $tgscore + $h;
			unless (scalar(grep { $_ == $ni } @openset)) {
				push(@openset, $ni);
			}
		}
	}
}

@s = ( ); while(defined($camefrom[$current])) {
	$route = $routefrom[$current];
	$current = $camefrom[$current];
	unshift(@s, $route);
}
print join(' - ', @s), "\n";
$miles = 0; foreach(@s) {
	print $roads[$edges[$_]->[0]], "($edges[$_]->[0]) - ",
		$cities[$edges[$_]->[2]], "($edges[$_]->[2]) - ",
		$cities[$edges[$_]->[1]], "($edges[$_]->[1]) ",
		$edges[$_]->[3], " miles\n";
        $miles += $edges[$_]->[3];
}
print "total $miles miles\n";
We now have implemented an
h(x)
that for a given node
x
returns its straight-line distance from the target node. Let's try it out.
% route-hastar 375 311
NEEDLES CA 
SAN BERNARDINO CA 
375
335, 443, 274, 376
443, 34, 274, 376
18, 442, 34, 274, 376
169, 442, 34, 274, 376, 262
311, 442, 34, 274, 376, 262
237 - 236 - 63 - 719
I 15 (31) - SAN BERNARDINO CA (375) - US395/I15 CA (443) 27 miles
I 15 (31) - US395/I15 CA (443) - BARSTOW CA (18) 44 miles
I 40 (60) - BARSTOW CA (18) - I40/US95 CA (169) 134 miles
I 40 (60) - I40/US95 CA (169) - NEEDLES CA (311) 12 miles
total 217 miles
% route-hastar 311 375
NEEDLES CA 
SAN BERNARDINO CA 
311
169, 251, 34
18, 251, 34, 262
443, 442, 251, 34, 262
375, 442, 251, 34, 262
719 - 63 - 236 - 237
I 40 (60) - I40/US95 CA (169) - NEEDLES CA (311) 12 miles
I 40 (60) - BARSTOW CA (18) - I40/US95 CA (169) 134 miles
I 15 (31) - US395/I15 CA (443) - BARSTOW CA (18) 44 miles
I 15 (31) - SAN BERNARDINO CA (375) - US395/I15 CA (443) 27 miles
total 217 miles
Remembering that Roadsearch works it backwards, we converge on the same solution examining the same nodes in the same number of iterations (four). Further proof is if we dump the program's array writes for the opposite direction:
# Needles 311 to San Bernardino 375

2f0e: 00 a8	N%(375,0)=168	SAN BERNARDINO CA 
2f0e: 00 a8	N%(375,0)=168	SAN BERNARDINO CA 
34f8: 00 00	N%(375,1)=0	SAN BERNARDINO CA 
46b6: 00 00	N%(375,4)=0	SAN BERNARDINO CA 	<destination>
3ae2: 00 a8	N%(375,2)=168	SAN BERNARDINO CA 
40cc: 00 01	N%(375,3)=1	SAN BERNARDINO CA 

2ebe: 00 87	N%(335,0)=135	PALM SPRINGS CA 
2ebe: 00 87	N%(335,0)=135	PALM SPRINGS CA 
34a8: 7f fe	N%(335,1)=32766	PALM SPRINGS CA 
34a8: 00 30	N%(335,1)=48	PALM SPRINGS CA 
3a92: 00 b7	N%(335,2)=183	PALM SPRINGS CA 
4666: 00 16	N%(335,4)=22	PALM SPRINGS CA  to SAN BERNARDINO CA  (48 miles) via I 10 
2e44: 00 de	N%(274,0)=222	LOS ANGELES CA 
2e44: 00 de	N%(274,0)=222	LOS ANGELES CA 
342e: 7f fe	N%(274,1)=32766	LOS ANGELES CA 
342e: 00 40	N%(274,1)=64	LOS ANGELES CA 
3a18: 01 1e	N%(274,2)=286	LOS ANGELES CA 
45ec: 00 17	N%(274,4)=23	SAN BERNARDINO CA  to LOS ANGELES CA  (64 miles) via I 10 
2f96: 00 a6	N%(443,0)=166	US395/I15 CA 
2f96: 00 a6	N%(443,0)=166	US395/I15 CA 
3580: 7f fe	N%(443,1)=32766	US395/I15 CA 
3580: 00 1b	N%(443,1)=27	US395/I15 CA 
3b6a: 00 c1	N%(443,2)=193	US395/I15 CA 
473e: 00 ee	N%(443,4)=238	US395/I15 CA  to SAN BERNARDINO CA  (27 miles) via I 15 
2f10: 00 d7	N%(376,0)=215	SAN DIEGO CA 
2f10: 00 d7	N%(376,0)=215	SAN DIEGO CA 
34fa: 7f fe	N%(376,1)=32766	SAN DIEGO CA 
34fa: 00 6d	N%(376,1)=109	SAN DIEGO CA 
3ae4: 01 44	N%(376,2)=324	SAN DIEGO CA 
46b8: 00 ef	N%(376,4)=239	SAN BERNARDINO CA  to SAN DIEGO CA  (109 miles) via I 15 
407c: 00 02	N%(335,3)=2	PALM SPRINGS CA 

2c64: 00 58	N%(34,0)=88	BLYTHE CA 
2c64: 00 58	N%(34,0)=88	BLYTHE CA 
324e: 7f fe	N%(34,1)=32766	BLYTHE CA 
324e: 00 ad	N%(34,1)=173	BLYTHE CA 
3838: 01 05	N%(34,2)=261	BLYTHE CA 
440c: 00 15	N%(34,4)=21	BLYTHE CA  to PALM SPRINGS CA  (125 miles) via I 10 
4154: 00 03	N%(443,3)=3	US395/I15 CA 

2c44: 00 8e	N%(18,0)=142	BARSTOW CA 
2c44: 00 8e	N%(18,0)=142	BARSTOW CA 
322e: 7f fe	N%(18,1)=32766	BARSTOW CA 
322e: 00 47	N%(18,1)=71	BARSTOW CA 
3818: 00 d5	N%(18,2)=213	BARSTOW CA 
43ec: 00 ed	N%(18,4)=237	BARSTOW CA  to US395/I15 CA  (44 miles) via I 15 
2f94: 00 ac	N%(442,0)=172	US395/CA58 CA 
2f94: 00 ac	N%(442,0)=172	US395/CA58 CA 
357e: 7f fe	N%(442,1)=32766	US395/CA58 CA 
357e: 00 45	N%(442,1)=69	US395/CA58 CA 
3b68: 00 f1	N%(442,2)=241	US395/CA58 CA 
473c: 01 92	N%(442,4)=402	US395/CA58 CA  to US395/I15 CA  (42 miles) via US 395 
3e02: 00 04	N%(18,3)=4	BARSTOW CA 

2d72: 00 0b	N%(169,0)=11	I40/US95 CA 
2d72: 00 0b	N%(169,0)=11	I40/US95 CA 
335c: 7f fe	N%(169,1)=32766	I40/US95 CA 
335c: 00 cd	N%(169,1)=205	I40/US95 CA 
3946: 00 d8	N%(169,2)=216	I40/US95 CA 
451a: 00 40	N%(169,4)=64	I40/US95 CA  to BARSTOW CA  (134 miles) via I 40 
2e2c: 00 64	N%(262,0)=100	LAS VEGAS NV 
2e2c: 00 64	N%(262,0)=100	LAS VEGAS NV 
3416: 7f fe	N%(262,1)=32766	LAS VEGAS NV 
3416: 00 e3	N%(262,1)=227	LAS VEGAS NV 
3a00: 01 47	N%(262,2)=327	LAS VEGAS NV 
45d4: 00 ec	N%(262,4)=236	LAS VEGAS NV  to BARSTOW CA  (156 miles) via I 15 
3f30: 00 05	N%(169,3)=5	I40/US95 CA 

2e8e: 00 00	N%(311,0)=0	NEEDLES CA 
2e8e: 00 00	N%(311,0)=0	NEEDLES CA 
3478: 7f fe	N%(311,1)=32766	NEEDLES CA 
3478: 00 d9	N%(311,1)=217	NEEDLES CA 
3a62: 00 d9	N%(311,2)=217	NEEDLES CA 
4636: 02 d0	N%(311,4)=720	NEEDLES CA  to I40/US95 CA  (12 miles) via I 40
This routing proceeds in six iterations, just as we do, and once again the nodes we end up considering in our new A-star model are also the same. It also explains
N%(x,0)
— this is the straight-line distance and thus our heuristic, calculated (it's backwards) as the distance to the "start." For example, Palm Springs is indeed roughly 135 miles from Needles as the crow flies, again depending on your exact termini, whereas the western US 95/Interstate 40 junction is only about 11 miles. Note that this process overwrites the coordinate information, but we only needed it to compute the estimate; since we reload
MATS
entirely anyway after the user exits routing, it doesn't cause a problem.
It should also be obvious that this "fudge" divisor has a direct effect on the efficiency of the routine. While we're purportedly using it as a means to scale down the heuristic, doing so is actually just a backhanded way of deciding how strongly we want the heuristic weighted. However, we can't really appreciate its magnitude in a problem space this small, so now we'll throw it a big one:
drive
from San Diego (376) to Bangor (17). (I did myself drive from Bangor to San Diego in 2006, but via Georgia to visit relatives.)
This route requires a lot more computation and will also generate multiple useless cycles in which no node is sufficiently profitable, so I added code to our heuristic A-star router to explicitly count iterations only when a candidate node is marked:
$iter = 0; while(scalar(@openset)) {
	@openset = sort { $fscore[$a] <=> $fscore[$b] } @openset;
	print join(", ", @openset), "\n";
	$current = shift(@openset);
	last if ($current == $v2);

	$niter = $iter;
	foreach $n (@{ $a[$current] }) {
		$ni = $n->[1];
		$tgscore = $gscore[$current] + $n->[2];
		if ($tgscore < $gscore[$ni]) {
			$niter = $iter + 1;
			$camefrom[$ni] = $current;
			$routefrom[$ni] = $n->[3];
			$gscore[$ni] = $tgscore;
			$h = &h($x[$ni], $y[$ni]) / $fudge;
			$fscore[$ni] = $tgscore + $h;
			unless (scalar(grep { $_ == $ni } @openset)) {
				push(@openset, $ni);
			}
		}
	}
	$iter = $niter;
}
With our computed initial fudge factor of 3.23, we get this (again, worked backwards):
% route-hastar 17 376
BANGOR ME 
SAN DIEGO CA 
17
398, 469, 148
469, 409, 354, 148
[...]
376, 100, 145, 239, 366, 318, 518, 66, 360, 461, 374, 121, 485, 274, 448, 346, 245, 125, 44, 419, 256, 445, 15, 134, 437, 526, 427, 31
372 - 373 - 374 - 375 - 376 - 651 - 765 - 168 - 209 - 603 - 368 - 379 - 686 - 687 - 608 - 681 - 205 - 701 - 703 - 107 - 704 - 106 - 105 - 104 - 103 - 102 - 101 - 627 - 100 - 99 - 98 - 644 - 575 - 472 - 471 - 470 - 57 - 58 - 59 - 60 - 588 - 61 - 62 - 719 - 63 - 236 - 237 - 238
I 95 (100) - WATERVILLE ME (469) - BANGOR ME (17) 59 miles
I 95 (100) - AUGUSTA ME (12) - WATERVILLE ME (469) 23 miles
I 95 (100) - PORTLAND ME (348) - AUGUSTA ME (12) 58 miles
I 95 (100) - PORTSMOUTH NH (350) - PORTLAND ME (348) 49 miles
I 95 (100) - I95/I93(N) MA (231) - PORTSMOUTH NH (350) 53 miles
I 95 (100) - I90/I95 MA (216) - I95/I93(N) MA (231) 15 miles
I 90 (96) - I90/I95 MA (216) - I90/I395 MA (214) 33 miles
I 90 (96) - I90/I395 MA (214) - I86/I90 MA (209) 12 miles
I 86 (92) - I86/I90 MA (209) - HARTFORD CT (143) 46 miles
I 91 (97) - I91/CT9 CT (220) - HARTFORD CT (143) 12 miles
I 91 (97) - NEW HAVEN CT (313) - I91/CT9 CT (220) 27 miles
I 95 (100) - I95/I287 NY (223) - NEW HAVEN CT (313) 50 miles
I 95 (100) - I95/I287 NY (223) - I95/I87/I487 NY (230) 20 miles
I 478 (64) - I95/I87/I487 NY (230) - NEW YORK NY (315) 10 miles
I 78 (83) - NEW YORK NY (315) - I95/I78 NJ (228) 10 miles
I 78 (83) - I95/I78 NJ (228) - ALLENTOWN PA (6) 85 miles
I 78 (83) - ALLENTOWN PA (6) - I78/I81 PA (191) 52 miles
I 81 (87) - I78/I81 PA (191) - HARRISBURG PA (142) 23 miles
I 76 (81) - BREEZEWOOD PA (38) - HARRISBURG PA (142) 81 miles
I 70 (76) - BREEZEWOOD PA (38) - I70/I76(W) PA (182) 86 miles
I 70 (76) - I70/I76(W) PA (182) - WASHINGTON PA (466) 42 miles
I 70 (76) - WASHINGTON PA (466) - CAMBRIDGE OH (48) 77 miles
I 70 (76) - CAMBRIDGE OH (48) - COLUMBUS OH (72) 79 miles
I 70 (76) - COLUMBUS OH (72) - DAYTON OH (84) 71 miles
I 70 (76) - DAYTON OH (84) - INDIANAPOLIS IN (235) 104 miles
I 70 (76) - INDIANAPOLIS IN (235) - EFFINGHAM IL (97) 154 miles
I 70 (76) - EFFINGHAM IL (97) - I70/I55 IL (180) 79 miles
I 70 (76) - I70/I64 IL (181) - I70/I55 IL (180) 17 miles
I 70 (76) - I70/I64 IL (181) - ST. LOUIS MO (410) 3 miles
I 70 (76) - ST. LOUIS MO (410) - COLUMBIA MO (69) 125 miles
I 70 (76) - COLUMBIA MO (69) - KANSAS CITY MO (248) 126 miles
I 35 (52) - KANSAS CITY MO (248) - KS TPK/I35 KS (253) 113 miles
KS TPK (113) - WICHITA KS (474) - KS TPK/I35 KS (253) 83 miles
US 54 (176) - WICHITA KS (474) - PRATT KS (351) 78 miles
US 54 (176) - PRATT KS (351) - LIBERAL KS (267) 132 miles
US 54 (176) - LIBERAL KS (267) - TUCUMCARI NM (434) 208 miles
I 40 (60) - SANTA ROSA NM (382) - TUCUMCARI NM (434) 59 miles
I 40 (60) - ALBUQUERQUE NM (5) - SANTA ROSA NM (382) 115 miles
I 40 (60) - GALLUP NM (124) - ALBUQUERQUE NM (5) 139 miles
I 40 (60) - FLAGSTAFF AZ (110) - GALLUP NM (124) 184 miles
I 40 (60) - I40/US93 AZ (168) - FLAGSTAFF AZ (110) 123 miles
I 40 (60) - KINGMAN AZ (251) - I40/US93 AZ (168) 23 miles
I 40 (60) - NEEDLES CA (311) - KINGMAN AZ (251) 60 miles
I 40 (60) - I40/US95 CA (169) - NEEDLES CA (311) 12 miles
I 40 (60) - BARSTOW CA (18) - I40/US95 CA (169) 134 miles
I 15 (31) - US395/I15 CA (443) - BARSTOW CA (18) 44 miles
I 15 (31) - SAN BERNARDINO CA (375) - US395/I15 CA (443) 27 miles
I 15 (31) - SAN DIEGO CA (376) - SAN BERNARDINO CA (375) 109 miles
total 3324 miles in 328 iterations
And now for the real thing.
This was not a quick process.
I did run on it on the 128DCR for yuks as well as the emulated SuperCPU. With my stopwatch, a whole lot of patience and something else to do, it took 36 minutes and 44 seconds — which, when you think about everything it has to juggle, is actually remarkably
quick
. Both our simulation and the real program agree on the optimal route, as demonstrated by the cumulative mileage.
If we're doing the same (or at least overall similar) work as the native version, then we should observe the same maximum iterations marked in
N%(x,3)
. Interestingly, we do not: our simulation converged on the optimal route in 328 iterations, but the Commodore got it in 307. However, if we tune our simulation's fudge factor to 3.03, we also get it in 307.
Is there an optimal fudge divisor? We know the optimal route, so we'll run a whole bunch of simulations over the entire interval, rejecting ones that get the wrong answer and noting the iterations that were required for the right ones. In fact, we can do this generally for any routing by using the longhand Dijkstra method to get the correct answer and then run a whole bunch of tweaked A-stars compared with its routing after that.
In our simulation, stepping the fudge divisor over the interval from 0 inclusive to 4 by 0.001 increments, I ran six long haul drives in total, San Diego (376) to Bangor (17) and back, Bellingham, WA (24) to Miami, FL (291) and back, and then San Francisco, CA (377) to Washington, DC (465) and back. I then plotted them all out as curves.
The X-axis is the fudge divisor and the Y-axis is the number of iterations where lower is of course better. The zero deserves explanation: since you can't divide by zero, I made that the
h(x)=0
heuristic from above, which is always accurate and the least goal directed (and consequently requires the most iterations).
First off, there is no single fudge divisor that always yields the most optimal route for all of our test cases. Notice how much of the graph yields absolutely wrong answers (so nothing is plotted), and even in the interval between around 2.2 and 2.8 or so not all of the curves are valid. They all become valid around 3, which I enlarged in the inset on the left, and each one's iteration count slowly rises after that with the zero heuristic as more or less the upper asymptote. Except for the purple curve, however, 3 is not generally their lower bound.
Second, there is no single fudge divisor that always corresponds to the program's iteration count, which is 311 (17 to 376), 307 (376 to 17), 183 (291 to 24), 264 (24 to 291), 261 (377 to 465) and 220 (465 to 377). With the value of 3.03 from above, however, our simulation generally does
better
than the real thing, which is both gratifying for the purposes of pathfinding and frustrating for the purposes of modeling.
I did some quick distribution scans (well, it was quick in the SuperCPU emulator with warp on, anyway) to make sure there were no multiples or skipped numbers when it marked an iteration. Other than zero, which I put in there as a check that my BASIC one-liner was correct, no numbers are skipped and no iteration number appears more than once.
So my best guess for why they don't match up is mathematical precision. We're much more precise than the native Commodore version — we already know we're truncating values by storing them into an integer array, and rather than an expensive square root the distance heuristic is probably a quick estimate that gets worse at longer distances. (For that matter, the "fudge" divisor is very likely a straight-up three and the remainder is tossed.) Our short routes lined up nicely because any accumulated error was negligible; our long routes diverge because the poor 6502 is just trying to cope with the same math that this 64-thread POWER9 churns out effortlessly and more accurately. Since our simulation has a better-quality heuristic function, we get to the answer with less work in fewer cycles. Let's hear it for goal-directed pathfinding.
One last point on routing: you may have wondered how certain roads are struck so that the algorithm won't consider them. That turned out to be very simple; a snoop on the array range shows that it sets the selected segment, indicated by the cities on either end, to a mile length of 9,999 miles (altering
B%(x,3)
). That assures it will always have an insuperably high cost, yet be unlikely to overflow if it's involved in any calculations, and thus it will never be pulled from the open set for evaluation. The in-memory database is always reloaded from disk after the route is disposed of.
As our final stop in this article nearly as long as some of the drives we've analysed, we'll do my first 2005 long haul expedition along US Highway 395. This is a useful way to show how to add your own roads and what the program does with that, since not all of its segments are in the database.
US 395 (OpenStreetMap tiles used for this image) is well-known for traversing the California Eastern Sierra with access to Mammoth, Mono Lake and Death Valley, but actually extends much further all the way to British Columbia, via the eastern reaches of Oregon and Washington state and a small section in Nevada. Presently it is approximately 1,305 miles (2100km) long. It was established as a United States Numbered Highway in 1926 first as a small spur route from Spokane, Washington to the Canadian border, but in 1934 it was dramatically extended all the way to San Diego, California where it met the original alignment of US 101 downtown. Although US 395 never actually reached the Mexican border at any point, it was still called the Three Flags Highway for the three countries it ostensibly connected.
In 1969 the California Division of Highways truncated it to Hesperia, California, just south of Victorville, where it still terminates today at Interstate 15. (You saw this junction point on our map above.) The former freeway alignments today are mostly represented by I-15, I-215, I-15 (again) and CA 163, and a fair bit of its even earlier portions now bear Historic Route 395 signage. This particular sign is no longer up but I always liked the classic button copy appearance. US 395 is a special highway to me because my late father used it as a frequent jumping-off point for family vacation destinations, so it was a major part of my childhood and I always wanted to see the "end."
Among the many sights include the Manzanar War Relocation Center where more than 120,000 Japanese-Americans were forcibly interred, a stain upon the history of the United States during World War II (this is the 慰霊塔 Soul Consoling Tower cemetery monument built by stonemason Ryozo Kado in 1943),
the alpine Convict Lake,
the otherworldly beaches and tufa spires of Mono Lake, along the shores of which US 395 passes directly,
the 8,143' or so (2482m) Conway Summit overlook and the highest point along the highway in all three states, shown here in early spring when a lot of snow was still down,
the famous Reno Arch along old US 395 on Virginia Street in its brief Nevada sojourn,
the Abert Rim in Oregon and one of the highway's loneliest segments between Lakeview and Burns,
the Monroe Street Bridge, its earliest alignment in Spokane, Washington (a freeway alignment is being constructed on the east end of town),
and finally the very end of the end, the stub route BC 395 in Cascade, BC after US 395 officially terminates in Laurier, WA at the Canadian border, the only place where there is an "END" (or in this case, "ENDS"). Yes, these are all my pictures, collected over the years and several trips. Ask me before using them, please.
Unfortunately, the 1985 database won't get you there.
In the first place, it doesn't know where Laurier, WA (the small town at the Canadian border where it terminates) is. That place is here at the United States border crossing, as I photographed it in 2005:
In the second place, it's missing other segments. For example, if we try to go to Spokane, Washington, which is directly served by US 395 and would have been the shortest route (even in 1985), ...
... it diverges off in Reno along I-80 and goes up through Idaho, backtracking on I-90 into Spokane. The reason for this is very simple: it doesn't know US 395 extends beyond Pendleton, Oregon, so the shortest route is east and it makes sense it wouldn't know about any of its other smaller destinations either.
Fortunately Roadsearch's author anticipated this. So, as our last stop on this great giant article, it's finally time to enter the editor.
The map editor ("Roadmap Development System") is accessed from the main menu and displays the maximum capacity available, which seems to be based on the maximum array size in memory. It might have been possible to expand it even further as the compiled BASIC text ends well short of $a000, something I may explore some other time.
I mentioned earlier about "resetting" the disk after the previous owners have used it. If you want to simply use the program for generating routes, and don't intend to add any additional cities or roads, it suffices to simply change the counts in
M
, which will then cause the program to ignore any extraneous ones. Style points are added if you clear the records in the RELative files and turn them into nulls, though this isn't required. For the 1985 release, set
M
to
20 34 38 37 20 0D 20 37 37 35 20 0D 20 32 31 35 20 0D 20 39 39 39 39 20 0D
, which is (in PETSCII) 487 cities, 775 road segments, 215 road names and serial number 9999 or as you like. (Note this will not change the serial number in the editor, but with this patch you're only using the main program in any case.)
However, if you try to use a disk modified this way to
add
routes or cities, it will correctly recognize the new ones as new but erroneously find their old links in the arrays. That will not only get you unexpected residual road links to any new cities, but the links' presence can also confuse the program to such an extent it will end up in an infinite loop. In this case you'll need to delete these hanging links by patching
MATS
to null out the entries in
B%()
and
N%()
referring to city numbers greater than 487 and road numbers greater than 215 (remember that there are three arrays in that file and that multi-dimensional arrays run out each dimension before going to the next, meaning you can't just truncate it and stuff nulls on the end). This is simple to understand in concept but a little tedious to do, so I have left this as an exercise for the reader. Should I come up with a clean
MATS
myself, I will put it up somewhere if there is interest; for now we'll do our work on a well-loved copy which means that the city numbers you see here may not necessarily be the ones you get if you're following along at home.
US 395 between Pendleton, Oregon and Pasco, Washington did not follow exactly the route in 1985 that it does today. Previously it went along what is now Oregon State Route 37 leaving Pendleton via Holdman to the banks of the Columbia River. It then traveled with US 730 to intersect US 410 (now US 12) west of Walla Walla, Washington at Wallula Junction, where US 730 terminated (and still does). US 395 continued with US 410/US 12 into Pasco and then went north from there to US 10 and later I-90 at Ritzville on its way to Spokane.
In 1975 Interstate 80N (renumbered to I-84 in 1980) was completed through northern Oregon along the routing of US 30, shown here in a 1973 archival photo from the U.S. National Archives and Records Administration, and US 395 was rerouted to it, diverging from the Interstate in Stanfield, Oregon.
From there it proceeded north to the Columbia River gorge and intersected US 730 further west, then went east with it as before to US 12. This intermediate state is shown on this 1976 Donnelley atlas page, with the relevant portion highlighted. It was not until around 1986-7 when Interstate 82 was completed that US 395 was moved to I-82 instead as its present-day routing, leaving only a tiny residual overlap with US 730 east of Umatilla, Oregon.
The problem is that none of these locations have waypoints we can easily connect to.
As you can see, I-84 and US 12 are "straight shots" in this region; only I-90 has an intermediate point, at Ellensburg, which isn't even close to where we come in.
So our strategy will be this: we'll split I-84 between Portland and Pendleton at Stanfield, I-90 between Ellensburg and Spokane at Ritzville, and US 12 at Wallula Junction and Pasco between Walla Walla and Yakima. We'll then add new US 395 segments between Stanfield and Power City, OR (where it meets US 730), Power City to Wallula Junction, Pasco to Ritzville, Spokane to Laurier and finally a tag of British Columbia Provincial Route 395 between the international border and the now uninhabited town of Cascade, where it terminates at the Crowsnest Highway between Christina Lake and Grand Forks, BC.
Although the editor has several search options for checking the presence of cities and roads and connections thereof, it has only one option for data entry, namely "Develop Roadmap." We start with an existing city in the database to hang new routings from.
We'll first start with Walla Walla (we could have started with Yakima but I just love typing Walla Walla). It has two links, US 12 to Yakima and then another along Oregon State Route 11 to, as it happens, Pendleton. (This is actually Washington State Route 125 when it crosses the border, but anyway.) There is a "break" option that would seem perfect for this but I found it was more straightforward to simply create a new chain of cities and then delete the old one — it only objects if you try to create a new US 12 alignment also to Yakima, which would be silly.
We go ahead and enter the road (US 12), the mileage (29) and the new city (Wallula Jct, which I'm using for consistency with the database names). Mileage is integer-only, so I fudged in Google Maps and made sure the totals matched the original edge we'll be replacing. It recognizes this is a new city, and asks if we meant to create it, which we do.
The roadgeeks still reading this will have asked why I didn't co-sign US 395 over US 12 (because it was), and the answer is we can't give any one edge more than one existing route name. We could conceivably create a US 395 link and a US 12 link completely parallel to each other going to the same places with the same mileage, but this strikes me as a dodgy kludge and I don't know how it would behave with routing. Alternatively, we could create a new road "US 12/US 395" just for that segment, but as US 12 seems to be the "primary" route here and it's less work overall, that's what we'll use.
Conveniently, the editor immediately moves to Wallula Junction. We then add the link to Pasco in the same way ...
... and then from Pasco to Yakima. This totals up to the original edge just in case anything was depending on that.
Now at Yakima, we delete the old single 132-mile route back to Walla Walla ...
... leaving only our new composite route. Let's exit the editor and have the routing algorithm test it out. When you press M for the menu, it actually just goes back to the city prompt, from which you simply press RETURN to return to the editor's main menu. Only then are your changes "live": the program, very wisely, seems to take some care in ensuring updates are atomic. While it will perform writes to the RELative files immediately, it keeps all other changes strictly in memory and will not save
M
or
MATS
to disk until this point so that if the process gets aborted in the middle, the database remains internally consistent except for some harmless unreferenced RELative file records that can be overwritten later.
From the main program, we run a check route from Yakima to Walla Walla, and it indeed uses the new alignments to connect them with the mileage we entered in the order we expected.
An interesting question: we know the A-star algorithm uses the encoded coordinates in
N%()
as its heuristic, but we were never asked for anything like latitude or longitude. How, then, can it get this information for the new cities we just created? At this point I dumped the RELative files and the new
MATS
to find out, and it so happens that the new city gets the same coordinates as the one it was connected to: both Wallula Junction and Walla Walla get coordinates 8062 and 20802, which are Walla Walla's coordinates. As we are connecting a couple new cities together along US 12, they also get the same coordinates, up to Yakima which retains its own. If we extended from both sides into the middle it would probably have made the database slightly more accurate at the cost of some inconvenient dancing around. This would be a good idea if you needed to reconstruct or chop up a particularly long segment, for example.
I had also made an earlier call-forward that cities added from the editor sometimes don't have columns 4 or 5 set to zero. I can see this for the entries the previous owner entered, but all of mine ended up zero, so I'm not sure under what conditions that occurred. It doesn't seem to matter to the program in any case.
We next do the same thing for I-90, adding Ritzville ...
... and I-84, adding Stanfield.
We have our junctions in place, so now let's hang the new alignments, starting with Stanfield to Power City ...
... and Power City to Wallula Junction ...
... showing all our new connections.
We then add in Ritzville ...
... Spokane to Laurier, another new "city,"
... and finally Laurier to Cascade along BC 395, which prompts us not only about the new city but also the new route number.
We're done.
Now, for the acid test: we'll go from its southern terminus near Hesperia (which in the database is "city" number 443) and all the way to Cascade, just as I would have driven it if I'd driven it 20 years before I did.
I also ran it on the roadwarrior SX-64 still sitting in my wife's passenger seat. Both the SX-64 and the emulated SuperCPU got the same distance, 1,323 miles, which would be roughly accurate for the time (the routing is longer than the more direct present-day routing along I-82, and in Nevada US 395 has also moved to the completed I-580 between Reno and Carson City which has reduced it by another few miles). Did it use the new roads? Is the heuristic still sufficiently accurate?
So far so good — it doesn't deviate from Reno along I-80 now, so it obviously found the new shorter alignment.
It also walks along I-84 and US 12 as we intended it to ...
... and gets all the way to British Columbia ...
... just like I did. Boy, I really needed a shave that day. A number of years ago I managed to acquire a real, retired BC 395 shield and it's still on our living room wall.
And this is the end of this article's journey too. The fact that the existing
.d64
disk images for this program all show new routes had been added suggests they got non-trivial usage by their owners, which really speaks to the strengths of the program and what it could accomplish. While it's hardly a sexy interface, it's functional and straightforward, and clearly a significant amount of time was spent getting the map data in and tuning up the routing algorithm so that it could perform decently on an entry-level home computer. Unfortunately, I suspect it didn't sell a lot of copies, because there are few advertisements for Columbia Software in any magazine of the time and no evidence that the Commodore version sold any better than the Apple II release did. That's a shame because I think its technical achievements merited a better market reception then, and it certainly deserves historical recognition today. We take things like Google Maps almost for granted, but a program that could drive a highway map on your 1985 Apple or Commodore would truly have been fascinating.
As for me, I look forward to another long haul road trip in the future, maybe US 95 or US 101, or possibly reacquainting myself with US 6 which I drove in 2006 from Bishop to Cape Cod, Massachusetts. Regardless of where we end up going, though, we won't be taking the SX-64 with us — my wife has insisted on getting her seat back.
