---
title: "I Wrote 4,000 Lines of Code with ChatGPT in a Weekend"
url: "https://hyperbo.la/w/chatgpt-4000/"
fetched_at: 2026-04-29T07:02:15.609445+00:00
source: "hyperbola :: blog"
tags: [blog, raw]
---

# I Wrote 4,000 Lines of Code with ChatGPT in a Weekend

Source: https://hyperbo.la/w/chatgpt-4000/

On June 10 and June 11, 2023, I pair programmed with ChatGPT on
Artichoke
Ruby
. Artichoke Ruby is primarily written in Rust. Nearly all of the code I
wrote with ChatGPT is Rust code.
Together, we authored 10 PRs totalling to about 4,100 lines of code changed or
added:
To me, the most impressive thing we worked on together is
artichoke/artichoke#2605
, which is a 2000 line, 100% code coverage,
no_std
iterator for parsing the format string given to Ruby’s
String#unpack
API.
For a bit of context, I consider myself skeptical of AI. I think a lot of what I
hear about AI disruption tends toward hype over substance. For me, AI software
development is an unknown and I am somewhat uncertain about it and afraid of it.
So, much like I did with
Bazel last year
, I ran towards my fears
and got my hands dirty with AI.
Methodology
I used the beta / preview / free version of ChatGPT. The version string at the
bottom of the chat interface says:
Free Research Preview. ChatGPT may produce inaccurate information about
people, places, or facts.
ChatGPT May 24 Version
.
I write all my code locally in neovim with no plugins other than syntax
highlighting and rustfmt on save. I interacted with ChatGPT by copying code in
vim, pasting it into the chat window at
chat.openai.com
in Chrome, and copying
code back into vim when I was satisfied with it. I ran
cargo test
and
cargo clippy
in additional
tmux
panes as an input to the iteration we did
together.
Experience Report
The experience of working with ChatGPT was similar to pair programming with
another person.
Unlike
a pair programming partner, however, ChatGPT has no
ego, defers to directions it is given, and writes code rapidly. It
felt
like
collaborating. I exercised the parts of my brain I use when brainstorming in a
group and thinking out loud.
ChatGPT does a
great
job cranking out tests. It “understands” APIs of the
relevant modules and can infer expected behavior from documentation and other
similar code it has trained on.
ChatGPT is able to do more with more context. By pasting in bug reports and
impacted code, we were able to quickly fix bugs and write regression tests.
Sometimes, ChatGPT would get stuck on some part of the conversation. Often this
would manifest as responses taking over a minute to generate. In these cases, I
had to find ways to reset the conversation.
Prompt Engineering
One prompt engineering technique I used to great success was to prompt ChatGPT
for a code review and guide it toward making refactors to improve quality of
existing code.
Some early reviewers of the blog post asked for more depth around the
art form
🎨 of choosing the prompts I used. The remarkable thing here is I didn’t need to
spend much extra energy to come up with the prompts; the sessions felt like I
was shoulder surfing in a pair programming session. I spoke to ChatGPT like I
would any other engineer: I gave it requirements, and then more requirements, as
we went.
I ended up treating ChatGPT as a highly technical junior engineer: it knows a
lot but doesn’t know how to deploy that knowledge to solve a problem. The
prompts need to shape that corpus of knowledge into a solution. Ultimately, it
boils down to communicating clearly and directly.
Conversational Search
For example, hacking on the
Dockerfile
s that push
Artichoke nightlies to
Docker Hub
, I used ChatGPT as a conversational Google:
I opened the conversation with “I have a dockerfile that I’d like to improve”
and pasted the contents of the
Dockerfile
.
ChatGTP would summarize the content of the
Dockerfile
and make general
remarks on its quality.
I then prompted ChatGPT for help making some changes I had in mind:
We generated a
.dockerignore
for the repository. I was able to help it by
pasting the output of the
tree
command for the Git repository.
We added comments to clarify the struture of the
Dockerfile
.
We simplified some conditional
COPY
commands.
We added missing
org.opencontainers
labels.
We fixed a bug where the custom UID and GID for the non-root user exceeded the
standard max range for these IDs on Linux.
Our session turned into:
Starting from Scratch
Artichoke has a utility crate that parses
.inputrc
and determines which line
editing mode to configure its REPL with. This crate already exists, but I
started by prompting ChatGPT with the requirements:
write a rust function to parse a GNU Readline config to determine whether the
line editing mode is vi or emacs. The function should always return a value,
using the GNU readline default if no editing mode is found in the config. Use
an enum to represent the editing mode value. The function accepts
AsRef<[u8]>
as input
This is the (working!) code it gave me:
#[derive(
Debug
,
PartialEq
)]
enum
EditingMode
{
Vi
,
Emacs
,
}
fn
parse_readline_config
(config
:
impl
AsRef
<[
u8
]>)
->
EditingMode
{
let
config_bytes
=
config
.
as_ref
();
let
config_str
=
match
std
::
str
::
from_utf8
(config_bytes) {
Ok
(s)
=>
s,
Err
(_)
=>
return
EditingMode
::
Emacs
,
// Default to Emacs if config is not valid UTF-8
};
for
line
in
config_str
.
lines
() {
if
let
Some
(mode)
=
line
.
strip_prefix
(
"set editing-mode vi"
) {
if
mode
.
trim
()
.
is_empty
() {
return
EditingMode
::
Vi
;
}
}
}
EditingMode
::
Emacs
// Default editing mode
}
It described the logic in the function and output a nice example:
fn
main
() {
let
config
=
b"set editing-mode vi
\n
"
;
let
editing_mode
=
parse_readline_config
(config);
println!
(
"Editing mode: {:?}"
, editing_mode);
}
This is a great start but not quite what I was looking for, so we began to
iterate.
Prompt iteration
rewrite this function so it operates on arbitrary input that is not
necessarily valud UTF-8. do not convert the slice to a str
does this function handle excess whitespace like GNU Readline?
Add tests using a variety of inputrc files that you have seen before
do you know of any example inputrc files that contain invalid
set editing-mode
configs?
add tests for these cases
update the
let config
declarations in all tests to be string literals. this
will improve readability and still work because the function takes
AsRef<[u8]>
ensure all test cases cover both emacs and vi editing modes
add tests to ensure all types of POSIX locale space characters are correctly
ignored
these tests are incorrect. newlines should cause parsing to fail
can you write some tests that ensure input with invalid UTF-8 is handled
correctly?
add invalid UTF-8 tests to ensure lines with invalid UTF-8 sequences are
skipped
show me the entire test module
ensure the vi case is exercised when input contains invalid UTF-8. show the
whole test module after you add these tests
show me the tests again but rename
parse_readline_config
to
get_readline_edit_mode
. output only the tests
rename
EditingMode
to
EditMode
and output the tests again
you did not include all of the tests
show me more tests with invalid UTF-8 byte content
show me 15 tests with invalid UTF-8 content. should include cases for emacs
and vi editing modes, multiple line configs, with invalid UTF-8 content at
different places in the config directives
only output tests for invalid UTF-8 configs
write me three integration tests. they should all contain multi-line inputrc
files. the editing mode directive should be in a different place in the config
in each test
change these tests so the editing-mode directive does not appear in the test
config, start numbering the integration tests at 4
is this a valid editing-mode directive?
set editing-mode "vi"
add tests to to check for proper handling of case insensitivity
show me tests that ensure quotes are rejected in editing mode
ensure the tests cover the emacs case
these tests show that quoted values are allowed. is that correct?
generate tests for the following function, ensuring full branch coverage […]
how does GNU Readline behave if a set directive appears multiple times in
inputrc?
generate some tests that ensure the last editing-mode directive is used
modify
get_readline_edit_mode
so the tests pass. include comments that
reference this behavior of
set
can you add other helpful comments to this function such as how whitespace and
case insensitivity are handled?
write a sample comment that indicates the
vi
and
emacs
values of the
set
directive are case insensitive
Our session turned into:
I was able to leverage ChatGPT’s deeper knowledge about the GNU Readline config
file to handle some additional edge cases. I have a
boatload
more tests than
before.
Asking for Code Review
Artichoke is a Cargo workspace with about 20 crates in it. Many of these crates
are small and implement one data structure (like
spinoso-securerandom
,
Artichoke’s data structures and routines for Ruby’s
SecureRandom
module) or
one collection of related utilities (like
scolapasta-path
for interacting with
Rust’s
Path
and
OsStr
types).
By virtue of many of these crates being small and edges in the functionality
DAG, we can cheat and just paste the whole crate or module into the prompt! I
did just that for
scolapasta-hex
, a
no_std
hex encoding library with an
Iterator
-based API.
I have a Rust implementation of a hex encoding and decoding library. In the
next message I will paste the code for this crate. Once I paste the code,
please give a code review, suggest APIs that are missing, tests that could be
added, or performance improvements that could be made. Do you understand?
There are limitations to this. The prompt dies if you give it too much code and
kills the session. I didn’t measure, but above 1000 lines in a single paste was
around the threshold.
Now for the truly amazing part:
what tests are missing from this code to ensure 100% branch coverage?
Which yielded:
To determine the missing tests for achieving 100% branch coverage in the
provided code, we can analyze the code and identify the branches that have not
been covered yet. Here are the branches that require additional tests:
The branch in the
next
method of the
Hex
iterator when there is a
remaining
EscapedByte
iterator. This branch is taken when
escaped_byte.next()
returns
None
.
The branch in the
next
method of the
Hex
iterator when there is no
remaining
EscapedByte
iterator, and there is a byte remaining in the
underlying byte slice.
The branch in the
next
method of the
Hex
iterator when there is no
remaining
EscapedByte
iterator, and there are no bytes remaining in the
underlying byte slice.
The branch in the
is_empty
method of the
Hex
iterator when there is a
remaining
EscapedByte
iterator.
The branch in the
is_empty
method of the
Hex
iterator when there is no
remaining
EscapedByte
iterator, and there are bytes remaining in the
underlying byte slice.
The branch in the
is_empty
method of the
Hex
iterator when there is no
remaining
EscapedByte
iterator, and there are no bytes remaining in the
underlying byte slice.
By adding tests that cover these branches, you should be able to achieve 100%
branch coverage for the provided code.
And then one-by-one we wrote the tests.
Our session turned into:
Working with API Prototypes
Hacking on Version 4 UUID generation with ChatGPT started with this prompt:
I have a function in Rust to generate V4 UUIDs with the following signature:
pub
fn
v4
()
->
Result
<
String
,
Error
>;
can you help me write tests for it?
It gave me this:
#[cfg(test)]
mod
tests
{
use
super
::*
;
#[test]
fn
test_v4_returns_valid_uuid
() {
let
result
=
v4
();
assert!
(result
.
is_ok
(),
"Expected Ok result"
);
let
uuid
=
result
.
unwrap
();
// Validate the UUID format
assert_eq!
(uuid
.
len
(),
36
,
"UUID length should be 36 characters"
);
assert_eq!
(
&
uuid[
8
..
9
],
"-"
,
"Invalid UUID format"
);
assert_eq!
(
&
uuid[
13
..
14
],
"-"
,
"Invalid UUID format"
);
assert_eq!
(
&
uuid[
18
..
19
],
"-"
,
"Invalid UUID format"
);
assert_eq!
(
&
uuid[
23
..
24
],
"-"
,
"Invalid UUID format"
);
// Validate that the UUID is version 4
assert_eq!
(
&
uuid[
14
..
15
],
"4"
,
"Invalid UUID version"
);
// Validate that the non-hyphen positions are lowercase ASCII alphanumeric characters
assert!
(uuid
.
chars
()
.
enumerate
()
.
all
(
|
(i, c)
|
{
if
i
==
8
||
i
==
13
||
i
==
18
||
i
==
23
{
c
==
'-'
}
else
{
c
.
is_ascii_lowercase
()
&&
c
.
is_ascii_alphanumeric
()
}
}),
"Non-hyphen positions should be lowercase ASCII alphanumeric"
);
// Additional validation if necessary
// ...
}
// Add more test cases if necessary
// ...
}
This is a great start, but I can see some problems with this test. I was also
interested in expanding on the “additional validation” and “more test cases”
comments in the code.
Prompt iteration
can you expand to add additional validation? ensure the non-hyphen positions
in the returned string are lowercase ASCII alphanumeric
this assertion is too permissive. it allows
-
to appear in places where
alphanumeric characters are required
does this test properly reject strings that contain ASCII characters like
x
and
j
?
write a
matches!
macro invocation that tests a char named
c
matches all
ASCII numeric and lowercase hex characters
After the above iteration, I cleaned up the code in my editor and prompted with:
after cleaning up your suggestion I ended up with this test:
#[cfg(test)]
mod
tests
{
use
super
::*
;
#[test]
fn
test_v4_returns_valid_uuid
() {
for
_
in
0
..
1024
{
let
uuid
=
v4
()
.
unwrap
();
// Validate the UUID format
assert_eq!
(uuid
.
len
(),
36
,
"UUID length should be 36 characters"
);
assert_eq!
(
&
uuid[
8
..
9
],
"-"
,
"Invalid UUID format"
);
assert_eq!
(
&
uuid[
13
..
14
],
"-"
,
"Invalid UUID format"
);
assert_eq!
(
&
uuid[
18
..
19
],
"-"
,
"Invalid UUID format"
);
assert_eq!
(
&
uuid[
23
..
24
],
"-"
,
"Invalid UUID format"
);
// Validate that the UUID is version 4
assert_eq!
(
&
uuid[
14
..
15
],
"4"
,
"Invalid UUID version"
);
// Validate that the non-hyphen positions are lowercase ASCII alphanumeric characters
for
(idx, c)
in
uuid
.
chars
()
.
enumerate
() {
if
matches!
(idx,
8
|
13
|
18
|
23
) {
assert_eq!
(c,
'-'
,
"Expected hyphen at position {idx}"
);
}
else
{
assert!
(
matches!
(c,
'0'
..=
'9'
|
'a'
..=
'f'
),
"Character at position {idx} should match ASCII numeric and lowercase hex"
);
}
}
}
// Additional validation if necessary
// ...
}
// Add more test cases if necessary
// ...
}
what additional validation do you suggest?
And got these great suggestions back, which we wrote one-by-one with additional
prompting:
Your test looks good, covering the basic validations for UUID format, version,
and character constraints. As for additional validation, you could consider
the following:
Validate the uniqueness of generated UUIDs: Since UUIDs are intended to be
unique, you could store the generated UUIDs in a set or a hashmap and
ensure that each generated UUID is unique within the test loop. This can
help catch any unexpected duplicates in the generated UUIDs.
Test the generation of a large number of UUIDs: The current test runs for
1024 iterations, which is a good start. However, you can consider
increasing the number of iterations to test the performance and correctness
of the
v4
function over a larger sample size.
Test edge cases or special scenarios: UUIDs have certain variations and use
cases, such as nil UUIDs, reserved variants, or UUIDs with specific
timestamp or node values. You can create additional test cases to cover
these scenarios if they are relevant to your use case.
Test the error case: Currently, your test assumes that
v4
will always
succeed in generating a valid UUID. However, it may be worth adding a test
case to explicitly test the error condition when the generation of a UUID
fails.
Remember that additional validation depends on your specific requirements and
the usage of UUIDs in your application. You can adapt and expand the tests
based on the desired behavior and constraints of your UUID generation
function.
Let me know if you need further assistance!
We continued:
can you write a test that validates the uniqueness of generated UUIDs?
write a separate test to check for uniqueness
how many iterations do you suggest using in these tests?
can you add a comment to the following constant declaration explaining the
rationale for choosing a high iteration count?
const
ITERATIONS
:
usize
=
10240
;
can you generate a documentation comment for the
v4
function? Include an
example section similar to the docs in rust
std
. Include an errors section
that indicates the function returns an error if the operating system’s source
of randomness returns an error.
change the import to
spinoso_securerandom::uuid
place the errors section last. wrap the example in a function (with the
function definition hidden) so
?
can be used on the error instead of calling
expect
add a sentence that references the relevant RFC and include a link
add some more test cases
write an assertion that the UUID is all ASCII characters
write a test that all UUIDs are ASCII-only. use a loop with the iterations
constant
I have a constant defined like this:
const
OCTETS
:
usize
=
16
;
can you write a comment for it and cite the RFC? refer to specific language in
the RFC
can you write a similar doc comment for this constant:
const
ENCODED_LENGTH
:
usize
=
36
;
Once we were done, we made some changes to internal documentation of this module
and I realized we had no test for the invariants around
clock_seq_hi_and_reserved
in Version 4 UUIDs. ChatGPT struggled to write this
test with the bit arithmetic, but it gave me a skeleton that I was able to
quickly make changes to.
add a test for the bit manipulations in
v4
to justify this comment:
// Per RFC 4122, Section 4.4, set bits for version and `clock_seq_hi_and_reserved`.
Our session turned into:
Removing the tedium from writing out the test cases allowed me to focus on the
requirements
for those test cases, which led to testing more invariants about
the Version 4 UUID format.
Fixing Bugs
I tried to work on fixing a bug:
scolapasta-path
incorrectly mutates verbatim
paths on Windows
artichoke/artichoke#2567
.
The prompt is a refined version of the bug report with the affected code:
I have a function which “normalizes” slashes in a Rust Path to convert
\
to
/
on Windows, shown below. This function is buggy in that it does should,
but does not, leave the path as is if the path is a “verbatim” path:
pub
fn
normalize_slashes
(path
:
PathBuf
)
->
Result
<
Vec
<
u8
>,
PathBuf
> {
let
mut
buf
=
OsString
::
from
(path)
.
into_string
()
?.
into_bytes
();
for
byte
in
&mut
buf {
if
*
byte
==
b'
\\
'
{
*
byte
=
b'/'
;
}
}
Ok
(buf)
}
can you fix this code?
With one additional clarification that ChatGPT should avoid unnecessary
allocations, the core of the fix was made with tests for various verbatim paths.
The code as given did not compile, and I took 5 minutes to fix it up while
refering to the Rust
std
docs.
Our session turned into:
I developed this bit of Windows-specific code on macOS. It ran and passed tests
the first time in CI with ChatGPT’s help without having been run locally while
iterating.
Writing a Parser from Scratch
The ✨
amaze
✨ moment for me was when I tried to push things in
artichoke/artichoke#2605
.
String#unpack
and
Array#pack
are two APIs that implement binary
de/serialization in Ruby Core. These APIs take a
format string
which is a
sequence of directives that instruct the de/serializer how to process the source
data.
Artichoke currently supports these APIs and a limited subset of the directives
via the mruby core it is slowly
strangling
and
oxidizing
. Specifically,
these APIs are one of the few remaining native mruby mrbgems that Artichoke
still depends on
.
This was the most challenging PR to put together of the set this blog post
discusses because we started with the least amount of context; we had no
existing code. This PR was generated in a single ChatGPT chat session with
upwards of 500 prompts.
I made an early mistake of starting with a general question:
can you explain the rules for Ruby’s
String#unpack
function, including ALL
specifiers
I got a decent description of the most common specifiers back, but I did not set
boundaries on what I needed ChatGPT to focus on. Interestingly, ChatGPT
correctly associated the specifiers to their correct deseralization.
ChatGPT’s summary of
String#unpack
Certainly! The
String#unpack
method in Ruby allows you to convert binary
data stored in a string into a more readable format. It takes a formatting
string as an argument, which consists of specifiers that define how the data
should be unpacked. Here are the most commonly used specifiers:
Integer Specifiers:
C
or
c
: Unpacks a one-byte unsigned (
C
) or signed (
c
) integer.
S
or
s
: Unpacks a two-byte unsigned (
S
) or signed (
s
) integer
using little-endian byte order.
L
or
l
: Unpacks a four-byte unsigned (
L
) or signed (
l
) integer
using little-endian byte order.
Q
or
q
: Unpacks an eight-byte unsigned (
Q
) or signed (
q
) integer
using little-endian byte order.
Float Specifiers:
E
or
e
: Unpacks a four-byte single-precision float using
little-endian byte order.
G
or
g
: Unpacks an eight-byte double-precision float using
little-endian byte order.
String Specifiers:
A
or
a
followed by a number: Unpacks a string of specified length,
padding with spaces (
A
) or null bytes (
a
).
Miscellaneous Specifiers:
x
or
X
followed by a number: Skips the specified number of bytes
(
x
) or backs up (
X
) the specified number of bytes.
@
followed by a number: Skips to the specified position in the string.
These are the basic specifiers used in
String#unpack
, but there are
additional variations and options available. For more advanced usage and
additional specifiers, you can refer to the official Ruby documentation for
String#unpack
.
After this, we got right to generating code:
show me a Rust function which accepts a byte slice of string contents as
AsRef<[u8]>
and an unpack pattern as a
&[u8]
. Implement support for the
specifiers you mentioned. Make an enum for the various return types. Return a
vec or an error if a malformed unpack pattern is given
ChatGPT gave me roughly 150 lines of code that
looked
plausible but was not
exhausive, did not parse repetition patterns out of the format string (e.g.
Q8C*
), and mixed parsing of the directives with unpacking the contents.
What followed was about an hour of going back and forth with me attempting to
refine ChatGPT’s output by pasting more and more context from the Ruby
documentation and examples. We weren’t making much progress so I took a break.
After a coffee, I used a prompt which I leaned on a lot in this session:
forget all code we have discussed so far. please acknowledge
At this point, I transitioned from attempting to implement the algorthim “top
down” to “bottom up”. We focused on the data model and defining the enums that
represented the parsed stream of formatting directives. This time we were
starting on a constrained problem and I pasted in the ASCII table of format
specifiers to begin:
String#unpack
format directives prompt
Integer       |         |
Directive     | Returns | Meaning
------------------------------------------------------------------
C             | Integer | 8-bit unsigned (unsigned char)
S             | Integer | 16-bit unsigned, native endian (uint16_t)
L             | Integer | 32-bit unsigned, native endian (uint32_t)
Q             | Integer | 64-bit unsigned, native endian (uint64_t)
J             | Integer | pointer width unsigned, native endian (uintptr_t)
|         |
c             | Integer | 8-bit signed (signed char)
s             | Integer | 16-bit signed, native endian (int16_t)
l             | Integer | 32-bit signed, native endian (int32_t)
q             | Integer | 64-bit signed, native endian (int64_t)
j             | Integer | pointer width signed, native endian (intptr_t)
|         |
S_ S!         | Integer | unsigned short, native endian
I I_ I!       | Integer | unsigned int, native endian
L_ L!         | Integer | unsigned long, native endian
Q_ Q!         | Integer | unsigned long long, native endian (ArgumentError
|         | if the platform has no long long type.)
J!            | Integer | uintptr_t, native endian (same with J)
|         |
s_ s!         | Integer | signed short, native endian
i i_ i!       | Integer | signed int, native endian
l_ l!         | Integer | signed long, native endian
q_ q!         | Integer | signed long long, native endian (ArgumentError
|         | if the platform has no long long type.)
j!            | Integer | intptr_t, native endian (same with j)
|         |
S> s> S!> s!> | Integer | same as the directives without ">" except
L> l> L!> l!> |         | big endian
I!> i!>       |         |
Q> q> Q!> q!> |         | "S>" is the same as "n"
J> j> J!> j!> |         | "L>" is the same as "N"
|         |
S< s< S!< s!< | Integer | same as the directives without "<" except
L< l< L!< l!< |         | little endian
I!< i!<       |         |
Q< q< Q!< q!< |         | "S<" is the same as "v"
J< j< J!< j!< |         | "L<" is the same as "V"
|         |
n             | Integer | 16-bit unsigned, network (big-endian) byte order
N             | Integer | 32-bit unsigned, network (big-endian) byte order
v             | Integer | 16-bit unsigned, VAX (little-endian) byte order
V             | Integer | 32-bit unsigned, VAX (little-endian) byte order
|         |
U             | Integer | UTF-8 character
w             | Integer | BER-compressed integer (see Array#pack)
Float        |         |
Directive    | Returns | Meaning
-----------------------------------------------------------------
D d          | Float   | double-precision, native format
F f          | Float   | single-precision, native format
E            | Float   | double-precision, little-endian byte order
e            | Float   | single-precision, little-endian byte order
G            | Float   | double-precision, network (big-endian) byte order
g            | Float   | single-precision, network (big-endian) byte order
String       |         |
Directive    | Returns | Meaning
-----------------------------------------------------------------
A            | String  | arbitrary binary string (remove trailing nulls and ASCII spaces)
a            | String  | arbitrary binary string
Z            | String  | null-terminated string
B            | String  | bit string (MSB first)
b            | String  | bit string (LSB first)
H            | String  | hex string (high nibble first)
h            | String  | hex string (low nibble first)
u            | String  | UU-encoded string
M            | String  | quoted-printable, MIME encoding (see RFC2045)
m            | String  | base64 encoded string (RFC 2045) (default)
|         | base64 encoded string (RFC 4648) if followed by 0
P            | String  | pointer to a structure (fixed-length string)
p            | String  | pointer to a null-terminated string
Misc.        |         |
Directive    | Returns | Meaning
-----------------------------------------------------------------
@            | ---     | skip to the offset given by the length argument
X            | ---     | skip backward one byte
x            | ---     | skip forward one byte
Even this was too much for ChatGPT to digest: it would drop directives, it would
invent directives, it would mismatch directive characters to values.
I continued to break down the problem further: we made one enum at a time for
each section of the table (i.e. one for
IntegerDirective
s, one for
FloatDirective
s, etc.). This narrowed scope got ChatGPT to “focus”. We got all
of the enums written. Then I spent the next 30 minutes playing around with the
documentation on the enums until they were all consistently formatted in a way
that I liked.
I tried combining all of this code into the prompt as it all lived in
lib.rs
locally, but ChatGPT continued to mix up the directives. I tried a new trick to
help ChatGPT learn the relationship between the entities. I refactored the crate
to have multiple modules and fed ChatGPT this prompt:
no need to show me the code. I’ll give you what we’ve worked on together so
far. I’ll show you the files in the crate. Ask me what is in each file and
I’ll show it to you.
$ tree
.
.
├── Cargo.toml
└── src
├── directive
│   ├── float.rs
│   ├── integer.rs
│   ├── misc.rs
│   └── string.rs
├── directive.rs
├── lib.rs
└── repetition.rs
3 directories, 8 files
The files in
crate::directive
are highly regular, full of the same code
structure and patterns.
ChatGPT asked me for some files like this:
Great! Please show me the contents of each file in the crate. We can start
with
src/directive.rs
.
which I obliged by
cat
’ing them in our pretend console session.
From here we quickly implemented
TryFrom
and
fmt::Display
for all enums.
An interesting thing about getting to this point was that most of the work to
get ChatGPT to do what I wanted led to me more deeply understanding the problem
I was trying to solve.
For example, the directive
S!>
is not a special multi-ASCII character
directive.
S
is the directive and
!
and
>
are
modifiers
which say:
Use the platform-specific type for this integer (i.e.
short
instead of
uint16_t
).
Parse that
short
with big endian byte order.
Now that
I
understood this, going back to ChatGPT to write up the routine to
parse integer directives was as simple as telling it to implement these APIs:
IntegerDirective::modify_little_endian
IntegerDirective::modify_big_endian
IntegerDirective::modify_platform_specific
The repetitive nature of the enums and their documentation we defined earlier
allowed ChatGPT to implement these parts of the state machine without issue on
the first attempt.
Our session turned into:
User Experience
Looking back on the weekend’s worth of work, I was very productive; however the
process of collaborating with ChatGPT was tedious.
Some things I liked:
Because we were collaborating outside of my editor, I was in control of what
code was accepted and what additional context I fed to ChatGPT.
The conversational interface was easy to use, it was easy to type out a
sentence or two of instructions without thinking too much.
Being able to stop generation part-way through a response allowed me to
clarify the prompt quickly.
Some things I didn’t like:
Copying and pasting was tedious, especially if I only wanted part of the
generated output.
I would have liked the ability to hot reload the my current blessed state of
the code into the conversation.
It was difficult to refer to earlier parts of the conversation to either purge
them from ChatGPT’s context or reinforce them as important. Maybe something
like the numbered cells in a Jupyter notebook or pinning prompts and responses
would be helpful here.
I had to take breaks if the session went longer than an hour because pairing
like this was mentally taxing.
AI Agents
The prompting techniques I used had the rough effect of turning each chat
session into an AI agent expert in the particular code we were hacking on.
Dreaming big, I’d love to see a workflow in the future where I can use off the
shelf agents and bring them into a session. Give me agents like:
A Rust agent trained on the
standard library API documentation
,
Rust’s release notes, the
Rust Performance Book
, and the
nomicon
.
One agent each for every crate that appears in my project’s
Cargo.toml
s.
Train it on the API docs, the commit history, the code, GitHub discussions,
GitHub Issues, and PRs.
An agent for the Ruby Core and Standard Library API documentation.
An agent trained on every
Ruby Spec
.
An agent for my local codebase, its commit history, PRs, and issues.
I’d love to talk to all of these agents in a chat interface on my local machine
separately from my editor. Let’s see if we get there someday.
