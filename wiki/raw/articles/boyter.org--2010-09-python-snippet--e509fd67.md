---
title: "Ben E. C. Boyter"
url: "https://boyter.org/2010/09/python-snippet/"
fetched_at: 2026-05-05T07:02:07.391723+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Ben E. C. Boyter

Source: https://boyter.org/2010/09/python-snippet/

Python Snippet
2010/09/29
(103 words)
The below is a quick Python snippet which I use on a day to day basis for weeks, then promptly forget. Essentially its reading from standard input and then doing something with it. Very useful when you are trying to process data on the command line and have forgotten how to use awk/sed properly and grep has run out of steam.
import
sys
import
re
for
line
in
sys
.
stdin:
values
=
line
.
split(
','
)
print
"
%s
\t
%s
"
%
(values[
0
],values[
1
])
The above just takes standard input, splits it on commas and prints out out with a tab space between them. A useless example, but shows the concept quite well.
