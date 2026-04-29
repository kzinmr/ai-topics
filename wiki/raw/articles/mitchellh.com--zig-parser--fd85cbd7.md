---
title: "Mitchell Hashimoto"
url: "https://mitchellh.com/zig/parser"
fetched_at: 2026-04-29T07:02:01.692562+00:00
source: "mitchellh.com"
tags: [blog, raw]
---

# Mitchell Hashimoto

Source: https://mitchellh.com/zig/parser

Table of Contents
Parsing is the next step in the compilation pipeline following
tokenization
. Parsing is responsible for constructing an
abstract syntax tree
from a stream of tokens. I’ve previously written about how Zig converts a stream of bytes (source) into a stream of tokens.
The Zig parser is located at
lib/std/zig/parser.zig
in the Zig source tree. It is available as part of the standard library via
std.zig.parse()
. The parser takes full source text and returns an
std.zig.Ast
(defined in
lib/std/zig/Ast.zig
).
MultiArrayList
From parsing onwards, the Zig compiler uses
MultiArrayList
structures heavily. You must understand the
MultiArrayList
in order to understand how the parser works as well as the structure of the created AST.
Before explaining a
MultiArrayList
, I’ll give a very brief overview of a normal
ArrayList
(no “Multi”). An
ArrayList
is a dynamic length array of values. When the array is full, a new larger array is allocated, and existing items are copied into the new array. This is a typical, dynamically allocated, growing (or shrinking) list of items.
For example, consider the Zig structure below:
pub
const
Tree
=
struct
{
age
:
u32
,
// trees can be very old, hence 32-bits
alive
:
bool
,
// is this tree still alive?
}
;
In an
ArrayList
, many
Tree
structures are stored like so:
┌──────────────┬──────────────┬──────────────┬──────────────┐
array: │     Tree     │     Tree     │     Tree     │     ...      │
       └──────────────┴──────────────┴──────────────┴──────────────┘
Each
Tree
requires 8 bytes of memory. An array of four trees is 32 bytes of memory.
Why 8 bytes?
A
u32
requires 4 bytes. A
bool
only requires 1 byte but since it is in a struct with a
u32
, it must be 4-byte aligned, so it also takes up 4 bytes (3 bytes wasted). The total is 8 bytes.
A
MultiArrayList
is similarly a dynamically allocated list of items. However, each
field
of the type stored in the array list is stored in a
separate contiguous array
. This has two primary benefits: (1) less wasted bytes due to alignment and (2) better cache locality. Both of these benefits often result in better performance.
Given our
Tree
structure, a
MultiArrayList(Tree)
is stored like so:
┌──────┬──────┬──────┬──────┐
   age:   │ age  │ age  │ age  │ ...  │
          └──────┴──────┴──────┴──────┘
          ┌┬┬┬┬┐
 alive:   ││││││
          └┴┴┴┴┘
Each field for the struct is stored in a separate contiguous array. An array of four trees uses 20 bytes, or 37.5% less memory. This ignores the overhead of the multiple array pointers, but that overhead is fixed so as the number of items in the list grows, it amortizes to a total of 37.5% less memory required for this example.
Why 20 bytes?
Since the struct is deconstructed, the
age
field requires 4 bytes, and our example uses 4 trees, hence 16 bytes. The
alive
field no longer needs to be 4-byte aligned since it isn’t part of a struct anymore, so it only requires 1 byte (no wasted bytes!). Our example uses 4 trees, hence 4 bytes for
alive
. This sums to 20 bytes total for both fields.
This page will not dive into how
MultiArrayList
is implemented. For the purpose of understanding the Zig compiler, it is only important to know that almost every structure (tokens, AST nodes, future IR nodes, etc.) is stored as a
MultiArrayList
. Compiling a real world program usually generates tens of thousands of “nodes” so this results in huge memory savings and improvements in cache locality.
Anatomy of the Parser
The parser uses a struct called
Parser
to store in-progress parsing state. This is not a publicly exported struct and is only used to manage internal state of the parse operation. Callers are returned an
Ast
as a result of a parsing operation, which is explored later in this page.
The structure of the parser at the time of writing is shown below. I’ve inserted newlines to separate the state into functional groups.
const
Parser
=
struct
{
gpa
:
Allocator
,
source
:
[]
const
u8
,
token_tags
:
[]
const
Token
.
Tag
,
token_starts
:
[]
const
Ast
.
ByteOffset
,
tok_i
:
TokenIndex
,
errors
:
std
.
ArrayListUnmanaged
(AstError)
,
nodes
:
Ast
.
NodeList
,
extra_data
:
std
.
ArrayListUnmanaged
(Node
.
Index)
,
scratch
:
std
.
ArrayListUnmanaged
(Node
.
Index)
,
}
;
The first group contains
gpa
and
source
. This is the allocator and full original source code of a single Zig file.
In the second group,
token_tags
and
token_starts
are the deconstructed results of tokenization. As noted earlier, the parser applies data-oriented design for better memory usage and cache locality. Therefore,
token_tags.len == token_starts.len
, they’re just the struct fields placed into separate contiguous chunks of memory. The
tok_i
value is the index to the current token that the parser is looking at (starting at 0).
The third group is the real working state of the parser. This where results that will be part of the
Ast
are accumulated. This third group is very important since it is the core of what the parser is building.
errors
is the list of errors as the parser progresses. Most well-behaved parsers attempt to continue parsing in various error scenarios and Zig’s parser is no different. The Zig parser will accumulate errors in this field and attempt to continue parsing.
nodes
is the list of AST nodes. This starts empty and is slowly built up as the parser continues. Understanding the structure of an AST node is extremely important and is covered in the next section.
extra_data
is a list of additional information that an AST node may need. For example, for a struct,
extra_data
contains the full list of all the struct members. This is again an example of data-oriented design; an alternate approach would be to put the extra data directly on a
Node
, but this makes the overall parser slower since it forces each Node to be much larger.
scratch
is temporary work space shared by the parser, usually to build up information for nodes or extra data. This is deallocated once the parser is done working.
Anatomy of an AST Node
The result of a parse is a list of AST nodes. Note that the AST itself is still a tree, but the result returned by the parser contains the list of the nodes in the tree since that is how a tree is represented in-memory.
The AST node structures can be
confusing
because there is a lot of indirection on top of the data itself being stored in a
MultiArrayList
. I recommend re-reading this section repeatedly to ensure you understand the structure of an AST node. While learning the internals of the Zig compiler, a lack of a
complete understanding
of this data pattern caused a lot of issues, because this pattern is reused in every subsequent stage of the compiler.
The AST structures can be found in
lib/std/zig/Ast.zig
. The primary structure is
Node
:
pub
const
Node
=
struct
{
tag
:
Tag
,
main_token
:
TokenIndex
,
data
:
Data
,
pub
const
Data
=
struct
{
lhs
:
Index
,
rhs
:
Index
,
}
;
pub
const
Index
=
u32
;
}
;
Note that the parser itself stores nodes in a
NodeList
, which is a
MultiArrayList(Node)
, meaning it is the Node structure with each field stored in a separate contiguous block of memory. Conceptually, you can think of nodes as single structs as shown above, but concretely, the fields are split when used.
The node
tag
is an enum of possible AST node types. For example,
fn_decl
for a function declaration,
integer_literal
for a literal integer,
builtin_call
for calling a builtin such as
@enumToInt
.
The
main_token
field isn’t extremely important to understand right now. It is the main token associated with the AST node. For example for a function declaration it might be
fn
. The value is an index into the list of tokens used to build the AST.
The
data
field is extremely important. This contains the information associated with an AST node. For example, a function declaration (
.tag == .fn_decl
) uses data to store the function prototype along with the function body. The data field is covered in detail in the next section.
AST Node Data
A key part of any AST node is data associated with it. For example, a function declaration has a function name, a parameter list, a return type, body, etc. Looking at the
Node
structure, it isn’t immediately clear where this information might be.
This is an extremely important detail to understand before we can dive into how the parser works.
And for those who want to know how the entire compiler pipeline works, this is a particularly critical detail since the AST uses a pattern that is reused throughout the compilation pipeline for other intermediary forms.
Let’s look at how the AST for a function declaration would be structured for the given Zig code:
fn
add
(a
:
u8
,
b
:
u8
)
callconv
(
.
C)
u8
{
return
a
+
b
;
}
Function Declaration
The root AST node for the function declaration has a tag of
fn_decl
.
For a
fn_decl
, the
data
field
lhs
stores an index to the function prototype (name, type information, etc.) and the
rhs
field stores an index to the function body. The only way you’d know this is reading the comments above the
.fn_decl
tag or reading the source or both.
The index values in
lhs
and
rhs
in this case are the array indices for the
Node
in the
NodeList
. So you’d find the function prototype in
tree.nodes[lhs]
(pseudo-code, not strictly correct).
So in this case, both fields of
data
are used to store
NodeList
indices. This is one usage of
data
and how information about an AST node is stored. Next, let’s look at the function prototype to determine how we’d determine the parameter list, return type, and calling convention.
Function Prototype
We can get the function prototype by reading the node at
tree.nodes[lhs]
. This node will have a tag of
fn_proto
in this case. This type of AST node stores information about the parameter, calling convention, return type, etc.
This particular AST node type uses
lhs
and
rhs
differently. The
rhs
field is used in the way same way as the function declaration and points to an index in the
NodeList
for the return type expression (since Zig supports various expressions for a comptime-computed return type in addition to direct type identifiers).
The
lhs
field, however, does
not
point to an AST node. Instead, it is an index into the
extra_data
field (seen in “Anatomy of the Parser”). This index is the
starting index
for additional metadata. The length of the additional metadata is known ahead of time based on the AST node type. So, instead of
tree.nodes[lhs]
, it is
tree.extra_data[lhs]
in this case.
Important point:
lhs/rhs
may point to either nodes or extra data.
As a reminder, the type of
extra_data
is
[]Index
. This may appear that
lhs
being used as
tree.extra_data[lhs]
is just pointing to
another
index. No,
lhs
(for a
.fn_proto
) is just pointing to the
first
index in
extra_data
. The number of subsequent fields to read is also tag-dependent. For a
fn_proto
this is six fields. How do we know its six? The comments in the source or reading the struct that is encoded:
pub
const
FnProto
=
struct
{
params_start
:
Index
,
params_end
:
Index
,
align_expr
:
Index
,
addrspace_expr
:
Index
,
section_expr
:
Index
,
callconv_expr
:
Index
,
}
;
So
tree.extra_data[lhs]
is
params_start
,
tree.extra_data[lhs+1]
is
params_end
, and so on until
tree.extra_data[lhs+5]
is
callconv_expr
.
The
Ast
struct provides a helper function
extraData()
to decode this. Given an AST tree
tree
you can access this easily using the following method. In the example below,
idx
is the index in the node list where the
.fn_proto
node exists.
const
fnData
=
tree
.
extraData
(idx
,
FnProto)
fnData
.
params_start
fnData
.
callconv_expr
// etc...
But what is
param_start
,
param_end
, etc. on the
FnProto
struct? These are
NodeList
indicies for the AST nodes representing the first parameter, last parameter, etc. This is how you read all the extra informatoin about the function prototype.
As warned earlier, there is a lot of indirection going on here. But this is all extremely important to understand now, or future stages of the pipline will be even more confusion.
Function Identifier
The
main_token
field is the only field on
Node
we haven’t used and is the final way that some data may be accessed for an AST node. For a function prototype, you can now see that the identifier itself (the function name) is nowhere to be found.
Some AST nodes — such as
.fn_proto
— use the
main_token
field for this. The
main_token
of a
fn_proto
is the index in the token stream to the “fn” keyword. In Zig, the function identifier is always immediately after this keyword. Therefore, you can extract the function identifier by looking at the token at index
main_token + 1
. This is exactly how later stages of the compiler read the identifier.
AST Data Layout Recap
If you’re interested in knowing how the remainder of the Zig compiler works,
it is extremely important that you deeply understand this information storage pattern.
It can be hard to understand on the first read (and maybe the second or third too). This section reviews how data is laid out for the AST.
AST node data can be found in three locations:
The token stream (for values such as identifiers)
The node list to find other AST nodes
The extra data list to find extra data structures
Subsequent AST nodes or extra data structures usually contain additional indexes that may point to additional nodes, extra data structures, or tokens. For example, a
fn_decl
points to a
fn_proto
points to an extra data
FnProto
structure which points to one AST node per parameter.
Finding what data is available and how you access it is dependent on the
tag
. You must read the comments in
lib/std/zig/Ast.zig
or read the parser source code to determine exactly what data is being set.
How Parsing Works
With a firm understanding of how information about the internal parser state and the structure of the resulting AST, we can now learn about how the parser actually parses some token stream.
Abstractly, a parser works by inspecting the current token in the token stream and using that as context to determine what the next token can or should be. For example, when parsing the token stream for
fn foo
, the first token seen is
.keyword_fn
and the next token expected would be an identifier. If it isn’t an identifier, it is a
syntax error
.
Unlike the tokenizer, the parser cares about whether the token order makes sense. The tokenizer just blindly creates tokens, so invalid syntax such as
fn pub var foo i32 } {
produces a valid token stream. But the parser sees that token stream and produces an error since it is non-sensical.
Next, let’s look concretely at how the parser parses the simple Zig file shown below.
var
x
=
7
;
pub
fn
inc
()
callconv
(
.
C)
void
{
x
+=
1
;
}
Parsing a Zig File
The primary entry is the
parse()
function which takes the complete source code of a Zig file. This initializes the parser state and calls
parseContainerMembers()
to parse the members of the Zig file. A Zig file is implicitly a
struct
, so the parser is effectively parsing a struct.
This leads to a while loop that looks at the current token to determine what to expect next. It is structured roughly like the following:
while
(
true
) {
switch
(p
.
token_tags[p
.
tok_i]) {
.
keyword_var
=>
...
}
}
Depending on the current token, it determines what to expect next. Our first token is
.keyword_var
since our example file is defining a variable. This ultimately leads to
parseVarDecl
to parse the variable declaration. There are many other valid tokens at this point as well:
comptime
,
fn
,
pub
, etc.
Parsing a Variable Declaration
The first member found in our Zig file is a variable declaration. The call chain eventually leads to
parseVarDecl
where we’ll see our first AST node created. A simplified version is shown below.
fn
parseVarDecl
(p
:
*
Parser)
!
Node
.
Index {
const
mut_token
=
p
.
eatToken
(
.
keyword_const)
orelse
p
.
eatToken
(
.
keyword_var)
orelse
return
null_node
;
_
=
try
p
.
expectToken
(
.
identifier)
;
const
type_node
:
Node
.
Index
=
if
(p
.
eatToken
(
.
colon)
==
null
)
0
else
try
p
.
expectTypeExpr
()
;
const
init_node
:
Node
.
Index
=
if
(p
.
eatToken
(
.
equal)
==
null
)
0
else
try
p
.
expectExpr
()
;
return
p
.
addNode
(
.
{
.
tag
=
.
simple_var_decl
,
.
main_token
=
mut_token
,
.
data
=
.
{
.
lhs
=
type_node
,
.
rhs
=
init_node
,
}
,
})
;
}
This “eats” the first token: either
const
or
var
(this parse function is used for both). “Eating” the token means it is consumed: the current token is returned and the
tok_i
index in the parser state is incremented. If it isn’t
const
or
var
, the
null_node
value is returned which produces an error up the call chain (a variable declaration must start with
const
or
var
).
Next, we expect an
identifier
for the variable name. The
expectToken
function returns an error if the token is not an
identifier
. For example, if we did
var 32
then this is where the parser would create and store the error that it expected an identifier, but got an integer literal.
Next, we have a few potential realities. By using the conditional around
eatToken
, we can determine what to do next. If the next token is a colon, we expect to find a type expression. For example
var x: u32
. But type expressions are optional and our actual example doesn’t have one, so this will set
type_node
to zero.
We then check if the next token is an equal token. If so, we expect to find a variable initialization expression. Our variable declaration does have this, so this will create an AST node and return the index into the node list. We will not look at
expectExpr
.
Notice that this produces multiple valid variable declaration syntaxes, such as
var x
,
var x: i32
, and
var x: i32 = 42
. But also notice what is
not valid
, such as
var : i32 x
or
var = 32
.
Finally, we call
addNode
to create the
Node
. This returns the index into the node list. In this case, we create a
.simple_var_decl
. If you look at the comments for
.simple_var_decl
, it notes that the
lhs
points to the index of the type expression AST node (or zero if there was no type expression) and
rhs
points to the index of the initialization expression AST node (or zero if there was no initialization).
The
parseVarDecl
function returns the index to the
.simple_var_decl
AST node. This eventually is returned all the way back out to the
parseContainerMembers
function we started at and is stored in the scratch state. We’ll explain how this scratch state is used later. For now, the
while
loop continues parsing and looks for the next token, which is
.keyword_pub
for beginning our function definition.
Parsing a Function Definition
Once
.keyword_pub
is found, the call chain eventually leads to
parseFnProto
and
parseBlock
to parse our function prototype and body, respectively. Let’s focus in on
parseFnProto
since it does something we haven’t seen yet.
A simplified, incomplete version of
parseFnProto
is shown below:
fn
parseFnProto
(p
:
*
Parser)
!
Node
.
Index {
const
fn_token
=
p
.
eatToken
(
.
keyword_fn)
orelse
return
null_node
;
// We want the fn proto node to be before its children in the array.
const
fn_proto_index
=
try
p
.
reserveNode
()
;
_
=
p
.
eatToken
(
.
identifier)
;
const
params
=
try
p
.
parseParamDeclList
()
;
const
callconv_expr
=
try
p
.
parseCallconv
()
;
_
=
p
.
eatToken
(
.
bang)
;
const
return_type_expr
=
try
p
.
parseTypeExpr
()
;
if
(return_type_expr
==
0
) {
try
p
.
warn
(
.
expected_return_type)
;
}
return
p
.
setNode
(fn_proto_index
,
.
{
.
tag
=
.
fn_proto_one
,
.
main_token
=
fn_token
,
.
data
=
.
{
.
lhs
=
try
p
.
addExtra
(Node
.
FnProtoOne{
.
param
=
params
.
zero_or_one
,
.
callconv_expr
=
callconv_expr
,
})
,
.
rhs
=
return_type_expr
,
}
,
})
}
This is similar to parsing the variable declaration. There are a couple new patterns that emerge. First, you can see that if the return type isn’t set, a warning is stored rather than halting all of the parsing. Parsers often try to continue parsing in the face an error and this is one of those scenarios.
Next, the
lhs
value for the
fn_proto_one
tag is an index to the
extra_data
. This shows how the extra data is written. The
addExtra
function takes a struct with all the values, and encodes it into
extra_data
in a type safe way, then returns the index to the starting index in extra data. As we showed earlier, consumers of this AST node will know exactly how many fields to expect for a
fn_proto_one
tag and they can read this information.
Finalizing the AST
Parsing continues recursively for the entire program, constructing an AST node. At the end of the parse, the parser returns an
Ast
struct which is structured as shown below:
pub
const
Ast
=
struct
{
source
:
[
:
0
]
const
u8
,
tokens
:
TokenList
.
Slice
,
nodes
:
NodeList
.
Slice
,
extra_data
:
[]Node
.
Index
,
errors
:
[]
const
Error
,
}
;
At this point, if you’ve read the tokenization page and fully understand the anatomy of a parser and an AST node, each of these fields should make sense. The AST has the full source as
source
(used to determine identifier strings, error messages, etc.), the list of tokens as
tokens
, the list of AST nodes in
nodes
, the extra data for the AST nodes in
extra_data
, and a potential list of accumulated errors in
errors
.
Next is the
AstGen process
.
