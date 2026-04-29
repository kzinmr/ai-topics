---
title: "Writing a good design document"
url: "https://grantslatton.com/how-to-design-document"
fetched_at: 2026-04-29T07:02:16.525061+00:00
source: "grantslatton.com"
tags: [blog, raw]
---

# Writing a good design document

Source: https://grantslatton.com/how-to-design-document

How to write a good design document
This essay is a version of
the response
I gave to my friend Vik's call for suggestions:
Definition
A design document is a technical report that outlines the implementation strategy of a system in the context of trade-offs and constraints.
Goal
Think of a design document like a proof in mathematics. The goal of a proof is to convince the reader that the theorem is true. The goal of a design document is to convince the reader the design is optimal given the situation.
The most important person to convince is
the author
. The act of writing a design document helps to add rigor to what are otherwise vague intuitions. Writing reveals how sloppy your thinking was (and later, code will show how sloppy your writing was).
Organization
Good design document organization is as important as code organization. You probably have opinions about code organization. You've probably used the phrase "spaghetti code" to describe poorly-organized code. Most programmers write "spaghetti design docs" unless they've had a lot of practice.
Let me illustrate a common code organization issue some programmers run into on their first day. The novice writes
terminal
.
print
(
"
Hello world
"
)
Then they decide they want to make the text red, so they edit their program to
terminal
.
print
(
"
Hello world
"
)
terminal
.
setPrintColor
(
"
red
"
)
And then they're confused that it didn't come out red. They haven't internalized that the first line of code
happens before
the second. They just get a soup of code on the screen that kind of has the ingredients for a program, and expect the computer to do what they want.
Novice document writers make the
exact
same mistake, but with prose instead of code. They get a soup of sentences and paragraphs and expect the reader's brain to do what they want.
If the reader is smart enough, you might actually get away with this. Just like an expert programmer can mentally untangle spaghetti code.
But a perfect doc is written such that the reader
is never surprised
. The reader should find that every sentence flows obviously from the previous ones. They should finish your doc and think "well this was entirely straightforward, why did we even need to have this meeting?".
This disappoints the ego-seeking behavior of many engineers. Good engineers often want people to realize how clever they were.
But a good doc will lay out the problem and mental models in a way that the solution that took weeks of hard thought to invent will be clear to the reader by the time the doc presents it.
This also requires having a good model of the minds of the people reading your doc. The goal of your doc is to take their minds from their current state to a new state in which they believe your design is a good one.
You should anticipate every objection someone would have and preemptively show why it's invalid, so that the reader never even thinks to bring it up.
Many engineers fail at modeling the starting state of their readers' minds, so fail at getting them to the destination state.
Editing
Once you've got the information organized and laid out properly, the next step is to edit for length. Remove every word that can be removed. Do this because your readers' attention is a scarce resource.
Unless you're an unusually terse writer, you can almost always cut length by ~30% from the first draft without sacrificing information.
The easiest way to get good at editing by going through
other
people's docs with a red pen and crossing out unnecessary words. You'll find tons. It's easier to criticize other people.
Once you've built this muscle, you can turn the weapon on yourself. Distilling thoughts to fit into the 280 character tweet limit is also surprisingly good practice.
Volume
There's no substitute for lots of practice. I'm grateful for having worked at AWS with a unique doc-writing culture. The first docs I wrote there were terrible, but after a few hundred, I like to think they were pretty good.
For unfamiliar readers: Amazon meetings start with the presenter passing out copies (historically physical, though increasingly digital since Covid) of a prose document. The document is 1-6 pages depending on the importance.
The meeting starts with everyone sitting in silence, reading the document, and adding notes and questions in the margins with red pen. Watching people mark up the document you spent so much time polishing is a
strong
forcing function to become a better writer.
Concrete tips
These work for me, but they may not work for you.
Use short paragraphs
You should think of your doc as a series of bullet points that flow into each other. That is, a doc might be organized like:
Observation A
Observation B
Because B, idea C
But problems D and E
Observation F
Therefore idea G
And improvement H
Each of those bullets should be a paragraph that can be summarized in a single sentence. It doesn't need to
be
a single sentence — you can elaborate where necessary. But, once read, the reader should be able to compress it to a single sentence in their mind.
This is related to the idea of editing, and that your reader's attention is a scarce resource. Your reader has a finite amount of stuff they can juggle in short-term memory. Writing in this "one idea per paragraph" style allows the reader to compress the paragraph and thus consume less of this scarce resource.
Use an appendix
If there is some number in the doc that is the result of a complex calculation or simulation, don't include that in the body of the doc. Use a footnote like:
A monte-carlo simulation[1] showed the probability of data loss due to corruption is less than 1 in 10^12
Then describe the simulation in more detail in the appendix. The appendix should not be necessary to read to understand the main conclusion of the doc. It's only there for the curious reader to check your work if they want.
Worked editing example
Here's a paragraph from above before I edited it:
Each one of those bullet points should be its own paragraph in your doc. And each paragraph should be summarizable in a single sentence. The paragraph doesn't need to actually
be
a single sentence. For example, you might include a few more sentences to really illustrate the whole concept you're trying to convey. But, once the reader has read it, they should be able to compress it to a single sentence in their mind.
And here is the edited version that conveys the exact same information, but smaller:
Each of those bullets should be a paragraph that can be summarized in a single sentence. It doesn't need to
be
a single sentence — you can elaborate where necessary. But, once read, the reader should be able to compress it to a single sentence in their mind.
Happy writing!
