---
title: "Code Spelunker a Code Search Command Line Tool"
url: "https://boyter.org/posts/code-spelunker-a-code-search-command-line-tool/"
fetched_at: 2026-05-05T07:01:55.872718+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Code Spelunker a Code Search Command Line Tool

Source: https://boyter.org/posts/code-spelunker-a-code-search-command-line-tool/

Code spelunker (cs) or code search is a new command line tool I have been working on and off over the last few years. It allows you to search over code or text files in the current directory either on the console, via a TUI or HTTP server, using some boolean queries or regular expressions. I just recently pushed out a stable first version release and thought I would write a quick post about it.
You can check it out via github
https://github.com/boyter/cs
The idea came about while watching a work colleague continually opening Visual Studio Code in order to search over files recursively in a directory. I asked why he didn’t use a tool like ripgrep with the context flag to which he replied that he liked the interactivity the UI gave him. Having wanted to work on a terminal UI application for a while, also being interested in code search and having always wanted to build a real search ranking algorithm it seemed like a overlap of goals to try and build a tool just for him.
Rather than bore you with details of how it works lets start by showing off the party trick. You can read the details about if after watching.
You can get something close to this idea without using
cs
by piping the results of ripgrep into fzf such as
rg test | fzf
although I think
cs
does offer enough over this technique to justify installing yet another command line tool.
Not just a one trick pony however cs can also serve up a crude but functional HTTP search interface. Yes you can swap out the templates for your own if you like and build whatever custom interface you want.
Get a copy of cs via github
https://github.com/boyter/cs
I will assume if you are still reading beyond this you are interested in how things came about. Otherwise the link above is all you need to get started. Go install it, find any bugs I missed report the back and ill try fixing them.
John Harrison
was a clockmaker who solved the problem of calculating longitude while at sea using accurate timekeeping devices. To do so he ended up changing course after 30 years of experimentation using large sea clocks and starting again with a “sea watch” of a much smaller design. In short he threw away what could be considered a lifetime of work for something better when he saw it.
I bring this up because I have spent the last 10 years or so working on searchcode.com and searchcodeserver.com and after rethinking the problem I am about to do something similar, but with far less material impact.
Lets discuss code search. There are a few main methods in practice today to do it. The first is to use regular expressions. Tools such as ripgrep, the silver searcher and ack work like this. You feed them either string literals or regular expressions and they will skip though files looking for matches.
Another method is to build an index based on tools like lucene which were originally written for full-text search. The original koders.com worked like this. My website searchcode.com and searchcodeserver.com also used this technique although they both put a lot of work into breaking code tokens apart such that a search for
i++
would match
for(i=0;i<100;i++)
to ensure the search experience works as expected. Incidentally lucene does support some regular expression searches (I think through literal extraction, but I have not found time to review its code) so it can work similar to the regular expression tools at a larger scale.
There is a hybrid between the regular expression tools and the index ones where you build a trie index. This is how google code search worked back in the day and allows you to bridge the gap and allow your regex search to scale. However unlike lucene this index is optimized for regular expressions, by taking a good guess as to what results would match, and then knowing which files to actually search.
The last method I can comment on is the one used in sourcegraph. It is a bit smarter than the others by actually trying to understand the source code. This means it knows what a function is, and how it relates to the rest of the codebase allowing links between files. This too relies on an index, but last time I checked under the hood its a custom one. It is also more expensive to calculate and as such more expensive to scale. This is similar to how ctags works, although it operates at a larger scale.
I have heard of some companies using machine learning to understand code but this is really out of my depth of understanding and I cannot thing of a public example available yet. I expect this to change in time however.
Each of the above techniques has pros and cons depending on what you are trying to do.
Regular expressions generally does not scale to very large corpus’s (tens of gigabytes), unless you go the hybrid route with an index to maintain and they do not rank results, although in theory they could. They also have difficulty doing boolean style searches. Index based searches scale quite well, rank results and support boolean searches but you have an index to maintain and are a huge overhead for small codebases (although still work). They also don’t search code very well without special attention. The sourcegraph approach works well, but you need to learn a special search syntax to get the most from it.
I believe this leaves a small space for a boolean search tool with ranking that “brute forces” its searches similar to the regular expression tools work. I also believe that this technique can work in other situations, such as for research purposes. I also think that given the HTTP interface that
cs
can be a replacement for a lot of the heavier tools such as searchcodeserver.com without the need to stand-up much infrastructure and wait for it to build its index.
I would normally write a lot about the code behind
cs
, but the reality is I already have. I took a lot of what went into
cs
over the years and adapted it into other projects. So I am just going to link to the posts that relate to what went into it below.
Probably most relevant would be the first about faster literal string matching. The only reason that code was written was to support
cs
. It just turned out to be useful enough that I wanted it for other projects.
