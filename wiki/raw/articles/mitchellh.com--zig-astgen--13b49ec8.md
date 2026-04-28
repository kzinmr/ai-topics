---
title: "Zig AstGen: AST => ZIR"
url: "https://mitchellh.com/zig/astgen"
fetched_at: 2026-04-28T07:02:41.429723+00:00
source: "mitchellh.com"
tags: [blog, raw]
---

# Zig AstGen: AST => ZIR

Source: https://mitchellh.com/zig/astgen

Table of Contents
After building the abstract syntax tree (AST), the next step in many compilers is to generate an intermediate representation (IR). Whereas the AST is a tree, the IR usually begins creating a sequence of instructions for various blocks of a program (a file, a function, etc.). This sequence of instructions format can be more easily analyzed for optimization and conversion to executable machine code.
The Zig compiler has multiple intermediate representations. The first IR form created is called the Zig Intermediate Representation (ZIR). The AST is converted directly to ZIR using a stage that is internally called “AstGen”. ZIR is an untyped IR form that is generated for each Zig file.
What Does ZIR Look Like?
Before diving into the internal structure of ZIR and the process for creating it, let’s take a look at a quick example of what ZIR looks like. You’re not expected to understand any of this right now.
Here is a very small Zig file:
const
result
=
42
;
export
fn
hello
()
u8
{
return
result
;
}
And the resulting ZIR for this file:
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
24
] result
line
(
0
)
hash
(
193c9ec04fd3f33e5e849a85f0c3b7fd
)
:
%
1
=
block_inline
({
%
2
=
int
(
42
)
%
3
=
break_inline
(
%
1
,
%
2
)
}) node_offset
:
1
:
1
[
32
]
export
hello
line
(
2
)
hash
(
322ad1340dd6faf97c80f152e26dfdd4
)
:
%
4
=
block_inline
({
%
11
=
func
(ret_ty
=
{
%
5
=
break_inline
(
%
11
,
@Ref
.
u8_type)
}
,
body
=
{
%
6
=
dbg_stmt
(
2
,
5
)
%
7
=
extended
(
ret_type
()) node_offset
:
4
:
5
%
8
=
decl_val
(
"result"
) token_offset
:
4
:
12
%
9
=
as_node
(
%
7
,
%
8
) node_offset
:
4
:
12
%
10
=
ret_node
(
%
9
) node_offset
:
4
:
5
}) (lbrace
=
1
:
22
,
rbrace
=
3
:
1
) node_offset
:
3
:
8
%
12
=
break_inline
(
%
4
,
%
11
)
}) node_offset
:
3
:
8
}
,
{}
,
{})
Note: ZIR isn’t necessarilly a stable format, so the output above may not match what the Zig compiler outputs today. Regardless, it will be close enough for the purpose of seeing ZIR for the first time.
The main thing to notice with ZIR is that the actual logic of the program is starting to get broken down into finer grained
instructions
. ZIR instructions can be referenced by their index, shown in the output above after the
%
sigil. For example, instruction 9 is converting the
result
reference to the return type for the
hello
function.
Want to see more ZIR?
If you compile Zig from source, you can use the
zig ast-check -t <file>
command to dump the ZIR for any Zig file. Writing simple Zig constructs and dumping the ZIR is a great way to learn about the AstGen step. The steps to compile Zig from source are not explained on this page.
Why is ZIR Untyped?
ZIR is an untyped intermediate format. This doesn’t mean that ZIR is unaware of types, it means that types are not fully evaluated. A language-defining feature of Zig is that it uses types as first-class values and comptime-evaluation as a mechanism for generic typing. Therefore, its possible that the type is
still unknown
in the AST and in the ZIR format.
This is easiest to see in example ZIR output. First, let’s look at a
mostly typed
form:
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
10
] a
line
(
0
)
hash
(
63c8310741c228c128abf6692d07292d
)
:
%
1
=
block_inline
({
%
2
=
int
(
42
)
%
3
=
as_node
(
@Ref
.
u32_type
,
%
2
) node_offset
:
1
:
16
%
4
=
break_inline
(
%
1
,
%
3
)
}) node_offset
:
1
:
1
}
,
{}
,
{})
Instruction
%3
converts the untyped
42
value to a
u32
. In this small example, the ZIR seems fully typed, but there are still untyped instructions. Instruction
%2
is an “untyped” constant
42
. It is untyped because the constant
42
can still be coerced into a
u8
,
u16
,
u32
, etc. It isn’t until our code assigns the untyped constant to a typed constant that ZIR emits a type coercision instruction
as_node
.
Next, let’s look at a
definitely untyped
form:
const
t
=
bool
;
const
result
:
t
=
42
;
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
16
] t
line
(
0
)
hash
(
243086356f9a6b0669ba4a7bb4a990e4
)
:
%
1
=
block_inline
({
%
2
=
break_inline
(
%
1
,
@Ref
.
bool_type)
}) node_offset
:
1
:
1
[
24
] result
line
(
1
)
hash
(
8c4cc7d2e9f1310630b3af7c4e9162bd
)
:
%
3
=
block_inline
({
%
4
=
decl_val
(
"t"
) token_offset
:
2
:
10
%
5
=
as_node
(
@Ref
.
type_type
,
%
4
) node_offset
:
2
:
10
%
6
=
int
(
42
)
%
7
=
as_node
(
%
5
,
%
6
) node_offset
:
2
:
14
%
8
=
break_inline
(
%
3
,
%
7
)
}) node_offset
:
2
:
1
}
,
{}
,
{})
In this scenario, the type of
result
is the constant
t
. You could argue the constant
t
is trivially known in this case, but Zig allows the assignment of
t
to be
any comptime expression
(which is pretty much the entire language so long as all values are comptime-known). This is an extremely powerful feature of Zig.
Given the dynamic possibilities, you can see that the ZIR for assignment to
result
is much more complicated. Instruction
%4
and
%5
load the value identified by
t
and coerce it into a
type
type (a type that represents a type instead of a value). Then instruction
%7
has the familiar
as_node
coercion, but this time the type operand references the result of a ZIR instruction
%5
rather than a static value.
As a final, more extreme example:
const
std
=
@import
(
"std"
)
;
const
result
:
std
.
ArrayListUnmanaged
(
u8
)
=
.
{}
;
I will not show the ZIR for this, because it is massive. The type for
result
is the generic type generated via comptime evaluation of the function
ArrayListUnmanaged
. ZIR cannot point to a predefined type for
result
because it simply isn’t known until comptime evaluation.
This is why ZIR is
untyped
. ZIR is the prepared intermediary form for comptime evaluation and further semantic analysis. After the comptime pass, all types will be known and a fully typed intermediate representation can be formed (this is known as AIR and is the result of the stage following AstGen).
Anatomy of AstGen
“AstGen” is the stage that converts AST to ZIR. The source for AstGen is in
src/AstGen.zig
. AstGen is not a publicy exported struct and is the struct is only used to manage internal state of the ZIR generation process. External callers call the
generate
function which takes an AST tree and returns ZIR for the entire tree.
The
AstGen
struct has many fields for internal state. We won’t go through all of them but some important ones are shown below. The fields of the structure below aren’t shown in the same order as they are in the source:
const
Astgen
=
struct
{
gpa
:
Allocator
,
arena
:
Allocator
,
tree
:
*
const
Ast
,
instructions
:
std
.
MultiArrayList
(Zir
.
Inst)
=
.
{}
,
extra
:
ArrayListUnmanaged
(
u32
)
=
.
{}
,
string_bytes
:
ArrayListUnmanaged
(
u8
)
=
.
{}
,
// other fields, not covered...
}
;
The first group
gpa
,
arena
, and
tree
are the inputs to the AstGen process.
gpa
is used to allocate data that lives beyond the generation process.
arena
is used to allocate temporary data used only during ZIR generation that is freed prior to returning the ZIR to the user. And
tree
is the AST that is being converted to ZIR.
Why is “arena” called “arena?”
An “arena allocator” is a category of memory allocator that allocates and deallocates an entire region of memory all at once instead of tracking and deallocating individual items one at a time. It is often used for allocations that all share a common lifecycle since it is much easier and more performant to deallocate an entire chunk of memory instead of tracking individual items. For more basics on allocators and Zig, see the talk
“What’s a Memory Allocator Anyways?”
The second group
instructions
,
extra
, and
string_bytes
are the outputs from the AstGen process. This group is very important since it is the core anatomy of the resulting ZIR:
instructions
is a list of instructions. Each entry in this list corresponds to a single instruction. For example, looking at the ZIR output earlier in this page, the 9th entry in this list would be the
as_node(%7, %8)
instruction.
extra
is extra data a ZIR instruction may need to store. This is the same pattern followed by AST nodes and their
extra_data
field. If you don’t understand AST
extra_data
, now would be a good time to review since that pattern is used everywhere during AstGen!
string_bytes
is a
string interning pool
for identifiers, string literals, doc comments, etc. All static strings are interned as part of AstGen, and ZIR instructions refer to the offset in this list of string bytes rather than store copies of the strings themselves.
Anatomy of a ZIR Instruction
Before diving into the operation of turning the AST into ZIR, I’m going to spend a significant amount of page space describing the format of a single ZIR instruction. I recommending reading and understanding this section carefully because this is a fundamental building block to understanding the construction of ZIR.
ZIR is effectively a list of instructions. The format of an instruction will have strong parallels to the patterns used with AST nodes so this page may gloss over some of the structural details. In those cases, I will make a point to call out the similarities.
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
pub
const
Tag
=
enum
(
u8
) {
add
,
addwrap
,
// many more...
}
;
pub
const
Data
=
union
{
// various fields that can be set depending on tag
}
;
}
;
This is
very
similar to AST nodes. The “tag” pattern is the same as AST nodes, but the tags are a completely different set. For example, the AST for an integer literal is
.integer_literal
regardless of the size of the integer. For ZIR, this translates to either
.int
or
.int_big
depending on if the integer fits into a
u64
or not.
Each instruction has data associated with it. The active field in the data union depends on the
tag
value. Data can be stored directly within the data field (such as an integer literal value) or the data field may be a reference to information located somewhere else.
Like AST nodes, ZIR has an
extra
field. This behaves more or less the same as the AST node
extra_data
field: some data entries may point to an entry in the
extra
field and some number of fields starting there will contain certain values relevant to the ZIR instruction. For more details, see the Zig Parser page in addition to the examples below.
Static Values
The simplest ZIR instructions are those that contain static values. Let’s look at the ZIR for a simple static integer value and the ZIR produced for this.
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
7
] x
line
(
0
)
hash
(
5b108956afe84d38689dcd3f2d652f04
)
:
%
1
=
block_inline
({
%
2
=
int
(
42
)
%
3
=
break_inline
(
%
1
,
%
2
)
}) node_offset
:
1
:
1
}
,
{}
,
{})
The relevant instruction is
%2
:
int(42)
. As you can see, the static value
42
is encoded directly into the instruction itself. Internally, this is represented as shown below:
Zir
.
Inst{
.
tag
=
.
int
,
.
data
=
.
{
.
int
=
42
,
}
,
}
This is the simplest that a ZIR instruction can be: the data is embedded directly within the instruction. In this case, the active tag for the data is
.int
which embeds the static integer value.
It is much more common that data is referenced or the tag contains more complicated information that doesn’t fit directly in the
Inst
structure. Examples of this are shown next.
Refs
Many ZIR instructions contain references to values. For example, the unary
!
operator (boolean NOT) prefixes any expression such as a static value
!true
, a variable
!myVar
, a function call
!myFunc()
, etc. It’s very important to understand how ZIR encodes references since they are so common.
ZIR references have a dedicacated type
Zir.Inst.Ref
. This is a
non-exhaustive enum
. The defined tags are for values that are primitives or very common. Otherwise, the value is a reference to another ZIR instruction index.
Tagged Refs
Let’s look at an example to see how this works:
This results in the following ZIR:
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
7
] result
line
(
0
)
hash
(
0be0bb45d9cb29941abcc19d4176dde6
)
:
%
1
=
block_inline
({
%
2
=
bool_not
(
@Ref
.
bool_true) node_offset
:
1
:
16
%
3
=
break_inline
(
%
1
,
%
2
)
}) node_offset
:
1
:
1
}
,
{}
,
{})
Look at instruction
%2
. It contains our
bool_not
instruction (the
!
operator) and the parameter is
@Ref.bool_true
. The
bool_not
instruction takes a single operand. Internally, this is a
Inst
with roughly the following structure (some fields purposely omitted that aren’t important for the example):
Zir
.
Inst{
.
tag
=
.
bool_not
,
.
data
=
.
{
.
un_node
=
.
{
.
operand
=
Ref
.
bool_true }
,
}
,
}
Ref.bool_true
is one of the tags for the
Ref
enum that represents the static value
true
. There are many more. For example, there is one for every built-in type. While the following example is nonsensical, it does result in valid ZIR (the compiler would error about it later):
const
x
=
!
u8
;
// ZIR: bool_not(@Ref.u8_type)
For well known primitives and values, a tagged value for
Ref
is used.
Refs to Instructions
For values that aren’t well-known, the
Ref
represents is the instruction index. Here is another example and the relevant ZIR that is produced.
const
input
=
true
;
const
x
=
!
input
;
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
13
] input
line
(
0
)
hash
(
1af5eb6ed7d8836d8d54ff390bb38c7d
)
:
%
1
=
block_inline
({
%
2
=
break_inline
(
%
1
,
@Ref
.
bool_true)
}) node_offset
:
1
:
1
[
21
] result
line
(
1
)
hash
(
4ba2a2df9e05a2d7963b6c1eb80fdcea
)
:
%
3
=
block_inline
({
%
4
=
decl_val
(
"input"
) token_offset
:
2
:
17
%
5
=
as_node
(
@Ref
.
bool_type
,
%
4
) node_offset
:
2
:
17
%
6
=
bool_not
(
%
5
) node_offset
:
2
:
16
%
7
=
break_inline
(
%
3
,
%
6
)
}) node_offset
:
2
:
1
}
,
{}
,
{})
The key instruction for looking at the ref is
%6
. We can see the familiar
bool_not
instruction again, but this time the operand is a reference to another instruction:
%5
. If you keep following the instruction chain, you should be able to intuitively understand it is reading the value of
input
as a boolean.
Internally, the instruction looks something like this:
Zir
.
Inst{
.
tag
=
.
bool_not
,
.
data
=
.
{
.
un_node
=
.
{
.
operand
=
Ref
.
typed_value_map
.
len
+
5
}
,
}
,
}
Or, more simply: the total number of tagged values plus 5. Likewise, to determine if a
Ref
value is a tag or an index, we can check if the value is greater than the number of tags. If so, the value minus the tag length equals the instruction.
This is so common that there are two public functions for doing this:
indexToRef
and
refToIndex
. In the example above, we’re setting the operand to
indexToRef(5)
and if you called
refToIndex(operand)
you’d get back
5
.
const
ref_start_index
:
u32
=
Inst
.
Ref
.
typed_value_map
.
len
;
pub
fn
indexToRef
(inst
:
Inst
.
Index) Inst
.
Ref {
return
@intToEnum
(Inst
.
Ref
,
ref_start_index
+
inst)
;
}
pub
fn
refToIndex
(inst
:
Inst
.
Ref)
?
Inst
.
Index {
const
ref_int
=
@enumToInt
(inst)
;
if
(ref_int
>=
ref_start_index) {
return
ref_int
-
ref_start_index
;
}
else
{
return
null
;
}
}
Some ZIR instructions contain references to the
extra
field which is also sometimes called “trailing” data. This is very similar to the
extra_data
field in AST nodes, so the encoding/decoding won’t be covered in detail here. If you do not know of or understand the
extra_data
field in AST nodes well, I recommend reviewing that section.
Let’s look at an example of extra data:
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
10
] x
line
(
0
)
hash
(
48fa081b63af0a1c7f2d11a7bf9fbbc3
)
:
%
1
=
block_inline
({
%
2
=
int
(
2
)
%
3
=
add
(
@Ref
.
one
,
%
2
) node_offset
:
1
:
13
%
4
=
break_inline
(
%
1
,
%
3
)
}) node_offset
:
1
:
1
}
,
{}
,
{})
This output ZIR builds on everything we’ve already learned above! There is a static value (instruction
%2
), there is a tagged ref (
@Ref.one
in instruction
%3
), and there is a ref referencing another instruction (the
%2
operand in instruction
%3
).
The binary addition operation uses
extra
. It isn’t immediately obvious in the ZIR text output because the ZIR renderer understand the
add
instruction and pretty-prints data from
extra
(instruction
%3
). Internally, it looks like this:
// Instruction
Zir
.
Inst{
.
tag
=
.
add
,
.
data
=
.
{
.
pl_node
=
.
{
.
payload_index
=
7
}
,
}
,
}
// Exra data
[
...,
Ref
.
one
,
%
2
,
...
]
The instruction uses the
pl_node
(short for “payload node”) data tag. This contains a field
payload_index
that points to the starting field in the
extra
array where additional data can be found. By looking at the comments for the
.add
tag, the structure stored in the
extra
field is a
Zir.Inst.Bin
which has a
lhs
and
rhs
. In this case
lhs = Ref.one
and
rhs = %2
.
Similar to AST nodes, the AstGen source contains a helper function
addExtra
that encodes structured extra data in a type-safe way. This pattern is described in more detail in the AST node section on the Zig Parser page.
Extra data itself may contain static values, other
Zig.Inst.Ref
values, and more. You’ll have to look at the source code for each tag to understand what values it encodes.
More Data Types
There are many more data types, but I will not cover them all exhaustively. I felt the data types above were particularly important to understanding the broader patterns that are used to encode information about a ZIR instruction.
Components of AstGen
The AstGen process has a number of common, shared components that are used while building ZIR. These components represent common or shared logic and are critical to understanding the full behavior of AstGen. Most of these components are arguments to every function within AstGen.
This isn’t an exhaustive list of every feature of AstGen, but highlights a few key items.
Scopes
AstGen introduces scope awareness, making it possible to reference identifiers in “parent” scopes, record an error when an undefined identifier is used, or detect identifier shadowing.
Scopes are defined using the
Scope
struct found in
AstGen.zig
. A scope is polymorphic and can be one of many sub-types. This is implemented in Zig using a common pattern with
@fieldParentPtr
. Explaining this pattern is outside the scope of this page since it is a common pattern within Zig.
There are seven scope “types” (at the time of writing this):
Scope.Top
- The outermost scope that represents a file. This is always the parent-most scope and has no parent scope. This scope doesn’t track any additional data.
GenZir
- This struct generally represents a “block” in Zig, but is used for a lot of additional state tracking across AST nodes. It tracks the current block label (if any), instruction list, whether we’re in a comptime location, etc.
Scope.Namespace
- This scope contains an unordered set of declarations that can be referenced. “Unordered” is the key word here, this scope is usually a child scope within a block for structs, unions, etc. Example: a struct variable can reference variables defined later in the file, whereas a function body cannot. One is a
Namespace
, the other is not.
Scope.LocalVal
and
Scope.LocalPtr
- A single identifier (such as a variable or constant) that has been defined. As identifiers are defined, a new child scope is created of this type so that it is now “in scope”. This is different than a
Namespace
because it represents exactly one declaration and it is not an unordered list.
Scope.Defer
- The scope around a
defer
or
errdefer
. This is used to track that a defer exists so that the instructions can be generated at all the exit points.
Scopes have a
parent
field that can be used to traverse upwards through the scopes. This is how identifier resolution works.
String Interning
String values (an array of bytes) are not stored directly within ZIR instructions. Strings are interned and stored in a single continuous
string_bytes
array. The index to the beginning of a string value is stored within ZIR instructions. This means that shared strings are stored exactly once (such as identifiers).
ZIR is the first structure in the pipeline so far that stores strings at all. AST nodes store token indexes and tokens store their start and end offset in the source code. This requires both the AST and the source remain available. After AstGen, the AST and source can be freed. This enables parsing extremely large Zig programs and storing only what we need in memory.
Result Locations
The
ResultLoc
structure keeps track of where the final result of an expression tree should be written. As an AST is being traversed and ZIR is being generated, it is possible for the value of some write operation to be deeply nested, and AstGen needs to know where to write the final value to.
Consider the following example:
const
x
=
blk1
:
{
switch
(someUnion) {
.
someTag
=>
break
:
blk1
42
,
else
=>
break
:
blk1
0
,
}
}
At the outermost scope, we are writing to a constant
x
. If you visualize the AST tree, we then have to nest into a block, then a switch, then a switch case, and finally a labeled
break
statement. After recursing at least four functions,
ResultLoc
is how AstGen knows where to write the value of the labeled break.
ResultLoc
is a tagged union with many possible result types. It is well commented so I recommend reading the source. A few of the example tags will be explained here:
.discard
- It means the assignment is thrown away because it is the right-hand side of a discard identifier
_
. In this case, AstGen knows to not generate any storage instructions, we can just throw the value away.
.ty
- The assignment is to some typed value. This generates an
as_node
to coerce a result value prior to returnign it.
.ptr
- The assignment is being written to a memory location. This generates a
store
instruction so that results are written to that memory location.
Generating ZIR
Let’s now learn about how AstGen turns an AST into ZIR. Abstractly, the AST is turned into ZIR by traversing the tree and emiting instructions for each node. AstGen eagerly converts the entire AST into ZIR (it does not lazily evaulate — a pattern that will surface in later compiler stages).
Importantly, AstGen introduces our first significant layer of
semantic validation
. For example, AstGen validates that identifiers are defined, do not shadow outer scopes, and knows how to traverse parent scopes. Recall previously that AST construction introduced
structural valiadation
: it ensured that token sequences such as
x pub == 7
raised syntax errors, but it didn’t validate that any identifier
x
was defined. And the tokenizer itself only enforced
per-token validation
: it validated
72
is a valid token but
72a
is not (identifiers cannot start with numbers).
The easiest place to start learning about how ZIR is generated is looking at the
expr
function. This generates the ZIR for any valid expression in the Zig language. I find it easiest to start with the simplest components of a language and then build up from there, since IR generation is a deeply recursive process.
Integer Literals
Let’s start with a simple static integer value:
This parses into the AST node tag
.integer_literal
which leads from
expr
to the
integerLiteral
function via the giant switch. The
integerLiteral
function is reproduced below:
fn
integerLiteral
(gz
:
*
GenZir
,
rl
:
ResultLoc
,
node
:
Ast
.
Node
.
Index) InnerError
!
Zir
.
Inst
.
Ref {
const
tree
=
astgen
.
tree
;
const
main_tokens
=
tree
.
nodes
.
items
(
.
main_token)
;
const
int_token
=
main_tokens[node]
;
const
prefixed_bytes
=
tree
.
tokenSlice
(int_token)
;
if
(std
.
fmt
.
parseInt
(
u64
,
prefixed_bytes
,
0
))
|
small_int
|
{
const
result
:
Zir
.
Inst
.
Ref
=
switch
(small_int) {
0
=>
.
zero
,
1
=>
.
one
,
else
=>
try
gz
.
addInt
(small_int)
,
}
;
return
rvalue
(gz
,
rl
,
result
,
node)
;
}
else
|
err
|
switch
(err) {
error
.
InvalidCharacter
=>
unreachable
,
// Caught by the parser.
error
.
Overflow
=>
{}
,
}
// ... other paths
}
There’s a lot here! This is why I start with the simplest possible thing. If I started with something like a function declaration, I’d get bogged down in so many details that it’d be overwhelming to learn. You may still be a bit overwhelmed looking at integer literals, but its the simplest it gets, so let’s dive in.
First, we use the AST to look up the token for the integer literal. Then, we can use the token start location to get the bytes associated with the token using
tree.tokenSlice
. This results in the string
"42"
or more specifically: two bytes
4
and
2
.
Next, we try to parse that character array as an unsigned 64-bit integer. If the number is too big, we fall through to the “other parts” comment which is complexity around storing “big ints” which we won’t explore here. For this example, we’ll assume all our integer constants are less than or equal to 18,446,744,073,709,551,615 (the max size of an unsigned 64-bit integer).
Unsigned? What about negative numbers?
The prefix
-
in front of a negative number is stored as a separate AST node and generates a unary operation separately in the ZIR. Integer literals are always positive.
Parsing the number in our example case will work, since
42
will parse as a valid
u64
. Next, we handle the special case that the value is
0
or
1
since those have a special tagged ref. Otherwise, we generate a
.int
ZIR instruction and store the instruction index in
result
.
Finally, we call
rvalue
which applies
ResultLoc
(covered earlier) semantics to the value to determine if we need to return it as-is, convert it a known type, store it in a memory location, etc. In many cases this will be a no-op and will simply return the
.int
ZIR instruction.
Addition
Let’s build up from a static integer value and do some addition:
This parses into the AST node tag
.add
which leads from
expr
to
simpleBinOp
.
fn
simpleBinOp
(
gz
:
*
GenZir
,
scope
:
*
Scope
,
rl
:
ResultLoc
,
node
:
Ast
.
Node
.
Index
,
op_inst_tag
:
Zir
.
Inst
.
Tag
,
) InnerError
!
Zir
.
Inst
.
Ref {
const
astgen
=
gz
.
astgen
;
const
tree
=
astgen
.
tree
;
const
node_datas
=
tree
.
nodes
.
items
(
.
data)
;
const
result
=
try
gz
.
addPlNode
(op_inst_tag
,
node
,
Zir
.
Inst
.
Bin{
.
lhs
=
try
reachableExpr
(gz
,
scope
,
.
none
,
node_datas[node]
.
lhs
,
node)
,
.
rhs
=
try
reachableExpr
(gz
,
scope
,
.
none
,
node_datas[node]
.
rhs
,
node)
,
})
;
return
rvalue
(gz
,
rl
,
result
,
node)
;
}
This is our first case of recursion. This builds a
.add
ZIR instruction with the data
lhs
and
rhs
populated by recursively building the ZIR for the left and right expression, respectively. The left expression is
42
and the right expression is
1
. We know from exploring integer literals that this will turn into
.int
instructions.
The resulting ZIR looks something like this:
%
1
=
int
(
42
)
%
2
=
add
(
%
1
,
@Ref
.
one)
Assignment
Next, let’s assign our addition to an untyped constant:
You won’t find a case for this in
expr
because this is not an expression, it is a statement. You won’t find a
statement
function either because in Zig variable assignment is only possible within containers (a struct) or blocks (i.e. a function body). You’ll find this in
containerMembers
or
blockExprStmts
. The former is used for struct bodies and the latter for function bodies. I think the easier one to look at first is
blockExprStmts
since
containerMembers
but both are valid next steps for educational purposes.
Let’s look at
blockExprStmts
, which has a switch that leads to
varDecl
for variable declarations (including constants).
varDecl
is big! I won’t paste the full function below. I’ll paste the most common code path:
const
type_node
=
var_decl
.
ast
.
type_node
;
const
result_loc
:
ResultLoc
=
if
(type_node
!=
0
)
.
{
.
ty
=
try
typeExpr
(gz
,
scope
,
type_node)
,
}
else
.
none
;
const
init_inst
=
try
reachableExpr
(gz
,
scope
,
result_loc
,
var_decl
.
ast
.
init_node
,
node)
;
const
sub_scope
=
try
block_arena
.
create
(Scope
.
LocalVal)
;
sub_scope
.
*
=
.
{
.
parent
=
scope
,
.
gen_zir
=
gz
,
.
name
=
ident_name
,
.
inst
=
init_inst
,
.
token_src
=
name_token
,
.
id_cat
=
.
@"local constant"
,
}
;
return
&
sub_scope
.
base
;
Let’s start with the top section. This section is just recursing and evaluating the type expression (if there is one) and the initialization expression. For a constant
const x: t = init
,
t
is the type expression and
init
is the initialization expression. For our example, we have no type expression, and our initialization expression is the
.add
instruction we know how to construct already.
Next, we create a new
LocalVal
scope to represent this value. The scope has the identifier name
x
, the value instruction
init_inst
and points to the parent scope given to the
varDecl
function. The scope is the return value for this function and the caller
blockExprStmts
replaces the current scope from that statement forward to this new scope so that future statements and expressions can reference this assignment.
Our previous examples returned ZIR instruction indexes and this one returned a scope. Notice that the named assignment to
x
does not generate a ZIR instruction. If you look at the generated ZIR, you won’t see
x
anywhere:
%
2
=
int
(
42
)
%
3
=
add
(
%
2
,
@Ref
.
one)
x
is in the
scope
and the scope is tracking the value instruction
inst
. If
x
is ever referenced, we’ll know that its value comes from that instruction and can reference it accordingly. For example, let’s look at the ZIR for the following in a function body:
const
x
=
42
+
1
;
const
y
=
x
;
%
2
=
int
(
42
)
%
3
=
add
(
%
2
,
@Ref
.
one)
// x assignment
%
4
=
ensure_result_non_error
(
%
3
)
// y assignment
Notice that the
y
assignment (instruction
%4
) comes directly from the instruction
%3
. We don’t need to do an explicit memory load/store in ZIR because we can reference instruction results exactly.
Note that when eventually machine code is generated, backends may determine a load/store is required (depending on the computer architecture), but the intermediate representation doesn’t need to make this decision.
As an exercise to the reader: as a next step, I would look at the statement
const y = x
and learn how identifier referencing works. This will explain how the ZIR above is generated and is a good stepping stone for future complexity.
Completing the AstGen Process
The AstGen process is run once per file, and recursively builds the ZIR for the entire file. At the end of the function, the caller receives a
Zir
value.
With the details of this page, you should be able to follow any Zig language construct and learn how the ZIR is generated. Remember, use the
zig ast-check
command frequently to review what the Zig compiler actually generates and use this as a guide for what functions to study.
Next is the
Sema process
.
