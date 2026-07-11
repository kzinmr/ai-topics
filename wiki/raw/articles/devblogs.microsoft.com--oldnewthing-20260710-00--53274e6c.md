---
title: "The case of the mysterious changes to integers when there shouldn't have been any code generation effect"
url: "https://devblogs.microsoft.com/oldnewthing/20260710-00/?p=112514"
fetched_at: 2026-07-11T07:00:47.659093+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# The case of the mysterious changes to integers when there shouldn't have been any code generation effect

Source: https://devblogs.microsoft.com/oldnewthing/20260710-00/?p=112514

A colleague made some code changes that should not have had any effect on the generated binary. Specifically, they migrated from
the
NDIS_
STRING_
CONST
macro
to
the more type-safe
RTL_
CONSTANT_
STRING
macro
. The two macros produce the same results at the end of the day, so the expectation was that this would not result in any change to the binary.
But they found a change to the binary.
Specifically, four functions changed, and what is particularly strange is that none of them involved the macro changes. Three of the functions are in one source file, and the fourth is in a source file that wasn’t even touched!
The changes looked like this:
Before
After
contoso!Evt­Wdf­Widget­Context­Cleanup
mov rax, [contoso!WdfFunctions_01031]
lea rcx, [??_C@__0DK@MPBCIIPN@...]
mov [rsp+20h], rcx
mov r9d,
62Bh
mov r8d, 52467443h
mov rcx, [contoso!WdfDriverGlobals]
mov rdx, rbx
mov rax, [rax+670h]
call __guard_dispatch_call
mov rax, [contoso!WdfFunctions_01031]
lea rcx, [??_C@__0DK@MPBCIIPN@...]
mov [rsp+20h], rcx
mov r9d,
62Ah
mov r8d, 52467443h
mov rcx, [contoso!WdfDriverGlobals]
mov rdx, rbx
mov rax, [rax+670h]
call __guard_dispatch_call
contoso!Function2
mov rax, [contoso!WdfFunctions_01031]
lea rcx, [??_C@__0DK@MPBCIIPN@...]
mov [rsp+20h], rcx
mov r9d,
616h
mov rcx, [contoso!WdfDriverGlobals]
mov r8d, 52467443h
mov rdx, rdi
mov rax, [rax+668h]
call __guard_dispatch_call
mov rax, [contoso!WdfFunctions_01031]
lea rcx, [??_C@__0DK@MPBCIIPN@...]
mov [rsp+20h], rcx
mov r9d,
615h
mov rcx, [contoso!WdfDriverGlobals]
mov r8d, 52467443h
mov rdx, rdi
mov rax, [rax+668h]
call __guard_dispatch_call
contoso!Function3
mov rax, [contoso!WdfFunctions_01031]
lea rcx, [??_C@__0DK@MPBCIIPN@...]
mov [r11-20h], rcx
xor r8d, r8d
mov rcx, [contoso!WdfDriverGlobals]
mov r9d,
35Dh
mov rax, [rax+0DB0h]
call __guard_dispatch_call
mov rax, [contoso!WdfFunctions_01031]
lea rcx, [??_C@__0DK@MPBCIIPN@...]
mov [r11-20h], rcx
xor r8d, r8d
mov rcx, [contoso!WdfDriverGlobals]
mov r9d,
35Ch
mov rax, [rax+0DB0h]
call __guard_dispatch_call
contoso!Function4
mov rax, [contoso!WdfFunctions_01031]
lea rcx, [??_C@__0DK@MPBCIIPN@...]
mov rdx, [rbp+8]
mov r9d,
377h
mov [rsp+20h], rcx
mov r8d, 49507443h
mov rcx, [contoso!WdfDriverGlobals]
mov rax, [rax+0DB8h]
call __guard_dispatch_call
mov rax, [contoso!WdfFunctions_01031]
lea rcx, [??_C@__0DK@MPBCIIPN@...]
mov rdx, [rbp+8]
mov r9d,
376h
mov [rsp+20h], rcx
mov r8d, 49507443h
mov rcx, [contoso!WdfDriverGlobals]
mov rax, [rax+0DB8h]
call __guard_dispatch_call
In all of the cases, the change is that a single integer changed to a value one smaller.
My colleague asked an LLM to explain this change, and it suggested that the changes were related to control flow guard metadata. Does this make sense?
It didn’t make sense to me, on two points. First, for the guard dispatch call, the only parameter to control flow guard is the
rax
register, which is the function being checked. All the other registers contain the parameters to the called function. Since the changes are to the
r9d
register, they are not related to control flow guard.
Second, the control flow guard metadata is not stored in code. It’s stored
as a data block inside the binary
.
So what are we seeing?
I took a look a
Evt­Wdf­Widget­Context­Cleanup
.
void EvtWdfWidgetContextCleanup(_In_ WDFOBJECT Object)
{
    auto widgetContext = GetContextFromWidgetHandle(Object);
    if (widgetContext->NeedsDereference)
    {
        widgetContext->NeedsDereference = FALSE;
        WdfObjectDereferenceWithTag(Object, CONTOSO_WIDGET_TAG);
    }
}
The compiler points to the
Wdf­Object­Dereference­With­Tag
as the location of the change. And we see that
it is defined as a macro
:
#define WdfObjectDereferenceWithTag(Handle, Tag) \
        WdfObjectDereferenceActual(Handle, Tag, __LINE__, __FILE__)
which is itself
an inline function:
_IRQL_requires_max_(DISPATCH_LEVEL)
VOID
FORCEINLINE
WdfObjectReferenceActual(
    _In_
    WDFOBJECT Handle,
    _In_opt_
    PVOID Tag,
    _In_
    LONG Line,
    _In_z_
    PCCH File
    )
{
    ((PFN_WDFOBJECTREFERENCEACTUAL) WdfFunctions[WdfObjectReferenceActualTableIndex])
        (WdfDriverGlobals, Handle, Tag, Line, File);
}
The last little detail is that
WdfFunctions
is a macro that expands to
WdfFunctions_01031
. The WDF header files give each version a unique name so that mismatched versions lead to a linker error rather than undefined behavior at runtime.
Now we can see how this code maps to the compiler output.
mov rax, [contoso!WdfFunctions_01031]   ; WdfFunctions
    lea rcx, [??_C@__0DK@MPBCIIPN@...]      ; Address of something
    mov [rsp+20h], rcx                      ; is the File parameter
    mov r9d, 62Bh                           ; Line parameter
    mov r8d, 52467443h                      ; Tag parameter
    mov rcx, [contoso!WdfDriverGlobals]     ; hard-coded parameter
    mov rdx, rbx                            ; Handle parameter
    mov rax, [rax+670h]                     ; Load the function pointer
    call __guard_dispatch_call              ; Validate and call¹
So the value that changed is the
line number
.
I went back to the pull request and observed that the pull requested deleted a line from the source file.
#include <strsafe.h>
#include "stringutils.h"
Part of the pull request included deleting the no-longer-needed header because it contained a private definition of the
NDIS_
STRING_
CONST
macro, which the code no longer uses.
Deleting a line from the source file causes all the line numbers to shift by one!
So what they were seeing was just a change to the line numbers. No change in functionality.
If they really wanted to make this a “no binary effect” change, they could replace the
#include "stringutils.h
with a comment or just leave it as a blank line.
Or they could just accept that line numbers can change when you change lines.
Bonus chatter
: But wait, I said that three of the changes were in one file, the one with the deleted line, but a fourth was in a file that didn’t change at all. What’s that about?
The fourth function contained a call to a function in the modified file, and link-time code generation decided to inline that call. The changed line number propagated into the inline function and resulted in a code generation change in a file that wasn’t even affected by the pull request.
¹ Recall that
in the validate-and-call pattern
, the function pointer is passed in the
rax
register, and everthing else is set up as if you were calling the function yourself.
