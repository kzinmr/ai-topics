---
title: "A curmudgeon tries a language server"
url: "https://entropicthoughts.com/curmudgeon-tries-language-server"
fetched_at: 2026-08-25T10:01:28.316269+00:00
source: "entropicthoughts.com"
tags: [blog, raw]
---

# A curmudgeon tries a language server

Source: https://entropicthoughts.com/curmudgeon-tries-language-server

One of the drawbacks of using
ghc
i (and consequently
ghc
id) for live reload
is that
ghc
i can only track one set of source files at a time. This means that
if the project is properly set up with distinct components for executable,
library, and test code,
ghc
i can only reload one of those components. To apply
changes to any of the other components, the entire
ghc
i process must be
restarted.
Since part of the intended workflow was being able to edit both tests and
program code and reload both, we are forced to co-locate all the code into one
component. This is a non-starter for serious projects, but acceptable for the
kind of toy project I was aiming for – and maybe even for the early evolutionary
stages of experiments where this workflow is most powerful.
The code for the part that live-reloads ends up looking something like this,
with comments explaining the mechanism.
In[1]:
module
Main
(main)
where
import
Control.Concurrent
import
Control.Concurrent.Async
import
Control.Exception
(bracketOnError)
import
Data.IORef
import
Foreign.Store
import
Test.Hspec
(describe, hspec, it)
import
Test.Hspec.QuickCheck
(prop)
--
The main function runs on reload, and has the
--
effect of first running the tests. If they
--
succeed, it runs the update function which makes
--
sure to restart the processing thread while
--
reusing resources.
main
::
IO
()
main
=
do
spec
  update
--
Unit tests in a mix of example-based and property
--
tests. These are written instead of poking about
--
in the REPL.
spec
::
IO
()
spec
=
hspec
$
do
describe
"forward euler solution"
$
do
prop
"ever increases with example study"
$
\
x y
->
--
...
--
A function that must start our process if it is
--
not running, or restart it (and reuse its
--
resources) if it is running.
update
::
IO
()
update
=
let
--
This contains an MVar with the resources
--
needed to run SDL. It also serves as a lock
--
that prevents multiple processes from running
--
simultaneously.
resourceStore
=
Store
0
--
This contains the Async of the process thread,
--
for cancelling during an update.
asyncStore
=
Store
1
--
Wait for resources to be available, reserve
--
them, and start a new thread that uses them.
withResources action
=
do
withStore resourceStore
$
\
resources
->
async
$
--
Catch async exceptions during execution,
--
such as when this thread is cancelled by
--
the update procedure. The exception
--
already causes the action function to stop
--
running, so then we release its resources.
bracketOnError
          (putStrLn
"Running action."
>>
takeMVar resources)
          (
\
res
->
putStrLn
"Action interrupted!"
>>
putMVar resources res)
          action

    start
=
do
--
Waits for resources and then runs the render
--
loop with them.
withResources
$
\
(window, renderer, texture)
->
do
renderLoop renderer texture (
State
study
Nothing
)
        putStrLn
"Render loop exited naturally."
--
Getting here in the control flow means the
--
render loop terminated but not through an
--
async exception. That implies the user
--
requested an exit, e.g. by closing the
--
window. Thus we should destroy resources
--
rather than release them back for reuse.
destroySdl window renderer texture
--
We also need to delete all stores so the
--
next time the update function is called,
--
it sees a blank slate and recreates
--
everything all over.
deleteStore asyncStore
        deleteStore resourceStore
in
do
lookupStore (
case
asyncStore
of
Store
i
->
i)
>>=
\
case
Nothing
->
do
--
If the thread id store does not exist, it
--
means we're starting from a blank slate.
--
We should initialise resources fresh and
--
start a new thread to use them.
initialiseSdl
>>=
void
.
storeAction (
Store
0)
.
newMVar
        start
>>=
void
.
storeAction (
Store
1)
.
newIORef
Just
tidStore
->
--
If the thread id store exists, we cancel
--
the thread its referencing, which will
--
return the resources it used, and then we
--
start a new thread. The new thread picks
--
whatever resources were in store.
withStore tidStore
$
\
ref
->
do
readIORef ref
>>=
cancel
          start
>>=
writeIORef ref
I initially tried using the higher-level Rapid library for this, but I couldn’t
get it to work properly. I found it much easier to get stability, resource
clean-up, and support for stdout in all sub-processes when I implemented the
plumbing myself with
IORef
s and
Async
.
The following invocation launches
ghc
id in a way that automatically reloads
and runs the development main function:
In[2]:
ghcid --command
"cabal repl --repl-options='-fobject-code -ferror-spans -fdiagnostics-color=always'"
\
--reverse-errors
\
--reload src
\
--restart diffeq.cabal
\
--test Main
This is the result of accretion-by-confusion. I couldn’t get something to work,
so I tried another command line argument, and that happened a few times in a
row. This is probably not the ideal way to write this command, but it seems to
work and for now I want to play around with it and see how convenient it is,
before I spend more time on it.
However, at first I couldn’t get this to work at all. The
ghc
id process
started all right, but it didn’t reload when code changed. It didn’t tell me why
either. I actually gave up on using
ghc
id because I couldn’t get it to work,
and then by accident I ran this command in a Nix development shell and it
worked. I have no idea what’s going on. I thought
direnv
would make it
unnecessary for me to first start a Nix development shell, but in this case it
seems not.
So far I really like the
ghc
id-and-foreign-store experience for this type of
programming. Instead of creating a complicated
gui
for defining differential
equations and initial conditions and whatnot, I can change constants in the code
and the visualisation updates. When I learn new things in the book I’m reading,
I can add code for them and the visualisation updates.
