---
title: "Lightweight property-based testing at Row Zero"
url: "https://grantslatton.com/rowzero-property-testing"
fetched_at: 2026-04-29T07:02:16.789868+00:00
source: "grantslatton.com"
tags: [blog, raw]
---

# Lightweight property-based testing at Row Zero

Source: https://grantslatton.com/rowzero-property-testing

Lightweight property-based testing at Row Zero
Row Zero
is the world's fastest spreadsheet. It's just like Microsoft Excel or Google Sheets, but 1000x faster.
Spreadsheets are a really interesting software domain, because they have a ton of overlapping features.
What happens if you enter two numbers into two cells, format the numbers as text, merge them into a single cell, copy paste that merged cell somewhere else, then filter that range by dates in a certain year?
The number of feature interactions grows with the square of the number of features. It's not tractable to test them all manually. How can we ensure software quality, then?
We lean heavily on
lightweight
property-based testing
.
Property-based testing
The general form of a property-based test is:
Sample an input from a distribution of possible inputs
Do the operation under test
Compare the result to some tautological properties, or some reference implementation
Repeat a lot of times
There are a few frameworks for doing this. Most can trace their lineage back to Haskell's
QuickCheck
library. The main thing the frameworks provide is:
Auto-generation of simple inputs
Input shrinking to try to find minimal cases
Deterministic replay of failures
Additionally, there are frameworks such as
AWS's Shuttle library
that allow for deterministic replay of
concurrent execution order
to enable testing for multithreaded race conditions. Most of the Row Zero team formerly worked at AWS and used tools like this to
formally verify the S3 filesystem
.
Verifying a spreadsheet
There are three main kinds of property-based test we use. In decreasing order of verification power, they are:
Test against a reference-model for blackbox equality
Test against a set of general properties or invariants
Test for crashes
Blackbox reference-model testing
Blackbox reference-model testing is the best and most powerful method. This involves testing the real implementation of something against a reference model. Typically, the reference model will be much less efficient than the real one, or lacking some functionality.
An example of this is how we store the values of the cells in the spreadsheet. You could imagine a solution that is just a giant hash table whose key is the cell name, and the value is the contents of that cell. In practice, we do something much more efficient than this, but our optimized implementation should still
behave
like a simple hash table.
So we can make a test that does random cell inserts, updates, and deletes to the real data structure, and a simple hash table reference. Then, at the end of the test, we compare them to make sure they have the same values in each cell.
Invariant testing
Sometimes, making a reference model would just be as complicated as the real test subject, so it's not feasible to do blackbox reference-model testing.
In these situations, you can often still test for invariants. An invariant is just some property that always must be true in any non-buggy implementation.
For example, in a test that randomly edits values from cells, we can assert the invariant that the number of values in cells must always be less than or equal to the total number of edits we've done.
You can come up with all sorts of invariants like this.
If only only edit cells to contain numbers, you can assert that no cells at the end of the test should contain text. You filter out rows that don't equal some value, you can assert that no cells with that value are visible.
With each invariant, you slice off a chunk of possible bugs. Overlapping a bunch of variants provides surprisingly high coverage. A lot of bugs will manifest in different ways that just happen to overlap with some of the variants you chose some of the time. Enough test iterations, and you'll often find them.
Crash testing
Sometimes, for the most general tests, the only invariant you can assert is that the program doesn't crash. One of the most valuable tests we ever wrote at Row Zero is the one that just takes the top-level spreadsheet interface, and takes completely random actions on it.
Copy paste. Update cell. Double-click drag. Undo. Redo. Filter range. Insert pivot table. Delete all. New sheet. Just every combination of actions imaginable.
Spreadsheets involve tracking
a lot
of state. Each cell has an evaluation, the raw user input, a format, visibility state, if it's in a merged range, and more. If any of these data structures get out of sync, weird things happen.
We insert test-only assertions all over the codebase to verify things are in sync. If they aren't, the assertion will fail, inducing a crash, and causing this test to fail.
We then inspect the set of random actions that led to the crash to debug the issue. You can find issues this way you would have
never
thought to create a specific unit test for. Random search is the most scalable solution to find this kind of bug.
Nuts and bolts: diving into some code
Now we'll talk about the actual implementation of these tests.
Template
The general form of a test is:
#
[
test
]
fn
foo_proptest
(
)
{
let
mut
rng
=
rand
::
thread_rng
(
)
;
for
action_count
in
1
..
4
{
for
_
in
0
..
10_000
{
let
seed
=
rng.
gen
::
<
u64
>
(
)
;
eprintln!
(
"
let seed = {seed};
"
)
;
let
mut
rng
=
ChaChaRng
::
seed_from_u64
(
seed
)
;
//
Set up and run an instance of the test
}
}
}
We don't use a testing framework like the Rust
proptest
crate. We find we don't get a lot of benefit from frameworks for our use case, and it's easy to get most of the functionality with something like our template above.
Let's break down this template.
Non-determinism
The first line is just getting a handle to
thread_rng()
which is a true random number generator that delegates to something like
/dev/urandom
.
We use the OS randomness in the outer loop so the test will run differently every time. Some bugs are so rare, you won't hit them every time! It's good to keep changing seeds to increase the surface area you test.
The lack of determinism here may bother some people. But we assert it's better to find the bug
late
than
never at all
because a deterministic seed just tests the same cases over and over again.
Most bugs are shallow and get found before they are committed. But sometimes, our CI will find a
super subtle
bug that was introduced a few commits ago, but it just took more runs to hit. Because these ultra-rare bugs are so absurdly difficult to induce, it's typically the case that no real users would ever get close to triggering them.
Complexity
The
action_count
loop dictates the
complexity
of the test. If we are testing say, our spreadsheet cell value data structure, this line will make us start by just updating 1 cell, then the next loop we'll update 2 cells, then 3, then 4.
These numbers are just picked out of a hat based on intuition on where the bugs probably are in the problem domain. We could just as well do
action_count in [3, 11, 99]
. But in this case, our intuition is that all cell-update bugs can be triggered with a maximum of 4 actions.
The value in going from low-complexity to high-complexity is you find the simple bugs first. The bugs that require the fewest actions to reproduce. These are the easiest to understand what went wrong, and the easiest to fix.
This is the poor man's version of
input shrinking
that some property-based testing frameworks provide for you.
With input shrinking, a property-based test that finds a failure will try to "shrink" the failure case by deleting actions, making inputs "smaller" in some way (e.g. smaller numbers, shorter strings), etc.
Our method is to simply do a series of depth-limited searches with increasing depth. The effect is that we will typically find the simplest cases early, and no shrinking is necessary.
In this template,
action_count
is just a stand-in for any kind of complexity configuration you want. You could make a
Config
struct with 3 fields, then define 4 instances that increase the complexity of those fields in some way, and then make our outer loop go through those configs in sequence.
Iteration
The next loop just tries to to find a bug 10,000 times. This number can be whatever you want and is reasonable. Some tests that are particularly resource-intensive may only get 100 iterations. Some really fast ones may get a 1,000,000. We usually start with 10,000 and scale it up or down as needed.
Sometimes, upon first implementing a test or feature, I'll set it to an absurdly high number and just leave it running while I go get lunch. I don't commit this number, but it gives additional confidence if a test ran for an hour and didn't find any issues.
Determinism
Inside the individual test case, you
do
want determinism. That is, given just the seed, you want to be able to reproduce the test.
So we use our real random number generator to make a seed for a pseudorandom number generator, then our test case uses
that
to create values and run the test.
We print out the seed to
stderr
so if the test fails, we can see the exact seed it failed on.
To replay a test, just do
let seed: u64 = 12345
or whatever the failing seed is.
The actual test case
This is where you set up your article under test, any reference models, etc. You do some random actions based on the config. Then you assert your invariants or check your model.
Examples
Here are some real examples from the Row Zero codebase.
Builtin functions
const
N
:
usize
=
2_000
;
let
mut
rng
=
thread_rng
(
)
;
for
max_arg_count
in
[
3
,
8
]
{
for
max_column_len
in
[
1
,
2
,
20
]
{
for
_
in
0
..
N
{
let
seed
=
rng.
gen
::
<
u64
>
(
)
;
let
mut
rng
=
ChaChaRng
::
seed_from_u64
(
seed
)
;
let
(
name
,
f
)
=
all_builtins
(
)
.
iter
(
)
.
choose
(
&
mut
rng
)
.
unwrap
(
)
;
eprintln!
(
"
-----------
\n
let seed = {seed}; // {name}
"
)
;
let
arg_count
=
rng.
gen_range
(
0
..
=
max_arg_count
)
;
let
column_len
=
rng.
gen_range
(
0
..
=
max_column_len
)
;
let
mut
args
=
vec!
[
]
;
for
_
in
0
..
arg_count
{
args.
push
(
gen_arg
(
column_len
,
&
mut
rng
)
)
;
}
This example is where we search for crashes in the implementation of our builtin functions (e.g.
SUM
,
VLOOKUP
, etc). We do this by just generating random inputs and sending them into the functions!
You can see rather than a
Config
object, we just use triple-nested loops to go from low-complexity to high-complexity cases.
This test protects us from weird cases like what happens when you compute
IRR
on diverging set of values that goes to infinity? Or what happens when you try to multiply two dates together? If the answer is "crash because we didn't expect that", this test will find it.
CSV parsing
let
mut
rng
=
thread_rng
(
)
;
for
_
in
0
..
1000
{
let
seed
:
u64
=
rng.
gen
(
)
;
eprintln!
(
"
let seed: u64 = {};
"
,
seed
)
;
let
mut
rng
=
ChaChaRng
::
seed_from_u64
(
seed
)
;
let
table
=
gen_table
(
&
mut
rng
)
;
let
schema
=
CsvSchema
::
gen
(
&
mut
rng
)
;
let
csv
=
schema.
encode
(
&
table
)
;
let
state
=
ImportCsvStateMachine
::
new
(
csv.
as_ref
(
)
)
.
unwrap
(
)
;
state.
update_schema
(
schema.
into
(
)
)
;
state.
feed
(
csv.
as_ref
(
)
)
;
let
parsed
=
state.
finalize
(
)
.
unwrap
(
)
;
assert_eq!
(
table
,
parsed
)
;
This is more of an invariant-style test. We make a random CSV schema (delimiter, separator, single or double quotes, etc). Then we make a random table of data and encode it with that schema. Then we parse that CSV. We assert that the parsed table is the same as the one we started with!
Handling busted CSVs
let
mut
rng
=
thread_rng
(
)
;
for
_
in
0
..
1000
{
let
seed
:
u64
=
rng.
gen
(
)
;
eprintln!
(
"
let seed: u64 = {};
"
,
seed
)
;
let
mut
rng
=
ChaChaRng
::
seed_from_u64
(
seed
)
;
let
table
=
gen_table
(
&
mut
rng
)
;
let
mut
schema
=
CsvSchema
::
gen
(
&
mut
rng
)
;
let
csv
=
schema.
encode
(
&
table
)
;
let
offset
=
rng.
gen_range
(
0
..
csv.
len
(
)
)
;
let
length
=
rng.
gen_range
(
0
..
csv
[
offset
..
]
.
len
(
)
)
;
//
cut out a random part of the csv
let
csv
=
format!
(
"
{}
{}
"
,
&
csv
[
..
offset
]
,
&
csv
[
offset
+
length
..
]
)
;
let
state
=
ImportCsvStateMachine
::
new
(
csv.
as_ref
(
)
)
.
unwrap
(
)
;
state.
update_schema
(
schema.
into
(
)
)
;
state.
feed
(
csv.
as_ref
(
)
)
;
state.
finalize
(
)
.
unwrap
(
)
;
This test is just a crash test. We generate a random CSV, but then cut out some portion of the middle, so now it's likely in a buggy state. Maybe we cut it mid-quote, or mid-line, etc. We just want to verify that our parser doesn't choke and crash on goofy inputs.
We have a bunch of other CSV parser tests that do other mutations, or assert other invariants.
Hidden rows
let
mut
rng
=
rand
::
thread_rng
(
)
;
for
action_count
in
1
..
4
{
for
_
in
0
..
10_000
{
let
seed
=
rng.
gen
::
<
u64
>
(
)
;
eprintln!
(
"
==================
"
)
;
eprintln!
(
"
let seed = {seed};
"
)
;
let
mut
rng
=
ChaChaRng
::
seed_from_u64
(
seed
)
;
let
mut
mock
=
MockHiddenRows
::
default
(
)
;
let
mut
real
=
HiddenRows
::
default
(
)
;
for
_
in
0
..
action_count
{
We keep track of which rows are hidden in an optimized structure. But that thing should behave just like a hash set of the rows that are hidden. In this case, we've put that hash set inside the
MockHiddenRows
object to keep the test readable, but the idea is still the same.
Conclusion
The tests are starting to all look familiar. The template is there in all of them. There's no special magic. Each test is typically between 15 and 100 lines of code. They provide
immense value
and are among the highest bang-for-your-buck tests you can write.
If you aren't using property-based tests, your application is probably riddled with bugs. At AWS, when we added property-based tests to some legacy code that didn't already have them, we almost always found things to fix.
Randomized property-based tests require minimal maintenance since they operate at the API-level and mostly on always-true invariants instead of implementation details. They are fast to code for the same reason.
Go write some today!
