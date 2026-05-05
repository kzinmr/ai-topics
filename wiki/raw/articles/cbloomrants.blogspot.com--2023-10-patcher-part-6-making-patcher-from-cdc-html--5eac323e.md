---
title: "Patcher Part 6 : Making a patcher from CDC"
url: "http://cbloomrants.blogspot.com/2023/10/patcher-part-6-making-patcher-from-cdc.html"
fetched_at: 2026-05-05T07:01:47.357580+00:00
source: "Charles Bloom"
tags: [blog, raw]
---

# Patcher Part 6 : Making a patcher from CDC

Source: http://cbloomrants.blogspot.com/2023/10/patcher-part-6-making-patcher-from-cdc.html

We have a scheme to
cut our file into content-defined chunks
.
So let's use that to make a patcher.
For each file, we can construct a "signature" analogous to the
rsync signature
(which is a hash of chunks of constant length at regular intervals).
Our signature is all the CDC chunk locations, and then a hash of each chunk.  We will use the hash to look up
the contents of each chunk; it is not a hash we need to roll, and we don't need it to be cyptographic.  A good
hash to use here is
XXH3
.
CDC file signature :

vector of :
  {
    chunk length (as determined by CDC)
    hash of chunk (64,128, or 256 bits, eg. from XXH3)
  }

chunk position = sum of previous lengths
Basically we will look at these signatures and match chunks that have the same hash.  There are a few details to cover.
An optional step that I add in my patcher is to find long runs of zeros and give them their own chunk.
Long runs of zeros are something that happens in the real world quite a lot (eg. in PDB, EXE, tar, and Unreal's packages),
and isn't handled great by the rest of the system.  In the worst case, runs of zeros can be a degenerate point in the CDC
chunk-finding rolling hash.  While I wound up choosing the table-based rolling hash that does not have that degeneracy, 
it's easier to test hash options if that is not an issue (if you don't special case zero runs,
then whether or not a hash has a degeneracy on zeros affect dominates everything else about the hash).
The CDC signature system also doesn't handle it well when runs of zeros change length.  Say you have a "before" file that
has a zero run of 1000 bytes, and in the "after" file there's a zero run of 1001 bytes.  The CDC rolling hash may put a cut
point at the beginning of the zero run and one at the end, but the chunk containing the zero run is not the same before/after
so doesn't match.
By special casing the zero runs, we can send changes in the length of zeros without causing any patch mismatch.
In theory you might want to find other repeating patterns, but in practice zero runs are the important common case (many file formats use
zeros to pad elements to some alignment).  Note also
that the scan for run patterns must be extremely fast or it will slow down the patcher.  I use a minimum length zero run of at least 32 bytes,
which can be checked for by looking at 16-byte aligned positions for 16 bytes of zeros (any run of zeros of length >= 31 will contain
16 zeros at a 16-byte aligned position).
So my modified CDC scheme is :
Find long zero runs
Make "zero-run" chunks where there are long zero runs

In between zero run chunks, do the CDC rolling hash to find chunk boundaries
Make chunks from those boundaries
Compute the data hash (XXH3) of those chunks
Okay, so we have a "signature" of the previous & new files, let's make the patch.
First we take all the chunks of the "previous" file (or possibly multiple files if you want to patch from a previous install of multiple files),
we take the data hash of all non-zero-run chunks and add them to a hash table.
Some care is needed with the hash table to make sure this is fast.  Pre-size the hash table for the chunk count so it doesn't need to resize as
you add.  Use an "open addressing" reprobring hash table where the entries are stored directly in the table, no pointer indirection.  Do not use
the STL hash_map.  Make the entry as small as possible to reduce memory size.  Because the hashes we are inserting are already very well scrambled,
the hash table should not do any extra work to do additional munges of the hash.  Since our "key" is already a hash, don't compute or store a separate
hash of the key.  It also helps to prefetch ahead during the adds.  See
cblib
for one example of a good hash table, though something specialized to purpose will always
be best.
Note the same hash value may occur many times, if your file has chunks of data that repeat.  It is optional whether you add multiple occurance
of the same chunk contents (which occur at different locations) or not.  If you want to do a patcher that requires data locality, then you
might want to go ahead and add all occurances of the same chunk contents.  If not, then you can choose to only add a chunk once.  Also, it is
possible but very unlikely that different chunk contents could occur that have the same hash value, so you would get a collision on add but
with different contents; that can be ignored because it is so unlikely.
Next we scan through the "new" file.  For each chunk (that's not a zero-run chunk) we take the hash value and look it up in the hash table.
If found, this gives us a very likely chunk match.  I don't like the idea of just trusting the hash value, I want to make patches that I know
100% of the time are valid, so I then verify that the actual contents of those chunks are the same with a memcmp.
Something that you can optionally do before looking up each chunk hash is to see if the previous chunk match can be extended to cover the
current chunk.  Say you're in a region that is unchanged; you might have 1 MB or more of contiguous bytes that match the previous contents,
but the CDC chunk cutter has still cut that into 512 or 1024 byte chunks, depending on your target chunk length.  Rather than look up all
those chunks in the hash one by one, once you find the first one, you can just extend it across the whole shared data run.  This does not
have a significant effect on speed in my experience, but can help to reduce fragmentation of the match locations.
So, we now have all the chunks of the "new" file, and each tracks a location where it matches in the "previous" file, if any.  But so far
these matches are all at the CDC hash-determined split points.  The big improvement we can do is to extend those matches when possible.
Any time there is a repeated portion of data, we are likely to get CDC chunk boundaries somewhere inside that.
In order for a chunk to match, it must first have boundaries at the same data-determined place, and to find those
boundaries we use a rolling hash with a 64-byte window, so you generally will only start matching a region after at
least 64 bytes where the new/old are equal.  eg :
D = different
S = same

DDDDDDDSSSSSSSSSSSSSSSSSSSSSSSSSSSSSDDDDDDDDDDDDDDDD
  ][          ][           ][            ][    CDC chunk boundaries

chunks with any D different bytes won't match
in the SS run, the CDC boundaries ][ would be in the same place
  only after enough same bytes get into the rolling hash window to forget all D bytes
so that chunk will find a match

  ][ no match ][MMMMMMMMMMM][ no match   ][

initial patch only matches the middle portion :

DDDDDDDSSSSSSSSSSSSSSSSSSSSSSSSSSSSSDDDDDDDDDDDDDDDD
               MMMMMMMMMMMMM 

grow region while bytes match :

DDDDDDDSSSSSSSSSSSSSSSSSSSSSSSSSSSSSDDDDDDDDDDDDDDDD
            <- MMMMMMMMMMMMM ->
       MMMMMMMMMMMMMMMMMMMMMMMMMMMMM
You can fail to match the first and last target_chunk_length on any repeated portion, so we can gain a lot by expanding the match to include those.
To do that we just take any match region that borders a no-match region and see if we can step that boundary by matching more bytes.  You keep
stepping the boundary into the no match region, possibly until it disappears completely.  (for efficiency it's important not to do something like
a std::vector erase when a chunk is reduced to zero length; you can just treat zero-length regions as being "deleted" and clean them up in one pass
at the end).
You can take adjacent "no match" regions and merge them into a single larger region (again being careful about how you delete).
Another clean up step which you may want to do is to take adjacent match regions and see if they can be merged.  If they point to adjacent
areas of the source file, then they can be trivially merged into a longer match without checking any bytes.
(ie. if the first chunk matches from pos P in the source, and the next chunk matches at pos (P+length_of_preceding_chunk),
they can be trivially merged).  If they point to different areas, then you need to
check to see if the neighboring chunk also occurs at that different area.
Note that this requires both the "new" and "previous" files to be completely in memory so that we can do data matches in them, so rsync couldn't
do this because it is designed to work only incrementally on one file at a time.  You could extend the rdiff patch maker to do something similar
to this (growing matches beyond chunks) if you made it keep both files in memory.  Similarly you can do the CDC patch scheme more like rsync, and
just trust the hashes without verifying the data match, and not grow the match regions beyond the CDC split points.  For my use, I want an offline
patcher that makes the minimum possible patch size (given the chunk size limitation, etc.), so I prefer to require the old and new file in memory
and do these extra steps.
So we now have a set of chunks that are either {zero run, matched, no match}.  We can output a patch :
For all chunks :
write chunk length
write trinary type of chunk : {zero run, matched, no match}
if chunk is a zero run , done
if chunk is a match, write match-from location
if chunk is a non-match, write "length" bytes of payload data
Okay, that's our patch generater.  Let's compare the worst case big-O complexity to the rsync method, and also look at where we spend time in
practice.
On a file of length N

We scan over all the bytes looking for zero runs or CDC boundaries
CDC scan steps a rolling hash byte by byte, comparing against threshold and tracking min

CDC scan should typically stop after ~ chunk_len bytes, but can go as far as 4*chunk_len before we enforce a limit,
but we then go back to the location of the min value, which can be less than chunk_len bytes
So worst case we actually scan 16X over each byte.  This is very unlikely.  In practice 2X does occur.
This is O(N) in any case.

Once we have chunks, we hash them all with XXH3 or similar; this is O(N)

We do this same scan on both the previous & new file (unlike rsync, it's symmetric).

For target chunk len L, we make (N/L) chunks typically.
We add (N/L) hashes from the previous file to a hash table.  This is O(N/L).

On the new file we go over the (N/L) chunks and look each up in the hash table.  This is O(N/L).
The hash table lookup tends to be a cache miss as the hash table is unlikely to fit in cache.
We then verify the hash match is an actual byte match.  This is L bytes per chunk over (N/L) chunks, so O(N).

We then try to extend matched chunks if they border unmatched chunks.  This is L bytes per chunk over (N/L) chunks, so O(N). 
Try to merge neighboring matching chunks.  I think this is O(N*log(N)), but rarely takes any time in practice.
Essentially all the steps are O(N) and there are no steps that can have terrible degeneracies that make us much slower.
The worst spot where unfavorable data can make us slower is in the CDC hash boundary finding step.  If we are consistently
hitting the fragment length limit without finding a natural hash-determined cut point, and then being sent back to the location
of the "min", that does cause a significant increase in run time (maybe 2X slower).  As long as the data is making nice random
rolling hash values, that is statistically unlikely, but on degenerate data that has patterns which put you into cycles of the
rolling hash, it does occur.
The speeds in practice are :
Make "signature" for both files :  1.7 cycles/byte
  find zero runs and CDC roll hash boundaries : 1.5 cycles/byte
  hash chunks with XXH3 : 0.2 cycles/byte

Make patches from signatures : 0.5 cycles/byte  (around 500 cycles per chunk)
  add to hash table and look up hashes : 300 cycles/chunk
  verify bytes match and output patch record : 200 cycles/chunk

The signature phase is done on both the "previous" and "new" file, so 2N bytes
The "make patches" phase is done only on the "new" file, so N bytes
(not counting file IO).  Obviously a major issue for speed in the real world will be file IO and parallelism, which we will
address in the next part.
Aside on things that I currently do NOT do :
When you send a chunk in the patch that was not matched, you are sending the bytes in that chunk.  I do not attempt to compress those bytes.
As noted
back in part 1
the problem I am considering is "coarse
grain patching" , where the data I am working on I assume to be already compressor and/or encrypted in chunks, so that the raw bytes are not
compressible.  If that is not the case, then there are a variety of options for further compressing the "no match" raw bytes.  (perhaps the
optimal way would be to find the portion of the source file that they are most similar to, but don't exactly match, and send them as a
"fine grain" delta from that region; this is large problem space to explore).
I currently only consider patching the "new" file from the "previous" file (or multiple previous files in a file set).  You could certainly
also patch against preceding data in the new file, or from other files in the "new" set.  Because the CDC "signature" is symmetric, you
compute the same thing on the new and old files, the same kind of matching you do to find equal chunks in the previous set could be used to
find matches of chunks within your own file or against other files in the new set.
I currently assume that the working set fits in memory.  eg. on a typical 256 GB machine we can patch roughly 110 GB
of "previous" data to 110 GB of "new" data (leaving some room for hash tables and patch output).  If you need to be able
to generate patches on data sets larger than memory, that can still be done efficiently, but adds complication and is not addressed here.
