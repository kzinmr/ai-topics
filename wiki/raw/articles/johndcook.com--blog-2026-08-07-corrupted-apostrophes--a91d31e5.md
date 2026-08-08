---
title: "Corrupted apostrophes"
url: "https://www.johndcook.com/blog/2026/08/07/corrupted-apostrophes/"
fetched_at: 2026-08-08T10:13:47.350110+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Corrupted apostrophes

Source: https://www.johndcook.com/blog/2026/08/07/corrupted-apostrophes/

I have a program that shares files between my laptop and my phone. It works well, except for apostrophes.
When I type an apostrophe
'
on my laptop, it becomes
â€™
on my phone. And when I type
's
on my phone, it becomes
痴
on my laptop.
Apparently the phone turns the apostrophe (U+0027) into a right single quote (U+2019), then bungles bytes in the UTF-8 encoding of U+2019 as three Windows-1252 characters. The bytes E28099
hex
are interpreted as
â
(E2
hex
),
€
(80
hex
), and
™
(99
hex
).
When I type
's
on my phone, it is encoded as two Windows-1252 characters 92
hex
and 73
hex
. Then by the time the text appears on my laptop, the bytes 9273
hex
are interpreted as a Shift-JIS encoding of the CJK character
痴
(U+75F4).
