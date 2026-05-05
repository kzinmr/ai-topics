---
title: "cbloom rants: Patcher Part 1"
url: "http://cbloomrants.blogspot.com/2023/09/patcher-part-1.html"
fetched_at: 2026-05-05T07:01:47.892533+00:00
source: "Charles Bloom"
tags: [blog, raw]
---

# cbloom rants: Patcher Part 1

Source: http://cbloomrants.blogspot.com/2023/09/patcher-part-1.html

I will descibe in this series the patcher that I wrote which is able to find "perfect" patches at full IO-bound speed; eg. 5 GB/s on
current gen SSD's.  (more on what "perfect" means exactly later).  I wanted to sanity check some of the patch sizes I was seeing from
other sources, so I wanted my own reference results to know what was possible.  At first I didn't care about speed, I just wanted
correct patch sizes to have a known ideal patch size to check against, but working on our huge data sets it became a practical necessity
to have reasonable speed, and then I became curious if fully IO bound speed was possible, and in fact it is.  That is, all CPU work
required for patch generation can be run in parallel with IO such that the critical path is at full IO speed.  This proves that any claim
that poor patch generators have to approximate in order to be efficient is not true, you can in fact generate "perfect" patches at the
maximum possible speed.
Part 1 will cover some background and context.
First of all, what do I mean by a "patcher" here?
Given a previous version of a data set, and a new version of data set, generate a patch file which can be applied to the old version
to generate the new version.
The data set may either be a single file, or a set of a files.  The patch may be either one file at a time, or refering to the entire
previous set.  I will often talk about patching from an "old file" to a "new file", but I mean more generally a set of files or other data.
Here I am looking at only coarse grain patching of large data sets.  That is, finding reasonably long chunks of data that repeat.  There is
a different but related problem of fine grain patching of smaller files (see aside later) which I will not address in this series.  One reason for
that is the data I care about has already been chunked and compressed/encrypted.  That is, while my patcher does not explicitly assume this,
the data we work with has often been cut into chunks, and those chunks have been compressed and/or encrypted.  This means the patcher will
only be able to find large-scale replication of whole chunks, because shared strings within chunks are scrambled by the compression/encryption,
so even if they do exist, they are impossible for us to find.
If your data was not previously compressed/encrypted, there would be further shared fine-grained strings within chunks.  You could do something
like use a coarse-grain patcher to find large-scale reused blocks, then do fine-grain patching within the blocks where there is no large match.
That is outside the scope of this series.
For this series, I assume the patcher can use the entire previous version of the data when patching.  In practice that might not be possible,
because the previous data doesn't fit in RAM (at the patch-applying time), you might want to limit where you can match from.  The typical scheme would be to use a sliding
winding of say 1 GB or so around the current file position where you can match anything, and matches outside that range would have to be bigger,
because they require a separate file IO.  I didn't look at finding patches under these contraints, but they are relatively easy to add.
What do we mean by "perfect" patches?  I assume that the patcher has some block size parameter.  It should find all repetitions of that block
size or larger, with probability of missing them only equal to the probability of random hash collisions.  That is, we will be finding repeats
using hashes of blocks, and there is some small chance of failing to find matches when hashes collide, but that is rare and we consider that to
be an acceptable unlikely deviation from the true smallest possible patch.  That is, there should be no other deficiency in the patch generator
that makes it miss out on repeated data other than hash collisions and the block size.  Furthermore, the block size should be able to be set
as small as 1024 bytes without compromising the performance or efficacy of the patch generator.
I use this meaning of "perfect" here because a patcher that finds all possible matches except a few unlucky ones is the best we can ask for
practically (given the desire of low memory use and fast speeds), and for all practical purposes finds 99.9% of patchable bytes.  This is to
distinguish from some patchers which use inherently bad broken algorithms and fail to find matches that they definitely could.
For concreteness, a typical data set I looked at would have 100 GB of previous data, 100 GB of new data.  So running at full 5 GB/s IO speed the 
patcher must take at least 40 seconds just to load the previous and new data.  My patcher took 44 seconds to generate the patch sizes.  These data
sets were typically cut into 64 KB chunks (before compression/encryption ; after compression the chunk sizes are smaller and variable).  We will
assume in this series that we don't know much about the data we are patching; that is we work on blind binary data, we don't have information like
where the compression/encryption chunk boundaries are.  It is important to put your compression/encryption chunk boundaries in the right place;
that is, don't mix together unrelated data, don't mix headers in with payloads, don't put fields that frequently change (like versions or dates) in
with payload data that rarely changes, etc.
For example, we might have some previous version of a data set that's like :
{A}{B}{C}{D}{E}{F}

where each {X} indicates a chunk of data of variable size.
As far as the patcher knows, this is just one big binary file, but in fact it was made from these logical chunks,
which are independently compressed+encrypted.  Maybe those chunks correspond to different resources in a video game.
Then the new version is :
{A}{B}{E}{X}{C2}{F}
some chunks are the same, some data has been inserted, and chunk C has changed only slightly.
If the chunks were not compressed+encrypted, then we should find small similarities between the original {C}
and the new version {C2} , but with compression+encryption they will usually change completely, so we will not
find anything useful for patching there.
The perfect patch size should be
size of {X} + {C2}
and the coarse grain patcher should find all the other bytes as references to the old file.
Aside: fine grain patching is an interesting topic, but is outside the scope of what I wanted to look at here.
In fine grain patching, you would have much smaller data sets, and you assume they are not previously compressed/encrypted.  (if they were, you
would want to undo the encryption+compression, find patches, then reapply it).  That means you can look for small repeated strings, and in
addition to just finding string repeats you might also do things like pre-train your statistical model on the old data, etc.  You can use
the previous version in various ways to predict the new version and reduce the size of the delta transmitted.
Fine grain patching can make good patches when the data has been scrambled around, even when coarse grain patching finds very few large
matches.
The simplest classic way of doing fine grain patching is just to use an off the shelf data compressor, and preload the model/dictionary of
the data compressor with the previous version of the file, and then compress the new version.  This is obviously far from optimal in various
ways (for example, it doesn't model the fact that data in the new file is more likely to match data in a similar position in the old file, or
near where other nearby matches were; it favors matching from the end of the old file, which is clearly wrong), but it's often good enough and
is very easy.  Any compressor that supports a precondition or dictionary preload can be used this way for patching.
Even for compressors that don't actually support it, you can still measure how they would do simply by compressing the concatenation
{old file + new file} and then subtracting off the size of just compression {old file}.
The first compressor that I heard of really pushing this method was
ACB by Leonid A. Broukhis
.
Inspired by that I put support in
PPMZ
.
Quite similar to ACB, and very amenable to this kind of reference compression is
LZSA (LZ-Suffix-Array)
.
Like ACB, LZSA is quite slow for adaptive sliding window encoding but can be pretty fast with static data (the whole previous file),
so can be nice for this kind of application.
Some specialized fine grain patchers exist, such as
bsdiff
and
Courgette
which is
specialized for executables.
Matt Mahoney's zpaq
has built-in support for deltas against previous versions using
coarse grain patching (finding large repeated chunks).  AFAIK it does not do fine grain patching.
As I was writing this I discovered that
ZStd has added a "patch-from" option
to explicitly
support this kind of usage, providing the previous version of the file to preload the LZ dictionary.
ZStd's patch-from is the most modern and well supported fine grained patcher, so I recommend that if it fits your needs.
For completeness see also my old post :
Patches and Deltas
for links to a bunch of
other patchers ("xdelta").  I've tried xdelta, jdiff, and many others, and found them to be very poor, I do not recommend them.
Coarse grain patchers all fundamentally work on some block size which is specified as a parameter.  I typically use 1024 or 512.
My patcher starts to work worse at block lengths below 512, because of certain assumptions.  One is the memory use per block is ~32 bytes;
with very short block lengths that becomes comparable to the size of the file.  Another is that I don't handle hash collisions of blocks,
so they need to be long enough that random hash function collisions are very rare.  Another is that I use a rolling hash that is hard-coded
to 64 bytes (machine word size) to scan for boundaries; the block length needs to be at least 4X this rolling hash window, so 256 is the
minimum.  Another is the way block size cuts are made from the rolling hash value relies on enough bytes getting in to get good randomness,
with shorter blocks you wind up making forced cuts in unnatural places, which leads to failed matches. (more on this later).
The net result is that coarse grain patching works well down to ~512 byte blocks or so.  Below that you would need to change to fine
grain patching.  Fine grain patching, OTOH, has the drawbacks that memory use is typically much higher, and/or it uses more approximate
string matchers such that it can fail to find long matches that the coarse grain patcher would find.  It is of course also typically much
much slower.
Next up, digging into details of how coarse grain patchers work.
