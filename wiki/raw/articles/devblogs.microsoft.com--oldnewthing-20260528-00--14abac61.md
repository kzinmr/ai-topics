---
title: "Sharing the result of a single Windows Runtime IAsyncOperation among multiple coroutines, part 2"
url: "https://devblogs.microsoft.com/oldnewthing/20260528-00/?p=112365"
fetched_at: 2026-05-29T07:01:24.644194+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# Sharing the result of a single Windows Runtime IAsyncOperation among multiple coroutines, part 2

Source: https://devblogs.microsoft.com/oldnewthing/20260528-00/?p=112365

Last time,
we tried to write a coroutine function that cached the result of another coroutine
, but our first attempt had lots of problems.
It turns out that you can do it much more simply, and simpler code means fewer places you can mess up.
struct Widget : WidgetT<Widget>
{
    std::optional<winrt::Thing> m_thing;
    wil::unique_event m_busy{ wil::EventOptions::Signaled }; // auto-reset, initially signaled

    IAsyncOperation<winrt::Thing> GetThingAsync()
    {
        auto lifetime = get_strong();

        co_await winrt::resume_on_signal(m_busy.get());
        auto not_busy = m_busy.SetEvent_scope_exit();

        // If we don't have a thing, try to get one.
        if (!m_thing) {
            m_thing = co_await GetThingWorkerAsync();
        }

        co_return *m_thing;
    }
};
We use an auto-reset event to serialize access to the function, remembering to set the event when control leaves the function so that the next caller can try.
Each time we try, we see if we have an answer already. If not, then we try to get the answer. If it fails, then we propagate the exception and
m_thing
remains empty. Otherwise, we save the answer into
m_thing
. Regardless of whether we have a cached answer or a fresh answer, we return it. (We can use the
*
operator because we know that the
m_thing
contains a value: If it didn’t, we would have attempted to get the value, and if the attempt failed, we would have thrown.)
The above code is careful to accommodate the case that
Get­Thing­Worker­Async
succeeds and produces
nullptr
, using the
std::
optional
‘s empty state as a “no value yet” sentinel. If you know that
Get­Thing­Worker­Async
cannot succeed with
nullptr
, then you can get rid of the
std::
optional
and let
nullptr
represent the empty state.
struct Widget : WidgetT<Widget>
{
winrt::Thing m_thing{ nullptr };
wil::unique_event m_busy{ wil::EventOptions::Signaled }; // auto-reset, initially signaled

    IAsyncOperation<winrt::Thing> GetThingAsync()
    {
        auto lifetime = get_strong();

        co_await winrt::resume_on_signal(m_busy.get());
        auto not_busy = m_busy.SetEvent_scope_exit();

        // If we don't have a thing, try to get one.
        if (!m_thing) {
            m_thing = co_await GetThingWorkerAsync();
assert(m_thing);
}

        co_return
m_thing
;
    }
};
Next time, we’ll come up with a version that tries only once rather than trying until it succeeds.
