---
title: "What happens when you put a non-agile object in the CoreApplication Properties?"
url: "https://devblogs.microsoft.com/oldnewthing/20261126-00/?p=112899/"
fetched_at: 2026-11-27T10:00:55.184761+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# What happens when you put a non-agile object in the CoreApplication Properties?

Source: https://devblogs.microsoft.com/oldnewthing/20261126-00/?p=112899/

Last time, we noticed that
non-agile objects in the
Core­Application.
Properties
appear to behave differently from agile objects
.
I mean, it looks like they behave differently, but that’s only because you are taking too narrow a view.
They behave the same if you interpret the rule as “The objects remain alive until there are no more apartments that can access them.” Non-agile objects can be used only from the apartment that created them, whereas agile objects can be used from any apartment. Therefore, non-agile objects expire when their host apartment shuts down, whereas agile objects expire when
all
apartments shut down.
The
Core­Application.
Properties
uses
Ro­Get­Agile­Reference
to wrap the non-agile object so that it can safely be stored. (Really, it just uses
Ro­Get­Agile­Reference
to wrap
all
objects, but an agile wrapper around an agile object is a nop.)
Internally,
Ro­Get­Agile­Reference
has a variety of mechanisms for creating the agile reference, depending on the flags you pass, but they all have the property that the reference to a non-agile object is released when the apartment shuts down. The observed behavior is coming from
Ro­Get­Agile­Reference
, not from
Core­Application.
Properties
.
Now, the
Properties
collection doesn’t know that the agile reference refers to an expired object. It’s just holding onto the agile reference, waiting to return it when requested.
So let’s try to access the expired object and see what happens.
#include <stdio.h>
#include <winrt/Windows.ApplicationModel.Core.h>
#include <winrt/Windows.Foundation.Collections.h>
struct NonAgile : winrt::implements<NonAgile,
winrt::Windows::Foundation::IInspectable, winrt::non_agile>
{
~NonAgile() { printf("Expired!\n"); }
};
int main()
{
    winrt::init_apartment(winrt::apartment_type::single_threaded);

    std::thread t([] {
        winrt::init_apartment(winrt::apartment_type::single_threaded);
        winrt::Windows::ApplicationModel::Core::CoreApplication::Properties().
            Insert(L"meow",
winrt::make<NonAgile>()
);
        winrt::uninit_apartment();
        });

    t.join();
bool present =
winrt::Windows::ApplicationModel::Core::CoreApplication::Properties().
HasKey(L"meow");
printf("Has the value: %s\n", present ? "true" : "false");
auto value =
winrt::Windows::ApplicationModel::Core::CoreApplication::Properties().
Lookup(L"meow");
printf("Has a value? %s\n", value ? "true" : "false");
winrt::uninit_apartment();
    return 0;
}
I added a message when the non-agile object is destructed so you can see (by stepping through the code) that it happens when the secondary thread calls
uninit_
apartment
to shut down its single-threaded apartment. This is the Global Interface Table relinquishing its reference at apartment shutdown.
After we put the non-agile object in the
Properties
and then shut down its apartment, the non-agile object is destroyed, but the entry remains in the
Properties
, which we can confirm by seeing that
HasKey()
still returns
true
. The key-value pair is still present in the
Properties
.
However, if we try to retrieve the value, the
Lookup
fails with an exception because the entry is now poisoned: It is a reference to an already-destroyed object.¹ You can’t retrieve the poisoned entry; all you can do is remove it.
Next time, we’ll look at how all this fits into the original problem of creating a fake agile wrapper that is technically agile but is not useful outside its home apartment because the original object refuses to be marshaled.
¹ The specific error that is returned is
E_
INVALID­ARG
because the Global interface Table entry is no longer valid. This specific error code is a leaky abstraction. If the developers had thought about it, they could have added code to transform the error into something more appropriate like
RPC_E_SERVER_DIED
.
