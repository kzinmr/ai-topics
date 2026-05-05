---
title: "LLVM 3.0 Type System Rewrite"
url: "https://blog.llvm.org/2011/11/llvm-30-type-system-rewrite.html"
fetched_at: 2026-05-05T07:01:43.661608+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM 3.0 Type System Rewrite

Source: https://blog.llvm.org/2011/11/llvm-30-type-system-rewrite.html

LLVM 3.0 Type System Rewrite
One of the most pervasive IR (and thus compiler API) changes in LLVM 3.0 was a complete reimplementation of the LLVM IR type system. This change was long overdue (the original type system lasted from LLVM 1.0!) and made the compiler faster, greatly simplified a critical subsystem of VMCore, and eliminated some design points of IR that were frequently confusing and inconvenient. This post explains why the change was made along with how the new system works.
Goals of the type system
The
LLVM IR type system
is a fairly straight-forward part of the IR. The type system consists of three major parts: primitive types (like 'double' and integer types), derived types (like structs, arrays and vectors), and a mechanism for handling forward declarations of types ('opaque').
The type system has several important requirements that constrains its design: we want to be able to use efficient pointer equality checks to determine structural type equality, we want to allow late refinement of types (e.g. when linking, one module should be able to complete types in another module), we want it to be easy to express many different source languages, and we want a simple and predictable system.
The only really difficult part of an IR type system is handling forward declarations of types. To see this, observe that the type system is actually represented with a complex graph of types (which is often cyclic). For example, a simple singly linked list of integers might be declared like this:
%intlist = type { %intlist*, i32 }
In this case, the type graph includes a StructType which points to an IntegerType and a PointerType. The PointerType points back to the StructType. In many real programs the graph is complex and heavily cyclic, particularly for C++ applications.
With this as background, lets start by talking about how LLVM 2.9 and earlier worked.
The old type system
The
LLVM 2.9
type system has all of the straight-forward pieces and represents forward type declarations with an instance of
OpaqueType
. When this type is later resolved (e.g. at link time), a process know as "type refinement"
updates all pointers
to the old OpaqueType to point to the new definition, mutating the type graph on the fly, and then deletes the original OpaqueType. For example, if a module contained:
%T1 = type opaque
%T2 = type %T1*
then T2 is a PointerType to an OpaqueType. If we resolve %T1 to {} (an empty struct), then %T2
mutates
to be a PointerType to the empty StructType. For more information on this, please see the
type resolution section
of the LLVM 2.9 Programmer's Manual.
Ramifications of mutating and moving types
Unfortunately, while conceptually simple, this type system had several problems. In order to guarantee that pointer equality checks work for structural type equivalence checks, VMCore is required to re-unique types whenever they are mutated during type resolution. This may not seem like such a big deal, but a single type refinement can cause hundreds of other types to be mutated, and it is quite common to refine hundreds or thousands of types (e.g. when linking an application for LTO). The performance of this was not acceptable, particularly because uniquing cyclic graphs requires full graphic isomorphism checks to be done, and our previous implementation was not algorithmically efficient.
Another problem is that more than just types need to be updated: anything that contains a pointer to a type has to be updated, or it gets a dangling pointer. This issue manifested in a number of ways: for example every Value has a pointer to a type. In order to make the system a bit more efficient, Value::getType() actually performed a lazy "union find" step to ensure that it always returned a canonicalized and uniqued type. This made Value::getType() (a very common call) more expensive than it should be.
An even worse problem that this "type updating" problem caused is when you were manipulating and building IR through the LLVM APIs. Because types could move, it was very easy to get dangling pointers, causing a lot of confusion and a lot of broken clients of the LLVM API. This was compounded by the fact that it was
required
to use type refinement to build
simple recursive types
. We tried to make this simpler with the PATypeHolder and PATypeHandle classes, but they only worked if you used them exactly right and they were generally poorly understood.
Surprising behavior with type uniquing
Many clients of LLVM, once they got things working, then quickly ran into a surprising aspect of type uniquing: type names were not part of the type system, they were an "on the side" data structure. The names were not taking into consideration during type uniquing, and you could have multiple names for one type (which led to a lot of confusion). For example, consider:
%T1 = type opaque
@G1 = external global %T1*
%T2 = type {}
@G2 = external global %T2*
If %T1 was later resolved to {}, then %T1 and %T2 would both become names for the same empty structure type, the type formerly known as "%T1*" would be unified with the type formerly known as "%T2*", and now the IR would print out as:
%T1 = type {}
@G1 = external global %T1*
%T2 = type {}
@G2 = external global %T1*
... note that G2 now has type "%T1*"! This is because the names in the type system was just a hash table on the side, so that asmprinter would pick one of the arbitrarily large number of names for a type when printing. This was "correct", but highly confusing the folks who did not know the ins and outs of the type system, and not helpful behavior. It also made reading .ll dumps from a C++ compiler very difficult, because it is very common to have many structurally identical types with different names.
Type Up-references
A final problem (that I don't want to dwell on too much) is that we previously could have the situation where a type existed that had no name at all. While this is fine from the type system graph's perspective, this made printing types impossible if they were cyclic and had no names. The solution to this problem was a system known as
type up-references
.
Type up-references were an elegant solution that allowed the asmprinter (and parser) to be able to represent an arbitrary recursive type in finite space, without requiring names. For example, the %intlist example above could be represented as "{\2*, i32}". It also allowed for construction of some nice (but surprising) types like "\1*" which was a pointer to itself!
Despite having some amount of beauty and elegance, type up-references were never well understood by most people and caused a lot of confusion. It is important to be able to strip the names out of an LLVM IR module (e.g. the -strip pass), but it is also important for compiler hackers to be able to understand the system!
Preparing for the new type system
With all of these problems, I realized that LLVM needed a newer and simpler type system. However, it is also important that new versions of LLVM be able to read old .bc and .ll files. To enable this, the big rewrite was carefully staged: the LLVM 2.9 asmprinter was enhanced to emit opaque types as numbered types instead of using up-references. Therefore, instead of emitting the %intlist example with up-references, LLVM 2.9 would emit it as:
%0 = type { %0*, i32 }
The plan for LLVM 3.0 was to drop compatibility with LLVM 2.8 (and earlier) files, so this made the "upgrade" logic needed in LLVM 3.0 much simpler.
The LLVM 3.0 Type System
To most clients, the new type system in LLVM 3.0 looks and smells a lot like the 2.9 type system. For example, .bc files and .ll files produced by LLVM 2.9 are readable and automatically upgraded to 3.0 features when read by the bitcode reader and .ll parser (though LLVM 3.1 will drop compatibility with 2.9). This is because the type system retains almost everything it had before: the primitive and derived types are the same, only OpaqueType has been removed and StructType has been enhanced.
In short, instead of a refinement based type system where types mutate in memory (requiring re-uniquing and moving/updating of pointers), LLVM 3.0 uses a type system very similar to what C has, based on type
completion
. Basically, instead of creating an opaque type and replacing it later, you now create an StructType with no body, then specify the body later. To create the %intlist type, you'd now write something like this:
StructType *IntList = StructType::create(SomeLLVMContext, "intlist");
Type *Elts[] = { PointerType::getUnqual(IntList), Int32Type };
IntList->setBody(Elts);
... which is simple and to the point, much better than
the 2.9 way
. There are a few non-obvious ramifications to this design though.
Only struct types can be recursive
In the previous type system, an OpaqueType could be resolved to any arbitrary type, allowing such oddities as "%t1 = type %t1*", which is a pointer to itself. In the new type system, only IR structure types can have their body missing, so it is impossible to create a recursive type that doesn't involve a struct.
Literal and Identified structs
In the new type system, there are actually two different kinds of structure type: a "literal" structure (e.g. "{i32, i32}") and an "identified" structure (e.g. "%ty = type {i32, i32}").
Identified structures are the kind we are talking about: they can have a name, and can have their body specified after the type is created. The identified structure is not uniqued with other structure types, which is why they are produced with StructType::create(...). Because identified types are potentially recursive, the asmprinter always prints them by their name (or a number like %42 if the identified struct has no name).
Literal structure types work similarly to the old IR structure types: they never have names and are uniqued by
structural
identity: this means that they must have their body elements available at construction time, and they can never be recursive. When printed by the asmprinter, they are always printed inline without a name. Literal structure types are created by the StructType::get(...) methods, reflecting that they are uniqued (the call may or may not actually allocate a new StructType).
We expect that identified structure types will be the most common, and that a frontend will only produce a literal structure type in special cases. For example, it is reasonable to use literal structure types for tuples, complex numbers, and other simple cases where a name would be arbitrary and would make the IR more difficult to read. The optimizer doesn't care one way or the other, so if you're the author of a front-end, just use whatever you prefer to see in your IR dumps.
Identified structs have a 1-1 mapping with a name
Where type names were kept as an "on the side" hash table before, they are now an intrinsic part of a type, and the only types that can be named are identified structs. This means that LLVM 3.0 doesn't exhibit the previous confusing behavior where two seemingly different structs would be printed with the same name. When stripping type names from a module, the identified structs just become anonymous: they are still 'identified', but they have no name. As with other anonymous entities in LLVM IR, they are asmprinted in a numeric form.
Struct names are uniqued at the LLVMContext level
Because StructType::create always returns a new identified type, we need some behavior for when you try to create two types with the same name. The solution is that VMCore detects the conflict and autorenames the later request by adding a suffix to the type: when you request a "foo" type, you may actually get back a type named "foo.42". This is consistent with other IR objects like instructions and functions, and the names are uniqued at the LLVMContext level.
The Linker "links" types and retypes IR objects
An interesting aspect of this design is that it makes the IR linker's job a bit more complex. Consider what happens when you link these two IR modules together:
x.ll:
%A = type { i32 }
@G = external global %A
y.ll:
%A = type { i32 }
@G = global %A zeroinitializer
The first thing the linker does is load the two modules into the same LLVMContext. Since the two types named "A"
must be different
types, and since there can only be one type named %A, we actually get these two modules in memory:
x.ll module:
%A = type { i32 }
@G = external global %A
y.ll module:
%A.1 = type { i32 }
@G = global %A.1 zeroinitializer
... and now it is quite clear that the @G objects have different types. When linking these two global variables, it is now up to the linker to remap the types of IR objects into a consistent set of types, and rewrite things into a consistent state. This requires the linker to compute the set of identical types and solve the same graph isomorphism problems that VMCore used to (see the "remapType" logic in lib/Linker/LinkModules.cpp if you're interested).
Putting this logic in the IR linker instead of VMCore is better that the previous design on many levels: now the cost for this merging and uniquing is only paid by the IR linker, not by all bitcode reading and other IR creation code. The code is easier to understand and algorithmically optimize, because we're merging two complete graphs at once - instead of resolving types one at a time. Finally, this shrinks the size of VMCore by moving some complex logic out of it.
Identifying magic IR types in the optimizer (or later)
As in LLVM 2.9, type names are not really designed to be used as semantic information in IR: we expect everything to continue working if the -strip pass is used to remove all extraneous names from the IR. However, for research and other purposes, it can sometimes be a convenient hack to propagate information from a front-end into LLVM IR by using type names. This will work reliably in LLVM 3.0 (so long as you don't run the strip pass or something equivalent) because identified types aren't uniqued. However, be aware that the suffix can be added and write your code to tolerate it.
A more robust way to be able to identify a specific type in the optimizer (or some other point after the frontend has run) is to use a named metadata node to find the type. For example, if you want to find the %foo type, you could generate IR that looks like this:
%foo = type { ... }
...
!magic.types = !{ %foo zeroinitializer }
Then to find the "foo" type, you'd just look up the "magic.types" named metadata, and get the type of the first element. Even if type names are stripped or types get auto-renamed, the type of the first element will always be correct and stable.
There seems to be some confusion around named metadata: unlike instruction-level metadata, they will
not
be dropped or invalidated by optimizer passes (so long as they don't point to functions or other IR objects that are modified by the optimizer). In general, named metadata is a much, much, better way to pass information from a frontend to an optimizer or backend than trying to play games with type names.
Conclusion
In conclusion, the new type system has solved a number of long-standing problems in LLVM IR. If you're upgrading some code from LLVM 2.x to 3.x, it is likely to be something that you'll run into. Hopefully, this helps answer some common questions about why we made the change and how it works!
-
Chris Lattner
