---
title: "Rusty thoughts on \"Parse, don't validate\""
url: "https://eli.thegreenplace.net/2026/rusty-thoughts-on-parse-dont-validate/"
fetched_at: 2026-09-27T10:01:13.791077+00:00
source: "eli.thegreenplace.net"
tags: [blog, raw]
---

# Rusty thoughts on "Parse, don't validate"

Source: https://eli.thegreenplace.net/2026/rusty-thoughts-on-parse-dont-validate/

September 26, 2026 at 08:25
Tags
Rust
Like many programmers, I find Alexis King's
Parse, don't validate
article fascinating, because it gives a name to an idiom that seems familiar and
important - one I've observed and used in the past without naming it explicitly.
This post is a review of the "Parse, don't validate" pattern applied to the Rust
programming language (the original post uses Haskell). I was particularly
interested in finding educational examples of this pattern in the Rust standard
library and other well-known projects.
Without repeating the original article (please read it first!), here's the
gist of it.
Consider the venerable
Vec
; its
first
method returns
Option<&T>
.
Why? Because a vector is not guaranteed to have any elements in it, so what
to do if
first
is invoked on an empty one? Returning an
Option
in this
case is idiomatic in Rust , with convenient syntax sugar for accepting
the result of functions that return
Option
and deciding what to do next.
So what's the issue?
Imagine we have a function to read some configuration paths from an env var,
while enforcing the invariant that the list can't be empty:
use
anyhow
::
{
Result
,
ensure
};
fn
get_configuration_directories
()
->
Result
<
Vec
<
PathBuf
>>
{
let
value
=
env
::
var
(
"CONFIG_DIRS"
).
context
(
"could not read CONFIG_DIRS"
)
?
;
let
directories
:
Vec
<
PathBuf
>
=
value
.
split
(
','
)
.
map
(
str
::
trim
)
.
map
(
PathBuf
::
from
)
.
collect
();
ensure
!
(
!
directories
.
is_empty
(),
"empty CONFIG_DIRS"
);
Ok
(
directories
)
}
So far, so good. Now let's take a typical usage of this function:
fn
main
()
->
Result
<
()
>
{
let
config_dirs
=
get_configuration_directories
()
?
;
match
config_dirs
.
first
()
{
Some
(
cache_dir
)
=>
initialize_cache
(
cache_dir
),
None
=>
unreachable!
(
"already checked that CONFIG_DIRS is non-empty"
),
}
Ok
(())
}
Once
get_configuration_directories
returns a successful result,
we are guaranteed that the vector isn't empty. And yet, if we want to get the
first element of this vector, we have to use the
first
method that returns
Option<&T>
. We are therefore forced - again - to handle a potentially
empty case (where the option is
None
).
As the original article states, this has a number of problems with code clarity,
potential performance implications and a ticking time bomb if the invariant
is ever changed in
get_configuration_directories
.
The core issue is that
Vec
is fundamentally a type that can be empty; we
can carry along a "This one can't be empty, pinky promise!" comment on all the
relevant code, but it's not formally checked by anything.
A type for "non-empty" vector
The solution is leveraging the type system to enforce a newly established
invariant. We can use a separate type for "a vector that cannot be empty";
in fact, such types already exist in several Rust crates - for example
nonempty
:
pub
struct
NonEmpty
<
T
>
{
pub
head
:
T
,
pub
tail
:
Vec
<
T
>
,
}
This type has no constructor that permits "no elements"; its
new
takes
one element, and its
first
method returns
&T
without an
Option
:
pub
const
fn
new
(
e
:
T
)
->
Self
{
Self
::
singleton
(
e
)
}
pub
const
fn
singleton
(
head
:
T
)
->
Self
{
NonEmpty
{
head
,
tail
:
Vec
::
new
(),
}
}
pub
const
fn
first
(
&
self
)
->
&
T
{
&
self
.
head
}
The rest of the crate deals with making
NonEmpty
behave as close as possible
to a normal
Vec
, by implementing many useful traits, as well as conversions
like:
pub
fn
from_vec
(
mut
vec
:
Vec
<
T
>
)
->
Option
<
NonEmpty
<
T
>>
{
if
vec
.
is_empty
()
{
None
}
else
{
let
head
=
vec
.
remove
(
0
);
Some
(
NonEmpty
{
head
,
tail
:
vec
})
}
}
Let's see how our
get_configuration_directories
function would look if it
returned a
NonEmpty
instead of a plain
Vec
:
fn
get_configuration_directories
()
->
Result
<
NonEmpty
<
PathBuf
>>
{
let
value
=
env
::
var
(
"CONFIG_DIRS"
).
context
(
"could not read CONFIG_DIRS"
)
?
;
let
directories
=
value
.
split
(
','
)
.
map
(
str
::
trim
)
.
map
(
PathBuf
::
from
)
.
collect
();
let
Some
(
directories
)
=
NonEmpty
::
from_vec
(
directories
)
else
{
bail
!
(
"CONFIG_DIRS cannot be empty"
);
};
Ok
(
directories
)
}
Note the use of
NonEmpty::from_vec
here - this is where the invariant is
established. Now a successful result is
NonEmpty
, not just
Vec
. The
client code looks like:
fn
main
()
->
Result
<
()
>
{
let
config_dirs
=
get_configuration_directories
()
?
;
initialize_cache
(
config_dirs
.
first
())
?
;
Ok
(())
}
There's no need to check if the returned value is empty again; this is enforced
by the type system!
This is where the parse vs. validate terminology of the original article comes
from. When
get_configuration_directories
returned a
Vec
, it simply
validated it. But when it returns a
NonEmpty
- the vector is transformed
into another entity which carries additional meaning. If we treat the concept
of parsing in the most generic sense - "transforming data from one format to
another", this fits.
To mention a less artificial example, the
Rust rewrite of core POSIX utilities
uses
NonEmpty
in several places . For example, when constructing a
shell pipeline:
pub
struct
Pipeline
{
pub
commands
:
NonEmpty
<
Command
>
,
pub
negate_status
:
bool
,
}
The command parser's code:
fn
parse_pipeline
(
&
mut
self
,
alias_table
:
&
AliasTable
)
->
ParseResult
<
Option
<
Pipeline
>>
{
// pipeline = "!" command ("|" linebreak command)*
let
negate_status
=
self
.
match_alternatives
(
&
[
CommandToken
::
Bang
])
?
.
is_some
();
let
mut
commands
=
if
let
Some
(
command
)
=
self
.
parse_command
(
alias_table
)
?
{
NonEmpty
::
new
(
command
)
}
else
{
return
Ok
(
None
);
};
// ...
A valid
Pipeline
is only returned if there are some commands in the
parsed AST. Otherwise, it just returns
None
. Once this is done, the client
code can use
commands.first()
without having to worry about the
possibility of it returning
None
.
Gradual parsing and type refinement
A somewhat more interesting example can be found in the source code of
rust-analyzer
. This project
has a type that represents an absolute filesystem path:
pub
struct
AbsPathBuf
(
Utf8PathBuf
);
Instead of carrying around a regular path, the absoluteness is recorded in
the type once the initial parsing and validation is done:
impl
TryFrom
<
Utf8PathBuf
>
for
AbsPathBuf
{
type
Error
=
Utf8PathBuf
;
fn
try_from
(
path_buf
:
Utf8PathBuf
)
->
Result
<
AbsPathBuf
,
Utf8PathBuf
>
{
if
!
path_buf
.
is_absolute
()
{
return
Err
(
path_buf
);
}
Ok
(
AbsPathBuf
(
path_buf
))
}
}
Subsequent code doesn't have to validate the the path is absolute. The type
enforces it.
Note also that
AbsPathBuf
wraps
Utf8PathBuf
, not
PathBuf
.
Utf8PathBuf
is itself a custom, "parsed" type refinement from the
camino crate
. Regular paths in the
Rust standard library aren't guaranteed to be valid UTF-8, so they cannot be
easily converted to a
String
(which has to be valid UTF-8 in Rust);
camino::Utf8PathBuf
establishes validity on construction, and can then
be converted to a string with just:
fn
as_str
(
&
self
)
->
&
str
{
..
.
}
So we have an example of gradual parsing and type refinement here:
std::path::PathBuf

      |
      |   prove UTF-8
      |
      V

camino::Utf8PathBuf

      |
      |   prove absolute
      |
      V

rust-analyzer's paths::AbsPathBuf
Non-zero integers
Rust has a generic type called
NonZero
,
to describe unsigned numeric quantities that are known to be non-zero.
For example,
thread::available_parallelism
is defined as:
pub
fn
available_parallelism
()
->
Result
<
NonZero
<
usize
>>
If the call is successful, it returns a
NonZero<usize>
, which is like
a normal
usize
with the restriction that it's not zero. Client code doesn't
have to keep checking whether the parallelism is 0 - it's enshrined in the type
system.
Rust defines the
division operator
with
NonZero<usize>
in the denominator as an operation that "cannot panic".
NonZero
has an additional advantage: zero is an invalid value for the
type, so Rust can use the zero bit pattern to represent
None
. Consequently,
Option<NonZeroUsize>
is
guaranteed to have the same size
and alignment as
NonZeroUsize
itself (and as
usize
). This can avoid the extra storage
that an
Option<usize>
would generally require.
Parsing JSON
A common example of the "parse, don't validate" idiom appears in deserializing
data from a JSON string. Rust's
serde
crate enables us to do the parsing,
with validated decisions encoded into the type system, e.g.:
#[derive(Debug, Deserialize)]
struct
Config
{
name
:
String
,
workers
:
NonZeroUsize
,
mode
:
Mode
,
}
#[derive(Debug, Deserialize)]
#[serde(rename_all =
"snake_case"
)]
enum
Mode
{
Fast
,
Safe
,
}
And then later:
let
input
=
r#"
{
"name": "compiler",
"workers": 4,
"mode": "fast"
}
"#
;
let
config
:
Config
=
serde_json
::
from_str
(
input
)
?
;
There is a lot happening behind the scenes:
The types of all fields are enforced (e.g. "name" cannot be an array).
The
mode
is validated to be one of the enum values of
Mode
.
workers
is validated to be a non-zero integer, because of the
NonZeroUsize
field type.
We take code like this for granted these days, but it's still a great example
of the pattern discussed in this post. Once the parser converted
mode
into
the
Mode
enum, no further validation is required.
In dynamic languages like Python and JS, the process is usually much more
manual. Python's
json.loads
gives us a dictionary, and it's up to the user
to validate its contents. Libraries like Pydantic permit an approach closer to
Rust's, but they're not universally used.
