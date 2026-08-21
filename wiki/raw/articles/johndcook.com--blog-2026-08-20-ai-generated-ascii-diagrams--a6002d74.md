---
title: "AI-generated ASCII diagrams"
url: "https://www.johndcook.com/blog/2026/08/20/ai-generated-ascii-diagrams/"
fetched_at: 2026-08-21T10:01:06.746157+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# AI-generated ASCII diagrams

Source: https://www.johndcook.com/blog/2026/08/20/ai-generated-ascii-diagrams/

I like AI-generated ASCII diagrams. Because nobody would ask AI to generate ASCII diagrams, and so, it’s congruous. I like incongruity [1].
Aside from the incongruity of using a gazillion-parameter neural network to make 1970’s style ASCII art, ASCII diagrams have some uses. They’re absolutely tiny compared to image files. But more importantly they can be inserted into plain text files, such as source code or markdown. A diagram embedded directly into a source file cannot become separated from the code.
ASCII diagrams are tedious to create, though there are
tools
to mitigate the tedium. But if an AI can generate the diagram, the tedium goes away.
I was curious how well Claude could create ASCII diagrams, so I tried a few examples. I hope these render well in whatever format you’re reading this post. They look fine for me previewing the post in a browser. I expect they might not turn out so well in an RSS reader.
I asked it to reproduce the graphs from my recently post on the
graph imbalance theorem
and the first diagram turned out nicely.
+-------+                                +-------+
                 |   A   |--------------------------------|   B   |
                 +-------+                                +-------+
                     |                                        |
                     |                                        |
   ------------------|------------------             ---------|---------
   |        |        |        |        |             |        |        |
   |        |        |        |        |             |        |        |
+-----+  +-----+  +-----+  +-----+  +-----+       +-----+  +-----+  +-----+
| a0  |  | a1  |  | a2  |  | a3  |  | a4  |       | b0  |  | b1  |  | b2  |
+-----+  +-----+  +-----+  +-----+  +-----+       +-----+  +-----+  +-----+
The second network is more complicated and so the corresponding ASCII diagram is hard to read.
+----------------------------------------------------------------+
   |                                                                |
   |+-----------------------------------------------+               |
   ||                                               |               |
   ||+-------------------------------+              |               |
  +-------+       +-------+       +-------+       +-------+       +-------+
  |  R1   |-------|  R2   |-------|  R3   |-------|  R4   |-------|  R5   |
  +-------+       +-------+       +-------+       +-------+       +-------+
      |             | | |          |   |           |   |           |  |  |
     ++             | | |          |   |           |   |           |  |  |
     | +---------------------------+   |           |   |           |  |  |
     | |            ++| |              |           |   |           |  |  |
     | |             || +--------------+           |   |           |  |  |
     | |             || |  +---------------------------------------+  |  |
     | |             |+-|--|-------------+         |   |              |  |
     | |             |  |  |             |  +------+   |              |  |
     | |             |  |  |             |  |  +----------------------+  |
     | |             |  +--|-------------|--|--|-------------+           |
     | |             |  |  |             |  |  |       +-----|--+        |
     | |             |  |  |             |  |  |             |  |  +-----+
     | |             |  |  |             |  |  |             |  |  |
  +-------+         +-------+           +-------+           +-------+
  |  G1   |         |  B1   |           |  B2   |           |  B3   |
  +-------+         +-------+           +-------+           +-------+
For a third example, here is a fairly complicated diagram that nevertheless lends itself to a readable ASCII diagram. It’s a
Feistel network
diagram for DES encryption.
+-------------+                    +-------------+
   |   L(i-1)    |                    |   R(i-1)    |--------
   +-------------+                    +-------------+       |
          |                                  |              |
          |                                  |              |
          |                      +-----------------------+  |
          |                      |   E (expand 32->48)   |  |
          |                      +-----------------------+  |
          |                                  |              |
          |                      +-----------------------+  |
          |                      |     XOR with K(i)     |  |
          |                      +-----------------------+  |
          |                                  |              |
          |                      +-----------------------+  |
          |                      |    S-boxes S1..S8     |  |
          |                      +-----------------------+  |
          |                                  |              |
          |                      +-----------------------+  |
          |                      |    P (permutation)    |  |
          |                      +-----------------------+  |
          |                                  |              |
          |                                  |              |
          |            +-------+             |              |
          +------------|  XOR  |-------------+              |
                       +-------+                            |
                           |                                |
          +----------------|--------------------------------+
          |                +------------------+
          |                                   |
   +-------------+                    +-------------+
   |    L(i)     |                    |    R(i)     |
   +-------------+                    +-------------+
Related posts
[1] See Christian Wolff’s discussion of dogs playing poker in The Accountant (2016).
