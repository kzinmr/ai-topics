---
source_url: https://layerfs.ai/
ingested: 2026-10-22
sha256: 4993975af2a6e165
---

LayerFS: the filesystem for AI coding agents

Layer
FS

v1.0.0 
→

releases

Docs

Arch

Architecture

Bench

Benchmarks

Blog

Docs

Architecture

Benchmarks

Blog

Releases 
v1.0.0

GitHub

+1

+1

+1

+1

+1

+1

+1

+1

+1

+1

+1

+1

+1

+1

Ephemerality: scaling multi-agent development beyond imagination

Ephemeral Workspaces.

Durable Shared History.

LayerFS is the substrate under your agents. Each one mounts a complete, writable Workspace over shared committed history, does its work, commits what it changed, and goes away.

GET STARTED

WATCH VIDEO

TRY IT LIVE ↓

Ephemeral workspaces

Durable results

Massive parallelism

LayerFS

×

and

DSH

Copy to play with LayerFS on DSH

LayerFS

×

and

Pi

soon

CLOSE 
✕

Why LayerFS

Ten ideas, one filesystem.

six core · four supporting

Ephemeral Computing

01 →

Compute exists only while a command runs.

fs · atomic write → Store

write

edit

rm

sandbox · workspace per bash

mount

exec

commit

unmount

mount

exec

commit

unmount

mount

exec

commit

unmount

mount

exec

commit

unmount

mount

exec

commit

unmount

>_ mkdir out

>_ cat log.txt

>_ python train.py

>_ node build.js

UpToDate

Store

C41

C42

C43

C44

C45

C46

Compute:
 Agents spend ~80% thinking, ~10% in Bash.

FS:
 Each file tool call is one atomic Store op.

Sandbox:
 Each Bash tool call mounts an ephemeral workspace, then commits.

Decentralized Agents

02 →

Agents on different computers share one serverless Store.

store.db

C41

C42

C43

C44

C45

C46

C47

computer 1

computer 2

computer 3

computer 4

Shared storage:
 Every agent commits to one Store, with no DB server.

Distributed computing:
 Each agent runs on its own computer.

Multiagent Coordination

03 →

One project, many branches. One branch, many agents.

main

auth

ui

login.ts

api.ts

session.ts

app.tsx

token.ts

app.tsx

nav.tsx

Conflict: app.tsx

app.tsx · merge markers

<<<<<<< head C44

 <Cart />

=======

 <Search />

>>>>>>> workspace

blame app.tsx

C12

import Nav

C44

<Header />

C44

<Cart />

C46

<Search />

L3 · publish

L4 · publish

Commits:
 Every tool call is a commit on its branch.

Conflict:
 A same-file clash is refused with Conflict.

Blame:
 Each line names the step that wrote it.

Recursive Filesystem

04 →

Fork recursively any commit, at any depth.

publish

0.62

0.48

0.21

0.40

0.78

0.66

0.30

0.71

0.91

0.69

pruned

pruned

pruned

pruned

pruned

★ best 0.91

explorers ×3

explorers ×3

explorers ×4

explorers ×3

explorers ×1

fork: no files copied

Zero cost:
 A fork is metadata and copies no files.

Recursive:
 A filesystem for RSI agents and recursive exploration for RL training.

Ultra Storage Optimization

05 →

10 copies compress into 0.31.

commits

1 · dedupe

12 chunks

13 chunks

14 chunks

15 chunks

11 matched
 · 
+1 new

11 matched
 · 
+1 new

11 matched
 · 
+1 new

dedup → ≈1.05 copies

→

2 · compress

≈0.31 copies

illustrative · store.stats

Dedup:
 Each content chunk is stored once.

Compression:
 The stored chunks shrink further.

Ratio:
 10 copies → 1.05 dedup → 0.31 compression wtf???

Instant Bootstrap

06 →

Dependencies come with every mount. No wasting time for re-installation.

1 · git / other AgentFS without .gitignore files

oops!

src/

package.json

.git/

node_modules/

node_modules/

.cache/

.cache/

$ npm test

✗ Error: Cannot find module 'react'

$ npm install

$ npm test

✓ passed

⏱ 0:05

⏱ 0:20

⏱ 1:00

⏱ 2:00

⏱ 3:00

⏱ 4:00

⏱ 5:00

⏱ ≈5 min before the first run

clone + install, typical

⚠ wasting time · waiting on install

⌛

2 · LayerFS

npm install committed once, back then (C12)

src/

package.json

.git/

node_modules/

.cache/

$ mount → workspace ready

$ npm test

✓ passed

instant · no install

⚡ mount 0.05 s

measured mounts: 5–20 ms

⚡

⚡ ready the moment it mounts

Git / other AgentFS:
 Drops ignored files; reinstalls.

LayerFS:
 Ignored files stay in every commit.

Comparison:
 ~5 min to install vs 0.05 s to mount.

Four supporting ideas

Auto Checkpoints

07 →

Every step an agent takes is a checkpoint to return to.

Every call:
 Each file call is a commit; each Bash call commits when it ends.

No noise:
 A call that changes nothing commits nothing.

Rewind:
 Fork from any checkpoint and read any file as it was.

Append-only Objects

08 →

Saved objects are never rewritten. The Store only grows.

Content-addressed:
 An object is named by the hash of its bytes.

Sealed:
 A written pack is never updated or deleted.

Safe to share:
 Branches share objects; readers never wait for the writer.

Conflict Rules (.lww)

09 →

Name the files that should never conflict. The newest edit wins.

/.lww:
 Gitignore-style rules at the root of the tree.

Newer wins:
 A matched file changed on both sides takes the newer edit.

For:
 Lockfiles, build output and caches.

Big File, Small Edit

10 →

An edit costs the size of the edit, not the size of the file.

Overlay:
 A write keeps only the bytes it wrote.

Commit:
 Only the edited extents and their tree path are rebuilt.

Storage:
 The rest of the file is shared with its old version.

Agent tool calls and their history

History

Terminals

HISTORY

main @ L0

0 commits · 0 live

Upright

Sideways

0:05

0:10

0:15

0:20

now

L0

main · show every Branch

main

main is the green middle bough; each publish adds a Layer band

Layer · a band on main

Commit · a leaf

Branch · a bough

merge · grafts back

publish · adds a band

stopped · bare twig

click a name tag to focus its Branch

main
read-only

1×

2×

5×

10×

sandboxes

0

0 workspaces mounted

12 idle

no Branch yet · the orchestrator forks one from main

unassigned

store.stats

main · read-only

dedupe

1.5×

compression

3.32×

stored

9.4 MB

file

10.0 MB

logical 
48.0 MB
 · canonical 
31.2 MB
 · 
metadata
 420 KB · free 180 KB · 0 commits · 1 layers

orchestrator

project · branch

LayerFS

project · branch

Layer
FS

Docs

Architecture

Benchmarks

Blog

Releases 
v1.0.0

GitHub