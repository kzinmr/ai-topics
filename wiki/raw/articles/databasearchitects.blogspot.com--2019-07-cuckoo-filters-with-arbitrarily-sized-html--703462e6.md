---
title: "Cuckoo Filters with arbitrarily sized tables"
url: "https://databasearchitects.blogspot.com/2019/07/cuckoo-filters-with-arbitrarily-sized.html"
fetched_at: 2026-05-05T07:01:29.028940+00:00
source: "Database Architects"
tags: [blog, raw]
---

# Cuckoo Filters with arbitrarily sized tables

Source: https://databasearchitects.blogspot.com/2019/07/cuckoo-filters-with-arbitrarily-sized.html

Cuckoo Filters
are an interesting alternative to
Bloom filters
. Instead of maintaining a filter bitmap, they maintain a small (cuckoo-)hash table of key signatures, which has several good properties. For example is stores just the signature of a key instead of the key itself, but is nevertheless able to move an element to a different position in the case of conflicts.
This conflict resolution mechanism is quite interesting: Just like regular cuckoo hash tables each element has two potential positions where is be placed, a primary position i1 and a secondary position i2. These can be computed as follows:
i1 = hash(x)
i2 = i1 xor hash(signature(x))
Remember that the cuckoo filter stores only the (small) signature(x), not x itself. Thus, when we encounter a value, we cannot know if it is at its position i1 or position i2. However, we can nevertheless alternate between positions because the following holds
i1 = i2 xor hash(signature(x))
and we have the signature stored in the table. Thus, we can just use the self-inverse xor hash(signature(x)) to switch between i1 and i2, regardless of whether are currently at i1 or i2. Which is a neat little trick. This allows is to switch between positions, which is used in the cuckoo filter conflict resolution logic.
However all this hold only because the original cuckoo filters use power-of-two hash tables. If our hash table size is not a power of 2, the xor can place the alternative position beyond the size of the hash table, which breaks the filter. Thus cuckoo filter tables always had to be powers of two, even if that wasted a lot of memory.
In
more recent work
Lang et al. proposed using cuckoo filters with size C, where C did not have to be a power of two, offering much better space utilization. They achieved this by using a different self-inverse function:
i1 = hash(x) mod C
i2 = -(i1 + hash(signature(x)) mod C
Note that the modulo computation can be made reasonable efficient by using
magic numbers
, which can be precomputed when allocating the filter.
A slightly different way to formulate this is to introduce a switch function f, which switches between positions:
f(i,sig,C) = -(i + hash(sig)) mod C
i1 = hash(x) mod C
i2 = f(i1, signature(x), C)
i1 = f(i2, signature(x), C)
All this works because f is
self-inverse
, i.e.,
i = f(f(i, signature(x), C), signature(x), C)
for all C>0, i between 0 and C-1, and signature(x)>0.
The only problem is: Is this true? In a purely mathematical sense it is, as you can convince yourself by expanding the formula, but the cuckoo filters are not executed on abstract machines but on real CPUs. And there something unpleasant happens: We can get numerical overflows of our integer registers, which implicitly introduces a modulo 2^32 into our computation. Which breaks the self-inverseness of f in some cases, except when C is power of two itself.
Andreas Kipf
noticed this problem when using the cuckoo filters with real world data. Which teaches us not to trust in formulas without additional extensive empirical validation... Fortunately we can repair the function f by using proper modular arithmetic. In pseudo-code this looks like this
f(i,sig,C)
x=(C-1)-(hash(sig) mod C)
if (x>=i)
return (x-i);
// The natural formula would be C-(i-x), but we prefer this one...
return C+(x-i);
This computes the correct wrap-around module C, at the cost of one additional if. We can avoid the if by using predication, as shown below
f(i,sig,C)
x=(C-1)-(hash(sig) mod C)
m = (x<i)*(~0)
return (m&C)+(x-i);
which can be attractive for SSE implementations where the comparison produces a bit mask anyway.
We have validated that this new f function is now self-inverse for all possible values of i, sig, and C. And we did this by not just looking at the formula, but by trying out all values programmatically. Which is a good way to get confidence in your approach; there is only a finite number of combinations, and we can test them all.
With this small fix, we can now enjoy Cuckoo Filters with arbitrarily sized tables.
Edit:
The original post did not mirror the hash space correctly (using C-... instead of (C-1)-...), thanks to Andreas Kipf for pointing this out.
