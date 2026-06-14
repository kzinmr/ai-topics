---
title: "How can I schedule work on a thread pool with low latency?"
url: "https://devblogs.microsoft.com/oldnewthing/20260612-00/?p=112417"
fetched_at: 2026-06-14T07:00:54.442519+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# How can I schedule work on a thread pool with low latency?

Source: https://devblogs.microsoft.com/oldnewthing/20260612-00/?p=112417

A customer had a callback that was used to report data being produced by a hardware device. The rule for the callback is that it has to return quickly so that the code wouldn’t miss the next batch of data because the device itself has a very small buffer: If they spend too much time in the callback, the buffer will overflow and data will be lost.
To avoid clogging the receiving thread, the customer queued a work item to the thread pool to process the data that was just received. However, they found that sometimes, the work item doesn’t run immediately but rather has a 100ms latency. But their program needs to process the data within 20ms. Is there a way to set a deadline on a thread pool work item, so that the system will make sure that it runs before a certain period of time elapses?
As I’ve noted before,
the thread pool is designed for throughput, not latency
. There is no option to set a deadline on a work item.
One reason why the thread pool is being slow to dispatch the work items is that there are other unrelated work items in the thread pool, and those other tasks are competing with your data processing task for the thread pool’s attention. On top of that, some of those other tasks might be long-running, which takes a thread pool thread out of commission for an extended period.
You can take these conflicting work items out of the picture by creating your own custom thread pool: Call
Create­Thread­Pool
and queue your work to that thread pool (by setting that thread pool in the work item’s environment). Now you won’t have any competing work items getting in front of you in the thread pool work queue because those competing work items are going to the process default thread pool and not to your private thread pool.
Note however that even though your work items are no longer fighting with other work items for the attention of your private thread pool, those other work items are still running on the process default thread pool, so they are still competing against your work items for CPU. But at least your work item got dispatched.
I’m guessing that the order in which the batches are processed is important, so you should set your private thread pool’s maximum thread count to 1 so that you don’t start processing one batch of data until you finish processing the previous batch. This effectively serializes the work items, but that’s what you want if you intend to process the batches in order.
In the case where you have a single-minded thread pool, you can prepare everything ahead of time so that all you have to do in the callback itself is call
SubmitThreadpoolWork
on a pre-created reusable work item.
// One-time preparation
pool = CreateThreadpool();
if (!pool) ⟦ error ⟧

TP_CALLBACK_ENVIRON env;
InitializeThreadpoolEnvironment(&env);
SetThreadpoolCallbackPool(&env, pool);
work = CreateThreadpoolWork(ProcessData, nullptr, &env);
if (!work) ⟦ error ⟧

void Callback()
{
    ⟦ add data to data queue ⟧
    SubmitThreadpoolWork(work); // request another callback
}
If you step back and look at this, you might realize that all we did was create a worker thread, but one where we delegated all the bookkeeping to the thread pool. Also, this particular customer was writing code in C#, and the BCL doesn’t have built-in support for custom thread pools.
So if all we have is a worker thread, maybe we can just make a worker thread. Here’s a really simple one.
Queue<Data> queue = new Queue<Data>();

Data WaitForWork()
{
    while (true) {
        lock (queue) {
            if (queue.Count > 0) {
                return queue.Dequeue();
            }
            Monitor.Wait(queue);
        }
    }
}

void WorkerThread()
{
    Data data;
    while ((data = WaitForWork()) != null) {
        ⟦ process the data #&x27e7;
    }
}

void QueueWork(Data data)
{
    lock (queue) {
        queue.Enqueue(data);
        Monitor.Pulse(queue);
    }
}

void EndWork()
{
    QueueWork(null);
}
The worker thread waits for elements to show up in the queue, and once one appears, it dequeues it and does whatever processing you want. If the queued value is
null
, that means that the worker thread is no longer needed, and it exits.
You can do something similar in C++ with a
std::
queue
and a condition variable.
