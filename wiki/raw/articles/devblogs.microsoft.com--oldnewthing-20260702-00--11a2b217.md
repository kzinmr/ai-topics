---
title: "The case of the thread executing from an unloaded third-party DLL"
url: "https://devblogs.microsoft.com/oldnewthing/20260702-00/?p=112500"
fetched_at: 2026-07-03T07:00:57.425947+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# The case of the thread executing from an unloaded third-party DLL

Source: https://devblogs.microsoft.com/oldnewthing/20260702-00/?p=112500

The Explorer team was investigating a crash that was occuring at a relatively high rate and found that it took the form of a thread executing from an unloaded third-party DLL.
0:173> k
RetAddr               Call Site
00000000`557c5820     <Unloaded_LibUtils_CloudNs_3.dll>+0x265fe
00000000`00000008     <Unloaded_LibUtils_CloudNs_3.dll>+0x2b5820
00000000`0000000e     0x8
00000000`00000008     0xe
00000000`557c8c18     0x8
ffffffff`fffffffe     <Unloaded_LibUtils_CloudNs_3.dll>+0x2b8c18
00000000`00000000     0xffffffff`fffffffe
There isn’t much on the stack at all.
0:173> dps @rsp
00000000`1248f920  00000000`557c5820 <Unloaded_LibUtils_CloudNs_3.dll>+0x2b5820
00000000`1248f928  00000000`00000008
00000000`1248f930  00000000`0000000e
00000000`1248f938  00000000`00000008
00000000`1248f940  00000000`557c8c18 <Unloaded_LibUtils_CloudNs_3.dll>+0x2b8c18
00000000`1248f948  ffffffff`fffffffe
00000000`1248f950  00000000`00000000
00000000`1248f958  00000000`00000000
00000000`1248f960  00000000`00000000
00000000`1248f968  00000000`00000000
00000000`1248f970  00000000`00000000
00000000`1248f978  00000000`00000000
00000000`1248f980  00000000`00000000
00000000`1248f988  00007ff9`a2117344 kernel32!BaseThreadInitThunk+0x14
00000000`1248f990  00000000`00000000
00000000`1248f998  00000000`00000000
This is just a worker thread the operates entirely inside
LibDB.CloudNs.3.dll
. It doesn’t have a very deep stack, so I suspect that it’s idle and is waiting for work to do.
For these types of investigations, there usually isn’t much to see directly in the crashing thread. That thread is the victim. You have to do additional research to figure out who unloaded the DLL prematurely.
Some snooping around found another stack that involves this unloaded DLL:
0:159> k
RetAddr               Call Site
00007ff9`9fdbbea0     ntdll!ZwWaitForMultipleObjects+0x14
00007ff9`9fdbbd9e     KERNELBASE!WaitForMultipleObjectsEx+0xf0
00000000`554d65fe     KERNELBASE!WaitForMultipleObjects+0xe
00000000`55765820     <Unloaded_LibDB_CloudNs_3.dll>+0x965fe
00000000`00000003     <Unloaded_LibUtils_JsonNs_3.dll>+0x255820
00000000`00000004     0x3
00000000`00000008     0x4
00000000`55768c18     0x8
ffffffff`fffffffe     <Unloaded_LibUtils_CloudNs_3.dll>+0x258c18
00000000`00000000     0xffffffff`fffffffe
The most recently unloaded DLLs are
00007ff9`6d7c0000 00007ff9`6d80a000   FabrikamContextMenu.dll
00007ff9`115e0000 00007ff9`1172f000   LitWareSync.dll
00007ff9`643d0000 00007ff9`64681000   CcNamespace.dll
00000000`55440000 00000000`5550b000   LibDB_CloudNs_3.dll
00000000`55860000 00000000`55998000   LibNet_CloudNs_3.dll
00000000`557f0000 00000000`5585b000   LibJson_CloudNs_3.dll
00000000`55510000 00000000`557e7000   LibUtils_CloudNs_3.dll
00000000`561a0000 00000000`56238000   MSVCP100.dll
00000000`56240000 00000000`56312000   MSVCR100.dll
00007ff9`85130000 00007ff9`85167000   EhStorShell.dll
00007ff9`3cac0000 00007ff9`3cb61000   wpdshext.dll
00007ff9`78a00000 00007ff9`78a26000   EhStorAPI.dll
00007ff9`686f0000 00007ff9`68754000   PlayToDevice.dll
00007ff9`67110000 00007ff9`6718d000   provsvc.dll
So the
LibDB.CloudNs.3.dll
that got unloaded is just part of an entire ecosystem of
Lib*.CloudNs.3.dll
dynamic libraries that all got unloaded together.
The ringleader of this operation appears to be
CcNamespace.dll
, which looks like the Contoso namespace extension that adds a “Contoso” node under
My Computer
This PC
that gives you a view into all your Contoso things stored in the Contoso cloud service. All the other DLLs are helpers that the main
CcNamespace.dll
uses to accomplish its tasks.
The main
CcNamespace.dll
was loaded by Explorer as a shell extension, and its
Dll­Can­Unload­Now
function was returning
S_OK
when there were no active references to objects in
CcNamespace.dll
. Unfortunately, when it said “Sure, it’s safe to unload me”, that linchpin DLL unloaded all its minions, unaware that one of the minions (the utility library) had spun up some worker threads.
You might think that the fix is to update the utility library’s
Dll­Can­Unload­Now
to return
S_FALSE
if there are still busy background threads.¹ But that doesn’t work because the utility library is probably not a COM DLL in the first place. It’s just a traditional DLL that
CcNamespace.dll
uses, and it is
CcNamespace.dll
that is the COM DLL.
The
Dll­Can­Unload­Now
in
CcNamespace.dll
could warn
LibUtils.CloudNs.3.dll
that it should start winding down, but you’re basically in a tricky spot because the
DLL_
PROCESS_
ATTACH
cannot wait for the worker thread to exit.
I think the way to go is for the worker thread to increment the DLL reference count when it starts its worker thread, and to use
Free­Library­And­Exit­Thread
to exit the worker thread. Alternatively, it could make its worker thread a threadpool thread and use
Free­Library­When­Callback­Returns
to request that the system decrement the DLL reference count when it finishes.
This is probably something the utility library should have done anyway. I suspect that the worker thread is not something that clients of the utility library are even aware of. It is just an implementation detail of the utility library, created without the knowledge of the main DLL.
Fortunately, the application compatibility team has a copy of Contoso Cloud in their library, so even though we couldn’t reproduce the crash, we were still able to confirm that
CcNamespace.dll
is indeed the shell extension DLL whose unloading triggers the unloading of all the dependent DLLs.
We were about to contact Contoso with our conclusions and suggestions for improvement, but we discovered that it would be pointless because Contoso discontinued that namespace extension years ago. They replaced it with a different way of integrating their cloud content into Windows; the only people using the namespace extension are those who still using an old version, either because they don’t want to pay for the upgrade, or because they are actively avoiding the upgrade because they like the old way.
Those customers are using a product that has gone out of support. Contoso doesn’t care about those old customers any more. Windows will have to fix it without Contoso’s help.
The Explorer team added an application compatibility flag for the Contoso Cloud namespace extension to say “When you load this shell extension, do a
Get­Module­Handle­Ex
with the
GET_
MODULE_
HANDLE_
EX_
FLAG_
PIN
flag so the DLL never unloads.” That way, even if the DLL says “Sure, go ahead and unload me, it’s totally safe, trust me,” and COM does a
FreeLibrary
, the DLL doesn’t actually unload.
¹ Even if you manage to get return
Dll­Can­Unload­Now
to return
S_FALSE
, it doesn’t help if COM is being uninitialized. In that case,
CoUninitalize
will ask a DLL if it is okay to unload now, but the answer is a foregone conclusion
: If COM is shutting down, COM is going to unload all the DLLs that it loaded. It asks you if you are okay with it, not because it cares what your answer is, but to give you a chance to do cleanup outside of
DllMain
.
