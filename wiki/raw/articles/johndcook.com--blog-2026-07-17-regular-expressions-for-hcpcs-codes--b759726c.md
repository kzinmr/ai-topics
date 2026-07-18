---
title: "Regular expressions for HCPCS codes"
url: "https://www.johndcook.com/blog/2026/07/17/regular-expressions-for-hcpcs-codes/"
fetched_at: 2026-07-18T07:00:46.941581+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Regular expressions for HCPCS codes

Source: https://www.johndcook.com/blog/2026/07/17/regular-expressions-for-hcpcs-codes/

Since I revisited my old post on ICD code matching, I thought I’d revisit by
post on HCPCS codes
too.
HCPCS stands for Healthcare Common Procedure Coding System, and is pronounced “hick picks.” When most people say HCPCS, they technically mean HCPCS Level II, and that’s what I mean here.
The format of a HCPCS code is simple: one letter and four digits. In regex terms,
[A-Z]\d{4}
Not all letters are used, so you can get more specific and say
[A-CEGHJ-MP-V][0-9]\d{4}
Some sources say no codes begin with U, but there are currently five codes that begin with U.
When I was doing some research on HCPCS codes recently using AI, I was told there is a D code for dentistry, but that was a hallucination.
HCPCS codes can also have also modifiers. These consist of a letter and either a letter or digit:
[A-Z][A-Z0-9]
Not all letters actually appear in modifiers—I, O, W, and Y are missing—so you could be more specific. At the time of writing there are 384 official modifiers.
Modifiers are often stored in a separate column in a database, but in text you’ll see a HCPCS code optionally followed by a dash and a modifier. So a regex to match HCPCS codes with possible modifiers would be
[A-CEGHJ-MP-V][0-9]\d{4}(-[A-Z][A-Z0-9])?
This regex will have some false positives, but it should not have false negatives: every real HCPCS code should match.
Of course you could search against a complete list of HCPCS codes. This would be more accurate and slower. I did a test similar to the one in the
previous post
and found a search with the regex above took 20 milliseconds, while a search against the list of HCPCS codes took 46 seconds.
However, the regex searched for possible modifiers and the exhaustive search only looked for unmodified HCPCS codes. A complete list of HCPCS codes with possible modifiers would be tedious to create because some combinations of codes and modifiers make no sense. And I imagine that some combinations that would make sense are not used in practice.
