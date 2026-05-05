---
title: "Understanding DeepMind's Sorting Algorithm"
url: "https://justine.lol/sorting/"
fetched_at: 2026-05-05T07:01:27.635604+00:00
source: "Justine Tunney"
tags: [blog, raw]
---

# Understanding DeepMind's Sorting Algorithm

Source: https://justine.lol/sorting/

June 12
th
, 2023 @
justine's web page
Understanding DeepMind's Sorting Algorithm
A few days ago, DeepMind published a
blog
post
talking about a
paper
they wrote, where they discovered tinier kernels for sorting algorithms.
They did this by taking their deep learning wisdom, which they gained by
building AlphaGo, and applying it to the discipline of
of
superoptimization
.
That piqued my interest, since as a C library author, I'm always looking
for opportunities to curate the best stuff. In some ways that's really
the whole purpose of the C library. There are so many functions that we
as programmers take for granted, which are the finished product of
decades of research, distilled into plain and portable code.
DeepMind earned a fair amount of well-deserved attention for this
discovery, but unfortunately they could have done a much better job
explaining it. Let's start with the assembly code they published for
sorting an array with three items, translated from pseudo-assembly into
assembly:
/	move37.S
.equ
P,
%rax
.equ
Q,
%rcx
.equ
R,
%rdx
.equ
S,
%rsi
move37
:
mov
(
%rdi
),P
mov
8(
%rdi
),Q
mov
16(
%rdi
),R
mov
R,S
cmp
P,R
cmovg
P,R
cmovl
P,S
cmp
S,Q
cmovg
Q,P
cmovg
S,Q
mov
R,(
%rdi
)
mov
Q,8(
%rdi
)
mov
P,16(
%rdi
)
ret
.type
move37,
@function
.size
move37,.-move37
.globl
move37
// deepsort1.c
#include
<stdio.h>
void
move37
(
long
*);
int
main
() {
long
A[3] = {3, 1, 2};
  move37(A);
  printf(
"%d %d %d\n"
, A[0], A[1], A[2]);
}
I named this function
move37()
because the DeepMind blog
post compares it to the 37th move AlphaGo made during its second
match
with Lee Sedol
back in 2016. That's the move which stunned the
experts who thought AlphaGo had made a mistake, but they were wrong,
because the machine ultimately did achieve
victory
against its opponent, who saw himself as the Hector of humanity. So if
we run the DeepMind code:
# run this on the shell
cc -o deepsort1 deepsort1.c move37.S
./deepsort1
2 1 3
That looks like a mistake to me. The array we gave it was {3, 1, 2} but
move37()
sorted it into {2, 1, 3}. DeepMind must be
trolling us, because I don't believe that 2 comes before 1. Let's take a
look at the
open source contribution they
made to LLVM libcxx
which should hopefully clarify things:
// Ensures that *__x, *__y and *__z are ordered according to the comparator __c,
// under the assumption that *__y and *__z are already ordered.
template
<
class
_Compare,
class
_RandomAccessIterator>
inline
_LIBCPP_HIDE_FROM_ABI
void
__partially_sorted_swap
(
    _RandomAccessIterator __x, _RandomAccessIterator __y,
    _RandomAccessIterator __z, _Compare __c) {
using
value_type =
typename
iterator_traits<_RandomAccessIterator>::value_type;
bool
__r = __c(*__z, *__x);
  value_type __tmp = __r ? *__z : *__x;
  *__z = __r ? *__x : *__z;
  __r = __c(__tmp, *__y);
  *__x = __r ? *__x : *__y;
  *__y = __r ? *__y : __tmp;
}
Now it makes sense. So
move37()
isn't actually a sorting
function. It's a sorting
kernel
that's intended to be used as
the building block of the
sort3()
function. It would have
been nice if the paper and blog post had mentioned that, since it made
me feel quite confused for the briefest of moments. Here's a better
version of the code, which includes the missing swap operation.
sort3
:
mov
(
%rdi
),
%rcx
mov
8(
%rdi
),
%rdx
mov
16(
%rdi
),
%rsi
mov
%rdx
,
%rax
cmp
%rdx
,
%rsi
cmovl
%rsi
,
%rax
cmovl
%rdx
,
%rsi
mov
%rcx
,
%rdx
cmp
%rcx
,
%rsi
cmovl
%rsi
,
%rdx
cmovl
%rcx
,
%rsi
cmp
%rax
,
%rdx
cmovge
%rax
,
%rcx
cmovl
%rax
,
%rdx
mov
%rcx
,(
%rdi
)
mov
%rdx
,8(
%rdi
)
mov
%rsi
,16(
%rdi
)
ret
.globl
sort3
.size
sort3,.-sort3
To explain why their code is important, let's consider how this
algorithm works at a high level. When I first tried to solve
the
sort3()
problem on my own, I came up with this:
// sorts [a,b,c]
if
(a > b) SWAP(a, b);
if
(a > c) SWAP(a, c);
if
(b > c) SWAP(b, c);
Then I looked at libcxx and found out they were doing the same thing.
The issue with the code above is that compilers aren't very good at
optimizing it. If you try to compile the above code, you'll notice that
your compiler inserts a lot of branch instructions. This is what
DeepMind sought to improve upon with their LLVM contribution, because
cleverer ways exist to code this sort of thing. However those techniques
tend to be less understandable. I actually like my naive code, since if
we squint our eyes a bit, we can see a pattern exists where it shares
the same basic idea as DeepMind's state of the art assembly code. That
idea is this problem essentially boils down into being just three
compare and swap operations:
mov
%rdx
,
%rax
// create temporary
cmp
%rdx
,
%rsi
// compare
cmovl
%rsi
,
%rax
// conditional move
cmovl
%rdx
,
%rsi
// conditional move
/
repeat thrice
The above code was the state of the art beforehand for sorting networks.
Now here's where DeepMind's novel discovery came into play. They found
out that sometimes the
mov
instruction above is
unnecessary.
sort3
:
mov
(
%rdi
),
%rcx
mov
8(
%rdi
),
%rdx
mov
16(
%rdi
),
%rsi
mov
%rdx
,
%rax
cmp
%rdx
,
%rsi
cmovl
%rsi
,
%rax
cmovl
%rdx
,
%rsi
mov
%rcx
,
%rdx
cmp
%rcx
,
%rsi
cmovl
%rsi
,
%rdx
cmovl
%rcx
,
%rsi
mov
%rdx
,
%rcx
// <-- wrekt by AlphaDev
cmp
%rax
,
%rdx
cmovge
%rax
,
%rcx
cmovl
%rax
,
%rdx
mov
%rcx
,(
%rdi
)
mov
%rdx
,8(
%rdi
)
mov
%rsi
,16(
%rdi
)
ret
If you try running the above code, then you'll see it's 100% correct
with or without the striked-out line. The line of code looks like it's
doing something, but it's actually doing nothing. So it doesn't surprise
me that something like this could have gone unnoticed by computer
science for decades. It should also become clearer now how AlphaDev
works. DeepMind basically built an artificial intelligence that fiddles
around with assembly code and deletes stuff at random to see if it
breaks. I'm not saying this to dismiss AlphaDev's intelligence, since
I'd be lying if I said I wasn't doing the same thing.
sort3
:
mov
(
%rdi
),
%rcx
mov
8(
%rdi
),
%rdx
mov
16(
%rdi
),
%rsi
mov
%rdx
,
%rax
// can it go?
cmp
%rdx
,
%rsi
cmovl
%rsi
,
%rax
cmovl
%rdx
,
%rsi
mov
%rcx
,
%rdx
// can it go?
cmp
%rcx
,
%rsi
cmovl
%rsi
,
%rdx
cmovl
%rcx
,
%rsi
mov
%rdx
,
%rcx
// <-- wrekt by AlphaDev
cmp
%rax
,
%rdx
cmovge
%rax
,
%rcx
cmovl
%rax
,
%rdx
mov
%rcx
,(
%rdi
)
mov
%rdx
,8(
%rdi
)
mov
%rsi
,16(
%rdi
)
ret
DeepMind also left some meat on the table. There's still two more
mov
instructions in the above code we could potentially
shave away. One of the ways we might do that is by using the ARM64
instruction set, which yields tinier code for problems like these. Here
we see that we don't need any instructions for creating temporary
variables:
sort3
:
ldp
x1,x2,[x0]
ldr
x3,[x0,16]
cmp
x2,x3
csel
x4,x2,x3,le
csel
x2,x2,x3,ge
cmp
x2,x1
csel
x3,x2,x1,le
csel
x2,x2,x1,ge
cmp
x4,x3
csel
x5,x1,x4,gt
csel
x4,x4,x3,ge
stp
x5,x4,[x0]
str
x2,[x0,16]
ret
Arm is all the rage these days, and I imagine the example above serves
as evidence of why they've earned their fame. Arm Limited is also one of
the most benevolent companies in open source right now. For example,
their
MbedTLS
library
is one of the most underrated gems I've seen so far. When I started
using it, I originally had this scheme of modifying Arm's code to work
better on x86 hardware instead. I wrote all these tricked out assembly
optimizations bringing it to the same realm of performance as OpenSSL on
x86. MbedTLS is plain, portable, hackable C code, so this is good news
for anyone wanting a crypto library that isn't assembly generated by
Perl. I told the folks at Arm what I was doing, and instead of finding
it subversive they were very kind and encouraging, since that's the kind
of people they are. One day I hope to find time to do what DeepMind did,
and upstream my modifications. Arm is also prolific for
their
Optimized
Routines
library, which is up there with
double-conversion
in terms of impeccable quality. It's of particular interest to C
libraries, since for decades the open source community has subsisted off
math functions written by Sun Microsystems back in the early 90's. Arm
found a way to improve upon several of them, such
as
pow(x,y)
. That's a very high impact thing to do,
considering it's a one of the most fundamental operations in math. For
example, if you use Arm's solution in pure software to
implement
pow(x,y)
on an x86 machine, then it'll go 5x
faster than Intel's native x87 instructions for doing the same thing.
Since we're so fortunate to have DeepMind entering this game too, I've
taken the liberty of translating their libcxx diff into plain readable C
code, so that everyone can appreciate its beauty. It's another thing I
would have liked to see included in the paper and blog post, because in
this code you'll find the canonical trick that experts use for getting
compilers to generate branchless
MOVcc
instructions.
// sorts [a,b]
static inline
void
Sort2
(
long
*a,
long
*b) {
int
r = *a < *b;
long
t = r ? *a : *b;
  *b = r ? *b : *a;
  *a = t;
}
// sorts [a,b,c] assuming [b,c] is already sorted
static inline
void
PartialSort3
(
long
*a,
long
*b,
long
*c) {
int
r = *c < *a;
long
t = r ? *c : *a;
  *c = r ? *a : *c;
  r = t < *b;
  *a = r ? *a : *b;
  *b = r ? *b : t;
}
// sorts [a,b,c]
static inline
void
Sort3
(
long
*a,
long
*b,
long
*c) {
  Sort2(b, c);
  PartialSort3(a, b, c);
}
// sorts [a,b,c,d]
static inline
void
Sort4
(
long
*a,
long
*b,
long
*c,
long
*d) {
  Sort2(a, c);
  Sort2(b, d);
  Sort2(a, b);
  Sort2(c, d);
  Sort2(b, c);
}
// sorts [a,b,c,d,e]
static inline
void
Sort5
(
long
*a,
long
*b,
long
*c,
long
*d,
long
*e) {
  Sort2(a, b);
  Sort2(d, e);
  PartialSort3(c, d, e);
  Sort2(b, e);
  PartialSort3(a, c, d);
  PartialSort3(b, c, d);
}
Once I saw the
Sort5()
function, I felt like I had gained a
better understanding of what had motivated DeepMind's research. If you
compile the
Sort5()
function on ARM64, then your compiler
will produce a function juggling 11 registers. If you were reasoning
about a mathematical equation, then would you be able to hold eleven
variables in your working memory at once? Probably not, which is why
having a nice kernel function like
PartialSort3
is so
useful. As sentient creatures, human beings aren't that much different
from the monkeys we once were. The main thing that makes us intelligent
is our ability to take hard problems and break them down into smaller
ones. So it's nice to see deep learning being applied to turbocharging
our abstractions.
It's also worth mentioning that
Sort3()
and
Sort5()
are kernels themselves, since they're intended
to be building blocks for a conventional sorting function. The blog post
covers this topic, but I thought it'd be useful to share something
that's actually portable and executable.
static inline
void
InsertionSort
(
long
*A,
long
n) {
long
i, j, t;
for
(i = 1; i < n; i++) {
    t = A[i];
    j = i - 1;
while
(j >= 0 && A[j] > t) {
      A[j + 1] = A[j];
      j = j - 1;
    }
    A[j + 1] = t;
  }
}
void
longsort
(
long
*A,
long
n) {
long
t, p, i, j;
switch
(n) {
case
0:
return
;
case
1:
return
;
case
2:
return
Sort2(A, A + 1);
case
3:
return
Sort3(A, A + 1, A + 2);
case
4:
return
Sort4(A, A + 1, A + 2, A + 3);
case
5:
return
Sort5(A, A + 1, A + 2, A + 3, A + 4);
default:
if
(n <= 32) {
        InsertionSort(A, n);
      }
else
{
for
(p = A[n >> 1], i = 0, j = n - 1;; i++, j--) {
while
(A[i] < p) i++;
while
(A[j] > p) j--;
          if (i >= j)
break
;
          t = A[i];
          A[i] = A[j];
          A[j] = t;
        }
        longsort(A, i);
        longsort(A + i, n - i);
      }
break
;
  }
}
The above algorithm shows what the new and improved libcxx is doing.
It's basically quicksort except it switches to the sorting kernels and
insertion sort when recursing into smaller slices. With libcxx I think
they even took the added step of schlepping in heapsort, which is kind
of slow, but prevents adversaries from smashing your stack.
The main thing you may be wondering at this point is, can I use this? Do
these sorting network kernels actually make sorting go faster? I would
say yes and no. When all you want is to sort ascending longs, the code
above will go 2x faster than the standard
qsort()
function
provided by your C library. Except you don't need the kernels to do
that. What I've determined so far is that, on my personal computer
(which has an Intel Core i9-12900KS) the above function sorts longs at
255 megabytes per second. However if I comment out the sorting kernels:
void
longsort
(
long
*A,
long
n) {
long
t, p, i, j;
switch
(n) {
case
0:
return
;
case
1:
return
;
/* case 2: */
/*   return Sort2(A, A + 1); */
/* case 3: */
/*   return Sort3(A, A + 1, A + 2); */
/* case 4: */
/*   return Sort4(A, A + 1, A + 2, A + 3); */
/* case 5: */
/*   return Sort5(A, A + 1, A + 2, A + 3, A + 4); */
default:
if
(n <= 32) {
        InsertionSort(A, n);
      }
else
{
for
(p = A[n >> 1], i = 0, j = n - 1;; i++, j--) {
while
(A[i] < p) i++;
while
(A[j] > p) j--;
          if (i >= j)
break
;
          t = A[i];
          A[i] = A[j];
          A[j] = t;
        }
        longsort(A, i);
        longsort(A + i, n - i);
      }
break
;
  }
}
Then my
longsort()
function goes 275 megabytes per second.
I achieved 7% better performance by dumbing down the algorithm. I say
let Intel do the damage. This is the function cosmopolitan libc uses to
sort elf symbol tables when loading your executables. The nice thing
about
long
is it's long enough to store an
int
key value pair. Being able to sort map entries fast is useful trick to
have. Blending naive quicksort with naive insertion sort is the best
solution I've found so far, in terms of striking a balance between
tininess and performance that's just right for my use case. The above
function compiles down to just 181 bytes of x86-64 machine code. Since
DeepMind's
sort3()
is only 42 bytes, I was hoping I could
trade away some size to gain a performance advantage. Since the next
best algorithm I've found so far would be switching to radix sort, which
goes 400 MB/s but needs a whopping 763 bytes of binary footprint, in
addition to depending on
malloc()
. So it would have been
nice to see these kernels do better.
That's not to imply DeepMind's ideas don't have merit. I think it's
important to note that DeepMind was generous enough to give us their
vectorized
quicksort
library last year (back when they were called Google
Brain) and in doing so achieved a sorting supremacy that can never be
challenged. Vqsort literally sorts longs at 1155 MB/s on my computer. It
even marginally outperforms
djbsort
, which is one of the
most beloved libraries in the open source community even though it never
generalized to more data types than
int
. The way both
implementations pulled it off is by vectorizing sorting networks. I
think that's where the sorting network technique truly shines. I imagine
AlphaDev would have done that if it weren't still a toddler as far as
intelligent entities go. When you're starting from first principles, the
baseline instruction set alone is enormously difficult to support. If we
wait, then I think we can expect to see great things from AlphaDev in
the future, as it works its way up to more formidable challenges.
I also just love the fact that DeepMind is making algorithms tinier,
since that's something I don't see very often. Size coding is one of my
favorite hobbies. On this blog I've published
a
383 byte virtual machine for
lambda calculus
and
a
lisp machine with garbage
collection in 436 bytes
. I've also blogged about
the
size optimization
tricks
I've used for
the
cosmpolitan c
library
. I love DeepMind's parent company too, since Google
awarded
me an open source peer bonus
a few weeks ago, and it's nice to see
them sharing my passion for making software smaller. It'd be great to
see them using it to improve vectorized quicksort. I would love nothing
more than to have the world's best longsort not be a C++ monster that
adds 24kB of binary footprint. It's 23,000 lines of assembly for
ascending long sort alone. Those are the lines of code I can't wait to
see AlphaDev ravage someday.
Finally, I like the idea of an artificial intelligence company building
machines that write code in machine language. Why wouldn't they? It's in
a machine's nature to be a machine. As a builder I find that much less
triggering than the future OpenAI is creating, where they've built a
great big paternalistic machine that competes with every builder on
earth in a zero-sum economy, and then enticing the rent-seekers of the
world to take control of that machine through government regulation. I
don't think it's progress that OpenAI is promising to automate all the
tasks I love doing most, like coding. What I want is to be able to
control a machine that's able to do the things I'm not able to do on my
own, like discovering sorting kernels. That's the real kind of progress
that's going to help humanity enrich itself, and I view every line of
assembly we can shave away as a step in a positive direction towards
that dream.
