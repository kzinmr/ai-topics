---
title: "Why Does RSC Integrate with a Bundler?"
url: "https://overreacted.io/why-does-rsc-integrate-with-a-bundler/"
fetched_at: 2026-04-29T07:01:56.137829+00:00
source: "overreacted.io"
tags: [blog, raw]
---

# Why Does RSC Integrate with a Bundler?

Source: https://overreacted.io/why-does-rsc-integrate-with-a-bundler/

Fair warning—this one’s for the nerds.
React Server Components is a programming paradigm that
extends the module system
to express a server/client application as a single program spanning two runtimes. Under the hood, the RSC implementation consists of two main pieces:
The
react-server
and
react-client
packages are internal to the React repo.
They are fully open source, of course, but they don’t get published in their raw form to npm. This is because they’re missing a key ingredient—the module system integration. Unlike many (de)serializers, RSC concerns itself not only with sending
data
, but also with sending
code
. For example, consider this tree:
<
p
>
Hello, world
</
p
>
If you want to turn this
<p>
tag into JSON, you could do it like this:
{
type:
'
p
'
,
props:
{
children:
'
Hello world
'
}
}
But now consider this
<Counter>
tag. How do you serialize it?
import
{
Counter
}
from
'
./client
'
;
<
Counter
initialCount={
10
} />
'
use client
'
;
import
{
useState
,
useEffect
}
from
'
react
'
;
export
function
Counter
(
{ initialCount }
)
{
const [
count
,
setCount
]
=
useState
(
initialCount
);
// ...
}
How does one serialize a
module?
Recall that we want to revive an actual
<Counter>
on the other side of the wire—so we don’t just want a snapshot of it. We want its entire logic for interactivity!
One way to serialize it is to literally embed the
Counter
code into our JSON:
{
type:
`
import { useState, useEffect } from 'react';
export function Counter({ initialCount }) {
const [count, setCount] = useState(initialCount);
// ...
}
`
,
props:
{
initialCount:
10
}
}
But that’s kind of bad, right? You don’t
really
want to send code as strings to
eval
on the client, and you don’t want to send the same component’s code many times. So instead it’s reasonable to assume its code is being served by our app as a static JS asset—which we can refer to in the JSON. It’s almost like a
<script>
tag:
{
type:
'
/src/client.js#Counter
'
,
// "Load src/client.js and grab Counter"
props:
{
initialCount:
10
}
}
In fact, on the client, you could load it
by
generating a
<script>
tag.
However, loading imports one by one from their source files over the network is inefficient. Recall that one file can import other files, and the client doesn’t know the import tree in advance. You don’t want to create a waterfall. We already know how to fix this from two decades of working on client-side applications: bundling.
For this reason, RSC integrates with bundlers. RSC doesn’t require a bundler
per se
: here’s a
bundler-less RSC ESM proof of concept
. But it exists mostly for posterity because of how inefficient it actually is to do naïvely without more optimizations.
Realistic RSC integrations are bundler-specific. Bindings for
Parcel
,
Webpack
, and (eventually)
Vite
live in the React repo and specify how to send and load modules:
First,
during the build,
their job is to find the files with
'use client'
and to actually create the bundle chunks for those entry points—a bit like
Astro Islands
.
Then,
on the server,
these bindings teach React how to send modules to the client. For example, a bundler might refer to a module like
'chunk123.js#Counter'
.
On the client,
they teach React how to ask the bundler runtime to load those modules. For example, the Parcel bindings
call a Parcel-specific function
for that.
Thanks to these three things, React Server will know how to serialize a module when it encounters one—and the React Client will know how to deserialize it.
The API to serialize a tree with the React Server is exposed
via
bundler bindings:
import
{
serialize
}
from
'
react-server-dom-yourbundler
'
;
// Bundler-specific package
const
reactTree
=
<
Counter
initialCount={
10
} />;
const
outputString
=
serialize
(
reactTree
);
// Something like the JSON above
Then one can store the
outputString
on the disk, or send it over the network, or cache it, whatever—and eventually feed it to the React Client. The React Client will deserialize the entire tree, loading code from the referenced modules as needed:
import
{
deserialize
}
from
'
react-server-dom-yourbundler/client
'
;
// Bundler-specific package
const
outputString
=
// ... received over network, read from disk, etc...
const
reactTree
=
deserialize
(
outputString
);
// <Counter initialCount={10} />
And that, assuming everything worked correctly, will give you a normal piece of JSX, as if you wrote
<Counter initialCount={10} />
on the client yourself. You can do anything with that tree—render it, keep it in state, turn into HTML, etc.
const
outputString
=
// ... received over network, read from disk, etc...
const
reactTree
=
deserialize
(
outputString
);
// <Counter initialCount={10} />
// You can do anything you'd do with a regular JSX tree, for example:
const
root
=
createRoot
(
domNode
);
root
.
render
(
reactTree
);
That’s the APIs that RSC frameworks like Next.js use under the hood.
If you want to play with RSC using these lower-level APIs and see your React trees getting (de)serialized, the
Parcel RSC implementation
is a good starting point.
(The
serialize
and
deserialize
names above are illustrative. The exact names are up to the bindings (and may have multiple overloads). For example,
@parcel/rsc
package, which is a thin wrapper over the underlying
react-server-dom-parcel
bindings, exposes serialization as
renderRSC
and deserialization as
fetchRSC
. Also, their actual implementations are non-blocking and support streaming on both sides.)
