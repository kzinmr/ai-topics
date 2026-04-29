---
title: "Looking at consequences of passing too few register parameters to a C function on various architectures"
url: "https://devblogs.microsoft.com/oldnewthing/20260427-00/?p=112271"
fetched_at: 2026-04-29T07:00:53.232072+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# Looking at consequences of passing too few register parameters to a C function on various architectures

Source: https://devblogs.microsoft.com/oldnewthing/20260427-00/?p=112271

In our exploration of calling conventions for various processors on Windows, we learned that in many cases, some of the parameters are passed in registers.
Suppose that there is a function that takes two parameters, but you know that the function ignores the second parameter if the first parameter is positive. What happens if you call the function with just one parameter (say, passing zero). The function should ignore the second parameter, so why does it matter that you didn’t pass one?
Even though the function doesn’t use the parameter, it still may decide to use the storage for that parameter as a conveniently provided scratch space. For example:
int blah(int a, int b)
{
    if (a <= 0) {
        int c = f1();
        f2(a);
        return c;
    } else {
        return f3(a, b);
}
Is it okay to call
blah
with zero as its only parameter? You aren’t passing
b
, but the function doesn’t use
b
, so why does it matter?
Formally, the C and C++ languages say that if you call a function with the wrong number of parameters, the behavior is undefined, so officially, you’ve broken the rules and anything can happen.
But let’s look at what types of things could go wrong.
If you pass too few parameters on the stack, and it is a callee-clean calling convention, then the callee will clean too many bytes off the stack,
resulting in stack imbalance
and likely memory corruption.
Even if it’s not a callee-clean calling convention, the called function will think that the memory for the parameter is present, and it may use it as scratch space, resulting in memory corruption in the stack frame of the calling function.
In our example above, the compiler might realize, “Hey, I don’t need to allocate new memory for the variable
c
. I can just reuse the memory that holds the now-dead variable
b
.” In other words, it rewrites the function as
int blah(int a, int b)
{
    if (a <= 0) {
b
= f1();
        f2(a);
        return c;
    } else {
        return f3(a, b);
}
Even if you don’t reserve memory for the variable
b
, the compiler will assume that you did and overwrite whatever is at the location the reserved memory should have been.
But what if the parameters are passed in registers, and you didn’t pass enough of them?
On most processors, what happens is that the called function will try to use that register and read whatever uninitialized value happens to be lying in that register.
Except on Itanium.
One special Itanium quirk is the presence of
the “Not a Thing” (NaT) bit
, which is a bit attached to each general purpose register that indicates whether the register holds a valid value. The most common ways for a register to enter the NaT state are if it was
the result of a failed speculative load
, or if it was the result of a mathematical calculation where at least one of the inputs was itself NaT. Therefore, if your uninitialized output register happens to be a NaT left over from an earlier failed speculation, the called function might decide to spill the value onto the stack for safekeeping before using that register for something else.
extern bool is_valid(int);

int blah2(int a, int b)
{
    if (is_valid(a)) {
        return f3(a, &b);
    } else {
        return 0;
    }
}
The compiler realizes that it needs to take the address of
b
if
a
is not valid, so it has to spill the value to memory (so that it can have an address). But
writing a NaT to memory raises a “NaT consumption” exception
, so this function crashes even in the case where it never actually uses the
b
variable.
But wait, there’s more.
On Itanium, the function call mechanism is architectural rather than merely conventional. The calling function declares the number of output registers (registers that will be passed to the called function), and those registers are renumbered on entry to the called function so that they are visible starting at register
r32
. If a calling function says “I am passing 2 registers,” then the called function sees them as registers
r32
and
r33
. I covered the details
some time ago
, but
leaf functions are particularly interesting
.
Leaf functions are functions that do not create a custom stack frame and simply make do with the architectural stack frame that the processor creates for them by default. And that default stack frame consists only of the inbound parameter registers. In the case of passing too few parameters to a function, that means that the default stack frame contains fewer registers than the function expects.
Architecturally, the rule is that if you read from a stacked register that lies outside the current frame, the results are “undefined”. I couldn’t find a formal definition of “undefined” in the Itanium documentation (though it’s eminently likely that I simply missed it), but I assume it means “can produce any result, including an exception, that is not dependent upon information outside the current processor execution mode.”¹ In particular, it can raise a processor exception, say, because the value of that stacked register happens to contain a leftover NaT.
The Itanium architecture takes an even stronger stance against writing a stack register that lies outside the current frame: It is required to raise an Illegal Operation fault.
I can imagine it being weird seeing an exception come out of a register-to-register move instruction.
So there you go, another case where the Itanium architecture more strictly enforces a programming rule, in this case, making sure that you pass the correct number of parameters to a function.
¹ This means that, for example, an “undefined” result in user-mode code cannot be dependent upon information available only to kernel mode.
