---
title: "RealTime Data Compression"
url: "http://fastcompression.blogspot.com/2016/04/working-with-streaming.html"
fetched_at: 2026-05-05T07:00:59.862122+00:00
source: "Yann Collet (LZ4/Zstd)"
tags: [blog, raw]
---

# RealTime Data Compression

Source: http://fastcompression.blogspot.com/2016/04/working-with-streaming.html

Streaming, an advanced and very nice processing mode that a few codecs offer to deal with small data segments. This is great in communication scenarios. For lossless data compression, it makes it possible to send tiny packets, in order to create a low-latency interaction, while preserving strong compression capabilities, by using previously sent data to compress following packets.
Ideally, on the encoding side, the user should be able to send any amount of data, from the smallest possible (1 byte) to much larger ones (~~MB). It's up to the encoder to decide how to deal with this. It may group several small fields into a single packet, or conversely break larger ones into multiple packets. In order to avoid any unwanted delay, a "flush" command shall be available, so that the user can decide it's time to send buffered data.
On the other side, a compatible decoder shall be able to cope with whatever data was sent by the encoder. This obviously requires a bit of coordination, a set of shared rules.
The zip format
defines a maximum copy distance (32 KB). Data is sent as a set of blocks, but there is no maximum block size (except non-compressed blocks, which must be <= 64 KB).
A compatible zip decoder must be able to cope with these conditions. It must keep up to 32 KB of previously received data, and be able to break decoding operation in the middle of a block, should it receive a block way too large to fit into its memory buffer.
Thankfully, once this capability is achieved, it's possible to decode with a buffer size of
32 KB + maximum chunk size
, with "chunk size" being the maximum size the decoder can decode from a single block. In general, it's a bit more than that, in order to ease a few side-effects, but we won't go into details.
The main take-away is : buffer size is
a consequence of
maximum copy distance, plus a reasonable amount of data to be decoded in a single pass.
zstd
's proposition is to reverse the logic : the size of the decoder buffer is set and announced in its frame header. The decoder can safely allocate the requested amount of memory. It's up to the encoder to respect this condition (otherwise, compressed data is considered corrupted).
In current version of the format, this buffer size can vary from 4 KB to 128 MB. It's a pretty wide range, and crucially, it includes possibilities for small memory footprint. A decoder which can only handle small buffer sizes can immediately detect and discard frames which ask for more than its capabilities.
Once the buffer size is settled, data is sent as "blocks". Each block has a maximum size of 128 KB. So, in theory, a block could be larger than the agreed decoder buffer. What would happen in such case ?
Following zip example, one solution would be for the decoder to be able to stop (and then resume) decoding operation in the middle of a block. This obviously increases decoder complexity. But the benefit is that the only condition the compressor has to respect is a max copy distance <= buffer size.
On the decoder side though, it's only one side of the problem. It's no point having a very small decoding buffer if some other memory budget dwarf it.
The decoding tables are not especially large : they use 5 KB by default, and could be reduced to half, or possibly a quarter of that (but with impact on compression ratio). Not a big budget.
The real issue is the size of the incoming compressed block. A compressed block must be smaller than its original size, otherwise it will be transmitted in uncompressed format. That still makes it possible to have a (128 KB - 1) block size. This is extremely large compared to a 4 KB buffer.
Zip's solution is that it's not necessary to receive the entire compressed block in memory in order to start decompressing it. This is possible because all symbols are entangled in a single bitstream, which is read in forward direction. So input buffer can be a fraction of a block. It simply stops when there is no more information available.
This will be difficult to imitate for zstd : it has multiple independent bitstreams (between 2 and 5) read in
backwards
direction.
The backward direction is unusual, and a direct consequence of using
ANS entropy
: encoding and decoding must be done in reverse direction.
FSE
solution is to write forward and read backward.
It could have been a different choice : write backward, read forward, as suggested by
Fabian Giesen
. But it makes the encoder's API more complex : the destination buffer would be filled from the end, instead of the beginning. From a user perspective, it breaks a few common assumptions, and become a good recipe for confusion.
Alternatively, the end result could be
memmove()
to the beginning of the buffer, with a small but noticeable speed cost.
But even that wouldn't solve the multiple bitstreams design, which is key to
zstd's speed advantage
. zstd is fast because it manages to keep multiple cpu execution units busy. This is achieved by reducing or eliminating dependencies between operations. At some point, it implies bitstream independence.
In a zstd block, literals are encoded first, followed by LZ symbols. Bitstreams are not entangled : each one occupy its own memory segment.
Considering this setup, it's required to access the full content block to start decoding it (well, more precisely, a few little things could be started in parallel, but it's damn complex and not worth the point here).
Save any last-minute breakthrough on this topic, this direction is a dead-end : any compressed block must be received entirely before starting its decompression.
As a consequence, since small decoding buffer is a consequence of constrained memory budget, it looks logical that the size of incoming compressed blocks should be limited too, to preserve memory.
The limit size of a compressed block could be a dedicated parameter, but it would add complexity. A fairly natural assumption would be that a compressed block should be no larger than the decoding buffer. So let's use that.
(PS : another potential candidate would be
cBlockSize <= bufferSize/2
, but even such a simple division by 2 looks like a recipe for future confusion).
So now, the encoder side enforces a maximum block size no larger than the decoding buffer. Fair enough. Multiple smaller blocks also means multiple headers, so it could impact compression efficiency. Thankfully,
zstd
includes both a "default statistics" and an experimental "repeat statistics" modes, which can be used to reduce header size to zero, and provide some answer to this issue.
But there is more to it.
Problem is, amount of data previously sent can be any size. The encoder may arbitrarily receive a "flush" order at any time. So each received block can be any size (up to maximum), and not necessarily fill the buffer.
Hence, what happens when we get closer to buffer's end ?
Presuming the decoder doesn't have the capability to stop decompression in the middle of a block, the next block shall not cross the limit of the decoder buffer. Hence, if there are 2.5 KB left in decoder buffer before reaching its end, the next block maximum size must be 2.5 KB.
It becomes a new condition for the encoder to respect : keep track of decoder buffer fill level, ensure to never cross the limit, stop at exact end of the buffer, and then restart from zero.
It looks complex, but the compressor knows the size of the decoder buffer : it was specified at the beginning of the frame. So it is manageable.
But is that desirable ?
From an encoder perspective, it seems better to get free of such restriction, just accept the block size and copy distance limits, and then let the decoder deal with it, even if it requires a complex capability of "stop and resume" in the middle of a block.
From a decoder perspective, it looks better to only handle full blocks, and require the encoder to pay attention to never break this assumption.
Classical transfer of complexity.
It makes for an interesting design choice. And as v1.0 gets nearer, one will have to be selected.
-------------------------------------------
Edit
: And the final choice is :
Well, a decision was necessary, so here it is :
The selected design only impose distance limit and maximum block size to the encoder , both values being equal, and provided in the frame header.
The encoder doesn't need to track the "fill level" of the decoder buffer.
As stated above, a compliant decoder using the exact buffer size should have the capability to break decompression operation in the middle of a block, in order to reach the exact end of the buffer, and restart from the beginning.
However, there is a trick ...
Should the decoder not have this capability, it's enough to extend the size of the buffer by the size of a single block (so it's basically 2x bigger for "small" buffer values (<= 128 KB) ). In which case, the decoder can safely decode every blocks in a single step, without breaking decoding operation in the middle.
Requiring more memory to safely decompress is an "implementation detail", and doesn't impact the spec, which is the real point here.
Thanks to this trick, it's possible to immediately target final spec, and update the decoder implementation later on, as a memory optimization. Therefore, it won't delay v1.0.
