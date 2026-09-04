---
title: "The case of the progress callback that never got called when progress happened"
url: "https://devblogs.microsoft.com/oldnewthing/20260903-00/?p=112672"
fetched_at: 2026-09-04T10:00:43.960294+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# The case of the progress callback that never got called when progress happened

Source: https://devblogs.microsoft.com/oldnewthing/20260903-00/?p=112672

A colleague was trying to figure out why their progress handler wasn’t being called.
// C#

async Task<bool> DownloadItemAsync(string id)
{
    var op = item.DownloadAsync(id);
    op.Progress += (s, pct) UpdateProgress(pct);
    var result = await op;
    ClearProgress();
    return result;
}
This is pretty standard stuff. Start the operation, hook up the progress, and then wait for the operation to complete. But they never got any progress.
I asked them to check if maybe the item was downloading so fast that they missed all the progress. But no, even if the download takes a long time, they never get any progress.
I suggested that they step through the
Download­Async
method to see where it raises progress, and then follow the execution to the point where the progress callback is supposed to be invoked, to see why it didn’t make it. (To be fair, this is a cross-language debugging problem, so it’s harder than it looks. I suggested just focusing on the C++ side: Wait for the COM-callable wrapper to be generated and set as the progress callback, and then set a breakpoint on that wrapper. If that breakpoint gets hit, but the C# code doesn’t run, then there is a problem in the projection. If the breakpoint never gets hit, then the problem is on the C++ side.)
My colleague came back with the answer. Here’s the code for
Download­Async
:
// C++/WinRT

winrt::IAsyncOperationWithProgress<bool, double>
    AggregateSource::DownloadAsync(winrt::hstring id)
{
    std::wstring_view idview { id };
    auto pos = idview.find(L':');
    if (pos == std::wstring_view::npos) {
        co_return false;
    }

    auto providerId = Unescape(idview.substr(0, pos - 1));

    auto provider = GetProvider(providerId);
    if (!provider) {
        co_return false;
    }

    auto providerItemId = Unescape(idview.substr(pos + 1));
    co_return co_await provider.DownloadAsync(providerItemId);
}
The
Aggregate­Source
gathers items from multiple providers. The format of the
id
is a provider, a colon, and then an ID. (The provider ID and item ID are escaped, just in case they themselves happen to contain a colon.)
We look up the provider, and then ask the provider to download the item.
Do you see the problem?
The
Download­Async
does not generate any progress reports!
It never calls
co_await winrt::get_progress_token()
, much less call the token with a progress value to generate a progress report.
It’s apparent that what the code wants to do when it attaches the progress callback is to receive callbacks from the
inner
operation, the one that comes from the provider. However, the only
IAsync­Operation­With­Progress
that it has access to is the one returned by the
Aggregate­Source::
Download­Async
method.
The easy solution here is to get rid of the middle man and just return the provider’s
IAsync­Operation­With­Progress
. That way, the caller can connect to the underlying operation’s progress.
winrt::IAsyncOperationWithProgress<bool, double>
    AggregateSource::DownloadAsync(winrt::hstring id)
{
    std::wstring_view idview { id };
    auto pos = idview.find(L':');
    if (pos == std::wstring_view::npos) {
return
completed_async
(false);
}

    auto providerId = Unescape(idview.substr(0, pos - 1));

    auto provider = GetProvider(providerId);
    if (!provider) {
return completed_async(false);
}

    auto providerItemId = Unescape(idview.substr(pos + 1));
return provider.DownloadAsync(providerItemId);
}
If you don’t believe in
completed_
async
, you can just write
return [] -> winrt::IAsyncOperationWithProgress<bool, double> {
            return false;
        }();
I said that this is the easy solution. There’s also a hard solution, which we will have to look at later because I haven’t written it up yet.
