---
title: "Forcing an ARM64X executable to run as a specific architecture"
url: "https://devblogs.microsoft.com/oldnewthing/20260814-00/?p=112613"
fetched_at: 2026-08-15T10:14:58.686499+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# Forcing an ARM64X executable to run as a specific architecture

Source: https://devblogs.microsoft.com/oldnewthing/20260814-00/?p=112613

ARM64X is a
fat binary
Windows executable and DLL format for 64-bit ARM systems. For DLLs, the choice is clear, since only one of them will work: The version of the DLL that is loaded is the one that matches the host process. If the host process uses the Windows ARM64 ABI, then the ARM64 version of the DLL is used, and if the host process is x86-64-based or uses the Windows ARM64EC ABI¹
For executables, the system has a choice. It could run the process as ARM64 or it could run it as ARM64EC. How can you force the system to choose the architecture you prefer?
You may want to do this if you have a program that is compiled as ARM64X because you have a plug-in model, and you want to be able to support plug-ins that are written either as ARM64 or x86-64. You compile an ARM64 version for ARM64 plug-ins, and you compile an ARM64EC version for x86-64 plug-ins. At run time, you realize that the user passed a plug-in for the other architecture, so you want to relaunch yourself as the matching architecture.
You can do it with the
PROC_
THREAD_
ATTRIBUTE_
MACHINE_
TYPE
attribute.
Here’s a program that takes a DLL on the command line. It tries to load it as the native architecture, but if that fails, and the native architecture is ARM64, then it relaunches itself as x86-64 to try again.
#include <windows.h>
#include <stdio.h>
#include <wil/result_macros.h>
#include <wil/resource.h>
#include <wil/stl.h>
#include <wil/win32_helpers.h>

int wmain(int argc, wchar_t** argv)
{
    if (argc < 2) {
        printf("Oops\n");
        return 0;
    }

    wil::unique_hmodule dll{ LoadLibraryExW(path, nullptr, 0) };
    if (dll) {
        return RunPlugin(dll);
    }

    if (GetLastError() != ERROR_BAD_EXE_FORMAT) {
        printf("Can't load DLL, sorry\n");
        return 0;
    }

    SYSTEM_INFO info{};
    GetSystemInfo(&info);
    if (info.wProcessorArchitecture != PROCESSOR_ARCHITECTURE_ARM64) {
        printf("Can't load DLL, sorry\n");
        return 0;
    }

    printf("Trying again as x86-64\n");
WORD arch = IMAGE_FILE_MACHINE_AMD64;
auto single =
make_proc_thread_attribute_list
({
{PROC_THREAD_ATTRIBUTE_MACHINE_TYPE, &arch}
});
wchar_t self[MAX_PATH + 1];
    std::wstring self;
    THROW_IF_FAILED(wil::GetModuleFileNameW(nullptr, self));

    wil::unique_process_information pi;

    STARTUPINFOEXW info{ sizeof(STARTUPINFOEXW) };
info.lpAttributeList = single.get();
if (!CreateProcessW(self.data(), GetCommandLineW(), nullptr, nullptr,
            false, EXTENDED_STARTUPINFO_PRESENT, nullptr, nullptr,
            &info.StartupInfo, &pi)) {
        printf("Can't relaunch as x86-64, sorry\n");
        return 0;
    }

    WaitForSingleObject(pi.hProcess, INFINITE);
    // destructors will close the handles
}
If we can load the DLL, then great! We run it as usual.
If we can’t load the DLL because it’s in the wrong format, then we will retry as x86-64 if the current process is running as ARM64. To do that, we create an attribute list with the
PROC_
THREAD_
ATTRIBUTE_
MACHINE_
TYPE
attribute whose value is the architecture we want to try, namely AMD64 (which is the Windows name for x86-64), and relaunch ourselves with the same command line.²
If the DLL fails to load even as x86-64, then the x86-64 version of our program just gives up without trying again as ARM64. (You don’t want to have the x86-64 version try again as ARM64 because that would create an infinite loop.)
¹ You can think of ARM64EC as “pre-jitted x86-64 on ARM64.” It is like taking an x86-64 binary and compiling it to ARM64 code that is equivalent to (but presumably has better performance than) the version the emulator would have created on the fly from your x86-64 version. Instead of shipping an x86-64 version that the emulator has to translate to ARM64, just ship the translated version.
² In real life, you probably would add some safety precautions to prevent accidental fork bombs. While writing up this article, I fork bombed my machine a few times by mistake.
