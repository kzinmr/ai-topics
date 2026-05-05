---
title: "Huffman revisited part 5 : combining multi-streams with multi-symbols"
url: "http://fastcompression.blogspot.com/2015/10/huffman-revisited-part-5-combining.html"
fetched_at: 2026-05-05T07:00:59.888508+00:00
source: "Yann Collet (LZ4/Zstd)"
tags: [blog, raw]
---

# Huffman revisited part 5 : combining multi-streams with multi-symbols

Source: http://fastcompression.blogspot.com/2015/10/huffman-revisited-part-5-combining.html

In
previous article
, a method to create a fast multi-symbols Huffman decoder has been described. The experiment used a single bitstream, for simplicity. However, earlier investigation proved that
using multiple bitstreams
was a good choice for speed on modern OoO (Out of Order) cpus, such as Intel's Core. So it seems only logical to combine both ideas and see where they lead.
The previous multi-streams format produced an entangled output, where each stream contributes regularly to 1-in-4 symbols, as shown below :
Multi-Streams single-symbol entangled output pattern
This pattern is very predictable, therefore decoding operations can be done in no particular order, as each stream knows at which position to write its next symbol.
This critical property is lost with multi-symbols decoding operations :
Multi-Streams multi-symbols entangled output pattern (example)
It's no longer clear where next symbols must be written. Hence, parallel-streams decoding becomes synchronization-dependent, nullifying multi-streams speed advantage.
There are several solutions to this problem :
- On the decoder side, reproduce regular output pattern, by breaking multi-symbols sequence into several single-symbol write operations. It works, but cost performance, since a single decode now produces multiple writes (or worse, introduce an unpredictable branch) and each stream requires its own tracking pointer.
- On the encoder side, take into consideration the decoder natural pattern, by grouping symbols exactly the same way they will be regenerated. This works too, and is the fastest method from a decoder perspective, introducing just some non-negligible complexity on the encoder side.
Ultimately, none of these solutions looked particularly attractive. I was especially worried about introducing a "rigid format", specifically built for a single efficient way to decode. For example, taking into consideration the way symbols will be grouped during decoding ties the format to a specific table construction.
An algorithm created for a large number of platforms cannot tolerate such rigidity. Maybe some implementations will prefer single-symbol decoding, maybe other ones will select a custom amount of memory for decoding tables. Such flexibility must be possible.
Final choice was to remove entanglement. And the new output pattern becomes :
Multi-Streams multi-symbols segment output pattern (example)
With 4 separate segments being decoded in parallel, the design looks a lot like classical multi-threading, but at micro-op level. And that's a fair enough description.
The picture looks simpler, but from a coding perspective, it's not.
The first issue is that each segment has its own tracking pointer during decoding operation. It increases the number of required registers from 1 to 4. Not a huge deal when registers are plentiful, but that's not always the case (x86 32-bits mode notably).
The second more important issue is that each segment gets decoded at its own speed, meaning some of them will be finished before other ones. Previously, entanglement ensured that all streams would finish together, with just a small tail to take care off. This is now more complex : we don't know which segment will finish first, and the "tail" sequence is now spread over multiple streams, of unpredictable length.
These complexities will cost a bit of performance, but we get serious benefits in exchange :
- Multi-streams decoding is an option : platforms may decide to decode segments serially, one after another, or 2 by 2, depending on their optimal capabilities.
- Single-symbol and multi-symbols decoding strategies are compatible
- Decoding table depth can be any size, including "frugal" ones trading cpu operations for memory space.
In essence, it's opened to a lot more trade-offs.
These new properties introduce a new API requirement : regenerated size must be known, exactly, to start decoding operation (previously, upper regenerated size limit was enough). This is required to guess where each segment starts before even finishing previous ones.
So, what kind of performance this new design delivers ? Here is an example, based on generic samples :
Decoding speed, multi-streams, 32 KB blocks
The picture looks similar to previous "single-stream" measurements, but features much higher speeds. Single-symbol variant wins when compression ratio is very poor. Quite quickly though, double-symbols variant dominates the region where Huffman compression makes most sense (underlined in red boxes). Quad-symbols performance catch up when distribution becomes more favorable, and clearly dominates later on, but that's a region where Huffman is no longer an optimal choice for entropy compression.
Still, by providing speed in the range of
800-900 MB/s
, the new multi-symbol decoder delivers sensible improvements over previous version. So, job done ?
Let's dig a little deeper. You may have noticed that previous measurements were produced on block sizes of 32 KB, which is a nice "average" situation. However, in many compressors such as
zstd
, blocks of symbols are the product of (LZ) transformation, and their size can vary, by a lot. Therefore, is above conclusion still valid when block size changes ?
Let's test this hypothesis in both directions, by measuring large (128 KB) and small (8 KB) block sizes. Results become :
Decoding speed, multi-streams, 128 KB blocks
Decoding speed, multi-streams, 8 KB blocks
While the general picture may look similar, some differences are indeed spotted.
First, 128 KB blocks are remarkably faster than 8 KB ones. This is a natural consequence of table construction times, which is a fixed cost whatever the size of blocks. Hence, their relative impact is inversely proportional to block sizes.
At 128 KB, symbol decoding dominates. It makes the quad-symbols version slightly better compared to double-symbols. Not necessarily enough, but still an alternative to consider when the right conditions are met.
At 8 KB, the reverse situation happens : quad-symbols is definitely out of the equation, due to its larger table construction time. Single-symbol relative performance is now better, taking the top spot when compression ratio is low enough.
With so many parameters, it may seem difficult to guess which version will perform best on a given compressed block, since it depends on the content to decode. Fortunately, such guess can be performed automatically by the library itself.
huff0
's solution is to propose a single decoder (
HUF_decompress()
) which makes such selection transparently. Given a set of heuristic values (table construction time, raw decoding speed, quantized compression ratio), it will automatically select which decoding algorithm it believes is a better fit for the job.
Decoding speed, auto-mode, 32 KB blocks
Ultimately, it only impacts faster speeds, since all versions are compatible and produce valid results. And if a user doesn't like automatic choices, it's still possible to manually override which decoder version is preferred.
As usual, the result of this investigation is made available as
open source software, at github,
under a BSD license. If you are used to previous versions of
fse
, pay attention that the directory and file structures have been changed quite a bit. In order to clarify interfaces,
huff0
now gets its own files and header.
