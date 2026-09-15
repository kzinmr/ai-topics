---
title: "Guessing the meaning of a number"
url: "https://www.johndcook.com/blog/2026/09/14/guessing-the-meaning-of-a-number/"
fetched_at: 2026-09-15T10:01:19.457786+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Guessing the meaning of a number

Source: https://www.johndcook.com/blog/2026/09/14/guessing-the-meaning-of-a-number/

Suppose I give you an
n
-digit number and ask you what it represents. This seems impossible, and in theory it
is
impossible. But in practice it’s often possible.
Apps on a phone may automatically interpret a 10-digit number as a phone number or a 16-digit number as a package tracking number. And very often these interpretations are correct, given the kinds of things most people use their phones for.
It’s not surprising that a 10-digit number
on a phone
is a
phone number
. It’s more interesting that a 16-digit number is likely a tracking number. It could be other things, such as a credit card number. But people don’t usually write out credit card numbers in a text note; credit card numbers likely saved in some more opaque way.
I run into a variation of this problem routinely, trying to infer what a number represents inside medical notes.
A five-digit number could be a US postal code, or it could be a
medical procedure code
.
A six-digit number could be a date in MMDDYY format, or it could be a medical record number.
A ten-digit number could be a phone number, or it could be an
NPI
(National Provider Identifier) number.
It’s interesting that it’s possible make a good guess at what a number means inside unstructured text. Context has been lost, but not all context: you know you’re looking at medical notes. And that meager bit of context can be surprisingly useful.
