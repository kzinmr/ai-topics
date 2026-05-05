---
title: "How Binary JSON Works in YDB"
url: "https://laplab.me/posts/how-binary-json-works-in-ydb/"
fetched_at: 2026-05-05T07:01:24.631983+00:00
source: "Nikita Lapkov (laplab)"
tags: [blog, raw]
---

# How Binary JSON Works in YDB

Source: https://laplab.me/posts/how-binary-json-works-in-ydb/

Feel free to join the
discussion on HackerNews
.
In the early 2020 I was working in the Distributed Queries team of YDB.
YDB
is a Distributed SQL Database that combines high availability and scalability with strong consistency and ACID transactions. One of my key tasks there was to develop new storage format for JSON data. YDB recently became open source, so I can now share some interesting technical details behind this journey.
Problem
When I joined YDB, there was already a data type for storing JSON data called
Json
. Internally, it was just a JSON object serialized into the string representation. The only real difference from the
String
type was the fact that you cannot create a
Json
value holding invalid JSON string, such as
{"a": 1
.
The main issue with such representation is that the whole JSON object needs to be parsed for any query to be executed on it. Imagine a situation where customer stores the following JSON object in the table column:
{
"type":
"sensor-north"
,
"measurements":
<
5
MB
array
of
doubles>
,
"error_corrections":
<
5
MB
array
of
doubles>
}
Even if the query only accesses field
type
, we still need to parse the rest of 10MB before extracting it. Overhead like this grows linearly with the number of rows scanned by the query.
Since we have effectively reached the ceiling in optimizing the JSON parsing, the need for an alternative storage format formed. Such format must:
Be traversable without full document parsing. We need a way to navigate through the document, skipping over the data we are not interested in
Not take significantly more space than the JSON string. It is okay for the encoded document to be slightly larger than the JSON string, but 2x size increase is not acceptable
Existing solutions
There are at least 2 widely used open source databases which already have custom binary JSON format: PostgreSQL and MongoDB.
BSON
MongoDB’s format is called
BSON
. BSON is used everywhere in MongoDB: from receiving user commands to storing the data. While it is a good format for MongoDB’s use cases, we did not find it suitable for usage in YDB. There are two main reasons for that:
Values are interleaved with the information about the document’s structure. For example, an object is encoded in BSON as a series of
(<fieldname>, <fieldvalue>)
pairs. This forces the reader of a BSON file to perform a linear search when looking for a field value, since there is no additional information to navigate through the fields quicker.
Legacy. BSON has certain quirks which YDB would not benefit from. There are quite a lot of datatypes (some of them deprecated), which YDB would never need and certain data redundancy (such as recording array indexes together with array elements), which YDB does not require.
JSONB
We really have to start naming things better.
JSONB is a format used by PostgreSQL. There is no offical specification, but relevant source files in the PostgreSQL repo are
well documented
. JSONB was much closer to what we wanted from our format, but it still interleaves the values and the structure. A much bigger problem though is the fact that JSONB is deeply integrated into the PostgreSQL codebase. It would be quite difficult to extract it as a separate library and to backport future changes from PostgreSQL repo into this library.
YDB’s approach
Since none of the existing formats suited YDB’s needs, we decided to come up with our own format called BinaryJson. It has the following properties:
Versioned.
It is very likely we might want to improve our format in the future, so it is important to have a way to distinguish between versions
Traversable without linear search.
Reader can traverse the document without full deserialization. Looking up a field in the object takes
O(logN)
time, looking up element by index in the array takes
O(1)
time
Minimal effort deserialization.
In most cases, reader just needs to copy some bytes to extract a value from a location in BinaryJson
The core idea behind the format is to store JSON values and document structure separately. Document structure is represented by a small array of 32-bit integers. Each element in this array corresponds to a node in the JSON document tree. Trivial JSON values (such as booleans and nulls) are stored directly in the nodes. Big values (such as 64-bit doubles and strings) are stored in a separate buffer and tree nodes simply reference them.
Let us take a closer look.
BinaryJson structure
A document encoded in the BinaryJson format is a sequence of bytes, which can be logically divided into 4 parts:
Header.
Metadata about this BinaryJson
Tree.
Structure of the stored JSON document
String index.
Place to store strings
Number index.
Place to store 64-bit doubles
We will start with the simplest parts of BinaryJson - Header and Number index. After that, we will take a look at the String index. In the end, we will study the Tree section, which ties everything together.
Header and Number index
Header of BinaryJson is simply a 32-bit integer. First 5 bits of this integer contain a version number (which at the moment of writing always equals to 1). These 5 bits is something that all future versions of BinaryJson will need to provide in order for parsers to understand what kind of structure to expect.
The rest 27 bits represent an offset from the start of BinaryJson buffer. This offset points to the first byte of the String index. This is an optimization to avoid parsing the whole Tree section just to understand where String index begins. But this also imposes first limitation of the format - Tree section cannot be longer than
2^27 - 1 = 134217727
bytes, because otherwise the offset will be too large to represent in 27 bits. We were willing to accept such tradeoff.
Number index is a place where all 64-bit doubles are stored. There is no special encoding, doubles are just stored continuously in the buffer. Since all doubles have the same size, we can compute the exact location of specific number using only the index:
LocationOfDouble(i) = StartOfNumberIndex + i * sizeof(double)
We will use this property later in the Tree section.
String index
String index is a place where all strings are stored. This includes both string values and keys in the JSON objects. The structure is a little bit more complicated than one of the Number index because we need to store data pieces of different sizes.
String index starts with a 32-bit number
N
representing how many strings are stored in the index. It is then followed by
N
32-bit numbers called
SEntry
.
SEntry #i
is an offset, pointing to the first byte right after the corresponding
SData #i
. This array is followed by an array of
N
elements of
SData
. Each
SData
is simply a null-terminated string. Format does not require the strings to be null-terminated, but we did this for convenience.
So,
SEntry 1
points to the first byte after the first string stored in the index.
SEntry N
points to the end of the whole BinaryJson.
Using this encoding, we can reference strings by integer indexes. To extract a string from the index, we need to know where it starts and where it ends. Each
SEntry
already points to the end of the corresponding string, so the only missing piece of information is the string start. We can use
SEntry
of the previous string for that, since ending of one string is the beginning of another.
The following formulas can be used:
Offset(i) = StringIndexStart   // We have this information from parsing the Header.
            + sizeof(uint32_t) // Skip the size of the String index.
            + i * sizeof(SEntry)

SEntry(i) = ReadFromBinaryJsonBuffer(Offset(i))

StringStart(i) = if i == 0 then StringIndexStart else SEntry(i - 1)
StringEnd(i) = SEntry(i)
I promise this was the most confusing part of the format.
Tree
Finally, the Tree section encodes the structure of the stored JSON document. It is essentially an array of 32-bit integers, where each element encodes a node of JSON tree. Let us start by describing how individual JSON values are encoded.
Values
Each value is represented by an
Entry
structure. In the same way Header is encoded, it is split into two parts, 5 bits and 27 bits. First 5 bits determine the type of the value and the rest is reserved to store the corresponding value. The value’s meaning depends on the type:
Type value
Type name
Value
0
Boolean false
Undefined
1
Boolean true
Undefined
2
Null
Undefined
3
String
Index of the string in String index
4
Number
Index of the number in Number index
5
Array or Object
Offset pointing to the first by of the
Meta
structure
One can notice that we encode the boolean value directly in the type instead of introducing a generic boolean type with the 1 stored in the value when it is true. To be completely honest, I do not remember why we did that. Maybe we tried to avoid extra
if
s in the decoding process, but this seems like a premature optimization to me.
We can see that arrays and objects are stored as a reference to some kind of
Meta
structure. Let us dive into that.
Meta
structure is a 32-bit integer split in a familiar way. First 5 bits are reserved to encode the type of a container and the remaining 27 bits encode the size of a container. Each container starts with a
Meta
structure. Here is the list of currently supported types and their meaning:
Type value
Type name
Size
0
Array
Length of the array
1
Object
Number of keys in the object
2
Top-level scalar
Undefined
We will discuss the last type later.
Arrays
Arrays encoding is quite simple. It starts with a
Meta
structure, describing type and size metadata about the array. It is then followed by
N
records of
Entry
structure.
Entry #i
describes the value of array element at the position
#i
.
The fact that all entries have the same size and are written continuously gives us the ability to access elements by index in
O(1)
time. The following formula can be used to compute the offset of the corresponding
Entry
structure:
ArrayElementOffset(i) = ArrayBeginning + i * sizeof(Entry)
Objects
Objects encoding is a little bit more complicated, since we need to store both keys and values. We can look at a JSON object as an array of pairs
(key #i, value #i)
, sorted by the key. We can then separate these pairs into an array of keys and an array of values. These two arrays is exactly how BinaryJson represents JSON objects.
As all containers do, objects start with a
Meta
structure, encoding its type and total number of keys
N
. After that, we have
N
records of
KeyEntry
structure, followed by
N
records of
Entry
structure. Each key is represented by
KeyEntry
structure, which is simply a 32-bit integer, holding the index of the key string in the String index. Each value is represented by
Entry
structure. Key-value pairs are stored sorted by the key string.
One can notice that given a BinaryJson object, we can access keys and values by their index in
O(1)
time. In the same way we did for Number index and arrays, we can compute exact offset of the key and value using the following formulas:
KeyOffset(i) = StartOfObject + i * sizeof(KeyEntry)
ValueOffset(i) = StartOfObject + N * sizeof(KeyEntry) + i * sizeof(Entry)
We can use this property and the fact that all keys are sorted to quickly lookup a key in the object:
Try to find the requested key in the
KeyEntry
array using binary search
If the key was not found, object does not contain it
If the key was found at the position
KeyEntry #i
, return matching value
Entry #i
This way, we can provide
O(logN)
time complexity for individual key lookups in BinaryJson objects.
Top-level values
BinaryJson expects the Tree section to always start with the
Meta
record. While this is true if the whole JSON value is an array or object, it is not the case for all other values (like numbers and strings). For cases like this, there is a special container type called “Top-level scalar”. It is basically an array of 1 element with a special type to signal the reader that it should decoded as just one value, without array surrounding it.
Conclusion
In the end, we have a format with the following properties:
Traversable.
Reader can deserialize only the parts they require
Quick random access.
Random access in arrays takes
O(1)
time and random access in objects takes
O(logN)
time
Reasonably sized.
On the workloads we were interested in, BinaryJson was a little bit larger than its textual representation, but within reasonable limits
There is a number of improvements we could do to the format. For example, since the BinaryJson is immutable once written, we could experiment with perfect hashing to store objects and speedup key lookup even more. We could also try to store
Entry
structure as 64-bit double to eliminate Number index and use NaN tagging to store non-number values. Another idea is to inline small strings in the
Entry
structure and optimize space used by String index. Maybe this is something YDB team will explore in the future, but the solution described above is what I came up with in a limited time we had.
If you are interested in the code, feel free to explore
binary_json
directory of YDB source.
