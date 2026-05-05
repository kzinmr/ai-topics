---
title: "Inside New Query Engine of MongoDB"
url: "https://laplab.me/posts/inside-new-query-engine-of-mongodb/"
fetched_at: 2026-05-05T07:01:24.391030+00:00
source: "Nikita Lapkov (laplab)"
tags: [blog, raw]
---

# Inside New Query Engine of MongoDB

Source: https://laplab.me/posts/inside-new-query-engine-of-mongodb/

Discussion on
HackerNews
and
Lobsters
.
MongoDB has recently
released
a new query engine coming in version 7.0. I was one of the people working on this engine during my 2 years in MongoDB and I would like to share some technical details about it.
Disclaimer:
Prior to writing this article, I have contacted my ex-colleagues at MongoDB to ensure that it does not conflict with their plans. They gave me the green light, provided I send them the draft before publishing, which I did. They did not have any notes on it.
Query what?
From the user perspective, a database can be seen as a machine for running queries - after all, that is mainly how the user interacts with the system. Under the hood, there is a plethora of components doing the work: storage engine, replication, sharding, maybe some other stuff, and finally the query engine.
Query engine itself usually consists of a bunch of subcomponents:
Query parser.
Responsible for transforming the user query into some internal representation and reporting any syntax errors while doing it. It is definitely the smallest of the three, but an absolute pain in the ass to get right.
Query optimizer.
There are usually many ways to execute a query, depending on the predicates specified, their selectivity, which indexes are present, etc. Query optimizer
picks the best
tries its best to pick an optimal strategy for executing the query. This part usually involves a lot of math, with specific formulas and constants considered a trade secret by the proprietary databases.
Query execution engine.
Once the optimal strategy is picked by the optimizer, it is this component’s job to execute this strategy as efficiently as possible. What exactly is meant by “efficiently” varies drastically from database to database, but it is usually some balance of latency, throughput in terms of how much data we can process in a given timeframe, throughput in terms of how much queries we can send without overwhelming the system and some other factors.
The part MongoDB announced to be completely overhauled for the 7.0 release and the one I have been working on is the Query Execution Engine.
Reason for rewrite
Rewriting the Query Execution Engine completely from scratch is an enourmous endevaour which costed tens of engineer-years to the company. So why bother? There are multiple reasons for that, but the main two are performance and maintanability.
The root cause for performance issues was the data model. Old query engine (lovingly called the “Classic” engine internally) was built around the concept of JSON documents, meaning that most execution stages were accepting the JSON object as an input and returning one as an output. If there are multiple stages involved in the query, each one of them was producing intermediary documents to pass to the next one. User is not interested in any intermediary computations, they want to see the final result of the query, so this is wasted work. It is not as bad when you just want to run some simple predicate like “give me 10 users with balance greater than zero”. However, more complex queries transforming/aggregating/joining the documents suffered pretty badly from it.
A couple of intermediate query stages, each creating a JSON document to pass to the next one. All documents are discarded except the last one on the right.
Then there was the maintainability aspect of it all. For historic reasons, MongoDB has two query languages available - so called “find” and “aggregate”. One can think of “find” as a syntax for expressing predicates which would usually go into the
WHERE
clause of an analogous SQL statement. “aggregate” on the other hand provides the ability to build linear pipelines of execution: apply filter, then group documents by this field, add some projections, etc. It is sort of
GROUP BY
, but on steroids. While the two languages might seem similar, they have completely different implementations under the hood. Despite providing similar functionality in some aspects (comparison and arithmetics for example), the code for this functionality was separate and even sometimes provided different semantics! This lead to code and bug duplication, making the maintenance punishing. It also made it impossible to reason about the system hollisticaly - clever optimization you thought of for “find” language might not be applicable to “aggregate” and vice versa.
To summarise, “Classic” engine is a mature system which served the MongoDB customers’ queries since inception. However, its data model and approach to the “find”/“aggregate” situation resulted in suboptimal performance and serious maintenance burden.
So we are building a new query engine. Exciting! How do we actually do that, by the way..?
Basic idea: Slots
One of the main problems of the “Classic” engine was constructing lots of intermediary documents between execution stages. The main reason stages were doing this in the first place was to pass some
values
between them. For example, a
SCAN
stage reading a MongoDB collection (table in SQL terms) might pass the document to a
PROJECT
stage, which picks field
"a"
, adds
42
to it and returns the result. The
PROJECT
stage does not need the whole JSON document to respond to the query, just the field
"a"
. It would be cool if the
SCAN
stage had some way of knowing that and passed only the data neccessary for the
PROJECT
stage. There are lots of opportunities like that in a query engine, the common theme being that query stages think in terms of
values
, instead of
documents
. So what if we allowed just that?
The new query engine of MongoDB is built around the concept of
slots
. One can think of a slot as a dynamically typed variable. Slot can contain any valid JSON value - number, string, array, document, etc. and it is the main way different parts of the query engine pass the data between each other. In the example above,
SCAN
stage would have exposed a special slot containing the value of field
"a"
.
PROJECT
stage would then read the data just from this slot and perform the computation. Instead of passing the whole document around, we now pass only the data required to actually answer the query.
As the query is executing, we compose the query result piece by piece, slot by slot, until they all merge in a final JSON document containing just the data user asked for.
Perhaps unsurprisingly, the new engine was called Slot Based Engine or SBE for short.
Architecture: Expressions and Stages
From a high-level perspective, SBE is built on a Volcano model. It was first published in 1994 and is still widely used in the industry today. Each type of operation (scanning a table, filtering something based on a predicate, joining) is represented as a stream of data or an iterator. This stream abstraction provides
open()
,
getNext()
and
close()
interface and can be used like this:
stream.open();
while
(stream.getNext()) {
// Do something with the data stream provided.
}
stream.close();
Some streams can take other streams as input. For example, filtering stream accepts an input stream to get the data that needs filtering. Similarly, join stream can accepts two input streams - left and right sides of the joining operation. Following this concept, streams are composed in a tree and then the outer code uses the root of this tree to get the query results. These streaming operations on data are called
stages
in SBE.
In this example we have tree with two branches, one performing a collection scan with filtering on top of it and another performing some kind of aggregation of documents from another collection scan. Both streams are then merged together and returned as the output of the query.
In addition to stages, SBE also has expressions. If stages are used to manipulate streams of data, expressions are used to compute values. For example, the filter stage is responsible for omitting data that does not match the predicate from the stream. But the predicate that is used to filter data is specified using expressions. Another distinction is that expressions do not have any effects - they do not know what is a database and can be even used as a separate language for manipulating JSON data. Stages, on the other hand, are tightly integrated with other components of the system, such as storage and sharding.
Data flow
So far SBE sounds a lot like the Classic engine - we have stages and they pass around data through
getNext()
interface. The main distinction is that
getNext()
does not make a single JSON document available to the caller, but rather a set of slots. Each stage has a set of slots (read: variables) that it makes available to its parent in the tree. For example, projection stage computes some expression and assigns the result to the slot. This slot is available for any of the parent stages to be read from.
Let’s take a look at example:
Each yellow overlapping box displays some property of the stage it overlaps with.
The data flows upwards here, from the
scan
stage to the
project
stage. The
scan
stage reads documents from
"example"
collection one by one and outputs the current document to slot
s1
. So after calling
getNext()
on this stage the first time, we will get the first document stored in
s1
. One more
getNext()
call will get us the second document in
s1
, etc.
The
project
stage executes an expression which takes field
"a"
from the document stored in
s1
. It can get the value from
s1
because it was made available through the shared context by the
scan
stage. Once the expression is executed, it stores the result in
s2
, which is made available to the outer code running
project
stage. On the next
getNext()
call,
project
will first call
getNext()
on the
scan
stage in order to get the next document stored in
s1
and then it will re-run the expression using this slot to store the result in
s2
.
Note that this logic of “call
getNext()
of your child before doing anything yourself” is unconditional in
project
stage. There is no dependency tracking like “my expression uses
s1
, which is provided by the
scan
stage, so I need to call
getNext()
on it”.
project
stage always calls
getNext()
of its child.
Despite the fact that the context through which the slots are accessed is shared, the slots themselves always have a single owning stage and are always immutable between
getNext()
calls. This allows the engine to avoid extra data synchronization in case some parts of the query are executed in parallel.
The things start to get interesting once you add a
filter
stage on top of this query:
This query only outputs documents with the value of field
"a"
equal to
1
.
Everything, including the query result, is stored in slots. Slots produced by the stage are always available after its
getNext()
call finishes. So how does the
filter
stage makes sure that it only outputs the correct documents? The answer is pretty simple - its
getNext()
implementation simply does not return until the predicate is satisfied. In pseudocode it would look something like this:
Result FilterStage::getNext() {
// Run until we have found a combination of slots
// in the child subtree that satisfies the predicate.
while
(! predicate.run()) {
// If the child does not have any data left,
// we know for sure there is nothing else that
// could match the predicate.
if
(child.getNext() == EOF) {
return
EOF;
}
}
return
OK;
}
Once the
filter
stage’s predicate was satisfied, it returns an
OK
result to the caller, signifying that values currently stored in the slots passed the filtering. Since slots’ scope extends upwards (with exception of a few stages), the outer code currently calling
getNext()
on the
filter
stage can get the document matching the predicate from
s1
.
In simple queries like the one above, the data flow is pretty straightforward. However, one can imagine how more complex stages like
nested loop join
can have a much more convoluted logic in how and when they call
getNext()
on their children. If the stage has multiple subtrees under it, it can be also pretty useful to access slots from one subtree in another one. Developer needs to remember rules on how the slot scoping is defined and it can get out of hand pretty quickly if you have a query with 5 levels of nested joins in it - not at all an uncommon case. I spent hours adjusting my mental model to how data flows in SBE and even more hours trying to explain it to new engineers during their onboarding.
Compilation
Expressions and stages were intentionally designed to not contain any knowledge about “find” or “aggregate” languages. For example, equality operator in expressions has a slightly different (and more sane, if you ask me) semantics compared to analogous
$eq
operator in “find” language. One of the SBE goals was to provide a
unified
execution runtime for both “find” and “aggregate” languages. To do that, SBE provides basic primitives with some well defined semantics and relies on the query compiler to construct necessary semantics from these building blocks.
To translate the query plan from the optimizer, SBE uses a “simple” visitor compiler, which traverses the query tree and constructs a bunch of stages and expressions from it. It is simple in a sense that there are almost no clever optimizations at this point. However, the amount of work that went into correctly expressing all the semantics of the MongoDB query language is just absolutely insane. There was a team of 10+ engineers working on this compiler just because of the sheer scope of this endavour with over a hundred of query operators analysed, implemented and tested for performance and correctness.
Since we do not have direct analogues of some operations from the query language, we need to generate quite a bit of bytecode to express the full semantics. For example, if the built-in addition operator of the Virtual Machines computes
1 + NaN
as a
NaN
value, but the
$sum
operator from the query language computes it as
null
, you need to build an if statement for this case. Instead of
left + right
you now have
if(right is NaN, null, left + right)
. Things like that add up really quickly for complex queries.
The worst part of it, however, is when this leads to re-evaluating constant expressions over and over again. For example, if the right hand argument of the sum operation is a constant number
2
, then we know at compile time that a predicate checking for
NaN
value will never be true. This makes the whole check useless, since we can just directly perform the summation.
To mitigate this problem, we have introduced an intermediary representation, into which our compiler translates the query. Once the query is translated, we run a few very simple optimization passes in order to fold constant expressions and make the code more straightforward in some cases, which saves a huge amount of work during the execution.
The root of the problem, however, is not in the compiler. The expression code size directly impacts the query performance and it is the query optimizer’s job to choose the best strategy to execute the query - including which expressions to use. However, rewriting the optimizer to understand SBE primitives at the same time as rewriting the whole execution engine was not a feasiable approach for us at the time, since it would make an already very ambitious scope even bigger. So we decided to try to make improvements incrementally and reuse parts of these simple optimization passes later in the new optimizer.
Why not just use LLVM at this point? JIT compilation of database queries is a well researched topic, but that does not make it any easier to implement. While LLVM would bring us some optimizations (like constant folding) out of the box, it also has some costs like increasing the query compilation time even more and introducing more fun ways to SEGFAULT the server. The general consensus at the time was that we should start with a good Virtual Machine for SBE first and dive into the JIT rabbit hole only after we got all the low-hanging fruits there. That did not stop me and some of my colleagues from experimenting with LLVM on internal hackathon though :) It did bring some performance benefits on complex expressions, but much lower than we expected, proving that it is not as easy as just calling
JIT.compileToMakeReallyFast()
.
Virtual Machine
SBE has its own virtual machine to execute expressions. It was purposefully created to be relatively simple stack-based VM with a very limited set of operations included.
One of the defining traits of this VM is that it manages all memory used by expressions. If an array was allocated during expression evaluation, it is ultimately the VM’s responsibility to free the allocated memory once it is no longer needed. It made evaluation code a bit more cumbersome with explicit lifetime management everywhere, but such managed approach meant there will be
no
a very limited amount of memory-related bugs in generated expressions.
It was always a hot debate topic internally which built-in operations to include in the VM. On one hand, if the instruction set is too bare, we end up with huge expressions even for the simplest queries, hurting the performance. If we create built-in function for each small task, the generated code will be very small and fast, but we would end up in a similar situation as the Classic engine with a myriad of single-purpose C++ functions to maintain and optimize. In the end, a good rule of thumb we ended up with is to try adding built-ins only when optimizing hot-paths on representative benchmarks and try to use the existing functionality otherwise.
Things I would do different
There are some things I would change in SBE retrospectively. Now that we are in a more stable part of this rewriting journey, it is easier to see which alternative paths we could have taken and where we could have (possibly) made things better.
Errors as values
One of the main goals of the project was for the VM to be query language agnostic. This means that the VM instructions themselves have no direct relation to the operators used in the query - much like assembly does not have any specific instructions with C++ or JavaScript semantics.
Or does it?
Unfortunately, this means that the VM operator cannot return a proper error for the user. Take a
+
VM instruction for example: it cannot throw error
"$add operands must be numbers"
because it is not always used for the
$add
operator. Maybe it is used for the
$count
operator in the aggregation query. Error mentioning some other operator would be very confusing for the user.
To mitigate that problem, all error checking must be done in some wrapper code generated for each query:
(
if
!isNumber
(
left
)
error
(
"left operand is not a number"
)
(
if
!isNumber
(
right
)
error
(
"right operand is not a number"
)
left
+
right
)
)
Not only that’s a lot of code to execute, but we also need to re-check all the conditions in the implementation of the
+
VM instruction again!
+
operand has no knowledge that the operands have been already type checked and must ensure the correct types once again in order to avoid undefined behaviour or even SEGFAULTs in some cases.
I think that making errors normal values and adding a construct to match against them would really help the situation.
+
instruction can return an error code which we can decipher in the wrapping code later like that:
(
match
left
+
right
(
errCode
(1)
error
(
"left operand is not a number"
))
(
errCode
(2)
error
(
"right operand is not a number"
))
)
Here, a special
match
operator checks if the returned error code matches against any of the provided branches and runs the corresponding code if it is (here we just throw an exception with
error
). If the
+
VM instruction returns an actual value instead of an error code, it just returns this value.
This approach allows us to avoid validating the same conditions two times in a row and leaves less code for the VM to interpret.
Debugging experience
At later stages of the development, SBE became a proper programming language and our compiler started to generate more and more complex expressions and trees. If the query was behaving incorrectly, it was becoming harder and harder to find out what exactly went wrong.
I am a println-debugging kind of guy, but I still use GDB for in-depth debugging sometimes. In this case, however, I cannot say it was very helpful. When debugging SBE programs, I was quite often interested in what the engine was doing step-by-step and going through layers and layers of indirection in the VM and the stages was quite tedious.
To help with that, I spent a few days of the internal hackathon building a recording debugger for SBE with a web interface looking like this:
This debugger recorded state of all slots on each step of the execution be it inside VM or between
getNext()
calls of the stages. The end result was that the developer could actually step through the SBE program and see the slot values at any point of time, which was quite useful when investigating correctness bugs.
I really wish we would merge this tool into the main branch, but the consensus of the more senior engineers was that it was too hard to maintain in the long term.
Conclusion
SBE is designed to solve a very difficult task. Without fixed schema, it can assume little about the data it works on, yet it is pressed to be as performant as SQL databases, which often have more opportunities for optimization. Despite the odds, it does perform quite well and provides a strong foundation for the future.
It was an absolute blast to work on it and I feel humbled that I had the chance to work with and learn from industry professionals at MongoDB. I would like to thank my colleagues for going through this journey with me and sincerely congratulate them on pushing it over the line for the 7.0 release. I wish them good luck and let the whiskey bar never dry out :)
