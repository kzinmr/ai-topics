---
title: "Getting the right scale"
url: "https://tomrenner.com/posts/getting-the-right-scale/"
fetched_at: 2026-04-25T12:09:25.699214+00:00
source: "tomrenner.com"
tags: [blog, raw]
---

# Getting the right scale

Source: https://tomrenner.com/posts/getting-the-right-scale/

Agile tells us that the most critical thing for getting software right is not up front design, but getting something out there and used, and then incorporating feedback. By getting feedback early, you are able to respond faster, changing your (initially incorrect) design in small steps towards a better solution. This works better in practice than designing everything at the start very carefully, which feels rigid and inflexible in the face of new information over the course of a project.
This is good. Everyone hates waterfalls.
However, iterative development processes also come with their own problems. Scope creep can become a much larger risk when there is the opportunity for specification change and revision at later stages, which is especially apparent on large projects.
My company works in the higher education sector, where development projects often last 6-12 months. Iterative change and feedback in this environment needs careful management to avoid the project scope increasing over time. This often feel like a failure in system design and specification, bringing us back to the need for better up front design! This can leave you feeling you’re between a rock and a hard place with too much upfront design vs. ever getting the damn thing live.
So we are looking for the sweet spot between too much up-front design and enough to mitigate scope creep and major structural changes late on on projects.
I have suspicions that sweet spot is very small, and that’s a major reason why this job is hard. It’s also why every codebase is littered with
//TODO
s, and why most of us find it much easier to start than finish a side-project. The real world gets involved and messes up your Grand Vision for The Perfect System (which, realistically, is probably why you started the project in the first place), and all of a sudden a “Grandish Idea for Another Probably Ok Webapp” hasn’t had a commit in 3 months.
All developer know that some problems require quick fixes, some fundamental re-writes of the system. Correctly resolving a problem and it not then causing you a major ballache later depends on picking the right scope of solution, and being able to identify that scope is a seriously valuable skill to have.
Scope: Are you looking for the One True Solution to all issues that look anything like the current one?
Are you trying to make something that is generalisable to other parts of the system?
So here are three things I try to keep in mind when starting out on a problem, to try to find that sweet spot of design:
We want to only write this bit of code once
We want to spend the minimum time possible writing this code
If possible we want to reuse this code in as many places as possible in future
The aim of this is to try to get as close to the optimum scope of solution that takes the minimum time while not having been revisited. Getting this step right for each small task minimises negative effects of project changes later on, by keeping your codebase flexible to react to future discoveries.
