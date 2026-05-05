---
title: "A Flexible Reflection System in C++: Part 1"
url: "https://preshing.com/20180116/a-primitive-reflection-system-in-cpp-part-1"
fetched_at: 2026-05-05T07:01:02.824945+00:00
source: "Preshing"
tags: [blog, raw]
---

# A Flexible Reflection System in C++: Part 1

Source: https://preshing.com/20180116/a-primitive-reflection-system-in-cpp-part-1

In this post, I’ll present a small, flexible system for
runtime reflection
using C++11 language features. This is a system to generate
metadata
for C++ types. The metadata takes the form of
TypeDescriptor
objects, created at runtime, that describe the structure of other runtime objects.
I’ll call these objects
type descriptors
. My initial motivation for writing a reflection system was to support
serialization
in my
custom C++ game engine
, since I have very specific needs. Once that worked, I began to use runtime reflection for other engine features, too:
3D rendering
: Every time the game engine draws something using OpenGL ES, it uses reflection to pass uniform parameters and describe vertex formats to the API. It makes graphics programming much more productive!
Importing JSON
: The engine’s asset pipeline has a generic routine to synthesize a C++ object from a JSON file and a type descriptor. It’s used to import 3D models, level definitions and other assets.
This reflection system is based on preprocessor macros and templates. C++, at least in its current form, was not designed to make runtime reflection easy. As anyone who’s written one knows, it’s tough to design a reflection system that’s easy to use, easily extended, and that actually works. I was burned many times by obscure language rules, order-of-initialization bugs and corner cases before settling on the system I have today.
To illustrate how it works, I’ve published a sample project
on GitHub:
This sample doesn’t actually use my game engine’s reflection system. It uses a tiny reflection system of its own, but the most interesting part – the way type descriptors are
created
,
structured
and
found
– is almost identical. That’s the part I’ll focus on in this post. In the next post, I’ll discuss how the system can be extended.
This post is meant for programmers who are interested in how to
develop
a runtime reflection system, not just use one. It touches on many advanced features of C++, but the sample project is only 242 lines of code, so hopefully, with some persistence, any determined C++ programmer can follow along. If you’re more interested in using an existing solution, take a look at
RTTR
.
Demonstration
In
Main.cpp
, the sample project defines a struct named
Node
. The
REFLECT()
macro tells the system to enable reflection for this type.
struct
Node {
    std::
string
key;
int
value;
    std::vector<Node> children;

    REFLECT()      
};
At runtime, the sample creates an object of type
Node
.
Node node = {
"
apple
"
,
3
, {{
"
banana
"
,
7
, {}}, {
"
cherry
"
,
11
, {}}}};
In memory, the
Node
object looks something like this:
Next, the sample finds
Node
’s type descriptor. For this to work, the following macros must be placed in a
.cpp
file somewhere. I put them in
Main.cpp
, but they could be placed in any file from which the definition of
Node
is visible.
REFLECT_STRUCT_BEGIN(Node)
REFLECT_STRUCT_MEMBER(key)
REFLECT_STRUCT_MEMBER(value)
REFLECT_STRUCT_MEMBER(children)
REFLECT_STRUCT_END()
Node
’s member variables are now said to be
reflected
.
A pointer to
Node
’s type descriptor is obtained by calling
reflect::TypeResolver<Node>::get()
:
reflect::TypeDescriptor* typeDesc = reflect::TypeResolver<Node>::get();
Having found the type descriptor, the sample uses it to dump a description of the
Node
object to the console.
This produces the following output:
How the Macros Are Implemented
When you add the
REFLECT()
macro to a struct or a class, it declares two additional static members:
Reflection
, the struct’s type descriptor, and
initReflection
, a function to initialize it. Effectively, when the macro is expanded, the complete
Node
struct looks like this:
struct
Node {
    std::
string
key;
int
value;
    std::vector<Node> children;
static
reflect::TypeDescriptor_Struct
Reflection
;
static
void
initReflection
(reflect::TypeDescriptor_Struct*);
};
Similarly, the block of
REFLECT_STRUCT_*()
macros in
Main.cpp
look like this when expanded:
reflect::TypeDescriptor_Struct Node::
Reflection
{Node::initReflection};
void
Node::
initReflection
(reflect::TypeDescriptor_Struct* typeDesc) {
using
T = Node;
    typeDesc->name =
"
Node
"
;
    typeDesc->size =
sizeof
(T);
    typeDesc->members = {
        {
"
key
"
, offsetof(T, key), reflect::TypeResolver<decltype(T::key)>::get()},
        {
"
value
"
, offsetof(T, value), reflect::TypeResolver<decltype(T::value)>::get()},
        {
"
children
"
, offsetof(T, children), reflect::TypeResolver<decltype(T::children)>::get()},
    };
}
Now, because
Node::Reflection
is a static member variable, its constructor, which accepts a pointer to
initReflection()
, is automatically called at program startup. You might be wondering: Why pass a function pointer to the constructor? Why not pass an
initializer list
instead? The answer is because the body of the function gives us a place to declare a C++11
type alias
:
using T = Node
. Without the type alias, we’d have to pass the identifier
Node
as an extra argument to every
REFLECT_STRUCT_MEMBER()
macro. The macros wouldn’t be as easy to use.
As you can see, inside the function, there are three additional calls to
reflect::TypeResolver<>::get()
. Each one finds the type descriptor for a reflected member of
Node
. These calls use C++11’s
decltype
specifier
to automatically pass the correct type to the
TypeResolver
template.
Finding TypeDescriptors
(Note that everything in this section is defined in the
reflect
namespace.)
TypeResolver
is a
class template
. When you call
TypeResolver<T>::get()
for a particular type
T
, the compiler instantiates a function that returns the corresponding
TypeDescriptor
for
T
. It works for reflected structs as well as for every reflected member of those structs. By default, this happens through the primary template, highlighted below.
By default, if
T
is a struct (or a class) that contains the
REFLECT()
macro, like
Node
,
get()
will return a pointer to that struct’s
Reflection
member  – which is what we want. For every other type
T
,
get()
instead calls
getPrimitiveDescriptor<T>
– a
function template
that handles primitive types such as
int
or
std::string
.
template
<
typename
T>
TypeDescriptor* getPrimitiveDescriptor();
struct
DefaultResolver {
    ...
template
<
typename
T, >
static
TypeDescriptor* get() {
return
&T::Reflection;
    }
template
<
typename
T, >
static
TypeDescriptor* get() {
return
getPrimitiveDescriptor<T>();
    }
};
template
<
typename
T>
struct
TypeResolver
{
static
TypeDescriptor*
get
() {
return
DefaultResolver::get<T>();
    }
};
This bit of compile-time logic – generating different code depending on whether a static member variable is present in
T
– is achieved using
SFINAE
. I omitted the SFINAE code from the above snippet because, quite frankly, it’s ugly. You can check the actual implementation
in the source code
. Part of it could be rewritten more elegantly using
if constexpr
, but I’m targeting C++11. Even then, the part that detects whether
T
has a specific member variable will remain ugly, at least until C++ adopts
static reflection
. In the meantime, however – it works!
The Structure of TypeDescriptors
In the sample project, every
TypeDescriptor
has a name, a size, and a couple of virtual functions:
struct
TypeDescriptor {
const
char
*
name
;
    size_t
size
;

    TypeDescriptor(
const
char
* name, size_t size) : name{name}, size{size} {}
virtual
~TypeDescriptor() {}
virtual
std::
string
getFullName
()
const
{
return
name; }
virtual
void
dump
(
const
void
* obj,
int
indentLevel =
0
)
const
=
0
;
};
The sample project never creates
TypeDescriptor
objects directly. Instead, the system creates objects of types derived from
TypeDescriptor
. That way, every type descriptor can hold extra information depending on, well, the
kind
of type descriptor it is.
For example, the actual type of the object returned by
TypeResolver<Node>::get()
is
TypeDescriptor_Struct
. It has one additional member variable,
members
, that holds information about every reflected member of
Node
. For each reflected member, there’s a pointer to another
TypeDescriptor
. Here’s what the whole thing looks like in memory. I’ve circled the various
TypeDescriptor
subclasses in red:
At runtime, you can get the full name of any type by calling
getFullName()
on its type descriptor. Most subclasses simply use the base class implementation of
getFullName()
, which returns
TypeDescriptor::name
. The only exception, in this example, is
TypeDescriptor_StdVector
, a subclass that describes
std::vector<>
specializations. In order to return a full type name, such as
"std::vector<Node>"
, it keeps a pointer to the type descriptor of its item type. You can see this in the above memory diagram: There’s a
TypeDescriptor_StdVector
object whose
itemType
member points all the way back to the type descriptor for
Node
.
Of course, type descriptors only describe
types
. For a complete description of a runtime object, we need both a type descriptor and a pointer to the object itself.
Note that
TypeDescriptor::dump()
accepts a pointer to the object as
const void*
. That’s because the abstract
TypeDescriptor
interface is meant to deal with
any
type of object. The subclassed implementation knows what type to expect. For example, here’s the implementation of
TypeDescriptor_StdString::dump()
. It casts the
const void*
to
const std::string*
.
virtual
void
dump(
const
void
* obj,
int
)
const
override {
    std::cout <<
"
std::string{
\"
"
<< *(
const
std::
string
*) obj <<
"
\"
}
"
;
}
You might wonder whether it’s safe to cast
void
pointers in this way. Clearly, if an invalid pointer is passed in, the program is likely to crash. That’s why, in my game engine, objects represented by
void
pointers always travel around with their type descriptors in pairs. By representing objects this way, it’s possible to write many kinds of generic algorithms.
In the sample project, dumping objects to the console is the only functionality implemented, but you can imagine how type descriptors could serve as a framework for serializing to a binary format instead.
In the next post, I’ll explain how to add built-in types to the reflection system, and what the “anonymous functions” are for in the above diagram. I’ll also discuss other ways to extend the system.
