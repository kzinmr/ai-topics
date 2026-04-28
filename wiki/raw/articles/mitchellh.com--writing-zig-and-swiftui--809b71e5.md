---
title: "Integrating Zig and SwiftUI"
url: "https://mitchellh.com/writing/zig-and-swiftui"
fetched_at: 2026-04-28T07:02:40.902403+00:00
source: "mitchellh.com"
tags: [blog, raw]
---

# Integrating Zig and SwiftUI

Source: https://mitchellh.com/writing/zig-and-swiftui

Table of Contents
Building a native GUI for a cross-platform application is a decades old
problem. Nowadays, most people just
don't
and fallback to using a non-native
experience such as Electron instead.
One approach to building a native GUI for a cross-platform application is to
write all of the business logic in a cross-platform language (C, Rust, Zig,
etc.) and then write the platform-specific GUI code.
This is the approach I take with my
my terminal emulator
and it works really well. As of the current date writing this post, 93% of my repository is
business logic in Zig and C, and 4% is macOS-specific GUI code in Swift.
As a result, my terminal emulator is truly native: you get native Mac windows,
Mac GUI components (buttons, text fields), etc. It looks and feels great. But
its also still cross-platform: I support Linux (using GTK) while sharing ~90%
of all code. In this post, I'll share details about how this setup works and
why I approached GUI programming this way.
I'll be using Zig as the example shared-logic language, but this general
pattern should apply to any systems language that can compile to a C-compatible
library, such as Rust.
This post will not teach you to Zig or SwiftUI programming. However, you
also don't need to be familiar with either. As long as you understand that
Zig is a programming language and SwiftUI is a native GUI toolkit, then
my explanations in this post are going to be more generally applicable.
High Level Idea
The high level idea:
Write your business logic in any language that supports exporting a
C-compatible library. This is just about any systems language
(Rust, Zig, C, C++, etc.). You could use a higher level language
(JavaScript, Ruby, Python) but the architecture changes since you need
a runtime.
Compile your cross-platform logic into a static library that exposes
the C ABI as the primary interface (acts like a "typical" system library).
Write your GUI logic in whatever native language and toolkit is recommended
for your platform, such as SwiftUI in XCode.
Link
the GUI to your
cross-platform library. 🎉
Exporting a C API with Zig
Zig makes it easy to export a C API. By prepending
export
to a function,
the function uses the C calling convention and is available for other programs
to call via standard linking. Here is the real exported function for initializing
the global state for my terminal:
export
fn
ghostty_init
()
c_int
{
main
.
state
.
init
()
;
return
0
;
}
The signature of an exported function (or more specifically: functions
using the C calling convention) is limited to parameters and return values
that are supported by C. This means you can not use comptime parameters,
generics, error sets, arbitrary bit width integers, etc. This restriction
only applies to the signature
. You can use all of those features inside
the function body.
From there, you can write your own header file and it quacks just like any
other library written in C. Note, you actually
must
write a header file,
because this is how Swift is going to know what the API is for your library.
# ghostty.h
int
ghostty_init
(
void
);
Finally, to build a static library, we can use the native Zig build tooling.
The
build.zig
ends up looking something like this. The result is that
you should see a file named
something.a
in your
zig-out
directory.
const
lib
=
b
.
addStaticLibrary
(
.
{
.
name
=
"ghostty"
,
.
root_source_file
=
.
{
.
path
=
"src/main_c.zig"
}
,
.
target
=
.
{
.
cpu_arch
=
.
aarch64
,
.
os_tag
=
.
macos
,
.
os_version_min
=
target
.
os_version_min
,
}
,
.
optimize
=
optimize
,
})
;
lib
.
bundle_compiler_rt
=
true
;
lib
.
linkLibC
()
;
b
.
default_step
.
dependOn
(
&
lib
.
step)
;
Zig version.
I am using the 0.11 nightly build for all the examples
in this post. Zig APIs are still regularly changing as the language matures
so I don't expect the code in this blog post to remain valid for very long,
but it should only require minor tweaks if you're close to 0.11.
Merging All Dependencies
Static libraries do not also embed their static dependencies. For example,
if your Zig code linked to
libcurl
, then any user of your
static library would still need to provide a static version of libcurl as well.
Note: this is only required if you have non-Zig library dependencies.
If you're compiling all your code and dependencies into a single unit,
then this step is not necessary.
Since we're only building our static libraries to integrate with our GUI
and not as general purpose static libraries, let's go ahead and package
up all our dependencies as well. To do that, we have to use
libtool(1)
.
The
build.zig
code looks like this:
var
lib_list
=
...;
try
lib_list
.
append
(
.
{
.
generated
=
&
lib
.
output_path_source })
;
const
libtool
=
LibtoolStep
.
create
(b
,
.
{
.
name
=
"ghostty"
,
.
out_name
=
"libghostty-aarch64-bundle.a"
,
.
sources
=
lib_list
.
items
,
})
;
libtool
.
step
.
dependOn
(
&
lib
.
step)
;
b
.
default_step
.
dependOn
(libtool
.
step)
;
The
LibtoolStep
is a custom step I wrote and the
source can be found here
.
LibtoolStep requires a list of all the dependencies, which we build up in
lib_list
(including adding our own library we just wrote). The result of
the libtool run is a "bundled" library which contains our library and
all of its dependencies.
Making a Universal (Multi-Arch) Library
macOS is still in the midst of its transition from Intel to Apple Silicon,
so we must build a library that works with both the
x86_64
and
aarch64
architectures. Mac supports what they call "Universal Binaries" which
work on both systems by just copying the final machine code for both architectures
into one file.
To build a universal binary, we have to build the static library for each
specific architecture, then use the
lipo
tool
to merge them together.
In
build.zig
, that looks like this:
const
static_lib_universal
=
LipoStep
.
create
(b
,
.
{
.
name
=
"ghostty"
,
.
out_name
=
"libghostty.a"
,
.
input_a
=
static_lib_aarch64
.
output
,
.
input_b
=
static_lib_x86_64
.
output
,
})
;
static_lib_universal
.
step
.
dependOn
(static_lib_aarch64
.
step)
;
static_lib_universal
.
step
.
dependOn
(static_lib_x86_64
.
step)
;
The
LipoStep
is a custom step I wrote to call
lipo
and the
source can be found here
.
The
static_lib_aarch64
and
static_lib_x86_64
are the results of the
addStaticLibrary
or
libtool
calls in the previous sections. The final result
is a universal library!
Creating an XCFramework
Finally, we need to build an
xcframework
file
.
An
xcframework
is a single bundle that contains the library, headers,
and other associated files that XCode can use a single unit to easily
integrate libraries.
I'm not going to explain xcframework files in detail. This blog post should
give you enough information for you to accurately Google search and find the
answers you need. This was the hardest part for me: just figuring out
what
I needed to know. I'm hoping this blog post gets you there!
I wrote a custom step for this too,
called
XCFrameworkStep
.
In
build.zig
it looks like this:
// The xcframework wraps our ghostty library so that we can link
// it to the final app built with Swift.
const
xcframework
=
XCFrameworkStep
.
create
(b
,
.
{
.
name
=
"GhosttyKit"
,
.
out_path
=
"macos/GhosttyKit.xcframework"
,
.
library
=
static_lib_universal
.
output
,
.
headers
=
.
{
.
path
=
"include"
}
,
})
;
xcframework
.
step
.
dependOn
(static_lib_universal
.
step)
;
b
.
default_step
.
dependOn
(xcframework
.
step)
;
This step takes our final library output along with a path to our
headers directory (that has the
ghostty.h
file) and builds our
xcframework.
IMPORTANT: You need a modulemap.
You need to create a
module.modulemap
file in your
include
directory. This is used by XCode with the xcframework
file to properly build your library. Put the
module.modulemap
file alongside
your C header:
// This makes Ghostty available to the XCode build for the macOS app.
// We append "Kit" to it not to be cute, but because targets have to have
// unique names and we use Ghostty for other things.
module GhosttyKit
{
umbrella header
"
ghostty.h
"
export
*
}
Integrating with an XCode Project
Our library is finally ready to be used by XCode. This step is thankfully
very easy: just drag and drop the built xcframework file into the "Frameworks"
section of your XCode project and select "Do Not Embed" as the embedding
option. That's it, your Swift code can now import it:
import
SwiftUI
import
GhosttyKit
@
main
struct
GhosttyApp
:
App
{
var
body:
some
Scene
{
...
}
}
The
import
name must match the name in your modulemap (previous section).
After you import, autocomplete will have all of your functions and types
from your header file, and they'll be automatically converted to Swift types
(the types they use for bridging to C).
At this point, you'll probably run into some challenges around C numeric types,
C booleans, C pointers, etc. and interoperating with Swift. But these are
all very Google-able problems.
Done
I admit, there are a lot of concepts to get to the promised land with this
idea: exporting a C API, building a static lib, libtooling dependencies,
lipoing for universal binaries, generating an xcframework, writing a
C header and modulemap file, then importing it into your XCode project.
But, each of these steps isn't doing anything cutting edge or esoteric.
All of the steps are tried and true -- usually decades-old -- operations
and tools for working with system libraries. They're unlikely to to be
brittle going forward.
For my terminal application, I've used this technique for a little over a year
including over one major macOS update so far, and nothing broke at all.
Going forward, I don't expect things to break, either.
And I think the payoff is worth it: you can get a truly native GUI
experience while keeping almost all of your application logic cross-platform.
To repeat from the introduction: for my application 94% of my code is
in Zig and is used cross-platform, and only 4% is platform-specific GUI
code for macOS. Admittedly, a terminal emulator doesn't have
that
much
GUI interactions, but that implements native tabs, splits, preference pane,
etc.
I know that this blog post doesn't have a turnkey, copy-and-paste solution
to integrating Zig with SwiftUI, but I hope it gives you the knowledge basis
necessary to follow this pattern.
Appendix: Why Not Objective-C?
One approach on macOS is to go lower level and try to use Objective-C
directly to interact with the system libraries such as AppKit or Foundation.
Objective-C has a native C API so most programming languages can interact
with it directly. I took this approach first, but I don't think its practically viable.
The major issue is that it is painfully clear that the future of Apple
device programming is Swift. While some core libraries are available in
ObjC, a majority of modern integrations
require
Swift to some extent
(or jumping through some absolutely-not-worth-it hoops to make something work).
A lot of this comes down to convenience: the
convenient
GUI integrations are
in Swift nowadays (such as SwiftUI). But sometimes, it comes down to actual
functionality. For example, if you want to integrate with the
iPhone Dynamic Island
,
you have to export a SwiftUI view as far as I know. I'm sure there is some
cursed way to use pure UIKit but... you'd be really fighting what Apple
wants
you to do.
