---
title: "Why do you say that a COM STA thread must pump messages if I see sample code creating STA threads and not pumping messages?"
url: "https://devblogs.microsoft.com/oldnewthing/20260522-00/?p=112348"
fetched_at: 2026-05-23T07:01:06.286432+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# Why do you say that a COM STA thread must pump messages if I see sample code creating STA threads and not pumping messages?

Source: https://devblogs.microsoft.com/oldnewthing/20260522-00/?p=112348

One of the rules for COM single-threaded apartments (STA) is that the thread in that apartment must pump messages. But we also see code that initializes COM in single-threaded mode but which never pumps messages. Consider
this function
from the
XML DOM object dynamic creation sample
:
int __cdecl wmain()
{
    HRESULT hr = CoInitialize(NULL);
    if (SUCCEEDED(hr))
    {
        dynamDOM();
        CoUninitialize();
    }
    return 0;
}
The
Co­Initialize
function initializes COM in single-threaded apartment mode, and then the program does some work, and then it uninitializes COM, and it
never pumps messages
. What gives? Shouldn’t there be a message loop?
The rule about single-threaded apartments is that they must pump messages
when idle
. If they are busy doing something, then clearly they can’t pump messages because they are busy doing something!¹
If your thread initializes COM as a single-threaded apartment, and then does a bunch of work, and then uninitializes COM, then that’s great. Your thread was never idle, so it never got a chance to pump messages. (Though if your thread made COM calls out to other threads, COM will pump messages while waiting for the reply, so it did pump messages while the thread was idle.)
Failing to pump messages when idle means that when another thread wants to communicate with your thread, it never gets a response. Now, if your thread is busy, then it’s fine that the other thread doesn’t get a response from you—you’re busy with something else after all. But if you are in a single-threaded COM apartment and you have finished with whatever you’re doing, you need to pump messages to see if there’s any work that COM wants you to do, or you need to uninitialize COM.
Now, you might say, “Look, my thread doesn’t create any windows, and it doesn’t do any cross-thread COM stuff, so who cares that it’s not pumping messages? It’s not like anybody is ever going to ask this thread to do anything, and since it created no windows, nobody could send it anything.”
Aha, but you see, your thread
did
create a window. When you initialize a thread as a single-threaded apartment,
COM
creates a window. It creates this window so that it can receive inbound requests for the thread to do something. If you don’t pump messages, then you have a thread blocked not pumping messages, which will jam up window broadcasts.
¹ An intentionally obtuse interpretation of the rule that “an STA thread must pump messages” would be that your thread can’t do anything except call
GetMessage
and
DispatchMessage
! Because any other line of code would not be “pumping messages”.
