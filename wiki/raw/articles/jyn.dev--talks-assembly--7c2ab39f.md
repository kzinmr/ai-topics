---
title: "Reverse Engineering"
url: "https://jyn.dev/talks/assembly/"
fetched_at: 2026-04-29T07:02:12.603390+00:00
source: "jyn.dev"
tags: [blog, raw]
---

# Reverse Engineering

Source: https://jyn.dev/talks/assembly/

Common x86 Instructions
mov/movq/movl
- move some data from {register,memory,immediate} to {register,memory}.
movl $0,%edi  # move 0 into index register
add
- add data to a register
addl $8, %edi  # add 8 to the index register
cmp
and
je
- Compare two values and jump if they're equal
loop:
 cmpl $10,%eax  # check if we hit the end
 je exit
 addl $1, %eax
 jmp loop
exit:
 movl $1,%eax
Common x86 Instructions
xor
- acts on two registers or register and immediate
xor %eax, %eax  # fast way to set eax to 0
push
and
pop
- store or load things onto the stack
pushl %eax  # save the contents of eax
mov $5, %eax  # do something with eax
pop %eax  # restore eax to former glory
Common x86 Instructions
call
and
ret
- function instructions
_start:
 call power
 mov %eax, %ebx  # return code
 movl $1, %eax   # syscall number
 syscall

power:
 movl 4(%esp), %ebx  # put first argument in %ebx
 movl 8(%esp), %ecx  # put second argument in %ecx
 movl $1,%eax  # result = 1
 ret
Common x86 Instructions
lea
- load effective address
lea    0x4(%rsp),%rcx
nop
- no operation
Addressing modes
Immediate:
mov $10, %eax
(assigning a constant to a variable)
Direct:
mov %esi, %eax
(assigning a variable to a variable)
Indirect:
mov (%esi), %eax
(dereferencing a pointer)
Offset:
mov 0x2000(%eax), %eax
(accessing an array, no pointer math)
Scaled offset:
mov 0x3113(,%eax,4), %ebx
(array indexing, pointer math)
Example
# printf.c:15:   size_t len = 0;
        movq    $0, -16(%rbp)   #, len
# printf.c:16:   fputs("Enter the password: ", stdout);
        movq    stdout(%rip), %rax      # stdout, stdout.0_1
        movq    %rax, %rcx      # stdout.0_1,
        movl    $20, %edx       #,
        movl    $1, %esi        #,
        leaq    .LC1(%rip), %rdi        #,
        call    fwrite@PLT      #
# printf.c:17:   getline(&line, &len, stdin);
        movq    stdin(%rip), %rdx       # stdin, stdin.1_2
        leaq    -16(%rbp), %rcx #, tmp93
        leaq    -24(%rbp), %rax #, tmp94
        movq    %rcx, %rsi      # tmp93,
        movq    %rax, %rdi      # tmp94,
        call    getline@PLT     #
# printf.c:18:   if (strcmp(line, "Magic super secret constant\n")) {
        movq    -24(%rbp), %rax # line, line.2_3
        leaq    .LC2(%rip), %rsi        #,
        movq    %rax, %rdi      # line.2_3,
        call    strcmp@PLT      #
        testl   %eax, %eax      # _4
        je      .L3     #,
# printf.c:19:     error();
        call    error   #
.L3:
# printf.c:21:   puts("You won!");
        leaq    .LC3(%rip), %rdi        #,
        call    puts@PLT        #
        movl    $0, %eax        #, _14
Common C idioms
if/then/else
while
argv
for
switch
recursion
If
Hint: look for
cmp
0000000000000864 <main>:
 864:   55                      push   %rbp
 865:   48 89 e5                mov    %rsp,%rbp
 868:   48 83 ec 20             sub    $0x20,%rsp
 86c:   64 48 8b 04 25 28 00    mov    %fs:0x28,%rax
 873:   00 00
 875:   48 89 45 f8             mov    %rax,-0x8(%rbp)
 879:   31 c0                   xor    %eax,%eax
 87b:   48 c7 45 f0 00 00 00    movq   $0x0,-0x10(%rbp)
 882:   00
 883:   48 8b 05 86 07 20 00    mov    0x200786(%rip),%rax        # 201010 <stdout@@GLIBC_2.2.5>
 88a:   48 89 c1                mov    %rax,%rcx
 88d:   ba 12 00 00 00          mov    $0x12,%edx
 892:   be 01 00 00 00          mov    $0x1,%esi
 897:   48 8d 3d fd 00 00 00    lea    0xfd(%rip),%rdi        # 99b <_IO_stdin_used+0x1b>
 89e:   e8 7d fe ff ff          callq  720 <fwrite@plt>
 8a3:   48 8b 05 76 07 20 00    mov    0x200776(%rip),%rax        # 201020 <stdin@@GLIBC_2.2.5>
 8aa:   48 8d 55 ec             lea    -0x14(%rbp),%rdx
 8ae:   48 8d 35 f9 00 00 00    lea    0xf9(%rip),%rsi        # 9ae <_IO_stdin_used+0x2e>
 8b5:   48 89 c7                mov    %rax,%rdi
 8b8:   b8 00 00 00 00          mov    $0x0,%eax
 8bd:   e8 1e fe ff ff          callq  6e0 <__isoc99_fscanf@plt>
 8c2:   8b 45 ec                mov    -0x14(%rbp),%eax
 8c5:   3d 8f a8 00 00          cmp    $0xa88f,%eax
 8ca:   74 05                   je     8d1 <main+0x6d>
 8cc:   e8 79 ff ff ff          callq  84a <error>
 8d1:   48 8d 3d d9 00 00 00    lea    0xd9(%rip),%rdi        # 9b1 <_IO_stdin_used+0x31>
 8d8:   e8 13 fe ff ff          callq  6f0 <puts@plt>
 8dd:   b8 00 00 00 00          mov    $0x0,%eax
 8e2:   48 8b 4d f8             mov    -0x8(%rbp),%rcx
 8e6:   64 48 33 0c 25 28 00    xor    %fs:0x28,%rcx
 8ed:   00 00
 8ef:   74 05                   je     8f6 <main+0x92>
 8f1:   e8 0a fe ff ff          callq  700 <__stack_chk_fail@plt>
 8f6:   c9                      leaveq
 8f7:   c3                      retq
 8f8:   0f 1f 84 00 00 00 00    nopl   0x0(%rax,%rax,1)
 8ff:   00
while
0x000000000000083b <+23>:    movl   $0x4,-0xc(%rbp)
                        ...
   0x0000000000000862 <+62>:    lea    -0x10(%rbp),%rax
   0x0000000000000866 <+66>:    mov    %rax,%rsi
   0x0000000000000869 <+69>:    lea    0x110(%rip),%rdi        # 0x980
   0x0000000000000870 <+76>:    mov    $0x0,%eax
   0x0000000000000875 <+81>:    callq  0x6c0 <__isoc99_scanf@plt>
   0x000000000000087a <+86>:    jmp    0x889 <main+101>   # check condition immmediately
   0x000000000000087c <+88>:    mov    -0x10(%rbp),%eax   # loop body
   0x000000000000087f <+91>:    add    $0x5,%eax
   0x0000000000000882 <+94>:    mov    %eax,-0x10(%rbp)
   0x0000000000000885 <+97>:    subl   $0x1,-0xc(%rbp)    # where have we seen this?
   0x0000000000000889 <+101>:   mov    -0x10(%rbp),%eax   # jump target
   0x000000000000088c <+104>:   cmp    $0x31,%eax         # while comparison
   0x000000000000088f <+107>:   jle    0x87c <main+88>    # goes backwards to loop
   0x0000000000000891 <+109>:   mov    -0x10(%rbp),%eax
   0x0000000000000894 <+112>:   cmp    $0x34,%eax
   0x0000000000000897 <+115>:   jne    0x89f <main+123>
   0x0000000000000899 <+117>:   cmpl   $0x0,-0xc(%rbp)    # two comparisons!
   0x000000000000089d <+121>:   je     0x8a4 <main+128>
   0x000000000000089f <+123>:   callq  0x80a <error>
   0x00000000000008a4 <+128>:   lea    0xd8(%rip),%rdi        # 0x983
   0x00000000000008ab <+135>:   callq  0x6a0 <puts@plt>
argv
a.k.a command-line arguments
0000000000000714 <main>:
 714:   55                      push   %rbp
 715:   48 89 e5                mov    %rsp,%rbp
 718:   48 83 ec 10             sub    $0x10,%rsp
 71c:   89 7d fc                mov    %edi,-0x4(%rbp)
 71f:   48 89 75 f0             mov    %rsi,-0x10(%rbp)
 723:   83 7d fc 02             cmpl   $0x2,-0x4(%rbp)
 727:   75 1e                   jne    747 <main+0x33>
 729:   48 8b 45 f0             mov    -0x10(%rbp),%rax
 72d:   48 83 c0 08             add    $0x8,%rax
 731:   48 8b 00                mov    (%rax),%rax
 734:   48 8d 35 c0 00 00 00    lea    0xc0(%rip),%rsi        # 7fb <_IO_stdin_used+0x1b>
 73b:   48 89 c7                mov    %rax,%rdi
 73e:   e8 7d fe ff ff          callq  5c0 <strcmp@plt>
 743:   85 c0                   test   %eax,%eax
 745:   74 05                   je     74c <main+0x38>
 747:   e8 ae ff ff ff          callq  6fa <error>
 74c:   48 8d 3d bf 00 00 00    lea    0xbf(%rip),%rdi        # 812 <_IO_stdin_used+0x32>
 753:   e8 58 fe ff ff          callq  5b0 <puts@plt>
 758:   b8 00 00 00 00          mov    $0x0,%eax
 75d:   c9                      leaveq
 75e:   c3                      retq
 75f:   90                      nop
for
Guess what? It's the same as a while loop
839:   31 c0                   xor    %eax,%eax
 83b:   48 8b 05 ce 07 20 00    mov    0x2007ce(%rip),%rax        # 201010 <stdout@@GLIBC_2.2.5>
 842:   48 89 c1                mov    %rax,%rcx
 845:   ba 14 00 00 00          mov    $0x14,%edx
 84a:   be 01 00 00 00          mov    $0x1,%esi
 84f:   48 8d 3d 15 01 00 00    lea    0x115(%rip),%rdi        # 96b <_IO_stdin_used+0x1b>
 856:   e8 85 fe ff ff          callq  6e0 <fwrite@plt>
 85b:   48 8d 45 f0             lea    -0x10(%rbp),%rax
 85f:   48 89 c6                mov    %rax,%rsi
 862:   48 8d 3d 17 01 00 00    lea    0x117(%rip),%rdi        # 980 <_IO_stdin_used+0x30>
 869:   b8 00 00 00 00          mov    $0x0,%eax
 86e:   e8 4d fe ff ff          callq  6c0 <__isoc99_scanf@plt>
 873:   c7 45 f4 04 00 00 00    movl   $0x4,-0xc(%rbp)
 87a:   eb 0d                   jmp    889 <main+0x65>
 87c:   8b 45 f0                mov    -0x10(%rbp),%eax
 87f:   83 c0 05                add    $0x5,%eax
 882:   89 45 f0                mov    %eax,-0x10(%rbp)
 885:   83 6d f4 01             subl   $0x1,-0xc(%rbp)
 889:   83 7d f4 00             cmpl   $0x0,-0xc(%rbp)
 88d:   7f ed                   jg     87c <main+0x58>
 88f:   8b 45 f0                mov    -0x10(%rbp),%eax
 892:   83 f8 34                cmp    $0x34,%eax
 895:   74 05                   je     89c <main+0x78>
 897:   e8 6e ff ff ff          callq  80a <error>
 89c:   48 8d 3d e0 00 00 00    lea    0xe0(%rip),%rdi        # 983 <_IO_stdin_used+0x33>
 8a3:   e8 f8 fd ff ff          callq  6a0 <puts@plt>
 8a8:   b8 00 00 00 00          mov    $0x0,%eax
switch
Same as a series of if/else statements, right?
71b:   48 89 44 24 08          mov    %rax,0x8(%rsp)
 720:   31 c0                   xor    %eax,%eax
 722:   e8 99 ff ff ff          callq  6c0 <fputs@plt>
 727:   48 8d 74 24 04          lea    0x4(%rsp),%rsi
 72c:   48 8d 3d 5d 02 00 00    lea    0x25d(%rip),%rdi        # 990 <_IO_stdin_used+0x30>
 733:   31 c0                   xor    %eax,%eax
 735:   e8 96 ff ff ff          callq  6d0 <__isoc99_scanf@plt>
 73a:   8b 44 24 04             mov    0x4(%rsp),%eax
 73e:   83 f8 01                cmp    $0x1,%eax
 741:   74 22                   je     765 <main+0x65>
 743:   7f 0d                   jg     752 <main+0x52>
 745:   85 c0                   test   %eax,%eax
 747:   48 8d 3d 45 02 00 00    lea    0x245(%rip),%rdi        # 993 <_IO_stdin_used+0x33>
 74e:   74 31                   je     781 <main+0x81>
 750:   eb 28                   jmp    77a <main+0x7a>
 752:   83 f8 02                cmp    $0x2,%eax
 755:   74 1a                   je     771 <main+0x71>
 757:   83 f8 03                cmp    $0x3,%eax
 75a:   48 8d 3d 64 02 00 00    lea    0x264(%rip),%rdi        # 9c5 <_IO_stdin_used+0x65>
 761:   74 1e                   je     781 <main+0x81>
 763:   eb 15                   jmp    77a <main+0x7a>
 765:   48 8d 3d 36 02 00 00    lea    0x236(%rip),%rdi        # 9a2 <_IO_stdin_used+0x42>
 76c:   e8 2f ff ff ff          callq  6a0 <puts@plt>
 771:   48 8d 3d 40 02 00 00    lea    0x240(%rip),%rdi        # 9b8 <_IO_stdin_used+0x58>
 778:   eb 07                   jmp    781 <main+0x81>
 77a:   48 8d 3d 4d 02 00 00    lea    0x24d(%rip),%rdi        # 9ce <_IO_stdin_used+0x6e>
 781:   e8 1a ff ff ff          callq  6a0 <puts@plt>
 786:   31 c0                   xor    %eax,%eax
 788:   48 8b 54 24 08          mov    0x8(%rsp),%rdx
 78d:   64 48 33 14 25 28 00    xor    %fs:0x28,%rdx
 794:   00 00
 796:   74 05                   je     79d <main+0x9d>
 798:   e8 13 ff ff ff          callq  6b0 <__stack_chk_fail@plt>
 79d:   48 83 c4 18             add    $0x18,%rsp
 7a1:   c3                      retq
BUT
could be a jump to an offset table
*
0x0000000000400f29 <+28>:    mov    $0x40258f,%esi
   0x0000000000400f2e <+33>:    callq  0x400bb0 <__isoc99_sscanf@plt>
   0x0000000000400f33 <+38>:    cmp    $0x1,%eax
   0x0000000000400f36 <+41>:    jg     0x400f3d <phase_3+48>
   0x0000000000400f38 <+43>:    callq  0x4013f2 <explode_bomb>
   0x0000000000400f3d <+48>:    cmpl   $0x7,(%rsp)
   0x0000000000400f41 <+52>:    ja     0x400f7e <phase_3+113>
   0x0000000000400f43 <+54>:    mov    (%rsp),%eax
   0x0000000000400f46 <+57>:    jmpq   *0x402400(,%rax,8)
   0x0000000000400f4d <+64>:    mov    $0x1e2,%eax
   0x0000000000400f52 <+69>:    jmp    0x400f8f <phase_3+130>
   0x0000000000400f54 <+71>:    mov    $0x318,%eax
   0x0000000000400f59 <+76>:    jmp    0x400f8f <phase_3+130>
   0x0000000000400f5b <+78>:    mov    $0x8d,%eax
   0x0000000000400f60 <+83>:    jmp    0x400f8f <phase_3+130>
   0x0000000000400f62 <+85>:    mov    $0x2f7,%eax
   0x0000000000400f67 <+90>:    jmp    0x400f8f <phase_3+130>
   0x0000000000400f69 <+92>:    mov    $0x2e9,%eax
   0x0000000000400f6e <+97>:    jmp    0x400f8f <phase_3+130>
   0x0000000000400f70 <+99>:    mov    $0x225,%eax
   0x0000000000400f75 <+104>:   jmp    0x400f8f <phase_3+130>
   0x0000000000400f77 <+106>:   mov    $0xdb,%eax
   0x0000000000400f7c <+111>:   jmp    0x400f8f <phase_3+130>
   0x0000000000400f7e <+113>:   callq  0x4013f2 <explode_bomb>
   0x0000000000400f83 <+118>:   mov    $0x0,%eax
   0x0000000000400f88 <+123>:   jmp    0x400f8f <phase_3+130>
   0x0000000000400f8a <+125>:   mov    $0x3b9,%eax
   0x0000000000400f8f <+130>:   cmp    0x4(%rsp),%eax
   0x0000000000400f93 <+134>:   je     0x400f9a <phase_3+141>
   0x0000000000400f95 <+136>:   callq  0x4013f2 <explode_bomb>
   0x0000000000400f9a <+141>:   mov    0x8(%rsp),%rax
   0x0000000000400f9f <+146>:   xor    %fs:0x28,%rax
   0x0000000000400fa8 <+155>:   je     0x400faf <phase_3+162>
   0x0000000000400faa <+157>:   callq  0x400b00 <__stack_chk_fail@plt>
   0x0000000000400faf <+162>:   add    $0x18,%rsp
   0x0000000000400fb3 <+166>:   retq
More info
*disclaimer: I have not been able to replicate this output with gcc
Recursion
Good news: This isn't harder than recursion in any other language
Bad news: This is as hard as recursion in any other language
000000000000068a <recursive>:
 68a:   55                      push   %rbp
 68b:   48 89 e5                mov    %rsp,%rbp
 68e:   53                      push   %rbx
 68f:   48 83 ec 18             sub    $0x18,%rsp
 693:   89 7d ec                mov    %edi,-0x14(%rbp)
 696:   83 7d ec 00             cmpl   $0x0,-0x14(%rbp)
 69a:   74 06                   je     6a2 <recursive+0x18>
 69c:   83 7d ec 01             cmpl   $0x1,-0x14(%rbp)
 6a0:   75 07                   jne    6a9 <recursive+0x1f>
 6a2:   b8 01 00 00 00          mov    $0x1,%eax
 6a7:   eb 1e                   jmp    6c7 <recursive+0x3d>
 6a9:   8b 45 ec                mov    -0x14(%rbp),%eax
 6ac:   83 e8 01                sub    $0x1,%eax
 6af:   89 c7                   mov    %eax,%edi
 6b1:   e8 d4 ff ff ff          callq  68a <recursive>
 6b6:   89 c3                   mov    %eax,%ebx
 6b8:   8b 45 ec                mov    -0x14(%rbp),%eax
 6bb:   83 e8 02                sub    $0x2,%eax
 6be:   89 c7                   mov    %eax,%edi
 6c0:   e8 c5 ff ff ff          callq  68a <recursive>
 6c5:   01 d8                   add    %ebx,%eax
 6c7:   48 83 c4 18             add    $0x18,%rsp
 6cb:   5b                      pop    %rbx
 6cc:   5d                      pop    %rbp
 6cd:   c3                      retq

00000000000006ce <main>:
 6ce:   55                      push   %rbp
 6cf:   48 89 e5                mov    %rsp,%rbp
 6d2:   48 83 ec 10             sub    $0x10,%rsp
 6d6:   89 7d fc                mov    %edi,-0x4(%rbp)
 6d9:   48 89 75 f0             mov    %rsi,-0x10(%rbp)
 6dd:   8b 45 fc                mov    -0x4(%rbp),%eax
 6e0:   89 c7                   mov    %eax,%edi
 6e2:   e8 a3 ff ff ff          callq  68a <recursive>
 6e7:   83 f8 37                cmp    $0x37,%eax
 6ea:   75 37                   jne    723 <main+0x55>
 6ec:   48 8b 45 f0             mov    -0x10(%rbp),%rax
 6f0:   48 83 c0 08             add    $0x8,%rax
 6f4:   48 8b 00                mov    (%rax),%rax
 6f7:   ba 0a 00 00 00          mov    $0xa,%edx
 6fc:   be 00 00 00 00          mov    $0x0,%esi
 701:   48 89 c7                mov    %rax,%rdi
 704:   e8 57 fe ff ff          callq  560 <strtol@plt>
 709:   89 c7                   mov    %eax,%edi
 70b:   e8 7a ff ff ff          callq  68a <recursive>
 710:   83 f8 08                cmp    $0x8,%eax
 713:   75 0e                   jne    723 <main+0x55>
 715:   48 8d 3d a8 00 00 00    lea    0xa8(%rip),%rdi        # 7c4 <_IO_stdin_used+0x4>
 71c:   e8 2f fe ff ff          callq  550 <puts@plt>
 721:   eb 0c                   jmp    72f <main+0x61>
 723:   48 8d 3d ac 00 00 00    lea    0xac(%rip),%rdi        # 7d6 <_IO_stdin_used+0x16>
 72a:   e8 21 fe ff ff          callq  550 <puts@plt>
 72f:   b8 00 00 00 00          mov    $0x0,%eax
 734:   c9                      leaveq
 735:   c3                      retq
