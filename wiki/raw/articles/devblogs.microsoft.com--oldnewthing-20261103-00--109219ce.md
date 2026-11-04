---
title: "How do you implement a random-access database when you don't have random-access external storage?"
url: "https://devblogs.microsoft.com/oldnewthing/20261103-00/?p=112825/"
fetched_at: 2026-11-04T10:00:59.921138+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# How do you implement a random-access database when you don't have random-access external storage?

Source: https://devblogs.microsoft.com/oldnewthing/20261103-00/?p=112825/

The mystery comment
investigated by
Beej’s Bit Bucket
reminded me of a similar trick in an Apple ][ telephone directory program.
The base Apple ][ was sold without a floppy drive. The only supported external storage device in the base unit was a cassette I/O port. Yet there was a database program for digitizing your phone list.¹ How did it do database stuff when the only I/O was a cassette drive? It could not programmatically start or stop the tape, or programmatically rewind or advance it.
If you took a listing of the program (which was written in BASIC), it began with a comment block saying not to edit any lines before line 1000. And then you saw your own telephone directory stored in
DATA
statements.² Followed by a bunch of dummy
DATA
statements. And then the program began.
Wait, how did your telephone directory show up as
DATA
statements? The BASIC
DATA
statement was a place for the program developer to store tables of precalculated read-only data, to be consumed by the
READ
statement at runtime. They shipped the program to you without your telephone directory in it, and yet somehow your telephone data ended up in the program.
That’s because the program used its own
DATA
statements as the memory for a database.
When it wanted to read from the database, it read the data via the usual
READ
command. And when it wanted to write to the database, it used self-modifying code to
POKE
the information back into its own
DATA
statements.
When you told the program that you wanted to save your changes, it told you to turn on the cassette player, and then it invoked the
SAVE
command to save the program to cassette. And since the program modified itself to contain your telephone data, saving the program also saved your data that was embedded inside it.
When you wanted to use your telephone directory, you loaded the program from cassette and ran it.
Now, the Apple ][ did have routines in the monitor ROM to save a block of memory to cassette, so it could have saved the database to tape in a more traditional manner. But that would have meant that when you wanted to use your telephone directory, you first had to load the program from cassette and run it, and then you had to set up the cassette a second time to load the database. Saving the entire program meant that the two load operations (loading the program and loading the data) were combined into a single cassette pass.
¹ This was back in the early days when the sales pitch for personal computers included “Organize your recipes!” and “Digitize your telephone directory!” Things that nobody ever actually did. (I don’t know how many people used it for personal finance, but it was definitely
very popular for
business
finance
.)
² At least, I think it was
DATA
statements. Maybe it was comments. But the same principle applies.
