---
title: "Taking a password joke seriously"
url: "https://www.johndcook.com/blog/2026/11/24/password-joke/"
fetched_at: 2026-11-25T10:00:48.621459+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Taking a password joke seriously

Source: https://www.johndcook.com/blog/2026/11/24/password-joke/

“I’m sorry but your password must contain 1 char each from: Arabic, Chinese, Thai, Korean, Klingon, Wingdings and an emoji”
This was a message from Finley Creative (@FinleyCreative) to Jeff Atwood (@codinghorror) on March 3, 2016. The original post seems to have gone away.
You could write a script to generate a password according to these rules. How secure would it be?
Multiplying the number of characters from each category gives
153 * 20992 * 57 * 11172 * 38 * 196 * 1409 = 21463556813227081728
possibilities. You could get different numbers depending on how you interpret each of the words in the rules. For example, the calculation above counts Arabic and Thai
letters
, but Klingon counts 26 letters, 10 digits and 3 punctuation marks.
Allowing the characters to appear in any order multiplies the number of possibilities by 7!  = 5040. This corresponds to 76.5 bits of entropy, about the same as 13 alphanumeric characters (upper and lower case).
You could generate a password as above, then using something like
Base 58 encoding
to turn into something you could type on a standard keyboard.
What if you wanted to use the seven Unicode characters as a password without converting them to ASCII characters first? This would be asking for trouble due to possible different encodings of the Unicode characters. Besides, sites that insist that your password contain a “symbol” can be quite restrictive in what symbols they allow.
