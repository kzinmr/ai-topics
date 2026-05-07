---
title: "Why not have changes in API behavior depend on the SDK you link against?"
url: "https://devblogs.microsoft.com/oldnewthing/20260506-00/?p=112303"
fetched_at: 2026-05-07T07:01:38.126478+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# Why not have changes in API behavior depend on the SDK you link against?

Source: https://devblogs.microsoft.com/oldnewthing/20260506-00/?p=112303

Some time ago, I noted that
the
Co­Initialize­Security
function demands an absolute security descriptor
, even though many functions in Windows produce self-relative security descriptors, forcing you to perform a relative-to-absolute conversion, even though the function internally just converts it back from absolute to relative.
Commenter tbodt wrote
,
This one seems easy enough to fix by Apple’s technique of giving the function the old behavior when the program is linked against the old SDK.
This sure sounds easy. If your program links with the newer SDK, then it gets the new behavior of accepting self-relative security descriptors. But if it links with the old SDK, then it gets the old behavior of requiring absolute security descriptors. If you want the new behavior, then you link with the new SDK.
This does create a subtlety that if you choose the wrong SDK to link against, everything still builds, but the results are different. Traditionally, Windows SDKs are forward-compatible: You can take an old program and link it against a newer SDK, and it will work exactly the same because the old program uses only the backward-compatible subset of the newer SDK. If you change behavior based on the SDK version that you link with, then it may not be obvious that the change in behavior you are experiencing is due to having upgraded the SDK libraries.
Also, what if a program is linked with one version of the SDK, but a DLL that it uses is linked with a different version of the SDK? Maybe you’re using a UI framework library that hasn’t seen any need to update to the newer SDK. Or maybe your program is the one using an old version of the SDK, but the UI framework library is using the newer one. Do you let the main program’s SDK version dictate the behavior of the function, even though the DLL is expecting different behavior? The poor DLL is going to call
Co­Initialize­Security
, and it won’t behave the way it expects.
Okay, so maybe you decide that the function changes its behavior not based on the program’s linked SDK version but rather the version of the calling DLL. But how does a function know which DLL called it? You might say, “Well, you can look at which DLL the return address belongs to.” But that doesn’t work in the case of tail call optimization.
// some function in a DLL
HRESULT InitializeWidgets(
    UINT maxWidgets,
    const WIDGET_ID* ownerId,
    PCWSTR ownerDescription,
    PCWSTR countainerName,
    PCWSTR containerDescription,
    COLORREF defaultColor,
    UINT defaultWidth,
    UINT defaultHeight,
    bool isRemoteAccessible,
    bool isPersistent)
{
    ⟦ various initialization steps ⟧

    static BYTE sd[] = { 0x01, ⟦ hard-coded values ⟧ };

    return CoInitializeSecurity(sd, -1, nullptr, nullptr,
                                RPC_C_AUTHN_LEVEL_DEFAULT,
                                RPC_C_IMP_LEVEL_IDENTIFY,
                                nullptr, EOAC_NONE, nullptr);
}
That final call to
Co­Initialize­Security
could be optimized into a tail call, in which case the subroutine call instruction changes to an unconditional branch, with the return address being the address of
Initialize­Widget
‘s caller. If
Co­Initialize­Security
snooped at its return address, it would be checking the SDK version of the wrong DLL.
Conversely, what if the function in the DLL is just a wrapper?
HRESULT CoInitializeSecuritywithLogging(
    _In_opt_ PSECURITY_DESCRIPTOR pSecDesc,
    _In_ LONG cAuthSvc,
    _In_reads_opt_(cAuthSvc) SOLE_AUTHENTICATION_SERVICE* asAuthSvc,
    _In_opt_ void* pReserved1,
    _In_ DWORD dwAuthnLevel,
    _In_ DWORD dwImpLevel,
    _In_opt_ void* pAuthList,
    _In_ DWORD dwCapabilities,
    _In_opt_ void* pReserved3)
{
    if (dwCapabilities & EOAC_APPID) {
        LogUuid("CoInitializeSecurity with APPID", (UUID*)pSecDesc);
    } else if (dwCapabilities & EOAC_ACCESS_CONTROL) {
        Log("CoInitializeSecurity with IAccessControl");
    } else {
        LogSecurityDescriptor("CoInitializeSecurity with security descriptor", pSecDesc);
    }
    HRESULT hr = CoInitializeSecurity(pSecDesc, cAuthSvc, asAuthSvc, pReserved1,
                        dwAuthnLevel, dwImpLevel, pAuthList, dwCapabilities, pReserved3);
    Log("CoInitializeSecurity returned", hr);
}
If you look at the return address, you will find the wrapper function and change your behavior to match the version that the wrapper function was built with, but that wrapper function is just passing through the parameters from its caller. It’s really the caller whose behavior we want to match, not the wrapper.
And what if the library is a static library rather than a DLL? It was written for one version of the SDK, but you link to another, and the behavior changes, and even if the function checks the return address, it will get the DLL’s address and see the DLL’s SDK version rather than the version the library wanted.
Changing behavior based on the SDK version you link to works only if programs are monolithic.
Bonus chatter
: Changing to a newer SDK’s
header files
do create behavioral changes because, for example, structures with an explicit size member might get extended to contain additional fields, and the API uses the value of the size member to decide which version of the SDK the caller is using. But this is not dependent on the SDK that the caller links to, which is a good thing, because it lets you take static libraries which use different versions of the SDK header files and link them all together into a single program or DLL, and they will still work.
