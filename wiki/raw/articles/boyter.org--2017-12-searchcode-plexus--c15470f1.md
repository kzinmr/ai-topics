---
title: "searchcode plexus"
url: "https://boyter.org/2017/12/searchcode-plexus/"
fetched_at: 2026-05-05T07:01:59.948438+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# searchcode plexus

Source: https://boyter.org/2017/12/searchcode-plexus/

Plexus “A combination of interlaced parts; a network.”
For a while I have been neglecting searchcode.com while working on searchcode server. This is of course not an ideal situation and as such I have started working on it again. The following is just a brief list of things I am considering, problems, issues etc…
So back when I first started working on searchcode I wrote it using PHP. For searchcode next (the current version) I rewrote it using Python and Django. I had intented to continue using this stack for the forseeable future when I chose it. I quite like writing Python code and at the time the performance was acceptable. When I started writing searchcode server however I wanted to make it as easy to install as possible. The reason being that I considered it a competitive advantage to have users installing searchcode without any pain and be off and running. At the time I considered writing it in Go or Rust but had little experience with either language. I decided to pull on my sensible pants and chose Java which is a language I had worked with before and had excellent library support. With the 8th version Java had become considerably less painful to work with.
This of course means I had two code bases which do roughtly the same thing. The Python/Django codebase and the Java one. I was porting code from Python into Java and then improving it where possible without backporting. At this point I can confidently say that the Java codebase is much better, with addtional performance (not due to Java) and bug fixes. Its also far more malleable with the static typing making refacotoring a breeze. As such I have started to look at moving searchcode.com over to use the same code that searchcode server uses.
This is not without its faults. There is a lot of code to port over and they both work in very different ways.
Take for example the indexing pipeline.
In searchcode.com the indexing pipeline is a bunch of cobbled together scripts of Python that do some analysis on code but mostly call out to external programs such as cloc and sloccount to determine what language is being used and to get other information. The current pointer to a repository is kept in the database and incremented every time the job is run so it picks up the next repository. There are a few of instances of the programming running and it runs constantly in the background on the lowest nice value.
By contrast searchcode server works around background jobs. There are multiple jobs that perform different tasks. One fires off every 10 minutes adding repositories to be indexed. Another picks up the repositories, checks it out and processes it before putting the resulting files on a queue. Another picks up items from that queue and then indexes them. They run on low thread priority with checks to ensure that they don’t impact search performance.
To move from the former to the latter requires effectivly a rewrite. This is because on searchcode.com the code is stored in a central database whereas searchcode server keeps a local copy at all times. Also searchcode server performs all the code analysis itself using its own database of languages and other tricks.
Recently I went through a large clean up of the searchcode server codebase. In doing so I kept in the back of my mind that I should consider making things such that I could move searchcode.com over to use it. As such I decoupled where appropiate, merged where it would make sense and effectively laid the ground work for the work to come. With that release pushed out I am not starting to looking to once again rewrite a large chunk of searchcode.com such that it shares the same codebase.
So the things I want to improve as a list when doing this are the following.
Indexing speed
Currently the process takes literally weeks for a project to be indexed. I want to cut this down to as short a time as possible. This was due to a few reasons. The first was that I could only run a single process on each server I had. While it was possible to run multiple I noticed that it ran into issues such as overusing resources. With tight integration into the codebase I can have the processing throttle back when more important work such as a user doing a search is running. Another issue was that the external programs I was using occasionally would time out or hang. By moving that code internally I can improve searchcode server as a product and have greater control.
Real Time Index
When I first started searchcode.com I was using Sphinx with an Index + Delta scheme for updates. I moved this over to a periodic full index due to performance issues. This means that anything added to the database can take a week before it is searchable. So even if I had fixed the indexing speed issues I was still going to be hobbled by how long it took to update the index. By using sphinx real time indexes I can speed this up and have things available to search the moment they are ready. It also means that deletes which happens when people accidently publish the wrong thing accidently can be cleaned up more effectively.
Language Support
The current version of searchcode.com has some hacks on top of the perl command line application cloc to identify languages beyond what cloc supports. It works well enough but its nice to be able to control this. Since the language identification is build into searchcode server this is a rather nice bonus.
Performance
While the majority of queries and requests are returned fairly quickly some outliers take multiple seconds and some time out totally. I did some profiling of the queries themselves and it appears that the majority return in under a second. This suggest that most of the slowness comes down to the parts outside of sphinx. One thing I was concious of when writing searchcode server was to ensure that it was fast to process results. There were a lot of optimisations that went into the code to help with this. This was actually the bulk of the code that I did not want to backport into the exisitng Python codebase. There is still performance work that needs to go into this but I feel that by having a unified codebase with large amounts of usage it will be easier to catch these edge cases and resolve them more quickly.
Addtional Filters
I wanted to add addtional filter types to the frontend. Things what would be nice would be the file owner IE who was the last person to touch the file. Other things such as the cyclocmatic complexity of the file would also be useful.
With all the above in mind the work has already started. You can view the progress on
https://github.com/boyter/searchcode-server/tree/searchcode
and while there is still a long way to go at this point I have already got the indexing working along with search and a few other things. Still a long journey to go but its nice to see it coming along. I will be posting more updates in the future, so watch this space!
