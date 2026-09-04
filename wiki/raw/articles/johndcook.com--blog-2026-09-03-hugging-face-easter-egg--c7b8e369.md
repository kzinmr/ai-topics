---
title: "Hugging Face Easter Egg"
url: "https://www.johndcook.com/blog/2026/09/03/hugging-face-easter-egg/"
fetched_at: 2026-09-04T10:00:43.652398+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Hugging Face Easter Egg

Source: https://www.johndcook.com/blog/2026/09/03/hugging-face-easter-egg/

NVIDIA has offered by buy Hugging Face for $12,930,300,000.
129303 is the Unicode code point for the Hugging Face emoj (U+1F917), which you can verify with the following Python code.
>>> import unicodedata
>>> 129303 == 0x1F917
True
>>> unicodedata.name(chr(0x1F917))
'HUGGING FACE'
Related posts
