---
title: "Patcher Part 4 : Content-Defined Chunking"
url: "http://cbloomrants.blogspot.com/2023/09/patcher-part-4-content-defined-chunking.html"
fetched_at: 2026-05-05T07:01:47.342139+00:00
source: "Charles Bloom"
tags: [blog, raw]
---

# Patcher Part 4 : Content-Defined Chunking

Source: http://cbloomrants.blogspot.com/2023/09/patcher-part-4-content-defined-chunking.html

The alternative to rsync-style patch generation is to use content-defined chunking (CDC).
There's enough to say about CDC that I'll do a whole post just about finding the chunks and won't talk about
patching specifically here.
Content-defined chunking (CDC) is the idea of using the values of the bytes in the local area to choose
where chunk boundaries go.  By using only the values of the bytes, and nothing about their location in the file
or length of chunk, you should put boundaries in the same place in the old file and the new file.
You might start with a heuristic idea like, everywhere there is a run of 0 bytes, put a chunk boundary.
That actually works well on many types of files that in practice tend to have runs of 0 bytes between different
data regions (for example pdb and tar).  But it won't work in general, we need a method that will find
boundaries at the desired average chunk size on any type of data.
To do that we use hashes.  We compute a hash over a small run of bytes, typically where in the 16-64 byte length
range.  Note this should not be a hash over your whole desired block size.  You want it to be only on the local
region around a boundary so it is not affected by changes farther away in the file.  It needs to be a long enough
region to give you sufficient randomness in the hash and not be too effected by degeneracies (shorter hashes,
like say on only 4 bytes are too likely to hit repeating patterns of those 4 bytes).  It needs to be reasonably much
shorter than your desired minimum chunk length , perhaps 1/4 of the minimum chunk length, which is 1/4 of the desired
average chunk length.
The hash used to find boundaries can be rolling or not; that's kind of an implementation detail whether it's faster
to roll or not.  In my patcher I use the rolling hashes that work by shifting hash out of the machine word, so they
cover 32 or 64 bytes.
(see
Patcher Part 2 : Some Rolling Hashes
)
Assuming the hash is like a random number, then we can make chunks of the desired average length by checking the hash
against each byte against a threshold :
uint64 threshold = ((uint64)-1)/target_len;

  if ( hash <= threshold ) -> boundary
This is often shown differently for power of 2 target lens :
if target_len is power of 2
  target_len = 1<
<
target_len_bits

  when target_len_bits of hash are zero -> boundary

  eg.

  uint64 mask = (target_len-1);

  if ( (hash & mask) == 0 ) -> boundary

  or

  theshold = ((uint64)-1)>>target_len_bits;

  if ( hash & (~threshold) ) -> boundary

  which is the same as :

  if ( hash <= threshold ) -> boundary
so you can think of it as looking for N bits of hash being off, but the comparison against threshold works
just as well and allows arbitrary non-power-of-2 target lengths.
Often the hashes we use have better randomness in the high bits, so checking the high bits here may be
preferrable.
Another caveat is we don't want runs of zero bytes to trigger this boundary condition; eg. we don't want
the hash value to go to zero on runs of zero bytes, because they occur too often in real world data (vastly
more often than if the data source as random bytes).
Simple multiplicative Rabin-Karp does have this problem :

H = H * M + B;

if you roll in zero bytes B
the hash value H goes to zero
That can be addressed by using a stronger Rabin-Karp that either uses (B+C) or table[B].
(as is done in the two versions of "RollHash" that I propose
here
).
Okay, so we can scan our 32 or 64 byte window hash over the file, at every byte checking if it is a
boundary.  This gives us boundaries determined by the data and splits the file into content-defined chunks.
One regions where the data of two files is the same, the boundaries will be in the same place, so we will
match the chunks.
old file:

ABCDEFGHIJKLMNOP

new file :

AXYCDEFGHIJKLMNOP

as we scan over ABCD in the old and AXYCD in the new, we will be making different hash values.
Either new or old may trigger boundaries there.

Once the "XY" difference gets out of the hash window, we will be scanning over the same bytes in new
and old.

Then if a boundary is triggered, it will be at the same place.

Say for example FGHI is a byte pattern that corresponds to (hash <= threshold) and so makes a boundary

[ABCDE][FGHIJKLMNOP]
[AXYCDE][FGHIJKLMNOP]

we'll put a boundary at FGHI in both new and old.
So far, so good, but there are problems.
The histogram of lengths of fragments made with this scheme is not a nice dense distribution
around the average (like a Gaussian or something).  While the average is target_len, the most likely
length is 1, and the probability steadily decreases.  It's an exponential distribution, it has a long tail of significant
probability much longer than target_len.  Just because the average is target_len it may mislead you into
thinking we are mainly making lengths around target_len, but in fact we are making much shorter ones
and much longer ones.
(note: in an ideal world, the hash values are nearly random numbers, and then the chunk lengths generated
this way would be a true exponential distribution.  In the real world, there are lots of repeated patterns in data
that cause the hash to take particular values much more often than others, so it is not a very good random number
and the chunk lengths tend to be much much more clumpy than ideal.  If your data has long byte patterns that repeat,
this is simply not avoidable, no matter how good your hash is.)
To prevent us from making too many very short fragments, we can simply enforce a minimum chunk length,
and don't start looking for boundary conditions inside that minimum length region.
I like (target_len/4) for the minimum chunk length, but smaller also works (but at least 64 for the
rolling hashes I use).
Skipping ahead by minimum chunk length is not ideal.  It makes our boundary choice not entirely dependent on local
content.  (when we say we want context-determined chunk boundary points, we mean using only the *local* content in the
local 32 or 64 byte area).
a concrete example:

consider two files that are mostly in sync

at some point they are different and one of the files triggers a boundary condition
but the other doesn't

then they get back in sync
and there's a byte sequence on both that would be a boundary
but it's too close to the previous boundary in one file

file 1:

AB][XCDEFGAB  XCDEFG...
  ^ "XCD" sequence makes a boundary
             ^ will not make a boundary here because its within minimum chunk len

AB  YCDEFGAB][XCDEFG
  ^ files differ, no boundary here
             ^ "XCD" sequence makes a boundary

In the "GABXCDEFG" region both files are the same and we would like to have made a boundary in both
but we can't because of the non-local condition of the minimum chunk length

that is, the minimum chunk length constraint is causing a divergence later in the file which is non-local
While this is not ideal in theory, it seems to be not a big problem in practice.  (for it to be a problem in practice,
you would have to have lots of cases where the boundary trigger is being hit within the min chunk length distance,
which is far more often than expected, meaning you have a big breakdown of hash value randomness)
The next problem, which is a more serious problem in practice, is that you sometimes get very long chunks.
In fact they can get infinitely long (to the end of the file) if the data is degenerate and doesn't trigger
any chunk boundaries at all.
The most common case for very severe degeneries is long runs of zero bytes with simple hash functions; that
case is so common that I handle it explicitly (more on this later), but other degeneracies can happen with simple repeated byte
patterns that get into cycles of the hash value that never trigger the hash boundary condition.
To prevent chunks going too long, we enforce a maximum chunk length.
I like (target_len*4) for the maximum chunk length.  But if you just cut off at that length, you create a severe
non-content-determined boundary and it does in fact hurt matching quite a lot.  Say you had a new and old file that
get out of alignment due to an inserted byte, then have a long run of data that matches but doesn't trigger a boundary.
We don't just want to put a boundary at maximum chunk length, because it would be out of sync and cause failure to
match.  We need to put it in a place that is determined by the local data so that we get back in sync.
a concrete example:

old: ][XYXYABCDEFGHIJKLM...
new: ][XYXYXABCDEFGHIJKLM...

][ is a chunk boundary
new file had an X inserted

imagine the alphabetic sequence ABCDEFG... does not trigger a boundary condition in the hash.

if we just put a boundary after maximum chunk length :

old: ][XYXYABCDEFGHI][JKLM...
new: ][XYXYXABCDEFGH][IJKLM...

then not only do we fail to match the current chunk, but the next chunk starts out of sync.

Instead when we get to maximum chunk length, we want a data-determined cut so they get back in sync :

old: ][XYXYABCDEFGHI][JKLM...
new: ][XYXYXABCDEFGHI][JKLM...
Okay, so how do we do that?
The way that is natural is to use the MIN of the hash value over the interval.
We can motivate this.  Ideally we wanted to find chunk boundaries by finding the place where ( hash <= threshold ).
So if we ran into maximum chunk length it means there was no place with ( hash <= threshold ), all the hash values
were too high.  We wanted the first hash below threshold, there weren't any, so take the next lowest that was seen.
Because the min of the hash value is data-determined, hopefully it will be in the same place in the two files and
we will get back in sync.
(there are alternative schemes; for example you could just check ( hash <= threshold ) and increase threshold as you go.
Or after a power of 2 steps you could do threshold *= 2.  That's equivalent to requiring 1 less bit of hash be zero,
or to looking for target chunks that are half the length you were looking for (and thus more likely to trigger more often).)
The check for tracking the min can be combined with the check for the threshold, so this is quite efficient.
The full algorithm now, in pseudo-code is :
ptr is at start of a chunk

ptr += min_chunk_len;

for ( ptr up to max_chunk_len or end of buffer )
{
  h = RollHash(h,ptr);

  if ( h < min_hash_value )
  {
    if ( h <= threshold ) -> found a true boundary, done!

    min_hash_value = h;
    min_hash_value_ptr = ptr;
  }

  ptr++;
}

// no true boundary was found
// put a boundary at min_hash_value_ptr
Crucially for speed the branch check for min_hash_value is predictably rare.  After N steps, the chance of finding a new min is (1/N)
We step a byte at a time, rolling the hash over the small local window (32 or 64 bytes) to find boundaries, tracking min as we go.
Note that we can back up most of our work by going back to the min location.  We may have scanned way ahead up to max_chunk_len,
but the min is way back at the start of the chunk, we'll back up then scan again.  We can wind up doing the RollHash operation on
double (or so) the number of bytes in the file.  There is a possibility of schemes that avoid this
backtracking and repeating scans but it's not clear if that's worth any additional complexity, more investigation is needed.
In practice the min scheme works well.
Reference C code :
FindBoundary.cpp
