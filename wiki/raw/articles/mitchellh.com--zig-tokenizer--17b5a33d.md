---
title: "Mitchell Hashimoto"
url: "https://mitchellh.com/zig/tokenizer"
fetched_at: 2026-05-01T07:02:03.999697+00:00
source: "mitchellh.com"
tags: [blog, raw]
---

# Mitchell Hashimoto

Source: https://mitchellh.com/zig/tokenizer

Table of Contents
Tokenization is the first step in a typical compiler pipeline. Tokenization is the process of converting a stream of bytes (the programming language syntax) into a stream of tokens.
Using Zig as an example, the syntax
comptime {}
is tokenized into
[.keyword_comptime, .l_brace, .r_brace]
. Tokenizers usually don’t handle
semantics
or whether a set of tokens are
meaningful.
For example,
comptime []
is not meaningful Zig syntax, but the tokenizer will happily turn that into
[.keyword_comptime, .l_bracket, .r_bracket]
. It is up to the
parser
(the next step after tokenization) to apply semantic meaning and error in invalid cases.
There are many ways to write a tokenizer. This page will focus on how Zig’s tokenizer works and does not aim to compare this to other ways to write the tokenizer.
The Zig Tokenizer
The Zig language tokenizer is part of the Zig standard library and is at
lib/std/zig/tokenizer.zig
and exposed as
std.zig.Tokenizer
. The tokenizer takes a slice of bytes as input and produces one token at a time until EOF. The tokenizer performs no allocations.
The basic usage is shown below, before we dive in to see how it works:
const
std
=
@import
(
"std"
)
;
const
expect
=
std
.
testing
.
expect
;
const
tok
=
std
.
zig
.
Tokenizer
.
init
(
"comptime {}"
)
;
try
expect
(tok
.
next
()
==
.
keyword_comptime)
;
try
expect
(tok
.
next
()
==
.
l_brace)
;
try
expect
(tok
.
next
()
==
.
r_brace)
;
try
expect
(tok
.
next
()
==
.
eof)
;
Some important properties of the tokenizer that are worth mentioning:
Operates on slices, not streams
- The tokenizer takes a
[:0] const u8
as input, not a reader. This means that for sufficiently large inputs, it is up to the caller to buffer and batch calls to the tokenizer. In practice, programming language inputs are not “sufficiently large” so the entire source file is tokenized at once; this is how Zig works today, too.
Does not allocate
- The tokenizer does not perform any heap allocation. In systems programming, it’s always useful to understand the memory usage and allocation properties of an API. Side note: with Zig, this is immediately obvious since the Tokenizer doesn’t take an
Allocator
as a parameter for anything.
The structure of the tokenizer is equally simple (as shown below). The tokenizer stores the buffer, the current index into the buffer (starts at zero), and a potential invalid token (will be ignored in this article).
pub
const
Tokenizer
=
struct
{
buffer
:
[
:
0
]
const
u8
,
index
:
usize
,
pending_invalid_token
:
?
Token
,
// ...
}
;
It should be apparent how a tokenizer functions with this state, even if you didn’t know anything about tokenizers. The tokenizer moves the index forward one byte at a time in the buffer and constructs a token.
Anatomy of a Token
With the high-level API of the tokenizer understood, the next question is: what is the anatomy of a token? In Zig, a token is the following structure:
pub
const
Token
=
struct
{
tag
:
Tag
,
loc
:
Loc
,
pub
const
Loc
=
struct
{
start
:
usize
,
end
:
usize
,
}
;
pub
const
Tag
=
enum
{
invalid
,
// ...
}
;
}
;
The
tag
field is an enum that represents all possible token types. Examples of tags are
.keyword_comptime, .l_brace, .r_brace, .eof
. At the time of writing, Zig has around 120 distinct tags.
Next, the location of the token is stored in the
loc
field which is comprised of a
start
and
end
index. Given these indices and the original source text (used to initialize the tokenizer), a caller can extract the text of the token using
source[tok.loc.start .. tok.loc.end]
. Storing only the start and end is a common efficiency trick.
The information given in the token is fundamental — a tag, a location — but the structure can vary between tokenizers. For example, the
Go tokenizer
models tokens as an int constant, and the
next()
equivalent function in Go returns the token int, position as an int byte offset, and the literal string capture of the token as distinct return values since Go supports multiple return values. This is more or less the same as Zig, but the subtle differences do have an important impact on compiler ergonomics and sometimes performance.
Finding the Next Token
The tokenizer returns one token at a time by calling the
next()
function.
This function starts at the current index into the buffer and looks at one byte at a time to construct the token. It uses a single
state
variable to implement a state machine in order to track what could possibly be next.
Before going through the actual states of the Zig tokenizer, let’s consider this approach at a high level. Let’s look at how the input
while
(including the space) would be tokenized.
First, a tokenizer would see the character
w
. At that point, we know it can’t be a number, but it could still be either a keyword or an identifier, so we don’t yet have a complete token. We only look one character at a time, so we grab the next one:
h
. This can still be an identifier or keyword, so we continue.
i
,
l
,
e
. Now, we have
while
, which we know is a keyword on its own, but this could
still
be an identifier because there can be more characters, so we have to look one more character forward. The next input is whitespace. We now definitively know that it is the
while
keyword, and not an identifier, and a token can be returned. If the next byte was a character such as
1
, we would know we’re constructing an identifier (incomplete) and that it would never be a keyword (no keyword starts with
while1
).
And that’s how the Zig tokenizer works. It maintains a current state (such as “we know we’re building an identifier or a keyword”) and looks one character at a time until it has unambiguously determined the token.
The tokenizer only looks at the state and the current character; it does not look backward, and it does not peek forward. Most tokenizers don’t. As noted in the beginning, a tokenizer is not concerned with semantics, so non-sensical inputs such as
if while comptime x = 7 { else }
produce a valid stream of tokens. It is up to the
parser
to take a stream of tokens and apply semantic meaning to it.
The Zig Implementation
The implementation of
next()
is done using nested whiles and switches. A snippet is shown below.
while
(
true
)
:
(self
.
index
+=
1
) {
const
c
=
self
.
buffer[self
.
index]
;
switch
(state) {
.
start
=>
switch
(c) {
'a'
...
'z'
,
'A'
...
'Z'
,
'_'
=>
{
state
=
.
identifier
;
result
.
tag
=
.
identifier
;
}
,
}
}
}
The first while is an infinite loop that continues forever, iterating one character at a time through the buffer. The loop body is expected to
break
when it finds a token or the buffer is empty. A nice property of Zig is that the type of
buffer
is
[:0] const u8
and that
:0
tells us that the buffer is guaranteed to end in a
0
byte, so we can look for that to break the loop.
Next, the tokenizer switches on the current
state
, which is an enum. Then, given a state, we switch on the current character to determine what to do next. In the snippet above, you can see how seeing the first character such as
A
would move the state to
.identifier
to build up an identifier.
From Tokens to Trees
The next phase of the compiler is the parser. The parser takes the stream of
tokens generated by
the tokenizer and converts it to a slightly more meaningful
abstract syntax tree. Continue reading about
the Zig parser
.
