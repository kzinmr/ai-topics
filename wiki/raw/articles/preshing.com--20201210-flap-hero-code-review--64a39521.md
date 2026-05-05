---
title: "Flap Hero Code Review"
url: "https://preshing.com/20201210/flap-hero-code-review"
fetched_at: 2026-05-05T07:01:02.865023+00:00
source: "Preshing"
tags: [blog, raw]
---

# Flap Hero Code Review

Source: https://preshing.com/20201210/flap-hero-code-review

Flap Hero is a small game written entirely in C++ without using an existing game engine. All of its source code is available
on GitHub
. I think it can serve as an interesting resource for novice and intermediate game developers to study.
In this post, I’ll explain how Flap Hero’s code is organized, how it differs from larger game projects, why it was written that way, and what could have been done better.
Very little information in this post is specific to C++. Most of it would still be relevant if Flap Hero was written in another language like C#, Rust or plain C. That said, if you browse (or build) the source code, you will need some fluency in C++.
Learn C++
and
Learn OpenGL
are two great resources for beginners. For the most part, Flap Hero’s source code sticks to a fairly straightforward subset of C++, but the deeper you go into its low-level modules (like
runtime
), the more you’ll encounter advanced C++ features like templates and SFINAE.
General Architecture
Flap Hero was developed using
Plywood
, a C++ framework that helps organize code into reusable modules. Each yellow box in the diagram below represents a Plywood module. The blue arrows represent dependencies.
platform
runtime
image
math
plywood
repo
flapGame
glfwFlap
GameFlow.cpp
GameState.cpp
Collision.cpp
Text.cpp
FlapHero
repo
Public.h
glfw
soloud
glad
assimp
Main.cpp
iOS project
Android project
iOS project
iOS project
Windows,
Linux
& macOS
Assets.cpp
GLHelpers.cpp
The biggest chunk of Flap Hero’s game code is located in the
flapGame
module, which contains roughly 6400 physical lines of code. The two most important source files in the
flapGame
module are
GameFlow.cpp
and
GameState.cpp
.
All the state for a single gameplay session is held inside a single
GameState
object. This object is, in turn, owned by a
GameFlow
object. The
GameFlow
can actually own two
GameState
objects at a given time, with both gameplay sessions updating concurrently. This is used to achieve an animated “split screen” effect during the transition from one gameplay session to the next.
GameState
GameState
GameFlow
The
flapGame
module is meant to be incorporated into a main project. On desktop operating systems, the main project is implemented by the
glfwFlap
module. The
glfwFlap
module is responsible for initializing the game’s OpenGL context and for passing input and update events to
flapGame
. (Android and iOS use completely different main projects, but those serve the same purpose as
glfwFlap
.)
glfwFlap
communicates with
flapGame
using an API defined in a single file:
Public.h
. There are only 13 functions in this API, and not all of them are used on every platform.
As Few Subsystems As Possible
Flap Hero is not based on an existing game engine. It’s just a C++ program that, when you run it, plays Flap Hero! As such, it doesn’t contain many of the
subsystems
found in a typical game engine. This was a deliberate choice. Flap Hero is a sample application, and I wanted to implement it using as little code as possible.
What do I mean by “subsystem”? I’ll give a few examples in the following sections. In some cases, it was OK to not have the subsystem; in other cases, it turned out to be a disadvantage. I’ll give a verdict for each one as we go.
No Abstract Scene Representation
In a typical game engine, there’s an intermediate representation of the 3D (or 2D) scene consisting of a bunch of abstract objects. In Godot, those objects inherit from
Spatial
; in Unreal, they’re
AActor
instances; in Unity, they’re
GameObject
instances. All of these objects are
abstract
, meaning that the details of how they’re rendered to the screen are filled in by subclasses or components.
One benefit of this approach is that it lets the renderer perform view frustum culling in a generic way. First, the renderer determines which objects are visible, then it effectively tells those objects to draw themselves. Ultimately, each object issues a series of draw calls to the underlying graphics API, whether it’s OpenGL, Metal, Direct3D, Vulkan or something else.
Renderer
Graphics API
Scene
abstract objects
Flap Hero has no such scene representation. In Flap Hero, rendering is performed using a dedicated set of functions that issue OpenGL calls directly. Most of the interesting stuff happens in the
renderGamePanel()
function. This function draws the bird, then the floor, then the pipes, then the shrubs, the cities in the background, the sky, the clouds, particle effects, and finally the UI layer. That’s it. No abstract objects are involved.
Renderer
Graphics API
For a game like Flap Hero, where the contents of the screen are similar every frame, this approach works perfectly fine.
Verdict: OK
Obviously, this approach has its limitations. If you’re making a game involving exploration, where the contents of the screen can differ greatly from one moment to the next, you’re going to want some kind of abstract scene representation. Depending on the style of game, you could even take a hybrid approach. For example, to make Flap Hero draw different obstacles instead of just pipes, you could replace the code that draws pipes with code that draws a collection of arbitrary objects. The rest of the
renderGamePanel()
function would remain the same.
No Shader Manager
Since the original Xbox, every game engine I’ve worked on has included some kind of shader manager. A shader manager allows game objects to refer to shader programs indirectly using some sort of “shader key”. The shader key typically describes which features are needed to render each mesh, whether it’s skinning, normal mapping, detail texturing or something else. For maximum flexibility, shader inputs are often passed to the graphics API automatically using some kind of reflection system.
Flap Hero has none of that. It has only a fixed set of shader programs.
Shaders.cpp
contains the source code for 15 shaders, and
Text.cpp
contains 2 more. There’s a dedicated shader for the pipes, another for the smoke cloud particles, a couple that are only used in the title screen. All shaders are compiled at startup.
Moreover, in Flap Hero, all shader parameters are managed
by hand
. What does that mean? It means that the game extracts the locations of all vertex attributes and uniform variables using code that is
written by hand for each shader
. Similarly, when the shader is used for drawing, the game passes uniform variables and configures vertex attributes using code
written by hand for each shader
.
matShader->vertPositionAttrib =
        GL_NO_CHECK(GetAttribLocation(matShader->shader.id,
"
vertPosition
"
));
    PLY_ASSERT(matShader->vertPositionAttrib >=
0
);
    matShader->vertNormalAttrib =
        GL_NO_CHECK(GetAttribLocation(matShader->shader.id,
"
vertNormal
"
));
    PLY_ASSERT(matShader->vertNormalAttrib >=
0
);
    ...
This approach became really tedious after the 16th or 17th shader.
Verdict: Bad
I found myself really missing the shader manager I had developed for my
custom game engine
, which uses runtime reflection to automatically configure vertex attributes and pass uniform variables. In other words, it takes care of a lot of “glue code” automatically. The main reason why I didn’t use a similar system in Flap Hero is because again, Flap Hero is a sample application and I didn’t want to bring in too much extra machinery.
Incidentally, Flap Hero uses the
glUniform
family of OpenGL functions to pass uniform variables to shaders. This approach is old-fashioned but easy to implement, and helps catch programming errors if you accidentally pass a uniform that the shader doesn’t expect. The more modern approach, which incurs less driver overhead, is to use
Uniform Buffer Objects
.
No Physics Engine
Many game engines incorporate a physics engine like
Bullet
,
Havok
or
Box2D
. Each of these physics engines uses an approach similar to the “abstract scene representation” described above. They each maintain their own representation of physics objects in a collection known as the
physics world
. For example, in Bullet, the physics world is represented by a
btDiscreteDynamicsWorld
object and contains a collection of
btCollisionObject
s. In Box2D, there’s a
b2World
containing
b2Body
objects.
You can almost think of the physics world as a game within a game. It’s more or less self-sufficient and independent of the game engine containing it. As long as the game keeps calling the physics engine’s step function – for example,
b2World::Step
in Box2D – the physics world will keep running on its own. The game engine takes advantage of the physics world by examining it after each step, using the state of physics objects to drive the position & orientation of its own game objects.
Physics World
physics objects
Scene
game objects
Flap Hero contains some primitive physics, but doesn’t use a physics engine. All Flap Hero needs is to check whether the bird collided with something. For collision purposes, the bird is treated as a sphere and the pipes are treated as cylinders. Most of the work is done by the
sphereCylinderCollisionTest()
function, which detects sphere-cylinder collisions. The sphere can collide with three parts of the cylinder: the side, the edge or the cap.
Side
Edge
Cap
For an arcade-style game like Flap Hero that only needs a few basic collision checks, this is good enough. A physics engine isn’t necessary and would have only added complexity to the project. The amount of code needed to integrate a physics engine would likely have been greater than the amount of code needed to perform the collision checks ourselves.
Verdict: Good
Having said that, if you’re working with a game engine that already has an integrated physics engine, it often makes sense to use it. And for games requiring collisions between multiple objects, like the debris in a first-person shooter or the collapsing structures in Angry Birds, physics engines are definitely the way to go.
No Asset Pipeline
By “asset”, I’m referring to data files that are loaded by the game: mainly textures, meshes, animations and sounds. I wrote about asset pipelines in an earlier post about
writing your own game engine
.
Flap Hero doesn’t have an asset pipeline and has no game-specific formats. Each of its assets is loaded from the format that was used to create it. The game imports 3D models from FBX using
Assimp
; decodes texture images from PNG using
stb_image
; loads a TrueType font and creates a texture atlas using
stb_truetype
; and decodes a 33-second Ogg Vorbis music file using
stb_vorbis
. All of this happens when the game starts up. Despite the amount of processing, the game still loads fairly quickly.
If Flap Hero had an asset pipeline, most of that processing would be performed ahead of time using an offline tool (often known as the “cooker”) and the game would start even more quickly. But I wasn’t worried about that. Flap Hero is just a sample project, and I didn’t want to introduce additional build steps. In the end, though, I have to admit that the lack of an asset pipeline made certain things more difficult.
Verdict: Bad
If you explore the way
materials are associated with 3D meshes
in Flap Hero, you’ll see what I mean. For example, the materials used to draw the bird have several properties: diffuse color, specular color, rim light color, specular exponent and rim light falloff. Not all of these properties can be represented in the FBX format. As a result, I ended up ignoring the FBX material properties and defining new materials entirely in code.
With an asset pipeline in place, that wouldn’t be necessary. For example, in my custom game engine, I can define arbitrary material properties in Blender and export them directly to a flexible in-game format. Each time a mesh is exported, the game engine reloads it on-the-fly, even when the game running on a mobile device. This approach is great for iteration times, but obviously takes a lot of work to set up in the first place.
