---
title: "Mutation Tester for All Languages"
url: "https://boyter.org/2012/01/mutation-tester-for-all-languages/"
fetched_at: 2026-05-05T07:02:05.848803+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Mutation Tester for All Languages

Source: https://boyter.org/2012/01/mutation-tester-for-all-languages/

Mutation Tester for All Languages
2012/01/06
(219 words)
As a fan of unit tests for bug checking and development (where applicable) I always have a doubt that even though my tests pass they might not be written correctly. This is especially true where you write the tests after development rather then following TDD.
Regardless you can still stress your code by doing some mutation testing. It’s essentially a way of testing your tests. Quite a few mutation testing frameworks are out there such as Heckle, Insure++, Nester etc.. but I was looking for one for my Python and PHP code that goes into making searchco.de
Unable to find one that met my requirements (or worked at all) I wrote the below github version in 10 mins or so. Rather then fiddling with opcode (like the previously mentioned versions) it applies the changes to the source files themselves. Because of this you should sure what you have has a backup somewhere before running it. I have tested it against a few languages (PHP, C#, JavaScript) and the results show my tests failing as expected so I am pretty happy with the outcome.
Usage is pretty simple,
python mutator.py DIRECTORY EXTENSION
Where directory is the directory you want to recursively target and extension is the file extension you want to target. You can get the code
here at github
.
