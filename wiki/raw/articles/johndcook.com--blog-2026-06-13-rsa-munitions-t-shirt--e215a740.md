---
title: "RSA munitions T-shirt"
url: "https://www.johndcook.com/blog/2026/06/13/rsa-munitions-t-shirt/"
fetched_at: 2026-06-14T07:00:54.216872+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# RSA munitions T-shirt

Source: https://www.johndcook.com/blog/2026/06/13/rsa-munitions-t-shirt/

Back when the US government classified strong encryption as “munitions,” RSA public key cryptography was illegal to export. In 1995, Adam Back protested this by creating a terse, obfuscated implementation of RSA in Perl code and used it as an email signature.
The code was also printed on T-shirts. The shirt was classified as munitions because it contained source code for strong encryption. More on the shirt
here
.
This was the code:
#!/bin/perl -s-- -export-a-crypto-system-sig -RSA-3-lines-PERL
$m=unpack(H.$w,$m."\0"x$w),$_=`echo "16do$w 2+4Oi0$d*-^1[d2%Sa
2/d0<X+d*La1=z\U$n%0]SX$k"[$m*]\EszlXx++p|dc`,s/^.|\W//g,print
pack('H*',$_)while read(STDIN,$m,($w=2*$d-1+length$n&~1)/2)
My initial intention was to unpack the code, explaining each piece in detail. I don’t have the time or patience for that, and I imagine many readers don’t either. For more of a blow-by-blow explanation, see this
commentary
from 1995.
dc
In the middle of the code is
echo ... | dc
This is the most dense and most important part of the code. Perl calls the
dc
calculator to do the arbitrary precision arithmetic that RSA encryption requires.
I’ve written about
bc
several times.
bc
(“basic calculator”) was a originally a more user-friendly wrapper around the reverse-Polish
dc
(“desktop calculator”).
dc
is still part of every Unix and Unix-like system, but I imagine
bc
is far more popular.
The important feature of
dc
for this post is that it is stack-based, meaning that users would push data and commands on to the stack and pop results off the stack. A sequence of commands that might be understandable when interactively using
dc
would look cryptic in a transcript. This is part of what makes the code so cryptic.
I’ll parse just a tiny bit of the
dc
code to give a flavor of what it does. The first four characters
16do
instructs
dc
to push 16 on to the stack, duplicate it, and set the output radix to 16, i.e. these four characters tell
dc
to work in hexadecimal.
Believe it or not, the
dc
code is computing
m
k
mod
n
using
fast exponentiation
, which is the key step in the RSA algorithm.
Textbook RSA
Note that Adam Back’s code is computing what we would now call textbook RSA, not RSA as it has been refined over the years and is
currently implemented
.
Related posts
