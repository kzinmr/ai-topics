---
title: "Anti-Patterns in Software Blogging"
url: "https://refactoringenglish.com/blog/anti-patterns-software-blogging/"
fetched_at: 2026-10-08T10:01:35.080461+00:00
source: "refactoringenglish.com"
tags: [blog, raw]
---

# Anti-Patterns in Software Blogging

Source: https://refactoringenglish.com/blog/anti-patterns-software-blogging/

In software development, we collect anti-patterns to recognize common traits that lead to poor outcomes in our software. I thought it would be helpful to do the same for software blogging, so I’ve catalogued the most frequent mistakes I see from beginner bloggers.
The meandering intro
🔗
The most common mistake in software blogging, by far, is meandering. I constantly find myself several paragraphs into a post with no idea what the author is trying to tell me.
Developers love specificity, so they start blog posts with backstory, historical context, and whatever else happens to be on their minds. That may be fun to write, but it’s not always interesting to read.
From the reader’s perspective, there are a billion other articles they could be reading. Why should they read yours? They’re not going to invest 20 minutes to read it in full unless they expect a payoff. Give the reader a reason to continue reading.
Give the reader a reason to continue reading.
When a developer begins reading an blog post, they’re trying to answer two questions as quickly as possible:
Did the author write this for someone like me?
How will I benefit from reading it?
Give yourself the title and the first three sentences to answer both questions.
The benefit you offer can be teaching the reader a new skill, explaining a concept, illustrating a new perspective, or delivering an entertaining rant. You just have to offer the reader
something
. They’re not going to read your blog post just because it’s there.
Here’s
an article I wrote recently
that gets straight to the point:
if got, want: A Simple Way to Write Better Go Tests
There’s an excellent Go testing pattern that too few people know. I can teach it to you in 30 seconds.
The introduction succinctly communicates that the article is relevant to programmers who use the Go programming language, and the value is teaching them a new technique they can learn quickly.
Preamble still counts as meandering
🔗
Some bloggers write a compelling intro but clutter the reader’s path with extras like a subtitle, a bio, an image, or a famous quote. You can include any of these things, but recognize that they count against your “inspire the reader to keep reading” budget. Everything you put in the reader’s path is extra work that chips away at their finite supply of focus.
“The reader knows everything I know except this one thing”
🔗
Effective teachers compare new concepts to something the reader finds familiar. For example, if you were explaining
Jellyfin
, you might say, “Jellyfin is a streaming service like Netflix, except it’s open-source and private, so nobody monitors your viewing habits.” The tricky part is knowing what the reader finds familiar.
In this article, I’ll introduce Docker to developers who have never heard of it before.
Docker is simple. It’s nothing more than a slick frontend to Linux cgroups. Oh, you know jails in *BSD? Docker is the Linux version of that.
Lots of developers want to use Docker but don’t recognize terms like cgroups, jails, or *BSD. They might not even know what Linux is, especially if they’re seeking out an introduction to Docker.
Instead of assuming the reader has your exact body of knowledge, minimize your assumptions about the reader:
Docker is a tool for packaging your app so that it has a consistent, reproducible environment wherever it runs. Docker allows you to define your app’s environment and dependencies in human-readable text files. These files capture your app’s requirements, so you know exactly how it works even after years of tweaks by different teams.
When you write a blog post, think about your target reader. What do they know? Imagine a friend or teammate you know in real life. Write a list of terms they would recognize and terms they would not. Then, re-read your blog post, and whenever you encounter a technical term, think about whether your reference reader would understand it.
Think of a person you know in real life. Read your article as that person and identify which terms feel unfamiliar.
You’re describing the audience I had in mind, but I’ve never tried listing out what that audience knows. Comparing your list against the assumptions in my draft is pretty mind-blowing.
–Tyler Cipriani, when I challenged assumptions about his target reader while editing
“The future of large files in Git is Git”
Overreliance on links
🔗
When’s the last time you read a book that directed you to stop reading, go buy a different book, read it in full, then continue your original book? Software bloggers do this all the time, though it’s more subtle.
Bloggers often want to mention a term the reader might not know, but they don’t feel like explaining it themselves. Instead, they slap a link on the term and think, “Problem solved!”
The problem is not solved because the reader doesn’t want to interrupt their flow and go read a whole different site just to understand one word.
Assign
firewall
rules to prevent external traffic from reaching your database.
The FreeBSD manual linked above is an excellent resource, but the chapter on firewalls chapter is about 20,000 words. When you link to such a wordy page, you dump a massive amount of work on the reader.
Instead of relying on a link to do your work for you, give the reader the minimum possible explanation to understand your article.
A
firewall
is a system that restricts how hosts and networks communicate with an app. You can increase your web app’s security by configuring firewall rules to only allow inbound requests to your database server when they originate from your app server.
By all means, link to useful resources, but make them a bonus rather than a prerequisite. Keep the reader on the page. Your target reader should be able to enjoy and understand your article from start to finish without clicking any links.
Keep the reader on the page.
The sequel injection bug
🔗
These days, everything is either a sequel or a reboot, including blog posts. I see a lot of blog posts that open like this:
In part one, we learned about quintuply linked lists and how they can 100x your daily LOC output. In today’s post, I’ll show you how
goto
statements let you scrunkmax (a term I invented in part one – remember?).
I hate to break it to you, but most readers have not read part one. If you assume your last article is fresh in the reader’s mind, they’ll think, “Oh, now there’s extra work to even
start
reading?”
It’s fine to refer to your previous posts, but don’t do it right out of the gate. When you do link to past posts, summarize what was relevant rather than force the reader to go back and read it in full.
If you’re writing about the hobby operating system you built from scratch, then sure, you probably need more than one blog post, but the vast majority of sequel posts could be standalone articles with like 3% more effort.
Excessive formality
🔗
Beginner software bloggers suffer from a mass delusion that you have to write in a stiff, overly formal way for people to take you seriously:
Several static analysis tools were utilized by my teammates and myself throughout the duration of this project’s lifetime.
You’re not writing for 80-year-old executives at IBM in 1988. Your field is software development, one of the least pretentious white-collar jobs out there. The person reading your article is probably wearing pajamas and flip flops while eating from a bowl of cereal next to their keyboard. They don’t expect or want you to talk like a legal document.
Just write the way you talk.
We tried a few static analyzers on this project.
With so many developers delegating their writing to AI, software blogging is becoming bland and homogenous. Readers are hungry for writing with personality. Here’s a random sentence from Joel Spolsky,
the best software blogger of all time
:
All the kids who did great in high school writing pong games in BASIC for their Apple II would get to college, take CompSci 101, a data structures course, and when they hit the pointers business their brains would just totally explode, and the next thing you knew, they were majoring in Political Science because law school seemed like a better idea.
– Joel Spolsky,
“The Perils of JavaSchools”
It’s not Spolsky’s best line, but it captures his style. It’s casual, personable, and unpretentious. It sounds like he’s telling a story to some friends at lunch. You can see the same style in the writing of
Kathy Sierra
,
Terence Eden
, and
Raymond Chen
. They’re not trying to sound smart–they’re just trying to sound like themselves, and that’s what readers enjoy.
Fumbling on the basics of rendering HTML
🔗
The hardest part of software blogging is writing in a compelling way, so it’s frustrating to see so many software bloggers bungle the part that should be easy: making a basic webpage.
Page overflow on mobile
🔗
The worst mistake you can make for mobile readers is overflowing the screen so the reader has to scroll back and forth to read your article. Usually, it’s because you have an image or code snippet that insists on being desktop size and screws up the layout of the rest of the page.
Your browser does not support the video tag.
Allowing the text to overflow the screen on mobile creates a miserable reading experience.
Desktop versions of Firefox and Chrome both have a mobile preview mode. Check your article with the mobile preview before you publish, and check for common rendering issues.
Don’t underestimate your mobile readers. According to my analytics, 25% of you are reading this page on your phones. On
my personal blog
, it’s 35%.
Unreadable font
🔗
Choose a font color and family that are easy to read. Stop it with this dark gray text on a light gray background. Firefox and Chrome both have built-in tools that flag low-contrast text for you.
Firefox’s accessibility tool identifying low-contrast text
If you don’t feel like searching around for the perfect font, the Braille Institute has a free font called
Atkinson Hyperlegible
that’s particularly comfortable to read, even for readers with poor vision.
Summary
🔗
Give the reader a compelling reason to continue reading. Get to it within the title and the first three sentences of your blog post.
Common reasons: they want to hear an entertaining story, learn a useful technique, or understand a concept that’s relevant to them.
Question your assumptions about what the reader knows and does not know.
Think about what concepts and terms you expect the reader to recognize and re-read your article to make sure it matches those expectations.
The reader should be able to read your article from start to finish without clicking links or hovering for tooltips.
Links should allow the reader to explore topics more deeply, but they should be a bonus rather than a pre-requisite.
Avoid presenting your article as a follow-up to a previous article.
Assume most readers haven’t read your previous articles. Summarize what’s relevant for them to know rather than expecting the reader to go read all your prior posts.
Drop the formality. Write the way you speak in real life.
Test your articles in your browser’s mobile view.
Make sure that your text doesn’t overflow the screen and force the reader to scroll horizontally as they read.
Use browser testing tools to find low-contrast text that makes your article difficult to read.
“Not Quite How Developers Read” and “What the Reader Knows” illustrations by
Piotr Letachowicz
.
