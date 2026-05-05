---
title: "RealTime Data Compression"
url: "http://fastcompression.blogspot.com/2018/01/zstandard-overview.html"
fetched_at: 2026-05-05T07:00:59.080374+00:00
source: "Yann Collet (LZ4/Zstd)"
tags: [blog, raw]
---

# RealTime Data Compression

Source: http://fastcompression.blogspot.com/2018/01/zstandard-overview.html

I recently realised that, while there is a
specification for Zstandard
, which describes in great details what is encoded where, there is no “overview” of the format, which would be neither too detailed nor too vague for programmers with a casual interest in data compression to understand its inner working. This blog post is an attempt to correct that.
Introduction
Zstandard
is an
LZ77-class
compressor, which primarily achieves compression by referencing from past data some segment of bytes identical to following bytes. Zstandard features a few other additional capabilities, but it doesn’t change the core formula. This construction offers several advantages, primarily speed related, especially on the decoder side, since a memory copy operation is all it takes to regenerate a bunch of bytes. Moreover, simple pointer arithmetic is enough to locate the reference to copy, which is as frugal as it gets both cpu and memory wise.
Blocks
Zstandard
format is block-oriented. It can only start decoding data when a first full block arrives (with the minor exception of uncompressed blocks). But it’s nonetheless stream-capable : any large input is automatically cut into smaller blocks, and decoding starts as soon as the first block arrives.
A block can have any size, up to a maximum of 128 KB. There are multiple reasons for such a limit to exist.
It’s not a concern related to initial latency for the first block, since the format allows this block to have
any
size up to maximum, so it can be made explicitly small whenever necessary.
The maximum block size puts an upper limit to the amount of data a decoder must handle in a single operation. The limit makes it possible to allocate a number of resources which are guaranteed to be enough for whatever data will follow.
There are also other concerns into the mix, such as the relative weight of headers and descriptors, time spent to build tables, local adaptation to source entropy, etc. 128 KB felt like a good middle ground providing a reasonable answer to all these topics.
It follows that a small source can be compressed into a single block, while larger ones will need multiple blocks.
The organisation of all these blocks into a single content is called a frame.
Frame
A frame will add a number of properties shared by all blocks in the current frame.
To begin with, it can restrict the maximum block size even further : largest maximum is 128 KB, but for a given frame, it can be defined to a value as small as 1 KB.
The frame can tell upfront how much data will be regenerated from its content, which can be useful to pre-allocate a destination buffer.
Most importantly, it can tell how much “past data” must be preserved in memory to decode next block. This is the “window size”, which has direct consequences on buffer sizes.
There are other properties stored there, but it’s not in the scope of this article to describe all of them. Should you wish to know more, feel free to consult the
specification
.
Once these properties are extracted, the decoding process is fairly straightforward : decompress data block after block.
Literals
A compressed block consists of 2 sections : literals and sequences.
Literals are the “left over” from LZ77 mechanism : remember, LZ77 compress next bytes by referencing an identical suite of bytes in the past. Sometimes, there is simply no such thing. Trivially, this is necessarily the case at the beginning of each source.
In such a  case, the algorithm outputs some “raw bytes”. These bytes are not compressed by LZ77, but they generally can be compressed using another technique :
Huffman compression
.
The principle behind Huffman is quite different : it transforms bytes into prefix codes using variable number of bits, and assign a low number of bits to frequent characters, while sacrificing infrequent characters with more bits.
The Huffman algorithm makes it possible to select the most efficient repartition of prefix codes.
When all bytes are equally present, it’s not possible to compress anything. But it’s generally not the case.
Consider a standard text file using ASCII character set, a whole set of byte values will not be present (>128), and some characters (like ‘e’) are expected to be more common than others (like ‘q’).
This is the kind of irregularity that Huffman can exploit to provide some compression for these left-over bytes. Typical gains range between 20% and 40%.
The literal section can be uncompressed (mostly when it’s very small, since describing a Huffman table cost multiple bytes), or compressed as a single stream of bits, or using multiple (4) streams of bits.
The multi streams strategy has been explained in
another post
, and is primarily designed for improved decoding speed.
All literals are decompressed into their own buffer. The buffer size is primarily limited by the block size, since in worst case circumstances, LZ77 will fail completely, leaving only Huffman to do the job.
Sequences
Obviously, we expect LZ77 to be useful. Its outcome is described in the second section, called “sequences”.
A block is rebuilt by a succession of sequences.
A “sequence” describes a number of bytes to copy from literals buffer, and then a number of byte to copy from past data, with an associated offset to locate its reference.
These values are of different nature, so they are encoded using 3 separated alphabets.
Each alphabet must be described, and there is a small header for each of them at the beginning of the section.
The compression technique used here is
Finite State Entropy
, a
tANS
variant, which offers better compression for dominant symbols.
Dominant symbols lose a lot of precision with Huffman, resulting in a loss of compression. They are unlikely to be present in “left over” literals, but for sequence symbols, the situation is less favourable.
FSE solves this issue, by being able to encode symbols using a fractional number of bits.
If you are interested in how FSE works, there is a
series of articles
which tries to describe it, but be aware that it’s fairly complex.
All sequence symbols are interleaved in a single bitstream, which must be read backward, due to ANS property of inverting directions for encoding vs decoding.
On 64-bits CPU, a single read operation is generally enough to grab all bits necessary to decode the 3 symbols forming the sequence. All it takes now is to apply the sequence : copy some bytes from the literals buffer, then copy some bytes from the past.
Decode next sequence. Rince, repeat. Stop when there is no more sequence left in the bitstream.
At this stage, whatever remains in the literals buffer is simply copied to complete the block.
And the decoder can move on to the next block.
Window
While decoding literals and sequence is a block-oriented job, that could be achieved in parallel within multiple blocks (expect a multi-threaded version in the future), the LZ copy operation is not.
It depends on previous blocks being already decoded, and is therefore serial in nature.
That’s where the frame header comes into play : it specifies how much past data the decoder must keep around to be able to decode next block.
The specification recommends to keep this value <= 8 MB, though it’s only a recommendation.
--ultra
levels for example go beyond this limit.
In most cases though, the decoder will not need that much. All levels <= 10 for example, which tend to be preferred due to their speed, require a memory budget <= 2 MB.
As could be guessed, using less memory is also good for speed.
Wrap up
That’s basically it. All these operations form the core of Zstandard compression format. There are a few more little details involved, such as the repeat offset symbols, shortened header with repeat tables and so on, which are described in the
specification
, but this description should be enough to grab the essence of the decoder.
The encoder is a bit more complex, not least because there are, in fact, multiple encoders.
The format doesn’t impose a single way to find or select references into the past. At every position into the file, there are always multiple possibilities to encode what’s next.
That’s why different strategies exist, providing different speed / compression trade off. Lower level are mapped onto LZ4, being very fast. Upper levels can be very complex, on top of very slow, offering improved compression ratio.
But the decoder remains always the same, preserving its speed properties.
