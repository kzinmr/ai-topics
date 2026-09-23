---
title: "Comparing exception behavior of magic statics, std::call_once, and std::async"
url: "https://devblogs.microsoft.com/oldnewthing/20260918-00/?p=112709/"
fetched_at: 2026-09-23T10:01:02.406725+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# Comparing exception behavior of magic statics, std::call_once, and std::async

Source: https://devblogs.microsoft.com/oldnewthing/20260918-00/?p=112709/

We’ve been comparing
magic statics,
std::
call_
once
, and
std::
async
, but one thing we haven’t considered is their behavior in the event of an exception.
For magic statics, if an exception occurs during initialization of the static, then the static is considered not to have been initialized. The exception propagates, and the next time the function is called, the language will try to initialize the static again.
For
call_
once
, if an exception occurs during execution of the lambda, then the call is considered not to have occurred. The exception propagates, so the next time you call
call_
once
with the same
once_
flag
, it will try to call it.
But
std::
async
is different. If an exception occurs during execution of the invocable, then the exception is saved, and when you ask the future or shared future for the result, the exception is rethrown. It does
not
try to execute the invocable again.
Let’s summarize this in a table.
Before
After success
After exception
Magic static
Uninitialized
Initialized
Uninitialized
std::
call_
once
Uninitialized
Initialized
Uninitialized
std::
async
Uninitialized
Initialized
Failed
Or we can do it in a state diagram.
magic static fail
call_once
fail
⮏
async
fail
Uninitialized
→
Failed
↓ success
Initialized
Going back to the choice between
std::
call_
once
and
std::
async
, you have to think about what you want to happen if an exception occurs while trying to initialize the variable. If you want to try again, then use
std::
call_
once
. If you want to remember the failure and keep rethrowing it, then use
std::
async
.
If you are indifferent, then I would suggest
std::
call_
once
, because it is much lighter weight.
