---
title: "Patcher Part 3 : How rsync works"
url: "http://cbloomrants.blogspot.com/2023/09/patcher-part-3-how-rsync-works.html"
fetched_at: 2026-05-05T07:01:47.398436+00:00
source: "Charles Bloom"
tags: [blog, raw]
---

# Patcher Part 3 : How rsync works

Source: http://cbloomrants.blogspot.com/2023/09/patcher-part-3-how-rsync-works.html

rsync is not a patcher; it is a method for transmitting differences of data over a network connection.
You can however build a patcher ("rdiff") on the rsync method, and that is commonly used, so I think it's
useful to look at how it works, because it gives us a standard reference point.
Because of its origin as a network transmission method, "rdiff" has limitations as a patcher which means it
does not find as good patches as possible, but it is perfectly reasonable within those limitations, so it
provides a good reference point for patch size.
To be clear "rsync" is the name of the algorithm and the differential network transmission protocol, "rdiff"
is the name of the tool that lets you use rsync on local files for patching.
rsync works by cutting the old/reference file into block_size chunks at block_size boundaries :
[block_size][block_size][block_size][...]
On each block it computes two hashes, one hash for lookup, and one to verify the data.
The lookup hash is a fast rolling hash (though at this stage we're not rolling it, since it is computed only at
block_size chunks).  The data verification hash is used
to check the contents of the block are the same.  This is needs to be a strong hash with a lot of bits (256 or so), because it is used
as the only check that a block has the same contents.  rsync gives different options for this hash.  This is a non-rolling hash.
(The hash for lookup is called "checksum1" or "weak sum" in rsync.  Hash to verify data is "checksum2" or "strong sum".
There are a couple different forks of rsync and they have been changed a lot.  In librsync, the data verification hash
is MD5, and the lookup hash is Rabin-Karp by default or Adler32-ish for backward compatibility.  In rsync the data verification
hash can be XXH3 or Blake3 for speed.  rsync calls these "checksums" but they are not, they are hashes.)
So for each block in the old file, we now have a lookup hash and a data hash.  This is called the "signature" of the old file.
rsync/rdiff does not get to use the whole contents of the old file, only the signatures.  This lets rsync send deltas even
if the sender does not have the old file that the client has.  The client can compute the signature of its old file, send that
back to the sender, and the sender transmits the deltas using only the signature and new file.
To make the patch, rsync then scans the new version of the file.  It has to do this byte by byte :
Compute a rolling hash of the "lookup hash" over block_size bytes.  (eg. Rabin-Karp or Adler32-ish)

At each byte :

Roll in+out the next byte to the "lookup hash".

Find the "lookup hash" in the signature set of the old file.
If it is found, then compute the "data hash" of the new file for this chunk (eg. XXH3 or MD5)
If that is the same, we matched the block!
  advance byte pointer ahead + block_size

else no match
advance byte pointer ahead +1
Note that this computing the rolling hash and looking it up in the hash table must be done at every byte, it cannot just be
done at block_size chunks, because the new file may have insertions or deletions relative to the old file, so you must handle
blocks moving.
rsync does not actually check that blocks exactly match at all.  It relies on the data hashes being equal as a substitute for
checking the block bytes.  AFAICT this means it is possible for rsync to make incorrect patches (though vanishingly unlikely,
as it uses strong 256 bit hashes for the data hash).
The worst case for rsync missing possible patches is on data of the form :
[] indicate block_size chunks

old: [ABCDEF][GHIJKL]
new: [*BCDEF][GHIJK*]
That is, one byte in each block changed, but there is a (2*block_size-2) run of bytes that are the same and could have been matched,
but rsync fails to find them.
We can say that, given the parameter "block_size" , rsync is "perfect" for matches longer than (2*block_size-2).  ("perfect" meaning that we
ignore missing matches due to bad luck hash collisions, as noted in part 1).
The time complexity of rsync is typically O(N) when you are not getting unlucky.
To compute the signature :

on N bytes
(N/block_size) blocks
compute two hashes of block_size bytes is O(block_size)

time = (N/block_size)*O(block_size) = O(N)

To find the patch :

If you are failing to find any matches :

at each of N bytes :
you roll the hash 1 step
even though the rolling hash is over block_size bytes, this is only an O(1) step
look up in the hash table and find nothing
advance 1 byte

this is O(N) over the whole file
In the failing to find any matches case, while it is O(N) and therefore not a bad scaling, it is doing N hash table
lookups, so it is quite slow (hash table lookups typically means a cache miss, so this is 200-300 cycles per byte).
If you are finding matches :

for (N/block_size) steps :
compute the good data hash in O(block_size)
step ahead block_size bytes
recompute the lookup hash

this is net O(N)
In the case of finding all matches (or nearly so), rsync/rdiff is reasonably fast and not worse than other algorithms.
There is however, a bad case (the "getting unlucky").  If you get "lookup hash" hits but then fail to match the good data hash, you can
wind up computing the data hash over "block_size" bytes, but then only stepping ahead by 1 byte.  This make you
O(N*block_size) which is very slow.
As noted, the rdiff/rsync scheme only uses the signatures and only matches whole blocks, because the delta generation
step does not get to look at the original file at all.  This was done because of the original of rsync as a network
transmission scheme.  In our case, we care about patch generation on a machine that has the old and new version of
the file, so we can do better by making use of that.  Details on how exactly in the next parts.
Memory use of rsync is quite low.  Both signature generation and patch generation just scan through the file
sequentially, so they can use a sliding IO buffer that is not proportional to file size.  Patch generation does
require the whole signature set in memory to look up in the hash table.  Depending on the size of the data verification
hash, this is something like 64 bytes per block; for a 1024 block size that's 16X less than the size of the old file
set.  The entire old file is not needed in memory because matches are only against whole blocks using the data hash.
add: "rdiff" is built on "librsync" which implements the same algorithm as "rsync" but is an independent code base.
librsync defaults to rabinkarp for the rolling hash, rsync only does the adler32-ish checkum.  librsync only does md5
for the strong hash, rsync has Blake3 and XXH3 options.  rsync has special cases for runs of zeros (checksum1 == 0)
and tries to make matches sequential when possible, I think librsync does not.  Lots of small differences but the
fundamentals are the same.
