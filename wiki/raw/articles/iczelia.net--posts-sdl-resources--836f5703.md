---
title: "SDL2: Easily embedding resources into applications."
url: "https://iczelia.net/posts/sdl-resources/"
fetched_at: 2026-05-05T07:01:21.236037+00:00
source: "Kamila Szewczyk (iczelia)"
tags: [blog, raw]
---

# SDL2: Easily embedding resources into applications.

Source: https://iczelia.net/posts/sdl-resources/

One of the issues I encounter notoriously often is managing resources. While loading auxiliary data from other files is a feasible option for large applications that supply gigabytes of textures, sounds and background music, it is rather inconvenient for small applications that are often under a megabyte in size. In this post, I would like to share my experiences and a reusable solution for embedding resources into SDL2 applications.
Asset types and the build system.
⌗
My solution works out-of-the-box for the following asset types:
Bitmaps (BMP)
TrueType fonts (TTF)
Wave files (WAV)
Icons (ICO)
However, it is easy to extend it to other kinds of auxiliary data, as demonstrated later.
My build system of choice for small C applications is just
make
. Assuming that all assets are located in the
assets/
directory, definining a few extra targets is enough to integrate the resource embedding into the build process:
The
assets
target is responsible for generating the
assets.h
and
assets.c
files, which contain the embedded resources. The
clean
target is responsible for truncating these files, so that they are regenerated on the next build. The
format
target is a minor convenience target responsible for formatting the source code using
clang-format
. The
all
target is responsible for building the entire program.
Generating the C source.
⌗
It is apparent that the
gen_assets.sh
script is responsible for generating the
assets.h
and
assets.c
files, which linked together with the program, provide the embedded resources. First, potential leftover data from previous runs is truncated:
Then, the
assets.h
file is generated.
The file will contain
extern
declarations of all resources defined in
assets.c
. In the meantime, a few useful macros are defined in
assets_load.c
to facilitate loading the resources of varying types from memory.
Freeing assets is slightly less complicated:
Next, the functions
assets_load()
and
assets_free()
are defined in their respective files:
Then, for every argument passed to the script, the data is embedded as follows:
After all files are processed, the script ends the loading and freeing functions and concatenates all auxiliary C files into a single
assets.c
file:
Source code
⌗
The final source code for the
gen_assets.sh
script can be found in the GitHub repository of
SDLMine
, a Minesweeper clone I wrote over a couple of hours in C using SDL2. Despite the license of the entire project (AGPLv3), feel free to use the script in your own projects as if it was licensed under CC0.
Compression
⌗
When distributing your application, it is advisable to compress the resulting executable using
UPX
. This will reduce the size of the executable by a significant amount, due to the fact that BMP, ICO and WAV assets are uncompressed. While beneficial for small applications (under a few megabytes), it may be troublesome for large programs, as UPX may take a long while to unpack the executable. Further, pages of uncompressed executables are usually loaded on demand, so the entire executable is not loaded into memory at once. This means that the executable will not take up as much space in memory as it does on disk (unless
mlockall(2)
or a similar system call is executed).
My
Spider Solitaire
game that uses a similar technique for asset embedding benefits from the use of
UPX
: the executable is reduced from 2.12MB to 442KB (around 80% reduction in size!). Compressing the executable with LZMA yields an even better reduction in size, down to 350KB, however UPX’s
--lzma
mode is notorious for its unreliability (
upx#60
,
upx#612
)
