---
title: "C# as a Language from old Google+ Post"
url: "https://boyter.org/2015/08/c-language-google-post/"
fetched_at: 2026-05-05T07:02:01.743856+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# C# as a Language from old Google+ Post

Source: https://boyter.org/2015/08/c-language-google-post/

The more I use C# as a language for writing things the more I am convinced that its approach really is the best language approach out there.
The unit test support is excellent which allows development speed to be just as fast as any dynamic language (Python, PHP, Perl).
The static typing catches so many issues before you get to runtime and allows sweeping changes without breaking things.
Unlike Java it has the var keyword (saves time and improves readability) and so many more useful functions which yes you can replicate but are just built in and work correctly.
Then you get to the really good stuff. LINQ is awesome. The lazy loading allows you to implement a repository pattern over your database which is just awesome. Set up the basic select * from then add extension methods allowing you to chain whatever you need, EG
from person in _dbContext.
GetPerson
().
ByUserName
(username).
ByPassword
(password);
100% elegant, easy to test, easy to write, easy to read and understand and generally works exactly as you would expect without any hidden gotchas. And because its lazy it doesn’t chew resources sucking back everything from the database.
You can use functional programming techniques if you wish, and with the new async decorators you can work in a node.js style if you with, with static typing and all existing library support.
Or you can continue to work in a C like manner, or mix it up with objects, procedural code and functional.
I switched back to Java not that long ago to write a simple server using Jetty and even with things like Guice (best DI implementation I have used so far) and Guava it was still painful. Less painful, but I really felt that the compiler was fighting me from doing things in an elegant manner most of the time. Even adding the “var” keyword would improve Java in a massive way. Add some functional programming in there and I would be pretty happy.
I just wish C# would run on the JVM as I would use it for pretty much everything in a heartbeat. As it is the Mono support is missing the stuff I really want and isn’t as seamless as the experience should be. A pity really as C# really is in my experience the nicest language to work today that’s production ready.
