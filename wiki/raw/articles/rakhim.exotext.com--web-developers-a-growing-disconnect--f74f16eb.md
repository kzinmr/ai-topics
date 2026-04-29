---
title: "How do you do, fellow web developers? A growing disconnect."
url: "https://rakhim.exotext.com/web-developers-a-growing-disconnect"
fetched_at: 2026-04-29T07:01:21.381867+00:00
source: "rakhim.exotext.com"
tags: [blog, raw]
---

# How do you do, fellow web developers? A growing disconnect.

Source: https://rakhim.exotext.com/web-developers-a-growing-disconnect

I had a "woah" moment once when one programmer got genuinely baffled about the fact that a website somehow "erases" the history of requests from the Network tab of Chrome DevTools. He was wondering what magic method was used to hide the communication. He hadn't realized the app was not a single-page JS application (SPA), and he actually
wasn't aware
there is another way to make web apps. The idea that each click actually makes the browser fetch a completely new page, without any JS involved, was alien to him.
I feel a growing disconnect between my notion of programming and the younger web developers' notion of it. I promise, this isn't a get-off-my-lawn post.
I'm not that old (right?..), 36 as of today, and have been programming since 11. My first lines of code were written on a 80286 16-bit machine (there weren't too many modern computers in our small town at the time). So, there are full-time developers today who had started their journeys after I had a few years of dabbling in code. There are young devs who were born when I was 18 and had a few part-time jobs done.
There's been a lot of talk about modern programmers not knowing how fast computers are (
Do you know how much your computer can do in a second?
,
Jon Blow's rant
,
Casey Muratori: How fast should an unoptimized terminal run?
). There are so many levels of rich abstractions on top of hardware and even the OS kernel, one can make some arguments to justify the obliviousness of someone who needs to develop a product feature in some web shop. I'm not talking about this today, but I do want to talk about abstraction levels. My growing feeling of disconnect gets fueled mostly by seemingly
shifting
notions. Some examples I've heard are people saying "vanilla JS" when talking about Node, or saying "JS without frameworks" when talking about React. The "woah" moment from the first paragraph is another example.
Today I watched the
pilot episode of Leet Heat
, a game show for developers. It's cool! I enjoyed watching it, but at the same time it refueled this feeling of disconnect. First, it's meant for
developers
, not just web developers. But the categories are:
Web standards
Typescript
Frameworks
Databases
Computer Science
You can guess that Frameworks is only about front-end web frameworks like React and Vue, and databases is about some unspecified SQL format and also Mongo. And then there's Computer Science. One of the questions there was:
What's the main difference between
Array.map()
and
Array.foreach()
a) Map returns a new array, foreach doesn't
b) Foreach is faster than map
c) Map only works with numeric values
d) There is no difference
This feels like a very JavaScript question... Sure,
map
is a generic kind of operation, but
foreach
and the kinds of answers are just assuming JS.
Another question in Computer Science was "What's the output of this code?":
const
p =
new
Promise
(
(
resolve, reject
) =>
{
resolve
(
1
);
resolve
(
2
);
reject
(
3
);
    }
);

p.
then
(
console
.
log
).
catch
(
console
.
log
);
But how is this computer science? Perhaps this is an example of shifting notions I was talking about. "Pure JS", as well as abstract logic of resolution of non-trivial promises in TypeScript is such a niche, low-level concept, that it's treated as the science of computation.
The question is presented on the screen in form of a screenshot from JetBrains IDE:
Notice the hints in grey boxes: they are not part of the code, but a feature of the IDE. So we aren't even looking at code, we're looking at its enhanced representation.
One can argue that any programming is computer science, and yes, sure, but by this logic the topic shouldn't even be among the categories. Web standards is also computer science. It's a game show for
web-developers
developers
computer scientists.
Another Computer Science question was:
Which method removes and returns the last element of an array?
I mean, sure, this is a fun game show where people eat spicy food for entertainment. It's probably not representative of job interviews or the way people think about programming. But I don't know, maybe it is? Again, I'm not bashing them for making it, nor am I trying to be the "um, ackchyually" guy. These are anthropological observations if you will.
I've always felt safety in coding. It was a comfortably logical, deterministic, and beautifully consistent refuge from the world of vague and ambagious reality. I also felt certain kinship to other programmers, it was my tribe. So I'm worried about this feeling of disconnect, a little bit. I don't want to become an old man yelling at cloud. What worries me even more is that when I see a similar sentiment in comments (HN, Reddit, etc.) and blogs, very often it goes way overboard, and I feel a disconnect toward that side, too. Someone would grumpily bash "stupid JS frameworks" and "bootcamp devs", while religiously proclaiming how everybody should just use bash and vim, or something.
It's all pretty fascinating.
Discussions:
