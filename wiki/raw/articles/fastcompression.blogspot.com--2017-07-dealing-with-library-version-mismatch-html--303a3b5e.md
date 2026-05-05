---
title: "Dealing with library version mismatch"
url: "http://fastcompression.blogspot.com/2017/07/dealing-with-library-version-mismatch.html"
fetched_at: 2026-05-05T07:00:59.166309+00:00
source: "Yann Collet (LZ4/Zstd)"
tags: [blog, raw]
---

# Dealing with library version mismatch

Source: http://fastcompression.blogspot.com/2017/07/dealing-with-library-version-mismatch.html

Note : this article was initially redacted as an answer to
David Jud's comment
, but it became long enough to be worth converting into a full blog entry.
In previous article, I attempted to introduce a few challenges related to designing an extensible API.
In this one, I'll cover an associated but more specific topic, on how to handle a library version mismatch.
Version mismatch is a more acute problem in a DLL scenario. In a static linking scenario, the programmer has several advantages :
Compiler will catch errors (if a type, or a prototype, has changed for example). This gives time to fix these errors. Of course, the application maintainer will prefer that a library update
doesn't
introduce any change in existing code, but worst case is, most errors should be trapped before shipping the product.
Compiler will automatically adapt ABI changes : if an updated type is larger/smaller than previous version, it will be automatically converted throughout the code base. Same thing happens in case of
enum
changes : adaptation to new
enum
values is automatically applied by compiler.
Library is available during compilation, which means programmer has a local copy that he can update (or not) according to its requirements.
Well, this last property is not always true : in larger organisations, library might belong to a "validated" pool, which cannot be easily adapted for a specific project. In which case, the user program will either have to host its own local copy, or adapt to the one selected by its organisation.
But you get the idea : problematic version mismatches are likely to be trapped or automatically fixed by the compiler, and therefore should be corrected before shipping a binary. Of course, the less changes, the better. Program maintainers will appreciate a library update as transparent as possible.
For a dynamic library though, the topic is a lot harder.
To begin with, user program typically does not have direct control over the library version deployed on target system. So it could be anything. The library could be more recent, or older, than expected during program development.
Now these two types of mismatches are quite different, and trigger different solutions :
Case 1 - library version is higher than expected
This one can, and should, be solved by the library itself.
It's relatively "easy" : never stop supporting older entry points.
This is of course easier said than done, but to be fair, it's first and foremost a question of respecting a policy, and therefore is not out of reach.
Zstandard tries to achieve that by guaranteeing that any prototype reaching "stable" status will be there "forever". For example,
ZSTD_getDecompressedSize()
, which has been recently superceded by
ZSTD_getFrameContentSize()
, will nonetheless remain an accessible entry point in future releases, because it's labelled "stable".
A more subtle applicable problem is ABI preservation, in particular structure size and alignment.
Suppose, for example, that version v1.1 defines a structure of size 40 bytes.
But v1.2 add some new capabilities, and now structure has a size of 64 bytes.
All previous fields from v1.1 are still there, at their expected place, but there are now more fields.
The user program, expecting v1.1, would allocate the 40-bytes version, and pass that as an argument to a function expecting a 64-bytes object. You can guess what will follow.
This could be "manually" worked around by inserting a "version" field and dynamically interpreting the object with the appropriate parser. But such manipulation is a recipe for complexity and errors.
That's why structures are pretty dangerous. For best safety, structure definition must remain identical "forever", like the approved "stable" prototypes.
In order to avoid such issue, it's recommended to use
incomplete types
. This will force the creation of underlying structure through a process entirely controlled by current library, whatever its version, thus avoiding any kind of size/alignment mismatch.
When above conditions are correctly met, the library is "safe" to use by applications expecting an older version : all entry points are still there, behaving as expected.
Whenever this condition cannot be respected anymore, an accepted work-around is to increase the Major digit of the version, indicating a breaking change.
Case 2 - library version is lower than expected
This one is more problematic.
Basically, responsibility is now on the application side. It's up to the application to detect the mismatch and act accordingly.
In
David Jud's comment
, he describes a pretty simple solution : if the library is not at the expected version, the application just stops there.
Indeed, that's one way to safely handle the matter.
But it's not always desirable. An application can have multiple library dependencies, and not all of them might be critical.
For example, maybe the user program access several libraries offering similar services (encryption for example). If one of them is not at the expected version, and cannot be made to work, it's not always a good reason to terminate the program : maybe there are already plenty of capabilities available without this specific library, and the program can run, just with less options.
Even inside a critical library dependency, some new functionality might be optional, or there might be several ways to get one job done.
Dealing with this case requires writing some "version dependent" code.
This is not an uncommon situation by the way. Gracefully handling potential version mismatches is one thing highly deployed programs tend to do well.
Here is how it can be made to work : presuming the user application wants access to a prototype which is only available in version v1.5+, it first tests the version number. If condition matches, then program can invoke target prototype as expected. If not, a backup scenario is triggered, be it an error, or a different way to get the same job done.
Problem is, this test must be done statically.
For example, in
Zstandard
, it's possible to ask for library version at runtime, using
ZSTD_versionNumber()
. But unfortunately, it's already too late.
Any invocation of a new function, such as
ZSTD_getFrameContentSize()
which only exists since v1.3.0, will trigger an error at link time, even if the invocation itself is protected by a prior check with
ZSTD_versionNumber()
.
What's required is to selectively remove any reference to such prototype from compilation and linking stages, which means this code cannot exist. It can be excluded through pre-processor.
So the correct method is to use a macro definition, in this case,
ZSTD_VERSION_NUMBER
.
Example :
#if ZSTD_VERSION_NUMBER >= 10300
size = ZSTD_getFrameContentSize(src, srcSize);
#else
size = ZSTD_getDecompressedSize(src, srcSize);
/* here,
0-size answer can be mistaken for "error", so add some code to mitigate the risk */
#endif
That works, but requires to compile binary with the correct version of
zstd.h
header file.
When the program is compiled on target system, it's a reasonable expectation : if
libzstd
is present,
zstd.h
is also supposed to be accessible. And it's reasonable to expect them to be synchronised. There can be some corner case scenarios where this does not work, but let's say that in general, it's acceptable.
The detection can also be done through a
./configure
script, in order to avoid an
#include
error during compilation, should the relevant
header.h
be not even present on target system, as sometimes the library is effectively optional to the program.
But compilation from server side is a different topic. While this is highly perilous to pre-compile a binary using dynamic libraries and then deploy it, this is nonetheless the method selected by many repositories, such as
aptitude
, in order to save deployment time. In which case, the binary is compiled for "system-provided libraries", which minimum version is known, and repository can solve dependencies. Hence, by construction, the case
"library has a lower version than expected"
is not supposed to happen. Case closed.
So, as we can see, the situation is solved either by local compilation and clever usage of preprocessing statements, or by dependency solving through repository rules.
Another possibility exists, and is, basically, the one proposed in
ZSTD_CCtx_setParameter()
API : the parameter to set is selected through an
enum
value, and if it doesn't exist, because the local library version is too old to support it, the return value signals an error.
Using safely this API feels a lot like the previous example, except that now, it becomes possible to check library version at runtime :
if (ZSTD_versionNumber() >= 10500) {
return ZSTD_CCtx_setParameter(cctx, ZSTD_p_someNewParam, value);
} else {
return ERROR(capability_not_present);
}
This time, there is no need to be in sync with the correct
header.h
version. As the version number comes directly at runtime from the library itself, it's necessarily correct.
Note however that
ZSTD_CCtx_setParameter()
only covers the topic of "new parameters". It cannot cover the topic of "new prototypes", which still requires using exclusion through macro detection.
So, which approach is best ?
Well, that's the good question to ask. There's a reason the new advanced API is currently in "experimental" mode : it needs to be field tested, to experience its strengths and weaknesses. There are pros and cons to both methods.
And now, the matter is to select the better one...
