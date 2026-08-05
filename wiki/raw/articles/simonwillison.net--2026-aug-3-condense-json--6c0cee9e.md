---
title: "condense-json 1.1"
url: "https://simonwillison.net/2026/Aug/3/condense-json/#atom-everything"
fetched_at: 2026-08-05T10:12:32.245433+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# condense-json 1.1

Source: https://simonwillison.net/2026/Aug/3/condense-json/#atom-everything

After shipping
condense-json 1.0
I started integrating it into LLM, and found there were some desirable new features already:
Replacements object can now include values other than strings. These will be identified and used as structural replacements by
condense_json()
and
uncondense_json()
.
#8
Objects can be used as the basis for merge operations.
condense_json()
will identify if there are objects that are a close match and will store instructions for keys to update or delete.
uncondense_json()
can then apply these merges.
I also added
some round-trip tests
using the
Hypothesis
property-based Python testing library.
