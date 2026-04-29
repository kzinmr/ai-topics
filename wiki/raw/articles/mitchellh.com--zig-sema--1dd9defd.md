---
title: "Zig Sema: ZIR => AIR"
url: "https://mitchellh.com/zig/sema"
fetched_at: 2026-04-29T07:02:01.048145+00:00
source: "mitchellh.com"
tags: [blog, raw]
---

# Zig Sema: ZIR => AIR

Source: https://mitchellh.com/zig/sema

Table of Contents
The next compiler stage after “AstGen” is “Sema.” Sema is responsible for taking the ZIR output from the AstGen stage and producing AIR. AIR, which stands for “Analyzed Intermediate Representation” is a fully typed intermediate representation, whereas ZIR is an untyped intermediate representation. AIR can then be lowered directly to machine code.
As noted in the AstGen page, one of the reasons ZIR is untyped is because fully typing a Zig program requires comptime evaluation so that generic types (amongst other things) can be fully realized. Therefore, Sema also performs all the comptime evaluation of Zig programs. This is where the magic happens!
AIR is generated per-function instead of per-file like ZIR or the AST. This page will focus on converting function bodies from ZIR to AIR. A future page will talk about how the larger compilation process invokes Sema.
Note:
There is some AIR that is generated at the file-scope, so it isn’t 100% accurate to say that AIR is generated per-function. However, understanding the file-scope AIR process requires also talking about the compilation process in more depth, and that is defered for a future article. This page will serve as an important building block towards that understanding.
What Does AIR Look Like?
We can look at example AIR before diving into how AIR is structured and built internally. Here is a simple Zig program and the AIR that it produces:
export
fn
add
(a
:
u32
,
b
:
u32
)
u32
{
return
a
+
b
;
}
# Begin Function AIR
:
add
:
%
0
=
arg
(
"a"
,
u32
)
%
1
=
arg
(
"b"
,
u32
)
%
2
!=
dbg_stmt
(
2
:
5
)
%
3
=
add
(
%
0
!
,
%
1
!
)
%
4
!=
ret
(
%
3
!
)
# End Function AIR
:
add
You can view AIR for any program by running
zig build-obj --verbose-air <file.zig>
. This will require a debug build of the Zig compiler. There is a guide in the Zig wiki for how to compile the Zig compiler from source.
AIR is generated and rendered per-function. In the output above, you can see the comment-style lines that note the AIR output for the
add
function. Also note that AIR is only generated for exported or referenced functions (it is lazily generated). Therefore, for debugging purposes, I usually
export
the function I want to view the AIR for.
If you’ve been reading about prior stages of the compiler, you’ll notice the rendered form of AIR is very similar to ZIR. While they are similar and in many cases even share instruction tag names, AIR is a completely separate intermediate representation.
The
%1
is the instruction index of an instruction. When it is followed by
!
it means that this instruction is unused or unreferenced by any other known part of the Zig program. In the example above,
%0
and
%1
are both used for the addition instruction to construct
%3
, which is used by the return instruction. But the debug statement
%2
and return result
%4
are unused. Backends that convert AIR to a final format can use this information if it is helpful.
Note:
As noted in the introduction, there is some AIR that is generated at the file scope and not the function scope. For example, file-scoped variable initialization, comptime blocks, etc. It is not possible currently to render this AIR. File-scoped AIR is usually just a series of
constant
instructions though since it is always comptime-evaluated.
Anatomy of AIR
Before looking into how ZIR is turned into AIR, I’m going to describe the format of AIR and individual AIR instructions. Understanding the structure of AIR makes understanding the construction of AIR much easier.
The structure of AIR is very similar to ZIR, but with subtle differences:
pub
const
AIR
=
struct
{
instructions
:
std
.
MultiArrayList
(Inst)
.
Slice
,
extra
:
[]
const
u32
,
values
:
[]
const
Value
,
}
;
Just like ZIR, AIR is fundamentally a series of instructions stored in the
instructions
field. And similar to ZIR and our AST, instructions may store instruction-specific extra data in the
extra
slice. These two fields behave identically to both ZIR and the AST; if you do not intuitively understand them at this point, I recommend going back and reviewing those structures (particularly the AST structure which goes in depth into how
extra
data is filled).
Note:
I also skip explaining the
MultiArrayList
here, because this is the identical pattern used with ZIR and the AST and was explained in depth in the parser exploration.
A new field present in AIR is the
values
slice. This contains known values from comptime execution of the ZIR. Instructions may reference comptime known values. For example, if the root of your file has
const a = 42;
, then the value
42
will be stored in the
values
list since it is comptime-known. We’ll see more examples of comptime values later.
Notice that fields such as string tables for string constants are not present. The AIR building process and the future Codegen process that uses AIR continues to have access to the ZIR so that it can lookup data in the ZIR string table.
Anatomy of a Single AIR Instruction
The structure for a single AIR instruction is the
Inst
struct.
pub
const
Inst
=
struct
{
tag
:
Tag
,
data
:
Data
,
}
;
This struct is structurally identical to the ZIR
Inst
struct. There is a
tag
which is an enum and then there is tag-specific
data
which is a union of possible data types. The AIR
Tag
and
Data
types are distinct from the ZIR types, but functionally identical.
Let’s look at a basic example. When semantic analysis determines a value is constant, it creates the
.constant
instruction. The data of a
constant
-tagged instruction is the
ty_pl
field which contains the type of the constant and the payload is an index into the
values
array with the comptime-known value.
%
0
=
constant
(
comptime_int
,
42
)
Inst{
.
tag
=
.
constant
,
.
data
=
.
{
.
ty_pl
=
.
{
.
ty
=
Type
.
initTag
(
.
comptime_int
)
,
.
pl
=
7
,
// index into values
}
,
}
,
}
;
The example above shows the Zig code, the rendered AIR, and the internal instruction representation. note that the
c
is not present anywhere because the ZIR analyzed to create this AIR is only for the right-hand side (rhs) of the assignment: the constant
42
.
Values, Types, TypedValues
There are three types very frequently used throughout Sema:
Value
,
Type
, and
TypedValue
. A
Value
represents a comptime-known value such as an integer, struct, etc. A
Type
is a comptime-known type such as
u8
(note: all types are comptime-known). And a
TypedValue
is a value with an exact known type: so pairing the value
42
with the type
u16
.
One thing that can be a bit confusing is that types are also valid values in Zigs. A type can be a value with type “type”. For example, in Zig, you can assign
const c = u8
.
c
is type “type” with a value of “u8”.  We’ll show numerous examples below of these scenarios so that this can become more intuitive.
Values
The
Value
structure is shown below:
pub
const
Value
=
extern
union
{
tag_if_small_enough
:
Tag
,
ptr_otherwise
:
*
Payload
,
}
A type has a
tag
describing the kind of value it is. I use “kind” here purposefully instead of “type” because a value is untyped although in certain cases the type can be trivially known.  Some
tag
values do not have a payload, while otherwise require a payload. The
ptr_otherwise
field is a pointer to a payload with more information required to get the value.
The
Payload
type is a pointer to the
Payload
-typed field of a more specific payload type. This is one way that polymorphic types are used within Zig. The
@fieldParentPtr
instrinsic is then used to determine the full type. This is a common pattern in Zig and explaining it in further detail is outside the scope of this page. Please search for
@fieldParentPtr
guides and Zig to understand how this works.
Integer
Let’s look at integer values. The constant
42
is represented using the
Value
below:
Value{
.
ptr_otherwise
=
&
Payload
.
U64{
.
tag
=
.
int_u64
,
.
data
=
42
,
}
,
}
;
Note:
The value isn’t
exactly
correct. The
ptr_otherwise
field points to a
Payload
and not the full
Payload.U64
struct. But, the above is more clear about what the intention is so I’ll use this format throughout.
As we can see, the value
42
is represented with the
int_u64
flag. This is because
int_u64
is used to represent all values that can fit within a
u64
. It
does not
mean that
42
is a
u64
type — it may still be a
u8
,
u16
, etc. A
Value
without a
Type
is untyped. Or, if its bothering you that we kind of have a type, you can consider a value as
not exactly typed.
Type Values (not TypedValues)
A type can also be a value in Zig. For example, the statement
const c = u8
is completely valid Zig: you’re assigning the type
u8
to the constant
c
which itself has the type
type
(it is a value holding a type). This can be really confusing, and it continues to get more confusing as type values are used in the actual semantic analysis, so it is explained early here.
The constant
u8
as a value is represented using the
Value
below:
Value{
.
tag_if_small_enough
=
.
u8_type
,
}
;
This value has no payload. The value is exactly represented by the tag
u8_type
. The value is the u8
type
. But the value itself is still
untyped
. However, the type is trivially known in this case because the only valid type for
u8_type
is
type
. But the
Value
struct itself is still technically untyped (for example one day Zig could introduce a keyword
inttype
to represent all integer types, and it would be valid for this value to be either
inttype
or
type
).
Let’s look at a more complex type value:
const c = [4]bool
.
Value{
.
ptr_otherwise
=
&
Payload
.
Ty{
.
tag
=
.
ty
,
.
data
=
Type{
// .tag = .array
// type data including element type (bool), length (4), etc.
}
,
}
,
}
;
This value has a tag of
.ty
(short for “type”). It is a value that is some type. The payload is the
Type
structure describing an array of 4 boolean elements. We’ll describe the
Type
structure in more detail in the next section. The point here is that
Value
is representing an array
type value
and not an array
value
.
If there is still some confusion, look at the
toValue
function defined for
Type
. A
Type
can always be converted a value, because a type can be a value, but the reverse is not always true.
Types
The
Type
structure is equivalent to
Value
, but using type-specific types:
pub
const
Type
=
extern
union
{
tag_if_small_enough
:
Tag
,
ptr_otherwise
:
*
Payload
,
}
There isn’t much to add here, since this behaves almost identically to
Value
. Let’s look at how
[4]bool
is represented so that we have at least one concrete example:
Type{
.
ptr_otherwise
=
&
Payload
.
Array{
.
tag
=
.
array
,
.
data
=
.
{
.
len
=
4
,
.
elem_type
=
Type{
.
tag_if_small_enough
=
.
bool
}
,
}
,
}
}
TypedValue
A
TypedValue
is just both a
Type
and a
Value
together so that the value is paired with exact type information. Only with both of these together is the exact type of a value known.
pub
const
TypedValue
=
struct
{
ty
:
Type
,
val
:
Value
,
}
;
Anatomy of Sema
The next phase in the Zig compiler after “AstGen” is colloquially known as “Sema.”
Sema
is also the struct that is primarily responsible for this phase. The source for Sema is in
src/Sema.zig
. It is a very large file (over 18,000 lines at the time of writing this) and is self-described as “the heart of the Zig compiler.”
There are many public APIs for Sema, but the most important is
analyzeBody
. The
Sema
struct has many fields for internal state. We won’t go through all of them but some of the primary ones are shown below. The fields are not shown in the same order as the source, in order to ease explanation of similar fields.
pub
const
Sema
=
struct
{
mod
:
*
Module
,
gpa
:
Allocator
,
arena
:
Allocator
,
perm_arena
:
Allocator
,
code
:
Zir
,
owner_decl
:
*
Decl
,
func
:
?*
Module
.
Fn
,
fn_ret_ty
:
Type
,
air_instructions
:
std
.
MultiArrayList
(Air
.
Inst)
=
.
{}
,
air_extra
:
std
.
ArrayListUnmanaged
(
u32
)
=
.
{}
,
air_values
:
std
.
ArrayListUnmanaged
(Value)
=
.
{}
,
inst_map
:
InstMap
=
.
{}
,
// other fields...
}
;
The first group are the main required inputs for the Sema process.
gpa
is used to allocate data that lives beyond the Sema process and the declaration lifetime.
arena
is used to allocate temporary data that is freed after Sema. And
perm_arena
is used to allocate data that is tied to the lifetime of the declaration that is undergoing semantic analysis.
mod
is the module that is being analyzed. Modules aren’t covered in this page, but encapsulates all the Zig code in a single program. We will ignore all module APIs for this page.
The second group are the inputs describing what is being semantically analyzed by Sema.
code
is the ZIR for the file that contains the decl being analyzed.
owner_decl
is typically the declaration being analyzed currently, such as a function, comptime block, test, etc.
func
and
fn_ret_ty
are extra information when a function is being analyzed.
The third group are the outputs of the Sema process. You may notice that these are mostly the fields that construct the
Air
structure. These are populated throughout the Sema process and used to construct the final
Air
result.
The
inst_map
field is particularly important and used throughout Sema. This is a map of ZIR to AIR. Not all ZIR instructions result in AIR instructions, but this is used frequently so that AIR instructions can refer to specific ZIR instructions that are resolved later (i.e. addition operands, function parameters, etc.).
Analyzing a Function Body
The core function in
Sema
is
analyzeBody
. This is used to analyze the ZIR for a “body” — function body, loop body, block body, etc. — and produce the AIR for that body. The simplest body to look at is a function body. To start, let’s look at a very simple function and the AIR it generates:
export
fn
add
()
u32
{
return
40
+
2
;
}
# Begin Function AIR
:
add
:
%
1
=
constant
(
comptime_int
,
40
)
%
2
=
constant
(
comptime_int
,
2
)
%
3
=
constant
(
comptime_int
,
42
)
%
4
=
constant
(
u32
,
42
)
%
0
!=
dbg_stmt
(
2
:
5
)
%
5
!=
ret
(
%
4
!
)
# End Function AIR
:
add
Reminder:
We can dump the AIR for a function by exporting it and executing
zig build-obj --verbose-air example.zig
.
Without knowing the specifics of AIR instructions, you should be able to figure out what is happening. The rough flow of steps is shown below:
We see the untyped constant int
40
(instruction
%1
)
We see the untyped constant int
2
(instruction
%2
)
We perform the add at comptime and know the result is the untyped constant into
42
(instruction
%3
).
The constant
42
is paired with the type
u32
(instruction
%4
). No conversion is necessary since the value
42
fits automatically into the type
u32
. This typing is necessary to match the return type
u32
.
We return the value produced in
%4
(instruction
%5
).
Neat! There is some verbosity here, but its clear to see how this implemenets our function
add
. Also, you can see that the comptime evaluation was done and our addition was done in this stage so that the result is already pre-known. When this eventually gets translated down to machine code, the actual addition result is already pre-computed.
Next, let’s see how this AIR was produced, step by step.
Stepping Through the Function
The primary AIR generation loop is in
analyzeBodyInner
(called by
analyzeBody
). This iterates over the ZIR instructions in order and produces zero or more AIR instructions for each individual ZIR instruction.
const
result
=
while
(
true
) {
const
inst
=
body[i]
;
const
air_inst
:
Air
.
Inst
.
Ref
=
switch
(tags[inst]) {
.
alloc
=>
try
sema
.
zirAlloc
(block
,
inst)
,
.
alloc_inferred
=>
try
sema
.
zirAllocInferred
(block
,
inst
,
Type
.
initTag
(
.
inferred_alloc_const))
,
.
alloc_inferred_mut
=>
try
sema
.
zirAllocInferred
(block
,
inst
,
Type
.
initTag
(
.
inferred_alloc_mut))
,
.
alloc_inferred_comptime
=>
try
sema
.
zirAllocInferredComptime
(inst
,
Type
.
initTag
(
.
inferred_alloc_const))
,
.
alloc_inferred_comptime_mut
=>
try
sema
.
zirAllocInferredComptime
(inst
,
Type
.
initTag
(
.
inferred_alloc_mut))
,
.
alloc_mut
=>
try
sema
.
zirAllocMut
(block
,
inst)
,
// hundreds more...
}
;
try
sema
.
inst_map
.
put
(sema
.
gpa
,
inst
,
air_inst)
;
i
+=
1
;
}
This makes it really easy to understand how AIR is produced for a given set of ZIR. You can dump the ZIR and go one instruction at a time and determine how the AIR is produced. The ZIR for our example
add
function above:
%
0
=
extended
(
struct_decl
(parent
,
Auto
,
{
[
25
]
export
add
line
(
6
)
hash
(
4ca8d4e33898374bdeee80480f698dad
)
:
%
1
=
block_inline
({
%
10
=
func
(ret_ty
=
{
%
2
=
break_inline
(
%
10
,
@Ref
.
u32_type)
}
,
body
=
{
%
3
=
dbg_stmt
(
2
,
5
)
%
4
=
extended
(
ret_type
()) node_offset
:
8
:
5
%
5
=
int
(
40
)
%
6
=
int
(
2
)
%
7
=
add
(
%
5
,
%
6
) node_offset
:
8
:
15
%
8
=
as_node
(
%
4
,
%
7
) node_offset
:
8
:
15
%
9
=
ret_node
(
%
8
) node_offset
:
8
:
5
}) (lbrace
=
1
:
21
,
rbrace
=
3
:
1
) node_offset
:
7
:
8
%
11
=
break_inline
(
%
1
,
%
10
)
}) node_offset
:
7
:
8
}
,
{}
,
{})
The function
body
starts at ZIR instruction
%3
and ends at
%9
.
%3
is the first instruction that
analyzeBodyInner
sees when analyzing the
add
function body. The earlier (and later) ZIR instructions such as
%2
and
%10
are analyzed earlier; that process will be discussed a bit later.
%3: dbg_stmt
The first instruction is
.dbg_stmt
. In the main loop we can see that leads to
zirDbgStmt
. That function is reproduced below in a slightly simplified form:
fn
zirDbgStmt
(sema
:
*
Sema
,
block
:
*
Block
,
inst
:
Zir
.
Inst
.
Index) CompileError
!
void
{
const
inst_data
=
sema
.
code
.
instructions
.
items
(
.
data)[inst]
.
dbg_stmt
;
_
=
try
block
.
addInst
(
.
{
.
tag
=
.
dbg_stmt
,
.
data
=
.
{
.
dbg_stmt
=
.
{
.
line
=
inst_data
.
line
,
.
column
=
inst_data
.
column
,
} }
,
})
;
}
This is a good, simple example of AIR instructions being translated from ZIR. It doesn’t get any simpler than this. In this case, the
dbg_stmt
ZIR is translated almost exactly to a
dbg_stmt
AIR instruction. This results in the
%0
AIR instruction shown earlier:
%4: extended(ret_type())
The
.extended
ZIR instruction calls
zirExtended
which loops over the child opcode to map
.ret_type
to
zirRetType
. This function is reproduced below:
fn
zirRetType
(
sema
:
*
Sema
,
block
:
*
Block
,
extended
:
Zir
.
Inst
.
Extended
.
InstData
,
) CompileError
!
Air
.
Inst
.
Ref {
const
src
:
LazySrcLoc
=
.
{
.
node_offset
=
@bitCast
(
i32
,
extended
.
operand) }
;
try
sema
.
requireFunctionBlock
(block
,
src)
;
return
sema
.
addType
(sema
.
fn_ret_ty)
;
}
The return type for the function under analysis is available on the
fn_ret_ty
field on
Sema
. The
addType
function will add an instruction for a type definition. For our function, the result type is
u32
which is a well known type which doesn’t generate an additional instruction.
For experimentation, if you change the return value to
u9
— a non-well-known type — the AIR produces the following instruction:
%5: int(40)
The
.int
instruction for our constant
40
is next. This leads to the
zirInt
function call in the main analyze body loop. The
zirInt
function reads the int value and calls
addConstant
. Both functions are shown below.
fn
zirInt
(sema
:
*
Sema
,
block
:
*
Block
,
inst
:
Zir
.
Inst
.
Index) CompileError
!
Air
.
Inst
.
Ref {
const
int
=
sema
.
code
.
instructions
.
items
(
.
data)[inst]
.
int
;
return
sema
.
addConstant
(ty
,
try
Value
.
Tag
.
int_u64
.
create
(sema
.
arena
,
int))
;
}
pub
fn
addConstant
(sema
:
*
Sema
,
ty
:
Type
,
val
:
Value) SemaError
!
Air
.
Inst
.
Ref {
const
gpa
=
sema
.
gpa
;
const
ty_inst
=
try
sema
.
addType
(ty)
;
try
sema
.
air_values
.
append
(gpa
,
val)
;
try
sema
.
air_instructions
.
append
(gpa
,
.
{
.
tag
=
.
constant
,
.
data
=
.
{
.
ty_pl
=
.
{
.
ty
=
ty_inst
,
.
payload
=
@intCast
(
u32
,
sema
.
air_values
.
items
.
len
-
1
)
,
} }
,
})
;
return
Air
.
indexToRef
(
@intCast
(
u32
,
sema
.
air_instructions
.
len
-
1
))
;
}
The
addConstant
function is called in many places in Sema to add a comptime-known value. This first adds the type using
addType
, which we saw with the last instruction. In this case, the type is
comptime_int
, which is a well-known type and produces no new instructions. Next, the value is added to
air_values
and finally the
constant
AIR instruction is added to
air_instructions
. This results in the following AIR instruction:
%
1
=
constant
(
comptime_int
,
40
)
One thing to note is that the
.constant
instruction payload references the index into the
air_values
slice. All comptime-known values are stored in
air_values
and any references in the instructions are stored as indexes into the
air_values
slice.
We’ll skip
%6
since it is identical to
%5
but for the constant
2
.
%7: add(%5, %6)
Next, we have our first real logical operation: addition. The
.add
instruction leads to the
zirArithmetic
function. This function is used for many binary math opeartions. The function is shown below:
fn
zirArithmetic
(
sema
:
*
Sema
,
block
:
*
Block
,
inst
:
Zir
.
Inst
.
Index
,
zir_tag
:
Zir
.
Inst
.
Tag
,
) CompileError
!
Air
.
Inst
.
Ref {
const
inst_data
=
sema
.
code
.
instructions
.
items
(
.
data)[inst]
.
pl_node
;
sema
.
src
=
.
{
.
node_offset_bin_op
=
inst_data
.
src_node }
;
const
lhs_src
:
LazySrcLoc
=
.
{
.
node_offset_bin_lhs
=
inst_data
.
src_node }
;
const
rhs_src
:
LazySrcLoc
=
.
{
.
node_offset_bin_rhs
=
inst_data
.
src_node }
;
const
extra
=
sema
.
code
.
extraData
(Zir
.
Inst
.
Bin
,
inst_data
.
payload_index)
.
data
;
const
lhs
=
sema
.
resolveInst
(extra
.
lhs)
;
const
rhs
=
sema
.
resolveInst
(extra
.
rhs)
;
return
sema
.
analyzeArithmetic
(block
,
zir_tag
,
lhs
,
rhs
,
sema
.
src
,
lhs_src
,
rhs_src)
;
}
All the constant variable assignments at the top are decoding the ZIR instruction. The particularly important assignments are
lhs
and
rhs
. The
resolveInst
function is used to find the AIR instruction index for a given ZIR instruction. So given the
%5
and
%6
ZIR instructions,
lhs
and
rhs
are set to their resulting AIR indexes, respectively. These AIR instructions were set as part of the previous loop iterations which created the
.constant
instructions for the arguments.
Where is the ZIR ⇒ AIR mapping maintained?
The ZIR to AIR mapping is maintained in the
inst_map
field by the
analyzeBodyInner
loop. There are a couple other places it could be updated but the body loop is the primary location.
This then leads to
analyzeArithmetic
. This is a long function that spends almost all of its lines determining if it can do a comptime-analysis of this arithmetic operation. The key lines are reproduced below:
const
maybe_lhs_val
=
try
sema
.
resolveMaybeUndefVal
(block
,
lhs_src
,
casted_lhs)
;
const
maybe_rhs_val
=
try
sema
.
resolveMaybeUndefVal
(block
,
rhs_src
,
casted_rhs)
;
if
(maybe_lhs_val)
|
lhs_val
|
{
if
(maybe_rhs_val)
|
rhs_val
|
{
if
(is_int) {
return
sema
.
addConstant
(
scalar_type
,
try
lhs_val
.
intAdd
(rhs_val
,
sema
.
arena)
,
)
;
}
}
}
return
block
.
addBinOp
(
.
add
,
casted_lhs
,
casted_rhs)
;
It first calls
resolveMaybeUndefVal
. This takes an AIR instruction index and attempts to load the comptime-known value for it. This returns an optional, because the return value will be
null
if the value cannot be comptime-known.
Next, we attempt to unwrap the optionals. If we were able to find comptime-known values for both the
lhs
and
rhs
and they are both integer types, then we can do comptime-addition to produce a final constant. This is what happens for our program to produce the
.constant
AIR instruction with our result
42
:
%
3
=
constant
(
comptime_int
,
42
)
I included the fallthrough in case the values aren’t comptime known:
block.addBinOp
. This would add a
.add
AIR instruction for runtime computation (instead of comptime). To experiment: change the constant
2
into a variable such as
var b: u32 = 2
and use that for the addition. This will produce a
.add
operation because variables can’t be operated on in comptime.
%8: as_node(%4, %7)
The next instruction implements safe type coercion. Looking at the ZIR, this is converting the add result to the return type. More specifically for what we already know: we must convert the comptime int
42
to a
u32
.
The
.as_node
instruction calls into
zirAsNode
which leads eventually to the core logic in
coerce
. The
coerce
function is used throughout Sema to perform safe type coercision from one type to another.
I’ll leave studying this function up to the reader. The logic is fairly straightforward, but verbose since it has to handle many type coercion cases. For
comptime_int
to
u32
, it is determined that the value fits in a
u32
and the value is returned as-is. No additional processing is required for the type conversion.
%9: ret_node(%8)
Finally, the
return
instruction is encoded in ZIR as
ret_node
. This leads to
zirRetNode
which creates a
.ret
AIR instruction with the result. There is nothing new or unexplored in the creation of this instruction.
The
zirRetNode
function returns
always_noreturn
. This value forces the
analyzeBodyInner
loop to exit, completing the function body AIR generation.
return
always completes function body AIR generation? What about multiple
return
statements?
A return always completes the AIR generation
for the current block
. Unreachable code is illegal and caught during AstGen, meaning the only way for multiple
return
statements is for them to be in different blocks. Therefore, multiple return statements are fine in the context of a function since it’ll recurse into multiple
analyzeBodyInner
calls.
Comptime Unavailable
The first example we looked at was a little boring, because all of the logic was comptime-capable. Comptime is only available for
const
values and not for
var
values, so we can see the AIR for runtime addition by using a
var
:
export
fn
add
()
u32
{
var
b
:
u32
=
2
;
return
40
+
b
;
}
# Begin Function AIR
:
add
:
%
2
=
constant
(
comptime_int
,
2
)
%
3
=
constant
(
u32
,
2
)
%
6
=
constant
(
comptime_int
,
40
)
%
8
=
constant
(
u32
,
40
)
%
0
!=
dbg_stmt
(
2
:
5
)
%
1
=
alloc
(
*
u32
)
%
4
!=
store
(
%
1
,
%
3
!
)
%
5
!=
dbg_stmt
(
3
:
5
)
%
7
=
load
(
u32
,
%
1
!
)
%
9
=
add
(
%
8
!
,
%
7
!
)
%
10
!=
ret
(
%
9
!
)
# End Function AIR
:
add
Changing a constant
2
to a variable-assigned value of
2
produces a lot more AIR! We now have allocation with
.alloc
, value storage with
.store
, and you can see a runtime
.add
operation, too.
This is a good program to study and trace to learn how AIR is generated. I’ll leave this as an exercise to the reader, since it is following a lot of the same codepaths as our previous example.
Comptime Target Emulation
For comptime-evaluated code, the Zig compiler emulates the properties of the target platform when necessary. This is a critical feature that makes comptime-evaluation safe and possible within Zig.
An example of this can be seen in the implementation for the
@floatCast
:
const
target
=
sema
.
mod
.
getTarget
()
;
const
src_bits
=
operand_ty
.
floatBits
(target)
;
const
dst_bits
=
dest_ty
.
floatBits
(target)
;
if
(dst_bits
>=
src_bits) {
return
sema
.
coerce
(block
,
dest_ty
,
operand
,
operand_src)
;
}
return
block
.
addTyOp
(
.
fptrunc
,
dest_ty
,
operand)
;
The function gets information about the target via
getTarget
, then determines the number of bits a float can support on the target platform. If the destination has more bits than the source, the type can be safely coerced. Otherwise, the float is truncated.
Completing the Sema Process
Sema is invoked once per function. This is the first process that is run per function rather than per file. Rather than go through every declaration, Sema is invoked once only for each
referenced declaration
. To determine all the referenced declarations, Sema starts at the process entrypoint function.
This implements Zig’s “lazy analysis.” This means that certain errors will not produce compiler errors unless the declaration is referenced. This makes the compilation process extremely fast and the resulting codegen smaller since only referenced code is compiled, but it does result in sometimes confusing behavior.
With the basic knowledge explained in this page, you should be able to follow any Zig program and determine how it is translated to AIR. Remember to use the
zig ast-check
and
zig build-obj --verbose-air
commands frequently to review what the Zig compiler is generating.
After this, the AIR is handed off to the “codegen” process to lower it into a final format. Codegen is the boundary between the shared compiler “frontend” and multiple “backends.” A backend may be LLVM or it could be a native backend such as WASM.
