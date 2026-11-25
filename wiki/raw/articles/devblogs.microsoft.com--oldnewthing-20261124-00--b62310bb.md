---
title: "What happens to entries in the CoreApplication Properties when the source apartment shuts down?"
url: "https://devblogs.microsoft.com/oldnewthing/20261124-00/?p=112889/"
fetched_at: 2026-11-25T10:00:48.786924+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# What happens to entries in the CoreApplication Properties when the source apartment shuts down?

Source: https://devblogs.microsoft.com/oldnewthing/20261124-00/?p=112889/

Commenter Luca Bacci observed
:
Don’t know why, but last I tried the COM static store (runtime class “Windows.ApplicationModel.Core.CoreApplication”) was accessible from an unpackaged, Win32 application. It also seems to tie entries to the originating apartment lifetime (namely: the apartment from which the property is added). Can you shed some light?
First part first: The COM static store is available to all applications.
This API is supported in Universal Windows Platform apps only,
except for the
Properties
property, which is always available
.
Okay, now the second part: What happens to the entries in the CoreApplication Properties when the source apartment shuts down?
Nothing.
Nothing happens to them. They are still there. Here’s a demonstration:
#include <stdio.h>
#include <winrt/Windows.ApplicationModel.Core.h>
#include <winrt/Windows.Foundation.Collections.h>

int main()
{
    winrt::init_apartment(winrt::apartment_type::single_threaded);

    std::thread t([] {
        winrt::init_apartment(winrt::apartment_type::single_threaded);
        winrt::Windows::ApplicationModel::Core::CoreApplication::Properties().
            Insert(L"meow", winrt::box_value(1));
        winrt::uninit_apartment();
        });

    t.join();

    auto value = winrt::unbox_value<int>(
        winrt::Windows::ApplicationModel::Core::CoreApplication::Properties().
        Lookup(L"meow"));
    
    printf("Got the value %d\n", value);
    winrt::uninit_apartment();
    return 0;
}
After initializing COM on the main thread, we create a secondary thread, on which we also initialize COM in single-threaded mode, add a value to the
Core­Application.
Properties
called
"meow"
with a value of 1, and then uninitialize the apartment.
Back on the main thread, we wait for that to finish, and then go to the
Core­Application.
Properties
and ask for the
"meow"
value, and hey, there it is!
So the entries in
Core­Application.
Properties
do not expire at the expiration of the apartment that added them. But, they do expire when the
last
apartment shuts down, because that’s when COM shuts down for the entire process.
Next time, we’ll investigate what Luca observed.
