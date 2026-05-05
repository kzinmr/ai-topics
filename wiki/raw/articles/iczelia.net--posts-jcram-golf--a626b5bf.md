---
title: "jcram: a principled approach to code golf."
url: "https://iczelia.net/posts/jcram-golf/"
fetched_at: 2026-05-05T07:01:19.809892+00:00
source: "Kamila Szewczyk (iczelia)"
tags: [blog, raw]
---

# jcram: a principled approach to code golf.

Source: https://iczelia.net/posts/jcram-golf/

This blog post will be a bit more relaxed than the previous ones. We will discuss (at least the more interesting topics) ground-up, perform a lot of experimentation and hopefully have fun.
An introduction to code golf
⌗
Code golf is a recreational computer programming activity in which participants strive to write the shortest possible program that accomplishes a certain loosely defined task. It stems from APL and Perl programming communities - languages widely known as remarkably terse and compact - and has since then become a popular pastime in many other programming communities. Since then, many languages have been designed with the explicit goal of making code golfing easier: 05AB1E, Jelly, Pyth, GolfScript and many others.
The principle on which languages made specifically for codegolf work is simple: they try to eliminate as much boilerplate as possible, make the language grammar terser, and most importantly provide a rich set of built-in functions and operators that can be used to solve a wide range of problems. The choice of primitive functions is a crucial part of the design of such languages: in principle, the core set of primitive functions should be as general as possible, while auxiliary functions that utilise multi-byte sequences should be geared towards solving more specific problems.
Information theoretic background
⌗
It is generally impossible to find the shortest possible program for a given task, as this would require solving the Kolmogorov complexity problem, which is undecidable. Further, if we consider a simple pseudocode foundation, code-golf languages can be understood as an application of the Lempel-Ziv algorithm with a pre-defined dictionary: the language’s built-in functions and operators. This realisation leads to a chain of realisations: existing codecs (like Brotli) make use of a fixed built-in dictionary to compress small files very efficiently.
Those familiar with data compression will wonder whether this application of the Lempel-Ziv algorithm with a fixed dictionary is indeed a good way to approach the problem of creating a golfing language. After all, general purpose data compressors such as
bzip2
,
bzip3
or
PPMd
excel at compressing text files and often outperform Lempel-Ziv codecs. Of course, we can not reach for this fruit yet: we need a replacement for the fixed dictionary that is more suitable for code-golfing.
This and many other topics are discussed in my book, which is currently in the works. The book is a comprehensive guide to data compression, covering the theoretical and practical foundations of the field, as well as the latest advancements like the Asymmetric Numeral Systems (ANS). If you are interested in the book, make sure to follow my website for updates - I also maintain a RSS feed for the newest blog posts. Despite having a neglible impact on the field myself, I worked on the book as an attempt to explain intricate concepts introduced by the seminal figures of data compression - that I have struggled with myself - in a simple and accessible manner.
The game plan
⌗
We will design a simple statistical data compressor and train it on a large corpus of code-golf problems. This way, the compressor can learn about common patterns in golfed code and hopefully exploit them in incoming input. The training process is rather difficult: First, we need to obtain a dataset. Then, we need to clean it up (remove any auxiliary code, comments, etc.) and extract a few validation samples to test the compressor on. We should focus our attention to representative samples of problem solutions: ignore excessively short or long solutions, solutions that have long string literals, etc…
Another problem is the language that we wish to use as the foundation for our compressor. Ideally, we want to pick a
conventional
programming language: a PPM compressor trained on a corpus of golfed code (to which the static dictionary Lempel-Ziv algorithm has been applied) will not be able to correlate contexts of the input. On the other hand, we would like to ideally avoid using a language that explicitly names its variables: while the programs
f=a=>b=>a+b
and
f=m=>n=>m+n
are semantically equivalent, they name their variables differently and thus the compressor will not be able to correlate them as well as a point-free program (Factor, APL, etc…).
To wrap it up, we want a language that was not designed to be terse: this way, the model will be able to compress it better: it is empirically easy to demonstrate that “stacking” compression algorithms is not a good idea:
% lz4 -12k dfns.dws 2>/dev/null
 % bzip3 dfns.dws
 % bzip3 dfns.dws.lz4
 % wc -c dfns.*
5917824 dfns.dws
 769405 dfns.dws.bz3
1392801 dfns.dws.lz4
1146664 dfns.dws.lz4.bz3
On the other hand, we want a language such that semantically equivalent programs are as synactically similar as possible. Finally, we want to pick a relatively common language so that the model can ascertain information about how the language is used in practice.
Unfortunately, to my knowledge (as of 25-02) there was no such language, hence I have settled on JavaScript: this is not a fantastic choice, as JavaScript does not satisfy the second desirable property that we were so keen on, but it is a perfect fit for the other two: there are many accessible JavaScript programs available that we can use to train the compressor. Further, JavaScript is a rather explicit language: it is not designed to be terse, hence it should be easier to compress.
The training phase
⌗
I have prepared a small toy compressor that we will train now. I have obtained approximately a few megabytes of diverse, minified code. Then, I have filtered it to remove not very interesting or excessively verbose snippets. This is one of the pivotal points in the process: the data is generally wildly diverse, and we need to make sure that it is actually representative of code golf programs. Hence, we should replace long defined identifiers with short ones (even if it makes the code stop working, it doesn’t entirely matter) and replace common “long” patterns (e.g. anonymous functions using
function
and not
=>
) with shorter ones. This is a rather difficult process, and I have not done it perfectly, but it should be good enough for this experiment.
Anyway, after the filtering and fixing process is over we have approximately 700KB of diverse code to train on, representing approximately 10'000 different minified code snippets. The resulting model is 120MB, amounting to approximately 30MB gzipped.
Format details
⌗
A lot of code golf programs are generally shorter than a hundred bytes, hence we could use a single byte for encoding the length. However, to support longer programs efficiently, we will use the highest bit of the first byte to determine how big is the program: a cleared value signals length under 128 bytes represented by the trailing bits, a set value signals that the length is represented by the trailing 7 bits of the first byte and the whole 8 bits of the next byte. This way we can support programs at most 32K long, which should be more than enough for our purposes. When the format was finished, I made the following online playground for the compressor:
jcram
. The compressor is fast enough to compress data in real time.
Further, I have decided to (semi-jokingly) invent a single byte character set for the resulting “golfing language” that I chose to name
jcram
.
Initial results
⌗
I have compressed a few programs that may have already been (partially) in the dataset: a “Hello, world!” program, a function that adds two numbers and a Fibonacci function
Initial demo
It is easy to see that in the “Hello, world!” example, the message was already present in the dataset: the compressor’s output did not change, bar the length byte, when we completed the program. Let’s try out some programs that are definitely
not
in the dataset:
Arnauld’s “Swap letter cases”
program on the site CodeGolf StackExchange:
Compresses, astonishingly, to the following 6 byte sequence:
∑∣⍘⍥Ⓡ⏛
This is perhaps not very surprising: string replacements and the regular expression for lowercase letters are pretty common in JavaScript code. For example, the following program similar in syntactic structure compresses down to 7 bytes:
While the following semantically equivalent program compresses to 8 bytes:
The problem with variable names and context recognition becomes really glaring, but there is very little (to my knowledge) that we can do to fix it. Trying to apply the same trick with renaming the lambda variable to
a
in Arnauld’s program makes it blow up in size almost twice.
Experiments with JSFuck
⌗
Let’s do something utterly useless! We will pass a few programs through JSFuck and try to measure the compression ratio on these.
alert(1)
- 8 bytes, jsfuck: 853 bytes, then jcram: 63 bytes
f=n=>n<2?n:f(n-1)+f(n-2)
- 24 bytes, jsfuck: 6228 bytes, then jcram: 214 bytes
(n,k)=>k<0||k>n?0:Array.from({length:k},(_,i)=>(n-i)/(i+1)).reduce((a,b)=>a*b)
- 78 bytes, jsfuck: 11229 bytes, then jcram: 353
We notice that the expansion ratio resulting from this transformation is generally not as bad as it might have seemed initially: it seems to tend to smaller values as the program size grows.
An interesting venue of thought is golfing the last binomial coefficient. Given that we have access to math.js, ramda and underscore.js, we can make the code a bit more functional:
(n,k)=>k<0||k>n?0:Array.from({length:k},(_,i)=>(n-i)/(i+1)).reduce((a,b)=>a*b)
- 78 -> 23 bytes.
(n,k)=>_.chain(_.range(k)).map(i=>(n-i)/(i+1)).reduce((a,b)=>a*b)
- 65 -> 21 bytes.
f=(n,k)=>!k||k==n?1:f(n-1,k-1)+f(n-1,k)
- 39 -> 11 bytes.
Wrapping up
⌗
From this discussion it becomes clear that a sufficiently sophisticated compressor is definitely capable of beating code golf languages on non-trivial problems. Does this carry any further implications regarding golfing language construction? Is it fair, or just a cop-out? Can golfing in jcram (i.e. trying to find patterns that “please” the compressor) be considered a form of cheating?
I hope that you have enjoyed this article and that it has given you some food for thought. I am looking forward to your comments, feedback and discussion.
