---
title: "Test Driven Development"
url: "https://boyter.org/2010/08/test-driven-development/"
fetched_at: 2026-05-05T07:02:08.151998+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Test Driven Development

Source: https://boyter.org/2010/08/test-driven-development/

Test Driven Development
2010/08/06
(335 words)
I was reading a blog post today linked from Dzone which alluded to
test driven development being a waste of time
I am one of those people who has caught the test driven development (TDD) bug and I am a big fan of TDD and unit testing in general. In fact I am the one who posted the first comment on the linked blog and prompted the authors change to it.
I thought I would quickly jot down the one single biggest thing I have found while following TDD methods of development.
TDD is not about fixing bugs in code. Repeat that after me. TDD is not about fixing bugs in code. You will still create bugs when you are writing your methods. What TDD does is ensure that your code works as your tests are dictated.
Now you are probably asking what is the benefit of this? Well firstly you have examples in code of how your code should be used. You can refer to the tests and know with certainty how the code works with any given input. Secondly it allows you to change the internals of your code without fear of breaking existing functionality. If a section of code is identified a little slow, you can tweak it to your hearts content without fear. Finally and what I feel is the greatest benefit of TDD is that it enforces good design. In order to have testable code methods and classes need to work in isolation and perform a single task which is the point of proper object orientated (OO) design.
So thats my personal five minute take on TDD and what the point of it is. I recently re-factored a web-crawler to use proper separation of concerns and logic by applying TDD development methods. The result? A crawler with 100% unit test coverage, a nice OO design and the ability to change things without fear of breaking existing functionality. All good things when you are trying to be as agile as possible.
