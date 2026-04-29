---
title: "Writing an LLM from scratch, part 33 -- what I learned from finally getting round to the appendices"
url: "https://www.gilesthomas.com/2026/04/llm-from-scratch-33-what-i-learned-from-the-appendices"
fetched_at: 2026-04-29T07:02:03.304434+00:00
source: "gilesthomas.com"
tags: [blog, raw]
---

# Writing an LLM from scratch, part 33 -- what I learned from finally getting round to the appendices

Source: https://www.gilesthomas.com/2026/04/llm-from-scratch-33-what-i-learned-from-the-appendices

Archives
Categories
Blogroll
After finishing the main body of
"
Build a Large Language Model (from Scratch)
",
I
set myself three follow-on goals
.
The first was training a full GPT-2-small-style base model myself.  That was
reasonably easy to do
but unlocked a
bunch of irresistible side quests
;
having finally got to the end of those, it's time to move on to the others: reading
through the book's appendices, and building my own GPT-2 style model in JAX.
This post is about the appendices.  The TL;DR: there was stuff in there that could have saved me time
in my side-questing, but I think that having to work those things out from scratch probably
helped me learn them better.
Appendix A: Introduction to PyTorch
This is an excellent overview of PyTorch, and given that I'm writing for people
who are reading the book too, all I can really say is that it's well worth reading,
even if you have some experience in it.  He gives an intro to what it is, some details
on how to choose to use GPUs (or Apple Silicon) if you have them, and an overview of tensors.
He then goes on to explain the basics of automated differentiation and back-propagation,
with a bit of background detail about the chain rule.  I think this bit is useful at a
"how-to" level, but the mathematical details felt like they were summarised too briefly
to be all that useful.  I can see why -- this is an appendix to a book on an adjacent
subject, not a textbook on the mathematics of training ML models.  But something this
brief feels like it would be confusing for people who don't know it already, but not
really useful for those that do.
Perhaps I'm underestimating the typical reader, but if and when I write up my own
explanation of how this works (perhaps as a follow-up to
"
The maths you need to start understanding LLMs
"), I'll
go quite a lot slower and try to explain things in more detail.
Anyway, as I said, the explanation is more of a bonus in this book, quite
far from its main focus, so this is a nit.
He then goes on to a high-level explanation of PyTorch's
Dataset
s and
DataLoader
s.
This was quite useful for me.  I must admit that I've been struggling a bit to see
the value of DataLoaders -- indexing directly into Datasets has worked very nicely
for me.  I suspect this is a question of scale more than anything; even my big
training runs, 44 hours of training a 163M-parameter model on 3 billion tokens, worked
fine without a DataLoader.  But after reading this section, I felt I was getting
some way towards having more of a handle on how they might help.  I'm not quite
there yet, but hopefully soon...
Next, there are sections on training loops, both with and without GPU support.  Nothing
new there for me, at least.
Then came the real surprise: a really solid walkthrough on training models across
multiple GPUs with DistributedDataParallel!  That's something I learned from the documentation
and various online tutorials
back in January
,
and reading this appendix first would have saved some time.
But thinking back on it, I think that the way I did it was better pedagogically for
me.  By having to grind through it from first principles -- following the docs, coding
something, seeing it break, trying again, and eventually getting there -- I think
I internalised the knowledge much better.
It's a balance, really.  If I read explanations, I learn faster, but
the knowledge is shallower.  Learning by doing is slower but deeper.  Working out
a good balance is hard.  It feels like I've struck a good balance on this one, but
I suppose it's difficult to know for sure.
The one thing in the DDP section that did stand out for me, though, was the use of a
DistributedSampler
for the
DataLoader
.  That might have made some of my DDP code
a bit simpler!
On to the next appendix.
Appendix B: References and further reading
I won't go through this in detail; it does what it says on the tin, and there's
a bunch of interesting stuff in there.  I scanned through and nothing felt like
a must-read right now, but I'll be checking it in the future if I'm looking for
suggestions for things to read about.
Appendix C: Exercise solutions
Another one that is exactly what it says it is.
Appendix D: Adding bells and whistles to the training loop
Once again, something I could have saved time by reading first!  In it, he covers
gradient clipping, which I went over back
in February
,
and warming up and then doing a cosine decay on the learning rate, which was something
I looked into
in March
.
Just like with DDP, I think that having to learn about these from resources I could
find on the Internet meant that I got to a deeper understanding than I would have if
I'd just been following the book.  This is not a point against the book, of course!
Again, it's one of those balancing acts: do it yourself and learn more, or read about
it and learn faster.
Still well worth reading though.
Appendix E: Parameter-efficient fine-tuning with LoRA
This was a really interesting read.  I've been reading about LoRA on the side, but
most treatments I've seen started with an explanation of the maths, but then essentially
said "now, to do it, install PEFT" (or Unsloth, or something similar).
Raschka gives the full code, showing how you can write your own LoRA stuff, and I
think this is excellent.  Digging into it right now would be a side quest, but I'm
inspired by it and might do my own LoRA writeup after finishing this LLM from scratch arc.
Let's see if I manage that or if I get distracted by something shiny first...
...and that's it!
The last page in the book.  Well, the first page of the index.  Done.  Wow!
But before I start the celebrations, there's one last step.  As I said
last November
, I wanted to:
[Build] my own LLM from scratch in a different framework,
  without using the book. That is, I think, essential, and perhaps would be the
  crowning post of this series. It would be a nice way to end it, wouldn't it?
I think I was right, so that's what's next.  I
asked people on Twitter
which
framework I should use, and the winner was JAX -- and so that's what's coming next.
Watch this space!
