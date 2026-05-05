---
title: "What is Chaos Testing / Engineering"
url: "https://boyter.org/2016/07/chaos-testing-engineering/"
fetched_at: 2026-05-05T07:02:01.171820+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# What is Chaos Testing / Engineering

Source: https://boyter.org/2016/07/chaos-testing-engineering/

A blog post by the excellent technical people at Netflix about
Chaos Engineering
and further posts about the subject by
Microsoft in Azure Search
prompted me to ask the question, What is chaos engineering and how can chaos testing be applied to help me?
What is Chaos Testing?
First coined by the afore-mentioned Netflix blog post, chaos engineering takes the approach that regardless how encompassing your test suite is, once your code is running on enough machines and reaches enough complexity errors are going to happen. Since failure is unavoidable, why not deliberately introduce it to ensure your systems and processes can deal with the failure?
To accomplish this, Netflix created the Netflix Simian Army, which consists of a series of tools known as “monkeys” (AKA Chaos Monkey’s) that deliberately inject failure into their services and systems. Microsoft adopted a similar approach by creating their own monkey’s which were able to inject faults into their test environments.
What are the advantages of Chaos Testing?
The advantage of chaos engineering is that you can quickly smoke out issues that other testing layers cannot easily capture. This can save you a lot of downtime in the future and help design and build fault tolerant systems. For example, Netflix runs in AWS and as a response to a regional failure changed their systems to become region agnostic. The easiest way to confirm this works is to regularly take down important services in separate regions, which is all done through a chaos monkey designed to replicate this failure.
While it is possible to sit down and anticipate some of the issues you can expect when a system fails it knowing what actually happens is another thing.
The result of this is you are forced to design and build highly fault tolerant systems and to withstand massive outages with minimal downtime. Expecting your systems to not have 100% uptime and planning accordingly to avoid this can be a tremendous competitive advantage.
One thing commonly overlooked with chaos engineering is its ability to find issues caused by cascading failure. You may be confident that your application still works when the database goes down, but would you be so sure if it when down along with your caching layer?
Should I be Chaos Testing?
This really depends on what your tolerances for failure are and based on the likelihood of them happening. If you are writing desktop software chaos testing is unlikely to yield any value. Much the same applies if you are running a financial system where failures are acceptable so long as everything reconciles at the end of the day.
If however you are running large distributed systems using cloud computing (think 50 or more instances) with a variety of services and process’s designed to scale up and out injecting some chaos will potentially be very valuable.
How to start Chaos Testing?
Thankfully with cloud computing and the API’s provided it can be relatively easy to begin chaos testing. These tools by allowing you to control the infrastructure through code allow the replication of many errors not easily reproducible when running bare hardware. This does not mean that bare hardware systems cannot perform chaos testing, just that some classes of errors will be harder to reproduce.
Lets start by looking at the way Microsoft and Netflix classify their “monkey’s”.
Low chaos
This refers to failures that our system can recover from gracefully with minimal or no interruption to service availability.
Medium chaos
Are failures that can also be recovered from gracefully, but may result in degraded service performance or availability.
High chaos
Are failures that are more catastrophic and will interrupt service availability.
Extreme chaos
Are operations that are failures which cause ungraceful degradation of the service, result in data loss, or that simply fail silently without raising alerts.
Microsoft found that by setting up a testing environment and letting the monkey’s loose that they were able to identify a variety of issues with provisioning instances and services as well as scaling them to suit. They also split the environments into periods of chaos where the monkey’s ran and dormant periods where they did not. Errors found in dormant periods were considered bugs, and flagged to be investigated and fixed. During chaos periods any low issues were also considered bugs and scheduled to be investigated and fixed. Medium issues raised low priority issues to on call staff to investigate along with high level issues. Extreme operations once identified were not run again until a fix had been introduced.
The process for fixing issues identified through this process was the following,
Discover the issue, identify the impacts if any and determine the root cause.
Mitigate the issue to prevent data loss or service impact in any customer facing environments
Reproduce the error through automation
Fix the error and verify through the previous step it will not reoccur
Once done the monkey created through the automation step could be added the the regular suite of tests ensuring that whatever issue was identified would not occur again.
Netflix uses a similar method for fixing issues, but by contrast runs their monkey’s in their live environments rather then in a pure testing environment. They also released some information on some of the monkey’s they used to introduce failures.
Latency Monkey
Induces artificial delays into the client-server communication layer to simulate service degradation and determine how consumers respond in this situation. By making very large delays they are able to simulate a node or even an entire service downtime. This can be useful as bringing an entire instance down can be problematic when an instance hosts multiple services and when it is not possible to do so through API’s.
Conformity Monkey / Security Monkey
Finds instances that don’t adhere to best-practices and shuts them down. Examples for this would be checking that instances in AWS are launched into permission limited roles and if they are not shutting them down. This forces the owner of the instance to investigate and fix issues. Security monkey as an extension that performs SSL certificate validation / expiry and other security best practice checks.
Doctor Monkey
Checks existing health checks that run on each instances to detect unhealthy instances. Unhealthy instances are removed from service.
Janitor Monkey
Checks for unused resources and deletes or removes them.
10-18 Monkey (Localisation monkey)
Ensures that services continue to work in different international environments by checking that languages other then the base system consisting to work
Chaos Gorilla
Similar to Chaos Monkey, but simulates an outage of an entire Amazon availability zone.
Well hopefully that explains what Chaos Testing / Engineering is for those who were previously unsure. Feel free to contact me over twitter or via the comments for further queries or information!
