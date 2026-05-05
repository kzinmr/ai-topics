---
title: "The Dreaded Two-Phase Name Lookup"
url: "https://blog.llvm.org/2009/12/dreaded-two-phase-name-lookup.html"
fetched_at: 2026-05-05T07:01:44.398645+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# The Dreaded Two-Phase Name Lookup

Source: https://blog.llvm.org/2009/12/dreaded-two-phase-name-lookup.html

Two-phase name lookup is not as complicated as its reputation implies. There are some non-obvious rules in the determination of what is a dependent vs. a non-dependent name, but otherwise the idea is simple. The problem with two-phase name lookup is that current compiler support for this feature is very poor. For example, GCC implements two-phase name lookup relatively well, but occasionally delays lookups that should have been done at template definition time (phase 1) until template instantiation time or performs lookups in both phases when it shouldn't. Visual C++, on the other hand, has a template parsing model that delays nearly every lookup to instantiation time (phase 2). By not implementing two-phase name lookup fully, both compilers tend to accept incorrect template code, and in some cases will end up compiling code differently from the mythical fully-conforming compiler. This is a portability issue, both between those two compilers (Visual C++ is more lenient) and to other, more pedantic compilers.
Like Clang. Clang was designed with complete support for two-phase name lookup, parsing template definitions (phase 1) as completely as possible and only performing name lookup at template instantiation time (phase 2) when required. Since we have chosen to make Clang C++ strict, we end up diagnosing template problems that other compilers miss. While that's generally good---correct code is more portable code---it also means that Clang needs to try extra-hard to produce decent diagnostics. Here's a recent problem Clang found within the LLVM code base (which compiled with GCC):
In file included from llvm/lib/Analysis/AliasAnalysisCounter.cpp:16:
In file included from llvm/include/llvm/Pass.h:369:
In file included from llvm/include/llvm/PassAnalysisSupport.h:24:
llvm/include/llvm/ADT/SmallVector.h:317:7:
error:
use of undeclared identifier 'setEnd'
setEnd(this->end()+1);
^
this->
In file included from llvm/lib/Analysis/AliasAnalysisCounter.cpp:16:
In file included from llvm/include/llvm/Pass.h:369:
llvm/include/llvm/PassAnalysisSupport.h:56:14: note:
in instantiation of member function 'llvm::SmallVectorImpl llvm::PassInfo const *>::push_back' requested here
Required.push_back(ID);
^
In file included from llvm/lib/Analysis/AliasAnalysisCounter.cpp:16:
In file included from llvm/include/llvm/Pass.h:369:
In file included from llvm/include/llvm/PassAnalysisSupport.h:24:
llvm/include/llvm/ADT/SmallVector.h:105:8: note:
must qualify identifier to find this declaration in dependent base class
void setEnd(T *P) { this->EndX = P; }
^
The problem itself is in SmallVectorImpl, in the call to setEnd(). The actual setEnd() function isn't in SmallVectorImpl, but in a base class, so we have a situation that looks like this:
template<typename T>
class SmallVectorTemplateCommon {
protected:
void setEnd(T *P);
};
template<typename T>
class SmallVectorImpl : public SmallVectorTemplateCommon<T> {
public:
void push_back(const T& value) {
// ...
setEnd(this->end() + 1);
}
};
If we weren't in a template, this code would be fine, because we would find setEnd in our base class. However, because we're in a template we're dealing with two-phase name lookup. While parsing push_back(), the compiler performs name lookup for the name "setEnd" at phase 1: however, it can't find anything because it isn't allowed to look into the dependent base class SmallVectorTemplateCommon<T>. However, this code is still valid: "setEnd" is taken as the name of a non-member function, which could be found at instantiation time via Argument Dependent Lookup. Unfortunately, when we do get around to instantiating push_back, Argument Dependent Lookup doesn't look into our base class, so Clang gives us a "use of undeclared identifier" error.
By itself, that error would leave the programmer scratching her head. GCC and Visual C++ accepted this code, and setEnd() is
obviously
in the base class, so what gives? To help out a bit, Clang gives more detail:
The note at the very end, which reads "must qualify identifier to find this declaration in dependent base class," tells the programmer what declaration Clang could find... if only she were to qualify the name somehow so that Clang were allowed to look there.
The original error had a little hint below the caret diagnostic, in green, providing advice on how to fix this particular issue. By adding "this->", we tell the compiler that "setEnd" is in the current class or one of its (possibly dependent) base classes, to be found at template instantiation time.
Clang C++ is designed to be a strict but helpful compiler, following the letter of the C++ standard to help programmers make sure that their code is portable. We also hope to make Clang a friendly compiler, that can use its knowledge of the program and the C++ language to help programmers get past portability problems like this one. And maybe, just maybe, Clang can shine a little light into the dark, scary corners of C++.
