---
title: "A New Cross-Platform Open Source C++ Framework"
url: "https://preshing.com/20200526/a-new-cross-platform-open-source-cpp-framework"
fetched_at: 2026-05-05T07:01:02.789901+00:00
source: "Preshing"
tags: [blog, raw]
---

# A New Cross-Platform Open Source C++ Framework

Source: https://preshing.com/20200526/a-new-cross-platform-open-source-cpp-framework

For the past little while – OK, long while – I’ve been working on a
custom game engine in C++
. Today, I’m releasing part of that game engine as an open source framework. It’s called the
Plywood
framework.
Please note that Plywood, by itself, is
not
a game engine! It’s a framework for building all kinds of software using C++.
For example, Plywood’s
documentation
is generated with the help of a C++ parser, formatted by a Markdown parser, and runs on a custom webserver all written using Plywood.
Integrating third-party libraries can a pain in C++, but Plywood aims to simplify it.
Here’s a short Plywood program
that uses
Cairo
and
Libavcodec
to render a vector animation to a video file:
And
here’s one
that synthesizes a short music clip to an MP3:
The source code for these examples is included in the Plywood repository, and everything builds and runs on Windows, Linux and macOS.
Of course, Plywood also serves as the foundation for my (proprietary) game engine, which I call the
Arc80 Engine
. That’s why Plywood came into existence in the first place. I haven’t shipped a complete game using the Arc80 Engine yet, but I have made a number of prototypes with it. More on that later!
What’s Included In Plywood
Plywood comes with:
A
workspace
designed to help you reuse code between applications.
A set of
built-in modules
providing cross-platform I/O, containers, process creation and more.
A runtime
reflection
and serialization system.
Here are a few more details about each component.
The Workspace
Most open source C++ projects are libraries that are meant to be integrated into other applications. Plywood is the opposite of that: It gives you a workspace into which source code and libraries can be integrated. A single Plywood workspace can contain several applications – a webserver, a game engine, a command-line tool. Plywood simplifies the task of building and sharing code between them.
Plywood uses
CMake
under the hood, but you don’t have to write any CMake scripts. Like any CMake-based project, a Plywood workspace has the concepts of
targets
and
build folders
that are kept separate from the source code, but it adds several other concepts on top of that, such as
modules, root targets and extern providers
. (Note: Plywood modules are not to be confused with C++20 modules; they’re different things.)
A Plywood workspace
external
packages
build
folders
root targets
repos
source code
modules
extern providers
An explanation of the Plywood workspace, and how it interacts with CMake, really deserves its own post, but what it helps achieve is
modularity
.
Arc80 is a modular game engine, and thanks to the Plywood workspace, it’s possible to quickly build small applications using Arc80 engine modules. For example, when I was developing the flame effect for a jet engine, I created a small test application that contained nothing but the flame effect. This test application allowed me to focus on the feature itself and kept the effect decoupled from the rest of the game.
Additional work is still needed to make the process more user-friendly. For example, to define a new module, you must currently write a C++ function using an API I haven’t documented yet. A simple configuration file would be preferable. That’s the next thing I plan to work on now that Plywood is released.
Built-In Modules
I thought about open-sourcing part of the Arc80 Engine for a long time, and that’s what led to the
repos
idea mentioned above. A single Plywood workspace can combine modules from separate Git repositories. When it came time to open-source Plywood, it was a matter of moving a bunch of modules from the proprietary
arc80
repo to the public
plywood
repo.
As of today, the
plywood
repo comes with
36
built-in modules
. These modules offer functionality for platform abstraction, vector math, JSON parsing, audio and image processing, and more. Of course, all modules are optional, so if you don’t think a specific module suits your needs, you don’t have to use it. Here’s a simplified diagram showing some of the modules included in the
plywood
repo (on the bottom) versus the modules I’m keeping private for now (on the top). The arrows represent dependencies:
platform
runtime
reflect
pylon
cook
math
image
web
cpp
codec
build
audio
libavcodec
cairo
libsass
plytool
WebCooker
WebServer
ui
session
graphic
physics
view
image
gpu
audio
assetBank
FreeType
SDL
Game
RemoteCooker
arc80
plywood
(not included)
(included)
The most important module is the one marked with a star:
runtime
. I originally used
Turf
for cross-platform threads and memory management, then I gradually added containers, I/O, a filesystem API and sensible Unicode support. The
runtime
module is the result. It also exposes things not available in the standard C or C++ runtime libraries, like redirecting I/O to a subprocess and watching for changes to a directory. The API could use some improvement here & there, but I already prefer it over the standard libraries quite a bit.
I would have liked to open source more of the Arc80 Engine, especially modules related to graphics and audio processing, but those aren’t ready for prime time yet. I might open source them in the future, but it’ll depend on whether Plywood is successful in the first place.
The Reflection System
Runtime reflection is, in my opinion, the biggest missing feature in standard C++. This feature enables an entire category of generic programming that’s simply not possible otherwise. I wrote about runtime reflection in the previous
two
posts
on this blog. Plywood comes with a built-in reflection system that’s based on the approach described in those posts, but adds a code generation step on top of it.
In short, Plywood’s reflection system exposes metadata about your program’s data structures at runtime. For example, a data structure named
Contents
is defined in Plywood’s
web-documentation
module:
struct
Contents {
    PLY_REFLECT()
    String title;
    String linkDestination;
    Array<Contents> children;
    
};
At runtime, Plywood’s documentation system loads an
Array<Contents>
from a JSON file:
[
  {
    "title": "Home",
    "linkDestination": "/",
    "children": [
    ]
  },
  {
    "title": "Quick Start",
    "linkDestination": "/docs/QuickStart",
    "children": [
      {
        "title": "Building the Documentation",
        "linkDestination": "/docs/QuickStart/BuildDocs",
        "children": [
        ]
      }
    ]
  },
  ...
The data is loaded by passing the metadata for
Array<Contents>
to a generic JSON loading function. No type-specific loading code needs to be written.
Currently, to make this work, you need to run
plytool codegen
at a command prompt before compiling your project. (I plan to eventually merge this command into the build process, but only after optimizing it so that it runs incrementally.) This command scans all available source code modules, extracts all the type declarations using a custom C++ parser, and generates some additional source code required for the metadata.
The Arc80 Engine also uses reflection for binary serialization, shader parameter passing and more.
If you’re a team working on a relatively new, cross-platform C++ project, I think it’s already viable to base that project on Plywood. You’ll have to follow Plywood development closely, and you’ll have to seek out some answers directly from the source code where the documentation is not yet complete (as is the case with any project). But given that I’ve already put roughly 4000 hours of work into this framework, you’ll have a significant head start compared to building a similar framework yourself.
There are a lot of features in Plywood that could be extended in the future:
Plywood’s built-in C++ parser could be extended to make it useful for other applications. It currently recognizes declarations but not expressions; function bodies are currently skipped. This feature would be a big undertaking.
The webserver could be improved. It doesn’t even use a thread pool yet. Any improvements to the webserver would likely make Plywood a better fit for other back-end services, too.
Plywood’s dependency on the standard C++ runtime could possibly be eliminated, and on some platforms, the standard C runtime too. Doing so would reduce build times and result in smaller executables.
PlyTool
could be made to invoke the C++ compiler directly, without requiring CMake to generate an intermediate build system first.
It’ll depend what other people consider useful, so I’m interested to hear your thoughts. Which of those improvements is worth pursuing? Do you see a way to simplify something in Plywood? Have a question, or more of a comment than a question? I’ll be hanging out on the shiny new
Plywood Discord server
, so feel free to jump in and join the discussion! Otherwise, you can
contact me directly.
