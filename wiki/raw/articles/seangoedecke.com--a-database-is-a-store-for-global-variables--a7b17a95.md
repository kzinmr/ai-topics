---
title: "A database is a store for global variables"
url: "https://seangoedecke.com/a-database-is-a-store-for-global-variables/"
fetched_at: 2026-11-06T10:01:09.822112+00:00
source: "seangoedecke.com"
tags: [blog, raw]
---

# A database is a store for global variables

Source: https://seangoedecke.com/a-database-is-a-store-for-global-variables/

Databases are for storing global variables. We usually call them “rows” or “records” instead, but they’re definitionally global variables: any part of your program can read or write them. Isn’t this kind of weird? It’s common programming advice that global variables are bad, and yet many elegant programs rely on databases. Either the common advice is wrong, or there’s something special about databases that makes them the exception to the rule.
What’s so bad about global variables? Here’s the two main
1
reasons, in my view:
They allow any part of your program to implicitly send data to any other part instead of passing it around via function signatures
They couple different parts of your program: if one part depends on a variable having some value, any other part can break it
Both of these apply to databases. Any part of your program that makes a query can send and receive data from any other part of your program. In practice this happens all the time: one function will save some data  on a record, and another one will check for it. And if you haven’t seen bugs where some piece of code makes some incorrect expectation about the shape
2
of a database column, you haven’t been working on web systems for long enough.
So why aren’t database-backed apps in terrible architectural shape? In the rest of this post I’ll consider some options.
First, we could
bite the bullet
:
maybe all database-backed apps really are a mess
. This is surprisingly plausible. When I think about the systems I’ve worked on that haven’t involved a database, they’re usually much cleaner and more elegant. If managing state is the hardest thing about designing software — and I think it is — then systems that manage less state are going to be better-designed. However, this doesn’t explain everything. Database-backed apps aren’t
that
bad, and even in database-backed apps, we try to avoid introducing regular global variables
3
, so in practice we treat global variables as worse.
Second, we could say that
databases offer ACID guarantees that mitigate the damage of global variables
. Unlike regular global variables, databases offer a consistent view of state and the ability to atomically change multiple pieces of state together. I don’t really buy this. The problem with global variables is not just that they can get out of sync, it’s that they exist at all. If you think this is the difference, you are committed to thinking
4
that if you stick a mutex around a global variable then it suddenly becomes acceptable.
Third, we could say that
databases are more explicit
. Mutating or reading a global variable looks like ordinary code, but database queries need some connection object to be passed in and some query function to be invoked. When you’re scanning through code, you can see where the database queries are at a glance
5
. Not so for global variables. This does actually kind of mitigate the implicit-coupling problem. Maybe regular global variables would be better if you had to set and get them with long, involved function calls.
Fourth, we could say that
databases are less flexible
. A global variable could store
anything
: a function, a class, an image, and so on. A database just stores
data
. I can buy this explanation for untyped languages. Global Ruby variables that could be reassigned from a string to a hash table are far more terrifying than a “global” database column that could change from one string to another string. But since the advice to avoid global variables applies to typed languages as well, I don’t think this could be the reason why databases are better.
Fifth, we could say that
we know how to use databases
. For instance, whenever I read from a database, I reflexively check the type of the column so that my code doesn’t make assumptions that aren’t guaranteed by the database. There are use-cases that I would never even consider using a database for (e.g. to track a counter in a loop, or to store the name of the
.env
file where my config is stored). In other words, we have norms and customs
6
around using databases that minimize a lot of the damage that global variables can cause. There’s nothing inherent about databases that make them better, it’s just how we use them in practice.
Overall I think the third and fifth reasons are most convincing: databases are better because they’re more explicit and because we only tend to use them for a limited set of purposes. It’s interesting to note that these reasons are
contingent
, not inherent. A codebase which had conventions around global variable use
7
could also fulfil these conditions. Would this make global variables fine, or at least no worse than a database? I think so.
I don’t recommend you go out and start putting global variables in your programs. It’s more interesting to note the meta-point here: that two pieces of common software engineering dogma — avoid global variables and use a database for state — are partially inconsistent. Most software design knowledge is still just a pile of loose heuristics.
I don’t really know how to build software and you don’t either
. As I’ve
written about before
, we should therefore all be very suspicious of engineers who appeal to “best practice” without being able to give concrete reasons, even in cases as obvious as “global variables are bad”.
