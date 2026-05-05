---
title: "DragonFFI: FFI/JIT for the C language using Clang/LLVM"
url: "https://blog.llvm.org/2018/03/dragonffi-ffijit-for-c-language-using.html"
fetched_at: 2026-05-05T07:01:38.073710+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# DragonFFI: FFI/JIT for the C language using Clang/LLVM

Source: https://blog.llvm.org/2018/03/dragonffi-ffijit-for-c-language-using.html

DragonFFI: FFI/JIT for the C language using Clang/LLVM
By Adrien Guinet
Mar 13, 2018
#Clang
,
#llvm
15 minute read
Introduction
A
foreign function interface
is "a mechanism by which a program written in one programming language can call routines or make use of services written in another".
In the case of DragonFFI, we expose a library that allows calling C functions and using C structures from any languages. Basically, we want to be able to do this, let's say in Python:
import
pydffi
CU
=
pydffi
.
FFI
()
.
cdef
(
"int puts(const char* s);"
);
CU
.
funcs
.
puts
(
"hello world!"
)
or, in a more advanced way, for instance to use
libarchive
directly from Python:
import
pydffi
pydffi
.
dlopen
(
"/path/to/libarchive.so"
)
CU
=
pydffi
.
FFI
()
.
cdef
(
"#include <archive.h>"
)
a
=
funcs
.
archive_read_new
()
assert
a
...
This blog post presents related works, their drawbacks, then how Clang/LLVM is used to circumvent these drawbacks, the inner working of DragonFFI and further ideas.
The code of the project is available on GitHub:
https://github.com/aguinet/dragonffi
. Python 2/3 wheels are available for Linux/OSX x86/x64. Python 3.6 wheels are available for Windows x64. On all these architectures, just use:
$ pip install pydffi
and play with it :)
See below for more information.
Related work
libffi
is the reference library that provides a FFI for the C language.
cffi
is a Python binding around this library that also uses
PyCParser
to be able to easily declare interfaces and types. Both these libraries have limitations, among them:
libffi
does not support the Microsoft x64 ABI under Linux x64. It isn't that trivial to add a new ABI (hand-written ABI, get the ABI right, ...), while a lot of effort have already been put into compilers to get these ABIs right.
PyCParser
only supports a very limited subset of C (no includes, function attributes, ...).
Moreover, in 2014, Jordan Rose and John McCall from Apple made a
talk
at the LLVM developer meeting of San José about how Clang can be used for C interoperability. This talk also shows various ABI issues, and has been a source of inspiration for DragonFFI at the beginning.
Somehow related, Sean Callanan, who worked on
lldb
, gave a
talk
in 2017 at the LLVM developer meeting of San José on how we could use parts of Clang/LLVM to implement some kind of
eval()
for C++. What can be learned from this talk is that debuggers like
lldb
must also be able to call an arbitrary C function, and uses debug information among other things to solve it (what we also do, see below :)).
DragonFFI is based on Clang/LLVM, and thanks to that it is able to get around these issues:
it uses Clang to parse header files, allowing direct usage of a C library headers without adaptation;
it support as many calling conventions and function attributes as Clang/LLVM do;
as a bonus, Clang and LLVM allows on-the-fly compilation of C functions, without relying on the presence of a compiler on the system (you still need the headers of the system's libc thought, or MSVCRT headers under Windows);
and this is a good way to have fun with Clang and LLVM! :)
Let's dive in!
Creating an FFI library for C
Supporting C ABIs
A C function is always compiled for a given C ABI. The C ABI isn't defined per the official C standards, and is system/architecture-dependent. Lots of things are defined by these ABIs, and it can be quite error prone to implement.
To see how ABIs can become complex, let's compile this C code:
typedef
struct
{
short
a
;
int
b
;
}
A
;
void
print_A
(
A
s
)
{
printf
(
"%d %d
\n
"
,
s
.
a
,
s
.
b
);
}
Compiled for Linux x64, it gives this LLVM IR:
target
datalayout
=
"e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target
triple
=
"x86_64-pc-linux-gnu"
@.str
=
private
unnamed_addr
constant
[
7
x
i8
]
c
"%d %d\0A\00"
,
align
1
define
void
@print_A
(
i64
)
local_unnamed_addr
{
%2
=
trunc
i64
%0
to
i32
%3
=
lshr
i64
%0
,
32
%4
=
trunc
i64
%3
to
i32
%5
=
shl
i32
%2
,
16
%6
=
ashr
exact
i32
%5
,
16
%7
=
tail
call
i32
(
i8
*,
...)
@printf
(
i8
*
getelementptr
inbounds
([
7
x
i8
],
[
7
x
i8
]*
@.str
,
i64
0
,
i64
0
),
i32
%6
,
i32
%4
)
ret
void
}
What happens here is what is called
structure coercion
. To optimize some function calls, some ABIs pass structure values through registers. For instance, an
llvm::ArrayRef
object, which is basically a structure with a pointer and a size (see
https://github.com/llvm-mirror/llvm/blob/release_60/include/llvm/ADT/ArrayRef.h#L51
), is passed through registers (though this optimization isn't guaranteed by any standard).
It is important to understand that ABIs are complex things to implement and we don't want to redo this whole work by ourselves, particularly when LLVM/Clang already know how.
Finding the right type abstraction
We want to list every types that is used in a parsed C file. To achieve that goal, various information are needed, among which:
the function types, and their calling convention
for structures: field offsets and names
for union/enums: field names (and values)
On one hand, we have seen in the previous section that the LLVM IR is too Low Level (as in
Low Level
Virtual Machine) for this. On the other hand, Clang's AST is too high level. Indeed, let's print the Clang AST of the code above:
[
...
]
|
-RecordDecl 0x5561d7f9fc20 <a.c:1:9, line:4:1> line:1:9 struct definition
|
|
-FieldDecl 0x5561d7ff4750 <line:2:3, col:9> col:9 referenced a
'short'
|
`
-FieldDecl 0x5561d7ff47b0 <line:3:3, col:7> col:7 referenced b
'int'
We can see that there is no information about the structure layout (padding, ...). There's also no information about the size of standard C types. As all of this depends on the backend used, it is not surprising that these informations are not present in the AST.
The right abstraction appears to be the LLVM metadata produced by Clang to emit DWARF or PDB structures. They provide structure fields offset/name, various basic type descriptions, and function calling conventions. Exactly what we need! For the example above, this gives (at the LLVM IR level, with some inline comments):
target
triple
=
"x86_64-pc-linux-gnu"
%struct.A
=
type
{
i16
,
i32
}
@.str
=
private
unnamed_addr
constant
[
7
x
i8
]
c
"%d %d\0A\00"
,
align
1
define
void
@print_A
(
i64
)
local_unnamed_addr
!dbg
!7
{
%2
=
trunc
i64
%0
to
i32
%3
=
lshr
i64
%0
,
32
%4
=
trunc
i64
%3
to
i32
tail
call
void
@llvm.dbg.value
(
metadata
i32
%4
,
i64
0
,
metadata
!18
,
metadata
!19
),
!dbg
!20
tail
call
void
@llvm.dbg.declare
(
metadata
%struct.A
*
undef
,
metadata
!18
,
metadata
!21
),
!dbg
!20
%5
=
shl
i32
%2
,
16
,
!dbg
!22
%6
=
ashr
exact
i32
%5
,
16
,
!dbg
!22
%7
=
tail
call
i32
(
i8
*,
...)
@printf
(
i8
*
getelementptr
inbounds
([...]
@.str
,
i64
0
,
i64
0
),
i32
%6
,
i32
%4
),
!dbg
!23
ret
void
,
!dbg
!24
}
[...]
!7
=
distinct
!DISubprogram
(
name:
"print_A"
,
scope:
!1
,
file:
!1
,
line:
6
,
type:
!8
,
[...]
,
variables:
!17
)
!8
=
!DISubroutineType
(
types:
!9
)
!9
=
!{
null
,
!10
}
!10
=
!DIDerivedType
(
tag:
DW_TAG_typedef
,
name:
"A"
,
file:
!1
,
line:
4
,
baseType:
!11
)
!11
=
distinct
!DICompositeType
(
tag:
DW_TAG_structure_
type
,
file:
!1
,
line:
1
,
size:
64
,
elements:
!12
)
!12
=
!{
!13
,
!15
}
!13
=
!DIDerivedType
(
tag:
DW_TAG_member
,
name:
"a"
,
scope:
!11
,
file:
!1
,
line:
2
,
baseType:
!14
,
size:
16
)
!14
=
!DIBasicType
(
name:
"short"
,
size:
16
,
encoding:
DW_ATE_signed
)
!15
=
!DIDerivedType
(
tag:
DW_TAG_member
,
name:
"b"
,
scope:
!11
,
file:
!1
,
line:
3
,
baseType:
!16
,
size:
32
,
offset:
32
)
!16
=
!DIBasicType
(
name:
"int"
,
size:
32
,
encoding:
DW_ATE_signed
)
[...]
Internals
DragonFFI first parses the debug information included by Clang in the LLVM IR it produces, and creates a custom type system to represent the various function types, structures, enumerations and typedefs of the parsed C file. This custom type system has been created for two reasons:
create a type system that gathers only the necessary informations from the metadata tree (we don't need the whole debug informations)
make the public headers of the DragonFFI library free from any LLVM headers (so that the whole LLVM headers aren't needed to use the library)
Once we've got this type system, the DragonFFI API for calling C functions is this one:
DFFI
FFI
([...]);
CompilationUnit
CU
=
FFI
.
cdef
(
"int puts(const char* s);"
,
[...]);
NativeFunc
F
=
CU
.
getFunction
(
"puts"
);
const
char
*
s
=
"hello world!"
;
void
*
Args
[]
=
{
&
s
};
int
Ret
;
F
.
call
(
&
Ret
,
Args
);
So, basically, a pointer to the returned data and an array of
void*
is given to DragonFFI. Each
void*
value is a pointer to the data that must be passed to the underlying function. So the last missing piece of the puzzle is the code that takes this array of
void*
(and pointer to the returned data) and calls
puts
, so a function like this:
void
call_puts
(
void
*
Ret
,
void
**
Args
)
{
*
((
int
*
)
Ret
)
=
puts
((
const
char
*
)
Args
[
0
]);
}
We call these "function wrappers" (how original! :)). One advantage of this signature is that it is a generic signature, which can be used in the implementation of DragonFFI. Supposing we manage to compile at run-time this function, we can then call it trivially as in the following:
typedef
void
(
*
puts_call_ty
)(
void
*
,
void
**
);
puts_call_ty
Wrapper
=
Wrapper
(
Ret
,
Args
);
Generating and compiling a function like this is something Clang/LLVM is able to do. For the record, this is also what
libffi
mainly does, by generating the necessary assembly
by hand
. We optimize the number of these wrappers in DragonFFI, by generating them for each different function type. So, the actual wrapper that would be generated for
puts
is actually this one:
void
__dffi_wrapper_0
(
int32_t
(
__attribute__
((
cdecl
))
*
__FPtr
)(
char
*
),
int32_t
*
__Ret
,
void
**
__Args
)
{
*
__Ret
=
(
__FPtr
)(
*
((
char
**
)
__Args
[
0
]));
}
For now, all the necessary wrappers are generated when the
DFFI::cdef
or
DFFI::compile
APIs are used. The only exception where they are generated on-the-fly (when calling
CompilationUnit::getFunction
) is for variadic arguments. One possible evolution is to let the user chooses whether he wants this to happen on-the-fly or not for every declared function.
Issues with Clang
There is one major issue with Clang that we need to hack around in order to have the
DFFI::cdef
functionality: unused declarations aren't emitted by Clang (even when using
-g
-femit-all-decls
).
Here is an example, produced from the following C code:
typedef
struct
{
short
a
;
int
b
;
}
A
;
void
print_A
(
A
s
);
$ clang -S -emit-llvm -g -femit-all-decls -o - a.c
|
grep print_A
|
wc -l
0
The produced LLVM IR does not contain a function named
print_A
! The hack we temporarily use parses the clang AST and generates temporary functions that looks like this:
void
__dffi_force_decl_print_A
(
A
s
)
{
}
This forces LLVM to generate an empty function named
__dffi_force_decl_print_A
with the good arguments (and associated debug informations).
This is why DragonFFI proposes another API,
DFFI::compile
. This API does not force declared-only functions to be present in the LLVM IR, and will only expose functions that end up naturally in the LLVM IR after optimizations.
If someone has a better idea to handle this, please let us know!
Python bindings
Python bindings were the first ones to have been written, simply because it's the "high level" language I know best.  Python provides its own set of challenges, but we will save that for another blog post.  These Python bindings are built using
pybind11
, and provides their own set of C types. Lots of example of what can be achieved can be found
here
and
here
.
Project status
DragonFFI currently supports Linux, OSX and Windows OSes, running on Intel 32 and 64-bits CPUs. Travis is used for continuous integration, and every changes is validated on all these platforms before being integrated.
The project will go from alpha to beta quality when the 0.3 version will be out (which will bring Travis and Appveyor CI integration and support for variadic functions). The project will be considered stable once these things happen:
user and developer documentations exist!
another foreign language is supported (JS? Ruby?)
the DragonFFI main library API is considered stable
a non negligible list of tests have been added
all the things in the
TODO
file have been done :)
Various ideas for the future
Here are various interesting ideas we have for the future. We don't know yet when they will be implemented, but we think some of them could be quite nice to have.
Parse embedded DWARF information
As the entry point of DragonFFI are DWARF informations, we could imagine parsing these debug informations from shared libraries that embed them (or provide them in a separate file). The main advantage is that all the necessary information for doing the FFI right are in one file, the header files are no longer required. The main drawback is that debug informations tend to take a lot of space (for instance, DWARF informations take 1.8Mb for
libarchive
3.32 compiled in release mode, for an original binary code size of 735Kb), and this brings us to the next idea.
Lightweight debug info?
The DWARF standard allows to define lots of information, and we don't need all of them in our case. We could imagine embedding only the necessary DWARF objects, that is just the necessary types to call the exported functions of a shared library. One experiment of this is available here:
https://github.com/aguinet/llvm-lightdwarf
. This is an LLVM optimisation pass that is inserted at the end of the optimisation pipeline, and parse metadata to only keep the relevant one for DragonFFI. More precisely, it only keeps the dwarf metadata related to
exported
and
visible
functions, with the associated types. It also keeps debug information of global variables, even thought these ones aren't supported yet in DragonFFI. It also does some unconventional things, like replacing every file and directory by "_", to save space. "Fun" fact, to do this, it borrows some code from the LLVM bitcode "obfuscator" included in recent Apple's clang version, that is used to anonymize some information from the LLVM bitcode that is sent with tvOS/iOS applications (see
http://lists.llvm.org/pipermail/llvm-dev/2016-February/095588.html
for more information).
Enough talking, let's see some preliminary results (on Linux x64):
on libarchive 3.3.2, DWARF goes from 1.8Mb to 536Kb, for an original binary code size of 735Kb
on zlib 1.2.11, DWARF goes from 162Kb to 61Kb, for an original binary code size of 99Kb
The instructions to reproduce this are available in the README of the LLVM pass repository.
We can conclude that defining this "light" DWARF format could be a nice idea. One other thing that could be done is defining a new binary format, that would be thus more space-efficient, but there are drawbacks going this way:
debug informations are well supported on every platform nowadays: tools exist to parse them, embed/extract them from binary, and so on
we already got DWARD and PDB:
https://xkcd.com/927/
Nevertheless, it still could be a nice experiment to try and do this, figuring out the space won and see if this is worth it!
As a final note, these two ideas would also benefit to
libffi
, as we could process these formats and create
libffi
types!
JIT code from the final language (like Python) to native function code
One advantage of embedding a full working C compiler is that we could JIT the code from the final language glue to the final C function call, and thus limit the performance impact of this glue code.
Indeed, when a call is issued from Python, the following things happen:
arguments are converted from Python to C according to the function type
the function pointer and wrapper and gathered from DragonFFI
the final call is made
All this process involves basically a loop on the types of the arguments of the called function, which contains a big switch case. This loop generates the array of
void*
values that represents the C arguments, which is then passed to the wrapper. We could JIT a specialised version of this loop for the function type, inline the already-compiled wrapper and apply classical optimisation on top of the resulting IR, and get a straightforward conversion code specialized for the given function type, directly from Python to C.
One idea we are exploring is combining
easy::jit
(hello fellow Quarkslab teammates!) with
LLPE
to achieve this goal.
Reducing DragonFFI library size
The DragonFFI shared library embed statically compiled versions of LLVM and Clang. The size of the final shared library is about 55Mb (stripped, under Linux x64). This is really really huge, compared for instance to the 39Kb of libffi (also stripped, Linux x64)!
Here are some idea to try and reduce this footprint:
compile DragonFFI, Clang and LLVM using (Thin) LTO, with visibility hidden for both Clang and LLVM. This could have the effect of removing code from Clang/LLVM that isn't used by DragonFFI.
make DragonFFI more modular: - one core module that only have the parts from CodeGen that deals with ABIs. If the types and function prototypes are defined "by hand" (without
DFFI::cdef
), that's more or less the only part that is needed (with LLVM obviously) - one optional module that includes the full clang compiler (to provide the
DFFI::cdef
and
DFFI::compile
APIs)
Even with all of this, it seems to be really hard to match the 39Kb of
libffi
, even if we remove the
cdef
/
compile
API from DragonFFI. As always, pick the right tool for your needs :)
Conclusion
Writing the first working version of DragonFFI has been a fun experiment, that made me discover new parts of Clang/LLVM :) The current goal is to try and achieve a first stable version (see above), and experiment with the various cited ideas.
It's a really long road, so feel free to come on
#dragonffi
on FreeNode for any questions/suggestions you might have, (inclusive) or if you want to contribute!
Acknowledgments
Thanks to Serge «sans paille» Guelton for the discussions around the Python bindings, and for helping me finding the name of the project :) (one of the most difficult task). Thanks also to him,
Fernand Lone-Sang
and
Kévin Szkudlapski
for their review of this blog post!
