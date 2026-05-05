---
title: "PHP Bug Trackers"
url: "https://boyter.org/2010/08/php-bug-trackers/"
fetched_at: 2026-05-05T07:02:08.228557+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# PHP Bug Trackers

Source: https://boyter.org/2010/08/php-bug-trackers/

So in keeping with the lean startup style, I needed to work out which version control system and which bug tracker I would use. Internally at work I use subversion and JIRA. Both do the job quite well but I have found some shortcomings with subversion and JIRA is needlessly complicated for a single developer at the moment. So I looked for alturnatives.
Version control was easier of the two to pick. I have been toying with GIT for a while and so I can now safely say I have been using GIT for the last few months. Im pretty happy with it and its workflow of branch, develop, merge, push works very well with my coding style. So no problems there. The bug tracker was a little more difficult to choose from.
Most bug trackers around are very complex designed to support bigger projects. All I really need at this point is a central point to stick my bugs, push them through a simple assigned, resolved, closed workflow and attach document etc… My requirements were that it is written in PHP due to ease of deployment. I had briefly considered going with 37 Signals base-camp but I don’t really want have someone else host this as I am trying to keep costs down. All I needed was something like a hosted spreadsheet or text file. A quick Google/Bing search turned up the following,
Mantis
– Looks a little complex and very JIRA like at first glace. I decided to skip trying this initially.
WebIssues
– Looks good but I wasn’t keen on having to install other software to interface with it.
The Bug Genie
– Looks good and was the first one I decided to try.
So I downloaded The Bug Genie installed it and had a play. My goal was to set up a project and add bugs as quickly as possible. Alas Genie wanted me to set up versions and components before allowing me to add bugs. Probably good practice in theory but I don’t need anything that complex at the moment. It was also rather slow and hard to modify permissions for users.
My next attempt was using
phpBugTracker
Its last update was in 2007 so it looks like its abandoned but the screenshots were simple enough which seemed to be what I wanted. However being old and unsupported it was unable to install on my machine. Looked like some sort of database interfacing issue which frankly I didn’t want to debug.
At this point I was out of ideas, but figured the heck with it lets try Mantis. The install was smooth and I was able to create a project and add bugs almost instantly. So a big win there. The best thing however was that I was able to hide most of the annoying interface stuff just by minimizing them using the interface and it remembered what I had done.
So now I am using Mantis which I had initially written off. I guess the point is try what is said to be the best software in its particular class before writing it off because odds are it might just be what you are looking for in the end.
If anyone does happen to read this let me know of any other simple PHP bug tracker software out there.
