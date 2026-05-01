---
title: "Underused Techniques for Effective Emails"
url: "https://refactoringenglish.com/chapters/techniques-for-writing-emails/"
fetched_at: 2026-05-01T07:01:24.955542+00:00
source: "refactoringenglish.com"
tags: [blog, raw]
---

# Underused Techniques for Effective Emails

Source: https://refactoringenglish.com/chapters/techniques-for-writing-emails/

For software developers, there’s tremendous value in writing effective emails. Good emails save time, reduce misunderstandings, and earn you recognition within your company.
You can drastically improve your emails with a few simple techniques, but too few developers know about them.
What’s an effective email?
🔗
An effective email has four key qualities:
Clear
: Recipients understand what you’re telling them without additional clarification.
Relevant
: Recipients quickly recognize why the information is relevant to them.
Efficient
: You and your recipients achieve your goals while minimizing everyone’s time reading and responding to the email thread.
Succinct
: The email maintains a high signal-to-noise ratio.
Deliver the most important information first
🔗
When you see a co-worker in person, you typically don’t blurt out the most important thing on your mind before even saying hello, but that’s the right thing to do in email.
Your co-workers receive hundreds of emails per day. They don’t have time to read every email in full, so they skim their inbox to find what’s relevant to them.
To ensure that your recipients see the information they need, present the most important information in your email first.
As an exercise, here’s an intentionally boring and long-winded email. Give it a quick skim to spot anything worth reading:
Subject: A surprise discovery
To: hamsterchat-team@​example.com, devops@​example.com
Hi All,
I was playing checkers with my dog, Sgt. Francisco, when I noticed that his ID tag had fallen off his collar. It may have been gone for months.
It made me wonder about other safety measures that I might be taking for granted. So, I started thinking about HamsterChat’s data backups.
On a hunch, I went to our data center last night at around 8 PM to test my theory. I talked to Tony, the admin there, and he set me up with a crash cart at our server. Sure enough, every backup snapshot I tested was corrupt and unrecoverable. I was able to isolate the problem to a faulty RAM stick. Boy, was that a surprise! Tony had never seen anything like it.
Goes to show that thinking about adjacent problems is worthwhile!
Sincerely,
William Hamsterton-Chatsworth
Unless you read the above email in full, you probably missed the most important detail:
all the backups are gone
.
For important emails, start with a one-line summary or a short list of bullet points before you even get to “Hello.” After the summary, present the supporting details in descending order of importance.
Here’s the previous email, rewritten to present the most important information first:
Subject: Failure in HamsterChat backups - all backups lost
To: hamsterchat-team@​example.com, devops@​example.com
tl;dr: All historical HamsterChat backups are corrupt and unusable. Backups are healthy again starting today.
Hi All,
Due to a hardware failure in our storage server, all of our HamsterChat backups are corrupt. I’ve replaced the faulty hardware and verified that backup and restore functionality is healthy.
I’m working with our DevOps team to automate a weekly backup and restore test. If anything corrupts our backups in the future, we’ll catch it within a week rather than stumbling across the issue months later by chance.
From digging into the logs and running diagnostics, I isolated the cause to a faulty RAM stick in our storage server. It appears that it was silently flipping bits on disk writes, so the filesystem thought the write succeeded, but the data that landed on the disk was corrupt.
After replacing the RAM stick, I took a backup and successfully restored it to a fresh disk. This strongly supports my hypothesis that the faulty RAM stick was to blame.
Sincerely,
William Hamsterton-Chatsworth
Some organizations call this style of writing
bottom-line, up front (BLUF)
. Journalists call this
“the inverted pyramid”
because the information becomes relevant to a smaller and smaller audience as you get deeper into the text.
Journalists structure news reports in an inverted pyramid, where the information relevant to the most people is at the top.
Note how the information in the email above matches the inverted pyramid style:
Details from the original email about the dog and the data center admin no longer appear in the revised email. Those details were irrelevant, so cutting them maintains a high signal-to-noise ratio, making it easier for recipients to capture important details.
Markdown Here is
a free, open-source browser extension
that lets you write emails in Markdown.
As a software developer, my emails frequently contain code snippets and inline code. Markdown Here makes it easy to format code clearly and add simple formatting right from the keyboard.
I compose emails in Markdown like this:
Then, I hit
Ctrl+Alt+M
, and Markdown Here turns my email into this:
I’m baffled that Markdown Here isn’t a thousand times more popular. I’ve been recommending it for a decade, and whenever I tell people about it, I feel like I’m in
that movie
where the guy wakes up one day, and nobody else knows who The Beatles are.
Write complete replies rather than quick ones
🔗
When an email is sitting in your inbox, a part of you just wants it to go away. The email represents work on your plate, and the sooner you reply, the sooner you can stop thinking about that work.
Sending a quick reply feels like completing a work task, but you’re actually creating more work for yourself and your teammates.
To show what I mean, here’s an email thread where everyone responds quickly:
Subject: Custom build for Optimoji
To: pm-team@​example.com; dev-team@​example.com
Optimoji agreed to participate in our HamsterChat beta, but they only have ARM servers.
Can you compile an out-of-band ARM build for them?
Subject: Custom build for Optimoji
To: pm-team@​example.com; dev-team@​example.com
Which version of ARM?
Subject: Custom build for Optimoji
To: pm-team@​example.com; dev-team@​example.com
I’m not sure. They’re running Ampere Altra Max machines.
Subject: Custom build for Optimoji
To: pm-team@​example.com; dev-team@​example.com
Okay, Ampere Altra Max is ARM v8.2a.
Do you want the Pro or Enterprise version for them?
Subject: Custom build for Optimoji
To: pm-team@​example.com; dev-team@​example.com
Enterprise.
Subject: Custom build for Optimoji
To: pm-team@​example.com; dev-team@​example.com
Do they need the multi-language extension, or is it just
en-US
?
Subject: Custom build for Optimoji
To: pm-team@​example.com; dev-team@​example.com
English only.
Subject: Custom build for Optimoji
To: pm-team@​example.com; dev-team@​example.com
Okay, here you go.
Had either participant in the thread put more care into their emails, they would have recognized that they were omitting critical details or failing to solicit them.
The thread above is eight emails, but let’s assume that there were 10 people on the thread. That’s now 80 emails, meaning this trivial thread caused 80 collective context switches for employees across this company.
Had the participants instead optimized for complete replies, they could have resolved this thread in two emails:
Subject: Custom build for Optimoji
To: pm-team@​example.com; dev-team@​example.com
Optimoji agreed to participate in our HamsterChat beta, but they only have ARM servers (Ampere Altra Max).
Can you do a custom build for them with these properties?
Architecture: ARM
Tier: Enterprise
Language: en-US only
Subject: Custom build for Optimoji
To: pm-team@​example.com; dev-team@​example.com
Sure, see attached.
Ampere Altra Max is ARMv8, so I added that to our build matrix for the next release.
If they need updates in the future, they can download our standard release builds as long as they choose ARMv8 flavor.
Cal Newport describes this style of managing email as
process-centric email
. Newport recommends treating every email thread as a problem the recipients must solve. The goal is to create a process for solving that problem in as few emails as possible.
Split threads and curate recipients
🔗
Sometimes an email thread drifts beyond its original scope. The subject line no longer matches the discussion, and the recipients are no longer the right audience.
When an email’s scope changes, actively split the thread to eliminate noise by doing the following:
Update the subject line to match the new scope of the discussion.
Move any recipients to bcc if the thread is no longer relevant to them.
Add any new recipients for whom the thread is relevant.
Briefly explain the context of the thread for the people you added.
As a concrete example, imagine that you start an email thread to review a design document:
Subject: HamsterChat v2 design review
To: architecture-astronauts@​example.com; hamsterchat-dev@​example.com
Hi All,
The HamsterChat v2 design document is now ready for review:
https://​example.com/docs/hamsterchat-v2-spec/edit
-William
Everyone signs off on the design, but someone suggests looping in the infrastructure team to coordinate hardware resources.
The anti-pattern at this stage would be to add the infrastructure team to the thread and ask them a vague question:
Subject: HamsterChat v2 design review
To:
infrastructure@​example.com
Cc: hamsterchat-dev@​example.com; architecture-astronauts@​example.com
Infrastructure folks - can you weigh in here?
What’s wrong with that email?
A lot, actually:
You’re forcing the infrastructure team to dig through the thread to understand what you’re asking them.
The subject line is still “HamsterChat design review,” even though it’s no longer a design review.
You’re dragging along a bunch of people from the design review who don’t care about coordinating hardware resources, so the email is now pure distraction for them.
You can solve all of those problems by splitting the thread:
Subject: HamsterChat Q3 infra resources WAS: HamsterChat v2 design review
To: infrastructure@​example.com
Cc: hamsterchat-dev@​example.com
Bcc: architecture-astronauts@​example.com
[adding infrastructure@, moving architecture-astronauts@ to bcc]
Hi Infrastructure Folks,
We’re planning to introduce a new version of HamsterChat in Q3 (see thread below).
The new service will require at least two 4-vCPU application servers and one 2-vCPU database server for testing. Will the infrastructure team be able to provide that by Q3?
-William
Create structure with headings and paragraph breaks
🔗
When talented speakers give presentations, they write every slide with care. They break up their talking points into small, digestible chunks, and they choose descriptive yet succinct headings.
When you’re writing a long email, think about how you’d present it as a slide deck. Focus each paragraph around a single idea. When in doubt, err on the side of shorter sentences and paragraphs. If your emails begin to look like LinkedIn clickbait, that’s too short.
Subject: Severe HamsterChat outage - all regions affected
To: all-staff@​example.com
Have you ever noticed that our website is unreachable?
I noticed.
And once I saw it, I couldn’t unsee it.
The cause? A stray curly brace in our nginx config.
Click below👇 for five unbeatable strategies to prevent outages.
For emails longer than about five paragraphs, use headings to help your readers recognize the structure of your email.
Subject: HamsterChat rollout plan
To: all-staff@​example.com
We are still on track for
the HamsterChat global release on Wednesday, July 16
.
There are many delicate pieces to this launch, so I’ve summarized them below to ensure that we’re all on the same page.
Release announcement
🔗
We’ll publish the release announcement to our blog on Wednesday at 12:01am ET.
We got a lot of great tips from
the release announcements chapter in
Refactoring English
, so we anticipate 10+ million visitors within the first few minutes.
Product Hunt launch
🔗
HamsterChat will launch on Product Hunt on Wednesday at 3:01am ET.
We purchased Product Hunt’s Authentic Indie Platinum package, which guarantees that HamsterChat finishes the day in the #1 spot from organic votes.
We anticipate the visibility on PH to bring in as many as four (4) unique visitors.
TechCrunch interview
🔗
…
Section headings are also helpful when your email has multiple audiences who care about different subsets of your email. When you’re emailing multiple teams, headings allow readers to zero in on the parts of your email that matter to them.
Summary
🔗
Effective emails are clear, relevant, efficient, and succinct.
Structure emails to deliver the most important information first, potentially with one-line summaries or bullet points.
Use the Markdown Here browser extension to format your emails beautifully.
Replying quickly is less important than minimizing the number of emails in a thread.
Update the subject line and recipients when a thread’s scope drifts from its original purpose.
Use headings and paragraph breaks to help recipients understand the structure of your emails.
