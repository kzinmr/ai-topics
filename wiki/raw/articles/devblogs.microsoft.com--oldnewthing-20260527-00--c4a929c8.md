---
title: "Sharing the result of a single Windows Runtime IAsyncOperation among multiple coroutines, part 1"
url: "https://devblogs.microsoft.com/oldnewthing/20260527-00/?p=112361"
fetched_at: 2026-05-28T07:00:50.716051+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# Sharing the result of a single Windows Runtime IAsyncOperation among multiple coroutines, part 1

Source: https://devblogs.microsoft.com/oldnewthing/20260527-00/?p=112361

Suppose you have a coroutine method called
GetThingAsync()
, and you want to do the work of getting “something” only once and caching the result. Here’s the version that does no caching:
struct Widget : WidgetT<Widget>
{
    IAsyncOperation<Thing> GetThingAsync()
    {
        co_return co_await GetThingWorkerAsync();
    }

    // The business logic goes here
    IAsyncOperation<Result> GetThingWorkerAsync();
};
Now, if this code were written in C#, we could take advantage of the fact that C# projects the Windows Runtime
IAsyncOperation
as a
Task
, and
Task
objects support being awaited on multiple times.
async Task<Thing> GetThingAsync()
{
    lock (m_lock) {
        // First person to call GetThingAsync starts the task.
        if (m_task == null) {
            m_task = GetThingWorker();
        }
    }
    return await m_getThingTask;
}
But we don’t have that in C++/WinRT.
One customer tried to build a solution out of
winrt::
resume_
on_
signal
, perhaps inspired by
one of my earlier explorations of this topic
.
// Don't use this code. See discussion.
struct Widget : WidgetT<Widget>
{
    winrt::Thing m_thing{ nullptr };
    winrt::IAsyncOperation<winrt::Thing> m_task{ nullptr };
    wil::unique_event m_finished{ wil::EventOptions::ManualReset }; /* initially unsignaled */
    bool m_busy{ false };
    std::mutex m_mutex;

    IAsyncOperation<winrt::Thing> GetThingAsync()
    {
        bool shouldStart;
        {
            std::lock_guard guard(m_mutex);
            if (m_thing != nullptr) {
                // Operation has finished.
                co_return m_thing;
            } else if (m_busy) {
                // Operation has started but not yet finished.
                shouldStart = false;
            } else {
                // Operation hasn't even started.
                m_busy = true;
                shouldStart = true;
            }
        }

        auto lifetime = get_strong();

        if (shouldStart) {
            auto task = GetThingWorker();
            m_finished.ResetEvent();
            task.Completed([weak = get_weak(), this](auto&&, auto&&) {
                if (auto strong = weak.get()) {
                    m_busy = false;
                    m_finished.SetEvent();
                }
            });
            m_task = std::move(task);
        }

        co_await winrt::resume_on_signal(m_finished.get());

        {
            std::lock_guard guard(m_mutex);
            if (m_thing == nullptr && m_task) {
                m_thing = m_task.GetResults();
            }
        }

        co_return m_thing;
    }

};
The idea is that the first time
Get­Thing­Async()
is called, we start the real task and then arrange to clear the busy flag and set the
m_finished
event when the task completes. Subsequent callers will see that the task has already started and will not start it again. And subsequent calls which occur after the task has completed will see that we already have a
m_thing
and return it immediately.
Everybody then waits for the
m_finished
event, and then whoever manages to enter the mutex first gets the result and saves it. Finally, everybody returns whatever is in
m_thing
, which should be the result of the task.
From the observation that they set
m_busy
back to false when the task completes, and they reset the
m_finished
event each time they start the task, I conclude that their intention was to allow multiple attempts to get the “something” if a previous attempt fails.
Okay, so let’s see what could go wrong.
For one thing, we see a data race because the completion lambda modifies
m_busy
outside the mutex. So we should at least protect that with a mutex.
Another problem is that this code is not exception-safe. If
Get­Thing­Worker­Async
throws an exception before returning an
IAsync­Operation
, then the
m_busy
flag is set and gets stuck there. This means that nobody else will try to start the task, and the
m_task
remains null, so all subsequent callers just fall through and return a null
Thing
, which may not be something that the callers are expecting. (I mean, this code certainly doesn’t handle the case where
Get­Thing­Worker­Async
produces a null result because it thinks that a null
m_thing
means that we should try again instead of “I successfully got nothing.”)
There’s also a race condition if the task completes just as somebody calls
Get­Thing­Async
:
Thread 1
Thread 2
GetThingAsync
called
m_busy = true
shouldStart = true
GetThingWorkerAsync()
m_finished.ResetEvent()
task.Completed(...)
m_task = std::move(task)
co_await resume_on_signal
(task completes)
m_busy = false
GetThing
called
m_busy = true
shouldStart = true
GetThingWorkerAsync
m_finished.ResetEvent()
task.Completed(...)
m_task = std::move(task)
co_await resume_on_signal
m_finished.SetEvent()
(completion handler returns)
m_thing = m_task.GetResults()
Notice that the second call to
Get­Thing­Async
happens after
m_busy
has been reset, but before we have signaled the event. This creates a window inside which another thread calls
Get­Thing­Async
and tries to start the task again. The second calls assignment to
m_task
overwrites the one from the first call, and then when the first caller tries to get the results, it gets them from the wrong task.
But really, this code is trying too hard. We’ll look at a simpler version next time.
