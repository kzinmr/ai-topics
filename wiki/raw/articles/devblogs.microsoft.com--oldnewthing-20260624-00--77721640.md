---
title: "Cancellation of Windows Runtime activities is asynchronous"
url: "https://devblogs.microsoft.com/oldnewthing/20260624-00/?p=112465"
fetched_at: 2026-06-26T07:00:57.206211+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# Cancellation of Windows Runtime activities is asynchronous

Source: https://devblogs.microsoft.com/oldnewthing/20260624-00/?p=112465

In the Windows Runtime, there are four interface patterns for representing asynchronous activity.
No return type
With return type
T
Without progress
IAsyncAction
IAsyncOperation<T>
With progress
IAsyncActionWithProgress<P>
IAsyncOperationWithProgress<T, P>
For the purpose of this discussion, I will collectively call these “asynchronous activities”.
One of the things you can do with asynchronous activities is cancel them, by calling the
Cancel
method. This method submits a request to cancel, but it does not wait for the operation to acknowledge the cancellation. If you want to wait for the operation to stop executing, you have to wait for it to call the completion callback.²
Asynchronous cancellation is important for avoiding deadlocks.
Most of the time, the scenarios involve cross-thread synchronous calls, but here’s an extremely obvious way it can happen.
Suppose that you have registered a progress callback on your asynchronous activity with progress.
// C#
async Task DoSomethingWithTimeoutAsync()
{
    var op = DoSomethingAsync();
    op.Progress = (sender, p) => {
        UpdateProgress(p);
        if (p >= 0.5) {
            sender.Cancel();
        }
    };
    try {
        await op;
    } catch (TaskCanceledException) {
        // ignore cancellation
    }
}

// C++/WinRT
winrt::fire_and_forget Widget::DoSomethingWithTimeoutAsync()
{
    auto op = DoSomethingAsync();
    op.Progress([&](auto&& sender, auto p) {
        this->UpdateProgress(p);
        if (p >= 0.5) {
            sender.Cancel();
        }
    });

    try {
        co_await op;
    } catch (winrt::hresult_canceled const&) {
        // ignore cancellation
    }
    co_return;
}
The code calls
DoSomethingAsync()
and attaches a progress callback which cancels the operation once the progress reaches 50%. If the
Cancel()
method waited for outstanding progress callbacks to completed, you have a deadlock: The
Cancel()
is waiting for the progress callback to complete. But the progress callback is itself calling
Cancel()
.¹
To avoid deadlocks when cancellation occurs while a progress callback is in progress, the cancellation method doesn’t wait for an acknowledgment. If you want to know when the activity is finished, wait for it to complete. If you want to ignore progress reports that arrive after you cancel, you can do that yourself.
// C#

async Task DoSomethingWithTimeoutAsync()
{
    var op = DoSomethingAsync();
bool canceled = false;
op.Progress = (sender, p) => {
if (!canceled) {
UpdateProgress(p);
            if (p >= 0.5) {
canceled = true;
sender.Cancel();
            }
        }
    };
    try {
        await op;
    } catch (TaskCanceledException) {
        // ignore cancellation
    }
}

// C++/WinRT

winrt::fire_and_forget Widget::DoSomethingWithTimeoutAsync()
{
    auto op = DoSomethingAsync();
bool canceled = false;
op.Progress([&](auto&& sender, auto p) {
if (!canceled) {
this->UpdateProgress(p);
            if (p >= 0.5) {
canceled = true;
sender.Cancel();
            }
        }
    });

    try {
        co_await op;
    } catch (winrt::hresult_canceled const&) {
        // ignore cancellation
    }
    co_return;
}
(The
canceled
variable doesn’t need to be atomic because progress callbacks do not overlap.)
Notice in the C++/winRT version that even after we call
Cancel()
, we wait for the
co_await op
to report completion before we return. Otherwise, the
Progress
callback will access an already-destroyed
canceled
variable.
¹ This is also the cancellation model for
I/O
and
RPC
: The cancellation method submits a cancellation request and returns immediately, and the underlying operation indicates that it has stopped executing by reporting some sort of completion.
² You might try to solve this by saying “Cancellation is asynchronous if the
Cancel
is issued from the same thread as the progress event”, but that doesn’t help in this case, which is more realistic:
// C#
async void CancelAfter(IAsyncInfo op, TimeSpan delay)
{
    co_await Task.Delay(delay);
    op.Cancel();
}

async Task DoSomethingWithTimeoutAsync()
{
    var op = DoSomethingAsync();
    op.Progress = (sender, p) => {
        Invoke(() => UpdateProgress(p));
    };
    CancelAfter(op, TimeSpan.FromSeconds(5));
    try {
        await op;
    } catch (TaskCanceledException) {
        // ignore cancellation
    }
}
Suppose the Progress event is raised on a background thread at 4.9999 seconds. Before the lambda can call
Invoke()
, the
Cancel­After­Delay
timeout elapses, and the UI thread calls
Cancel()
. Now you have a deadlock because the Progress event is waiting for the lambda, the lambda is waiting for the Invoke, the Invoke is waiting for the UI thread, the UI thread is waiting for the Cancel, and the Cancel is waiting for the Progress event.
