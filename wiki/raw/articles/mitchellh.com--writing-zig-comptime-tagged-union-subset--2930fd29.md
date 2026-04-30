---
title: "Tagged Union Subsets with Comptime in Zig"
url: "https://mitchellh.com/writing/zig-comptime-tagged-union-subset"
fetched_at: 2026-04-30T07:01:53.808396+00:00
source: "mitchellh.com"
tags: [blog, raw]
---

# Tagged Union Subsets with Comptime in Zig

Source: https://mitchellh.com/writing/zig-comptime-tagged-union-subset

Zig supports tagged unions
1
and the Zig compiler will error if you
switch
on a tagged union without handling all possible cases. This is a great feature
because it helps you avoid bugs when new cases are added to the union. Many
languages support similar functionality.
However, sometimes you want to work with a subset of the tagged union.
You don't want to lose compiler safety by using catch-all cases in your
switch
statement, but you also don't want to handle every case with a noop.
In this post, I'll illustrate a real world example of this scenario and how
Zig's comptime can be used to elegantly solve it. The real world example
will come from
my terminal project
.
A Real Example: Keybind Actions
The following is how keybind actions are represented in
Ghostty
. A keybind action is the action that a keyboard
shortcut triggers. For example:
ctrl+n
might trigger the action to
open a new window.
pub
const
Action
=
union
(
enum
) {
quit
:
void
,
new_window
:
void
,
close_window
:
void
,
close_all_windows
:
void
,
open_config
:
void
,
reload_config
:
void
,
scroll_lines
:
i16
,
// Many more in reality, but we'll use the above for this blog post.
}
;
Most keybinding actions have no data associated with them (
void
) but
some do. For example, the
scroll_lines
action has an
i16
associated
with it to specify the number of lines up (negative) or down (positive)
to scroll.
This tagged union approach is nice because in the part of the code
that executes keybind actions, I can
switch
on the
Action
union
and the compiler will error if I don't handle all cases. This ensures that
when I add a new keybind action, I also add the code to handle it.
pub
fn
performAction
(action
:
Action)
void
{
switch
(action) {
.
quit
=>
...,
.
new_window
=>
...,
.
close_window
=>
...,
.
close_all_windows
=>
...,
.
open_config
=>
...,
.
reload_config
=>
...,
.
scroll_lines
=>
|
amount
|
...,
}
}
This is how Ghostty initially implemented keybind actions.
The Case for Union Subsets
Recently, I needed to add a new keybind action that was scoped not
to a specific terminal but to the entire Ghostty application. As part of this,
I wanted to refactor out
performAction
so that the terminal-specific
actions were handled by the terminal structure and the application-wide
actions were handled by the application structure.
The problem is that the
Action
union contains both terminal-specific
actions and application-wide actions. Initially, I did something like this:
pub
fn
performAppAction
(action
:
Action)
void
{
switch
(action) {
.
quit
=>
...,
.
close_all_windows
=>
...,
.
open_config
=>
...,
.
reload_config
=>
...,
else
=>
{}
,
}
}
This
works
but do you see the
else
there? That's a catch-all case
and when there is a catch-all case, the compiler can't error if I add
a new action to the
Action
union and forget to handle it in
performAppAction
.
Next, I exhaustively listed out all the actions I didn't care about
and did nothing:
pub
fn
performAppAction
(action
:
Action)
void
{
switch
(action) {
.
quit
=>
...,
.
close_all_windows
=>
...,
.
open_config
=>
...,
.
reload_config
=>
...,
// Do nothing for terminal-specific actions.
.
new_window
,
.
close_window
,
.
scroll_lines
,
=>
{}
,
}
}
This
works
but I have a few issues with it:
It's verbose. I have to list out all the terminal-specific actions
even though I don't care about them. The blog post example only shows
a half dozen actions but in reality there are many, many more.
From a types perspective, I don't like that
performAppAction
can accept terminal-specific actions. It'd be nicer if the type
signature self-documented that it only accepts application-wide
actions and what those were.
This same issue is mirrored in the
performTerminalAction
function
(which I didn't show here).
What I really want is something like the following:
// NOT REAL ZIG CODE! THIS IS PSUEDO CODE!
const
AppAction
=
union
(
enum
) {
quit
:
void
,
// ... other app actions ...
}
;
const
TerminalAction
=
union
(
enum
) {
new_window
:
void
,
// ... other terminal actions ...
}
;
// Union of both.
NOTE
THIS IS NOT REAL CODE. THIS IS CONCEPTUAL.
const
Action
=
AppAction
|
TerminalAction
;
One might ask: "why not just have two separate unions?" The answer is
because other parts of the codebase need to work with the single
Action
.
For example, the configuration parser needs to be able to parse all actions
for keybinds.
Comptime Union Subsets
We can use Zig comptime to create our subset types.
We could've just as easily created our subset types and used
comptime to create our full union type. As an exercise to the reader,
I encourage you to try this. It works just as well, but has different
edge cases and ergonomic tradeoffs.
The first thing we need to know is what scope each action belongs to.
To do this, we can introduce a new function to tell us:
pub
const
Scope
=
enum
{ app
,
terminal }
;
pub
fn
scope
(action
:
Action) Scope {
return
switch
(action) {
.
quit
,
.
close_all_windows
,
.
open_config
,
.
reload_config
=>
.
app
,
.
new_window
,
.
close_window
,
.
scroll_lines
=>
.
terminal
,
}
;
}
This is a very straightforward function. It is verbose since we need
to include every case, but it is centralized in a single location and
easy to maintain.
Next, we can use this function and comptime to create our subset types:
/// Returns a union type that only contains actions that are scoped to
/// the given scope.
pub
fn
ScopedAction
(
comptime
s
:
Scope)
type
{
const
all_fields
=
@typeInfo
(Action)
.
Union
.
fields
;
// Find all fields that are scoped to s
var
i
:
usize
=
0
;
var
fields
:
[all_fields
.
len]std
.
builtin
.
Type
.
UnionField
=
undefined
;
for
(all_fields)
|
field
|
{
const
action
=
@unionInit
(Action
,
field
.
name
,
undefined
)
;
if
(action
.
scope
()
==
s) {
fields[i]
=
field
;
i
+=
1
;
}
}
// Build our union
return
@Type
(
.
{
.
Union
=
.
{
.
layout
=
.
auto
,
.
tag_type
=
null
,
.
fields
=
fields[
0
..
i]
,
.
decls
=
&
.
{}
,
} })
;
}
I'm sorry, I know this is a "draw the rest of the fucking owl" moment
2
.
I'll walk through this step by step.
pub
fn
ScopedAction
(
comptime
s
:
Scope)
type
{
First, capitalized identifiers in Zig are idiomatically types. The
compiler doesn't enforce or require this, it's just idiomatic styling.
When a function is capitalized, it signals to the caller that it will
return a type.
This is a function that returns a type. This is how Zig does generics.
Since Zig has comptime code execution, and comptime code execution is
the full language
, we can use functions that take parameters at comptime
and return things like... types.
In this case, our function is taking a
Scope
and using that to generate
a new action union that only contains actions that have that scope.
const
all_fields
=
@typeInfo
(Action)
.
Union
.
fields
;
The
@typeInfo
builtin function
3
returns structured information
about a type at comptime. We call it on
Action
to extract all the
fields in the union.
// Find all fields that are scoped to s
var
i
:
usize
=
0
;
var
fields
:
[all_fields
.
len]std
.
builtin
.
Type
.
UnionField
=
undefined
;
for
(all_fields)
|
field
|
{
const
action
=
@unionInit
(Action
,
field
.
name
,
undefined
)
;
if
(action
.
scope
()
==
s) {
fields[i]
=
field
;
i
+=
1
;
}
}
We now iterate over all the fields in the
Action
union. For each field,
we determine if it belongs to the scope we're interested in. If it does,
we save it.
The
@unionInit
function is a builtin that creates a union value with
a comptime-known field name and value. The value we use is
undefined
(uninitialized memory) because we don't care about the value; our
scope()
function only looks at the tag. If we ever access undefined
memory in comptime, we'll get a compiler error, so this is safe.
We need to create a value with the given type so we can call
scope()
on it. Note that our
scope()
function above has no idea if it is
being executed in comptime or runtime. It doesn't care. It's just a
normal function. Comptime is fucking cool that way.
// Build our union
return
@Type
(
.
{
.
Union
=
.
{
.
layout
=
.
auto
,
.
tag_type
=
null
,
.
fields
=
fields[
0
..
i]
,
.
decls
=
&
.
{}
,
} })
;
The
@Type
builtin reifies a type (creates a new type). In this case,
we're creating a union with the fields we accumulated; the fields that
have the scope we're looking for.
Finally, at the end of all this,
we have a new type that only
contains a subset of our original union. It looks like this:
pub
fn
performAppAction
(action
:
ScopedAction
(
.
app))
void
{
switch
(action) {
.
quit
=>
...,
.
close_all_windows
=>
...,
.
open_config
=>
...,
.
reload_config
=>
...,
}
}
Beautiful. We have a simple
switch
with compiler-enforced exhaustiveness
and our function signature self-documents that it only accepts application-wide
actions. When we add new actions to the
Action
union, we'll get a compiler
error to update the
scope()
function and after that everything else will
just work.
Also, in case its not obvious: all of this logic happens
at compile time
.
There is no runtime cost to doing any of this. Since we only execute this
logic at compile time, it also doesn't generate any new runtime code.
Converting To A Subset
The final challenge: given a full
Action
, how do we convert it to a
typed subset such as
ScopedAction(.app)
? The function below does
just that:
pub
fn
scoped
(self
:
Action
,
comptime
s
:
Scope)
?
ScopedAction
(s) {
switch
(self) {
inline
else
=>
|
v
,
tag
|
{
// Use comptime to prune out invalid actions
if
(
comptime
@unionInit
(
Action
,
@tagName
(tag)
,
undefined
,
)
.
scope
()
!=
s)
return
null
;
// Initialize our app action
return
@unionInit
(
ScopedAction
(s)
,
@tagName
(tag)
,
v
,
)
;
}
,
}
}
Let's walk through this one as well.
pub
fn
scoped
(self
:
Action
,
comptime
s
:
Scope)
?
ScopedAction
(s) {
A few neat things here. First, this function takes both runtime and
comptime parameters. The compiler will enforce that the comptime parameters
are known at compile time.
The scope parameter must be comptime known because we use it to determine
our return value. Notice we use
s
in the return type
?ScopedAction(s)
.
If we didn't have the
comptime
prefix on
s
, the compiler would error
because we can't use a runtime value to generate information that must
be compile-time known (a type).
The
?
in the return type notates an optional return value. This means
that the return value may be null. For this function, we'll return null
if the
self
action doesn't belong to the scope we're looking for.
switch
(self) {
inline
else
=>
|
v
,
tag
|
{
The
inline else
is a special case in Zig. It is a catch-all case that
generates runtime code for each case that wasn't explicitly handled. Because
it is inline, the compiler will provide the
tag
as a compile-time known
value. This is important because we need to use it to determine the scope
of the action.
inline else
can be hard to understand at first. I recommend trying to
delete the
inline
keyword and see what the compiler tells you. Then
think through what the compiler is trying to do and it should become
more clear why
inline
is necessary.
// Use comptime to prune out invalid actions
if
(
comptime
@unionInit
(
Action
,
@tagName
(tag)
,
undefined
,
)
.
scope
()
!=
s)
return
null
;
Here we use
@unionInit
again to create a union value with the comptime-known
tag. We then call
scope()
on it to determine if it belongs to the scope
we're looking for. If it doesn't, we return null. Since this conditional
is a comptime, this will conditionally compile out the rest of the block
so we don't get a type error initializing a scoped action for an invalid
tag.
// Initialize our app action
return
@unionInit
(
ScopedAction
(s)
,
@tagName
(tag)
,
v
,
)
;
Finally, we return the initialized scoped action.
Compared to the previous section, this function does have
some
runtime cost.
This function uses a runtime switch statement to filter out actions that
don't belong to the scope we're looking for. I didn't bother disassemblying
the code to see how this is lowered, but I suspect the compiler optimizes
a lot of this away because the converted unions have the same memory layout.
I did profile this function in a synthetic case where I infinite loop a
cheap keyboard shortcut in Ghostty and it didn't show up in the profile, so
I'm not worried about it.
Conclusion
Zig's comptime is a powerful feature that allows you to do some really
amazing things. In this post, I combined multiple comptime features
of Zig to solve a real-world problem: generating types at comptime,
calling comptime-oblivious functions at comptime,
inline else
,
@unionInit
, and more.
This post demonstrates an admittedly advanced use of Zig's comptime.
For newcomers to Zig, the techniques and language features used here
are likely to be overwhelming. It took me some time to get comfortable
with these features, but they are incredibly powerful once you do.
I'm a type pragmatist. I believe leaning on the type system to enforce
correctness is a powerful tool. At the same time, I believe some languages
take this too far and make the type system a burden. Zig strikes a nice
balance for me and I believe this post demonstrates that.
