---
title: "Patcher Part 8 : Summary"
url: "http://cbloomrants.blogspot.com/2023/10/patcher-part-8-summary.html"
fetched_at: 2026-05-05T07:01:47.656015+00:00
source: "Charles Bloom"
tags: [blog, raw]
---

# Patcher Part 8 : Summary

Source: http://cbloomrants.blogspot.com/2023/10/patcher-part-8-summary.html

In this series I described how to build a patcher that can make very good (near minimal size) "coarse grain" patches, and run near maximum possible speed
(IO limited).
Posts in the series :
cbloom rants- Patcher Part 1 - Introduction with context and defining terminology and goals
cbloom rants- Patcher Part 2 - Some Rolling Hashes
cbloom rants- Patcher Part 3 - How rsync works
cbloom rants- Patcher Part 4 - Content-Defined Chunking
cbloom rants- Patcher Part 5 - Aside for some proofs
cbloom rants- Patcher Part 6 - Making a patcher from CDC
cbloom rants- Patcher Part 7 - Patcher File IO and Parallelism
To wrap up, some real performance and patch sizes :
Generating patch sizes for three different Fortnite releases on my ThreadRipper :
patcher run time : 20.533 s total_io_bytes=99.326 gB speed=4.837 gB/s
patcher run time : 23.461 s total_io_bytes=100.165 gB speed=4.269 gB/s
patcher run time : 18.366 s total_io_bytes=77.022 gB speed=4.194 gB/s
These times show the total time and net speed (net speed = total bytes over total time), eg. including startup allocs and shutdown frees.
These are times just to generate patch sizes ("patcher s" mode), not including writing the patch output files.
The three times are for three different data shapes; the first is lots of loose files, patching one file to one previous file, the
second is lots of loose files but patching each new file from all previous files, and the first is patching big aggregate tar against
previous.  (those three styles are interesting because they multi-thread differently).
For sanity check, I verified patch size against rdiff :
On a single 38 GB Fortnite package file :

rdiff with block size set to 1024 :

rdiff_delta fn2401_pakchunk10-XboxOneGDKClient.ucas fn2410_pakchunk10-XboxOneGDKClient.ucas

fn2401_2410_xb1_rdiff_delta_bs1024     927,988,455

vs my patcher with default block size (1024) :

patch size : 903386162 / 38553104896 bytes = 2.34%
Our patch is 2.6% smaller than rdiff.
Our patch size should (almost) always beat rdiff by a little because of match extension.
("almost" because there is some randomness and luck in the hash-based CDC splits and chunk matches, so you can get unlucky).
Another rdiff comparison with timing :
On my Intel laptop ; Core i7-8750H CPU @ 2.20GHz , 6 cores (12 hyper)

On a 3.5 GB PDB , block sizes 1024 :

rdiff : fnpdb.rdiff_bs1024     807,066,347
rdiff timerun: 127.729 seconds

patcher : patch size : 792333063 / 3498102784 bytes = 22.65%
patcher run time : 2.681 s total_io_bytes=6.996 gB speed=2.609 gB/s

(patcher "s" mode, only generating patch size not writing output)
Again we're similar size but slightly smaller, as expected.  Rdiff takes 127.7 seconds to our 2.7 seconds, so yes good patches
can be made much faster than current tools.  To be fair, many of the techniques we use could also be applied to speed up rdiff;
the rdiff/rsync algorithm is not inherently a terrible way to generate patches and could be ~10X faster than it is now.
Also rdiff here is writing the signature file to disk, and actually writing the patch file, while my run is writing no output to
disk, so it's not apples-to-apples, and of course we are multi-threaded but rdiff is not.  So it's by no means intended as a
direct comparison of the maximum theoretical speed of the rsync algorithm vs the cdc algorithm, which should be much closer.  The
point is sort of that all those practical things to make a fast patcher are important and surmountable.
For the record a full profile run of the above 2.7s PDB patcher run :
On my Intel laptop ; Core i7-8750H CPU @ 2.20GHz , 6 cores (12 hyper)

m:\test_data\patcher>patcher s fnpdb\FortniteClient.pdb fnpdb\FortniteClient.pdb.2 -p
patcher built Oct 10 2023, 09:41:23
args: patcher s fnpdb\FortniteClient.pdb fnpdb\FortniteClient.pdb.2 -p
got option : do_profile
detected disk type = ssd
cores_hyper = 12 physical = 6 large_pages = true
io_limit_count=2 cpu_limit_count=12
make patch from fnpdb\FortniteClient.pdb to fnpdb\FortniteClient.pdb.2
FortniteClient.pdb.2: read_and_make_sourcefile: 3498102784 start...
FortniteClient.pdb.2: read_and_make_sourcefile: 3498151936 start...
patch size : 792333063 / 3498102784 bytes = 22.65%
 patch bytes matched :  70053394 / 3498102784 bytes =  2.00%
 patch bytes nomatch : 792232278 / 3498102784 bytes = 22.65%
 patch bytes zeros   : 2635817112 / 3498102784 bytes = 75.35%
patcher run time : 2.681 s total_io_bytes=6.996 gB speed=2.609 gB/s
SimpleProf                       :seconds    calls     count :   clk/call  clk/count
patcher                          : 2.6714        1         1 :   10661.5m  10661.54m
 makepatch_one_file              : 2.6314        1         1 :   10502.1m  10502.10m
  read_and_make_sourcefile_twice : 2.3262        1         1 : 9283832.7k   9283.83m
   read_and_make_sourcefile      : 4.5463        2         2 : 9072217.6k   9072.22m
    make_fragments               : 2.3581      677  6996987k : 13901373.8       1.35
     make_fragments_sub          : 1.7625     5068  4351168k :  1387917.2       1.62
    ComputeWholeFileHash         : 0.3554        2         2 :  709214.9k 709214.94k
  makepatch_one_file_sub         : 0.1575        1  3498102k :  628657.0k       0.18
   make_base_fragment_hash       : 0.1192        1         1 :  475762.4k 475762.35k
  write_one_file_patch           : 0.1444        1 792333063 :  576399.6k       0.73
The bulk of the time is in the "read and make signature" CDC phase which does the boundary scan and hashes
each fragment.  This can be done on the two input files at the same time so the net CPU time for it is 4.5463s
(read_and_make_sourcefile), but the wall time is 2.3262s (read_and_make_sourcefile_twice).
Other applications :
We've looked at patching from just one "previous" file (or set of previous files) to one "new" file, but there
are other applications of these techniques.  You can do partial transmission like rsync, you can do file system dedupe
like ZFS.
I use "patcher s" size mode just as a fuzzy binary diff.  If the patch size needed to get from file A to file B is small,
it tells me they are very similar.
The way we use "patcher" at Epic is currently primarily for analysis.  On most of our important platforms, the actual patches
are made by the platform distribution tools, which we cannot control, so we can't actually generate our own patches.  We use
"patcher" to see what the minimum possible patch size would be with a perfect patch tool, so we can see how much of the patch
size is from actually changed content vs. bad platform patch tools.  We can also use "patcher" to output a CSV of change locations
so that we can identify exactly what content actually changed.
Another application I've used is grouping similar files together for compression (which I call "orderer").
The CDC "signature" provides a quick way
to identify files that have chunks of repeated bytes.  When making a multi-file solid archive, you gain a lot by
putting those files close to each other in the archive.  To do that you just take the N files and compute signatures,
then try to put them in a linear order to maximize the number of chunk hashes that are equal in adjacent files.
Note the rsync/rdiff method works okay (similar big-O speed to CDC method) when doing file-to-file patching, 
but the CDC method has a big advantage here
of being totally symmetric, the expensive work is per-file not per-compare, so when doing a group of N files
where they can all match each other, it is a huge win.
You could also use these techniques to find long-distance matches within a huge file which can be used to make sure you find LZ matches (for something
like Kraken or ZStd) at very long range (which can otherwise get lost when using something like a cache table matcher, since very old/far
matches will get replaced by closer ones).  (but realistically if you are doing super huge file compression you should have something specialized,
which maybe finds these big repeats first, and then compresses the non-repeating portions in independent pieces for multi-threading)
(I believe that "zpaq" does something like this, but haven't looked into it).
