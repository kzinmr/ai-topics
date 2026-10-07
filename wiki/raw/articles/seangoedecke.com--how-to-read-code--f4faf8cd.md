---
title: "How to read code"
url: "https://seangoedecke.com/how-to-read-code/"
fetched_at: 2026-10-07T10:01:27.336866+00:00
source: "seangoedecke.com"
tags: [blog, raw]
---

# How to read code

Source: https://seangoedecke.com/how-to-read-code/

Everyone knows how to read a book. Beginning at the first page, you read each word in order
, stopping periodically to think, until you arrive at the last word on the last page. That’s how you read a newspaper article, or a poem, or an email. Why would reading code be any different?
Why code is different
English text is designed to be read in order. In fact, there are almost no constraints on the order of a text aside from how you want the reader to consume it. In writing this post, I could put the ideas I want to convey in any order I like. Code, on the other hand, is designed to be
run
by a computer. The order is thus primarily determined by non-human factors. I cannot simply move
a line of code to the beginning of a file or function because I think it provides a better introduction to the program for human readers.
The other big difference is that English text is always read as a final product, while code is usually read as a
diff
. We software engineers spend most of our time reading subtle changes to existing code, not brand-new programs. Imagine if reading this post was like that. You would read each successive draft in the order I wrote them, consuming the post as a changed sentence here and a new sentence there. It would be easy to lose track of the overall flow.
The third reason — and I say this as a lover of literature and poetry — is that code is much more structurally complex than English texts. Even famously difficult books are
syntactically
simpler than most computer programs (for instance, grammatical dependencies are largely bounded by a single paragraph, while code dependencies can stretch across the entire codebase). Their primary difficulty lies in understanding the nuances of human nature being discussed, not in understanding what each word’s grammatical function is
. Large codebases are also just longer:
War and Peace
contains around 600,000 words, while most large modern codebases have that many
lines
.
People are bad at reading code
As I’ve said
many
times
, large computer programs are simply too complex for a single person to fully understand. Reading code in a large program is thus a process of
compromise
: of deciding which parts to thoroughly grasp and which parts to gloss over; or of portioning out your finite mental capacity across the codebase.
Because of all this,
most people read code very badly
. They struggle through it front-to-back, like a book, and lose track of the execution flow. Or they just read through the diff and miss the significance of un-edited parts of the code
. Or they simply are defeated by the complexity, give up and just guess what it means. How can you do better?
How I read code
The best article I’ve read about reading code is
this piece
about reading mathematics papers, which have a similar structure. The author describes a technique called “dyadic scanning”. Instead of reading slowly and sequentially, you make several passes: first to figure out the overall structure, then the sub-structure, and then finally the details.
For code
, this means reading out-of-order. I like to pick an important path (say, the happy path for the feature introduced in the diff) and trace through which functions are calling which other functions, just to get a sense of the flow. Only once I’ve got a good sense of that do I pay close attention to what those functions are actually doing.
Usually I do multiple passes, each following a different thread. I’ll take a function or a piece of data and try to figure out how it’s used, fanning out to multiple call-sites (including ones outside the diff) as I go. For small diffs, I just ctrl+f for the function name to jump around; for large diffs, I open it in-editor and ctrl+click for easier navigation. I try to be ruthlessly focused on just the thing I’m looking at right now: everything else gets treated as a black box.
Once I’m confident I understand the diff, only then will I sit down and carefully read it end-to-end. The purpose of that read is less to learn about the structure — which I should already know by this point — than to catch any weird bits of code I hadn’t noticed in previous out-of-order passes. If I do see anything unusual, I then go back to doing passes.
This might sound slow. But in fact each pass is very fast, since I’m not painstakingly puzzling through each line of code.
Can’t AI just do it for you?
Many people are now saying that you don’t have to read code anymore: either because LLMs now produce reliably high-quality code without oversight, or because you can simply ask a reviewer LLM to read the code for you. I think both of these ideas are false.
Obviously the quality of LLM code is context-dependent. As I wrote in
Pure and impure software engineering
, some software fields (game development, libraries, tools like databases) have wildly different engineering standards, practices and values to other software fields (say, distributed systems at big tech companies). If you’re just making a tool for yourself, you probably don’t have to read the code if you don’t want to. But having read a bunch of AI-generated code this year, I can say that you definitely still have to read it.
I
routinely
find massive errors in AI-generated code. These are not bugs — the code typically does what the AI wanted it to do — so much as they’re problems of
alignment
. As a recent example, a small change to thread an extra value through some existing code ballooned out into a complex three-thousand-line diff, because the agent noticed a race condition and built a complex machinery to “fix” it. In fact, this race condition was harmless by design: two pieces of unrelated data could become briefly out of sync, with no customer impact.
Can LLMs just read the code for you? No, for the same reason: even if they make no mistakes, their technical values will not match yours or those of your company. You can still use LLMs to help you read code, but you have to carefully read and review that LLM output, and you should also be carefully reading the code itself.
Here's a preview of a related post that shares tags with this one.
