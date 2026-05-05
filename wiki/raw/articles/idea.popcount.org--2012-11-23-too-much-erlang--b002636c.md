---
title: "Too much Erlang - Idea of the day"
url: "https://idea.popcount.org/2012-11-23-too-much-erlang"
fetched_at: 2026-05-05T07:01:14.077839+00:00
source: "Marek Vavruša (idea.popcount)"
tags: [blog, raw]
---

# Too much Erlang - Idea of the day

Source: https://idea.popcount.org/2012-11-23-too-much-erlang

Too much Erlang
23 November 2012
You know you had enough Erlang once your C code starts looking like
this:
#define TUPLE_U8U8(a,b) \
(u16) (((u8)(a) << 8) | ((u8)(b) & 0xFF))
...
switch
(
TUPLE_U8U8
(
sc
->
registered
,
req
->
type
))
{
case
TUPLE_U8U8
(
0
,
MSG_REGISTER
)
:
...
break
;
case
TUPLE_U8U8
(
1
,
MSG_WAIT
)
:
...
break
;
case
TUPLE_U8U8
(
1
,
MSG_UNREGISTER
)
:
...
break
;
default:
FATAL
();
}
...
