---
title: "Importing a frontend Javascript library without a build system"
url: "https://jvns.ca/blog/2024/11/18/how-to-import-a-javascript-library/"
fetched_at: 2026-05-05T07:01:46.962283+00:00
source: "Julia Evans (jvns)"
tags: [blog, raw]
---

# Importing a frontend Javascript library without a build system

Source: https://jvns.ca/blog/2024/11/18/how-to-import-a-javascript-library/

I like writing Javascript
without a build system
and for the millionth time yesterday I ran into a problem where I needed to
figure out how to import a Javascript library in my code without using a build
system, and it took FOREVER to figure out how to import it because the
library’s setup instructions assume that you’re using a build system.
Luckily at this point I’ve mostly learned how to navigate this situation and
either successfully use the library or decide it’s too difficult and switch to
a different library, so here’s the guide I wish I had to importing Javascript
libraries years ago.
I’m only going to talk about using Javacript libraries on the frontend, and
only about how to use them in a no-build-system setup.
In this post I’m going to talk about:
the three main types of Javascript files a library might provide (ES Modules, the “classic” global variable kind, and CommonJS)
how to figure out which types of files a Javascript library includes in its build
ways to import each type of file in your code
There are 3 basic types of Javascript files a library can provide:
the “classic” type of file that defines a global variable. This is the kind
of file that you can just
<script src>
and it’ll Just Work. Great if you
can get it but not always available
an ES module (which may or may not depend on other files, we’ll get to that)
a “CommonJS” module. This is for Node, you can’t use it in a browser at all
without using a build system.
I’m not sure if there’s a better name for the “classic” type but I’m just going
to call it “classic”. Also there’s a type called “AMD” but I’m not sure how
relevant it is in 2024.
Now that we know the 3 types of files, let’s talk about how to figure out which
of these the library actually provides!
Every Javascript library has a
build
which it uploads to NPM. You might be
thinking (like I did originally) – Julia! The whole POINT is that we’re not
using Node to build our library! Why are we talking about NPM?
But if you’re using a link from a CDN like
https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.min.js
,
you’re still using the NPM build! All the files on the CDNs originally come
from NPM.
Because of this, I sometimes like to
npm install
the library even if I’m not
planning to use Node to build my library at all – I’ll just create a new temp
folder,
npm install
there, and then delete it when I’m done. I like being able to poke
around in the files in the NPM build on my filesystem, because then I can be
100% sure that I’m seeing everything that the library is making available in
its build and that the CDN isn’t hiding something from me.
So let’s
npm install
a few libraries and try to figure out what types of
Javascript files they provide in their builds!
First let’s look inside
Chart.js
, a plotting library.
$ cd /tmp/whatever
$ npm install chart.js
$ cd node_modules/chart.js/dist
$ ls *.*js
chart.cjs  chart.js  chart.umd.js  helpers.cjs  helpers.js
This library seems to have 3 basic options:
option 1:
chart.cjs
. The
.cjs
suffix tells me that this is a
CommonJS
file
, for using in Node. This means it’s impossible to use it directly in the
browser without some kind of build step.
option 2:
chart.js
. The
.js
suffix by itself doesn’t tell us what kind of
file it is, but if I open it up, I see
import '@kurkle/color';
which is an
immediate sign that this is an ES module – the
import ...
syntax is ES
module syntax.
option 3:
chart.umd.js
. “UMD” stands for “Universal Module Definition”,
which I think means that you can use this file either with a basic
<script src>
, CommonJS,
or some third thing called AMD that I don’t understand.
When I was using Chart.js I picked Option 3. I just needed to add this to my
code:
<script src="./chart.umd.js"> </script>
and then I could use the library with the global
Chart
environment variable.
Couldn’t be easier. I just copied
chart.umd.js
into my Git repository so that
I didn’t have to worry about using NPM or the CDNs going down or anything.
A lot of libraries will put their build in the
dist
directory, but not
always! The build files’ location is specified in the library’s
package.json
.
For example here’s an excerpt from Chart.js’s
package.json
.
"jsdelivr": "./dist/chart.umd.js",
  "unpkg": "./dist/chart.umd.js",
  "main": "./dist/chart.cjs",
  "module": "./dist/chart.js",
I think this is saying that if you want to use an ES Module (
module
) you
should use
dist/chart.js
, but the jsDelivr and unpkg CDNs should use
./dist/chart.umd.js
. I guess
main
is for Node.
chart.js
’s
package.json
also says
"type": "module"
, which
according to this documentation
tells Node to treat files as ES modules by default. I think it doesn’t tell us
specifically which files are ES modules and which ones aren’t but it does tell
us that
something
in there is an ES module.
@atcute/oauth-browser-client
is a library for logging into Bluesky with OAuth in the browser.
Let’s see what kinds of Javascript files it provides in its build!
$ npm install @atcute/oauth-browser-client
$ cd node_modules/@atcute/oauth-browser-client/dist
$ ls *js
constants.js  dpop.js  environment.js  errors.js  index.js  resolvers.js
It seems like the only plausible root file in here is
index.js
, which looks
something like this:
export { configureOAuth } from './environment.js';
export * from './errors.js';
export * from './resolvers.js';
This
export
syntax means it’s an
ES module
. That means we can use it in
the browser without a build step! Let’s see how to do that.
Using an ES module isn’t an easy as just adding a
<script src="whatever.js">
. Instead, if
the ES module has dependencies (like
@atcute/oauth-browser-client
does) the
steps are:
Set up an import map in your HTML
Put import statements like
import { configureOAuth } from '@atcute/oauth-browser-client';
in your JS code
Include your JS code in your HTML like this:
<script type="module" src="YOURSCRIPT.js"></script>
The reason we need an import map instead of just doing something like
import { BrowserOAuthClient } from "./oauth-client-browser.js"
is that internally the module has more import statements like
import {something} from @atcute/client
, and we need to tell the browser where to get the code for
@atcute/client
and all of its other dependencies.
Here’s what the importmap I used looks like for
@atcute/oauth-browser-client
:
<script type="importmap">
{
  "imports": {
    "nanoid": "./node_modules/nanoid/bin/dist/index.js",
    "nanoid/non-secure": "./node_modules/nanoid/non-secure/index.js",
    "nanoid/url-alphabet": "./node_modules/nanoid/url-alphabet/dist/index.js",
    "@atcute/oauth-browser-client": "./node_modules/@atcute/oauth-browser-client/dist/index.js",
    "@atcute/client": "./node_modules/@atcute/client/dist/index.js",
    "@atcute/client/utils/did": "./node_modules/@atcute/client/dist/utils/did.js"
  }
}
</script>
Getting these import maps to work is pretty fiddly, I feel like there must be a
tool to generate them automatically but I haven’t found one yet. It’s definitely possible to
write a script that automatically generates the importmaps using
esbuild’s metafile
but I haven’t done that and
maybe there’s a better way.
I decided to set up importmaps yesterday to get
github.com/jvns/bsky-oauth-example
to work, so there’s some example code in that repo.
Also someone pointed me to Simon Willison’s
download-esm
, which will
download an ES module and rewrite the imports to point to the JS files directly
so that you don’t need importmaps. I haven’t tried it yet but it seems like a
great idea.
I did run into some problems with using importmaps in the browser though – it
needed to download dozens of Javascript files to load my site, and my webserver
in development couldn’t keep up for some reason. I kept seeing files fail to
load randomly and then had to reload the page and hope that they would succeed
this time.
It wasn’t an issue anymore when I deployed my site to production, so I guess it
was a problem with my local dev environment.
Also one slightly annoying thing about ES modules in general is that you need to
be running a webserver to use them, I’m sure this is for a good reason but it’s
easier when you can just open your
index.html
file without starting a
webserver.
Because of the “too many files” thing I think actually using ES modules with
importmaps in this way isn’t actually that appealing to me, but it’s good to
know it’s possible.
If the ES module doesn’t have dependencies then it’s even easier – you don’t
need the importmaps! You can just:
put
<script type="module" src="YOURCODE.js"></script>
in your HTML. The
type="module"
is important.
put
import {whatever} from "https://example.com/whatever.js"
in
YOURCODE.js
If you don’t want to use importmaps, you can also use a build system like
esbuild
. I talked about how to do
that in
Some notes on using esbuild
, but this blog post is
about ways to avoid build systems completely so I’m not going to talk about
that option here. I do still like esbuild though and I think it’s a good option
in this case.
CanIUse
says that importmaps are in
“Baseline 2023: newly available across major browsers” so my sense is that in
2024 that’s still maybe a little bit too new? I think I would use importmaps
for some fun experimental code that I only wanted like myself and 12 people to
use, but if I wanted my code to be more widely usable I’d use
esbuild
instead.
Let’s look at one final example library! This is a different Bluesky auth
library than
@atcute/oauth-browser-client
.
$ npm install @atproto/oauth-client-browser
$ cd node_modules/@atproto/oauth-client-browser/dist
$ ls *js
browser-oauth-client.js  browser-oauth-database.js  browser-runtime-implementation.js  errors.js  index.js  indexed-db-store.js  util.js
Again, it seems like only real candidate file here is
index.js
. But this is a
different situation from the previous example library! Let’s take a look at
index.js
:
There’s a bunch of stuff like this in
index.js
:
__exportStar(require("@atproto/oauth-client"), exports);
__exportStar(require("./browser-oauth-client.js"), exports);
__exportStar(require("./errors.js"), exports);
var util_js_1 = require("./util.js");
This
require()
syntax is CommonJS syntax, which means that we can’t use this
file in the browser at all, we need to use some kind of build step, and
ESBuild won’t work either.
Also in this library’s
package.json
it says
"type": "commonjs"
which is
another way to tell it’s CommonJS.
Originally I thought it was impossible to use CommonJS modules without learning
a build system, but then someone Bluesky told me about
esm.sh
! It’s a CDN that will translate anything into an ES
Module.
skypack.dev
does something similar, I’m not
sure what the difference is but one person mentioned that if one doesn’t work
sometimes they’ll try the other one.
For
@atproto/oauth-client-browser
using it seems pretty simple, I just need to put this in my HTML:
<script type="module" src="script.js"> </script>
and then put this in
script.js
.
import { BrowserOAuthClient } from "https://esm.sh/@atproto/oauth-client-browser@0.3.0"
It seems to Just Work, which is cool! Of course this is still sort of using a
build system – it’s just that esm.sh is running the build instead of me. My
main concerns with this approach are:
I don’t really trust CDNs to keep working forever – usually I like to copy dependencies into my repository so that they don’t go away for some reason in the future.
I’ve heard of some issues with CDNs having security compromises which scares me.
I don’t really understand what esm.sh is doing.
I also learned that you can also use
esbuild
to convert a CommonJS module
into an ES module, though there are some limitations – the
import { BrowserOAuthClient } from
syntax doesn’t work. Here’s a
github issue about that
.
I think the
esbuild
approach is probably more appealing to me than the
esm.sh
approach because it’s a tool that I already have on my computer so I
trust it more. I haven’t experimented with this much yet though.
Here’s a summary of the three types of JS files you might encounter, options
for how to use them, and how to identify them.
Unhelpfully a
.js
or
.min.js
file extension could be any of these 3
options, so if the file is
something.js
you need to do more detective work to
figure out what you’re dealing with.
“classic” JS files
How to use it:
:
<script src="whatever.js"></script>
Ways to identify it:
The website has a big friendly banner in its setup instructions saying “Use this with a CDN!”  or something
A
.umd.js
extension
Just try to put it in a
<script src=...
tag and see if it works
ES Modules
Ways to use it:
If there are no dependencies, just
import {whatever} from "./my-module.js"
directly in your code
If there are dependencies, create an importmap and
import {whatever} from "my-module"
Use
esbuild
or any ES Module bundler
Ways to identify it:
Look for an
import
or
export
statement. (not
module.exports = ...
, that’s CommonJS)
An
.mjs
extension
maybe
"type": "module"
in
package.json
(though it’s not clear to me which file exactly this refers to)
CommonJS Modules
Ways to use it:
Use
https://esm.sh
to convert it into an ES module, like
https://esm.sh/@atproto/oauth-client-browser@0.3.0
Use a build somehow (??)
Ways to identify it:
Look for
require()
or
module.exports = ...
in the code
A
.cjs
extension
maybe
"type": "commonjs"
in
package.json
(though it’s not clear to me which file exactly this refers to)
The main difference between CommonJS modules and ES modules from my perspective
is that ES modules are actually a standard. This makes me feel a lot more
confident using them, because browsers commit to backwards compatibility for
web standards forever – if I write some code using ES modules today, I can
feel sure that it’ll still work the same way in 15 years.
It also makes me feel better about using tooling like
esbuild
because even if
the esbuild project dies, because it’s implementing a standard it feels likely
that there will be another similar tool in the future that I can replace it
with.
A lot of the time when I talk about this stuff I get responses like “I hate
javascript!!! it’s the worst!!!”. But my experience is that there are a lot of great tools for Javascript
(I just learned about
https://esm.sh
yesterday which seems great! I love
esbuild!), and that if I take the time to learn how things works I can take
advantage of some of those tools and make my life a lot easier.
So the goal of this post is definitely not to complain about Javascript, it’s
to understand the landscape so I can use the tooling in a way that feels good
to me.
Here are some questions I still have, I’ll add the answers into the post if I
learn the answer.
Is there a tool that automatically generates importmaps for an ES Module that
I have set up locally? (apparently yes:
jspm
)
How can I convert a CommonJS module into an ES module on my computer, the way
https://esm.sh
does? (apparently esbuild can sort of do this, though
named exports don’t work
)
When people normally build CommonJS modules into regular JS code, what’s code is
doing that? Obviously there are tools like webpack, rollup, esbuild, etc, but
do those tools all implement their own JS parsers/static analysis? How many
JS parsers are there out there?
Is there any way to bundle an ES module into a single file (like
atcute-client.js
), but so that in the browser I can still import multiple
different paths from that file (like both
@atcute/client/lexicons
and
@atcute/client
)?
Here’s a list of every tool we talked about in this post:
Writing this post has made me think that even though I usually don’t want to
have a build that I run every time I update the project, I might be willing to
have a build step (using
download-esm
or something) that I run
only once
when setting up the project and never run again except maybe if I’m updating my
dependency versions.
Thanks to
Marco Rogers
who taught me a lot of the things
in this post. I’ve probably made some mistakes in this post and I’d love to
know what they are – let me know on Bluesky or Mastodon!
