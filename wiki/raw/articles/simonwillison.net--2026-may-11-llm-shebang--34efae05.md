---
title: "Using LLM in the shebang line of a script"
url: "https://simonwillison.net/2026/May/11/llm-shebang/#atom-everything"
fetched_at: 2026-05-12T07:00:48.362181+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Using LLM in the shebang line of a script

Source: https://simonwillison.net/2026/May/11/llm-shebang/#atom-everything

Kim_Bruning
on Hacker News
:
But seriously, you can put a shebang on an english text file now (if you're sufficiently brave) [...]
This inspired me to look at patterns for doing exactly that with
LLM
. Here's the simplest, which takes advantage of
LLM fragments
:
#!/usr/bin/env -S llm -f
Generate an SVG of a pelican riding a bicycle
But you can also incorporate
tool calls
using the
-T name_of_tool
option:
#!/usr/bin/env -S llm -T llm_time -f
Write a haiku that mentions the exact current time
Or even execute YAML templates directly that define extra tools as Python functions:
#
!/usr/bin/env -S llm -t
model
:
gpt-5.4-mini
system
:
|
Use tools to run calculations
functions
:
|
def add(a: int, b: int) -> int:
return a + b
def multiply(a: int, b: int) -> int:
return a * b
Then:
./calc.sh 'what is 2344 * 5252 + 134' --td
Which outputs (thanks to that
--td
tools debug option):
Tool call: multiply({'a': 2344, 'b': 5252})
  12310688

Tool call: add({'a': 12310688, 'b': 134})
  12310822

2344 × 5252 + 134 = **12,310,822**
Read the full TIL for
a more complex example
that uses the Datasette SQL API to answer questions about content on my blog.
