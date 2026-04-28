---
title: "Introducing RSC Explorer"
url: "https://overreacted.io/introducing-rsc-explorer/"
fetched_at: 2026-04-28T07:02:36.345108+00:00
source: "overreacted.io"
tags: [blog, raw]
---

# Introducing RSC Explorer

Source: https://overreacted.io/introducing-rsc-explorer/

In the past few weeks, since the disclosure of the
critical security vulnerability in React Server Components (RSC)
, there’s been a lot of interest in the RSC protocol.
The RSC protocol is the format in which React trees (and a
superset of JSON
) get serialized and deserialized by React. React provides both a writer and a reader for the RSC protocol, which are versioned and evolved in lockstep with each other.
Because the RSC protocol is an
implementation detail
of React, it is not explicitly documented outside the source code. The benefit of this approach is that React has a lot of leeway to improve the format and add new features and optimizations to it.
However, the downside is that even people who actively build apps with React Server Components often don’t have an intuition for how it works under the hood.
A few months ago, I wrote
Progressive JSON
to explain some of the ideas used by the RSC protocol. While you don’t “need” to know them to use RSC, I think it’s one of the cases where looking under the hood is actually quite fun and instructive.
I wish the circumstances around the increased interest now were different, but in any case,
that interest inspired me to make a new little tool
to show how it works.
I’m calling it
RSC Explorer
, and you can find it at
https://rscexplorer.dev/
.
Obviously, it’s
open
source
.
“Show, don’t tell”, as they say. Well, there it is as an embed.
Let’s start with the Hello World:
Notice there’s a yellow highlighted line that says something cryptic. If you look closely, it’s
<h1>Hello</h1>
represented as a piece of JSON. This line is a part of the RSC stream from the server.
That’s how React talks to itself over the network.
Now press the big yellow “step” button!
Notice how
<h1>Hello</h1>
now appears on the right. This is the JSX that the
client
reconstructs after reading this line. We’ve just seen a simple piece of JSX—the
<h1>Hello</h1>
tag—cross the network and get revived on the other side.
Well, not
really
“cross the network”.
One cool thing about RSC Explorer is that it’s a single-page app, i.e.
it runs entirely in your browser
(more precisely, the Server part runs in a worker). This is why, if you check the Network tab, you’ll see no requests. So in a sense it’s a simulation.
Nevertheless, RSC Explorer is built using exactly the same packages that React provides to read and write the RSC protocol, so every line of the output is real.
Let’s try something slightly more interesting to see
streaming
in action.
Take this example and press the big yellow “step” button
exactly two times:
(If you miscounted, press “restart” on the left, and then “step” two times again.)
Have a look at the upper right pane. You can see three chunks in the RSC protocol format (which, again, you don’t technically
need
to read—and which changes between versions). On the right, you see what Client React reconstructed
so far
.
Notice a “hole” in the middle of the streamed tree, visualized as a “Pending” pill.
By default, React would not show an inconsistent UI with “holes”. However, since you’ve declared a loading state with
<Suspense>
, a partially completed UI now can be displayed (notice how the
<h1>
is already visible but
<Suspense>
shows the fallback content because
<SlowComponent />
has not streamed in yet).
Press the “step” button once again, and the “hole” will be filled.
So far, we’ve only sent
data
to the client; now let’s also send some
code
.
Let’s use a counter as the classic example.
Press the big yellow “step” button twice:
That’s just a good old counter, nothing too interesting here.
Or is there?
Have a look at the protocol payload. It’s a bit tricky to read, but notice that we’re not sending the string
"Count: 0"
or the
<button>
s, or any HTML. We’re sending
<Counter initialCount={0} />
itself—the “virtual DOM”.
It can, of course, be turned to HTML later, just like any JSX can, but it doesn’t have to be.
It’s like we’re returning React trees from API routes.
Notice how the
Counter
reference becomes
["client",[],"Counter"]
in the RSC protocol, which says “grab the
Counter
export from the
client
module”. In a real framework, this would be done by the bundler, which is why RSC integrates with bundlers. If you’re familiar with webpack, this is similar to reading from the webpack require cache. (In fact,
that’s how
RSC Explorer implements that.)
We’ve just seen the server
referring
to a piece of code exposed by the client.
Now let’s see the client
referring
to a piece of code exposed by the server.
Here,
greet
is a
Server Action
, exposed with
'use server'
as an endpoint. It’s passed as a prop to the Client
Form
component that sees it as an
async
function.
Press the big yellow “step” button three times:
Now enter your name in the Preview pane and press “Greet”. The RSC Explorer debugger will “pause” again, showing we’ve hit the
greet
Server Action with a request. Press the yellow “step” button to see the response returned to the client.
RSC is often taught with a framework, but that obscures what’s happening. For example, how does a framework refresh server content? How does a router work?
RSC Explorer shows
frameworkless RSC.
There’s no
router.refresh
—but you can implement your own
refresh
Server Action and a
Router
Component.
Press the “step” button repeatedly to get the whole initial UI on the screen:
Look at the ticking timer. Notice how the
ColorTimer
component from the Server passed a random color to the
Timer
component on the Client. Again, the Server has
returned
<Timer color="hsl(96, 70%, 85%)" />
(or such).
Now press the Refresh button right above the timer.
Without digging into the code, “step” through the server response and see what happens. You should see a continously ticking
Timer
receive new props from the server
.
Its background color will change but its state will be preserved!
In a sense, it’s like refetching HTML using something like htmx, except it’s a normal React “virtual DOM” update, so it doesn’t destroy state. It’s just receiving new props… from the server. Press “Refresh” a few times and step through it.
If you want to look how this works under the hood, scroll down both Server and Client parts. In short, the Client
Router
keeps a Promise to the server JSX, which is returned by
renderPage()
. Initially,
renderPage()
is called on the Server (for the first render output), and later, it is called from the Client (for refetches).
This technique, combined with URL matching and nesting, is pretty much how RSC frameworks handle routing. I think that’s a pretty cool example!
I’ve made a few more examples for the curious folks:
And, of course, the infamous:
(As you would expect, this one only works on the vulnerable versions so you’d need to select 19.2.0 in the top right corner to actually get it to work.)
I’d love to see more cool RSC examples created by the community.
RSC Explorer lets you embed snippets on other pages (as I’ve done in this post) and create sharable links as long as the code itself is not bigger than the URL limit. The tool is entirely client-side and I intend to keep it that way for simplicity.
You’re more than welcome to browse its source code on
Tangled
or
GitHub
. This is a hobby project so I don’t promise anything specific but I hope it’s useful.
Thank you for checking it out!
