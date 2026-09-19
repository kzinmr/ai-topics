---
title: "std::call_once vs. std::async"
url: "https://devblogs.microsoft.com/oldnewthing/20260917-00/?p=112706"
fetched_at: 2026-09-18T10:00:52.301270+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# std::call_once vs. std::async

Source: https://devblogs.microsoft.com/oldnewthing/20260917-00/?p=112706

Last time, we compared
magic statics with
std::call_once
and concluded that
std::call_once
lets you construct magic statics-like behavior for non-static variables.
But there is also
std::async
for delayed execution. Can we use that instead?
The idea here is that you tell
std::async
that you want it to defer execution of something (say, a lambda). It returns a
std::future
representing that deferred execution.
auto f = std::async(std::launch::deferred, ⟦ lambda ⟧);
At some later point, you can ask for the deferred execution to execute and retrieve the result.
auto value = future.get();
There are a few catches here.
To permit getting non-copyable types, getting the value is a destructive operation: You are allowed to call
get()
only once, and subsequent calls result in undefined behavior. This is a problem for the case where you ask for the value multiple times, but you can fix it by converting the
std::
future
to a
std::
shared_
future
:
auto f = std::async(std::launch::deferred, ⟦ lambda ⟧)
.share()
;
When you call
get()
on a
shared_
future
, it gives you a const reference to the cached value and retains the cached value for future calls. The
shared_
future::
get()
method is marked
const
, which in the C++ standard library means that it is thread-safe with respect to itself and other
const
members. Therefore, you can call
get()
as many times as you like, and the first will run the lambda and return the result, and the others will return the already-calculated result.
Okay, so our
Gadget
class can look like this:
class Gadget
{
public:
    Gadget(std::shared_ptr<Widget> const& widget) : widget(widget) {}

    bool can_reverse_polarity()
    {
        return can_reverse_polarity_future.get();
    }

private:
    std::shared_ptr<Widget> const widget;
    std::shared_future<bool> const can_reverse_polarity_future =
        std::async(std::launch::deferred,
            [=] {
                return is_configuration_enabled("polarity_reversal") &&
                is_widget_polarity_reversible(*widget);
            }).share();
};
So why choose one over the other?
Well,
std::call_
once
is very small. Visual Studio builds it out of the Win32
INIT_ONCE
, which is the size of a pointer.¹
On the other hand
std::
future
and
std::
shared_
future
involve a heap allocation to manage the shared state, as well to store the invocable and its parameters, and the result. Also, since
std::
async
supports other modes of execution, you pull in code to support those other modes that you might even be using. (For example, it has to worry about the possibility that you pass
std::
launch::
async
, so it links in the thread library, as well as other machinery to support
wait_
for
.)
But a significant difference between them has to do with their exception behavior, which we haven’t even talked about yet.
We’ll do that next time.
¹ I can’t find what gcc builds it out of, but an old implementation I found just
builds it manually
with many defects. Just a quick look at it shows that it is not exception-safe and suffers from data races. The code appears to have
moved around
, but it’s still intact. It seems that
the lack of exception safety is called out with a todo-like comment
. The data race is addressed by a comment saying that the processor implicitly makes all loads acquire and all stores release, and while that may be true, it doesn’t prevent the
compiler
from reordering the stores and loads. The compiler might decide to inline the callback and then reorder the stores so that the store to
done
happens before the end of the callback.
