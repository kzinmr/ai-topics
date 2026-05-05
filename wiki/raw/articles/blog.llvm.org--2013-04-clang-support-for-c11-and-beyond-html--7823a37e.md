---
title: "Clang support for C++11 and beyond"
url: "https://blog.llvm.org/2013/04/clang-support-for-c11-and-beyond.html"
fetched_at: 2026-05-05T07:01:43.248728+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# Clang support for C++11 and beyond

Source: https://blog.llvm.org/2013/04/clang-support-for-c11-and-beyond.html

Clang support for C++11 and beyond
As of
r179861
, Clang implements the
entirety
of the C++11 language standard. The following features have been implemented since the release of Clang 3.2, along with our plans for "C++1y".
Support for
[[attributes]]
C++11's
[[attribute]]
syntax is now fully supported, including support for the standard
[[noreturn]]
and
[[carries_dependency]]
attributes (although
[[carries_dependency]]
does not provide improved code generation). This allows non-returning functions to be written with a standard syntax:
[[noreturn]] void foo() {
while (true) do_something();
}
Just like
__attribute__((noreturn))
, Clang will warn you if you use this attribute on a function which can return, and will optimize callers on the assumption that the function does not return. Unlike
__attribute__((noreturn))
,
[[noreturn]]
is never part of a function's type.
As with g++'s implementation,
__attribute__((foo))
attributes which are supported by g++ can be written as
[[gnu::foo]]
. Clang-specific
__attribute__((...))
s are not available through this syntax (patches to add
[[clang::...]]
attribute names are welcome).
Clang also now provides complete support for C++11's almost-attribute
alignas(...)
.
Inheriting constructors
Clang now supports C++11's inheriting constructor syntax, which provides a simple mechanism to re-export all the constructors from a base class, other than default constructors, or constructors which would be copy or move constructors for either the base or derived class. Example:
struct Base {
Base(); // default constructor, not inherited
Base(int, char);
template<typename T> Base(T &x);
};
struct Derived : Base {
using Base::Base;
};
Derived f(1, 'x');
Derived d("foo"); // ok, calls inheriting constructor template
thread_local
variables
Clang now supports C++11's
thread_local
keyword, including dynamic initialization and destruction of thread-local objects. Dynamic destruction requires a C++ runtime library which provides
__cxa_thread_atexit
, which is currently only provided by the g++4.8 C++ runtime library.
C++1y
With C++11 out of the door, what's next? The C++ standardization committee voted yesterday to create the first Committee Draft for C++1y (which will very likely be C++14). Since this is only the first draft, there will probably be many minor changes before C++1y is done, but the rough feature set is unlikely to change much. This new language standard includes:
Generalized lambdas, allowing a templated call operator and arbitrary captures:
auto apply = [v(21)] (auto &&fn) { fn(v); };
apply([] (int &n) { n += 21; });
apply([] (int n) { std::cout << n; });
Return type deduction for (non-lambda) functions:
auto fn(int n) { return something(n); }
A more powerful
constexpr
feature, allowing variable mutation and loops:
constexpr auto len(const char *str) {
int k = 0;
while (*str++) ++k;
return k;
}
static_assert(len("foo") == 3, "hooray");
The improved
constexpr
feature comes with a backwards-compatibility cost, however. In order to support variable mutation for user-defined types, those types need to have
constexpr
member functions which are not
const
, so the C++11 rule which made
constexpr
member functions implicitly
const
has been removed. This means that you will need to make the
const
explicit if you were previously relying on this shorthand. Rewrite:
struct S {
int n;
constexpr int get() { return n; }
};
... as ...
struct S {
int n;
constexpr int get() const { return n; }
};
... and your code will work in both C++11 and C++14. Clang already has a warning for code which is relying on the implicit
const
rule, and will fix it for you if you run
clang -fixit
. Other compilers supporting C++11
constexpr
are expected to start providing similar warnings soon.
Several of the new features were prototyped in Clang prior to standardization, and we expect implementations of those to land in Clang SVN over the coming weeks. See the
Clang C++ status page
for the latest details on C++1y features and Clang's support for them. The implemented features can be enabled with the
-std=c++1y
command-line flag.
If you find bugs in the C++11 support, please report them on
our bug tracker
. If you want to get involved fixing bugs or working on C++1y support,
our website
has details of how you can help.
