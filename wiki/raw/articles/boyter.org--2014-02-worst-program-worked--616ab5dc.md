---
title: "The worst program I ever worked on"
url: "https://boyter.org/2014/02/worst-program-worked/"
fetched_at: 2026-05-05T07:02:03.932360+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# The worst program I ever worked on

Source: https://boyter.org/2014/02/worst-program-worked/

The worst program I ever worked on was something I was asked to maintain once. It consisted of two parts. The first was a web application writen in ASP. The second portion was essentially Microsoft Reporting Services implemented in 80,000 lines of VB.NET.
The first thing I did was chuck it into VS2010 and run some code metrics on it. The results were, 10 or so Methods had 2000+ lines of code. The maintainability index was 0 (number between 0 and 100 where 0 is unmaintainable). The worst function had a cyclomatic complexity of 2700 (the worst I have ever seen on a function before was 750 odd). It was full of nested in-line dynamic SQL all of which referred to tables with 100+ columns, which had helpful names like sdf_324. There were about 5000 stored procedures of which most were 90% similar to other ones with a similar naming scheme. There were no foreign key constraints in the database. Every query including updates, inserts and deletes used NOLOCK (so no data integrity). It all lived in a single 80,000 line file, which crashed VS every time you tried to do a simple edit.
I essentially told my boss I would quit over it as there was no way I could support it without other aspects of work suffering. Thankfully it was put in the too hard basket and nobody else had to endure my pain. I ended up peer reviewing the changes the guy made some time later and a single column update touched in the order of 500 lines of code.
There was one interesting thing I found with it however, there was so much repeated/nested if code in methods you could hold down page down and it would look like the page was moving the other way, similar to how a wheel on TV looks like its spinning the other way.
