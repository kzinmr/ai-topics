---
title: "The art of designing advanced API"
url: "http://fastcompression.blogspot.com/2017/07/the-art-of-designing-advanced-api.html"
fetched_at: 2026-05-05T07:00:59.571982+00:00
source: "Yann Collet (LZ4/Zstd)"
tags: [blog, raw]
---

# The art of designing advanced API

Source: http://fastcompression.blogspot.com/2017/07/the-art-of-designing-advanced-api.html

A library
API (Application Programming Interface)
is even more important than its implementation.
There are many reasons for this statement :
- An API exposes a
suitable abstraction
. Should it prove broken, unclear or just too complex, the library will be misused, which will ultimately be paid by users' time (multiplied by nb of users).
- An API is a contract. Break it, and existing applications can no longer work with your library. Adaptation cost is once again paid by users' time (if it ever happens).
- Because of this, API tend to stick around for a
long
time, much longer than underlying implementation.
If an implementation is modified to provide, say, a 5% speed improvement, it's all free, every user can immediately benefit about it without further hassle. But if one has to add a single parameter, it's havoc time.
Because it's so stressful to modify an API, one can be tempted to look very hard once, in order to design and expose a
perfect API
, one that will stand the test of time, and will never need to be changed. This search is (mostly) a delusion.
- perfect API, embedding such a strong restriction to never change in the future, can take forever to build, all under intense stress, as there is always a question mark hanging around : "is there a use case that it does not cover ?". Eventually, it's only a matter of time before you (or your users) find one.
- perfect API lean towards "complex API", as the requirement to support everything makes it add more parameters and control, becoming more and more difficult to manage by users.
- "complex" quickly leads to "misleading", as supporting some "future scenarios" for which there is no current implementation, and maybe no current need, will be categorised bad ideas after all, but side-effects of this useless abstraction will remain in the API.
So, the next great idea is to plan for API changes.
The way
Zstandard library
tries to achieve this is by quickly converging towards some very simple prototypes, which offer "core" functionalities at a low complexity level.
Then, more complex use cases, not covered by simple API, do show up, and the need to serve them introduce the creation of an "experimental section", a place where it's still possible to play with API, trying to find an optimal abstraction for intended use case, before moving into "stable" status (aka: this method will no longer change).
A consequence of this strategy is the creation of more and more prototypes, dedicated to serving their own use case.
Need to compress with dictionary ? Sure, here comes
ZSTD_compress_usingDict()
.
Need to process data in a streaming fashion ? Please find
ZSTD_compressStream()
.
In a streaming fashion with a dictionary ?
ZSTD_compressStream_usingDict()
.
Need control over specific parameters ? Go to
_advanced()
variants.
Preprocess dictionary for faster loading time ? Here are
_usingCDict()
variants.
Some multithreading maybe ?
ZSTDMT_*()
Combine all this ? Of course. Here is a list of a gazillion methods.
As one can see, this doesn't scale too well. It used to be "good enough" for a dozen or so methods, but as combinatorial complexity explodes, it's no longer suitable.
ZSTD_compress_generic()
is the new main compression method. It's designed to support all other compression methods. It can do block, streaming, dictionary, multithreading, and any combination of those. We have plan for even more extensions, and they all seem to fit in.
This is possible because now sending parameters is a separate operation, which can be completed in as many steps as necessary.
The main vehicle to set these parameters is
ZSTD_CCtx_setParameter()
.
It uses an
enum
based policy, where the parameter is selected in an
enum
list, and new value is provided as an
unsigned
type.
This design has been favoured over previous one, which was using a
struct
to pass all parameters in a single step. The
struct
was inconvenient as it forced user to select a value for each and every parameter, even out-of-scope ones, in order to change just one of them. Perhaps even more importantly, the
struct
is problematic for future changes : adding any new parameter would change the
struct
size, which is an ABI break. It can quickly get ugly when the program and library work on common memory areas using different sizes.
The
enum
policy allow us to add any new parameter while preserving API and ABI, so it looks very flexible.
However, it comes with its own set of troubles.
To begin with,
enum
values can very easily change : just add a new
enum
in the list, and see all enum values after that one slide by one.
It can be a problem if, in a version of the library,
ZSTD_p_compressionLevel
is attributed a 2, but in a future version, it becomes a 3. In a dynamic library scenario, where version mismatch can easily happen, it means the caller is changing some other random parameter.
To counter that, it will be necessary to pin down all
enum
values to a manually assigned one. This will guarantee the attribution.
Another issue is that the value of the parameter is provided as an
unsigned
type, so the parameter must fit this type. That's not always possible.
For example, there is a dedicated method to set
pledgedSrcSize
, which is essentially a promise about how much data is going to be processed. This amount can be very large, so an
unsigned
type is not enough. Instead, we need an
unsigned long long
, hence a dedicated method.
Another even more obvious one happens when referencing a prepared dictionary in read-only mode : this parameter is a
const ZSTD_CDict*
type, so it is  set through a dedicated method,
ZSTD_CCtx_refCDict().
And we have a few other exceptions using their own method, as the argument cannot fit into an
unsigned
.
But the large majority of them uses
ZSTD_CCtx_setParameter()
.
In some cases, the adaptation works though it's not "best".
For example, a few parameters are selected among a list of enums, for example
ZSTD_strategy
. The enum is simply casted to an
unsigned
and passed as argument. It works. But it would have been even nicer to keep the argument type as the intended enum, giving the compiler a chance to catch potential type mismatch (
example
).
So this design could be in competition with another one : define one method per parameter. The most important benefit would be that each parameter can have its own type.
But this alternate design has also its own flaws :
adding any new parameter means adding a method. Therefore, if a program uses a "recent" method, but links against an older library version, this is a link error.
In contrast, the
enum
policy would just generate an error in the return code, which can be identified and gracefully dealt with.
Creating future-proof API is hard. There is always a new unexpected use case which shows up and would require another entry point or another parameter. The best we can do is plan for those changes.
The new Zstandard's advanced API tries to do that. But since it is a first attempt, it likely is perfectible.
This is design time, and it will cost a few revisions before reaching "stable" status. As always, user feedback will be key to decide if the new design fits the bill, and how to amend it.
Follow up
:
Dealing with library version mismatch
Edit :
Arseny Kapoulkine made an interesting comment, arguing that specialized entry points make it possible for compiler's DCE (Dead Code Elimination) optimisation to kick in, removing useless code from the final binary :
https://twitter.com/zeuxcg/status/882816066296172550
In general this is true. Calling
specialized_function1(...)
is clear for the linker,
then it's possible to remove any potentially unused
specialized_function2()
from binary generation.
In contrast calling
generic_function(mode=1, ...)
with
void generic_function(int mode, ...)
{
switch(mode) {
case 1 : return specialized_function1(...);
case 2 : return specialized_function2(...);
}
makes it much more difficult. In general, for the second case,
specialized_function2()
will remain in the binary.
(an exception being usage of
inline
, associated with
-flto
, and non-ambiguous selection parameter, but that's no longer a "simple" setup).
For Zstandard though, it doesn't make a lot difference.
The reason is, whatever "specialized" entry point is invoked, (
ZSTD_compress()
, or
ZSTD_compress_usingDict()
for example), it's just an entry point. The compression code is not "immediately behind", it's reached after several indirection levels. This design make it possible for a single compression code to address multiple usage scenarios with vastly different set of parameters, which is vital for maintenance. But disentagling that for DCE is a lot more difficult.
If required,
-flto
makes it possible to optimize size better, and some difference become visible, but remain relatively small.
