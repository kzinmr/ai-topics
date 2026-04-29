---
title: "Programming Aphorisms"
url: "https://matklad.github.io/2026/02/11/programming-aphorisms.html"
fetched_at: 2026-04-29T07:02:04.996599+00:00
source: "matklad.github.io"
tags: [blog, raw]
---

# Programming Aphorisms

Source: https://matklad.github.io/2026/02/11/programming-aphorisms.html

Programming Aphorisms
Feb 11, 2026
A meta programming post — looking at my thought process when coding
          and trying to pin down what is programming “knowledge”. Turns out, a
          significant fraction of that is just reducing new problems to a
          vocabulary of known tricks. This is a personal, descriptive post, not
          a prescriptive post for you.
It starts with a question posted on Ziggit. The background here is
          that Zig is in the process of removing ambient IO capabilities.
          Currently, you can access program environment from anywhere via
std.process.getEnvVarOwned
.
In the next Zig version, you’ll have to thread
std.process.Environ.Map
from main down to every routine that needs access to the environment.
          In this user’s case, they have a
readHistory
function
          which used to look up the path to the history file in the environment,
          and they are wondering how to best model that in the new Zig. The
          options on the table are:
pub
fn
readHistory
(
io: std.Io,
alloc: Allocator,
file: std.Io.File,
) ReadHistoryError
!
void
;
pub
fn
readHistory
(
io: std.Io,
alloc: Allocator,
maybe_environ_map: ?
*
std.process.Environ.Map,
) ReadHistoryError
!
void
;
pub
fn
readHistory
(
io: std.Io,
alloc: Allocator,
maybe_absolute_path: ?[]
const
u8
,
maybe_environ_map: ?
*
std.process.Environ.Map,
) ReadHistoryError
!
void
;
My starting point would instead be this:
pub
const
HistoryOptions =
struct
{
file: []
const
u8
,
pub
fn
from_environment
(
environment:
*
const
std.process.Environ.Map,
) HistoryOptions;
};
pub
fn
readHistory
(
io: std.Io,
gpa: Allocator,
options: HistoryOptions,
) ReadHistoryError
!
void
;
In terms of meta programming, what I find fascinating is that this,
          for me, is both immediate (I don’t have to think about it), but also
          is clearly decomposable into multiple factoids I’ve accumulated
          before. Here’s a deconstruction of what I did here, the verbal
          “labels” I use to think about what I did, and where I had learned to
          do that:
First
, I “raised the abstraction level” by giving
it
a name and a type (
HistoryOptions
). This is a rare
          transformation which I learned and named myself. Naming is important
          for my thinking and communicating process. “Let’s raise abstraction
          level” is a staple code review comment of mine.
Second
, I avoided “midlayer mistake” by making sure that
          every aspect of options is user-configurable. Easy to do in Zig, where
          all fields are public. I learned about
midlayer mistake
from a
          GitHub comment by
Josh Triplett
.
Third
, I provided a “shortcut”, the
from_environment
convenience function that cuts across abstraction layers. I learned
          the “shortcut” aphorism from
Django Views — The Right Way
.
Germane to the present article, I read that post a decade after I had
          touched Django the last time. It was useless to me on the object
          level. On the meta level, reading the article solidified and
named
several programming tricks for me. See reverberations
          in
How to Make a 💡?
.
Fourth
, I instinctively renamed
alloc
to “gpa”
          (in opposition to “arena”), the naming I spotted in the Zig compiler.
Fifth
, I named the configuration parameter “options”, not
config
,
props
or
params
, a
          naming scheme I learned at TigerBeetle.
Sixth
, I made sure that the signature follows “positional DI”
          scheme. Arguments that are dependencies, resources with unique types
          are injected positionally (and have canonical names like
io
or
gpa
). Arguments that
directly
vary the behavior of function (as opposed to affecting transitive
          callees) are passed by name, in the
Options
struct.
To be specific, I don’t claim that my snippet is the right way to do
          this! I have no idea, as I don’t have access to the full context.
          Rather, if I were
actually
solving the problem, the snippet
          above would be my initial starting point for further iteration.
Note that I also don’t explain
why
I am doing the above six
          things, I only name them and point at the origin. Actually explaining
          the
why
would take a blog post of its own for every one of
          them.
And this is I think the key property of my thought process — I have a
          bag of tricks, where the tricks are named. Inside my mind, this label
          points both to the actual trick (code to type), as well as a
          justification for it (in what context that would be a good trick to
          use).
And I use these tricks all the time, literally! Just answering in
          passing to a forum comment makes me grab a handful! A lot of my
          knowledge is structured like a book of coding aphorisms.
Meta meta — how come I have acquired all those tricks? I read
          voraciously, random commits, issues, jumping enthusiastically into
          rabbit holes and going on wiki trips. The key skill here is
          recognizing an aphorism once you see it. Reading Ziggit is part of
          trick-acquisition routine for me. Having learned the trick, I remember
          it, where “remembering” is an act of active recall at the opportune
          moment. This recall powers “horizontal gene transfer” across domains,
          stealing shortcuts from Django and midlayer mistake from the kernel.
          Did you notice that applying “horizontal gene transfer” to the domain
          of software engineering tacit knowledge is horizontal gene transfer?
          When entering a new domain, I actively seek out the missing tricks. I
          am relatively recent in Zig, but all the above tricks are either Zig
          native, or at least Zig adapted. Every once in a while, I “invent” a
          trick of my own. For example, “positional DI” is something I only
          verbalized last year. This doesn’t mean I hadn’t been doing that
          before, just that the activity wasn’t mentally labeled as a separate
          thing you can deliberately do. I had the idea, now I also have an
          aphorism.
