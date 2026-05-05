---
title: "“csinc”, the AArch64 instruction you didn’t know you wanted"
url: "https://danlark.org/2023/06/06/csinc-the-arm-instruction-you-didnt-know-you-wanted/"
fetched_at: 2026-05-05T07:01:52.832639+00:00
source: "Daniel Kutenin (danlark)"
tags: [blog, raw]
---

# “csinc”, the AArch64 instruction you didn’t know you wanted

Source: https://danlark.org/2023/06/06/csinc-the-arm-instruction-you-didnt-know-you-wanted/

After a long time of not publishing anything and being passive about doing any writing in this blog, I am coming back for … however many articles I can. Today I want to talk about an underrated feature of AArch64 ISA which is often overlooked but used by compilers a lot. It’s just a good and short story on what made Arm even better and more “CISCy” when it comes down to conditional moves. The story of
csinc
deserves an article like this.
You probably heard of cmov
Traditionally, when you encounter conditional moves in literature, it is about x86 instruction
cmov
. It’s a nice feature and allows to accomplish better performance in low level optimization. Say, if you merge 2 arrays, you can compare numbers and choose the one depending on the value of compare instructions (more precisely, flags):
while ((pos1 < size1) & (pos2 < size2)) {
    v1 = input1[pos1];
    v2 = input2[pos2];
    output_buffer[pos++] = (v1 <= v2) ? v1 : v2;
    pos1 = (v1 <= v2) ? pos1 + 1 : pos1;
    pos2 = (v1 >= v2) ? pos2 + 1 : pos2;
}
cmpl %r14d, %ebp   # compare which one is smaller, set CF
setbe %bl          # set CF to %bl if it's smaller
cmovbl %ebp, %r14d # move ebp into r14d if flag CF was set
If branches are unpredictable, for instance, you merge 2 arrays of random integers, conditional move instructions bring significant speed-ups against branchy version because of removing the branch misprediction penalty. A lot was written about this in
the Lemire’s blog
. Much engineering has been done on this including
Agner Fog
,
cmov vs branch profile guided optimizations
. Conditional move instructions are a huge domain of modern software, pretty much anything you run likely have them.
What about Arm?
AArch64 is no exception in this area and has some conditional move instructions as well. The immediate equivalent, if you Google it, is
csel
which is translated like
conditional select
. There is almost no difference to
cmov
except you
specify directly
which condition you want to check and destination register (in cmov the destination is unchanged if condition is not met). To my eye it is a bit more intuitive to read:
When I was studying the structure of this instruction in the optimization guide, I noticed the family included different variations:
I was intrigued by the existence of some other forms as this involves more opportunities for the compilers and engineers to write software. For example,
csinc Xd, Xa, Xb, cond
(conditional select
increase
) means that if the condition holds,
Xd = Xb + 1
, otherwise
Xd = Xa
. For example, in merging 2 arrays, the line:
pos1 = (v1 <= v2) ? pos1 + 1 : pos1;
can be compiled into:
csinc X0, X0, X0, #condition_of_v1_less_equal_v2
where
X0
is a register for
pos1
.
csneg
,
csinv
are similar and represent conditional negations and inversions.
For example, clang recognizes this sequence, whereas GCC does not.
https://godbolt.org/z/5cKG3vvKT
Where can this be useful otherwise?
Interestingly enough, in compression! You might heard of
Snappy
, the old Google compression library which was surpassed by
LZ4
many times. For x86, the difference in speed – even for the latest version of clang – is quite big. For example, on my server Intel Xeon 2.00GHz I have
2721MB/s
of decompression for LZ4 and
2172MB/s
for Snappy which is a
25% gap.
For Snappy to reach that level of decompression, engineers needed to write very subtle code to
achieve
cmov
code generation
:
SNAPPY_ATTRIBUTE_ALWAYS_INLINE
inline size_t AdvanceToNextTagX86Optimized(const uint8_t** ip_p, size_t* tag) {
const uint8_t*& ip = *ip_p;
// This section is crucial for the throughput of the decompression loop.
// The latency of an iteration is fundamentally constrained by the
// following data chain on ip.
// ip -> c = Load(ip) -> ip1 = ip + 1 + (c & 3) -> ip = ip1 or ip2
//                       ip2 = ip + 2 + (c >> 2)
// This amounts to 8 cycles.
// 5 (load) + 1 (c & 3) + 1 (lea ip1, [ip + (c & 3) + 1]) + 1 (cmov)
size_t literal_len = *tag >> 2;
size_t tag_type = *tag;
bool is_literal;
#if defined(__GCC_ASM_FLAG_OUTPUTS__) && defined(__x86_64__)
// TODO clang misses the fact that the (c & 3) already correctly
// sets the zero flag.
asm("and $3, %k[tag_type]\n\t"
: [tag_type] "+r"(tag_type), "=@ccz"(is_literal)
:: "cc");
#else
tag_type &= 3;
is_literal = (tag_type == 0);
#endif
// TODO
// This is code is subtle. Loading the values first and then cmov has less
// latency then cmov ip and then load. However clang would move the loads
// in an optimization phase, volatile prevents this transformation.
// Note that we have enough slop bytes (64) that the loads are always valid.
size_t tag_literal =
static_cast<const volatile uint8_t*>(ip)[1 + literal_len];
size_t tag_copy = static_cast<const volatile uint8_t*>(ip)[tag_type];
*tag = is_literal ? tag_literal : tag_copy;
const uint8_t* ip_copy = ip + 1 + tag_type;
const uint8_t* ip_literal = ip + 2 + literal_len;
ip = is_literal ? ip_literal : ip_copy;
#if defined(__GNUC__) && defined(__x86_64__)
// TODO Clang is "optimizing" zero-extension (a totally free
// operation) this means that after the cmov of tag, it emits another movzb
// tag, byte(tag). It really matters as it's on the core chain. This dummy
// asm, persuades clang to do the zero-extension at the load (it's automatic)
// removing the expensive movzb.
asm("" ::"r"(tag_copy));
#endif
return tag_type;
}
For Arm,
csinc
instruction was used because of the nature of the format:
Shortly, last 2 bits of the byte that opens the block have the instruction on what to do and which memory to copy:
00
copies
len-1
data. With careful optimization of conditional moves, we can save on adding this +1 back through
csinc
:
https://gcc.godbolt.org/z/oPErYhz9b
On Google T2A instances I got
3048MB/s
decompression for LZ4 and
2839MB/s
which is
only a 7% gap.
If I enable
LZ4_FAST_DEC_LOOP
, I have
3233MB/s
which still makes a
13% gap
but not 25% as per x86 execution.
In conclusion, conditional select instructions for Arm deserve attention and awareness:
csel
,
csinc
and others have same latency and throughput, meaning, they are as cheap as usual
csel
for almost all modern Arm processors including
Apple M1, M2
.
Compilers do recognize them (in my experience, clang did better than GCC, see above), no need to do anything special, just be aware that some formats might work better for Arm than for x86.
To sum up, contrary to the belief of CISC vs RISC debate about x86 and Arm ISA, the latter has surprising features of conditional instructions which are more flexible than the traditionally discussed ones.
You can read more about this topic in
other blogs
, in
Arm reference guide
,
Microsoft blog of AArch64 conditional execution
.
