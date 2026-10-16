---
title: "C++ futures part 3: The mental model for std::async"
url: "https://devblogs.microsoft.com/oldnewthing/20261014-00/?p=112774/"
fetched_at: 2026-10-16T10:00:36.834590+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# C++ futures part 3: The mental model for std::async

Source: https://devblogs.microsoft.com/oldnewthing/20261014-00/?p=112774/

We continue our study of C++ futures
with
std::
async
.
The more complex case is the
std::
async
. You give
std::
async
a callable and optional parameters to pass to that callable, and you also specify how and when you want the callable to be invoked. You get two axes: Do you want it to be calculated immediately or on demand? Do you want the calculation to happen on the thread that requests the value or on its own thread?
Now, you’d think you could fill out the table like this:
Immediate
On demand (“deferred”)
Same thread
Call now and save the value
Call when waited
New thread (“async”)
Start the thread now
Start the thread when waited
However, that’s not what the C++ standard says.
The C++ standard disallows asking for an immediate value on the same thread. There’s really no value to doing it that way, since there is no actual “future”; it all happens in the present! “This future could have been a function call.”
auto f = std::async({}, calculator);

auto result = f.get();
This would, in theory, mean “Immediately call the calculator and wait for it to produce a value. Store it in the
source
and return a future that fetches the value from that source.” But that’s the same as just
auto result = calculator();
I’m guessing that the C++ standard disallows it because there’s no point.
The C++ standard also says that if you combine both
std::
launch::
deferred
and
std::
launch::
async
, it doesn’t mean that you get a calculation that lazy-starts on its own thread. Instead, the standard says that the implementation can choose which flag to honor and which to ignore.
So really, the table is
Immediate
On demand (“deferred”)
Same thread
Illegal
Call when waited
New thread (“async”)
Start the thread now
Dealer’s choice
In all cases, the result of the callable (either a value or an exception) is stored in the
source
.
Now, I noted that there’s no point to asking
std::
async
for an immediate on-thread calculation. But maybe you want to do it anyway because you are interfacing with some other component that expects to receive a
future
. How could you get the same result?
We’ll look at that next time.
