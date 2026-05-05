---
title: "What Every C Programmer Should Know About Undefined Behavior #3/3"
url: "https://blog.llvm.org/2011/05/what-every-c-programmer-should-know_21.html"
fetched_at: 2026-05-05T07:01:43.810188+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# What Every C Programmer Should Know About Undefined Behavior #3/3

Source: https://blog.llvm.org/2011/05/what-every-c-programmer-should-know_21.html

Some cases of undefined behavior are silently transformed into implicitly trapping operations if there is a good way to do that. For example, with Clang, this C++ function:
int *foo(long x) {
return new int[x];
}
compiles into this X86-64 machine code:
__Z3fool:
movl $4, %ecx
movq %rdi, %rax
mulq %rcx
movq $-1, %rdi        # Set the size to -1 on overflow
cmovnoq %rax, %rdi    # Which causes 'new' to throw std::bad_alloc
jmp __Znam
instead of the code GCC produces:
__Z3fool:
salq $2, %rdi
jmp __Znam             # Security bug on overflow!
The difference here is that we've decided to invest a few cycles in preventing a potentially
serious integer overflow bug
that can lead to buffer overflows and exploits (operator new is typically fairly expensive, so the overhead is almost never noticable). The GCC folks have been aware of this
since at least 2005
but haven't fixed this at the time of this writing.
