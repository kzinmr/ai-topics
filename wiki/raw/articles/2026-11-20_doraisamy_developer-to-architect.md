---
title: "We promoted developers into architects without informing them (Mani Doraisamy)"
source: https://manidoraisamy.com/developer-to-architect.html
date: 2026-11-21
type: article
sha256: b6682c0fbb0c9c1489a29f627a035fd194b02976fe484ba93495ec138dba589b
---

> HN discussion: https://news.ycombinator.com/item?id=50579331 (461 pts)

We promoted developers into architects without informing them 

 Developer forever

 Read my posts

 All posts

 We promoted developers into architects without informing them

 Mani Doraisamy

 18 hours ago

 5

 3

 Yesterday, I was debugging a performance problem with our Google Forms addon. It turned out my colleague had vibe coded the logging part, so that he could monitor the new installs every week. Monitoring new customers is the most important part of running a business, so he is absolutely right in doing that. Except, he was logging the user’s email and Google has severely restricted how much detail you can get about the user since last December. So, AI had written a series of try/catch statements:
 First, try to get the email if the user gave consent to share it during installation.
 If it fails, it would try to fetch his user ID.
 If that fails, it would log an error saying the user has installed, but we don’t know his email or user ID.
 
 All of these are one line of code, but internally each of these makes multiple API calls to Google servers. Since logging was the first line to execute after installation, the welcome screen took 15 seconds to load.
 What is the right code for this?
 If you are a senior developer or architect who understands the number of API calls behind each method, you would have:
 Logged just the timestamp of the install instead of trying to fetch the email or user ID, and told the marketing team they won’t be able to send the follow-up email based on installation alone.
 Or, if marketing wants the user’s email on install, you would have shown the welcome screen first and logged the email or user ID asynchronously from the browser, while the user is looking at the welcome screen. But calling your server from the addon’s welcome screen might require your server to bypass security and log an unauthenticated payload.
 
 In other words, your job as an architect is to push back on requirements that can slow down the app. Or, find a way to work around the performance and security issues by making it async or accepting a reasonable hack.

 Why AI won’t push back
 AI is great at writing code. But it doesn’t know if you are launching the app or have millions of users, which it needs to make the right architecture call to log a timestamp vs email. It is also sycophantic and tries to execute your requirements exactly without pushing back, which means you end up with a slow app that takes 15 seconds to load a static welcome screen.
 Essentially, if you generate code by specifying your requirements instead of specifying your architecture, AI will decide the architecture on your behalf. It is so paranoid about security that it will never write code to accept an unauthenticated payload. Even if you write it yourself, it will rewrite it into an authenticated payload and screw up performance or force users to sign in again on your app.

 Your new job is to architect
 AI coding tools are tuned to implement your functional requirements and two non-functional requirements, i.e. security and backward compatibility to avoid breaking your app. This invariably leads to:
 Architecture that trades off performance for security and slows down the app.
 Multiple versions of datamodel design with redundant tables, columns and code.
 
 That means you define the architecture, design the datamodel first and ask AI to code within that constraint. Every time you give a requirement that changes your architecture or design, coding tools have to ask you before changing it, instead of changing it on their own. You have to tell it when it needs to be backward compatible, so it’s ok to keep multiple versions of logic or database tables, and when to delete the old logic and tables and keep a single version for maintainability.
 If you are an architect who is used to designing the datamodel, delegating the implementation to developers and then reviewing their code to see if they have implemented it correctly, this should be natural to you. But the problem is that today we have taken developers who were great at coding and moved them into an architect’s job. They see that the job they love, i.e. coding, is now completely done by AI. But nobody has told them about the new job of pushing back on requirements, designing the datamodel, constraining AI to their architecture and reviewing that it falls in line. This is the reason for all the confusion and hate among developers about vibe coding.

 Your future as developer
 In our case, the right fix is simple. Log the timestamp, show the welcome screen first and tell marketing what they can’t get on install. But AI will never make that call for you, because it doesn’t know your users and it won’t push back on your requirements. That is the architect’s job. If you are a developer, the coding job is going away. But it doesn’t mean your job is going away. Non-developers who don’t understand architecture and design will end up with bad performance and unmaintainable database tables. So, stop missing the coding and become an architect. Learn to push back on requirements, design the datamodel, constrain AI to it and review the code the way an architect reviews a developer’s code. You got promoted. Nobody told you, so I am telling you. 

 5 
 
 Like

 forum
 
 3 

 share
 
 Share

 Comments · 3 

 Srinivasa Prasanna

 14 hours ago

 Mani - could adopting a method like spec-driven development have helped here ?

 Reply 

 Anh Le

 8 hours ago

 @斯里尼瓦萨·普拉萨纳 在这个案例中，如果你的规格不是从架构层面，而是从需求层面出发的就没有

 Reply 

 Halberdus Ravenheim

 2 minutes ago

 "stop missing the coding"

The coding was the fun part and I never wanted this promotion.

 Reply 

 Add your comment

 Compose 🪄 

 Comment
