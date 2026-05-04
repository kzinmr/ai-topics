---
title: "Vertically Aligning Roman Numerals in Code"
url: "https://shkspr.mobi/blog/2026/05/vertically-aligning-roman-numerals-in-code/"
fetched_at: 2026-05-04T07:01:10.039223+00:00
source: "shkspr.mobi"
tags: [blog, raw]
---

# Vertically Aligning Roman Numerals in Code

Source: https://shkspr.mobi/blog/2026/05/vertically-aligning-roman-numerals-in-code/

I have a PHP function which uses Roman Numerals. It looks like this:
⧉
PHP
$romanNumerals
= [
"Ⅿ"
=> 1000,
"ⅭⅯ"
=> 900,
"Ⅾ"
=> 500,
"ⅭⅮ"
=> 400,
"Ⅽ"
=> 100,
"ⅩC"
=>  90,
"Ⅼ"
=>  50,
"ⅩⅬ"
=> 40,
"Ⅹ"
=> 10,
"Ⅸ"
=> 9,
"Ⅷ"
=> 8,
"Ⅶ"
=> 7,
"Ⅵ"
=> 6,
"Ⅴ"
=> 5,
"Ⅳ"
=> 4,
"Ⅲ"
=> 3,
"Ⅱ"
=> 2,
"Ⅰ"
=> 1
];
The problem is, the operators don't line up and the whole thing looks messy. Why? Because the
Unicode Roman Numerals
are
not
monospaced!
ⅭⅯ
is a different width to
ⅩC
and
Ⅷ
is only a single character!  Copy the above to a text editor and see if you can get neat columns. I bet you can't!
I'm obsessed with
vertically aligning my code
. So how to solve this ugly problem?
The
answer was simple
. Assign keys to the values and then flip the array!
⧉
PHP
$romanNumerals
=
array_flip
([
    1000 =>
"Ⅿ"
,
     900 =>
"ⅭⅯ"
,
     500 =>
"Ⅾ"
,
     400 =>
"ⅭⅮ"
,
     100 =>
"Ⅽ"
,
      90 =>
"ⅩC"
,
      50 =>
"Ⅼ"
,
      40 =>
"ⅩⅬ"
,
      10 =>
"Ⅹ"
,
       9 =>
"Ⅸ"
,
       8 =>
"Ⅷ"
,
       7 =>
"Ⅶ"
,
       6 =>
"Ⅵ"
,
       5 =>
"Ⅴ"
,
       4 =>
"Ⅳ"
,
       3 =>
"Ⅲ"
,
       2 =>
"Ⅱ"
,
       1 =>
"Ⅰ"
]);
There! Doesn't that look much neater!
As was written long ago
:
A computer language is not just a way of getting a computer to perform operations but rather … it is a novel formal medium for expressing ideas about methodology. Thus, programs must be written for people to read, and only incidentally for machines to execute.
