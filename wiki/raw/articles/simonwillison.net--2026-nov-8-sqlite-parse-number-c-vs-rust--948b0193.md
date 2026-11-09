---
title: "parse_number() as a SQLite extension: C vs Rust"
url: "https://simonwillison.net/2026/Nov/8/sqlite-parse-number-c-vs-rust/"
fetched_at: 2026-11-09T10:11:02.096477+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# parse_number() as a SQLite extension: C vs Rust

Source: https://simonwillison.net/2026/Nov/8/sqlite-parse-number-c-vs-rust/

I was out walking the dog when I got curious about how easy/difficult it would be to write a SQLite C extension that adds a
parse_number()
function for turning strings like
-$1,234.56
or
'12.5%'
into numeric values that could be summed and sorted.
I fired up regular Claude chat (Opus 5.5)
and prompted
:
I'm thinking about a SQLite custom function 'parse_number(value)' that strips ',', '$', '£' and '%', handles a leading '-', and returns 'NULL' for anything it can’t parse
Explore the difference between building this as a SQLite extension in C v.s. in Rust - I want to compare performance and code complexity and size of the resulting
.so
(or whatever) file
This gave me a solid starting point - the Rust extension was 321 KB (using
Rusqlite
) and 298 KB (using
sqlite-loadable-rs
), while the C extension was 14 KB. But the Rust extension was faster!
Turns out that's because the Rust equivalent of C's
strtod
is "twice as fast". So I prompted:
Try writing your own C function for parsing text into a decimal number that catches up to or beats the Rust implementation
And it did, using "Clinger's fast path":
Net cost per row over 2 million rows, lower is better:
first C
new C
rusqlite
sqlite-loadable
Mixed data
67 ns
19 ns
46 ns
41 ns
Integers only
25 ns
16 ns
36 ns
32 ns
Decimals only
106 ns
18 ns
55 ns
47 ns
Finally, I had it rewrite the prototype as a research report to match the others in
simonw/research
by prompting this:
Clone simonw/research from GitHub and turn your above investigation into a research report as seen in that repository - you can give me a zip file to download that contains your new folder
Here's
the resulting report
.
