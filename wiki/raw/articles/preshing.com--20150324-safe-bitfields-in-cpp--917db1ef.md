---
title: "Safe Bitfields in C++"
url: "https://preshing.com/20150324/safe-bitfields-in-cpp"
fetched_at: 2026-05-05T07:01:04.244279+00:00
source: "Preshing"
tags: [blog, raw]
---

# Safe Bitfields in C++

Source: https://preshing.com/20150324/safe-bitfields-in-cpp

In my
cpp11-on-multicore
project on GitHub, there’s
a class
that packs three 10-bit values into a 32-bit integer.
I could have implemented it using traditional bitfields…
struct
Status
{
    uint32_t readers :
10
;
    uint32_t waitToRead :
10
;
    uint32_t writers :
10
;
};
Or with some bit twiddling…
uint32_t status = readers | (waitToRead << 10) | (writers << 20);
Instead, I did what any overzealous C++ programmer does. I abused the preprocessor and templating system.
BEGIN_BITFIELD_TYPE(Status, uint32_t)           
    ADD_BITFIELD_MEMBER(readers,
0
,
10
)         
    ADD_BITFIELD_MEMBER(waitToRead,
10
,
10
)
    ADD_BITFIELD_MEMBER(writers,
20
,
10
)
END_BITFIELD_TYPE()
The above set of macros defines a new bitfield type
Status
with three members. The second argument to
BEGIN_BITFIELD_TYPE()
must be an unsigned integer type. The second argument to
ADD_BITFIELD_MEMBER()
specifies each member’s offset, while the third argument specifies the number of bits.
I call this a
safe bitfield
because it performs safety checks to ensure that every operation on the bitfield fits within the available number of bits. It also supports packed arrays. I thought the technique deserved a quick explanation here, since I’m going to refer back to it in future posts.
How to Manipulate a Safe Bitfield
Let’s take
Status
as an example. Simply create an object of type
Status
as you would any other object. By default, it’s initialized to zero, but you can initialize it from any integer of the same size. In the GitHub project, it’s often initialized from the result of a C++11 atomic operation.
Status status = m_status.load(std::memory_order_relaxed);
Setting the value of a bitfield member is easy. Just assign to the member the same way you would using a traditional bitfield. If asserts are enabled – such as in a debug build – and you try to assign a value that’s too large for the bitfield, an assert will occur at runtime. It’s meant to help catch programming errors during development.
status.writers =
1023
;     
status.writers =
1024
;
You can increment or decrement a bitfield member using the
++
and
--
operators. If the resulting value is too large, or if it underflows past zero, the operation will trigger an assert as well.
status.writers++;          
status.writers--;
It would be easy to implement a version of increment and decrement that silently wrap around, without corrupting any neighboring bitfield members, but I haven’t done so yet. I’ll add those functions as soon as I have a need for them.
You can pass the entire bitfield to any function that expects a
uint32_t
. In the GitHub project, they’re often passed to C++11 atomic operations. It even works by reference.
m_status.store(
status
, std::memory_order_relaxed);
m_status.compare_exchange_weak(
oldStatus
,
newStatus
,
                               std::memory_order_acquire, std::memory_order_relaxed));
For each bitfield member, there are helper functions that return the representation of
1
, as well as the maximum value the member can hold. These helper functions let you atomically increment a specific member using
std::atomic<>::fetch_add()
. You can invoke them on temporary objects, since they return the same value for any
Status
object.
Status oldStatus = m_status.fetch_add(
Status().writers.one()
, std::memory_order_acquire);
assert(oldStatus.writers +
1
<=
Status().writers.maximum()
);
How It’s Implemented
When expanded by the preprocessor, the macros shown near the top of this post generate a
union
that contains four member variables:
wrapper
,
readers
,
waitToRead
and
writers
:
union
Status
{
struct
Wrapper
    {
        uint32_t value;
    };
    Wrapper
wrapper
;

    Status(uint32_t v =
0
) { wrapper.value = v; }
    Status&
operator
=(uint32_t v) { wrapper.value = v;
return
*
this
; }
operator
uint32_t&() {
return
wrapper.value; }
operator
uint32_t()
const
{
return
wrapper.value; }
typedef
uint32_t StorageType;

    
    BitFieldMember<StorageType,
0
,
10
>
readers
;

    
    BitFieldMember<StorageType,
10
,
10
>
waitToRead
;

    
    BitFieldMember<StorageType,
20
,
10
>
writers
;


};
The cool thing about unions in C++ is that they share a lot of the same capabilities as C++ classes. As you can see, I’ve given this one a constructor and overloaded several operators, to support some of the functionality described earlier.
Each member of the union is exactly 32 bits wide.
readers
,
waitToRead
and
writers
are all instances of the
BitFieldMember
class template.
BitFieldMember<uint32_t, 20, 10>
, for example, represents a range of 10 bits starting at offset 20 within a
uint32_t
. (In the diagram below, the bits are ordered from most significant to least, so we count offsets starting from the right.)
Here’s a partial definition of the the
BitFieldMember
class template. You can view the full definition
on GitHub
:
template
<
typename
T,
int
Offset,
int
Bits>
struct
BitFieldMember
{
    T value;
static
const
T Maximum = (T(
1
) << Bits) -
1
;
static
const
T Mask = Maximum << Offset;
operator
T()
const
{
return
(value >> Offset) & Maximum;
    }

    BitFieldMember&
operator
=(T v)
    {
        assert(v <= Maximum);               
        value = (value & ~Mask) | (v << Offset);
return
*
this
;
    }

    ...
operator T()
is a user-defined conversion that lets us read the bitfield member as if it was a plain integer.
operator=(T v)
is, of course, a copy assignment operator that lets use write to the bitfield member. This is where all the necessary bit twiddling and safety checks take place.
No Undefined Behavior
Is this legal C++? We’ve been reading from various
Status
members after writing to others; something the C++ standard
generally forbids
. Luckily, in
§9.5.1
, it makes the following exception:
If a standard-layout union contains several standard-layout structs that share a common initial sequence … it is permitted to inspect the common initial sequence of any of standard-layout struct members.
In our case,
Status
fits the definition of a standard-layout union;
wrapper
,
readers
,
waitToRead
and
writers
are all standard-layout structs; and they share a common initial sequence:
uint32_t value
. Therefore, we have the standard’s endorsement, and there’s no
undefined behavior
. (Thanks to Michael Reilly and others for helping me sort that out.)
Bonus: Support for Packed Arrays
In
another class
, I needed a bitfield to hold a packed array of eight 4-bit values.
Packed array members are supported using the
ADD_BITFIELD_ARRAY
macro. It’s similar to the
ADD_BITFIELD_MEMBER
macro, but it takes an additional argument to specify the number of array elements.
BEGIN_BITFIELD_TYPE(AllStatus, uint32_t)
    ADD_BITFIELD_ARRAY(philos,
0
,
4
,
8
)     
END_BITFIELD_TYPE()
You can index a packed array member just like a regular array. An assert is triggered if the array index is out of range.
AllStatus status;
status.philos[
0
] =
5
;           
status.philos[
8
] =
0
;
Packed array items support all of the same operations as bitfield members. I won’t go into the details, but the trick is to overload
operator[]
in
philos
so that it returns a temporary object that has the same capabilities as a
BitFieldMember
instance.
status.philos[
1
]++;
status.philos[
2
]--;
std::cout << status.philos[
3
];
When optimizations are enabled, MSVC, GCC and Clang do a great job of inlining all the hidden function calls behind this technique. The generated machine code ends up as efficient as if you had explicitly performed all of the bit twiddling yourself.
I’m not the first person to implement custom bitfields on top of C++ unions and templates. The implementation here was inspired by
this blog post
by Evan Teran, with a few twists of my own. I don’t usually like to rely on clever language contortions, but this is one of those cases where the convenience gained feels worth the increase in obfuscation.
