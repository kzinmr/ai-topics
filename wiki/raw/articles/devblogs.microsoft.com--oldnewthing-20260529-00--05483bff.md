---
title: "Sharing the result of a single Windows Runtime IAsyncOperation among multiple coroutines, part 3"
url: "https://devblogs.microsoft.com/oldnewthing/20260529-00/?p=112368"
fetched_at: 2026-05-30T07:01:26.788955+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# Sharing the result of a single Windows Runtime IAsyncOperation among multiple coroutines, part 3

Source: https://devblogs.microsoft.com/oldnewthing/20260529-00/?p=112368

Last time,
we wrote a coroutine function that cached the result of another coroutine
, but it only cached successful calls. It didn’t cache failures, so if the inner coroutine fails, the outer one will simply try again the next time it is called. But what if we want to call the inner coroutine only once and cache the failure, too?
We now have three states: Never tried, tried with success (and cache the success result), and tried with failure (and cache the failure). We can represent that as a variant with three types, using
std::
monostate
to represent the “never tried” state.¹
struct Widget : WidgetT<Widget>
{
    std::variant<std::monostate, winrt::Thing, std::exception_ptr> m_thing;
    wil::unique_event m_busy{ wil::EventOptions::Signaled }; // auto-reset, initially signaled

    IAsyncOperation<winrt::Thing> GetThingAsync()
    {
        auto lifetime = get_strong();

        co_await winrt::resume_on_signal(m_busy.get());
        auto not_busy = m_busy.SetEvent_scope_exit();

        // If haven't tried, then this is our chance.
        if (m_thing.holds_alternative<std::monostate>()) {
            try {
                m_thing = co_await GetThingWorkerAsync();
            } catch (...) {
                m_thing = std::current_exception();
            }
        }

        // Return the cached result or cached failure.
        if (auto thing = std::get_if<winrt::Thing>(&m_thing)) {
            co_return *thing;
        } else {
            std::rethrow_exception(std::get<std::exception_ptr>());
        }
    }
};
After getting past our serialization, we check whether the
m_thing
holds a
std::
monostate
, meaning that we haven’t tried getting the thing yet. If so, then this is the first time through the function, so we will call
Get­Thing­Worker­Async
and save the answer in the
m_thing
. If the call fails, then we save the exception in the
m_thing
.
Regardeless of whether this is the first or subsequent call, we know that by the time we get past the first
if
, the
m_thing
is definitely not a
std::
monostate
. If it has a
winrt::
Thing
, then we return that cached thing. Otherwise, it must be a
std::
exception_
ptr
, so we rethrow that exception.
If we know that
Get­Thing­Worker­Async
never succeeds with
nullptr
, we can simplify the code by having separate variables (one for the non-null successful result and one for the exception pointer on failure), knowing that at most one of them will be non-null. And if both are null, then it means we haven’t attempted the call yet.
struct Widget : WidgetT<Widget>
{
winrt::Thing m_thing{ nullptr };
std::exception_ptr m_ex;
wil::unique_event m_busy{ wil::EventOptions::Signaled }; // auto-reset, initially signaled

    IAsyncOperation<winrt::Thing> GetThingAsync()
    {
        auto lifetime = get_strong();

        co_await winrt::resume_on_signal(m_busy.get());
        auto not_busy = m_busy.SetEvent_scope_exit();

        // If haven't tried, then this is our chance.
        if (
!m_thing && !m_ex
) {
            try {
                m_thing = co_await GetThingWorkerAsync();
assert(m_thing);
} catch (...) {
m_ex
= std::current_exception();
            }
        }
// Return the cached result or cached failure.
if (m_thing) {
co_return m_thing;
} else {
std::rethrow_exception(m_ex);
}
}
};
¹ Bonus reading about
std::
monostate
:
What’s the point of
std::
monostate
? You can’t do anything with it
.
