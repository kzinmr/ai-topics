---
title: "How to Talk to Your Coworkers"
url: "https://idiallo.com/blog/how-to-talk-to-your-coworkers?src=feed"
fetched_at: 2026-05-23T07:01:06.462294+00:00
source: "idiallo.com"
tags: [blog, raw]
---

# How to Talk to Your Coworkers

Source: https://idiallo.com/blog/how-to-talk-to-your-coworkers?src=feed

You know you explained the same issue before in two or three different places, yet here they are asking again. Why don't they understand you? Why do they ask the same question when you've already given them the answer right there on Jira? Are they stupid? Lazy, maybe? Do they not take the time to read?
I often hear this from developers. They write clear documentation and instructions, and people still bother them to hop on a call. This happens so frequently that I think it is worth addressing. An over-abundance of information is just as confusing as too little. But something I should add is that repetition is normal. In fact, repetition should be a tool you use frequently.
To do our jobs as developers, we read instructions. Our tasks are usually carefully written and specced out as a document we can implement and check off. There are usually bullet points, requirements, and acceptance criteria. Sometimes, you could implement a feature by following the instructions without even knowing or understanding what the feature actually does.
In other jobs, non-technical ones, people derive their work from conversation. A lossy format. For example, when a non-technical manager wants a new feature, they'll have a conversation with a software architect. A conversation that the architect then has to turn into a spec that a developer can implement.
One group talks in instructions, the other in conversations. Which is why they often talk past each other.
Whenever I hear developers complain that someone keeps pestering them with questions they've already answered, I know it's because they're speaking two different languages.
Just because you provided an answer doesn't mean everyone saw it or understood it. You might think you're giving a fine explanation of how a feature works by describing how the different APIs interact. But you fail to see that your audience has no frame of reference for understanding that APIs are supposed to work together, or what an API even is.
In that same vein, a manager who wants to have meetings and conversations about every step of development might find that people are declining their invites. For that manager, meetings and discussions are how work gets done, while others are expecting purely documented instructions.
In simple terms, the answer to this problem is:
Translate and Repeat.
By translation, I don't mean language, I mean frame of reference. There is always a temptation to provide all available information, whether it's too technical or too detailed. Again, too much information
===
no information. Instead of explaining how you are solving a problem, focus on what your solution does.
For example, I recently worked on a widget that was showing the incorrect number of sales for the month, and only a handful of customers were complaining. Long story short, it turned out that running a job at what we call nighttime is someone else's daytime. Those customers were accessing the widget before the job ran, and the data was cached for a full day. Meaning they were seeing stale data for up to 24 hours. Our fix involved revamping how we display data, we removed caching and created a normalized table that updates in real time, eliminating the need for a complex query.
Internally, we had created new APIs and restructured database tables. What looked like a handful of numbers on the UI was far more complicated under the hood. But when explaining this to a manager, they don't need to know about the cron job, the caching strategy, or how the old system compared to the new one.
All they need to know is:
"We've updated the widget to display real-time data, and we've added a smarter caching strategy for performance."
That's the whole answer. If they want the nitty-gritty details, we can have a separate conversation.
But developers often start with the technical autopsy first because that's what we would want if another developer asked us. We want the root cause, the stack trace, the PR link. The problem is, different audiences require different information.
While leading with the technical breakdown might make you sound thorough in a meeting, non-technical attendees will walk out clueless and ping you on Slack asking the same questions. The goal isn't to eliminate questions entirely. In fact, no matter how well you tailor your message to your audience, someone will still come back with the same question you already answered. That's exactly why repetition matters.
It's fascinating to watch children learn. When I'm doing first-grade math with my kids, we use the same strategy for additions and subtractions. At first, it just doesn't click. I count on my fingers, I use popsicle sticks, and to make it fun I even use my toes. My method doesn't always make sense to them. We'll complete a whole packet of homework and I can tell they're just going through the motions. But we repeat it every day, the same way, no deviation. And somehow, eventually, they just know how to do the math.
Not to compare your coworkers to children, but repetition works the same way on everyone. Every time they hear your explanation, they pick up one or two more pieces of it. When you keep saying "we upgraded the payment SDK," they don't know what that means, and stopping to explain that one concept isn't going to unlock the whole picture. But maybe they Google "SDK" on their own later. Then "payment SDK." The next time you repeat your explanation, they're better equipped to follow along. Each repetition gets them a little closer to understanding the full picture.
The same applies to managers who rely on conversation to communicate with developers. While it can be hard to extract a clear requirement from a meeting, the information is in there. It just needs to be surfaced and shaped. And honestly a conversation is often a good way to kick things off.
Imagine if the manager came in with rigid, detailed instructions while having no understanding of how the codebase actually works. Through conversation, a feature can take shape. Developers can push back, raise concerns, and adjust the scope to something realistic for the current state of the infrastructure.
That back and forth is what filters raw ideas into actionable instructions.
So when you post a Jira comment or Slack message with a detailed explanation of the authentication flow and token expiry logic and it goes ignored, it's not because your coworker is lazy. It was ignored because it was written in a language they don't speak. They asked again not to annoy you, but because they couldn't extract the answer they needed from what you gave them.
You don't need to write longer comments or bold more words. Instead, ask yourself whether what you wrote was intended for the right audience, then translate it into something digestible. And be prepared to repeat it a few more times until it lands.
