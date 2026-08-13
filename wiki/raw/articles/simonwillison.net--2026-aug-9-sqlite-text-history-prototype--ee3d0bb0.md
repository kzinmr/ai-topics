---
title: "SQLite compressed text-history prototypes"
url: "https://simonwillison.net/2026/Aug/9/sqlite-text-history-prototype/"
fetched_at: 2026-08-13T10:19:21.497602+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# SQLite compressed text-history prototypes

Source: https://simonwillison.net/2026/Aug/9/sqlite-text-history-prototype/

I'm perennially interested in options for storing revision histories in relational databases. While out on a dog walk I had a new idea: how about taking the full text of every prior version in a big JSON array of strings and then applying zlib or zstd compression to the whole thing? Surely that would compress really well due to all of the repeated strings.
The new
GPT‑Live voice mode
in the ChatGPT iPhone app has got really good, so I discussed the prototype with that. You still can't share URLs to voice conversations, but here's what I said copied from the transcript as a proper stream of consciousness:
I have an interesting idea for a scheme for saving all previous versions of a piece of text that's constantly edited in a  SQLite database um column in as efficient a way as possible. Okay, so I built these kinds of systems in the past, and it's always difficult to come up with a efficient way to do this. Like the easiest way is you have a row for every previous copy of the previous previous value of the string. But if it's a long document Like20 kilobytes of data, that means that every single edit adds another 20 kilobytes of data to the database, right. So, what I've now thinking, is um compression would work really well, right? If you Bundle all of those different um Every every version of this document all the way back to the start if you were to apply a good compression algorithm to them that should basically wipe out huge amounts of the redund- the um redundant text, right Um, so what I'd thinking is how about really, really simple mechanism There is a history column on the single on this uh uh table and it's a blob, it's a BLOB so it stores binary data and then you just stick in there a Zlib or maybe even  ZSTD um compressed JSON text array of all of the previous documents, and so you probably have two columns, right? You'd have a column that's this magic JSON array of text You have a second column which is a JSON array of timestamps and that doesn't need to be compressed at all, right? A timestamp can just be a uh- it's an array of integers, right? Unix integers But that's the whole scheme.
Then I stopped voice mode and typed the following text prompt to GPT-5.6 Sol Pro:
Use Python and Build experimental prototypes around this idea
It churned away for 38 minutes and delivered
this answer
plus the files you see in
this folder
.
The approach works really well! 1,000 simulated revisions to a document resulted in 20.4 MB of raw revision text that compressed to 80.3 KB as Zstandard-compressed JSON array.
To avoid the overhead of decompressing and recompressing the entire array on every edit Sol suggested breaking the history up into multiple rows, with each one containing a maximum of either 128 revisions or 3MB of uncompressed JSON.
