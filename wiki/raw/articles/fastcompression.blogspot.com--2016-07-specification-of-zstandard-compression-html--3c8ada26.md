---
title: "Specification of Zstandard compression format"
url: "http://fastcompression.blogspot.com/2016/07/specification-of-zstandard-compression.html"
fetched_at: 2026-05-05T07:00:59.567524+00:00
source: "Yann Collet (LZ4/Zstd)"
tags: [blog, raw]
---

# Specification of Zstandard compression format

Source: http://fastcompression.blogspot.com/2016/07/specification-of-zstandard-compression.html

If you ever wanted to know how the algorithm works, and / or wanted to create your own version in any language of your choice, this is the place to start.
It is a first version though, with usual caveats : expect it to be perfectible and require a few rounds, feedbacks and modifications, before reaching a stage of being unambiguous and clear.
This is an opened public consultation phase, every feedback is welcomed.
It's also the very last chance to review the different choices that made it into the format, introducing questions and possibly
suggesting
improvements or simplifications.
I don't expect "big changes", but maybe a collection of very minor things, which could, collectively, be worth considering a last polishing touch before pushing to v1.0.
Edit
: Indeed, there will be a polishing stage...
Writing the specification made it possible to grab a complete view of the multiple choices which made it into the format. Retrospectively, some of these choices are similar yet slightly different. For example, encoding types exist for all symbols, but are not numbered in the same way. Most fields are little-endian, but some are big-endian, some corner cases optimizations are so rare they are not worth their complexity, etc.
Therefore, in an effort to properly unify every minor detail of the specification and bring a few simplifications, a last modification round will be performed. It will be released as 0.8. No major change to expect, only a collection of minor ones. But a change is a change, so it's nonetheless a new format.
As usual, 0.8 will be released with a "legacy mode", allowing reading data already compressed with 0.7.x series and before.
Unlike usual though, we plan to release a "v0.7 transition" version, able to read data created with v0.8, in order to smooth transition in live systems which depend on listeners / producers, and need to ensure all listeners are able to read data sent to them before upgrading to 0.8.
Edit 2 :
v0.8.0
and "
transition v0.7.5
" have been released
