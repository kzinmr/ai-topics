---
title: "C++ futures part 2: The mental model for std::promise, std::packaged_task"
url: "https://devblogs.microsoft.com/oldnewthing/20261013-00/?p=112769/"
fetched_at: 2026-10-14T10:01:15.471684+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# C++ futures part 2: The mental model for std::promise, std::packaged_task

Source: https://devblogs.microsoft.com/oldnewthing/20261013-00/?p=112769/

Last time
, we looked at the “state” that powers the
std::promise
,
std::packaged_task
,
std::async
,
std::future
, and
std::shared
future
classes. Now we’ll see how that “state” (which I call the
source
) gets used and passed around.
The lifetime of the
source
is managed by a
std::
shared_
ptr<source<T>>
. Everybody who has a reference to the source uses this shared pointer.
The simplest case is
std::promise
. The operations on
std::promise
pretty much map directly to the operations on the
source
we laid out last time.
The next more complicated case is the
std::
packaged_task
. This takes a callable and saves it for later. You can then call
get_future
to get a future and hand it to somebody as an IOU for “A value will appear here someday.”
When you want to produce a value, you invoke the
packaged_task
with whatever parameters you want to pass to the original callable. The result of the invocation (either a value or an exception) is then stored in the
source
object, which can then be retrieved by the future.
You can imagine a packaged task as just wrapping a promise:
template<typename R, typename... Args>
class packaged_task
{
    std::promise<R> p;
    std::function<R(Args...)> func;

public:
    template<typename F>
    packaged_task(F&& f) : func(std::forward<F>(f)) {}

    auto get_future() { return p.get_future(); }

    void operator()(Args... args) {
        try {
            p.set_value(func(args...));
        } catch (...) {
            promise.set_exception(std::current_exception());
        }
    }
};
When you invoke it, it calls the stored callable with the arguments and puts the result in the promise.
Okay, those were the easy cases of pushing values into the
source
. Next time, we’ll look at the messy case:
std::
async
.
