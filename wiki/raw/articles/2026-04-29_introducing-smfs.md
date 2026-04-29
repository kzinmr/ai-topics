---
title: "Introducing SMFS - RAG sucks and filesystems are broken. We fixed both with supermemory filesystems."
type: x-article
date: 2026-04-28
source: twitter
tweet_id: 2049324612635562492
author: supermemory
url: https://x.com/i/article/2049324612635562492
bookmark_count: see_metadata
---

# Introducing SMFS - RAG sucks and filesystems are broken. We fixed both with supermemory filesystems.

Everyone and their mom is arguing about "RAG is dead" and "filesystems are awesome", without capturing the full nuance.
TLDR: We brought the best of RAG and filesystem into a mountable filesystem which replaces the UNIX operations and makes them better for agents. it's called Supermemory Filesystem (SMFS.ai) 
https://github.com/supermemoryai/smfs
RAG isn't dead. With better agents, managing embeddings and vector databases just became too much of a pain. MCP and grep seemed to make "fancy retrieval" unnecessary. Claude Code popularized agentic search - letting the agent walk a codebase with grep and find... and it worked! Very well!
And yeah, agentic search on a filesystem is a simply beautiful paradigm. You throw in some files and let the agent look around.
It works because codebases are special. Filenames mean what they say. Function names are designed to be searchable. The whole tree was organized by humans(or agents) who knew an agent would walk it later.
Your notes folder is not a codebase. Drop a thousand PDFs, meeting transcripts, and design docs in there and watch it fall apart. Filenames stop being signposts. The agent greps for "OAuth refresh failure" and misses the doc that calls it "token rotation issue." It can't grep a diagram inside a PDF at all.
So, you reach for RAG. Top-K returns chunks - relevant, severed from the files they came from - leading to subpar answers. What do you do now? You stitch together many systems, trying to make it better one step at a time.
What if you didn't have to choose? Introducing SMFS: Supermemory Filesystem.
We made a mountable filesystem that our agent can use to do semantic search while also just... dealing with files.
Still simply beautiful, but with steroids.
1/ Semantic grep
What if grep itself was semantic? What if the agent didn't have to learn seperate tool calls like "search vectors" etc.? Agents are already great at filesystems, so what if the filesystem ITSELF could be made for the agent?
Same command, same line-oriented output, same muscle memory, but the matching function underneath is a vector query, scoped to the path you're standing in. Results land back on real paths. The agent cats the file. Lists the directory. Re-greps with a narrower scope.
The index and the file tree. both. It can do whatever it needs to do.
 
Flagged grep -F stays literal. grep without flags is semantic. Same muscle memory. New reach.
2/ User profiles
𝚌𝚊𝚝 𝚙𝚛𝚘𝚏𝚒𝚕𝚎.𝚖𝚍 returns a live digest of every memory in the container. Not stored - synthesized on read and always fresh. The agent's first useful action in a new directory is usually a read. We made that read free.
We keep it fresh because the profile is actually derived from the graph. if a fact updates in the supermemory graph, it automatically updates in the profile.
3/ Sync engine
Multiple agents can mount the same container. Agent A writes a memory. Agent B sees it on the next pull. The folder is the shared state, always synced with supermemory cloud.
This also means that the operations themselves are instant, in a local sqlite state, and can incrementally synchronize with the system.
4/ Auto extraction: Drop the file. We'll do the rest.
PDFs, videos, screenshots, audio, docs — drop the raw files straight into the mount. No OCR. No transcription. No PDF parser. No chunking. The pipeline you would have built is gone, and grep works across every format.
yes, so your agent can now grep through files as well. 
$ grep "action items" ~/smfs/
contract.pdf      ...follow-up action items due Friday
standup.mp4       [02:14] action items from yesterday
screenshot.png    [OCR] Action Items (whiteboard)
handbook.docx     §4 tracking action items effectively
interview.m4a     [8:02] emerging action items for Q1
The numbers
We ran 20 real retrieval tasks with Claude and Codex. Same agent, same documents, with and without SMFS:
 
We asked coding harnesses to do retrieval tasks across large a corpus. with SMFS, agents used significantly less time and latency!
Codex: 1.2M → 203K tokens (-83%). Answer found 19/20 times
Claude: 116 → 42 tool calls (-64%). Tokens -36%. Answer found 16/20 → 18/20 with smfs.
Less context, more right answers, fewer turns. The agent stops walking the tree speculatively and starts asking the right question, directly
We are working on a larger report which will be published soon on smfs.ai, it almost always beats agentic search by >50% in our internal benchmarks!
A few details we sweated.
One binary. Open source. Built with rust btw.
No kernel extensions. FUSE on Linux. NFSv3 on macOS via a pure-Rust localhost server, mounted natively. No macFUSE. No kext. No security prompts. Shows up in Finder. 
Works with Daytona, E2b, Cloudflare, vercel, and pretty much all sandboxes.
Local-first sync. Reads never block on the network. Writes commit to a local SQLite cache and drain to Supermemory in the background with exponential backoff. Survives restarts. Offline reads keep working. Your edits don't get lost.
Same surface, every runtime. Your laptop, an ephemeral sandbox, a serverless edge runtime with no kernel — there's a virtual-bash SDK that exposes the same Unix surface as a single tool the agent can call.
 
You get the index. You get the map.
Just try it! or view our demo at smfs.ai 
And star the repo! github.com/supermemoryai/smfs we'd love to see what you build 🫶
