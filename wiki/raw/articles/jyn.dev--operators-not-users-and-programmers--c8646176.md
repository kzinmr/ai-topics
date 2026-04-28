---
title: "operators, not users and programmers"
url: "https://jyn.dev/operators-not-users-and-programmers/"
fetched_at: 2026-04-28T07:02:50.794903+00:00
source: "jyn.dev"
tags: [blog, raw]
---

# operators, not users and programmers

Source: https://jyn.dev/operators-not-users-and-programmers/

the modern distinction between “programmers” and “users” is evil and destroys agency.
consider how the spreadsheets grow
spreadsheets are hugely successful. Felienne Hermans, who has spent her career studying spreadsheets,
attributes this success
to "
their immediate feedback system and their continuous deployment model
": the spreadsheet shows you its result as soon as you open it, and it requires no steps to run other than to install Excel and double-click the file.
Rik calls Excel “malleable software” and the resulting programs
“vine-like systems”
:
The dream of malleable software is that we can enlarge the space of possibilities, users can enjoy more freedom and get more out of their software, without having to rely on software developers to provide it for them.
i would go one step further: the dream of malleable software is to unify users and programmers, such that there are just “operators” of a computer, and “writing a program” doesn’t sound any harder than “writing a resume”:
the distinction between "user" and "programmer" is an artifact of our presently barely-programmable and barely-usable computing systems.  I would like to use the neutral word "operator" instead.
Stanislav
this is a relatively new distinction! if we look at the history of computing and of programming languages, we see very different patterns:
In the 1960’s the supply of programmers was not very deep so IBM and other companies trying to gain a computer sale would often have to sell the business prospect on the idea of creating its own programmer(s). Sometimes it was the shipping clerk; sometimes it was the head order taker; sometimes it was a bookkeeper, and sometimes it was a woman or man packing items in the warehouse.
Brian M. Kelly, The AS/400 and IBM i RPG Programming Guide
this is what i want: for programming to be easy and simple enough to pick up that people can do it without specialized training in the field, so that they can write
situated software
.
the “user/programmer” distinction
contrast malleable software to the systems that programmers often build:
Many, many technologists have taken one look at an existing workflow of spreadsheets, reacted with performative disgust, and proposed the trifecta of microservices, Kubernetes and something called a "service mesh".
This kind of Big Enterprise technology however takes away that basic agency of those Excel users, who no longer understand the business process they run and now have to negotiate with
ludicrous technology dweebs
for each software change. The previous pliability of the spreadsheets has been completely lost.
Cal Peterson
now, this doesn’t happen because programmers are stupid and evil. it happens because the systems we build are amenable to all the features that programmers
take for granted
:
distributed version control systems (VCS)
automated testing (when integrated with a VCS, often called "continuous integration")
gradual controlled rollouts (when integrated with a VCS, often called "continuous deployment")
what i want to imagine is what it would look like to build computing systems that have those features and are also malleable.
what could a malleable system with
low technical risk
look like?
let's start by looking at what malleable systems already exist.
malleable languages
spreadsheets, as previously discussed
WYSIWYG editors: Microsoft Word, Obsidian, Typst, Wordpress. In Word, and in Obsidian's default view, the compile step is completely hidden and it appears to the user as if the source and rendered view are the same. in other editors, the rendered view updates quickly and frequently enough that they get immediate feedback, just like a spreadsheet.
browser devtools, where editing an element in the inspector immediately updates the rendered view
sonic-pi
, where editing code live-updates the sound played
my blog
note these aren't
just
hot-patching, where you edit a system while it's running. hot-patching is certainly useful and i would like to see more of it, but it doesn't unify the source and rendered version of a program, you still have to trip the condition in order to observe the change. malleable languages are a combination of:
hot-patching
live previews that makes updates appear instant
undo/redo for the whole system
malleable version control
file shares: google drive; sharepoint; onedrive; etc. the tooling for diffing and reverting is very primitive compared to git or hg (in particular diffing is the responsibility of the application, not the VCS), but the primitives are there.
Bank Python
, where the distinction between local and persisted storage is smoothed over by the runtime
note a pattern here: these don't require prior approval in order to use. anyone can throw a file into google drive and hit share without prior approval (sometimes this is frowned upon, in which case it gets called "Shadow IT").
malleable deployment
Bank Python's
vouch system
, where hitting "approve" insta-deploys to prod. at a technical level this is basically the same as code review, but unlike normal CI systems it’s not configured to require tests to pass, because anything that’s too annoying will end up with people bypassing the system to build shadow IT.
unfortunately i am not aware of a malleable testing system—if you know of one, please do
tell me
!
putting it together
so, we want the following from a malleable system:
hot-reloading and live previews, like spreadsheets
in particular, we want the user to write in the representation that makes the most sense to them, whether that's a spreadsheet or an SQL query or a text editor of markup
automatic and continuous durability
, like autosave in microsoft office products.
in particular this undo/redo capability works on the whole system including derived data, not just the source code itself, so you can try new things without fear of breaking everything. the closest programmers have to this today is
jj
, which
automatically snapshots the working tree
, but taking snapshots still requires a manual action, and you need to set up the system in advance.
distributed version control++
with unrestricted
distribution
and an easy interface, like google drive and dropbox
with diffing/merging/reverting, like traditional VCS
automated and instantly triggered testing, like piper at google. this could run your tests in the background as you edit your program, with integrated build caching so that only the affected tests rerun.
continuous deployment
we want explicit approval and controlled rollout, like traditional CD, so we can separate "upload the code" from "run the code in prod"
but we want it to be trivially easy to give that approval, like double-clicking an email attachment or the vouch system. don't confuse "controlled rollout" with access control—it's useful even if you're a solo programmer.
and of course, performance.
this is a tall order! the rest of this series is dedicated to ideas about how to make this possible.
bibliography
P.S: what will people build with this power?
i consulted a local friend of mine, a polisci major, and asked him what he would build if he were able to program. he said a penguin that walks across the screen, followed by a puffin friend for him. so, here's to penguins 🐧
