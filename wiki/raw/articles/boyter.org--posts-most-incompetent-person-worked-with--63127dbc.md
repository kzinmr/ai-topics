---
title: "The Most Incompetent Person I Ever Worked With"
url: "https://boyter.org/posts/most-incompetent-person-worked-with/"
fetched_at: 2026-05-05T07:01:56.920737+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# The Most Incompetent Person I Ever Worked With

Source: https://boyter.org/posts/most-incompetent-person-worked-with/

Previously I had covered the
worst program
I had ever worked on (although that probably needs updating now) and the
worst individual
. I thought it was time branch out into the most incompetent person I ever worked with.
So a bit of back history. This was at lendlease where we were working on a system that massaged all employee data into a single place allowing accurate counts of employees, and getting titles mapped to real ones and such. This was important because lendlease being an umbrella style company had gobbled up lots of other ones and so nobody had a clue how many people actually worked for it.
The initial build for this was done at this point and we were building further downstream systems to integrate and build off this data source, and enhance it.
I am not going to name the person in question, so lets call him John (which is nice and generic). He was assigned to build some reports in SQL Server Reporting Services (SSRS). We were informed that he was an absolute gun at this and an expert in SSRS. I forget the exact nature of what he needed to do but it was something like querying the golden records of people in order to identify people’s managers or some such.
This was where John started to go wrong. He had great difficulty joining the multiple tables together required in order to get a “golden record” which related to a single person. At the time I considered this fair enough as I had been doing the same thing. I offered to turn my SQL into a view which he could then query. With this done he thanked me and we moved on.
Several days later during standup John mentioned that the view was a bit slow and making it hard to do his job. Considering under the hood it was doing multiple left joins I agreed, and modified how it worked. I ran the query again at the end of the existing ETL process and dumped the results into a table with multiple indexes on it optimized for the queries I would be running and the ones John would be.
The resulting view ran in a under a millisecond for most of the queries I tried. I showed it to John, and he was happy and we continued on. The next day he mentioned at standup that the view was still slow. I was starting to hear from other people on the team that John appeared to be useless at this point so I went with John to see what he was doing.
He showed me the queries he was running, and which he had left running overnight. A quick check using the SQL Server estimates showed that it estimating that it would return billions of rows. Considering that the view itself should only return 50,000 rows or so I was fairly suspicious. I checked the query itself and John was doing a cross join on the view itself multiple times for some reason.
I asked what he was trying to achieve, and then wrote a simple query that returned almost instantly for him solving his issues.
At this point I was in agreement with my workmates, and suggested John be removed from the project, and as a contractor sent back. This was not done sadly. As a result we were moved John to be responsible for releases. This we figured was fairly safe, all he would need to is update code and scripts from source control and deploy it to UAT. This was before devop’s and automated deployments had really become best practice.
This worked for a short period of time. However developers tended to deploy to UAT themselves when needed as the UAT environment had close to production levels of data, and was looked at by business users. John’s main job was to roll out everyone’s changes so that the environment was in sync and ready for a full deployment to production.
However we noticed over time that it seemed like a lot of things were bring reverted. This resulted in lots of questions to John of “Did you deploy it?” which he always responded that he had. This continued for a while, before we asked to see how he was doing it. It was then that the penny dropped. While he was deploying the code and generally competently, he was never updating it from source control, freezing our deployments to several weeks ago. This lead to us explaining how source control works to John.
I don’t think we ever found a job for John after that. He ended up sitting out the rest of his contract doing nothing from memory. I do know that after he left most of what he wrote was redone, in order to improve performance and resolve several bugs.
What was funny was that someone I did respect at lendlease mentioned that he had worked with John many years before, and that he was extremely competent. From memory that was dealing with C code. I had no way to validate those claims, and I have no idea how he fell so far from grace.
Many years later I bumped into John on the train while heading home. No words were exchanged, but he eyed me and I eyed him. I don’t know if he knew who I was, and I never got to find out seeing as the next station was my stop.
I won’t wish John any harm. I don’t know if he has remained as useless as he was then, but I hope not. If he has however, I dearly hope he has moved into some other role, or ideally out of the IT industry in general.
