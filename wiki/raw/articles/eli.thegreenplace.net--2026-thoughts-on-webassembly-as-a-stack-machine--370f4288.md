---
title: "Thoughts on WebAssembly as a stack machine"
url: "https://eli.thegreenplace.net/2026/thoughts-on-webassembly-as-a-stack-machine/"
fetched_at: 2026-04-30T07:00:41.813037+00:00
source: "eli.thegreenplace.net"
tags: [blog, raw]
---

# Thoughts on WebAssembly as a stack machine

Source: https://eli.thegreenplace.net/2026/thoughts-on-webassembly-as-a-stack-machine/

This week the article
Wasm is not quite a stack machine
has been
making the rounds and has caught my eye. The post claims that WASM is not a pure
stack machine because it has locals and is missing some stack manipulation
operations like
dup
and
swap
.
While I don't necessarily disagree, IMHO it's a bit of a semantic
discussion because - to the best of my knowledge - there is no
formal
definition of what is a stack machine. Wikipedia, for example,
says:
[...], a stack machine is a computer processor or a process virtual machine in
which the primary interaction is moving short-lived temporary values to and
from a push-down stack.
WASM certainly fits this definition; the
primary
interaction is through the
stack, though WASM is augmented with an infinite register file (locals).
The more purist stack machines like Forth are only limited to the stack and a
memory (pointers into which are managed on the stack); WASM has these too, plus
the registers.
Speaking of Forth, the mention of
dup
reminded me of my own impressions
of programming in that language, documented in my post about
implementing Forth in Go and C
. There,
I highlighted the following essential library function for Forth; it adds an
addend to a value stored in memory.
:
+!
( addend addr -- )
tuck
( addr addend addr )
@
( addr addend value-at-addr )
+
( addr updated-value )
swap
( updated-value addr )
!
;
And lamented how difficult it is to understand such code without the
detailed stack view in comments alongside it.
I find it much simpler to reason about this WASM code:
(
func
(
export
"add_to_byte"
)
(
param
$addr
i32
)
(
param
$delta
i32
)
(
i32.store8
(
local.get
$addr
)
(
i32.add
(
i32.load8_u
(
local.get
$addr
))
(
local.get
$delta
)))
)
You may say this is cheating because folded WASM instructions help readability
and they're just syntactic sugar; OK, here's the linear code:
local.get
$addr
local.get
$addr
i32.load8_u
local.get
$delta
i32.add
i32.store8
It's still very readable, because - while the stack is used for all the
calculations and actual commands - some of the data lives in named "registers"
instead of on the stack. So we don't need all those tuck-swap contortions to get
things into the right order.
One might worry about the duplicated
local.get $addr
; wouldn't a real
dup
be better? Well, not in terms of readability, as we've already discussed. How
about performance? Since the stack VM is just an abstraction and the underlying
CPUs executing this code are register machines anyway, the answer is no - it
doesn't matter at all.
Modern compiler engineers were forged in the fires of C and its descendants;
arbitrary control flow, arbitrary register and memory access, anything goes.
Compilers are quite sophisticated. Let's see how
wasmtime
compiles our
add_to_byte
to native code (using
wasmtime explore
with its
default
opt-level=2
); comments are added by me:
// Prologue
push
rbp
mov
rbp
,
rsp
// wasmtime's VM context pointer lives in rdi; 0x38 is likely its offset
// to the default linear memory. Therefore, r10 will hold the base address
// of the linear memory buffer
mov
r10
,
qword
ptr
[
rdi
+
0x38
]
// The first parameter ($addr) is in edx; since WASM values are i32, it's
// zero-extended into the 64-bit r11 by copying into r11d
mov
r11d
,
edx
// r10+r11 is memory[$addr]; this loads the current value into rsi
// (zero-extending from 8 bits)
movzx
rsi
,
byte
ptr
[
r10
+
r11
]
// ecx is the first parameter ($delta); this adds the addend to the
// current value
add
esi
,
ecx
// Store cur_value+addend back into memory[$addr]
mov
byte
ptr
[
r10
+
r11
],
sil
// Epilogue
mov
rsp
,
rbp
pop
rbp
ret
This is pretty much the code we'd expect to be emitted for the C statement
mem[addr] += addend
, or if we were writing x86-64 assembly by hand. The
compiler had no difficulty figuring out that two consecutive loads from
the same WASM local produce the same value and do not - in fact - have to be
duplicated. The WASM model makes it rather easy, because you can't alias locals;
as long as there are no intervening writes into the same local, multiple reads
are known to produce the same value (redundant load elimination).
