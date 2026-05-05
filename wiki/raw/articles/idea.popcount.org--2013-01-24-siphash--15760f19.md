---
title: "SipHash - Idea of the day"
url: "https://idea.popcount.org/2013-01-24-siphash"
fetched_at: 2026-05-05T07:01:13.604302+00:00
source: "Marek Vavruša (idea.popcount)"
tags: [blog, raw]
---

# SipHash - Idea of the day

Source: https://idea.popcount.org/2013-01-24-siphash

SipHash
24 January 2013
On 29C3 djb, Jean-Philippe Aumasson and Martin Boßlet gave a very
interesting
talk on SipHash
(
see the video
).
In short -
SipHash
is a new hash,
created especially to save you from hash flooding attacks. The hash
takes two parameters - a 128 bit "secret" key and an arbitrary data
blob. This is different from traditional hashes which required only a
data blob as an input. SipHash outputs a secure 64 bit hash.
SipHash is described in detail in the extremely well written
paper
.
python
SipHash seems to be pretty easy to implement - I took a chance and
implemented it in Python:
https://github.com/majek/pysiphash
.
Use
pip
for the installation:
Usage is rather obvious:
>>>
import
siphash
>>>
key
=
'0123456789ABCDEF'
>>>
siphash
.
SipHash_2_4
(
key
,
'a'
)
.
hash
()
12398370950267227270L
c
I also wrote a
C version
,
although I must admit the code is quite closely based on the
reference implementation
.
The minimalistic usage example:
#include <stdio.h>
#include <stdint.h>
#include <string.h>
uint64_t
siphash24
(
const
char
*
in
,
unsigned
long
inlen
,
const
char
k
[
16
]);
int
main
()
{
char
key
[
16
]
=
{
0
,
1
,
2
,
3
,
4
,
5
,
6
,
7
,
8
,
9
,
0xa
,
0xb
,
0xc
,
0xd
,
0xe
,
0xf
};
char
*
pt
=
"hello world!"
;
uint64_t
hash
=
siphash24
(
pt
,
strlen
(
pt
),
key
);
printf
(
"plaintext=%s hash=%llu
\n
"
,
pt
,
hash
);
return
0
;
}
In my
C SipHash implementation
I tried to keep the code as short and as readable as possible. In
total the code is 90-odd lines long of which around half is real
code.
45 lines of C code is an excellent result for a strong hash. Thanks
Jean-Philippe for a great hash!
Continue reading about
bitslicing SipHash →
