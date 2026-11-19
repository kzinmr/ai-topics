---
title: "Supersequences and Superpermutations"
url: "https://www.johndcook.com/blog/2026/11/18/supersequences/"
fetched_at: 2026-11-19T10:01:32.869950+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Supersequences and Superpermutations

Source: https://www.johndcook.com/blog/2026/11/18/supersequences/

A word is
universal
if it contains every permutation of its alphabet as a subsequence: the letters must appear in order, but gaps are allowed.
For example, you can find all six permutations of the digits 1, 2, and 3 inside the string 1231213. Not all permutations can be found as a contiguous substring—that would be a superpermutation—but all can be found as a subsequence.
The word
01234567890123456780293451670823451960782134506978231405678213904567823109456782301
is universal for the set of 10 digits. This word was discovered some time ago, but Jason Davies has recently proved that this the smallest universal word on 10 digits. It has 83 characters, and Davies proved that no word of 82 characters is universal over the digits. See his paper
here
.
I’m surprised that all 10! = 3,628,800 permutations of 10 digits can be found as subsequences of such a relatively short word.
Universal words, or
supersequences
, are easily confused with
superpermutations
. See OEIS sequences
A062714
and
A180632
. Minimal length superpermuations are necessarily longer than minimal length supersequences [1] since the requirements on the former are stricter, requiring permutations to appear as contiguous substrings and not merely as subsequences. In other words, every superpermutation is a supersequence, but not vice versa.
For example,
123412314231243121342132413214321
is a minimal superpermutation on four symbols while
123412314213
is a minimal supersequence.
Note that it’s trivial to produce a supersequence: just concatenate all
n
! permutations of the symbols into one sequence. But finding
minimal
supersequences and
minimal
superpermutations is challenging.
[1] For
n
= 1 or 2 the minimal supersequence and minimal superpermutation are the same. For
n
> 2 they are not.
