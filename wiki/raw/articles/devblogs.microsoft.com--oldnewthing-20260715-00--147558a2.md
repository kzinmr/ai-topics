---
title: "The case of the invalid function pointer when shutting down the display control panel"
url: "https://devblogs.microsoft.com/oldnewthing/20260715-00/?p=112535"
fetched_at: 2026-07-16T07:01:39.130558+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# The case of the invalid function pointer when shutting down the display control panel

Source: https://devblogs.microsoft.com/oldnewthing/20260715-00/?p=112535

The number one crash in the display control panel looks like this:
rax=ffffffff924bbde0 rbx=0000000000000001 rcx=0000000000030440
rdx=0000000000000002 rsi=0000000000030440 rdi=0000000080006011
rip=00007ffac835cd1e rsp=000000155e48e3f8 rbp=000000155e48e749
 r8=0000000000000000  r9=0000000000000000 r10=007fffffffe41b69
r11=00007df502390000 r12=0000000000000000 r13=0000000000000000
r14=0000000000000002 r15=0000000000000000
iopl=0         nv up ei pl nz na pe nc
cs=0033  ss=002b  ds=002b  es=002b  fs=0053  gs=002b             efl=00010206
ntdll!LdrpDispatchUserCallTarget+0xe:
00007fff`924acd1e mov     r11,qword ptr [r11+r10*8] ds:04007df5`0159db48=????????????????
0:000> k
Call Site
ntdll!LdrpDispatchUserCallTarget+0xe
user32!UserCallWinProcCheckWow+0x2bd
user32!DispatchClientMessage+0x9c
user32!__fnDWORD+0x33
ntdll!KiUserCallbackDispatcherContinue
win32u!ZwUserDestroyWindow+0x14
comctl32!_RealPropertySheet+0x36d
comctl32!_PropertySheet+0x47
Display!PropertySheetW+0x5d
Display!AdvancedSettingSheetHelper+0x3be
Display!ShowAdapterSettings+0x89
rundll32!CallRunDllFunction+0x1c
rundll32!wWinMain+0x2bf
rundll32!__wmainCRTStartup+0x1c9
kernel32!BaseThreadInitThunk+0x14
ntdll!RtlUserThreadStart+0x21
From the stack, we see that we have a display adapter settings property sheet. We are destroying it, and we crash trying to validate the window procedure address.
We saw some time ago that
you can pull out the bad address by inspection
.
0:000> u .-e .
ntdll!LdrpDispatchUserCallTarget:
00007fff`924acd10 mov     r11,qword ptr [ntdll+0x001813a8]
00007fff`924acd17 mov     r10,rax
00007fff`924acd1a shr     r10,9
00007fff`924acd1e mov     r11,qword ptr [r11+r10*8]
The register that is the source of the shift is
rax
, so that’s the function pointer. And from the register dump, we see that the address is
rax=ffffffff924bbde0
Yeah, that address doesn’t look like a valid function pointer.
On 64-bit systems, user-mode pointers have low addresses (which start with
0000
), and kernel-mode pointers have high addresses (which start with
ffff
). So this function pointer is clearly invalid for user mode.
Maybe we can fix it so it’s valid again. Let’s see what code addresses are valid in this process.
0:000> lm
start             end                 module name
00000001`80000000 00000001`80043000   contoso
00007ff6`44570000 00007ff6`44587000   rundll32
00007fff`6a4f0000 00007fff`6a6b7000   d3d9
00007fff`6e600000 00007fff`6e6a9000   comctl32_7fff6e600000
00007fff`6f5d0000 00007fff`6f5e5000   pcacli
00007fff`753b0000 00007fff`753c1000   sfc_os
...
00007fff`91020000 00007fff`910f0000   comdlg32
00007fff`912b0000 00007fff`915e6000   combase
00007fff`91600000 00007fff`91794000   user32
00007fff`917a0000 00007fff`91852000   kernel32
00007fff`918e0000 00007fff`91989000   SHCore
00007fff`91990000 00007fff`91ae6000   ole32
00007fff`91af0000 00007fff`91b16000   gdi32
00007fff`91b20000 00007fff`91bc3000   advapi32
00007fff`91bd0000 00007fff`91c67000   sechost
00007fff`91c70000 00007fff`91cc2000   shlwapi
00007fff`91cd0000 00007fff`91ced000   imagehlp
00007fff`91d50000 00007fff`921c0000   setupapi
00007fff`92220000 00007fff`92355000   msctf
00007fff`92420000 00007fff`92610000   ntdll
...
Ny suspicion is that the function pointer got truncated to a 32-bit value, and then was sign-extended back up to a 64-bit value. So we are looking for valid function pointers of the form
xxxxxxxx`924bbde0
. In the above list of valid code addresses, the only ones that have the lower bits in the
92xxxxxx
range all have a high 32 bits of
00007fff
, so let’s plug that in and see if we get a window procedure.
0:000> ln 7fff924bbde0
(00007fff`924bbde0)   ntdll!NtdllButtonWndProc_A   |  (00007fff`924bbdf0)   ntdll!NtdllButtonWndProc_W
Jackpot.
So the caller probably subclassed a window, and then tried to restore the original window procedure, but messed up and restored only the bottom 32 bits.
But who could that be?
0:000> k
Call Site
ntdll!LdrpICallHandler+0xf
ntdll!RtlpExecuteHandlerForException+0xf
ntdll!RtlDispatchException+0x219
ntdll!KiUserExceptionDispatch+0x2e
ntdll!LdrpDispatchUserCallTarget+0xe
user32!UserCallWinProcCheckWow+0x2bd
user32!DispatchClientMessage+0x9c
user32!__fnDWORD+0x33
ntdll!KiUserCallbackDispatcherContinue
win32u!ZwUserDestroyWindow+0x14
comctl32!_RealPropertySheet+0x36d
comctl32!_PropertySheet+0x47
Display!PropertySheetW+0x5d
Display!AdvancedSettingSheetHelper+0x3be
Display!ShowAdapterSettings+0x89
rundll32!CallRunDllFunction+0x1c
rundll32!wWinMain+0x2bf
rundll32!__wmainCRTStartup+0x1c9
kernel32!BaseThreadInitThunk+0x14
ntdll!RtlUserThreadStart+0x21
This is a property sheet, so we should be able to extract the pages of the property sheet. (Note: Requires internal Microsoft symbols, so you won’t be able to do this at home.)
0:000> .frame d
09 00000017`85a7e820 00007fff`86e60349 Display!AdvancedSettingSheetHelper+0x3be
0:000> dv
     hwndParent = <value unavailable>
            psh = struct _PROPSHEETHEADERW_V2
      szMonitor = wchar_t [140] "Generic PnP Monitor"
         rPages = struct _PSP *[100]
        iResult = 0n0
The desktop background control panel is extensible
, and the way that a plug-in adds a page to the desktop background control panel is by handling the
IShellPropSheetExt::
AddPages
method and calling the provided “page adding function” with a
HPROPSHEETPAGE
. What that function does is add the
HPROPSHEETPAGE
to the pages in the property sheet. (We can see that there’s room for 100 of them in the
rPages
.)
And the
psh
is the
PROPSHEETHEADER
.
0:000> ?? psh
struct _PROPSHEETHEADERW_V2
   +0x000 dwSize           : 0x60
   +0x004 dwFlags          : 0x2000001
   +0x008 hwndParent       : 0x00000000`000401aa HWND__
   +0x010 hInstance        : 0x00007fff`86e50000 HINSTANCE__
   +0x018 hIcon            : (null)
   +0x020 pszCaption       : 0x00000017`85a7f100  "Generic PnP Monitor and Contoso Chipset"
   +0x028 nPages           :
4
+0x030 nStartPage       : 0
   +0x038 ppsp             : 0x00000017`85a7ec70 _PROPSHEETPAGEW
   +0x038 phpage           : 0x00000017`85a7ec70  -> 0x000001d5`4e1aac90 _PSP
We see that there are four pages, so we can inspect the first four
HPROPSHEETPAGE
s in
rPages
.
And hey look, we have an array of
HPROPSHEETPAGE
structures
0:000> ?? psh.phpage[0]
struct _PSP * 0x000001d5`4e1aac90
0:000> ?? psh.phpage[1]
struct _PSP * 0x000001d5`4e19e470
0:000> ?? psh.phpage[2]
struct _PSP * 0x000001d5`4e19e520
0:000> ?? psh.phpage[3]
struct _PSP * 0x000001d5`4e1d26d0
The
HPROPSHEETPAGE
is an opaque structure, but we can dump it and look for interesting things, for entertainment purposes only.
0:000> dps 0x000001d5`4e1aac90 l4
000001d5`4e1aac90  000001d5`4e1aac60
000001d5`4e1aac98  00000000`00000000
000001d5`4e1aaca0  00004088`00000068
000001d5`4e1aaca8  00007fff`88d70000 deskadp
0:000> dps 0x000001d5`4e19e470 l4
000001d5`4e19e470  000001d5`4e19e440
000001d5`4e19e478  00000000`00000000
000001d5`4e19e480  00004088`00000068
000001d5`4e19e488  00007fff`893e0000 deskmon
0:000> dps 0x000001d5`4e19e520 l4
000001d5`4e19e520  000001d5`4e19e4f0
000001d5`4e19e528  00000000`00000000
000001d5`4e19e530  000040c8`00000068
000001d5`4e19e538  00007fff`86e30000 colorui
0:000> dps 0x000001d5`4e1d26d0 l4
000001d5`4e1d26d0  000001d5`4e1bcb30
000001d5`4e1d26d8  000001d5`4e1d26a0
000001d5`4e1d26e0  0000008a`00000068
000001d5`4e1d26e8  00000001`80000000 contoso
There are a bunch of
HMODULE
s here, which are probably the modules that the property sheet page came from. The first three come with Windows. The last one apparently is Contoso. Let’s focus on at last one.
After the first two values (which look like pointers), we have
0x00000068
which is not-coincidentally
sizeof(PROPSHEETPAGE)
, so I’m going to guess that this is where the system stores the
PROPSHEETPAGE
that the handle was created from.
Note
: Note that this is an implementation detail and should be used only for debugging purposes. Please don’t write programs that rely on this, because it can change.¹
0:000> dt comctl32!_PROPSHEETPAGEW  000001d5`4e1d26e0
   +0x000 dwSize           : 0x68
   +0x004 dwFlags          : 0x8a
   +0x008 hInstance        : 0x00000001`80000000 HINSTANCE__
   +0x010 pszTemplate      : 0x00000000`00000589  "--- memory read error at address 0x00000000`00000589 ---"
   +0x010 pResource        : 0x00000000`00000589 DLGTEMPLATE
   +0x018 hIcon            : 0x00000000`000503b9 HICON__
   +0x018 pszIcon          : 0x00000000`000503b9  "--- memory read error at address 0x00000000`000503b9 ---"
   +0x020 pszTitle         : 0x000001d5`4e19cde0  "?????"
   +0x028 pfnDlgProc       :
0x00000001`800047ac
contoso+0x47ac
   +0x030 lParam           : 0n2015682301296
   +0x038 pfnCallback      : (null)
   +0x040 pcRefParent      : (null)
   +0x048 pszHeaderTitle   : (null)
   +0x050 pszHeaderSubTitle : (null)
   +0x058 hActCtx          : (null)
   +0x060 hbmHeader        : (null)
   +0x060 pszbmHeader      : (null)
The dialog procedure is
0x00000001`800047ac
. I’m hoping I can reverse-engineer it enough to see the place where it subclassed the button incorrectly.
00000001`800047ac mov     [rsp+8],rbx
00000001`800047b1 mov     [rsp+10h],rbp
00000001`800047b6 mov     [rsp+18h],rsi
00000001`800047bb push    rdi
00000001`800047bc sub     rsp,30h
00000001`800047c0 mov     rdi,r9                ; rdi = r9 = lParam
00000001`800047c3 mov     rbp,r8                ; rbp = r8 = wParam
00000001`800047c6 mov     esi,edx               ; esi = edx = message
00000001`800047c8 mov     rbx,rcx               ; rbx = rcx = hdlg
00000001`800047cb cmp     edx,110h              ; Q: WM_INITDIALOG?
00000001`800047d1 jne     00000001`800047e2     ; N: Skip
00000001`800047d3 mov     r8,[r9+30h]           ; Y: r8 = ((PROPSHEETPAGE*)r9)->lParam
00000001`800047d7 mov     edx,0FFFFFFEBh        ; edx = -21
                                                ; ecx = hdlg (unchanged)
00000001`800047dc call    [00000001`8002b4a0]   ; mystery function 1

00000001`800047e2 mov     edx,0FFFFFFEBh        ; edx = -21
00000001`800047e7 mov     rcx,rbx               ; rcx = hdlg
00000001`800047ea call    [00000001`8002b480]   ; mystery function 2
00000001`800047f0 test    rax,rax               ; Q: Failed?
00000001`800047f3 je      00000001`8000480b     ; Y: Bail out
00000001`800047f5 mov     r9,rbp                ; param4 = wParam
00000001`800047f8 mov     r8d,esi               ; param3 = message
00000001`800047fb mov     rdx,rbx               ; param2 = hdlg
00000001`800047fe mov     rcx,rax               ; param1 = from mystery function 2
00000001`80004801 mov     [rsp+20h],rdi         ; param5 = lParam
00000001`80004806 call    00000001`800045fc     ; mystery function 3
00000001`8000480b mov     rbx,[rsp+40h]         ; restore registers
00000001`80004810 mov     rbp,[rsp+48h]
00000001`80004815 mov     rsi,[rsp+50h]
00000001`8000481a add     rsp,30h
00000001`8000481e pop     rdi
00000001`8000481f ret                            ; done
We know that the
lParam
parameter to the
WM_
INIT­DIALOG
message is the value passed as the “parameter” to functions like
CreateDialogParam
, and specifically for property sheets, it’s a pointer to a
PROPSHEETPAGE
. And we saw from the structure dump above that offset
0x30
is the
lParam
.
From the structure of this function, it’s clear that the magic value
-21
is
GWLP_
USERDATA
, mystery function 1 is
SetWindowLongPtr
, and mystery function 2 is
GetWindowLongPtr
. This is a standard pattern for dialog box functions, and it’s common to use a wrapper function.
The real dialog procedure is the third mystery function, so let’s look at that.
00000001`800045fc mov     [rsp+8],rbx
00000001`80004601 mov     [rsp+10h],rbp
00000001`80004606 mov     [rsp+18h],rsi
00000001`8000460b push    rdi
00000001`8000460c push    r12
00000001`8000460e push    r13
00000001`80004610 sub     rsp,20h
00000001`80004614 mov     rsi,[rsp+60h]     ; rsi = lParam
00000001`80004619 mov     rbp,r9            ; rbp = wParam
00000001`8000461c mov     ebx,r8d           ; ebx = message
00000001`8000461f mov     r13,rdx           ; r13 = hdlg
00000001`80004622 mov     rdi,rcx           ; rdi = this
00000001`80004625 cmp     r8d,2Bh           ; Q: WM_DRAWITEM?
00000001`80004629 jne     00000001`80004685 ; N: Skip
After the initial register spilling and saving, it checks if the message is
0x2B
:
WM_DRAWITEM
. That’s not particularly interesting to us, so let’s assume it’s not.
00000001`80004685 sub     ebx,2             ; Q: WM_DESTROY?
00000001`80004688 je      00000001`8000470f
Ooh, the
WM_
DESTROY
message is interesting. It’s probably going to restore the original window procedure in its
WM_
DESTROY
handler, and that’s where we hope to find the truncation.
00000001`8000470f mov     rcx,[rdi+110h]        ; rcx = something
00000001`80004716 movsxd  rbx,dword ptr [00000001`80039c50] ; rbx = something
00000001`8000471d mov     edx,668h              ; ecx = some number
00000001`80004722 call    [00000001`8002b4e0]   ; mystery function 4
00000001`80004728 mov     r8,rbx                ; r8 = something
00000001`8000472b mov     edx,0FFFFFFFCh        ; edx = -12
00000001`80004730 mov     rcx,rax               ; rcx = function 4 retval
00000001`80004733 call    [00000001`8002b4a0]   ; mystery function 1 again
On receipt of the
WM_
DESTROY
message, the code starts by getting something out of the
this
pointer (which we saw in the prologue was saved in
rdi
), and loads some other thing from a global variable.
Next, it calls mystery function
00000001`8002b4e0
with
0x668
as the second parameter. Not sure what that is, but we’ll keep it in mind.
Next, we set up for another function call, and this one we recognize:
00000001`8002b4a0
is the import address table entry for
SetWindowLongPtr
. We saw it in the static dialog procedure.
The parameters are the window handle that was obtained from mystery function 4, the constant
-12
, and the 32-bit value we loaded from
00000001`80039c50
. The mystery function 4 was probably
Get­Dlg­Item
. And since we figured out that the function being called is
SetWindowLongPtr
, the value
-12
is
GWLP_WNDPROC
.
The value being set is the third parameter, which was loaded by
movsxd dword ptr
, which is a 32-bit to 64-bit sign-extended load. This is a problem because the window procedure is a 64-bit value.
I bet they loaded the value incorrectly.
0:000> dp 00000001`80039c50 l1
00000001`80039c50  00007fff`924bbde0
Hey look, it’s the full 64-bit pointer we were supposed to have used, except we messed up and truncated the pointer.
The C++ source code probably looked like this:
SetWindowLongPtr(GetDlgItem(m_hdlg, 0x668),
    GWLP_WNDPROC, (LONG)g_originalWndProc);
The cast to
LONG
is what’s doing the truncation and sign extension. It should be a cast to
LONG_PTR
.
We can patch this into the binary after looking at the processor instruction encoding documentation.
The original instruction was
00000001`80004716 48631d33550300  movsxd  rbx,dword ptr [00000001`80039c50]
The documentation says that the encoding for
movxsd r64, r/m32
is “REX.W + 63 /r”.
What we want is
mov rbx, [00000001`80039c50]
, and the documentation says that the encoding for
mov r64, r/m64
is “REX.W + 8B /r”.
So let’s patch the
63
to
8b
.
0:000> eb 00000001`80004717 8b
0:000> u 00000001`80004716 l1
00000001`80004716 488b1d33550300  mov     rbx,qword ptr [00000001`80039c50]
This is literally a one-byte bug fix.
Next time, we’ll speculate on how this bug arose.
Bonus reading
:
The decoy control panel
.
¹ Back in the late 1990’s, we discovered a program that reverse-engineered the internal data structures of the Windows 95 property sheet manager to the point where instead of passing an
HPROPSHEETPAGE
that was created by the
Create­Property­Sheet­Page
function, it created fake
HPROPSHEETPAGE
s that it had constructed manually in memory. This made adding support for Unicode property sheets that much harder because the internal structure of
HPROPSHEETPAGE
s changed in order to support both ANSI and Unicode property sheet pages, and they were passing the old version. The property sheet manager has to recognize that it is being given a fake
HPROPSHEETPAGE
and convert it on the fly to a real one.
