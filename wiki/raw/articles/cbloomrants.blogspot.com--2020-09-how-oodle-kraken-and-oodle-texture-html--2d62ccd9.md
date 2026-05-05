---
title: "How Oodle Kraken and Oodle Texture supercharge the IO system of the Sony PS5"
url: "http://cbloomrants.blogspot.com/2020/09/how-oodle-kraken-and-oodle-texture.html"
fetched_at: 2026-05-05T07:01:49.198598+00:00
source: "Charles Bloom"
tags: [blog, raw]
---

# How Oodle Kraken and Oodle Texture supercharge the IO system of the Sony PS5

Source: http://cbloomrants.blogspot.com/2020/09/how-oodle-kraken-and-oodle-texture.html

The Sony PS5 will have the fastest data loading ever available in a mass market consumer device, and we think it may be even better
than you have previously heard.
What makes that possible is a fast SSD, an excellent IO stack that is fully independent of the CPU, and the Kraken hardware
decoder.  Kraken compression acts as a multiplier for the IO speed and disk capacity, storing more games and loading faster
in proportion to the compression ratio.
Sony has previously published that the SSD is capable of 5.5 GB/s and expected decompressed bandwidth around 8-9 GB/s,
based on measurements of average compression ratios of games around 1.5 to 1.  While Kraken is an excellent generic compressor,
it struggled to find usable patterns on a crucial type of content : GPU textures, which make up a large fraction of game
content.  Since then we've made huge progress on
improving the compression ratio of GPU textures, with
Oodle Texture
which encodes them such that subsequent Kraken compression can find patterns it can exploit.  The result is that we 
expect the average compression ratio of games to be much better in the future, closer to 2 to 1.
Oodle Kraken is the lossless data compression we invented at RAD Game Tools, which gets very high
compression ratios and is also very fast to decode.  Kraken is uniquely well suited to compress game content
and keep up with the speed requirements of the fast SSD without ever being the bottleneck.
We originally developed
Oodle Kraken
as software for modern CPUs.  In Kraken our goal was to reformulate
traditional dictionary compression to maximize instruction level parallelism in the CPU
with lots independent work running at all times, and a minimum of serial dependencies and branches.
Adapting it for hardware was a new challenge, but it turned out that the design decisions we had made to make Kraken great on
modern CPUs were also exactly what was needed to be good in hardware.
The Kraken decoder acts as an effective speed multiplier for data loading.  Data is stored compressed on the SSD
and decoded transparently at load time on PS5.  What the game sees is the rate that it receives decompressed data,
which is equal to the SSD speed multiplied by the compression ratio.
Good data compression also improves game download times, and lets you store more games on disk.
Again the compression ratio acts as
an effective multiplier for download speed and disk capacity.

A game might use 80 GB uncompressed, but with 2 to 1 compression it only take 40 GB on disk, letting you store twice as many games.
A smaller disk with better compression can hold more games than a larger disk with worse compression.
When a game needs data on PS5, it makes a request to the IO system, which loads compressed data from the SSD;
that is then handed to the hardware Kraken decoder, which outputs the decompressed data the game wanted to the RAM.
As far the game is concerned, they just get their decompressed data, but with higher throughput.  On other platforms, Kraken
can be run in software, getting the same compression gains but using CPU time to decode.  When using software Kraken, you
would first load the compressed data, then when that IO completes perform decompression on the CPU.
If the compression ratio was exactly 1.5 to 1, the 5.5 GB/s peak bandwidth of the SSD would
decompress to 8.25 GB/s uncompressed bytes output from the Kraken decoder.
Sony has estimated an average
compression ratio of between 1.45 to 1 and 1.64 to 1 for games without Oodle Texture, resulting in expected decompressed
bandwidth of 8-9 GB/s.
Since then, Sony has licensed our new technology
Oodle Texture
for all games on the PS4 and PS5.  Oodle Texture lets games encode their textures so that they are
drastically more compressible by Kraken, but with
high visual quality
.  Textures often make up the majority of content of large games and prior to Oodle Texture were difficult
to compress for general purpose compressors like Kraken.
The combination of Oodle Texture and Kraken can give very large gains in compression ratio.  For example on
a texture set from a recent game :
Zip
1.64 to 1
Kraken
1.82 to 1
Zip + Oodle Texture
2.69 to 1
Kraken + Oodle Texture
3.16 to 1
Kraken plus Oodle Texture gets nearly double the compression of Zip alone on this texture set.
Oodle Texture is a software library that game developers use at content creation time to
compile their source art into GPU-ready BC1-7 formats.  All games use GPU texture encoders, but previous encoders did not
optimize the compiled textures for compression like Oodle Texture does.
Not all games at launch of PS5 will be using Oodle Texture as it's a very new technology, but we expect it to be in the majority of
PS5 games in the future.  Because of this we expect the average compression ratio and therefore the effective IO speed to be even better
than previously estimated.
How does Kraken do it?
The most common alternative to Kraken would be the well known Zip compressor (aka "zlib" or "deflate").  Zip hardware decoders
are readily available, but Kraken has special advantages over Zip for this application.  Kraken gets more compression than Zip
because it's able to model patterns and redundancy in the data that Zip can't.  Kraken is also inherently faster to decode than Zip,
which in hardware translates to more bytes processed per cycle.
Kraken is a reinvention of dictionary compression for the modern world.  Traditional compressors like Zip were built around the
requirement of streaming with low delay.  In the past it was important for compressors to be able to process a few
bytes of input and immediately output a few bytes, so that encoding and decoding could be done incrementally.  This was needed
due to very small RAM budgets and very slow communication channels, and typical data sizes were far smaller than they are now.
When loading from HDD or SSD, we always load data in chunks, so decompressing in smaller increments is not needed.
Kraken is fundamentally built around decoding whole chunks, and by changing that
requirement Kraken is able to work in different ways that are much more efficient for hardware.
All dictionary compressors send commands to the decoder to reproduce the uncompressed bytes.  These are either a "match" to a
previous substring of a specified length at an "offset" from the current output pointer in the uncompressed stream,
or a "literal" for a raw byte that was not matched.
Old fashioned compressors like Zip parsed the compressed bit stream serially, acting on each bit in different ways, which requires
lots of branches in the decoder - does this bit tell you it's a match or a literal, how many bits of offset should I fetch, etc.
This is also creates an inherent
data dependency, where decoding each token depends on the last, because you have to know where the previous token ends to find
the next one.  This means the CPU has to wait for each step of the decoder before it begins the next step.
Kraken can pre-decode all the tokens it needs to form the output, then fetch them all at once and do one
branchless select to form output bytes.
Kraken creates optimized streams for the decoder
One of the special things about Kraken is that the encoded bit stream format is modular.  Different features of the encoder can
be turned on and off, such as entropy coding modes for the different components, data transforms, and string match modes.  Crucially
the Kraken encoder can choose these modes without re-encoding the entire stream, so it can optimize the way the encoder works
for each chunk of data it sees.  Orthogonality of bit stream options is a game changer; it means we can try N boolean options in
only O(N) time by measuring the benefit of each option independently.  If you had to re-encode for each set of options (as in traditional
monolithic compressors), it would take O(2^N) time to find the best settings.
The various bit stream options do well on different types of data, and they have different performance
trade offs in terms of decoder speed vs compression ratio.  On the Sony PS5 we use this to make encoded bit streams that 
can be consumed at the peak SSD bandwidth so that the Kraken decoder is never the bottleneck.  As long as the
Kraken decoder is running faster than 5.5 GB/s input, we can turn on slower modes that get more compression.  
This lets us tune the stream to make
maximum use of the time budget, to maximize the compression ratio under the constraint of always reading compressed bits from
the SSD at full speed.  Without this ability to tune the stream you would have very variable decode
speed, so you would have to way over-provision the decoder to ensure it was never the bottleneck, and it would often be wasting
computational capacity.
There are a huge number of possible compressed streams that will all decode to the same
uncompressed bytes.
We think of the Kraken decoder as a virtual machine
that executes instructions to make output bytes, and the compressed streams are programs
for that virtual machine.  The Kraken encoder is then like an optimizing
compiler that tries to find the best possible program to run on that virtual machine (the decoder).
Previous compressors only tried to minimize the size of the compressed stream without
considering how choices affect decode time.
When we're encoding for a software decoder, the Kraken encoder targets a blend of 
decode time and size.  When encoding for the PS5 hardware decoder, we look for the smallest
stream that meets the speed requirement.
We designed Kraken to inherently have less variable performance than traditional dictionary compressors like Zip.
All dictionary compressors work by copying matches to frequently occurring substrings; therefore they have a fast mode of
decompression when they are getting lots of long string matches, they can output many bytes per step of the decoder.
Prior compressors like Zip fall into a much slower mode on hard to compress data with few matches, where only one byte
at a time is being output per step, and another slow mode when they have to switch back and forth between literals
and short matches.  In Kraken we rearrange the decoder so that more work needs to be done to output long matches,
since that's already a super fast path, and we make sure the worst case is faster.  Data with short matches or no
matches or frequent switches between the two can still be decoded in one step to output at least three bytes per step.
This ensures that our performance is much more stable, which means the clock rate of the hardware Kraken decoder doesn't
have to be as high to meet the minimum speed required.
Kraken plus Oodle Texture can double previous compression ratios
Kraken is a powerful generic compressor that can find good compression on data with repeated patterns or structure.
Some types of data are scrambled in such a way that the compressability is hard for Kraken to find unless that data
is prepared in the right way to put it in a usable form.  An important case of this for games is in GPU textures.
Oodle Kraken offers even bigger advantages for games when combined with Oodle Texture.  Often the majority of game content is in BC1-BC7
textures.  BC1-7 textures are a lossy format for GPU that encodes 4x4 blocks of pixels into 8 or 16 byte blocks.
Oodle Kraken is designed to model patterns in this kind of granularity, but with previous BC1-BC7 texture encoders,
there simply wasn't any pattern there to find, they were nearly incompressible with both Zip and Kraken.  Oodle Texture
creates BC1-7 textures in a way that has patterns in the data that Kraken
can find to improve compression, but
that are not visible to the human eye
.
Kraken can see that certain structures in the data repeat, the
lengths of matches and offsets and space between matches, and code them in fewer bits.  This is done without expensive
operations like context coding or arithmetic coding.
It's been a real pleasure working with Sony on the hardware implementation of Kraken for PS5.  It has long been our
mission at RAD to develop the best possible compression for games, so we're happy to see publishers and platforms taking
data loading and sizes seriously.
