---
title: "How do functions like alloca allocate memory from the stack?"
url: "https://devblogs.microsoft.com/oldnewthing/20260817-40/?p=112617"
fetched_at: 2026-08-18T10:03:44.507137+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# How do functions like alloca allocate memory from the stack?

Source: https://devblogs.microsoft.com/oldnewthing/20260817-40/?p=112617

A little while ago, I talked about
how compilers ensure that large stack allocations do not skip over the guard page
. Shawn Van Ness was curious
how this works with
_alloca
. “Does it do the necessary
_chkstk()
probing?”
Yes, the
_alloca()
function calls the same
_chkstk()
function to probe the stack before adjusting the stack pointer for the allocated memory.
Here’s an artificial example:
#include <malloc.h>

void consume(void*,void*);

void f(int n)
{
    char buffer[16384];
    consume(alloca(n), buffer);
}
On x86-64, this results in
push    rbp
        mov     eax, 16416          ; probe for local frame
        call    __chkstk
        sub     rsp, rax            ; create local frame

        lea     rbp, [rsp+32]

        movsxd  rax, ecx            ; n
        lea     rcx, [rax+15]       ; round up to multiple of 16
        and     rcx, -16

        mov     rax, rcx            ; special __chkstk calling convention
        call    __chkstk
        sub     rsp, rcx            ; allocate n bytes

        lea     rdx, [rbp]          ; rdx -> buffer
        lea     rcx, [rsp+32]       ; rcx -> alloca'd memory
        call    consume

        lea     rsp, [rbp+16384]    ; clean up local frame
        pop     rbp
        ret     0
Observe that the same
__chkstk
function is used both for performing the initial stack probe when creating the local frame as well as for the
alloca()
.
