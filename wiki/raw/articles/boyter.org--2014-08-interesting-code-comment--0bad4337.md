---
title: "Interesting Code Comment"
url: "https://boyter.org/2014/08/interesting-code-comment/"
fetched_at: 2026-05-05T07:02:03.098921+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Interesting Code Comment

Source: https://boyter.org/2014/08/interesting-code-comment/

Interesting Code Comment
2014/08/11
(281 words)
Found the following comment in some code I had modified a few years ago.
Just to set this up, its an existing application I had no hand in creating, and is a totally atrocity of 180,000 lines of untested code (and pretty much un-testable) which through the abuse of extension methods lives in a single class spread out across multiple files.
/*
This is evil but necessary. For some reason people have put validation rules here rather then in the bloody ValidationHelper. Thanks to their incompetence or genius... we now have no idea if we add the extra validation in the correct place and call it here if it will work. Since this is also 180,000 lines of non tested nor testable code (without refactoring) I have no confidence in making any changes. Sure we have subversion but that dosnt allow us to code fearlessly ripping apart methods and refactoring since we have no test safety net.

I guess the obligatory car analogy would be driving down the highway, carrying nuclear waste, in an open container, in a snow storm, with acid/lsd/ice fueled drugie ninja bikies attacking you, while on fire, while juggling chainsaws, and all of a sudden you need to change the tyre. So much is going on that its you dont want to risk it and then when forced to do so
you know its going to end up badly.

If you are still reading this then for the love of all things holy, help by refacting stuff so we can test it properly. The DAO layer should be fairly simple but everthing else is a shambles.

Rant time over. Lets commit sin by adding more validation.
*/
