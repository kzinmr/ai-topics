---
title: "ActivityBot is the recipient of an NLnet grant!"
url: "https://shkspr.mobi/blog/2026/08/activitybot-is-the-recipient-of-an-nlnet-grant/"
fetched_at: 2026-08-31T10:07:33.942119+00:00
source: "shkspr.mobi"
tags: [blog, raw]
---

# ActivityBot is the recipient of an NLnet grant!

Source: https://shkspr.mobi/blog/2026/08/activitybot-is-the-recipient-of-an-nlnet-grant/

Back in February, I applied for
NLnet's Next Generation Zero grant
. They were looking for Fediverse projects to help rewild the social media landscape. Or, as they describe it:
Reclaim the public nature of the internet
Small and medium-sized R&D grants between 5.000 and 50.000 euro, with the possibility to scale up.
I run
ActivityBot
- it is a single-file ActivityPub server suitable for launching automated accounts and designed as a learning tool for those who want to understand how the protocol works. Several people have told me how useful it is, but I haven't had the time to make it better. So I decided to stick in a last-minute application to the fund.
I really didn't know how much to apply for - or even if my project would be suitable for funding - so I cheekily asked for €10,000. After a few months of back-and-forth, I'm delighted to announce that I was successful!
In the spirit of openness, this blog post details how the NLnet grant process worked for me and what I'll be using the money for.
The application was delightfully simple. Here's what it asked for, along with my answers. If you apply, please don't copy these verbatim; use your own words.
Abstract    : A single file server for ActivityPub. Designed for write-only bots. Allows any project to quickly and easily start publishing automated content to the Fediverse. Uses PHP, no other dependencies.
Experience  : I am the sole developer of Single File ActivityPub - https://gitlab.com/edent/activitypub-single-php-file
I was formerly the UK Government's representative to the W3C and have contributed to various ActivityPub projects and specifications.
Amount      : € 10000
Use         : The fund will be used for development, testing, promotional activity (including conference travel).
I anticipate this will fund 6 months of development. I have funded all previous development.
Comparison  : Most ActivityPub services are complex. They implement a full specification and are designed for multi-user environments. Other projects allow reading and writing. ActivityBot is deliberately designed to be as simple as possible. A single file to upload, one user, publish only.
This will enable more projects to be able to instantly start publishing with low development cost and close to zero hosting cost.
Challenges  : Formal spec verification and a security audit will be the main technical challenges. The ActivityBot software has been running well for over a year. The funding will allow for better compatibility and security.
Ecosystem   : The project has mostly targeted individuals who want to run small bots. After further development, the project will engage with IoT providers, smaller publishers, open source projects who wish to publish updates, and other relevant parties.
I was told there was intense competition. After a couple of months, I received word that I'd made it to the 2nd round.
What then followed was a
very
polite interrogation about my ideas, how I would develop the project, what I would use the money for, and what my AI usage policy was.  They also wanted a breakdown of the main tasks - with the understanding that this would be a provisional document subject to change.
I was on
a train through Europe
when I wrote this. I don't claim it to be a brilliant document - but it got the job done!
1. User Research
Recruit 2 - 5 potential users. Offer an incentive (approx £20ea) to participate in a user research session. Study design will take 1 - 2 days. Each interview and write up to take 1 day. Consolidation and report 2 days.
Total effort 3 - 4 weeks.
2. Standards Research
Participate in ActivityPub user communities and standardisation groups. Attend virtual conferences (or any local to the UK). Approx 1 day per week for 6 months.
3. Test Driven Development
Create modern test harness, write test suite, iterate design based on tests. Anticipated effort 2 days per week for approx 3 months.
4. Security Testing
Work with the community and security professionals to test the resultant code. This will use human testers and normal fuzzers - this will not use AI tools. Anticipated effort 2 days per week for approx 2 months.
5. User Acceptance Testing
Recruit 2 - 5 potential users (ideally different to the research participants). Offer an incentive (approx £20ea) to participate in a user acceptance session. Study design will take 1 - 2 days. Each interview and write up to take 1 day. Consolidation and report 2 days.
Total effort 3 - 4 weeks.
6. Updates Based on Research, Testing, and Security
While it would be lovely to anticipate getting everything right first time, the reality is that changes will need to be made based on the findings of the above. This will take up the remainder of the allocated time.
Again, there was a little more back and forth. But a few weeks later I was informed that I was at the final stage, pending review. And, a few weeks after that, I was told my project had been given the green light.
I was invited to a group call where the very friendly team discussed the practicalities of the grant, what it could and couldn't fund. I also met a bunch of other people who'd also won.
The final stage was writing a proper Memorandum of Understanding. With the help of one of the team (thanks Victoria!) I was able to turn my scrappy plan into something a bit more formal. The project tool NLnet uses made it easy to build up a plan and put € amounts by each task.
The idea is that I will invoice against the grant whenever I have completed a task or sub-task. Obviously I don't want to leave invoicing until the end of the project, but I also need to be mindful of the foreign exchange fees charged by my bank for receiving Euro payments.
This is the plan I submitted. It represents what I hope to accomplish and how I'll draw down on the grant. I suspect this will change as the months go on.
ActivityBot is an Open Source project which aims to develop, maintain, and improve a minimum viable ActivityPub server in a single PHP file.
The project is run by Terence Eden (trading as @edent); a developer residing in England.
This project is expected to run for approximately 6 months. All of the deliverables will be openly licenced using either an OSI approved software licence or a Creative Commons licence.
The high-level aims of the project are for ActivityBot to be:
A fully compliant ActivityPub server, running in a single PHP file.
A teaching tool to help developers understand the practical aspects of creating an ActivityPub server.
A practical method of publishing automated messages to the Fediverse.
A promotional tool to show how simple and easy ActivityPub development can be.
A secure and usable tool written in modern PHP.
Written by humans, with no AI/LLM generated code.
In light of NLnet's non-profit status, costs assume a discounted rate of €330 per day (£280). Incidentals such as hardware, software, travel, or sundries will be charged at cost with receipts provided.
Ensure that the project is in a suitable state for initial release and future development.
Deliverable: Updates published to GitLab.
€495 Prepare initial release. Clarify licencing, solicit community engagement, include example usage.
€495 Standards Research. Collation of standards websites. Ensure code comments refer to specific standards. Publish blog post(s) about findings for others to reference.
Recruit up to 10 participants for a user-research study. Participants should represent the diversity of the Fediverse.
Investigate what participants want from a tool like ActivityPub. The project plan may be adapted following the results of this study.
Deliverable: Study plan and results will be published and given a Creative Commons licence. Changes based on the results will be pushed to GitLab.
€660 Study Design and recruitment of participants (blog post published as deliverable).
€990 Two days of user interviews, write up and publish results as blog post.
Create a modern test harness, write test suite, iterate design based on tests.
Deliverable: Tests published to GitLab. Blog posts published about the process and results.
Working with NLnet's security offering, ensure that the project meets modern security requirements.
€720 Work with security team to assess security risks and possible mitigations. Fixes based on security team feedback
Deliverable: Updates published to GitLab. Blogs published about the process and results.
Recruit up to 10 participants for a user-acceptance study. Participants should represent the diversity of the Fediverse.
Investigate whether participants are able to use ActivityBot. See which aspects need improvement. The project plan may be adapted following the results of this study.
Deliverable: Study plan and results will be published and given a Creative Commons licence. Changes based on feedback will be published to GitLab.
€660 Study Design and recruitment of participants (blog post published as deliverable).
€990 Two days of user interviews, write up and publish results as blog post.
Open Source participation often depends on attending conferences, either in person or virtually. Getting involved in the standardisation process ensures that future versions of ActivityPub and associated standards will be suitable for the community.
Deliverables: Presentations material (slideware), speaking at conferences (may be published as video), conference outputs. Where possible, these will be available under a suitable Creative Commons licence.
€700 Travel and accommodation to one EU conference
€330 Publishing blog posts about ActivityPub standards work.
€330 Publishing blog posts about ActivityPub standards work.
Creating a final release for this phase of the ActivityBot project. This will involve incorporating all feedback received so far, improving documentation, and publishing code.
Deliverable: Updates published to GitLab. Blog post written. Release announcements.
€330 Phase 1: Process and implement feedback from users
€330 Phase 2: Bug fixes
€330 Phase 3: Features
€330 Phase 4: Bug fixes
€330 Phase 5: Features
€330 Phase 6: Remedial work
€330 Process and implement feedback from accessibility scan
€330 Final release
I've already begun work on updating the code. If you'd like to get involved, or have suggestions or bug reports - please
take a look at ActivityBot on GitLab
.
I'll be putting out a call for user-research participants once I've had a chance to catch my breath 😆
