---
title: "Shrinking a Fedora virtual disk"
url: "https://entropicthoughts.com/shrinking-fedora-virtual-disk"
fetched_at: 2026-09-25T10:01:25.944561+00:00
source: "entropicthoughts.com"
tags: [blog, raw]
---

# Shrinking a Fedora virtual disk

Source: https://entropicthoughts.com/shrinking-fedora-virtual-disk

Fortunately, Btrfs makes it really easy to shrink a file system. The command is
In[1]:
sudo btrfs filesystem resize 150G /
and it will move Btrfs
chunks
from outside the first 150
gb
into that space,
and then truncate the size of the file system.
Un
fortunately, chunks are
typically 1
gb
each, so if there are more than 150 chunks used in the
filesystem, the command will fail due to lack of space. The upside is that it
fails safe, so we can just try it and see if it works.
If it fails, the solution is to consolidate chunks. In my case, I started with
290
gb
of data on a file system that was 300
gb
in size. This means Btrfs
likely used all of 300 chunks to store this data, and the chunks were on average
290/300=96 % used. After cleaning, when there were only 90
gb
of data left,
Btrfs would still have used the same 300 chunks, but they would only have been
90/300=30 % used on average. These chunks can be consolidated into, say,
120 chunks at 75 % utilisation instead, which would fit into a file system of
150
gb
.
A command like
In[2]:
sudo btrfs balance start -dusage=50 -musage=50 /
will aggressively consolidate chunks. It will find chunks that are at less than
50 % utilisation (counting either data or metadata), and create new chunks to
hold the data from multiple such under-utilised chunks. If there’s not enough
space to create new chunks, this command can fail (safely). If it fails, we can
perform the consolidation in stages.
14
Why doesn’t Btrfs do this on its own? I
have no idea.
First we delete any chunks that are completely unused.
In[3]:
sudo btrfs balance start -dusage=0 /
Then we can move data from chunks that are less than 5 % filled.
In[4]:
sudo btrfs balance start -dusage=5 /
The data from chunks that are less than 5 % filled is so little data
15
A few
times 50
mb
at worst.
Btrfs can probably sweep all of it up from the entire
disk and put it into one new chunk.
16
Maybe Btrfs can even move this data into
existing chunks? I’m not fully sure how the balancing algorithm works.
This
means we free up multiple chunks at the cost of just one additional chunk.
Then we move data from chunks that are 20 % used or less.
In[5]:
sudo btrfs balance start -dusage=20 /
This probably requires creating multiple new chunks to store the data, but in
the previous command we
just
liberated that capacity, so it has a better
chance of succeeding now. This should free up a good number of additional
chunks.
Then we try the first
balance
command again to perform a final pass, combining
all chunks that are at 50 % utilisation or lower. If we have significantly less
data than the size we’re trying to resize the file system to, this final
consolidation pass should have freed up enough space for the
resize
command to
complete.
We are now at a point where the Linux disk usage can’t grow beyond where a
second copy of the Linux disk is possible. But we haven’t seen any of this space
saving on the physical disk yet, because the virtual disk file is still
290
gb
.
