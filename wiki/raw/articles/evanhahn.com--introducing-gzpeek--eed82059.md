---
title: "Introducing gzpeek, a tool to parse gzip metadata"
url: "https://evanhahn.com/introducing-gzpeek/"
fetched_at: 2026-04-29T07:02:20.032946+00:00
source: "evanhahn.com"
tags: [blog, raw]
---

# Introducing gzpeek, a tool to parse gzip metadata

Source: https://evanhahn.com/introducing-gzpeek/

Introducing gzpeek, a tool to parse gzip metadata
In short: gzip streams contain metadata, like the operating system that did the compression. I built
a tool
to read this metadata.
I love reading specifications for file formats. They always have little surprises.
I had assumed that the gzip format was strictly used for compression. My guess was: a few bytes of bookkeeping, the compressed data, and maybe a checksum.
But then I read
the spec
. The gzip header holds more than I expected!
In addition to two bytes identifying the data as gzip, there’s also:
The
operating system
that did the compression. This was super surprising to me! There’s a single byte that identifies the compressor’s OS:
0
for Windows,
1
for the Amiga,
3
for Unix, and many others I’d never heard of. Compressors can also set
255
for an “unknown” OS.
Different tools set this value differently. zlib, the most popular gzip library,
changes the flag based on the operating system
. (It even defines some OSes that aren’t in the spec, like
18
for BeOS.) Many other libraries build atop zlib and inherit this behavior, such as .NET’s
GZipStream
, Ruby’s
GzipWriter
, and PHP’s
gzencode
.
Java’s
GZIPOutputStream
, JavaScript’s
CompressionStream
, and Go’s
compress/gzip
set the OS to “unknown” regardless of operating system. Some, like Zopfli and Apache’s
mod_deflate
, hard-code it to “Unix” no matter what.
All that to say: in practice, you can’t rely on this flag to determine the source OS, but it can give you a hint.
Modification time
for the data. This can be the time that compression started or the modification time of the file. It can also be set to
0
if you don’t want to communicate a time.
This is represented as an unsigned 32-bit integer in the Unix format. That means it can represent any moment between January 1, 1970 and February 7, 2106. I hope we devise a better compression format in the next ~80 years, because we can only represent dates in that range.
In my testing, many implementations set this to
0
. A few set it to the current time or the file’s modification time—the
gzip
command is one of these.
FTEXT
, a boolean flag vaguely indicating that the data is “probably ASCII text”. When I say vaguely, I mean it: the spec “deliberately [does] not specify the algorithm used to set this”. This is apparently for systems which have different storage formats for ASCII and binary data.
In all my testing, nobody sets this flag to anything but
0
.
An extra flag
indicating how hard the compressor worked.
2
signals that it was compressed with max compression (e.g.,
gzip -9
),
4
for the fastest algorithm, and
0
for everything else.
In practice, zlib and many others set this correctly per the spec, but some tools hard-code it to
0
. And as far as I can tell, this byte is not used during decompression, so it doesn’t really matter.
The
original file name
. For example, when I run
gzip my_file.txt
, the name is set to
my_file.txt
. This field is optional, so many tools don’t set it, but the
gzip
command line tool does. You can disable that with
gzip --no-name
.
A
comment
. This optional field is seldom used, and many decompressors ignore it. But you could add a little comment if you want.
Extra arbitrary data
. If the other metadata wasn’t enough, you can stuff whatever you want into arbitrary subfields. Each subfield has a two-byte identifier and then 0 or more bytes of additional info.
That’s way more info than I expected!
I was intrigued by this metadata and I’ve been wanting to learn
Zig
, so I wrote
gzpeek
.
gzpeek is a command-line tool that lets you inspect the metadata of gzip streams. Here’s how to read metadata from a gzipped file:
gzpeek my_file.gz
# FTEXT: 0
# MTIME: 1591676406
# XFL: 2
# OS: 3 (Unix)
# NAME: my_file.txt
It extracts everything I listed above: the operating system, original file name, modification time, and more. I used it a bunch when surveying different gzip implementations.
Give it a try, and
let me know
what gzip metadata you find.
