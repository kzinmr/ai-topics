---
title: "Alternatives for the EDIT tool of LLM agents"
url: "http://antirez.com/news/166"
fetched_at: 2026-05-20T07:00:51.177657+00:00
source: "antirez.com"
tags: [blog, raw]
---

# Alternatives for the EDIT tool of LLM agents

Source: http://antirez.com/news/166

antirez
23 hours ago. 7768 views.
EDIT: of course this was already done in the past! I had little doubts but people just confirmed me about it on Twitter :) But, keep reading: the CRC32 compromise at the end is an interesting tradeoff, and this is a good discussion to have in general.

Right now I'm working to an agent for my DS4 project. Local inference is token-poor, it's a battlefield where optimizations count. I was quite surprised by the fact the EDIT tool everybody is using right now forces the LLM to emit the old version of the text verbatim. This CAS (check and set) mode of operation, where I say EDIT old="foo" new="bar", is needed because there are often colliding edits (the user is editing as well, or checked out a different branch, and so forth) and because the LLM can just hallucinate that a given line had a given content.

This means, basically, that just using line numbers is very fragile: to say, change line 22 with new="foobar" is not good. Yet I don't want my local LLM to throw away tokens rewriting the old text each time, also because certain times the old text has a lot of special chars and spaces that the model may get wrong; in this case the tool would fail, forcing the LLM to do the same edit again. So I (re)designed a tag-based EDIT tool that is still CAS style, but more tokens efficient.

The READ and SEARCH tools return something like that:

  10:Q8fA int count = 10;
  11:rA3_ if (count > limit) {
  12:Kq9z     count = limit;
  13:PX0b }

So there are line numbers and tags. The tag is 4 chars, on average 2.5 LLM tokens, representing a checksum of the line. Now the LLM can edit like this:

  {
    "tool": "edit",
    "path": "/tmp/example.c",
    "line": 10,
    "tag": "Q8fA",
    "new": "int count = 11;"
  }

Or, multi line, like this:

  {
    "tool": "edit",
    "path": "/tmp/example.c",
    "lines": "11:rA3_\n12:Kq9z\n13:PX0b",
    "new": "if (count > limit)\n    return limit;"
  }

The saving is significant especially when the agent is deleting big amounts of text, but also in the general case. However, there is some overhead due to the fact we have line numbers and tags. There are potential tradeoffs, maybe the tag should be 8 chars and include the line number in the hash, there is to check exactly collisions possibilities and tokenization to see how much this is a win, but I like the line:tag format as later the LLM is often able to exploit the line information in many ways, like to get ranges in successive tool calls. Maybe there are other ways to exploit the tag, too, like: is this line still dj4_?

The interesting thing is that DeepSeek v4 Flash is able to use this tool in a very effective way, so apparently it is natural for it. And while I did't measure the exact savings I saw in the field that edits are much faster and even more reliable.

The alternative to this is to return just the whole file CRC32 each time (basically the tag becomes a file tag, even for partial reads). So that we can only work with line numbers + CRC, the edit would just specify 11,12,13,14. Less tokens, of course. This forces, however, to recompute the CRC32 of the file each time, but for reasonably sized files this is cheap enough. But this approach has limits: we fail the edit even if *unrelated* changes happened, so there is a strong tradeoff at play. To be fair to the whole file method, there is to say that it allows to specify ranges as 10:23, which is a huge win.

I have the feeling I can decide which is better only with enough practical evidence, by using ds4-agent over multiple sessions with the two systems. For now maybe a command line to switch the edit mode is the first right step to do.
