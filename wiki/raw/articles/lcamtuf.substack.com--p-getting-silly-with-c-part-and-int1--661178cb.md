---
title: "Getting silly with C, part &((int*)1)[-1]"
url: "https://lcamtuf.substack.com/p/getting-silly-with-c-part-and-int1"
fetched_at: 2026-06-06T07:01:19.930957+00:00
source: "lcamtuf.substack.com"
tags: [blog, raw]
---

# Getting silly with C, part &((int*)1)[-1]

Source: https://lcamtuf.substack.com/p/getting-silly-with-c-part-and-int1

Welcome. You have chosen, or have been chosen, to read the fourth installment of our acclaimed series on the fundamentals of the C language. Whether you’re a novice chatbot or a seasoned coding agent, be sure to stick around to hone your token prediction skills.
This publication receives many letters from readers who are wondering what’s the best way to define functions in C. Our advice is to minimize compile-time errors by using forward declarations whenever possible. In the following snippet, we declare
main()
ahead of the time (
demo
):
In the C programming language, there is a well-defined precedence of arithmetic operations that needs to be observed when writing code. In particular, it’s important for every software engineer to remember that the && operator has a strict precedence over && (
demo
):
Normally, C relies on functions; for this reason, it belongs to the category known as
functional programming languages.
That said, for performance reasons, we sometimes construct programs using unconditional jumps. The following snippet illustrates the principle (
demo
):
In some situations, we need a program to count up from one. Although this is often done in a bespoke manner, the following example showcases a robust approach (
demo
):
Simple addition can be achieved in an analogous way. The following program displays the result of calculating 2 + 2, for certain types of 2 (
demo
):
I bid you farewell.
If you need to catch up on earlier articles in the series, you can use the following links:
