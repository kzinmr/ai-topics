---
title: "Intern interview questions"
url: "https://boyter.org/posts/intern-interview-questions/"
fetched_at: 2026-05-05T07:01:57.482743+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Intern interview questions

Source: https://boyter.org/posts/intern-interview-questions/

Recently my workplace has been accepting some interns as part of contributing back to the industry in general, as well as promoting the brand and hopefully being able to grow and grab excellent candidates in the future when they graduate. One recently wanted some time to sit down with me to ask a few questions. In order to give him the best use of time I asked to have the questions written in advance so I could respond to them before chatting and then build out my answers verbally.
Since I put some effort into writing the answers, and in accordance with my goal of putting anything I write into my website here are the questions and answers, slightly sanitised for public viewing.
General Questions
What interested you in I.T?
Honestly, I just don’t see too many other things I would be interested in. Its hard to find any other role with as much impact.
What are you looking forward to working?
I am enjoying the current project I am on now, where we are storing large amounts of genetic and clinical data. Really hoping we get a crack at the large search problems in the future. I have no idea how to search over terabytes of genetic data beyond some abstract ways using bloom filters so it sounds cool. I have been reading up on how others have solved it in anticipation, which might be jumping the gun a little.
What would be the best project to work on?
For me personally anything involving search tends to get my attention. Or anything that requires extreme scale. I like search problems because I find they have that perfect overlap of large data, high performance and neat algorithms that are hard to find. Sadly we tend to just use off the shelf tools to solve it most of the time, which is probably the right thing to do when someone is paying for it though.
What is your least favourite language and why?
Probably JavaScript… because I am not very good with it, don’t like the package manager or ecosystem. I remember when it was a case of F5 in your browser and you could see the results, and that was changed with transpilers and the like. I only dislike it because I am forced to use it at times, and I think if you aren’t all in on it its hard to get productive at it, which bothers me. I find javascript/typescript to be incredibly dense languages as well, and callbacks/promises fairly un-intuitive.
The Kablamo culture, what makes it different from other places you have worked at?
So the first is that at Kablamo I am a profit center. Which I think makes me appreciated more than say in a business where you are a cost center. There is an incentive to keep you around so long as you generate income.
What I really like is that the people here are brilliant. There is nobody in the company who does not have something to offer me technically I can learn from. What’s the saying, If you are the best musician in your band, find another band? That’s what it feels like here, the other band, where everyone is pushing you to learn more.
What do you look for when interviewing candidates?
Problem solving ability. I tend to ask every candidate the same question. Imagine there is a bug in production (on some system they are working with) and ask them to debug it. I then but in and take away whatever they said. So if they said “I look at the logs” after a while I will suggest that we don’t have logs, or there is nothing in there. This repeats until they give in or some time has passed.
It’s there to promote a little stress, and see how you think and can you overcome problems. You do tend to run into people that when say “Newrelic does not exist” will say “Well I install it or cannot do my job”. Being able to think things through and diagnose problems is one of the most important skills you can have.
Did you always know you wanted to be a full stack developer?
No. I just wanted to be a developer and keep working on code because I enjoy it so much. So many people my age have transitioned out from it, but I still find writing code thrilling. If I have to move to some other role to do it I would.
Are you working on any side projects of your own?
So many… searchcode.com searchcodeserver.com scc are probably the main ones. Otherwise I have been looking into building an indexing engine for searchcode using bloom filters which is keeping me interested. Other things have been building a general purpose duplicate code detector, and a bitbucket cloud plugin (which I finished but need them to launch pay via atlassian before I launch it). Oh and I also have a command line search tool called cs im working on in my spare time sometimes. Finally a licence checker command line application which I should get back into one of these days.
Too many really, but its my time so its fine :)
How do you keep yourself updated about the new trends in the industry?
I don’t for the most part. A lot of things are cyclic, and you see the same things over and over. Consider everyone going on about the Nodejs event loop for example. I had people tell me “It’s new and fast!” with a straight face. Ignoring that event loops go back to Windows 1 days and Nodejs is NOT fast by any stretch of the imagination. It did solve certain harder problems at the time though.
Otherwise I tend to see what’s trending on things like HackerNews. I also follow a lot of interesting tech leaders on twitter, I also keep an eye out on what’s interesting on the company slack.
What’s the most recent thing that you have learned?
That SLOCCount came before CLOC. Otherwise probably in depth details of how bloom filters actually work, how to implement them and a host of interesting problems they can solve that you wouldn’t really consider.
I have a habit of writing down anything I learn on my blog these days, this one, so the most recent post there is usually what I have been thinking about recently.
What’s hard about coding?
It’s not syntax, that’s for dammed sure. Syntax is just noise. You get used to it over time and eventually learn to like it even if you were radically opposed to start. Consider Python… the indent thing is annoying at first, and later it’s just something you accept. Same with the use of { or } in C languages or ( and ) in lisp languages.
There are a few responses to this. Lets go with doing things for yourself first. The hard thing is finishing things off. It’s pretty easy to get a 80% there thing working for yourself. Where it gets hard is knuckling down, and sanding the corners to get a nice working implementation. I guess maybe less than 5% of people actually publish things online that actually get used by more than themselves and their Mum. What’s the saying, the remaining 10% of the work takes another 90% of the time?
Otherwise the other hard part is learning to listen to what the user/customer actually wants. To quote House MD, they lie. It’s common to get at the end of a project “That’s what we asked for but its not what we want!”. A lot of it is actually about drilling into what problem they are trying to solve, and then looking for a solution together. The technology is irrelevant. Don’t think of yourself as a coder, but as someone who solves business problems, and just happens to use technology to do it.
If you want to know what’s the hardest part about the technology itself. I would say being able to code fearlessly. A lot of projects/places have a high penalty to failure. This means you are afraid to make changes which makes you risk averse which means it takes ages to ship. Getting the team and yourself into a situation where the penalty of failure is so small as to make no difference means you can move faster and make sweeping changes. Getting to that state can be very hard depending on where you start though.
Which technologies and languages would you need to develop a project from scratch?
Irrelevant. What’s more important is what problem you are trying to solve. That’s going to dictate the technology choices anyway. You aren’t going to try and build a hard real time system using Python/JavaScript for example, nor using Java or Go (unless you are allowed to restart it now and then).
All things being equal though, Go, TypeScript, React, Lambda, S3, RDS, Fargate, ALB, Route53, SQS will solve 99% of all problems you are likely to encounter. Its more about knowing when not to use those, then looking for a problem for them to solve.
What is the best implementation or debugging you have done in the past?
Im fairly happy with this code
https://github.com/boyter/go-string/blob/master/index.go
which is pretty well documented, fast and easyish to understand.
As for debugging… the most exciting thing I have debugged recently was a branch prediction fail in scc. It was running slow in some cases and I was wondering why. Turned out by recording the if statements after suspecting it was a branch prediction fail resolved it and it was much faster. I felt like a programming god for about an hour afterwards.
Oh! Or there was a bug in searchcode.com where some pages would return slowly, and cause a CPU to peg at 100%. I spend a lot of time tracking it down and eventually put a profiler into the real web application to catch it. It turned out it was a problem in a library I depended on that needed to use a non RE2 regular expression engine, and as such was running into a backtracking issue. It was easy enough to fix once I knew the issue.
My favorite was a performance issue in a .NET application years ago. There was a 3 level nested loop which everyone was saying “Thats the issue”. I agreed, but said lets run it though a profiler. Turned out the slowest part of it was string to integer parsing. I swapped it out for the fastest one in .NET and then added a cache and the page load time went from 10 seconds to under 1.
I like performance issues :)
Oh one other one was how symlinks work and how to deal with them in code. That was especially annoying.
What’s the most puzzling programming challenge you have come across recently?
So I don’t tend to look at programming once, but this one
https://boyter.org/2017/03/golang-solution-faster-equivalent-java-solution/
was especially fun. Otherwise looking into how how unicode search works
https://boyter.org/posts/faster-literal-string-matching-in-go/
and
https://boyter.org/posts/unicode-support-what-does-that-actually-mean/
was pretty fun. Recently its been all about learning how Bitfunnel works which is how the fresh index in Bing works using bloom filters.
Are there any disadvantages to GraphQL?
Building a robust GraphQL endpoint that is performant, scalable, secure, etc, is much more difficult than REST. GraphQL is optimised for front-end developers over all else. Also if you aren’t fully aware of your data up-front it can quickly become a big ball of mud.
The scale is the one I am most worried about personally. REST tends to return a specific set of data which you can optimise queries for, be that through indexes or caches. GraphQL by contrast handles arbitrary queries so you can end up with queries that are impossible to optimise. This is especially problematic at scale or if you allow it to be consumed publicly. It works the other way too though, GraphQL clients can optimise to just the edges they need, but I tend to never trust the client.
But yes, database load is a big problem with GraphQL. In theory it can be more performant but that’s hard to get right.
Keep in mind there is nothing special about GraphQL. You can implement a REST style API that works in a very similar way if you want, see
https://www.vinaysahni.com/best-practices-for-a-pragmatic-restful-api
You can do joins in REST, restrict fields etc…
I think GraphQL tends to make hard things easier, but easy things harder. The returning of the schema in GraphQL is pretty neat though.
If you had any advice to tell a student studying I.T that wanted to become a full stack developer or Tech Lead, what would that be?
Learn to communicate, both written and verbal. Join toastmasters to help with this. The stereotype of nerds not being able to speak is a bit overblown but there is a lot of truth that technical people tend to talk in technobabble to people making the decisions.
Most business/customers don’t care that you implemented unit/integration tests with a coverage of 80% or some such. They do care that you put checks in place to reduce defects and can prove it.
This is important because IT is usually a cost in most companies bottom line and not a profit center. So you need to be able to articulate your worth. This is done though verbal communication and through written emails/slack and others.
Tech Lead Questions
How do you keep your technology skills current?
So mostly by keeping an eye on what is trending. Generally though I stick with anything thats at least 10 years old. I tend to be overly critical of anything new till it has proven itself. For projects however I think you tend to have a “novelty” budget which you can spend on a new technology or tool. So for any project I tend to push for something new which will give the customer a good outcome, with the idea that if it does not work out we can back out. You want to limit this to one or two things per project though. If you jump into everything being new that usually does not work out well as its hard to go back.
What strengths do you think are most important in a developer [or another relevant IT position]?
Communication. Both verbal and written. Being able to communicate ideas is literally the only difference between you and someone sitting in india/vietnam at a cheaper rate. Its your advantage over everything else, so double down on it as best you can.
Knowing some area outside of technology is useful too. Be it in depth knowledge of finance, business, medicine, or something else. You can probably pivot this into a successful startup if you have the desire too.
Lastly listening. So many fail to really listen and understand problems. Nobody really cares if you use a No-SQL or SQL database, Java or Go, AWS or dedicated servers. They do care if you solved their problem at a reasonable price.
What are your favourite and least favourite technology products, and why?
Favorite… I really like Rust at the moment. Zig looks pretty interesting. From a technology point of view I am really digging the following, ripgrep and redis. I have a lot of respect for the people who wrote those. As for least… I really do not like BMC Remedy (time tracking sort of thing) or anything from SAP. They solve problems, and even have decent tech in them but come together to be a horrible product. Its run by marketers over product people in that respect.
Although probably the thing I am most interested in right now is the ActivityPub standard for distributed social networks. Probably a lot of opportunities in that space.
Oh I also really like the technology behind mailinator.com which is one of the more impressive over optimisation examples there are around, but in totally cool ways. Some of my favorite blog posts come from Paul who was the guy behind it.
What skills or characteristics make someone an effective remote worker?
The same ones that make them effective in an office or otherwise. Communication skills. No understating how important this is. Its also why I think that outsourcing tends to not work as well as people expect unless you have a very clear idea of what you want.
How do you handle tight deadlines?
By avoiding them. Be honest with what can be delivered in the time frame and work towards a solution where you trade scope to meet it.
Otherwise I am fortunate that I have enough pre projects I have worked on that I can snap together most things pretty quickly using existing code which helps. Especially if you combine them together.
Sometimes there is little for it, but just knuckle down and solve the problems as quickly as possible, which usually involves a little quiet time with few distractions and purpose.
