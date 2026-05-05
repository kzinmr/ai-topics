---
title: "Jonathan Shapiro's Retrospective Thoughts on BitC"
url: "https://danluu.com/bitc-retrospective/"
fetched_at: 2026-05-05T07:01:36.260871+00:00
source: "Dan Luu"
tags: [blog, raw]
---

# Jonathan Shapiro's Retrospective Thoughts on BitC

Source: https://danluu.com/bitc-retrospective/

This is an archive of the Jonathan Shapiro's "Retrospective Thoughts on BitC" that seems to have disappeared from the internet; at the time, BitC was aimed at the same niche as Rust
Jonathan S. Shapiro shap at eros-os.org
Fri Mar 23 15:06:41 PDT 2012
By now it will be obvious to everyone that I have stopped work on BitC. An explanation of
why
seems long overdue.
One answer is that work on Coyotos stopped when I joined Microsoft, and the work that I am focused on
now
doesn't really require (or seem to benefit from) BitC. As we all know, there is only so much time to go around in our lives. But that alone wouldn't have stopped me entirely.
A second answer is that BitC isn't going to work in its current form. I had hit a short list of issues that required a complete re-design of the language and type system followed by a ground-up new implementation. Experience with the first implementation suggested that this would take quite a while, and it was simply more than I could afford to take on without external support and funding. Programming language work is not easy to fund.
But the third answer may of greatest interest, which is that I no longer believe that type classes "work" in their current form from the standpoint of language design. That's the only important science lesson here.
In the large, there were four sticking points for the current design:
The compilation model.
The insufficiency of the current type system w.r.t. by-reference and reference types.
The absence of some form of inheritance.
The instance coherence problem.
The first two issues are in my opinion solvable, thought the second requires a nearly complete re-implementation of the compiler. The last (instance coherence) does not appear to admit any general solution, and it raises conceptual concerns about the use of type classes for method overload in my mind. It's sufficiently important that I'm going to deal with the first three topics here and take up the last as a separate note.
Inheritance is something that people on the BitC list might (and sometimes have) argue about strongly. So a few brief words on the subject may be relevant.
BitC was initially designed as an [imperative] functional language because of our focus on software verification. Specification of the typing and semantics of functional languages is an area that has a
lot
of people working on it. We (as a field)
kind
of know how to do it, and it was an area where our group at Hopkins didn't know very much when we started. Software verification is a known-hard problem, doing it over an imperative language was already a challenge, and this didn't seem like a good place for a group of novice language researchers to buck the current trends in the field. Better, it seemed, to choose our battles. We knew that there were interactions between inheritance and inference
,
and it
appeared
that type classes with clever compilation could achieve much of the same operational results. I therefore decided early
not
to include inheritance in the language.
To me, as a programmer, the removal of inheritance and objects was a very reluctant decision, because it sacrificed any possibility of transcoding the large body of existing C++ code into a safer language. And as it turns out, you can't really remove the underlying semantic challenges from a successful systems language. A systems language
requires
some mechanism for existential encapsulation. The
mechanism
which embodies that encapsulation isn't really the issue; once you introduce that sort of encapsulation, you bring into play most of the verification issues that objects with subtyping bring into play, and once you do that, you might as well gain the benefit of objects. The remaining issue, in essence, is the modeling of the Self type, and for a range of reasons it's fairly essential to have a Self type in a systems language once you introduce encapsulation. So you end up pushed in to an object type system at some point in
any
case. With the benefit of eight years of hindsight, I can now say that this is perfectly obvious!
I'm strongly of the opinion that multiple inheritance is a mess. The argument pro or con about single inheritance still seems to me to be largely a matter of religion. Inheritance and virtual methods certainly aren't the
only
way to do encapsulation, and they may or may not be the best primitive mechanism. I have always been more interested in getting a large body of software into a safe, high-performance language than I am in innovating in this area of language design. If transcoding current code is any sort of goal, we need something very similar to inheritance.
The last reason we left objects out of BitC initially was purity. I wanted to preserve a powerful, pure subset language - again to ease verification. The object languages that I knew about at the time were heavily stateful, and I couldn't envision how to do a non-imperative object-oriented language. Actually, I'm
still
not sure I can see how to do that practically for the kinds of applications that are of interest for BitC. But as our faith in the value of verification declined, my personal willingness to remain restricted by purity for the sake of verification decayed quickly.
The
other
argument for a pure subset language has to do with advancing concurrency, but as I really started to dig in to concurrency support in BitC, I came increasingly to the view that this approach to concurrency isn't a good match for the type of concurrent problems that people are actually trying to solve, and that the needs and uses for non-mutable state in practice are a lot more nuanced than the pure programming approach can address. Pure subprograms clearly play an important role, but they aren't enough.
And I
still
don't believe in monads. :-)
Compilation Model
One of the objectives for BitC was to obtain acceptable performance under a conventional, static separate compilation scheme. It may be short-sighted on my part, but complex optimizations at run-time make me very nervous from the standpoint of robustness and assurance. I understand that bytecode virtual machines today do very aggressive optimizations with considerable success, but there are a number of concerns with this:
For a robust language, we want to
minimize
the size and complexity of the code that is exempted from type checking and [eventual] verification. Run-time code is excepted in this fashion. The garbage collector taken alone is already large enough to justify assurance concerns. Adding a large and complex optimizer to the pile drags the credibility of the assurance story down immeasurably.
Run-time optimization has very negative consequences for startup times
especially in the context of transaction processing. Lots of hard data on this from IBM (in DB/2) and others. It is one of the reasons that "Java in the database" never took hold. As the frequency of process and component instantiation in a system rises, startup delays become more and more of a concern. Robust systems don't recycle subsystems.
Run-time optimization adds a
huge
amount of space overhead to the run-time environment of the application. While the
code
of the run-time compiler can be shared, the
state
of the run-time compiler cannot, and there is quite a lot of that state.
Run-time optimization - especially when it is done "on demand" - introduces both variance and unpredictability into performance numbers. For some of the applications that are of interest to me, I need "steady state" performance. If the code is getting optimized on the fly such that it improves by even a modest constant factor, real-time scheduling starts to be a very puzzling challenge.
Code that is
produced
by a run-time optimizer is difficult to share across address spaces, though this probably isn't solved very well by * other* compilation approaches models either.
If run-time optimization is present, applications will come to rely on it for performance. That is: for social reasons, "optional" run-time optimization tends to quickly become required.
To be clear, I'm
not
opposed to continuous compilation. I actually think it's a good idea, and I think that there are some fairly compelling use-cases. I
do
think that the run-time optimizer should be implemented in a strongly typed, safe language. I
also
think that it took an awfully long time for the hotspot technology to stabilize, and that needs to be taken as a cautionary tale. It's also likely that many of the problems/concerns that I have enumerated can be solved - but probably not * soon*. For the applications that are most important to me, the concerns about assurance are primary. So from a language design standpoint, I'm delighted to exploit continuous compilation, but I don't want to design a language that
requires
continuous compilation in order to achieve reasonable baseline performance.
The optimizer complexity issue, of course, can be raised just as seriously for conventional compilers. You are going to optimize
somewhere
. But my experience with dynamic translation tells me that it's a lot easier to do (and to reason about) one thing at a time. Once we have a high-confidence optimizer in a safe language,
then
it may make sense to talk about integrating it into the run-time in a high-confidence system. Until then, separation of concerns should be the watch-word of the day.
Now strictly speaking, it should be said that run-time compilation actually isn't necessary for BitC, or for any other bytecode language. Run-time compilation doesn't become necessary until you combine run-time loading with compiler-abstracted representations (see below) and allow types having abstracted representation to appear in the signatures of run-time loaded libraries. Until then it is possible to maintain a proper phase separation between code generation and execution. Read on - I'll explain some of that below.
In any case, I knew going in that strongly abstracted types would raise concerns on this issue, and I initially adopted the following view:
Things like kernels can be whole-program compiled. This effectively eliminates the run-time optimizer requirement.
Things like critical system components want to be statically linked anyway, so they can
also
be dealt with as whole-program compilation problems.
For everything else, I hoped to adopt a kind of "template expansion" approach to run-time compilation. This wouldn't undertake the full complexity of an optimizer; it would merely extend run-time linking and loading to incorporate span and offset resolution. It's still a lot of code, but it's not horribly
complex
code, and it's the kind of thing that lends itself to rigorous - or even formal - specification.
It took several years for me to realize that the template expansion idea wasn't going to produce acceptable baseline performance. The problem lies in the interaction between abstract types, operator overloading, and inlining.
Compiler-Abstracted Representations vs. Optimization
Types have representations. This sometimes seems to make certain members of the PL community a bit uncomfortable. A thing to be held at arms length. Very much like a zip-lock bag full of dog poo (insert cartoon here). From the perspective of a systems person, I regret to report that where the bits are placed, how big they are, and their assemblage actually
does
matter. If you happen to be a dog owner, you'll note that the "bits as dog poo" analogy is holding up well here. It seems to be the lot of us systems people to wade daily through the plumbing of computational systems, so perhaps that shouldn't be a surprise. Ahem.
In any case, the PL community set representation issues aside in order to study type issues first. I don't think that pragmatics was forgotten, but I think it's fair to say that representation issues are not a focus in current, mainstream PL research. There is even a school of thought that views representation as a fairly yucky matter that should be handled in the compiler "by magic", and that imperative operations should be handled that way too. For systems code that approach doesn't work, because a lot of the representations and layouts we need to deal with are dictated to us by the hardware.
In any case, types
do
have representations, and knowledge of those representations is utterly essential for even the simplest compiler optimizations. So we need to be a bit careful not to abstract types* too * successfully
,
lest we manage to break the compilation model.
In C, the "+" operator is primitive, and the compiler can always select the appropriate opcode directly. Similarly for other "core" arithmetic operations. Now try a thought experiment: suppose we take every use of such core operations in a program and replace each one with a functionally equivalent procedure call to a runtime-implemented intrinsic. You only have to do this for
user
operations - addition introduced by the compiler to perform things like address arithmetic is always done on concrete types, so those can still be generated efficiently. But even though it is only done for user operations, this would clearly harm the performance of the program quite a lot. You
can
recover that performance with a run-time optimizer, but it's complicated.
In C++, the "+" operator can be overloaded. But (1) the bindings for primitive types cannot be replaced, (2) we know, statically, what the bindings and representations
are
for the other types, and (3) we can control, by means of inlining, which of those operations entail a procedure call at run time. I'm not trying to suggest that we want to be forced to control that manually. The key point is that the compiler has enough visibility into the implementation of the operation that it is possible to inline the primitive operators (and many others) at static compile time.
Why is this possible in C++, but not in BitC?
In C++, the instantiation of an abstract type (a template) occurs in an environment where complete knowledge of the representations involved is visible to the compiler. That information may not all be in scope to the programmer, but the compiler can chase across the scopes, find all of the pieces, assemble them together, and understand their shapes. This is what induces the "explicit instantiation" model of C++. It also causes a lot of "internal" type declarations and implementation code to migrate into header files, which tends to constrain the use of templates and increase the number of header file lines processed for each compilation unit - we measured this at one point on a very early (pre templates) C++ product and found that we processed more than 150 header lines for each "source" line. The ratio has grown since then by at least a factor of ten, and (because of templates) quite likely 20.
It's all rather a pain in the ass, but it's what makes static-compile-time template expansion possible. From the
compiler
perspective, the types involved (and more importantly, the representations) aren't abstracted at all. In BitC,
both
of these things
are
abstracted at static compile time. It isn't until link time that all of the representations are in hand.
Now as I said above, we can imagine extending the linkage model to deal with this. All of that header file information is supplied to deal with * representation* issues, not type checking. Representation, in the end, comes down to sizes, alignments, and offsets. Even if we don't know the concrete values, we
do
know that all of those are compile-time constants, and that the results we need to compute at compile time are entirely formed by sums and multiples of these constants. We could imagine dealing with these as
opaque
constants at static compile time, and filling in the blanks at link time. Which is more or less what I had in mind by link-time template expansion. Conceptually: leave all the offsets and sizes "blank", and rely on the linker to fill them in, much in the way that it handles relocation.
The problem with this approach is that it removes key information that is needed for optimization and registerization, and it doesn't support inlining. In BitC, we can
and do
extend this kind of instantiation all the way down to the primitive operators! And perhaps more importantly, to primitive accessors and mutators. The reason is that we want to be able to write expressions like "a + b" and say "that expression is well-typed provided there is an appropriate resolution for +:('a,'a)->'a". Which is a fine way to
type
the operation, but it leaves the representation of 'a fully abstracted. Which means that we cannot see when they are primitive types. Which means that we are
exactly
(or all too often, in any case) left in the position of generating
all
user-originated "+" operations as procedure calls. Now surprisingly, that's actually not the end of the world. We can imagine inventing some form of "high-level assembler" that our static code generator knows how to translate into machine code. If the static code generator does this, the run-time loader can be handed responsibility for emitting procedure calls, and can substitute intrinsic calls at appropriate points. Which would cause us to lose code sharing, but that might be tolerable on non-embedded targets.
Unfortunately, this kind of high-level assembler has some fairly nasty implications for optimization: First, we no longer have any idea what the * cost* of the "+" operator is for optimization purposes. We don't know how many cycles that particular use of + will take, but more importantly, we don't know how many bytes of code it will emit. And without that information there is a very long list of optimization decisions that we can no longer make at static compile time. Second, we no longer have enough information at static code generation time to perform a long list of
basic
register and storage optimizations, because we don't know which procedure calls are actually going to use registers.
That creaking and groaning noise that you are hearing is the run-time code generator gaining weight and losing reliability as it grows. While the impact of this mechanism actually wouldn't be as bad as I am sketching - because a lot of user types
aren't
abstract - the
complexity
of the mechanism really is as bad as I am proposing. In effect we end up deferring code generation and optimization to link time. That's an idea that goes back (at least) to David Wall's work on link time register optimization in the mid-1980s. It's been explored in many variants since then. It's a compelling idea, but it has pros and cons.
What is going on here is that types in BitC are
too
successfully abstracted for static compilation. The result is a rather
large
bag of poo, so perhaps the PL people are on to something.:-)
Two Solutions
The most obvious solution - adopted by C++ - is to redesign the language so that representation issues are not hidden from the compiler. That's actually a solution that is worth considering. The problem in C++ isn't so much the number of header file lines per source line as it is the fact that the C preprocessor requires us to process those lines
de novo
for each compilation unit. BitC lacks (intentionally) anything comparable to the C preprocessor.
The other possibility is to shift to what might be labeled "install time compilation". Ship some form of byte code, and do a static compilation at install time. This gets you back all of the code sharing and optimization that you might reasonably have expected from the classical compilation approach, it opens up some interesting design point options from a systems perspective, and (with care) it can be retrofitted to existing systems. There are platforms today (notably cell phones) where we basically do this already.
The design point that you don't want to cross here is dynamic
loading
where the loaded interface carries a type with an abstracted representation. At that point you are effectively committing yourself to run-time code generation
,
though I do have some ideas on how to mitigate that.
Conclusion Concerning Compilation Model
If static, separate compilation is a requirement, it becomes necessary for the compiler to see into the source code across module boundaries whenever an abstract type is used. That is: any procedure having abstract type must have an exposed source-level implementation.
The practical alternative is a high-level intermediate form coupled with install-time or run-time code generation. That is certainly feasible, but it's more that I felt I could undertake.
That's all manageable and doable. Unfortunately, it isn't the path we had taken on, so it basically meant starting over.
Insufficiency of the Type System
At a certain point we had enough of BitC working to start building library code. It may not surprise you that the first thing we set out to do in the library was IO. We found that we couldn't handle typed input within the type system. Why not?
Even if you are prepared to do dynamic allocation within the IO library, there is a level of abstraction at which you need to implement an operation that amounts to "inputStream.read(someObject: ByRef mutable 'a)" There are a couple of variations on this, but the point is that you want the ability at some point to move the incoming bytes into previously allocated storage. So far so good.
Unfortunately, in an effort to limit creeping featurism in the type system, I had declared (unwisely, as it turned out) that the only place we needed to deal with ByRef types was at parameters. Swaroop took this statement a bit more literally than I intended. He noticed that if this is
really
the only place where ByRef needs to be handled, then you can internally treat "ByRef 'a" as 'a, merely keeping a marker on the parameter's identifier record to indicate that an extra dereference is required at code generation time. Which is actually quite clever, except that it doesn't extend well to signature matching between type classes and their instances. Since the argument type for
read
is
ByRef 'a
, InputStream is such a type class.
So now we were faced with a couple of issues. The first was that we needed to make ByRef 'a a first-class type within the compiler so that we could unify it, and the second was that we needed to deal with the implicit coercion issues that this would entail. That is: conversion back and forth between ByRef 'a and 'a at copy boundaries. The coercion part wasn't so bad; ByRef is never inferred, and the type coercions associated with ByRef happen in exactly the same places that const/mutable coercions happen. We already had a cleanly isolated place in the type checker to deal with that.
But even if ByRef isn't inferred, it can propagate through the code by unification. And
that
causes safety violations! The fact that ByRef was syntactically restricted to appear only at parameters had the (intentional) consequence of ensuring that safety restrictions associated with the lifespan of references into the stack were honored - that was why I had originally imposed the restriction that ByRef could appear only at parameters. Once the ByRef type can unify, the syntactic restriction no longer guarantees the enforcement of the lifespan restriction. To see why, consider what happens in:
define byrefID(x:ByRef 'a) { return x; }
Something that is
supposed
to be a downward-only reference ends up getting returned up the stack. Swaroop's solution was clever, in part, because it silently prevented this propagation problem. In some sense, his implementation doesn't really treat ByRef as a type, so it can't propagate. But *because *he didn't treat it as a type, we also couldn't do the necessary matching check between instances and type classes.
It turns out that being able to do this is
useful
. The essential requirement of an abstract mutable "property" (in the C# sense) is that we have the ability within the language to construct a function that returns the
location
of the thing to be mutated. That location will often be on the stack, so returning the location is
exactly
like the example above. The "ByRef only at parameters" restriction is actually very conservative, and we knew that it was preventing certain kinds of things that we eventually wanted to do. We had a vague notion that we would come back and fix that at a later time by introducing region types.
As it turned out, "later" had to be "now", because region types are the right way to re-instate lifetime safety when ByRef types become first class. But
adding
region types presented two problems (which is why we had hoped to defer them):
Adding region types meant rewriting the type checker and re-verifying the soundness and completeness of the inference algorithm,
and
It wasn't just a re-write. Regions introduce subtyping. Subtyping and polymorphism don't get along, so we would need to go back and do a lot of study.
Region polymorphism with region subtyping had certainly been done before, but we were looking at subtyping in another case too (below). That was pushing us toward a kinding system and a different type system.
So to fix the ByRef problem, we very nearly needed to re-design both the type system and the compiler from scratch. Given the accumulation of cruft in the compiler, that might have been a good thing in any case, but Swaroop was now full-time at Microsoft, and I didn't have the time or the resources to tackle this by myself.
Conclusion Concerning the Type System
In retrospect, it's hard to imagine a strongly typed imperative language that doesn't type locations in a first-class way. If the language simultaneously supports explicit unboxing, it is effectively forced to deal with location lifespan and escape issues, which makes memory region typing of some form almost unavoidable.
For this reason alone, even if for no other, the type system of an imperative language with unboxing must incorporate some form of subtyping. To ensure termination, this places some constraints on the use of type inference. On the bright side, once you introduce subtyping you are able to do quite a number of useful things in the language that are hard to do without it.
Inheritance and Encapsulation
Our first run-in with inheritance actually showed up in the compiler itself. In spite of our best efforts, the C++ implementation of the BitC compiler had not entirely avoided inheritance, so it didn't have a direct translation into BitC. And even if we changed the code of the compiler, there are a large number of third-party libraries that we would like to be able to transcode. A good many of those rely on [single] inheritance. Without having at least some form of interface (type) inheritance, We can't really even do a good job interfacing to those libraries as foreign objects.
The compiler aside, we also needed a mechanism for encapsulation. I had been playing with "capsules", but it soon became clear that capsules were really a degenerate form of subclassing, and that trying to duck that issue wasn't going to get me anywhere.
I could nearly imagine getting what I needed by adding "ThisType" and inherited
interfaces
. But the combination of those two features introduces subtyping. In fact, the combination is equivalent (from a type system perspective) to single-inheritance subclassing.
And the more I stared at interfaces, the more I started to ask myself why an interface wasn't just a type class.
That
brought me up against the instance coherence problem from a new direction, which was already making my head hurt. It also brought me to the realization that Interfaces work, in part, because they are always parameterized over a single type (the ThisType) - once you know that one, the bindings for all of the others are determined by type constructors or by explicit specification.
And introducing SelfType was an even bigger issue than introducing subtypes. It means moving out of System F<: entirely, and into the object type system of Cardelli
et al
. That wasn't just a matter of re-implementing the type checker to support a variant of the type system we already had. It meant re-formalizing the type system entirely, and learning how to think in a different model.
Doable, but time not within the framework or the compiler that we had built. At this point, I decided that I needed to start over. We had learned a lot from the various parts of the BitC effort, but sometimes you have to take a step back before you can take more steps forward.
Instance Coherence and Operator Overloading
BitC largely borrows its type classes from Haskell. Type classes aren't just a basis for type qualifiers; they provide the mechanism for *ad hoc*polymorphism. A feature which, language purists notwithstanding, real languages actually do need.
The problem is that there can be multiple type class instances for a given type class at a given type. So it is possible to end up with a function like:
define f(x : 'x) {
  ...
  a:int32 + b  // typing fully resolved at static compile time
  return x + x  // typing not resolvable until instantiation
}
Problem: we don't know which instance of "+" to use when 'x instantiates to
int32
. In order for "+" to be meaningful in a+b, we need a static-compile-time resolution for +:(int32, int32)->int32. And we get that from Arith(int32). So far so good. But if 'x is instantiated to
int32
, we will get a type class instance supplied by the caller. The problem is that there is no way to guarantee that this is the
same
instance of Arith(int32) that we saw before.
The solution in Haskell is to impose the
ad hoc
rule that you can only instantiate a type class once for each unique type tuple in a given application. This is similar to what is done in C++: you can only have one overload of a given global operator at a particular type. If there is more than one overload at that type, you get a link-time failure. This restriction is tolerable in C++ largely because operator overloading is so limited:
The set of overloadable operators is small and non-extensible.
Most of them can be handled satisfactorily as methods, which makes their resolution unambiguous.
Most of the ones that
can't
be handled as methods are arithmetic operations, and there are practical limits to how much people want to extend those.
The remaining highly overloaded global operators are associated with I/O. These
could
be methods in a suitably polymorphic language.
In languages (like BitC) that enable richer use of operator overloading, it seems unlikely that these properties would suffice.
But in Haskell and BitC, overloading is extended to
type properties
as well. For example, there is a type class "Ord 'a", which states whether a type 'a admits an ordering. Problem: most types that admit ordering admit more than one! The fact that we know an ordering
exists
really isn't enough to tell us which ordering to
use
. And we can't introduce
two
orderings for 'a in Haskell or BitC without creating an instance coherence problem. And in the end, the instance coherence problem exists because the language design performs method resolution in what amounts to a non-scoped way.
But if nothing else, you can hopefully see that the heavier use of overloading in BitC and Haskell places much higher pressure on the "single instance" rule. Enough so, in my opinion, to make that rule untenable. And coming from the capability world, I have a strong allergy to things that smell like ambient authority.
Now we can get past this issue, up to a point, by imposing an arbitrary restriction on where (which compilation unit) an instance can legally be defined. But as with the "excessively abstract types" issue, we seemed to keep tripping on type class issues. There are other problems as well when multi-variable type classes get into the picture.
At the end of the day, type classes just don't seem to work out very well as a mechanism for overload resolution without some other form of support.
A second problem with type classes is that you can't resolve operators at static compile time. And if instances are explicitly named, references to instances have a way of turning into first-class values. At that point the operator reference can no longer be statically resolved at all, and we have effectively re-invented operator methods!
Conclusion about Type Classes and Overloading:
The type class notion (more precisely: qualified types) is seductive, but absent a reasonable approach for instance coherence and lexical resolution it provides an unsatisfactory basis for operator overloading. There is a disturbingly close relationship between type class instances and object instances that needs further exploration by the PL community. The important distinction may be pragmatic rather than conceptual: type class instances are compile-time constants while object instances are run-time values. This has no major consequences for typing, but it leads to significant differences w.r.t. naming, binding, and [human] conceptualization.
There are unresolved formal issues that remain with multi-parameter type classes. Many of these appear to have natural practical solutions in a polymorphic object type system, but concerns of implementation motivate kinding distinctions between boxed and unboxed types that are fairly unsatisfactory.
Wrapping Up
The current outcome is
extremely
frustrating. While the blind spots here were real, we were driven by the requirements of the academic research community to spend nearly three years finding a way to do complete inference over mutability. That was an enormous effort, and it delayed our recognition that we were sitting on the wrong kind of underlying type system entirely. While I continue to think that there is some value in mutability inference, I think it's a shame that a fairly insignificant wart in the original inference mechanism managed to prevent larger-scale success in the overall project for what amount to
political
reasons. If not for that distraction, I think we would probably have learned enough about the I/O and the instance coherency issues to have moved to a different type system while we still had a group to do it with, and we would have a working and useful language today.
The distractions of academia aside, it is fair to ask why we weren't building small "concept test" programs as a sanity check of our design. There are a number answers, none very satisfactory:
Research languages can adopt simplifications on primitive types (notably integers) that systems languages cannot. That's what pushed us into type classes in the first place, we new that polymorphism over unboxed types hadn't seen a lot of attention in the literature, and we knew that mutability inference had never been done. We had limited manpower, so we chose to focus on those issues first.
We knew that parametric polymorphism and subtyping didn't get along, so we wanted to avoid that combination. Unfortunately, we avoided subtypes too well for too long, and they turned out to be something unavoidable.
For the first several years, we were very concerned with software verification, which
also
drove us strongly away from object-based languages and subtyping. That blinded us.
Coming to language design as "systems" people, working in a department that lacked deep expertise and interest in type systems, there was an enormous amount of subject matter that we needed to learn. Some of the reasons for our failure are "obvious" to people in the PL community, but others are not. Our desire for a "systems" language drove us to explore the space in a different way and with different priorities than are common in the PL community.
I think we did make some interesting contributions. We now know how to do (that is: to implement) polymorphism over unboxed types with significant code sharing, and we understand how to deal with inferred mutability. Both of those are going to be very useful down the road. We have also learned a great deal about advanced type systems.
In any case, BitC in its current form clearly needs to be set aside and re-worked. I have a fairly clear notion about how I would approach
continuing
this work, but that's going to have to wait until someone is willing to pay for all this.
