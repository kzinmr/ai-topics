---
title: "Securely indexing large codebases · Cursor"
source: "Cursor Blog"
url: "https://cursor.com/blog/secure-codebase-indexing"
scraped: "2026-05-10T01:19:42.257594+00:00"
lastmod: "2026-05-09T16:09:42.638Z"
type: "sitemap"
---

# Securely indexing large codebases · Cursor

**Source**: [https://cursor.com/blog/secure-codebase-indexing](https://cursor.com/blog/secure-codebase-indexing)

Blog
/
research
Jan 27, 2026
·
research
Securely indexing large codebases
Jeremy Stribling
·
6 min read
Table of Contents
↑
Building the first index
Finding the best index to reuse
Proving access
Faster onboarding
Semantic search is one of the biggest drivers of agent performance. In our
recent evaluation
, it improved response accuracy by 12.5% on average, produced code changes that were more likely to be retained in codebases, and raised overall request satisfaction.
To power semantic search, Cursor builds a searchable index of your codebase when you open a project. For small projects, this happens almost instantly. But large repositories with tens of thousands of files can take hours to process if indexed naively, and semantic search isn't available until at least 80% of that work is finished.
We looked for ways to speed up indexing based on the simple observation that most teams work from near-identical copies of the same codebase. In fact, clones of the same codebase average 92% similarity across users within an organization.
This means that rather than rebuilding every index from scratch when someone joins or switches machines, we can securely reuse a teammate's existing index. This cuts time-to-first-query from hours to seconds on the largest repos.
#
Building the first index
Cursor builds its first view of a codebase using a
Merkle tree
, which lets it detect exactly which files and directories have changed without reprocessing everything. The Merkle tree features a cryptographic hash of every file, along with hashes of each folder that are based on the hashes of its children.
Small client-side edits change only the hashes of the edited file itself and the hashes of the parent directories up to the root of the codebase. Cursor compares those hashes to the server's version to see exactly where the two Merkle trees diverge. Entries whose hashes differ get synced. Entries that match are skipped. Any entry missing on the client is deleted from the server, and any entry missing on the server is added. The sync process never modifies files on the client side.
The Merkle tree approach significantly reduces the amount of data that needs to be transferred on each sync. In a workspace with fifty thousand files, just the filenames and SHA-256 hashes add up to roughly 3.2 MB. Without the tree, you would move that data on every update. With the tree, Cursor walks only the branches where hashes differ.
When a file changes, Cursor splits it into syntactic chunks. These chunks are converted into the embeddings that enable semantic search. Creating embeddings is the expensive step, which is why Cursor does it asynchronously in the background.
Most edits leave most chunks unchanged. Cursor caches embeddings by chunk content. Unchanged chunks hit the cache, and agent responses stay fast without paying that cost again at inference time. The resulting index is fast to update and light to maintain.
#
Finding the best index to reuse
The indexing pipeline above uploads every file when a codebase is new to Cursor. New users inside an organization don't need to go through that entire process though.
When a new user joins, the client computes the Merkle tree for a new codebase and derives a value called a similarity hash (
simhash
) from that tree. This is a single value that acts as a summary of the file content hashes in the codebase.
The client uploads the simhash to the server. The server then uses it as a vector to search in a vector database composed of all the other current simhashes for all other indexes in Cursor in the same team (or from the same user) as the client. For each result returned by the vector database, we check whether it matches the client similarity hash above a threshold value. If it does, we use that index as the initial index for the new codebase.
This copy happens in the background. In the meantime, the client is allowed to make new semantic searches against the original index being copied, resulting in a very quick time-to-first-query for the client.
But this only works if two constraints hold. Results need to reflect the user's local codebase, even when it differs from the copied index. And the client can never see results for code it doesn't already have.
#
Proving access
To guarantee that files won't leak across copies of the codebase, we reuse the cryptographic properties of the Merkle tree.
Each node in the tree is a cryptographic hash of the content beneath it. You can only compute that hash if you have the file. When a workspace starts from a copied index, the client uploads its full Merkle tree along with the similarity hash. This associates a hash with each encrypted path in the codebase.
The server stores this tree as a set of content proofs. During search, the server filters results by checking those hashes against the client's tree. If the client can't prove it has a file, the result is dropped.
This allows the client to query immediately and see results only for code it shares with the copied index. The background sync reconciles the remaining differences. Once the client and server Merkle tree roots match, the server deletes the content proofs and future queries run against the fully synced index.
#
Faster onboarding
Reusing teammate indexes improves setup time for repos of all sizes. The effect compounds with the size of the repo:
For the median repo, time-to-first-query drops from 7.87 seconds to 525 milliseconds
At the 90th percentile it falls from 2.82 minutes to 1.87 seconds
At the 99th percentile it falls from 4.03 hours to 21 seconds.
These changes remove a major source of repeated work and let Cursor understand even very large codebases in seconds, not hours.
Filed under:
research
Author
:
Jeremy Stribling
