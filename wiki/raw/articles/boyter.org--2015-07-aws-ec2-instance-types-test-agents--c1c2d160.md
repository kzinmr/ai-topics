---
title: "AWS EC2 Instance Types to Use as Test Agents"
url: "https://boyter.org/2015/07/aws-ec2-instance-types-test-agents/"
fetched_at: 2026-05-05T07:02:02.117406+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# AWS EC2 Instance Types to Use as Test Agents

Source: https://boyter.org/2015/07/aws-ec2-instance-types-test-agents/

When you are running test agents on AWS knowing what instance type to run as test agents (for TeamCity or otherwise) can involve a lot of trial and error. Not only can there be great savings to be made by picking the correct instance type you can speed up your builds and get test feedback back faster which can be far more valuable the cost of a few additional cents an hour.
The following are some results that I have found when playing with different instance types. Before Amazon released the burstable t2 instance types one of the most common instances I had seen used was general purpose instances such as the m3.medium. This always seemed like a good choice as most tests tend to use a mixture of CPU/Disk/Network and thats what the agents are supposed to be good at.
The moment that the bustable instances were released several agents were relaunched as t2.mediums and left in the cluster for a week.
The outcome was that no only were they saving money since they cost lest per month, they were able to run tests and build faster then the previous agents. This was a surprise at first until we observed that with very few exceptions every test was CPU bound. This included browser tests which we had expected to be more network bound. The performance increase as such was mostly down to them accumulating credits over time faster then they could be spent. See the below image which was taken from a live instance where you can clearly see how this works.
For the record this agent runs 24/7 running builds and tests over dozens of different projects including a lot of selenium tests for multiple browsers.
There were however a few tests which consumed considerably more CPU then expected. These tests comprised of a collection of very heavy math operations and integrations all running on the same machine. A single agent was boosted to a c4.medium to take care of these tests and everything has been working fine since. Build times were down and the developers had feedback sooner.
We also tried relaunching the instances with a higher number, such as a m3.large into a m4.large and the result was far faster builds. This is probably due to the underlying hardware AWS is using being faster. It was however still worth using t2 agents due to the cost saving and roughly equivalent performance.
Conclusions
It really depends on your environment and how much you are using the agents. I think the following guidelines apply fairly well though.
For any test agents running Windows you want the minimum of a t2.medium on AWS or the equivalent with 2 CPU’s and 4 gig of RAM.
Test agents running Linux want to be the minimum of a t2.small on AWS or the equivalent with a single CPU and 2 gig of RAM.
For agents that run tests infrequently as in less then 6 times an hour stick with the lower end t2 instances.
For agents that run heavy loads consider using a c4.large as the increased CPU will really cut down on the test time.
Always go for the latest type in AWS, IE use a c4.large over a c3.large for increased performance
The main takeaway however is ensure you can relaunch your instances as different types easily. Try out different types and see what happens. The winning strategy I found was to launch as a t2.medium at first and then dial it down to a t2.small if it was overpowered (which was never the case for Windows) and relaunch as a c4.medium if it was underpowered.
The result was much faster builds saving developer time and frustration.
