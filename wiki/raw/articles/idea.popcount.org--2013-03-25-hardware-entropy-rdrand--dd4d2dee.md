---
title: "Hardware entropy: RDRAND"
url: "https://idea.popcount.org/2013-03-25-hardware-entropy-rdrand"
fetched_at: 2026-05-05T07:01:13.348672+00:00
source: "Marek Vavruša (idea.popcount)"
tags: [blog, raw]
---

# Hardware entropy: RDRAND

Source: https://idea.popcount.org/2013-03-25-hardware-entropy-rdrand

Hardware entropy: RDRAND
25 March 2013
This is the third blog post on machine instructions:
This time I've noticed
RdRand
instruction.
According to
Wikipedia
RdRand
is:
... a random number generator that is compliant with security and
cryptographic standards such as NIST SP800-90, FIPS 140-2,
and ANSI X9.82.
The generator uses an on-processor entropy source, which passes the
randomly generated bits to an AES (in CBC-MAC mode) conditioner to
distill the entropy into non-deterministic random numbers.
Sounds good. Basically
RdRand
is a
RNG
using
AES which seed (in theory) can't be extracted. Obviously, one need to
trust Intel that the "on-processor entropy source" generates good
entropy.
For those interested in the inner workings of the hardware generator,
David Wragg suggests
an excellent article from IEEE:
"Behind Intel's New Random-Number Generator"
.
Back to the instruction. Usage is not completely straightforward - one
must check the
carry flag
to see if there is enough entropy. Intel manual describes this situation as "unlikely":
Under heavy load, with multiple cores executing RDRAND in parallel,
it is possible, though unlikely, for the demand of random numbers by
software processes/threads to exceed the rate at which the random
number generator hardware can supply them. This will lead to the
RDRAND instruction returning no data transitorily. The RDRAND
instruction indicates the occurrence of this rare situation by
clearing the CF flag.
And here's
a working snippet stolen from the Linux kernel
:
#ifdef __x86_64__
#  define RDRAND_LONG ".byte 0x48,0x0f,0xc7,0xf0"
#else
#  define RDRAND_INT  ".byte 0x0f,0xc7,0xf0"
#  define RDRAND_LONG   RDRAND_INT
#endif
#define RDRAND_RETRY_LOOPS  10
static
inline
long
rdrand_long
(
unsigned
long
*
v
)
{
int
ok
;
asm
volatile
(
"1: "
RDRAND_LONG
"
\n\t
"
"jc 2f
\n\t
"
"decl %0
\n\t
"
"jnz 1b
\n\t
"
"2:"
:
"=r"
(
ok
),
"=a"
(
*
v
)
:
"0"
(
RDRAND_RETRY_LOOPS
));
return
ok
;
}
That's it. Now you have access to a supposedly good hardware-generated
entropy without the cost of a context switch.
