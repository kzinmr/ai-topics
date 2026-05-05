---
title: "A Small Open Source Game In C++"
url: "https://preshing.com/20201126/a-small-open-source-game-in-cpp"
fetched_at: 2026-05-05T07:01:02.663787+00:00
source: "Preshing"
tags: [blog, raw]
---

# A Small Open Source Game In C++

Source: https://preshing.com/20201126/a-small-open-source-game-in-cpp

I just released a mobile game called
Flap Hero
. It’s a
Flappy Bird
clone with cartoony graphics and a couple of twists: You can go in the pipes (wow!) and it takes
two
collisions to end the game. Flap Hero is free, quick to download (between 3 - 5 MB) and opens instantly. Give it a try!
Flap Hero is
open source
, too. Its source code is released under the MIT license and its assets (3D models, sounds, music) are dedicated to the public domain. Do whatever you want with them! Everything’s available
on GitHub
.
I’m releasing this game to promote
Plywood
, an open source C++ framework I
released
a few months ago. Flap Hero was made using Plywood.
How Flap Hero Uses Plywood
If you only read up to this point, you might think that Plywood is a game engine.
It isn’t!
Plywood is best described as a “module-oriented” C++ framework. It gives you a workspace, a set of built-in modules and some (optional) code generation tricks.
Plywood currently has 36 built-in modules, none of which are specific to game development. For game-specific functionality, Flap Hero relies on several excellent third-party libraries:
Assimp
to load 3D models,
SoLoud
for audio,
stb
to load textures and fonts, and
GLFW
for desktop windowing & input.
If Flap Hero relies on third-party libraries, you might be wondering, what’s the point of Plywood? Well, those libraries have to be integrated into
something
. In Plywood, that something is the
Plywood workspace
. In this workspace, you can create your own
modules
that depend on other Plywood modules as well as on third-party libraries. You can then instantiate those modules in
build folders
, and they’ll bring all their dependencies along with them.
In addition to the aforementioned libraries, Flap Hero uses several built-in Plywood modules such as
runtime
,
math
and
image
. Plywood’s
runtime
module offers an alternative to the standard C and C++ runtimes, providing lean cross-platform I/O, strings, containers and more. The
math
module provides vectors, matrices, quaternions and other primitives. I’ll continue fleshing out the details of these modules in
Plywood’s documentation
over time.
A Framework for Efficient Software
Flap Hero is written entirely in C++ and isn’t built on any existing game engine. It keeps bloat to a minimum, resulting in a small download, fast load times, low memory usage, responsive controls and high framerate for the user, even on older devices. This is the “handmade” style of software development championed by communities such as the
Handmade Network
.
That’s the kind of software that Plywood is meant to help create. Still, Plywood is a work in progress. Here’s what I’d like to do next:
Improve the documentation
Create a GUI build manager
Open source more modules
I’m especially excited about the potential of a GUI build manager. The GUI build manager would be a graphical user interface that lets you manage the Plywood workspace interactively, bypassing the somewhat cumbersome
command line tool
. Ideally, this tool would have close integration with various package managers across different platforms. The goal would be to make it as simple as possible to integrate third-party libraries and get projects built on other machines – something that’s still a bit of a weak spot in Plywood.
The next post on this blog will be a review of Flap Hero’s source code. Stay tuned if that kind of thing interests you!
