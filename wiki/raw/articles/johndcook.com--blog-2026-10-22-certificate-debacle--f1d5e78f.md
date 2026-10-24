---
title: "How the eMudrha certificate debacle might have happened"
url: "https://www.johndcook.com/blog/2026/10/22/certificate-debacle/"
fetched_at: 2026-10-23T10:01:32.609688+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# How the eMudrha certificate debacle might have happened

Source: https://www.johndcook.com/blog/2026/10/22/certificate-debacle/

You may have seen references to a password being the number 4. There are countless allusions to this online, but they don’t give the context.
As I mentioned in an
earlier post
, eMudrha was using the numbers 4, 56, 115, 155, 156, 230, and 237 as secret keys. I haven’t seen details of how this happened, but in this post I’ll give a plausible account of how it
might
have happened, what someone could have done to produce those results. I’m not trying to do forensic analysis on this specific incident, just exploring what someone might do.
eMudrha was using the NIST elliptic curve P-384, and a secret key should be a random number chosen between 1 and 2
384
. That upper bound isn’t exactly correct, but it’s close. See
this post
if you want to know the exact number.
Someone might have chosen numbers up to 384 rather than 2
384
out of ignorance. Or they might done so by a typo. Maybe they generated a random value that might have been larger than 2
384
and then intended to reduce the number mod 2
384
, but instead of typing
% 2**384
they typed
% 384
It seems more likely, however, that somehow someone took one byte of a random value because all the keys are less than 2
8
= 256.
The probability of choosing seven numbers from 1 to 384 and all being less than or equal to 237 is around 0.034. But the same probability for numbers chosen between 1 and 256 is about 0.60.
