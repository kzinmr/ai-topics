---
title: "Revisiting Knuth’s “Premature Optimization” Paper"
url: "https://probablydance.com/2025/06/19/revisiting-knuths-premature-optimization-paper/"
fetched_at: 2026-05-05T07:01:26.162650+00:00
source: "Malte Skarupke (Probably Dance)"
tags: [blog, raw]
---

# Revisiting Knuth’s “Premature Optimization” Paper

Source: https://probablydance.com/2025/06/19/revisiting-knuths-premature-optimization-paper/

The most famous quote from Knuth’s paper “Structured Programming with go to Statements” is this:
There is no doubt that the grail of efficiency leads to abuse. Programmers waste enormous amounts of time thinking about, or worrying about, the speed of noncritical parts of their programs, and these attempts at efficiency actually have a strong negative impact when debugging and maintenance are considered. We should forget about small efficiencies, say about 97% of the time: premature optimization is the root of all evil.
People always use this quote wrong, and to get a feeling for that we just have to look at the original paper, and the context in which it was written. The paper isn’t actually about optimization. It’s about when we have to use goto statements because structured programming couldn’t express certain things at the time. Or at least it couldn’t do so efficiently, requiring extra checks, and that’s why Knuth has to talk about performance: The topic he is addressing is “Can we get rid of goto statements without sacrificing performance?”
The famous quote occurs just after Knuth talks about the problem of writing what C++ oxymoronically calls a multiset. (he obviously doesn’t call it that, but that’s what it is called in C++) Imagine you want to store a set of items, and the items can occur multiple times. Instead of actually storing them multiple times, you might as well just keep a count for each item. In C++ you might write it like this:
template<typename T>
struct counting_multiset
{
    int insert(const T & x)
    {
        return ++counts[x];
    }

private:
    std::map<T, int> counts;
};
I’ll leave the other methods like ‘find’ and ‘erase’ as an exercise to the reader.
Knuth builds this set using two arrays: One for the elements, one for the counts. And, for the purposes of the paper, he always assumes that there is enough space in the array. So an insert might look like this, using goto:
template<typename T>
struct knuth_multiset
{
    int insert_1(const T & x)
    {
        size_t i = 0;
        for (; i < size; ++i)
        {
            if (elems[i] == x)
                goto found;
        }
        ++size;
        elems[i] = x;
        counts[i] = 0;
      found:
        return ++counts[i];
    }

private:
    std::unique_ptr<T[]> elems;
    std::unique_ptr<int[]> counts;
    size_t size = 0;
};
So just iterate through the array until we find the element. If we don’t find it, insert it at the end.
How does this compare in performance to the map-based approach? This is O(n), the map-based approach is O(log n), but arrays are fast. Arrays win until the set has more than ~300 elements in it:
The x-axis is the number of inserts, and for this benchmark I decided that 1/3 inserts would be a new element, and 2/3 just update existing elements, so the size of the container at 1024 (when map is faster) is actually 1024/3 = ~341.
Knuth doesn’t do this comparison, he just says that this is a common example to justify gotos. So why use a goto here? Because there are two different ways of exiting the loop, which share some code afterwards but not all code. Without a goto it would have to look like this:
int insert_1a(const T & x)
    {
        size_t i = 0;
        while (i < size && elems[i] != x)
            ++i;
        if (i == size)
        {
            ++size;
            elems[i] = x;
            counts[i] = 0;
        }
        return ++counts[i];
    }
We would need an extra check after the loop exits, to see whether the element is already in the set or not. That extra check isn’t much of a performance problem, the bigger problem is that
insert_1
is easier to read, and wasn’t code supposed to be easier to read if we get rid of goto?
Except then Knuth says that he actually thinks this is a bad example. He says this is a common argument in favor of goto, but
insert_1
is actually a bad way to search for the element. Instead what we should do is optimistically insert the item, so that we always know that it is present, so that we can save ourselves one condition in the loop:
int insert_2(const T & x)
    {
        elems[size] = x;
        size_t i = 0;
        while (elems[i] != x)
            ++i;
        if (i == size)
        {
            counts[size] = 1;
            ++size;
            return 1;
        }
        else
        {
            return ++counts[i];
        }
    }
See we never have to check whether we went past the end of the array because we always know that we’ll find the item. And next Knuth goes further and says we might as well unroll this loop once to make it faster:
int insert_2a(const T & x)
    {
        elems[size] = x;
        size_t i = 0;
        goto test;
      loop:
        i += 2;
      test:
        if (elems[i] == x)
            goto found;
        if (elems[i + 1] != x)
            goto loop;
        ++i;
      found:
        if (i == size)
        {
            ++size;
            counts[i] = 1;
            return 1;
        }
        else
        {
            return ++counts[i];
        }
    }
So this increments i by 2 per loop iteration. So instead of “add; compare; add; compare; add; compare…” we do “add; compare; compare; add; compare; compare”. (the “i+1” in the test section is free because there are instructions for “dereference pointer with fixed offset”) Knuth does some math and says that if you assume 20 elements in the set, insert_2a will be ~12% faster than insert_2, which is already 21% faster than insert_1. And in this context he talks about premature optimization:
The improvement in speed from Example 2 to Example 2a is only about 12%, and many people would pronounce that insignificant. The conventional wisdom shared by many of today’s software engineers calls for ignoring efficiency in the small; but I believe this is simply an overreaction to the abuses they see being practiced by penny-wise-and-pound-foolish programmers, who can’t debug or maintain their “optimized” programs. In established engineering disciplines a 12 % improvement, easily obtained, is never considered marginal; and I believe the same viewpoint should prevail in software engineering. Of course I wouldn’t bother making such optimizations on a one-shot job, but when it’s a question of preparing quality programs, I don’t want to restrict myself to tools that deny me such efficiencies.
There is no doubt that the grail of efficiency leads to abuse. Programmers waste enormous amounts of time thinking about, or worrying about, the speed of noncritical parts of their programs, and these attempts at efficiency actually have a strong negative impact when debugging and maintenance are considered. We should forget about small efficiencies, say about 97% of the time: premature optimization is the root of all evil.
Yet we should not pass up our opportunities in that critical 3 %. A good programmer will not be lulled into complacency by such reasoning, he will be wise to look carefully at the critical code; but only after that code has been identified. It is often a mistake to make a priori judgments about what parts of a program are really critical, since the universal experience of programmers who have been using measurement tools has been that their intuitive guesses fail. After working with such tools for seven years, I’ve become convinced that all compilers written from now on should be designed to provide all programmers with feedback indicating what parts of their programs are costing the most; indeed, this feedback should be supplied automatically unless it has been specifically turned off.
After a programmer knows which parts of his routines are really important, a transformation like doubling up of loops will be worthwhile.
I think this says the opposite of how the quote is usually used. Usually people say “premature optimization is the root of all evil” to say “small optimizations are not worth it” but just before that paragraph Knuth says that small optimizations, like unrolling this loop once, are worth it, and should not be considered premature optimizations.
Instead what matters is whether you benchmarked your code and whether you determined that this optimization actually makes a difference to the runtime of the program. Don’t do this in a piece of the code that doesn’t even make a difference. But if you know that something matters, or if it’s in a library function that will be used all over the place, then a 12% improvement is definitely worth it.
So if you would have used this quote to tell someone to not do this last optimization, you’re using it wrong.
Measuring the Improvements
OK but does this actually matter? Optimizing compilers have gotten a lot better. Can’t they do this by themselves? They might be able to do the loop unrolling, but in practice they usually won’t. They certainly won’t do the change to optimistically insert the element first before doing the search. Even on current compilers I can measure improvements for each of these:
The left side of the graph is too noisy, with all the lines being really close together. But as I increase the number of inserts, the difference becomes clearer. At the right-most measure, insert_2 is 13.5% faster than insert_1, and insert_2a is 7% faster again. Not quite Knuth’s numbers, but noticeable. But actually that right-hand side is not interesting because you wouldn’t use linear search for a container of that size. (I’ll get later to what you should use instead) So lets zoom in on the small numbers:
I added error bars to this, which are impossible to read here (sorry, LibreOffice isn’t good but it’s easy to plot data in there…), but at least they show that all of these overlap. Meaning there is no big difference between these. But I ran these very often and the median result of all my benchmark shows that insert_1 is faster than insert_2, which is faster than insert_2a. Meaning for small number of elements, its not worth the overhead of optimistically inserting the element.
Fastest of all is a new entry, insert_0. Knuth doesn’t show insert_0 in the paper, but mentions it in a throwaway comment:
if I hadn’t seen how to remove one of the operations from the loop in Example 1, by changing to Example 2. I would probably (at least) have made the for loop run from m to 1 instead of from 1 to m, since it’s usually easier to test for zero than to compare with m.
Sometimes comparing against 0 is faster because it lines up well with the available instructions, so might as well change the loop to count to zero. My implementation looks like this:
int insert_0(const T & x)
    {
        size_t i = size;
        while (i-- != 0)
        {
            if (elems[i] == x)
                return ++counts[i];
        }
        elems[size] = x;
        counts[size] = 1;
        ++size;
        return 1;
    }
In the loop in insert_1 there are five instructions per loop iteration:
Increment
Compare (with size)
Conditional jump (to end the loop)
Compare (with x)
Conditional jump (to label found)
With this version there are only four instructions:
Decrement
Conditional jump (to end the loop)
Compare (with x)
Conditional jump (out of the function)
We need one comparison less, because you there is a conditional jump instruction available that jumps if the decrement went negative.
Unfortunately both Clang and GCC mess this up. Clang removes the compare, then adds in one new instruction whose purpose I don’t understand, putting us back at five instruction. GCC doesn’t understand the optimization. So I actually had to write a custom assembly version of the loop (by taking the Clang assembly and removing the unnecessary instruction) to get proper measurements of the improvement that Knuth mentions.
So for small sets this version is actually fastest. (for large sets it’s the same speed as insert_1) But all of these have roughly the same speed, and you can only really see a difference once the set gets big enough where you would just use a hashtable anyways. Why is this? Why do they have the same speed until the set gets big?
My best guess is that none of these loops fully tax my CPU. If you’re not fully using instruction-level-parallelism, sometimes it’s free to just throw in one more instruction. Maybe when this paper was written, in 1974, you could still get a good estimate for performance by counting instructions. Today CPUs run multiple instructions per cycle, and if your loop has more instructions, all that happens is that it goes from running at 1.7 instructions per cycle to running at 1.9 instructions per cycle, but overall it takes the same amount of time. But once the sets get large, the branch prediction gets good, and the loop runs at 3.5 instructions per cycle because the CPU runs multiple iterations of the loop at once. At that point it matters how many instructions each iteration through the loop takes because you’re getting close to the hard limit of 4 instructions per cycle. (on my current CPU)
So What Should We Do?
Honestly I don’t think you should worry about most of this, and you should just use a good library. So in order of increasing sanity, lets try three things:
Use the STL
Use std::unordered_map
Use a fast hashtable
Starting with the first one, how does std::find do?
For small sizes it doesn’t do as well as insert_0, but it does pretty well and is faster than insert_2a.
(note: The timings above are different from the other graphs above. I wrote most if this blog post in 2023 but hadn’t created these last graphs yet. So now these were created on different hardware with different compilers. Sorry for that…)
For large sizes it doesn’t do as well as insert_2a, but it does pretty well and is faster than insert_0.
So on average this is just the best option. It is well-optimized: the inner loop is unrolled 4 times, because the authors of std::find did not think that loop unrolling is premature optimization. For linear search you should just use the STL.
But really using linear search is silly here, and using a std::map like I did at the beginning is silly, too. Clearly you want a hash table. Lets start with unordered_map:
It does OK. Slower for small sizes, but not terrible. So lets use a
fast flat hash map
instead:
This does really well already at 8 insertions. With 2/3 of these being updates of existing entries, the container only contains between 2 and 4 items at that size. A fast flat hash map makes linear search unnecessary even at those sizes.
Conclusion
So what did we learn?
A 10% improvement is not automatically a “premature optimization”. Instead what matters is whether you have benchmarked your program and determined that the optimization actually makes a difference to the program. And for library functions even smaller optimizations may be worth doing because they are used so often.
The corollary of that is that you should use library functions that have been written by people who understand that optimizing their functions is not premature optimization.
Compilers will not do these optimizations for you. Even 50 years after the paper was first written. In fact if a programmer does a straightforward optimizations like “iterate down to 0 instead of iterating up,” the compiler may mess that up and I ended up having to write a little bit of assembly by hand.
P.S.
My apologies to Casey Muratori who recently
announced
that he was going to cover the “premature optimization” paper in his (recommended)
Computer, Enhance!
video series. I’ve been having a hard time getting out blog posts in recent years, and when he announced that he was working on covering this paper, that reminded me that I had this mostly-finished blog post from 2023 lying around. All I had to do was insert a few more graphs at the end and write a conclusion, so I rushed to finish it before he got the video out because I was worried that my work would be redundant with his. My apologies Casey if I you were going to cover this from the same angle.
