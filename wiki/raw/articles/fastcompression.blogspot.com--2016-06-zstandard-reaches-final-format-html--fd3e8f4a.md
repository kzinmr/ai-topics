---
title: "Zstandard reaches Candidate Compression Format"
url: "http://fastcompression.blogspot.com/2016/06/zstandard-reaches-final-format.html"
fetched_at: 2026-05-05T07:00:59.652829+00:00
source: "Yann Collet (LZ4/Zstd)"
tags: [blog, raw]
---

# Zstandard reaches Candidate Compression Format

Source: http://fastcompression.blogspot.com/2016/06/zstandard-reaches-final-format.html

Finally. That was a pretty long journey.
With the release of v0.7,
Zstandard
has reached an important milestone where the compression format is stable and complete enough to pretend becoming v1.0.
We don't call it v1.0 yet, because it's safer to spend some time on a "confirmation period" during which the final compression format is field-tested. It shall confirm its ability to match its objectives, dealing with all situations it is planned for.
Then
it will be rebranded v1.0.
With the
source code
out, it's also time to think about other supportive actions, such as documentation. The next priority task is to redact a specification of the compression format, so that it can be better exposed, understood and implemented by third parties. The goal is that any third party should be able to create its own version. However, describing algorithm in a way which is clear and concise is not trivial. It's expected that some paragraphs will need re-write in an effort to become clearer and more complete, reducing sources of confusion. So this effort will benefit from user exposure and feedback
It's also time to have some more involved discussions around the API.
The current "stable API" is expected to remain, but its scope is also limited, providing mostly the "basics", such as compressing a buffer into another buffer. More complex usages are possible (streaming in memory-constrained environment using a custom allocator for example), but need to access advanced prototypes, exposed in the "experimental" section.
Now will be a good time to seriously consider extending the scope of "stable API".
Just "promoting" a prototype from "experimental" to "stable" is not necessarily the better way to go. It's important that the extended API remain simple enough to understand and use (which is not the main priority of "experimental" section).
After being immersed in the code for so long, some technical complexities can become invisible, while becoming real obstacles to newcomers. Therefore, it's important to "think" extended API properly, to create interfaces easy to use.
For this objective, the key is to listen 3rd parties, in order to better fit natural expectations.
