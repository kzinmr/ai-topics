---
title: "In memory of the man who put red and green squiggles under words"
url: "https://devblogs.microsoft.com/oldnewthing/20260622-00/?p=112451"
fetched_at: 2026-06-23T07:00:55.523170+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# In memory of the man who put red and green squiggles under words

Source: https://devblogs.microsoft.com/oldnewthing/20260622-00/?p=112451

I recently learned of the passing of someone whose work nearly everybody knows, but nobody knows his name.
Tony Krueger is
remembered in Wikipedia
as the person who ported the game Chip’s Challenge to Windows for the Windows Entertainment Pack.¹ But that’s probably not the code he wrote that touched the most people.
Tony worked on Word 1.0, 1.1, 2.0, then on Word for OS/2 and Word for Mac, then returned to Word 6.0 and several versions beyond that. He probably holds the record for “most versions of Word shipped.”
In early versions of Word, the Spell Check feature was something that you explicitly invoked, and then you had to sit and wait while the program looked for all your potentially-misspelled words, and then showed them to you one at a time for a decision on what to do for each one. Word did introduce an Auto Spell Check feature to run spell check when the user was idle, so that when you hit the Spell Check button, the results were ready to go. However, the Auto Spell Check was still a blocking operation. As a result, a lot of users turned it off because it always seemed to decide “Now would be a good time to spell-check the document” just as you wanted to do something, forcing you to wait for the spell check pass to complete before you could, say, save and exit.
Tony made the spell checker much more unobtrusive so that it didn’t interfere with your foreground work. And when it found a problem, instead of waiting for you to trigger a spell check, it immediately drew red squiggles under potentially-misspelled words (and later green squiggles under potential grammatical errors).
Tony was an early fan of the magic/comedy team Penn and Teller. A friend and colleague attended a show and hung out afterward to ask the duo to sign a photo for his friend Tony. “He was on the team that did the red and green squiggles in Word.”
Upon hearing this, Penn Jillette announced in his stentorian voice which filled the entire theater: “The red and green squiggles!? I
love
the red and green squiggles!” Teller silently concurred.
Tony received that autographed photo for his birthday, and it wasn’t clear which he was more happy about, the autographed photo or the fact that Penn and Teller loved his feature.
Many years later, “Weird Al” Yankovic recorded a parody video titled
Word Crimes
, in which the Word red squiggles make a brief appearance. That same friend got “Weird Al” to autograph the screen shot.
Today, there are red (and even green and blue) squiggles in nearly every word processor, and often outside word processors. Tony did it first. The next time a red squiggle catches one of your mistakes, say thanks to Tony. I think he’d appreciate it.
¹ Probably not as widely documented is that he accomplished this without the source code: He reverse-engineered the MS-DOS version and then reimplemented it for Windows.
