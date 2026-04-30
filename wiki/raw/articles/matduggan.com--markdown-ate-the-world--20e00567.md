---
title: "Untitled"
url: "https://matduggan.com/markdown-ate-the-world/"
fetched_at: 2026-04-30T07:01:48.291396+00:00
source: "matduggan.com"
tags: [blog, raw]
---

# Untitled

Source: https://matduggan.com/markdown-ate-the-world/

I have always enjoyed the act of typing words and seeing them come up on screen. While my favorite word processor of all time might be WordPerfect (
here
), I've used almost all of them. These programs were what sold me on the entire value proposition of computers. They were like typewriters, which I had used in school, except easier in every single way. You could delete things. You could move paragraphs around. It felt like cheating, and I loved it.
As time has gone up what makes up a "document" in word processing has increased in complexity. This grew as word processors moved on from being proxies for typewriters and into something closer to a publishing suite. In the beginning programs like WordPerfect, WordStar, MultiMate, etc had flat binary files with proprietary formatting codes embedded in there.
When word processors were just proxies for typewriters, this made a lot of sense. But as Microsoft Word took off in popularity and quickly established itself as the dominant word processor, we saw the rise of the .doc file format. This was an exponential increase in complexity from what came before, which made sense because suddenly word processors were becoming "everything tools" — not just typing, but layout, images, revision tracking, embedded objects, and whatever else Microsoft could cram in there.
The .doc: A Filesystem Inside Your File
At its base the
.doc
is a Compound File Binary Format, which is effectively just a FAT file system with the file broken into sectors that are chained together with a File Allocation Table.
It's an interesting design. A normal file system would end up with sort of a mess of files to try and contain everything that the
.doc
has, but if you store all of that inside of a simplified file system contained within one file then you could optimize for performance and reduced the overhead that comes with storing separate objects in a flat file. It also optimizes writes, because you don't need to rewrite the entire file when you add an object and it keeps it simple to keep revision history. But from a user perspective, they're "just" dealing with a single file. (
Reference
)
The .doc exploded and quickly became the default file format for humanity's written output. School papers, office memos, résumés, the Great American Novel your uncle was definitely going to finish — all .doc files. But there was a problem with these files.
They would become corrupted all of the goddamn time.
Remember, these were critical documents traveling from spinning rust drives on machines that crashed constantly compared to modern computers, often copied to floppy disks or later to cheap thumb drives you got from random vendor giveaways at conferences, and then carried to other computers in backpacks and coat pockets. The entire workflow had the structural integrity of a sandwich bag full of soup.
Your hard drive filesysystem -> your .doc file (which can get corrupted as a file) -> containers a mini filesystem (which can ALSO get corrupted internally) -> manages your actual document content
So when Word was saving your critical file, it was actually doing a bunch of different operations. It was:
Updating the document stream (your text)
Updating the formatting tables
Update the sector allocation tables
Update the directory entries
Update summary information
Flush everything to disk
These weren't atomic operations so it was super easy in an era when computers constantly crashed or had problems to end up in a situation where some structures were updated and others weren't. Compared to like a
.txt
file where you would either get the old version or a truncated new version. You might lose content, but you almost never ended up with an unreadable file. With
.doc
as someone doing like helpdesk IT, you
constantly
ended up with people that had just corrupted unreadable files.
And here's the part that really twisted the knife: the longer you worked on the same file, the more important that file likely was. But Word didn't clean up after itself. As a .doc accumulated images, tracked changes, and revision history, the internal structure grew more complex and the file got larger. But even when you deleted content from the document, the data wasn't actually removed from the file. It was marked as free space internally but left sitting there, like furniture you moved to the curb that nobody ever picked up.
The file bloated. The internal fragmentation worsened. And the probability of corruption increased in direct proportion to how much you cared about the contents.
Users had to be trained both to save the file often (as AutoRecover wasn't reliable enough) and to periodically "Save As" a new file to force Word to write a clean version from scratch. This was the digital equivalent of being told that your car works fine, you just need to rebuild the engine every 500 miles as routine maintenance.
The end result was that Microsoft Word quickly developed a reputation among technical people as horrible to work with. Not because it was a bad word processor — it was actually quite good at the word processing part — but because when a user showed up at the Help Desk with tears in their eyes, the tools I had to help them were mostly useless.
I could scan the raw file for text patterns, which often pulled out the content, but without formatting it wasn't really a recovered file — it was more like finding your belongings scattered across a field after a tornado. Technically your stuff, but not in any useful arrangement. Sometimes you could rebuild the FAT or try alternative directory entries to recover slightly older versions. But in general, if the .doc encountered a structural error, the thing was toast and your work was gone forever.
This led to a never-ending series of helpdesk sessions where I had to explain to people that yes, I understood they had worked on this file for months, but it was gone and nobody could help them. I became a grief counselor who happened to know about filesystems. Thankfully, people quickly learned to obsessively copy their files to multiple locations with different names — thesis_final.doc, thesis_final_v2.doc, thesis_FINAL_FINAL_REAL.doc — but this required getting burned at least once, which is sort of like saying you learned your car's brakes didn't work by driving into a bus.
Enter the XML Revolution
So around 2007 we see the shift from
.doc
to
.docx
, which introduces a lot of hard lessons from the problems of
.doc
. First, it's just a bundle, specifically a ZIP archive.
my_document.docx (renamed to .zip)
├── [Content_Types].xml
├── _rels/
│   └── .rels
├── word/
│   ├── document.xml        ← the actual text content
│   ├── styles.xml          ← formatting/styles
│   ├── fontTable.xml
│   ├── settings.xml
│   └── media/
│       ├── image1.png      ← embedded images
│       └── image2.jpg
└── docProps/
    ├── app.xml
    └── core.xml            ← metadata
Now in theory, this is great. Your content is human-readable XML. Your images are just image files. If something goes wrong, you can rename the file to .zip, extract it, and at least recover your text by opening document.xml in Notepad. The days of staring at an opaque binary blob and praying were supposed to be over.
However, in practice, something terrible happened. Microsoft somehow managed to produce the worst XML to ever exist in human history.
Let me lay down the scope of this complexity, because I have never seen anything like it in my life.
Here
is the standards website for ECMA-376. Now you know you are in trouble when you see a 4 part download that looks like the following:
Part 1 “Fundamentals And Markup Language Reference”, 5th edition, December 2016
Part 2 “Open Packaging Conventions”, 5th edition, December 2021
Part 3 “Markup Compatibility and Extensibility”, 5th edition, December 2015
Part 4 “Transitional Migration Features”, 5th edition, December 2016
If you download Part 1, you are given the following:
Now if you open that PDF, get ready for it. It's a 5039 page PDF.
I have never conceived of something this complicated. It's also functionally unreadable, and I say this as someone who has, on multiple occasions in his life, read a car repair manual cover to cover because I didn't have anything else to do. I once read the Haynes manual for a 1994 Honda Civic like it was a beach novel. This is not that. This is what happens when a standards committee gets a catering budget and no deadline.
Some light reading before bed
There was an accusation at the time that Microsoft was making OOXML deliberately more complicated than it needed to be — that the goal was to claim it was an "open standard" while making the standard so incomprehensibly vast that it would take a heroic effort for anyone else to implement it. I think this is unquestionably true. LibreOffice
has a great blog post on it
that includes this striking comparison:
The difference in complexity between the document.xml and content.xml files is striking when you compare their lengths: the content.xml file has 6,802 lines, while the document.xml file has 60,245 lines, compared to a text document of 5,566 lines.
So the difference between ODF format and the OOXML format results in a exponentially less complicated XML file. Either you could do the
incredible
amount of work to become compatible with this nightmarish specification or you could effectively find yourself cut out of the entire word processing ecosystem.
Now without question this was done by Microsoft in order to have their cake and eat it too. They would be able to tell regulators and customers that this
wasn't
a proprietary format and that nobody was locked into the Microsoft Office ecosystem for the production of documents, which had started to become a concern among non-US countries that now all of their government documents and records were effectively locked into using Microsoft. However the somewhat ironic thing is it ended up not mattering that much because soon the only desktop application that would matter is the browser.
Rise of Markdown
The file formats of word processors were their own problems, but more fundamentally the
nature
of how people consumed content was changing. Desktop based applications became less and less important post 2010 and users got increasingly more frustrated with the incredibly clunky way of working with Microsoft Word and all traditional files with emailing them back and forth endlessly or working with file shares.
So while
.docx
was a superior format from the perspective of "opening the file and it becoming corrupted", it also was fundamentally incompatible with the smartphone era. Even though you could open these files, soon the expectation was that whatever content you wanted people to consume should be viewable through a browser.
As "working for a software company" went from being a niche profession to being something that seemingly everyone you met did, the defacto platform for issues, tracking progress, discussions, etc moved to GitHub. This was where I (and many others) first encountered Markdown and started using it on a regular basis.
John Gruber, co-creator of Markdown, has a great breakdown of "standard" Markdown and then there are specific flavors that have branched off over time. You can see that
here
. The important part though is: it lets you very quickly generate webpages that work on every browser on the planet with almost no memorization and (for the most part) the same thing works in GitHub, on Slack, in Confluence, etc. You no longer had to ponder whether the person you were sending to had the right license to see the thing you were writing in the correct format.
This combined with the rise of Google Workspace with Google Docs, Slides, etc meant your technical staff were having conversations through Markdown pages and your less technical staff were operating entirely in the cloud. Google was better than Microsoft at the sort of stuff Word had always been used for, which is tracking revisions, handling feedback, sharing securely, etc. It had a small subset of the total features but as we all learned, nobody knew about the more advanced features of Word anyway.
By 2015 the writing was on the wall. Companies stopped giving me an Office license by default, switching them to "you can request a license". This, to anyone who has ever worked for a large company, is the kiss of death. If I cannot be certain that you can successfully
open
the file I'm working on, there is absolutely no point in writing it inside of that platform. Combine that with the corporate death of email and replacing it with Slack/Teams, the entire workflow died without a lot of fanfare.
Then with the rise of LLMs and their use (perhaps overuse) of Markdown, we've reached peak
.md
. Markdown is the format of our help docs, many of our websites are generated exclusively from Markdown. It's now the most common format that I write anything in. This was originally written in Markdown inside of Vim.
Why It Won
There's a lot of reasons why I think Markdown ended up winning, in no small part because it solved a real problem in an easy to understand way. Writing HTML is miserable and overkill for most tasks, this removed the need to do that and your output was consumable in a universal and highly performant way that required nothing of your users except access to a web browser.
But I also think it demonstrates an interesting lesson about formats.
.doc
and .
docx
along with ODF are pretty highly specialized things designed to handle the complexity of what modern word processing can do. LibreOffice lets you do some pretty incredible things that cover a
huge
range of possible needs.
Markdown doesn't do most of what those formats do. You can't set margins. You can't do columns. You can't embed a pivot table or track changes or add a watermark that says DRAFT across every page in 45-degree gray Calibri. Markdown doesn't even have a native way to change the font color.
And none of that mattered, because it turns out most writing isn't about any of those things. Most writing is about getting words down in a structure that makes sense, and then getting those words in front of other people. Markdown does that with less friction than anything else ever created. You can learn it in ten minutes, write it in any text editor on any device, read the source file without rendering it, diff it in version control, and convert it to virtually any output format.
The files are plain text. They will outlive every application that currently renders them. They don't belong to any company. They can't become corrupted in any meaningful way — the worst thing that can happen to a Markdown file is you lose some characters, and even then the rest of the file is fine. After decades of nursing .doc files like they were delicate flowers that you had to transport home strapped to your car roof, the idea of a format that simply cannot structurally fail is not just convenient. It's a kind of liberation.
I think about this sometimes when I'm writing in Vim at midnight, just me and a blinking cursor and a plain text file that will still be readable when I'm dead. No filesystem-within-a-filesystem. No sector allocation tables. No 5,039-page specification. Just words, a few hash marks, and never having to think about it again.
