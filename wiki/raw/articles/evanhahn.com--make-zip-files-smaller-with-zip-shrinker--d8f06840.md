---
title: "Make ZIP files smaller with ZIP Shrinker"
url: "https://evanhahn.com/make-zip-files-smaller-with-zip-shrinker/"
fetched_at: 2026-05-17T07:01:24.927122+00:00
source: "evanhahn.com"
tags: [blog, raw]
---

# Make ZIP files smaller with ZIP Shrinker

Source: https://evanhahn.com/make-zip-files-smaller-with-zip-shrinker/

Make ZIP files smaller with ZIP Shrinker
I built ZIP Shrinker, a little browser tool to shrink ZIP files. It also works with formats that are secretly ZIPs underneath, like APK, EPUB, JAR, and many more.
Try it out!
How does it work?
At a high level, this tool (1) re-compresses every file in the ZIP archive with higher compression (2) removes all metadata (3) removes entries for directories.
Re-compressing
ZIP files are typically compressed with an algorithm called
Deflate
.
There are a few tools that can re-compress Deflate data and make it smaller, usually by spending more time on the computation. I took one of these tools,
libdeflate
, and applied it to each compressed entry in the ZIP. I chose libdeflate because of its performance; alternatives like
Zopfli
can achieve marginally smaller results but take
much
longer.
I created
libdeflate.js
, a WebAssembly wrapper for libdeflate, as part of this work. (I always relish my time working with WASM!)
Each entry in a ZIP file can contain additional metadata like comments. These aren’t typically used, and if they’re there, my shrinker removes them. This usually doesn’t save too many bytes, but it doesn’t hurt.
Removing directories is a slightly spicier decision. Usually, the existence of a file entry implies the existence of the directory it’s inside. For example,
foo/bar.txt
implies the existence of the
foo
directory. Some ZIPs include separate entries for directories, but because most extractors don’t need them, I remove those. This has the side effect of removing empty directories—
let me know
if that’s a problem for you.
If you want to see how the whole project works,
check out the full source code
.
How good is it?
I tested several ZIPs to see what this tool could do. Some anecdotal results:
File
Savings
Linux v6.19 source
15.8 MiB (5.62%)
Romeo & Juliet EPUB from Project Gutenberg
51.2 KiB (18.16%)
Signal for Android v8.3.4 (APK)
25.6 MiB (30.06%)
Not particularly scientific, but useful to see.
Why did I do this?
This proof-of-concept shows that you can make ZIP files smaller without sacrificing backwards compatibility. It could be useful for sending an archive to someone, but could also be useful to reduce bandwidth and server costs. For example, if Project Gutenberg re-compressed all their EPUB books with this method, they might be able to save some money.
Of course, ZIP isn’t always the most efficient format. Typically, other archives like
.tar.bz2
can be smaller. But those aren’t backwards-compatible!
ZIP also supports compression methods other than Deflate. They’re atypical, but you could use them to achieve a smaller result, too.
Give my tool a try
if you want a smaller ZIP.
