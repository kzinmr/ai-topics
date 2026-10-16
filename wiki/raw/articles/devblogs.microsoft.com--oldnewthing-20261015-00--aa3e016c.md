---
title: "C++ futures part 4: What if I want an immediate on-thread std::async?"
url: "https://devblogs.microsoft.com/oldnewthing/20261015-00/?p=112776/"
fetched_at: 2026-10-16T10:00:36.651408+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# C++ futures part 4: What if I want an immediate on-thread std::async?

Source: https://devblogs.microsoft.com/oldnewthing/20261015-00/?p=112776/

I noted last time
that you are not allowed to ask
std::
async
for an immediate on-thread calculation. The C++ library designers probably chose not to support it because there’s no point: An immediate on-thread calculation is just a function call, so call the function already and leave me out of it.
But maybe you want to do it because you are interfacing with a component that wants a
std::
future
. How could you do it?
One way would be to implement the immediately synchronous case manually by setting a value into a promise.
template<typename F, typename... Args>
auto
    make_immediate_future(F&& f, Args&&... args)
-> std::future<
        std::invoke_result_t<std::decay_t<F>,
                             std::decay_t<Args>...>>
{
    std::promise<
        std::invoke_result_t<std::decay_t<F>,
                             std::decay_t<Args>...>> p;
    try {
        p.set_value(std::invoke(auto(f), auto(args)...));
    } catch (...) {
        p.set_exception(std::current_exception());
    }
    return p.get_future();
}
Or you could make
packaged_task
do the work for you:
template<typename F, typename... Args>
auto
    make_immediate_future(F&& f, Args&&... args)
-> std::future<
        std::invoke_result_t<std::decay_t<F>,
                             std::decay_t<Args>...>>
{
    using R = std::invoke_result_t<std::decay_t<F>,
                                   std::decay_t<Args>...>;

    std::packaged_task<R(Args...)> task(f);
    task(args...);
    return task.get_future();
}
Yet another way would be to ask for an on-demand in-thread execution, and then immediately demand it.
template<typename F, typename... Args>
auto
    make_immediate_future(F&& f, Args&&... args)
-> std::future<
        std::invoke_result_t<std::decay_t<F>,
                             std::decay_t<Args>...>>
{
    auto f = std::async(std::launch::deferred,
                        std::forward<F>(f),
                        std::forward<Args>(args)...);
    f.wait();
    return f;
}
