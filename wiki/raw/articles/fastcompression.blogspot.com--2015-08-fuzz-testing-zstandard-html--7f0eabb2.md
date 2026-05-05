---
title: "RealTime Data Compression"
url: "http://fastcompression.blogspot.com/2015/08/fuzz-testing-zstandard.html"
fetched_at: 2026-05-05T07:01:00.257686+00:00
source: "Yann Collet (LZ4/Zstd)"
tags: [blog, raw]
---

# RealTime Data Compression

Source: http://fastcompression.blogspot.com/2015/08/fuzz-testing-zstandard.html

An advance issue that any production-grade codec must face is the ability to deal with erroneous data.
Such requirement tends to come at a second development stage, since it's already difficult enough to make an algorithm work under "normal conditions". Before reaching erroneous data, there is already a large number of valid edge cases to properly deal with.
Erroneous input is nonetheless important, not least because it can degenerate into a full program crash if not properly taken care of. At a more advanced level, it can even serve as an attack vector, trying to push some executable code into unauthorized memory segments. Even without reaching that point, just the perspective to make a system crash with the use of a predictable pattern is a good enough nuisance.
Dealing with such problems can be partially mitigated using stringent
unit tests
. But that's more easily said than done. Sometimes, not only is it painful to build
and maintain
a thorough and wishfully complete list of unit test for each function, it's also useless in predicting some unexpected behavior resulting from an improbable chain of events at different stages in the program.
Hence the idea to find such bugs at "system level". The system's input will be fed with a set of data, and the results will be observed. If you create test set manually, you will likely test some important, visible and expected use cases, which is still a pretty good start. But some less obvious interaction patterns will be missed.
That's where starts the realm of
Fuzz Testing
. The main idea is that random will make a better job at finding stupid forgotten edge cases, which are good candidates to crash a program. And it works pretty well. But how to setup "random" ?
In fact, even "random" must be defined within some limits. For example, if you only feed a lossless compression algorithm with some random input, it will simply not be able to compress it, meaning you will always test the same code path.
The way I've dealt with such issue for
lz4
or
zstd
is to create programs able to generate "random compressible data", with some programmable characteristics (compressibility, symbol variation, reproducible by seed). And it helped a lot to test valid code path.
The decompression side is more interested by resistance to invalid input. But even with random parameters, there is a need to target interesting properties to test. Typically, a valid decompression stage is first run, to serve as a model. Then some "credible" fail scenarios are built from them. Zstd fuzzer tool typically tests : truncated input, too small destination buffer, and noisy source created from a valid one with some random changes, in order to bypass too simple screening stages.
All these tests were extremely useful to strengthen the reliability of the code. But the idea that "random" was in fact defined within some limits make it clear that maybe some other code path, outside of limits of "random", may still fail if properly triggered.
But how to find them ? As stated earlier, brute force is not a good approach. There are too many similar cases which would be trivially reduced to a single code path. For example, the compressed format of
zstd
includes an initial 4-bytes identifier. A dumb random input would therefore have a 1 in 4 billion chances to pass such early screening, leaving little energy to test the rest of the code.
For a long time, I believed it was necessary to know in details one's code to create some useful fuzzer tool. Thanks to kind notification from Vitaly Magerya, it seems this is no longer the only one solution. I discovered earlier today the
American Fuzzy Lop
. No, not the rabbit;
this
test tool, by
Michał Zalewski
.
It's
relatively
easy to setup (for Unix programmers). Build, install and usage follow clean conventions, and the Readme is a fairly good read, easy to follow. With just a few initial test cases to provide, a special compilation stage and a command line, the tool is ready to go.
American Fuzzy Lop, testing zstd decoder
It displays a simple live board in text mode, which successfully captures the mind. One can see, or rather guess, how the genetic algorithm tries to create new use cases. It basically starts from the initially provided set of tests, and create new ones by modifying them using simple transformations. It analyzes the results, which are relatively precise thanks to special instrumentation installed in the target binary during the compilation stage. It deduces from them the triggered code path and if it has found a new one. Then generate new test cases built on top of "promising" previous ones, restart, ad infinitum.
This is simple and brilliant. Most importantly, it is
generic
, meaning no special knowledge of zstd was required for it to test thoroughly the algorithm and its associated source code.
There are obviously limits. For example, the amount of memory that can be spent for each test. Therefore, successfully resisting for hours the tricky tests created by this fuzzer tool is not the same as "bug free", but it's a damn good step into this direction, and would at least deserve the term "robust".
Anyway, the result of all these tests, using internal and external fuzzer tools, is
a first release of Zstandard
. It's not yet "format stable", meaning specifically that the current format is not guaranteed to remain unmodified in the future (such stage is planned to be reached early 2016). But it's already quite robust. So if you wanted to test the algorithm in your application, now seems a good time,
even in production environment
.
[Edit]
: If you're interested in fuzz testing, I recommend reading an
excellent follow up by Maciej Adamczyk
, which get into great details on how to do your own fuzz testing for your project.
