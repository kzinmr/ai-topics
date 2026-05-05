---
title: "Huffman revisited - Part 2 : the Decoder"
url: "http://fastcompression.blogspot.com/2015/07/huffman-revisited-part-2-decoder.html"
fetched_at: 2026-05-05T07:01:00.054902+00:00
source: "Yann Collet (LZ4/Zstd)"
tags: [blog, raw]
---

# Huffman revisited - Part 2 : the Decoder

Source: http://fastcompression.blogspot.com/2015/07/huffman-revisited-part-2-decoder.html

The first attempt to decompress the Huffman bitStream created by a
version of huff0 modified to use FSE bitStream
ended up in brutal disenchanting. While decoding operation itself worked fine, the resulting speed was a mere
180 MB/s
.
OK, in absolute, it looks reasonable speed, but keep in mind this is far off the objective of beating FSE (which decodes at 475 MB/s on the same system), and even worse than
reference zlib huffman
. Some generic attempts at improving speed barely changed this, moving up just above 190 MB/s.
This was a disappointment, and a clear proof that the bitStream alone wasn't enough to explain FSE speed. So what could produce such a large difference ?
Let's look at the code. The critical section of FSE decoding loop looks like this :
DInfo = table[state];
    nbBits = DInfo.nbBits;
    symbol = DInfo.symbol;
    lowBits = FSE_readBits(bitD, nbBits);
    state = DInfo.newState + lowBits;
    return symbol;
while for Huff0, it would look like this :
symbol = tableSymbols[state];
    nbBits = tableNbBits[symbol];
    lowBits = FSE_readBits(bitD, nbBits);
    state = ((state << nbBits) & mask) + lowBits;
    return symbol;
There are some similarities, but also some visible differences. First, Huff0 creates 2 decoding tables, one to determine the symbol being decoded, the other one to determine how many bits are read. This is a good design for memory space : the larger table is
tableSymbols
, as its size primarily depends on
1<<maxNbBits
. The second table,
tableNbBits
, is much smaller : its size only depends on
nbSymbols
. This construction allows using only 1 byte per cell. It favorably compares to 4 bytes per cell for FSE. This memory advantage can be used either as a net space saver, or as a way to boost accuracy, by increasing
maxNbBits
.
The cost for it is that there are 2 interdependent operations : first decode the state to get the symbol,
then
use the symbol to get
nbBits
.
This interdependence is likely the bottleneck. When trying to design high performance computation loops, there are 3 major rules to keep in mind :
Ensure hot data is already in the cache.
Avoid badly predictable branches (predictable ones are fine)
For modern OoO (Out of Order) CPU : keep their multiple execution units busy by feeding them with independent (parallelizable) operations.
This list is given in priority order. It makes no sense to try optimizing your code for OoO operations if the CPU has to wait for data from main memory, as the latency cost is much higher than any CPU operation. If your code is full of badly predictable branches, resulting in branch flush penalties, this is also a much larger problem than having some idle execution units. So you can only get to the third set of optimization after properly solving the previous ones.
This is exactly the situation where Huff0 is, with a fully branchless bitstream and data tables entirely within L1 cache. So the next performance boost will likely be found into OoO operations.
In order to avoid dependency between
symbol first, then nbBits
, let's try a different table design, where nbBits is directly stored alongside symbol, in the state table. This double the memory cost, hence reducing the memory advantage enjoyed by Huffman compared to FSE. But let's see where it goes :
symbol = table[state].symbol;
    nbBits = table[state].nbBits;
    lowBits = FSE_readBits(bitD, nbBits);
    state = ((state << nbBits) & mask) + lowBits;
    return symbol;
This simple change alone is enough to boost the speed to
250 MB/s
. Still quite far from the 475 MB/s enjoyed by FSE on the same system, but nonetheless a nice performance boost. More critically, it underlines that the diagnosis was correct : untangling operation dependency free up CPU OoO execution units, they can do more work within each cycle.
So let's ramp up the concept. We have removed one operation dependency. Is there another one ?
Yes. When looking at the main decoding loop from a higher perspective, we can see there are 4 decoding operations per loop. But each decoding operation must wait for the previous one to be completed, because in order to know how to read the bitStream for symbol 2, we need first to know of many bits were consumed by symbol 1.
Compare with how FSE work : since state values are separated from bitStream, it's possible to decode symbol1 and symbol2,
and
retrieve their respective nbBits, in any order, without any dependency. Only later operations, retrieving
lowBits
from the bitStream to calculate the next state values, introduce some ordering dependency (and even this one can be partially unordered).
The main idea is this one : to decode faster, it's necessary retrieve several symbols in parallel, without dependency. So let's create a compressed data flow which makes such operation possible.
Re-using FSE principles "as is" to design a faster Huffman decoding is an obvious choice, but it predictably results in about the same speed. As stated previously, it's not interesting to design a new Huffman encoder/decoder if it just ends up being as fast as FSE. If that is the outcome, then let's simply use FSE instead.
Fortunately, we already know that compression can be faster. So let's concentrate on the decoding side. Since it seems impossible to decode the next symbol without first decoding the previous one from the same bitStream, let's design multiple bitStreams.
The new design is a bit more complex. Compression side is affected : in order to create multiple bitStreams, one solution is to scan input data block multiple times. It proved efficient enough to not bother with a different design. On top of that, a jumptable is required at the beginning of the block, to let the decoder know where each bitStream starts.
Within each bitStream, it's still necessary to decode the first symbol to read the second. But each bitStream is independent, so it's possible to decode up to 4 symbols in parallel.
This proved a design win. The new huff0 decompresses at
600 MB/s
while preserving the compression speed of
500 MB/s
. This compares favorably to FSE or zlib's huffman, as detailed below :
Algorithm
Compression
Decompression
huff0
500 MB/s
600 MB/s
FSE
320 MB/s
475 MB/s
zlib-h
250 MB/s
250 MB/s
With that part solved, it was possible to check that there is no visible compression difference between FSE and Huff0 on Literals data. To be more precise, compression is slightly worse, but header size is slightly better (huffman headers are simpler to describe). On average, both effects compensate.
The new API mimic its FSE counterparts, and provides only the higher (simpler) prototypes for now :
size_t HUF_compress (void* dst, size_t dstSize, 
               const void* src, size_t srcSize);
size_t HUF_decompress(void* dst,  size_t maxDstSize,
                const void* cSrc, size_t cSrcSize);
For the time being, both FSE and huff0 are available within the same library, and even within the same file. The reasoning is that they share the same bitStream code. Obviously, many design choices will have the opportunity to be challenged and improved in the near future.
Having created a new competitor to FSE, it was only logical to check how it would behave within
Zstandard
. It's almost a drop-in replacement for literal compression.
Zstandard
previous
Huff0 literals
compression speed
200 MB/s
240 MB/s
decompression speed
540 MB/s
620 MB/s
A nice speed boost with no impact on compression ratio. Overall, a fairly positive outcome.
