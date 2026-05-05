---
title: "Why is std::pair broken?"
url: "https://danlark.org/2020/04/13/why-is-stdpair-broken/"
fetched_at: 2026-05-05T07:01:56.423730+00:00
source: "Daniel Kutenin (danlark)"
tags: [blog, raw]
---

# Why is std::pair broken?

Source: https://danlark.org/2020/04/13/why-is-stdpair-broken/

Today we are going to talk about C++ basic
std::pair
class in a way how and why it is broken.
Story
std::pair
first appeared in C++98 as a pretty basic class with a very simple semantics — you have two types
T1
and
T2
, you can write
std::pair<T1, T2>
and access
.first
and
.second
members with all intuitive copy, assignment, comparison operators, etc. This is used in all map containers as value type to store and can be expanded into
structured bindings
, for example, with the following code:
std::unordered_map<std::string, int> m;
// …
for (const auto& [key, value] : m) {
// …
}
Pretty convenient, almost all C++ programmers know about this class and use it appropriately but several style guides including Google Style Guide
suggest
using user defined structs where appropriate. It has several reasons but the first one is readability — I personally want to kill people who write more than one level of
std::pair
, for example,
std::pair<int, std::pair<int, std::pair<int, int>>>
and then access it with
el.second.second.second
. And as the structure of the objects in a maintainable code tends to grow, it is better to use structs rather than pairs and tuples. Other reasons are more interesting.
Performance
Default construction
This is a minor and debatable thing but
std::pair
with trivial and non default zero initialized scalars is zero initialized:
constexpr std::pair<int, int> t;
static_assert(t.first == 0 && t.second == 0);
std::array<int, 5> arr;
// assert(arr[0] == 0); // Undefined behavior
In contrast,
std::array
does not initialize their elements with the default construction (if the underlying type is trivial) and leaves this for the user. It is debatable because some people don’t like the uninitialized memory but in the end this is an inconsistency between the containers and is a different behavior from default struct what people tend to think about
std::pair
(yet, I still think this should look like this):
template <typename T, typename U>
struct pair {
T first;
U second;
constexpr std::strong_ordering operator<=>(const pair& other) const {
if (auto first_comp = first <=> other.first; first_comp != 0) {
return first_comp;
} else {
return second <=> other.second;
}
}
};
Copying
I found this issue when I wanted to serialize and deserialize
std::pair
. One of the default implementations in struct/type serialization and deserialization is the following:
template <class T>
T Deserialize(const void* memory) {
T t;
memcpy(&t, memory, sizeof(T));
return t;
}
template <class T>
void Serialize(const T& t, void* memory) {
memcpy(memory, &t, sizeof(T));
}
If we go to
memcpy
documentation and see the following:
If the objects are potentially-overlapping or not
TriviallyCopyable
, the behavior of memcpy is not specified and may be undefined.
https://en.cppreference.com/w/cpp/string/byte/memcpy
TriviallyCopyable are objects that satisfy the following conditions:
Every copy constructor is trivial or deleted.
pair(const pair&)
. So, it should be either
= default
, either
= delete
, either omitted/created by the
rule of X
and all underlying objects are trivially copyable.
Every move constructor is trivial or deleted. Same with
pair(pair&&).
Every copy assignment operator is trivial or deleted. Same with
pair& operator=(const pair&)
.
Every move assignment operator is trivial or deleted. Same with
pair& operator=(pair&&)
.
At least one copy constructor, move constructor, copy assignment operator, or move assignment operator is non-deleted.
Trivial non-deleted destructor. This means that virtual classes cannot be trivially copyable because we need to copy the implementation
vptr
.
If we write our pair above and check if it is trivially copyable (with some trivial underlying types), it definitely is because we use the rule of zero and thus everything is generated automatically. Also, a small note — in the examples above you need to make sure that the types are trivially copyable, a perfect variant looks like (this is also
heavily used
by the compilers to generate the unaligned loads and work with unaligned memory):
template <class T>
T Deserialize(const void* memory) noexcept {
static_assert(std::is_trivially_copyable_v<T>);
T t;
memcpy(std::addressof(t), memory, sizeof(T));
return t;
}
// std::remove_reference_t for non-deduced context to prevent such code to blow below:
// char first = f(); char second = g();
// Serialize(first – second, to) (int will be deduced)
template <class T>
void Serialize(const std::remove_reference_t<T>& t, void* memory) noexcept {
static_assert(std::is_trivially_copyable_v<T>);
memcpy(to, std::addressof(t), sizeof(T));
}
Let’s see what
std::pair
guarantees. Good news is standard guarantees the copy and move constructors to be
defaulted
(see 7 and 8).
Also, from C++17 we have the requirement that if the types of the pair are trivially destructible, pair is also trivially destructible. This allows having many optimizations including putting the type onto registers. For example,
std::variant
and
std::optional
had
a different proposal to make this possible.
With everything else, it is more complicated. Let’s see what is going on with the copy assignment, in libc++ it is implemented like this:
struct __nat {};
pair& operator=(typename conditional<
is_copy_assignable<first_type>::value &&
is_copy_assignable<second_type>::value,
pair, __nat>::type const& __p)
noexcept(is_nothrow_copy_assignable<first_type>::value &&
s_nothrow_copy_assignable<second_type>::value)
{
first = __p.first;
second = __p.second;
return *this;
}
__nat
is used for disabling the instantiation of the copy assignment operator if it is invoked — a cool C++98 hack to delete the operator.
This helps the compiler to use
std::pair
with the references. By default, references cannot be implicitly copied or, if said in a more clever way, if you have them in the class, the copy assignment operator is implicitly deleted unless user defined. For example:
template <typename T, typename U>
struct pair {
T first;
U second;
};
int main() {
int x = 10;
int y = 20;
pair<int&, int> p{x, x};
pair<int&, int> p1{y, y};
p1 = p; // ill-formed, with std::pair, well-formed
}
In C++ copying the reference changes the underlying object and thus the referenced is binded to the class.
Here
is a good explanation why it was designed this way. So, the assignment operator is deleted because copying reference has slightly different semantics but in C++98 people (maybe) thought it was convenient. So, we cannot easily write
= default
to provide a default assignment operator (despite the fact this is an ABI (application binary interface) break).
All these facts lead to suboptimal performance, for example, in copying the vector of pairs. With the standard pair we have a simple loop, with trivially copyable type, we have fast
memmove
, the difference might be up to the register size,
memmove
is highly optimized.
https://gcc.godbolt.org/z/wtLLBU
Some attempts to fix this
First of all, all fixes will require an ABI break but as C++ standard will be (I hope) more or less ok with ABI breaks (or
not
:smile:), this can be done in a way.
Conceptually, we need to make a conditional default copy assignment operator with some restrictions:
We cannot write
= default
in the main class because it disallows the assignment of the references.
We cannot add the (possibly defaulted) template arguments to the pair because it will break the forward declarations.
We cannot use SFINAE on the return types of the defaulted copy assignment operators.
std::enable_if_t<std::is_reference<T1>::value || std::is_reference<T2>::value> operator=(const pair&) = default;
is disallowed by the standard.
We can move the
.first
and
.second
fields to the base classes and have partial specialisations like:
template <class T1, class T2, bool is_reference>
struct MyPairBase;
// Dispatch the reference specialisation and use it as a storage.
template <class T1, class T2>
struct MyPairBase<T1, T2, false> {
T1 a;
T2 b;
MyPairBase& operator=(const MyPairBase& other) = default;
};
template <class T1, class T2>
struct MyPairBase<T1, T2, true> {
T1 a;
T2 b;
MyPairBase& operator=(const MyPairBase& other) {
a = other.a;
b = other.b;
return *this;
}
// Possibly we will need to copy many things there.
};
template <class T1, class T2>
struct MyPair : public MyPairBase<T1, T2, std::is_reference<T1>::value ||
std::is_reference<T2>::value> {
using Base = MyPairBase<T1, T2, std::is_reference<T1>::value ||
std::is_reference<T2>::value>;
// … all the implementation
};
For example,
std::optional
does it
this way. The downside that we need to copy lots of code and such a simple class like optional turned out to be
1300+ lines of code
. Too much for
std::pair
, isn’t it?
Good solution I found is using C++20 concepts. They allow (at least they don’t disallow) the usage of the conditional default assignment operators.
#include <type_traits>
template<class T1, class T2>
struct MyPair {
T1 first;
T2 second;
static constexpr bool has_references = std::is_reference_v<T1> ||
std::is_reference_v<T2>;
MyPair(const T1& x, const T2& y) : first(x), second(y) {}
MyPair& operator=(const MyPair&) requires(!has_references) = default;
MyPair& operator=(const MyPair& other) requires(has_references) {
first = other.first;
second = other.second;
return *this;
}
};
int main() {
int x = 10;
MyPair<int&, int> a(x, 5);
MyPair<int&, int> b(x, 10);
b = a;
}
https://gcc.godbolt.org/z/XuvrC9
This fixes the problem, does not blow up the code size and at least is very intuitive to read. In the end I found several proposals trying to suggest it in a more generic way. See
one
,
two
and see the
blog
where they use the feature and reduce the number of lines from 1200 to 400 for
std::optional
. Yet, I haven’t found that this was accepted but this is a very good idea of improving and simplifying things in C++.
The funny
I knew it already but cannot be silent about it. LLVM and GCC optimizers optimize
std::pair<int, int>
to use one 64 bit register. It does not do it with
std::tuple<int, int>
. So, if you have the choice between pair and tuple, always use pair or even user defined structs.
https://gcc.godbolt.org/z/TCp9my
Conclusion
All that was written there also applies to
std::tuple
, they have the identical behavior in many places. Yet, this is one more argument why C++ old containers and even basic things are broken and ABI stability is doing more harm than good. I will finish it with a tweet that reminds me of a
CAP theorem
:
I really think that if at some point strong but breaking change does not happen, we will have a C++ fork that will do it.
