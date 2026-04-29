---
title: "How to write complex software"
url: "https://grantslatton.com/how-to-software"
fetched_at: 2026-04-29T07:02:16.551146+00:00
source: "grantslatton.com"
tags: [blog, raw]
---

# How to write complex software

Source: https://grantslatton.com/how-to-software

How to write complex software
Suppose you are implementing some complex piece of software — a database, a word processor, a filesystem, a web browser, whatever. How do you get started? How do you actually organize the code?
This post attempts to lay out a general method for approaching this problem with some specific techniques and guiding heuristics.
Overview
The 10,000 foot view of what we'll discuss:
Write some toy driver programs to find out the physical constraints of the solution-space you're operating in
Start at the top of the stack, usually this means the user interface or API
Implement your software in layers, where each layer peels off the minimum amount of logic possible and delegates all remaining complexity to the next layer
When coding a layer, define the API of the next layer down to be the perfect
domain-specific language
to implement the current layer in
Stub out the layer down as you code the current layer
When the current layer is done, recurse and implement the layer down for real using this same method
Continue until you are done
Only implement mockable abstract interfaces for parts of the code that do IO — everything else should be concrete
When this post applies
Developing complex software is really different than small software. If your whole program can fit in under 5000 lines or so, you'll often be best served by a single giant file with minimal abstractions.
Minimal abstraction means making changes will often involve mutating a lot of code, the total amount of code in the whole project is small, so this is fine.
When working on a large project, one that is unavoidably tens or hundreds of thousands of lines of code, this strategy does not work, and abstraction and organization is needed.
Getting started
Before actually writing any software, we want to find the boundaries of the space of possible solutions.
If we're writing a database, let's create a mock request and test just how many requests per second we can parse in the best case scenario? How many small reads and writes can our disk handle? How many checksums can your CPU compute per second?
You should write little micro-benchmark programs to find the answers to these questions.
While you don't know what your actual software will look like yet, you know some broad things that must be true. A filesystem must write the data to disk. A webserver must send data over a socket. A word processor must render text.
How those goals are actually accomplished is determined by the software, but you know they must be done, and you can often establish some a priori bounds of your hardware.
I think of this part of the process as carving off large, coarse chunks of the solution space. You might find out something like "well, there is no way I can compute a checksum of every individual file, it uses way too much CPU, so I know whatever design I use must batch files with at least 100 files per batch".
These are the types of learnings you'll want to keep in mind while actually implementing the software.
Working top to bottom
A trap some engineers fall into is to view software development as a
directed acyclic graph
(DAG) of components that depend on each other, and the natural place to start developing software is the components with no dependencies.
For example, consider a word processor. The UI depends on the layout engine. The layout engine depends on the text data representation. The text data representation depends on the file format.
So the engineer will start implementing their word processor by coding the file format first! After all, it can be coded, tested, completed without any other components.
Then they'll move up the stack to the text data representation. Then the layout engine. And finally, the UI.
The advantage of this method is you never have to stub out anything, never have to write mocks, etc.
The disadvantage is
huge
though. You're locking yourself into a design before you have written the software! When you're implementing one layer, you're guessing at what API the layer up is going to need, and implementing that.
When you go to implement the layer up, you may have to work around a not-quite-perfect API that you are hesitant to change because you already spent all that time implementing it.
The method I propose is the exact opposite. You start coding at the top of the stack, letting each layer define the API of the layer below it. Only once that layer's implementation is beautiful — because the stubbed out API of the layer down is just what it needs — do you implement the layer down.
Another advantage of this method is you always have semi-working software. You always have a UI to show the boss or an API the other team can start testing against. It may not be functionally complete yet, but partial is better than nothing!
A disadvantage of this method is you will spend a little time implementing dummy placeholder implementations while you work. The mock implementation will probably only take 5% of the time as the real implementation, so your total velocity will only be slowed by 5%. You'll gain that time back — and more — elsewhere with this method.
Implementing a layer
Each layer of your software should ideally be easily readable. If it's not readable, this means it's peeling off too much logic. Consider these two toy examples:
class
Blog
:
def
serve
(
self
,
request
)
:
self
.
rate_limiter
.
throttle
(
request
)
article
=
self
.
article_store
.
get
(
request
.
article
)
if
not
article
:
return
self
.
not_found_page
formatted
=
article
.
format
(
request
.
locale
)
return
formatted
versus
class
Blog
:
def
serve
(
self
,
request
)
:
if
request
.
ip
not
in
self
.
request_counts
:
self
.
request_counts
[
request
.
ip
]
=
1
else
:
self
.
request_counts
[
request
.
ip
]
+=
1
backoff_duration
=
0
.
5
*
(
2
*
*
(
self
.
request_counts
[
request
.
ip
]
-
1
)
)
time
.
sleep
(
backoff_duration
)
file_path
=
f
"
/storage/articles/
{
request
.
article
}
.txt
"
if
not
os
.
path
.
isfile
(
file_path
)
:
return
self
.
not_found_page
with
open
(
file_path
,
'
r
'
)
as
f
:
article
=
f
.
read
(
)
if
request
.
locale
==
"
en
"
:
...
etc
...
This is obviously just a toy example, and it's likely a simple blog backend falls in the category of "small software" that should really just be one giant file with no abstraction.
The point of this example is to demonstrate what I mean about peeling off complexity.
Most people do this wrong, though. They start by implementing the complex latter example, and only later
refactor
it into the abstracted simpler form.
The right way to do it is to
code the simple version first
. Code it that way
before
you have implemented the
rate_limiter
or the
article_store
or whatever. Just imagine they exist. Code as if the perfect API to implement this layer already existed.
Then, once your code looks beautiful, go implement those things.
Stubbing implementations
Once you code a layer, you need to implement the APIs you imagined. You should start by simply stubbing them.
A stub can be as simple as returning a fixed value or even throwing an exception or crashing. Just whatever is needed to make the project build or code compile.
For example, a stub of the
rate_limiter
above may just do nothing, or sleep for a constant 100 milliseconds. A stub for
article_store
might always return
None
or always return the string
"dummy article"
.
Stubs can also be somewhat more fully-fledged
mocks
. An example mock article store might be a hash table of a few sample articles, to enable testing something like an article index page. Maybe it even allows creating new articles, but doesn't persist them to any permanent storage.
You want to minimize the amount of time you spend implementing stubs and mocks, because you're going to be implementing the real thing soon. Do whatever the minimum needed is. Feel free to use temporary hacks.
When to really mock
The only thing you want to consider producing separate "real" mocks for is the IO layer. You want to do this for tests, because you probably want your tests to be fast and deterministic. You don't want them making network calls or whatever.
So in the case of a database, say, you would mock out the underlying data storage layer, i.e. the hard drive or filesystem.
If your database is something like SQLite that stores the database into a file, you can implement an interface that matches the features of the POSIX file handle interface. The real implementation just wraps a real file handle. The mock just stores data in an in-memory buffer or something.
Now with your mock, you can do things like deterministically inject corruptions, failures, etc to test your software in those scenarios.
Do
not
mock things that don't do IO. Why would you? You have the real implementation! Test your real implementation! Only swap out the IO dependencies with your IO mocks.
Collaboration
An advantage of this method is once you get the process started, it becomes natural to have one person implement one API while someone else implements another.
The "layers" analogy isn't like a cake, where 1 layer sits on 1 other layer. Each layer often has
many
sub-layers. The blog example above has 3: the rate limiter, the article store, and the formatter.
And in a more complex piece of software, those sub-layers may themselves have sub-layers! Each of these branches represents a point to delegate work to another engineer.
They have a well-defined API to implement. You've provided a stub implementation. Your layer that exercises it hopefully comes with unit tests. You have set them up for success!
This does mean most projects will need to
start
with only 1 developer who codes the very top layer. But this is a good thing! It's a great responsibility and sets the tone for the whole project.
Pitfalls
It's rare, but you can code a layer in terms of an API that isn't actually possible to implement.
Maybe you go to implement it and realize there is no way for this sub-layer to have all the information it needs to do its job, or the plumbing is just wacky. It happens.
In this case, rather than trying to force it to work or tweak things into place, I recommend just deleting this code, backtracking up the stack, and re-implementing the layer above with your newfound knowledge with a new API you think will be implementable.
Closing thoughts
No hard and fast rules
All such heuristics should be applied judiciously. This is a general guide, not a formal algorithm. You will need to deviate from it when appropriate. Becoming a better software engineer is the process of learning when to deviate from paths like this.
AI Devs
This general method is particularly well-suited to developing software with LLM agents, since it's kind of a general flow chart and chunks up work nicely to fit into context windows, etc.
If someone makes an LLM agent that writes software with this method, let me know, I'd love to see it.
Further reading
Algorithms we develop software by
— Another article I wrote about the solution-finding part of the software process, whereas this is more about the nitty-gritty code writing.
Lightweight property-based testing
— An article about a powerful unit testing technique that can be applied to most software
Modern functional programming, Onion architecture
— An article I read almost a decade ago that got me thinking about this general idea. I disagree with some of the recommendations and details, but have to acknowledge its influence. It got me thinking of software as layers of domain-specific languages. The article is mostly about functional programming / Haskell, but can be applied to any language.
