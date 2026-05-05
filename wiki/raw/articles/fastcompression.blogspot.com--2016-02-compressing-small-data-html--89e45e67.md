---
title: "RealTime Data Compression"
url: "http://fastcompression.blogspot.com/2016/02/compressing-small-data.html"
fetched_at: 2026-05-05T07:00:59.475910+00:00
source: "Yann Collet (LZ4/Zstd)"
tags: [blog, raw]
---

# RealTime Data Compression

Source: http://fastcompression.blogspot.com/2016/02/compressing-small-data.html

Data compression is primarily seen as a file compression algorithm. After all, the main objective is to save storage space, is it ?
With this background in mind, it's also logical to focus on bigger files. Good compression achieved on a single large archive is worth the savings for countless smaller ones.
However, this is no longer where the bulk of compression happen. Today, compression is everywhere, embedded
within
systems, achieving its space and transmission savings without user intervention, nor awareness. The key to these invisible gains is to remain below the end-user perception threshold. To achieve this objective, it's not possible to wait for some large amount of data to process. Instead, data is processed in small amounts.
This would be all good and well if it wasn't for a simple observation : the smaller the amount to compress, the worse the compression ratio.
The reason is pretty simple : data compression works by finding redundancy within the processed source. When a new source starts, there is not yet any redundancy to build upon. And it takes time for any algorithm to achieve meaningful outcome.
Therefore, as the issue comes from starting from a blank history, what about starting from an already populated history ?
Streaming to the rescue
A first solution is streaming : data is cut into smaller blocks, but each block can make reference to previously sent ones. And it works quite well. In spite of some minor losses at block borders, most of the compression opportunities of a single large data source are preserved, but now with the advantage to process, send, and receive tiny blocks on the fly, making the experience smooth.
However, this scenario only works with serial data, a communication channel for example, where order is known and preserved.
For a large category of applications, such as database and storage, this cannot work : data must remain accessible in a random fashion, no known "a priori" order. Reaching a specific block sector should not require to decode all preceding ones just to rebuild the dynamic context.
For such use case, a common work-around is to create some "not too small blocks". Say there are many records of a few hundred bytes each. Group them in packs of at least 16 KB. Now this achieves some nice middle-ground between not-to-poor compression ratio and good enough random access capability.
This is still not ideal though, since it's required to decompress a full block just to get a single random record out of it. Therefore, each application will settle for its own middle ground, using block sizes of 4 KB, 16 KB or even 128 KB, depending on usage pattern.
Dictionary compression
Preserving random access at record level
and
good compression ratio, is hard. But it's achievable too, using a
dictionary
. To summarize, it's a kind of common prefix, shared by all compressed objects. It makes every compression and decompression operation start from the same populated history.
Dictionary compression has the great property to be compatible with random access. Even for communication scenarios, it can prove easier to manage at scale than "per-connection streaming", since instead of storing one different context per connection, there is always the same context to start from when compressing or decompressing any new data block.
A good dictionary can compress small records into tiny compressed blobs. Sometimes, the current record can be found "as is" entirely within the dictionary, reducing it to a single reference. More likely, some critical redundant elements will be detected (header, footer, keywords) leaving only variable ones to be described (ID fields, date, etc.).
For this situation to work properly, the dictionary needs to be tuned for the underlying structure of objects to compress. There is no such thing as a "universal dictionary". One must be created and used for a target data type.
Fortunately, this condition can be met quite often.
Just created some new protocol for a transaction engine or an online game ? It's likely based on a few common important messages and keywords (even binary ones). Have some event or log records ? There is likely a grammar for them (json, xml maybe). The same can be said of digital resources, be it html files, css stylesheets, javascript programs, etc.
If you know what you are going to compress, you can create a dictionary for it.
The key is, since it's not possible to create a meaningful "universal dictionary", one must create one dictionary per resource type.
Example of a structured JSON message
How to create a dictionary from a training set ? Well, even though one could be tempted to manually create one, by compacting all keywords and repeatable sequences into a file, this can be a tedious task. Moreover, there is always a chance that the dictionary will have to be updated regularly due to moving conditions.
This is why,
starting from v0.5
, zstd offers a
dictionary builder capability
.
Using the builder, it's possible to quickly create a dictionary from a list of samples. The process is relatively fast (a matter of seconds), which makes it possible to generate and update multiple dictionaries for multiple targets.
But what good can achieve dictionary compression ?
To answer this question, a few tests were run on some typical samples. A flow of JSON records from a probe, some Mercurial log events, and a collection of large JSON documents, provided by @KryzFr.
Collection Name
direct
compression
Dictionary
compression
Gains
Average
unit
Range
Small JSON records
x1.331 - x1.366
x5.860 - x6.830
~ x4.7
300
200 - 400
Mercurial events
x2.322 - x2.538
x3.377 - x4.462
~ x1.5
1.5 KB
20 - 200 KB
Large JSON docs
x3.813 - x4.043
x8.935 - x13.366
~ x2.8
6 KB
800 - 20 KB
These compression gains are achieved without any speed loss, and even feature faster decompression processing. As one can see, it's no "small improvement". This method can achieve transformative gains, especially for very small records.
Large documents will benefit proportionally less, since dictionary gains are mostly effective in the first few KB. Then there is enough history to build upon, and the compression algorithm can rely on it to compress the rest of the file.
Dictionary compression will work if there is some correlation in a family of small data (common keywords and structure). Hence, deploying one dictionary per type of data will provide the greater benefits.
Anyway, if you are in a situation where compressing small data can be useful for your use case (databases and contextless communication scenarios come to mind, but there are likely other ones), you are welcomed to
have a look at this new open source tool and compression methodology
and report your experience or feature requests.
Zstd is now getting closer to v1.0 release, it's a good time to provide feedback and integrate them into final specification.
