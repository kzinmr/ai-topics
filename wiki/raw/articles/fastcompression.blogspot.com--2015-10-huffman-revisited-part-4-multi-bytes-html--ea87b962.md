---
title: "Huffman revisited, Part 4 : Multi-bytes decoding"
url: "http://fastcompression.blogspot.com/2015/10/huffman-revisited-part-4-multi-bytes.html"
fetched_at: 2026-05-05T07:01:00.303295+00:00
source: "Yann Collet (LZ4/Zstd)"
tags: [blog, raw]
---

# Huffman revisited, Part 4 : Multi-bytes decoding

Source: http://fastcompression.blogspot.com/2015/10/huffman-revisited-part-4-multi-bytes.html

In most Huffman implementations I'm aware of, decoding symbols is achieved in a serial fashion, one-symbol-after-another.
Decoding fast is not that trivial, but it has been already well studied. Eventually, the one symbol per decoding operation becomes its upper limit.
Consider how work a fast Huffman decoder : all possible bit combinations are pre-calculated into a table, of predefined maximum depth. For each bit combination, it's a simple table lookup to get the symbol decoded and the number of bits to consume.
Huffman Table lookup (example)
More complex schemes may break the decoding into 2 steps, most notably in an attempt to reduce look-up table sizes and still manage to decode symbols which exceed table depth. But it doesn't change the whole picture : that's still a number of operations to decode a single symbol.
In an attempt to extract more speed from decoding operation, I was curious to investigate if it would be possible to decode
more than one symbol
per lookup.
Intuitively, that sounds plausible. Consider some large Huffman decoding table, there is ample room for some bit sequences to represent 2 or more unequivocal symbols. For example, if one symbol is dominant, it only needs 1 bit. So, with only 2 bits, we have 25% chances to get a sequence which means "decode 2 dominant symbols in a row", in a single decode operation.
This can be visualized on below example :
Example of small single-symbol decoding table
which can be transformed into :
Example of multi-symbols decoding table
In some ways, it can look reminiscent of
Tunstall codes
, since we basically try to fit as many symbols as possible into a given depth. But it's not : we don't guarantee reading the entire depth each time, the number of bits read is still variable, just more regular. And there is no "order 1 correlation" : probabilities remain the same per symbol, without depending on prior prefix.
Even with above table available, there is still the question of using it efficiently. It doesn't make any good if a single decoding step is now a lot more complex in order to potentially decode multiple symbols. As an example of what
not
to do, a straightforward approach would be to start decoding the first symbol, then figure out if there is some place left for another one, proceed with the second symbol, then test for a 3rd one, etc. Each of these tests become an unpredictable branch, destroying performance in the process.
The breakthrough came by observing LZ decompression process such as
lz4
: it's insanely fast, because it decodes
matches
, aka. suite of symbols, as a
single copy
operation.
This is in essence what we should do here : copy a sequence of multiple symbols, and
then
decide how many symbols there really are. It avoids branches.
On current generation CPU, copying 2 or 4 bytes is not much slower than copying a single byte, so the strategy is effective. Overwriting same position is also not an issue thanks to modern cache structure.
With this principle settled, it now requires an adapted lookup table structure to work with. I settled with these ones :
Huffman lookup cell structure
The double-symbols structure could seem poorly ambitious : after all, it is only able to store up to 2 symbols into the `
sequence
` field. But in fact, tests will show it's a good trade-off, since most of the time, 2 symbols is what can be reasonably stored into a table lookup depth.
Some quick maths : depth of a lookup table is necessarily limited, in order to fit into memory cache where access times are best. An Intel's cpu L1 data cache is typically 32 KB (potentially shared due to hyper-threading). Since no reasonable OS is single-threaded anymore, let's not use the entire cache : half seems good enough, that's 16 KB. Since a single cell for double-symbols is now 4 bytes (incidentally, the same size as
FSE decoder
), that means 4K cells, hence a maximum depth of 12 bits. Within 12 bits, it's unlikely to get more than 2 symbols at a time. But this outcome entirely depends on alphabet distribution.
This limitation must be balanced with increased complexity for table lookup construction. The quad-symbols one is significantly slower, due to more fine-tuned decisions and recursive nature of the algorithm, defeating inlining optimizations. Below graph show the relative speed of each construction algorithm (right side, in grey, is provided for information, since if target distribution falls into this category, Huffman entropy is no longer a recommended choice).
Lookup table construction speed
The important part is roughly underlined in red boxes, showing areas which are relevant for some typical LZ symbols. The single-symbol lut construction is always faster, significantly. To make sense, slower table construction must be compensated by improved symbol decoding speed. Which, fortunately, is the case.
Decoding speed, at 32 KB block
As suspected, the "potentially faster" quad-symbols variant is hampered by its slower construction time. It manages to become competitive at "length & offset" area, but since it costs 50% more memory, it needs to be unquestionably better to justify that cost. Which is the case as alphabet distribution become more squeezed. By that time though, it becomes questionable if Huffman is still a reasonable choice for the selected alphabet, since its compression power will start to wane significantly against more precise methods such as
FSE
.
The "double-symbols" variant, on the other hand, takes off relatively fast and dominate the distribution region where Huffman makes most sense, making it a prime contender for an upgrade.
By moving from a 260 MB/s baseline to a faster 350-450 MB/s region, the new decoding algorithm is providing fairly sensible gains, but we still have not reached the level of
previous multi-stream variant
, which gets closer to 600 MB/s. The logical next step is to combine both ideas, creating a multi-streams multi-symbols variant. A challenge which proved more involving than it sounds. But that's for another post ...
