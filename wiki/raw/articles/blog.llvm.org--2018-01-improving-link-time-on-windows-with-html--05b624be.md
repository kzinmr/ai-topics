---
title: "Improving Link Time on Windows with clang-cl and lld"
url: "https://blog.llvm.org/2018/01/improving-link-time-on-windows-with.html"
fetched_at: 2026-05-05T07:01:38.259575+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# Improving Link Time on Windows with clang-cl and lld

Source: https://blog.llvm.org/2018/01/improving-link-time-on-windows-with.html

Clang's Solution - The COFF
.debug$H
section
This new approach tries to combine the ideas behind type servers and fastlink PDBs.  Like type servers, it attempts to offload the work of de-duplication to the compilation phase so that it can be done in parallel.  However, it does so using an algorithm with the property that the resulting hash can be used to identify a type record even across type streams.  Specifically,
if two records have the same hash, they are the same record even if they are from different object files.
If you can take it on faith that such an algorithm exists (which will be henceforth referred to as a
global hash
), then the amount of work that the linker needs to perform is greatly reduced.  And the work that it does still have to do can be done much quicker.  Perhaps most importantly,
it produces a byte-for-byte identical PDB to when the option is not used
, meaning all of the issues surrounding Fastlink PDBs and compatibility are gone.
Previously, the linker would do something that looks roughly like this:
HashTable<Type> HashedTypes;
vector<Type> MergedTypes;
for (ObjectFile &Obj : Objects) {
for (Type &T : Obj.types()) {
remapAllTypeIndices(MergedTypes, T);
if (!HashedTypes.try_insert(T))
continue;
MergedTypes.push_back(T);
}
}
The important observations here are:
remapAllTypeIndices
is called unconditionally for every type in every object file.
A hash of the type is computed unconditionally for every type
At least one
full record comparison is done for every type.  In practice it turns out to be much more, because hash buckets are computed modulo table size, so there will actually be 1 full record comparison for every probe.
Given a global hash function as described above, the algorithm can be re-written like this:
HashMap<SHA1, int> HashToIndex;
vector<Type> OrderedTypes;
for (ObjectFile &Obj : Objects) {
auto Hashes = Obj.DebugHSectionHashes;
for (int I=0; I < Obj.NumTypes; ++I) {
int NextIndex = OrderedTypes.size();
if (!HashToIndex.try_emplace(Hashes[I], NextIndex))
continue;
remapAllTypeIndices(T);
OrderedTypes.push_back(T);
}
}
While this appears very similar, its performance characteristics are quite different.
remapAllTypeIndices
is only called when the record is actually new.  Which, as we discussed earlier, is a small fraction of the time over many linker inputs.
A hash of the type is
never
computed by the linker.
It is simply there in the object file (the exception to this is mixed linker inputs, discussed earlier, but those are a small fraction of input files).
Full record comparisons
never
happen
.
Since we are using a strong hash function with negligible chance of false collisions, and since the hash of a record provides equality semantics across streams, the hash is as good as the record itself.
Combining all of these points, we get an algorithm that is extremely cache friendly.  Amortized over all input files, most records during type merging are cache hits (i.e. duplicate records).  With this algorithm when we get a cache hit, the only two data structures that are accessed are:
An array of contiguous hash values.
An array of contiguous hash buckets.
Since we never do full equality comparison (which would blow out the L1 and sometimes even L2 cache due to the average size of a type record being larger than a cache line) the algorithm here is very fast.
We’ve deferred discussion of how to create such a hash up until now, but it is actually fairly straightforward.  We use what is known as a “tree hash” or “Merkle tree”.  The idea is to pass bytes from a type record directly to the hash function up until the point we get to a type index.  Then, instead of passing the numeric value of the type index to the hash function, we pass the previously computed hash of the record that is being referenced.
Such a hash is very fast to compute in the compiler because
the compiler must already hash types anyway
, so the incremental cost to emit this to the .debug$H section is negligible.  For example, when a type is encountered in a translation unit, before you can add that type to the object file’s
.debug$T
section, it must first be verified that the type has not already been added.  And since this is happening naturally in the order in which types are encountered, all that has to be done is to save these hash values in an array indexed by type index, and subsequent hash operations will have O(1) access to all of the information needed to compute this merkle hash.
Mixed Input Files and Compiler/Linker Compatibility
A linker must be prepared to deal with a mixed set of input files.  For example, while a particular compiler may choose to always emit
.debug$H
sections, a linker must be prepared to link objects that for whatever reason do not have this section.  To handle this, the linker can examine all inputs up front and manually compute hashes for inputs with missing
.debug$H
sections.  In practice this proves to be a small fraction and the penalty for doing this serially is negligible, although it should be noted that in theory this can also be done as a parallel pre-processing step if some use cases show that this has non-negligible cost.
Similarly, the emission of this section in an object file has no impact on linkers which have not been taught to use it.  Since it is a purely additive (and optional) inclusion into the object file, any linker which does not understand it will continue to work exactly as it does today.
The On-Disk Format
Clang uses the following on-disk format for the
.debug$H
section.
0x0     : <Section Magic>  (4 bytes)
0x4     : <Version>        (2 bytes)
0x6     : <Hash Algorithm> (2 bytes)
0x8     : <Hash Value>     (N bytes)
0x8 + N : <Hash Value>     (N bytes)
…
Here, “Section Magic” is an arbitrarily chosen 4-byte number whose purpose is to provide some level of certainty that what we’re seeing is a real
.debug$H
section, and not some section that someone created that accidentally happened
to be called that.   Our current implementation uses the value 0x133C9C5, which represents the date of the initial prototype implementation.  But this can be any reasonable value here, as long as it never changes.
“Version” is reserved for future use, so that the format of the section can theoretically change.
“Hash Algorithm” is a value that indicates what algorithm was used to generate the hashes that follow.  As such, the value of N above is also a function of what hash algorithm is used.  Currently, the only proposed value for Hash Algorithm is SHA1 = 0, which would imply N = 20 when Hash Algorithm = 0.  Should it prove useful to have truncated 8-byte SHA1 hashes, we could define SHA1_8 = 1, for example.
Limitations and Pitfalls
The biggest limitation of this format is that it increases object file size.  Experiments locally on fairly large projects show an average aggregate object file size increase of ~15% compared to /DEBUG:FULL (which, for clang-cl, actually makes .debug$H object files
smaller
than those needed to support /DEBUG:FASTLINK).
There is another, less obvious potential pitfall as well.  The worst case scenario is when no input files have a
.debug$H
section present, but this limitation is the same in principle even if only a subset of files have a
.debug$H
section.  Since the linker must agree on a single hash function for all object files, there is the question of what to do when not all object files agree on hash function, or when not all object files contain a
.debug$H
section.  If the code is not written carefully, you could get into a situation where, for example, no input files contain a
.debug$H
section so the linker decides to synthesize one on the fly for every input file.  Since SHA1 (for example) is quite slow, this could cause a huge performance penalty.
This limitation can be coded around with some care, however.  For example, tree hashes can be computed up-front in parallel as a pre-processing step.  Alternatively, a hash function could be chosen based on some heuristic estimate of what would likely lead to the fastest link (based on the percentage of inputs that had a
.debug$H
section, for example).  There are other possibilities as well.  The important thing is to just be aware of this potential pitfall, and if your links become very slow, you'll know that the first thing you should check is "do all my object files have .debug$H sections?"
Finally, since a hash is considered to be identical to the original record, we must consider the possibility of collisions.  That said, this does not appear to be a serious concern in practice.  A single PDB can have a theoretical maximum of 2
32
type records anyway (due to a type index being 4 bytes).  The following table shows the expected number of type records needed for a collision to exist as a function of hash size.
Hash Size (Bytes)
Average # of records needed for a collision
4
82,137
6
21,027,121
8
5,382,943,231
12
3.53 x 10
14
16
2.31 x 10
19
20
1.52 x 10
24
