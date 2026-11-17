---
title: "Release: llm 0.37.3"
url: "https://simonwillison.net/2026/Nov/16/llm/"
fetched_at: 2026-11-17T10:00:44.292879+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Release: llm 0.37.3

Source: https://simonwillison.net/2026/Nov/16/llm/

A bug fix release for
LLM
, mainly to cover a problem with the most recent Homebrew package of the software.
Homebrew now ships the latest SQLite,
3.54.1
, which includes
a fix
that
broke LLM's logging code
.
Short version: in SQLite 3.54.0 the following SQL:
select json_object('a', (select json_array(1)))
Returns this:
{"a":[1]}
But in 3.54.1 the same query returns this:
{"a":"[1]"}
According
to D. Richard Hipp
:
That was a bug fix. Per the documentation, (SELECT json_array(...)) returns SQL text, not JSON. Hence the 3.54.1 behavior is correct and 3.54.0 was a bug.
The workaround looks like this:
select json_object('a', json((select json_array(1))))
