---
title: "LLaMA Now Goes Faster on CPUs"
url: "https://justine.lol/matmul/"
fetched_at: 2026-05-05T07:01:27.203951+00:00
source: "Justine Tunney"
tags: [blog, raw]
---

# LLaMA Now Goes Faster on CPUs

Source: https://justine.lol/matmul/

Mar 31
st
, 2024 @
justine's web page
LLaMA Now Goes Faster on CPUs
I just wrote 84 new matrix multiplication kernels for
llamafile
which
enable it to read prompts / images faster. Compared to llama.cpp, prompt
eval time with llamafile should go anywhere between 30% and 500% faster
when using F16 and Q8_0 weights on CPU. The improvements are most
dramatic for ARMv8.2+ (e.g. RPI 5), Intel (e.g. Alderlake), and AVX512
(e.g. Zen 4) computers. My kernels go 2x faster than MKL for matrices
that fit in L2 cache, which makes them a work in progress, since the
speedup works best for prompts having fewer than 1,000 tokens.
Background
llamafile is a local LLM project I started with Mozilla back in Nov
2023. We're using
Cosmopolitan Libc
to package
llama.cpp
as a
single-file cross-platform binary that runs on six OSes for AMD64 and
ARM64, while making gentle modifications. I believe that by improving
the core technology, we can give our users the best possible llama.cpp
experience, while helping both projects reach a broader audience.
Mozilla has been giving me the resources to do this.
When I first got into LLMs, my workstation was an austere Hewlett
Packard running Alpine with a spinning disk, slow RAM, an AVX2
processor, and no GPU. What I liked about llama.cpp is they were the
first LLM project that cared about people like me. So I started
volunteering full time and collaborated with guys like Slaren to
introduce
mmap()
support, which made weights load instantly using half as much
RAM. It was a leap forward for local LLMs at the time, but did little to
improve evaluation speed. Most of the inference code was written by
Georgi Gerganov himself, and it's so good that it'd take me another year
to finally improve upon. Now that I have, let's see how much faster
things go on my old Hewlett Packard.
LLM
     Performance on HP Intel® Core™ i9-9900 ($439) w/ 2200 MT/s RAM c. 2020
prompt
tok/sec
eval
tok/sec
model
weights
data type
hardware
software
28
7
Mistral 7b
q4_0
Skylake
llamafile-0.7
17
7
Mistral 7b
q4_0
Skylake
llama.cpp 2024-03-26
12
7
Mistral 7b
q4_0
Skylake
llamafile-0.6.2
32
4
Mistral 7b
q8_0
Skylake
llamafile-0.7
22
4
Mistral 7b
q8_0
Skylake
llama.cpp 2024-03-26
16
4
Mistral 7b
q8_0
Skylake
llamafile-0.6.2
23
2
Mistral 7b
f16
Skylake
llamafile-0.7
15
2
Mistral 7b
f16
Skylake
llama.cpp 2024-03-26
14
2
Mistral 7b
f16
Skylake
llamafile-0.6.2
205
26
TinyLlama 1.1B
q8_0
Skylake
llamafile-0.7
144
26
TinyLlama 1.1B
q8_0
Skylake
llama.cpp 2024-03-26
91
23
TinyLlama 1.1B
q8_0
Skylake
llamafile-0.6.2
171
15
TinyLlama 1.1B
f16
Skylake
llamafile-0.7
118
15
TinyLlama 1.1B
f16
Skylake
llama.cpp 2024-03-26
101
15
TinyLlama 1.1B
f16
Skylake
llamafile-0.6.2
Here we see that, on Skylake, llamafile users can expect to see a 2x
speedup and llama.cpp users can expect 50% better performance. Please
note this only applies to certain weights. So far, I've only written
optimized kernels for the q8_0, f16, q4_1, q4_0, and f32 data types. I
think both q8_0 and f16 are really solid choices. Possibly even f32 if
you've got plenty of RAM. That's because my new kernels change the
rules. They're doing such a good job fixing the memory bandwidth quants
always solved, that quantization could become the bigger bottleck. That
would be great news for the future of local language models, since it
means less need to trade away knowledge for speed.
You don't need a large computer to run a large language model. One of
the best personal computers available in stores today is the Raspberry Pi. They
deliver good performance at a great price and consume very little power.
LLM Performance on $136
Raspberry Pi v5
(ARMv8.2) and v4 (ARMv8.0)
prompt
tok/sec
eval
tok/sec
model
weights
data type
hardware
software
62
5
TinyLlama 1.1B
f16
RPI5
llamafile-0.7
28
5
TinyLlama 1.1B
f16
RPI5
llama.cpp 2024-03-26
8
5
TinyLlama 1.1B
f16
RPI5
llamafile-0.6.2
45
9
TinyLlama 1.1B
q8_0
RPI5
llamafile-0.7
35
9
TinyLlama 1.1B
q8_0
RPI5
llama.cpp 2024-03-26
20
9
TinyLlama 1.1B
q8_0
RPI5
llamafile-0.6.2
10
3
TinyLlama 1.1B
q8_0
RPI4
llamafile-0.7
10
3
TinyLlama 1.1B
q8_0
RPI4
llama.cpp 2024-03-26
9
3
TinyLlama 1.1B
q8_0
RPI4
llamafile-0.6.2
3
2
TinyLlama 1.1B
f16
RPI4
llamafile-0.7
3
2
TinyLlama 1.1B
f16
RPI4
llama.cpp 2024-03-26
4
2
TinyLlama 1.1B
f16
RPI4
llamafile-0.6.2
Raspberry Pi released their fifth edition a few months ago and it's
outrageously fast compared to their previous model. They also introduced
support for the ARMv8.2 dotprod and fp16 arithmetic ISAs, which are very
useful for LLMs. Those two features alone enabled llama.cpp to achieve a
10x performance boost for f16 weights last year. This week I teased out
another 2x performance boost on top of that, by using a kernel that I
originally intended for AVX512. You wouldn't think a kernel designed for
beefy data center equipment would work out for a teensy tiny little
Raspberry Pi, but it actually fit hand in glove since both CPUs have 32
vector registers.
It's worthwhile to note that the new ARMv8.2 fp16 ISA may introduce more
errors than usual, since it causes llamafile to use fp16 words and we
aren't using techniques like
Kahan summation
for
computing dot products. So Q8_0 weights actually end up having slightly
better perplexity, because it uses the dotprod ISA which lets us updot
signed 8-bit integers into a 32-bit compute type which absorbs errors.
However this doesn't mean the faster fp16 weights can't be useful. Many
developers in this field view the differences as negligible.
For example, let's say you want to setup an email server on your pihole
and have TinyLLaMA filter spam. It's possible to
configure Postfix
to filter content using a shell script
which lets you run the
llamafile command.
llamafile -m TinyLlama-1.1B-Chat-v1.0.f16.gguf \
          --grammar
'root ::= "yes" | "no"'
--temp 0 -c 0 \
          --no-display-prompt --log-disable -p
"<|user|>
Can you say for certain that the following email is spam?

To: jtunney@gmail.com
From: Federal-Tax-DebtHelp <ConfirmationEmail.inzk@janents.com>
Subject: Reduce your payments to what you can afford

Reduce your payments to what you can afford 
 
 [IMG] 
 [IMG] 
 
 [IMG] 
</s>
<|assistant|>"
When I run the shell script above on my RPI5, it takes 3 seconds.
jart@pi5:~/scratch$ time ./spam.sh
yes

real    0m3.168s
user    0m10.851s
sys     0m0.541s
There are several important things happening here:
--temp 0
turns off the random number generator (we
    don't want improvisation for a spam filter)
Here we see why prompt eval time is king. Token generation speed
    (eval time) doesn't matter for this use case, since we're using
    the
--grammar
flag to force the LLM to only print a
    single "yes\n" or "no\n" token.
I piped the original email through
links -codepage utf-8
    -force-html -width 400 -dump /dev/stdin
which reduced the
    number of tokens and removed hidden HTML content that was put there
    by the spammer to make the email look like ham to naive Bayesian
    filters.
The
-c 0
flag configures TinyLLaMA to use the maximum
    context size, which is 2048 tokens. That's the largest prompt we can
    give it. To help avoid feeding in too much text, you can pipe the
    email through
sed 's/   */ /g' | dd bs=1
    count=7000
to remove superfluous spaces and place an upper
    limit on its size.
Please note that spam filtering is just the tip of the iceberg. I've
always thought that "generative ai" is a misnomer, because language
models (more commonly known as "The Algorithm") have always been used by
tech companies in the past to extract knowledge, curate information, and
rank content. That requires reading rather than writing. AI has never
traditionally needed to talk that much, because the English language
just isn't that useful at the scale tech companies operate. Even if you
could generate English summaries for exabytes of text a millionth its
size, that would still be more words than any team could hope to read in
a lifetime.
Gamers have the highest quality expectations of any value consumer, so
any hardware built for them is usually pretty good. In the machine
learning industry, we have thrived for years repurposing hardware that
was intended for gamers. If it weren't for their important contribution,
the AI Winter may have needed to last another ten years. So a few months
ago, I asked a gamer to build me a computer that can replace my old
Hewlett Packard.
LLM Performance on
Intel® Core™
    i9-14900K
($438) w/ 6400 MT/s RAM
prompt
tok/sec
eval
tok/sec
model
weights
data type
hardware
software
63
12
Mistral 7b
q8_0
Alderlake
llamafile-0.7
40
9
Mistral 7b
q8_0
Alderlake
llama.cpp 2024-03-26
19
7
Mistral 7b
q8_0
Alderlake
llamafile-0.6.2
50
7
Mistral 7b
f16
Alderlake
llamafile-0.7
13
5
Mistral 7b
f16
Alderlake
llama.cpp 2024-03-26
10
4
Mistral 7b
f16
Alderlake
llamafile-0.6.2
406
67
TinyLlama 1.1B
q8_0
Alderlake
llamafile-0.7
273
53
TinyLlama 1.1B
q8_0
Alderlake
llama.cpp 2024-03-26
114
43
TinyLlama 1.1B
q8_0
Alderlake
llamafile-0.6.2
407
42
TinyLlama 1.1B
f16
Alderlake
llamafile-0.7
90
31
TinyLlama 1.1B
f16
Alderlake
llama.cpp 2024-03-26
68
30
TinyLlama 1.1B
f16
Alderlake
llamafile-0.6.2
I think Alderlake is a great CPU but it's popularly misunderstood, as
evidenced by how easily I quintupled its float16 performance. Unlike
ARMv8.2, I was able to do that without introducing rounding errors,
since my x86 kernels use a float32 compute type internally. This means I
can have an even smarter spam filter. For example, when I run
my
spam.sh
shell script, it only takes 420 milliseconds,
which is 7x faster than my Raspberry Pi 5. That's right, when it comes
to small workloads, this chip is able to finish before CUDA even gets
started.
Alderlake owners can also look forward to the fact that llamafile takes
special care to not run on your efficiency cores. This is one of the
things that helps llamafile to go faster than llama.cpp. It also means
you can run LLMs around the clock and there's still plenty of resources
leftover for the other programs on your computer. The reason why that's
important is because llama.cpp dispatches threads in lockstep, which
would have meant that if any
1
core takes longer than the
others to do its job, then all other
n
cores would need to
busy loop until it completed.
However the greatest feature of this microprocessor is how quickly it
can build all 2.6 million lines of code in the Cosmopolitan monorepo. My
Hewlett Packard always took 64 seconds, but this gaming computer does it
in 20. It actually took 35 seconds originally; what made it faster was applying
liquid
metal
and AI overclocking. Another reason systems code is so fast on
the Alderlake is there was a fire fight between the hackers and
scientists in the creation of this CPU, and the hackers won. I hope
they'll strike out a better compromise on AVX512 in the future, but
overall I'm very happy with this chip, since I believe it represents
significant progress over previous models.
If there's a personal computer with the most class, it would definitely
be the Mac Studio. Gaining the performance advantage here was harder for
me, because it's the hardware platform the llama.cpp developers care
about most, plus I'm working with a handicap due to my choice to use
Stallman's compiler instead of Apple's proprietary tools.
LLM Performance on Mac Studio CPU w/ 24-core
     M2 Ultra ($5000)
prompt
tok/sec
eval
tok/sec
model
weights
data type
hardware
software
90
25
Mistral 7b
q8_0
M2 Ultra
llamafile-0.7
90
27
Mistral 7b
q8_0
M2 Ultra
llama.cpp 2024-03-26
37
24
Mistral 7b
q8_0
M2 Ultra
llamafile-0.6.2
79
15
Mistral 7b
f16
M2 Ultra
llamafile-0.7
57
15
Mistral 7b
f16
M2 Ultra
llama.cpp 2024-03-26
21
15
Mistral 7b
f16
M2 Ultra
llamafile-0.6.2
457
95
TinyLlama 1.1B
q8_0
M2 Ultra
llamafile-0.7
564
108
TinyLlama 1.1B
q8_0
M2 Ultra
llama.cpp 2024-03-26
236
95
TinyLlama 1.1B
q8_0
M2 Ultra
llamafile-0.6.2
419
66
TinyLlama 1.1B
f16
M2 Ultra
llamafile-0.7
400
67
TinyLlama 1.1B
f16
M2 Ultra
llama.cpp 2024-03-26
141
66
TinyLlama 1.1B
f16
M2 Ultra
llamafile-0.6.2
I wouldn't want to pick a fight with an Apple user, because their M2
microprocessor turns llamafile into a firehose of synthetic content. The
trick Apple used to do it is leveraging their vertical integration. If
you buy a Mac Studio and look inside, you'll discover that they put the
RAM DIMMs
inside
the CPU. It makes latency-bound operations
like token generation go much faster, because the CPU no longer needs to
make all these long distance phone calls. However, in terms of sheer
flops (as measured by prompt tok/sec), we can see that compared to my
much cheaper Intel computer, the M2 Ultra only exposes 30% more compute
via the ARM ISA. You need to go through their proprietary frameworks
like Metal and Accelerate if you want to access anything more. If you
have xcode installed, then llamafile by default will compile a small
stub module which does just that, since despite my values I'm happy to
help you get in front of any closed source library standing between you
and your silicon.
One important thing to know if you're considering buying a Mac Studio is
that, like the Windows Executive, XNU does a really good job keeping
your desktop stable, and that means protecting your system from you. It
takes me 45 seconds on Mac Studio to compile the Cosmo monorepo, due to
all these safety features; but if I fork bombed it, I'd be surprised if
Netflix skipped a single frame. My
spam.sh
script also goes
430ms, which is slower than Intel. However none of this concerns me,
since I've seen the way Asahi Linux is able to unleash the M2's full
potential.
While llamafile cares deeply about helping the GPU poor, it offers a
first-class experience to the 1% too. The AMD Ryzen Threadripper PRO
7995WX was just launched several months ago and it's the most expensive
CPU money can buy right now. It'll set you back $10,000 but you get 96
cores of AVX512, based on the Zen4 architecture.
LLM Performance on
AMD Ryzen Threadripper PRO 7995WX
w/ 96 cores ($10,000)
prompt
tok/sec
eval
tok/sec
model
weights
data type
hardware
software
557
17
Mistral 7b
bf16
7995WX
llamafile-0.7
485
17
Mistral 7b
f16
7995WX
llamafile-0.7
197
16
Mistral 7b
f16
7995WX
llama.cpp 2024-03-29
52
18
Mistral 7b
f16
7995WX
llamafile-0.6.2
480
10
Mistral 7b
f32
7995WX
llamafile-0.7
221
10
Mistral 7b
f32
7995WX
llama.cpp 2024-03-30
38
9
Mistral 7b
f32
7995WX
llamafile-0.6.2
382
25
Mistral 7b
q8_0
7995WX
llamafile-0.7
283
24
Mistral 7b
q8_0
7995WX
llama.cpp 2024-03-29
37
25
Mistral 7b
q8_0
7995WX
llamafile-0.6.2
1929
52
TinyLlama 1.1B
bf16
7995WX
llamafile-0.7
1819
52
TinyLlama 1.1B
f16
7995WX
llamafile-0.7
824
51
TinyLlama 1.1B
f16
7995WX
llama.cpp 2024-03-29
295
89
TinyLlama 1.1B
f16
7995WX
llamafile-0.6.2
1268
60
TinyLlama 1.1B
q8_0
7995WX
llamafile-0.7
1127
60
TinyLlama 1.1B
q8_0
7995WX
llama.cpp 2024-03-29
169
93
TinyLlama 1.1B
q8_0
7995WX
llamafile-0.6.2
Here we see that, despite only being twice the price, the 7995WX x86 ISA
offers 7x more raw compute power than the M2 Ultra ARM ISA, and nearly
the same token generation speed, which is likely thanks to its 384mb L3
cache. When I bought this chip, I had to expand support in llama.cpp for
bfloat16 and AVX512 before I could fully test its capabilities. My work
means you can now run LLaMA 2.8x faster on Zen4 than you could before.
One thing I like about AVX512 is that Google's Gemma model can
solve math
riddles on AVX512 but not on AVX2
because the bigger vectors usually
make it easier to reduce rounding errors. Its
VDPBF16PS
instruction helps us updot bf16 similar to VNNI and ARM dotprod. Having
native support for bf16 is nice, since models like Mistral and TinyLLaMA
distribute weights using bfloat16 as their canonical format. If we were
to convert bf16 to fp16, then only 13% of the numbers that are possible
can be accurately represented. In practice, it matters little, since
99.71% of the numbers Mistral 7b uses are among that 13%. However I
believe that llamafile should deliver, to the best of its ability,
whatever number of bits are being claimed. Especially when doing so also
enables us to better exploit the capabilities of our hardware. Adding
bf16 support is my first big step towards improving that.
Please be warned that a lot of people who bought this Threadripper ran
into issues with sketchy RAM. I had to RMA the first DIMMs I bought for
this computer, because most of them died and I was getting 5 eval tokens
per second with Mistral. I've been having better luck with
a
new full kit of eight sticks
that just arrived today. When I run
sysbench memory run
it
reports 10,033,424 mops, which is oddly faster than my Mac Studio where
9,892,584 mops is reported, however my Intel computer does 14,490,952. I
expected my Threadripper's RAM to have that speed since both set of
components advertised 6400 MT/s with the same timings, but I'm told that
I traded this away to have 256GB of ECC. As for disk speed,
dd
if=/dev/zero of=/tmp/output bs=128k count=50k; rm -f /tmp/output
reports 1.6 GB/s which is 3.6x slower than my Mac Studio, and 3x slower
than my Intel (which has the same M.2 stick). I'm told that Intel and
Apple are just better at this, but I wish I understood why.
Last but not least, it runs my
spam.sh
script in 323ms and
builds the whole Cosmo monorepo in 13 seconds. It's actually capable of
building it faster, since this is the first time I've ever seen my build
config being constrained by an individual artifact blocking the critical
path. I never thought I'd live to see the day. I'm also puzzled that
llamafile v0.6.2 is somehow managing to do 93 tokens per second; that's
40% faster than my M2. It's exciting news, since after reviewing the
breadth of this blog post, I would have wept if there were no more
optimizations possible.
The source code for my matrix multiplication kernels can be found at:
Both Mozilla and myself felt it would be worthwhile to contribute these
improvements to the upstream project. Doing that required adapting the
code to their preferred method of handling portability at compile-time.
We also took the liberty of changing the license from Apache 2.0 to MIT,
since the latter is what the llama.cpp developers prefer. Here are links
to the most recent pull requests I've sent them:
There are dozens of mathematical operations a transformer model needs to
perform in order to generate text, e.g. rope, transpose, reshape,
softmax, rms_norm, etc. All of the performance improvements I described
above, were achieved by focusing exclusively on a single one, which
is
GGML_OP_MUL_MAT
, because that's what my Linux Perf
profiler told me llamafile spends 95% of its time doing.
So what is this matrix multiplication thing? We shall start by defining
the most important algorithm in the world using the pythonic dialect of
Python that is most popular with developers today:
def
matmul
(A, B):
assert
len
(B) ==
len
(A[0])
return
[[
sum
(A[i][l] * B[l][j]
for
l
in
range
(
len
(B)))
for
j
in
range
(
len
(B[0]))]
for
i
in
range
(
len
(A))]
As we can see, it's just three for loops and a multiply-add. How hard
could it be?
On my workstation (which I call meatball), the code above goes a
screeching 0.042 gigaflops. Most Python programmers are smart enough to
know that they should delegate tasks like these to a library
like
np.matmul
, which goes 29 gigaflops. NumPy achieves its
speed using FORTRAN which for generations has been favored
by
real programmers
who've led us to believe these libraries are something mysterious
chiseled in stone by the hand of Moses himself; but if we look at the
FORTRAN code NumPy actually uses, then it really isn't all that
complicated and could clearly benefit from some revision.
SUBROUTINE
SGEMM
(TRANSA,TRANSB,M,N,K,ALPHA,A,LDA,B,LDB,BETA,C,LDC)
*     .. Scalar Arguments ..
REAL
ALPHA,BETA
INTEGER
K,LDA,LDB,LDC,M,N
CHARACTER
TRANSA,TRANSB
*     .. Array Arguments ..
REAL
A(LDA,*),B(LDB,*),C(LDC,*)
      [...]
*
*           Form  C := alpha*A*B + beta*C.
*
DO
90
J = 1,N
IF
(BETA.
EQ
.ZERO)
THEN
DO
50
I = 1,M
                          C(I,J) = ZERO
50
CONTINUE
ELSE IF
(BETA.
NE
.ONE)
THEN
DO
60
I = 1,M
                          C(I,J) = BETA*C(I,J)
60
CONTINUE
END IF
DO
80
L = 1,K
IF
(B(L,J).
NE
.ZERO)
THEN
TEMP = ALPHA*B(L,J)
DO
70
I = 1,M
                              C(I,J) = C(I,J) + TEMP*A(I,L)
70
CONTINUE
END IF
80
CONTINUE
90
CONTINUE
[...]
RETURN
END
I like to define my subroutines using a modern language like C++, which
goes 47 gigaflops. This means C++ is three orders of a magnitude faster
than Python. That's twenty years of progress per Moore's law.
// multiplies matrices on cpu
// with column major ordering
//
//     m×k * k×n → m×n
//     k×m * k×n → m×n if aᵀ
//     m×k * n×k → m×n if bᵀ
//     k×m * n×k → m×n if aᵀ and bᵀ
//
template
<
typename
T,
typename
TA,
typename
TB,
typename
TC>
void
GEMM
(
bool
aᵀ,
bool
bᵀ,
int
m,
int
n,
int
k,
T
α,
const
TA
*A,
int
lda,
const
TB
*B,
int
ldb,
T
β,
TC
*C,
int
ldc) {
assert
(m >= 0 && n >= 0 && k >= 0);
assert
(lda >=
std
::max(1, aᵀ ? k : m));
assert
(ldb >=
std
::max(1, bᵀ ? n : k));
assert
(ldc >=
std
::max(1, m));
#pragma omp parallel for collapse(2) if (m * n * k > 300000)
for
(
int
i = 0; i < m; ++i)
for
(
int
j = 0; j < n; ++j) {
T
d = 0;
for
(
int
l = 0; l < k; ++l) {
T
a = A[aᵀ ? lda * i + l : lda * l + i];
T
b = B[bᵀ ? ldb * l + j : ldb * j + l];
                d += a * b;
            }
if
(β) {
T
c = C[ldc * j + i];
                C[ldc * j + i] = α * d + β * c;
            }
else
{
                C[ldc * j + i] = α * d;
            }
        }
}
In order to do better than 47 gigaflops on CPU, most C++ developers are
smart enough to know they should use a BLAS library. Mightiest of the
open source BLAS is
BLIS
which is funded by Microsoft, Intel, Texas Instruments, AMD, HPE,
Oracle, Huawei, Facebook, ARM, and the National Science Foundation.
"Any time somebody outside Intel beats MKL by a nontrivial amount, I
report it to the MKL team. It is fantastic for any open-source project
to get within 10% of MKL... [T]his is why Intel funds BLIS development."
(@jeffhammond)
blis/issues/264
That's very impressive. Matrix multiplication is the practical
application of hardware that hardware makers care about optimizing most.
Since nobody knows more about Intel hardware than Intel, I imagine it's
not everday that somebody manages to challenge Intel for supremacy on
their own platform. Based on my own evaluation, what BLIS says is true.
However that is only true for single-threaded performance. Their
multithreading mode is still experimental, but if I use
a
./configure
flag to turn it on, then I'm able to boost
performance to 85 gigaflops.
llama.cpp had the important insight that less is more when it comes to
linear algebra. The alpha and beta parameters are never used, so they're
always set to to 1 and 0. The op graph for LLMs are designed in such a
way that the A matrix is almost always transposed and B is almost never
transposed, which means inner dimension dot product can vectorize over
contiguous memory. The m/k dimensions are usually evenly divisible by
64. While generating tokens, n=1 is usually the case, which makes matmul
a de facto matvec for the performance most people care about. BLAS
libraries usually hurt more than they help for matrix-vector
multiplication, because it's so computationally simple by comparison.
Sort of like the difference between downloading a movie and pinging a
server. Matrix vector multiplication is an operation where latency (not
throughput) is the bottleneck, and the bloat of fancy libraries has a
measurable impact. So llama.cpp does something like this, which goes 233
gigaflops.
template
<
typename
T>
void
LLMM
(
int
m,
int
n,
int
k,
const
T
*A,
int
lda,
const
T
*B,
int
ldb,
T
*C,
int
ldc) {
#pragma omp parallel for collapse(2) if (m * n * k > 300000)
for
(
int
i = 0; i < m; ++i)
for
(
int
j = 0; j < n; ++j) {
T
d = 0;
for
(
int
l = 0; l < k; ++l)
                d += A[lda * i + l] * B[ldb * j + l];
            C[ldc * j + i] = d;
        }
}
This gives us the best possible token generation speeds. However
llama.cpp's Achilles heel on CPU has always been prompt processing
speed, which goes much slower. That's because chewing through prompts
requires bona fide matrix-matrix multiplication. Being able to do this
fast is important if you care about text summarization and LLaVA image
processing. That's the reason why support for countless BLAS libraries
has been added to llama.cpp over the past year. The most formidable of
them is Intel's Math Kernel Library (MKL) which goes 384 gigaflops.
The difference between 233 versus 384 gigaflops may not seem like much,
at least not compared to Python, but it's a tremendous gulf. MKL is also
closed source and proprietary. We aren't even allowed to disassemble it
and try to reverse engineer how it works. Intel has been developing math
kernels for fifty years and they hold the secrets they've acquired very
close to their chest. But even if our desire for performance was so
great that we were willing to overlook the ethics of an open source
project spending the majority of its time inside a proprietary blob, the
simple fact of the matter is that integrating foreign BLAS libraries
into llama.cpp isn't that practical, due to the way its threading model
works. In order to improve prompt processing speed, we must figure out
the trick BLAS libraries use, and implement it in a scrappy
dependency-free way that stays true to llama.cpp's roots.
I believe the trick with CPU math kernels is exploiting instruction
level parallelism with fewer memory references. If you compile the
example above with
-O3 -ffast-math -march=native
then the
code your compiler generates should look like this:
void
SLLMM
(
int
m,
int
n,
int
k,
const
float
*A,
int
lda,
const
float
*B,
int
ldb,
float
*C,
int
ldc) {
#pragma omp parallel for collapse(2) if (m * n * k > 300000)
for
(
int
i = 0; i < m; ++i)
for
(
int
j = 0; j < n; ++j) {
__m256
c = _mm256_setzero_ps();
for
(
int
l = 0; l < k; l += 8)
                c = _mm256_fmadd_ps(_mm256_loadu_ps(A + lda * i + l),
                                    _mm256_loadu_ps(B + ldb * j + l), c);
            C[ldc * j + i] = hsum(c);
        }
}
So what llama.cpp usually does when it wants to improve things, is it'll
unroll the innermost loop like this:
void
SLLMM2
(
int
m,
int
n,
int
k,
const
float
*A,
int
lda,
const
float
*B,
int
ldb,
float
*C,
int
ldc) {
#pragma omp parallel for collapse(2) if (m * n * k > 300000)
for
(
int
i = 0; i < m; ++i)
for
(
int
j = 0; j < n; ++j) {
__m256
c0 = _mm256_setzero_ps();
__m256
c1 = _mm256_setzero_ps();
for
(
int
l = 0; l < k; l += 16) {
                c0 = _mm256_fmadd_ps(_mm256_loadu_ps(A + lda * i + l + 0),
                                     _mm256_loadu_ps(B + ldb * j + l + 0), c0);
                c1 = _mm256_fmadd_ps(_mm256_loadu_ps(A + lda * i + l + 8),
                                     _mm256_loadu_ps(B + ldb * j + l + 8), c1);
            }
            C[ldc * j + i] = hsum(c0) + hsum(c1);
        }
}
That may slightly improve numerical stability, but it does very little
to enhance performance, since modern CPUs are perfectly capable of
speculatively executing future loop iterations on their own. What we
want to do instead is unroll the
outer
loop. The advantage of
doing this becomes clear if we consider how it enables us to share
the
a0
register load across multiple floating point
operations.
void
SLLMM4
(
int
m,
int
n,
int
k,
const
float
*A,
int
lda,
const
float
*B,
int
ldb,
float
*C,
int
ldc) {
#pragma omp parallel for collapse(2) if (m * n * k > 300000)
for
(
int
i = 0; i < m; ++i)
for
(
int
j = 0; j < n; j += 4) {
__m256
c0 = _mm256_setzero_ps();
__m256
c1 = _mm256_setzero_ps();
__m256
c2 = _mm256_setzero_ps();
__m256
c3 = _mm256_setzero_ps();
for
(
int
l = 0; l < k; l += 8) {
__m256
a0 = _mm256_loadu_ps(A + lda * (i + 0) + l);
__m256
k0 = _mm256_loadu_ps(B + ldb * (j + 0) + l);
__m256
k1 = _mm256_loadu_ps(B + ldb * (j + 1) + l);
__m256
k2 = _mm256_loadu_ps(B + ldb * (j + 2) + l);
__m256
k3 = _mm256_loadu_ps(B + ldb * (j + 3) + l);
                c0 = _mm256_fmadd_ps(a0, k0, c0);
                c1 = _mm256_fmadd_ps(a0, k1, c1);
                c2 = _mm256_fmadd_ps(a0, k2, c2);
                c3 = _mm256_fmadd_ps(a0, k3, c3);
            }
            C[ldc * (j + 0) + (i + 0)] = hsum(c0);
            C[ldc * (j + 1) + (i + 0)] = hsum(c1);
            C[ldc * (j + 2) + (i + 0)] = hsum(c2);
            C[ldc * (j + 3) + (i + 0)] = hsum(c3);
        }
}
If we unroll both outer loops, the effect is compounded.
void
SLLMM3X4
(
int
m,
int
n,
int
k,
const
float
*A,
int
lda,
const
float
*B,
int
ldb,
float
*C,
int
ldc) {
#pragma omp parallel for collapse(2) if (m * n * k > 300000)
for
(
int
i = 0; i < m; i += 3)
for
(
int
j = 0; j < n; j += 4) {
__m256
c00 = _mm256_setzero_ps();
__m256
c01 = _mm256_setzero_ps();
__m256
c02 = _mm256_setzero_ps();
__m256
c03 = _mm256_setzero_ps();
__m256
c10 = _mm256_setzero_ps();
__m256
c11 = _mm256_setzero_ps();
__m256
c12 = _mm256_setzero_ps();
__m256
c13 = _mm256_setzero_ps();
__m256
c20 = _mm256_setzero_ps();
__m256
c21 = _mm256_setzero_ps();
__m256
c22 = _mm256_setzero_ps();
__m256
c23 = _mm256_setzero_ps();
for
(
int
l = 0; l < k; l += 8) {
__m256
k0 = _mm256_loadu_ps(B + ldb * (j + 0) + l);
__m256
k1 = _mm256_loadu_ps(B + ldb * (j + 1) + l);
__m256
k2 = _mm256_loadu_ps(B + ldb * (j + 2) + l);
__m256
k3 = _mm256_loadu_ps(B + ldb * (j + 3) + l);
__m256
a0 = _mm256_loadu_ps(A + lda * (i + 0) + l);
                c00 = _mm256_fmadd_ps(a0, k0, c00);
                c01 = _mm256_fmadd_ps(a0, k1, c01);
                c02 = _mm256_fmadd_ps(a0, k2, c02);
                c03 = _mm256_fmadd_ps(a0, k3, c03);
__m256
a1 = _mm256_loadu_ps(A + lda * (i + 1) + l);
                c10 = _mm256_fmadd_ps(a1, k0, c10);
                c11 = _mm256_fmadd_ps(a1, k1, c11);
                c12 = _mm256_fmadd_ps(a1, k2, c12);
                c13 = _mm256_fmadd_ps(a1, k3, c13);
__m256
a2 = _mm256_loadu_ps(A + lda * (i + 2) + l);
                c20 = _mm256_fmadd_ps(a2, k0, c20);
                c21 = _mm256_fmadd_ps(a2, k1, c21);
                c22 = _mm256_fmadd_ps(a2, k2, c22);
                c23 = _mm256_fmadd_ps(a2, k3, c23);
            }
            C[ldc * (j + 0) + (i + 0)] = hsum(c00);
            C[ldc * (j + 1) + (i + 0)] = hsum(c01);
            C[ldc * (j + 2) + (i + 0)] = hsum(c02);
            C[ldc * (j + 3) + (i + 0)] = hsum(c03);
            C[ldc * (j + 0) + (i + 1)] = hsum(c10);
            C[ldc * (j + 1) + (i + 1)] = hsum(c11);
            C[ldc * (j + 2) + (i + 1)] = hsum(c12);
            C[ldc * (j + 3) + (i + 1)] = hsum(c13);
            C[ldc * (j + 0) + (i + 2)] = hsum(c20);
            C[ldc * (j + 1) + (i + 2)] = hsum(c21);
            C[ldc * (j + 2) + (i + 2)] = hsum(c22);
            C[ldc * (j + 3) + (i + 2)] = hsum(c23);
        }
}
Vectorized outer product with OpenMP goes 810 gigaflops on my Alderlake
i9-14900K with 6400 MT/s RAM when multiplying a 513×512 with a 512×512
matrix. That is twenty eight years of progress per Moore's law compared
to Python. It's clearly optimal since my CPU is listed as only being
capable of going
780
gigaflops
. Yes, I overclocked it with liquid metal. On the other
hand, MKL processes this matrix size at 295 gigaflops on my machine.
1
:
vmovups
(
%r10
,
%r9
,4),
%ymm0
vmovups
(
%rsi
,
%r9
,4),
%ymm4
vmovups
(
%rcx
,
%r9
,4),
%ymm2
vmovups
(
%rdx
,
%r9
,4),
%ymm1
vfmadd231ps
(
%r11
,
%r9
,4),
%ymm0
,
%ymm6
vfmadd231ps
%ymm4
,
%ymm0
,
%ymm15
vfmadd231ps
%ymm2
,
%ymm0
,
%ymm12
vfmadd231ps
%ymm1
,
%ymm0
,
%ymm9
vmovups
(
%rdi
,
%r9
,4),
%ymm0
vfmadd231ps
(
%r11
,
%r9
,4),
%ymm0
,
%ymm5
vfmadd231ps
%ymm4
,
%ymm0
,
%ymm14
vfmadd231ps
%ymm2
,
%ymm0
,
%ymm11
vfmadd231ps
%ymm1
,
%ymm0
,
%ymm8
vmovups
(
%rbx
,
%r9
,4),
%ymm0
vfmadd231ps
(
%r11
,
%r9
,4),
%ymm0
,
%ymm3
add
$8
,
%r9
vfmadd231ps
%ymm4
,
%ymm0
,
%ymm13
vfmadd231ps
%ymm2
,
%ymm0
,
%ymm10
vfmadd231ps
%ymm1
,
%ymm0
,
%ymm7
cmp
%r9d
,
%r14d
jg
1
b
But does the C function above generalize to all matrix sizes? Nope. If I
bump the complexity up from 512 to 1024, then I'm pretty much back at
square one, not doing much better than a naive kernel, and MKL wins once
more. I personally don't view this as too problematic, since llama.cpp
by default processes prompts in modestly sized batches, and a kernel
should only need to be good for its intended size. It's also only a
matter of time until I unriddle the tricks needed for optimal tiling and
cache locality that can make my kernels scale.
Now to incorporate this into llamafile, we can't use OpenMP for the same
reason we can't use BLAS libraries. The kernel must be harmonized with
the way llama.cpp works. Its threading model is very similar to GPUs.
Ops in the model graph are processed one by one. A thread is spawned for
each core. Threads are restrained by a spinlock barrier and then set
loose to compute different parts of an output matrix in parallel as soon
as the next op is ready for execution. The id of each thread is
called
ith
and the number of threads is
called
nth
. There are no futexes or semaphores, because
kernel scheduling would greatly reduce tokens/sec. If we were to have
the
ith=0
thread call a BLAS API that spawned threads of
its own, then they'd be immediately starved of resources by all
the
ith>0
threads returning to the spinlock barrier. We
can work within this model by defining a new kernel framework.
#define
BEGIN_KERNEL
(RM, RN) \
int
ytiles = (m - m0) / RM; \
int
xtiles = (n - n0) / RN; \
int
tiles = ytiles * xtiles; \
int
duty = (tiles + nth - 1) / nth; \
int
start = duty * ith; \
int
end = start + duty; \
if
(end > tiles) \
        end = tiles; \
for
(
int
job = start; job < end; ++job) { \
int
i = m0 + job / xtiles * RM; \
int
j = n0 + job % xtiles * RN;
#define
END_KERNEL
() }
Along with a solution for packing tiles.
template
<
typename
T>
class
GEMMER
{
public:
GEMMER
(
int
k,
const
T
*A,
int
lda,
const
T
*B,
int
ldb,
float
*C,
int
ldc,
int
ith,
int
nth)
        : k(k), A(A), lda(lda), B(B), ldb(ldb), C(C), ldc(ldc), ith(ith), nth(nth) {
    }
void
llmm
(
int
m,
int
n) {
        mnpack(0, m, 0, n);
    }
private:
void
mnpack
(
int
m0,
int
m,
int
n0,
int
n) {
if
(m - m0 <= 0 || n - n0 <= 0)
            return;
int
mc, nc, mp, np;
if
(m - m0 >= 3 && n - n0 >= 4) {
            mc = 3;
            nc = 4;
            llmm3x4(m0, m, n0, n);
        }
else if
(m - m0 >= 4 && n - n0 >= 1) {
            mc = 4;
            nc = 1;
            llmm4x1(m0, m, n0, n);
        }
else if
(m - m0 >= 1 && n - n0 >= 4) {
            mc = 1;
            nc = 4;
            llmm1x4(m0, m, n0, n);
        }
else
{
            mc = 1;
            nc = 1;
            llmm1x1(m0, m, n0, n);
        }
        mp = m0 + (m - m0) / mc * mc;
        np = n0 + (n - n0) / nc * nc;
        mnpack(mp, m, n0, np);
        mnpack(m0, mp, np, n);
        mnpack(mp, m, np, n);
    }
// ...
void
llmm1x1
(
int
m0,
int
m,
int
n0,
int
n) {
        BEGIN_KERNEL(1, 1)
__m256
c = _mm256_setzero_ps();
for
(
int
l = 0; l < k; l += 8)
            c = _mm256_fmadd_ps(_mm256_loadu_ps(A + lda * i + l),
                                _mm256_loadu_ps(B + ldb * j + l), c);
        C[ldc * j + i] = hsum(c);
        END_KERNEL()
    }
const
int
k;
const
T
*
const
A;
const
int
lda;
const
T
*
const
B;
const
int
ldb;
float
*
const
C;
const
int
ldc;
const
int
ith;
const
int
nth;
};
We can now export nice friendly C APIs to GGML that go 790 gigaflops
while incurring none of the latency disadvantages associated with
traditional BLAS libraries.
void
SLLMMT
(
int
m,
int
n,
int
k,
const
float
*A,
int
lda,
const
float
*B,
int
ldb,
float
*C,
int
ldc,
int
ith,
int
nth) {
if
(nth) {
GEMMER
<
float
> tb{k, A, lda, B, ldb, C, ldc, ith, nth};
        tb.llmm(m, n);
    }
else if
(!HAVE_OPENMP || n * m * k < THRESHOLD) {
GEMMER
<
float
> tb{k, A, lda, B, ldb, C, ldc, 0, 1};
        tb.llmm(m, n);
    }
else
{
        nth = sysconf(_SC_NPROCESSORS_ONLN);
#pragma omp parallel for
for
(ith = 0; ith < nth; ++ith) {
GEMMER
<
float
> tb{k, A, lda, B, ldb, C, ldc, ith, nth};
            tb.llmm(m, n);
        }
    }
}
You need to run the following command on Linux in order to benchmark
llamafile reliably. It also helps a little bit with timings to run as
root, but that shouldn't be necessary.
echo
performance | sudo tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
On Apple Silicon, I needed to build llama.cpp using the following
command in order to get it to run in CPU mode.
make -j32 LLAMA_NO_ACCELERATE=1 LLAMA_NO_METAL=1
Some of you might be surprised that I didn't write my kernels in
assembly like BLIS does, especially given my history of projects
like
blink
,
SectorLISP
and
SectorLAMBDA
. The truth is I've been
coding in assembly this whole time. I configured Emacs so I can push a
button, and the disassembly for the C++ code I'm working on will pop up
on the screen in a few milliseconds. I know anyone whose codebase has
slow build times doesn't possess this advantage, which has made me
famous. Once I figure out how to do that for .cu files, I'll be
unstoppable.
I learned how to write math kernels by renting
Vast
VMs and watching
Gautham Venkatasubramanian
and
mrdomino
develop CUDA kernels
in a tmux session. They've been focusing on solving a much more
important challenge for llamafile, which is helping it not have a
mandatory dependency on the cuBLAS: the reigning supreme linear algebra
library of such speed, accuracy, and ferocity that it could only have
been written by the prince of darkness himself. You're encouraged to
follow our ongoing progress on GitHub. The monospace font used on this
page is called
PragmataPro
and it
was was designed
by
Fabrizio
Schiavi
in Italy.
Congratulations on reading this far. I'd like to extend an invitation
for you to join us on the
Mozilla AI Discord
, where
you can ask questions and hang out with me, folks from Mozilla, and
others in the llamafile community.
My full-time work on open source projects like llamafile is funded
thanks to the generous support of Mozilla,
my
GitHub sponsors
, and
Patreon subscribers
. Thank
you everyone, for helping me have the opportunity to serve you these
last four years. Your support made it possible for high-quality math
kernels to be shared with the commons.
