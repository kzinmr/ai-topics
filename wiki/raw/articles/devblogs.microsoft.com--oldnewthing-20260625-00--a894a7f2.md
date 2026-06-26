---
title: "The case of the DLL that was not present in memory despite not being formally unloaded, part 1"
url: "https://devblogs.microsoft.com/oldnewthing/20260625-00/?p=112467"
fetched_at: 2026-06-26T07:00:57.215136+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# The case of the DLL that was not present in memory despite not being formally unloaded, part 1

Source: https://devblogs.microsoft.com/oldnewthing/20260625-00/?p=112467

The team responsible for shell32.dll received a bug saying that they were responsible for a large number of crashes in a particular third party program. Opening the crash dumps showed the clear signs of a stack overflow:
# Child-SP          RetAddr           Call Site
00 000000ba`92851098 00007ff9`fed521c1 ntdll!_chkstk+0x37
01 000000ba`928510b0 00007ff9`feea5ace ntdll!RtlDispatchException+0x2d1
02 000000ba`92851300 00007ff9`fed4e02d ntdll!KiUserExceptionDispatch+0x2e
03 000000ba`92852060 00007ff9`fed5222f ntdll!RtlLookupFunctionEntry+0x8d
04 000000ba`928520b0 00007ff9`feea5ace ntdll!RtlDispatchException+0x33f
05 000000ba`92852800 00007ff9`fed4e02d ntdll!KiUserExceptionDispatch+0x2e
06 000000ba`92853560 00007ff9`fed5222f ntdll!RtlLookupFunctionEntry+0x8d
07 000000ba`928535b0 00007ff9`feea5ace ntdll!RtlDispatchException+0x33f
08 000000ba`92853d00 00007ff9`fed4e02d ntdll!KiUserExceptionDispatch+0x2e
09 000000ba`92854a60 00007ff9`fed5222f ntdll!RtlLookupFunctionEntry+0x8d
0a 000000ba`92854ab0 00007ff9`feea5ace ntdll!RtlDispatchException+0x33f
0b 000000ba`92855200 00007ff9`fed51f29 ntdll!KiUserExceptionDispatch+0x2e
0c 000000ba`92855f70 00007ff9`feea5ace ntdll!RtlLookupFunctionEntry+0x8d
0d 000000ba`928561c0 00007ff9`fed4e02d ntdll!RtlDispatchException+0x33f
...
The highlighted block of stack frames (from
Rtl­Lookup­Function­Entry
to
Ki­User­Exception­Dispatch
) repeated for a very long time.
We are clearly in some sort of recursive exception handling death spiral. An exception occurred, and the kernel has decided that it is not something that kernel mode can handle,¹ so it reflected the exception back into user mode for further processing (
Ki­User­Exception­Dispatch
). While trying to figure out which exception handler to call, (
Rtl­Lookup­Function­Entry
), we took an exception, which restarted the exception loop.
Eventually, all of these recursive exceptions exhausted the stack, and we take a stack overflow exception that terminates the process.
The bug was assigned to shell32 because it looked like shell32 was the source of the original exception. If you walk all the way back to the bottom of the stack, you get something like this:
23f 000000ba`9294c620 00007ff9`fed5222f ntdll!RtlLookupFunctionEntry+0x8d
240 000000ba`9294c670 00007ff9`feea5ace ntdll!RtlDispatchException+0x33f
241 000000ba`9294cdc0 00007ff9`fed4e02d ntdll!KiUserExceptionDispatch+0x2e
242 000000ba`9294db20 00007ff9`fed5222f ntdll!RtlLookupFunctionEntry+0x8d
243 000000ba`9294db70 00007ff9`feea5ace ntdll!RtlDispatchException+0x33f
244 000000ba`9294e2c0 00007ff9`fcba0af0 ntdll!KiUserExceptionDispatch+0x2e
245 000000ba`9294f018 00007ff9`fde2ad13 combase!CoTaskMemFree
246 000000ba`9294f020 00007ff9`fc7abc75 shell32!wil::details::string_maker::~string_maker+0x13
247 000000ba`9294f050 00007ff9`fc7ab897 ucrtbase!<lambda_f03950bc5685219e0bcd2087efbe011e>::operator()+0xa5
248 000000ba`9294f0a0 00007ff9`fc7ab84d ucrtbase!__crt_seh_guarded_call<int>::operator()+0x3b
249 000000ba`9294f0d0 00007ff9`fc7d2f0c ucrtbase!execute_onexit_table+0x3d
24a 000000ba`9294f110 00007ff9`fdff4645 ucrtbase!__crt_state_management::wrapped_invoke+0x2c
24b 000000ba`9294f140 00007ff9`fdff476e shell32!dllmain_crt_process_detach+0x45
24c 000000ba`9294f180 00007ff9`fee9f6fe shell32!dllmain_dispatch+0xe6
24d 000000ba`9294f1e0 00007ff9`fed4bcae ntdll!LdrpCallInitRoutineInternal+0x22
24e 000000ba`9294f210 00007ff9`fedcd37f ntdll!LdrpCallInitRoutine+0x10e
24f 000000ba`9294f280 00007ff9`fedcc54e ntdll!LdrShutdownProcess+0x17f
250 000000ba`9294f390 00007ff9`fdcb18ab ntdll!RtlExitUserProcess+0x9e
251 000000ba`9294f3c0 00007ff9`e754882e kernel32!ExitProcessImplementation+0xb
252 000000ba`9294f3f0 00007ff9`e754f344 mscoreei!RuntimeDesc::ShutdownAllActiveRuntimes+0x2fa
253 000000ba`9294f6d0 00007ff9`e66f464b mscoreei!CLRRuntimeHostInternalImpl::ShutdownAllRuntimesThenExit+0x14
254 000000ba`9294f700 00007ff9`e66f44c9 clr!EEPolicy::ExitProcessViaShim+0x8b
255 000000ba`9294f760 00007ff9`e66f441e clr!SafeExitProcess+0x9d
256 000000ba`9294f9e0 00007ff9`e66f3f44 clr!HandleExitProcessHelper+0x3e
257 000000ba`9294fa10 00007ff9`e66f3e24 clr!_CorExeMainInternal+0xf8
258 000000ba`9294faa0 00007ff9`e753d6da clr!CorExeMain+0x14
259 000000ba`9294fae0 00007ff9`e75d785b mscoreei!CorExeMain+0xfa
25a 000000ba`9294fb40 00007ff9`fdc9e8d7 mscoree!CorExeMain_Exported+0xb
25b 000000ba`9294fb70 00007ff9`fedcc40c kernel32!BaseThreadInitThunk+0x17
25c 000000ba`9294fba0 00000000`00000000 ntdll!RtlUserThreadStart+0x2c
The repeating block stops at the source of the first exception:
combase!
Co­Task­Mem­Free
.
We can look for the exception record to see what the original problem was.
The exception record and context record are probably passed to
Rtl­Dispatch­Exception
, so we can see what
Ki­User­Exception­Dispatch
passes.
# Child-SP
RetAddr
Call Site
243 000000ba`9294db70
00007ff9`feea5ace
ntdll!RtlDispatchException+0x33f
244 000000ba`9294e2c0
00007ff9`fcba0af0
ntdll!KiUserExceptionDispatch+0x2e

0:000> u ntdll!KiUserExceptionDispatch 00007ff9`feea5ace 
ntdll!KiUserExceptionDispatch:
00007ff9`feea5aa0 cld
00007ff9`feea5aa1 mov     rax,qword ptr [ntdll!Wow64PrepareForException (00007ff9`fef272f0)]
00007ff9`feea5aa8 test    rax,rax
00007ff9`feea5aab je      ntdll!KiUserExceptionDispatch+0x1c (00007ff9`feea5abc)
00007ff9`feea5aad mov     rcx,rsp
00007ff9`feea5ab0 add     rcx,4F0h
00007ff9`feea5ab7 mov     rdx,rsp
00007ff9`feea5aba call    rax
00007ff9`feea5abc
mov     rcx,rsp
00007ff9`feea5abf
add     rcx,4F0h
00007ff9`feea5ac6
mov     rdx,rsp
00007ff9`feea5ac9 call    ntdll!RtlDispatchException (00007ff9`fed51ef0)
00007ff9`feea5ace test    al,al
We see that the two parameters passed to
Rtl­Dispatch­Exception
are at
rsp+4f0h
and
rsp
. I’m guessing that the exception record comes first, followed by the context record, since that’s the order that those pointers appear in the
EXCEPTION_POINTERS
.
#
Child-SP
RetAddr           Call Site
244
000000ba`9294e2c0
00007ff9`fcba0af0 ntdll!KiUserExceptionDispatch+0x2e

00007ff9`feea5ace test    al,al
0:000> dps 000000ba`9294e2c0+4f0
000000ba`9294e7b0  00000000`
c0000005
← STATUS_ACCESS_VIOLATION
000000ba`9294e7b8  00000000`00000000
000000ba`9294e7c0  00007ff9`fcba0af0 combase!CoTaskMemFree
000000ba`9294e7c8  00000000`00000002
000000ba`9294e7d0  00000000`00000008
Yup, that looks like an exception record. It starts with the exception code, and is shortly after followed by the code address where the exception was taken.
0:000> .exr 000000ba`9294e2c0+4f0
ExceptionAddress: 00007ff9fcba0af0 (combase!CoTaskMemFree)
   ExceptionCode: c0000005 (Access violation)
  ExceptionFlags: 00000000
NumberParameters: 2
   Parameter[0]: 0000000000000008
   Parameter[1]: 00007ff9fcba0af0
Attempt to execute non-executable address 00007ff9fcba0af0
Okay, so we attempted to execute a non-executable address, and the address is
combase!
Co­Task­Mem­Free
.
Just for fun, let’s confirm that the second parameter really is a context record:
0:000> .cxr 000000ba`9294e2c0
rax=00007ff9fe3a9850 rbx=000001bbebd12388 rcx=000001bbebd63140
rdx=00007ff9fe4e99e0 rsi=000001bbebd12828 rdi=000001bbebd12310
rip=00007ff9fcba0af0 rsp=000000ba9294f018 rbp=0000df1c60b20569
 r8=000001bbebd12310  r9=0000df1c60b20569 r10=d94b3944a87271f0
r11=000000000000000b r12=0000000000000001 r13=00007ff9fdff47c0
r14=000000ba9294f128 r15=000001bbebd12310
iopl=0         nv up ei pl nz na pe nc
cs=0033  ss=002b  ds=002b  es=002b  fs=0053  gs=002b             efl=00010202
combase!CoTaskMemFree:
00007ff9`fcba0af0 sub     rsp,28h
Yup, looks like a context record.
But wait, the exception claims that
combase!
Co­Task­Mem­Free
isn’t executable. First, let’s see if the debugger agrees with this assessment.
0:000> !address  00007ff9`fcba0af0

Usage:                  Image
Base Address:           00007ff9`fcb20000
End Address:            00007ff9`fcea6000
Region Size:            00000000`00386000 (   3.523 MB)
State:                  00010000
MEM_FREE
Protect:                00000001
PAGE_NOACCESS
Type:                   <info not present at the target>
Image Path:             C:\Windows\System32\combase.dll
Module Name:            combase
Loaded Image Name:      combase.dll
Mapped Image Name:      C:\symbols\combase.dll
More info:              lmv m combase
More info:              !lmi combase
More info:              ln 0x7ff9fcba0af0
More info:              !dh 0x7ff9fcb20000

Content source: 2 (mapped), length: 1eb510
The memory that contains the
Co­Task­Mem­Free
function has been freed!
In fact, if you look at the base address and region size, you see that the entirety of
combase.dll
has been unloaded from memory.
On the other hand, if you ask the loader what it thinks about that address, it says “Oh, that’s code inside
combase.dll
.”
0:000> !dlls -c 00007ff9`fcba0af0

0x1bbeb111020: C:\WINDOWS\System32\combase.dll
      Base   0x7ff9fcb20000  EntryPoint  0x7ff9fcc9a9d0  Size        0x00386000    DdagNode     0x1bbeb114380
      Flags  0x0028a2cc  TlsIndex    0x00000000  LoadCount   0xffffffff    NodeRefCount 0x00000000
             <unknown>
             LDRP_LOAD_NOTIFICATIONS_SENT
             LDRP_IMAGE_DLL
             LDRP_PROCESS_ATTACH_CALLED
Okay, now that we’ve gathered evidence, let’s see what theory we can develop.
The
combase.dll
is still in the loader’s bookkeeping, and we see that its load count is
0xFFFFFFFF
, which means that the DLL has been “pinned”, meaning that the loader will never unload it. These two pieces of information suggest that the DLL was not removed from memory by
Free­Library
, but rather by somebody explicitly freeing it, say by doing a
Virtual­Free
on the memory.
My guess is that a memory corruption bug somewhere caused some code to clean up the wrong memory blocks, and it unwittingly freed the memory occupied by
combase.dll
, say because somebody overwrote its “don’t forget to free this” variable with the address of
combase.dll
, or because there is an uninitialized variable bug, and the uninitialized value just happened to be a leftover copy of
combase.dll
‘s base address.
But either way, the problem is not with shell32. Shell32 is just another victim, being the first DLL to call into combase after it was forcibly removed from memory by some unknown component.
If this theory is true, then I should be able to find similar types of crashes where some other DLL is the victim of a DLL being forcibly removed from memory.
I asked for the 100 most recent crashes in that third party program and put them into a pivot table so I could see the distribution.
Failure type
Count
bugcheck_0x124_0_…
1
bugcheck_0x139_a_…
1
bugcheck_0x7f_8_…
1
bugcheck_0xe6_26_…
7
access_violation_c0000005_contoso!unknown_error_in_application
23
access_violation_c0000005_gdi32full.dll!__dyn_tls_init
1
access_violation_c0000005_shell32.dll!invokeshellexecutehook
1
clr_exception_80004005_contoso!contoso.program.main
3
clr_exception_80004005_contoso!unknown_function
1
clr_exception_80070002_contoso!contoso.program.main
6
clr_exception_80070002_contoso!unknown_function
3
clr_exception_80070005_contoso!contoso.program.main
1
clr_exception_8007000b_contoso!contoso.program.main
21
clr_exception_8007000e_contoso!contoso.program.main
1
clr_exception_80070422_windows.management.winmd!unknown
1
clr_exception_800705af_contoso!contoso.program.main
1
clr_exception_800705af_contoso!unknown_function
2
clr_exception_8013152d_contoso!contoso.program.main
1
illegal_instruction_c000001d_contoso!unknown_error_in_application
1
stack_overflow_c0000005_contoso!unknown_error_in_application
9
stack_overflow_c0000005_ctxapclient64.dll!unknown
2
stack_overflow_c0000005_shell32.dll!wil::details::string_maker::~string_maker
11
stack_overflow_c00000fd_contoso!unknown_error_in_process
1
The shell32 bug is the second-from the bottom, responsible for 11% of the crashes. But there are 13 other stack overflow bugs. And there are also a bunch of access violations in “unknown”.
I spot checked those stack overflow and “unknown access violation” crashes, and I found that they were all the same form as the shell32 bug, but with different DLLs: While sending
DLL_
PROCESS_
DETACH
notifications, a DLL was found to have been forcible removed from memory, and whatever DLL was the next one to call into that force-unloaded DLL was blamed, even though it was the victim. (A bunch of these arrived as “unknown access violation” because the system saw the crash inside the exception dispatching code and was for some reason unable to walk the stack all the way to the start of the recursive crash loop.)
So a total of 46% of the crashes were due to this rogue force-unload of a DLL. This is a case of
bucket spray
, where a single underlying cause generates a large number of different types of crashes.
The good news for the shell32 team is that they are off the hook; they are the victim. The bad news is that we don’t know who the culprit is.
Next time, we’ll learn some more about these crashes, and that will help confirm some theories about this specific one and may even discredit other theories.
¹ Things that kernel mode can handle are things like guard page exceptions (by expanding the stack) or page faults in paged-out memory (by paging it back in).
